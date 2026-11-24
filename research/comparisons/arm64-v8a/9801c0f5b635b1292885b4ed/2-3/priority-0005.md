# v16.0.1 → v16.0.2 · 最優先の変更候補 (5)

[一覧の目次](README.md)

<a id="compare-b2d5f4b75f41d53291b2ae776801a62b"></a>

### [`00473394`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473394.md) → [`004733d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/004733d4.md) FUN_004733d4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0089d4c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089d/0089d4c8.md) · 呼出先 7件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00473540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473540.md) [`0047975c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/0047975c.md) [`00479760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479760.md) [`005509a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509a0.md)
- 新版 呼出元 1件 [`0089d520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089d/0089d520.md) · 呼出先 7件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00473580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/00473580.md) [`0047979c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00479/0047979c.md) [`004797a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00479/004797a0.md) [`005509e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/005509e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.50% / 新版 97.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0047344c",
      "incomplete_value": false,
      "site": "0047344c",
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
            "const:30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047340c",
      "incomplete_value": false,
      "site": "0047340c",
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
            "const:f60:8"
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
      "0047344c",
      "DATA",
      [
        "storage",
        "00c64f60",
        null,
        "undefined *"
      ]
    ],
    [
      "00473488",
      "READ",
      [
        "storage",
        "00c64f80",
        null,
        "pointer"
      ]
    ],
    [
      "00473488",
      "READ",
      [
        "storage",
        "00c64f88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047344c",
      "DATA",
      [
        "storage",
        "00c65030",
        null,
        "undefined *"
      ]
    ],
    [
      "00473488",
      "READ",
      [
        "storage",
        "00c65050",
        null,
        "pointer"
      ]
    ],
    [
      "00473488",
      "READ",
      [
        "storage",
        "00c65058",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047344c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473394.md#insn-0047344c) · [`004733f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473394.md#insn-004733f0) · [`00473400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473394.md#insn-00473400)
- 新版 `0047348c`（命令位置の公開資料なし） · `00473430`（命令位置の公開資料なし） · `00473440`（命令位置の公開資料なし）

~~~diff
- 0047344c ["COPY", "register:0:8", ["register:4040:8"]]
- 0047344c ["INT_ADD", "register:40f0:8", ["const:47344c:8", "const:4:8"]]
- 0047344c ["CALLIND", null, ["register:0:8"]]
+ 0047348c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047348c ["INT_ADD", "register:40f0:8", ["const:47348c:8", "const:4:8"]]
+ 0047348c ["CALLIND", null, ["register:0:8"]]
- 0047344c bytes 00013fd6
+ 0047348c bytes 00013fd6
- 004733f0 ["INT_ADD", "register:40f0:8", ["const:4733f0:8", "const:4:8"]]
- 004733f0 ["CALL", null, ["callee:0043bb60:8"]]
+ 00473430 ["INT_ADD", "register:40f0:8", ["const:473430:8", "const:4:8"]]
+ 00473430 ["CALL", null, ["callee:0043bb60:8"]]
- 004733f0 bytes cc21ff97
+ 00473430 bytes cc21ff97
- 00473400 ["INT_ADD", "register:40f0:8", ["const:473400:8", "const:4:8"]]
- 00473400 ["CALL", null, ["callee:00473580:8"]]
+ 00473440 ["INT_ADD", "register:40f0:8", ["const:473440:8", "const:4:8"]]
+ 00473440 ["CALL", null, ["callee:00473580:8"]]
- 00473400 bytes 50000094
+ 00473440 bytes 50000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cbc9c6292914901986caf0aa0de57082"></a>

### [`00473690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473690.md) → [`004736d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/004736d0.md) FUN_004736d0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 4件 [`00479814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479814.md) [`00479818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479818.md) [`005509a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509a0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) · 呼出先 4件 [`00479854`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00479/00479854.md) [`00479858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00479/00479858.md) [`005509e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/005509e0.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

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
      "definition_site": "0047370c",
      "incomplete_value": false,
      "site": "0047370c",
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
            "const:c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004736cc",
      "incomplete_value": false,
      "site": "004736cc",
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
            "const:ff0:8"
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
      "0047370c",
      "DATA",
      [
        "storage",
        "00c64ff0",
        null,
        "undefined *"
      ]
    ],
    [
      "00473744",
      "READ",
      [
        "storage",
        "00c65010",
        null,
        "pointer"
      ]
    ],
    [
      "00473744",
      "READ",
      [
        "storage",
        "00c65018",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047370c",
      "DATA",
      [
        "storage",
        "00c650c0",
        null,
        "undefined *"
      ]
    ],
    [
      "00473744",
      "READ",
      [
        "storage",
        "00c650e0",
        null,
        "pointer"
      ]
    ],
    [
      "00473744",
      "READ",
      [
        "storage",
        "00c650e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004736c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473690.md#insn-004736c4) · [`004736c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473690.md#insn-004736c8) · [`004736dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473690.md#insn-004736dc)
- 新版 `00473704`（命令位置の公開資料なし） · `00473708`（命令位置の公開資料なし） · `0047371c`（命令位置の公開資料なし）

~~~diff
- 004736c4 ["COPY", "register:4048:8", ["const:c64000:8"]]
+ 00473704 ["COPY", "register:4048:8", ["const:c65000:8"]]
- 004736c4 bytes 893f00b0
+ 00473704 bytes 893f00d0
- 004736c8 ["COPY", "tmp:0:8", ["const:ff0:8"]]
- 004736c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004736c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004736c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00473708 ["COPY", "tmp:0:8", ["const:c0:8"]]
+ 00473708 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00473708 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00473708 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004736c8 bytes 29c13f91
+ 00473708 bytes 29010391
- 004736dc ["INT_ADD", "register:40f0:8", ["const:4736dc:8", "const:4:8"]]
- 004736dc ["CALL", null, ["callee:005509e0:8"]]
+ 0047371c ["INT_ADD", "register:40f0:8", ["const:47371c:8", "const:4:8"]]
+ 0047371c ["CALL", null, ["callee:005509e0:8"]]
- 004736dc bytes b1740394
+ 0047371c bytes b1740394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eccd78d624fc4cfa75ba377940f461e4"></a>

### [`0047377c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/0047377c.md) → [`004737bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/004737bc.md) FUN_004737bc

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0088c120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c120.md) [`00893dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/00893dbc.md) [`0089d4c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089d/0089d4c8.md) · 呼出先 20件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044b584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b584.md) [`00474198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474198.md) [`00479ae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479ae8.md) [`00479f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479f4c.md)
- 新版 呼出元 3件 [`0088c178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c178.md) [`00893e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00893/00893e14.md) [`0089d520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089d/0089d520.md) · 呼出先 20件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0044b5c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b5c4.md) [`004741d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00474/004741d8.md) [`00479b28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00479/00479b28.md) [`00479f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00479/00479f8c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.02% / 新版 96.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00473878",
      "incomplete_value": true,
      "site": "00473888",
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
                "const:7d7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00473838",
      "incomplete_value": true,
      "site": "00473848",
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
                "const:833:8"
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
      "definition_site": "0047387c",
      "incomplete_value": true,
      "site": "0047388c",
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
                "const:a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047383c",
      "incomplete_value": true,
      "site": "0047384c",
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
                "const:a:8"
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
      "definition_site": "00473880",
      "incomplete_value": true,
      "site": "00473890",
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
                "const:ad0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00473840",
      "incomplete_value": true,
      "site": "00473850",
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
                "const:a90:8"
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
      "00473878",
      "READ",
      [
        "storage",
        "002af833",
        null,
        "string"
      ]
    ],
    [
      "0047387c",
      "READ",
      [
        "storage",
        "002af83d",
        null,
        "string"
      ]
    ],
    [
      "00473880",
      "READ",
      [
        "storage",
        "002c2a90",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00473878",
      "READ",
      [
        "storage",
        "002af7d7",
        null,
        "string"
      ]
    ],
    [
      "0047387c",
      "READ",
      [
        "storage",
        "002af7e1",
        null,
        "string"
      ]
    ],
    [
      "00473880",
      "READ",
      [
        "storage",
        "002c2ad0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047380c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/0047377c.md#insn-0047380c) · [`0047386c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/0047377c.md#insn-0047386c) · [`00473a38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/0047377c.md#insn-00473a38)
- 新版 `0047384c`（命令位置の公開資料なし） · `004738ac`（命令位置の公開資料なし） · `00473a78`（命令位置の公開資料なし）

~~~diff
- 0047380c ["INT_ADD", "register:40f0:8", ["const:47380c:8", "const:4:8"]]
- 0047380c ["CALL", null, ["callee:00c57f80:8"]]
+ 0047384c ["INT_ADD", "register:40f0:8", ["const:47384c:8", "const:4:8"]]
+ 0047384c ["CALL", null, ["callee:00c57f80:8"]]
- 0047380c bytes a9911f94
+ 0047384c bytes cd911f94
- 0047386c ["INT_ADD", "register:40f0:8", ["const:47386c:8", "const:4:8"]]
- 0047386c ["CALL", null, ["callee:004741d8:8"]]
+ 004738ac ["INT_ADD", "register:40f0:8", ["const:4738ac:8", "const:4:8"]]
+ 004738ac ["CALL", null, ["callee:004741d8:8"]]
- 0047386c bytes 4b020094
+ 004738ac bytes 4b020094
- 00473a38 ["INT_ADD", "register:40f0:8", ["const:473a38:8", "const:4:8"]]
- 00473a38 ["CALL", null, ["callee:00c58040:8"]]
+ 00473a78 ["INT_ADD", "register:40f0:8", ["const:473a78:8", "const:4:8"]]
+ 00473a78 ["CALL", null, ["callee:00c58040:8"]]
- 00473a38 bytes 4e911f94
+ 00473a78 bytes 72911f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76034d656d7b91c6db75670dd5f656f7"></a>

### [`00474198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474198.md) → [`004741d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00474/004741d8.md) FUN_004741d8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 17件 [`0047377c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/0047377c.md) [`00474198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474198.md) [`004761a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/004761a4.md) [`0048c000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048c000.md) [`00623f68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00623/00623f68.md) · 呼出先 23件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)
- 新版 呼出元 18件 [`004737bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/004737bc.md) [`004741d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00474/004741d8.md) [`004761e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00476/004761e4.md) [`0048c040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048c040.md) [`00623fa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00623/00623fa8.md) · 呼出先 23件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`00441d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441d2c.md)

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
      "definition_site": "00474328",
      "incomplete_value": false,
      "site": "00474330",
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
            "const:f93:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004742e8",
      "incomplete_value": false,
      "site": "004742f0",
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
            "const:f53:8"
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
      "definition_site": "004743e4",
      "incomplete_value": false,
      "site": "004743ec",
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
            "const:e27:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004743a4",
      "incomplete_value": false,
      "site": "004743ac",
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
            "const:de7:8"
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
      "definition_site": "004743fc",
      "incomplete_value": false,
      "site": "00474408",
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
            "const:f29:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004743bc",
      "incomplete_value": false,
      "site": "004743c8",
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
            "const:ee9:8"
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
      "00474328",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "004743e4",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ],
    [
      "004743fc",
      "PARAM",
      [
        "storage",
        "002c0ee9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00474328",
      "PARAM",
      [
        "storage",
        "002b7f93",
        null,
        null
      ]
    ],
    [
      "004743e4",
      "PARAM",
      [
        "storage",
        "002b5e27",
        null,
        null
      ]
    ],
    [
      "004743fc",
      "PARAM",
      [
        "storage",
        "002c0f29",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004742f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474198.md#insn-004742f0) · [`004743ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474198.md#insn-004743ac) · [`004743c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474198.md#insn-004743c8)
- 新版 `00474330`（命令位置の公開資料なし） · `004743ec`（命令位置の公開資料なし） · `00474408`（命令位置の公開資料なし）

~~~diff
- 004742f0 ["INT_ADD", "register:40f0:8", ["const:4742f0:8", "const:4:8"]]
- 004742f0 ["CALL", null, ["callee:00441ed4:8"]]
+ 00474330 ["INT_ADD", "register:40f0:8", ["const:474330:8", "const:4:8"]]
+ 00474330 ["CALL", null, ["callee:00441ed4:8"]]
- 004742f0 bytes e936ff97
+ 00474330 bytes e936ff97
- 004743ac ["INT_ADD", "register:40f0:8", ["const:4743ac:8", "const:4:8"]]
- 004743ac ["CALL", null, ["callee:00441ed4:8"]]
+ 004743ec ["INT_ADD", "register:40f0:8", ["const:4743ec:8", "const:4:8"]]
+ 004743ec ["CALL", null, ["callee:00441ed4:8"]]
- 004743ac bytes ba36ff97
+ 004743ec bytes ba36ff97
- 004743c8 ["INT_ADD", "register:40f0:8", ["const:4743c8:8", "const:4:8"]]
- 004743c8 ["CALL", null, ["callee:00442834:8"]]
+ 00474408 ["INT_ADD", "register:40f0:8", ["const:474408:8", "const:4:8"]]
+ 00474408 ["CALL", null, ["callee:00442834:8"]]
- 004743c8 bytes 0b39ff97
+ 00474408 bytes 0b39ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e6b57c8fb4293b489992d70df041cdb"></a>

### [`00474ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474ab8.md) → [`00474af8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00474/00474af8.md) FUN_00474af8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)

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
      "definition_site": "00474afc",
      "incomplete_value": false,
      "site": "00474b00",
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
            "const:e80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00474abc",
      "incomplete_value": false,
      "site": "00474ac0",
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
            "const:db0:8"
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
      "00474b00",
      "DATA",
      [
        "storage",
        "00c64db0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00474b00",
      "DATA",
      [
        "storage",
        "00c64e80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00474abc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474ab8.md#insn-00474abc)
- 新版 `00474afc`（命令位置の公開資料なし）

~~~diff
- 00474abc ["COPY", "tmp:0:8", ["const:db0:8"]]
- 00474abc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00474abc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00474abc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00474afc ["COPY", "tmp:0:8", ["const:e80:8"]]
+ 00474afc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00474afc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00474afc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00474abc bytes 08c13691
+ 00474afc bytes 08013a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ac7cbc129e0eaf5e23f07c62cbe4c02"></a>

### [`00474ac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474ac8.md) → [`00474b08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00474/00474b08.md) FUN_00474b08

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00474b18",
      "incomplete_value": false,
      "site": "00474b20",
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
            "const:e80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00474ad8",
      "incomplete_value": false,
      "site": "00474ae0",
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
            "const:db0:8"
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
      "00474b20",
      "DATA",
      [
        "storage",
        "00c64db0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00474b20",
      "DATA",
      [
        "storage",
        "00c64e80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00474ad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474ac8.md#insn-00474ad8) · [`00474ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474ac8.md#insn-00474ae4)
- 新版 `00474b18`（命令位置の公開資料なし） · `00474b24`（命令位置の公開資料なし）

~~~diff
- 00474ad8 ["COPY", "tmp:0:8", ["const:db0:8"]]
- 00474ad8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00474ad8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00474ad8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00474b18 ["COPY", "tmp:0:8", ["const:e80:8"]]
+ 00474b18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00474b18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00474b18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00474ad8 bytes 08c13691
+ 00474b18 bytes 08013a91
- 00474ae4 ["INT_ADD", "register:40f0:8", ["const:474ae4:8", "const:4:8"]]
- 00474ae4 ["CALL", null, ["callee:00c57f70:8"]]
+ 00474b24 ["INT_ADD", "register:40f0:8", ["const:474b24:8", "const:4:8"]]
+ 00474b24 ["CALL", null, ["callee:00c57f70:8"]]
- 00474ae4 bytes ef8c1f94
+ 00474b24 bytes 138d1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d03beba4b7af63abaebc767a5c42073b"></a>

### [`00474cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474cbc.md) → [`00474cfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00474/00474cfc.md) FUN_00474cfc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)

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
      "definition_site": "00474d00",
      "incomplete_value": false,
      "site": "00474d04",
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
            "const:ed0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00474cc0",
      "incomplete_value": false,
      "site": "00474cc4",
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
            "const:e00:8"
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
      "00474d04",
      "DATA",
      [
        "storage",
        "00c64e00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00474d04",
      "DATA",
      [
        "storage",
        "00c64ed0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00474cc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474cbc.md#insn-00474cc0)
- 新版 `00474d00`（命令位置の公開資料なし）

~~~diff
- 00474cc0 ["COPY", "tmp:0:8", ["const:e00:8"]]
- 00474cc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00474cc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00474cc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00474d00 ["COPY", "tmp:0:8", ["const:ed0:8"]]
+ 00474d00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00474d00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00474d00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00474cc0 bytes 08013891
+ 00474d00 bytes 08413b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f08ca53c7ab676d814d1eb31d507488"></a>

### [`00474ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474ccc.md) → [`00474d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00474/00474d0c.md) FUN_00474d0c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00474d1c",
      "incomplete_value": false,
      "site": "00474d24",
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
            "const:ed0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00474cdc",
      "incomplete_value": false,
      "site": "00474ce4",
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
            "const:e00:8"
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
      "00474d24",
      "DATA",
      [
        "storage",
        "00c64e00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00474d24",
      "DATA",
      [
        "storage",
        "00c64ed0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00474cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474ccc.md#insn-00474cdc) · [`00474ce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474ccc.md#insn-00474ce8)
- 新版 `00474d1c`（命令位置の公開資料なし） · `00474d28`（命令位置の公開資料なし）

~~~diff
- 00474cdc ["COPY", "tmp:0:8", ["const:e00:8"]]
- 00474cdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00474cdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00474cdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00474d1c ["COPY", "tmp:0:8", ["const:ed0:8"]]
+ 00474d1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00474d1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00474d1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00474cdc bytes 08013891
+ 00474d1c bytes 08413b91
- 00474ce8 ["INT_ADD", "register:40f0:8", ["const:474ce8:8", "const:4:8"]]
- 00474ce8 ["CALL", null, ["callee:00c57f70:8"]]
+ 00474d28 ["INT_ADD", "register:40f0:8", ["const:474d28:8", "const:4:8"]]
+ 00474d28 ["CALL", null, ["callee:00c57f70:8"]]
- 00474ce8 bytes 6e8c1f94
+ 00474d28 bytes 928c1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-faa8480a0467d75300aa44243fcbfa37"></a>

### [`00475830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475830.md) → [`00475870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00475/00475870.md) FUN_00475870

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00475894",
      "incomplete_value": false,
      "site": "00475894",
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
            "const:f20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00475854",
      "incomplete_value": false,
      "site": "00475854",
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
            "const:e50:8"
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
      "00475894",
      "DATA",
      [
        "storage",
        "00c64e50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00475894",
      "DATA",
      [
        "storage",
        "00c64f20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00475844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475830.md#insn-00475844) · [`00475850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475830.md#insn-00475850)
- 新版 `00475884`（命令位置の公開資料なし） · `00475890`（命令位置の公開資料なし）

~~~diff
- 00475844 ["INT_ADD", "register:40f0:8", ["const:475844:8", "const:4:8"]]
- 00475844 ["CALL", null, ["callee:00c57f60:8"]]
+ 00475884 ["INT_ADD", "register:40f0:8", ["const:475884:8", "const:4:8"]]
+ 00475884 ["CALL", null, ["callee:00c57f60:8"]]
- 00475844 bytes 93891f94
+ 00475884 bytes b7891f94
- 00475850 ["COPY", "tmp:0:8", ["const:e50:8"]]
- 00475850 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00475850 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00475850 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00475890 ["COPY", "tmp:0:8", ["const:f20:8"]]
+ 00475890 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00475890 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00475890 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00475850 bytes 08413991
+ 00475890 bytes 08813c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a82b1f2fafdea4a32ad652375ec0a9d9"></a>

### [`00475864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475864.md) → [`004758a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00475/004758a4.md) FUN_004758a4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "004758b0",
      "incomplete_value": false,
      "site": "004758b0",
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
            "const:f20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00475870",
      "incomplete_value": false,
      "site": "00475870",
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
            "const:e50:8"
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
      "004758b0",
      "DATA",
      [
        "storage",
        "00c64e50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004758b0",
      "DATA",
      [
        "storage",
        "00c64f20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047586c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475864.md#insn-0047586c)
- 新版 `004758ac`（命令位置の公開資料なし）

~~~diff
- 0047586c ["COPY", "tmp:0:8", ["const:e50:8"]]
- 0047586c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0047586c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0047586c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004758ac ["COPY", "tmp:0:8", ["const:f20:8"]]
+ 004758ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004758ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004758ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0047586c bytes 29413991
+ 004758ac bytes 29813c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5cde623ebdf73db8d33004283743a0fb"></a>

### [`00475da0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475da0.md) → [`00475de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00475/00475de0.md) FUN_00475de0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00473270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473270.md) · 呼出先 16件 [`004761a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/004761a4.md) [`00476588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/00476588.md) [`00478cc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478cc4.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)
- 新版 呼出元 1件 [`004732b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/004732b0.md) · 呼出先 16件 [`004761e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00476/004761e4.md) [`004765c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00476/004765c8.md) [`00478d04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00478/00478d04.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.54% / 新版 98.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00475e34",
      "incomplete_value": false,
      "site": "00475e38",
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
            "const:45:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00475df4",
      "incomplete_value": false,
      "site": "00475df8",
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
            "const:5:8"
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
      "definition_site": "00476078",
      "incomplete_value": false,
      "site": "0047607c",
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
            "const:3a5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00476038",
      "incomplete_value": false,
      "site": "0047603c",
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
            "const:3f9:8"
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
      "00475e34",
      "PARAM",
      [
        "storage",
        "002b8005",
        null,
        "string"
      ]
    ],
    [
      "00475e48",
      "READ",
      [
        "storage",
        "002c4400",
        null,
        "undefined8"
      ]
    ],
    [
      "00476078",
      "PARAM",
      [
        "storage",
        "002bc3f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00475e34",
      "PARAM",
      [
        "storage",
        "002b8045",
        null,
        "string"
      ]
    ],
    [
      "00475e48",
      "READ",
      [
        "storage",
        "002c4440",
        null,
        "undefined8"
      ]
    ],
    [
      "00476078",
      "PARAM",
      [
        "storage",
        "002bc3a5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00475df8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475da0.md#insn-00475df8) · [`00475ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475da0.md#insn-00475ffc) · [`0047603c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475da0.md#insn-0047603c)
- 新版 `00475e38`（命令位置の公開資料なし） · `0047603c`（命令位置の公開資料なし） · `0047607c`（命令位置の公開資料なし）

~~~diff
- 00475df8 ["INT_ADD", "register:40f0:8", ["const:475df8:8", "const:4:8"]]
- 00475df8 ["CALL", null, ["callee:00c58540:8"]]
+ 00475e38 ["INT_ADD", "register:40f0:8", ["const:475e38:8", "const:4:8"]]
+ 00475e38 ["CALL", null, ["callee:00c58540:8"]]
- 00475df8 bytes 9e891f94
+ 00475e38 bytes c2891f94
- 00475ffc ["INT_ADD", "register:40f0:8", ["const:475ffc:8", "const:4:8"]]
- 00475ffc ["CALL", null, ["callee:00c581c0:8"]]
+ 0047603c ["INT_ADD", "register:40f0:8", ["const:47603c:8", "const:4:8"]]
+ 0047603c ["CALL", null, ["callee:00c581c0:8"]]
- 00475ffc bytes 3d881f94
+ 0047603c bytes 61881f94
- 0047603c ["INT_ADD", "register:40f0:8", ["const:47603c:8", "const:4:8"]]
- 0047603c ["CALL", null, ["callee:00c58540:8"]]
+ 0047607c ["INT_ADD", "register:40f0:8", ["const:47607c:8", "const:4:8"]]
+ 0047607c ["CALL", null, ["callee:00c58540:8"]]
- 0047603c bytes 0d891f94
+ 0047607c bytes 31891f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6bf264f295a824b8cd3f142ee3a7434"></a>

### [`004761a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/004761a4.md) → [`004761e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00476/004761e4.md) FUN_004761e4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00475da0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475da0.md) · 呼出先 11件 [`00474198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474198.md) [`004766c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/004766c8.md) [`00476b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/00476b50.md) [`004779cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00477/004779cc.md) [`00477e0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00477/00477e0c.md)
- 新版 呼出元 1件 [`00475de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00475/00475de0.md) · 呼出先 11件 [`004741d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00474/004741d8.md) [`00476708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00476/00476708.md) [`00476b90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00476/00476b90.md) [`00477a0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00477/00477a0c.md) [`00477e4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00477/00477e4c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.14% / 新版 97.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00476244",
      "incomplete_value": true,
      "site": "00476260",
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
                "const:ad0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00476204",
      "incomplete_value": true,
      "site": "00476220",
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
                "const:a90:8"
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
      "00476244",
      "READ",
      [
        "storage",
        "002c2a90",
        null,
        null
      ]
    ],
    [
      "00476328",
      "READ",
      [
        "storage",
        "002af833",
        null,
        "string"
      ]
    ],
    [
      "00476338",
      "READ",
      [
        "storage",
        "002af83d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00476244",
      "READ",
      [
        "storage",
        "002c2ad0",
        null,
        null
      ]
    ],
    [
      "00476328",
      "READ",
      [
        "storage",
        "002af7d7",
        null,
        "string"
      ]
    ],
    [
      "00476338",
      "READ",
      [
        "storage",
        "002af7e1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004761f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/004761a4.md#insn-004761f4) · [`00476204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/004761a4.md#insn-00476204) · [`0047620c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/004761a4.md#insn-0047620c)
- 新版 `00476234`（命令位置の公開資料なし） · `00476244`（命令位置の公開資料なし）

~~~diff
- 004761f4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004761f4 ["INT_ADD", "register:40f0:8", ["const:4761f4:8", "const:4:8"]]
- 004761f4 ["CALLIND", null, ["register:0:8"]]
+ 00476234 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00476234 ["INT_ADD", "register:40f0:8", ["const:476234:8", "const:4:8"]]
+ 00476234 ["CALLIND", null, ["register:0:8"]]
- 004761f4 bytes 20013fd6
+ 00476234 bytes 20013fd6
- 00476204 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a90:8"]]
- 00476204 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 00476204 ["COPY", "register:5010:8", ["const:0:8"]]
- 00476204 ["COPY", "register:5018:8", ["const:0:8"]]
+ 00476244 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ad0:8"]]
+ 00476244 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
+ 00476244 ["COPY", "register:5010:8", ["const:0:8"]]
+ 00476244 ["COPY", "register:5018:8", ["const:0:8"]]
- 00476204 bytes 20a5c23d
+ 00476244 bytes 20b5c23d
- 0047620c ["COPY", "register:40c8:8", ["const:2af000:8"]]
- 0047620c bytes d9f1ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21927740dc302703f1dc40c965358eeb"></a>

### [`004766c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/004766c8.md) → [`00476708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00476/00476708.md) FUN_00476708

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`004761a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/004761a4.md) · 呼出先 23件 [`0044f8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f8e0.md) [`004539dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/004539dc.md) [`00472e34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472e34.md) [`00473028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473028.md) [`00478148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478148.md)
- 新版 呼出元 1件 [`004761e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00476/004761e4.md) · 呼出先 23件 [`0044f920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f920.md) [`00453a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00453/00453a1c.md) [`00472e74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00472/00472e74.md) [`00473068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/00473068.md) [`00478188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00478/00478188.md)

変更の種類 call, call_argument_candidate, call_count, call_target, constant, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 93.83% / 新版 93.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 2件, `unresolved_call_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0047677c",
      "value": [
        "leaf",
        "ram:7643dc:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0047673c",
      "value": [
        "leaf",
        "ram:764384:8"
      ]
    },
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00476740"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00476788",
      "value": [
        "leaf",
        "ram:764f38:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00476748",
      "value": [
        "leaf",
        "ram:764ee0:8"
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
      "0047677c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764384"
      ]
    ],
    [
      "unmatched:00476740",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00851550"
      ]
    ],
    [
      "00476788",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764ee0"
      ]
    ]
  ],
  "added": [
    [
      "0047677c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007643dc"
      ]
    ],
    [
      "00476780",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00851550"
      ]
    ],
    [
      "00476788",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764f38"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00476700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/004766c8.md#insn-00476700) · [`0047673c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/004766c8.md#insn-0047673c) · [`00476740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/004766c8.md#insn-00476740)
- 新版 `00476740`（命令位置の公開資料なし） · `0047677c`（命令位置の公開資料なし）

~~~diff
- 00476700 ["COPY", "register:0:8", ["register:4048:8"]]
- 00476700 ["INT_ADD", "register:40f0:8", ["const:476700:8", "const:4:8"]]
- 00476700 ["CALLIND", null, ["register:0:8"]]
+ 00476740 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00476740 ["INT_ADD", "register:40f0:8", ["const:476740:8", "const:4:8"]]
+ 00476740 ["CALLIND", null, ["register:0:8"]]
- 00476700 bytes 20013fd6
+ 00476740 bytes 20013fd6
- 0047673c ["INT_ADD", "register:40f0:8", ["const:47673c:8", "const:4:8"]]
- 0047673c ["CALL", null, ["ram:764384:8"]]
+ 0047677c ["INT_ADD", "register:40f0:8", ["const:47677c:8", "const:4:8"]]
+ 0047677c ["CALL", null, ["ram:7643dc:8"]]
- 0047673c bytes 12b70b94
+ 0047677c bytes 18b70b94
- 00476740 ["INT_ADD", "register:40f0:8", ["const:476740:8", "const:4:8"]]
- 00476740 ["CALL", null, ["callee:00851550:8"]]
- 00476740 bytes 6e6b0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-157b9d0e39352fb5361961709a7b618d"></a>

### [`00476b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/00476b50.md) → [`00476b90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00476/00476b90.md) FUN_00476b90

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004761a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/004761a4.md) · 呼出先 22件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00442b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442b38.md) [`0044b6a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b6a8.md) [`00478314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478314.md)
- 新版 呼出元 1件 [`004761e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00476/004761e4.md) · 呼出先 22件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00442b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442b78.md) [`0044b6e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b6e8.md) [`00478354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00478/00478354.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.95% / 新版 98.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004773bc",
      "incomplete_value": true,
      "site": "004773bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fb9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047737c",
      "incomplete_value": true,
      "site": "0047737c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 64,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00476c5c",
      "incomplete_value": false,
      "site": "00476c68",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00476c1c",
      "incomplete_value": false,
      "site": "00476c28",
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
            "const:fd8:8"
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
      "definition_site": "00476d28",
      "incomplete_value": false,
      "site": "00476d34",
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
            "const:6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00476ce8",
      "incomplete_value": false,
      "site": "00476cf4",
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
            "const:5a:8"
          ]
        ]
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
      "00476c5c",
      "PARAM",
      [
        "storage",
        "002b7fd8",
        null,
        "string"
      ]
    ],
    [
      "00476d28",
      "PARAM",
      [
        "storage",
        "002ba05a",
        null,
        "string"
      ]
    ],
    [
      "00476e80",
      "PARAM",
      [
        "storage",
        "002ad67a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00476c5c",
      "PARAM",
      [
        "storage",
        "002b8018",
        null,
        "string"
      ]
    ],
    [
      "00476d28",
      "PARAM",
      [
        "storage",
        "002ba006",
        null,
        "string"
      ]
    ],
    [
      "00476e80",
      "PARAM",
      [
        "storage",
        "002ad61e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00476c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/00476b50.md#insn-00476c28) · [`00476cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/00476b50.md#insn-00476cf4) · [`00476e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/00476b50.md#insn-00476e4c)
- 新版 `00476c68`（命令位置の公開資料なし） · `00476d34`（命令位置の公開資料なし） · `00476e8c`（命令位置の公開資料なし）

~~~diff
- 00476c28 ["INT_ADD", "register:40f0:8", ["const:476c28:8", "const:4:8"]]
- 00476c28 ["CALL", null, ["callee:00c58030:8"]]
+ 00476c68 ["INT_ADD", "register:40f0:8", ["const:476c68:8", "const:4:8"]]
+ 00476c68 ["CALL", null, ["callee:00c58030:8"]]
- 00476c28 bytes ce841f94
+ 00476c68 bytes f2841f94
- 00476cf4 ["INT_ADD", "register:40f0:8", ["const:476cf4:8", "const:4:8"]]
- 00476cf4 ["CALL", null, ["callee:00c58030:8"]]
+ 00476d34 ["INT_ADD", "register:40f0:8", ["const:476d34:8", "const:4:8"]]
+ 00476d34 ["CALL", null, ["callee:00c58030:8"]]
- 00476cf4 bytes 9b841f94
+ 00476d34 bytes bf841f94
- 00476e4c ["INT_ADD", "register:40f0:8", ["const:476e4c:8", "const:4:8"]]
- 00476e4c ["CALL", null, ["callee:00c58030:8"]]
+ 00476e8c ["INT_ADD", "register:40f0:8", ["const:476e8c:8", "const:4:8"]]
+ 00476e8c ["CALL", null, ["callee:00c58030:8"]]
- 00476e4c bytes 45841f94
+ 00476e8c bytes 69841f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e75b46a304e20f13573aa6e2f67b4e2"></a>

### [`004779cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00477/004779cc.md) → [`00477a0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00477/00477a0c.md) FUN_00477a0c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`004761a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/004761a4.md) · 呼出先 20件 [`0044f8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f8e0.md) [`004539dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00453/004539dc.md) [`00472e34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472e34.md) [`00473028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473028.md) [`00478148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478148.md)
- 新版 呼出元 1件 [`004761e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00476/004761e4.md) · 呼出先 20件 [`0044f920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f920.md) [`00453a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00453/00453a1c.md) [`00472e74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00472/00472e74.md) [`00473068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/00473068.md) [`00478188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00478/00478188.md)

変更の種類 call, call_argument_candidate, call_count, call_target, constant, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 92.38% / 新版 92.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 2件, `store_value` 1件, `unresolved_call_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00477b0c",
      "incomplete_value": true,
      "site": "00477b18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00477acc",
      "incomplete_value": true,
      "site": "00477ad8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:190:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00477a68",
      "value": [
        "leaf",
        "ram:7643dc:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00477a28",
      "value": [
        "leaf",
        "ram:764384:8"
      ]
    },
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00477a2c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00477a68",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764384"
      ]
    ],
    [
      "unmatched:00477a2c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00851550"
      ]
    ],
    [
      "00477a74",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764ee0"
      ]
    ]
  ],
  "added": [
    [
      "00477a68",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007643dc"
      ]
    ],
    [
      "00477a6c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00851550"
      ]
    ],
    [
      "00477a74",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764f38"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00477a28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00477/004779cc.md#insn-00477a28) · [`00477a2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00477/004779cc.md#insn-00477a2c) · [`00477a34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00477/004779cc.md#insn-00477a34)
- 新版 `00477a68`（命令位置の公開資料なし） · `00477a74`（命令位置の公開資料なし）

~~~diff
- 00477a28 ["INT_ADD", "register:40f0:8", ["const:477a28:8", "const:4:8"]]
- 00477a28 ["CALL", null, ["ram:764384:8"]]
+ 00477a68 ["INT_ADD", "register:40f0:8", ["const:477a68:8", "const:4:8"]]
+ 00477a68 ["CALL", null, ["ram:7643dc:8"]]
- 00477a28 bytes 57b20b94
+ 00477a68 bytes 5db20b94
- 00477a2c ["INT_ADD", "register:40f0:8", ["const:477a2c:8", "const:4:8"]]
- 00477a2c ["CALL", null, ["callee:00851550:8"]]
- 00477a2c bytes b3660f94
- 00477a34 ["INT_ADD", "register:40f0:8", ["const:477a34:8", "const:4:8"]]
- 00477a34 ["CALL", null, ["ram:764ee0:8"]]
+ 00477a74 ["INT_ADD", "register:40f0:8", ["const:477a74:8", "const:4:8"]]
+ 00477a74 ["CALL", null, ["ram:764f38:8"]]
- 00477a34 bytes 2bb50b94
+ 00477a74 bytes 31b50b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4937ba936aed647dae22dc15e62dbc94"></a>

### [`00477e0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00477/00477e0c.md) → [`00477e4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00477/00477e4c.md) FUN_00477e4c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`004761a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/004761a4.md) [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) · 呼出先 10件 [`0044b584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044b584.md) [`00478c90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478c90.md) [`00478c94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478c94.md) [`00561d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00561/00561d34.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)
- 新版 呼出元 1件 [`004761e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00476/004761e4.md) · 呼出先 10件 [`0044b5c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044b/0044b5c4.md) [`00478cd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00478/00478cd0.md) [`00478cd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00478/00478cd4.md) [`00561d74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00561/00561d74.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)

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
      "definition_site": "00477f50",
      "incomplete_value": false,
      "site": "00477f50",
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
            "const:fb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00477f10",
      "incomplete_value": false,
      "site": "00477f10",
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
            "const:ee0:8"
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
      "definition_site": "00477e88",
      "incomplete_value": false,
      "site": "00477e90",
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
            "const:3d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00477e48",
      "incomplete_value": false,
      "site": "00477e50",
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
            "const:434:8"
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
      "definition_site": "00477f0c",
      "incomplete_value": true,
      "site": "00477f14",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00477ecc",
      "incomplete_value": true,
      "site": "00477ed4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c08:8"
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
      "00477e88",
      "PARAM",
      [
        "storage",
        "002a6434",
        null,
        "string"
      ]
    ],
    [
      "00477f0c",
      "READ",
      [
        "storage",
        "00c9ac08",
        null,
        "pointer"
      ]
    ],
    [
      "00477f0c",
      "PARAM",
      [
        "storage",
        "00ca5ce8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00477e88",
      "PARAM",
      [
        "storage",
        "002a63d8",
        null,
        "string"
      ]
    ],
    [
      "00477f0c",
      "READ",
      [
        "storage",
        "00c9acd8",
        null,
        "pointer"
      ]
    ],
    [
      "00477f0c",
      "PARAM",
      [
        "storage",
        "00ca5de8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00477e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00477/00477e0c.md#insn-00477e50) · [`00477ed4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00477/00477e0c.md#insn-00477ed4) · [`00477e40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00477/00477e0c.md#insn-00477e40)
- 新版 `00477e90`（命令位置の公開資料なし） · `00477f14`（命令位置の公開資料なし） · `00477e80`（命令位置の公開資料なし）

~~~diff
- 00477e50 ["INT_ADD", "register:40f0:8", ["const:477e50:8", "const:4:8"]]
- 00477e50 ["CALL", null, ["callee:00c58040:8"]]
+ 00477e90 ["INT_ADD", "register:40f0:8", ["const:477e90:8", "const:4:8"]]
+ 00477e90 ["CALL", null, ["callee:00c58040:8"]]
- 00477e50 bytes 48801f94
+ 00477e90 bytes 6c801f94
- 00477ed4 ["INT_ADD", "register:40f0:8", ["const:477ed4:8", "const:4:8"]]
- 00477ed4 ["CALL", null, ["callee:00561d74:8"]]
+ 00477f14 ["INT_ADD", "register:40f0:8", ["const:477f14:8", "const:4:8"]]
+ 00477f14 ["CALL", null, ["callee:00561d74:8"]]
- 00477ed4 bytes 98a70394
+ 00477f14 bytes 98a70394
- 00477e40 ["INT_ADD", "register:40f0:8", ["const:477e40:8", "const:4:8"]]
- 00477e40 ["CALL", null, ["callee:0044b5c4:8"]]
+ 00477e80 ["INT_ADD", "register:40f0:8", ["const:477e80:8", "const:4:8"]]
+ 00477e80 ["CALL", null, ["callee:0044b5c4:8"]]
- 00477e40 bytes d14dff97
+ 00477e80 bytes d14dff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d8640e45fff2adb8fd0b7f44ce34bf6"></a>

### [`00478314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478314.md) → [`00478354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00478/00478354.md) FUN_00478354

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00476b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/00476b50.md) [`0048ceb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ceb8.md) · 呼出先 13件 [`004594d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fa0.md) [`00c57fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fb0.md)
- 新版 呼出元 2件 [`00476b90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00476/00476b90.md) [`0048cef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cef8.md) · 呼出先 13件 [`00459510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459510.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58070.md) [`00c58080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58080.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 88.83% / 新版 88.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004783c4",
      "incomplete_value": true,
      "site": "004783c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00478384",
      "incomplete_value": true,
      "site": "00478388",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004783c0",
      "incomplete_value": true,
      "site": "004783d0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00478380",
      "incomplete_value": true,
      "site": "00478390",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004783d8",
      "incomplete_value": true,
      "site": "004783d8",
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
      "definition_site": "00478398",
      "incomplete_value": true,
      "site": "00478398",
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
      "unmatched:0047836c",
      "READ",
      [
        "storage",
        "00c9abb8",
        null,
        "pointer"
      ]
    ],
    [
      "004783c0",
      "READ",
      [
        "storage",
        "00c93208",
        null,
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "004783c0",
      "READ",
      [
        "storage",
        "00c93210",
        null,
        "pointer __((offset(0x40)))"
      ]
    ]
  ],
  "added": [
    [
      "004783a8",
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      "004783c0",
      "READ",
      [
        "storage",
        "00c932d8",
        null,
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "004783c0",
      "READ",
      [
        "storage",
        "00c932e0",
        null,
        "pointer __((offset(0x40)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004783b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478314.md#insn-004783b0) · [`004783d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478314.md#insn-004783d0) · [`00478428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478314.md#insn-00478428)
- 新版 `004783f0`（命令位置の公開資料なし） · `00478410`（命令位置の公開資料なし） · `00478468`（命令位置の公開資料なし）

~~~diff
- 004783b0 ["INT_ADD", "register:40f0:8", ["const:4783b0:8", "const:4:8"]]
- 004783b0 ["CALL", null, ["callee:00c582b0:8"]]
+ 004783f0 ["INT_ADD", "register:40f0:8", ["const:4783f0:8", "const:4:8"]]
+ 004783f0 ["CALL", null, ["callee:00c582b0:8"]]
- 004783b0 bytes 8c7f1f94
+ 004783f0 bytes b07f1f94
- 004783d0 ["INT_ADD", "register:40f0:8", ["const:4783d0:8", "const:4:8"]]
- 004783d0 ["CALL", null, ["callee:00c582c0:8"]]
+ 00478410 ["INT_ADD", "register:40f0:8", ["const:478410:8", "const:4:8"]]
+ 00478410 ["CALL", null, ["callee:00c582c0:8"]]
- 004783d0 bytes 887f1f94
+ 00478410 bytes ac7f1f94
- 00478428 ["INT_ADD", "register:40f0:8", ["const:478428:8", "const:4:8"]]
- 00478428 ["CALL", null, ["callee:00c58350:8"]]
+ 00478468 ["INT_ADD", "register:40f0:8", ["const:478468:8", "const:4:8"]]
+ 00478468 ["CALL", null, ["callee:00c58350:8"]]
- 00478428 bytes 967f1f94
+ 00478468 bytes ba7f1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fbba1f510560199aa48979d2a8d35cc8"></a>

### [`00478690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478690.md) → [`004786d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00478/004786d0.md) FUN_004786d0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00476b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/00476b50.md) [`0048ceb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ceb8.md) · 呼出先 6件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00478b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478b90.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)
- 新版 呼出元 2件 [`00476b90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00476/00476b90.md) [`0048cef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cef8.md) · 呼出先 6件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00478bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00478/00478bd0.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)

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
      "definition_site": "0047871c",
      "incomplete_value": true,
      "site": "0047871c",
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
            "const:ef0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004786dc",
      "incomplete_value": true,
      "site": "004786dc",
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
            "const:df0:8"
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
      "definition_site": "004787c0",
      "incomplete_value": true,
      "site": "004787c0",
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
            "const:ef0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00478780",
      "incomplete_value": true,
      "site": "00478780",
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
            "const:df0:8"
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
      "definition_site": "00478864",
      "incomplete_value": true,
      "site": "00478864",
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
            "const:ef0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00478824",
      "incomplete_value": true,
      "site": "00478824",
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
            "const:df0:8"
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
      "004786ec",
      "READ",
      [
        "storage",
        "00ca4e08",
        null,
        "undefined1"
      ]
    ],
    [
      "004786f8",
      "READ",
      [
        "storage",
        "00ca4e00",
        null,
        "undefined8"
      ]
    ],
    [
      "00478710",
      "READ",
      [
        "storage",
        "00ca4df8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004786ec",
      "READ",
      [
        "storage",
        "00ca4f08",
        null,
        "undefined1"
      ]
    ],
    [
      "004786f8",
      "READ",
      [
        "storage",
        "00ca4f00",
        null,
        "undefined8"
      ]
    ],
    [
      "00478710",
      "READ",
      [
        "storage",
        "00ca4ef8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004786dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478690.md#insn-004786dc) · [`00478780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478690.md#insn-00478780) · [`00478824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478690.md#insn-00478824)
- 新版 `0047871c`（命令位置の公開資料なし） · `004787c0`（命令位置の公開資料なし） · `00478864`（命令位置の公開資料なし）

~~~diff
- 004786dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:df0:8"]]
- 004786dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 0047871c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ef0:8"]]
+ 0047871c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 004786dc bytes 68fa06f9
+ 0047871c bytes 687a07f9
- 00478780 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:df0:8"]]
- 00478780 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 004787c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ef0:8"]]
+ 004787c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00478780 bytes 68fa06f9
+ 004787c0 bytes 687a07f9
- 00478824 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:df0:8"]]
- 00478824 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00478864 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ef0:8"]]
+ 00478864 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00478824 bytes 68fa06f9
+ 00478864 bytes 687a07f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f8bdfb470558f70c0918cdb37743ce6"></a>

### [`00478b98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478b98.md) → [`00478bd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00478/00478bd8.md) FUN_00478bd8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fa0.md) [`00c57fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fc0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58070.md) [`00c58080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58080.md) [`00c58090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58090.md)

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
      "definition_site": "00478bfc",
      "incomplete_value": true,
      "site": "00478c04",
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
      "definition_site": "00478bbc",
      "incomplete_value": true,
      "site": "00478bc4",
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
      "definition_site": "00478c10",
      "incomplete_value": true,
      "site": "00478c10",
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
      "definition_site": "00478bd0",
      "incomplete_value": true,
      "site": "00478bd0",
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
      "definition_site": "00478c10",
      "incomplete_value": true,
      "site": "00478c10",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00478bd0",
      "incomplete_value": true,
      "site": "00478bd0",
      "value": [
        "LOAD",
        "8",
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
      "00478bf4",
      "READ",
      [
        "storage",
        "00c9abb8",
        null,
        "pointer"
      ]
    ],
    [
      "00478bfc",
      "READ",
      [
        "storage",
        "00c93200",
        "_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "00478c00",
      "READ",
      [
        "storage",
        "00c93218",
        null,
        "pointer __((offset(0x40)))"
      ]
    ]
  ],
  "added": [
    [
      "00478bf4",
      "READ",
      [
        "storage",
        "00c9ac88",
        null,
        "pointer"
      ]
    ],
    [
      "00478bfc",
      "READ",
      [
        "storage",
        "00c932d0",
        "_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "00478c00",
      "READ",
      [
        "storage",
        "00c932e8",
        null,
        "pointer __((offset(0x40)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00478bb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478b98.md#insn-00478bb4) · [`00478bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478b98.md#insn-00478bb8) · [`00478bcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478b98.md#insn-00478bcc)
- 新版 `00478bf4`（命令位置の公開資料なし） · `00478c0c`（命令位置の公開資料なし）

~~~diff
- 00478bb4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:bb8:8"]]
- 00478bb4 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00478bf4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:c88:8"]]
+ 00478bf4 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
- 00478bb4 bytes b5de45f9
+ 00478bf4 bytes b54646f9
- 00478bb8 ["COPY", "register:4098:8", ["register:4000:8"]]
- 00478bb8 bytes f30300aa
- 00478bcc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:bc0:8"]]
- 00478bcc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00478c0c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c90:8"]]
+ 00478c0c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00478bcc bytes 29e145f9
+ 00478c0c bytes 294946f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-246ec513ad2b4151e3f0598d0fa77481"></a>

### [`00478c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478c5c.md) → [`00478c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00478/00478c9c.md) FUN_00478c9c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00478cb0",
      "incomplete_value": false,
      "site": "00478cb4",
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
            "const:fb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00478c70",
      "incomplete_value": false,
      "site": "00478c74",
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
            "const:ee0:8"
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
      "00478cb4",
      "DATA",
      [
        "storage",
        "00c64ee0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00478cb4",
      "DATA",
      [
        "storage",
        "00c64fb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00478c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478c5c.md#insn-00478c68) · [`00478c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478c5c.md#insn-00478c70)
- 新版 `00478ca8`（命令位置の公開資料なし） · `00478cb0`（命令位置の公開資料なし）

~~~diff
- 00478c68 ["INT_ADD", "register:40f0:8", ["const:478c68:8", "const:4:8"]]
- 00478c68 ["CALL", null, ["callee:00c57f60:8"]]
+ 00478ca8 ["INT_ADD", "register:40f0:8", ["const:478ca8:8", "const:4:8"]]
+ 00478ca8 ["CALL", null, ["callee:00c57f60:8"]]
- 00478c68 bytes 8a7c1f94
+ 00478ca8 bytes ae7c1f94
- 00478c70 ["COPY", "tmp:0:8", ["const:ee0:8"]]
- 00478c70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00478c70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00478c70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00478cb0 ["COPY", "tmp:0:8", ["const:fb0:8"]]
+ 00478cb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00478cb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00478cb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00478c70 bytes 08813b91
+ 00478cb0 bytes 08c13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c7b1d3569ec0542cac687ee7ff41f69"></a>

### [`00478c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478c80.md) → [`00478cc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00478/00478cc0.md) FUN_00478cc0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00478cc4",
      "incomplete_value": false,
      "site": "00478cc8",
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
            "const:fb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00478c84",
      "incomplete_value": false,
      "site": "00478c88",
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
            "const:ee0:8"
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
      "00478cc8",
      "DATA",
      [
        "storage",
        "00c64ee0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00478cc8",
      "DATA",
      [
        "storage",
        "00c64fb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00478c84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478c80.md#insn-00478c84)
- 新版 `00478cc4`（命令位置の公開資料なし）

~~~diff
- 00478c84 ["COPY", "tmp:0:8", ["const:ee0:8"]]
- 00478c84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00478c84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00478c84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00478cc4 ["COPY", "tmp:0:8", ["const:fb0:8"]]
+ 00478cc4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00478cc4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00478cc4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00478c84 bytes 08813b91
+ 00478cc4 bytes 08c13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67024039cf0f77df0f57a189c3cf81f6"></a>

### [`00479714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479714.md) → [`00479754`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00479/00479754.md) FUN_00479754

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00479778",
      "incomplete_value": false,
      "site": "00479778",
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
            "const:30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00479738",
      "incomplete_value": false,
      "site": "00479738",
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
            "const:f60:8"
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
      "00479778",
      "DATA",
      [
        "storage",
        "00c64f60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00479778",
      "DATA",
      [
        "storage",
        "00c65030",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00479728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479714.md#insn-00479728) · [`00479730`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479714.md#insn-00479730) · [`00479734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479714.md#insn-00479734)
- 新版 `00479768`（命令位置の公開資料なし） · `00479770`（命令位置の公開資料なし） · `00479774`（命令位置の公開資料なし）

~~~diff
- 00479728 ["INT_ADD", "register:40f0:8", ["const:479728:8", "const:4:8"]]
- 00479728 ["CALL", null, ["callee:00c57f60:8"]]
+ 00479768 ["INT_ADD", "register:40f0:8", ["const:479768:8", "const:4:8"]]
+ 00479768 ["CALL", null, ["callee:00c57f60:8"]]
- 00479728 bytes da791f94
+ 00479768 bytes fe791f94
- 00479730 ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 00479770 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 00479730 bytes 483f00f0
+ 00479770 bytes 683f0090
- 00479734 ["COPY", "tmp:0:8", ["const:f60:8"]]
- 00479734 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00479734 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00479734 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00479774 ["COPY", "tmp:0:8", ["const:30:8"]]
+ 00479774 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00479774 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00479774 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00479734 bytes 08813d91
+ 00479774 bytes 08c10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e6af48f2c80804a79a005c9062c6c84"></a>

### [`00479748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479748.md) → [`00479788`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00479/00479788.md) FUN_00479788

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00479794",
      "incomplete_value": false,
      "site": "00479794",
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
            "const:30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00479754",
      "incomplete_value": false,
      "site": "00479754",
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
            "const:f60:8"
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
      "00479794",
      "DATA",
      [
        "storage",
        "00c64f60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00479794",
      "DATA",
      [
        "storage",
        "00c65030",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047974c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479748.md#insn-0047974c) · [`00479750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479748.md#insn-00479750)
- 新版 `0047978c`（命令位置の公開資料なし） · `00479790`（命令位置の公開資料なし）

~~~diff
- 0047974c ["COPY", "register:4048:8", ["const:c64000:8"]]
+ 0047978c ["COPY", "register:4048:8", ["const:c65000:8"]]
- 0047974c bytes 493f00f0
+ 0047978c bytes 693f0090
- 00479750 ["COPY", "tmp:0:8", ["const:f60:8"]]
- 00479750 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00479750 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00479750 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00479790 ["COPY", "tmp:0:8", ["const:30:8"]]
+ 00479790 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00479790 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00479790 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00479750 bytes 29813d91
+ 00479790 bytes 29c10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52ef845b7ba2a113000fe5d2419a7a4e"></a>

### [`004797cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/004797cc.md) → [`0047980c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00479/0047980c.md) FUN_0047980c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00479830",
      "incomplete_value": false,
      "site": "00479830",
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
            "const:c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004797f0",
      "incomplete_value": false,
      "site": "004797f0",
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
            "const:ff0:8"
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
      "00479830",
      "DATA",
      [
        "storage",
        "00c64ff0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00479830",
      "DATA",
      [
        "storage",
        "00c650c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004797e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/004797cc.md#insn-004797e0) · [`004797e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/004797cc.md#insn-004797e8) · [`004797ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/004797cc.md#insn-004797ec)
- 新版 `00479820`（命令位置の公開資料なし） · `00479828`（命令位置の公開資料なし） · `0047982c`（命令位置の公開資料なし）

~~~diff
- 004797e0 ["INT_ADD", "register:40f0:8", ["const:4797e0:8", "const:4:8"]]
- 004797e0 ["CALL", null, ["callee:00c57f60:8"]]
+ 00479820 ["INT_ADD", "register:40f0:8", ["const:479820:8", "const:4:8"]]
+ 00479820 ["CALL", null, ["callee:00c57f60:8"]]
- 004797e0 bytes ac791f94
+ 00479820 bytes d0791f94
- 004797e8 ["COPY", "register:4040:8", ["const:c64000:8"]]
+ 00479828 ["COPY", "register:4040:8", ["const:c65000:8"]]
- 004797e8 bytes 483f00f0
+ 00479828 bytes 683f0090
- 004797ec ["COPY", "tmp:0:8", ["const:ff0:8"]]
- 004797ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004797ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004797ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0047982c ["COPY", "tmp:0:8", ["const:c0:8"]]
+ 0047982c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0047982c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0047982c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004797ec bytes 08c13f91
+ 0047982c bytes 08010391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20a52a395e9d6388c0dd113eebce1fe4"></a>

### [`00479800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479800.md) → [`00479840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00479/00479840.md) FUN_00479840

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0047984c",
      "incomplete_value": false,
      "site": "0047984c",
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
            "const:c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047980c",
      "incomplete_value": false,
      "site": "0047980c",
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
            "const:ff0:8"
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
      "0047984c",
      "DATA",
      [
        "storage",
        "00c64ff0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047984c",
      "DATA",
      [
        "storage",
        "00c650c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00479804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479800.md#insn-00479804) · [`00479808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479800.md#insn-00479808)
- 新版 `00479844`（命令位置の公開資料なし） · `00479848`（命令位置の公開資料なし）

~~~diff
- 00479804 ["COPY", "register:4048:8", ["const:c64000:8"]]
+ 00479844 ["COPY", "register:4048:8", ["const:c65000:8"]]
- 00479804 bytes 493f00f0
+ 00479844 bytes 693f0090
- 00479808 ["COPY", "tmp:0:8", ["const:ff0:8"]]
- 00479808 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00479808 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00479808 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00479848 ["COPY", "tmp:0:8", ["const:c0:8"]]
+ 00479848 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00479848 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00479848 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00479808 bytes 29c13f91
+ 00479848 bytes 29010391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3cabdb4d8420a1ac8ea1e3384fcec0fd"></a>

### [`0047987c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/0047987c.md) → [`004798bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00479/004798bc.md) FUN_004798bc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "004798d4",
      "incomplete_value": false,
      "site": "004798d8",
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
      "definition_site": "00479894",
      "incomplete_value": false,
      "site": "00479898",
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
            "const:70:8"
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
      "004798d8",
      "DATA",
      [
        "storage",
        "00c65070",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004798d8",
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

- 旧版 [`004798d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/0047987c.md#insn-004798d8) · [`00479894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/0047987c.md#insn-00479894) · [`004798a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/0047987c.md#insn-004798a4)
- 新版 `00479918`（命令位置の公開資料なし） · `004798d4`（命令位置の公開資料なし） · `004798e4`（命令位置の公開資料なし）

~~~diff
- 004798d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004798d8 ["INT_ADD", "register:40f0:8", ["const:4798d8:8", "const:4:8"]]
- 004798d8 ["CALLIND", null, ["register:0:8"]]
+ 00479918 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00479918 ["INT_ADD", "register:40f0:8", ["const:479918:8", "const:4:8"]]
+ 00479918 ["CALLIND", null, ["register:0:8"]]
- 004798d8 bytes 00013fd6
+ 00479918 bytes 00013fd6
- 00479894 ["COPY", "tmp:0:8", ["const:70:8"]]
- 00479894 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00479894 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00479894 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004798d4 ["COPY", "tmp:0:8", ["const:140:8"]]
+ 004798d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004798d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004798d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00479894 bytes 29c10191
+ 004798d4 bytes 29010591
- 004798a4 ["INT_ADD", "register:40f0:8", ["const:4798a4:8", "const:4:8"]]
- 004798a4 ["CALL", null, ["callee:00c57f80:8"]]
+ 004798e4 ["INT_ADD", "register:40f0:8", ["const:4798e4:8", "const:4:8"]]
+ 004798e4 ["CALL", null, ["callee:00c57f80:8"]]
- 004798a4 bytes 83791f94
+ 004798e4 bytes a7791f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ad04fc7de8f48e6809166108eb623d3"></a>

### [`004798ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/004798ec.md) → [`0047992c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00479/0047992c.md) FUN_0047992c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00479944",
      "incomplete_value": false,
      "site": "00479948",
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
      "definition_site": "00479904",
      "incomplete_value": false,
      "site": "00479908",
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
            "const:70:8"
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
      "00479948",
      "DATA",
      [
        "storage",
        "00c65070",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00479948",
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

- 旧版 [`00479904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/004798ec.md#insn-00479904) · [`00479914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/004798ec.md#insn-00479914) · [`00479928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/004798ec.md#insn-00479928)
- 新版 `00479944`（命令位置の公開資料なし） · `00479954`（命令位置の公開資料なし） · `00479968`（命令位置の公開資料なし）

~~~diff
- 00479904 ["COPY", "tmp:0:8", ["const:70:8"]]
- 00479904 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00479904 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00479904 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00479944 ["COPY", "tmp:0:8", ["const:140:8"]]
+ 00479944 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00479944 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00479944 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00479904 bytes 29c10191
+ 00479944 bytes 29010591
- 00479914 ["INT_ADD", "register:40f0:8", ["const:479914:8", "const:4:8"]]
- 00479914 ["CALL", null, ["callee:00c57f80:8"]]
+ 00479954 ["INT_ADD", "register:40f0:8", ["const:479954:8", "const:4:8"]]
+ 00479954 ["CALL", null, ["callee:00c57f80:8"]]
- 00479914 bytes 67791f94
+ 00479954 bytes 8b791f94
- 00479928 ["INT_ADD", "register:40f0:8", ["const:479928:8", "const:4:8"]]
- 00479928 ["CALL", null, ["callee:00c53da0:8"]]
+ 00479968 ["INT_ADD", "register:40f0:8", ["const:479968:8", "const:4:8"]]
+ 00479968 ["CALL", null, ["callee:00c53da0:8"]]
- 00479928 bytes f6681f94
+ 00479968 bytes 0e691f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7aed4171715c7587f3947b02d219e8d"></a>

### [`00479958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479958.md) → [`00479998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00479/00479998.md) FUN_00479998

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "004799c0",
      "incomplete_value": false,
      "site": "004799c4",
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
      "definition_site": "00479980",
      "incomplete_value": false,
      "site": "00479984",
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
            "const:70:8"
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
      "004799c4",
      "DATA",
      [
        "storage",
        "00c65070",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004799c4",
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

- 旧版 [`0047996c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479958.md#insn-0047996c) · [`00479980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479958.md#insn-00479980) · [`0047999c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479958.md#insn-0047999c)
- 新版 `004799ac`（命令位置の公開資料なし） · `004799c0`（命令位置の公開資料なし） · `004799dc`（命令位置の公開資料なし）

~~~diff
- 0047996c ["INT_ADD", "register:40f0:8", ["const:47996c:8", "const:4:8"]]
- 0047996c ["CALL", null, ["callee:00c57f60:8"]]
+ 004799ac ["INT_ADD", "register:40f0:8", ["const:4799ac:8", "const:4:8"]]
+ 004799ac ["CALL", null, ["callee:00c57f60:8"]]
- 0047996c bytes 49791f94
+ 004799ac bytes 6d791f94
- 00479980 ["COPY", "tmp:0:8", ["const:70:8"]]
- 00479980 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00479980 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00479980 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004799c0 ["COPY", "tmp:0:8", ["const:140:8"]]
+ 004799c0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004799c0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004799c0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00479980 bytes 29c10191
+ 004799c0 bytes 29010591
- 0047999c ["INT_ADD", "register:40f0:8", ["const:47999c:8", "const:4:8"]]
- 0047999c ["CALL", null, ["callee:00c53d70:8"]]
+ 004799dc ["INT_ADD", "register:40f0:8", ["const:4799dc:8", "const:4:8"]]
+ 004799dc ["CALL", null, ["callee:00c53d70:8"]]
- 0047999c bytes cd681f94
+ 004799dc bytes e5681f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ba04fa7a26ad36e22acf79ff63e4aee"></a>

### [`004799f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/004799f8.md) → [`00479a38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00479/00479a38.md) FUN_00479a38

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)

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
      "definition_site": "00479a54",
      "incomplete_value": false,
      "site": "00479a60",
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
      "definition_site": "00479a14",
      "incomplete_value": false,
      "site": "00479a20",
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
            "const:70:8"
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
      "00479a60",
      "DATA",
      [
        "storage",
        "00c65070",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00479a60",
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

- 旧版 [`00479a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/004799f8.md#insn-00479a60) · [`00479a14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/004799f8.md#insn-00479a14) · [`00479a34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/004799f8.md#insn-00479a34)
- 新版 `00479aa0`（命令位置の公開資料なし） · `00479a54`（命令位置の公開資料なし） · `00479a74`（命令位置の公開資料なし）

~~~diff
- 00479a60 ["INT_ADD", "register:40f0:8", ["const:479a60:8", "const:4:8"]]
- 00479a60 ["CALL", null, ["callee:0043bb60:8"]]
+ 00479aa0 ["INT_ADD", "register:40f0:8", ["const:479aa0:8", "const:4:8"]]
+ 00479aa0 ["CALL", null, ["callee:0043bb60:8"]]
- 00479a60 bytes 3008ff97
+ 00479aa0 bytes 3008ff97
- 00479a14 ["COPY", "tmp:0:8", ["const:70:8"]]
- 00479a14 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00479a14 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00479a14 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00479a54 ["COPY", "tmp:0:8", ["const:140:8"]]
+ 00479a54 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00479a54 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00479a54 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00479a14 bytes 29c10191
+ 00479a54 bytes 29010591
- 00479a34 ["INT_ADD", "register:40f0:8", ["const:479a34:8", "const:4:8"]]
- 00479a34 ["CALL", null, ["callee:00c53d70:8"]]
+ 00479a74 ["INT_ADD", "register:40f0:8", ["const:479a74:8", "const:4:8"]]
+ 00479a74 ["CALL", null, ["callee:00c53d70:8"]]
- 00479a34 bytes a7681f94
+ 00479a74 bytes bf681f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d19e38185f5d814cf20099863256d85f"></a>

### [`00479b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479b48.md) → [`00479b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00479/00479b88.md) FUN_00479b88

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 7件 [`00479da8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479da8.md) [`00550990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550990.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00479de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00479/00479de8.md) [`005509d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/005509d0.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00479c20",
      "incomplete_value": false,
      "site": "00479c28",
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
            "const:1b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00479be0",
      "incomplete_value": false,
      "site": "00479be8",
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
            "const:e0:8"
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
      "definition_site": "00479c38",
      "incomplete_value": false,
      "site": "00479c38",
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
            "const:200:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00479bf8",
      "incomplete_value": false,
      "site": "00479bf8",
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
            "const:130:8"
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
      "site": "00479bf4",
      "value": [
        "leaf",
        "ram:5509d0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00479bb4",
      "value": [
        "leaf",
        "ram:550990:8"
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
      "00479bf4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00550990"
      ]
    ],
    [
      "00479c28",
      "DATA",
      [
        "storage",
        "00c650e0",
        null,
        "pointer"
      ]
    ],
    [
      "00479c38",
      "DATA",
      [
        "storage",
        "00c65130",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00479bf4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005509d0"
      ]
    ],
    [
      "00479c28",
      "DATA",
      [
        "storage",
        "00c651b0",
        null,
        "pointer"
      ]
    ],
    [
      "00479c38",
      "DATA",
      [
        "storage",
        "00c65200",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00479bb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479b48.md#insn-00479bb4) · [`00479b88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479b48.md#insn-00479b88) · [`00479ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479b48.md#insn-00479ba4)
- 新版 `00479bf4`（命令位置の公開資料なし） · `00479bc8`（命令位置の公開資料なし） · `00479be4`（命令位置の公開資料なし）

~~~diff
- 00479bb4 ["INT_ADD", "register:40f0:8", ["const:479bb4:8", "const:4:8"]]
- 00479bb4 ["CALL", null, ["ram:550990:8"]]
+ 00479bf4 ["INT_ADD", "register:40f0:8", ["const:479bf4:8", "const:4:8"]]
+ 00479bf4 ["CALL", null, ["ram:5509d0:8"]]
- 00479bb4 bytes 775b0394
+ 00479bf4 bytes 775b0394
- 00479b88 ["COPY", "register:0:8", ["register:4040:8"]]
- 00479b88 ["INT_ADD", "register:40f0:8", ["const:479b88:8", "const:4:8"]]
- 00479b88 ["CALLIND", null, ["register:0:8"]]
+ 00479bc8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00479bc8 ["INT_ADD", "register:40f0:8", ["const:479bc8:8", "const:4:8"]]
+ 00479bc8 ["CALLIND", null, ["register:0:8"]]
- 00479b88 bytes 00013fd6
+ 00479bc8 bytes 00013fd6
- 00479ba4 ["COPY", "register:0:8", ["register:4048:8"]]
- 00479ba4 ["INT_ADD", "register:40f0:8", ["const:479ba4:8", "const:4:8"]]
- 00479ba4 ["CALLIND", null, ["register:0:8"]]
+ 00479be4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00479be4 ["INT_ADD", "register:40f0:8", ["const:479be4:8", "const:4:8"]]
+ 00479be4 ["CALLIND", null, ["register:0:8"]]
- 00479ba4 bytes 20013fd6
+ 00479be4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a0996ddd05c90dcc2f31c758113e24a"></a>

### [`00479d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479d68.md) → [`00479da8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00479/00479da8.md) FUN_00479da8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)

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
      "definition_site": "00479dac",
      "incomplete_value": false,
      "site": "00479db0",
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
            "const:1b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00479d6c",
      "incomplete_value": false,
      "site": "00479d70",
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
            "const:e0:8"
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
      "00479db0",
      "DATA",
      [
        "storage",
        "00c650e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00479db0",
      "DATA",
      [
        "storage",
        "00c651b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00479d6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479d68.md#insn-00479d6c)
- 新版 `00479dac`（命令位置の公開資料なし）

~~~diff
- 00479d6c ["COPY", "tmp:0:8", ["const:e0:8"]]
- 00479d6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00479d6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00479d6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00479dac ["COPY", "tmp:0:8", ["const:1b0:8"]]
+ 00479dac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00479dac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00479dac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00479d6c bytes 08810391
+ 00479dac bytes 08c10691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-464b4cfd29774b8e2193a8c9f72a0c35"></a>

### [`00479d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479d78.md) → [`00479db8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00479/00479db8.md) FUN_00479db8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00479dc8",
      "incomplete_value": false,
      "site": "00479dd0",
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
            "const:1b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00479d88",
      "incomplete_value": false,
      "site": "00479d90",
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
            "const:e0:8"
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
      "00479dd0",
      "DATA",
      [
        "storage",
        "00c650e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00479dd0",
      "DATA",
      [
        "storage",
        "00c651b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00479d88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479d78.md#insn-00479d88) · [`00479d94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479d78.md#insn-00479d94)
- 新版 `00479dc8`（命令位置の公開資料なし） · `00479dd4`（命令位置の公開資料なし）

~~~diff
- 00479d88 ["COPY", "tmp:0:8", ["const:e0:8"]]
- 00479d88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00479d88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00479d88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00479dc8 ["COPY", "tmp:0:8", ["const:1b0:8"]]
+ 00479dc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00479dc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00479dc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00479d88 bytes 08810391
+ 00479dc8 bytes 08c10691
- 00479d94 ["INT_ADD", "register:40f0:8", ["const:479d94:8", "const:4:8"]]
- 00479d94 ["CALL", null, ["callee:00c57f70:8"]]
+ 00479dd4 ["INT_ADD", "register:40f0:8", ["const:479dd4:8", "const:4:8"]]
+ 00479dd4 ["CALL", null, ["callee:00c57f70:8"]]
- 00479d94 bytes 43781f94
+ 00479dd4 bytes 67781f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d84408f2ed907f948d79a1c7b9cf5cc5"></a>

### [`00479e00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479e00.md) → [`00479e40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00479/00479e40.md) FUN_00479e40

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

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
      "definition_site": "00479e54",
      "incomplete_value": false,
      "site": "00479e58",
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
            "const:298:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00479e14",
      "incomplete_value": false,
      "site": "00479e18",
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
            "const:1c8:8"
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
      "00479e58",
      "DATA",
      [
        "storage",
        "00c651c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00479e58",
      "DATA",
      [
        "storage",
        "00c65298",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00479e14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479e00.md#insn-00479e14) · [`00479e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479e00.md#insn-00479e28) · [`00479e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479e00.md#insn-00479e48)
- 新版 `00479e54`（命令位置の公開資料なし） · `00479e68`（命令位置の公開資料なし） · `00479e88`（命令位置の公開資料なし）

~~~diff
- 00479e14 ["COPY", "tmp:0:8", ["const:1c8:8"]]
- 00479e14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00479e14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00479e14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00479e54 ["COPY", "tmp:0:8", ["const:298:8"]]
+ 00479e54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00479e54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00479e54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00479e14 bytes 08210791
+ 00479e54 bytes 08610a91
- 00479e28 ["INT_ADD", "register:40f0:8", ["const:479e28:8", "const:4:8"]]
- 00479e28 ["CALL", null, ["callee:00c53da0:8"]]
+ 00479e68 ["INT_ADD", "register:40f0:8", ["const:479e68:8", "const:4:8"]]
+ 00479e68 ["CALL", null, ["callee:00c53da0:8"]]
- 00479e28 bytes b6671f94
+ 00479e68 bytes ce671f94
- 00479e48 ["COPY", "register:0:8", ["register:4040:8"]]
- 00479e48 ["INT_ADD", "register:40f0:8", ["const:479e48:8", "const:4:8"]]
- 00479e48 ["CALLIND", null, ["register:0:8"]]
+ 00479e88 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00479e88 ["INT_ADD", "register:40f0:8", ["const:479e88:8", "const:4:8"]]
+ 00479e88 ["CALLIND", null, ["register:0:8"]]
- 00479e48 bytes 00013fd6
+ 00479e88 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ade0f0b12b60910b84d8b363839df93"></a>

### [`00479e5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479e5c.md) → [`00479e9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00479/00479e9c.md) FUN_00479e9c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00479eb4",
      "incomplete_value": false,
      "site": "00479eb8",
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
            "const:298:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00479e74",
      "incomplete_value": false,
      "site": "00479e78",
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
            "const:1c8:8"
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
      "00479eb8",
      "DATA",
      [
        "storage",
        "00c651c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00479eb8",
      "DATA",
      [
        "storage",
        "00c65298",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00479e74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479e5c.md#insn-00479e74) · [`00479e88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479e5c.md#insn-00479e88) · [`00479e9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479e5c.md#insn-00479e9c)
- 新版 `00479eb4`（命令位置の公開資料なし） · `00479ec8`（命令位置の公開資料なし） · `00479edc`（命令位置の公開資料なし）

~~~diff
- 00479e74 ["COPY", "tmp:0:8", ["const:1c8:8"]]
- 00479e74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00479e74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00479e74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00479eb4 ["COPY", "tmp:0:8", ["const:298:8"]]
+ 00479eb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00479eb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00479eb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00479e74 bytes 08210791
+ 00479eb4 bytes 08610a91
- 00479e88 ["INT_ADD", "register:40f0:8", ["const:479e88:8", "const:4:8"]]
- 00479e88 ["CALL", null, ["callee:00c53da0:8"]]
+ 00479ec8 ["INT_ADD", "register:40f0:8", ["const:479ec8:8", "const:4:8"]]
+ 00479ec8 ["CALL", null, ["callee:00c53da0:8"]]
- 00479e88 bytes 9e671f94
+ 00479ec8 bytes b6671f94
- 00479e9c ["COPY", "register:0:8", ["register:4040:8"]]
- 00479e9c ["INT_ADD", "register:40f0:8", ["const:479e9c:8", "const:4:8"]]
- 00479e9c ["CALLIND", null, ["register:0:8"]]
+ 00479edc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00479edc ["INT_ADD", "register:40f0:8", ["const:479edc:8", "const:4:8"]]
+ 00479edc ["CALLIND", null, ["register:0:8"]]
- 00479e9c bytes 00013fd6
+ 00479edc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-137fbe2b509c94e3fc80255a5bb31d95"></a>

### [`00479eb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479eb8.md) → [`00479ef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00479/00479ef8.md) FUN_00479ef8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00479f1c",
      "incomplete_value": false,
      "site": "00479f20",
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
            "const:298:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00479edc",
      "incomplete_value": false,
      "site": "00479ee0",
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
            "const:1c8:8"
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
      "00479f20",
      "DATA",
      [
        "storage",
        "00c651c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00479f20",
      "DATA",
      [
        "storage",
        "00c65298",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00479ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479eb8.md#insn-00479ecc) · [`00479edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479eb8.md#insn-00479edc) · [`00479efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479eb8.md#insn-00479efc)
- 新版 `00479f0c`（命令位置の公開資料なし） · `00479f1c`（命令位置の公開資料なし） · `00479f3c`（命令位置の公開資料なし）

~~~diff
- 00479ecc ["INT_ADD", "register:40f0:8", ["const:479ecc:8", "const:4:8"]]
- 00479ecc ["CALL", null, ["callee:00c57f60:8"]]
+ 00479f0c ["INT_ADD", "register:40f0:8", ["const:479f0c:8", "const:4:8"]]
+ 00479f0c ["CALL", null, ["callee:00c57f60:8"]]
- 00479ecc bytes f1771f94
+ 00479f0c bytes 15781f94
- 00479edc ["COPY", "tmp:0:8", ["const:1c8:8"]]
- 00479edc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00479edc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00479edc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00479f1c ["COPY", "tmp:0:8", ["const:298:8"]]
+ 00479f1c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00479f1c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00479f1c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00479edc bytes 29210791
+ 00479f1c bytes 29610a91
- 00479efc ["INT_ADD", "register:40f0:8", ["const:479efc:8", "const:4:8"]]
- 00479efc ["CALL", null, ["callee:00c53d70:8"]]
+ 00479f3c ["INT_ADD", "register:40f0:8", ["const:479f3c:8", "const:4:8"]]
+ 00479f3c ["CALL", null, ["callee:00c53d70:8"]]
- 00479efc bytes 75671f94
+ 00479f3c bytes 8d671f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09be70c880e9de905856eeefafb070b5"></a>

### [`00479f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479f10.md) → [`00479f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00479/00479f50.md) FUN_00479f50

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)

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
      "definition_site": "00479f58",
      "incomplete_value": false,
      "site": "00479f5c",
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
            "const:298:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00479f18",
      "incomplete_value": false,
      "site": "00479f1c",
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
            "const:1c8:8"
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
      "00479f5c",
      "DATA",
      [
        "storage",
        "00c651c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00479f5c",
      "DATA",
      [
        "storage",
        "00c65298",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00479f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479f10.md#insn-00479f18) · [`00479f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479f10.md#insn-00479f40)
- 新版 `00479f58`（命令位置の公開資料なし） · `00479f80`（命令位置の公開資料なし）

~~~diff
- 00479f18 ["COPY", "tmp:0:8", ["const:1c8:8"]]
- 00479f18 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00479f18 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00479f18 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00479f58 ["COPY", "tmp:0:8", ["const:298:8"]]
+ 00479f58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00479f58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00479f58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00479f18 bytes 29210791
+ 00479f58 bytes 29610a91
- 00479f40 ["INT_ADD", "register:40f0:8", ["const:479f40:8", "const:4:8"]]
- 00479f40 ["CALL", null, ["callee:00c53d70:8"]]
+ 00479f80 ["INT_ADD", "register:40f0:8", ["const:479f80:8", "const:4:8"]]
+ 00479f80 ["CALL", null, ["callee:00c53d70:8"]]
- 00479f40 bytes 64671f94
+ 00479f80 bytes 7c671f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3ab99688267915066f95d3befb5aa37"></a>

### [`00479fec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479fec.md) → [`0047a02c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047a02c.md) FUN_0047a02c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0047a178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a178.md) [`0047a17c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a17c.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`004938d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/004938d4.md) [`00550994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550994.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0047a1b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047a1b8.md) [`0047a1bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047a1bc.md) [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`00493914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493914.md) [`005509d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/005509d4.md)

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
      "definition_site": "0047a088",
      "incomplete_value": false,
      "site": "0047a090",
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
            "const:318:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047a048",
      "incomplete_value": false,
      "site": "0047a050",
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
            "const:248:8"
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
      "site": "0047a060",
      "value": [
        "leaf",
        "ram:5509d4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0047a020",
      "value": [
        "leaf",
        "ram:550994:8"
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
      "site": "0047a080",
      "value": [
        "leaf",
        "ram:48cd38:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0047a040",
      "value": [
        "leaf",
        "ram:48ccf8:8"
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
      "0047a060",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00550994"
      ]
    ],
    [
      "0047a080",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "0047a090",
      "DATA",
      [
        "storage",
        "00c65248",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047a060",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005509d4"
      ]
    ],
    [
      "0047a080",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ],
    [
      "0047a090",
      "DATA",
      [
        "storage",
        "00c65318",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479fec.md#insn-0047a020) · [`0047a040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479fec.md#insn-0047a040) · [`0047a060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00479/00479fec.md#insn-0047a060)
- 新版 `0047a060`（命令位置の公開資料なし） · `0047a080`（命令位置の公開資料なし） · `0047a0a0`（命令位置の公開資料なし）

~~~diff
- 0047a020 ["INT_ADD", "register:40f0:8", ["const:47a020:8", "const:4:8"]]
- 0047a020 ["CALL", null, ["ram:550994:8"]]
+ 0047a060 ["INT_ADD", "register:40f0:8", ["const:47a060:8", "const:4:8"]]
+ 0047a060 ["CALL", null, ["ram:5509d4:8"]]
- 0047a020 bytes 5d5a0394
+ 0047a060 bytes 5d5a0394
- 0047a040 ["INT_ADD", "register:40f0:8", ["const:47a040:8", "const:4:8"]]
- 0047a040 ["CALL", null, ["ram:48ccf8:8"]]
+ 0047a080 ["INT_ADD", "register:40f0:8", ["const:47a080:8", "const:4:8"]]
+ 0047a080 ["CALL", null, ["ram:48cd38:8"]]
- 0047a040 bytes 2e4b0094
+ 0047a080 bytes 2e4b0094
- 0047a060 ["INT_ADD", "register:40f0:8", ["const:47a060:8", "const:4:8"]]
- 0047a060 ["CALL", null, ["callee:00493914:8"]]
+ 0047a0a0 ["INT_ADD", "register:40f0:8", ["const:47a0a0:8", "const:4:8"]]
+ 0047a0a0 ["CALL", null, ["callee:00493914:8"]]
- 0047a060 bytes 1d660094
+ 0047a0a0 bytes 1d660094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afd96514bef4da74401757ccbcea5a90"></a>

### [`0047a144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a144.md) → [`0047a184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047a184.md) FUN_0047a184

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "0047a198",
      "incomplete_value": false,
      "site": "0047a19c",
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
            "const:318:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047a158",
      "incomplete_value": false,
      "site": "0047a15c",
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
            "const:248:8"
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
      "0047a19c",
      "DATA",
      [
        "storage",
        "00c65248",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047a19c",
      "DATA",
      [
        "storage",
        "00c65318",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047a150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a144.md#insn-0047a150) · [`0047a158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a144.md#insn-0047a158)
- 新版 `0047a190`（命令位置の公開資料なし） · `0047a198`（命令位置の公開資料なし）

~~~diff
- 0047a150 ["INT_ADD", "register:40f0:8", ["const:47a150:8", "const:4:8"]]
- 0047a150 ["CALL", null, ["callee:00c57f60:8"]]
+ 0047a190 ["INT_ADD", "register:40f0:8", ["const:47a190:8", "const:4:8"]]
+ 0047a190 ["CALL", null, ["callee:00c57f60:8"]]
- 0047a150 bytes 50771f94
+ 0047a190 bytes 74771f94
- 0047a158 ["COPY", "tmp:0:8", ["const:248:8"]]
- 0047a158 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0047a158 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0047a158 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0047a198 ["COPY", "tmp:0:8", ["const:318:8"]]
+ 0047a198 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0047a198 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0047a198 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0047a158 bytes 08210991
+ 0047a198 bytes 08610c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fefc6b2b6429d1ae59cfe9d7409c5b15"></a>

### [`0047a168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a168.md) → [`0047a1a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047a1a8.md) FUN_0047a1a8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0047a1ac",
      "incomplete_value": false,
      "site": "0047a1b0",
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
            "const:318:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047a16c",
      "incomplete_value": false,
      "site": "0047a170",
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
            "const:248:8"
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
      "0047a1b0",
      "DATA",
      [
        "storage",
        "00c65248",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047a1b0",
      "DATA",
      [
        "storage",
        "00c65318",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047a16c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a168.md#insn-0047a16c)
- 新版 `0047a1ac`（命令位置の公開資料なし）

~~~diff
- 0047a16c ["COPY", "tmp:0:8", ["const:248:8"]]
- 0047a16c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0047a16c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0047a16c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0047a1ac ["COPY", "tmp:0:8", ["const:318:8"]]
+ 0047a1ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0047a1ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0047a1ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0047a16c bytes 08210991
+ 0047a1ac bytes 08610c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf43086ce687d184ea81ad226fc97379"></a>

### [`0047a180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a180.md) → [`0047a1c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047a1c0.md) FUN_0047a1c0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00442b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442b38.md) [`0047a744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a744.md) [`0047a794`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a794.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00442b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442b78.md) [`0047a784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047a784.md) [`0047a7d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047a7d4.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md)

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
      "definition_site": "0047a1e4",
      "incomplete_value": true,
      "site": "0047a200",
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
                "const:bdb:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047a1a4",
      "incomplete_value": true,
      "site": "0047a1c0",
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
                "const:baa:8"
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
      "definition_site": "0047a334",
      "incomplete_value": false,
      "site": "0047a334",
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
            "const:388:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047a2f4",
      "incomplete_value": false,
      "site": "0047a2f4",
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
            "const:2b8:8"
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
      "0047a1e4",
      "READ",
      [
        "storage",
        "002b4baa",
        null,
        "string"
      ]
    ],
    [
      "0047a334",
      "DATA",
      [
        "storage",
        "00c652b8",
        null,
        "undefined *"
      ]
    ],
    [
      "0047a3c4",
      "READ",
      [
        "storage",
        "00c652d8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0047a1e4",
      "READ",
      [
        "storage",
        "002b4bdb",
        null,
        "string"
      ]
    ],
    [
      "0047a334",
      "DATA",
      [
        "storage",
        "00c65388",
        null,
        "undefined *"
      ]
    ],
    [
      "0047a3c4",
      "READ",
      [
        "storage",
        "00c653a8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047a19c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a180.md#insn-0047a19c) · [`0047a1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a180.md#insn-0047a1d0) · [`0047a218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a180.md#insn-0047a218)
- 新版 `0047a1dc`（命令位置の公開資料なし） · `0047a210`（命令位置の公開資料なし） · `0047a258`（命令位置の公開資料なし）

~~~diff
- 0047a19c ["COPY", "tmp:0:8", ["const:baa:8"]]
- 0047a19c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0047a19c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0047a19c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0047a1dc ["COPY", "tmp:0:8", ["const:bdb:8"]]
+ 0047a1dc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0047a1dc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0047a1dc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0047a19c bytes 4aa92e91
+ 0047a1dc bytes 4a6d2f91
- 0047a1d0 ["INT_ADD", "register:40f0:8", ["const:47a1d0:8", "const:4:8"]]
- 0047a1d0 ["CALL", null, ["callee:0048ce94:8"]]
+ 0047a210 ["INT_ADD", "register:40f0:8", ["const:47a210:8", "const:4:8"]]
+ 0047a210 ["CALL", null, ["callee:0048ce94:8"]]
- 0047a1d0 bytes 214b0094
+ 0047a210 bytes 214b0094
- 0047a218 ["INT_ADD", "register:40f0:8", ["const:47a218:8", "const:4:8"]]
- 0047a218 ["CALL", null, ["callee:0043bb60:8"]]
+ 0047a258 ["INT_ADD", "register:40f0:8", ["const:47a258:8", "const:4:8"]]
+ 0047a258 ["CALL", null, ["callee:0043bb60:8"]]
- 0047a218 bytes 4206ff97
+ 0047a258 bytes 4206ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0a934e500489aeb5a64756930c79bbc"></a>

### [`0047a608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a608.md) → [`0047a648`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047a648.md) FUN_0047a648

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

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
      "definition_site": "0047a65c",
      "incomplete_value": false,
      "site": "0047a660",
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
            "const:388:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047a61c",
      "incomplete_value": false,
      "site": "0047a620",
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
            "const:2b8:8"
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
      "0047a660",
      "DATA",
      [
        "storage",
        "00c652b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047a660",
      "DATA",
      [
        "storage",
        "00c65388",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047a61c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a608.md#insn-0047a61c) · [`0047a630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a608.md#insn-0047a630) · [`0047a650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a608.md#insn-0047a650)
- 新版 `0047a65c`（命令位置の公開資料なし） · `0047a670`（命令位置の公開資料なし） · `0047a690`（命令位置の公開資料なし）

~~~diff
- 0047a61c ["COPY", "tmp:0:8", ["const:2b8:8"]]
- 0047a61c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0047a61c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0047a61c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0047a65c ["COPY", "tmp:0:8", ["const:388:8"]]
+ 0047a65c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0047a65c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0047a65c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0047a61c bytes 08e10a91
+ 0047a65c bytes 08210e91
- 0047a630 ["INT_ADD", "register:40f0:8", ["const:47a630:8", "const:4:8"]]
- 0047a630 ["CALL", null, ["callee:00c53da0:8"]]
+ 0047a670 ["INT_ADD", "register:40f0:8", ["const:47a670:8", "const:4:8"]]
+ 0047a670 ["CALL", null, ["callee:00c53da0:8"]]
- 0047a630 bytes b4651f94
+ 0047a670 bytes cc651f94
- 0047a650 ["COPY", "register:0:8", ["register:4040:8"]]
- 0047a650 ["INT_ADD", "register:40f0:8", ["const:47a650:8", "const:4:8"]]
- 0047a650 ["CALLIND", null, ["register:0:8"]]
+ 0047a690 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047a690 ["INT_ADD", "register:40f0:8", ["const:47a690:8", "const:4:8"]]
+ 0047a690 ["CALLIND", null, ["register:0:8"]]
- 0047a650 bytes 00013fd6
+ 0047a690 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a326ab9944652cb0aca2db47c7559a5f"></a>

### [`0047a664`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a664.md) → [`0047a6a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047a6a4.md) FUN_0047a6a4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "0047a6bc",
      "incomplete_value": false,
      "site": "0047a6c0",
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
            "const:388:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047a67c",
      "incomplete_value": false,
      "site": "0047a680",
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
            "const:2b8:8"
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
      "0047a6c0",
      "DATA",
      [
        "storage",
        "00c652b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047a6c0",
      "DATA",
      [
        "storage",
        "00c65388",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047a67c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a664.md#insn-0047a67c) · [`0047a690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a664.md#insn-0047a690) · [`0047a6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a664.md#insn-0047a6a4)
- 新版 `0047a6bc`（命令位置の公開資料なし） · `0047a6d0`（命令位置の公開資料なし） · `0047a6e4`（命令位置の公開資料なし）

~~~diff
- 0047a67c ["COPY", "tmp:0:8", ["const:2b8:8"]]
- 0047a67c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0047a67c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0047a67c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0047a6bc ["COPY", "tmp:0:8", ["const:388:8"]]
+ 0047a6bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0047a6bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0047a6bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0047a67c bytes 08e10a91
+ 0047a6bc bytes 08210e91
- 0047a690 ["INT_ADD", "register:40f0:8", ["const:47a690:8", "const:4:8"]]
- 0047a690 ["CALL", null, ["callee:00c53da0:8"]]
+ 0047a6d0 ["INT_ADD", "register:40f0:8", ["const:47a6d0:8", "const:4:8"]]
+ 0047a6d0 ["CALL", null, ["callee:00c53da0:8"]]
- 0047a690 bytes 9c651f94
+ 0047a6d0 bytes b4651f94
- 0047a6a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0047a6a4 ["INT_ADD", "register:40f0:8", ["const:47a6a4:8", "const:4:8"]]
- 0047a6a4 ["CALLIND", null, ["register:0:8"]]
+ 0047a6e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047a6e4 ["INT_ADD", "register:40f0:8", ["const:47a6e4:8", "const:4:8"]]
+ 0047a6e4 ["CALLIND", null, ["register:0:8"]]
- 0047a6a4 bytes 00013fd6
+ 0047a6e4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b128402f1849db1f905866036e822e6"></a>

### [`0047a6c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a6c0.md) → [`0047a700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047a700.md) FUN_0047a700

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "0047a724",
      "incomplete_value": false,
      "site": "0047a724",
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
            "const:388:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047a6e4",
      "incomplete_value": false,
      "site": "0047a6e4",
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
            "const:2b8:8"
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
      "0047a724",
      "DATA",
      [
        "storage",
        "00c652b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047a724",
      "DATA",
      [
        "storage",
        "00c65388",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047a6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a6c0.md#insn-0047a6d4) · [`0047a6e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a6c0.md#insn-0047a6e0) · [`0047a6fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a6c0.md#insn-0047a6fc)
- 新版 `0047a714`（命令位置の公開資料なし） · `0047a720`（命令位置の公開資料なし） · `0047a73c`（命令位置の公開資料なし）

~~~diff
- 0047a6d4 ["INT_ADD", "register:40f0:8", ["const:47a6d4:8", "const:4:8"]]
- 0047a6d4 ["CALL", null, ["callee:00c57f60:8"]]
+ 0047a714 ["INT_ADD", "register:40f0:8", ["const:47a714:8", "const:4:8"]]
+ 0047a714 ["CALL", null, ["callee:00c57f60:8"]]
- 0047a6d4 bytes ef751f94
+ 0047a714 bytes 13761f94
- 0047a6e0 ["COPY", "tmp:0:8", ["const:2b8:8"]]
- 0047a6e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0047a6e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0047a6e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0047a720 ["COPY", "tmp:0:8", ["const:388:8"]]
+ 0047a720 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0047a720 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0047a720 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0047a6e0 bytes 29e10a91
+ 0047a720 bytes 29210e91
- 0047a6fc ["INT_ADD", "register:40f0:8", ["const:47a6fc:8", "const:4:8"]]
- 0047a6fc ["CALL", null, ["callee:00c53d70:8"]]
+ 0047a73c ["INT_ADD", "register:40f0:8", ["const:47a73c:8", "const:4:8"]]
+ 0047a73c ["CALL", null, ["callee:00c53d70:8"]]
- 0047a6fc bytes 75651f94
+ 0047a73c bytes 8d651f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ed605a46ad73dbbf5109cbb43ce93cb"></a>

### [`0047a710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a710.md) → [`0047a750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047a750.md) FUN_0047a750

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)

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
      "definition_site": "0047a75c",
      "incomplete_value": false,
      "site": "0047a75c",
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
            "const:388:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047a71c",
      "incomplete_value": false,
      "site": "0047a71c",
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
            "const:2b8:8"
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
      "0047a75c",
      "DATA",
      [
        "storage",
        "00c652b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047a75c",
      "DATA",
      [
        "storage",
        "00c65388",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047a718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a710.md#insn-0047a718) · [`0047a738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a710.md#insn-0047a738)
- 新版 `0047a758`（命令位置の公開資料なし） · `0047a778`（命令位置の公開資料なし）

~~~diff
- 0047a718 ["COPY", "tmp:0:8", ["const:2b8:8"]]
- 0047a718 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0047a718 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0047a718 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0047a758 ["COPY", "tmp:0:8", ["const:388:8"]]
+ 0047a758 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0047a758 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0047a758 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0047a718 bytes 29e10a91
+ 0047a758 bytes 29210e91
- 0047a738 ["INT_ADD", "register:40f0:8", ["const:47a738:8", "const:4:8"]]
- 0047a738 ["CALL", null, ["callee:00c53d70:8"]]
+ 0047a778 ["INT_ADD", "register:40f0:8", ["const:47a778:8", "const:4:8"]]
+ 0047a778 ["CALL", null, ["callee:00c53d70:8"]]
- 0047a738 bytes 66651f94
+ 0047a778 bytes 7e651f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37badafda84ef1db99c93c9588209448"></a>

### [`0047a964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a964.md) → [`0047a9a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047a9a4.md) _INIT_16

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

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
      "definition_site": "0047a9e0",
      "incomplete_value": true,
      "site": "0047a9fc",
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
                "const:f66:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047a9a0",
      "incomplete_value": true,
      "site": "0047a9bc",
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
                "const:f26:8"
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
      "definition_site": "0047aa04",
      "incomplete_value": true,
      "site": "0047aa20",
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
                "const:f79:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047a9c4",
      "incomplete_value": true,
      "site": "0047a9e0",
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
                "const:f39:8"
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
      "definition_site": "0047aa24",
      "incomplete_value": true,
      "site": "0047aa40",
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
                "const:d6e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047a9e4",
      "incomplete_value": true,
      "site": "0047aa00",
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
                "const:dc2:8"
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
      "0047a9e0",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "0047aa04",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "0047aa24",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0047a9e0",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "0047aa04",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "0047aa24",
      "READ",
      [
        "storage",
        "002b8d6e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047a9dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a964.md#insn-0047a9dc) · [`0047a9fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a964.md#insn-0047a9fc) · [`0047aac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047a964.md#insn-0047aac4)
- 新版 `0047aa1c`（命令位置の公開資料なし） · `0047aa3c`（命令位置の公開資料なし） · `0047ab04`（命令位置の公開資料なし）

~~~diff
- 0047a9dc ["COPY", "tmp:0:8", ["const:dc2:8"]]
- 0047a9dc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0047a9dc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0047a9dc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0047aa1c ["COPY", "tmp:0:8", ["const:d6e:8"]]
+ 0047aa1c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0047aa1c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0047aa1c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0047a9dc bytes 4a093791
+ 0047aa1c bytes 4ab93591
- 0047a9fc ["COPY", "tmp:0:8", ["const:f62:8"]]
- 0047a9fc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0047a9fc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0047a9fc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0047aa3c ["COPY", "tmp:0:8", ["const:f15:8"]]
+ 0047aa3c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0047aa3c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0047aa3c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0047a9fc bytes 4a893d91
+ 0047aa3c bytes 4a553c91
- 0047aac4 ["INT_ADD", "register:40f0:8", ["const:47aac4:8", "const:4:8"]]
- 0047aac4 ["CALL", null, ["callee:0043b838:8"]]
+ 0047ab04 ["INT_ADD", "register:40f0:8", ["const:47ab04:8", "const:4:8"]]
+ 0047ab04 ["CALL", null, ["callee:0043b838:8"]]
- 0047aac4 bytes 4d03ff97
+ 0047ab04 bytes 4d03ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e70e428382a40a2e90bdb9858d8987f0"></a>

### [`0047af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047af10.md) → [`0047af50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047af50.md) FUN_0047af50

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b28f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b28/00b28f54.md) · 呼出先 23件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470714.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0047b50c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047b50c.md) [`0047d27c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d27c.md)
- 新版 呼出元 1件 [`00b28ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b28/00b28ff0.md) · 呼出先 23件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470754`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470754.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0047b54c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047b/0047b54c.md) [`0047d2bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047d/0047d2bc.md)

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
      "definition_site": "0047af98",
      "incomplete_value": false,
      "site": "0047afa8",
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
            "const:e08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047af58",
      "incomplete_value": false,
      "site": "0047af68",
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
            "const:d38:8"
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
      "definition_site": "0047b3f8",
      "incomplete_value": true,
      "site": "0047b3fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0047b3b8",
      "incomplete_value": true,
      "site": "0047b3bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0047b3f4",
      "incomplete_value": true,
      "site": "0047b400",
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
      "definition_site": "0047b3b4",
      "incomplete_value": true,
      "site": "0047b3c0",
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
      "0047afa8",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "0047b3e8",
      "READ",
      [
        "storage",
        "00c9abb0",
        null,
        "pointer"
      ]
    ],
    [
      "0047b3ec",
      "READ",
      [
        "storage",
        "00c9abb8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0047afa8",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "0047b3e8",
      "READ",
      [
        "storage",
        "00c9ac80",
        null,
        "pointer"
      ]
    ],
    [
      "0047b3ec",
      "READ",
      [
        "storage",
        "00c9ac88",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047b400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047af10.md#insn-0047b400) · [`0047af4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047af10.md#insn-0047af4c) · [`0047af58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047af10.md#insn-0047af58)
- 新版 `0047b440`（命令位置の公開資料なし） · `0047af8c`（命令位置の公開資料なし） · `0047af98`（命令位置の公開資料なし）

~~~diff
- 0047b400 ["INT_ADD", "register:40f0:8", ["const:47b400:8", "const:4:8"]]
- 0047b400 ["CALL", null, ["callee:00c58080:8"]]
+ 0047b440 ["INT_ADD", "register:40f0:8", ["const:47b440:8", "const:4:8"]]
+ 0047b440 ["CALL", null, ["callee:00c58080:8"]]
- 0047b400 bytes ec721f94
+ 0047b440 bytes 10731f94
- 0047af4c ["INT_ADD", "register:40f0:8", ["const:47af4c:8", "const:4:8"]]
- 0047af4c ["CALL", null, ["callee:00487e60:8"]]
+ 0047af8c ["INT_ADD", "register:40f0:8", ["const:47af8c:8", "const:4:8"]]
+ 0047af8c ["CALL", null, ["callee:00487e60:8"]]
- 0047af4c bytes b5330094
+ 0047af8c bytes b5330094
- 0047af58 ["COPY", "tmp:0:8", ["const:d38:8"]]
- 0047af58 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0047af58 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0047af58 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0047af98 ["COPY", "tmp:0:8", ["const:e08:8"]]
+ 0047af98 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0047af98 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0047af98 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0047af58 bytes 4ae13491
+ 0047af98 bytes 4a213891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-082826711ff8d2d490a67a08181ba1a1"></a>

### [`0047b84c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047b84c.md) → [`0047b88c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047b/0047b88c.md) FUN_0047b88c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0047fa4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047fa4c.md) [`005ba798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ba/005ba798.md) [`00876f04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876f04.md) · 呼出先 13件 [`0043dba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dba4.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`00550c20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550c20.md) [`00550c24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550c24.md) [`00550c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550c28.md)
- 新版 呼出元 3件 [`0047fa8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047f/0047fa8c.md) [`005ba7d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ba/005ba7d8.md) [`00876f5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876f5c.md) · 呼出先 13件 [`0043dbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043dbe4.md) [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`00550c60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550c60.md) [`00550c64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550c64.md) [`00550c68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550c68.md)

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
      "definition_site": "0047b8e4",
      "incomplete_value": true,
      "site": "0047b8e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047b8a4",
      "incomplete_value": true,
      "site": "0047b8a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:20:8"
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
      "definition_site": "0047ba08",
      "incomplete_value": true,
      "site": "0047ba08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7f2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047b9c8",
      "incomplete_value": true,
      "site": "0047b9c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:84e:8"
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
      "definition_site": "0047bb98",
      "incomplete_value": false,
      "site": "0047bb9c",
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
            "const:9d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047bb58",
      "incomplete_value": false,
      "site": "0047bb5c",
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
            "const:8d8:8"
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
      "0047b8d0",
      "READ",
      [
        "storage",
        "002b8020",
        null,
        "string"
      ]
    ],
    [
      "0047b9f4",
      "READ",
      [
        "storage",
        "002af84e",
        null,
        "string"
      ]
    ],
    [
      "0047bb98",
      "PARAM",
      [
        "storage",
        "00ca48d8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0047b8d0",
      "READ",
      [
        "storage",
        "002b8060",
        null,
        "string"
      ]
    ],
    [
      "0047b9f4",
      "READ",
      [
        "storage",
        "002af7f2",
        null,
        "string"
      ]
    ],
    [
      "0047bb98",
      "PARAM",
      [
        "storage",
        "00ca49d8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047bb1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047b84c.md#insn-0047bb1c) · [`0047bb5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047b84c.md#insn-0047bb5c) · [`0047bbe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047b84c.md#insn-0047bbe8)
- 新版 `0047bb5c`（命令位置の公開資料なし） · `0047bb9c`（命令位置の公開資料なし） · `0047bc28`（命令位置の公開資料なし）

~~~diff
- 0047bb1c ["INT_ADD", "register:40f0:8", ["const:47bb1c:8", "const:4:8"]]
- 0047bb1c ["CALL", null, ["callee:00c57f80:8"]]
+ 0047bb5c ["INT_ADD", "register:40f0:8", ["const:47bb5c:8", "const:4:8"]]
+ 0047bb5c ["CALL", null, ["callee:00c57f80:8"]]
- 0047bb1c bytes e5701f94
+ 0047bb5c bytes 09711f94
- 0047bb5c ["INT_ADD", "register:40f0:8", ["const:47bb5c:8", "const:4:8"]]
- 0047bb5c ["CALL", null, ["callee:00c581b0:8"]]
+ 0047bb9c ["INT_ADD", "register:40f0:8", ["const:47bb9c:8", "const:4:8"]]
+ 0047bb9c ["CALL", null, ["callee:00c581b0:8"]]
- 0047bb5c bytes 61711f94
+ 0047bb9c bytes 85711f94
- 0047bbe8 ["INT_ADD", "register:40f0:8", ["const:47bbe8:8", "const:4:8"]]
- 0047bbe8 ["CALL", null, ["callee:00c581c0:8"]]
+ 0047bc28 ["INT_ADD", "register:40f0:8", ["const:47bc28:8", "const:4:8"]]
+ 0047bc28 ["CALL", null, ["callee:00c581c0:8"]]
- 0047bbe8 bytes 42711f94
+ 0047bc28 bytes 66711f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-919af8467476c4a9edcb2587513123ab"></a>

### [`0047bd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047bd00.md) → [`0047bd40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047b/0047bd40.md) FUN_0047bd40

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00854670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00854/00854670.md) · 呼出先 4件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md)
- 新版 呼出元 1件 [`008546c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00854/008546c8.md) · 呼出先 4件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c581b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581b0.md) [`00c581c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581c0.md)

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
      "definition_site": "0047bd58",
      "incomplete_value": false,
      "site": "0047bd60",
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
            "const:9d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047bd18",
      "incomplete_value": false,
      "site": "0047bd20",
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
            "const:8d8:8"
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
      "0047bd58",
      "PARAM",
      [
        "storage",
        "00ca48d8",
        null,
        null
      ]
    ],
    [
      "0047be0c",
      "PARAM",
      [
        "storage",
        "00ca48d8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0047bd58",
      "PARAM",
      [
        "storage",
        "00ca49d8",
        null,
        null
      ]
    ],
    [
      "0047be0c",
      "PARAM",
      [
        "storage",
        "00ca49d8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047bd20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047bd00.md#insn-0047bd20) · [`0047bd18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047bd00.md#insn-0047bd18) · [`0047bd64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047bd00.md#insn-0047bd64)
- 新版 `0047bd60`（命令位置の公開資料なし） · `0047bd58`（命令位置の公開資料なし） · `0047bda4`（命令位置の公開資料なし）

~~~diff
- 0047bd20 ["INT_ADD", "register:40f0:8", ["const:47bd20:8", "const:4:8"]]
- 0047bd20 ["CALL", null, ["callee:00c581b0:8"]]
+ 0047bd60 ["INT_ADD", "register:40f0:8", ["const:47bd60:8", "const:4:8"]]
+ 0047bd60 ["CALL", null, ["callee:00c581b0:8"]]
- 0047bd20 bytes f0701f94
+ 0047bd60 bytes 14711f94
- 0047bd18 ["COPY", "tmp:0:8", ["const:8d8:8"]]
- 0047bd18 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0047bd18 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0047bd18 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0047bd58 ["COPY", "tmp:0:8", ["const:9d8:8"]]
+ 0047bd58 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0047bd58 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0047bd58 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0047bd18 bytes 00602391
+ 0047bd58 bytes 00602791
- 0047bd64 ["INT_ADD", "register:40f0:8", ["const:47bd64:8", "const:4:8"]]
- 0047bd64 ["CALL", null, ["callee:00c53da0:8"]]
+ 0047bda4 ["INT_ADD", "register:40f0:8", ["const:47bda4:8", "const:4:8"]]
+ 0047bda4 ["CALL", null, ["callee:00c53da0:8"]]
- 0047bd64 bytes e75f1f94
+ 0047bda4 bytes ff5f1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-002af6860e7dd73c09290c6ea2c6d8f5"></a>

### [`0047bde0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047bde0.md) → [`0047be20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047b/0047be20.md) FUN_0047be20

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0047c048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047c048.md) · 呼出先 9件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0047d71c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d71c.md) [`0047d720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d720.md) [`0047d724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d724.md) [`0056b23c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0056b/0056b23c.md)
- 新版 呼出元 1件 [`0047c088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047c088.md) · 呼出先 9件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`0047d75c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047d/0047d75c.md) [`0047d760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047d/0047d760.md) [`0047d764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047d/0047d764.md) [`0056b27c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0056b/0056b27c.md)

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
      "definition_site": "0047be54",
      "incomplete_value": false,
      "site": "0047be54",
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
            "const:428:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047be14",
      "incomplete_value": false,
      "site": "0047be14",
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
      "0047be54",
      "DATA",
      [
        "storage",
        "00c65358",
        null,
        "undefined *"
      ]
    ],
    [
      "0047bf04",
      "READ",
      [
        "storage",
        "00c65388",
        null,
        "undefined *"
      ]
    ],
    [
      "0047bf78",
      "READ",
      [
        "storage",
        "00c65378",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0047be54",
      "DATA",
      [
        "storage",
        "00c65428",
        null,
        "undefined *"
      ]
    ],
    [
      "0047bf04",
      "READ",
      [
        "storage",
        "00c65458",
        null,
        "undefined *"
      ]
    ],
    [
      "0047bf78",
      "READ",
      [
        "storage",
        "00c65448",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047be10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047bde0.md#insn-0047be10) · [`0047be24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047bde0.md#insn-0047be24) · [`0047be34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047bde0.md#insn-0047be34)
- 新版 `0047be50`（命令位置の公開資料なし） · `0047be64`（命令位置の公開資料なし） · `0047be74`（命令位置の公開資料なし）

~~~diff
- 0047be10 ["COPY", "tmp:0:8", ["const:358:8"]]
- 0047be10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0047be10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0047be10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0047be50 ["COPY", "tmp:0:8", ["const:428:8"]]
+ 0047be50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0047be50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0047be50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0047be10 bytes 08610d91
+ 0047be50 bytes 08a11091
- 0047be24 ["INT_ADD", "register:40f0:8", ["const:47be24:8", "const:4:8"]]
- 0047be24 ["CALL", null, ["callee:0047d764:8"]]
+ 0047be64 ["INT_ADD", "register:40f0:8", ["const:47be64:8", "const:4:8"]]
+ 0047be64 ["CALL", null, ["callee:0047d764:8"]]
- 0047be24 bytes 40060094
+ 0047be64 bytes 40060094
- 0047be34 ["INT_ADD", "register:40f0:8", ["const:47be34:8", "const:4:8"]]
- 0047be34 ["CALL", null, ["callee:0056b27c:8"]]
+ 0047be74 ["INT_ADD", "register:40f0:8", ["const:47be74:8", "const:4:8"]]
+ 0047be74 ["CALL", null, ["callee:0056b27c:8"]]
- 0047be34 bytes 02bd0394
+ 0047be74 bytes 02bd0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47db1c2bfc2de2a4589e68f0599c137d"></a>

### [`0047c048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047c048.md) → [`0047c088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047c088.md) FUN_0047c088

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0047cddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cddc.md) [`0047cf08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cf08.md) [`0047fa4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047fa4c.md) · 呼出先 22件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0043dba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dba4.md) [`0047bde0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047bde0.md) [`0047c968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047c968.md) [`0047ca8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047ca8c.md)
- 新版 呼出元 4件 [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0047ce1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce1c.md) [`0047cf48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047cf48.md) [`0047fa8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047f/0047fa8c.md) · 呼出先 22件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0043dbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043dbe4.md) [`0047be20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047b/0047be20.md) [`0047c9a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047c9a8.md) [`0047cacc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047cacc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.06% / 新版 99.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0047c2f4",
      "incomplete_value": true,
      "site": "0047c2f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eee:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047c2b4",
      "incomplete_value": true,
      "site": "0047c2b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f3b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 47,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0047c758",
      "incomplete_value": false,
      "site": "0047c75c",
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
            "const:9d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047c718",
      "incomplete_value": false,
      "site": "0047c71c",
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
            "const:8d8:8"
          ]
        ]
      ]
    },
    "ordinal": 48,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0047c794",
      "incomplete_value": false,
      "site": "0047c798",
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
            "const:9d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047c754",
      "incomplete_value": false,
      "site": "0047c758",
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
            "const:8d8:8"
          ]
        ]
      ]
    },
    "ordinal": 52,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0047c2dc",
      "READ",
      [
        "storage",
        "0029ff3b",
        null,
        "string"
      ]
    ],
    [
      "0047c758",
      "PARAM",
      [
        "storage",
        "00ca48d8",
        null,
        null
      ]
    ],
    [
      "0047c794",
      "PARAM",
      [
        "storage",
        "00ca48d8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0047c2dc",
      "READ",
      [
        "storage",
        "0029feee",
        null,
        "string"
      ]
    ],
    [
      "0047c758",
      "PARAM",
      [
        "storage",
        "00ca49d8",
        null,
        null
      ]
    ],
    [
      "0047c794",
      "PARAM",
      [
        "storage",
        "00ca49d8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047c2f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047c048.md#insn-0047c2f4) · [`0047c6dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047c048.md#insn-0047c6dc) · [`0047c718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047c048.md#insn-0047c718)
- 新版 `0047c334`（命令位置の公開資料なし） · `0047c71c`（命令位置の公開資料なし） · `0047c758`（命令位置の公開資料なし）

~~~diff
- 0047c2f4 ["INT_ADD", "register:40f0:8", ["const:47c2f4:8", "const:4:8"]]
- 0047c2f4 ["CALL", null, ["callee:00c57f80:8"]]
+ 0047c334 ["INT_ADD", "register:40f0:8", ["const:47c334:8", "const:4:8"]]
+ 0047c334 ["CALL", null, ["callee:00c57f80:8"]]
- 0047c2f4 bytes ef6e1f94
+ 0047c334 bytes 136f1f94
- 0047c6dc ["COPY", "register:0:8", ["register:4040:8"]]
- 0047c6dc ["INT_ADD", "register:40f0:8", ["const:47c6dc:8", "const:4:8"]]
- 0047c6dc ["CALLIND", null, ["register:0:8"]]
+ 0047c71c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0047c71c ["INT_ADD", "register:40f0:8", ["const:47c71c:8", "const:4:8"]]
+ 0047c71c ["CALLIND", null, ["register:0:8"]]
- 0047c6dc bytes 00013fd6
+ 0047c71c bytes 00013fd6
- 0047c718 ["COPY", "tmp:0:8", ["const:8d8:8"]]
- 0047c718 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0047c718 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0047c718 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0047c758 ["COPY", "tmp:0:8", ["const:9d8:8"]]
+ 0047c758 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0047c758 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0047c758 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0047c718 bytes 00602391
+ 0047c758 bytes 00602791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a64f30abcdf8014ac12cfdc782a73394"></a>

### [`0047d1f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d1f8.md) → [`0047d238`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047d/0047d238.md) FUN_0047d238

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00853c78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00853/00853c78.md) · 呼出先 2件 [`0047e20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e20c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00853cd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00853/00853cd0.md) · 呼出先 2件 [`0047e24c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e24c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "0047d268",
      "incomplete_value": false,
      "site": "0047d274",
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
            "const:4b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047d228",
      "incomplete_value": false,
      "site": "0047d234",
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
            "const:3e8:8"
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
      "0047d274",
      "DATA",
      [
        "storage",
        "00c653e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047d274",
      "DATA",
      [
        "storage",
        "00c654b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047d21c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d1f8.md#insn-0047d21c) · [`0047d228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d1f8.md#insn-0047d228) · [`0047d244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d1f8.md#insn-0047d244)
- 新版 `0047d25c`（命令位置の公開資料なし） · `0047d268`（命令位置の公開資料なし） · `0047d284`（命令位置の公開資料なし）

~~~diff
- 0047d21c ["INT_ADD", "register:40f0:8", ["const:47d21c:8", "const:4:8"]]
- 0047d21c ["CALL", null, ["callee:00c57f60:8"]]
+ 0047d25c ["INT_ADD", "register:40f0:8", ["const:47d25c:8", "const:4:8"]]
+ 0047d25c ["CALL", null, ["callee:00c57f60:8"]]
- 0047d21c bytes 1d6b1f94
+ 0047d25c bytes 416b1f94
- 0047d228 ["COPY", "tmp:0:8", ["const:3e8:8"]]
- 0047d228 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0047d228 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0047d228 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0047d268 ["COPY", "tmp:0:8", ["const:4b8:8"]]
+ 0047d268 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0047d268 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0047d268 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0047d228 bytes 08a10f91
+ 0047d268 bytes 08e11291
- 0047d244 ["INT_ADD", "register:40f0:8", ["const:47d244:8", "const:4:8"]]
- 0047d244 ["CALL", null, ["callee:0047e24c:8"]]
+ 0047d284 ["INT_ADD", "register:40f0:8", ["const:47d284:8", "const:4:8"]]
+ 0047d284 ["CALL", null, ["callee:0047e24c:8"]]
- 0047d244 bytes f2030094
+ 0047d284 bytes f2030094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d5172cddf5cc9fbe1167cd1ca1db201"></a>

### [`0047d404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d404.md) → [`0047d444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047d/0047d444.md) FUN_0047d444

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0047d27c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d27c.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 1件 [`0047d2bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047d/0047d2bc.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "0047d450",
      "incomplete_value": false,
      "site": "0047d454",
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
            "const:f8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047d410",
      "incomplete_value": false,
      "site": "0047d414",
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
            "const:f4c:8"
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
      "0047d450",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0047d450",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047d414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d404.md#insn-0047d414) · [`0047d410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d404.md#insn-0047d410)
- 新版 `0047d454`（命令位置の公開資料なし） · `0047d450`（命令位置の公開資料なし）

~~~diff
- 0047d414 ["INT_ADD", "register:40f0:8", ["const:47d414:8", "const:4:8"]]
- 0047d414 ["CALL", null, ["callee:0043b7b8:8"]]
+ 0047d454 ["INT_ADD", "register:40f0:8", ["const:47d454:8", "const:4:8"]]
+ 0047d454 ["CALL", null, ["callee:0043b7b8:8"]]
- 0047d414 bytes d9f8fe97
+ 0047d454 bytes d9f8fe97
- 0047d410 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 0047d410 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0047d410 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0047d410 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0047d450 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 0047d450 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0047d450 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0047d450 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0047d410 bytes 00303d91
+ 0047d450 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52126438194ed0447f164026722265d0"></a>

### [`0047d5a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d5a0.md) → [`0047d5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047d/0047d5e0.md) FUN_0047d5e0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0047d418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d418.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 1件 [`0047d458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047d/0047d458.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "0047d5ec",
      "incomplete_value": false,
      "site": "0047d5f0",
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
            "const:f8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047d5ac",
      "incomplete_value": false,
      "site": "0047d5b0",
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
            "const:f4c:8"
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
      "0047d5ec",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0047d5ec",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047d5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d5a0.md#insn-0047d5b0) · [`0047d5ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d5a0.md#insn-0047d5ac)
- 新版 `0047d5f0`（命令位置の公開資料なし） · `0047d5ec`（命令位置の公開資料なし）

~~~diff
- 0047d5b0 ["INT_ADD", "register:40f0:8", ["const:47d5b0:8", "const:4:8"]]
- 0047d5b0 ["CALL", null, ["callee:0043b7b8:8"]]
+ 0047d5f0 ["INT_ADD", "register:40f0:8", ["const:47d5f0:8", "const:4:8"]]
+ 0047d5f0 ["CALL", null, ["callee:0043b7b8:8"]]
- 0047d5b0 bytes 72f8fe97
+ 0047d5f0 bytes 72f8fe97
- 0047d5ac ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 0047d5ac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0047d5ac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0047d5ac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0047d5ec ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 0047d5ec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0047d5ec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0047d5ec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0047d5ac bytes 00303d91
+ 0047d5ec bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c307a83f750753d2a0d43a096cc00697"></a>

### [`0047d6b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d6b8.md) → [`0047d6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047d/0047d6f8.md) FUN_0047d6f8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 8件 [`0047b50c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047b50c.md) [`0047d5b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d5b4.md) [`0049b4a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b4a0.md) [`0049bc5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049bc5c.md) [`0049eba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049e/0049eba0.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 8件 [`0047b54c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047b/0047b54c.md) [`0047d5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047d/0047d5f4.md) [`0049b4e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b4e0.md) [`0049bc9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049bc9c.md) [`0049ebe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049ebe0.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "0047d704",
      "incomplete_value": false,
      "site": "0047d708",
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
            "const:f8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047d6c4",
      "incomplete_value": false,
      "site": "0047d6c8",
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
            "const:f4c:8"
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
      "0047d704",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0047d704",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047d6c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d6b8.md#insn-0047d6c8) · [`0047d6c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d6b8.md#insn-0047d6c4)
- 新版 `0047d708`（命令位置の公開資料なし） · `0047d704`（命令位置の公開資料なし）

~~~diff
- 0047d6c8 ["INT_ADD", "register:40f0:8", ["const:47d6c8:8", "const:4:8"]]
- 0047d6c8 ["CALL", null, ["callee:0043b7b8:8"]]
+ 0047d708 ["INT_ADD", "register:40f0:8", ["const:47d708:8", "const:4:8"]]
+ 0047d708 ["CALL", null, ["callee:0043b7b8:8"]]
- 0047d6c8 bytes 2cf8fe97
+ 0047d708 bytes 2cf8fe97
- 0047d6c4 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 0047d6c4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0047d6c4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0047d6c4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0047d704 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 0047d704 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0047d704 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0047d704 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0047d6c4 bytes 00303d91
+ 0047d704 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d021021a4f6cb9c8068746b2372d8aed"></a>

### [`0047d6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d6d4.md) → [`0047d714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047d/0047d714.md) FUN_0047d714

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "0047d738",
      "incomplete_value": false,
      "site": "0047d738",
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
            "const:428:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047d6f8",
      "incomplete_value": false,
      "site": "0047d6f8",
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
      "0047d738",
      "DATA",
      [
        "storage",
        "00c65358",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047d738",
      "DATA",
      [
        "storage",
        "00c65428",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047d6e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d6d4.md#insn-0047d6e8) · [`0047d6f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d6d4.md#insn-0047d6f4)
- 新版 `0047d728`（命令位置の公開資料なし） · `0047d734`（命令位置の公開資料なし）

~~~diff
- 0047d6e8 ["INT_ADD", "register:40f0:8", ["const:47d6e8:8", "const:4:8"]]
- 0047d6e8 ["CALL", null, ["callee:00c57f60:8"]]
+ 0047d728 ["INT_ADD", "register:40f0:8", ["const:47d728:8", "const:4:8"]]
+ 0047d728 ["CALL", null, ["callee:00c57f60:8"]]
- 0047d6e8 bytes ea691f94
+ 0047d728 bytes 0e6a1f94
- 0047d6f4 ["COPY", "tmp:0:8", ["const:358:8"]]
- 0047d6f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0047d6f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0047d6f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0047d734 ["COPY", "tmp:0:8", ["const:428:8"]]
+ 0047d734 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0047d734 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0047d734 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0047d6f4 bytes 08610d91
+ 0047d734 bytes 08a11091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bc5cb8a69063ea02dd66530a256e2a5"></a>

### [`0047d708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d708.md) → [`0047d748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047d/0047d748.md) FUN_0047d748

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0047d754",
      "incomplete_value": false,
      "site": "0047d754",
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
            "const:428:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047d714",
      "incomplete_value": false,
      "site": "0047d714",
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
      "0047d754",
      "DATA",
      [
        "storage",
        "00c65358",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047d754",
      "DATA",
      [
        "storage",
        "00c65428",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047d710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d708.md#insn-0047d710)
- 新版 `0047d750`（命令位置の公開資料なし）

~~~diff
- 0047d710 ["COPY", "tmp:0:8", ["const:358:8"]]
- 0047d710 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0047d710 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0047d710 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0047d750 ["COPY", "tmp:0:8", ["const:428:8"]]
+ 0047d750 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0047d750 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0047d750 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0047d710 bytes 29610d91
+ 0047d750 bytes 29a11091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9de68b78d2d284e4f19f725a9ed3b66f"></a>

### [`0047d860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d860.md) → [`0047d8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047d/0047d8a0.md) FUN_0047d8a0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`0047c968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047c968.md) [`0047d860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d860.md) [`00656e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00656/00656e90.md) [`00781044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00781/00781044.md) · 呼出先 22件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)
- 新版 呼出元 4件 [`0047c9a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047c9a8.md) [`0047d8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047d/0047d8a0.md) [`00656ed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00656/00656ed0.md) [`0078109c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00781/0078109c.md) · 呼出先 22件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`00441d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441d2c.md)

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
      "definition_site": "0047d9fc",
      "incomplete_value": false,
      "site": "0047da04",
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
            "const:f93:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047d9bc",
      "incomplete_value": false,
      "site": "0047d9c4",
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
            "const:f53:8"
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
      "definition_site": "0047da20",
      "incomplete_value": false,
      "site": "0047da2c",
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
            "const:f29:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047d9e0",
      "incomplete_value": false,
      "site": "0047d9ec",
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
            "const:ee9:8"
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
      "definition_site": "0047db54",
      "incomplete_value": false,
      "site": "0047db5c",
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
            "const:e27:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047db14",
      "incomplete_value": false,
      "site": "0047db1c",
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
            "const:de7:8"
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
      "0047d9fc",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "0047da20",
      "PARAM",
      [
        "storage",
        "002c0ee9",
        null,
        "string"
      ]
    ],
    [
      "0047db54",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0047d9fc",
      "PARAM",
      [
        "storage",
        "002b7f93",
        null,
        null
      ]
    ],
    [
      "0047da20",
      "PARAM",
      [
        "storage",
        "002c0f29",
        null,
        "string"
      ]
    ],
    [
      "0047db54",
      "PARAM",
      [
        "storage",
        "002b5e27",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047d9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d860.md#insn-0047d9c4) · [`0047d9ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d860.md#insn-0047d9ec) · [`0047db1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d860.md#insn-0047db1c)
- 新版 `0047da04`（命令位置の公開資料なし） · `0047da2c`（命令位置の公開資料なし） · `0047db5c`（命令位置の公開資料なし）

~~~diff
- 0047d9c4 ["INT_ADD", "register:40f0:8", ["const:47d9c4:8", "const:4:8"]]
- 0047d9c4 ["CALL", null, ["callee:00441ed4:8"]]
+ 0047da04 ["INT_ADD", "register:40f0:8", ["const:47da04:8", "const:4:8"]]
+ 0047da04 ["CALL", null, ["callee:00441ed4:8"]]
- 0047d9c4 bytes 3411ff97
+ 0047da04 bytes 3411ff97
- 0047d9ec ["INT_ADD", "register:40f0:8", ["const:47d9ec:8", "const:4:8"]]
- 0047d9ec ["CALL", null, ["callee:00442834:8"]]
+ 0047da2c ["INT_ADD", "register:40f0:8", ["const:47da2c:8", "const:4:8"]]
+ 0047da2c ["CALL", null, ["callee:00442834:8"]]
- 0047d9ec bytes 8213ff97
+ 0047da2c bytes 8213ff97
- 0047db1c ["INT_ADD", "register:40f0:8", ["const:47db1c:8", "const:4:8"]]
- 0047db1c ["CALL", null, ["callee:00441ed4:8"]]
+ 0047db5c ["INT_ADD", "register:40f0:8", ["const:47db5c:8", "const:4:8"]]
+ 0047db5c ["CALL", null, ["callee:00441ed4:8"]]
- 0047db1c bytes de10ff97
+ 0047db5c bytes de10ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bfb76b863fe6bd6c6cd2a5ec0490e754"></a>

### [`0047e1bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e1bc.md) → [`0047e1fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e1fc.md) FUN_0047e1fc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)

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
      "definition_site": "0047e200",
      "incomplete_value": false,
      "site": "0047e204",
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
            "const:4b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047e1c0",
      "incomplete_value": false,
      "site": "0047e1c4",
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
            "const:3e8:8"
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
      "0047e204",
      "DATA",
      [
        "storage",
        "00c653e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047e204",
      "DATA",
      [
        "storage",
        "00c654b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047e1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e1bc.md#insn-0047e1c0)
- 新版 `0047e200`（命令位置の公開資料なし）

~~~diff
- 0047e1c0 ["COPY", "tmp:0:8", ["const:3e8:8"]]
- 0047e1c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0047e1c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0047e1c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0047e200 ["COPY", "tmp:0:8", ["const:4b8:8"]]
+ 0047e200 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0047e200 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0047e200 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0047e1c0 bytes 08a10f91
+ 0047e200 bytes 08e11291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e9b627960755794a29bdbfe8e3b7788"></a>

### [`0047e1cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e1cc.md) → [`0047e20c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e20c.md) FUN_0047e20c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "0047e21c",
      "incomplete_value": false,
      "site": "0047e224",
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
            "const:4b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047e1dc",
      "incomplete_value": false,
      "site": "0047e1e4",
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
            "const:3e8:8"
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
      "0047e224",
      "DATA",
      [
        "storage",
        "00c653e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047e224",
      "DATA",
      [
        "storage",
        "00c654b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047e1dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e1cc.md#insn-0047e1dc) · [`0047e1e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e1cc.md#insn-0047e1e8)
- 新版 `0047e21c`（命令位置の公開資料なし） · `0047e228`（命令位置の公開資料なし）

~~~diff
- 0047e1dc ["COPY", "tmp:0:8", ["const:3e8:8"]]
- 0047e1dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0047e1dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0047e1dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0047e21c ["COPY", "tmp:0:8", ["const:4b8:8"]]
+ 0047e21c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0047e21c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0047e21c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0047e1dc bytes 08a10f91
+ 0047e21c bytes 08e11291
- 0047e1e8 ["INT_ADD", "register:40f0:8", ["const:47e1e8:8", "const:4:8"]]
- 0047e1e8 ["CALL", null, ["callee:00c57f70:8"]]
+ 0047e228 ["INT_ADD", "register:40f0:8", ["const:47e228:8", "const:4:8"]]
+ 0047e228 ["CALL", null, ["callee:00c57f70:8"]]
- 0047e1e8 bytes 2e671f94
+ 0047e228 bytes 52671f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4808427e7e33d92cd2adea583272e26b"></a>

### [`0047e20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e20c.md) → [`0047e24c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e24c.md) FUN_0047e24c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0047d1f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d1f8.md) · 呼出先 12件 [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`00597ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ec8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)
- 新版 呼出元 1件 [`0047d238`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047d/0047d238.md) · 呼出先 12件 [`0047e64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e64c.md) [`0047e91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e91c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`00597f08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f08.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

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
      "definition_site": "0047e28c",
      "incomplete_value": false,
      "site": "0047e28c",
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
            "const:508:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047e24c",
      "incomplete_value": false,
      "site": "0047e24c",
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
            "const:438:8"
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
      "definition_site": "0047e2f4",
      "incomplete_value": true,
      "site": "0047e2f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:93e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047e2b4",
      "incomplete_value": true,
      "site": "0047e2b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:99a:8"
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
      "definition_site": "0047e30c",
      "incomplete_value": true,
      "site": "0047e30c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047e2cc",
      "incomplete_value": true,
      "site": "0047e2cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2c:8"
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
      "0047e28c",
      "DATA",
      [
        "storage",
        "00c65438",
        null,
        "undefined *"
      ]
    ],
    [
      "0047e2ac",
      "PARAM",
      [
        "storage",
        "002c94d6",
        null,
        "string"
      ]
    ],
    [
      "0047e2c0",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0047e28c",
      "DATA",
      [
        "storage",
        "00c65508",
        null,
        "undefined *"
      ]
    ],
    [
      "0047e2ac",
      "PARAM",
      [
        "storage",
        "002c9516",
        null,
        "string"
      ]
    ],
    [
      "0047e2c0",
      "READ",
      [
        "storage",
        "00ca5038",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047e274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e20c.md#insn-0047e274) · [`0047e2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e20c.md#insn-0047e2f0) · [`0047e310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e20c.md#insn-0047e310)
- 新版 `0047e2b4`（命令位置の公開資料なし） · `0047e330`（命令位置の公開資料なし） · `0047e350`（命令位置の公開資料なし）

~~~diff
- 0047e274 ["INT_ADD", "register:40f0:8", ["const:47e274:8", "const:4:8"]]
- 0047e274 ["CALL", null, ["callee:00c58260:8"]]
+ 0047e2b4 ["INT_ADD", "register:40f0:8", ["const:47e2b4:8", "const:4:8"]]
+ 0047e2b4 ["CALL", null, ["callee:00c58260:8"]]
- 0047e274 bytes c7671f94
+ 0047e2b4 bytes eb671f94
- 0047e2f0 ["INT_ADD", "register:40f0:8", ["const:47e2f0:8", "const:4:8"]]
- 0047e2f0 ["CALL", null, ["callee:0047e64c:8"]]
+ 0047e330 ["INT_ADD", "register:40f0:8", ["const:47e330:8", "const:4:8"]]
+ 0047e330 ["CALL", null, ["callee:0047e64c:8"]]
- 0047e2f0 bytes c7000094
+ 0047e330 bytes c7000094
- 0047e310 ["INT_ADD", "register:40f0:8", ["const:47e310:8", "const:4:8"]]
- 0047e310 ["CALL", null, ["callee:00c53da0:8"]]
+ 0047e350 ["INT_ADD", "register:40f0:8", ["const:47e350:8", "const:4:8"]]
+ 0047e350 ["CALL", null, ["callee:00c53da0:8"]]
- 0047e310 bytes 7c561f94
+ 0047e350 bytes 94561f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db5afdd476214463b75e012eebfccc24"></a>

### [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) → [`0047e64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e64c.md) FUN_0047e64c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 118件 [`0047e20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e20c.md) [`005ba310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ba/005ba310.md) [`005c425c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c4/005c425c.md) [`005cc1b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cc/005cc1b4.md) [`005e1bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e1bb8.md) · 呼出先 14件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`0047ef0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047ef0c.md) [`0047f050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f050.md) [`0047f14c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f14c.md)
- 新版 呼出元 118件 [`0047e24c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e24c.md) [`005ba350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ba/005ba350.md) [`005c429c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c4/005c429c.md) [`005cc1f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005cc/005cc1f4.md) [`005e1bf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e1/005e1bf8.md) · 呼出先 14件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`0047ef4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047ef4c.md) [`0047f090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047f/0047f090.md) [`0047f18c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047f/0047f18c.md)

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
      "definition_site": "0047e714",
      "incomplete_value": false,
      "site": "0047e720",
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
            "const:578:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047e6d4",
      "incomplete_value": false,
      "site": "0047e6e0",
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
            "const:4a8:8"
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
      "0047e720",
      "DATA",
      [
        "storage",
        "00c654a8",
        null,
        "pointer"
      ]
    ],
    [
      "0047e868",
      "READ",
      [
        "storage",
        "00c654b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047e720",
      "DATA",
      [
        "storage",
        "00c65578",
        null,
        "pointer"
      ]
    ],
    [
      "0047e868",
      "READ",
      [
        "storage",
        "00c65588",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047e658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md#insn-0047e658) · [`0047e664`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md#insn-0047e664) · [`0047e678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md#insn-0047e678)
- 新版 `0047e698`（命令位置の公開資料なし） · `0047e6a4`（命令位置の公開資料なし） · `0047e6b8`（命令位置の公開資料なし）

~~~diff
- 0047e658 ["INT_ADD", "register:40f0:8", ["const:47e658:8", "const:4:8"]]
- 0047e658 ["CALL", null, ["callee:00440fb0:8"]]
+ 0047e698 ["INT_ADD", "register:40f0:8", ["const:47e698:8", "const:4:8"]]
+ 0047e698 ["CALL", null, ["callee:00440fb0:8"]]
- 0047e658 bytes 460aff97
+ 0047e698 bytes 460aff97
- 0047e664 ["INT_ADD", "register:40f0:8", ["const:47e664:8", "const:4:8"]]
- 0047e664 ["CALL", null, ["callee:0047ef4c:8"]]
+ 0047e6a4 ["INT_ADD", "register:40f0:8", ["const:47e6a4:8", "const:4:8"]]
+ 0047e6a4 ["CALL", null, ["callee:0047ef4c:8"]]
- 0047e664 bytes 2a020094
+ 0047e6a4 bytes 2a020094
- 0047e678 ["INT_ADD", "register:40f0:8", ["const:47e678:8", "const:4:8"]]
- 0047e678 ["CALL", null, ["callee:00c57f80:8"]]
+ 0047e6b8 ["INT_ADD", "register:40f0:8", ["const:47e6b8:8", "const:4:8"]]
+ 0047e6b8 ["CALL", null, ["callee:00c57f80:8"]]
- 0047e678 bytes 0e661f94
+ 0047e6b8 bytes 32661f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1882d56b1c871a57916dbcafb4ea2d06"></a>

### [`0047e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md) → [`0047e91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e91c.md) FUN_0047e91c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 92件 [`0047e20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e20c.md) [`005ba310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ba/005ba310.md) [`005fa824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fa/005fa824.md) [`006103bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00610/006103bc.md) [`006247a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00624/006247a8.md) · 呼出先 12件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0047f250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f250.md) [`0047f45c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f45c.md) [`00489168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489168.md) [`0048a808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048a/0048a808.md)
- 新版 呼出元 92件 [`0047e24c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e24c.md) [`005ba350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ba/005ba350.md) [`005fa864`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fa/005fa864.md) [`006103fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00610/006103fc.md) [`006247e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00624/006247e8.md) · 呼出先 12件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0047f290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047f/0047f290.md) [`0047f49c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047f/0047f49c.md) [`004891a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/004891a8.md) [`0048a848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048a/0048a848.md)

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
      "definition_site": "0047ea64",
      "incomplete_value": false,
      "site": "0047ea70",
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
            "const:578:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047ea24",
      "incomplete_value": false,
      "site": "0047ea30",
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
            "const:4a8:8"
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
      "definition_site": "0047eae0",
      "incomplete_value": false,
      "site": "0047eaf0",
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
            "const:735:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047eaa0",
      "incomplete_value": false,
      "site": "0047eab0",
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
            "const:6f5:8"
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
      "0047ea70",
      "DATA",
      [
        "storage",
        "00c654a8",
        null,
        "pointer"
      ]
    ],
    [
      "0047eae0",
      "PARAM",
      [
        "storage",
        "002c86f5",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0047ea70",
      "DATA",
      [
        "storage",
        "00c65578",
        null,
        "pointer"
      ]
    ],
    [
      "0047eae0",
      "PARAM",
      [
        "storage",
        "002c8735",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047e9f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md#insn-0047e9f0) · [`0047eab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md#insn-0047eab0) · [`0047e950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md#insn-0047e950)
- 新版 `0047ea30`（命令位置の公開資料なし） · `0047eaf0`（命令位置の公開資料なし） · `0047e990`（命令位置の公開資料なし）

~~~diff
- 0047e9f0 ["INT_ADD", "register:40f0:8", ["const:47e9f0:8", "const:4:8"]]
- 0047e9f0 ["CALL", null, ["callee:00c585c0:8"]]
+ 0047ea30 ["INT_ADD", "register:40f0:8", ["const:47ea30:8", "const:4:8"]]
+ 0047ea30 ["CALL", null, ["callee:00c585c0:8"]]
- 0047e9f0 bytes c0661f94
+ 0047ea30 bytes e4661f94
- 0047eab0 ["INT_ADD", "register:40f0:8", ["const:47eab0:8", "const:4:8"]]
- 0047eab0 ["CALL", null, ["callee:0047f49c:8"]]
+ 0047eaf0 ["INT_ADD", "register:40f0:8", ["const:47eaf0:8", "const:4:8"]]
+ 0047eaf0 ["CALL", null, ["callee:0047f49c:8"]]
- 0047eab0 bytes 6b020094
+ 0047eaf0 bytes 6b020094
- 0047e950 ["INT_ADD", "register:40f0:8", ["const:47e950:8", "const:4:8"]]
- 0047e950 ["CALL", null, ["callee:0043bb60:8"]]
+ 0047e990 ["INT_ADD", "register:40f0:8", ["const:47e990:8", "const:4:8"]]
+ 0047e990 ["CALL", null, ["callee:0043bb60:8"]]
- 0047e950 bytes 74f4fe97
+ 0047e990 bytes 74f4fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bfb3530ed7894f193b602ece9d4a9a51"></a>

### [`0047eba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047eba4.md) → [`0047ebe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047ebe4.md) FUN_0047ebe4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c584e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c584e0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c585b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c585b0.md)

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
      "definition_site": "0047ebfc",
      "incomplete_value": false,
      "site": "0047ec00",
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
            "const:508:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047ebbc",
      "incomplete_value": false,
      "site": "0047ebc0",
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
            "const:438:8"
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
      "0047ec00",
      "DATA",
      [
        "storage",
        "00c65438",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047ec00",
      "DATA",
      [
        "storage",
        "00c65508",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047ebbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047eba4.md#insn-0047ebbc) · [`0047ebcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047eba4.md#insn-0047ebcc) · [`0047ebe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047eba4.md#insn-0047ebe0)
- 新版 `0047ebfc`（命令位置の公開資料なし） · `0047ec0c`（命令位置の公開資料なし） · `0047ec20`（命令位置の公開資料なし）

~~~diff
- 0047ebbc ["COPY", "tmp:0:8", ["const:438:8"]]
- 0047ebbc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0047ebbc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0047ebbc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0047ebfc ["COPY", "tmp:0:8", ["const:508:8"]]
+ 0047ebfc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0047ebfc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0047ebfc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0047ebbc bytes 29e11091
+ 0047ebfc bytes 29211491
- 0047ebcc ["INT_ADD", "register:40f0:8", ["const:47ebcc:8", "const:4:8"]]
- 0047ebcc ["CALL", null, ["callee:00c57f80:8"]]
+ 0047ec0c ["INT_ADD", "register:40f0:8", ["const:47ec0c:8", "const:4:8"]]
+ 0047ec0c ["CALL", null, ["callee:00c57f80:8"]]
- 0047ebcc bytes b9641f94
+ 0047ec0c bytes dd641f94
- 0047ebe0 ["INT_ADD", "register:40f0:8", ["const:47ebe0:8", "const:4:8"]]
- 0047ebe0 ["CALL", null, ["callee:00c53da0:8"]]
+ 0047ec20 ["INT_ADD", "register:40f0:8", ["const:47ec20:8", "const:4:8"]]
+ 0047ec20 ["CALL", null, ["callee:00c53da0:8"]]
- 0047ebe0 bytes 48541f94
+ 0047ec20 bytes 60541f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc406039df0323371062f6192228d64d"></a>

### [`0047ec40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047ec40.md) → [`0047ec80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047ec80.md) FUN_0047ec80

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c584e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c584e0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c585b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c585b0.md)

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
      "definition_site": "0047ec98",
      "incomplete_value": false,
      "site": "0047ec9c",
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
            "const:508:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047ec58",
      "incomplete_value": false,
      "site": "0047ec5c",
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
            "const:438:8"
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
      "0047ec9c",
      "DATA",
      [
        "storage",
        "00c65438",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047ec9c",
      "DATA",
      [
        "storage",
        "00c65508",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047ec58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047ec40.md#insn-0047ec58) · [`0047ec68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047ec40.md#insn-0047ec68) · [`0047ec7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047ec40.md#insn-0047ec7c)
- 新版 `0047ec98`（命令位置の公開資料なし） · `0047eca8`（命令位置の公開資料なし） · `0047ecbc`（命令位置の公開資料なし）

~~~diff
- 0047ec58 ["COPY", "tmp:0:8", ["const:438:8"]]
- 0047ec58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0047ec58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0047ec58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0047ec98 ["COPY", "tmp:0:8", ["const:508:8"]]
+ 0047ec98 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0047ec98 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0047ec98 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0047ec58 bytes 29e11091
+ 0047ec98 bytes 29211491
- 0047ec68 ["INT_ADD", "register:40f0:8", ["const:47ec68:8", "const:4:8"]]
- 0047ec68 ["CALL", null, ["callee:00c57f80:8"]]
+ 0047eca8 ["INT_ADD", "register:40f0:8", ["const:47eca8:8", "const:4:8"]]
+ 0047eca8 ["CALL", null, ["callee:00c57f80:8"]]
- 0047ec68 bytes 92641f94
+ 0047eca8 bytes b6641f94
- 0047ec7c ["INT_ADD", "register:40f0:8", ["const:47ec7c:8", "const:4:8"]]
- 0047ec7c ["CALL", null, ["callee:00c53da0:8"]]
+ 0047ecbc ["INT_ADD", "register:40f0:8", ["const:47ecbc:8", "const:4:8"]]
+ 0047ecbc ["CALL", null, ["callee:00c53da0:8"]]
- 0047ec7c bytes 21541f94
+ 0047ecbc bytes 39541f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9868a463d2f8d8fe162031adf518d05d"></a>

### [`0047f010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f010.md) → [`0047f050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047f/0047f050.md) FUN_0047f050

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)

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
      "definition_site": "0047f054",
      "incomplete_value": false,
      "site": "0047f058",
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
            "const:578:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047f014",
      "incomplete_value": false,
      "site": "0047f018",
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
            "const:4a8:8"
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
      "0047f058",
      "DATA",
      [
        "storage",
        "00c654a8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0047f058",
      "DATA",
      [
        "storage",
        "00c65578",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047f014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f010.md#insn-0047f014)
- 新版 `0047f054`（命令位置の公開資料なし）

~~~diff
- 0047f014 ["COPY", "tmp:0:8", ["const:4a8:8"]]
- 0047f014 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0047f014 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0047f014 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0047f054 ["COPY", "tmp:0:8", ["const:578:8"]]
+ 0047f054 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0047f054 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0047f054 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0047f014 bytes 08a11291
+ 0047f054 bytes 08e11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a5b5a2169355a26464e08ef3209053e"></a>

### [`0047f020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f020.md) → [`0047f060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047f/0047f060.md) FUN_0047f060

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "0047f070",
      "incomplete_value": false,
      "site": "0047f078",
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
            "const:578:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047f030",
      "incomplete_value": false,
      "site": "0047f038",
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
            "const:4a8:8"
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
      "0047f078",
      "DATA",
      [
        "storage",
        "00c654a8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0047f078",
      "DATA",
      [
        "storage",
        "00c65578",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047f030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f020.md#insn-0047f030) · [`0047f03c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f020.md#insn-0047f03c)
- 新版 `0047f070`（命令位置の公開資料なし） · `0047f07c`（命令位置の公開資料なし）

~~~diff
- 0047f030 ["COPY", "tmp:0:8", ["const:4a8:8"]]
- 0047f030 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0047f030 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0047f030 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0047f070 ["COPY", "tmp:0:8", ["const:578:8"]]
+ 0047f070 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0047f070 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0047f070 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0047f030 bytes 08a11291
+ 0047f070 bytes 08e11591
- 0047f03c ["INT_ADD", "register:40f0:8", ["const:47f03c:8", "const:4:8"]]
- 0047f03c ["CALL", null, ["callee:00c57f70:8"]]
+ 0047f07c ["INT_ADD", "register:40f0:8", ["const:47f07c:8", "const:4:8"]]
+ 0047f07c ["CALL", null, ["callee:00c57f70:8"]]
- 0047f03c bytes 99631f94
+ 0047f07c bytes bd631f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fd3b9227e2067c1c8a751911afc8df8"></a>

### [`0047f6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f6d4.md) → [`0047f714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047f/0047f714.md) FUN_0047f714

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0047ece4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047ece4.md) · 呼出先 8件 [`0047f81c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f81c.md) [`0047f97c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f97c.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`0047ed24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047ed24.md) · 呼出先 8件 [`0047f85c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047f/0047f85c.md) [`0047f9bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047f/0047f9bc.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0047f754",
      "incomplete_value": false,
      "site": "0047f760",
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
            "const:5c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047f714",
      "incomplete_value": false,
      "site": "0047f720",
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
            "const:4f8:8"
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
      "definition_site": "0047f788",
      "incomplete_value": true,
      "site": "0047f790",
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
                "const:d90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047f748",
      "incomplete_value": true,
      "site": "0047f750",
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
                "const:d50:8"
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
      "0047f760",
      "DATA",
      [
        "storage",
        "00c654f8",
        null,
        "pointer"
      ]
    ],
    [
      "0047f788",
      "READ",
      [
        "storage",
        "002c2d50",
        null,
        null
      ]
    ],
    [
      "0047f7d8",
      "READ",
      [
        "storage",
        "00c65508",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047f760",
      "DATA",
      [
        "storage",
        "00c655c8",
        null,
        "pointer"
      ]
    ],
    [
      "0047f788",
      "READ",
      [
        "storage",
        "002c2d90",
        null,
        null
      ]
    ],
    [
      "0047f7d8",
      "READ",
      [
        "storage",
        "00c655d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047f760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f6d4.md#insn-0047f760) · [`0047f704`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f6d4.md#insn-0047f704) · [`0047f714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f6d4.md#insn-0047f714)
- 新版 `0047f7a0`（命令位置の公開資料なし） · `0047f744`（命令位置の公開資料なし） · `0047f754`（命令位置の公開資料なし）

~~~diff
- 0047f760 ["INT_ADD", "register:40f0:8", ["const:47f760:8", "const:4:8"]]
- 0047f760 ["CALL", null, ["callee:0047f85c:8"]]
+ 0047f7a0 ["INT_ADD", "register:40f0:8", ["const:47f7a0:8", "const:4:8"]]
+ 0047f7a0 ["CALL", null, ["callee:0047f85c:8"]]
- 0047f760 bytes 2f000094
+ 0047f7a0 bytes 2f000094
- 0047f704 ["INT_ADD", "register:40f0:8", ["const:47f704:8", "const:4:8"]]
- 0047f704 ["CALL", null, ["callee:00c57f60:8"]]
+ 0047f744 ["INT_ADD", "register:40f0:8", ["const:47f744:8", "const:4:8"]]
+ 0047f744 ["CALL", null, ["callee:00c57f60:8"]]
- 0047f704 bytes e3611f94
+ 0047f744 bytes 07621f94
- 0047f714 ["COPY", "tmp:0:8", ["const:4f8:8"]]
- 0047f714 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0047f714 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0047f714 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0047f754 ["COPY", "tmp:0:8", ["const:5c8:8"]]
+ 0047f754 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0047f754 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0047f754 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0047f714 bytes 08e11391
+ 0047f754 bytes 08211791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a38b7047722ec12411a972bbd4658588"></a>

### [`0047f81c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f81c.md) → [`0047f85c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047f/0047f85c.md) FUN_0047f85c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0047f6d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f6d4.md) · 呼出先 6件 [`0047fc6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047fc6c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58100.md) [`00c58110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58110.md)
- 新版 呼出元 1件 [`0047f714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047f/0047f714.md) · 呼出先 6件 [`0047fcac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047f/0047fcac.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c581d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581d0.md) [`00c581e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581e0.md)

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
      "definition_site": "0047f8c8",
      "incomplete_value": false,
      "site": "0047f8d4",
      "value": [
        "leaf",
        "const:47fcac:8"
      ]
    },
    "old": {
      "definition_site": "0047f888",
      "incomplete_value": false,
      "site": "0047f894",
      "value": [
        "leaf",
        "const:47fc6c:8"
      ]
    },
    "ordinal": 3,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0047f918",
      "incomplete_value": false,
      "site": "0047f91c",
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
            "const:eda:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047f8d8",
      "incomplete_value": false,
      "site": "0047f8dc",
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
            "const:f27:8"
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
      "0047f8c8",
      "PARAM",
      [
        "storage",
        "0047fc6c",
        null,
        null
      ]
    ],
    [
      "0047f918",
      "PARAM",
      [
        "storage",
        "002a3f27",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0047f8c8",
      "PARAM",
      [
        "storage",
        "0047fcac",
        null,
        null
      ]
    ],
    [
      "0047f918",
      "PARAM",
      [
        "storage",
        "002a3eda",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047f894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f81c.md#insn-0047f894) · [`0047f8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f81c.md#insn-0047f8dc) · [`0047f850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f81c.md#insn-0047f850)
- 新版 `0047f8d4`（命令位置の公開資料なし） · `0047f91c`（命令位置の公開資料なし） · `0047f890`（命令位置の公開資料なし）

~~~diff
- 0047f894 ["INT_ADD", "register:40f0:8", ["const:47f894:8", "const:4:8"]]
- 0047f894 ["CALL", null, ["callee:00c581e0:8"]]
+ 0047f8d4 ["INT_ADD", "register:40f0:8", ["const:47f8d4:8", "const:4:8"]]
+ 0047f8d4 ["CALL", null, ["callee:00c581e0:8"]]
- 0047f894 bytes 1f621f94
+ 0047f8d4 bytes 43621f94
- 0047f8dc ["INT_ADD", "register:40f0:8", ["const:47f8dc:8", "const:4:8"]]
- 0047f8dc ["CALL", null, ["callee:00c581f0:8"]]
+ 0047f91c ["INT_ADD", "register:40f0:8", ["const:47f91c:8", "const:4:8"]]
+ 0047f91c ["CALL", null, ["callee:00c581f0:8"]]
- 0047f8dc bytes 11621f94
+ 0047f91c bytes 35621f94
- 0047f850 ["INT_ADD", "register:40f0:8", ["const:47f850:8", "const:4:8"]]
- 0047f850 ["CALL", null, ["callee:00c57f60:8"]]
+ 0047f890 ["INT_ADD", "register:40f0:8", ["const:47f890:8", "const:4:8"]]
+ 0047f890 ["CALL", null, ["callee:00c57f60:8"]]
- 0047f850 bytes 90611f94
+ 0047f890 bytes b4611f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9cba19eab3856bd34dcb2b6f89d0857"></a>

### [`0047f928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f928.md) → [`0047f968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047f/0047f968.md) FUN_0047f968

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c57e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e60.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c580d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580d0.md) [`00c582f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582f0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c57f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f30.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c581a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581a0.md) [`00c583c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583c0.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)

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
      "definition_site": "0047f98c",
      "incomplete_value": true,
      "site": "0047f98c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0047f94c",
      "incomplete_value": true,
      "site": "0047f94c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "0047f980",
      "READ",
      [
        "storage",
        "00c9ac50",
        null,
        "pointer"
      ]
    ],
    [
      "0047f98c",
      "DATA",
      [
        "storage",
        "00c92cd8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "0047f980",
      "READ",
      [
        "storage",
        "00c9ad20",
        null,
        "pointer"
      ]
    ],
    [
      "0047f98c",
      "DATA",
      [
        "storage",
        "00c92da8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047f940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f928.md#insn-0047f940) · [`0047f950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f928.md#insn-0047f950) · [`0047f958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f928.md#insn-0047f958)
- 新版 `0047f980`（命令位置の公開資料なし） · `0047f990`（命令位置の公開資料なし） · `0047f998`（命令位置の公開資料なし）

~~~diff
- 0047f940 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c50:8"]]
- 0047f940 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0047f980 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d20:8"]]
+ 0047f980 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0047f940 bytes 082946f9
+ 0047f980 bytes 089146f9
- 0047f950 ["INT_ADD", "register:40f0:8", ["const:47f950:8", "const:4:8"]]
- 0047f950 ["CALL", null, ["callee:00c581a0:8"]]
+ 0047f990 ["INT_ADD", "register:40f0:8", ["const:47f990:8", "const:4:8"]]
+ 0047f990 ["CALL", null, ["callee:00c581a0:8"]]
- 0047f950 bytes e0611f94
+ 0047f990 bytes 04621f94
- 0047f958 ["INT_ADD", "register:40f0:8", ["const:47f958:8", "const:4:8"]]
- 0047f958 ["CALL", null, ["callee:00c57f30:8"]]
+ 0047f998 ["INT_ADD", "register:40f0:8", ["const:47f998:8", "const:4:8"]]
+ 0047f998 ["CALL", null, ["callee:00c57f30:8"]]
- 0047f958 bytes 42611f94
+ 0047f998 bytes 66611f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-340fbcb69925879099e7fd17fd8818a3"></a>

### [`0047f9a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f9a4.md) → [`0047f9e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047f/0047f9e4.md) FUN_0047f9e4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047fa4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047fa4c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58550.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047fa8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047f/0047fa8c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58620.md)

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
      "site": "0047fa08",
      "value": [
        "leaf",
        "ram:47fa8c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0047f9c8",
      "value": [
        "leaf",
        "ram:47fa4c:8"
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
      "0047fa08",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047fa4c"
      ]
    ]
  ],
  "added": [
    [
      "0047fa08",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047fa8c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047f9c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f9a4.md#insn-0047f9c8) · [`0047f9d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f9a4.md#insn-0047f9d0) · [`0047fa44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047f9a4.md#insn-0047fa44)
- 新版 `0047fa08`（命令位置の公開資料なし） · `0047fa10`（命令位置の公開資料なし） · `0047fa84`（命令位置の公開資料なし）

~~~diff
- 0047f9c8 ["INT_ADD", "register:40f0:8", ["const:47f9c8:8", "const:4:8"]]
- 0047f9c8 ["CALL", null, ["ram:47fa4c:8"]]
+ 0047fa08 ["INT_ADD", "register:40f0:8", ["const:47fa08:8", "const:4:8"]]
+ 0047fa08 ["CALL", null, ["ram:47fa8c:8"]]
- 0047f9c8 bytes 21000094
+ 0047fa08 bytes 21000094
- 0047f9d0 ["INT_ADD", "register:40f0:8", ["const:47f9d0:8", "const:4:8"]]
- 0047f9d0 ["CALL", null, ["callee:00c58620:8"]]
+ 0047fa10 ["INT_ADD", "register:40f0:8", ["const:47fa10:8", "const:4:8"]]
+ 0047fa10 ["CALL", null, ["callee:00c58620:8"]]
- 0047f9d0 bytes e0621f94
+ 0047fa10 bytes 04631f94
- 0047fa44 ["INT_ADD", "register:40f0:8", ["const:47fa44:8", "const:4:8"]]
- 0047fa44 ["CALL", null, ["callee:00c57fb0:8"]]
+ 0047fa84 ["INT_ADD", "register:40f0:8", ["const:47fa84:8", "const:4:8"]]
+ 0047fa84 ["CALL", null, ["callee:00c57fb0:8"]]
- 0047fa44 bytes 27611f94
+ 0047fa84 bytes 4b611f94
~~~


<a id="compare-06948473c20b03980f32212bd6e24323"></a>

### [`0047fd88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047fd88.md) → [`0047fdc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047f/0047fdc8.md) _INIT_17

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

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
      "definition_site": "0047fe04",
      "incomplete_value": true,
      "site": "0047fe20",
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
                "const:f66:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047fdc4",
      "incomplete_value": true,
      "site": "0047fde0",
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
                "const:f26:8"
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
      "definition_site": "0047fe28",
      "incomplete_value": true,
      "site": "0047fe44",
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
                "const:f79:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047fde8",
      "incomplete_value": true,
      "site": "0047fe04",
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
                "const:f39:8"
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
      "definition_site": "0047fe48",
      "incomplete_value": true,
      "site": "0047fe64",
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
                "const:d6e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047fe08",
      "incomplete_value": true,
      "site": "0047fe24",
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
                "const:dc2:8"
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
      "0047fe04",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "0047fe28",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "0047fe48",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0047fe04",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "0047fe28",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "0047fe48",
      "READ",
      [
        "storage",
        "002b8d6e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047fe00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047fd88.md#insn-0047fe00) · [`0047fe20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047fd88.md#insn-0047fe20) · [`0047fee8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047f/0047fd88.md#insn-0047fee8)
- 新版 `0047fe40`（命令位置の公開資料なし） · `0047fe60`（命令位置の公開資料なし） · `0047ff28`（命令位置の公開資料なし）

~~~diff
- 0047fe00 ["COPY", "tmp:0:8", ["const:dc2:8"]]
- 0047fe00 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0047fe00 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0047fe00 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0047fe40 ["COPY", "tmp:0:8", ["const:d6e:8"]]
+ 0047fe40 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0047fe40 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0047fe40 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0047fe00 bytes 4a093791
+ 0047fe40 bytes 4ab93591
- 0047fe20 ["COPY", "tmp:0:8", ["const:f62:8"]]
- 0047fe20 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0047fe20 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0047fe20 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0047fe60 ["COPY", "tmp:0:8", ["const:f15:8"]]
+ 0047fe60 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0047fe60 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0047fe60 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0047fe20 bytes 4a893d91
+ 0047fe60 bytes 4a553c91
- 0047fee8 ["INT_ADD", "register:40f0:8", ["const:47fee8:8", "const:4:8"]]
- 0047fee8 ["CALL", null, ["callee:0043b838:8"]]
+ 0047ff28 ["INT_ADD", "register:40f0:8", ["const:47ff28:8", "const:4:8"]]
+ 0047ff28 ["CALL", null, ["callee:0043b838:8"]]
- 0047fee8 bytes 44eefe97
+ 0047ff28 bytes 44eefe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-514a9252455775d32dbfe084f2991ec4"></a>

### [`00481430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481430.md) → [`00481470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00481/00481470.md) FUN_00481470

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 18件 [`0043c258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043c/0043c258.md) [`0043ec60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043ec60.md) [`0043f91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f91c.md) [`00470f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470f34.md) [`00637850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00637/00637850.md) · 呼出先 0件 
- 新版 呼出元 18件 [`0043c298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043c/0043c298.md) [`0043eca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043eca0.md) [`0043f95c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f95c.md) [`00470f74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470f74.md) [`00637890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00637/00637890.md) · 呼出先 0件 

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
      "definition_site": "00481484",
      "incomplete_value": false,
      "site": "00481488",
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
            "const:610:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00481444",
      "incomplete_value": false,
      "site": "00481448",
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
            "const:540:8"
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
      "00481488",
      "DATA",
      [
        "storage",
        "00c65540",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00481488",
      "DATA",
      [
        "storage",
        "00c65610",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00481444`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481430.md#insn-00481444)
- 新版 `00481484`（命令位置の公開資料なし）

~~~diff
- 00481444 ["COPY", "tmp:0:8", ["const:540:8"]]
- 00481444 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00481444 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00481444 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00481484 ["COPY", "tmp:0:8", ["const:610:8"]]
+ 00481484 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00481484 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00481484 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00481444 bytes 08011591
+ 00481484 bytes 08411891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be677a94b0aca83cf0164dd9abccfa5e"></a>

### [`00482b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/00482b0c.md) → [`00482b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00482/00482b4c.md) FUN_00482b4c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 17件 [`0043c258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043c/0043c258.md) [`0043ec60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043ec60.md) [`0043f91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f91c.md) [`00470f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470f34.md) [`00482b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/00482b0c.md) · 呼出先 34件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0043de78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043de78.md) [`00440b00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440b00.md) [`00481460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481460.md)
- 新版 呼出元 17件 [`0043c298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043c/0043c298.md) [`0043eca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043eca0.md) [`0043f95c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f95c.md) [`00470f74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470f74.md) [`00482b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00482/00482b4c.md) · 呼出先 34件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`0043deb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043deb8.md) [`00440b40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440b40.md) [`004814a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00481/004814a0.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 95.14% / 新版 95.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 13件, `call_target` 4件, `store_destination` 4件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0048328c",
      "incomplete_value": true,
      "site": "0048328c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d8:8"
          ],
          [
            "leaf",
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048324c",
      "incomplete_value": true,
      "site": "0048324c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d8:8"
          ],
          [
            "leaf",
            "const:f68:8"
          ]
        ]
      ]
    },
    "ordinal": 48,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004833fc",
      "incomplete_value": false,
      "site": "00483400",
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
            "const:610:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004833bc",
      "incomplete_value": false,
      "site": "004833c0",
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
            "const:540:8"
          ]
        ]
      ]
    },
    "ordinal": 64,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00483660",
      "incomplete_value": true,
      "site": "00483660",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d8:8"
          ],
          [
            "leaf",
            "const:58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00483620",
      "incomplete_value": true,
      "site": "00483620",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d8:8"
          ],
          [
            "leaf",
            "const:f58:8"
          ]
        ]
      ]
    },
    "ordinal": 76,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004831a0",
      "READ",
      [
        "storage",
        "00ca4f70",
        null,
        "undefined1"
      ]
    ],
    [
      "004831ac",
      "READ",
      [
        "storage",
        "00ca4f68",
        null,
        "undefined8"
      ]
    ],
    [
      "00483200",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ]
  ],
  "added": [
    [
      "004831a0",
      "READ",
      [
        "storage",
        "00ca5070",
        null,
        "undefined1"
      ]
    ],
    [
      "004831ac",
      "READ",
      [
        "storage",
        "00ca5068",
        null,
        "undefined8"
      ]
    ],
    [
      "00483200",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004831c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/00482b0c.md#insn-004831c0) · [`004831d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/00482b0c.md#insn-004831d4) · [`004831fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/00482b0c.md#insn-004831fc)
- 新版 `00483200`（命令位置の公開資料なし） · `00483214`（命令位置の公開資料なし） · `0048323c`（命令位置の公開資料なし）

~~~diff
- 004831c0 ["INT_ADD", "register:40f0:8", ["const:4831c0:8", "const:4:8"]]
- 004831c0 ["CALL", null, ["ram:48ccf8:8"]]
+ 00483200 ["INT_ADD", "register:40f0:8", ["const:483200:8", "const:4:8"]]
+ 00483200 ["CALL", null, ["ram:48cd38:8"]]
- 004831c0 bytes ce260094
+ 00483200 bytes ce260094
- 004831d4 ["INT_ADD", "register:40f0:8", ["const:4831d4:8", "const:4:8"]]
- 004831d4 ["CALL", null, ["callee:0043de18:8"]]
+ 00483214 ["INT_ADD", "register:40f0:8", ["const:483214:8", "const:4:8"]]
+ 00483214 ["CALL", null, ["callee:0043de18:8"]]
- 004831d4 bytes 01ebfe97
+ 00483214 bytes 01ebfe97
- 004831fc ["INT_ADD", "register:40f0:8", ["const:4831fc:8", "const:4:8"]]
- 004831fc ["CALL", null, ["ram:48ccf8:8"]]
+ 0048323c ["INT_ADD", "register:40f0:8", ["const:48323c:8", "const:4:8"]]
+ 0048323c ["CALL", null, ["ram:48cd38:8"]]
- 004831fc bytes bf260094
+ 0048323c bytes bf260094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b535768a748acaa2b80288da08b73b20"></a>

### [`004838cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/004838cc.md) → [`0048390c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00483/0048390c.md) FUN_0048390c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00a1a750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a750.md) [`00a223d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a22/00a223d0.md) · 呼出先 18件 [`0043dba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dba4.md) [`00486dcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486dcc.md) [`00486ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486ea4.md) [`00487128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487128.md) [`00550c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550c28.md)
- 新版 呼出元 2件 [`00a1a7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a1a/00a1a7a4.md) [`00a22424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a22/00a22424.md) · 呼出先 18件 [`0043dbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043dbe4.md) [`00486e0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00486/00486e0c.md) [`00486ee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00486/00486ee4.md) [`00487168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487168.md) [`00550c68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550c68.md)

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
      "definition_site": "00483b00",
      "incomplete_value": false,
      "site": "00483b08",
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
            "const:700:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00483ac0",
      "incomplete_value": false,
      "site": "00483ac8",
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
            "const:630:8"
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
      "definition_site": "00483b28",
      "incomplete_value": false,
      "site": "00483b28",
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
            "const:750:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00483ae8",
      "incomplete_value": false,
      "site": "00483ae8",
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
            "const:680:8"
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
      "definition_site": "00483b50",
      "incomplete_value": false,
      "site": "00483b60",
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
            "const:790:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00483b10",
      "incomplete_value": false,
      "site": "00483b20",
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
            "const:6c0:8"
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
      "00483b08",
      "DATA",
      [
        "storage",
        "00c65630",
        null,
        "pointer"
      ]
    ],
    [
      "00483b28",
      "DATA",
      [
        "storage",
        "00c65680",
        null,
        null
      ]
    ],
    [
      "00483b60",
      "DATA",
      [
        "storage",
        "00c656c0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00483b08",
      "DATA",
      [
        "storage",
        "00c65700",
        null,
        "pointer"
      ]
    ],
    [
      "00483b28",
      "DATA",
      [
        "storage",
        "00c65750",
        null,
        null
      ]
    ],
    [
      "00483b60",
      "DATA",
      [
        "storage",
        "00c65790",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00483aa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/004838cc.md#insn-00483aa8) · [`00483b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/004838cc.md#insn-00483b08) · [`00483b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/004838cc.md#insn-00483b80)
- 新版 `00483ae8`（命令位置の公開資料なし） · `00483b48`（命令位置の公開資料なし） · `00483bc0`（命令位置の公開資料なし）

~~~diff
- 00483aa8 ["INT_ADD", "register:40f0:8", ["const:483aa8:8", "const:4:8"]]
- 00483aa8 ["CALL", null, ["callee:0055e8b0:8"]]
+ 00483ae8 ["INT_ADD", "register:40f0:8", ["const:483ae8:8", "const:4:8"]]
+ 00483ae8 ["CALL", null, ["callee:0055e8b0:8"]]
- 00483aa8 bytes 726b0394
+ 00483ae8 bytes 726b0394
- 00483b08 ["INT_ADD", "register:40f0:8", ["const:483b08:8", "const:4:8"]]
- 00483b08 ["CALL", null, ["callee:00c57f60:8"]]
+ 00483b48 ["INT_ADD", "register:40f0:8", ["const:483b48:8", "const:4:8"]]
+ 00483b48 ["CALL", null, ["callee:00c57f60:8"]]
- 00483b08 bytes e2501f94
+ 00483b48 bytes 06511f94
- 00483b80 ["INT_ADD", "register:40f0:8", ["const:483b80:8", "const:4:8"]]
- 00483b80 ["CALL", null, ["callee:00c57f50:8"]]
+ 00483bc0 ["INT_ADD", "register:40f0:8", ["const:483bc0:8", "const:4:8"]]
+ 00483bc0 ["CALL", null, ["callee:00c57f50:8"]]
- 00483b80 bytes c0501f94
+ 00483bc0 bytes e4501f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a32a2f0d7a02572480bf150b831c033e"></a>

### [`004847c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/004847c0.md) → [`00484800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00484/00484800.md) FUN_00484800

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`008725a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00872/008725a0.md) [`009d5cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d5/009d5cf8.md) [`009d992c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d9/009d992c.md) [`00ab88a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ab8/00ab88a4.md) · 呼出先 14件 [`0043dba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dba4.md) [`00470e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470e54.md) [`00471724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471724.md) [`00471930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471930.md) [`00481f84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481f84.md)
- 新版 呼出元 4件 [`008725f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00872/008725f8.md) [`009d5d4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d5/009d5d4c.md) [`009d9980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d9/009d9980.md) [`00ab8914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ab8/00ab8914.md) · 呼出先 14件 [`0043dbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043dbe4.md) [`00470e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470e94.md) [`00471764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00471/00471764.md) [`00471970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00471/00471970.md) [`00481fc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00481/00481fc4.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.59% / 新版 98.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004848b8",
      "incomplete_value": false,
      "site": "004848c4",
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
            "const:610:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00484878",
      "incomplete_value": false,
      "site": "00484884",
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
            "const:540:8"
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
      "site": "00484830",
      "value": [
        "leaf",
        "ram:470e94:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004847f0",
      "value": [
        "leaf",
        "ram:470e54:8"
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
      "site": "00484a8c",
      "value": [
        "leaf",
        "ram:470e94:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00484a4c",
      "value": [
        "leaf",
        "ram:470e54:8"
      ]
    },
    "ordinal": 28,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00484830",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00470e54"
      ]
    ],
    [
      "004848c4",
      "DATA",
      [
        "storage",
        "00c65540",
        null,
        "undefined *"
      ]
    ],
    [
      "0048494c",
      "DATA",
      [
        "storage",
        "00c65540",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00484830",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00470e94"
      ]
    ],
    [
      "004848c4",
      "DATA",
      [
        "storage",
        "00c65610",
        null,
        "undefined *"
      ]
    ],
    [
      "0048494c",
      "DATA",
      [
        "storage",
        "00c65610",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004847f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/004847c0.md#insn-004847f0) · [`004848c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/004847c0.md#insn-004848c4) · [`00484a4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/004847c0.md#insn-00484a4c)
- 新版 `00484830`（命令位置の公開資料なし） · `00484904`（命令位置の公開資料なし） · `00484a8c`（命令位置の公開資料なし）

~~~diff
- 004847f0 ["INT_ADD", "register:40f0:8", ["const:4847f0:8", "const:4:8"]]
- 004847f0 ["CALL", null, ["ram:470e54:8"]]
+ 00484830 ["INT_ADD", "register:40f0:8", ["const:484830:8", "const:4:8"]]
+ 00484830 ["CALL", null, ["ram:470e94:8"]]
- 004847f0 bytes 99b1ff97
+ 00484830 bytes 99b1ff97
- 004848c4 ["INT_ADD", "register:40f0:8", ["const:4848c4:8", "const:4:8"]]
- 004848c4 ["CALL", null, ["callee:00c57f80:8"]]
+ 00484904 ["INT_ADD", "register:40f0:8", ["const:484904:8", "const:4:8"]]
+ 00484904 ["CALL", null, ["callee:00c57f80:8"]]
- 004848c4 bytes 7b4d1f94
+ 00484904 bytes 9f4d1f94
- 00484a4c ["INT_ADD", "register:40f0:8", ["const:484a4c:8", "const:4:8"]]
- 00484a4c ["CALL", null, ["ram:470e54:8"]]
+ 00484a8c ["INT_ADD", "register:40f0:8", ["const:484a8c:8", "const:4:8"]]
+ 00484a8c ["CALL", null, ["ram:470e94:8"]]
- 00484a4c bytes 02b1ff97
+ 00484a8c bytes 02b1ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83ba2b48b2a3826d52474832c9084e13"></a>

### [`00484cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/00484cdc.md) → [`00484d1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00484/00484d1c.md) FUN_00484d1c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0087f368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087f/0087f368.md) [`00a14a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a14/00a14a80.md) · 呼出先 4件 [`00597610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597610.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 2件 [`0087f3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087f/0087f3c0.md) [`00a14ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a14/00a14ad4.md) · 呼出先 4件 [`00597650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597650.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

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
      "definition_site": "00484d50",
      "incomplete_value": false,
      "site": "00484d58",
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
            "const:668:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00484d10",
      "incomplete_value": false,
      "site": "00484d18",
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
            "const:598:8"
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
      "00484d58",
      "DATA",
      [
        "storage",
        "00c65598",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00484d58",
      "DATA",
      [
        "storage",
        "00c65668",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00484d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/00484cdc.md#insn-00484d10) · [`00484d2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/00484cdc.md#insn-00484d2c) · [`00484d4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/00484cdc.md#insn-00484d4c)
- 新版 `00484d50`（命令位置の公開資料なし） · `00484d6c`（命令位置の公開資料なし） · `00484d8c`（命令位置の公開資料なし）

~~~diff
- 00484d10 ["COPY", "tmp:0:8", ["const:598:8"]]
- 00484d10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00484d10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00484d10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00484d50 ["COPY", "tmp:0:8", ["const:668:8"]]
+ 00484d50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00484d50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00484d50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00484d10 bytes 08611691
+ 00484d50 bytes 08a11991
- 00484d2c ["INT_ADD", "register:40f0:8", ["const:484d2c:8", "const:4:8"]]
- 00484d2c ["CALL", null, ["callee:00597650:8"]]
+ 00484d6c ["INT_ADD", "register:40f0:8", ["const:484d6c:8", "const:4:8"]]
+ 00484d6c ["CALL", null, ["callee:00597650:8"]]
- 00484d2c bytes 394a0494
+ 00484d6c bytes 394a0494
- 00484d4c ["INT_ADD", "register:40f0:8", ["const:484d4c:8", "const:4:8"]]
- 00484d4c ["CALL", null, ["callee:00c53da0:8"]]
+ 00484d8c ["INT_ADD", "register:40f0:8", ["const:484d8c:8", "const:4:8"]]
+ 00484d8c ["CALL", null, ["callee:00c53da0:8"]]
- 00484d4c bytes ed3b1f94
+ 00484d8c bytes 053c1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dada7374c88ee818b77411232486a272"></a>

### [`004853b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/004853b0.md) → [`004853f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00485/004853f0.md) FUN_004853f0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00485620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/00485620.md) · 呼出先 8件 [`0055e870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e870.md) [`00560458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560458.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`00485660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00485/00485660.md) · 呼出先 8件 [`0055e8b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055e8b0.md) [`00560498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/00560498.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

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
      "definition_site": "004855cc",
      "incomplete_value": false,
      "site": "004855d4",
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
    "old": {
      "definition_site": "0048558c",
      "incomplete_value": false,
      "site": "00485594",
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
            "const:3ea:8"
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
      "004855cc",
      "PARAM",
      [
        "storage",
        "002a63ea",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "004855cc",
      "PARAM",
      [
        "storage",
        "002a638e",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00485554`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/004853b0.md#insn-00485554) · [`00485594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/004853b0.md#insn-00485594) · [`00485400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/004853b0.md#insn-00485400)
- 新版 `00485594`（命令位置の公開資料なし） · `004855d4`（命令位置の公開資料なし） · `00485440`（命令位置の公開資料なし）

~~~diff
- 00485554 ["INT_ADD", "register:40f0:8", ["const:485554:8", "const:4:8"]]
- 00485554 ["CALL", null, ["callee:00c57f80:8"]]
+ 00485594 ["INT_ADD", "register:40f0:8", ["const:485594:8", "const:4:8"]]
+ 00485594 ["CALL", null, ["callee:00c57f80:8"]]
- 00485554 bytes 574a1f94
+ 00485594 bytes 7b4a1f94
- 00485594 ["INT_ADD", "register:40f0:8", ["const:485594:8", "const:4:8"]]
- 00485594 ["CALL", null, ["callee:00c58260:8"]]
+ 004855d4 ["INT_ADD", "register:40f0:8", ["const:4855d4:8", "const:4:8"]]
+ 004855d4 ["CALL", null, ["callee:00c58260:8"]]
- 00485594 bytes ff4a1f94
+ 004855d4 bytes 234b1f94
- 00485400 ["INT_ADD", "register:40f0:8", ["const:485400:8", "const:4:8"]]
- 00485400 ["CALL", null, ["callee:0055e8b0:8"]]
+ 00485440 ["INT_ADD", "register:40f0:8", ["const:485440:8", "const:4:8"]]
+ 00485440 ["CALL", null, ["callee:0055e8b0:8"]]
- 00485400 bytes 1c650394
+ 00485440 bytes 1c650394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13fab999048bba35a6bc554de97cc33b"></a>

### [`00485b20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/00485b20.md) → [`00485b60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00485/00485b60.md) FUN_00485b60

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00481460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481460.md) [`00485b20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/00485b20.md) · 呼出先 23件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)
- 新版 呼出元 2件 [`004814a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00481/004814a0.md) [`00485b60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00485/00485b60.md) · 呼出先 23件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`00441d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441d2c.md)

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
      "definition_site": "00485cb8",
      "incomplete_value": false,
      "site": "00485cc0",
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
            "const:f93:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00485c78",
      "incomplete_value": false,
      "site": "00485c80",
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
            "const:f53:8"
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
      "definition_site": "00485d74",
      "incomplete_value": false,
      "site": "00485d7c",
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
            "const:e27:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00485d34",
      "incomplete_value": false,
      "site": "00485d3c",
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
            "const:de7:8"
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
      "definition_site": "00485d8c",
      "incomplete_value": false,
      "site": "00485d98",
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
            "const:f29:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00485d4c",
      "incomplete_value": false,
      "site": "00485d58",
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
            "const:ee9:8"
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
      "00485cb8",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "00485d74",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ],
    [
      "00485d8c",
      "PARAM",
      [
        "storage",
        "002c0ee9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00485cb8",
      "PARAM",
      [
        "storage",
        "002b7f93",
        null,
        null
      ]
    ],
    [
      "00485d74",
      "PARAM",
      [
        "storage",
        "002b5e27",
        null,
        null
      ]
    ],
    [
      "00485d8c",
      "PARAM",
      [
        "storage",
        "002c0f29",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00485c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/00485b20.md#insn-00485c80) · [`00485d3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/00485b20.md#insn-00485d3c) · [`00485d58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/00485b20.md#insn-00485d58)
- 新版 `00485cc0`（命令位置の公開資料なし） · `00485d7c`（命令位置の公開資料なし） · `00485d98`（命令位置の公開資料なし）

~~~diff
- 00485c80 ["INT_ADD", "register:40f0:8", ["const:485c80:8", "const:4:8"]]
- 00485c80 ["CALL", null, ["callee:00441ed4:8"]]
+ 00485cc0 ["INT_ADD", "register:40f0:8", ["const:485cc0:8", "const:4:8"]]
+ 00485cc0 ["CALL", null, ["callee:00441ed4:8"]]
- 00485c80 bytes 85f0fe97
+ 00485cc0 bytes 85f0fe97
- 00485d3c ["INT_ADD", "register:40f0:8", ["const:485d3c:8", "const:4:8"]]
- 00485d3c ["CALL", null, ["callee:00441ed4:8"]]
+ 00485d7c ["INT_ADD", "register:40f0:8", ["const:485d7c:8", "const:4:8"]]
+ 00485d7c ["CALL", null, ["callee:00441ed4:8"]]
- 00485d3c bytes 56f0fe97
+ 00485d7c bytes 56f0fe97
- 00485d58 ["INT_ADD", "register:40f0:8", ["const:485d58:8", "const:4:8"]]
- 00485d58 ["CALL", null, ["callee:00442834:8"]]
+ 00485d98 ["INT_ADD", "register:40f0:8", ["const:485d98:8", "const:4:8"]]
+ 00485d98 ["CALL", null, ["callee:00442834:8"]]
- 00485d58 bytes a7f2fe97
+ 00485d98 bytes a7f2fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f821a8700331ee1d0a773cd70c084a5"></a>

### [`00486458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486458.md) → [`00486498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00486/00486498.md) FUN_00486498

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00485b20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00485/00485b20.md) [`00486458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486458.md) · 呼出先 23件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)
- 新版 呼出元 2件 [`00485b60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00485/00485b60.md) [`00486498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00486/00486498.md) · 呼出先 23件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`00441d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441d2c.md)

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
      "definition_site": "004865e8",
      "incomplete_value": false,
      "site": "004865f0",
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
            "const:f93:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004865a8",
      "incomplete_value": false,
      "site": "004865b0",
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
            "const:f53:8"
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
      "definition_site": "004866a4",
      "incomplete_value": false,
      "site": "004866ac",
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
            "const:e27:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00486664",
      "incomplete_value": false,
      "site": "0048666c",
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
            "const:de7:8"
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
      "definition_site": "004866bc",
      "incomplete_value": false,
      "site": "004866c8",
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
            "const:f29:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048667c",
      "incomplete_value": false,
      "site": "00486688",
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
            "const:ee9:8"
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
      "004865e8",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "004866a4",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ],
    [
      "004866bc",
      "PARAM",
      [
        "storage",
        "002c0ee9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004865e8",
      "PARAM",
      [
        "storage",
        "002b7f93",
        null,
        null
      ]
    ],
    [
      "004866a4",
      "PARAM",
      [
        "storage",
        "002b5e27",
        null,
        null
      ]
    ],
    [
      "004866bc",
      "PARAM",
      [
        "storage",
        "002c0f29",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004865b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486458.md#insn-004865b0) · [`0048666c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486458.md#insn-0048666c) · [`00486688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486458.md#insn-00486688)
- 新版 `004865f0`（命令位置の公開資料なし） · `004866ac`（命令位置の公開資料なし） · `004866c8`（命令位置の公開資料なし）

~~~diff
- 004865b0 ["INT_ADD", "register:40f0:8", ["const:4865b0:8", "const:4:8"]]
- 004865b0 ["CALL", null, ["callee:00441ed4:8"]]
+ 004865f0 ["INT_ADD", "register:40f0:8", ["const:4865f0:8", "const:4:8"]]
+ 004865f0 ["CALL", null, ["callee:00441ed4:8"]]
- 004865b0 bytes 39eefe97
+ 004865f0 bytes 39eefe97
- 0048666c ["INT_ADD", "register:40f0:8", ["const:48666c:8", "const:4:8"]]
- 0048666c ["CALL", null, ["callee:00441ed4:8"]]
+ 004866ac ["INT_ADD", "register:40f0:8", ["const:4866ac:8", "const:4:8"]]
+ 004866ac ["CALL", null, ["callee:00441ed4:8"]]
- 0048666c bytes 0aeefe97
+ 004866ac bytes 0aeefe97
- 00486688 ["INT_ADD", "register:40f0:8", ["const:486688:8", "const:4:8"]]
- 00486688 ["CALL", null, ["callee:00442834:8"]]
+ 004866c8 ["INT_ADD", "register:40f0:8", ["const:4866c8:8", "const:4:8"]]
+ 004866c8 ["CALL", null, ["callee:00442834:8"]]
- 00486688 bytes 5bf0fe97
+ 004866c8 bytes 5bf0fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1bfe1ac9e11236910a0ed8060cf3e89b"></a>

### [`00486d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486d78.md) → [`00486db8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00486/00486db8.md) FUN_00486db8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00482b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00482/00482b0c.md) [`00508364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00508/00508364.md) [`0089d4c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089d/0089d4c8.md) [`00a67830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a67/00a67830.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)
- 新版 呼出元 4件 [`00482b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00482/00482b4c.md) [`005083a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/005083a4.md) [`0089d520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089d/0089d520.md) [`00a678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a67/00a678a0.md) · 呼出先 1件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md)

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
      "definition_site": "00486dc4",
      "incomplete_value": false,
      "site": "00486dc8",
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
            "const:f8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00486d84",
      "incomplete_value": false,
      "site": "00486d88",
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
            "const:f4c:8"
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
      "00486dc4",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00486dc4",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00486d88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486d78.md#insn-00486d88) · [`00486d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486d78.md#insn-00486d84)
- 新版 `00486dc8`（命令位置の公開資料なし） · `00486dc4`（命令位置の公開資料なし）

~~~diff
- 00486d88 ["INT_ADD", "register:40f0:8", ["const:486d88:8", "const:4:8"]]
- 00486d88 ["CALL", null, ["callee:00442970:8"]]
+ 00486dc8 ["INT_ADD", "register:40f0:8", ["const:486dc8:8", "const:4:8"]]
+ 00486dc8 ["CALL", null, ["callee:00442970:8"]]
- 00486d88 bytes eaeefe97
+ 00486dc8 bytes eaeefe97
- 00486d84 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00486d84 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00486d84 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00486d84 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00486dc4 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00486dc4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00486dc4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00486dc4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00486d84 bytes 00303d91
+ 00486dc4 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf4650b0365bdc9565b7f530ced27d39"></a>

### [`00486d8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486d8c.md) → [`00486dcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00486/00486dcc.md) FUN_00486dcc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)

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
      "definition_site": "00486dd0",
      "incomplete_value": false,
      "site": "00486dd4",
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
            "const:700:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00486d90",
      "incomplete_value": false,
      "site": "00486d94",
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
            "const:630:8"
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
      "00486dd4",
      "DATA",
      [
        "storage",
        "00c65630",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00486dd4",
      "DATA",
      [
        "storage",
        "00c65700",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00486d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486d8c.md#insn-00486d90)
- 新版 `00486dd0`（命令位置の公開資料なし）

~~~diff
- 00486d90 ["COPY", "tmp:0:8", ["const:630:8"]]
- 00486d90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00486d90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00486d90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00486dd0 ["COPY", "tmp:0:8", ["const:700:8"]]
+ 00486dd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00486dd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00486dd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00486d90 bytes 08c11891
+ 00486dd0 bytes 08011c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd0e1c6eb6a7896298644069a5290059"></a>

### [`00486d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486d9c.md) → [`00486ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00486/00486ddc.md) FUN_00486ddc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00486dec",
      "incomplete_value": false,
      "site": "00486df4",
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
            "const:700:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00486dac",
      "incomplete_value": false,
      "site": "00486db4",
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
            "const:630:8"
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
      "00486df4",
      "DATA",
      [
        "storage",
        "00c65630",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00486df4",
      "DATA",
      [
        "storage",
        "00c65700",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00486dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486d9c.md#insn-00486dac) · [`00486db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486d9c.md#insn-00486db8)
- 新版 `00486dec`（命令位置の公開資料なし） · `00486df8`（命令位置の公開資料なし）

~~~diff
- 00486dac ["COPY", "tmp:0:8", ["const:630:8"]]
- 00486dac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00486dac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00486dac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00486dec ["COPY", "tmp:0:8", ["const:700:8"]]
+ 00486dec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00486dec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00486dec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00486dac bytes 08c11891
+ 00486dec bytes 08011c91
- 00486db8 ["INT_ADD", "register:40f0:8", ["const:486db8:8", "const:4:8"]]
- 00486db8 ["CALL", null, ["callee:00c57f70:8"]]
+ 00486df8 ["INT_ADD", "register:40f0:8", ["const:486df8:8", "const:4:8"]]
+ 00486df8 ["CALL", null, ["callee:00c57f70:8"]]
- 00486db8 bytes 3a441f94
+ 00486df8 bytes 5e441f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9084523dfad28155a90a7fdab201e108"></a>

### [`00486dcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486dcc.md) → [`00486e0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00486/00486e0c.md) FUN_00486e0c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004838cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/004838cc.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`0048390c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00483/0048390c.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

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
      "definition_site": "00486e20",
      "incomplete_value": false,
      "site": "00486e24",
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
            "const:750:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00486de0",
      "incomplete_value": false,
      "site": "00486de4",
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
            "const:680:8"
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
      "00486e24",
      "DATA",
      [
        "storage",
        "00c65680",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00486e24",
      "DATA",
      [
        "storage",
        "00c65750",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00486de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486dcc.md#insn-00486de0) · [`00486df4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486dcc.md#insn-00486df4) · [`00486e14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486dcc.md#insn-00486e14)
- 新版 `00486e20`（命令位置の公開資料なし） · `00486e34`（命令位置の公開資料なし） · `00486e54`（命令位置の公開資料なし）

~~~diff
- 00486de0 ["COPY", "tmp:0:8", ["const:680:8"]]
- 00486de0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00486de0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00486de0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00486e20 ["COPY", "tmp:0:8", ["const:750:8"]]
+ 00486e20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00486e20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00486e20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00486de0 bytes 08011a91
+ 00486e20 bytes 08411d91
- 00486df4 ["INT_ADD", "register:40f0:8", ["const:486df4:8", "const:4:8"]]
- 00486df4 ["CALL", null, ["callee:00c53da0:8"]]
+ 00486e34 ["INT_ADD", "register:40f0:8", ["const:486e34:8", "const:4:8"]]
+ 00486e34 ["CALL", null, ["callee:00c53da0:8"]]
- 00486df4 bytes c3331f94
+ 00486e34 bytes db331f94
- 00486e14 ["COPY", "register:0:8", ["register:4040:8"]]
- 00486e14 ["INT_ADD", "register:40f0:8", ["const:486e14:8", "const:4:8"]]
- 00486e14 ["CALLIND", null, ["register:0:8"]]
+ 00486e54 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00486e54 ["INT_ADD", "register:40f0:8", ["const:486e54:8", "const:4:8"]]
+ 00486e54 ["CALLIND", null, ["register:0:8"]]
- 00486e14 bytes 00013fd6
+ 00486e54 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-652bc30de9afa1a8a0f1ec77340bdbcd"></a>

### [`00486e64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486e64.md) → [`00486ea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00486/00486ea4.md) FUN_00486ea4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)

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
      "definition_site": "00486ea8",
      "incomplete_value": false,
      "site": "00486eac",
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
            "const:790:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00486e68",
      "incomplete_value": false,
      "site": "00486e6c",
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
            "const:6c0:8"
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
      "00486eac",
      "DATA",
      [
        "storage",
        "00c656c0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00486eac",
      "DATA",
      [
        "storage",
        "00c65790",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00486e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486e64.md#insn-00486e68)
- 新版 `00486ea8`（命令位置の公開資料なし）

~~~diff
- 00486e68 ["COPY", "tmp:0:8", ["const:6c0:8"]]
- 00486e68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00486e68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00486e68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00486ea8 ["COPY", "tmp:0:8", ["const:790:8"]]
+ 00486ea8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00486ea8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00486ea8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00486e68 bytes 08011b91
+ 00486ea8 bytes 08411e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ead70ea3c957bb8e72217e28eab780c3"></a>

### [`00486e74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486e74.md) → [`00486eb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00486/00486eb4.md) FUN_00486eb4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00486ec4",
      "incomplete_value": false,
      "site": "00486ecc",
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
            "const:790:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00486e84",
      "incomplete_value": false,
      "site": "00486e8c",
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
      "00486ecc",
      "DATA",
      [
        "storage",
        "00c656c0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00486ecc",
      "DATA",
      [
        "storage",
        "00c65790",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00486e84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486e74.md#insn-00486e84) · [`00486e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486e74.md#insn-00486e90)
- 新版 `00486ec4`（命令位置の公開資料なし） · `00486ed0`（命令位置の公開資料なし）

~~~diff
- 00486e84 ["COPY", "tmp:0:8", ["const:6c0:8"]]
- 00486e84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00486e84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00486e84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00486ec4 ["COPY", "tmp:0:8", ["const:790:8"]]
+ 00486ec4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00486ec4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00486ec4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00486e84 bytes 08011b91
+ 00486ec4 bytes 08411e91
- 00486e90 ["INT_ADD", "register:40f0:8", ["const:486e90:8", "const:4:8"]]
- 00486e90 ["CALL", null, ["callee:00c57f70:8"]]
+ 00486ed0 ["INT_ADD", "register:40f0:8", ["const:486ed0:8", "const:4:8"]]
+ 00486ed0 ["CALL", null, ["callee:00c57f70:8"]]
- 00486e90 bytes 04441f94
+ 00486ed0 bytes 28441f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d7b7ed4299db4d8ea810d673a987cbd"></a>

### [`00486ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486ea4.md) → [`00486ee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00486/00486ee4.md) FUN_00486ee4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004838cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/004838cc.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`0048390c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00483/0048390c.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

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
      "definition_site": "00486efc",
      "incomplete_value": false,
      "site": "00486f00",
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
            "const:7e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00486ebc",
      "incomplete_value": false,
      "site": "00486ec0",
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
            "const:710:8"
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
      "definition_site": "00486f38",
      "incomplete_value": false,
      "site": "00486f3c",
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
            "const:828:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00486ef8",
      "incomplete_value": false,
      "site": "00486efc",
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
      "00486f00",
      "DATA",
      [
        "storage",
        "00c65710",
        null,
        null
      ]
    ],
    [
      "00486f3c",
      "DATA",
      [
        "storage",
        "00c65758",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00486f00",
      "DATA",
      [
        "storage",
        "00c657e0",
        null,
        null
      ]
    ],
    [
      "00486f3c",
      "DATA",
      [
        "storage",
        "00c65828",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00486ebc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486ea4.md#insn-00486ebc) · [`00486ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486ea4.md#insn-00486ed0) · [`00486ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486ea4.md#insn-00486ee4)
- 新版 `00486efc`（命令位置の公開資料なし） · `00486f10`（命令位置の公開資料なし） · `00486f24`（命令位置の公開資料なし）

~~~diff
- 00486ebc ["COPY", "tmp:0:8", ["const:710:8"]]
- 00486ebc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00486ebc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00486ebc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00486efc ["COPY", "tmp:0:8", ["const:7e0:8"]]
+ 00486efc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00486efc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00486efc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00486ebc bytes 08411c91
+ 00486efc bytes 08811f91
- 00486ed0 ["INT_ADD", "register:40f0:8", ["const:486ed0:8", "const:4:8"]]
- 00486ed0 ["CALL", null, ["callee:00c53da0:8"]]
+ 00486f10 ["INT_ADD", "register:40f0:8", ["const:486f10:8", "const:4:8"]]
+ 00486f10 ["CALL", null, ["callee:00c53da0:8"]]
- 00486ed0 bytes 8c331f94
+ 00486f10 bytes a4331f94
- 00486ee4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00486ee4 ["INT_ADD", "register:40f0:8", ["const:486ee4:8", "const:4:8"]]
- 00486ee4 ["CALLIND", null, ["register:0:8"]]
+ 00486f24 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00486f24 ["INT_ADD", "register:40f0:8", ["const:486f24:8", "const:4:8"]]
+ 00486f24 ["CALLIND", null, ["register:0:8"]]
- 00486ee4 bytes 00013fd6
+ 00486f24 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f532c9df4af16f1f5113f6b4ad382ac7"></a>

### [`00487128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487128.md) → [`00487168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487168.md) FUN_00487168

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004838cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00483/004838cc.md) · 呼出先 5件 [`00550ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550ba4.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`0048390c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00483/0048390c.md) · 呼出先 5件 [`00550be4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550be4.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

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
      "definition_site": "004871a8",
      "incomplete_value": false,
      "site": "004871ac",
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
            "const:840:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00487168",
      "incomplete_value": false,
      "site": "0048716c",
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
            "const:770:8"
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
      "definition_site": "004871bc",
      "incomplete_value": false,
      "site": "004871bc",
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
            "const:8d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048717c",
      "incomplete_value": false,
      "site": "0048717c",
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
            "const:800:8"
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
      "definition_site": "004871dc",
      "incomplete_value": false,
      "site": "004871e0",
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
            "const:890:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048719c",
      "incomplete_value": false,
      "site": "004871a0",
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
            "const:7c0:8"
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
      "004871ac",
      "DATA",
      [
        "storage",
        "00c65770",
        null,
        "undefined *"
      ]
    ],
    [
      "004871bc",
      "DATA",
      [
        "storage",
        "00c65800",
        null,
        "pointer"
      ]
    ],
    [
      "004871e0",
      "DATA",
      [
        "storage",
        "00c657c0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004871ac",
      "DATA",
      [
        "storage",
        "00c65840",
        null,
        "undefined *"
      ]
    ],
    [
      "004871bc",
      "DATA",
      [
        "storage",
        "00c658d0",
        null,
        "pointer"
      ]
    ],
    [
      "004871e0",
      "DATA",
      [
        "storage",
        "00c65890",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00487158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487128.md#insn-00487158) · [`00487168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487128.md#insn-00487168) · [`00487194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487128.md#insn-00487194)
- 新版 `00487198`（命令位置の公開資料なし） · `004871a8`（命令位置の公開資料なし） · `004871d4`（命令位置の公開資料なし）

~~~diff
- 00487158 ["COPY", "tmp:0:8", ["const:800:8"]]
- 00487158 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00487158 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00487158 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00487198 ["COPY", "tmp:0:8", ["const:8d0:8"]]
+ 00487198 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00487198 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00487198 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00487158 bytes 29012091
+ 00487198 bytes 29412391
- 00487168 ["COPY", "tmp:0:8", ["const:770:8"]]
- 00487168 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00487168 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00487168 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004871a8 ["COPY", "tmp:0:8", ["const:840:8"]]
+ 004871a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004871a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004871a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00487168 bytes 08c11d91
+ 004871a8 bytes 08012191
- 00487194 ["INT_ADD", "register:40f0:8", ["const:487194:8", "const:4:8"]]
- 00487194 ["CALL", null, ["callee:00c53d70:8"]]
+ 004871d4 ["INT_ADD", "register:40f0:8", ["const:4871d4:8", "const:4:8"]]
+ 004871d4 ["CALL", null, ["callee:00c53d70:8"]]
- 00487194 bytes cf321f94
+ 004871d4 bytes e7321f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13a77c85b37736a0bef33bd8599697e6"></a>

### [`00487264`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487264.md) → [`004872a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/004872a4.md) FUN_004872a4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md)

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
      "definition_site": "004872a8",
      "incomplete_value": false,
      "site": "004872ac",
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
            "const:840:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00487268",
      "incomplete_value": false,
      "site": "0048726c",
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
            "const:770:8"
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
      "004872ac",
      "DATA",
      [
        "storage",
        "00c65770",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004872ac",
      "DATA",
      [
        "storage",
        "00c65840",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00487268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487264.md#insn-00487268)
- 新版 `004872a8`（命令位置の公開資料なし）

~~~diff
- 00487268 ["COPY", "tmp:0:8", ["const:770:8"]]
- 00487268 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00487268 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00487268 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004872a8 ["COPY", "tmp:0:8", ["const:840:8"]]
+ 004872a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004872a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004872a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00487268 bytes 08c11d91
+ 004872a8 bytes 08012191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8248581ff1ad32bb0e2ee718ef87f01b"></a>

### [`00487274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487274.md) → [`004872b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/004872b4.md) FUN_004872b4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "004872c4",
      "incomplete_value": false,
      "site": "004872cc",
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
            "const:840:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00487284",
      "incomplete_value": false,
      "site": "0048728c",
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
            "const:770:8"
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
      "004872cc",
      "DATA",
      [
        "storage",
        "00c65770",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004872cc",
      "DATA",
      [
        "storage",
        "00c65840",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00487284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487274.md#insn-00487284) · [`00487290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487274.md#insn-00487290)
- 新版 `004872c4`（命令位置の公開資料なし） · `004872d0`（命令位置の公開資料なし）

~~~diff
- 00487284 ["COPY", "tmp:0:8", ["const:770:8"]]
- 00487284 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00487284 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00487284 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004872c4 ["COPY", "tmp:0:8", ["const:840:8"]]
+ 004872c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004872c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004872c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00487284 bytes 08c11d91
+ 004872c4 bytes 08012191
- 00487290 ["INT_ADD", "register:40f0:8", ["const:487290:8", "const:4:8"]]
- 00487290 ["CALL", null, ["callee:00c57f70:8"]]
+ 004872d0 ["INT_ADD", "register:40f0:8", ["const:4872d0:8", "const:4:8"]]
+ 004872d0 ["CALL", null, ["callee:00c57f70:8"]]
- 00487290 bytes 04431f94
+ 004872d0 bytes 28431f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc904ae7bda72ae147c9d0f249611bd5"></a>

### [`004872a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/004872a4.md) → [`004872e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/004872e4.md) FUN_004872e4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

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
      "definition_site": "004872fc",
      "incomplete_value": false,
      "site": "00487300",
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
            "const:890:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004872bc",
      "incomplete_value": false,
      "site": "004872c0",
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
            "const:7c0:8"
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
      "definition_site": "00487338",
      "incomplete_value": false,
      "site": "0048733c",
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
            "const:8d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004872f8",
      "incomplete_value": false,
      "site": "004872fc",
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
            "const:800:8"
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
      "00487300",
      "DATA",
      [
        "storage",
        "00c657c0",
        null,
        null
      ]
    ],
    [
      "0048733c",
      "DATA",
      [
        "storage",
        "00c65800",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00487300",
      "DATA",
      [
        "storage",
        "00c65890",
        null,
        null
      ]
    ],
    [
      "0048733c",
      "DATA",
      [
        "storage",
        "00c658d0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004872bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/004872a4.md#insn-004872bc) · [`004872d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/004872a4.md#insn-004872d0) · [`004872e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/004872a4.md#insn-004872e4)
- 新版 `004872fc`（命令位置の公開資料なし） · `00487310`（命令位置の公開資料なし） · `00487324`（命令位置の公開資料なし）

~~~diff
- 004872bc ["COPY", "tmp:0:8", ["const:7c0:8"]]
- 004872bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004872bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004872bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004872fc ["COPY", "tmp:0:8", ["const:890:8"]]
+ 004872fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004872fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004872fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004872bc bytes 08011f91
+ 004872fc bytes 08412291
- 004872d0 ["INT_ADD", "register:40f0:8", ["const:4872d0:8", "const:4:8"]]
- 004872d0 ["CALL", null, ["callee:00c53da0:8"]]
+ 00487310 ["INT_ADD", "register:40f0:8", ["const:487310:8", "const:4:8"]]
+ 00487310 ["CALL", null, ["callee:00c53da0:8"]]
- 004872d0 bytes 8c321f94
+ 00487310 bytes a4321f94
- 004872e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 004872e4 ["INT_ADD", "register:40f0:8", ["const:4872e4:8", "const:4:8"]]
- 004872e4 ["CALLIND", null, ["register:0:8"]]
+ 00487324 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00487324 ["INT_ADD", "register:40f0:8", ["const:487324:8", "const:4:8"]]
+ 00487324 ["CALLIND", null, ["register:0:8"]]
- 004872e4 bytes 00013fd6
+ 00487324 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04db318d657dbe87a1fae11d63590458"></a>

### [`00487344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487344.md) → [`00487384`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487384.md) FUN_00487384

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

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
      "definition_site": "00487398",
      "incomplete_value": false,
      "site": "0048739c",
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
            "const:8d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00487358",
      "incomplete_value": false,
      "site": "0048735c",
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
            "const:800:8"
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
      "0048739c",
      "DATA",
      [
        "storage",
        "00c65800",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0048739c",
      "DATA",
      [
        "storage",
        "00c658d0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00487358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487344.md#insn-00487358) · [`0048736c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487344.md#insn-0048736c) · [`0048738c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487344.md#insn-0048738c)
- 新版 `00487398`（命令位置の公開資料なし） · `004873ac`（命令位置の公開資料なし） · `004873cc`（命令位置の公開資料なし）

~~~diff
- 00487358 ["COPY", "tmp:0:8", ["const:800:8"]]
- 00487358 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00487358 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00487358 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00487398 ["COPY", "tmp:0:8", ["const:8d0:8"]]
+ 00487398 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00487398 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00487398 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00487358 bytes 08012091
+ 00487398 bytes 08412391
- 0048736c ["INT_ADD", "register:40f0:8", ["const:48736c:8", "const:4:8"]]
- 0048736c ["CALL", null, ["callee:00c53da0:8"]]
+ 004873ac ["INT_ADD", "register:40f0:8", ["const:4873ac:8", "const:4:8"]]
+ 004873ac ["CALL", null, ["callee:00c53da0:8"]]
- 0048736c bytes 65321f94
+ 004873ac bytes 7d321f94
- 0048738c ["COPY", "register:0:8", ["register:4040:8"]]
- 0048738c ["INT_ADD", "register:40f0:8", ["const:48738c:8", "const:4:8"]]
- 0048738c ["CALLIND", null, ["register:0:8"]]
+ 004873cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 004873cc ["INT_ADD", "register:40f0:8", ["const:4873cc:8", "const:4:8"]]
+ 004873cc ["CALLIND", null, ["register:0:8"]]
- 0048738c bytes 00013fd6
+ 004873cc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab4ca14f5e1162482ae06503dd4b406c"></a>

### [`0048758c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048758c.md) → [`004875cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/004875cc.md) _INIT_18

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

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
      "definition_site": "00487608",
      "incomplete_value": true,
      "site": "00487624",
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
                "const:f66:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004875c8",
      "incomplete_value": true,
      "site": "004875e4",
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
                "const:f26:8"
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
      "definition_site": "0048762c",
      "incomplete_value": true,
      "site": "00487648",
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
                "const:f79:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004875ec",
      "incomplete_value": true,
      "site": "00487608",
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
                "const:f39:8"
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
      "definition_site": "0048764c",
      "incomplete_value": true,
      "site": "00487668",
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
                "const:d6e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048760c",
      "incomplete_value": true,
      "site": "00487628",
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
                "const:dc2:8"
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
      "00487608",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "0048762c",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "0048764c",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00487608",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "0048762c",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "0048764c",
      "READ",
      [
        "storage",
        "002b8d6e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00487604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048758c.md#insn-00487604) · [`00487624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048758c.md#insn-00487624) · [`004876ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048758c.md#insn-004876ec)
- 新版 `00487644`（命令位置の公開資料なし） · `00487664`（命令位置の公開資料なし） · `0048772c`（命令位置の公開資料なし）

~~~diff
- 00487604 ["COPY", "tmp:0:8", ["const:dc2:8"]]
- 00487604 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00487604 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00487604 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00487644 ["COPY", "tmp:0:8", ["const:d6e:8"]]
+ 00487644 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00487644 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00487644 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00487604 bytes 4a093791
+ 00487644 bytes 4ab93591
- 00487624 ["COPY", "tmp:0:8", ["const:f62:8"]]
- 00487624 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00487624 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00487624 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00487664 ["COPY", "tmp:0:8", ["const:f15:8"]]
+ 00487664 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00487664 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00487664 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00487624 bytes 4a893d91
+ 00487664 bytes 4a553c91
- 004876ec ["INT_ADD", "register:40f0:8", ["const:4876ec:8", "const:4:8"]]
- 004876ec ["CALL", null, ["callee:0043b838:8"]]
+ 0048772c ["INT_ADD", "register:40f0:8", ["const:48772c:8", "const:4:8"]]
+ 0048772c ["CALL", null, ["callee:0043b838:8"]]
- 004876ec bytes 43d0fe97
+ 0048772c bytes 43d0fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e87a9c719281dd61226c2e9090be1b4b"></a>

### [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md) → [`00487e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md) FUN_00487e60

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 153件 [`0043d77c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043d77c.md) [`00444bd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/00444bd8.md) [`00444e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/00444e20.md) [`0046d120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d120.md) [`0046e970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e970.md) · 呼出先 2件 [`00c581e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581e0.md) [`00c581f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581f0.md)
- 新版 呼出元 153件 [`0043d7bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043d7bc.md) [`00444c18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444c18.md) [`00444e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444e60.md) [`0046d160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d160.md) [`0046e9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e9b0.md) · 呼出先 2件 [`00c582b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c582b0.md) [`00c582c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c582c0.md)

変更の種類 constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 70.00% / 新版 70.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00487eb0",
      "incomplete_value": true,
      "site": "00487eb0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00487e70",
      "incomplete_value": true,
      "site": "00487e70",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00487e90",
      "incomplete_value": false,
      "site": "00487eb8",
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
            "const:8e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00487e50",
      "incomplete_value": false,
      "site": "00487e78",
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
            "const:818:8"
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
      "definition_site": "00487ebc",
      "incomplete_value": true,
      "site": "00487ebc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00487e7c",
      "incomplete_value": true,
      "site": "00487e7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "unmatched:00487e44",
      "READ",
      [
        "storage",
        "00c9abb8",
        null,
        "pointer"
      ]
    ],
    [
      "00487e9c",
      "READ",
      [
        "storage",
        "00c93208",
        null,
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "00487eac",
      "READ",
      [
        "storage",
        "00c93210",
        null,
        "pointer __((offset(0x40)))"
      ]
    ]
  ],
  "added": [
    [
      "00487e88",
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      "00487e9c",
      "READ",
      [
        "storage",
        "00c932d8",
        null,
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "00487eac",
      "READ",
      [
        "storage",
        "00c932e0",
        null,
        "pointer __((offset(0x40)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00487e44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md#insn-00487e44) · [`00487e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md#insn-00487e48)
- 新版 `00487e94`（命令位置の公開資料なし） · `00487e84`（命令位置の公開資料なし）

~~~diff
+ 00487e94 ["COPY", "register:40b8:8", ["register:4000:8"]]
+ 00487e94 bytes f70300aa
- 00487e44 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:bb8:8"]]
- 00487e44 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 00487e44 bytes 18df45f9
- 00487e48 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:c88:8"]]
- 00487e48 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00487e84 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:c88:8"]]
+ 00487e84 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 00487e48 bytes 394746f9
+ 00487e84 bytes 184746f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-422f85f18d1f6407f9ecd0175df43365"></a>

### [`00488690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488690.md) → [`004886d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/004886d0.md) FUN_004886d0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00b110ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b11/00b110ec.md) · 呼出先 1件 [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md)
- 新版 呼出元 1件 [`00b11188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b11/00b11188.md) · 呼出先 1件 [`00487e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md)

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
      "definition_site": "004886e8",
      "incomplete_value": false,
      "site": "004886f0",
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
            "const:948:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004886a8",
      "incomplete_value": false,
      "site": "004886b0",
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
            "const:878:8"
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
      "004886f0",
      "DATA",
      [
        "storage",
        "00c65878",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004886f0",
      "DATA",
      [
        "storage",
        "00c65948",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004886a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488690.md#insn-004886a0) · [`004886a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488690.md#insn-004886a8)
- 新版 `004886e0`（命令位置の公開資料なし） · `004886e8`（命令位置の公開資料なし）

~~~diff
- 004886a0 ["INT_ADD", "register:40f0:8", ["const:4886a0:8", "const:4:8"]]
- 004886a0 ["CALL", null, ["callee:00487e60:8"]]
+ 004886e0 ["INT_ADD", "register:40f0:8", ["const:4886e0:8", "const:4:8"]]
+ 004886e0 ["CALL", null, ["callee:00487e60:8"]]
- 004886a0 bytes e0fdff97
+ 004886e0 bytes e0fdff97
- 004886a8 ["COPY", "tmp:0:8", ["const:878:8"]]
- 004886a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004886a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004886a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004886e8 ["COPY", "tmp:0:8", ["const:948:8"]]
+ 004886e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004886e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004886e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004886a8 bytes 08e12191
+ 004886e8 bytes 08212591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab6a3f9851da73d69d84a1b66892aee2"></a>

### [`00488790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488790.md) → [`004887d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/004887d0.md) FUN_004887d0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00444bd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/00444bd8.md) [`00444e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/00444e20.md) [`005e3114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e3/005e3114.md) · 呼出先 14件 [`0043dba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dba4.md) [`00470e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470e54.md) [`00471724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471724.md) [`00471930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471930.md) [`00488054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488054.md)
- 新版 呼出元 3件 [`00444c18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444c18.md) [`00444e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444e60.md) [`005e3154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e3/005e3154.md) · 呼出先 14件 [`0043dbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043dbe4.md) [`00470e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470e94.md) [`00471764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00471/00471764.md) [`00471970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00471/00471970.md) [`00488094`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488094.md)

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
      "definition_site": "00488970",
      "incomplete_value": true,
      "site": "00488970",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:580:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00488930",
      "incomplete_value": true,
      "site": "00488930",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5dc:8"
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
      "site": "00488800",
      "value": [
        "leaf",
        "ram:470e94:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004887c0",
      "value": [
        "leaf",
        "ram:470e54:8"
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
      "site": "004888e4",
      "value": [
        "leaf",
        "ram:470e94:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004888a4",
      "value": [
        "leaf",
        "ram:470e54:8"
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
      "00488800",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00470e54"
      ]
    ],
    [
      "004888e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00470e54"
      ]
    ],
    [
      "00488950",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ]
  ],
  "added": [
    [
      "00488800",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00470e94"
      ]
    ],
    [
      "004888e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00470e94"
      ]
    ],
    [
      "00488950",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004887c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488790.md#insn-004887c0) · [`00488864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488790.md#insn-00488864) · [`004888a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488790.md#insn-004888a4)
- 新版 `00488800`（命令位置の公開資料なし） · `004888a4`（命令位置の公開資料なし） · `004888e4`（命令位置の公開資料なし）

~~~diff
- 004887c0 ["INT_ADD", "register:40f0:8", ["const:4887c0:8", "const:4:8"]]
- 004887c0 ["CALL", null, ["ram:470e54:8"]]
+ 00488800 ["INT_ADD", "register:40f0:8", ["const:488800:8", "const:4:8"]]
+ 00488800 ["CALL", null, ["ram:470e94:8"]]
- 004887c0 bytes a5a1ff97
+ 00488800 bytes a5a1ff97
- 00488864 ["COPY", "register:0:8", ["register:4040:8"]]
- 00488864 ["INT_ADD", "register:40f0:8", ["const:488864:8", "const:4:8"]]
- 00488864 ["CALLIND", null, ["register:0:8"]]
+ 004888a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004888a4 ["INT_ADD", "register:40f0:8", ["const:4888a4:8", "const:4:8"]]
+ 004888a4 ["CALLIND", null, ["register:0:8"]]
- 00488864 bytes 00013fd6
+ 004888a4 bytes 00013fd6
- 004888a4 ["INT_ADD", "register:40f0:8", ["const:4888a4:8", "const:4:8"]]
- 004888a4 ["CALL", null, ["ram:470e54:8"]]
+ 004888e4 ["INT_ADD", "register:40f0:8", ["const:4888e4:8", "const:4:8"]]
+ 004888e4 ["CALL", null, ["ram:470e94:8"]]
- 004888a4 bytes 6ca1ff97
+ 004888e4 bytes 6ca1ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d294761474d82cfcaaa3513790288431"></a>

### [`00488c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488c14.md) → [`00488c54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488c54.md) FUN_00488c54

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fa0.md) [`00c57fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fc0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58070.md) [`00c58080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58080.md) [`00c58090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58090.md)

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
      "definition_site": "00488c6c",
      "incomplete_value": false,
      "site": "00488c78",
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
            "const:8e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00488c2c",
      "incomplete_value": false,
      "site": "00488c38",
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
            "const:818:8"
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
      "definition_site": "00488c8c",
      "incomplete_value": true,
      "site": "00488c8c",
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
      "definition_site": "00488c4c",
      "incomplete_value": true,
      "site": "00488c4c",
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
      "definition_site": "00488c9c",
      "incomplete_value": true,
      "site": "00488c9c",
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
      "definition_site": "00488c5c",
      "incomplete_value": true,
      "site": "00488c5c",
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
      "00488c70",
      "READ",
      [
        "storage",
        "00c9abb8",
        null,
        "pointer"
      ]
    ],
    [
      "00488c78",
      "DATA",
      [
        "storage",
        "00c65818",
        null,
        "undefined *"
      ]
    ],
    [
      "00488c84",
      "READ",
      [
        "storage",
        "00c93200",
        "_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "00488c70",
      "READ",
      [
        "storage",
        "00c9ac88",
        null,
        "pointer"
      ]
    ],
    [
      "00488c78",
      "DATA",
      [
        "storage",
        "00c658e8",
        null,
        "undefined *"
      ]
    ],
    [
      "00488c84",
      "READ",
      [
        "storage",
        "00c932d0",
        "_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00488c2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488c14.md#insn-00488c2c) · [`00488c30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488c14.md#insn-00488c30) · [`00488c34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488c14.md#insn-00488c34)
- 新版 `00488c6c`（命令位置の公開資料なし） · `00488c70`（命令位置の公開資料なし）

~~~diff
- 00488c2c ["COPY", "tmp:0:8", ["const:818:8"]]
- 00488c2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00488c2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00488c2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00488c6c ["COPY", "tmp:0:8", ["const:8e8:8"]]
+ 00488c6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00488c6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00488c6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00488c2c bytes 08612091
+ 00488c6c bytes 08a12391
- 00488c30 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:bb8:8"]]
- 00488c30 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00488c70 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:c88:8"]]
+ 00488c70 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
- 00488c30 bytes d6de45f9
+ 00488c70 bytes d64646f9
- 00488c34 ["COPY", "register:40a0:8", ["register:4000:8"]]
- 00488c34 bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1526cf20924609cb45a35ec83d581aa"></a>

### [`00488cc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488cc8.md) → [`00488d08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488d08.md) FUN_00488d08

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00488da0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488da0.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fa0.md) [`00c57fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fc0.md)
- 新版 呼出元 1件 [`00488de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488de0.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58070.md) [`00c58080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58080.md) [`00c58090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58090.md)

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
      "definition_site": "00488d24",
      "incomplete_value": false,
      "site": "00488d28",
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
            "const:948:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00488ce4",
      "incomplete_value": false,
      "site": "00488ce8",
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
            "const:878:8"
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
      "definition_site": "00488d40",
      "incomplete_value": false,
      "site": "00488d4c",
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
            "const:8e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00488d00",
      "incomplete_value": false,
      "site": "00488d0c",
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
            "const:818:8"
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
      "definition_site": "00488d5c",
      "incomplete_value": true,
      "site": "00488d5c",
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
      "definition_site": "00488d1c",
      "incomplete_value": true,
      "site": "00488d1c",
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
      "00488d28",
      "DATA",
      [
        "storage",
        "00c65878",
        null,
        "undefined *"
      ]
    ],
    [
      "00488d44",
      "READ",
      [
        "storage",
        "00c9abb8",
        null,
        "pointer"
      ]
    ],
    [
      "00488d4c",
      "DATA",
      [
        "storage",
        "00c65818",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00488d28",
      "DATA",
      [
        "storage",
        "00c65948",
        null,
        "undefined *"
      ]
    ],
    [
      "00488d44",
      "READ",
      [
        "storage",
        "00c9ac88",
        null,
        "pointer"
      ]
    ],
    [
      "00488d4c",
      "DATA",
      [
        "storage",
        "00c658e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00488cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488cc8.md#insn-00488cf4) · [`00488d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488cc8.md#insn-00488d28) · [`00488d4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488cc8.md#insn-00488d4c)
- 新版 `00488d34`（命令位置の公開資料なし） · `00488d68`（命令位置の公開資料なし） · `00488d8c`（命令位置の公開資料なし）

~~~diff
- 00488cf4 ["INT_ADD", "register:40f0:8", ["const:488cf4:8", "const:4:8"]]
- 00488cf4 ["CALL", null, ["callee:00c57f80:8"]]
+ 00488d34 ["INT_ADD", "register:40f0:8", ["const:488d34:8", "const:4:8"]]
+ 00488d34 ["CALL", null, ["callee:00c57f80:8"]]
- 00488cf4 bytes 6f3c1f94
+ 00488d34 bytes 933c1f94
- 00488d28 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:bc0:8"]]
- 00488d28 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00488d68 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c90:8"]]
+ 00488d68 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00488d28 bytes 29e145f9
+ 00488d68 bytes 294946f9
- 00488d4c ["INT_ADD", "register:40f0:8", ["const:488d4c:8", "const:4:8"]]
- 00488d4c ["CALL", null, ["callee:00c58070:8"]]
+ 00488d8c ["INT_ADD", "register:40f0:8", ["const:488d8c:8", "const:4:8"]]
+ 00488d8c ["CALL", null, ["callee:00c58070:8"]]
- 00488d4c bytes 953c1f94
+ 00488d8c bytes b93c1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a683cd825cc56977134e97f744715e1a"></a>

### [`00488dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488dc4.md) → [`00488e04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488e04.md) FUN_00488e04

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004882ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/004882ec.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 1件 [`0048832c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/0048832c.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "00488e10",
      "incomplete_value": false,
      "site": "00488e14",
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
            "const:f8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00488dd0",
      "incomplete_value": false,
      "site": "00488dd4",
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
            "const:f4c:8"
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
      "00488e10",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00488e10",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00488dd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488dc4.md#insn-00488dd4) · [`00488dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488dc4.md#insn-00488dd0)
- 新版 `00488e14`（命令位置の公開資料なし） · `00488e10`（命令位置の公開資料なし）

~~~diff
- 00488dd4 ["INT_ADD", "register:40f0:8", ["const:488dd4:8", "const:4:8"]]
- 00488dd4 ["CALL", null, ["callee:0043b7b8:8"]]
+ 00488e14 ["INT_ADD", "register:40f0:8", ["const:488e14:8", "const:4:8"]]
+ 00488e14 ["CALL", null, ["callee:0043b7b8:8"]]
- 00488dd4 bytes 69cafe97
+ 00488e14 bytes 69cafe97
- 00488dd0 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00488dd0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00488dd0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00488dd0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00488e10 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00488e10 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00488e10 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00488e10 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00488dd0 bytes 00303d91
+ 00488e10 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b0631e9c8d335f212bb9df83beeb348"></a>

### [`00488dd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488dd8.md) → [`00488e18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488e18.md) _INIT_19

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

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
      "definition_site": "00488e54",
      "incomplete_value": true,
      "site": "00488e70",
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
                "const:f66:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00488e14",
      "incomplete_value": true,
      "site": "00488e30",
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
                "const:f26:8"
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
      "definition_site": "00488e78",
      "incomplete_value": true,
      "site": "00488e94",
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
                "const:f79:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00488e38",
      "incomplete_value": true,
      "site": "00488e54",
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
                "const:f39:8"
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
      "definition_site": "00488e98",
      "incomplete_value": true,
      "site": "00488eb4",
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
                "const:d6e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00488e58",
      "incomplete_value": true,
      "site": "00488e74",
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
                "const:dc2:8"
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
      "00488e54",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00488e78",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00488e98",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00488e54",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "00488e78",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "00488e98",
      "READ",
      [
        "storage",
        "002b8d6e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00488e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488dd8.md#insn-00488e50) · [`00488e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488dd8.md#insn-00488e70) · [`00488f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488dd8.md#insn-00488f38)
- 新版 `00488e90`（命令位置の公開資料なし） · `00488eb0`（命令位置の公開資料なし） · `00488f78`（命令位置の公開資料なし）

~~~diff
- 00488e50 ["COPY", "tmp:0:8", ["const:dc2:8"]]
- 00488e50 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00488e50 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00488e50 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00488e90 ["COPY", "tmp:0:8", ["const:d6e:8"]]
+ 00488e90 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00488e90 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00488e90 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00488e50 bytes 4a093791
+ 00488e90 bytes 4ab93591
- 00488e70 ["COPY", "tmp:0:8", ["const:f62:8"]]
- 00488e70 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00488e70 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00488e70 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00488eb0 ["COPY", "tmp:0:8", ["const:f15:8"]]
+ 00488eb0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00488eb0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00488eb0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00488e70 bytes 4a893d91
+ 00488eb0 bytes 4a553c91
- 00488f38 ["INT_ADD", "register:40f0:8", ["const:488f38:8", "const:4:8"]]
- 00488f38 ["CALL", null, ["callee:0043b838:8"]]
+ 00488f78 ["INT_ADD", "register:40f0:8", ["const:488f78:8", "const:4:8"]]
+ 00488f78 ["CALL", null, ["callee:0043b838:8"]]
- 00488f38 bytes 30cafe97
+ 00488f78 bytes 30cafe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d21c12210bc077e269d39f3eaff28faa"></a>

### [`00489168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489168.md) → [`004891a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/004891a8.md) FUN_004891a8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md) [`00633374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00633/00633374.md) [`006337e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00633/006337e4.md) [`007bda44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bd/007bda44.md) · 呼出先 0件 
- 新版 呼出元 6件 [`0047e64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e64c.md) [`0047e91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e91c.md) [`006333b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00633/006333b4.md) [`00633824`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00633/00633824.md) [`007bda9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bd/007bda9c.md) · 呼出先 0件 

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
      "definition_site": "004891b4",
      "incomplete_value": true,
      "site": "004891bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:240:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00489174",
      "incomplete_value": true,
      "site": "0048917c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:200:8"
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
      "004891b4",
      "READ",
      [
        "storage",
        "002c4200",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004891b4",
      "READ",
      [
        "storage",
        "002c4240",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00489174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489168.md#insn-00489174)
- 新版 `004891b4`（命令位置の公開資料なし）

~~~diff
- 00489174 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:200:8"]]
- 00489174 ["LOAD", "register:5020:8", ["const:1b1:8", "tmp:0:8"]]
- 00489174 ["COPY", "register:5028:8", ["const:0:8"]]
- 00489174 ["COPY", "register:5030:8", ["const:0:8"]]
+ 004891b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:240:8"]]
+ 004891b4 ["LOAD", "register:5020:8", ["const:1b1:8", "tmp:0:8"]]
+ 004891b4 ["COPY", "register:5028:8", ["const:0:8"]]
+ 004891b4 ["COPY", "register:5030:8", ["const:0:8"]]
- 00489174 bytes 010141fd
+ 004891b4 bytes 012141fd
~~~


