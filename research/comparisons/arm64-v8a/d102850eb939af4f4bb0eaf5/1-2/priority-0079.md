# v16.0.2 → v16.0.3 · 最優先の変更候補 (79)

[一覧の目次](README.md)

<a id="compare-7f31c73cdcc3242627aeb81c6ce46678"></a>

### [`00ba9dd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba9/00ba9dd8.md) → [`00baadcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baa/00baadcc.md) FUN_00baadcc

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b78ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b78/00b78ea0.md) · 呼出先 23件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00b79e94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b79/00b79e94.md) · 呼出先 23件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.55% / 新版 98.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00baaf40",
      "incomplete_value": false,
      "site": "00baaf4c",
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
            "const:d11:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba9f4c",
      "incomplete_value": false,
      "site": "00ba9f58",
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
            "const:cc7:8"
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
      "definition_site": "00bab344",
      "incomplete_value": false,
      "site": "00bab350",
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
            "const:c02:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00baa350",
      "incomplete_value": false,
      "site": "00baa35c",
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
            "const:bb8:8"
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bab358",
      "incomplete_value": false,
      "site": "00bab364",
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
            "const:ba9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00baa364",
      "incomplete_value": false,
      "site": "00baa370",
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
            "const:b69:8"
          ]
        ]
      ]
    },
    "ordinal": 27,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00baae34",
      "PARAM",
      [
        "storage",
        "002af48e",
        null,
        "string"
      ]
    ],
    [
      "00baaf40",
      "PARAM",
      [
        "storage",
        "002c1cc7",
        null,
        "string"
      ]
    ],
    [
      "00baaf54",
      "PARAM",
      [
        "storage",
        "002a0b69",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00baae34",
      "PARAM",
      [
        "storage",
        "002af565",
        null,
        "string"
      ]
    ],
    [
      "00baaf40",
      "PARAM",
      [
        "storage",
        "002c1d11",
        null,
        "string"
      ]
    ],
    [
      "00baaf54",
      "PARAM",
      [
        "storage",
        "002a0ba9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba9f58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba9/00ba9dd8.md#insn-00ba9f58) · [`00baa35c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba9/00ba9dd8.md#insn-00baa35c) · [`00baa370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba9/00ba9dd8.md#insn-00baa370)
- 新版 [`00baaf4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baa/00baadcc.md#insn-00baaf4c) · [`00bab350`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baa/00baadcc.md#insn-00bab350) · [`00bab364`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baa/00baadcc.md#insn-00bab364)

~~~diff
- 00ba9f58 ["INT_ADD", "register:40f0:8", ["const:ba9f58:8", "const:4:8"]]
- 00ba9f58 ["CALL", null, ["callee:00c59150:8"]]
+ 00baaf4c ["INT_ADD", "register:40f0:8", ["const:baaf4c:8", "const:4:8"]]
+ 00baaf4c ["CALL", null, ["callee:00c59150:8"]]
- 00ba9f58 bytes 8ab80294
+ 00baaf4c bytes 81b80294
- 00baa35c ["INT_ADD", "register:40f0:8", ["const:baa35c:8", "const:4:8"]]
- 00baa35c ["CALL", null, ["callee:00c59150:8"]]
+ 00bab350 ["INT_ADD", "register:40f0:8", ["const:bab350:8", "const:4:8"]]
+ 00bab350 ["CALL", null, ["callee:00c59150:8"]]
- 00baa35c bytes 89b70294
+ 00bab350 bytes 80b70294
- 00baa370 ["INT_ADD", "register:40f0:8", ["const:baa370:8", "const:4:8"]]
- 00baa370 ["CALL", null, ["callee:00c59150:8"]]
+ 00bab364 ["INT_ADD", "register:40f0:8", ["const:bab364:8", "const:4:8"]]
+ 00bab364 ["CALL", null, ["callee:00c59150:8"]]
- 00baa370 bytes 84b70294
+ 00bab364 bytes 7bb70294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5407a061c06cab8699504505db9fe632"></a>

### [`00bb2784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb2/00bb2784.md) → [`00bb3778`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb3/00bb3778.md) _ZN11flatbuffers19SetLoadFileFunctionEPFbPKcbPNSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bb27a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb2/00bb27a8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bb379c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb3/00bb379c.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb3794",
      "incomplete_value": true,
      "site": "00bb3794",
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
            "const:748:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb27a0",
      "incomplete_value": true,
      "site": "00bb27a0",
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
            "const:778:8"
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
      "00bb377c",
      "READ",
      [
        "storage",
        "00ca4778",
        null,
        "pointer"
      ]
    ],
    [
      "00bb3790",
      "DATA",
      [
        "storage",
        "00bb27a8",
        null,
        null
      ]
    ],
    [
      "00bb3794",
      "WRITE",
      [
        "storage",
        "00ca4778",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bb377c",
      "READ",
      [
        "storage",
        "00ca5748",
        null,
        "pointer"
      ]
    ],
    [
      "00bb3790",
      "DATA",
      [
        "storage",
        "00bb379c",
        null,
        null
      ]
    ],
    [
      "00bb3794",
      "WRITE",
      [
        "storage",
        "00ca5748",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb27a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb2/00bb2784.md#insn-00bb27a0) · [`00bb2784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb2/00bb2784.md#insn-00bb2784) · [`00bb2788`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb2/00bb2784.md#insn-00bb2788)
- 新版 [`00bb3794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb3/00bb3778.md#insn-00bb3794) · [`00bb3778`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb3/00bb3778.md#insn-00bb3778) · [`00bb377c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb3/00bb3778.md#insn-00bb377c)

~~~diff
- 00bb27a0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
- 00bb27a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 00bb3794 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:748:8"]]
+ 00bb3794 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00bb27a0 bytes 2abd03f9
+ 00bb3794 bytes 2aa503f9
- 00bb2784 ["COPY", "register:4048:8", ["const:ca4000:8"]]
+ 00bb3778 ["COPY", "register:4048:8", ["const:ca5000:8"]]
- 00bb2784 bytes 890700d0
+ 00bb3778 bytes 890700d0
- 00bb2788 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
- 00bb2788 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb377c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:748:8"]]
+ 00bb377c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb2788 bytes 28bd43f9
+ 00bb377c bytes 28a543f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cae41d574db5844793fc5c99a9d6c6f8"></a>

### [`00bb2bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb2/00bb2bac.md) → [`00bb3ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb3/00bb3ba0.md) _ZN11flatbuffers21SetFileExistsFunctionEPFbPKcE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bb2bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb2/00bb2bd0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bb3bc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb3/00bb3bc4.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb3bbc",
      "incomplete_value": true,
      "site": "00bb3bbc",
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
            "const:750:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb2bc8",
      "incomplete_value": true,
      "site": "00bb2bc8",
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
            "const:780:8"
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
      "00bb3ba4",
      "READ",
      [
        "storage",
        "00ca4780",
        null,
        "pointer"
      ]
    ],
    [
      "00bb3bb8",
      "DATA",
      [
        "storage",
        "00bb2bd0",
        null,
        null
      ]
    ],
    [
      "00bb3bbc",
      "WRITE",
      [
        "storage",
        "00ca4780",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bb3ba4",
      "READ",
      [
        "storage",
        "00ca5750",
        null,
        "pointer"
      ]
    ],
    [
      "00bb3bb8",
      "DATA",
      [
        "storage",
        "00bb3bc4",
        null,
        null
      ]
    ],
    [
      "00bb3bbc",
      "WRITE",
      [
        "storage",
        "00ca5750",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb2bc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb2/00bb2bac.md#insn-00bb2bc8) · [`00bb2bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb2/00bb2bac.md#insn-00bb2bac) · [`00bb2bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb2/00bb2bac.md#insn-00bb2bb0)
- 新版 [`00bb3bbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb3/00bb3ba0.md#insn-00bb3bbc) · [`00bb3ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb3/00bb3ba0.md#insn-00bb3ba0) · [`00bb3ba4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb3/00bb3ba0.md#insn-00bb3ba4)

~~~diff
- 00bb2bc8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:780:8"]]
- 00bb2bc8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 00bb3bbc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:750:8"]]
+ 00bb3bbc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00bb2bc8 bytes 2ac103f9
+ 00bb3bbc bytes 2aa903f9
- 00bb2bac ["COPY", "register:4048:8", ["const:ca4000:8"]]
+ 00bb3ba0 ["COPY", "register:4048:8", ["const:ca5000:8"]]
- 00bb2bac bytes 890700d0
+ 00bb3ba0 bytes 890700d0
- 00bb2bb0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:780:8"]]
- 00bb2bb0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb3ba4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:750:8"]]
+ 00bb3ba4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb2bb0 bytes 28c143f9
+ 00bb3ba4 bytes 28a943f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b70fafd4e46762d193d0947d114a39b2"></a>

### [`00bb2bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb2/00bb2bd0.md) → [`00bb3bc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb3/00bb3bc4.md) FUN_00bb3bc4

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00bb2744`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb2/00bb2744.md) [`00bb2bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb2/00bb2bac.md) · 呼出先 7件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c582b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c582b0.md) [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c5a160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a160.md) [`00c5d1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1b0.md)
- 新版 呼出元 2件 [`00bb3738`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb3/00bb3738.md) [`00bb3ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb3/00bb3ba0.md) · 呼出先 7件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59280.md) [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c5b130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b130.md) [`00c5e180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb3c00",
      "incomplete_value": true,
      "site": "00bb3c1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00bb2c0c",
      "incomplete_value": true,
      "site": "00bb2c28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb3c3c",
      "incomplete_value": true,
      "site": "00bb3c44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00bb2c48",
      "incomplete_value": true,
      "site": "00bb2c50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb3c40",
      "incomplete_value": true,
      "site": "00bb3c4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00bb2c4c",
      "incomplete_value": true,
      "site": "00bb2c58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00bb3be8",
      "READ",
      [
        "storage",
        "00c9b990",
        null,
        "pointer"
      ]
    ],
    [
      "00bb3c1c",
      "DATA",
      [
        "storage",
        "00c91008",
        null,
        "pointer"
      ]
    ],
    [
      "00bb3c20",
      "DATA",
      [
        "storage",
        "00c90fe0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bb3be8",
      "READ",
      [
        "storage",
        "00c9c960",
        null,
        "pointer"
      ]
    ],
    [
      "00bb3c1c",
      "DATA",
      [
        "storage",
        "00c91fd8",
        null,
        "pointer"
      ]
    ],
    [
      "00bb3c20",
      "DATA",
      [
        "storage",
        "00c91fb0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb2c90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb2/00bb2bd0.md#insn-00bb2c90) · [`00bb2bec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb2/00bb2bd0.md#insn-00bb2bec) · [`00bb2bf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb2/00bb2bd0.md#insn-00bb2bf4)
- 新版 [`00bb3c84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb3/00bb3bc4.md#insn-00bb3c84) · [`00bb3be0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb3/00bb3bc4.md#insn-00bb3be0) · [`00bb3be8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb3/00bb3bc4.md#insn-00bb3be8)

~~~diff
- 00bb2c90 ["INT_ADD", "register:40f0:8", ["const:bb2c90:8", "const:4:8"]]
- 00bb2c90 ["CALL", null, ["callee:00c5b130:8"]]
+ 00bb3c84 ["INT_ADD", "register:40f0:8", ["const:bb3c84:8", "const:4:8"]]
+ 00bb3c84 ["CALL", null, ["callee:00c5b130:8"]]
- 00bb2c90 bytes 349d0294
+ 00bb3c84 bytes 2b9d0294
- 00bb2bec ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00bb3be0 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00bb2bec bytes 480700b0
+ 00bb3be0 bytes 480700b0
- 00bb2bf4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:990:8"]]
- 00bb2bf4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb3be8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:960:8"]]
+ 00bb3be8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb2bf4 bytes 08c944f9
+ 00bb3be8 bytes 08b144f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa960a5369c2d8ef8765dcc94414be96"></a>

### [`00bb2d14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb2/00bb2d14.md) → [`00bb3d08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb3/00bb3d08.md) _ZN11flatbuffers8SaveFileEPKcS1_mb

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c582b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c582b0.md) [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c58d40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58d40.md) [`00c58fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58fe0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59280.md) [`00c59340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59340.md) [`00c59d10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59d10.md) [`00c59fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59fb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.51% / 新版 94.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb3d54",
      "incomplete_value": true,
      "site": "00bb3d68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00bb2d60",
      "incomplete_value": true,
      "site": "00bb2d74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00bb3d50",
      "incomplete_value": true,
      "site": "00bb3d6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00bb2d5c",
      "incomplete_value": true,
      "site": "00bb2d78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb3d88",
      "incomplete_value": true,
      "site": "00bb3d90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00bb2d94",
      "incomplete_value": true,
      "site": "00bb2d9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00bb3d34",
      "READ",
      [
        "storage",
        "00c9b998",
        null,
        "pointer"
      ]
    ],
    [
      "00bb3d68",
      "DATA",
      [
        "storage",
        "00c91210",
        null,
        "pointer"
      ]
    ],
    [
      "00bb3d6c",
      "DATA",
      [
        "storage",
        "00c911e8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bb3d34",
      "READ",
      [
        "storage",
        "00c9c968",
        null,
        "pointer"
      ]
    ],
    [
      "00bb3d68",
      "DATA",
      [
        "storage",
        "00c921e0",
        null,
        "pointer"
      ]
    ],
    [
      "00bb3d6c",
      "DATA",
      [
        "storage",
        "00c921b8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb2d38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb2/00bb2d14.md#insn-00bb2d38) · [`00bb2d40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb2/00bb2d14.md#insn-00bb2d40) · [`00bb2d7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb2/00bb2d14.md#insn-00bb2d7c)
- 新版 [`00bb3d2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb3/00bb3d08.md#insn-00bb3d2c) · [`00bb3d34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb3/00bb3d08.md#insn-00bb3d34) · [`00bb3d70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb3/00bb3d08.md#insn-00bb3d70)

~~~diff
- 00bb2d38 ["COPY", "register:4048:8", ["const:c9b000:8"]]
+ 00bb3d2c ["COPY", "register:4048:8", ["const:c9c000:8"]]
- 00bb2d38 bytes 490700b0
+ 00bb3d2c bytes 490700b0
- 00bb2d40 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:998:8"]]
- 00bb2d40 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb3d34 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:968:8"]]
+ 00bb3d34 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb2d40 bytes 29cd44f9
+ 00bb3d34 bytes 29b544f9
- 00bb2d7c ["INT_ADD", "register:40f0:8", ["const:bb2d7c:8", "const:4:8"]]
- 00bb2d7c ["CALL", null, ["callee:00c59280:8"]]
+ 00bb3d70 ["INT_ADD", "register:40f0:8", ["const:bb3d70:8", "const:4:8"]]
+ 00bb3d70 ["CALL", null, ["callee:00c59280:8"]]
- 00bb2d7c bytes 4d950294
+ 00bb3d70 bytes 44950294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9138c27183b6dfb51a1a66298f05e936"></a>

### [`00bb3874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb3/00bb3874.md) → [`00bb4868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb4/00bb4868.md) _ZN11flatbuffers18RelativeToRootPathERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEES8_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5d240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d240.md) · 呼出先 10件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md)
- 新版 呼出元 1件 [`00c5e210`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e210.md) · 呼出先 10件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.90% / 新版 98.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb4d08",
      "incomplete_value": false,
      "site": "00bb4d14",
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
            "const:a7e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb3d14",
      "incomplete_value": false,
      "site": "00bb3d20",
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
            "const:9a0:8"
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
      "definition_site": "00bb4d28",
      "incomplete_value": false,
      "site": "00bb4d30",
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
            "const:a7e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb3d34",
      "incomplete_value": false,
      "site": "00bb3d3c",
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
            "const:9a0:8"
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
      "00bb4a98",
      "PARAM",
      [
        "storage",
        "002a52f6",
        null,
        null
      ]
    ],
    [
      "00bb4d08",
      "PARAM",
      [
        "storage",
        "002bf9a0",
        null,
        null
      ]
    ],
    [
      "00bb4d28",
      "PARAM",
      [
        "storage",
        "002bf9a0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bb4a98",
      "PARAM",
      [
        "storage",
        "002a53c1",
        null,
        null
      ]
    ],
    [
      "00bb4d08",
      "PARAM",
      [
        "storage",
        "002bfa7e",
        null,
        null
      ]
    ],
    [
      "00bb4d28",
      "PARAM",
      [
        "storage",
        "002bfa7e",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb3d20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb3/00bb3874.md#insn-00bb3d20) · [`00bb3d3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb3/00bb3874.md#insn-00bb3d3c) · [`00bb38ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb3/00bb3874.md#insn-00bb38ac)
- 新版 [`00bb4d14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb4/00bb4868.md#insn-00bb4d14) · [`00bb4d30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb4/00bb4868.md#insn-00bb4d30) · [`00bb48a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb4/00bb4868.md#insn-00bb48a0)

~~~diff
- 00bb3d20 ["INT_ADD", "register:40f0:8", ["const:bb3d20:8", "const:4:8"]]
- 00bb3d20 ["CALL", null, ["callee:00c5c660:8"]]
+ 00bb4d14 ["INT_ADD", "register:40f0:8", ["const:bb4d14:8", "const:4:8"]]
+ 00bb4d14 ["CALL", null, ["callee:00c5c660:8"]]
- 00bb3d20 bytes 5c9e0294
+ 00bb4d14 bytes 539e0294
- 00bb3d3c ["INT_ADD", "register:40f0:8", ["const:bb3d3c:8", "const:4:8"]]
- 00bb3d3c ["CALL", null, ["callee:00c5c660:8"]]
+ 00bb4d30 ["INT_ADD", "register:40f0:8", ["const:bb4d30:8", "const:4:8"]]
+ 00bb4d30 ["CALL", null, ["callee:00c5c660:8"]]
- 00bb3d3c bytes 559e0294
+ 00bb4d30 bytes 4c9e0294
- 00bb38ac ["INT_ADD", "register:40f0:8", ["const:bb38ac:8", "const:4:8"]]
- 00bb38ac ["CALL", null, ["callee:00c5d7c0:8"]]
+ 00bb48a0 ["INT_ADD", "register:40f0:8", ["const:bb48a0:8", "const:4:8"]]
+ 00bb48a0 ["CALL", null, ["callee:00c5d7c0:8"]]
- 00bb38ac bytes d1a30294
+ 00bb48a0 bytes c8a30294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a5be8e64cfd9ba9b157486a253f3e76"></a>

### [`00bb40ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb4/00bb40ac.md) → [`00bb50a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb5/00bb50a0.md) _ZN11flatbuffers11ConvertCaseERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEENS_4CaseES9_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00bb40ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb4/00bb40ac.md) [`00c5c7e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5c7e0.md) · 呼出先 19件 [`00b611c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b611c8.md) [`00bb40ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb4/00bb40ac.md) [`00bb4e20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb4/00bb4e20.md) [`00bb51ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb51ec.md) [`00bb5204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5204.md)
- 新版 呼出元 2件 [`00bb50a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb5/00bb50a0.md) [`00c5d7b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5d7b0.md) · 呼出先 19件 [`00b621bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b621bc.md) [`00bb50a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb5/00bb50a0.md) [`00bb5e14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb5/00bb5e14.md) [`00bb61e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb61e0.md) [`00bb61f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb61f8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 99.19% / 新版 99.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb553c",
      "incomplete_value": true,
      "site": "00bb553c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bb4548",
      "incomplete_value": true,
      "site": "00bb4548",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bb553c",
      "incomplete_value": true,
      "site": "00bb553c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:940:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb4548",
      "incomplete_value": true,
      "site": "00bb4548",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:970:8"
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
      "definition_site": "00bb58d8",
      "incomplete_value": true,
      "site": "00bb58d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bb48e4",
      "incomplete_value": true,
      "site": "00bb48e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 65,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bb5114",
      "PARAM",
      [
        "storage",
        "002bc013",
        null,
        "string"
      ]
    ],
    [
      "00bb5134",
      "DATA",
      [
        "storage",
        "0030e584",
        "switchD_00bb4148::switchdataD_0030e584",
        "ushort"
      ]
    ],
    [
      "00bb53f8",
      "PARAM",
      [
        "storage",
        "002b24fd",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bb5114",
      "PARAM",
      [
        "storage",
        "002bc0f1",
        null,
        "string"
      ]
    ],
    [
      "00bb5134",
      "DATA",
      [
        "storage",
        "0030e5c4",
        "switchD_00bb513c::switchdataD_0030e5c4",
        "ushort"
      ]
    ],
    [
      "00bb53f8",
      "PARAM",
      [
        "storage",
        "002b2547",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb4124`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb4/00bb40ac.md#insn-00bb4124) · [`00bb40f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb4/00bb40ac.md#insn-00bb40f0) · [`00bb4120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb4/00bb40ac.md#insn-00bb4120)
- 新版 [`00bb5118`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb5/00bb50a0.md#insn-00bb5118) · [`00bb50e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb5/00bb50a0.md#insn-00bb50e4) · [`00bb5114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb5/00bb50a0.md#insn-00bb5114)

~~~diff
- 00bb4124 ["INT_ADD", "register:40f0:8", ["const:bb4124:8", "const:4:8"]]
- 00bb4124 ["CALL", null, ["callee:00c59510:8"]]
+ 00bb5118 ["INT_ADD", "register:40f0:8", ["const:bb5118:8", "const:4:8"]]
+ 00bb5118 ["CALL", null, ["callee:00c59510:8"]]
- 00bb4124 bytes 07910294
+ 00bb5118 bytes fe900294
- 00bb40f0 ["INT_ADD", "register:40f0:8", ["const:bb40f0:8", "const:4:8"]]
- 00bb40f0 ["CALL", null, ["callee:00c5c650:8"]]
+ 00bb50e4 ["INT_ADD", "register:40f0:8", ["const:bb50e4:8", "const:4:8"]]
+ 00bb50e4 ["CALL", null, ["callee:00c5c650:8"]]
- 00bb40f0 bytes 649d0294
+ 00bb50e4 bytes 5b9d0294
- 00bb4120 ["COPY", "tmp:0:8", ["const:13:8"]]
- 00bb4120 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bb4120 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bb4120 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bb5114 ["COPY", "tmp:0:8", ["const:f1:8"]]
+ 00bb5114 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb5114 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb5114 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bb4120 bytes 004c0091
+ 00bb5114 bytes 00c40391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5849d87c0a5bad294d1f36d73f5a5725"></a>

### [`00bb5584`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5584.md) → [`00bb6578`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb6578.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEEC2Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d270.md) · 呼出先 7件 [`00bb5a5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5a5c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58350.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md) [`00c5a870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a870.md)
- 新版 呼出元 1件 [`00c5e240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e240.md) · 呼出先 7件 [`00bb6a50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb6a50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59320`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59320.md) [`00c59330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59330.md) [`00c5b840`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b840.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.77% / 新版 95.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb65a8",
      "incomplete_value": true,
      "site": "00bb65ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bb55b4",
      "incomplete_value": true,
      "site": "00bb55b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bb65cc",
      "incomplete_value": true,
      "site": "00bb65e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bb55d8",
      "incomplete_value": true,
      "site": "00bb55f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bb65f8",
      "incomplete_value": true,
      "site": "00bb6600",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:958:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb5604",
      "incomplete_value": true,
      "site": "00bb560c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:988:8"
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
      "00bb6598",
      "READ",
      [
        "storage",
        "00c9b918",
        null,
        "pointer"
      ]
    ],
    [
      "00bb65ac",
      "DATA",
      [
        "storage",
        "00c90d80",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "00bb65bc",
      "READ",
      [
        "storage",
        "00c9b9c0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bb6598",
      "READ",
      [
        "storage",
        "00c9c8e8",
        null,
        "pointer"
      ]
    ],
    [
      "00bb65ac",
      "DATA",
      [
        "storage",
        "00c91d50",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "00bb65bc",
      "READ",
      [
        "storage",
        "00c9c990",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb560c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5584.md#insn-00bb560c) · [`00bb5638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5584.md#insn-00bb5638) · [`00bb559c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5584.md#insn-00bb559c)
- 新版 [`00bb6600`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb6578.md#insn-00bb6600) · [`00bb662c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb6578.md#insn-00bb662c) · [`00bb6590`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb6578.md#insn-00bb6590)

~~~diff
- 00bb560c ["INT_ADD", "register:40f0:8", ["const:bb560c:8", "const:4:8"]]
- 00bb560c ["CALL", null, ["callee:00c5e220:8"]]
+ 00bb6600 ["INT_ADD", "register:40f0:8", ["const:bb6600:8", "const:4:8"]]
+ 00bb6600 ["CALL", null, ["callee:00c5e220:8"]]
- 00bb560c bytes 119f0294
+ 00bb6600 bytes 089f0294
- 00bb5638 ["INT_ADD", "register:40f0:8", ["const:bb5638:8", "const:4:8"]]
- 00bb5638 ["CALL", null, ["callee:00c59320:8"]]
+ 00bb662c ["INT_ADD", "register:40f0:8", ["const:bb662c:8", "const:4:8"]]
+ 00bb662c ["CALL", null, ["callee:00c59320:8"]]
- 00bb5638 bytes 468b0294
+ 00bb662c bytes 3d8b0294
- 00bb559c ["COPY", "register:4048:8", ["const:c9b000:8"]]
+ 00bb6590 ["COPY", "register:4048:8", ["const:c9c000:8"]]
- 00bb559c bytes 290700d0
+ 00bb6590 bytes 290700d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e66bd335cb6c798958417bd3dfc0234f"></a>

### [`00bb5810`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5810.md) → [`00bb6804`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb6804.md) FUN_00bb6804

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5d1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1b0.md) [`00c5d280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d280.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5e180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e180.md) [`00c5e250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e250.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 72.22% / 新版 72.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb6830",
      "incomplete_value": true,
      "site": "00bb6830",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00bb583c",
      "incomplete_value": true,
      "site": "00bb583c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb6834",
      "incomplete_value": true,
      "site": "00bb6834",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00bb5840",
      "incomplete_value": true,
      "site": "00bb5840",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00bb681c",
      "READ",
      [
        "storage",
        "00c9b100",
        null,
        "pointer"
      ]
    ],
    [
      "00bb6830",
      "DATA",
      [
        "storage",
        "00c90f90",
        null,
        "pointer"
      ]
    ],
    [
      "00bb6834",
      "DATA",
      [
        "storage",
        "00c90fb8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bb681c",
      "READ",
      [
        "storage",
        "00c9c0d0",
        null,
        "pointer"
      ]
    ],
    [
      "00bb6830",
      "DATA",
      [
        "storage",
        "00c91f60",
        null,
        "pointer"
      ]
    ],
    [
      "00bb6834",
      "DATA",
      [
        "storage",
        "00c91f88",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb5820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5810.md#insn-00bb5820) · [`00bb5828`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5810.md#insn-00bb5828) · [`00bb5844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5810.md#insn-00bb5844)
- 新版 [`00bb6814`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb6804.md#insn-00bb6814) · [`00bb681c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb6804.md#insn-00bb681c) · [`00bb6838`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb6804.md#insn-00bb6838)

~~~diff
- 00bb5820 ["COPY", "register:4048:8", ["const:c9b000:8"]]
+ 00bb6814 ["COPY", "register:4048:8", ["const:c9c000:8"]]
- 00bb5820 bytes 290700d0
+ 00bb6814 bytes 290700d0
- 00bb5828 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:100:8"]]
- 00bb5828 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb681c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d0:8"]]
+ 00bb681c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb5828 bytes 298140f9
+ 00bb681c bytes 296940f9
- 00bb5844 ["INT_ADD", "register:40f0:8", ["const:bb5844:8", "const:4:8"]]
- 00bb5844 ["CALL", null, ["callee:00c5e250:8"]]
+ 00bb6838 ["INT_ADD", "register:40f0:8", ["const:bb6838:8", "const:4:8"]]
+ 00bb6838 ["CALL", null, ["callee:00c5e250:8"]]
- 00bb5844 bytes 8f9e0294
+ 00bb6838 bytes 869e0294
~~~


<a id="compare-50bfdbfa2c52f43a16a00d40a6de17ed"></a>

### [`00bb5858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5858.md) → [`00bb684c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb684c.md) FUN_00bb684c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5d1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1b0.md) [`00c5d280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d280.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5e180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e180.md) [`00c5e250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e250.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 76.19% / 新版 76.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb687c",
      "incomplete_value": true,
      "site": "00bb687c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00bb5888",
      "incomplete_value": true,
      "site": "00bb5888",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb6880",
      "incomplete_value": true,
      "site": "00bb6880",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00bb588c",
      "incomplete_value": true,
      "site": "00bb588c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bb6864",
      "READ",
      [
        "storage",
        "00c9b100",
        null,
        "pointer"
      ]
    ],
    [
      "00bb687c",
      "DATA",
      [
        "storage",
        "00c90f90",
        null,
        "pointer"
      ]
    ],
    [
      "00bb6880",
      "DATA",
      [
        "storage",
        "00c90fb8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bb6864",
      "READ",
      [
        "storage",
        "00c9c0d0",
        null,
        "pointer"
      ]
    ],
    [
      "00bb687c",
      "DATA",
      [
        "storage",
        "00c91f60",
        null,
        "pointer"
      ]
    ],
    [
      "00bb6880",
      "DATA",
      [
        "storage",
        "00c91f88",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb5868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5858.md#insn-00bb5868) · [`00bb5870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5858.md#insn-00bb5870) · [`00bb5890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5858.md#insn-00bb5890)
- 新版 [`00bb685c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb684c.md#insn-00bb685c) · [`00bb6864`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb684c.md#insn-00bb6864) · [`00bb6884`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb684c.md#insn-00bb6884)

~~~diff
- 00bb5868 ["COPY", "register:4048:8", ["const:c9b000:8"]]
+ 00bb685c ["COPY", "register:4048:8", ["const:c9c000:8"]]
- 00bb5868 bytes 290700d0
+ 00bb685c bytes 290700d0
- 00bb5870 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:100:8"]]
- 00bb5870 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb6864 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d0:8"]]
+ 00bb6864 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb5870 bytes 298140f9
+ 00bb6864 bytes 296940f9
- 00bb5890 ["INT_ADD", "register:40f0:8", ["const:bb5890:8", "const:4:8"]]
- 00bb5890 ["CALL", null, ["callee:00c5e250:8"]]
+ 00bb6884 ["INT_ADD", "register:40f0:8", ["const:bb6884:8", "const:4:8"]]
+ 00bb6884 ["CALL", null, ["callee:00c5e250:8"]]
- 00bb5890 bytes 7c9e0294
+ 00bb6884 bytes 739e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cdc719be6128e460a339cf17265be0b8"></a>

### [`00bb58ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb58ac.md) → [`00bb68a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb68a0.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEED2Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5d280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d280.md) · 呼出先 5件 [`00bb5a5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb5a5c.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md) [`00c5a0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0d0.md) [`00c5bf10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf10.md) [`00c5d260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d260.md)
- 新版 呼出元 1件 [`00c5e250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e250.md) · 呼出先 5件 [`00bb6a50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb6a50.md) [`00c59330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59330.md) [`00c5b0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0a0.md) [`00c5cee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cee0.md) [`00c5e230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e230.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.31% / 新版 92.31%

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
      "definition_site": "00bb68bc",
      "incomplete_value": true,
      "site": "00bb68c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bb58c8",
      "incomplete_value": true,
      "site": "00bb58cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bb6928",
      "incomplete_value": true,
      "site": "00bb6928",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bb5934",
      "incomplete_value": true,
      "site": "00bb5934",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00bb68b4",
      "READ",
      [
        "storage",
        "00c9b9c0",
        null,
        "pointer"
      ]
    ],
    [
      "00bb68c0",
      "DATA",
      [
        "storage",
        "00c91040",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "00bb68e8",
      "READ",
      [
        "storage",
        "00c91058",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "00bb68b4",
      "READ",
      [
        "storage",
        "00c9c990",
        null,
        "pointer"
      ]
    ],
    [
      "00bb68c0",
      "DATA",
      [
        "storage",
        "00c92010",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "00bb68e8",
      "READ",
      [
        "storage",
        "00c92028",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb58b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb58ac.md#insn-00bb58b8) · [`00bb58c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb58ac.md#insn-00bb58c0) · [`00bb58d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb58ac.md#insn-00bb58d8)
- 新版 [`00bb68ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb68a0.md#insn-00bb68ac) · [`00bb68b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb68a0.md#insn-00bb68b4) · [`00bb68cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb68a0.md#insn-00bb68cc)

~~~diff
- 00bb58b8 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00bb68ac ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00bb58b8 bytes 280700d0
+ 00bb68ac bytes 280700d0
- 00bb58c0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9c0:8"]]
- 00bb58c0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb68b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:990:8"]]
+ 00bb68b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb58c0 bytes 08e144f9
+ 00bb68b4 bytes 08c944f9
- 00bb58d8 ["INT_ADD", "register:40f0:8", ["const:bb58d8:8", "const:4:8"]]
- 00bb58d8 ["CALL", null, ["callee:00c5e230:8"]]
+ 00bb68cc ["INT_ADD", "register:40f0:8", ["const:bb68cc:8", "const:4:8"]]
+ 00bb68cc ["CALL", null, ["callee:00c5e230:8"]]
- 00bb58d8 bytes 629e0294
+ 00bb68cc bytes 599e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cdc532d930a56c1119b9e3dab2171b90"></a>

### [`00bb647c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb647c.md) → [`00bb7470`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7470.md) FUN_00bb7470

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md) [`00c5d1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1b0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59330.md) [`00c5e180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e180.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 77.42% / 新版 77.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb7490",
      "incomplete_value": true,
      "site": "00bb749c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00bb649c",
      "incomplete_value": true,
      "site": "00bb64a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb74a0",
      "incomplete_value": true,
      "site": "00bb74a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00bb64ac",
      "incomplete_value": true,
      "site": "00bb64ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00bb74d0",
      "incomplete_value": true,
      "site": "00bb74d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bb64dc",
      "incomplete_value": true,
      "site": "00bb64e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00bb7488",
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      "00bb749c",
      "DATA",
      [
        "storage",
        "00c910e0",
        null,
        "pointer"
      ]
    ],
    [
      "00bb74a0",
      "DATA",
      [
        "storage",
        "00c91108",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bb7488",
      "READ",
      [
        "storage",
        "00c9bd28",
        null,
        "pointer"
      ]
    ],
    [
      "00bb749c",
      "DATA",
      [
        "storage",
        "00c920b0",
        null,
        "pointer"
      ]
    ],
    [
      "00bb74a0",
      "DATA",
      [
        "storage",
        "00c920d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb648c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb647c.md#insn-00bb648c) · [`00bb6494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb647c.md#insn-00bb6494) · [`00bb64b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb647c.md#insn-00bb64b0)
- 新版 [`00bb7480`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7470.md#insn-00bb7480) · [`00bb7488`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7470.md#insn-00bb7488)

~~~diff
- 00bb648c ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 00bb7480 ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 00bb648c bytes 29070090
+ 00bb7480 bytes 29070090
- 00bb6494 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d58:8"]]
- 00bb6494 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb7488 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d28:8"]]
+ 00bb7488 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb6494 bytes 29ad46f9
+ 00bb7488 bytes 299546f9
- 00bb64b0 ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 00bb64b0 bytes 29070090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a5b21769cae9255190220f43aac8c74"></a>

### [`00bb64f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb64f8.md) → [`00bb74ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb74ec.md) FUN_00bb74ec

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58360.md) [`00c5d1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1b0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59330.md) [`00c5e180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e180.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 72.73% / 新版 72.73%

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
      "definition_site": "00bb750c",
      "incomplete_value": true,
      "site": "00bb7518",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00bb6518",
      "incomplete_value": true,
      "site": "00bb6524",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb751c",
      "incomplete_value": true,
      "site": "00bb751c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00bb6528",
      "incomplete_value": true,
      "site": "00bb6528",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00bb752c",
      "incomplete_value": true,
      "site": "00bb7530",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bb6538",
      "incomplete_value": true,
      "site": "00bb653c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00bb7504",
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      "00bb7518",
      "DATA",
      [
        "storage",
        "00c910e0",
        null,
        "pointer"
      ]
    ],
    [
      "00bb751c",
      "DATA",
      [
        "storage",
        "00c91108",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bb7504",
      "READ",
      [
        "storage",
        "00c9bd28",
        null,
        "pointer"
      ]
    ],
    [
      "00bb7518",
      "DATA",
      [
        "storage",
        "00c920b0",
        null,
        "pointer"
      ]
    ],
    [
      "00bb751c",
      "DATA",
      [
        "storage",
        "00c920d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb6508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb64f8.md#insn-00bb6508) · [`00bb6510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb64f8.md#insn-00bb6510) · [`00bb652c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb64f8.md#insn-00bb652c)
- 新版 [`00bb74fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb74ec.md#insn-00bb74fc) · [`00bb7504`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb74ec.md#insn-00bb7504)

~~~diff
- 00bb6508 ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 00bb74fc ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 00bb6508 bytes 29070090
+ 00bb74fc bytes 29070090
- 00bb6510 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d58:8"]]
- 00bb6510 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb7504 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d28:8"]]
+ 00bb7504 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb6510 bytes 29ad46f9
+ 00bb7504 bytes 299546f9
- 00bb652c ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 00bb652c bytes 29070090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-185d48f04c538f72225aaa5066d70907"></a>

### [`00bb66fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb66fc.md) → [`00bb76f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb76f0.md) _INIT_284

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bb3e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb3/00bb3e50.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c5d2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d2f0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bb4e44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb4/00bb4e44.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c5e2c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e2c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 70.59% / 新版 70.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb7724",
      "incomplete_value": true,
      "site": "00bb7724",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb6730",
      "incomplete_value": true,
      "site": "00bb6730",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:900:8"
              ]
            ]
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
      "definition_site": "00bb76fc",
      "incomplete_value": false,
      "site": "00bb7708",
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
            "const:28b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb6708",
      "incomplete_value": false,
      "site": "00bb6714",
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
            "const:1bc:8"
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
      "00bb76fc",
      "PARAM",
      [
        "storage",
        "002b61bc",
        null,
        null
      ]
    ],
    [
      "00bb7714",
      "READ",
      [
        "storage",
        "00c9b900",
        null,
        "pointer"
      ]
    ],
    [
      "00bb7714",
      "PARAM",
      [
        "storage",
        "011262e0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb76fc",
      "PARAM",
      [
        "storage",
        "002b628b",
        null,
        null
      ]
    ],
    [
      "00bb7714",
      "READ",
      [
        "storage",
        "00c9c8d0",
        null,
        "pointer"
      ]
    ],
    [
      "00bb7714",
      "PARAM",
      [
        "storage",
        "011272a0",
        "_ZN11flatbuffers13ClassicLocale9instance_E",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb6714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb66fc.md#insn-00bb6714) · [`00bb6708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb66fc.md#insn-00bb6708) · [`00bb6718`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb66fc.md#insn-00bb6718)
- 新版 [`00bb7708`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb76f0.md#insn-00bb7708) · [`00bb76fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb76f0.md#insn-00bb76fc) · [`00bb770c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb76f0.md#insn-00bb770c)

~~~diff
- 00bb6714 ["INT_ADD", "register:40f0:8", ["const:bb6714:8", "const:4:8"]]
- 00bb6714 ["CALL", null, ["callee:00c5e2c0:8"]]
+ 00bb7708 ["INT_ADD", "register:40f0:8", ["const:bb7708:8", "const:4:8"]]
+ 00bb7708 ["CALL", null, ["callee:00c5e2c0:8"]]
- 00bb6714 bytes f79a0294
+ 00bb7708 bytes ee9a0294
- 00bb6708 ["COPY", "tmp:0:8", ["const:1bc:8"]]
- 00bb6708 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00bb6708 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00bb6708 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00bb76fc ["COPY", "tmp:0:8", ["const:28b:8"]]
+ 00bb76fc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00bb76fc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00bb76fc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00bb6708 bytes 21f00691
+ 00bb76fc bytes 212c0a91
- 00bb6718 ["COPY", "register:4008:8", ["const:c9b000:8"]]
+ 00bb770c ["COPY", "register:4008:8", ["const:c9c000:8"]]
- 00bb6718 bytes 210700b0
+ 00bb770c bytes 210700b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a87ae496fca53dc82ddd4bfab3ae5036"></a>

### [`00bb67b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb67b4.md) → [`00bb77a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb77a8.md) _ZN8firebase9messaging8internal36RegisterTerminateOnDefaultAppDestroyEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5d4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d4f0.md) · 呼出先 5件 [`00bb76e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb76e8.md) [`00c5aca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aca0.md) [`00c5acc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acc0.md) [`00c5acd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acd0.md) [`00c5ad30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad30.md)
- 新版 呼出元 1件 [`00c5e4c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e4c0.md) · 呼出先 5件 [`00bb86dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb86dc.md) [`00c5bc70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bc70.md) [`00c5bc90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bc90.md) [`00c5bca0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bca0.md) [`00c5bd00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 81.25% / 新版 81.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb77b4",
      "incomplete_value": false,
      "site": "00bb77b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:30e000:8"
          ],
          [
            "leaf",
            "const:75f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb67c0",
      "incomplete_value": false,
      "site": "00bb67c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:30e000:8"
          ],
          [
            "leaf",
            "const:71f:8"
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
      "00bb77b4",
      "PARAM",
      [
        "storage",
        "0030e71f",
        null,
        "string"
      ]
    ],
    [
      "00bb77d8",
      "PARAM",
      [
        "storage",
        "0030e71f",
        null,
        "string"
      ]
    ],
    [
      "00bb77dc",
      "PARAM",
      [
        "storage",
        "00bb76e8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bb77b4",
      "PARAM",
      [
        "storage",
        "0030e75f",
        null,
        "string"
      ]
    ],
    [
      "00bb77d8",
      "PARAM",
      [
        "storage",
        "0030e75f",
        null,
        "string"
      ]
    ],
    [
      "00bb77dc",
      "PARAM",
      [
        "storage",
        "00bb86dc",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb67c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb67b4.md#insn-00bb67c4) · [`00bb67c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb67b4.md#insn-00bb67c0) · [`00bb67d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb67b4.md#insn-00bb67d4)
- 新版 [`00bb77b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb77a8.md#insn-00bb77b8) · [`00bb77b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb77a8.md#insn-00bb77b4) · [`00bb77c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb77a8.md#insn-00bb77c8)

~~~diff
- 00bb67c4 ["INT_ADD", "register:40f0:8", ["const:bb67c4:8", "const:4:8"]]
- 00bb67c4 ["CALL", null, ["callee:00c5bc70:8"]]
+ 00bb77b8 ["INT_ADD", "register:40f0:8", ["const:bb77b8:8", "const:4:8"]]
+ 00bb77b8 ["CALL", null, ["callee:00c5bc70:8"]]
- 00bb67c4 bytes 37910294
+ 00bb77b8 bytes 2e910294
- 00bb67c0 ["COPY", "tmp:0:8", ["const:71f:8"]]
- 00bb67c0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bb67c0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bb67c0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bb77b4 ["COPY", "tmp:0:8", ["const:75f:8"]]
+ 00bb77b4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb77b4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb77b4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bb67c0 bytes 007c1c91
+ 00bb77b4 bytes 007c1d91
- 00bb67d4 ["INT_ADD", "register:40f0:8", ["const:bb67d4:8", "const:4:8"]]
- 00bb67d4 ["CALL", null, ["callee:00c5bd00:8"]]
+ 00bb77c8 ["INT_ADD", "register:40f0:8", ["const:bb77c8:8", "const:4:8"]]
+ 00bb77c8 ["CALL", null, ["callee:00c5bd00:8"]]
- 00bb67d4 bytes 57910294
+ 00bb77c8 bytes 4e910294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebe33c1fbe05ba47de7090dfcfbfd978"></a>

### [`00bb67f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb67f4.md) → [`00bb77e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb77e8.md) _ZN8firebase9messaging8internal38UnregisterTerminateOnDefaultAppDestroyEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5d500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d500.md) · 呼出先 5件 [`00c5aca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aca0.md) [`00c5acc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acc0.md) [`00c5ace0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ace0.md) [`00c5ad30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad30.md) [`00c5d4e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d4e0.md)
- 新版 呼出元 1件 [`00c5e4d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e4d0.md) · 呼出先 5件 [`00c5bc70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bc70.md) [`00c5bc90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bc90.md) [`00c5bcb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bcb0.md) [`00c5bd00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd00.md) [`00c5e4b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e4b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb77f4",
      "incomplete_value": false,
      "site": "00bb77f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:30e000:8"
          ],
          [
            "leaf",
            "const:75f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb6800",
      "incomplete_value": false,
      "site": "00bb6804",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:30e000:8"
          ],
          [
            "leaf",
            "const:71f:8"
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
      "00bb77f4",
      "PARAM",
      [
        "storage",
        "0030e71f",
        null,
        "string"
      ]
    ],
    [
      "00bb7814",
      "PARAM",
      [
        "storage",
        "0030e71f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bb77f4",
      "PARAM",
      [
        "storage",
        "0030e75f",
        null,
        "string"
      ]
    ],
    [
      "00bb7814",
      "PARAM",
      [
        "storage",
        "0030e75f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb6804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb67f4.md#insn-00bb6804) · [`00bb6800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb67f4.md#insn-00bb6800) · [`00bb680c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb67f4.md#insn-00bb680c)
- 新版 [`00bb77f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb77e8.md#insn-00bb77f8) · [`00bb77f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb77e8.md#insn-00bb77f4) · [`00bb7800`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb77e8.md#insn-00bb7800)

~~~diff
- 00bb6804 ["INT_ADD", "register:40f0:8", ["const:bb6804:8", "const:4:8"]]
- 00bb6804 ["CALL", null, ["callee:00c5bc70:8"]]
+ 00bb77f8 ["INT_ADD", "register:40f0:8", ["const:bb77f8:8", "const:4:8"]]
+ 00bb77f8 ["CALL", null, ["callee:00c5bc70:8"]]
- 00bb6804 bytes 27910294
+ 00bb77f8 bytes 1e910294
- 00bb6800 ["COPY", "tmp:0:8", ["const:71f:8"]]
- 00bb6800 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bb6800 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bb6800 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bb77f4 ["COPY", "tmp:0:8", ["const:75f:8"]]
+ 00bb77f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb77f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb77f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bb6800 bytes 007c1c91
+ 00bb77f4 bytes 007c1d91
- 00bb680c ["INT_ADD", "register:40f0:8", ["const:bb680c:8", "const:4:8"]]
- 00bb680c ["CALL", null, ["callee:00c5e4b0:8"]]
+ 00bb7800 ["INT_ADD", "register:40f0:8", ["const:bb7800:8", "const:4:8"]]
+ 00bb7800 ["CALL", null, ["callee:00c5e4b0:8"]]
- 00bb680c bytes 359b0294
+ 00bb7800 bytes 2c9b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4a3dbe42fc7678939e980be3a2baf43"></a>

### [`00bb6834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6834.md) → [`00bb7828`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7828.md) _ZN8firebase9messaging11SetListenerEPNS0_8ListenerE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d380.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5d3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d3c0.md)
- 新版 呼出元 1件 [`00c5e350`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e350.md) · 呼出先 5件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5e390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e390.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 75.47% / 新版 75.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 5件, `call_argument_candidate` 2件, `store_condition` 7件, `store_destination` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb787c",
      "incomplete_value": true,
      "site": "00bb787c",
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
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb6888",
      "incomplete_value": true,
      "site": "00bb6888",
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
            "const:338:8"
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
      "definition_site": "00bb78a8",
      "incomplete_value": true,
      "site": "00bb78a8",
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
            "const:300:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb68b4",
      "incomplete_value": true,
      "site": "00bb68b4",
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
            "const:340:8"
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb78ac",
      "incomplete_value": true,
      "site": "00bb78ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:2f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb68b8",
      "incomplete_value": true,
      "site": "00bb68b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:330:8"
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bb7848",
      "PARAM",
      [
        "storage",
        "01126308",
        null,
        null
      ]
    ],
    [
      "00bb7858",
      "READ",
      [
        "storage",
        "01126330",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb785c",
      "READ",
      [
        "storage",
        "01126338",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb7848",
      "PARAM",
      [
        "storage",
        "011272c8",
        null,
        null
      ]
    ],
    [
      "00bb7858",
      "READ",
      [
        "storage",
        "011272f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb785c",
      "READ",
      [
        "storage",
        "011272f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb6858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6834.md#insn-00bb6858) · [`00bb6888`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6834.md#insn-00bb6888) · [`00bb68b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6834.md#insn-00bb68b4)
- 新版 [`00bb784c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7828.md#insn-00bb784c) · [`00bb787c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7828.md#insn-00bb787c) · [`00bb78a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7828.md#insn-00bb78a8)

~~~diff
- 00bb6858 ["INT_ADD", "register:40f0:8", ["const:bb6858:8", "const:4:8"]]
- 00bb6858 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00bb784c ["INT_ADD", "register:40f0:8", ["const:bb784c:8", "const:4:8"]]
+ 00bb784c ["CALL", null, ["callee:00c5baa0:8"]]
- 00bb6858 bytes 9e900294
+ 00bb784c bytes 95900294
- 00bb6888 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:338:8"]]
- 00bb6888 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bb787c ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:2f8:8"]]
+ 00bb787c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb6888 bytes e09e01f9
+ 00bb787c bytes e07e01f9
- 00bb68b4 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:340:8"]]
- 00bb68b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bb78a8 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:300:8"]]
+ 00bb78a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb68b4 bytes 00a301f9
+ 00bb78a8 bytes 008301f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-603e62dd7cac7f531bf231b2485fe7f0"></a>

### [`00bb69fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb69fc.md) → [`00bb79f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb79f0.md) _ZN8firebase9messaging11HasListenerEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5d370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d370.md) · 呼出先 2件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)
- 新版 呼出元 1件 [`00c5e340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e340.md) · 呼出先 2件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb7a04",
      "incomplete_value": false,
      "site": "00bb7a08",
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
            "const:2c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb6a10",
      "incomplete_value": false,
      "site": "00bb6a14",
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
            "const:308:8"
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
      "00bb7a04",
      "PARAM",
      [
        "storage",
        "01126308",
        null,
        null
      ]
    ],
    [
      "00bb7a10",
      "READ",
      [
        "storage",
        "01126330",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb7a14",
      "PARAM",
      [
        "storage",
        "01126308",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bb7a04",
      "PARAM",
      [
        "storage",
        "011272c8",
        null,
        null
      ]
    ],
    [
      "00bb7a10",
      "READ",
      [
        "storage",
        "011272f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb7a14",
      "PARAM",
      [
        "storage",
        "011272c8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb6a14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb69fc.md#insn-00bb6a14) · [`00bb6a08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb69fc.md#insn-00bb6a08) · [`00bb6a0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb69fc.md#insn-00bb6a0c)
- 新版 [`00bb7a08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb79f0.md#insn-00bb7a08) · [`00bb79fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb79f0.md#insn-00bb79fc) · [`00bb7a00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb79f0.md#insn-00bb7a00)

~~~diff
- 00bb6a14 ["INT_ADD", "register:40f0:8", ["const:bb6a14:8", "const:4:8"]]
- 00bb6a14 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00bb7a08 ["INT_ADD", "register:40f0:8", ["const:bb7a08:8", "const:4:8"]]
+ 00bb7a08 ["CALL", null, ["callee:00c5baa0:8"]]
- 00bb6a14 bytes 2f900294
+ 00bb7a08 bytes 26900294
- 00bb6a08 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bb79fc ["COPY", "register:4098:8", ["const:1127000:8"]]
- 00bb6a08 bytes 932b0090
+ 00bb79fc bytes 932b0090
- 00bb6a0c ["COPY", "tmp:0:8", ["const:308:8"]]
- 00bb6a0c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00bb6a0c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00bb6a0c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00bb7a00 ["COPY", "tmp:0:8", ["const:2c8:8"]]
+ 00bb7a00 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00bb7a00 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00bb7a00 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00bb6a0c bytes 73220c91
+ 00bb7a00 bytes 73220b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc4896ad65f505516a18d2b261c22d58"></a>

### [`00bb6a54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6a54.md) → [`00bb7a48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7a48.md) _ZN8firebase9messaging23NotifyListenerOnMessageERKNS0_7MessageE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d470.md) · 呼出先 2件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)
- 新版 呼出元 1件 [`00c5e440`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e440.md) · 呼出先 2件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bb7a6c",
      "incomplete_value": true,
      "site": "00bb7a6c",
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
      "definition_site": "00bb6a78",
      "incomplete_value": true,
      "site": "00bb6a78",
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
      "definition_site": "00bb7a5c",
      "incomplete_value": false,
      "site": "00bb7a60",
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
            "const:2c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb6a68",
      "incomplete_value": false,
      "site": "00bb6a6c",
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
            "const:308:8"
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
      "definition_site": "00bb7a84",
      "incomplete_value": false,
      "site": "00bb7a88",
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
            "const:2c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb6a90",
      "incomplete_value": false,
      "site": "00bb6a94",
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
            "const:308:8"
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
      "00bb7a5c",
      "PARAM",
      [
        "storage",
        "01126308",
        null,
        null
      ]
    ],
    [
      "00bb7a68",
      "READ",
      [
        "storage",
        "01126330",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb7a84",
      "PARAM",
      [
        "storage",
        "01126308",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bb7a5c",
      "PARAM",
      [
        "storage",
        "011272c8",
        null,
        null
      ]
    ],
    [
      "00bb7a68",
      "READ",
      [
        "storage",
        "011272f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb7a84",
      "PARAM",
      [
        "storage",
        "011272c8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb6a6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6a54.md#insn-00bb6a6c) · [`00bb6a94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6a54.md#insn-00bb6a94) · [`00bb6a64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6a54.md#insn-00bb6a64)
- 新版 [`00bb7a60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7a48.md#insn-00bb7a60) · [`00bb7a88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7a48.md#insn-00bb7a88) · [`00bb7a58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7a48.md#insn-00bb7a58)

~~~diff
- 00bb6a6c ["INT_ADD", "register:40f0:8", ["const:bb6a6c:8", "const:4:8"]]
- 00bb6a6c ["CALL", null, ["callee:00c5baa0:8"]]
+ 00bb7a60 ["INT_ADD", "register:40f0:8", ["const:bb7a60:8", "const:4:8"]]
+ 00bb7a60 ["CALL", null, ["callee:00c5baa0:8"]]
- 00bb6a6c bytes 19900294
+ 00bb7a60 bytes 10900294
- 00bb6a94 ["INT_ADD", "register:40f0:8", ["const:bb6a94:8", "const:4:8"]]
- 00bb6a94 ["CALL", null, ["callee:00c5bab0:8"]]
+ 00bb7a88 ["INT_ADD", "register:40f0:8", ["const:bb7a88:8", "const:4:8"]]
+ 00bb7a88 ["CALL", null, ["callee:00c5bab0:8"]]
- 00bb6a94 bytes 13900294
+ 00bb7a88 bytes 0a900294
- 00bb6a64 ["COPY", "register:4000:8", ["const:1126000:8"]]
+ 00bb7a58 ["COPY", "register:4000:8", ["const:1127000:8"]]
- 00bb6a64 bytes 802b0090
+ 00bb7a58 bytes 802b0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02dbb77ca07ac5a285b38f95d790957b"></a>

### [`00bb6ac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6ac4.md) → [`00bb7ab8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7ab8.md) _ZN8firebase9messaging29NotifyListenerOnTokenReceivedEPKc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d480.md) · 呼出先 8件 [`00440c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440c7c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md)
- 新版 呼出元 1件 [`00c5e450`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e450.md) · 呼出先 8件 [`00440f9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00440/00440f9c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md) [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 2件, `store_condition` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb7b48",
      "incomplete_value": true,
      "site": "00bb7b48",
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
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb6b54",
      "incomplete_value": true,
      "site": "00bb6b54",
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
            "const:338:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb7b8c",
      "incomplete_value": false,
      "site": "00bb7b8c",
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
            "const:308:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb6b98",
      "incomplete_value": false,
      "site": "00bb6b98",
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
            "const:348:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bb7ae0",
      "incomplete_value": true,
      "site": "00bb7ae0",
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
      "definition_site": "00bb6aec",
      "incomplete_value": true,
      "site": "00bb6aec",
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
      "00bb7ad0",
      "PARAM",
      [
        "storage",
        "01126308",
        null,
        null
      ]
    ],
    [
      "00bb7adc",
      "READ",
      [
        "storage",
        "01126338",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb7b48",
      "WRITE",
      [
        "storage",
        "01126338",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb7ad0",
      "PARAM",
      [
        "storage",
        "011272c8",
        null,
        null
      ]
    ],
    [
      "00bb7adc",
      "READ",
      [
        "storage",
        "011272f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb7b48",
      "WRITE",
      [
        "storage",
        "011272f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb6ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6ac4.md#insn-00bb6ae0) · [`00bb6b54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6ac4.md#insn-00bb6b54) · [`00bb6b98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6ac4.md#insn-00bb6b98)
- 新版 [`00bb7ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7ab8.md#insn-00bb7ad4) · [`00bb7b48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7ab8.md#insn-00bb7b48) · [`00bb7b8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7ab8.md#insn-00bb7b8c)

~~~diff
- 00bb6ae0 ["INT_ADD", "register:40f0:8", ["const:bb6ae0:8", "const:4:8"]]
- 00bb6ae0 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00bb7ad4 ["INT_ADD", "register:40f0:8", ["const:bb7ad4:8", "const:4:8"]]
+ 00bb7ad4 ["CALL", null, ["callee:00c5baa0:8"]]
- 00bb6ae0 bytes fc8f0294
+ 00bb7ad4 bytes f38f0294
- 00bb6b54 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:338:8"]]
- 00bb6b54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bb7b48 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:2f8:8"]]
+ 00bb7b48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb6b54 bytes a09e01f9
+ 00bb7b48 bytes a07e01f9
- 00bb6b98 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00bb6b98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:348:8"]]
- 00bb6b98 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bb7b8c ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 00bb7b8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:308:8"]]
+ 00bb7b8c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bb6b98 bytes 09210d39
+ 00bb7b8c bytes 09210c39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c688b4df1ad877886f76b9de64406cc"></a>

### [`00bb6be4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6be4.md) → [`00bb7bd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7bd8.md) _ZN8firebase9messaging36NotifyListenerOnRegistrationReceivedEPKc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d490.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5b180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b180.md)
- 新版 呼出元 1件 [`00c5e460`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e460.md) · 呼出先 5件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5c150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c150.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 2件, `store_condition` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb7c24",
      "incomplete_value": true,
      "site": "00bb7c24",
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
            "const:300:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb6c30",
      "incomplete_value": true,
      "site": "00bb6c30",
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
            "const:340:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb7c68",
      "incomplete_value": false,
      "site": "00bb7c68",
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
            "const:309:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb6c74",
      "incomplete_value": false,
      "site": "00bb6c74",
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
            "const:349:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bb7c0c",
      "incomplete_value": true,
      "site": "00bb7c0c",
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
      "definition_site": "00bb6c18",
      "incomplete_value": true,
      "site": "00bb6c18",
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
      "00bb7bfc",
      "PARAM",
      [
        "storage",
        "01126308",
        null,
        null
      ]
    ],
    [
      "00bb7c08",
      "READ",
      [
        "storage",
        "01126340",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb7c24",
      "WRITE",
      [
        "storage",
        "01126340",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb7bfc",
      "PARAM",
      [
        "storage",
        "011272c8",
        null,
        null
      ]
    ],
    [
      "00bb7c08",
      "READ",
      [
        "storage",
        "01127300",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb7c24",
      "WRITE",
      [
        "storage",
        "01127300",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb6c0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6be4.md#insn-00bb6c0c) · [`00bb6c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6be4.md#insn-00bb6c30) · [`00bb6c74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6be4.md#insn-00bb6c74)
- 新版 [`00bb7c00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7bd8.md#insn-00bb7c00) · [`00bb7c24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7bd8.md#insn-00bb7c24) · [`00bb7c68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7bd8.md#insn-00bb7c68)

~~~diff
- 00bb6c0c ["INT_ADD", "register:40f0:8", ["const:bb6c0c:8", "const:4:8"]]
- 00bb6c0c ["CALL", null, ["callee:00c5baa0:8"]]
+ 00bb7c00 ["INT_ADD", "register:40f0:8", ["const:bb7c00:8", "const:4:8"]]
+ 00bb7c00 ["CALL", null, ["callee:00c5baa0:8"]]
- 00bb6c0c bytes b18f0294
+ 00bb7c00 bytes a88f0294
- 00bb6c30 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:340:8"]]
- 00bb6c30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bb7c24 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:300:8"]]
+ 00bb7c24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb6c30 bytes a0a201f9
+ 00bb7c24 bytes a08201f9
- 00bb6c74 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00bb6c74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:349:8"]]
- 00bb6c74 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bb7c68 ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 00bb7c68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:309:8"]]
+ 00bb7c68 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bb6c74 bytes 09250d39
+ 00bb7c68 bytes 09250c39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cdeb507647207438825e44d138541e1b"></a>

### [`00bb6cb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6cb4.md) → [`00bb7ca8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7ca8.md) _ZN8firebase9messaging38NotifyListenerOnUnregistrationReceivedEPKc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d4a0.md) · 呼出先 7件 [`00440c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440c7c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md)
- 新版 呼出元 1件 [`00c5e470`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e470.md) · 呼出先 7件 [`00440f9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00440/00440f9c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md) [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb7d44",
      "incomplete_value": true,
      "site": "00bb7d44",
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
            "const:300:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb6d50",
      "incomplete_value": true,
      "site": "00bb6d50",
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
            "const:340:8"
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
      "definition_site": "00bb7d48",
      "incomplete_value": false,
      "site": "00bb7d48",
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
            "const:309:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb6d54",
      "incomplete_value": false,
      "site": "00bb6d54",
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
            "const:349:8"
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
      "definition_site": "00bb7cdc",
      "incomplete_value": true,
      "site": "00bb7cdc",
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
      "definition_site": "00bb6ce8",
      "incomplete_value": true,
      "site": "00bb6ce8",
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
      "00bb7ccc",
      "PARAM",
      [
        "storage",
        "01126308",
        null,
        null
      ]
    ],
    [
      "00bb7cd8",
      "READ",
      [
        "storage",
        "01126340",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb7d44",
      "WRITE",
      [
        "storage",
        "01126340",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb7ccc",
      "PARAM",
      [
        "storage",
        "011272c8",
        null,
        null
      ]
    ],
    [
      "00bb7cd8",
      "READ",
      [
        "storage",
        "01127300",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb7d44",
      "WRITE",
      [
        "storage",
        "01127300",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb6cdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6cb4.md#insn-00bb6cdc) · [`00bb6d50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6cb4.md#insn-00bb6d50) · [`00bb6d54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6cb4.md#insn-00bb6d54)
- 新版 [`00bb7cd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7ca8.md#insn-00bb7cd0) · [`00bb7d44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7ca8.md#insn-00bb7d44) · [`00bb7d48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7ca8.md#insn-00bb7d48)

~~~diff
- 00bb6cdc ["INT_ADD", "register:40f0:8", ["const:bb6cdc:8", "const:4:8"]]
- 00bb6cdc ["CALL", null, ["callee:00c5baa0:8"]]
+ 00bb7cd0 ["INT_ADD", "register:40f0:8", ["const:bb7cd0:8", "const:4:8"]]
+ 00bb7cd0 ["CALL", null, ["callee:00c5baa0:8"]]
- 00bb6cdc bytes 7d8f0294
+ 00bb7cd0 bytes 748f0294
- 00bb6d50 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:340:8"]]
- 00bb6d50 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bb6d50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bb7d44 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:300:8"]]
+ 00bb7d44 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bb7d44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bb6d50 bytes bfa201f9
+ 00bb7d44 bytes bf8201f9
- 00bb6d54 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bb6d54 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bb6d54 ["INT_ADD", "tmp:2:8", ["register:4040:8", "const:349:8"]]
- 00bb6d54 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bb7d48 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bb7d48 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bb7d48 ["INT_ADD", "tmp:2:8", ["register:4040:8", "const:309:8"]]
+ 00bb7d48 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bb6d54 bytes 1f250d39
+ 00bb7d48 bytes 1f250c39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9efa326a7cf01b9a7bb260d1f1aacb14"></a>

### [`00bb6e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6e50.md) → [`00bb7e44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7e44.md) _ZN8firebase9messaging16PollableListenerD2Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ab90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab90.md) [`00c5d450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d450.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5bb60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb60.md) [`00c5e420`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e420.md)

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
      "definition_site": "00bb7e60",
      "incomplete_value": true,
      "site": "00bb7e64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bb6e6c",
      "incomplete_value": true,
      "site": "00bb6e70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00bb7e58",
      "READ",
      [
        "storage",
        "00c9b9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00bb7e64",
      "DATA",
      [
        "storage",
        "00c912f8",
        null,
        "undefined1[64]"
      ]
    ]
  ],
  "added": [
    [
      "00bb7e58",
      "READ",
      [
        "storage",
        "00c9c9a0",
        null,
        "pointer"
      ]
    ],
    [
      "00bb7e64",
      "DATA",
      [
        "storage",
        "00c922c8",
        null,
        "undefined1[64]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb6e5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6e50.md#insn-00bb6e5c) · [`00bb6e64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6e50.md#insn-00bb6e64) · [`00bb6e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6e50.md#insn-00bb6e7c)
- 新版 [`00bb7e50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7e44.md#insn-00bb7e50) · [`00bb7e58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7e44.md#insn-00bb7e58) · [`00bb7e70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7e44.md#insn-00bb7e70)

~~~diff
- 00bb6e5c ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00bb7e50 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00bb6e5c bytes 280700b0
+ 00bb7e50 bytes 280700b0
- 00bb6e64 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 00bb6e64 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb7e58 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9a0:8"]]
+ 00bb7e58 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb6e64 bytes 08e944f9
+ 00bb7e58 bytes 08d144f9
- 00bb6e7c ["INT_ADD", "register:40f0:8", ["const:bb6e7c:8", "const:4:8"]]
- 00bb6e7c ["CALL", null, ["callee:00c5e420:8"]]
+ 00bb7e70 ["INT_ADD", "register:40f0:8", ["const:bb7e70:8", "const:4:8"]]
+ 00bb7e70 ["CALL", null, ["callee:00c5e420:8"]]
- 00bb6e7c bytes 75990294
+ 00bb7e70 bytes 6c990294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18a7844e10995bc963888af73725f5b3"></a>

### [`00bb6f58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6f58.md) → [`00bb7f4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7f4c.md) _ZN8firebase9messaging16PollableListenerD0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ab90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab90.md) [`00c5d450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d450.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5bb60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb60.md) [`00c5e420`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e420.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb7f68",
      "incomplete_value": true,
      "site": "00bb7f6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bb6f74",
      "incomplete_value": true,
      "site": "00bb6f78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00bb7f60",
      "READ",
      [
        "storage",
        "00c9b9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00bb7f6c",
      "DATA",
      [
        "storage",
        "00c912f8",
        null,
        "undefined1[64]"
      ]
    ]
  ],
  "added": [
    [
      "00bb7f60",
      "READ",
      [
        "storage",
        "00c9c9a0",
        null,
        "pointer"
      ]
    ],
    [
      "00bb7f6c",
      "DATA",
      [
        "storage",
        "00c922c8",
        null,
        "undefined1[64]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb6f64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6f58.md#insn-00bb6f64) · [`00bb6f6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6f58.md#insn-00bb6f6c) · [`00bb6f84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6f58.md#insn-00bb6f84)
- 新版 [`00bb7f58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7f4c.md#insn-00bb7f58) · [`00bb7f60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7f4c.md#insn-00bb7f60) · [`00bb7f78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7f4c.md#insn-00bb7f78)

~~~diff
- 00bb6f64 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00bb7f58 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00bb6f64 bytes 280700b0
+ 00bb7f58 bytes 280700b0
- 00bb6f6c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 00bb6f6c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb7f60 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9a0:8"]]
+ 00bb7f60 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb6f6c bytes 08e944f9
+ 00bb7f60 bytes 08d144f9
- 00bb6f84 ["INT_ADD", "register:40f0:8", ["const:bb6f84:8", "const:4:8"]]
- 00bb6f84 ["CALL", null, ["callee:00c5e420:8"]]
+ 00bb7f78 ["INT_ADD", "register:40f0:8", ["const:bb7f78:8", "const:4:8"]]
+ 00bb7f78 ["CALL", null, ["callee:00c5e420:8"]]
- 00bb6f84 bytes 33990294
+ 00bb7f78 bytes 2a990294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9030f3be5ad0066702cadf372d6ebc92"></a>

### [`00bb76e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb76e8.md) → [`00bb86dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb86dc.md) FUN_00bb86dc

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bb67b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb67b4.md) · 呼出先 3件 [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5d4e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d4e0.md) [`00c5d510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d510.md)
- 新版 呼出元 1件 [`00bb77a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb77a8.md) · 呼出先 3件 [`00c5bd40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd40.md) [`00c5e4b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e4b0.md) [`00c5e4e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e4e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb86e8",
      "incomplete_value": false,
      "site": "00bb86ec",
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
            "const:b73:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb76f4",
      "incomplete_value": false,
      "site": "00bb76f8",
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
            "const:b33:8"
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
      "00bb86e8",
      "PARAM",
      [
        "storage",
        "0029fb33",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bb86e8",
      "PARAM",
      [
        "storage",
        "0029fb73",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb76f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb76e8.md#insn-00bb76f8) · [`00bb76f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb76e8.md#insn-00bb76f4) · [`00bb76fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb76e8.md#insn-00bb76fc)
- 新版 [`00bb86ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb86dc.md#insn-00bb86ec) · [`00bb86e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb86dc.md#insn-00bb86e8) · [`00bb86f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb8/00bb86dc.md#insn-00bb86f0)

~~~diff
- 00bb76f8 ["INT_ADD", "register:40f0:8", ["const:bb76f8:8", "const:4:8"]]
- 00bb76f8 ["CALL", null, ["callee:00c5bd40:8"]]
+ 00bb86ec ["INT_ADD", "register:40f0:8", ["const:bb86ec:8", "const:4:8"]]
+ 00bb86ec ["CALL", null, ["callee:00c5bd40:8"]]
- 00bb76f8 bytes 9e8d0294
+ 00bb86ec bytes 958d0294
- 00bb76f4 ["COPY", "tmp:0:8", ["const:b33:8"]]
- 00bb76f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bb76f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bb76f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bb86e8 ["COPY", "tmp:0:8", ["const:b73:8"]]
+ 00bb86e8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb86e8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb86e8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bb76f4 bytes 00cc2c91
+ 00bb86e8 bytes 00cc2d91
- 00bb76fc ["INT_ADD", "register:40f0:8", ["const:bb76fc:8", "const:4:8"]]
- 00bb76fc ["CALL", null, ["callee:00c5e4b0:8"]]
+ 00bb86f0 ["INT_ADD", "register:40f0:8", ["const:bb86f0:8", "const:4:8"]]
+ 00bb86f0 ["CALL", null, ["callee:00c5e4b0:8"]]
- 00bb76fc bytes 79970294
+ 00bb86f0 bytes 70970294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-484c8674e6dddf062b85176d82294417"></a>

### [`00bb8424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8424.md) → [`00bb9418`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9418.md) _ZNSt6__ndk15dequeIN8firebase9messaging7MessageENS_9allocatorIS3_EEE19__add_back_capacityEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5d580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d580.md) · 呼出先 9件 [`00b4035c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b4035c.md) [`00bb8638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8638.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00c5e550`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e550.md) · 呼出先 9件 [`00b41350`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41350.md) [`00bb962c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb962c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.09% / 新版 99.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb95c8",
      "incomplete_value": false,
      "site": "00bb95cc",
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
            "const:777:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb85d4",
      "incomplete_value": false,
      "site": "00bb85d8",
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
            "const:61f:8"
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
      "00bb95c8",
      "PARAM",
      [
        "storage",
        "002a861f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bb95c8",
      "PARAM",
      [
        "storage",
        "002a8777",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb85d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8424.md#insn-00bb85d8) · [`00bb8470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8424.md#insn-00bb8470) · [`00bb84c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8424.md#insn-00bb84c4)
- 新版 [`00bb95cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9418.md#insn-00bb95cc) · [`00bb9464`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9418.md#insn-00bb9464) · [`00bb94b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9418.md#insn-00bb94b8)

~~~diff
- 00bb85d8 ["INT_ADD", "register:40f0:8", ["const:bb85d8:8", "const:4:8"]]
- 00bb85d8 ["CALL", null, ["callee:00b41350:8"]]
+ 00bb95cc ["INT_ADD", "register:40f0:8", ["const:bb95cc:8", "const:4:8"]]
+ 00bb95cc ["CALL", null, ["callee:00b41350:8"]]
- 00bb85d8 bytes 611ffe97
+ 00bb95cc bytes 611ffe97
- 00bb8470 ["INT_ADD", "register:40f0:8", ["const:bb8470:8", "const:4:8"]]
- 00bb8470 ["CALL", null, ["callee:00bb962c:8"]]
+ 00bb9464 ["INT_ADD", "register:40f0:8", ["const:bb9464:8", "const:4:8"]]
+ 00bb9464 ["CALL", null, ["callee:00bb962c:8"]]
- 00bb8470 bytes 72000094
+ 00bb9464 bytes 72000094
- 00bb84c4 ["INT_ADD", "register:40f0:8", ["const:bb84c4:8", "const:4:8"]]
- 00bb84c4 ["CALL", null, ["callee:00c58f30:8"]]
+ 00bb94b8 ["INT_ADD", "register:40f0:8", ["const:bb94b8:8", "const:4:8"]]
+ 00bb94b8 ["CALL", null, ["callee:00c58f30:8"]]
- 00bb84c4 bytes a77e0294
+ 00bb94b8 bytes 9e7e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-537929d3dd26fe362eb85561eaf8e383"></a>

### [`00bb8638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8638.md) → [`00bb962c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb962c.md) FUN_00bb962c

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bb8424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8424.md) · 呼出先 4件 [`00b4035c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b4035c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 1件 [`00bb9418`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9418.md) · 呼出先 4件 [`00b41350`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41350.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.75% / 新版 98.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb9764",
      "incomplete_value": false,
      "site": "00bb9768",
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
            "const:777:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb8770",
      "incomplete_value": false,
      "site": "00bb8774",
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
            "const:61f:8"
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
      "00bb9764",
      "PARAM",
      [
        "storage",
        "002a861f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bb9764",
      "PARAM",
      [
        "storage",
        "002a8777",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8774`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8638.md#insn-00bb8774) · [`00bb86a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8638.md#insn-00bb86a4) · [`00bb86dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8638.md#insn-00bb86dc)
- 新版 [`00bb9768`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb962c.md#insn-00bb9768) · [`00bb9698`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb962c.md#insn-00bb9698) · [`00bb96d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb962c.md#insn-00bb96d0)

~~~diff
- 00bb8774 ["INT_ADD", "register:40f0:8", ["const:bb8774:8", "const:4:8"]]
- 00bb8774 ["CALL", null, ["callee:00b41350:8"]]
+ 00bb9768 ["INT_ADD", "register:40f0:8", ["const:bb9768:8", "const:4:8"]]
+ 00bb9768 ["CALL", null, ["callee:00b41350:8"]]
- 00bb8774 bytes fa1efe97
+ 00bb9768 bytes fa1efe97
- 00bb86a4 ["INT_ADD", "register:40f0:8", ["const:bb86a4:8", "const:4:8"]]
- 00bb86a4 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00bb9698 ["INT_ADD", "register:40f0:8", ["const:bb9698:8", "const:4:8"]]
+ 00bb9698 ["CALL", null, ["callee:00c58fe0:8"]]
- 00bb86a4 bytes 5b7e0294
+ 00bb9698 bytes 527e0294
- 00bb86dc ["INT_ADD", "register:40f0:8", ["const:bb86dc:8", "const:4:8"]]
- 00bb86dc ["CALL", null, ["callee:00c58f30:8"]]
+ 00bb96d0 ["INT_ADD", "register:40f0:8", ["const:bb96d0:8", "const:4:8"]]
+ 00bb96d0 ["CALL", null, ["callee:00c58f30:8"]]
- 00bb86dc bytes 217e0294
+ 00bb96d0 bytes 187e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5a22fdacba5b1ec97f5394e296aa899"></a>

### [`00bb8778`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8778.md) → [`00bb976c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb976c.md) _ZNSt6__ndk114__split_bufferIPN8firebase9messaging7MessageENS_9allocatorIS4_EEE9push_backEOS4_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5d550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d550.md) · 呼出先 4件 [`00b4035c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b4035c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 1件 [`00c5e520`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e520.md) · 呼出先 4件 [`00b41350`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41350.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.75% / 新版 98.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb98a4",
      "incomplete_value": false,
      "site": "00bb98a8",
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
            "const:777:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb88b0",
      "incomplete_value": false,
      "site": "00bb88b4",
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
            "const:61f:8"
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
      "00bb98a4",
      "PARAM",
      [
        "storage",
        "002a861f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bb98a4",
      "PARAM",
      [
        "storage",
        "002a8777",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb88b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8778.md#insn-00bb88b4) · [`00bb87e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8778.md#insn-00bb87e4) · [`00bb881c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8778.md#insn-00bb881c)
- 新版 [`00bb98a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb976c.md#insn-00bb98a8) · [`00bb97d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb976c.md#insn-00bb97d8) · [`00bb9810`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb976c.md#insn-00bb9810)

~~~diff
- 00bb88b4 ["INT_ADD", "register:40f0:8", ["const:bb88b4:8", "const:4:8"]]
- 00bb88b4 ["CALL", null, ["callee:00b41350:8"]]
+ 00bb98a8 ["INT_ADD", "register:40f0:8", ["const:bb98a8:8", "const:4:8"]]
+ 00bb98a8 ["CALL", null, ["callee:00b41350:8"]]
- 00bb88b4 bytes aa1efe97
+ 00bb98a8 bytes aa1efe97
- 00bb87e4 ["INT_ADD", "register:40f0:8", ["const:bb87e4:8", "const:4:8"]]
- 00bb87e4 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00bb97d8 ["INT_ADD", "register:40f0:8", ["const:bb97d8:8", "const:4:8"]]
+ 00bb97d8 ["CALL", null, ["callee:00c58fe0:8"]]
- 00bb87e4 bytes 0b7e0294
+ 00bb97d8 bytes 027e0294
- 00bb881c ["INT_ADD", "register:40f0:8", ["const:bb881c:8", "const:4:8"]]
- 00bb881c ["CALL", null, ["callee:00c58f30:8"]]
+ 00bb9810 ["INT_ADD", "register:40f0:8", ["const:bb9810:8", "const:4:8"]]
+ 00bb9810 ["CALL", null, ["callee:00c58f30:8"]]
- 00bb881c bytes d17d0294
+ 00bb9810 bytes c87d0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e736fc3b7dc20fc93081b31e926d7d89"></a>

### [`00bb88b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb88b8.md) → [`00bb98ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb98ac.md) _ZNSt6__ndk114__split_bufferIPN8firebase9messaging7MessageENS_9allocatorIS4_EEE10push_frontEOS4_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5d540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d540.md) · 呼出先 4件 [`00b4035c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b4035c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 1件 [`00c5e510`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e510.md) · 呼出先 4件 [`00b41350`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41350.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.75% / 新版 98.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb99e4",
      "incomplete_value": false,
      "site": "00bb99e8",
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
            "const:777:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb89f0",
      "incomplete_value": false,
      "site": "00bb89f4",
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
            "const:61f:8"
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
      "00bb99e4",
      "PARAM",
      [
        "storage",
        "002a861f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bb99e4",
      "PARAM",
      [
        "storage",
        "002a8777",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb89f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb88b8.md#insn-00bb89f4) · [`00bb8928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb88b8.md#insn-00bb8928) · [`00bb8960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb88b8.md#insn-00bb8960)
- 新版 [`00bb99e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb98ac.md#insn-00bb99e8) · [`00bb991c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb98ac.md#insn-00bb991c) · [`00bb9954`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb98ac.md#insn-00bb9954)

~~~diff
- 00bb89f4 ["INT_ADD", "register:40f0:8", ["const:bb89f4:8", "const:4:8"]]
- 00bb89f4 ["CALL", null, ["callee:00b41350:8"]]
+ 00bb99e8 ["INT_ADD", "register:40f0:8", ["const:bb99e8:8", "const:4:8"]]
+ 00bb99e8 ["CALL", null, ["callee:00b41350:8"]]
- 00bb89f4 bytes 5a1efe97
+ 00bb99e8 bytes 5a1efe97
- 00bb8928 ["INT_ADD", "register:40f0:8", ["const:bb8928:8", "const:4:8"]]
- 00bb8928 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00bb991c ["INT_ADD", "register:40f0:8", ["const:bb991c:8", "const:4:8"]]
+ 00bb991c ["CALL", null, ["callee:00c58fe0:8"]]
- 00bb8928 bytes ba7d0294
+ 00bb991c bytes b17d0294
- 00bb8960 ["INT_ADD", "register:40f0:8", ["const:bb8960:8", "const:4:8"]]
- 00bb8960 ["CALL", null, ["callee:00c58f30:8"]]
+ 00bb9954 ["INT_ADD", "register:40f0:8", ["const:bb9954:8", "const:4:8"]]
+ 00bb9954 ["CALL", null, ["callee:00c58f30:8"]]
- 00bb8960 bytes 807d0294
+ 00bb9954 bytes 777d0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80f1d3e021c51ff49d44bf525c7b01c6"></a>

### [`00bb89f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb89f8.md) → [`00bb99ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb99ec.md) _ZNSt6__ndk114__split_bufferIPN8firebase9messaging7MessageERNS_9allocatorIS4_EEE9push_backEOS4_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5d570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d570.md) · 呼出先 4件 [`00b4035c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b4035c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 1件 [`00c5e540`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e540.md) · 呼出先 4件 [`00b41350`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41350.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.75% / 新版 98.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb9b24",
      "incomplete_value": false,
      "site": "00bb9b28",
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
            "const:777:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb8b30",
      "incomplete_value": false,
      "site": "00bb8b34",
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
            "const:61f:8"
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
      "00bb9b24",
      "PARAM",
      [
        "storage",
        "002a861f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bb9b24",
      "PARAM",
      [
        "storage",
        "002a8777",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8b34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb89f8.md#insn-00bb8b34) · [`00bb8a64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb89f8.md#insn-00bb8a64) · [`00bb8a9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb89f8.md#insn-00bb8a9c)
- 新版 [`00bb9b28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb99ec.md#insn-00bb9b28) · [`00bb9a58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb99ec.md#insn-00bb9a58) · [`00bb9a90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb99ec.md#insn-00bb9a90)

~~~diff
- 00bb8b34 ["INT_ADD", "register:40f0:8", ["const:bb8b34:8", "const:4:8"]]
- 00bb8b34 ["CALL", null, ["callee:00b41350:8"]]
+ 00bb9b28 ["INT_ADD", "register:40f0:8", ["const:bb9b28:8", "const:4:8"]]
+ 00bb9b28 ["CALL", null, ["callee:00b41350:8"]]
- 00bb8b34 bytes 0a1efe97
+ 00bb9b28 bytes 0a1efe97
- 00bb8a64 ["INT_ADD", "register:40f0:8", ["const:bb8a64:8", "const:4:8"]]
- 00bb8a64 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00bb9a58 ["INT_ADD", "register:40f0:8", ["const:bb9a58:8", "const:4:8"]]
+ 00bb9a58 ["CALL", null, ["callee:00c58fe0:8"]]
- 00bb8a64 bytes 6b7d0294
+ 00bb9a58 bytes 627d0294
- 00bb8a9c ["INT_ADD", "register:40f0:8", ["const:bb8a9c:8", "const:4:8"]]
- 00bb8a9c ["CALL", null, ["callee:00c58f30:8"]]
+ 00bb9a90 ["INT_ADD", "register:40f0:8", ["const:bb9a90:8", "const:4:8"]]
+ 00bb9a90 ["CALL", null, ["callee:00c58f30:8"]]
- 00bb8a9c bytes 317d0294
+ 00bb9a90 bytes 287d0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c0d6e1adc0ac6de63f3353a5a8fbb51"></a>

### [`00bb8b38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8b38.md) → [`00bb9b2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9b2c.md) _ZNSt6__ndk114__split_bufferIPN8firebase9messaging7MessageERNS_9allocatorIS4_EEE10push_frontERKS4_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5d560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d560.md) · 呼出先 4件 [`00b4035c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b40/00b4035c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 1件 [`00c5e530`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e530.md) · 呼出先 4件 [`00b41350`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b41/00b41350.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.75% / 新版 98.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb9c64",
      "incomplete_value": false,
      "site": "00bb9c68",
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
            "const:777:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb8c70",
      "incomplete_value": false,
      "site": "00bb8c74",
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
            "const:61f:8"
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
      "00bb9c64",
      "PARAM",
      [
        "storage",
        "002a861f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bb9c64",
      "PARAM",
      [
        "storage",
        "002a8777",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8c74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8b38.md#insn-00bb8c74) · [`00bb8ba8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8b38.md#insn-00bb8ba8) · [`00bb8be0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8b38.md#insn-00bb8be0)
- 新版 [`00bb9c68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9b2c.md#insn-00bb9c68) · [`00bb9b9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9b2c.md#insn-00bb9b9c) · [`00bb9bd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9b2c.md#insn-00bb9bd4)

~~~diff
- 00bb8c74 ["INT_ADD", "register:40f0:8", ["const:bb8c74:8", "const:4:8"]]
- 00bb8c74 ["CALL", null, ["callee:00b41350:8"]]
+ 00bb9c68 ["INT_ADD", "register:40f0:8", ["const:bb9c68:8", "const:4:8"]]
+ 00bb9c68 ["CALL", null, ["callee:00b41350:8"]]
- 00bb8c74 bytes ba1dfe97
+ 00bb9c68 bytes ba1dfe97
- 00bb8ba8 ["INT_ADD", "register:40f0:8", ["const:bb8ba8:8", "const:4:8"]]
- 00bb8ba8 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00bb9b9c ["INT_ADD", "register:40f0:8", ["const:bb9b9c:8", "const:4:8"]]
+ 00bb9b9c ["CALL", null, ["callee:00c58fe0:8"]]
- 00bb8ba8 bytes 1a7d0294
+ 00bb9b9c bytes 117d0294
- 00bb8be0 ["INT_ADD", "register:40f0:8", ["const:bb8be0:8", "const:4:8"]]
- 00bb8be0 ["CALL", null, ["callee:00c58f30:8"]]
+ 00bb9bd4 ["INT_ADD", "register:40f0:8", ["const:bb9bd4:8", "const:4:8"]]
+ 00bb9bd4 ["CALL", null, ["callee:00c58f30:8"]]
- 00bb8be0 bytes e07c0294
+ 00bb9bd4 bytes d77c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02473a6061bec4da7383cf0afd22271f"></a>

### [`00bb8c78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8c78.md) → [`00bb9c6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9c6c.md) _INIT_285

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00b655ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b655ac.md) [`00bb6740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6740.md) [`00bb6780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb6/00bb6780.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c5ac90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ac90.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00b665a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b665a0.md) [`00bb7734`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7734.md) [`00bb7774`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb7/00bb7774.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c5bc60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bc60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 64.29% / 新版 64.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 4件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb9c98",
      "incomplete_value": false,
      "site": "00bb9c98",
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
            "const:2a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb8ca4",
      "incomplete_value": false,
      "site": "00bb8ca4",
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
            "const:2e8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb9c98",
      "incomplete_value": false,
      "site": "00bb9c98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:30e000:8"
          ],
          [
            "leaf",
            "const:75f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb8ca4",
      "incomplete_value": false,
      "site": "00bb8ca4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:30e000:8"
          ],
          [
            "leaf",
            "const:71f:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb9c98",
      "incomplete_value": false,
      "site": "00bb9c98",
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
                "const:1127000:8"
              ],
              [
                "leaf",
                "const:2a8:8"
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
      "definition_site": "00bb8ca4",
      "incomplete_value": false,
      "site": "00bb8ca4",
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
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:2e8:8"
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
      "00bb9c88",
      "PARAM",
      [
        "storage",
        "011262e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9c98",
      "WRITE",
      [
        "storage",
        "011262e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9c98",
      "DATA",
      [
        "storage",
        "0030e71f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bb9c88",
      "PARAM",
      [
        "storage",
        "011272a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9c98",
      "WRITE",
      [
        "storage",
        "011272a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9c98",
      "DATA",
      [
        "storage",
        "0030e75f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8cb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8c78.md#insn-00bb8cb0) · [`00bb8cc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8c78.md#insn-00bb8cc4) · [`00bb8c84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8c78.md#insn-00bb8c84)
- 新版 [`00bb9ca4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9c6c.md#insn-00bb9ca4) · [`00bb9cb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9c6c.md#insn-00bb9cb8) · [`00bb9c78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9c6c.md#insn-00bb9c78)

~~~diff
- 00bb8cb0 ["INT_ADD", "register:40f0:8", ["const:bb8cb0:8", "const:4:8"]]
- 00bb8cb0 ["CALL", null, ["callee:00c5bc60:8"]]
+ 00bb9ca4 ["INT_ADD", "register:40f0:8", ["const:bb9ca4:8", "const:4:8"]]
+ 00bb9ca4 ["CALL", null, ["callee:00c5bc60:8"]]
- 00bb8cb0 bytes f8870294
+ 00bb9ca4 bytes ef870294
- 00bb8cc4 ["INT_ADD", "register:40f0:8", ["const:bb8cc4:8", "const:4:8"]]
- 00bb8cc4 ["CALL", null, ["callee:00c5bd20:8"]]
+ 00bb9cb8 ["INT_ADD", "register:40f0:8", ["const:bb9cb8:8", "const:4:8"]]
+ 00bb9cb8 ["CALL", null, ["callee:00c5bd20:8"]]
- 00bb8cc4 bytes 23880294
+ 00bb9cb8 bytes 1a880294
- 00bb8c84 ["COPY", "register:4000:8", ["const:1126000:8"]]
+ 00bb9c78 ["COPY", "register:4000:8", ["const:1127000:8"]]
- 00bb8c84 bytes 602b00d0
+ 00bb9c78 bytes 602b00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c607672aebe82579eeb7d01cd2bcf4c"></a>

### [`00bb8cfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8cfc.md) → [`00bb9cf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9cf0.md) _ZN8firebase9messaging18firebase_messaging19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9alloc

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
      "definition_site": "00bb9d1c",
      "incomplete_value": true,
      "site": "00bb9d1c",
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
            "const:368:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb8d28",
      "incomplete_value": true,
      "site": "00bb8d28",
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
            "const:3a8:8"
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
      "definition_site": "00bb9d04",
      "incomplete_value": true,
      "site": "00bb9d04",
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
      "definition_site": "00bb8d10",
      "incomplete_value": true,
      "site": "00bb8d10",
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
      "definition_site": "00bb9d10",
      "incomplete_value": false,
      "site": "00bb9d14",
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
            "const:f28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb8d1c",
      "incomplete_value": false,
      "site": "00bb8d20",
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
            "const:e4a:8"
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
      "00bb9d00",
      "READ",
      [
        "storage",
        "011263a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9d10",
      "PARAM",
      [
        "storage",
        "002bae4a",
        null,
        "string"
      ]
    ],
    [
      "00bb9d1c",
      "WRITE",
      [
        "storage",
        "011263a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb9d00",
      "READ",
      [
        "storage",
        "01127368",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9d10",
      "PARAM",
      [
        "storage",
        "002baf28",
        null,
        "string"
      ]
    ],
    [
      "00bb9d1c",
      "WRITE",
      [
        "storage",
        "01127368",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8d20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8cfc.md#insn-00bb8d20) · [`00bb8d28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8cfc.md#insn-00bb8d28) · [`00bb8d08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8cfc.md#insn-00bb8d08)
- 新版 [`00bb9d14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9cf0.md#insn-00bb9d14) · [`00bb9d1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9cf0.md#insn-00bb9d1c) · [`00bb9cfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9cf0.md#insn-00bb9cfc)

~~~diff
- 00bb8d20 ["INT_ADD", "register:40f0:8", ["const:bb8d20:8", "const:4:8"]]
- 00bb8d20 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00bb9d14 ["INT_ADD", "register:40f0:8", ["const:bb9d14:8", "const:4:8"]]
+ 00bb9d14 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00bb8d20 bytes b0880294
+ 00bb9d14 bytes a7880294
- 00bb8d28 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3a8:8"]]
- 00bb8d28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bb9d1c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:368:8"]]
+ 00bb9d1c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb8d28 bytes 60d601f9
+ 00bb9d1c bytes 60b601f9
- 00bb8d08 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bb9cfc ["COPY", "register:4098:8", ["const:1127000:8"]]
- 00bb8d08 bytes 732b00d0
+ 00bb9cfc bytes 732b00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94427b621fc5353102b2d914dd9a1fa6"></a>

### [`00bb8d3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8d3c.md) → [`00bb9d30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9d30.md) _ZN8firebase9messaging18firebase_messaging19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9alloc

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
      "definition_site": "00bb9d5c",
      "incomplete_value": true,
      "site": "00bb9d5c",
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
            "const:368:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb8d68",
      "incomplete_value": true,
      "site": "00bb8d68",
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
            "const:3a8:8"
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
      "definition_site": "00bb9d44",
      "incomplete_value": true,
      "site": "00bb9d44",
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
      "definition_site": "00bb8d50",
      "incomplete_value": true,
      "site": "00bb8d50",
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
      "definition_site": "00bb9d4c",
      "incomplete_value": false,
      "site": "00bb9d54",
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
            "const:f28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb8d58",
      "incomplete_value": false,
      "site": "00bb8d60",
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
            "const:e4a:8"
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
      "00bb9d40",
      "READ",
      [
        "storage",
        "011263a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9d4c",
      "PARAM",
      [
        "storage",
        "002bae4a",
        null,
        "string"
      ]
    ],
    [
      "00bb9d5c",
      "WRITE",
      [
        "storage",
        "011263a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb9d40",
      "READ",
      [
        "storage",
        "01127368",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9d4c",
      "PARAM",
      [
        "storage",
        "002baf28",
        null,
        "string"
      ]
    ],
    [
      "00bb9d5c",
      "WRITE",
      [
        "storage",
        "01127368",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8d60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8d3c.md#insn-00bb8d60) · [`00bb8d68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8d3c.md#insn-00bb8d68) · [`00bb8d48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8d3c.md#insn-00bb8d48)
- 新版 [`00bb9d54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9d30.md#insn-00bb9d54) · [`00bb9d5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9d30.md#insn-00bb9d5c) · [`00bb9d3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9d30.md#insn-00bb9d3c)

~~~diff
- 00bb8d60 ["INT_ADD", "register:40f0:8", ["const:bb8d60:8", "const:4:8"]]
- 00bb8d60 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00bb9d54 ["INT_ADD", "register:40f0:8", ["const:bb9d54:8", "const:4:8"]]
+ 00bb9d54 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00bb8d60 bytes a0880294
+ 00bb9d54 bytes 97880294
- 00bb8d68 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3a8:8"]]
- 00bb8d68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bb9d5c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:368:8"]]
+ 00bb9d5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb8d68 bytes 60d601f9
+ 00bb9d5c bytes 60b601f9
- 00bb8d48 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bb9d3c ["COPY", "register:4098:8", ["const:1127000:8"]]
- 00bb8d48 bytes 732b00d0
+ 00bb9d3c bytes 732b00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7aafae13b252b9bd4a5cac25039e5bf3"></a>

### [`00bb8d7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8d7c.md) → [`00bb9d70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9d70.md) _ZN8firebase9messaging18firebase_messaging10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bb9da0",
      "incomplete_value": true,
      "site": "00bb9da0",
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
            "const:368:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb8dac",
      "incomplete_value": true,
      "site": "00bb8dac",
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
            "const:3a8:8"
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
      "definition_site": "00bb9d84",
      "incomplete_value": true,
      "site": "00bb9d84",
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
      "definition_site": "00bb8d90",
      "incomplete_value": true,
      "site": "00bb8d90",
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
      "definition_site": "00bb9d90",
      "incomplete_value": false,
      "site": "00bb9d98",
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
            "const:f28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb8d9c",
      "incomplete_value": false,
      "site": "00bb8da4",
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
            "const:e4a:8"
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
      "00bb9d80",
      "READ",
      [
        "storage",
        "011263a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9d90",
      "PARAM",
      [
        "storage",
        "002bae4a",
        null,
        "string"
      ]
    ],
    [
      "00bb9da0",
      "WRITE",
      [
        "storage",
        "011263a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb9d80",
      "READ",
      [
        "storage",
        "01127368",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9d90",
      "PARAM",
      [
        "storage",
        "002baf28",
        null,
        "string"
      ]
    ],
    [
      "00bb9da0",
      "WRITE",
      [
        "storage",
        "01127368",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8da4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8d7c.md#insn-00bb8da4) · [`00bb8dac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8d7c.md#insn-00bb8dac) · [`00bb8d88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8d7c.md#insn-00bb8d88)
- 新版 [`00bb9d98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9d70.md#insn-00bb9d98) · [`00bb9da0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9d70.md#insn-00bb9da0) · [`00bb9d7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9d70.md#insn-00bb9d7c)

~~~diff
- 00bb8da4 ["INT_ADD", "register:40f0:8", ["const:bb8da4:8", "const:4:8"]]
- 00bb8da4 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00bb9d98 ["INT_ADD", "register:40f0:8", ["const:bb9d98:8", "const:4:8"]]
+ 00bb9d98 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00bb8da4 bytes 8f880294
+ 00bb9d98 bytes 86880294
- 00bb8dac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3a8:8"]]
- 00bb8dac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bb9da0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:368:8"]]
+ 00bb9da0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb8dac bytes 60d601f9
+ 00bb9da0 bytes 60b601f9
- 00bb8d88 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bb9d7c ["COPY", "register:4098:8", ["const:1127000:8"]]
- 00bb8d88 bytes 732b00d0
+ 00bb9d7c bytes 732b00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82d5b1d4c4d51ad9f1b15f0f77a194c9"></a>

### [`00bb8dc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8dc0.md) → [`00bb9db4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9db4.md) _ZN8firebase9messaging18firebase_messaging10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bb9de4",
      "incomplete_value": true,
      "site": "00bb9de4",
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
            "const:368:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb8df0",
      "incomplete_value": true,
      "site": "00bb8df0",
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
            "const:3a8:8"
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
      "definition_site": "00bb9dc8",
      "incomplete_value": true,
      "site": "00bb9dc8",
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
      "definition_site": "00bb8dd4",
      "incomplete_value": true,
      "site": "00bb8dd4",
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
      "definition_site": "00bb9dd0",
      "incomplete_value": false,
      "site": "00bb9ddc",
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
            "const:f28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb8ddc",
      "incomplete_value": false,
      "site": "00bb8de8",
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
            "const:e4a:8"
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
      "00bb9dc4",
      "READ",
      [
        "storage",
        "011263a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9dd0",
      "PARAM",
      [
        "storage",
        "002bae4a",
        null,
        "string"
      ]
    ],
    [
      "00bb9de4",
      "WRITE",
      [
        "storage",
        "011263a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb9dc4",
      "READ",
      [
        "storage",
        "01127368",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9dd0",
      "PARAM",
      [
        "storage",
        "002baf28",
        null,
        "string"
      ]
    ],
    [
      "00bb9de4",
      "WRITE",
      [
        "storage",
        "01127368",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8dc0.md#insn-00bb8de8) · [`00bb8df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8dc0.md#insn-00bb8df0) · [`00bb8dcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8dc0.md#insn-00bb8dcc)
- 新版 [`00bb9ddc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9db4.md#insn-00bb9ddc) · [`00bb9de4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9db4.md#insn-00bb9de4) · [`00bb9dc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9db4.md#insn-00bb9dc0)

~~~diff
- 00bb8de8 ["INT_ADD", "register:40f0:8", ["const:bb8de8:8", "const:4:8"]]
- 00bb8de8 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00bb9ddc ["INT_ADD", "register:40f0:8", ["const:bb9ddc:8", "const:4:8"]]
+ 00bb9ddc ["CALL", null, ["callee:00c5bfb0:8"]]
- 00bb8de8 bytes 7e880294
+ 00bb9ddc bytes 75880294
- 00bb8df0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3a8:8"]]
- 00bb8df0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bb9de4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:368:8"]]
+ 00bb9de4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb8df0 bytes 60d601f9
+ 00bb9de4 bytes 60b601f9
- 00bb8dcc ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bb9dc0 ["COPY", "register:4098:8", ["const:1127000:8"]]
- 00bb8dcc bytes 732b00d0
+ 00bb9dc0 bytes 732b00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7490734ed091710936109f4afc255396"></a>

### [`00bb8e10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8e10.md) → [`00bb9e04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9e04.md) _ZN8firebase9messaging18firebase_messaging15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00bb9e5c",
      "incomplete_value": true,
      "site": "00bb9e5c",
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
            "const:370:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb8e68",
      "incomplete_value": true,
      "site": "00bb8e68",
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
            "const:3b0:8"
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
      "definition_site": "00bb9e38",
      "incomplete_value": true,
      "site": "00bb9e44",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:368:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb8e44",
      "incomplete_value": true,
      "site": "00bb8e50",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:3a8:8"
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
      "00bb9e18",
      "READ",
      [
        "storage",
        "011263b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb9e38",
      "READ",
      [
        "storage",
        "011263a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9e5c",
      "WRITE",
      [
        "storage",
        "011263b0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb9e18",
      "READ",
      [
        "storage",
        "01127370",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb9e38",
      "READ",
      [
        "storage",
        "01127368",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9e5c",
      "WRITE",
      [
        "storage",
        "01127370",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8e10.md#insn-00bb8e50) · [`00bb8e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8e10.md#insn-00bb8e68) · [`00bb8e20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8e10.md#insn-00bb8e20)
- 新版 [`00bb9e44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9e04.md#insn-00bb9e44) · [`00bb9e5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9e04.md#insn-00bb9e5c) · [`00bb9e14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9e04.md#insn-00bb9e14)

~~~diff
- 00bb8e50 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb8e50 ["INT_ADD", "register:40f0:8", ["const:bb8e50:8", "const:4:8"]]
- 00bb8e50 ["CALLIND", null, ["register:0:8"]]
+ 00bb9e44 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb9e44 ["INT_ADD", "register:40f0:8", ["const:bb9e44:8", "const:4:8"]]
+ 00bb9e44 ["CALLIND", null, ["register:0:8"]]
- 00bb8e50 bytes 00013fd6
+ 00bb9e44 bytes 00013fd6
- 00bb8e68 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bb8e68 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:3b0:8"]]
- 00bb8e68 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bb9e5c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bb9e5c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:370:8"]]
+ 00bb9e5c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bb8e68 bytes a0c20e39
+ 00bb9e5c bytes a0c20d39
- 00bb8e20 ["COPY", "register:40a8:8", ["const:1126000:8"]]
+ 00bb9e14 ["COPY", "register:40a8:8", ["const:1127000:8"]]
- 00bb8e20 bytes 752b00d0
+ 00bb9e14 bytes 752b00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d867dc63e57383559388fd4896e0978a"></a>

### [`00bb8e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8e7c.md) → [`00bb9e70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9e70.md) _ZN8firebase9messaging18firebase_messaging12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb9eac",
      "incomplete_value": true,
      "site": "00bb9eac",
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
            "const:370:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb8eb8",
      "incomplete_value": true,
      "site": "00bb8eb8",
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
            "const:3b0:8"
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
      "definition_site": "00bb9ecc",
      "incomplete_value": true,
      "site": "00bb9ecc",
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
            "const:368:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb8ed8",
      "incomplete_value": true,
      "site": "00bb8ed8",
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
            "const:3a8:8"
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
      "definition_site": "00bb9e88",
      "incomplete_value": true,
      "site": "00bb9e88",
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
      "definition_site": "00bb8e94",
      "incomplete_value": true,
      "site": "00bb8e94",
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
      "00bb9e84",
      "READ",
      [
        "storage",
        "011263a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9e90",
      "READ",
      [
        "storage",
        "011263b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb9eac",
      "WRITE",
      [
        "storage",
        "011263b0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb9e84",
      "READ",
      [
        "storage",
        "01127368",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9e90",
      "READ",
      [
        "storage",
        "01127370",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb9eac",
      "WRITE",
      [
        "storage",
        "01127370",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8eb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8e7c.md#insn-00bb8eb8) · [`00bb8ed8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8e7c.md#insn-00bb8ed8) · [`00bb8e8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8e7c.md#insn-00bb8e8c)
- 新版 [`00bb9eac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9e70.md#insn-00bb9eac) · [`00bb9ecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9e70.md#insn-00bb9ecc) · [`00bb9e80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9e70.md#insn-00bb9e80)

~~~diff
- 00bb8eb8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bb8eb8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bb8eb8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:3b0:8"]]
- 00bb8eb8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bb9eac ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bb9eac ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bb9eac ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:370:8"]]
+ 00bb9eac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bb8eb8 bytes bfc20e39
+ 00bb9eac bytes bfc20d39
- 00bb8ed8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3a8:8"]]
- 00bb8ed8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bb8ed8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bb9ecc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:368:8"]]
+ 00bb9ecc ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bb9ecc ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bb8ed8 bytes 9fd601f9
+ 00bb9ecc bytes 9fb601f9
- 00bb8e8c ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00bb9e80 ["COPY", "register:40a0:8", ["const:1127000:8"]]
- 00bb8e8c bytes 742b00d0
+ 00bb9e80 bytes 742b00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc758abdfbb0e817169688005616c0ca"></a>

### [`00bb8eec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8eec.md) → [`00bb9ee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9ee0.md) _ZN8firebase9messaging18firebase_messaging14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bb9f20",
      "incomplete_value": true,
      "site": "00bb9f20",
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
            "const:368:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb8f2c",
      "incomplete_value": true,
      "site": "00bb8f2c",
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
            "const:3a8:8"
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
      "definition_site": "00bb9efc",
      "incomplete_value": true,
      "site": "00bb9efc",
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
      "definition_site": "00bb8f08",
      "incomplete_value": true,
      "site": "00bb8f08",
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
      "definition_site": "00bb9f04",
      "incomplete_value": false,
      "site": "00bb9f18",
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
            "const:f28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb8f10",
      "incomplete_value": false,
      "site": "00bb8f24",
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
            "const:e4a:8"
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
      "00bb9ef4",
      "READ",
      [
        "storage",
        "011263a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9f04",
      "PARAM",
      [
        "storage",
        "002bae4a",
        null,
        "string"
      ]
    ],
    [
      "00bb9f20",
      "WRITE",
      [
        "storage",
        "011263a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb9ef4",
      "READ",
      [
        "storage",
        "01127368",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9f04",
      "PARAM",
      [
        "storage",
        "002baf28",
        null,
        "string"
      ]
    ],
    [
      "00bb9f20",
      "WRITE",
      [
        "storage",
        "01127368",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8eec.md#insn-00bb8f24) · [`00bb8f2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8eec.md#insn-00bb8f2c) · [`00bb8ef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8eec.md#insn-00bb8ef8)
- 新版 [`00bb9f18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9ee0.md#insn-00bb9f18) · [`00bb9f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9ee0.md#insn-00bb9f20) · [`00bb9eec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9ee0.md#insn-00bb9eec)

~~~diff
- 00bb8f24 ["INT_ADD", "register:40f0:8", ["const:bb8f24:8", "const:4:8"]]
- 00bb8f24 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00bb9f18 ["INT_ADD", "register:40f0:8", ["const:bb9f18:8", "const:4:8"]]
+ 00bb9f18 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00bb8f24 bytes 2f880294
+ 00bb9f18 bytes 26880294
- 00bb8f2c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3a8:8"]]
- 00bb8f2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bb9f20 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:368:8"]]
+ 00bb9f20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb8f2c bytes 80d601f9
+ 00bb9f20 bytes 80b601f9
- 00bb8ef8 ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00bb9eec ["COPY", "register:40a0:8", ["const:1127000:8"]]
- 00bb8ef8 bytes 742b00d0
+ 00bb9eec bytes 742b00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9aef9d441c979a093fb86d5eb416f0d"></a>

### [`00bb8f5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8f5c.md) → [`00bb9f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9f50.md) _ZN8firebase9messaging18firebase_messaging11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bb9f6c",
      "incomplete_value": false,
      "site": "00bb9f70",
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
      "definition_site": "00bb8f78",
      "incomplete_value": false,
      "site": "00bb8f7c",
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
      "definition_site": "00bb9f7c",
      "incomplete_value": true,
      "site": "00bb9f88",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bb8f88",
      "incomplete_value": true,
      "site": "00bb8f94",
      "value": [
        "LOAD",
        "8",
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
      "00bb9f6c",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00bb9f7c",
      "DATA",
      [
        "storage",
        "011263b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb9f6c",
      "PARAM",
      [
        "storage",
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      "00bb9f7c",
      "DATA",
      [
        "storage",
        "01127378",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8f7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8f5c.md#insn-00bb8f7c) · [`00bb8f78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8f5c.md#insn-00bb8f78) · [`00bb8f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8f5c.md#insn-00bb8f80)
- 新版 [`00bb9f70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9f50.md#insn-00bb9f70) · [`00bb9f6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9f50.md#insn-00bb9f6c) · [`00bb9f74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9f50.md#insn-00bb9f74)

~~~diff
- 00bb8f7c ["INT_ADD", "register:40f0:8", ["const:bb8f7c:8", "const:4:8"]]
- 00bb8f7c ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00bb9f70 ["INT_ADD", "register:40f0:8", ["const:bb9f70:8", "const:4:8"]]
+ 00bb9f70 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00bb8f7c bytes 55880294
+ 00bb9f70 bytes 4c880294
- 00bb8f78 ["COPY", "tmp:0:8", ["const:30b:8"]]
- 00bb8f78 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bb8f78 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bb8f78 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bb9f6c ["COPY", "tmp:0:8", ["const:463:8"]]
+ 00bb9f6c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb9f6c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb9f6c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bb8f78 bytes 002c0c91
+ 00bb9f6c bytes 008c1191
- 00bb8f80 ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00bb9f74 ["COPY", "register:4040:8", ["const:1127000:8"]]
- 00bb8f80 bytes 682b00d0
+ 00bb9f74 bytes 682b00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16d27d88909fd84745728088ffd4ee3c"></a>

### [`00bb8f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8f98.md) → [`00bb9f8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9f8c.md) _ZN8firebase9messaging18firebase_messaging13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bb9fcc",
      "incomplete_value": true,
      "site": "00bb9fcc",
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
            "const:368:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb8fd8",
      "incomplete_value": true,
      "site": "00bb8fd8",
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
            "const:3a8:8"
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
      "definition_site": "00bb9fa8",
      "incomplete_value": true,
      "site": "00bb9fa8",
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
      "definition_site": "00bb8fb4",
      "incomplete_value": true,
      "site": "00bb8fb4",
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
      "definition_site": "00bb9fb0",
      "incomplete_value": false,
      "site": "00bb9fc4",
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
            "const:f28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb8fbc",
      "incomplete_value": false,
      "site": "00bb8fd0",
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
            "const:e4a:8"
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
      "00bb9fa0",
      "READ",
      [
        "storage",
        "011263a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9fb0",
      "PARAM",
      [
        "storage",
        "002bae4a",
        null,
        "string"
      ]
    ],
    [
      "00bb9fcc",
      "WRITE",
      [
        "storage",
        "011263a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bb9fa0",
      "READ",
      [
        "storage",
        "01127368",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9fb0",
      "PARAM",
      [
        "storage",
        "002baf28",
        null,
        "string"
      ]
    ],
    [
      "00bb9fcc",
      "WRITE",
      [
        "storage",
        "01127368",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8f98.md#insn-00bb8fd0) · [`00bb8fd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8f98.md#insn-00bb8fd8) · [`00bb8fa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb8/00bb8f98.md#insn-00bb8fa4)
- 新版 [`00bb9fc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9f8c.md#insn-00bb9fc4) · [`00bb9fcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9f8c.md#insn-00bb9fcc) · [`00bb9f98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9f8c.md#insn-00bb9f98)

~~~diff
- 00bb8fd0 ["INT_ADD", "register:40f0:8", ["const:bb8fd0:8", "const:4:8"]]
- 00bb8fd0 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00bb9fc4 ["INT_ADD", "register:40f0:8", ["const:bb9fc4:8", "const:4:8"]]
+ 00bb9fc4 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00bb8fd0 bytes 04880294
+ 00bb9fc4 bytes fb870294
- 00bb8fd8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3a8:8"]]
- 00bb8fd8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bb9fcc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:368:8"]]
+ 00bb9fcc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb8fd8 bytes 80d601f9
+ 00bb9fcc bytes 80b601f9
- 00bb8fa4 ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00bb9f98 ["COPY", "register:40a0:8", ["const:1127000:8"]]
- 00bb8fa4 bytes 742b00d0
+ 00bb9f98 bytes 742b00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac0dab25e5e40d8845127d9019c30abe"></a>

### [`00bb9008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9008.md) → [`00bb9ffc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9ffc.md) _ZN8firebase9messaging18firebase_messaging10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bba018",
      "incomplete_value": false,
      "site": "00bba01c",
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
      "definition_site": "00bb9024",
      "incomplete_value": false,
      "site": "00bb9028",
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
      "definition_site": "00bba028",
      "incomplete_value": true,
      "site": "00bba034",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bb9034",
      "incomplete_value": true,
      "site": "00bb9040",
      "value": [
        "LOAD",
        "8",
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
      "00bba018",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00bba028",
      "DATA",
      [
        "storage",
        "01126410",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bba018",
      "PARAM",
      [
        "storage",
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      "00bba028",
      "DATA",
      [
        "storage",
        "011273d0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb9028`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9008.md#insn-00bb9028) · [`00bb9024`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9008.md#insn-00bb9024) · [`00bb902c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9008.md#insn-00bb902c)
- 新版 [`00bba01c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9ffc.md#insn-00bba01c) · [`00bba018`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9ffc.md#insn-00bba018) · [`00bba020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9ffc.md#insn-00bba020)

~~~diff
- 00bb9028 ["INT_ADD", "register:40f0:8", ["const:bb9028:8", "const:4:8"]]
- 00bb9028 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00bba01c ["INT_ADD", "register:40f0:8", ["const:bba01c:8", "const:4:8"]]
+ 00bba01c ["CALL", null, ["callee:00c5c0a0:8"]]
- 00bb9028 bytes 2a880294
+ 00bba01c bytes 21880294
- 00bb9024 ["COPY", "tmp:0:8", ["const:54d:8"]]
- 00bb9024 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bb9024 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bb9024 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bba018 ["COPY", "tmp:0:8", ["const:61a:8"]]
+ 00bba018 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bba018 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bba018 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bb9024 bytes 00341591
+ 00bba018 bytes 00681891
- 00bb902c ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00bba020 ["COPY", "register:4040:8", ["const:1127000:8"]]
- 00bb902c bytes 682b00b0
+ 00bba020 bytes 682b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7cf25c7b9e9cfd77d32a9c42c0bc5966"></a>

### [`00bb9044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9044.md) → [`00bba038`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba038.md) _ZN8firebase9messaging27registration_intent_service19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileEN

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
      "definition_site": "00bba064",
      "incomplete_value": true,
      "site": "00bba064",
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
            "const:3d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9070",
      "incomplete_value": true,
      "site": "00bb9070",
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
            "const:418:8"
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
      "definition_site": "00bba04c",
      "incomplete_value": true,
      "site": "00bba04c",
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
      "definition_site": "00bb9058",
      "incomplete_value": true,
      "site": "00bb9058",
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
      "definition_site": "00bba058",
      "incomplete_value": false,
      "site": "00bba05c",
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
            "const:c01:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9064",
      "incomplete_value": false,
      "site": "00bb9068",
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
            "const:b23:8"
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
      "00bba048",
      "READ",
      [
        "storage",
        "01126418",
        null,
        "undefined8"
      ]
    ],
    [
      "00bba058",
      "PARAM",
      [
        "storage",
        "002b9b23",
        null,
        "string"
      ]
    ],
    [
      "00bba064",
      "WRITE",
      [
        "storage",
        "01126418",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bba048",
      "READ",
      [
        "storage",
        "011273d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bba058",
      "PARAM",
      [
        "storage",
        "002b9c01",
        null,
        "string"
      ]
    ],
    [
      "00bba064",
      "WRITE",
      [
        "storage",
        "011273d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb9068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9044.md#insn-00bb9068) · [`00bb9070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9044.md#insn-00bb9070) · [`00bb9050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9044.md#insn-00bb9050)
- 新版 [`00bba05c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba038.md#insn-00bba05c) · [`00bba064`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba038.md#insn-00bba064) · [`00bba044`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba038.md#insn-00bba044)

~~~diff
- 00bb9068 ["INT_ADD", "register:40f0:8", ["const:bb9068:8", "const:4:8"]]
- 00bb9068 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00bba05c ["INT_ADD", "register:40f0:8", ["const:bba05c:8", "const:4:8"]]
+ 00bba05c ["CALL", null, ["callee:00c5bfb0:8"]]
- 00bb9068 bytes de870294
+ 00bba05c bytes d5870294
- 00bb9070 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:418:8"]]
- 00bb9070 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bba064 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3d8:8"]]
+ 00bba064 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb9070 bytes 600e02f9
+ 00bba064 bytes 60ee01f9
- 00bb9050 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bba044 ["COPY", "register:4098:8", ["const:1127000:8"]]
- 00bb9050 bytes 732b00b0
+ 00bba044 bytes 732b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7bc0de3ac44e61da7c48ec4ff236897f"></a>

### [`00bb9084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9084.md) → [`00bba078`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba078.md) _ZN8firebase9messaging27registration_intent_service19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileEN

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
      "definition_site": "00bba0a4",
      "incomplete_value": true,
      "site": "00bba0a4",
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
            "const:3d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb90b0",
      "incomplete_value": true,
      "site": "00bb90b0",
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
            "const:418:8"
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
      "definition_site": "00bba08c",
      "incomplete_value": true,
      "site": "00bba08c",
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
      "definition_site": "00bb9098",
      "incomplete_value": true,
      "site": "00bb9098",
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
      "definition_site": "00bba094",
      "incomplete_value": false,
      "site": "00bba09c",
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
            "const:c01:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb90a0",
      "incomplete_value": false,
      "site": "00bb90a8",
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
            "const:b23:8"
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
      "00bba088",
      "READ",
      [
        "storage",
        "01126418",
        null,
        "undefined8"
      ]
    ],
    [
      "00bba094",
      "PARAM",
      [
        "storage",
        "002b9b23",
        null,
        "string"
      ]
    ],
    [
      "00bba0a4",
      "WRITE",
      [
        "storage",
        "01126418",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bba088",
      "READ",
      [
        "storage",
        "011273d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bba094",
      "PARAM",
      [
        "storage",
        "002b9c01",
        null,
        "string"
      ]
    ],
    [
      "00bba0a4",
      "WRITE",
      [
        "storage",
        "011273d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb90a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9084.md#insn-00bb90a8) · [`00bb90b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9084.md#insn-00bb90b0) · [`00bb9090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9084.md#insn-00bb9090)
- 新版 [`00bba09c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba078.md#insn-00bba09c) · [`00bba0a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba078.md#insn-00bba0a4) · [`00bba084`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba078.md#insn-00bba084)

~~~diff
- 00bb90a8 ["INT_ADD", "register:40f0:8", ["const:bb90a8:8", "const:4:8"]]
- 00bb90a8 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00bba09c ["INT_ADD", "register:40f0:8", ["const:bba09c:8", "const:4:8"]]
+ 00bba09c ["CALL", null, ["callee:00c5bfb0:8"]]
- 00bb90a8 bytes ce870294
+ 00bba09c bytes c5870294
- 00bb90b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:418:8"]]
- 00bb90b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bba0a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3d8:8"]]
+ 00bba0a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb90b0 bytes 600e02f9
+ 00bba0a4 bytes 60ee01f9
- 00bb9090 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bba084 ["COPY", "register:4098:8", ["const:1127000:8"]]
- 00bb9090 bytes 732b00b0
+ 00bba084 bytes 732b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39bed4302d660ca50d52991ae0634869"></a>

### [`00bb90c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb90c4.md) → [`00bba0b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba0b8.md) _ZN8firebase9messaging27registration_intent_service10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bba0e8",
      "incomplete_value": true,
      "site": "00bba0e8",
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
            "const:3d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb90f4",
      "incomplete_value": true,
      "site": "00bb90f4",
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
            "const:418:8"
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
      "definition_site": "00bba0cc",
      "incomplete_value": true,
      "site": "00bba0cc",
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
      "definition_site": "00bb90d8",
      "incomplete_value": true,
      "site": "00bb90d8",
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
        "00bb90d8"
      ],
      [
        "FALL_THROUGH",
        "00bba0cc"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00bba0cc",
      "incomplete_value": true,
      "site": "00bba0e8",
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
      "definition_site": "00bb90d8",
      "incomplete_value": true,
      "site": "00bb90f4",
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
      "00bba0c8",
      "READ",
      [
        "storage",
        "01126418",
        null,
        "undefined8"
      ]
    ],
    [
      "00bba0d8",
      "PARAM",
      [
        "storage",
        "002b9b23",
        null,
        "string"
      ]
    ],
    [
      "00bba0e8",
      "WRITE",
      [
        "storage",
        "01126418",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bba0c8",
      "READ",
      [
        "storage",
        "011273d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bba0d8",
      "PARAM",
      [
        "storage",
        "002b9c01",
        null,
        "string"
      ]
    ],
    [
      "00bba0e8",
      "WRITE",
      [
        "storage",
        "011273d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb90f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb90c4.md#insn-00bb90f4) · [`00bb90d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb90c4.md#insn-00bb90d0) · [`00bb90d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb90c4.md#insn-00bb90d4)
- 新版 [`00bba0e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba0b8.md#insn-00bba0e8) · [`00bba0c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba0b8.md#insn-00bba0c4) · [`00bba0c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba0b8.md#insn-00bba0c8)

~~~diff
- 00bb90f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:418:8"]]
- 00bb90f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bba0e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3d8:8"]]
+ 00bba0e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb90f4 bytes 600e02f9
+ 00bba0e8 bytes 60ee01f9
- 00bb90d0 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bba0c4 ["COPY", "register:4098:8", ["const:1127000:8"]]
- 00bb90d0 bytes 732b00b0
+ 00bba0c4 bytes 732b00b0
- 00bb90d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:418:8"]]
- 00bb90d4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bba0c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3d8:8"]]
+ 00bba0c8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb90d4 bytes 680e42f9
+ 00bba0c8 bytes 68ee41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a07b234913308de84c725493539c6f48"></a>

### [`00bb9108`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9108.md) → [`00bba0fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba0fc.md) _ZN8firebase9messaging27registration_intent_service10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bba12c",
      "incomplete_value": true,
      "site": "00bba12c",
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
            "const:3d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9138",
      "incomplete_value": true,
      "site": "00bb9138",
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
            "const:418:8"
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
      "definition_site": "00bba110",
      "incomplete_value": true,
      "site": "00bba110",
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
      "definition_site": "00bb911c",
      "incomplete_value": true,
      "site": "00bb911c",
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
        "00bb911c"
      ],
      [
        "FALL_THROUGH",
        "00bba110"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00bba110",
      "incomplete_value": true,
      "site": "00bba12c",
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
      "definition_site": "00bb911c",
      "incomplete_value": true,
      "site": "00bb9138",
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
      "00bba10c",
      "READ",
      [
        "storage",
        "01126418",
        null,
        "undefined8"
      ]
    ],
    [
      "00bba118",
      "PARAM",
      [
        "storage",
        "002b9b23",
        null,
        "string"
      ]
    ],
    [
      "00bba12c",
      "WRITE",
      [
        "storage",
        "01126418",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bba10c",
      "READ",
      [
        "storage",
        "011273d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bba118",
      "PARAM",
      [
        "storage",
        "002b9c01",
        null,
        "string"
      ]
    ],
    [
      "00bba12c",
      "WRITE",
      [
        "storage",
        "011273d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb9138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9108.md#insn-00bb9138) · [`00bb9114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9108.md#insn-00bb9114) · [`00bb9118`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9108.md#insn-00bb9118)
- 新版 [`00bba12c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba0fc.md#insn-00bba12c) · [`00bba108`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba0fc.md#insn-00bba108) · [`00bba10c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba0fc.md#insn-00bba10c)

~~~diff
- 00bb9138 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:418:8"]]
- 00bb9138 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bba12c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3d8:8"]]
+ 00bba12c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb9138 bytes 600e02f9
+ 00bba12c bytes 60ee01f9
- 00bb9114 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bba108 ["COPY", "register:4098:8", ["const:1127000:8"]]
- 00bb9114 bytes 732b00b0
+ 00bba108 bytes 732b00b0
- 00bb9118 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:418:8"]]
- 00bb9118 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bba10c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3d8:8"]]
+ 00bba10c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb9118 bytes 680e42f9
+ 00bba10c bytes 68ee41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39ba6ad65de9beaaedf17d73a642b691"></a>

### [`00bb9158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9158.md) → [`00bba14c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba14c.md) _ZN8firebase9messaging27registration_intent_service15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00bba1a4",
      "incomplete_value": true,
      "site": "00bba1a4",
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
            "const:3e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb91b0",
      "incomplete_value": true,
      "site": "00bb91b0",
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
            "const:420:8"
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
      "definition_site": "00bba180",
      "incomplete_value": true,
      "site": "00bba18c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb918c",
      "incomplete_value": true,
      "site": "00bb9198",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:418:8"
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
      "00bba160",
      "READ",
      [
        "storage",
        "01126420",
        null,
        "undefined1"
      ]
    ],
    [
      "00bba180",
      "READ",
      [
        "storage",
        "01126418",
        null,
        "undefined8"
      ]
    ],
    [
      "00bba1a4",
      "WRITE",
      [
        "storage",
        "01126420",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bba160",
      "READ",
      [
        "storage",
        "011273e0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bba180",
      "READ",
      [
        "storage",
        "011273d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bba1a4",
      "WRITE",
      [
        "storage",
        "011273e0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb9198`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9158.md#insn-00bb9198) · [`00bb91b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9158.md#insn-00bb91b0) · [`00bb9168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9158.md#insn-00bb9168)
- 新版 [`00bba18c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba14c.md#insn-00bba18c) · [`00bba1a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba14c.md#insn-00bba1a4) · [`00bba15c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba14c.md#insn-00bba15c)

~~~diff
- 00bb9198 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb9198 ["INT_ADD", "register:40f0:8", ["const:bb9198:8", "const:4:8"]]
- 00bb9198 ["CALLIND", null, ["register:0:8"]]
+ 00bba18c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bba18c ["INT_ADD", "register:40f0:8", ["const:bba18c:8", "const:4:8"]]
+ 00bba18c ["CALLIND", null, ["register:0:8"]]
- 00bb9198 bytes 00013fd6
+ 00bba18c bytes 00013fd6
- 00bb91b0 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bb91b0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:420:8"]]
- 00bb91b0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bba1a4 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bba1a4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:3e0:8"]]
+ 00bba1a4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bb91b0 bytes a0821039
+ 00bba1a4 bytes a0820f39
- 00bb9168 ["COPY", "register:40a8:8", ["const:1126000:8"]]
+ 00bba15c ["COPY", "register:40a8:8", ["const:1127000:8"]]
- 00bb9168 bytes 752b00b0
+ 00bba15c bytes 752b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81f0d37f00346bdd9d21ecc56d1a0126"></a>

### [`00bb91c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb91c4.md) → [`00bba1b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba1b8.md) _ZN8firebase9messaging27registration_intent_service12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00bba1f4",
      "incomplete_value": true,
      "site": "00bba1f4",
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
            "const:3e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9200",
      "incomplete_value": true,
      "site": "00bb9200",
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
            "const:420:8"
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
      "definition_site": "00bba214",
      "incomplete_value": true,
      "site": "00bba214",
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
            "const:3d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9220",
      "incomplete_value": true,
      "site": "00bb9220",
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
            "const:418:8"
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
      "definition_site": "00bba1d0",
      "incomplete_value": true,
      "site": "00bba1d0",
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
      "definition_site": "00bb91dc",
      "incomplete_value": true,
      "site": "00bb91dc",
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
      "00bba1cc",
      "READ",
      [
        "storage",
        "01126418",
        null,
        "undefined8"
      ]
    ],
    [
      "00bba1d8",
      "READ",
      [
        "storage",
        "01126420",
        null,
        "undefined1"
      ]
    ],
    [
      "00bba1f4",
      "WRITE",
      [
        "storage",
        "01126420",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bba1cc",
      "READ",
      [
        "storage",
        "011273d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bba1d8",
      "READ",
      [
        "storage",
        "011273e0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bba1f4",
      "WRITE",
      [
        "storage",
        "011273e0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb9200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb91c4.md#insn-00bb9200) · [`00bb921c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb91c4.md#insn-00bb921c) · [`00bb9220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb91c4.md#insn-00bb9220)
- 新版 [`00bba1f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba1b8.md#insn-00bba1f4) · [`00bba210`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba1b8.md#insn-00bba210) · [`00bba214`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba1b8.md#insn-00bba214)

~~~diff
- 00bb9200 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bb9200 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bb9200 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:420:8"]]
- 00bb9200 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bba1f4 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bba1f4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bba1f4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:3e0:8"]]
+ 00bba1f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bb9200 bytes bf821039
+ 00bba1f4 bytes bf820f39
- 00bb921c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb921c ["INT_ADD", "register:40f0:8", ["const:bb921c:8", "const:4:8"]]
- 00bb921c ["CALLIND", null, ["register:0:8"]]
+ 00bba210 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bba210 ["INT_ADD", "register:40f0:8", ["const:bba210:8", "const:4:8"]]
+ 00bba210 ["CALLIND", null, ["register:0:8"]]
- 00bb921c bytes 00013fd6
+ 00bba210 bytes 00013fd6
- 00bb9220 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:418:8"]]
- 00bb9220 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bb9220 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bba214 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3d8:8"]]
+ 00bba214 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bba214 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bb9220 bytes 9f0e02f9
+ 00bba214 bytes 9fee01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b75030052887e2390e4a22a0ec428e2"></a>

### [`00bb9234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9234.md) → [`00bba228`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba228.md) _ZN8firebase9messaging27registration_intent_service14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bba268",
      "incomplete_value": true,
      "site": "00bba268",
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
            "const:3d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9274",
      "incomplete_value": true,
      "site": "00bb9274",
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
            "const:418:8"
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
      "definition_site": "00bba244",
      "incomplete_value": true,
      "site": "00bba244",
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
      "definition_site": "00bb9250",
      "incomplete_value": true,
      "site": "00bb9250",
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
      "definition_site": "00bba24c",
      "incomplete_value": false,
      "site": "00bba260",
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
            "const:c01:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9258",
      "incomplete_value": false,
      "site": "00bb926c",
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
            "const:b23:8"
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
      "00bba23c",
      "READ",
      [
        "storage",
        "01126418",
        null,
        "undefined8"
      ]
    ],
    [
      "00bba24c",
      "PARAM",
      [
        "storage",
        "002b9b23",
        null,
        "string"
      ]
    ],
    [
      "00bba268",
      "WRITE",
      [
        "storage",
        "01126418",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bba23c",
      "READ",
      [
        "storage",
        "011273d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bba24c",
      "PARAM",
      [
        "storage",
        "002b9c01",
        null,
        "string"
      ]
    ],
    [
      "00bba268",
      "WRITE",
      [
        "storage",
        "011273d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb926c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9234.md#insn-00bb926c) · [`00bb9274`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9234.md#insn-00bb9274) · [`00bb9240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9234.md#insn-00bb9240)
- 新版 [`00bba260`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba228.md#insn-00bba260) · [`00bba268`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba228.md#insn-00bba268) · [`00bba234`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba228.md#insn-00bba234)

~~~diff
- 00bb926c ["INT_ADD", "register:40f0:8", ["const:bb926c:8", "const:4:8"]]
- 00bb926c ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00bba260 ["INT_ADD", "register:40f0:8", ["const:bba260:8", "const:4:8"]]
+ 00bba260 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00bb926c bytes 5d870294
+ 00bba260 bytes 54870294
- 00bb9274 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:418:8"]]
- 00bb9274 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bba268 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3d8:8"]]
+ 00bba268 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb9274 bytes 800e02f9
+ 00bba268 bytes 80ee01f9
- 00bb9240 ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00bba234 ["COPY", "register:40a0:8", ["const:1127000:8"]]
- 00bb9240 bytes 742b00b0
+ 00bba234 bytes 742b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95330337cff53729e9b8cd485d424895"></a>

### [`00bb92a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb92a4.md) → [`00bba298`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba298.md) _ZN8firebase9messaging27registration_intent_service11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bba2c4",
      "incomplete_value": true,
      "site": "00bba2d0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bb92d0",
      "incomplete_value": true,
      "site": "00bb92dc",
      "value": [
        "LOAD",
        "8",
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
      "00bba2b4",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00bba2c4",
      "DATA",
      [
        "storage",
        "01126428",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bba2b4",
      "PARAM",
      [
        "storage",
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      "00bba2c4",
      "DATA",
      [
        "storage",
        "011273e8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb92c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb92a4.md#insn-00bb92c0) · [`00bb92c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb92a4.md#insn-00bb92c4) · [`00bb92c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb92a4.md#insn-00bb92c8)
- 新版 [`00bba2b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba298.md#insn-00bba2b4) · [`00bba2b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba298.md#insn-00bba2b8) · [`00bba2bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba298.md#insn-00bba2bc)

~~~diff
- 00bb92c0 ["COPY", "tmp:0:8", ["const:30b:8"]]
- 00bb92c0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bb92c0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bb92c0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bba2b4 ["COPY", "tmp:0:8", ["const:463:8"]]
+ 00bba2b4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bba2b4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bba2b4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bb92c0 bytes 002c0c91
+ 00bba2b4 bytes 008c1191
- 00bb92c4 ["INT_ADD", "register:40f0:8", ["const:bb92c4:8", "const:4:8"]]
- 00bb92c4 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00bba2b8 ["INT_ADD", "register:40f0:8", ["const:bba2b8:8", "const:4:8"]]
+ 00bba2b8 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00bb92c4 bytes 83870294
+ 00bba2b8 bytes 7a870294
- 00bb92c8 ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00bba2bc ["COPY", "register:4040:8", ["const:1127000:8"]]
- 00bb92c8 bytes 682b00b0
+ 00bba2bc bytes 682b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50e1b300679528441fcaf3486eb42e31"></a>

### [`00bb92e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb92e0.md) → [`00bba2d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba2d4.md) _ZN8firebase9messaging27registration_intent_service13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bba314",
      "incomplete_value": true,
      "site": "00bba314",
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
            "const:3d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9320",
      "incomplete_value": true,
      "site": "00bb9320",
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
            "const:418:8"
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
      "definition_site": "00bba2f0",
      "incomplete_value": true,
      "site": "00bba2f0",
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
      "definition_site": "00bb92fc",
      "incomplete_value": true,
      "site": "00bb92fc",
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
      "definition_site": "00bba2f8",
      "incomplete_value": false,
      "site": "00bba30c",
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
            "const:c01:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9304",
      "incomplete_value": false,
      "site": "00bb9318",
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
            "const:b23:8"
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
      "00bba2e8",
      "READ",
      [
        "storage",
        "01126418",
        null,
        "undefined8"
      ]
    ],
    [
      "00bba2f8",
      "PARAM",
      [
        "storage",
        "002b9b23",
        null,
        "string"
      ]
    ],
    [
      "00bba314",
      "WRITE",
      [
        "storage",
        "01126418",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bba2e8",
      "READ",
      [
        "storage",
        "011273d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bba2f8",
      "PARAM",
      [
        "storage",
        "002b9c01",
        null,
        "string"
      ]
    ],
    [
      "00bba314",
      "WRITE",
      [
        "storage",
        "011273d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb9318`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb92e0.md#insn-00bb9318) · [`00bb9320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb92e0.md#insn-00bb9320) · [`00bb92ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb92e0.md#insn-00bb92ec)
- 新版 [`00bba30c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba2d4.md#insn-00bba30c) · [`00bba314`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba2d4.md#insn-00bba314) · [`00bba2e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba2d4.md#insn-00bba2e0)

~~~diff
- 00bb9318 ["INT_ADD", "register:40f0:8", ["const:bb9318:8", "const:4:8"]]
- 00bb9318 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00bba30c ["INT_ADD", "register:40f0:8", ["const:bba30c:8", "const:4:8"]]
+ 00bba30c ["CALL", null, ["callee:00c5bfb0:8"]]
- 00bb9318 bytes 32870294
+ 00bba30c bytes 29870294
- 00bb9320 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:418:8"]]
- 00bb9320 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bba314 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3d8:8"]]
+ 00bba314 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb9320 bytes 800e02f9
+ 00bba314 bytes 80ee01f9
- 00bb92ec ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00bba2e0 ["COPY", "register:40a0:8", ["const:1127000:8"]]
- 00bb92ec bytes 742b00b0
+ 00bba2e0 bytes 742b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef5e1b2a84eb4208028cd91f185fe532"></a>

### [`00bb9350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9350.md) → [`00bba344`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba344.md) _ZN8firebase9messaging27registration_intent_service10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bba360",
      "incomplete_value": false,
      "site": "00bba364",
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
      "definition_site": "00bb936c",
      "incomplete_value": false,
      "site": "00bb9370",
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
      "definition_site": "00bba370",
      "incomplete_value": true,
      "site": "00bba37c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bb937c",
      "incomplete_value": true,
      "site": "00bb9388",
      "value": [
        "LOAD",
        "8",
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
      "00bba360",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00bba370",
      "DATA",
      [
        "storage",
        "01126430",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bba360",
      "PARAM",
      [
        "storage",
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      "00bba370",
      "DATA",
      [
        "storage",
        "011273f0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb9370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9350.md#insn-00bb9370) · [`00bb936c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9350.md#insn-00bb936c) · [`00bb9374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9350.md#insn-00bb9374)
- 新版 [`00bba364`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba344.md#insn-00bba364) · [`00bba360`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba344.md#insn-00bba360) · [`00bba368`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba344.md#insn-00bba368)

~~~diff
- 00bb9370 ["INT_ADD", "register:40f0:8", ["const:bb9370:8", "const:4:8"]]
- 00bb9370 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00bba364 ["INT_ADD", "register:40f0:8", ["const:bba364:8", "const:4:8"]]
+ 00bba364 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00bb9370 bytes 58870294
+ 00bba364 bytes 4f870294
- 00bb936c ["COPY", "tmp:0:8", ["const:54d:8"]]
- 00bb936c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bb936c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bb936c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bba360 ["COPY", "tmp:0:8", ["const:61a:8"]]
+ 00bba360 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bba360 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bba360 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bb936c bytes 00341591
+ 00bba360 bytes 00681891
- 00bb9374 ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00bba368 ["COPY", "register:4040:8", ["const:1127000:8"]]
- 00bb9374 bytes 682b00b0
+ 00bba368 bytes 682b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d65d708d0c967e26a83fbf01c8fc1f7b"></a>

### [`00bb938c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb938c.md) → [`00bba380`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba380.md) _ZN8firebase9messaging26illegal_argument_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS

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
      "definition_site": "00bba3ac",
      "incomplete_value": true,
      "site": "00bba3ac",
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
            "const:3f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb93b8",
      "incomplete_value": true,
      "site": "00bb93b8",
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
            "const:438:8"
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
      "definition_site": "00bba394",
      "incomplete_value": true,
      "site": "00bba394",
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
      "definition_site": "00bb93a0",
      "incomplete_value": true,
      "site": "00bb93a0",
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
      "definition_site": "00bba3a0",
      "incomplete_value": false,
      "site": "00bba3a4",
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
            "const:f83:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb93ac",
      "incomplete_value": false,
      "site": "00bb93b0",
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
            "const:eb8:8"
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
      "00bba390",
      "READ",
      [
        "storage",
        "01126438",
        null,
        "undefined8"
      ]
    ],
    [
      "00bba3a0",
      "PARAM",
      [
        "storage",
        "002a4eb8",
        null,
        "string"
      ]
    ],
    [
      "00bba3ac",
      "WRITE",
      [
        "storage",
        "01126438",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bba390",
      "READ",
      [
        "storage",
        "011273f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bba3a0",
      "PARAM",
      [
        "storage",
        "002a4f83",
        null,
        "string"
      ]
    ],
    [
      "00bba3ac",
      "WRITE",
      [
        "storage",
        "011273f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb93b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb938c.md#insn-00bb93b0) · [`00bb93b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb938c.md#insn-00bb93b8) · [`00bb9398`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb938c.md#insn-00bb9398)
- 新版 [`00bba3a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba380.md#insn-00bba3a4) · [`00bba3ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba380.md#insn-00bba3ac) · [`00bba38c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba380.md#insn-00bba38c)

~~~diff
- 00bb93b0 ["INT_ADD", "register:40f0:8", ["const:bb93b0:8", "const:4:8"]]
- 00bb93b0 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00bba3a4 ["INT_ADD", "register:40f0:8", ["const:bba3a4:8", "const:4:8"]]
+ 00bba3a4 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00bb93b0 bytes 0c870294
+ 00bba3a4 bytes 03870294
- 00bb93b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:438:8"]]
- 00bb93b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bba3ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3f8:8"]]
+ 00bba3ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb93b8 bytes 601e02f9
+ 00bba3ac bytes 60fe01f9
- 00bb9398 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bba38c ["COPY", "register:4098:8", ["const:1127000:8"]]
- 00bb9398 bytes 732b00b0
+ 00bba38c bytes 732b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a17a3f5c28f727c81f6b05cce93ff031"></a>

### [`00bb93cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb93cc.md) → [`00bba3c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba3c0.md) _ZN8firebase9messaging26illegal_argument_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS

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
      "definition_site": "00bba3ec",
      "incomplete_value": true,
      "site": "00bba3ec",
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
            "const:3f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb93f8",
      "incomplete_value": true,
      "site": "00bb93f8",
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
            "const:438:8"
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
      "definition_site": "00bba3d4",
      "incomplete_value": true,
      "site": "00bba3d4",
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
      "definition_site": "00bb93e0",
      "incomplete_value": true,
      "site": "00bb93e0",
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
      "definition_site": "00bba3dc",
      "incomplete_value": false,
      "site": "00bba3e4",
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
            "const:f83:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb93e8",
      "incomplete_value": false,
      "site": "00bb93f0",
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
            "const:eb8:8"
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
      "00bba3d0",
      "READ",
      [
        "storage",
        "01126438",
        null,
        "undefined8"
      ]
    ],
    [
      "00bba3dc",
      "PARAM",
      [
        "storage",
        "002a4eb8",
        null,
        "string"
      ]
    ],
    [
      "00bba3ec",
      "WRITE",
      [
        "storage",
        "01126438",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bba3d0",
      "READ",
      [
        "storage",
        "011273f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bba3dc",
      "PARAM",
      [
        "storage",
        "002a4f83",
        null,
        "string"
      ]
    ],
    [
      "00bba3ec",
      "WRITE",
      [
        "storage",
        "011273f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb93f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb93cc.md#insn-00bb93f0) · [`00bb93f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb93cc.md#insn-00bb93f8) · [`00bb93d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb93cc.md#insn-00bb93d8)
- 新版 [`00bba3e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba3c0.md#insn-00bba3e4) · [`00bba3ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba3c0.md#insn-00bba3ec) · [`00bba3cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba3c0.md#insn-00bba3cc)

~~~diff
- 00bb93f0 ["INT_ADD", "register:40f0:8", ["const:bb93f0:8", "const:4:8"]]
- 00bb93f0 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00bba3e4 ["INT_ADD", "register:40f0:8", ["const:bba3e4:8", "const:4:8"]]
+ 00bba3e4 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00bb93f0 bytes fc860294
+ 00bba3e4 bytes f3860294
- 00bb93f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:438:8"]]
- 00bb93f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bba3ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3f8:8"]]
+ 00bba3ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb93f8 bytes 601e02f9
+ 00bba3ec bytes 60fe01f9
- 00bb93d8 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bba3cc ["COPY", "register:4098:8", ["const:1127000:8"]]
- 00bb93d8 bytes 732b00b0
+ 00bba3cc bytes 732b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f492f03942621b10a47afd67a62ca70d"></a>

### [`00bb940c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb940c.md) → [`00bba400`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba400.md) _ZN8firebase9messaging26illegal_argument_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00bba430",
      "incomplete_value": true,
      "site": "00bba430",
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
            "const:3f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb943c",
      "incomplete_value": true,
      "site": "00bb943c",
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
            "const:438:8"
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
      "definition_site": "00bba414",
      "incomplete_value": true,
      "site": "00bba414",
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
      "definition_site": "00bb9420",
      "incomplete_value": true,
      "site": "00bb9420",
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
      "definition_site": "00bba420",
      "incomplete_value": false,
      "site": "00bba428",
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
            "const:f83:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb942c",
      "incomplete_value": false,
      "site": "00bb9434",
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
            "const:eb8:8"
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
      "00bba410",
      "READ",
      [
        "storage",
        "01126438",
        null,
        "undefined8"
      ]
    ],
    [
      "00bba420",
      "PARAM",
      [
        "storage",
        "002a4eb8",
        null,
        "string"
      ]
    ],
    [
      "00bba430",
      "WRITE",
      [
        "storage",
        "01126438",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bba410",
      "READ",
      [
        "storage",
        "011273f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bba420",
      "PARAM",
      [
        "storage",
        "002a4f83",
        null,
        "string"
      ]
    ],
    [
      "00bba430",
      "WRITE",
      [
        "storage",
        "011273f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb9434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb940c.md#insn-00bb9434) · [`00bb943c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb940c.md#insn-00bb943c) · [`00bb9418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb940c.md#insn-00bb9418)
- 新版 [`00bba428`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba400.md#insn-00bba428) · [`00bba430`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba400.md#insn-00bba430) · [`00bba40c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba400.md#insn-00bba40c)

~~~diff
- 00bb9434 ["INT_ADD", "register:40f0:8", ["const:bb9434:8", "const:4:8"]]
- 00bb9434 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00bba428 ["INT_ADD", "register:40f0:8", ["const:bba428:8", "const:4:8"]]
+ 00bba428 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00bb9434 bytes eb860294
+ 00bba428 bytes e2860294
- 00bb943c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:438:8"]]
- 00bb943c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bba430 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3f8:8"]]
+ 00bba430 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb943c bytes 601e02f9
+ 00bba430 bytes 60fe01f9
- 00bb9418 ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bba40c ["COPY", "register:4098:8", ["const:1127000:8"]]
- 00bb9418 bytes 732b00b0
+ 00bba40c bytes 732b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50a9b81b034e94f544cd4179beb22a1a"></a>

### [`00bb9450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9450.md) → [`00bba444`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba444.md) _ZN8firebase9messaging26illegal_argument_exception10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00bba474",
      "incomplete_value": true,
      "site": "00bba474",
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
            "const:3f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9480",
      "incomplete_value": true,
      "site": "00bb9480",
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
            "const:438:8"
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
      "definition_site": "00bba458",
      "incomplete_value": true,
      "site": "00bba458",
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
      "definition_site": "00bb9464",
      "incomplete_value": true,
      "site": "00bb9464",
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
      "definition_site": "00bba460",
      "incomplete_value": false,
      "site": "00bba46c",
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
            "const:f83:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb946c",
      "incomplete_value": false,
      "site": "00bb9478",
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
            "const:eb8:8"
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
      "00bba454",
      "READ",
      [
        "storage",
        "01126438",
        null,
        "undefined8"
      ]
    ],
    [
      "00bba460",
      "PARAM",
      [
        "storage",
        "002a4eb8",
        null,
        "string"
      ]
    ],
    [
      "00bba474",
      "WRITE",
      [
        "storage",
        "01126438",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bba454",
      "READ",
      [
        "storage",
        "011273f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bba460",
      "PARAM",
      [
        "storage",
        "002a4f83",
        null,
        "string"
      ]
    ],
    [
      "00bba474",
      "WRITE",
      [
        "storage",
        "011273f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb9478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9450.md#insn-00bb9478) · [`00bb9480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9450.md#insn-00bb9480) · [`00bb945c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9450.md#insn-00bb945c)
- 新版 [`00bba46c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba444.md#insn-00bba46c) · [`00bba474`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba444.md#insn-00bba474) · [`00bba450`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba444.md#insn-00bba450)

~~~diff
- 00bb9478 ["INT_ADD", "register:40f0:8", ["const:bb9478:8", "const:4:8"]]
- 00bb9478 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00bba46c ["INT_ADD", "register:40f0:8", ["const:bba46c:8", "const:4:8"]]
+ 00bba46c ["CALL", null, ["callee:00c5bfb0:8"]]
- 00bb9478 bytes da860294
+ 00bba46c bytes d1860294
- 00bb9480 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:438:8"]]
- 00bb9480 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bba474 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3f8:8"]]
+ 00bba474 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb9480 bytes 601e02f9
+ 00bba474 bytes 60fe01f9
- 00bb945c ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bba450 ["COPY", "register:4098:8", ["const:1127000:8"]]
- 00bb945c bytes 732b00b0
+ 00bba450 bytes 732b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37fe75946a1ba0e7076cba1f0458cf9c"></a>

### [`00bb94a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb94a0.md) → [`00bba494`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba494.md) _ZN8firebase9messaging26illegal_argument_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00bba4ec",
      "incomplete_value": true,
      "site": "00bba4ec",
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
            "const:400:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb94f8",
      "incomplete_value": true,
      "site": "00bb94f8",
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
            "const:440:8"
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
      "definition_site": "00bba4c8",
      "incomplete_value": true,
      "site": "00bba4d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb94d4",
      "incomplete_value": true,
      "site": "00bb94e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:438:8"
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
      "00bba4a8",
      "READ",
      [
        "storage",
        "01126440",
        null,
        "undefined1"
      ]
    ],
    [
      "00bba4c8",
      "READ",
      [
        "storage",
        "01126438",
        null,
        "undefined8"
      ]
    ],
    [
      "00bba4ec",
      "WRITE",
      [
        "storage",
        "01126440",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bba4a8",
      "READ",
      [
        "storage",
        "01127400",
        null,
        "undefined1"
      ]
    ],
    [
      "00bba4c8",
      "READ",
      [
        "storage",
        "011273f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bba4ec",
      "WRITE",
      [
        "storage",
        "01127400",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb94e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb94a0.md#insn-00bb94e0) · [`00bb94f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb94a0.md#insn-00bb94f8) · [`00bb94b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb94a0.md#insn-00bb94b0)
- 新版 [`00bba4d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba494.md#insn-00bba4d4) · [`00bba4ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba494.md#insn-00bba4ec) · [`00bba4a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba494.md#insn-00bba4a4)

~~~diff
- 00bb94e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb94e0 ["INT_ADD", "register:40f0:8", ["const:bb94e0:8", "const:4:8"]]
- 00bb94e0 ["CALLIND", null, ["register:0:8"]]
+ 00bba4d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bba4d4 ["INT_ADD", "register:40f0:8", ["const:bba4d4:8", "const:4:8"]]
+ 00bba4d4 ["CALLIND", null, ["register:0:8"]]
- 00bb94e0 bytes 00013fd6
+ 00bba4d4 bytes 00013fd6
- 00bb94f8 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00bb94f8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:440:8"]]
- 00bb94f8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bba4ec ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bba4ec ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:400:8"]]
+ 00bba4ec ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bb94f8 bytes a0021139
+ 00bba4ec bytes a0021039
- 00bb94b0 ["COPY", "register:40a8:8", ["const:1126000:8"]]
+ 00bba4a4 ["COPY", "register:40a8:8", ["const:1127000:8"]]
- 00bb94b0 bytes 752b00b0
+ 00bba4a4 bytes 752b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a49147676d446eb9e1b867eec6d2845"></a>

### [`00bb950c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb950c.md) → [`00bba500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba500.md) _ZN8firebase9messaging26illegal_argument_exception12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00bba53c",
      "incomplete_value": true,
      "site": "00bba53c",
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
            "const:400:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9548",
      "incomplete_value": true,
      "site": "00bb9548",
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
            "const:440:8"
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
      "definition_site": "00bba55c",
      "incomplete_value": true,
      "site": "00bba55c",
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
            "const:3f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9568",
      "incomplete_value": true,
      "site": "00bb9568",
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
            "const:438:8"
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
      "definition_site": "00bba518",
      "incomplete_value": true,
      "site": "00bba518",
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
      "definition_site": "00bb9524",
      "incomplete_value": true,
      "site": "00bb9524",
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
      "00bba514",
      "READ",
      [
        "storage",
        "01126438",
        null,
        "undefined8"
      ]
    ],
    [
      "00bba520",
      "READ",
      [
        "storage",
        "01126440",
        null,
        "undefined1"
      ]
    ],
    [
      "00bba53c",
      "WRITE",
      [
        "storage",
        "01126440",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bba514",
      "READ",
      [
        "storage",
        "011273f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bba520",
      "READ",
      [
        "storage",
        "01127400",
        null,
        "undefined1"
      ]
    ],
    [
      "00bba53c",
      "WRITE",
      [
        "storage",
        "01127400",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb9548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb950c.md#insn-00bb9548) · [`00bb9564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb950c.md#insn-00bb9564) · [`00bb9568`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb950c.md#insn-00bb9568)
- 新版 [`00bba53c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba500.md#insn-00bba53c) · [`00bba558`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba500.md#insn-00bba558) · [`00bba55c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba500.md#insn-00bba55c)

~~~diff
- 00bb9548 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bb9548 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bb9548 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:440:8"]]
- 00bb9548 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bba53c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bba53c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bba53c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:400:8"]]
+ 00bba53c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bb9548 bytes bf021139
+ 00bba53c bytes bf021039
- 00bb9564 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb9564 ["INT_ADD", "register:40f0:8", ["const:bb9564:8", "const:4:8"]]
- 00bb9564 ["CALLIND", null, ["register:0:8"]]
+ 00bba558 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bba558 ["INT_ADD", "register:40f0:8", ["const:bba558:8", "const:4:8"]]
+ 00bba558 ["CALLIND", null, ["register:0:8"]]
- 00bb9564 bytes 00013fd6
+ 00bba558 bytes 00013fd6
- 00bb9568 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:438:8"]]
- 00bb9568 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bb9568 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bba55c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3f8:8"]]
+ 00bba55c ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bba55c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bb9568 bytes 9f1e02f9
+ 00bba55c bytes 9ffe01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50b8ea3fc2a9cd7db46af5fa464832f3"></a>

### [`00bb957c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb957c.md) → [`00bba570`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba570.md) _ZN8firebase9messaging26illegal_argument_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bba5b0",
      "incomplete_value": true,
      "site": "00bba5b0",
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
            "const:3f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb95bc",
      "incomplete_value": true,
      "site": "00bb95bc",
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
            "const:438:8"
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
      "definition_site": "00bba58c",
      "incomplete_value": true,
      "site": "00bba58c",
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
      "definition_site": "00bb9598",
      "incomplete_value": true,
      "site": "00bb9598",
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
      "definition_site": "00bba594",
      "incomplete_value": false,
      "site": "00bba5a8",
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
            "const:f83:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb95a0",
      "incomplete_value": false,
      "site": "00bb95b4",
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
            "const:eb8:8"
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
      "00bba584",
      "READ",
      [
        "storage",
        "01126438",
        null,
        "undefined8"
      ]
    ],
    [
      "00bba594",
      "PARAM",
      [
        "storage",
        "002a4eb8",
        null,
        "string"
      ]
    ],
    [
      "00bba5b0",
      "WRITE",
      [
        "storage",
        "01126438",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bba584",
      "READ",
      [
        "storage",
        "011273f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bba594",
      "PARAM",
      [
        "storage",
        "002a4f83",
        null,
        "string"
      ]
    ],
    [
      "00bba5b0",
      "WRITE",
      [
        "storage",
        "011273f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb95b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb957c.md#insn-00bb95b4) · [`00bb95bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb957c.md#insn-00bb95bc) · [`00bb9588`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb957c.md#insn-00bb9588)
- 新版 [`00bba5a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba570.md#insn-00bba5a8) · [`00bba5b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba570.md#insn-00bba5b0) · [`00bba57c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba570.md#insn-00bba57c)

~~~diff
- 00bb95b4 ["INT_ADD", "register:40f0:8", ["const:bb95b4:8", "const:4:8"]]
- 00bb95b4 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00bba5a8 ["INT_ADD", "register:40f0:8", ["const:bba5a8:8", "const:4:8"]]
+ 00bba5a8 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00bb95b4 bytes 8b860294
+ 00bba5a8 bytes 82860294
- 00bb95bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:438:8"]]
- 00bb95bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bba5b0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3f8:8"]]
+ 00bba5b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb95bc bytes 801e02f9
+ 00bba5b0 bytes 80fe01f9
- 00bb9588 ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00bba57c ["COPY", "register:40a0:8", ["const:1127000:8"]]
- 00bb9588 bytes 742b00b0
+ 00bba57c bytes 742b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb9c9cdd777478b137c1749883887c43"></a>

### [`00bb95ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb95ec.md) → [`00bba5e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba5e0.md) _ZN8firebase9messaging26illegal_argument_exception11GetMethodIdENS1_6MethodE

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
      "definition_site": "00bba5fc",
      "incomplete_value": false,
      "site": "00bba600",
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
      "definition_site": "00bb9608",
      "incomplete_value": false,
      "site": "00bb960c",
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
      "definition_site": "00bba60c",
      "incomplete_value": true,
      "site": "00bba618",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bb9618",
      "incomplete_value": true,
      "site": "00bb9624",
      "value": [
        "LOAD",
        "8",
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
      "00bba5fc",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00bba60c",
      "DATA",
      [
        "storage",
        "01126448",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bba5fc",
      "PARAM",
      [
        "storage",
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      "00bba60c",
      "DATA",
      [
        "storage",
        "01127408",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb960c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb95ec.md#insn-00bb960c) · [`00bb9608`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb95ec.md#insn-00bb9608) · [`00bb9610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb95ec.md#insn-00bb9610)
- 新版 [`00bba600`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba5e0.md#insn-00bba600) · [`00bba5fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba5e0.md#insn-00bba5fc) · [`00bba604`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba5e0.md#insn-00bba604)

~~~diff
- 00bb960c ["INT_ADD", "register:40f0:8", ["const:bb960c:8", "const:4:8"]]
- 00bb960c ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00bba600 ["INT_ADD", "register:40f0:8", ["const:bba600:8", "const:4:8"]]
+ 00bba600 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00bb960c bytes b1860294
+ 00bba600 bytes a8860294
- 00bb9608 ["COPY", "tmp:0:8", ["const:30b:8"]]
- 00bb9608 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bb9608 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bb9608 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bba5fc ["COPY", "tmp:0:8", ["const:463:8"]]
+ 00bba5fc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bba5fc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bba5fc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bb9608 bytes 002c0c91
+ 00bba5fc bytes 008c1191
- 00bb9610 ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00bba604 ["COPY", "register:4040:8", ["const:1127000:8"]]
- 00bb9610 bytes 682b00b0
+ 00bba604 bytes 682b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6cbcd3cee54d1f723d911d0fd538942"></a>

### [`00bb9628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9628.md) → [`00bba61c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba61c.md) _ZN8firebase9messaging26illegal_argument_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00bba65c",
      "incomplete_value": true,
      "site": "00bba65c",
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
            "const:3f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9668",
      "incomplete_value": true,
      "site": "00bb9668",
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
            "const:438:8"
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
      "definition_site": "00bba638",
      "incomplete_value": true,
      "site": "00bba638",
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
      "definition_site": "00bb9644",
      "incomplete_value": true,
      "site": "00bb9644",
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
      "definition_site": "00bba640",
      "incomplete_value": false,
      "site": "00bba654",
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
            "const:f83:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb964c",
      "incomplete_value": false,
      "site": "00bb9660",
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
            "const:eb8:8"
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
      "00bba630",
      "READ",
      [
        "storage",
        "01126438",
        null,
        "undefined8"
      ]
    ],
    [
      "00bba640",
      "PARAM",
      [
        "storage",
        "002a4eb8",
        null,
        "string"
      ]
    ],
    [
      "00bba65c",
      "WRITE",
      [
        "storage",
        "01126438",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bba630",
      "READ",
      [
        "storage",
        "011273f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bba640",
      "PARAM",
      [
        "storage",
        "002a4f83",
        null,
        "string"
      ]
    ],
    [
      "00bba65c",
      "WRITE",
      [
        "storage",
        "011273f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb9660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9628.md#insn-00bb9660) · [`00bb9668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9628.md#insn-00bb9668) · [`00bb9634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9628.md#insn-00bb9634)
- 新版 [`00bba654`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba61c.md#insn-00bba654) · [`00bba65c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba61c.md#insn-00bba65c) · [`00bba628`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba61c.md#insn-00bba628)

~~~diff
- 00bb9660 ["INT_ADD", "register:40f0:8", ["const:bb9660:8", "const:4:8"]]
- 00bb9660 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00bba654 ["INT_ADD", "register:40f0:8", ["const:bba654:8", "const:4:8"]]
+ 00bba654 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00bb9660 bytes 60860294
+ 00bba654 bytes 57860294
- 00bb9668 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:438:8"]]
- 00bb9668 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bba65c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3f8:8"]]
+ 00bba65c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb9668 bytes 801e02f9
+ 00bba65c bytes 80fe01f9
- 00bb9634 ["COPY", "register:40a0:8", ["const:1126000:8"]]
+ 00bba628 ["COPY", "register:40a0:8", ["const:1127000:8"]]
- 00bb9634 bytes 742b00b0
+ 00bba628 bytes 742b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d62178946dbfcca83ed9184b5efb3c7"></a>

### [`00bb9698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9698.md) → [`00bba68c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba68c.md) _ZN8firebase9messaging26illegal_argument_exception10GetFieldIdENS1_5FieldE

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
      "definition_site": "00bba6a8",
      "incomplete_value": false,
      "site": "00bba6ac",
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
      "definition_site": "00bb96b4",
      "incomplete_value": false,
      "site": "00bb96b8",
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
      "definition_site": "00bba6b8",
      "incomplete_value": true,
      "site": "00bba6c4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00bb96c4",
      "incomplete_value": true,
      "site": "00bb96d0",
      "value": [
        "LOAD",
        "8",
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
      "00bba6a8",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00bba6b8",
      "DATA",
      [
        "storage",
        "01126450",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bba6a8",
      "PARAM",
      [
        "storage",
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      "00bba6b8",
      "DATA",
      [
        "storage",
        "01127410",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb96b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9698.md#insn-00bb96b8) · [`00bb96b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9698.md#insn-00bb96b4) · [`00bb96bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9698.md#insn-00bb96bc)
- 新版 [`00bba6ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba68c.md#insn-00bba6ac) · [`00bba6a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba68c.md#insn-00bba6a8) · [`00bba6b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba68c.md#insn-00bba6b0)

~~~diff
- 00bb96b8 ["INT_ADD", "register:40f0:8", ["const:bb96b8:8", "const:4:8"]]
- 00bb96b8 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00bba6ac ["INT_ADD", "register:40f0:8", ["const:bba6ac:8", "const:4:8"]]
+ 00bba6ac ["CALL", null, ["callee:00c5c0a0:8"]]
- 00bb96b8 bytes 86860294
+ 00bba6ac bytes 7d860294
- 00bb96b4 ["COPY", "tmp:0:8", ["const:54d:8"]]
- 00bb96b4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bb96b4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bb96b4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bba6a8 ["COPY", "tmp:0:8", ["const:61a:8"]]
+ 00bba6a8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bba6a8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bba6a8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bb96b4 bytes 00341591
+ 00bba6a8 bytes 00681891
- 00bb96bc ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00bba6b0 ["COPY", "register:4040:8", ["const:1127000:8"]]
- 00bb96bc bytes 682b00b0
+ 00bba6b0 bytes 682b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a03a1618c65f874e029e72d6ef00f10"></a>

### [`00bb97c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb97c8.md) → [`00bba7bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba7bc.md) _ZN8firebase9messaging17NotifyListenerSetEPNS0_8ListenerE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5d3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d3c0.md) · 呼出先 6件 [`00c598a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c598a0.md) [`00c5a0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0d0.md) [`00c5a160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a160.md) [`00c5a330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a330.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)
- 新版 呼出元 1件 [`00c5e390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e390.md) · 呼出先 6件 [`00c5a870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a870.md) [`00c5b0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0a0.md) [`00c5b130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b130.md) [`00c5b300`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b300.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.56% / 新版 97.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bba7d4",
      "incomplete_value": true,
      "site": "00bba7d4",
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
      "definition_site": "00bb97e0",
      "incomplete_value": true,
      "site": "00bb97e0",
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00bba84c",
      "incomplete_value": true,
      "site": "00bba84c",
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
      "definition_site": "00bb9858",
      "incomplete_value": true,
      "site": "00bb9858",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bba820",
      "incomplete_value": false,
      "site": "00bba824",
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
            "const:1b5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb982c",
      "incomplete_value": false,
      "site": "00bb9830",
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
            "const:ea:8"
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
      "00bba7d0",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00bba7dc",
      "READ",
      [
        "storage",
        "01126490",
        null,
        "undefined8"
      ]
    ],
    [
      "00bba800",
      "READ",
      [
        "storage",
        "01126468",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bba7d0",
      "READ",
      [
        "storage",
        "01127420",
        null,
        "undefined8"
      ]
    ],
    [
      "00bba7dc",
      "READ",
      [
        "storage",
        "01127450",
        null,
        "undefined8"
      ]
    ],
    [
      "00bba800",
      "READ",
      [
        "storage",
        "01127428",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb9830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb97c8.md#insn-00bb9830) · [`00bb97d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb97c8.md#insn-00bb97d8) · [`00bb97dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb97c8.md#insn-00bb97dc)
- 新版 [`00bba824`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba7bc.md#insn-00bba824) · [`00bba7cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba7bc.md#insn-00bba7cc) · [`00bba7d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba7bc.md#insn-00bba7d0)

~~~diff
- 00bb9830 ["INT_ADD", "register:40f0:8", ["const:bb9830:8", "const:4:8"]]
- 00bb9830 ["CALL", null, ["callee:00c5b130:8"]]
+ 00bba824 ["INT_ADD", "register:40f0:8", ["const:bba824:8", "const:4:8"]]
+ 00bba824 ["CALL", null, ["callee:00c5b130:8"]]
- 00bb9830 bytes 4c820294
+ 00bba824 bytes 43820294
- 00bb97d8 ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00bba7cc ["COPY", "register:4040:8", ["const:1127000:8"]]
- 00bb97d8 bytes 682b00b0
+ 00bba7cc bytes 682b00b0
- 00bb97dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:460:8"]]
- 00bb97dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bba7d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:420:8"]]
+ 00bba7d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb97dc bytes 083142f9
+ 00bba7d0 bytes 081142f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-516eb180d3bc8d6b03fe58f38610642a"></a>

### [`00bb98b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb98b4.md) → [`00bba8a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba8a8.md) _ZN8firebase9messaging17RequestPermissionEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5ae70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae70.md) [`00c5aea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aea0.md) [`00c5aed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aed0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5bb30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb30.md) [`00c5be40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5be40.md) [`00c5be70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5be70.md) [`00c5bea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bea0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.25% / 新版 98.25%

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
      "definition_site": "00bba8d4",
      "incomplete_value": true,
      "site": "00bba8d4",
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
      "definition_site": "00bb98e0",
      "incomplete_value": true,
      "site": "00bb98e0",
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
      "definition_site": "00bba954",
      "incomplete_value": false,
      "site": "00bba958",
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
            "const:993:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9960",
      "incomplete_value": false,
      "site": "00bb9964",
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
            "const:8c8:8"
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
      "00bba8d0",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00bba954",
      "PARAM",
      [
        "storage",
        "002a28c8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bba8d0",
      "READ",
      [
        "storage",
        "01127420",
        null,
        "undefined8"
      ]
    ],
    [
      "00bba954",
      "PARAM",
      [
        "storage",
        "002a2993",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb9964`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb98b4.md#insn-00bb9964) · [`00bb98d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb98b4.md#insn-00bb98d8) · [`00bb98dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb98b4.md#insn-00bb98dc)
- 新版 [`00bba958`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba8a8.md#insn-00bba958) · [`00bba8cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba8a8.md#insn-00bba8cc) · [`00bba8d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba8a8.md#insn-00bba8d0)

~~~diff
- 00bb9964 ["INT_ADD", "register:40f0:8", ["const:bb9964:8", "const:4:8"]]
- 00bb9964 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00bba958 ["INT_ADD", "register:40f0:8", ["const:bba958:8", "const:4:8"]]
+ 00bba958 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00bb9964 bytes db850294
+ 00bba958 bytes d2850294
- 00bb98d8 ["COPY", "register:4048:8", ["const:1126000:8"]]
+ 00bba8cc ["COPY", "register:4048:8", ["const:1127000:8"]]
- 00bb98d8 bytes 692b00b0
+ 00bba8cc bytes 692b00b0
- 00bb98dc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:460:8"]]
- 00bb98dc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bba8d0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:420:8"]]
+ 00bba8d0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb98dc bytes 293142f9
+ 00bba8d0 bytes 291142f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52aa4d7bf4cb89b71e0bd36dafe3ba06"></a>

### [`00bb99dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb99dc.md) → [`00bba9d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba9d0.md) _ZN8firebase9messaging27RequestPermissionLastResultEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5d680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d680.md) · 呼出先 8件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5acb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acb0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md)
- 新版 呼出元 1件 [`00c5e650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e650.md) · 呼出先 8件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bc80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bc80.md) [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5bdf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bdf0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 97.62% / 新版 97.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bba9ec",
      "incomplete_value": true,
      "site": "00bba9ec",
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
      "definition_site": "00bb99f8",
      "incomplete_value": true,
      "site": "00bb99f8",
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
      "definition_site": "00bbaa40",
      "incomplete_value": false,
      "site": "00bbaa44",
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
            "const:993:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9a4c",
      "incomplete_value": false,
      "site": "00bb9a50",
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
            "const:8c8:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00bb99f8"
      ],
      [
        "FALL_THROUGH",
        "00bba9ec"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00bba9ec",
      "incomplete_value": true,
      "site": "00bbaa20",
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
      "definition_site": "00bb99f8",
      "incomplete_value": true,
      "site": "00bb9a2c",
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
      "00bba9e4",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbaa40",
      "PARAM",
      [
        "storage",
        "002a28c8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bba9e4",
      "READ",
      [
        "storage",
        "01127420",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbaa40",
      "PARAM",
      [
        "storage",
        "002a2993",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb9a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb99dc.md#insn-00bb9a50) · [`00bb99ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb99dc.md#insn-00bb99ec) · [`00bb99f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb99dc.md#insn-00bb99f0)
- 新版 [`00bbaa44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba9d0.md#insn-00bbaa44) · [`00bba9e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba9d0.md#insn-00bba9e0) · [`00bba9e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bba9d0.md#insn-00bba9e4)

~~~diff
- 00bb9a50 ["INT_ADD", "register:40f0:8", ["const:bb9a50:8", "const:4:8"]]
- 00bb9a50 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00bbaa44 ["INT_ADD", "register:40f0:8", ["const:bbaa44:8", "const:4:8"]]
+ 00bbaa44 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00bb9a50 bytes a0850294
+ 00bbaa44 bytes 97850294
- 00bb99ec ["COPY", "register:4048:8", ["const:1126000:8"]]
+ 00bba9e0 ["COPY", "register:4048:8", ["const:1127000:8"]]
- 00bb99ec bytes 692b00b0
+ 00bba9e0 bytes 692b00b0
- 00bb99f0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:460:8"]]
- 00bb99f0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bba9e4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:420:8"]]
+ 00bba9e4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb99f0 bytes 293142f9
+ 00bba9e4 bytes 291142f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2153be00d6d6c304b1a957aaf0efba9a"></a>

### [`00bb9ab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9ab0.md) → [`00bbaaa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bbaaa4.md) _ZN8firebase9messaging15ProcessMessagesEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5d670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d670.md) · 呼出先 41件 [`0046d5e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d5e8.md) [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`00bbd1f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd1f0.md) [`00bbd1f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd1f4.md)
- 新版 呼出元 1件 [`00c5e640`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e640.md) · 呼出先 41件 [`0046d908`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d908.md) [`00497b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`00497da8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497da8.md) [`00bbe1e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe1e4.md) [`00bbe1e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe1e8.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 14件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bbab30",
      "incomplete_value": true,
      "site": "00bbab30",
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
            "const:448:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9b3c",
      "incomplete_value": true,
      "site": "00bb9b3c",
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
            "const:488:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bbaae4",
      "incomplete_value": true,
      "site": "00bbaae4",
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
      "definition_site": "00bb9af0",
      "incomplete_value": true,
      "site": "00bb9af0",
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
      "definition_site": "00bbab3c",
      "incomplete_value": true,
      "site": "00bbab3c",
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
      "definition_site": "00bb9b48",
      "incomplete_value": true,
      "site": "00bb9b48",
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
      "00bbaad0",
      "PARAM",
      [
        "storage",
        "01126358",
        null,
        null
      ]
    ],
    [
      "00bbaae0",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbaafc",
      "PARAM",
      [
        "storage",
        "01126358",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bbaad0",
      "PARAM",
      [
        "storage",
        "01127318",
        null,
        null
      ]
    ],
    [
      "00bbaae0",
      "READ",
      [
        "storage",
        "01127420",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbaafc",
      "PARAM",
      [
        "storage",
        "01127318",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb9ae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9ab0.md#insn-00bb9ae4) · [`00bb9b0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9ab0.md#insn-00bb9b0c) · [`00bb9b3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9ab0.md#insn-00bb9b3c)
- 新版 [`00bbaad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bbaaa4.md#insn-00bbaad8) · [`00bbab00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bbaaa4.md#insn-00bbab00) · [`00bbab30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bbaaa4.md#insn-00bbab30)

~~~diff
- 00bb9ae4 ["INT_ADD", "register:40f0:8", ["const:bb9ae4:8", "const:4:8"]]
- 00bb9ae4 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00bbaad8 ["INT_ADD", "register:40f0:8", ["const:bbaad8:8", "const:4:8"]]
+ 00bbaad8 ["CALL", null, ["callee:00c5baa0:8"]]
- 00bb9ae4 bytes fb830294
+ 00bbaad8 bytes f2830294
- 00bb9b0c ["INT_ADD", "register:40f0:8", ["const:bb9b0c:8", "const:4:8"]]
- 00bb9b0c ["CALL", null, ["callee:00c5bab0:8"]]
+ 00bbab00 ["INT_ADD", "register:40f0:8", ["const:bbab00:8", "const:4:8"]]
+ 00bbab00 ["CALL", null, ["callee:00c5bab0:8"]]
- 00bb9b0c bytes f5830294
+ 00bbab00 bytes ec830294
- 00bb9b3c ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00bb9b3c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:488:8"]]
- 00bb9b3c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bbab30 ["COPY", "tmp:0:4", ["register:4040:4"]]
+ 00bbab30 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:448:8"]]
+ 00bbab30 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bb9b3c bytes a8221239
+ 00bbab30 bytes a8221139
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68918b3b37b866ff2e6ef70f903d8b0f"></a>

### [`00bba6c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bba6c4.md) → [`00bbb6b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbb/00bbb6b8.md) _ZN8firebase9messaging10InitializeERKNS_3AppEPNS0_8ListenerERKNS0_16MessagingOptionsE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5d660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d660.md) · 呼出先 33件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`00b5ac50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5a/00b5ac50.md) [`00bbabec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbabec.md) [`00bbaca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbaca8.md)
- 新版 呼出元 1件 [`00c5e630`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e630.md) · 呼出先 33件 [`00497b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`00497da8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497da8.md) [`00b5bc44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5b/00b5bc44.md) [`00bbbbe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbb/00bbbbe0.md) [`00bbbc9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbb/00bbbc9c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 83.39% / 新版 83.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 25件, `store_destination` 16件

アドレスに依存する影響 `branch_value` 3件, `call_argument_candidate` 2件, `store_condition` 2件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bbb78c",
      "incomplete_value": true,
      "site": "00bbb78c",
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
            "const:368:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bba798",
      "incomplete_value": true,
      "site": "00bba798",
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
            "const:3a8:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bbb7e4",
      "incomplete_value": true,
      "site": "00bbb7e4",
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
            "const:3d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bba7f0",
      "incomplete_value": true,
      "site": "00bba7f0",
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
            "const:418:8"
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
      "definition_site": "00bbb820",
      "incomplete_value": true,
      "site": "00bbb820",
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
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bba82c",
      "incomplete_value": true,
      "site": "00bba82c",
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
            "const:460:8"
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
      "00bbb708",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbb714",
      "PARAM",
      [
        "storage",
        "002a3b5c",
        null,
        "string"
      ]
    ],
    [
      "00bbb764",
      "READ",
      [
        "storage",
        "011263a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bbb708",
      "READ",
      [
        "storage",
        "01127420",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbb714",
      "PARAM",
      [
        "storage",
        "002a3c27",
        null,
        "string"
      ]
    ],
    [
      "00bbb764",
      "READ",
      [
        "storage",
        "01127368",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bba724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bba6c4.md#insn-00bba724) · [`00bba790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bba6c4.md#insn-00bba790) · [`00bba798`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bba6c4.md#insn-00bba798)
- 新版 [`00bbb718`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbb/00bbb6b8.md#insn-00bbb718) · [`00bbb784`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbb/00bbb6b8.md#insn-00bbb784) · [`00bbb78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbb/00bbb6b8.md#insn-00bbb78c)

~~~diff
- 00bba724 ["INT_ADD", "register:40f0:8", ["const:bba724:8", "const:4:8"]]
- 00bba724 ["CALL", null, ["callee:00c5bd40:8"]]
+ 00bbb718 ["INT_ADD", "register:40f0:8", ["const:bbb718:8", "const:4:8"]]
+ 00bbb718 ["CALL", null, ["callee:00c5bd40:8"]]
- 00bba724 bytes 93810294
+ 00bbb718 bytes 8a810294
- 00bba790 ["INT_ADD", "register:40f0:8", ["const:bba790:8", "const:4:8"]]
- 00bba790 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00bbb784 ["INT_ADD", "register:40f0:8", ["const:bbb784:8", "const:4:8"]]
+ 00bbb784 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00bba790 bytes 14820294
+ 00bbb784 bytes 0b820294
- 00bba798 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:3a8:8"]]
- 00bba798 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bbb78c ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:368:8"]]
+ 00bbb78c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bba798 bytes 00d701f9
+ 00bbb78c bytes 00b701f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c22a72484e44f97abcc0ce7753fc957"></a>

### [`00bbabec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbabec.md) → [`00bbbbe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbb/00bbbbe0.md) FUN_00bbbbe0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00bba6c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bba6c4.md) [`00bbb0f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbb0f4.md) · 呼出先 1件 [`00c5b030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b030.md)
- 新版 呼出元 2件 [`00bbb6b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbb/00bbb6b8.md) [`00bbc0e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbc/00bbc0e8.md) · 呼出先 1件 [`00c5c000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c000.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 87.23% / 新版 87.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 4件

アドレスに依存する影響 `branch_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bbbc1c",
      "incomplete_value": true,
      "site": "00bbbc1c",
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
            "const:370:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbac28",
      "incomplete_value": true,
      "site": "00bbac28",
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
            "const:3b0:8"
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
      "definition_site": "00bbbc3c",
      "incomplete_value": true,
      "site": "00bbbc3c",
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
            "const:368:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbac48",
      "incomplete_value": true,
      "site": "00bbac48",
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
            "const:3a8:8"
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
      "definition_site": "00bbbc68",
      "incomplete_value": true,
      "site": "00bbbc68",
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
            "const:3e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbac74",
      "incomplete_value": true,
      "site": "00bbac74",
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
            "const:420:8"
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
      "00bbbbf4",
      "READ",
      [
        "storage",
        "011263a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbbc04",
      "READ",
      [
        "storage",
        "011263b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bbbc1c",
      "WRITE",
      [
        "storage",
        "011263b0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bbbbf4",
      "READ",
      [
        "storage",
        "01127368",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbbc04",
      "READ",
      [
        "storage",
        "01127370",
        null,
        "undefined1"
      ]
    ],
    [
      "00bbbc1c",
      "WRITE",
      [
        "storage",
        "01127370",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbac28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbabec.md#insn-00bbac28) · [`00bbac44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbabec.md#insn-00bbac44) · [`00bbac48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbabec.md#insn-00bbac48)
- 新版 [`00bbbc1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbb/00bbbbe0.md#insn-00bbbc1c) · [`00bbbc38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbb/00bbbbe0.md#insn-00bbbc38) · [`00bbbc3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbb/00bbbbe0.md#insn-00bbbc3c)

~~~diff
- 00bbac28 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bbac28 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bbac28 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:3b0:8"]]
- 00bbac28 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bbbc1c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bbbc1c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bbbc1c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:370:8"]]
+ 00bbbc1c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bbac28 bytes bfc20e39
+ 00bbbc1c bytes bfc20d39
- 00bbac44 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bbac44 ["INT_ADD", "register:40f0:8", ["const:bbac44:8", "const:4:8"]]
- 00bbac44 ["CALLIND", null, ["register:0:8"]]
+ 00bbbc38 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bbbc38 ["INT_ADD", "register:40f0:8", ["const:bbbc38:8", "const:4:8"]]
+ 00bbbc38 ["CALLIND", null, ["register:0:8"]]
- 00bbac44 bytes 00013fd6
+ 00bbbc38 bytes 00013fd6
- 00bbac48 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3a8:8"]]
- 00bbac48 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00bbac48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bbbc3c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:368:8"]]
+ 00bbbc3c ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bbbc3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00bbac48 bytes 9fd601f9
+ 00bbbc3c bytes 9fb601f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4a88090898fa3a5d7b0243324a3ea70"></a>

### [`00bbaca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbaca8.md) → [`00bbbc9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbb/00bbbc9c.md) FUN_00bbbc9c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bba6c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bba6c4.md) · 呼出先 11件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58190.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 1件 [`00bbb6b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbb/00bbb6b8.md) · 呼出先 11件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59160.md) [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.47% / 新版 92.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bbbcdc",
      "incomplete_value": true,
      "site": "00bbbcdc",
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
      "definition_site": "00bbace8",
      "incomplete_value": true,
      "site": "00bbace8",
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
      "definition_site": "00bbbcc8",
      "incomplete_value": false,
      "site": "00bbbcd0",
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
            "const:318:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbacd4",
      "incomplete_value": false,
      "site": "00bbacdc",
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
            "const:358:8"
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
      "definition_site": "00bbbcf4",
      "incomplete_value": false,
      "site": "00bbbcf8",
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
            "const:318:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbad00",
      "incomplete_value": false,
      "site": "00bbad04",
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
            "const:358:8"
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
      "00bbbcc8",
      "PARAM",
      [
        "storage",
        "01126358",
        null,
        null
      ]
    ],
    [
      "00bbbcd8",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbbcf4",
      "PARAM",
      [
        "storage",
        "01126358",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bbbcc8",
      "PARAM",
      [
        "storage",
        "01127318",
        null,
        null
      ]
    ],
    [
      "00bbbcd8",
      "READ",
      [
        "storage",
        "01127420",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbbcf4",
      "PARAM",
      [
        "storage",
        "01127318",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbacdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbaca8.md#insn-00bbacdc) · [`00bbad04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbaca8.md#insn-00bbad04) · [`00bbacd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbaca8.md#insn-00bbacd0)
- 新版 [`00bbbcd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbb/00bbbc9c.md#insn-00bbbcd0) · [`00bbbcf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbb/00bbbc9c.md#insn-00bbbcf8) · [`00bbbcc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbb/00bbbc9c.md#insn-00bbbcc4)

~~~diff
- 00bbacdc ["INT_ADD", "register:40f0:8", ["const:bbacdc:8", "const:4:8"]]
- 00bbacdc ["CALL", null, ["callee:00c5baa0:8"]]
+ 00bbbcd0 ["INT_ADD", "register:40f0:8", ["const:bbbcd0:8", "const:4:8"]]
+ 00bbbcd0 ["CALL", null, ["callee:00c5baa0:8"]]
- 00bbacdc bytes 7d7f0294
+ 00bbbcd0 bytes 747f0294
- 00bbad04 ["INT_ADD", "register:40f0:8", ["const:bbad04:8", "const:4:8"]]
- 00bbad04 ["CALL", null, ["callee:00c5bab0:8"]]
+ 00bbbcf8 ["INT_ADD", "register:40f0:8", ["const:bbbcf8:8", "const:4:8"]]
+ 00bbbcf8 ["CALL", null, ["callee:00c5bab0:8"]]
- 00bbad04 bytes 777f0294
+ 00bbbcf8 bytes 6e7f0294
- 00bbacd0 ["COPY", "register:4000:8", ["const:1126000:8"]]
+ 00bbbcc4 ["COPY", "register:4000:8", ["const:1127000:8"]]
- 00bbacd0 bytes 602b0090
+ 00bbbcc4 bytes 602b0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4189ecd2f360a8558895e51a16877943"></a>

### [`00bbae40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbae40.md) → [`00bbbe34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbb/00bbbe34.md) _ZN8firebase9messaging33SetTokenRegistrationOnInitEnabledEb

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5abb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5abb0.md) · 呼出先 6件 [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`00574d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00574/00574d2c.md) [`00bbafec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbafec.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 1件 [`00c5bb80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb80.md) · 呼出先 6件 [`00497da8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497da8.md) [`0057504c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00575/0057504c.md) [`00bbbfe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbb/00bbbfe0.md) [`00c5bd40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd40.md) [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_condition, store_destination

命令の説明率　旧版 70.00% / 新版 70.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 4件, `call_argument_candidate` 9件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bbbf30",
      "incomplete_value": false,
      "site": "00bbbf30",
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
            "const:4c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbaf3c",
      "incomplete_value": false,
      "site": "00bbaf3c",
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
            "const:500:8"
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
      "definition_site": "00bbbe54",
      "incomplete_value": true,
      "site": "00bbbe54",
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
      "definition_site": "00bbae60",
      "incomplete_value": true,
      "site": "00bbae60",
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
      "definition_site": "00bbbe68",
      "incomplete_value": true,
      "site": "00bbbe68",
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
      "definition_site": "00bbae74",
      "incomplete_value": true,
      "site": "00bbae74",
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
      "00bbbe4c",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbbe60",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbbe70",
      "PARAM",
      [
        "storage",
        "002a28c8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bbbe4c",
      "READ",
      [
        "storage",
        "01127420",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbbe60",
      "READ",
      [
        "storage",
        "01127420",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbbe70",
      "PARAM",
      [
        "storage",
        "002a2993",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbae80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbae40.md#insn-00bbae80) · [`00bbae8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbae40.md#insn-00bbae8c) · [`00bbaeb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbae40.md#insn-00bbaeb4)
- 新版 [`00bbbe74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbb/00bbbe34.md#insn-00bbbe74) · [`00bbbe80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbb/00bbbe34.md#insn-00bbbe80) · [`00bbbea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbb/00bbbe34.md#insn-00bbbea8)

~~~diff
- 00bbae80 ["INT_ADD", "register:40f0:8", ["const:bbae80:8", "const:4:8"]]
- 00bbae80 ["CALL", null, ["callee:00c5bd40:8"]]
+ 00bbbe74 ["INT_ADD", "register:40f0:8", ["const:bbbe74:8", "const:4:8"]]
+ 00bbbe74 ["CALL", null, ["callee:00c5bd40:8"]]
- 00bbae80 bytes bc7f0294
+ 00bbbe74 bytes b37f0294
- 00bbae8c ["INT_ADD", "register:40f0:8", ["const:bbae8c:8", "const:4:8"]]
- 00bbae8c ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00bbbe80 ["INT_ADD", "register:40f0:8", ["const:bbbe80:8", "const:4:8"]]
+ 00bbbe80 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00bbae8c bytes 91800294
+ 00bbbe80 bytes 88800294
- 00bbaeb4 ["INT_ADD", "register:40f0:8", ["const:bbaeb4:8", "const:4:8"]]
- 00bbaeb4 ["CALL", null, ["callee:00497da8:8"]]
+ 00bbbea8 ["INT_ADD", "register:40f0:8", ["const:bbbea8:8", "const:4:8"]]
+ 00bbbea8 ["CALL", null, ["callee:00497da8:8"]]
- 00bbaeb4 bytes f572e397
+ 00bbbea8 bytes c06fe397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1dba820ef5a30af0c85d9c04d18bca7b"></a>

### [`00bbaf80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbaf80.md) → [`00bbbf74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbb/00bbbf74.md) _ZN8firebase9messaging32IsTokenRegistrationOnInitEnabledEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00497da8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497da8.md) [`00c5bd40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd40.md) [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md) [`00c5c120`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c120.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 74.07% / 新版 74.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bbbf88",
      "incomplete_value": true,
      "site": "00bbbf88",
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
      "definition_site": "00bbaf94",
      "incomplete_value": true,
      "site": "00bbaf94",
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00bbbfa8",
      "incomplete_value": true,
      "site": "00bbbfa8",
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
      "definition_site": "00bbafb4",
      "incomplete_value": true,
      "site": "00bbafb4",
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
      "definition_site": "00bbbf90",
      "incomplete_value": false,
      "site": "00bbbf94",
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
            "const:993:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbaf9c",
      "incomplete_value": false,
      "site": "00bbafa0",
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
            "const:8c8:8"
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
      "00bbbf84",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbbf90",
      "PARAM",
      [
        "storage",
        "002a28c8",
        null,
        "string"
      ]
    ],
    [
      "00bbbf9c",
      "PARAM",
      [
        "storage",
        "002b071b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bbbf84",
      "READ",
      [
        "storage",
        "01127420",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbbf90",
      "PARAM",
      [
        "storage",
        "002a2993",
        null,
        "string"
      ]
    ],
    [
      "00bbbf9c",
      "PARAM",
      [
        "storage",
        "002b07f2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbafa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbaf80.md#insn-00bbafa0) · [`00bbafac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbaf80.md#insn-00bbafac) · [`00bbafcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbaf80.md#insn-00bbafcc)
- 新版 [`00bbbf94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbb/00bbbf74.md#insn-00bbbf94) · [`00bbbfa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbb/00bbbf74.md#insn-00bbbfa0) · [`00bbbfc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbb/00bbbf74.md#insn-00bbbfc0)

~~~diff
- 00bbafa0 ["INT_ADD", "register:40f0:8", ["const:bbafa0:8", "const:4:8"]]
- 00bbafa0 ["CALL", null, ["callee:00c5bd40:8"]]
+ 00bbbf94 ["INT_ADD", "register:40f0:8", ["const:bbbf94:8", "const:4:8"]]
+ 00bbbf94 ["CALL", null, ["callee:00c5bd40:8"]]
- 00bbafa0 bytes 747f0294
+ 00bbbf94 bytes 6b7f0294
- 00bbafac ["INT_ADD", "register:40f0:8", ["const:bbafac:8", "const:4:8"]]
- 00bbafac ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00bbbfa0 ["INT_ADD", "register:40f0:8", ["const:bbbfa0:8", "const:4:8"]]
+ 00bbbfa0 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00bbafac bytes 49800294
+ 00bbbfa0 bytes 40800294
- 00bbafcc ["INT_ADD", "register:40f0:8", ["const:bbafcc:8", "const:4:8"]]
- 00bbafcc ["CALL", null, ["callee:00497da8:8"]]
+ 00bbbfc0 ["INT_ADD", "register:40f0:8", ["const:bbbfc0:8", "const:4:8"]]
+ 00bbbfc0 ["CALL", null, ["callee:00497da8:8"]]
- 00bbafcc bytes af72e397
+ 00bbbfc0 bytes 7a6fe397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc12d65634f308657ee61f83d53c52eb"></a>

### [`00bbafec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbafec.md) → [`00bbbfe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbb/00bbbfe0.md) FUN_00bbbfe0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00bba6c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bba6c4.md) [`00bbae40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbae40.md) · 呼出先 11件 [`0087b414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b414.md) [`00bbd410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd410.md) [`00bbd428`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd428.md) [`00bbd434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd434.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 2件 [`00bbb6b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbb/00bbb6b8.md) [`00bbbe34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbb/00bbbe34.md) · 呼出先 11件 [`0087c3c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087c3c0.md) [`00bbe404`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe404.md) [`00bbe41c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe41c.md) [`00bbe428`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe428.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.74% / 新版 90.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `branch_value` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bbc030",
      "incomplete_value": false,
      "site": "00bbc030",
      "value": [
        "leaf",
        "const:bbe428:8"
      ]
    },
    "old": {
      "definition_site": "00bbb03c",
      "incomplete_value": false,
      "site": "00bbb03c",
      "value": [
        "leaf",
        "const:bbd434:8"
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bbc004",
      "incomplete_value": true,
      "site": "00bbc004",
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
      "definition_site": "00bbb010",
      "incomplete_value": true,
      "site": "00bbb010",
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
      "definition_site": "00bbc050",
      "incomplete_value": true,
      "site": "00bbc064",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbb05c",
      "incomplete_value": true,
      "site": "00bbb070",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9e0:8"
              ]
            ]
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
      "00bbc000",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbc030",
      "DATA",
      [
        "storage",
        "00bbd434",
        null,
        null
      ]
    ],
    [
      "00bbc050",
      "READ",
      [
        "storage",
        "00c9b9e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bbc000",
      "READ",
      [
        "storage",
        "01127420",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbc030",
      "DATA",
      [
        "storage",
        "00bbe428",
        null,
        null
      ]
    ],
    [
      "00bbc050",
      "READ",
      [
        "storage",
        "00c9c9b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbb070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbafec.md#insn-00bbb070) · [`00bbb090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbafec.md#insn-00bbb090) · [`00bbb09c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbafec.md#insn-00bbb09c)
- 新版 [`00bbc064`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbb/00bbbfe0.md#insn-00bbc064) · [`00bbc084`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbb/00bbbfe0.md#insn-00bbc084) · [`00bbc090`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbb/00bbbfe0.md#insn-00bbc090)

~~~diff
- 00bbb070 ["COPY", "register:0:8", ["register:4048:8"]]
- 00bbb070 ["INT_ADD", "register:40f0:8", ["const:bbb070:8", "const:4:8"]]
- 00bbb070 ["CALLIND", null, ["register:0:8"]]
+ 00bbc064 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00bbc064 ["INT_ADD", "register:40f0:8", ["const:bbc064:8", "const:4:8"]]
+ 00bbc064 ["CALLIND", null, ["register:0:8"]]
- 00bbb070 bytes 20013fd6
+ 00bbc064 bytes 20013fd6
- 00bbb090 ["INT_ADD", "register:40f0:8", ["const:bbb090:8", "const:4:8"]]
- 00bbb090 ["CALL", null, ["callee:00c5bd40:8"]]
+ 00bbc084 ["INT_ADD", "register:40f0:8", ["const:bbc084:8", "const:4:8"]]
+ 00bbc084 ["CALL", null, ["callee:00c5bd40:8"]]
- 00bbb090 bytes 387f0294
+ 00bbc084 bytes 2f7f0294
- 00bbb09c ["INT_ADD", "register:40f0:8", ["const:bbb09c:8", "const:4:8"]]
- 00bbb09c ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00bbc090 ["INT_ADD", "register:40f0:8", ["const:bbc090:8", "const:4:8"]]
+ 00bbc090 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00bbb09c bytes 0d800294
+ 00bbc090 bytes 04800294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e4e0704ec2a74149d4463cbf65fa1c5"></a>

### [`00bbb0f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbb0f4.md) → [`00bbc0e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbc/00bbc0e8.md) _ZN8firebase9messaging9TerminateEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5d510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d510.md) · 呼出先 23件 [`00bbabec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbabec.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c598a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c598a0.md) [`00c5a0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0d0.md) [`00c5a160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a160.md)
- 新版 呼出元 1件 [`00c5e4e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e4e0.md) · 呼出先 23件 [`00bbbbe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbb/00bbbbe0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5a870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a870.md) [`00c5b0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0a0.md) [`00c5b130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b130.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 83.50% / 新版 83.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 5件, `call_argument_candidate` 9件, `store_destination` 9件

アドレスに依存する影響 `branch_value` 3件, `call_argument_candidate` 2件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bbc138",
      "incomplete_value": true,
      "site": "00bbc138",
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
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbb144",
      "incomplete_value": true,
      "site": "00bbb144",
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
            "const:460:8"
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
      "definition_site": "00bbc254",
      "incomplete_value": true,
      "site": "00bbc254",
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
            "const:430:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbb260",
      "incomplete_value": true,
      "site": "00bbb260",
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
            "const:470:8"
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
      "definition_site": "00bbc274",
      "incomplete_value": true,
      "site": "00bbc274",
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
            "const:418:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbb280",
      "incomplete_value": true,
      "site": "00bbb280",
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
            "const:458:8"
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
      "00bbc104",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbc110",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbc11c",
      "PARAM",
      [
        "storage",
        "0030e801",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bbc104",
      "READ",
      [
        "storage",
        "01127420",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbc110",
      "READ",
      [
        "storage",
        "01127420",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbc11c",
      "PARAM",
      [
        "storage",
        "0030e841",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbb120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbb0f4.md#insn-00bbb120) · [`00bbb130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbb0f4.md#insn-00bbb130) · [`00bbb140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbb0f4.md#insn-00bbb140)
- 新版 [`00bbc114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbc/00bbc0e8.md#insn-00bbc114) · [`00bbc124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbc/00bbc0e8.md#insn-00bbc124) · [`00bbc134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbc/00bbc0e8.md#insn-00bbc134)

~~~diff
- 00bbb120 ["INT_ADD", "register:40f0:8", ["const:bbb120:8", "const:4:8"]]
- 00bbb120 ["CALL", null, ["callee:00c5c120:8"]]
+ 00bbc114 ["INT_ADD", "register:40f0:8", ["const:bbc114:8", "const:4:8"]]
+ 00bbc114 ["CALL", null, ["callee:00c5c120:8"]]
- 00bbb120 bytes 0c800294
+ 00bbc114 bytes 03800294
- 00bbb130 ["INT_ADD", "register:40f0:8", ["const:bbb130:8", "const:4:8"]]
- 00bbb130 ["CALL", null, ["callee:00c5bfa0:8"]]
+ 00bbc124 ["INT_ADD", "register:40f0:8", ["const:bbc124:8", "const:4:8"]]
+ 00bbc124 ["CALL", null, ["callee:00c5bfa0:8"]]
- 00bbb130 bytes a87f0294
+ 00bbc124 bytes 9f7f0294
- 00bbb140 ["INT_ADD", "register:40f0:8", ["const:bbb140:8", "const:4:8"]]
- 00bbb140 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00bbc134 ["INT_ADD", "register:40f0:8", ["const:bbc134:8", "const:4:8"]]
+ 00bbc134 ["CALL", null, ["callee:00c5baa0:8"]]
- 00bbb140 bytes 647e0294
+ 00bbc134 bytes 5b7e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-612c3c56cb2c56831735fd5512270912"></a>

### [`00bbb468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbb468.md) → [`00bbc45c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbc/00bbc45c.md) _ZN8firebase9messaging9SubscribeEPKc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 18件 [`00bbb738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbb738.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)
- 新版 呼出元 0件  · 呼出先 18件 [`00bbc72c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbc/00bbc72c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_condition

命令の説明率　旧版 96.38% / 新版 96.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `branch_value` 2件, `call_argument_candidate` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bbc490",
      "incomplete_value": true,
      "site": "00bbc490",
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
      "definition_site": "00bbb49c",
      "incomplete_value": true,
      "site": "00bbb49c",
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
      "definition_site": "00bbc57c",
      "incomplete_value": true,
      "site": "00bbc57c",
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
      "definition_site": "00bbb588",
      "incomplete_value": true,
      "site": "00bbb588",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bbc4a0",
      "incomplete_value": true,
      "site": "00bbc4a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:430:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbb4ac",
      "incomplete_value": true,
      "site": "00bbb4b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:470:8"
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
      "00bbc48c",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbc498",
      "READ",
      [
        "storage",
        "01126470",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbc4dc",
      "READ",
      [
        "storage",
        "01126508",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bbc48c",
      "READ",
      [
        "storage",
        "01127420",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbc498",
      "READ",
      [
        "storage",
        "01127430",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbc4dc",
      "READ",
      [
        "storage",
        "011274c8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbb4b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbb468.md#insn-00bbb4b0) · [`00bbb50c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbb468.md#insn-00bbb50c) · [`00bbb518`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbb468.md#insn-00bbb518)
- 新版 [`00bbc4a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbc/00bbc45c.md#insn-00bbc4a4) · [`00bbc500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbc/00bbc45c.md#insn-00bbc500) · [`00bbc50c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbc/00bbc45c.md#insn-00bbc50c)

~~~diff
- 00bbb4b0 ["INT_ADD", "register:40f0:8", ["const:bbb4b0:8", "const:4:8"]]
- 00bbb4b0 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00bbc4a4 ["INT_ADD", "register:40f0:8", ["const:bbc4a4:8", "const:4:8"]]
+ 00bbc4a4 ["CALL", null, ["callee:00c5baa0:8"]]
- 00bbb4b0 bytes 887d0294
+ 00bbc4a4 bytes 7f7d0294
- 00bbb50c ["INT_ADD", "register:40f0:8", ["const:bbb50c:8", "const:4:8"]]
- 00bbb50c ["CALL", null, ["callee:00c5bd40:8"]]
+ 00bbc500 ["INT_ADD", "register:40f0:8", ["const:bbc500:8", "const:4:8"]]
+ 00bbc500 ["CALL", null, ["callee:00c5bd40:8"]]
- 00bbb50c bytes 197e0294
+ 00bbc500 bytes 107e0294
- 00bbb518 ["INT_ADD", "register:40f0:8", ["const:bbb518:8", "const:4:8"]]
- 00bbb518 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00bbc50c ["INT_ADD", "register:40f0:8", ["const:bbc50c:8", "const:4:8"]]
+ 00bbc50c ["CALL", null, ["callee:00c5c0a0:8"]]
- 00bbb518 bytes ee7e0294
+ 00bbc50c bytes e57e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-827940e02ad228829218bb110c8f7f43"></a>

### [`00bbb738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbb738.md) → [`00bbc72c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbc/00bbc72c.md) FUN_00bbc72c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00bbb468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbb468.md) [`00bbd25c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd25c.md) · 呼出先 14件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00bbd4fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd4fc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 2件 [`00bbc45c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbc/00bbc45c.md) [`00bbe250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe250.md) · 呼出先 14件 [`00497b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`00bbe4f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe4f0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.50% / 新版 95.50%

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
      "definition_site": "00bbc758",
      "incomplete_value": true,
      "site": "00bbc764",
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
            "const:442:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbb764",
      "incomplete_value": true,
      "site": "00bbb770",
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
            "const:375:8"
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
      "definition_site": "00bbc76c",
      "incomplete_value": true,
      "site": "00bbc770",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:420:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbb778",
      "incomplete_value": true,
      "site": "00bbb77c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:460:8"
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
      "definition_site": "00bbc790",
      "incomplete_value": true,
      "site": "00bbc7a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:458:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbb79c",
      "incomplete_value": true,
      "site": "00bbb7b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:498:8"
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
      "00bbc758",
      "PARAM",
      [
        "storage",
        "002ae375",
        null,
        "string"
      ]
    ],
    [
      "00bbc76c",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbc790",
      "READ",
      [
        "storage",
        "01126498",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bbc758",
      "PARAM",
      [
        "storage",
        "002ae442",
        null,
        "string"
      ]
    ],
    [
      "00bbc76c",
      "READ",
      [
        "storage",
        "01127420",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbc790",
      "READ",
      [
        "storage",
        "01127458",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbb770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbb738.md#insn-00bbb770) · [`00bbb77c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbb738.md#insn-00bbb77c) · [`00bbb7b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbb738.md#insn-00bbb7b0)
- 新版 [`00bbc764`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbc/00bbc72c.md#insn-00bbc764) · [`00bbc770`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbc/00bbc72c.md#insn-00bbc770) · [`00bbc7a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbc/00bbc72c.md#insn-00bbc7a4)

~~~diff
- 00bbb770 ["INT_ADD", "register:40f0:8", ["const:bbb770:8", "const:4:8"]]
- 00bbb770 ["CALL", null, ["callee:00c5c1d0:8"]]
+ 00bbc764 ["INT_ADD", "register:40f0:8", ["const:bbc764:8", "const:4:8"]]
+ 00bbc764 ["CALL", null, ["callee:00c5c1d0:8"]]
- 00bbb770 bytes a47e0294
+ 00bbc764 bytes 9b7e0294
- 00bbb77c ["INT_ADD", "register:40f0:8", ["const:bbb77c:8", "const:4:8"]]
- 00bbb77c ["CALL", null, ["callee:00c5c120:8"]]
+ 00bbc770 ["INT_ADD", "register:40f0:8", ["const:bbc770:8", "const:4:8"]]
+ 00bbc770 ["CALL", null, ["callee:00c5c120:8"]]
- 00bbb77c bytes 757e0294
+ 00bbc770 bytes 6c7e0294
- 00bbb7b0 ["INT_ADD", "register:40f0:8", ["const:bbb7b0:8", "const:4:8"]]
- 00bbb7b0 ["CALL", null, ["callee:00497b94:8"]]
+ 00bbc7a4 ["INT_ADD", "register:40f0:8", ["const:bbc7a4:8", "const:4:8"]]
+ 00bbc7a4 ["CALL", null, ["callee:00497b94:8"]]
- 00bbb7b0 bytes 3170e397
+ 00bbc7a4 bytes fc6ce397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb380a196270eebcd651310136aa94ee"></a>

### [`00bbb934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbb934.md) → [`00bbc928`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbc/00bbc928.md) _ZN8firebase9messaging19SubscribeLastResultEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5acb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acb0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bc80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bc80.md) [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5bdf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bdf0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 97.62% / 新版 97.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bbc944",
      "incomplete_value": true,
      "site": "00bbc944",
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
      "definition_site": "00bbb950",
      "incomplete_value": true,
      "site": "00bbb950",
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
      "definition_site": "00bbc998",
      "incomplete_value": false,
      "site": "00bbc99c",
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
            "const:993:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbb9a4",
      "incomplete_value": false,
      "site": "00bbb9a8",
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
            "const:8c8:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00bbb950"
      ],
      [
        "FALL_THROUGH",
        "00bbc944"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00bbc944",
      "incomplete_value": true,
      "site": "00bbc978",
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
      "definition_site": "00bbb950",
      "incomplete_value": true,
      "site": "00bbb984",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bbc93c",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbc998",
      "PARAM",
      [
        "storage",
        "002a28c8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bbc93c",
      "READ",
      [
        "storage",
        "01127420",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbc998",
      "PARAM",
      [
        "storage",
        "002a2993",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbb9a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbb934.md#insn-00bbb9a8) · [`00bbb944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbb934.md#insn-00bbb944) · [`00bbb948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbb934.md#insn-00bbb948)
- 新版 [`00bbc99c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbc/00bbc928.md#insn-00bbc99c) · [`00bbc938`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbc/00bbc928.md#insn-00bbc938) · [`00bbc93c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbc/00bbc928.md#insn-00bbc93c)

~~~diff
- 00bbb9a8 ["INT_ADD", "register:40f0:8", ["const:bbb9a8:8", "const:4:8"]]
- 00bbb9a8 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00bbc99c ["INT_ADD", "register:40f0:8", ["const:bbc99c:8", "const:4:8"]]
+ 00bbc99c ["CALL", null, ["callee:00c5c0a0:8"]]
- 00bbb9a8 bytes ca7d0294
+ 00bbc99c bytes c17d0294
- 00bbb944 ["COPY", "register:4048:8", ["const:1126000:8"]]
+ 00bbc938 ["COPY", "register:4048:8", ["const:1127000:8"]]
- 00bbb944 bytes 492b00f0
+ 00bbc938 bytes 492b00f0
- 00bbb948 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:460:8"]]
- 00bbb948 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bbc93c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:420:8"]]
+ 00bbc93c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00bbb948 bytes 293142f9
+ 00bbc93c bytes 291142f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1d67ed9e002b51e3bce280b6064b11f"></a>

### [`00bbba0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbba0c.md) → [`00bbca00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbc/00bbca00.md) _ZN8firebase9messaging11UnsubscribeEPKc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 18件 [`00bbbcdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbbcdc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)
- 新版 呼出元 0件  · 呼出先 18件 [`00bbccd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbc/00bbccd0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_condition

命令の説明率　旧版 96.38% / 新版 96.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `branch_value` 2件, `call_argument_candidate` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bbca34",
      "incomplete_value": true,
      "site": "00bbca34",
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
      "definition_site": "00bbba40",
      "incomplete_value": true,
      "site": "00bbba40",
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
      "definition_site": "00bbcb20",
      "incomplete_value": true,
      "site": "00bbcb20",
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
      "definition_site": "00bbbb2c",
      "incomplete_value": true,
      "site": "00bbbb2c",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bbca44",
      "incomplete_value": true,
      "site": "00bbca48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:430:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbba50",
      "incomplete_value": true,
      "site": "00bbba54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:470:8"
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
      "00bbca30",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbca3c",
      "READ",
      [
        "storage",
        "01126470",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbca80",
      "READ",
      [
        "storage",
        "01126508",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bbca30",
      "READ",
      [
        "storage",
        "01127420",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbca3c",
      "READ",
      [
        "storage",
        "01127430",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbca80",
      "READ",
      [
        "storage",
        "011274c8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbba54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbba0c.md#insn-00bbba54) · [`00bbbab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbba0c.md#insn-00bbbab0) · [`00bbbabc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbba0c.md#insn-00bbbabc)
- 新版 [`00bbca48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbc/00bbca00.md#insn-00bbca48) · [`00bbcaa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbc/00bbca00.md#insn-00bbcaa4) · [`00bbcab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbc/00bbca00.md#insn-00bbcab0)

~~~diff
- 00bbba54 ["INT_ADD", "register:40f0:8", ["const:bbba54:8", "const:4:8"]]
- 00bbba54 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00bbca48 ["INT_ADD", "register:40f0:8", ["const:bbca48:8", "const:4:8"]]
+ 00bbca48 ["CALL", null, ["callee:00c5baa0:8"]]
- 00bbba54 bytes 1f7c0294
+ 00bbca48 bytes 167c0294
- 00bbbab0 ["INT_ADD", "register:40f0:8", ["const:bbbab0:8", "const:4:8"]]
- 00bbbab0 ["CALL", null, ["callee:00c5bd40:8"]]
+ 00bbcaa4 ["INT_ADD", "register:40f0:8", ["const:bbcaa4:8", "const:4:8"]]
+ 00bbcaa4 ["CALL", null, ["callee:00c5bd40:8"]]
- 00bbbab0 bytes b07c0294
+ 00bbcaa4 bytes a77c0294
- 00bbbabc ["INT_ADD", "register:40f0:8", ["const:bbbabc:8", "const:4:8"]]
- 00bbbabc ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00bbcab0 ["INT_ADD", "register:40f0:8", ["const:bbcab0:8", "const:4:8"]]
+ 00bbcab0 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00bbbabc bytes 857d0294
+ 00bbcab0 bytes 7c7d0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7722853f9e08a7f55e89940466ca005c"></a>

### [`00bbbcdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbbcdc.md) → [`00bbccd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbc/00bbccd0.md) FUN_00bbccd0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00bbba0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbba0c.md) [`00bbd25c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd25c.md) · 呼出先 14件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00bbd4fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd4fc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 2件 [`00bbca00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbc/00bbca00.md) [`00bbe250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe250.md) · 呼出先 14件 [`00497b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`00bbe4f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe4f0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.50% / 新版 95.50%

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
      "definition_site": "00bbccfc",
      "incomplete_value": false,
      "site": "00bbcd08",
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
            "const:c1d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbbd08",
      "incomplete_value": false,
      "site": "00bbbd14",
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
            "const:bd3:8"
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
      "definition_site": "00bbcd10",
      "incomplete_value": true,
      "site": "00bbcd14",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:420:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbbd1c",
      "incomplete_value": true,
      "site": "00bbbd20",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:460:8"
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
      "definition_site": "00bbce18",
      "incomplete_value": false,
      "site": "00bbce2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bbe000:8"
          ],
          [
            "leaf",
            "const:4f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbbe24",
      "incomplete_value": false,
      "site": "00bbbe38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bbd000:8"
          ],
          [
            "leaf",
            "const:4fc:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bbccfc",
      "PARAM",
      [
        "storage",
        "002c0bd3",
        null,
        "string"
      ]
    ],
    [
      "00bbcd10",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbcd34",
      "READ",
      [
        "storage",
        "01126498",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bbccfc",
      "PARAM",
      [
        "storage",
        "002c0c1d",
        null,
        "string"
      ]
    ],
    [
      "00bbcd10",
      "READ",
      [
        "storage",
        "01127420",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbcd34",
      "READ",
      [
        "storage",
        "01127458",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbbd14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbbcdc.md#insn-00bbbd14) · [`00bbbd20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbbcdc.md#insn-00bbbd20) · [`00bbbe38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbbcdc.md#insn-00bbbe38)
- 新版 [`00bbcd08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbc/00bbccd0.md#insn-00bbcd08) · [`00bbcd14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbc/00bbccd0.md#insn-00bbcd14) · [`00bbce2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbc/00bbccd0.md#insn-00bbce2c)

~~~diff
- 00bbbd14 ["INT_ADD", "register:40f0:8", ["const:bbbd14:8", "const:4:8"]]
- 00bbbd14 ["CALL", null, ["callee:00c5c1d0:8"]]
+ 00bbcd08 ["INT_ADD", "register:40f0:8", ["const:bbcd08:8", "const:4:8"]]
+ 00bbcd08 ["CALL", null, ["callee:00c5c1d0:8"]]
- 00bbbd14 bytes 3b7d0294
+ 00bbcd08 bytes 327d0294
- 00bbbd20 ["INT_ADD", "register:40f0:8", ["const:bbbd20:8", "const:4:8"]]
- 00bbbd20 ["CALL", null, ["callee:00c5c120:8"]]
+ 00bbcd14 ["INT_ADD", "register:40f0:8", ["const:bbcd14:8", "const:4:8"]]
+ 00bbcd14 ["CALL", null, ["callee:00c5c120:8"]]
- 00bbbd20 bytes 0c7d0294
+ 00bbcd14 bytes 037d0294
- 00bbbe38 ["INT_ADD", "register:40f0:8", ["const:bbbe38:8", "const:4:8"]]
- 00bbbe38 ["CALL", null, ["callee:00c5bfe0:8"]]
+ 00bbce2c ["INT_ADD", "register:40f0:8", ["const:bbce2c:8", "const:4:8"]]
+ 00bbce2c ["CALL", null, ["callee:00c5bfe0:8"]]
- 00bbbe38 bytes 767c0294
+ 00bbce2c bytes 6d7c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-715d3e632be226da886cee46f8c6e51a"></a>

### [`00bbbed8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbbed8.md) → [`00bbcecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbc/00bbcecc.md) _ZN8firebase9messaging21UnsubscribeLastResultEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5acb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acb0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bc80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bc80.md) [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5bdf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bdf0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 97.62% / 新版 97.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bbcee8",
      "incomplete_value": true,
      "site": "00bbcee8",
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
      "definition_site": "00bbbef4",
      "incomplete_value": true,
      "site": "00bbbef4",
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
      "definition_site": "00bbcf3c",
      "incomplete_value": false,
      "site": "00bbcf40",
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
            "const:993:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbbf48",
      "incomplete_value": false,
      "site": "00bbbf4c",
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
            "const:8c8:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00bbbef4"
      ],
      [
        "FALL_THROUGH",
        "00bbcee8"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00bbcee8",
      "incomplete_value": true,
      "site": "00bbcf1c",
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
      "definition_site": "00bbbef4",
      "incomplete_value": true,
      "site": "00bbbf28",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bbcee0",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbcf3c",
      "PARAM",
      [
        "storage",
        "002a28c8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bbcee0",
      "READ",
      [
        "storage",
        "01127420",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbcf3c",
      "PARAM",
      [
        "storage",
        "002a2993",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbbf4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbbed8.md#insn-00bbbf4c) · [`00bbbee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbbed8.md#insn-00bbbee8) · [`00bbbeec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbbed8.md#insn-00bbbeec)
- 新版 [`00bbcf40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbc/00bbcecc.md#insn-00bbcf40) · [`00bbcedc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbc/00bbcecc.md#insn-00bbcedc) · [`00bbcee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbc/00bbcecc.md#insn-00bbcee0)

~~~diff
- 00bbbf4c ["INT_ADD", "register:40f0:8", ["const:bbbf4c:8", "const:4:8"]]
- 00bbbf4c ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00bbcf40 ["INT_ADD", "register:40f0:8", ["const:bbcf40:8", "const:4:8"]]
+ 00bbcf40 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00bbbf4c bytes 617c0294
+ 00bbcf40 bytes 587c0294
- 00bbbee8 ["COPY", "register:4048:8", ["const:1126000:8"]]
+ 00bbcedc ["COPY", "register:4048:8", ["const:1127000:8"]]
- 00bbbee8 bytes 492b00f0
+ 00bbcedc bytes 492b00f0
- 00bbbeec ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:460:8"]]
- 00bbbeec ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bbcee0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:420:8"]]
+ 00bbcee0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00bbbeec bytes 293142f9
+ 00bbcee0 bytes 291142f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cdd9e6a302dc74e88a5476a8fe812c16"></a>

### [`00bbbfb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbbfb0.md) → [`00bbcfa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbc/00bbcfa4.md) _ZN8firebase9messaging38DeliveryMetricsExportToBigQueryEnabledEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00497da8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497da8.md) [`00c5c120`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c120.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bbcfb4",
      "incomplete_value": true,
      "site": "00bbcfb4",
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
      "definition_site": "00bbbfc0",
      "incomplete_value": true,
      "site": "00bbbfc0",
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
      "definition_site": "00bbcfc4",
      "incomplete_value": true,
      "site": "00bbcfcc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:458:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbbfd0",
      "incomplete_value": true,
      "site": "00bbbfd8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:498:8"
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
      "definition_site": "00bbcfc8",
      "incomplete_value": true,
      "site": "00bbcfcc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbbfd4",
      "incomplete_value": true,
      "site": "00bbbfd8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3e0:8"
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
      "00bbcfb0",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbcfc4",
      "READ",
      [
        "storage",
        "01126498",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbcfc8",
      "READ",
      [
        "storage",
        "011263e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bbcfb0",
      "READ",
      [
        "storage",
        "01127420",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbcfc4",
      "READ",
      [
        "storage",
        "01127458",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbcfc8",
      "READ",
      [
        "storage",
        "011273a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbbfd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbbfb0.md#insn-00bbbfd8) · [`00bbbfb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbbfb0.md#insn-00bbbfb8) · [`00bbbfbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbbfb0.md#insn-00bbbfbc)
- 新版 [`00bbcfcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbc/00bbcfa4.md#insn-00bbcfcc) · [`00bbcfac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbc/00bbcfa4.md#insn-00bbcfac) · [`00bbcfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbc/00bbcfa4.md#insn-00bbcfb0)

~~~diff
- 00bbbfd8 ["INT_ADD", "register:40f0:8", ["const:bbbfd8:8", "const:4:8"]]
- 00bbbfd8 ["CALL", null, ["callee:00497da8:8"]]
+ 00bbcfcc ["INT_ADD", "register:40f0:8", ["const:bbcfcc:8", "const:4:8"]]
+ 00bbcfcc ["CALL", null, ["callee:00497da8:8"]]
- 00bbbfd8 bytes ac6ee397
+ 00bbcfcc bytes 776be397
- 00bbbfb8 ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00bbcfac ["COPY", "register:4040:8", ["const:1127000:8"]]
- 00bbbfb8 bytes 482b00f0
+ 00bbcfac bytes 482b00f0
- 00bbbfbc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:460:8"]]
- 00bbbfbc ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bbcfb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:420:8"]]
+ 00bbcfb0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00bbbfbc bytes 003142f9
+ 00bbcfb0 bytes 001142f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73672ae399de9d58eb6210c7a42db444"></a>

### [`00bbc070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc070.md) → [`00bbd064`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbd/00bbd064.md) _ZN8firebase9messaging27IsRegistrationOnInitEnabledEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00497a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497a88.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5b150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b150.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00497da8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497da8.md) [`00c5bd40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd40.md) [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md) [`00c5c120`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c120.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 3件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bbd078",
      "incomplete_value": true,
      "site": "00bbd078",
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
      "definition_site": "00bbc084",
      "incomplete_value": true,
      "site": "00bbc084",
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00bbd098",
      "incomplete_value": true,
      "site": "00bbd098",
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
      "definition_site": "00bbc0a4",
      "incomplete_value": true,
      "site": "00bbc0a4",
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
      "definition_site": "00bbd08c",
      "incomplete_value": false,
      "site": "00bbd090",
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
            "const:7f2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbc098",
      "incomplete_value": false,
      "site": "00bbc09c",
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
            "const:71b:8"
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
      "00bbd074",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbd080",
      "PARAM",
      [
        "storage",
        "002a28c8",
        null,
        "string"
      ]
    ],
    [
      "00bbd08c",
      "PARAM",
      [
        "storage",
        "002b071b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bbd074",
      "READ",
      [
        "storage",
        "01127420",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbd080",
      "PARAM",
      [
        "storage",
        "002a2993",
        null,
        "string"
      ]
    ],
    [
      "00bbd08c",
      "PARAM",
      [
        "storage",
        "002b07f2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbc09c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc070.md#insn-00bbc09c) · [`00bbc0bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc070.md#insn-00bbc0bc) · [`00bbc07c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc070.md#insn-00bbc07c)
- 新版 [`00bbd090`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbd/00bbd064.md#insn-00bbd090) · [`00bbd0b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbd/00bbd064.md#insn-00bbd0b0) · [`00bbd070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbd/00bbd064.md#insn-00bbd070)

~~~diff
- 00bbc09c ["INT_ADD", "register:40f0:8", ["const:bbc09c:8", "const:4:8"]]
- 00bbc09c ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00bbd090 ["INT_ADD", "register:40f0:8", ["const:bbd090:8", "const:4:8"]]
+ 00bbd090 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00bbc09c bytes 0d7c0294
+ 00bbd090 bytes 047c0294
- 00bbc0bc ["INT_ADD", "register:40f0:8", ["const:bbc0bc:8", "const:4:8"]]
- 00bbc0bc ["CALL", null, ["callee:00497da8:8"]]
+ 00bbd0b0 ["INT_ADD", "register:40f0:8", ["const:bbd0b0:8", "const:4:8"]]
+ 00bbd0b0 ["CALL", null, ["callee:00497da8:8"]]
- 00bbc0bc bytes 736ee397
+ 00bbd0b0 bytes 3e6be397
- 00bbc07c ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bbd070 ["COPY", "register:4098:8", ["const:1127000:8"]]
- 00bbc07c bytes 532b00d0
+ 00bbd070 bytes 532b00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81037c6d948dedb53d01fc9b42941072"></a>

### [`00bbc0dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc0dc.md) → [`00bbd0d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbd/00bbd0d0.md) _ZN8firebase9messaging8RegisterEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 20件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00bbc344`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc344.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md)
- 新版 呼出元 0件  · 呼出先 20件 [`00497b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`00bbd338`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbd/00bbd338.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 91.45% / 新版 91.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 7件, `store_condition` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bbd100",
      "incomplete_value": true,
      "site": "00bbd100",
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
      "definition_site": "00bbc10c",
      "incomplete_value": true,
      "site": "00bbc10c",
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
      "definition_site": "00bbd10c",
      "incomplete_value": true,
      "site": "00bbd110",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:430:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbc118",
      "incomplete_value": true,
      "site": "00bbc11c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:470:8"
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
      "definition_site": "00bbd144",
      "incomplete_value": true,
      "site": "00bbd148",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:420:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbc150",
      "incomplete_value": true,
      "site": "00bbc154",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:460:8"
              ]
            ]
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
      "00bbd0fc",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbd108",
      "READ",
      [
        "storage",
        "01126470",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbd144",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bbd0fc",
      "READ",
      [
        "storage",
        "01127420",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbd108",
      "READ",
      [
        "storage",
        "01127430",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbd144",
      "READ",
      [
        "storage",
        "01127420",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbc11c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc0dc.md#insn-00bbc11c) · [`00bbc154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc0dc.md#insn-00bbc154) · [`00bbc16c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc0dc.md#insn-00bbc16c)
- 新版 [`00bbd110`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbd/00bbd0d0.md#insn-00bbd110) · [`00bbd148`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbd/00bbd0d0.md#insn-00bbd148) · [`00bbd160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbd/00bbd0d0.md#insn-00bbd160)

~~~diff
- 00bbc11c ["INT_ADD", "register:40f0:8", ["const:bbc11c:8", "const:4:8"]]
- 00bbc11c ["CALL", null, ["callee:00c5baa0:8"]]
+ 00bbd110 ["INT_ADD", "register:40f0:8", ["const:bbd110:8", "const:4:8"]]
+ 00bbd110 ["CALL", null, ["callee:00c5baa0:8"]]
- 00bbc11c bytes 6d7a0294
+ 00bbd110 bytes 647a0294
- 00bbc154 ["INT_ADD", "register:40f0:8", ["const:bbc154:8", "const:4:8"]]
- 00bbc154 ["CALL", null, ["callee:00c5c120:8"]]
+ 00bbd148 ["INT_ADD", "register:40f0:8", ["const:bbd148:8", "const:4:8"]]
+ 00bbd148 ["CALL", null, ["callee:00c5c120:8"]]
- 00bbc154 bytes ff7b0294
+ 00bbd148 bytes f67b0294
- 00bbc16c ["INT_ADD", "register:40f0:8", ["const:bbc16c:8", "const:4:8"]]
- 00bbc16c ["CALL", null, ["callee:00497b94:8"]]
+ 00bbd160 ["INT_ADD", "register:40f0:8", ["const:bbd160:8", "const:4:8"]]
+ 00bbd160 ["CALL", null, ["callee:00497b94:8"]]
- 00bbc16c bytes c26de397
+ 00bbd160 bytes 8d6ae397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78732e73b18435f4cc5552eab8738833"></a>

### [`00bbc344`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc344.md) → [`00bbd338`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbd/00bbd338.md) FUN_00bbd338

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00bbc0dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc0dc.md) [`00bbc534`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc534.md) [`00bbceb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbceb0.md) · 呼出先 8件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) [`00c5acb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acb0.md)
- 新版 呼出元 3件 [`00bbd0d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbd/00bbd0d0.md) [`00bbd528`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbd/00bbd528.md) [`00bbdea4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbd/00bbdea4.md) · 呼出先 8件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bb30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb30.md) [`00c5bc80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bc80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bbd384",
      "incomplete_value": false,
      "site": "00bbd388",
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
            "const:340:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbc390",
      "incomplete_value": false,
      "site": "00bbc394",
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
            "const:380:8"
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
      "definition_site": "00bbd3bc",
      "incomplete_value": false,
      "site": "00bbd3c0",
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
            "const:206:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbc3c8",
      "incomplete_value": false,
      "site": "00bbc3cc",
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
            "const:139:8"
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
      "definition_site": "00bbd3e0",
      "incomplete_value": false,
      "site": "00bbd3e4",
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
            "const:340:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbc3ec",
      "incomplete_value": false,
      "site": "00bbc3f0",
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
            "const:380:8"
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
      "00bbd384",
      "PARAM",
      [
        "storage",
        "01126380",
        null,
        null
      ]
    ],
    [
      "00bbd3bc",
      "PARAM",
      [
        "storage",
        "002ac139",
        null,
        "string"
      ]
    ],
    [
      "00bbd3e0",
      "PARAM",
      [
        "storage",
        "01126380",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bbd384",
      "PARAM",
      [
        "storage",
        "01127340",
        null,
        null
      ]
    ],
    [
      "00bbd3bc",
      "PARAM",
      [
        "storage",
        "002ac206",
        null,
        "string"
      ]
    ],
    [
      "00bbd3e0",
      "PARAM",
      [
        "storage",
        "01127340",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbc394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc344.md#insn-00bbc394) · [`00bbc3cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc344.md#insn-00bbc3cc) · [`00bbc3f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc344.md#insn-00bbc3f0)
- 新版 [`00bbd388`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbd/00bbd338.md#insn-00bbd388) · [`00bbd3c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbd/00bbd338.md#insn-00bbd3c0) · [`00bbd3e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbd/00bbd338.md#insn-00bbd3e4)

~~~diff
- 00bbc394 ["INT_ADD", "register:40f0:8", ["const:bbc394:8", "const:4:8"]]
- 00bbc394 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00bbd388 ["INT_ADD", "register:40f0:8", ["const:bbd388:8", "const:4:8"]]
+ 00bbd388 ["CALL", null, ["callee:00c5baa0:8"]]
- 00bbc394 bytes cf790294
+ 00bbd388 bytes c6790294
- 00bbc3cc ["INT_ADD", "register:40f0:8", ["const:bbc3cc:8", "const:4:8"]]
- 00bbc3cc ["CALL", null, ["callee:00c5be80:8"]]
+ 00bbd3c0 ["INT_ADD", "register:40f0:8", ["const:bbd3c0:8", "const:4:8"]]
+ 00bbd3c0 ["CALL", null, ["callee:00c5be80:8"]]
- 00bbc3cc bytes b97a0294
+ 00bbd3c0 bytes b07a0294
- 00bbc3f0 ["INT_ADD", "register:40f0:8", ["const:bbc3f0:8", "const:4:8"]]
- 00bbc3f0 ["CALL", null, ["callee:00c5bab0:8"]]
+ 00bbd3e4 ["INT_ADD", "register:40f0:8", ["const:bbd3e4:8", "const:4:8"]]
+ 00bbd3e4 ["CALL", null, ["callee:00c5bab0:8"]]
- 00bbc3f0 bytes bc790294
+ 00bbd3e4 bytes b3790294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3db431a7b331c6adddfad66ef357bd57"></a>

### [`00bbc45c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc45c.md) → [`00bbd450`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbd/00bbd450.md) _ZN8firebase9messaging18RegisterLastResultEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5acb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acb0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bc80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bc80.md) [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5bdf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bdf0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 97.62% / 新版 97.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bbd46c",
      "incomplete_value": true,
      "site": "00bbd46c",
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
      "definition_site": "00bbc478",
      "incomplete_value": true,
      "site": "00bbc478",
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
      "definition_site": "00bbd4c0",
      "incomplete_value": false,
      "site": "00bbd4c4",
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
            "const:993:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbc4cc",
      "incomplete_value": false,
      "site": "00bbc4d0",
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
            "const:8c8:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00bbc478"
      ],
      [
        "FALL_THROUGH",
        "00bbd46c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00bbd46c",
      "incomplete_value": true,
      "site": "00bbd4a0",
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
      "definition_site": "00bbc478",
      "incomplete_value": true,
      "site": "00bbc4ac",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bbd464",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbd4c0",
      "PARAM",
      [
        "storage",
        "002a28c8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bbd464",
      "READ",
      [
        "storage",
        "01127420",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbd4c0",
      "PARAM",
      [
        "storage",
        "002a2993",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbc4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc45c.md#insn-00bbc4d0) · [`00bbc46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc45c.md#insn-00bbc46c) · [`00bbc470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc45c.md#insn-00bbc470)
- 新版 [`00bbd4c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbd/00bbd450.md#insn-00bbd4c4) · [`00bbd460`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbd/00bbd450.md#insn-00bbd460) · [`00bbd464`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbd/00bbd450.md#insn-00bbd464)

~~~diff
- 00bbc4d0 ["INT_ADD", "register:40f0:8", ["const:bbc4d0:8", "const:4:8"]]
- 00bbc4d0 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00bbd4c4 ["INT_ADD", "register:40f0:8", ["const:bbd4c4:8", "const:4:8"]]
+ 00bbd4c4 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00bbc4d0 bytes 007b0294
+ 00bbd4c4 bytes f77a0294
- 00bbc46c ["COPY", "register:4048:8", ["const:1126000:8"]]
+ 00bbd460 ["COPY", "register:4048:8", ["const:1127000:8"]]
- 00bbc46c bytes 492b00d0
+ 00bbd460 bytes 492b00d0
- 00bbc470 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:460:8"]]
- 00bbc470 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bbd464 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:420:8"]]
+ 00bbd464 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00bbc470 bytes 293142f9
+ 00bbd464 bytes 291142f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ebfde066edb589ff8971fb7f9a3a434"></a>

### [`00bbc534`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc534.md) → [`00bbd528`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbd/00bbd528.md) _ZN8firebase9messaging10UnregisterEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 20件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00bbc344`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc344.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md)
- 新版 呼出元 0件  · 呼出先 20件 [`00497b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`00bbd338`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbd/00bbd338.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 91.45% / 新版 91.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 5件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bbd558",
      "incomplete_value": true,
      "site": "00bbd558",
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
      "definition_site": "00bbc564",
      "incomplete_value": true,
      "site": "00bbc564",
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
      "definition_site": "00bbd59c",
      "incomplete_value": true,
      "site": "00bbd5a0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:420:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbc5a8",
      "incomplete_value": true,
      "site": "00bbc5ac",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:460:8"
              ]
            ]
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
      "definition_site": "00bbd62c",
      "incomplete_value": false,
      "site": "00bbd630",
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
            "const:993:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbc638",
      "incomplete_value": false,
      "site": "00bbc63c",
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
            "const:8c8:8"
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
      "00bbd554",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbd560",
      "READ",
      [
        "storage",
        "01126470",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbd59c",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bbd554",
      "READ",
      [
        "storage",
        "01127420",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbd560",
      "READ",
      [
        "storage",
        "01127430",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbd59c",
      "READ",
      [
        "storage",
        "01127420",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbc5ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc534.md#insn-00bbc5ac) · [`00bbc63c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc534.md#insn-00bbc63c) · [`00bbc648`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc534.md#insn-00bbc648)
- 新版 [`00bbd5a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbd/00bbd528.md#insn-00bbd5a0) · [`00bbd630`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbd/00bbd528.md#insn-00bbd630) · [`00bbd63c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbd/00bbd528.md#insn-00bbd63c)

~~~diff
- 00bbc5ac ["INT_ADD", "register:40f0:8", ["const:bbc5ac:8", "const:4:8"]]
- 00bbc5ac ["CALL", null, ["callee:00c5c120:8"]]
+ 00bbd5a0 ["INT_ADD", "register:40f0:8", ["const:bbd5a0:8", "const:4:8"]]
+ 00bbd5a0 ["CALL", null, ["callee:00c5c120:8"]]
- 00bbc5ac bytes e97a0294
+ 00bbd5a0 bytes e07a0294
- 00bbc63c ["INT_ADD", "register:40f0:8", ["const:bbc63c:8", "const:4:8"]]
- 00bbc63c ["CALL", null, ["callee:00c5bd40:8"]]
+ 00bbd630 ["INT_ADD", "register:40f0:8", ["const:bbd630:8", "const:4:8"]]
+ 00bbd630 ["CALL", null, ["callee:00c5bd40:8"]]
- 00bbc63c bytes cd790294
+ 00bbd630 bytes c4790294
- 00bbc648 ["INT_ADD", "register:40f0:8", ["const:bbc648:8", "const:4:8"]]
- 00bbc648 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00bbd63c ["INT_ADD", "register:40f0:8", ["const:bbd63c:8", "const:4:8"]]
+ 00bbd63c ["CALL", null, ["callee:00c5c0a0:8"]]
- 00bbc648 bytes a27a0294
+ 00bbd63c bytes 997a0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0be5cd9e6b0899fd0ae5b0e242bd83cf"></a>

### [`00bbc874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc874.md) → [`00bbd868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbd/00bbd868.md) _ZN8firebase9messaging8GetTokenEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5d690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d690.md) · 呼出先 22件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00b44054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b44/00b44054.md) [`00bbcb50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbcb50.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00c5e660`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e660.md) · 呼出先 22件 [`00497b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`00b45048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b45/00b45048.md) [`00bbdb44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbd/00bbdb44.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 92.65% / 新版 92.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 6件, `store_condition` 4件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bbd89c",
      "incomplete_value": true,
      "site": "00bbd89c",
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
      "definition_site": "00bbc8a8",
      "incomplete_value": true,
      "site": "00bbc8a8",
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
      "definition_site": "00bbd8a8",
      "incomplete_value": true,
      "site": "00bbd8ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:430:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbc8b4",
      "incomplete_value": true,
      "site": "00bbc8b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:470:8"
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
      "definition_site": "00bbd8d0",
      "incomplete_value": true,
      "site": "00bbd8e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:758:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbc8dc",
      "incomplete_value": true,
      "site": "00bbc8ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:788:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bbd898",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbd8a4",
      "READ",
      [
        "storage",
        "01126470",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbd8d0",
      "READ",
      [
        "storage",
        "00c9b788",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bbd898",
      "READ",
      [
        "storage",
        "01127420",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbd8a4",
      "READ",
      [
        "storage",
        "01127430",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbd8d0",
      "READ",
      [
        "storage",
        "00c9c758",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbc8b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc874.md#insn-00bbc8b8) · [`00bbc8ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc874.md#insn-00bbc8ec) · [`00bbc908`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc874.md#insn-00bbc908)
- 新版 [`00bbd8ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbd/00bbd868.md#insn-00bbd8ac) · [`00bbd8e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbd/00bbd868.md#insn-00bbd8e0) · [`00bbd8fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbd/00bbd868.md#insn-00bbd8fc)

~~~diff
- 00bbc8b8 ["INT_ADD", "register:40f0:8", ["const:bbc8b8:8", "const:4:8"]]
- 00bbc8b8 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00bbd8ac ["INT_ADD", "register:40f0:8", ["const:bbd8ac:8", "const:4:8"]]
+ 00bbd8ac ["CALL", null, ["callee:00c5baa0:8"]]
- 00bbc8b8 bytes 86780294
+ 00bbd8ac bytes 7d780294
- 00bbc8ec ["INT_ADD", "register:40f0:8", ["const:bbc8ec:8", "const:4:8"]]
- 00bbc8ec ["CALL", null, ["callee:00c5bee0:8"]]
+ 00bbd8e0 ["INT_ADD", "register:40f0:8", ["const:bbd8e0:8", "const:4:8"]]
+ 00bbd8e0 ["CALL", null, ["callee:00c5bee0:8"]]
- 00bbc8ec bytes 89790294
+ 00bbd8e0 bytes 80790294
- 00bbc908 ["INT_ADD", "register:40f0:8", ["const:bbc908:8", "const:4:8"]]
- 00bbc908 ["CALL", null, ["callee:00c5c120:8"]]
+ 00bbd8fc ["INT_ADD", "register:40f0:8", ["const:bbd8fc:8", "const:4:8"]]
+ 00bbd8fc ["CALL", null, ["callee:00c5c120:8"]]
- 00bbc908 bytes 127a0294
+ 00bbd8fc bytes 097a0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eddb6bf892aaec88e0f468cef28c211e"></a>

### [`00bbcb50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbcb50.md) → [`00bbdb44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbd/00bbdb44.md) FUN_00bbdb44

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbc874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc874.md) · 呼出先 15件 [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 1件 [`00bbd868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbd/00bbd868.md) · 呼出先 15件 [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.62% / 新版 96.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bbdb78",
      "incomplete_value": false,
      "site": "00bbdb90",
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
      "definition_site": "00bbcb84",
      "incomplete_value": false,
      "site": "00bbcb9c",
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
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bbdbf8",
      "incomplete_value": false,
      "site": "00bbdbfc",
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
            "const:340:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbcc04",
      "incomplete_value": false,
      "site": "00bbcc08",
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
            "const:380:8"
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
      "definition_site": "00bbdc4c",
      "incomplete_value": false,
      "site": "00bbdc50",
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
            "const:206:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbcc58",
      "incomplete_value": false,
      "site": "00bbcc5c",
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
            "const:139:8"
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
      "00bbdb78",
      "PARAM",
      [
        "storage",
        "002a638e",
        null,
        "undefined1"
      ]
    ],
    [
      "00bbdbf8",
      "PARAM",
      [
        "storage",
        "01126380",
        null,
        null
      ]
    ],
    [
      "00bbdc4c",
      "PARAM",
      [
        "storage",
        "002ac139",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bbdb78",
      "PARAM",
      [
        "storage",
        "002a64e6",
        null,
        "undefined1"
      ]
    ],
    [
      "00bbdbf8",
      "PARAM",
      [
        "storage",
        "01127340",
        null,
        null
      ]
    ],
    [
      "00bbdc4c",
      "PARAM",
      [
        "storage",
        "002ac206",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbcb9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbcb50.md#insn-00bbcb9c) · [`00bbcc08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbcb50.md#insn-00bbcc08) · [`00bbcc5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbcb50.md#insn-00bbcc5c)
- 新版 [`00bbdb90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbd/00bbdb44.md#insn-00bbdb90) · [`00bbdbfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbd/00bbdb44.md#insn-00bbdbfc) · [`00bbdc50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbd/00bbdb44.md#insn-00bbdc50)

~~~diff
- 00bbcb9c ["INT_ADD", "register:40f0:8", ["const:bbcb9c:8", "const:4:8"]]
- 00bbcb9c ["CALL", null, ["callee:00c5c660:8"]]
+ 00bbdb90 ["INT_ADD", "register:40f0:8", ["const:bbdb90:8", "const:4:8"]]
+ 00bbdb90 ["CALL", null, ["callee:00c5c660:8"]]
- 00bbcb9c bytes bd7a0294
+ 00bbdb90 bytes b47a0294
- 00bbcc08 ["INT_ADD", "register:40f0:8", ["const:bbcc08:8", "const:4:8"]]
- 00bbcc08 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00bbdbfc ["INT_ADD", "register:40f0:8", ["const:bbdbfc:8", "const:4:8"]]
+ 00bbdbfc ["CALL", null, ["callee:00c5baa0:8"]]
- 00bbcc08 bytes b2770294
+ 00bbdbfc bytes a9770294
- 00bbcc5c ["INT_ADD", "register:40f0:8", ["const:bbcc5c:8", "const:4:8"]]
- 00bbcc5c ["CALL", null, ["callee:00c5be80:8"]]
+ 00bbdc50 ["INT_ADD", "register:40f0:8", ["const:bbdc50:8", "const:4:8"]]
+ 00bbdc50 ["CALL", null, ["callee:00c5be80:8"]]
- 00bbcc5c bytes 95780294
+ 00bbdc50 bytes 8c780294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c47f789ce52762215fe761cede82ed5"></a>

### [`00bbceb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbceb0.md) → [`00bbdea4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbd/00bbdea4.md) _ZN8firebase9messaging11DeleteTokenEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 20件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00bbc344`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbc344.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md)
- 新版 呼出元 0件  · 呼出先 20件 [`00497b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00497/00497b94.md) [`00bbd338`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbd/00bbd338.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 91.45% / 新版 91.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bbdf18",
      "incomplete_value": true,
      "site": "00bbdf1c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:420:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbcf24",
      "incomplete_value": true,
      "site": "00bbcf28",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:460:8"
              ]
            ]
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
      "definition_site": "00bbdf28",
      "incomplete_value": true,
      "site": "00bbdf34",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:458:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbcf34",
      "incomplete_value": true,
      "site": "00bbcf40",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:498:8"
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
      "definition_site": "00bbdf2c",
      "incomplete_value": true,
      "site": "00bbdf34",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbcf38",
      "incomplete_value": true,
      "site": "00bbcf40",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3f8:8"
              ]
            ]
          ]
        ]
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
      "00bbded0",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbdedc",
      "READ",
      [
        "storage",
        "01126470",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbdf18",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bbded0",
      "READ",
      [
        "storage",
        "01127420",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbdedc",
      "READ",
      [
        "storage",
        "01127430",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbdf18",
      "READ",
      [
        "storage",
        "01127420",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbcf28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbceb0.md#insn-00bbcf28) · [`00bbcf40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbceb0.md#insn-00bbcf40) · [`00bbcfb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbceb0.md#insn-00bbcfb8)
- 新版 [`00bbdf1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbd/00bbdea4.md#insn-00bbdf1c) · [`00bbdf34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbd/00bbdea4.md#insn-00bbdf34) · [`00bbdfac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbd/00bbdea4.md#insn-00bbdfac)

~~~diff
- 00bbcf28 ["INT_ADD", "register:40f0:8", ["const:bbcf28:8", "const:4:8"]]
- 00bbcf28 ["CALL", null, ["callee:00c5c120:8"]]
+ 00bbdf1c ["INT_ADD", "register:40f0:8", ["const:bbdf1c:8", "const:4:8"]]
+ 00bbdf1c ["CALL", null, ["callee:00c5c120:8"]]
- 00bbcf28 bytes 8a780294
+ 00bbdf1c bytes 81780294
- 00bbcf40 ["INT_ADD", "register:40f0:8", ["const:bbcf40:8", "const:4:8"]]
- 00bbcf40 ["CALL", null, ["callee:00497b94:8"]]
+ 00bbdf34 ["INT_ADD", "register:40f0:8", ["const:bbdf34:8", "const:4:8"]]
+ 00bbdf34 ["CALL", null, ["callee:00497b94:8"]]
- 00bbcf40 bytes 4d6ae397
+ 00bbdf34 bytes 1867e397
- 00bbcfb8 ["INT_ADD", "register:40f0:8", ["const:bbcfb8:8", "const:4:8"]]
- 00bbcfb8 ["CALL", null, ["callee:00c5bd40:8"]]
+ 00bbdfac ["INT_ADD", "register:40f0:8", ["const:bbdfac:8", "const:4:8"]]
+ 00bbdfac ["CALL", null, ["callee:00c5bd40:8"]]
- 00bbcfb8 bytes 6e770294
+ 00bbdfac bytes 65770294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9efc3bc9b3a9e68906e3b42edb6a669d"></a>

### [`00bbd118`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd118.md) → [`00bbe10c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe10c.md) _ZN8firebase9messaging21DeleteTokenLastResultEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5acb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acb0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bc80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bc80.md) [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5bdf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bdf0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 97.62% / 新版 97.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bbe128",
      "incomplete_value": true,
      "site": "00bbe128",
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
      "definition_site": "00bbd134",
      "incomplete_value": true,
      "site": "00bbd134",
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
      "definition_site": "00bbe17c",
      "incomplete_value": false,
      "site": "00bbe180",
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
            "const:993:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbd188",
      "incomplete_value": false,
      "site": "00bbd18c",
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
            "const:8c8:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00bbd134"
      ],
      [
        "FALL_THROUGH",
        "00bbe128"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00bbe128",
      "incomplete_value": true,
      "site": "00bbe15c",
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
      "definition_site": "00bbd134",
      "incomplete_value": true,
      "site": "00bbd168",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bbe120",
      "READ",
      [
        "storage",
        "01126460",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbe17c",
      "PARAM",
      [
        "storage",
        "002a28c8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bbe120",
      "READ",
      [
        "storage",
        "01127420",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbe17c",
      "PARAM",
      [
        "storage",
        "002a2993",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbd18c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd118.md#insn-00bbd18c) · [`00bbd128`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd118.md#insn-00bbd128) · [`00bbd12c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd118.md#insn-00bbd12c)
- 新版 [`00bbe180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe10c.md#insn-00bbe180) · [`00bbe11c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe10c.md#insn-00bbe11c) · [`00bbe120`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe10c.md#insn-00bbe120)

~~~diff
- 00bbd18c ["INT_ADD", "register:40f0:8", ["const:bbd18c:8", "const:4:8"]]
- 00bbd18c ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00bbe180 ["INT_ADD", "register:40f0:8", ["const:bbe180:8", "const:4:8"]]
+ 00bbe180 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00bbd18c bytes d1770294
+ 00bbe180 bytes c8770294
- 00bbd128 ["COPY", "register:4048:8", ["const:1126000:8"]]
+ 00bbe11c ["COPY", "register:4048:8", ["const:1127000:8"]]
- 00bbd128 bytes 492b00b0
+ 00bbe11c bytes 492b00b0
- 00bbd12c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:460:8"]]
- 00bbd12c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bbe120 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:420:8"]]
+ 00bbe120 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00bbd12c bytes 293142f9
+ 00bbe120 bytes 291142f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6b101d43cbf7171b4e3175a7258b916"></a>

### [`00bbd1f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd1f4.md) → [`00bbe1e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe1e8.md) FUN_00bbe1e8

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bb9ab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9ab0.md) · 呼出先 4件 [`00bbd25c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd25c.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5d480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d480.md)
- 新版 呼出元 1件 [`00bbaaa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bbaaa4.md) · 呼出先 4件 [`00bbe250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe250.md) [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5e450`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e450.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bbe214",
      "incomplete_value": false,
      "site": "00bbe214",
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
            "const:4c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbd220",
      "incomplete_value": false,
      "site": "00bbd220",
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
            "const:508:8"
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
      "definition_site": "00bbe200",
      "incomplete_value": true,
      "site": "00bbe200",
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
      "definition_site": "00bbd20c",
      "incomplete_value": true,
      "site": "00bbd20c",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00bbd20c"
      ],
      [
        "FALL_THROUGH",
        "00bbe200"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00bbe200",
      "incomplete_value": true,
      "site": "00bbe214",
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
      "definition_site": "00bbd20c",
      "incomplete_value": true,
      "site": "00bbd220",
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
      "00bbe1f8",
      "READ",
      [
        "storage",
        "01126470",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbe214",
      "WRITE",
      [
        "storage",
        "01126508",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bbe1f8",
      "READ",
      [
        "storage",
        "01127430",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbe214",
      "WRITE",
      [
        "storage",
        "011274c8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbd220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd1f4.md#insn-00bbd220) · [`00bbd200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd1f4.md#insn-00bbd200) · [`00bbd204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd1f4.md#insn-00bbd204)
- 新版 [`00bbe214`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe1e8.md#insn-00bbe214) · [`00bbe1f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe1e8.md#insn-00bbe1f4) · [`00bbe1f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe1e8.md#insn-00bbe1f8)

~~~diff
- 00bbd220 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00bbd220 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:508:8"]]
- 00bbd220 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bbe214 ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 00bbe214 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:4c8:8"]]
+ 00bbe214 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bbd220 bytes 09211439
+ 00bbe214 bytes 09211339
- 00bbd200 ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00bbe1f4 ["COPY", "register:4040:8", ["const:1127000:8"]]
- 00bbd200 bytes 482b00b0
+ 00bbe1f4 bytes 482b00b0
- 00bbd204 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:470:8"]]
- 00bbd204 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bbe1f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:430:8"]]
+ 00bbe1f8 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00bbd204 bytes 143942f9
+ 00bbe1f8 bytes 141942f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9349f3cdc70dbbb53f77d011024a00f0"></a>

### [`00bbd25c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd25c.md) → [`00bbe250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe250.md) FUN_00bbe250

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00bbd1f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd1f4.md) [`00bbd3a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd3a4.md) [`00bbd434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd434.md) · 呼出先 4件 [`00bbb738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbb738.md) [`00bbbcdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbb/00bbbcdc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md)
- 新版 呼出元 3件 [`00bbe1e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe1e8.md) [`00bbe398`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe398.md) [`00bbe428`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe428.md) · 呼出先 4件 [`00bbc72c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbc/00bbc72c.md) [`00bbccd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbc/00bbccd0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5bb30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb30.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 91.46% / 新版 91.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

アドレスに依存する影響 `branch_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bbe268",
      "incomplete_value": true,
      "site": "00bbe268",
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
      "definition_site": "00bbd274",
      "incomplete_value": true,
      "site": "00bbd274",
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
      "definition_site": "00bbe2fc",
      "incomplete_value": true,
      "site": "00bbe2fc",
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
      "definition_site": "00bbd308",
      "incomplete_value": true,
      "site": "00bbd308",
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
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bbe32c",
      "incomplete_value": true,
      "site": "00bbe330",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "INT_ADD",
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
      "definition_site": "00bbd338",
      "incomplete_value": true,
      "site": "00bbd33c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "INT_ADD",
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
      "00bbe264",
      "READ",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbe28c",
      "READ",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbe2f8",
      "READ",
      [
        "storage",
        "01126480",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bbe264",
      "READ",
      [
        "storage",
        "01127438",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbe28c",
      "READ",
      [
        "storage",
        "01127438",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbe2f8",
      "READ",
      [
        "storage",
        "01127440",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbd26c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd25c.md#insn-00bbd26c) · [`00bbd270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd25c.md#insn-00bbd270) · [`00bbd294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd25c.md#insn-00bbd294)
- 新版 [`00bbe260`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe250.md#insn-00bbe260) · [`00bbe264`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe250.md#insn-00bbe264) · [`00bbe288`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe250.md#insn-00bbe288)

~~~diff
- 00bbd26c ["COPY", "register:40a8:8", ["const:1126000:8"]]
+ 00bbe260 ["COPY", "register:40a8:8", ["const:1127000:8"]]
- 00bbd26c bytes 552b00b0
+ 00bbe260 bytes 552b00b0
- 00bbd270 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:478:8"]]
- 00bbd270 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bbe264 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:438:8"]]
+ 00bbe264 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00bbd270 bytes b43e42f9
+ 00bbe264 bytes b41e42f9
- 00bbd294 ["INT_ADD", "register:40f0:8", ["const:bbd294:8", "const:4:8"]]
- 00bbd294 ["CALL", null, ["callee:00bbc72c:8"]]
+ 00bbe288 ["INT_ADD", "register:40f0:8", ["const:bbe288:8", "const:4:8"]]
+ 00bbe288 ["CALL", null, ["callee:00bbc72c:8"]]
- 00bbd294 bytes 29f9ff97
+ 00bbe288 bytes 29f9ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e49416e9384af73baa4552420c2039f"></a>

### [`00bbd3a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd3a4.md) → [`00bbe398`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe398.md) FUN_00bbe398

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bb9ab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb9/00bb9ab0.md) · 呼出先 4件 [`00bbd25c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd25c.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5d490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d490.md)
- 新版 呼出元 1件 [`00bbaaa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bba/00bbaaa4.md) · 呼出先 4件 [`00bbe250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe250.md) [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5e460`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e460.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bbe3c4",
      "incomplete_value": false,
      "site": "00bbe3c4",
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
            "const:4c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbd3d0",
      "incomplete_value": false,
      "site": "00bbd3d0",
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
            "const:508:8"
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
      "definition_site": "00bbe3b0",
      "incomplete_value": true,
      "site": "00bbe3b0",
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
      "definition_site": "00bbd3bc",
      "incomplete_value": true,
      "site": "00bbd3bc",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00bbd3bc"
      ],
      [
        "FALL_THROUGH",
        "00bbe3b0"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00bbe3b0",
      "incomplete_value": true,
      "site": "00bbe3c4",
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
      "definition_site": "00bbd3bc",
      "incomplete_value": true,
      "site": "00bbd3d0",
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
      "00bbe3a8",
      "READ",
      [
        "storage",
        "01126470",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbe3c4",
      "WRITE",
      [
        "storage",
        "01126508",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bbe3a8",
      "READ",
      [
        "storage",
        "01127430",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbe3c4",
      "WRITE",
      [
        "storage",
        "011274c8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbd3d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd3a4.md#insn-00bbd3d0) · [`00bbd3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd3a4.md#insn-00bbd3b0) · [`00bbd3b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd3a4.md#insn-00bbd3b4)
- 新版 [`00bbe3c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe398.md#insn-00bbe3c4) · [`00bbe3a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe398.md#insn-00bbe3a4) · [`00bbe3a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe398.md#insn-00bbe3a8)

~~~diff
- 00bbd3d0 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00bbd3d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:508:8"]]
- 00bbd3d0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bbe3c4 ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 00bbe3c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:4c8:8"]]
+ 00bbe3c4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bbd3d0 bytes 09211439
+ 00bbe3c4 bytes 09211339
- 00bbd3b0 ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00bbe3a4 ["COPY", "register:4040:8", ["const:1127000:8"]]
- 00bbd3b0 bytes 482b00b0
+ 00bbe3a4 bytes 482b00b0
- 00bbd3b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:470:8"]]
- 00bbd3b4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bbe3a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:430:8"]]
+ 00bbe3a8 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00bbd3b4 bytes 143942f9
+ 00bbe3a8 bytes 141942f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64815d3492076248cfbddb6623276c46"></a>

### [`00bbd434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd434.md) → [`00bbe428`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe428.md) FUN_00bbe428

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bbafec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bba/00bbafec.md) · 呼出先 4件 [`00bbd25c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd25c.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5d480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d480.md)
- 新版 呼出元 1件 [`00bbbfe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbb/00bbbfe0.md) · 呼出先 4件 [`00bbe250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe250.md) [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5e450`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e450.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 97.22% / 新版 97.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bbe454",
      "incomplete_value": false,
      "site": "00bbe454",
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
            "const:4c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbd460",
      "incomplete_value": false,
      "site": "00bbd460",
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
            "const:508:8"
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
      "definition_site": "00bbe440",
      "incomplete_value": true,
      "site": "00bbe440",
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
      "definition_site": "00bbd44c",
      "incomplete_value": true,
      "site": "00bbd44c",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00bbd44c"
      ],
      [
        "FALL_THROUGH",
        "00bbe440"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00bbe440",
      "incomplete_value": true,
      "site": "00bbe454",
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
      "definition_site": "00bbd44c",
      "incomplete_value": true,
      "site": "00bbd460",
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
      "00bbe438",
      "READ",
      [
        "storage",
        "01126470",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbe454",
      "WRITE",
      [
        "storage",
        "01126508",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bbe438",
      "READ",
      [
        "storage",
        "01127430",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbe454",
      "WRITE",
      [
        "storage",
        "011274c8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbd460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd434.md#insn-00bbd460) · [`00bbd440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd434.md#insn-00bbd440) · [`00bbd444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd434.md#insn-00bbd444)
- 新版 [`00bbe454`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe428.md#insn-00bbe454) · [`00bbe434`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe428.md#insn-00bbe434) · [`00bbe438`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe428.md#insn-00bbe438)

~~~diff
- 00bbd460 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00bbd460 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:508:8"]]
- 00bbd460 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bbe454 ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 00bbe454 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:4c8:8"]]
+ 00bbe454 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bbd460 bytes 09211439
+ 00bbe454 bytes 09211339
- 00bbd440 ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00bbe434 ["COPY", "register:4040:8", ["const:1127000:8"]]
- 00bbd440 bytes 482b00b0
+ 00bbe434 bytes 482b00b0
- 00bbd444 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:470:8"]]
- 00bbd444 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bbe438 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:430:8"]]
+ 00bbe438 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00bbd444 bytes 143942f9
+ 00bbe438 bytes 141942f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-596b1d57085ce0389d2dfff91d2976f7"></a>

### [`00bbd75c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd75c.md) → [`00bbe750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe750.md) _INIT_286

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b655ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b655ac.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c5ad50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad50.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00b665a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b665a0.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c5bd20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd20.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 79.31% / 新版 79.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bbe76c",
      "incomplete_value": false,
      "site": "00bbe770",
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
            "const:318:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbd778",
      "incomplete_value": false,
      "site": "00bbd77c",
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
            "const:358:8"
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
      "definition_site": "00bbe788",
      "incomplete_value": true,
      "site": "00bbe790",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:718:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbd794",
      "incomplete_value": true,
      "site": "00bbd79c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bbe78c",
      "incomplete_value": false,
      "site": "00bbe790",
      "value": [
        "leaf",
        "const:c64030:8"
      ]
    },
    "old": {
      "definition_site": "00bbd798",
      "incomplete_value": false,
      "site": "00bbd79c",
      "value": [
        "leaf",
        "const:c63060:8"
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
      "00bbe76c",
      "PARAM",
      [
        "storage",
        "01126358",
        null,
        null
      ]
    ],
    [
      "00bbe778",
      "READ",
      [
        "storage",
        "00c9b748",
        null,
        "pointer"
      ]
    ],
    [
      "00bbe784",
      "PARAM",
      [
        "storage",
        "01126358",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bbe76c",
      "PARAM",
      [
        "storage",
        "01127318",
        null,
        null
      ]
    ],
    [
      "00bbe778",
      "READ",
      [
        "storage",
        "00c9c718",
        null,
        "pointer"
      ]
    ],
    [
      "00bbe784",
      "PARAM",
      [
        "storage",
        "01127318",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbd77c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd75c.md#insn-00bbd77c) · [`00bbd79c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd75c.md#insn-00bbd79c) · [`00bbd76c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd75c.md#insn-00bbd76c)
- 新版 [`00bbe770`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe750.md#insn-00bbe770) · [`00bbe790`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe750.md#insn-00bbe790) · [`00bbe760`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe750.md#insn-00bbe760)

~~~diff
- 00bbd77c ["INT_ADD", "register:40f0:8", ["const:bbd77c:8", "const:4:8"]]
- 00bbd77c ["CALL", null, ["callee:00c5bd20:8"]]
+ 00bbe770 ["INT_ADD", "register:40f0:8", ["const:bbe770:8", "const:4:8"]]
+ 00bbe770 ["CALL", null, ["callee:00c5bd20:8"]]
- 00bbd77c bytes 75750294
+ 00bbe770 bytes 6c750294
- 00bbd79c ["INT_ADD", "register:40f0:8", ["const:bbd79c:8", "const:4:8"]]
- 00bbd79c ["CALL", null, ["callee:00c58ed0:8"]]
+ 00bbe790 ["INT_ADD", "register:40f0:8", ["const:bbe790:8", "const:4:8"]]
+ 00bbe790 ["CALL", null, ["callee:00c58ed0:8"]]
- 00bbd79c bytes d9690294
+ 00bbe790 bytes d0690294
- 00bbd76c ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bbe760 ["COPY", "register:4098:8", ["const:1127000:8"]]
- 00bbd76c bytes 532b00b0
+ 00bbe760 bytes 532b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67e2d4bbd1d836e773f7b9120e90fd75"></a>

### [`00bc13b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc13b0.md) → [`00bc23a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc2/00bc23a4.md) _INIT_287

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bc1308`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1308.md) [`00bc1310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1310.md) [`00c5ac90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ac90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bc22fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc2/00bc22fc.md) [`00bc2304`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc2/00bc2304.md) [`00c5bc60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bc60.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 41.67% / 新版 41.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 4件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc23c4",
      "incomplete_value": false,
      "site": "00bc23c4",
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
            "const:4d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc13d0",
      "incomplete_value": false,
      "site": "00bc13d0",
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
            "const:510:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc23c4",
      "incomplete_value": false,
      "site": "00bc23c4",
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
            "const:911:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc13d0",
      "incomplete_value": false,
      "site": "00bc13d0",
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
            "const:844:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc23c4",
      "incomplete_value": false,
      "site": "00bc23c4",
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
                "const:1127000:8"
              ],
              [
                "leaf",
                "const:4d0:8"
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
      "definition_site": "00bc13d0",
      "incomplete_value": false,
      "site": "00bc13d0",
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
                "const:1126000:8"
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
      "00bc23b4",
      "PARAM",
      [
        "storage",
        "01126510",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc23c4",
      "WRITE",
      [
        "storage",
        "01126510",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc23c4",
      "DATA",
      [
        "storage",
        "002a9844",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc23b4",
      "PARAM",
      [
        "storage",
        "011274d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc23c4",
      "WRITE",
      [
        "storage",
        "011274d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc23c4",
      "DATA",
      [
        "storage",
        "002a9911",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc13b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc13b0.md#insn-00bc13b0) · [`00bc13b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc13b0.md#insn-00bc13b8) · [`00bc13bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc13b0.md#insn-00bc13bc)
- 新版 [`00bc23a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc2/00bc23a4.md#insn-00bc23a4) · [`00bc23ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc2/00bc23a4.md#insn-00bc23ac) · [`00bc23b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc2/00bc23a4.md#insn-00bc23b0)

~~~diff
- 00bc13b0 ["COPY", "register:4000:8", ["const:1126000:8"]]
+ 00bc23a4 ["COPY", "register:4000:8", ["const:1127000:8"]]
- 00bc13b0 bytes 202b00b0
+ 00bc23a4 bytes 202b00b0
- 00bc13b8 ["COPY", "register:4048:8", ["const:bc1000:8"]]
+ 00bc23ac ["COPY", "register:4048:8", ["const:bc2000:8"]]
- 00bc13b8 bytes 09000090
+ 00bc23ac bytes 09000090
- 00bc13bc ["COPY", "register:4050:8", ["const:bc1000:8"]]
+ 00bc23b0 ["COPY", "register:4050:8", ["const:bc2000:8"]]
- 00bc13bc bytes 0a000090
+ 00bc23b0 bytes 0a000090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3df02c0ba870a64605a3db8b6ee70658"></a>

### [`00bc13e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc13e8.md) → [`00bc23dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc2/00bc23dc.md) _ZN8firebase13remote_config12RemoteConfig11GetInstanceEPNS_3AppE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5ac00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ac00.md) · 呼出先 11件 [`00bc1b00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1b00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5acc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acc0.md)
- 新版 呼出元 1件 [`00c5bbd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bbd0.md) · 呼出先 11件 [`00bc2af4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc2/00bc2af4.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bc90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bc90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.45% / 新版 98.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bc2418",
      "incomplete_value": true,
      "site": "00bc2418",
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
      "definition_site": "00bc1424",
      "incomplete_value": true,
      "site": "00bc1424",
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
      "definition_site": "00bc23fc",
      "incomplete_value": true,
      "site": "00bc2400",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc1408",
      "incomplete_value": true,
      "site": "00bc140c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a00:8"
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
      "definition_site": "00bc2458",
      "incomplete_value": true,
      "site": "00bc245c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc1464",
      "incomplete_value": true,
      "site": "00bc1468",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a00:8"
              ]
            ]
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
      "00bc23f4",
      "READ",
      [
        "storage",
        "00c9ba00",
        null,
        "pointer"
      ]
    ],
    [
      "00bc23fc",
      "PARAM",
      [
        "storage",
        "01126550",
        "_ZN8firebase13remote_config10g_rc_mutexE",
        "undefined1[40]"
      ]
    ],
    [
      "00bc2404",
      "PARAM",
      [
        "storage",
        "01126550",
        "_ZN8firebase13remote_config10g_rc_mutexE",
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00bc23f4",
      "READ",
      [
        "storage",
        "00c9c9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00bc23fc",
      "PARAM",
      [
        "storage",
        "01127510",
        "_ZN8firebase13remote_config10g_rc_mutexE",
        "undefined1[40]"
      ]
    ],
    [
      "00bc2404",
      "PARAM",
      [
        "storage",
        "01127510",
        "_ZN8firebase13remote_config10g_rc_mutexE",
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc140c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc13e8.md#insn-00bc140c) · [`00bc1468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc13e8.md#insn-00bc1468) · [`00bc1488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc13e8.md#insn-00bc1488)
- 新版 [`00bc2400`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc2/00bc23dc.md#insn-00bc2400) · [`00bc245c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc2/00bc23dc.md#insn-00bc245c) · [`00bc247c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc2/00bc23dc.md#insn-00bc247c)

~~~diff
- 00bc140c ["INT_ADD", "register:40f0:8", ["const:bc140c:8", "const:4:8"]]
- 00bc140c ["CALL", null, ["callee:00c5baa0:8"]]
+ 00bc2400 ["INT_ADD", "register:40f0:8", ["const:bc2400:8", "const:4:8"]]
+ 00bc2400 ["CALL", null, ["callee:00c5baa0:8"]]
- 00bc140c bytes b1650294
+ 00bc2400 bytes a8650294
- 00bc1468 ["INT_ADD", "register:40f0:8", ["const:bc1468:8", "const:4:8"]]
- 00bc1468 ["CALL", null, ["callee:00c5bab0:8"]]
+ 00bc245c ["INT_ADD", "register:40f0:8", ["const:bc245c:8", "const:4:8"]]
+ 00bc245c ["CALL", null, ["callee:00c5bab0:8"]]
- 00bc1468 bytes 9e650294
+ 00bc245c bytes 95650294
- 00bc1488 ["INT_ADD", "register:40f0:8", ["const:bc1488:8", "const:4:8"]]
- 00bc1488 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00bc247c ["INT_ADD", "register:40f0:8", ["const:bc247c:8", "const:4:8"]]
+ 00bc247c ["CALL", null, ["callee:00c5c0a0:8"]]
- 00bc1488 bytes 12670294
+ 00bc247c bytes 09670294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b17644e21b7d1ed2f872bb6980091bc2"></a>

### [`00bc181c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc181c.md) → [`00bc2810`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc2/00bc2810.md) _ZN8firebase13remote_config12RemoteConfigC2EPNS_3AppE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md) [`00c5d940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d940.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md) [`00c5e910`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e910.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc2830",
      "incomplete_value": false,
      "site": "00bc2834",
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
      "definition_site": "00bc183c",
      "incomplete_value": false,
      "site": "00bc1840",
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
      "00bc2830",
      "PARAM",
      [
        "storage",
        "002b2609",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc2830",
      "PARAM",
      [
        "storage",
        "002b2653",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc181c.md#insn-00bc1840) · [`00bc183c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc181c.md#insn-00bc183c) · [`00bc184c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc181c.md#insn-00bc184c)
- 新版 [`00bc2834`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc2/00bc2810.md#insn-00bc2834) · [`00bc2830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc2/00bc2810.md#insn-00bc2830) · [`00bc2840`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc2/00bc2810.md#insn-00bc2840)

~~~diff
- 00bc1840 ["INT_ADD", "register:40f0:8", ["const:bc1840:8", "const:4:8"]]
- 00bc1840 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00bc2834 ["INT_ADD", "register:40f0:8", ["const:bc2834:8", "const:4:8"]]
+ 00bc2834 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00bc1840 bytes 24660294
+ 00bc2834 bytes 1b660294
- 00bc183c ["COPY", "tmp:0:8", ["const:609:8"]]
- 00bc183c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bc183c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bc183c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bc2830 ["COPY", "tmp:0:8", ["const:653:8"]]
+ 00bc2830 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc2830 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc2830 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bc183c bytes 00241891
+ 00bc2830 bytes 004c1991
- 00bc184c ["INT_ADD", "register:40f0:8", ["const:bc184c:8", "const:4:8"]]
- 00bc184c ["CALL", null, ["callee:00c58f30:8"]]
+ 00bc2840 ["INT_ADD", "register:40f0:8", ["const:bc2840:8", "const:4:8"]]
+ 00bc2840 ["CALL", null, ["callee:00c58f30:8"]]
- 00bc184c bytes c5590294
+ 00bc2840 bytes bc590294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1e1a4a137743771bcc94d9920ed1347"></a>

### [`00bc1b00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1b00.md) → [`00bc2af4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc2/00bc2af4.md) FUN_00bc2af4

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc13e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc13e8.md) · 呼出先 2件 [`00c5aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aeb0.md) [`00c5d780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d780.md)
- 新版 呼出元 1件 [`00bc23dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc2/00bc23dc.md) · 呼出先 2件 [`00c5be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5be80.md) [`00c5e750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e750.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc2b0c",
      "incomplete_value": false,
      "site": "00bc2b14",
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
            "const:242:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc1b18",
      "incomplete_value": false,
      "site": "00bc1b20",
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
            "const:175:8"
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
      "00bc2b0c",
      "PARAM",
      [
        "storage",
        "002ac175",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc2b0c",
      "PARAM",
      [
        "storage",
        "002ac242",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1b00.md#insn-00bc1b20) · [`00bc1b18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1b00.md#insn-00bc1b18)
- 新版 [`00bc2b14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc2/00bc2af4.md#insn-00bc2b14) · [`00bc2b0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc2/00bc2af4.md#insn-00bc2b0c)

~~~diff
- 00bc1b20 ["INT_ADD", "register:40f0:8", ["const:bc1b20:8", "const:4:8"]]
- 00bc1b20 ["CALL", null, ["callee:00c5be80:8"]]
+ 00bc2b14 ["INT_ADD", "register:40f0:8", ["const:bc2b14:8", "const:4:8"]]
+ 00bc2b14 ["CALL", null, ["callee:00c5be80:8"]]
- 00bc1b20 bytes e4640294
+ 00bc2b14 bytes db640294
- 00bc1b18 ["COPY", "tmp:0:8", ["const:175:8"]]
- 00bc1b18 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bc1b18 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bc1b18 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bc2b0c ["COPY", "tmp:0:8", ["const:242:8"]]
+ 00bc2b0c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc2b0c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bc2b0c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bc1b18 bytes 00d40591
+ 00bc2b0c bytes 00080991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97e65d5c02f4c59b560af863f2b5893b"></a>

### [`00bc1b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1b74.md) → [`00bc2b68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc2/00bc2b68.md) _INIT_288

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00b655ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b655ac.md) [`00bc13e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc13e0.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c5ad50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad50.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00b665a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b665a0.md) [`00bc23d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc2/00bc23d4.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c5bd20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd20.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 2件, `store_destination` 3件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc2b8c",
      "incomplete_value": true,
      "site": "00bc2b8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bc1b98",
      "incomplete_value": true,
      "site": "00bc1b98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc2b98",
      "incomplete_value": true,
      "site": "00bc2b98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bc1ba4",
      "incomplete_value": true,
      "site": "00bc1ba4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bc2b9c",
      "incomplete_value": true,
      "site": "00bc2b9c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc1ba8",
      "incomplete_value": true,
      "site": "00bc1ba8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a08:8"
              ]
            ]
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
      "00bc2b78",
      "READ",
      [
        "storage",
        "00c9ba08",
        null,
        "pointer"
      ]
    ],
    [
      "00bc2b78",
      "PARAM",
      [
        "storage",
        "01126538",
        "_ZN8firebase13remote_config5g_rcsE",
        "undefined8"
      ]
    ],
    [
      "00bc2b8c",
      "WRITE",
      [
        "storage",
        "01126540",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc2b78",
      "READ",
      [
        "storage",
        "00c9c9d8",
        null,
        "pointer"
      ]
    ],
    [
      "00bc2b78",
      "PARAM",
      [
        "storage",
        "011274f8",
        "_ZN8firebase13remote_config5g_rcsE",
        "undefined8"
      ]
    ],
    [
      "00bc2b8c",
      "WRITE",
      [
        "storage",
        "01127500",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1b74.md#insn-00bc1bac) · [`00bc1bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1b74.md#insn-00bc1bc0) · [`00bc1b80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1b74.md#insn-00bc1b80)
- 新版 [`00bc2ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc2/00bc2b68.md#insn-00bc2ba0) · [`00bc2bb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc2/00bc2b68.md#insn-00bc2bb4) · [`00bc2b74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc2/00bc2b68.md#insn-00bc2b74)

~~~diff
- 00bc1bac ["INT_ADD", "register:40f0:8", ["const:bc1bac:8", "const:4:8"]]
- 00bc1bac ["CALL", null, ["callee:00c58ed0:8"]]
+ 00bc2ba0 ["INT_ADD", "register:40f0:8", ["const:bc2ba0:8", "const:4:8"]]
+ 00bc2ba0 ["CALL", null, ["callee:00c58ed0:8"]]
- 00bc1bac bytes d5580294
+ 00bc2ba0 bytes cc580294
- 00bc1bc0 ["INT_ADD", "register:40f0:8", ["const:bc1bc0:8", "const:4:8"]]
- 00bc1bc0 ["CALL", null, ["callee:00c5bd20:8"]]
+ 00bc2bb4 ["INT_ADD", "register:40f0:8", ["const:bc2bb4:8", "const:4:8"]]
+ 00bc2bb4 ["CALL", null, ["callee:00c5bd20:8"]]
- 00bc1bc0 bytes 64640294
+ 00bc2bb4 bytes 5b640294
- 00bc1b80 ["COPY", "register:4008:8", ["const:c9b000:8"]]
+ 00bc2b74 ["COPY", "register:4008:8", ["const:c9c000:8"]]
- 00bc1b80 bytes c10600d0
+ 00bc2b74 bytes c10600d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4d7337c9a054872f297d83e59240eff"></a>

### [`00bc1be0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1be0.md) → [`00bc2bd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc2/00bc2bd4.md) _ZN8firebase13remote_config8internal6config19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS7_9allo

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
      "definition_site": "00bc2c00",
      "incomplete_value": true,
      "site": "00bc2c00",
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
            "const:538:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc1c0c",
      "incomplete_value": true,
      "site": "00bc1c0c",
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
            "const:578:8"
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
      "definition_site": "00bc2be8",
      "incomplete_value": true,
      "site": "00bc2be8",
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
      "definition_site": "00bc1bf4",
      "incomplete_value": true,
      "site": "00bc1bf4",
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
      "definition_site": "00bc2bf4",
      "incomplete_value": false,
      "site": "00bc2bf8",
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
            "const:711:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc1c00",
      "incomplete_value": false,
      "site": "00bc1c04",
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
            "const:63a:8"
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
      "00bc2be4",
      "READ",
      [
        "storage",
        "01126578",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2bf4",
      "PARAM",
      [
        "storage",
        "002b163a",
        null,
        "string"
      ]
    ],
    [
      "00bc2c00",
      "WRITE",
      [
        "storage",
        "01126578",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bc2be4",
      "READ",
      [
        "storage",
        "01127538",
        null,
        "undefined8"
      ]
    ],
    [
      "00bc2bf4",
      "PARAM",
      [
        "storage",
        "002b1711",
        null,
        "string"
      ]
    ],
    [
      "00bc2c00",
      "WRITE",
      [
        "storage",
        "01127538",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc1c04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1be0.md#insn-00bc1c04) · [`00bc1c0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1be0.md#insn-00bc1c0c) · [`00bc1bec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1be0.md#insn-00bc1bec)
- 新版 [`00bc2bf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc2/00bc2bd4.md#insn-00bc2bf8) · [`00bc2c00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc2/00bc2bd4.md#insn-00bc2c00) · [`00bc2be0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc2/00bc2bd4.md#insn-00bc2be0)

~~~diff
- 00bc1c04 ["INT_ADD", "register:40f0:8", ["const:bc1c04:8", "const:4:8"]]
- 00bc1c04 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00bc2bf8 ["INT_ADD", "register:40f0:8", ["const:bc2bf8:8", "const:4:8"]]
+ 00bc2bf8 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00bc1c04 bytes f7640294
+ 00bc2bf8 bytes ee640294
- 00bc1c0c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:578:8"]]
- 00bc1c0c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bc2c00 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:538:8"]]
+ 00bc2c00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bc1c0c bytes 60be02f9
+ 00bc2c00 bytes 609e02f9
- 00bc1bec ["COPY", "register:4098:8", ["const:1126000:8"]]
+ 00bc2be0 ["COPY", "register:4098:8", ["const:1127000:8"]]
- 00bc1bec bytes 332b00b0
+ 00bc2be0 bytes 332b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

