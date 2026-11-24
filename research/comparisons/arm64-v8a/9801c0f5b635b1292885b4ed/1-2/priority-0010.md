# v16.0.0 → v16.0.1 · 最優先の変更候補 (10)

[一覧の目次](README.md)

<a id="compare-0f18a90a20533596c5d3cc19eba46c4e"></a>

### [`004ea930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004ea930.md) → [`004ea970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ea/004ea970.md) _ZNK5Botan10Public_Key22create_verification_opERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
      "definition_site": "004ea9f8",
      "incomplete_value": true,
      "site": "004ea9f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004eaa30",
      "incomplete_value": true,
      "site": "004eaa34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ea9bc",
      "incomplete_value": false,
      "site": "004ea9c4",
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
            "const:645:8"
          ]
        ]
      ]
    },
    "old": {
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
      "004ea9bc",
      "PARAM",
      [
        "storage",
        "002a6569",
        null,
        "string"
      ]
    ],
    [
      "004ea9e4",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "004ea9f8",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004ea9bc",
      "PARAM",
      [
        "storage",
        "002a6645",
        null,
        "string"
      ]
    ],
    [
      "004ea9e4",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "004ea9f8",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ea984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004ea930.md#insn-004ea984) · [`004eaa1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004ea930.md#insn-004eaa1c) · [`004ea95c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004ea930.md#insn-004ea95c)
- 新版 [`004ea9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ea/004ea970.md#insn-004ea9c4) · [`004eaa5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ea/004ea970.md#insn-004eaa5c) · [`004ea99c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ea/004ea970.md#insn-004ea99c)

~~~diff
- 004ea984 ["INT_ADD", "register:40f0:8", ["const:4ea984:8", "const:4:8"]]
- 004ea984 ["CALL", null, ["callee:00c57f70:8"]]
+ 004ea9c4 ["INT_ADD", "register:40f0:8", ["const:4ea9c4:8", "const:4:8"]]
+ 004ea9c4 ["CALL", null, ["callee:00c57f70:8"]]
- 004ea984 bytes 7bb41d94
+ 004ea9c4 bytes 6bb51d94
- 004eaa1c ["INT_ADD", "register:40f0:8", ["const:4eaa1c:8", "const:4:8"]]
- 004eaa1c ["CALL", null, ["callee:00c57f10:8"]]
+ 004eaa5c ["INT_ADD", "register:40f0:8", ["const:4eaa5c:8", "const:4:8"]]
+ 004eaa5c ["CALL", null, ["callee:00c57f10:8"]]
- 004eaa1c bytes 3db41d94
+ 004eaa5c bytes 2db51d94
- 004ea95c ["INT_ADD", "register:40f0:8", ["const:4ea95c:8", "const:4:8"]]
- 004ea95c ["CALL", null, ["callee:00c57ef0:8"]]
+ 004ea99c ["INT_ADD", "register:40f0:8", ["const:4ea99c:8", "const:4:8"]]
+ 004ea99c ["CALL", null, ["callee:00c57ef0:8"]]
- 004ea95c bytes 65b41d94
+ 004ea99c bytes 55b51d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc1e0c01106254327f4cbf839137e998"></a>

### [`004eaab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004eaab4.md) → [`004eaaf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ea/004eaaf4.md) _ZNK5Botan11Private_Key20create_decryption_opERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
      "definition_site": "004eab84",
      "incomplete_value": true,
      "site": "004eab84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004eabbc",
      "incomplete_value": true,
      "site": "004eabc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004eab48",
      "incomplete_value": false,
      "site": "004eab50",
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
            "const:b1d:8"
          ]
        ]
      ]
    },
    "old": {
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
      "004eab48",
      "PARAM",
      [
        "storage",
        "002b3add",
        null,
        "string"
      ]
    ],
    [
      "004eab70",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "004eab84",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004eab48",
      "PARAM",
      [
        "storage",
        "002b3b1d",
        null,
        "string"
      ]
    ],
    [
      "004eab70",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "004eab84",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004eab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004eaab4.md#insn-004eab10) · [`004eaba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004eaab4.md#insn-004eaba8) · [`004eaae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004eaab4.md#insn-004eaae0)
- 新版 [`004eab50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ea/004eaaf4.md#insn-004eab50) · [`004eabe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ea/004eaaf4.md#insn-004eabe8) · [`004eab20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ea/004eaaf4.md#insn-004eab20)

~~~diff
- 004eab10 ["INT_ADD", "register:40f0:8", ["const:4eab10:8", "const:4:8"]]
- 004eab10 ["CALL", null, ["callee:00c57f70:8"]]
+ 004eab50 ["INT_ADD", "register:40f0:8", ["const:4eab50:8", "const:4:8"]]
+ 004eab50 ["CALL", null, ["callee:00c57f70:8"]]
- 004eab10 bytes 18b41d94
+ 004eab50 bytes 08b51d94
- 004eaba8 ["INT_ADD", "register:40f0:8", ["const:4eaba8:8", "const:4:8"]]
- 004eaba8 ["CALL", null, ["callee:00c57f10:8"]]
+ 004eabe8 ["INT_ADD", "register:40f0:8", ["const:4eabe8:8", "const:4:8"]]
+ 004eabe8 ["CALL", null, ["callee:00c57f10:8"]]
- 004eaba8 bytes dab31d94
+ 004eabe8 bytes cab41d94
- 004eaae0 ["INT_ADD", "register:40f0:8", ["const:4eaae0:8", "const:4:8"]]
- 004eaae0 ["CALL", null, ["callee:00c57ef0:8"]]
+ 004eab20 ["INT_ADD", "register:40f0:8", ["const:4eab20:8", "const:4:8"]]
+ 004eab20 ["CALL", null, ["callee:00c57ef0:8"]]
- 004eaae0 bytes 04b41d94
+ 004eab20 bytes f4b41d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e612dd87a859e39caff9ca1d42d88b4"></a>

### [`004eac40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004eac40.md) → [`004eac80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ea/004eac80.md) _ZNK5Botan11Private_Key24create_kem_decryption_opERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocato

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
      "definition_site": "004ead10",
      "incomplete_value": true,
      "site": "004ead10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ead48",
      "incomplete_value": true,
      "site": "004ead4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004eacd4",
      "incomplete_value": false,
      "site": "004eacdc",
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
            "const:293:8"
          ]
        ]
      ]
    },
    "old": {
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
      "004eacd4",
      "PARAM",
      [
        "storage",
        "002ba253",
        null,
        "string"
      ]
    ],
    [
      "004eacfc",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "004ead10",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004eacd4",
      "PARAM",
      [
        "storage",
        "002ba293",
        null,
        "string"
      ]
    ],
    [
      "004eacfc",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "004ead10",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004eac9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004eac40.md#insn-004eac9c) · [`004ead34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004eac40.md#insn-004ead34) · [`004eac6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004eac40.md#insn-004eac6c)
- 新版 [`004eacdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ea/004eac80.md#insn-004eacdc) · [`004ead74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ea/004eac80.md#insn-004ead74) · [`004eacac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ea/004eac80.md#insn-004eacac)

~~~diff
- 004eac9c ["INT_ADD", "register:40f0:8", ["const:4eac9c:8", "const:4:8"]]
- 004eac9c ["CALL", null, ["callee:00c57f70:8"]]
+ 004eacdc ["INT_ADD", "register:40f0:8", ["const:4eacdc:8", "const:4:8"]]
+ 004eacdc ["CALL", null, ["callee:00c57f70:8"]]
- 004eac9c bytes b5b31d94
+ 004eacdc bytes a5b41d94
- 004ead34 ["INT_ADD", "register:40f0:8", ["const:4ead34:8", "const:4:8"]]
- 004ead34 ["CALL", null, ["callee:00c57f10:8"]]
+ 004ead74 ["INT_ADD", "register:40f0:8", ["const:4ead74:8", "const:4:8"]]
+ 004ead74 ["CALL", null, ["callee:00c57f10:8"]]
- 004ead34 bytes 77b31d94
+ 004ead74 bytes 67b41d94
- 004eac6c ["INT_ADD", "register:40f0:8", ["const:4eac6c:8", "const:4:8"]]
- 004eac6c ["CALL", null, ["callee:00c57ef0:8"]]
+ 004eacac ["INT_ADD", "register:40f0:8", ["const:4eacac:8", "const:4:8"]]
+ 004eacac ["CALL", null, ["callee:00c57ef0:8"]]
- 004eac6c bytes a1b31d94
+ 004eacac bytes 91b41d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed37c0d77398070e4ec22bc641ff9bdd"></a>

### [`004eadcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004eadcc.md) → [`004eae0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ea/004eae0c.md) _ZNK5Botan11Private_Key19create_signature_opERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
      "definition_site": "004eae9c",
      "incomplete_value": true,
      "site": "004eae9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004eaed4",
      "incomplete_value": true,
      "site": "004eaed8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004eae60",
      "incomplete_value": false,
      "site": "004eae68",
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
            "const:208:8"
          ]
        ]
      ]
    },
    "old": {
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
      "004eae60",
      "PARAM",
      [
        "storage",
        "002b81c8",
        null,
        "string"
      ]
    ],
    [
      "004eae88",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "004eae9c",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004eae60",
      "PARAM",
      [
        "storage",
        "002b8208",
        null,
        "string"
      ]
    ],
    [
      "004eae88",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "004eae9c",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004eae28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004eadcc.md#insn-004eae28) · [`004eaec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004eadcc.md#insn-004eaec0) · [`004eadf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004eadcc.md#insn-004eadf8)
- 新版 [`004eae68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ea/004eae0c.md#insn-004eae68) · [`004eaf00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ea/004eae0c.md#insn-004eaf00) · [`004eae38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ea/004eae0c.md#insn-004eae38)

~~~diff
- 004eae28 ["INT_ADD", "register:40f0:8", ["const:4eae28:8", "const:4:8"]]
- 004eae28 ["CALL", null, ["callee:00c57f70:8"]]
+ 004eae68 ["INT_ADD", "register:40f0:8", ["const:4eae68:8", "const:4:8"]]
+ 004eae68 ["CALL", null, ["callee:00c57f70:8"]]
- 004eae28 bytes 52b31d94
+ 004eae68 bytes 42b41d94
- 004eaec0 ["INT_ADD", "register:40f0:8", ["const:4eaec0:8", "const:4:8"]]
- 004eaec0 ["CALL", null, ["callee:00c57f10:8"]]
+ 004eaf00 ["INT_ADD", "register:40f0:8", ["const:4eaf00:8", "const:4:8"]]
+ 004eaf00 ["CALL", null, ["callee:00c57f10:8"]]
- 004eaec0 bytes 14b31d94
+ 004eaf00 bytes 04b41d94
- 004eadf8 ["INT_ADD", "register:40f0:8", ["const:4eadf8:8", "const:4:8"]]
- 004eadf8 ["CALL", null, ["callee:00c57ef0:8"]]
+ 004eae38 ["INT_ADD", "register:40f0:8", ["const:4eae38:8", "const:4:8"]]
+ 004eae38 ["CALL", null, ["callee:00c57ef0:8"]]
- 004eadf8 bytes 3eb31d94
+ 004eae38 bytes 2eb41d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6278102754b309a543de40e74f7e86d7"></a>

### [`004eaf58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004eaf58.md) → [`004eaf98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ea/004eaf98.md) _ZNK5Botan11Private_Key23create_key_agreement_opERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocator

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
      "definition_site": "004eb028",
      "incomplete_value": true,
      "site": "004eb028",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004eb060",
      "incomplete_value": true,
      "site": "004eb064",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004eafec",
      "incomplete_value": false,
      "site": "004eaff4",
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
            "const:79:8"
          ]
        ]
      ]
    },
    "old": {
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
      "004eafec",
      "PARAM",
      [
        "storage",
        "0029ffac",
        null,
        "string"
      ]
    ],
    [
      "004eb014",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "004eb028",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004eafec",
      "PARAM",
      [
        "storage",
        "002a0079",
        null,
        "string"
      ]
    ],
    [
      "004eb014",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "004eb028",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004eafa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004eaf58.md#insn-004eafa8) · [`004eafb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004eaf58.md#insn-004eafb4) · [`004eb04c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004eaf58.md#insn-004eb04c)
- 新版 [`004eafe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ea/004eaf98.md#insn-004eafe8) · [`004eaff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ea/004eaf98.md#insn-004eaff4) · [`004eb08c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ea/004eaf98.md#insn-004eb08c)

~~~diff
- 004eafa8 ["COPY", "register:4008:8", ["const:29f000:8"]]
+ 004eafe8 ["COPY", "register:4008:8", ["const:2a0000:8"]]
- 004eafa8 bytes a1edffb0
+ 004eafe8 bytes a1edffd0
- 004eafb4 ["INT_ADD", "register:40f0:8", ["const:4eafb4:8", "const:4:8"]]
- 004eafb4 ["CALL", null, ["callee:00c57f70:8"]]
+ 004eaff4 ["INT_ADD", "register:40f0:8", ["const:4eaff4:8", "const:4:8"]]
+ 004eaff4 ["CALL", null, ["callee:00c57f70:8"]]
- 004eafb4 bytes efb21d94
+ 004eaff4 bytes dfb31d94
- 004eb04c ["INT_ADD", "register:40f0:8", ["const:4eb04c:8", "const:4:8"]]
- 004eb04c ["CALL", null, ["callee:00c57f10:8"]]
+ 004eb08c ["INT_ADD", "register:40f0:8", ["const:4eb08c:8", "const:4:8"]]
+ 004eb08c ["CALL", null, ["callee:00c57f10:8"]]
- 004eb04c bytes b1b21d94
+ 004eb08c bytes a1b31d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68ebd6c7c8a0c2c677d8d6b31d18d63a"></a>

### [`004eb0e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004eb0e4.md) → [`004eb124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004eb/004eb124.md) FUN_004eb124

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004f5890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f5890.md) · 呼出先 6件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c58ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58ba0.md) [`00c590f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c590f0.md)
- 新版 呼出元 1件 [`004f58d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f5/004f58d0.md) · 呼出先 6件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c58fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58fa0.md) [`00c594f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c594f0.md)

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
      "definition_site": "004eb138",
      "incomplete_value": false,
      "site": "004eb140",
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
            "const:e68:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004eb19c",
      "incomplete_value": true,
      "site": "004eb1a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ed0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004eb198",
      "incomplete_value": false,
      "site": "004eb1a4",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004eb158",
      "incomplete_value": false,
      "site": "004eb164",
      "value": [
        "leaf",
        "const:535828:8"
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
      "004eb140",
      "DATA",
      [
        "storage",
        "00c66a68",
        null,
        "undefined *"
      ]
    ],
    [
      "004eb198",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004eb19c",
      "READ",
      [
        "storage",
        "00c9aad0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004eb140",
      "DATA",
      [
        "storage",
        "00c66e68",
        null,
        "undefined *"
      ]
    ],
    [
      "004eb198",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004eb19c",
      "READ",
      [
        "storage",
        "00c9aed0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004eb140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004eb0e4.md#insn-004eb140) · [`004eb164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004eb0e4.md#insn-004eb164) · [`004eb0f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004eb0e4.md#insn-004eb0f8)
- 新版 [`004eb180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004eb/004eb124.md#insn-004eb180) · [`004eb1a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004eb/004eb124.md#insn-004eb1a4) · [`004eb138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004eb/004eb124.md#insn-004eb138)

~~~diff
- 004eb140 ["INT_ADD", "register:40f0:8", ["const:4eb140:8", "const:4:8"]]
- 004eb140 ["CALL", null, ["callee:00c57ef0:8"]]
+ 004eb180 ["INT_ADD", "register:40f0:8", ["const:4eb180:8", "const:4:8"]]
+ 004eb180 ["CALL", null, ["callee:00c57ef0:8"]]
- 004eb140 bytes 6cb21d94
+ 004eb180 bytes 5cb31d94
- 004eb164 ["INT_ADD", "register:40f0:8", ["const:4eb164:8", "const:4:8"]]
- 004eb164 ["CALL", null, ["callee:00c57f10:8"]]
+ 004eb1a4 ["INT_ADD", "register:40f0:8", ["const:4eb1a4:8", "const:4:8"]]
+ 004eb1a4 ["CALL", null, ["callee:00c57f10:8"]]
- 004eb164 bytes 6bb21d94
+ 004eb1a4 bytes 5bb31d94
- 004eb0f8 ["COPY", "tmp:0:8", ["const:a68:8"]]
- 004eb0f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004eb0f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004eb0f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004eb138 ["COPY", "tmp:0:8", ["const:e68:8"]]
+ 004eb138 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004eb138 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004eb138 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004eb0f8 bytes 08a12991
+ 004eb138 bytes 08a13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89317dc4402552cfd3f690fb33e81b42"></a>

### [`004eb2cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004eb2cc.md) → [`004eb30c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004eb/004eb30c.md) FUN_004eb30c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)

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
      "definition_site": "004eb3c8",
      "incomplete_value": true,
      "site": "004eb3c8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004eb3f4",
      "incomplete_value": true,
      "site": "004eb3f4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "004eb3b8",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004eb3e4",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004eb3b8",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004eb3e4",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004eb388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004eb2cc.md#insn-004eb388) · [`004eb3b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004eb2cc.md#insn-004eb3b4) · [`004eb310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004eb2cc.md#insn-004eb310)
- 新版 [`004eb3c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004eb/004eb30c.md#insn-004eb3c8) · [`004eb3f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004eb/004eb30c.md#insn-004eb3f4) · [`004eb350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004eb/004eb30c.md#insn-004eb350)

~~~diff
- 004eb388 ["COPY", "register:0:8", ["register:4048:8"]]
- 004eb388 ["INT_ADD", "register:40f0:8", ["const:4eb388:8", "const:4:8"]]
- 004eb388 ["CALLIND", null, ["register:0:8"]]
+ 004eb3c8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004eb3c8 ["INT_ADD", "register:40f0:8", ["const:4eb3c8:8", "const:4:8"]]
+ 004eb3c8 ["CALLIND", null, ["register:0:8"]]
- 004eb388 bytes 20013fd6
+ 004eb3c8 bytes 20013fd6
- 004eb3b4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004eb3b4 ["INT_ADD", "register:40f0:8", ["const:4eb3b4:8", "const:4:8"]]
- 004eb3b4 ["CALLIND", null, ["register:0:8"]]
+ 004eb3f4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004eb3f4 ["INT_ADD", "register:40f0:8", ["const:4eb3f4:8", "const:4:8"]]
+ 004eb3f4 ["CALLIND", null, ["register:0:8"]]
- 004eb3b4 bytes 20013fd6
+ 004eb3f4 bytes 20013fd6
- 004eb310 ["COPY", "register:0:8", ["register:4048:8"]]
- 004eb310 ["INT_ADD", "register:40f0:8", ["const:4eb310:8", "const:4:8"]]
- 004eb310 ["CALLIND", null, ["register:0:8"]]
+ 004eb350 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004eb350 ["INT_ADD", "register:40f0:8", ["const:4eb350:8", "const:4:8"]]
+ 004eb350 ["CALLIND", null, ["register:0:8"]]
- 004eb310 bytes 20013fd6
+ 004eb350 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fa069f98c6b6927150f19fff89b30c9"></a>

### [`004eb428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004eb428.md) → [`004eb468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004eb/004eb468.md) FUN_004eb468

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004f53c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f53c0.md) · 呼出先 6件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c58ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58ba0.md) [`00c590f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c590f0.md)
- 新版 呼出元 1件 [`004f5400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f5/004f5400.md) · 呼出先 6件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c58fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58fa0.md) [`00c594f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c594f0.md)

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
      "definition_site": "004eb47c",
      "incomplete_value": false,
      "site": "004eb484",
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
            "const:eb8:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004eb4e0",
      "incomplete_value": true,
      "site": "004eb4e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ed0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004eb4dc",
      "incomplete_value": false,
      "site": "004eb4e8",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004eb49c",
      "incomplete_value": false,
      "site": "004eb4a8",
      "value": [
        "leaf",
        "const:535828:8"
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
      "004eb484",
      "DATA",
      [
        "storage",
        "00c66ab8",
        null,
        "undefined *"
      ]
    ],
    [
      "004eb4dc",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004eb4e0",
      "READ",
      [
        "storage",
        "00c9aad0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004eb484",
      "DATA",
      [
        "storage",
        "00c66eb8",
        null,
        "undefined *"
      ]
    ],
    [
      "004eb4dc",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004eb4e0",
      "READ",
      [
        "storage",
        "00c9aed0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004eb484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004eb428.md#insn-004eb484) · [`004eb4a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004eb428.md#insn-004eb4a8) · [`004eb43c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004eb428.md#insn-004eb43c)
- 新版 [`004eb4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004eb/004eb468.md#insn-004eb4c4) · [`004eb4e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004eb/004eb468.md#insn-004eb4e8) · [`004eb47c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004eb/004eb468.md#insn-004eb47c)

~~~diff
- 004eb484 ["INT_ADD", "register:40f0:8", ["const:4eb484:8", "const:4:8"]]
- 004eb484 ["CALL", null, ["callee:00c57ef0:8"]]
+ 004eb4c4 ["INT_ADD", "register:40f0:8", ["const:4eb4c4:8", "const:4:8"]]
+ 004eb4c4 ["CALL", null, ["callee:00c57ef0:8"]]
- 004eb484 bytes 9bb11d94
+ 004eb4c4 bytes 8bb21d94
- 004eb4a8 ["INT_ADD", "register:40f0:8", ["const:4eb4a8:8", "const:4:8"]]
- 004eb4a8 ["CALL", null, ["callee:00c57f10:8"]]
+ 004eb4e8 ["INT_ADD", "register:40f0:8", ["const:4eb4e8:8", "const:4:8"]]
+ 004eb4e8 ["CALL", null, ["callee:00c57f10:8"]]
- 004eb4a8 bytes 9ab11d94
+ 004eb4e8 bytes 8ab21d94
- 004eb43c ["COPY", "tmp:0:8", ["const:ab8:8"]]
- 004eb43c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004eb43c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004eb43c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004eb47c ["COPY", "tmp:0:8", ["const:eb8:8"]]
+ 004eb47c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004eb47c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004eb47c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004eb43c bytes 08e12a91
+ 004eb47c bytes 08e13a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b91512c5cfa92d22ce02e910ef1a7de7"></a>

### [`004eb824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004eb824.md) → [`004eb864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004eb/004eb864.md) FUN_004eb864

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md) [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)

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
      "definition_site": "004eb94c",
      "incomplete_value": true,
      "site": "004eb94c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004eb990",
      "incomplete_value": true,
      "site": "004eb990",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "004eb93c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004eb980",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004eb93c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004eb980",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004eb90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004eb824.md#insn-004eb90c) · [`004eb950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004eb824.md#insn-004eb950) · [`004eb878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004eb824.md#insn-004eb878)
- 新版 [`004eb94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004eb/004eb864.md#insn-004eb94c) · [`004eb990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004eb/004eb864.md#insn-004eb990) · [`004eb8b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004eb/004eb864.md#insn-004eb8b8)

~~~diff
- 004eb90c ["COPY", "register:0:8", ["register:4048:8"]]
- 004eb90c ["INT_ADD", "register:40f0:8", ["const:4eb90c:8", "const:4:8"]]
- 004eb90c ["CALLIND", null, ["register:0:8"]]
+ 004eb94c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004eb94c ["INT_ADD", "register:40f0:8", ["const:4eb94c:8", "const:4:8"]]
+ 004eb94c ["CALLIND", null, ["register:0:8"]]
- 004eb90c bytes 20013fd6
+ 004eb94c bytes 20013fd6
- 004eb950 ["COPY", "register:0:8", ["register:4048:8"]]
- 004eb950 ["INT_ADD", "register:40f0:8", ["const:4eb950:8", "const:4:8"]]
- 004eb950 ["CALLIND", null, ["register:0:8"]]
+ 004eb990 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004eb990 ["INT_ADD", "register:40f0:8", ["const:4eb990:8", "const:4:8"]]
+ 004eb990 ["CALLIND", null, ["register:0:8"]]
- 004eb950 bytes 20013fd6
+ 004eb990 bytes 20013fd6
- 004eb878 ["COPY", "register:0:8", ["register:4040:8"]]
- 004eb878 ["INT_ADD", "register:40f0:8", ["const:4eb878:8", "const:4:8"]]
- 004eb878 ["CALLIND", null, ["register:0:8"]]
+ 004eb8b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004eb8b8 ["INT_ADD", "register:40f0:8", ["const:4eb8b8:8", "const:4:8"]]
+ 004eb8b8 ["CALLIND", null, ["register:0:8"]]
- 004eb878 bytes 00013fd6
+ 004eb8b8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f652c612ffbc1426e7a1609e49078021"></a>

### [`004ebb20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004ebb20.md) → [`004ebb60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004eb/004ebb60.md) _ZN5Botan5PKCS810PEM_encodeERKNS_11Private_KeyE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c591f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c591f0.md) · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c59090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59090.md) [`00c591e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c591e0.md)
- 新版 呼出元 1件 [`00c595f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c595f0.md) · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c59490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59490.md) [`00c595e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c595e0.md)

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
      "definition_site": "004ebbb8",
      "incomplete_value": true,
      "site": "004ebbb8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:140:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004ebc00",
      "incomplete_value": true,
      "site": "004ebc00",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "004ebba4",
      "READ",
      [
        "storage",
        "002a1073",
        null,
        "string"
      ]
    ],
    [
      "004ebbf0",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ebba4",
      "READ",
      [
        "storage",
        "002a1140",
        null,
        "string"
      ]
    ],
    [
      "004ebbf0",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ebbc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004ebb20.md#insn-004ebbc0) · [`004ebb48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004ebb20.md#insn-004ebb48) · [`004ebb54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004ebb20.md#insn-004ebb54)
- 新版 [`004ebc00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004eb/004ebb60.md#insn-004ebc00) · [`004ebb88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004eb/004ebb60.md#insn-004ebb88) · [`004ebb94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004eb/004ebb60.md#insn-004ebb94)

~~~diff
- 004ebbc0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004ebbc0 ["INT_ADD", "register:40f0:8", ["const:4ebbc0:8", "const:4:8"]]
- 004ebbc0 ["CALLIND", null, ["register:0:8"]]
+ 004ebc00 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004ebc00 ["INT_ADD", "register:40f0:8", ["const:4ebc00:8", "const:4:8"]]
+ 004ebc00 ["CALLIND", null, ["register:0:8"]]
- 004ebbc0 bytes 20013fd6
+ 004ebc00 bytes 20013fd6
- 004ebb48 ["INT_ADD", "register:40f0:8", ["const:4ebb48:8", "const:4:8"]]
- 004ebb48 ["CALL", null, ["callee:00c595e0:8"]]
+ 004ebb88 ["INT_ADD", "register:40f0:8", ["const:4ebb88:8", "const:4:8"]]
+ 004ebb88 ["CALL", null, ["callee:00c595e0:8"]]
- 004ebb48 bytes a6b51d94
+ 004ebb88 bytes 96b61d94
- 004ebb54 ["COPY", "tmp:0:8", ["const:73:8"]]
- 004ebb54 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004ebb54 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004ebb54 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004ebb94 ["COPY", "tmp:0:8", ["const:140:8"]]
+ 004ebb94 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004ebb94 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004ebb94 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004ebb54 bytes 29cd0191
+ 004ebb94 bytes 29010591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-268046f754533f2b661982f79280823f"></a>

### [`004ebc2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004ebc2c.md) → [`004ebc6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004eb/004ebc6c.md) _ZN5Botan5PKCS810BER_encodeERKNS_11Private_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS6_11char_traitsIcEENS6_9allocatorIc

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c59200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59200.md) · 呼出先 20件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`004a6d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6d70.md) [`004e2414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e2/004e2414.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00535b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b40.md)
- 新版 呼出元 1件 [`00c59600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59600.md) · 呼出先 20件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`004a6db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6db0.md) [`004e2454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e2/004e2454.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00535b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b80.md)

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
      "definition_site": "004ebd68",
      "incomplete_value": false,
      "site": "004ebd68",
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
            "const:c7a:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004ebd68",
      "incomplete_value": false,
      "site": "004ebd68",
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
            "const:b23:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004ebf48",
      "incomplete_value": false,
      "site": "004ebf48",
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
            "const:3cd:8"
          ]
        ]
      ]
    },
    "old": {
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
      "004ebd68",
      "DATA",
      [
        "storage",
        "002bec3a",
        null,
        "string"
      ]
    ],
    [
      "004ebd68",
      "DATA",
      [
        "storage",
        "002a9a56",
        null,
        "string"
      ]
    ],
    [
      "004ebf48",
      "DATA",
      [
        "storage",
        "002ab38d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004ebd68",
      "DATA",
      [
        "storage",
        "002bec7a",
        null,
        "string"
      ]
    ],
    [
      "004ebd68",
      "DATA",
      [
        "storage",
        "002a9b23",
        null,
        "string"
      ]
    ],
    [
      "004ebf48",
      "DATA",
      [
        "storage",
        "002ab3cd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ebf84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004ebc2c.md#insn-004ebf84) · [`004ec04c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004ebc2c.md#insn-004ec04c) · [`004ec0f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004ebc2c.md#insn-004ec0f4)
- 新版 [`004ebfc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004eb/004ebc6c.md#insn-004ebfc4) · [`004ec08c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004eb/004ebc6c.md#insn-004ec08c) · [`004ec134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004eb/004ebc6c.md#insn-004ec134)

~~~diff
- 004ebf84 ["COPY", "register:0:8", ["register:4048:8"]]
- 004ebf84 ["INT_ADD", "register:40f0:8", ["const:4ebf84:8", "const:4:8"]]
- 004ebf84 ["CALLIND", null, ["register:0:8"]]
+ 004ebfc4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004ebfc4 ["INT_ADD", "register:40f0:8", ["const:4ebfc4:8", "const:4:8"]]
+ 004ebfc4 ["CALLIND", null, ["register:0:8"]]
- 004ebf84 bytes 20013fd6
+ 004ebfc4 bytes 20013fd6
- 004ec04c ["COPY", "register:0:8", ["register:4048:8"]]
- 004ec04c ["INT_ADD", "register:40f0:8", ["const:4ec04c:8", "const:4:8"]]
- 004ec04c ["CALLIND", null, ["register:0:8"]]
+ 004ec08c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004ec08c ["INT_ADD", "register:40f0:8", ["const:4ec08c:8", "const:4:8"]]
+ 004ec08c ["CALLIND", null, ["register:0:8"]]
- 004ec04c bytes 20013fd6
+ 004ec08c bytes 20013fd6
- 004ec0f4 ["INT_ADD", "register:40f0:8", ["const:4ec0f4:8", "const:4:8"]]
- 004ec0f4 ["CALL", null, ["callee:00c580b0:8"]]
+ 004ec134 ["INT_ADD", "register:40f0:8", ["const:4ec134:8", "const:4:8"]]
+ 004ec134 ["CALL", null, ["callee:00c580b0:8"]]
- 004ec0f4 bytes efae1d94
+ 004ec134 bytes dfaf1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32bbdfb1745e3a33dd639c58387f92f3"></a>

### [`004ec25c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ec25c.md) → [`004ec29c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ec29c.md) _ZN5Botan5PKCS810PEM_encodeERKNS_11Private_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS6_11char_traitsIcEENS6_9allocatorIc

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59090.md) [`00c591f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c591f0.md) [`00c59200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59200.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59490.md) [`00c595f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c595f0.md) [`00c59600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59600.md)

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
      "definition_site": "004ec2f0",
      "incomplete_value": true,
      "site": "004ec300",
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
                "const:dc0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ec304",
      "incomplete_value": true,
      "site": "004ec304",
      "value": [
        "LOAD",
        "8",
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
      "004ec2f0",
      "READ",
      [
        "storage",
        "002b4d80",
        null,
        "string"
      ]
    ],
    [
      "004ec2f4",
      "READ",
      [
        "storage",
        "002b4d8d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004ec2f0",
      "READ",
      [
        "storage",
        "002b4dc0",
        null,
        "string"
      ]
    ],
    [
      "004ec2f4",
      "READ",
      [
        "storage",
        "002b4dcd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ec298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ec25c.md#insn-004ec298) · [`004ec2a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ec25c.md#insn-004ec2a4) · [`004ec2d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ec25c.md#insn-004ec2d4)
- 新版 [`004ec2d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ec29c.md#insn-004ec2d8) · [`004ec2e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ec29c.md#insn-004ec2e4) · [`004ec314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ec29c.md#insn-004ec314)

~~~diff
- 004ec298 ["INT_ADD", "register:40f0:8", ["const:4ec298:8", "const:4:8"]]
- 004ec298 ["CALL", null, ["callee:00c59600:8"]]
+ 004ec2d8 ["INT_ADD", "register:40f0:8", ["const:4ec2d8:8", "const:4:8"]]
+ 004ec2d8 ["CALL", null, ["callee:00c59600:8"]]
- 004ec298 bytes dab31d94
+ 004ec2d8 bytes cab41d94
- 004ec2a4 ["COPY", "tmp:0:8", ["const:d80:8"]]
- 004ec2a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004ec2a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004ec2a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004ec2e4 ["COPY", "tmp:0:8", ["const:dc0:8"]]
+ 004ec2e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004ec2e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004ec2e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004ec2a4 bytes 29013691
+ 004ec2e4 bytes 29013791
- 004ec2d4 ["INT_ADD", "register:40f0:8", ["const:4ec2d4:8", "const:4:8"]]
- 004ec2d4 ["CALL", null, ["callee:00c59490:8"]]
+ 004ec314 ["INT_ADD", "register:40f0:8", ["const:4ec314:8", "const:4:8"]]
+ 004ec314 ["CALL", null, ["callee:00c59490:8"]]
- 004ec2d4 bytes 6fb31d94
+ 004ec314 bytes 5fb41d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-616c6f641f38125c0bbf31059e5d413a"></a>

### [`004ec378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ec378.md) → [`004ec3b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ec3b8.md) _ZN5Botan5PKCS831BER_encode_encrypted_pbkdf_iterERKNS_11Private_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS6_11char_trait

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59210.md) · 呼出先 12件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`004a6d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6d70.md) [`004e2414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e2/004e2414.md) [`00535b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b40.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00c59610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59610.md) · 呼出先 12件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`004a6db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6db0.md) [`004e2454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e2/004e2454.md) [`00535b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "004ec450",
      "incomplete_value": true,
      "site": "004ec450",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c7a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004ec534",
      "incomplete_value": true,
      "site": "004ec534",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004ec5fc",
      "incomplete_value": true,
      "site": "004ec5fc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "004ec43c",
      "READ",
      [
        "storage",
        "002bec3a",
        null,
        "string"
      ]
    ],
    [
      "004ec524",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004ec5ec",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ec43c",
      "READ",
      [
        "storage",
        "002bec7a",
        null,
        "string"
      ]
    ],
    [
      "004ec524",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004ec5ec",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ec4f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ec378.md#insn-004ec4f4) · [`004ec5bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ec378.md#insn-004ec5bc) · [`004ec3bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ec378.md#insn-004ec3bc)
- 新版 [`004ec534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ec3b8.md#insn-004ec534) · [`004ec5fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ec3b8.md#insn-004ec5fc) · [`004ec3fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ec3b8.md#insn-004ec3fc)

~~~diff
- 004ec4f4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004ec4f4 ["INT_ADD", "register:40f0:8", ["const:4ec4f4:8", "const:4:8"]]
- 004ec4f4 ["CALLIND", null, ["register:0:8"]]
+ 004ec534 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004ec534 ["INT_ADD", "register:40f0:8", ["const:4ec534:8", "const:4:8"]]
+ 004ec534 ["CALLIND", null, ["register:0:8"]]
- 004ec4f4 bytes 20013fd6
+ 004ec534 bytes 20013fd6
- 004ec5bc ["COPY", "register:0:8", ["register:4048:8"]]
- 004ec5bc ["INT_ADD", "register:40f0:8", ["const:4ec5bc:8", "const:4:8"]]
- 004ec5bc ["CALLIND", null, ["register:0:8"]]
+ 004ec5fc ["COPY", "register:0:8", ["register:4048:8"]]
+ 004ec5fc ["INT_ADD", "register:40f0:8", ["const:4ec5fc:8", "const:4:8"]]
+ 004ec5fc ["CALLIND", null, ["register:0:8"]]
- 004ec5bc bytes 20013fd6
+ 004ec5fc bytes 20013fd6
- 004ec3bc ["INT_ADD", "register:40f0:8", ["const:4ec3bc:8", "const:4:8"]]
- 004ec3bc ["CALL", null, ["callee:00c595e0:8"]]
+ 004ec3fc ["INT_ADD", "register:40f0:8", ["const:4ec3fc:8", "const:4:8"]]
+ 004ec3fc ["CALL", null, ["callee:00c595e0:8"]]
- 004ec3bc bytes 89b31d94
+ 004ec3fc bytes 79b41d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-710bbdc650d36015b599ec2b7c08d9dc"></a>

### [`004ec69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ec69c.md) → [`004ec6dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ec6dc.md) _ZN5Botan5PKCS831PEM_encode_encrypted_pbkdf_iterERKNS_11Private_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS6_11char_trait

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59090.md) [`00c59210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59210.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59490.md) [`00c59610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59610.md)

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
      "definition_site": "004ec718",
      "incomplete_value": true,
      "site": "004ec728",
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
                "const:dc0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ec72c",
      "incomplete_value": true,
      "site": "004ec72c",
      "value": [
        "LOAD",
        "8",
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
      "004ec718",
      "READ",
      [
        "storage",
        "002b4d80",
        null,
        "string"
      ]
    ],
    [
      "004ec71c",
      "READ",
      [
        "storage",
        "002b4d8d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004ec718",
      "READ",
      [
        "storage",
        "002b4dc0",
        null,
        "string"
      ]
    ],
    [
      "004ec71c",
      "READ",
      [
        "storage",
        "002b4dcd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ec6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ec69c.md#insn-004ec6c0) · [`004ec6cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ec69c.md#insn-004ec6cc) · [`004ec6fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ec69c.md#insn-004ec6fc)
- 新版 [`004ec700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ec6dc.md#insn-004ec700) · [`004ec70c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ec6dc.md#insn-004ec70c) · [`004ec73c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ec6dc.md#insn-004ec73c)

~~~diff
- 004ec6c0 ["INT_ADD", "register:40f0:8", ["const:4ec6c0:8", "const:4:8"]]
- 004ec6c0 ["CALL", null, ["callee:00c59610:8"]]
+ 004ec700 ["INT_ADD", "register:40f0:8", ["const:4ec700:8", "const:4:8"]]
+ 004ec700 ["CALL", null, ["callee:00c59610:8"]]
- 004ec6c0 bytes d4b21d94
+ 004ec700 bytes c4b31d94
- 004ec6cc ["COPY", "tmp:0:8", ["const:d80:8"]]
- 004ec6cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004ec6cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004ec6cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004ec70c ["COPY", "tmp:0:8", ["const:dc0:8"]]
+ 004ec70c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004ec70c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004ec70c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004ec6cc bytes 29013691
+ 004ec70c bytes 29013791
- 004ec6fc ["INT_ADD", "register:40f0:8", ["const:4ec6fc:8", "const:4:8"]]
- 004ec6fc ["CALL", null, ["callee:00c59490:8"]]
+ 004ec73c ["INT_ADD", "register:40f0:8", ["const:4ec73c:8", "const:4:8"]]
+ 004ec73c ["CALL", null, ["callee:00c59490:8"]]
- 004ec6fc bytes 65b21d94
+ 004ec73c bytes 55b31d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3345aefdbf2a4a0a89c94256bf66feec"></a>

### [`004ec780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ec780.md) → [`004ec7c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ec7c0.md) _ZN5Botan5PKCS831BER_encode_encrypted_pbkdf_msecERKNS_11Private_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS6_11char_trait

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59220.md) · 呼出先 12件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`004a6d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6d70.md) [`004e2414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e2/004e2414.md) [`00535b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b40.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00c59620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59620.md) · 呼出先 12件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`004a6db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6db0.md) [`004e2454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e2/004e2454.md) [`00535b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "004ec860",
      "incomplete_value": true,
      "site": "004ec860",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c7a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004ec954",
      "incomplete_value": true,
      "site": "004ec954",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004eca1c",
      "incomplete_value": true,
      "site": "004eca1c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "004ec84c",
      "READ",
      [
        "storage",
        "002bec3a",
        null,
        "string"
      ]
    ],
    [
      "004ec944",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004eca0c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ec84c",
      "READ",
      [
        "storage",
        "002bec7a",
        null,
        "string"
      ]
    ],
    [
      "004ec944",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004eca0c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ec914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ec780.md#insn-004ec914) · [`004ec9dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ec780.md#insn-004ec9dc) · [`004ec7cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ec780.md#insn-004ec7cc)
- 新版 [`004ec954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ec7c0.md#insn-004ec954) · [`004eca1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ec7c0.md#insn-004eca1c) · [`004ec80c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ec7c0.md#insn-004ec80c)

~~~diff
- 004ec914 ["COPY", "register:0:8", ["register:4048:8"]]
- 004ec914 ["INT_ADD", "register:40f0:8", ["const:4ec914:8", "const:4:8"]]
- 004ec914 ["CALLIND", null, ["register:0:8"]]
+ 004ec954 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004ec954 ["INT_ADD", "register:40f0:8", ["const:4ec954:8", "const:4:8"]]
+ 004ec954 ["CALLIND", null, ["register:0:8"]]
- 004ec914 bytes 20013fd6
+ 004ec954 bytes 20013fd6
- 004ec9dc ["COPY", "register:0:8", ["register:4048:8"]]
- 004ec9dc ["INT_ADD", "register:40f0:8", ["const:4ec9dc:8", "const:4:8"]]
- 004ec9dc ["CALLIND", null, ["register:0:8"]]
+ 004eca1c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004eca1c ["INT_ADD", "register:40f0:8", ["const:4eca1c:8", "const:4:8"]]
+ 004eca1c ["CALLIND", null, ["register:0:8"]]
- 004ec9dc bytes 20013fd6
+ 004eca1c bytes 20013fd6
- 004ec7cc ["INT_ADD", "register:40f0:8", ["const:4ec7cc:8", "const:4:8"]]
- 004ec7cc ["CALL", null, ["callee:00c595e0:8"]]
+ 004ec80c ["INT_ADD", "register:40f0:8", ["const:4ec80c:8", "const:4:8"]]
+ 004ec80c ["CALL", null, ["callee:00c595e0:8"]]
- 004ec7cc bytes 85b21d94
+ 004ec80c bytes 75b31d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b5424a63b069fce2ceca930b1435550"></a>

### [`004ecac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ecac0.md) → [`004ecb00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ecb00.md) _ZN5Botan5PKCS831PEM_encode_encrypted_pbkdf_msecERKNS_11Private_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS6_11char_trait

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59090.md) [`00c59220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59220.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59490.md) [`00c59620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59620.md)

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
      "definition_site": "004ecb3c",
      "incomplete_value": true,
      "site": "004ecb4c",
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
                "const:dc0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ecb50",
      "incomplete_value": true,
      "site": "004ecb50",
      "value": [
        "LOAD",
        "8",
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
      "004ecb3c",
      "READ",
      [
        "storage",
        "002b4d80",
        null,
        "string"
      ]
    ],
    [
      "004ecb40",
      "READ",
      [
        "storage",
        "002b4d8d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004ecb3c",
      "READ",
      [
        "storage",
        "002b4dc0",
        null,
        "string"
      ]
    ],
    [
      "004ecb40",
      "READ",
      [
        "storage",
        "002b4dcd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ecae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ecac0.md#insn-004ecae4) · [`004ecaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ecac0.md#insn-004ecaf0) · [`004ecb20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ecac0.md#insn-004ecb20)
- 新版 [`004ecb24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ecb00.md#insn-004ecb24) · [`004ecb30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ecb00.md#insn-004ecb30) · [`004ecb60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ecb00.md#insn-004ecb60)

~~~diff
- 004ecae4 ["INT_ADD", "register:40f0:8", ["const:4ecae4:8", "const:4:8"]]
- 004ecae4 ["CALL", null, ["callee:00c59620:8"]]
+ 004ecb24 ["INT_ADD", "register:40f0:8", ["const:4ecb24:8", "const:4:8"]]
+ 004ecb24 ["CALL", null, ["callee:00c59620:8"]]
- 004ecae4 bytes cfb11d94
+ 004ecb24 bytes bfb21d94
- 004ecaf0 ["COPY", "tmp:0:8", ["const:d80:8"]]
- 004ecaf0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004ecaf0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004ecaf0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004ecb30 ["COPY", "tmp:0:8", ["const:dc0:8"]]
+ 004ecb30 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004ecb30 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004ecb30 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004ecaf0 bytes 29013691
+ 004ecb30 bytes 29013791
- 004ecb20 ["INT_ADD", "register:40f0:8", ["const:4ecb20:8", "const:4:8"]]
- 004ecb20 ["CALL", null, ["callee:00c59490:8"]]
+ 004ecb60 ["INT_ADD", "register:40f0:8", ["const:4ecb60:8", "const:4:8"]]
+ 004ecb60 ["CALL", null, ["callee:00c59490:8"]]
- 004ecb20 bytes 5cb11d94
+ 004ecb60 bytes 4cb21d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce413083b6362b312b68093c6458cd53"></a>

### [`004eccd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004eccd0.md) → [`004ecd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ecd10.md) FUN_004ecd10

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 9件 [`004ecba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ecba4.md) [`004edc54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ed/004edc54.md) [`004edd9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ed/004edd9c.md) [`004ede74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ed/004ede74.md) [`004edfd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ed/004edfd8.md) · 呼出先 34件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`004a573c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a573c.md) [`004a6f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6f5c.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md)
- 新版 呼出元 9件 [`004ecbe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ecbe4.md) [`004edc94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ed/004edc94.md) [`004edddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ed/004edddc.md) [`004edeb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ed/004edeb4.md) [`004ee018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004ee018.md) · 呼出先 34件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`004a577c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a577c.md) [`004a6f9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6f9c.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.79% / 新版 93.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `call_target` 9件, `store_value` 5件

アドレスに依存する影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ecd54",
      "incomplete_value": true,
      "site": "004ecd5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ecf9c",
      "incomplete_value": true,
      "site": "004ecf9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "ordinal": 40,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ed244",
      "incomplete_value": true,
      "site": "004ed258",
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
                "const:2f1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "004ecd40",
      "READ",
      [
        "storage",
        "00c9a938",
        null,
        "pointer"
      ]
    ],
    [
      "004ecd5c",
      "DATA",
      [
        "storage",
        "00c65da8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004ecdd4",
      "DATA",
      [
        "storage",
        "00c65da8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004ecd40",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "004ecd5c",
      "DATA",
      [
        "storage",
        "00c661a8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004ecdd4",
      "DATA",
      [
        "storage",
        "00c661a8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ece04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004eccd0.md#insn-004ece04) · [`004ece44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004eccd0.md#insn-004ece44) · [`004ecfa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004eccd0.md#insn-004ecfa0)
- 新版 [`004ece44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ecd10.md#insn-004ece44) · [`004ece84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ecd10.md#insn-004ece84) · [`004ecfe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ecd10.md#insn-004ecfe0)

~~~diff
- 004ece04 ["INT_ADD", "register:40f0:8", ["const:4ece04:8", "const:4:8"]]
- 004ece04 ["CALL", null, ["callee:00c57eb0:8"]]
+ 004ece44 ["INT_ADD", "register:40f0:8", ["const:4ece44:8", "const:4:8"]]
+ 004ece44 ["CALL", null, ["callee:00c57eb0:8"]]
- 004ece04 bytes 2bab1d94
+ 004ece44 bytes 1bac1d94
- 004ece44 ["COPY", "register:0:8", ["register:4048:8"]]
- 004ece44 ["INT_ADD", "register:40f0:8", ["const:4ece44:8", "const:4:8"]]
- 004ece44 ["CALLIND", null, ["register:0:8"]]
+ 004ece84 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004ece84 ["INT_ADD", "register:40f0:8", ["const:4ece84:8", "const:4:8"]]
+ 004ece84 ["CALLIND", null, ["register:0:8"]]
- 004ece44 bytes 20013fd6
+ 004ece84 bytes 20013fd6
- 004ecfa0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004ecfa0 ["INT_ADD", "register:40f0:8", ["const:4ecfa0:8", "const:4:8"]]
- 004ecfa0 ["CALLIND", null, ["register:0:8"]]
+ 004ecfe0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004ecfe0 ["INT_ADD", "register:40f0:8", ["const:4ecfe0:8", "const:4:8"]]
+ 004ecfe0 ["CALLIND", null, ["register:0:8"]]
- 004ecfa0 bytes 20013fd6
+ 004ecfe0 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf12fe5e1615249cd77782c00ee241ab"></a>

### [`004edc54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ed/004edc54.md) → [`004edc94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ed/004edc94.md) _ZN5Botan5PKCS88load_keyERNS_10DataSourceERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59230.md) · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`004eccd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004eccd0.md) [`0054586c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/0054586c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00c59630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59630.md) · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`004ecd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ecd10.md) [`005458ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/005458ac.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.72% / 新版 96.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004edd04",
      "incomplete_value": false,
      "site": "004edd04",
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
            "const:520:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004edcc4",
      "incomplete_value": false,
      "site": "004edcc4",
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
            "const:120:8"
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
      "004edd04",
      "DATA",
      [
        "storage",
        "00c6a120",
        null,
        "undefined *"
      ]
    ],
    [
      "004edd48",
      "READ",
      [
        "storage",
        "00c6a148",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004edd04",
      "DATA",
      [
        "storage",
        "00c6a520",
        null,
        "undefined *"
      ]
    ],
    [
      "004edd48",
      "READ",
      [
        "storage",
        "00c6a548",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004edca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ed/004edc54.md#insn-004edca4) · [`004edcb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ed/004edc54.md#insn-004edcb0) · [`004edcc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ed/004edc54.md#insn-004edcc0)
- 新版 [`004edce4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ed/004edc94.md#insn-004edce4) · [`004edcf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ed/004edc94.md#insn-004edcf0) · [`004edd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ed/004edc94.md#insn-004edd00)

~~~diff
- 004edca4 ["INT_ADD", "register:40f0:8", ["const:4edca4:8", "const:4:8"]]
- 004edca4 ["CALL", null, ["callee:0043bb20:8"]]
+ 004edce4 ["INT_ADD", "register:40f0:8", ["const:4edce4:8", "const:4:8"]]
+ 004edce4 ["CALL", null, ["callee:0043bb20:8"]]
- 004edca4 bytes 8f37fd97
+ 004edce4 bytes 8f37fd97
- 004edcb0 ["INT_ADD", "register:40f0:8", ["const:4edcb0:8", "const:4:8"]]
- 004edcb0 ["CALL", null, ["callee:00c57e90:8"]]
+ 004edcf0 ["INT_ADD", "register:40f0:8", ["const:4edcf0:8", "const:4:8"]]
+ 004edcf0 ["CALL", null, ["callee:00c57e90:8"]]
- 004edcb0 bytes 78a71d94
+ 004edcf0 bytes 68a81d94
- 004edcc0 ["COPY", "tmp:0:8", ["const:120:8"]]
- 004edcc0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004edcc0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004edcc0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004edd00 ["COPY", "tmp:0:8", ["const:520:8"]]
+ 004edd00 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004edd00 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004edd00 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004edcc0 bytes 29810491
+ 004edd00 bytes 29811491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03fb37f3d6da0f89d46e4efd5c186610"></a>

### [`004edd9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ed/004edd9c.md) → [`004edddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ed/004edddc.md) _ZN5Botan5PKCS88load_keyERNS_10DataSourceE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59240.md) · 呼出先 4件 [`004eccd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004eccd0.md) [`00545930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545930.md) [`00545934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545934.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00c59640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59640.md) · 呼出先 4件 [`004ecd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ecd10.md) [`00545970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545970.md) [`00545974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545974.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

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
      "definition_site": "004eddf4",
      "incomplete_value": false,
      "site": "004ede04",
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
            "const:5b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004eddb4",
      "incomplete_value": false,
      "site": "004eddc4",
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
            "const:1b0:8"
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
      "004ede04",
      "DATA",
      [
        "storage",
        "00c6a1b0",
        null,
        "undefined *"
      ]
    ],
    [
      "004ede3c",
      "READ",
      [
        "storage",
        "00c6a1d0",
        null,
        "pointer"
      ]
    ],
    [
      "004ede3c",
      "READ",
      [
        "storage",
        "00c6a1d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004ede04",
      "DATA",
      [
        "storage",
        "00c6a5b0",
        null,
        "undefined *"
      ]
    ],
    [
      "004ede3c",
      "READ",
      [
        "storage",
        "00c6a5d0",
        null,
        "pointer"
      ]
    ],
    [
      "004ede3c",
      "READ",
      [
        "storage",
        "00c6a5d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004eddb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ed/004edd9c.md#insn-004eddb4) · [`004eddd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ed/004edd9c.md#insn-004eddd4) · [`004ede00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ed/004edd9c.md#insn-004ede00)
- 新版 [`004eddf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ed/004edddc.md#insn-004eddf4) · [`004ede14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ed/004edddc.md#insn-004ede14) · [`004ede40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ed/004edddc.md#insn-004ede40)

~~~diff
- 004eddb4 ["COPY", "tmp:0:8", ["const:1b0:8"]]
- 004eddb4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004eddb4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004eddb4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 004eddf4 ["COPY", "tmp:0:8", ["const:5b0:8"]]
+ 004eddf4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 004eddf4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 004eddf4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004eddb4 bytes 4ac10691
+ 004eddf4 bytes 4ac11691
- 004eddd4 ["INT_ADD", "register:40f0:8", ["const:4eddd4:8", "const:4:8"]]
- 004eddd4 ["CALL", null, ["callee:004ecd10:8"]]
+ 004ede14 ["INT_ADD", "register:40f0:8", ["const:4ede14:8", "const:4:8"]]
+ 004ede14 ["CALL", null, ["callee:004ecd10:8"]]
- 004eddd4 bytes bffbff97
+ 004ede14 bytes bffbff97
- 004ede00 ["COPY", "register:0:8", ["register:4040:8"]]
- 004ede00 ["INT_ADD", "register:40f0:8", ["const:4ede00:8", "const:4:8"]]
- 004ede00 ["CALLIND", null, ["register:0:8"]]
+ 004ede40 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004ede40 ["INT_ADD", "register:40f0:8", ["const:4ede40:8", "const:4:8"]]
+ 004ede40 ["CALLIND", null, ["register:0:8"]]
- 004ede00 bytes 00013fd6
+ 004ede40 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08473e9b9c034efd386bd40c74fa31e5"></a>

### [`004ede74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ed/004ede74.md) → [`004edeb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ed/004edeb4.md) _ZN5Botan5PKCS88copy_keyERKNS_11Private_KeyE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59250.md) · 呼出先 9件 [`004eccd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004eccd0.md) [`00545930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545930.md) [`00545934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545934.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00c59650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59650.md) · 呼出先 9件 [`004ecd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ecd10.md) [`00545970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545970.md) [`00545974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545974.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.72% / 新版 96.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004edf00",
      "incomplete_value": false,
      "site": "004edf08",
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
            "const:5b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004edec0",
      "incomplete_value": false,
      "site": "004edec8",
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
            "const:1b0:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004edf74",
      "incomplete_value": true,
      "site": "004edf74",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004edf34",
      "incomplete_value": true,
      "site": "004edf34",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004edf08",
      "DATA",
      [
        "storage",
        "00c6a1b0",
        null,
        "undefined *"
      ]
    ],
    [
      "004edf48",
      "READ",
      [
        "storage",
        "00c6a1d0",
        null,
        "pointer"
      ]
    ],
    [
      "004edf48",
      "READ",
      [
        "storage",
        "00c6a1d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004edf08",
      "DATA",
      [
        "storage",
        "00c6a5b0",
        null,
        "undefined *"
      ]
    ],
    [
      "004edf48",
      "READ",
      [
        "storage",
        "00c6a5d0",
        null,
        "pointer"
      ]
    ],
    [
      "004edf48",
      "READ",
      [
        "storage",
        "00c6a5d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004edf34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ed/004ede74.md#insn-004edf34) · [`004ede9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ed/004ede74.md#insn-004ede9c) · [`004edea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ed/004ede74.md#insn-004edea8)
- 新版 [`004edf74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ed/004edeb4.md#insn-004edf74) · [`004ededc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ed/004edeb4.md#insn-004ededc) · [`004edee8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ed/004edeb4.md#insn-004edee8)

~~~diff
- 004edf34 ["COPY", "register:0:8", ["register:4048:8"]]
- 004edf34 ["INT_ADD", "register:40f0:8", ["const:4edf34:8", "const:4:8"]]
- 004edf34 ["CALLIND", null, ["register:0:8"]]
+ 004edf74 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004edf74 ["INT_ADD", "register:40f0:8", ["const:4edf74:8", "const:4:8"]]
+ 004edf74 ["CALLIND", null, ["register:0:8"]]
- 004edf34 bytes 20013fd6
+ 004edf74 bytes 20013fd6
- 004ede9c ["INT_ADD", "register:40f0:8", ["const:4ede9c:8", "const:4:8"]]
- 004ede9c ["CALL", null, ["callee:00c595f0:8"]]
+ 004ededc ["INT_ADD", "register:40f0:8", ["const:4ededc:8", "const:4:8"]]
+ 004ededc ["CALL", null, ["callee:00c595f0:8"]]
- 004ede9c bytes d5ac1d94
+ 004ededc bytes c5ad1d94
- 004edea8 ["INT_ADD", "register:40f0:8", ["const:4edea8:8", "const:4:8"]]
- 004edea8 ["CALL", null, ["callee:00c594c0:8"]]
+ 004edee8 ["INT_ADD", "register:40f0:8", ["const:4edee8:8", "const:4:8"]]
+ 004edee8 ["CALL", null, ["callee:00c594c0:8"]]
- 004edea8 bytes 86ac1d94
+ 004edee8 bytes 76ad1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-847103b4ef9f0e097d79600a73b50dd5"></a>

### [`004ee214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004ee214.md) → [`004ee254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004ee254.md) _ZN5Botan5PKCS88load_keyERNS_10DataSourceERNS_21RandomNumberGeneratorE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`004eccd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004eccd0.md) [`00545930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545930.md) [`00545934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545934.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004ecd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ecd10.md) [`00545970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545970.md) [`00545974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545974.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004ee26c",
      "incomplete_value": false,
      "site": "004ee27c",
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
            "const:5b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ee22c",
      "incomplete_value": false,
      "site": "004ee23c",
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
            "const:1b0:8"
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
      "004ee27c",
      "DATA",
      [
        "storage",
        "00c6a1b0",
        null,
        "undefined *"
      ]
    ],
    [
      "004ee2b8",
      "READ",
      [
        "storage",
        "00c6a1d0",
        null,
        "pointer"
      ]
    ],
    [
      "004ee2b8",
      "READ",
      [
        "storage",
        "00c6a1d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004ee27c",
      "DATA",
      [
        "storage",
        "00c6a5b0",
        null,
        "undefined *"
      ]
    ],
    [
      "004ee2b8",
      "READ",
      [
        "storage",
        "00c6a5d0",
        null,
        "pointer"
      ]
    ],
    [
      "004ee2b8",
      "READ",
      [
        "storage",
        "00c6a5d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ee27c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004ee214.md#insn-004ee27c) · [`004ee22c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004ee214.md#insn-004ee22c) · [`004ee250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004ee214.md#insn-004ee250)
- 新版 [`004ee2bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004ee254.md#insn-004ee2bc) · [`004ee26c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004ee254.md#insn-004ee26c) · [`004ee290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004ee254.md#insn-004ee290)

~~~diff
- 004ee27c ["COPY", "register:0:8", ["register:4040:8"]]
- 004ee27c ["INT_ADD", "register:40f0:8", ["const:4ee27c:8", "const:4:8"]]
- 004ee27c ["CALLIND", null, ["register:0:8"]]
+ 004ee2bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 004ee2bc ["INT_ADD", "register:40f0:8", ["const:4ee2bc:8", "const:4:8"]]
+ 004ee2bc ["CALLIND", null, ["register:0:8"]]
- 004ee27c bytes 00013fd6
+ 004ee2bc bytes 00013fd6
- 004ee22c ["COPY", "tmp:0:8", ["const:1b0:8"]]
- 004ee22c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004ee22c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004ee22c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004ee26c ["COPY", "tmp:0:8", ["const:5b0:8"]]
+ 004ee26c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004ee26c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004ee26c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004ee22c bytes 29c10691
+ 004ee26c bytes 29c11691
- 004ee250 ["INT_ADD", "register:40f0:8", ["const:4ee250:8", "const:4:8"]]
- 004ee250 ["CALL", null, ["callee:004ecd10:8"]]
+ 004ee290 ["INT_ADD", "register:40f0:8", ["const:4ee290:8", "const:4:8"]]
+ 004ee290 ["CALL", null, ["callee:004ecd10:8"]]
- 004ee250 bytes a0faff97
+ 004ee290 bytes a0faff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f31b9cf1c2d3dac32dd6c3734278256c"></a>

### [`004ee4f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004ee4f4.md) → [`004ee534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004ee534.md) _ZN5Botan5PKCS88load_keyERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERNS_21RandomNumberGeneratorES9_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`004eccd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004eccd0.md) [`00545ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545ab0.md) [`00545b74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545b74.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`004ecd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ecd10.md) [`00545af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545af0.md) [`00545bb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545bb4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004ee5ac",
      "incomplete_value": false,
      "site": "004ee5ac",
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
            "const:630:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ee56c",
      "incomplete_value": false,
      "site": "004ee56c",
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
            "const:230:8"
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
      "004ee5ac",
      "DATA",
      [
        "storage",
        "00c6a230",
        null,
        "pointer"
      ]
    ],
    [
      "004ee5ec",
      "READ",
      [
        "storage",
        "00c6a240",
        null,
        "undefined *"
      ]
    ],
    [
      "004ee650",
      "READ",
      [
        "storage",
        "00c6a258",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004ee5ac",
      "DATA",
      [
        "storage",
        "00c6a630",
        null,
        "pointer"
      ]
    ],
    [
      "004ee5ec",
      "READ",
      [
        "storage",
        "00c6a640",
        null,
        "undefined *"
      ]
    ],
    [
      "004ee650",
      "READ",
      [
        "storage",
        "00c6a658",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ee524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004ee4f4.md#insn-004ee524) · [`004ee54c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004ee4f4.md#insn-004ee54c) · [`004ee558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004ee4f4.md#insn-004ee558)
- 新版 [`004ee564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004ee534.md#insn-004ee564) · [`004ee58c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004ee534.md#insn-004ee58c) · [`004ee598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004ee534.md#insn-004ee598)

~~~diff
- 004ee524 ["INT_ADD", "register:40f0:8", ["const:4ee524:8", "const:4:8"]]
- 004ee524 ["CALL", null, ["callee:00c59660:8"]]
+ 004ee564 ["INT_ADD", "register:40f0:8", ["const:4ee564:8", "const:4:8"]]
+ 004ee564 ["CALL", null, ["callee:00c59660:8"]]
- 004ee524 bytes 4fab1d94
+ 004ee564 bytes 3fac1d94
- 004ee54c ["INT_ADD", "register:40f0:8", ["const:4ee54c:8", "const:4:8"]]
- 004ee54c ["CALL", null, ["callee:0043bb20:8"]]
+ 004ee58c ["INT_ADD", "register:40f0:8", ["const:4ee58c:8", "const:4:8"]]
+ 004ee58c ["CALL", null, ["callee:0043bb20:8"]]
- 004ee54c bytes 6535fd97
+ 004ee58c bytes 6535fd97
- 004ee558 ["INT_ADD", "register:40f0:8", ["const:4ee558:8", "const:4:8"]]
- 004ee558 ["CALL", null, ["callee:00c57e90:8"]]
+ 004ee598 ["INT_ADD", "register:40f0:8", ["const:4ee598:8", "const:4:8"]]
+ 004ee598 ["CALL", null, ["callee:00c57e90:8"]]
- 004ee558 bytes 4ea51d94
+ 004ee598 bytes 3ea61d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6acb3cd83d1bf48f3519e4f9a738add"></a>

### [`004ee700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004ee700.md) → [`004ee740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004ee740.md) _ZN5Botan5PKCS88load_keyERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERNS_21RandomNumberGeneratorE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`004eccd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004eccd0.md) [`00545930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545930.md) [`00545934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545934.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59260.md)
- 新版 呼出元 0件  · 呼出先 6件 [`004ecd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ecd10.md) [`00545970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545970.md) [`00545974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/00545974.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59660.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.56% / 新版 95.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004ee770",
      "incomplete_value": false,
      "site": "004ee778",
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
            "const:5b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ee730",
      "incomplete_value": false,
      "site": "004ee738",
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
            "const:1b0:8"
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
      "004ee778",
      "DATA",
      [
        "storage",
        "00c6a1b0",
        null,
        "undefined *"
      ]
    ],
    [
      "004ee7b8",
      "READ",
      [
        "storage",
        "00c6a1d0",
        null,
        "pointer"
      ]
    ],
    [
      "004ee7b8",
      "READ",
      [
        "storage",
        "00c6a1d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004ee778",
      "DATA",
      [
        "storage",
        "00c6a5b0",
        null,
        "undefined *"
      ]
    ],
    [
      "004ee7b8",
      "READ",
      [
        "storage",
        "00c6a5d0",
        null,
        "pointer"
      ]
    ],
    [
      "004ee7b8",
      "READ",
      [
        "storage",
        "00c6a5d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ee728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004ee700.md#insn-004ee728) · [`004ee730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004ee700.md#insn-004ee730) · [`004ee750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004ee700.md#insn-004ee750)
- 新版 [`004ee768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004ee740.md#insn-004ee768) · [`004ee770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004ee740.md#insn-004ee770) · [`004ee790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004ee740.md#insn-004ee790)

~~~diff
- 004ee728 ["INT_ADD", "register:40f0:8", ["const:4ee728:8", "const:4:8"]]
- 004ee728 ["CALL", null, ["callee:00c59660:8"]]
+ 004ee768 ["INT_ADD", "register:40f0:8", ["const:4ee768:8", "const:4:8"]]
+ 004ee768 ["CALL", null, ["callee:00c59660:8"]]
- 004ee728 bytes ceaa1d94
+ 004ee768 bytes beab1d94
- 004ee730 ["COPY", "tmp:0:8", ["const:1b0:8"]]
- 004ee730 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004ee730 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004ee730 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004ee770 ["COPY", "tmp:0:8", ["const:5b0:8"]]
+ 004ee770 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004ee770 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004ee770 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004ee730 bytes 08c10691
+ 004ee770 bytes 08c11691
- 004ee750 ["INT_ADD", "register:40f0:8", ["const:4ee750:8", "const:4:8"]]
- 004ee750 ["CALL", null, ["callee:004ecd10:8"]]
+ 004ee790 ["INT_ADD", "register:40f0:8", ["const:4ee790:8", "const:4:8"]]
+ 004ee790 ["CALL", null, ["callee:004ecd10:8"]]
- 004ee750 bytes 60f9ff97
+ 004ee790 bytes 60f9ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79dbca6e47ef526d2a74f385137e6edb"></a>

### [`004ee854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004ee854.md) → [`004ee894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004ee894.md) _ZNK5Botan12PK_Decryptor7decryptEPKhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58df0.md) · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`00c591f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c591f0.md) · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
      "definition_site": "004ee918",
      "incomplete_value": false,
      "site": "004ee920",
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
            "const:99:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ee8d8",
      "incomplete_value": false,
      "site": "004ee8e0",
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
            "const:fcc:8"
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
      "definition_site": "004ee954",
      "incomplete_value": true,
      "site": "004ee960",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ee914",
      "incomplete_value": true,
      "site": "004ee920",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ee950",
      "incomplete_value": false,
      "site": "004ee960",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004ee910",
      "incomplete_value": false,
      "site": "004ee920",
      "value": [
        "leaf",
        "const:535828:8"
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
      "004ee918",
      "PARAM",
      [
        "storage",
        "0029ffcc",
        null,
        "string"
      ]
    ],
    [
      "004ee950",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004ee954",
      "READ",
      [
        "storage",
        "00c9a950",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ee918",
      "PARAM",
      [
        "storage",
        "002a0099",
        null,
        "string"
      ]
    ],
    [
      "004ee950",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004ee954",
      "READ",
      [
        "storage",
        "00c9ad50",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ee8e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004ee854.md#insn-004ee8e0) · [`004ee920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004ee854.md#insn-004ee920) · [`004ee894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004ee854.md#insn-004ee894)
- 新版 [`004ee920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004ee894.md#insn-004ee920) · [`004ee960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004ee894.md#insn-004ee960) · [`004ee8d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004ee894.md#insn-004ee8d4)

~~~diff
- 004ee8e0 ["INT_ADD", "register:40f0:8", ["const:4ee8e0:8", "const:4:8"]]
- 004ee8e0 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004ee920 ["INT_ADD", "register:40f0:8", ["const:4ee920:8", "const:4:8"]]
+ 004ee920 ["CALL", null, ["callee:0043ddd8:8"]]
- 004ee8e0 bytes 2e3dfd97
+ 004ee920 bytes 2e3dfd97
- 004ee920 ["INT_ADD", "register:40f0:8", ["const:4ee920:8", "const:4:8"]]
- 004ee920 ["CALL", null, ["callee:00c57f10:8"]]
+ 004ee960 ["INT_ADD", "register:40f0:8", ["const:4ee960:8", "const:4:8"]]
+ 004ee960 ["CALL", null, ["callee:00c57f10:8"]]
- 004ee920 bytes 7ca41d94
+ 004ee960 bytes 6ca51d94
- 004ee894 ["COPY", "register:0:8", ["register:4048:8"]]
- 004ee894 ["INT_ADD", "register:40f0:8", ["const:4ee894:8", "const:4:8"]]
- 004ee894 ["CALLIND", null, ["register:0:8"]]
+ 004ee8d4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004ee8d4 ["INT_ADD", "register:40f0:8", ["const:4ee8d4:8", "const:4:8"]]
+ 004ee8d4 ["CALLIND", null, ["register:0:8"]]
- 004ee894 bytes 20013fd6
+ 004ee8d4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f233fb79d915f065665f1c125c2d113d"></a>

### [`004ee97c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004ee97c.md) → [`004ee9bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004ee9bc.md) _ZNK5Botan12PK_Decryptor17decrypt_or_randomEPKhmmRNS_21RandomNumberGeneratorES2_S2_m

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59280.md) · 呼出先 6件 [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58250.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md)
- 新版 呼出元 1件 [`00c59680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59680.md) · 呼出先 6件 [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md) [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58650.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.78% / 新版 97.78%

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
      "definition_site": "004eeb78",
      "incomplete_value": true,
      "site": "004eeb78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004eeb38",
      "incomplete_value": true,
      "site": "004eeb38",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004eec64",
      "incomplete_value": false,
      "site": "004eec84",
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
            "const:8ba:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004eec24",
      "incomplete_value": false,
      "site": "004eec44",
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
            "const:87a:8"
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
      "definition_site": "004eec6c",
      "incomplete_value": false,
      "site": "004eec84",
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
            "const:f68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004eec2c",
      "incomplete_value": false,
      "site": "004eec44",
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
            "const:f28:8"
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
      "004eeb68",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004eec64",
      "PARAM",
      [
        "storage",
        "002ae87a",
        null,
        "string"
      ]
    ],
    [
      "004eec6c",
      "PARAM",
      [
        "storage",
        "002b8f28",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004eeb68",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004eec64",
      "PARAM",
      [
        "storage",
        "002ae8ba",
        null,
        "string"
      ]
    ],
    [
      "004eec6c",
      "PARAM",
      [
        "storage",
        "002b8f68",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004eeb38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004ee97c.md#insn-004eeb38) · [`004eec44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004ee97c.md#insn-004eec44) · [`004ee9d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004ee97c.md#insn-004ee9d4)
- 新版 [`004eeb78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004ee9bc.md#insn-004eeb78) · [`004eec84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004ee9bc.md#insn-004eec84) · [`004eea14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004ee9bc.md#insn-004eea14)

~~~diff
- 004eeb38 ["COPY", "register:0:8", ["register:4048:8"]]
- 004eeb38 ["INT_ADD", "register:40f0:8", ["const:4eeb38:8", "const:4:8"]]
- 004eeb38 ["CALLIND", null, ["register:0:8"]]
+ 004eeb78 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004eeb78 ["INT_ADD", "register:40f0:8", ["const:4eeb78:8", "const:4:8"]]
+ 004eeb78 ["CALLIND", null, ["register:0:8"]]
- 004eeb38 bytes 20013fd6
+ 004eeb78 bytes 20013fd6
- 004eec44 ["INT_ADD", "register:40f0:8", ["const:4eec44:8", "const:4:8"]]
- 004eec44 ["CALL", null, ["callee:00c58650:8"]]
+ 004eec84 ["INT_ADD", "register:40f0:8", ["const:4eec84:8", "const:4:8"]]
+ 004eec84 ["CALL", null, ["callee:00c58650:8"]]
- 004eec44 bytes 83a51d94
+ 004eec84 bytes 73a61d94
- 004ee9d4 ["INT_ADD", "register:40f0:8", ["const:4ee9d4:8", "const:4:8"]]
- 004ee9d4 ["CALL", null, ["callee:004b3508:8"]]
+ 004eea14 ["INT_ADD", "register:40f0:8", ["const:4eea14:8", "const:4:8"]]
+ 004eea14 ["CALL", null, ["callee:004b3508:8"]]
- 004ee9d4 bytes bd12ff97
+ 004eea14 bytes bd12ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5de79d5c01a5341edbdf7011182d4b1"></a>

### [`004eeca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004eeca0.md) → [`004eece0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004eece0.md) _ZN5Botan16PK_Encryptor_EMEC2ERKNS_10Public_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS6_11char_traitsIcEENS6_9allocatorI

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58dd0.md) · 呼出先 7件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md)
- 新版 呼出元 1件 [`00c591d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c591d0.md) · 呼出先 7件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c57f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004eed18",
      "incomplete_value": true,
      "site": "004eed18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004eecd8",
      "incomplete_value": true,
      "site": "004eecd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004eedc8",
      "incomplete_value": false,
      "site": "004eedd4",
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
            "const:e02:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004eed88",
      "incomplete_value": false,
      "site": "004eed94",
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
            "const:dc2:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004eedf4",
      "incomplete_value": false,
      "site": "004eedfc",
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
            "const:d68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004eedb4",
      "incomplete_value": false,
      "site": "004eedbc",
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
      "004eed08",
      "READ",
      [
        "storage",
        "00c9ac08",
        null,
        "pointer"
      ]
    ],
    [
      "004eed18",
      "DATA",
      [
        "storage",
        "00c66b78",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004eedc8",
      "PARAM",
      [
        "storage",
        "002bfdc2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004eed08",
      "READ",
      [
        "storage",
        "00c9b008",
        null,
        "pointer"
      ]
    ],
    [
      "004eed18",
      "DATA",
      [
        "storage",
        "00c66f78",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004eedc8",
      "PARAM",
      [
        "storage",
        "002bfe02",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004eed18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004eeca0.md#insn-004eed18) · [`004eed94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004eeca0.md#insn-004eed94) · [`004eedbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004eeca0.md#insn-004eedbc)
- 新版 [`004eed58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004eece0.md#insn-004eed58) · [`004eedd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004eece0.md#insn-004eedd4) · [`004eedfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004eece0.md#insn-004eedfc)

~~~diff
- 004eed18 ["COPY", "register:0:8", ["register:4040:8"]]
- 004eed18 ["INT_ADD", "register:40f0:8", ["const:4eed18:8", "const:4:8"]]
- 004eed18 ["CALLIND", null, ["register:0:8"]]
+ 004eed58 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004eed58 ["INT_ADD", "register:40f0:8", ["const:4eed58:8", "const:4:8"]]
+ 004eed58 ["CALLIND", null, ["register:0:8"]]
- 004eed18 bytes 00013fd6
+ 004eed58 bytes 00013fd6
- 004eed94 ["INT_ADD", "register:40f0:8", ["const:4eed94:8", "const:4:8"]]
- 004eed94 ["CALL", null, ["callee:00c57f60:8"]]
+ 004eedd4 ["INT_ADD", "register:40f0:8", ["const:4eedd4:8", "const:4:8"]]
+ 004eedd4 ["CALL", null, ["callee:00c57f60:8"]]
- 004eed94 bytes 73a31d94
+ 004eedd4 bytes 63a41d94
- 004eedbc ["INT_ADD", "register:40f0:8", ["const:4eedbc:8", "const:4:8"]]
- 004eedbc ["CALL", null, ["callee:00c57f70:8"]]
+ 004eedfc ["INT_ADD", "register:40f0:8", ["const:4eedfc:8", "const:4:8"]]
+ 004eedfc ["CALL", null, ["callee:00c57f70:8"]]
- 004eedbc bytes 6da31d94
+ 004eedfc bytes 5da41d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1b2b212d4ece9099d277974053acf10"></a>

### [`004ef05c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ef/004ef05c.md) → [`004ef09c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ef/004ef09c.md) _ZN5Botan16PK_Decryptor_EMEC1ERKNS_11Private_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS6_11char_traitsIcEENS6_9allocator

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58de0.md) · 呼出先 7件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md)
- 新版 呼出元 1件 [`00c591e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c591e0.md) · 呼出先 7件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c57f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ef0d4",
      "incomplete_value": true,
      "site": "004ef0d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004ef094",
      "incomplete_value": true,
      "site": "004ef094",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004ef18c",
      "incomplete_value": false,
      "site": "004ef198",
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
            "const:e02:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ef14c",
      "incomplete_value": false,
      "site": "004ef158",
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
            "const:dc2:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ef1b8",
      "incomplete_value": false,
      "site": "004ef1c0",
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
            "const:b1d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ef178",
      "incomplete_value": false,
      "site": "004ef180",
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
      "004ef0c4",
      "READ",
      [
        "storage",
        "00c9ac10",
        null,
        "pointer"
      ]
    ],
    [
      "004ef0d4",
      "DATA",
      [
        "storage",
        "00c66ba8",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004ef18c",
      "PARAM",
      [
        "storage",
        "002bfdc2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004ef0c4",
      "READ",
      [
        "storage",
        "00c9b010",
        null,
        "pointer"
      ]
    ],
    [
      "004ef0d4",
      "DATA",
      [
        "storage",
        "00c66fa8",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004ef18c",
      "PARAM",
      [
        "storage",
        "002bfe02",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ef0d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ef/004ef05c.md#insn-004ef0d4) · [`004ef158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ef/004ef05c.md#insn-004ef158) · [`004ef180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ef/004ef05c.md#insn-004ef180)
- 新版 [`004ef114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ef/004ef09c.md#insn-004ef114) · [`004ef198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ef/004ef09c.md#insn-004ef198) · [`004ef1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ef/004ef09c.md#insn-004ef1c0)

~~~diff
- 004ef0d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 004ef0d4 ["INT_ADD", "register:40f0:8", ["const:4ef0d4:8", "const:4:8"]]
- 004ef0d4 ["CALLIND", null, ["register:0:8"]]
+ 004ef114 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004ef114 ["INT_ADD", "register:40f0:8", ["const:4ef114:8", "const:4:8"]]
+ 004ef114 ["CALLIND", null, ["register:0:8"]]
- 004ef0d4 bytes 00013fd6
+ 004ef114 bytes 00013fd6
- 004ef158 ["INT_ADD", "register:40f0:8", ["const:4ef158:8", "const:4:8"]]
- 004ef158 ["CALL", null, ["callee:00c57f60:8"]]
+ 004ef198 ["INT_ADD", "register:40f0:8", ["const:4ef198:8", "const:4:8"]]
+ 004ef198 ["CALL", null, ["callee:00c57f60:8"]]
- 004ef158 bytes 82a21d94
+ 004ef198 bytes 72a31d94
- 004ef180 ["INT_ADD", "register:40f0:8", ["const:4ef180:8", "const:4:8"]]
- 004ef180 ["CALL", null, ["callee:00c57f70:8"]]
+ 004ef1c0 ["INT_ADD", "register:40f0:8", ["const:4ef1c0:8", "const:4:8"]]
+ 004ef1c0 ["CALL", null, ["callee:00c57f70:8"]]
- 004ef180 bytes 7ca21d94
+ 004ef1c0 bytes 6ca31d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d0133115dcd23d67c6199a106c246a8"></a>

### [`004ef2f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ef/004ef2f4.md) → [`004ef334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ef/004ef334.md) _ZN5Botan16PK_KEM_EncryptorC2ERKNS_10Public_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS6_11char_traitsIcEENS6_9allocatorI

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c57f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.70% / 新版 96.70%

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
      "definition_site": "004ef410",
      "incomplete_value": false,
      "site": "004ef41c",
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
            "const:e02:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ef3d0",
      "incomplete_value": false,
      "site": "004ef3dc",
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
            "const:dc2:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ef43c",
      "incomplete_value": false,
      "site": "004ef444",
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
            "const:afc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ef3fc",
      "incomplete_value": false,
      "site": "004ef404",
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ef48c",
      "incomplete_value": true,
      "site": "004ef498",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ef44c",
      "incomplete_value": true,
      "site": "004ef458",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004ef410",
      "PARAM",
      [
        "storage",
        "002bfdc2",
        null,
        "string"
      ]
    ],
    [
      "004ef43c",
      "PARAM",
      [
        "storage",
        "002b3abc",
        null,
        "string"
      ]
    ],
    [
      "004ef488",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004ef410",
      "PARAM",
      [
        "storage",
        "002bfe02",
        null,
        "string"
      ]
    ],
    [
      "004ef43c",
      "PARAM",
      [
        "storage",
        "002b3afc",
        null,
        "string"
      ]
    ],
    [
      "004ef488",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ef3dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ef/004ef2f4.md#insn-004ef3dc) · [`004ef404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ef/004ef2f4.md#insn-004ef404) · [`004ef458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ef/004ef2f4.md#insn-004ef458)
- 新版 [`004ef41c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ef/004ef334.md#insn-004ef41c) · [`004ef444`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ef/004ef334.md#insn-004ef444) · [`004ef498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ef/004ef334.md#insn-004ef498)

~~~diff
- 004ef3dc ["INT_ADD", "register:40f0:8", ["const:4ef3dc:8", "const:4:8"]]
- 004ef3dc ["CALL", null, ["callee:00c57f60:8"]]
+ 004ef41c ["INT_ADD", "register:40f0:8", ["const:4ef41c:8", "const:4:8"]]
+ 004ef41c ["CALL", null, ["callee:00c57f60:8"]]
- 004ef3dc bytes e1a11d94
+ 004ef41c bytes d1a21d94
- 004ef404 ["INT_ADD", "register:40f0:8", ["const:4ef404:8", "const:4:8"]]
- 004ef404 ["CALL", null, ["callee:00c57f70:8"]]
+ 004ef444 ["INT_ADD", "register:40f0:8", ["const:4ef444:8", "const:4:8"]]
+ 004ef444 ["CALL", null, ["callee:00c57f70:8"]]
- 004ef404 bytes dba11d94
+ 004ef444 bytes cba21d94
- 004ef458 ["INT_ADD", "register:40f0:8", ["const:4ef458:8", "const:4:8"]]
- 004ef458 ["CALL", null, ["callee:00c57f10:8"]]
+ 004ef498 ["INT_ADD", "register:40f0:8", ["const:4ef498:8", "const:4:8"]]
+ 004ef498 ["CALL", null, ["callee:00c57f10:8"]]
- 004ef458 bytes aea11d94
+ 004ef498 bytes 9ea21d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0955f062bd090e6b223ba1f73767e1df"></a>

### [`004ef554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ef/004ef554.md) → [`004ef594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ef/004ef594.md) _ZN5Botan16PK_KEM_DecryptorC1ERKNS_11Private_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS6_11char_traitsIcEENS6_9allocator

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c57f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.77% / 新版 96.77%

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
      "definition_site": "004ef678",
      "incomplete_value": false,
      "site": "004ef684",
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
            "const:e02:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ef638",
      "incomplete_value": false,
      "site": "004ef644",
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
            "const:dc2:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ef6a4",
      "incomplete_value": false,
      "site": "004ef6ac",
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
            "const:293:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ef664",
      "incomplete_value": false,
      "site": "004ef66c",
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ef6f4",
      "incomplete_value": true,
      "site": "004ef700",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ef6b4",
      "incomplete_value": true,
      "site": "004ef6c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004ef678",
      "PARAM",
      [
        "storage",
        "002bfdc2",
        null,
        "string"
      ]
    ],
    [
      "004ef6a4",
      "PARAM",
      [
        "storage",
        "002ba253",
        null,
        "string"
      ]
    ],
    [
      "004ef6f0",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004ef678",
      "PARAM",
      [
        "storage",
        "002bfe02",
        null,
        "string"
      ]
    ],
    [
      "004ef6a4",
      "PARAM",
      [
        "storage",
        "002ba293",
        null,
        "string"
      ]
    ],
    [
      "004ef6f0",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ef644`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ef/004ef554.md#insn-004ef644) · [`004ef66c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ef/004ef554.md#insn-004ef66c) · [`004ef6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ef/004ef554.md#insn-004ef6c0)
- 新版 [`004ef684`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ef/004ef594.md#insn-004ef684) · [`004ef6ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ef/004ef594.md#insn-004ef6ac) · [`004ef700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ef/004ef594.md#insn-004ef700)

~~~diff
- 004ef644 ["INT_ADD", "register:40f0:8", ["const:4ef644:8", "const:4:8"]]
- 004ef644 ["CALL", null, ["callee:00c57f60:8"]]
+ 004ef684 ["INT_ADD", "register:40f0:8", ["const:4ef684:8", "const:4:8"]]
+ 004ef684 ["CALL", null, ["callee:00c57f60:8"]]
- 004ef644 bytes 47a11d94
+ 004ef684 bytes 37a21d94
- 004ef66c ["INT_ADD", "register:40f0:8", ["const:4ef66c:8", "const:4:8"]]
- 004ef66c ["CALL", null, ["callee:00c57f70:8"]]
+ 004ef6ac ["INT_ADD", "register:40f0:8", ["const:4ef6ac:8", "const:4:8"]]
+ 004ef6ac ["CALL", null, ["callee:00c57f70:8"]]
- 004ef66c bytes 41a11d94
+ 004ef6ac bytes 31a21d94
- 004ef6c0 ["INT_ADD", "register:40f0:8", ["const:4ef6c0:8", "const:4:8"]]
- 004ef6c0 ["CALL", null, ["callee:00c57f10:8"]]
+ 004ef700 ["INT_ADD", "register:40f0:8", ["const:4ef700:8", "const:4:8"]]
+ 004ef700 ["CALL", null, ["callee:00c57f10:8"]]
- 004ef6c0 bytes 14a11d94
+ 004ef700 bytes 04a21d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-922b5965b078f2aebdb46afca0de864a"></a>

### [`004ef7bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ef/004ef7bc.md) → [`004ef7fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ef/004ef7fc.md) _ZN5Botan16PK_Key_AgreementC2ERKNS_11Private_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS6_11char_traitsIcEENS6_9allocator

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c57f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.77% / 新版 96.77%

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
      "definition_site": "004ef8e0",
      "incomplete_value": false,
      "site": "004ef8ec",
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
            "const:e02:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ef8a0",
      "incomplete_value": false,
      "site": "004ef8ac",
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
            "const:dc2:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ef90c",
      "incomplete_value": false,
      "site": "004ef914",
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
            "const:79:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ef8cc",
      "incomplete_value": false,
      "site": "004ef8d4",
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ef95c",
      "incomplete_value": true,
      "site": "004ef968",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ef91c",
      "incomplete_value": true,
      "site": "004ef928",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004ef8e0",
      "PARAM",
      [
        "storage",
        "002bfdc2",
        null,
        "string"
      ]
    ],
    [
      "004ef90c",
      "PARAM",
      [
        "storage",
        "0029ffac",
        null,
        "string"
      ]
    ],
    [
      "004ef958",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004ef8e0",
      "PARAM",
      [
        "storage",
        "002bfe02",
        null,
        "string"
      ]
    ],
    [
      "004ef90c",
      "PARAM",
      [
        "storage",
        "002a0079",
        null,
        "string"
      ]
    ],
    [
      "004ef958",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ef8ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ef/004ef7bc.md#insn-004ef8ac) · [`004ef8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ef/004ef7bc.md#insn-004ef8d4) · [`004ef928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ef/004ef7bc.md#insn-004ef928)
- 新版 [`004ef8ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ef/004ef7fc.md#insn-004ef8ec) · [`004ef914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ef/004ef7fc.md#insn-004ef914) · [`004ef968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ef/004ef7fc.md#insn-004ef968)

~~~diff
- 004ef8ac ["INT_ADD", "register:40f0:8", ["const:4ef8ac:8", "const:4:8"]]
- 004ef8ac ["CALL", null, ["callee:00c57f60:8"]]
+ 004ef8ec ["INT_ADD", "register:40f0:8", ["const:4ef8ec:8", "const:4:8"]]
+ 004ef8ec ["CALL", null, ["callee:00c57f60:8"]]
- 004ef8ac bytes ada01d94
+ 004ef8ec bytes 9da11d94
- 004ef8d4 ["INT_ADD", "register:40f0:8", ["const:4ef8d4:8", "const:4:8"]]
- 004ef8d4 ["CALL", null, ["callee:00c57f70:8"]]
+ 004ef914 ["INT_ADD", "register:40f0:8", ["const:4ef914:8", "const:4:8"]]
+ 004ef914 ["CALL", null, ["callee:00c57f70:8"]]
- 004ef8d4 bytes a7a01d94
+ 004ef914 bytes 97a11d94
- 004ef928 ["INT_ADD", "register:40f0:8", ["const:4ef928:8", "const:4:8"]]
- 004ef928 ["CALL", null, ["callee:00c57f10:8"]]
+ 004ef968 ["INT_ADD", "register:40f0:8", ["const:4ef968:8", "const:4:8"]]
+ 004ef968 ["CALL", null, ["callee:00c57f10:8"]]
- 004ef928 bytes 7aa01d94
+ 004ef968 bytes 6aa11d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12fafb445331b6ce1a8df5e17e56883f"></a>

### [`004efb38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ef/004efb38.md) → [`004efb78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ef/004efb78.md) _ZN5Botan9PK_SignerC1ERKNS_11Private_KeyERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS6_11char_traitsIcEENS6_9allocatorIcEEEENS

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58e30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58e30.md) · 呼出先 7件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md)
- 新版 呼出元 1件 [`00c59230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59230.md) · 呼出先 7件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c57f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.25% / 新版 97.25%

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
      "definition_site": "004efc9c",
      "incomplete_value": false,
      "site": "004efca8",
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
            "const:e02:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004efc5c",
      "incomplete_value": false,
      "site": "004efc68",
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
            "const:dc2:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004efcc8",
      "incomplete_value": false,
      "site": "004efcd0",
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
            "const:d85:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004efc88",
      "incomplete_value": false,
      "site": "004efc90",
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
            "const:d45:8"
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
      "definition_site": "004efd18",
      "incomplete_value": true,
      "site": "004efd24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004efcd8",
      "incomplete_value": true,
      "site": "004efce4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004efc9c",
      "PARAM",
      [
        "storage",
        "002bfdc2",
        null,
        "string"
      ]
    ],
    [
      "004efcc8",
      "PARAM",
      [
        "storage",
        "002bed45",
        null,
        "string"
      ]
    ],
    [
      "004efd14",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004efc9c",
      "PARAM",
      [
        "storage",
        "002bfe02",
        null,
        "string"
      ]
    ],
    [
      "004efcc8",
      "PARAM",
      [
        "storage",
        "002bed85",
        null,
        "string"
      ]
    ],
    [
      "004efd14",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004efc68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ef/004efb38.md#insn-004efc68) · [`004efc90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ef/004efb38.md#insn-004efc90) · [`004efce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ef/004efb38.md#insn-004efce4)
- 新版 [`004efca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ef/004efb78.md#insn-004efca8) · [`004efcd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ef/004efb78.md#insn-004efcd0) · [`004efd24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ef/004efb78.md#insn-004efd24)

~~~diff
- 004efc68 ["INT_ADD", "register:40f0:8", ["const:4efc68:8", "const:4:8"]]
- 004efc68 ["CALL", null, ["callee:00c57f60:8"]]
+ 004efca8 ["INT_ADD", "register:40f0:8", ["const:4efca8:8", "const:4:8"]]
+ 004efca8 ["CALL", null, ["callee:00c57f60:8"]]
- 004efc68 bytes be9f1d94
+ 004efca8 bytes aea01d94
- 004efc90 ["INT_ADD", "register:40f0:8", ["const:4efc90:8", "const:4:8"]]
- 004efc90 ["CALL", null, ["callee:00c57f70:8"]]
+ 004efcd0 ["INT_ADD", "register:40f0:8", ["const:4efcd0:8", "const:4:8"]]
+ 004efcd0 ["CALL", null, ["callee:00c57f70:8"]]
- 004efc90 bytes b89f1d94
+ 004efcd0 bytes a8a01d94
- 004efce4 ["INT_ADD", "register:40f0:8", ["const:4efce4:8", "const:4:8"]]
- 004efce4 ["CALL", null, ["callee:00c57f10:8"]]
+ 004efd24 ["INT_ADD", "register:40f0:8", ["const:4efd24:8", "const:4:8"]]
+ 004efd24 ["CALL", null, ["callee:00c57f10:8"]]
- 004efce4 bytes 8b9f1d94
+ 004efd24 bytes 7ba01d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc5c4fe9118f7bef15087059789b04b9"></a>

### [`004efde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ef/004efde4.md) → [`004efe24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ef/004efe24.md) _ZN5Botan9PK_Signer9signatureERNS_21RandomNumberGeneratorE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58e50.md) · 呼出先 21件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`004a6d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6d70.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00535b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b40.md)
- 新版 呼出元 1件 [`00c59250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59250.md) · 呼出先 21件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`004a6db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6db0.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00535b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b80.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.84% / 新版 97.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 1件

アドレスに依存する影響 `call_argument_candidate` 2件, `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004efeec",
      "incomplete_value": true,
      "site": "004efeec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004efeac",
      "incomplete_value": true,
      "site": "004efeac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f00c8",
      "incomplete_value": true,
      "site": "004f00c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f0088",
      "incomplete_value": true,
      "site": "004f0088",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 16,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f012c",
      "incomplete_value": true,
      "site": "004f012c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f00ec",
      "incomplete_value": true,
      "site": "004f00ec",
      "value": [
        "LOAD",
        "8",
        [
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
      "004efedc",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004f00b8",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004f011c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004efedc",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004f00b8",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004f011c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004efeac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ef/004efde4.md#insn-004efeac) · [`004f0088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ef/004efde4.md#insn-004f0088) · [`004f00ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ef/004efde4.md#insn-004f00ec)
- 新版 [`004efeec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ef/004efe24.md#insn-004efeec) · [`004f00c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ef/004efe24.md#insn-004f00c8) · [`004f012c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ef/004efe24.md#insn-004f012c)

~~~diff
- 004efeac ["COPY", "register:0:8", ["register:4048:8"]]
- 004efeac ["INT_ADD", "register:40f0:8", ["const:4efeac:8", "const:4:8"]]
- 004efeac ["CALLIND", null, ["register:0:8"]]
+ 004efeec ["COPY", "register:0:8", ["register:4048:8"]]
+ 004efeec ["INT_ADD", "register:40f0:8", ["const:4efeec:8", "const:4:8"]]
+ 004efeec ["CALLIND", null, ["register:0:8"]]
- 004efeac bytes 20013fd6
+ 004efeec bytes 20013fd6
- 004f0088 ["COPY", "register:0:8", ["register:4048:8"]]
- 004f0088 ["INT_ADD", "register:40f0:8", ["const:4f0088:8", "const:4:8"]]
- 004f0088 ["CALLIND", null, ["register:0:8"]]
+ 004f00c8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f00c8 ["INT_ADD", "register:40f0:8", ["const:4f00c8:8", "const:4:8"]]
+ 004f00c8 ["CALLIND", null, ["register:0:8"]]
- 004f0088 bytes 20013fd6
+ 004f00c8 bytes 20013fd6
- 004f00ec ["COPY", "register:0:8", ["register:4048:8"]]
- 004f00ec ["INT_ADD", "register:40f0:8", ["const:4f00ec:8", "const:4:8"]]
- 004f00ec ["CALLIND", null, ["register:0:8"]]
+ 004f012c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f012c ["INT_ADD", "register:40f0:8", ["const:4f012c:8", "const:4:8"]]
+ 004f012c ["CALLIND", null, ["register:0:8"]]
- 004f00ec bytes 20013fd6
+ 004f012c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4d161a3b56d4ab0ccebad5fd4abaa1b"></a>

### [`004f0324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0324.md) → [`004f0364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f0/004f0364.md) _ZN5Botan11PK_VerifierC2ERKNS_10Public_KeyERKNSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEENS_16Signature_FormatESC_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58e40.md) · 呼出先 7件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md)
- 新版 呼出元 1件 [`00c59240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59240.md) · 呼出先 7件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c57f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.06% / 新版 97.06%

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
      "definition_site": "004f046c",
      "incomplete_value": false,
      "site": "004f0478",
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
            "const:e02:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f042c",
      "incomplete_value": false,
      "site": "004f0438",
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
            "const:dc2:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f0498",
      "incomplete_value": false,
      "site": "004f04a0",
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
            "const:14c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f0458",
      "incomplete_value": false,
      "site": "004f0460",
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
            "const:7f:8"
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
      "definition_site": "004f04e8",
      "incomplete_value": true,
      "site": "004f04f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f04a8",
      "incomplete_value": true,
      "site": "004f04b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004f046c",
      "PARAM",
      [
        "storage",
        "002bfdc2",
        null,
        "string"
      ]
    ],
    [
      "004f0498",
      "PARAM",
      [
        "storage",
        "002a107f",
        null,
        "string"
      ]
    ],
    [
      "004f04e4",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004f046c",
      "PARAM",
      [
        "storage",
        "002bfe02",
        null,
        "string"
      ]
    ],
    [
      "004f0498",
      "PARAM",
      [
        "storage",
        "002a114c",
        null,
        "string"
      ]
    ],
    [
      "004f04e4",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f0438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0324.md#insn-004f0438) · [`004f0460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0324.md#insn-004f0460) · [`004f04b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0324.md#insn-004f04b4)
- 新版 [`004f0478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f0/004f0364.md#insn-004f0478) · [`004f04a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f0/004f0364.md#insn-004f04a0) · [`004f04f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f0/004f0364.md#insn-004f04f4)

~~~diff
- 004f0438 ["INT_ADD", "register:40f0:8", ["const:4f0438:8", "const:4:8"]]
- 004f0438 ["CALL", null, ["callee:00c57f60:8"]]
+ 004f0478 ["INT_ADD", "register:40f0:8", ["const:4f0478:8", "const:4:8"]]
+ 004f0478 ["CALL", null, ["callee:00c57f60:8"]]
- 004f0438 bytes ca9d1d94
+ 004f0478 bytes ba9e1d94
- 004f0460 ["INT_ADD", "register:40f0:8", ["const:4f0460:8", "const:4:8"]]
- 004f0460 ["CALL", null, ["callee:00c57f70:8"]]
+ 004f04a0 ["INT_ADD", "register:40f0:8", ["const:4f04a0:8", "const:4:8"]]
+ 004f04a0 ["CALL", null, ["callee:00c57f70:8"]]
- 004f0460 bytes c49d1d94
+ 004f04a0 bytes b49e1d94
- 004f04b4 ["INT_ADD", "register:40f0:8", ["const:4f04b4:8", "const:4:8"]]
- 004f04b4 ["CALL", null, ["callee:00c57f10:8"]]
+ 004f04f4 ["INT_ADD", "register:40f0:8", ["const:4f04f4:8", "const:4:8"]]
+ 004f04f4 ["CALL", null, ["callee:00c57f10:8"]]
- 004f04b4 bytes 979d1d94
+ 004f04f4 bytes 879e1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8fb2ac6e61843eb504b8712fce6e9a4a"></a>

### [`004f05a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f05a4.md) → [`004f05e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f0/004f05e4.md) _ZN5Botan11PK_Verifier16set_input_formatENS_16Signature_FormatE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
      "definition_site": "004f0650",
      "incomplete_value": false,
      "site": "004f0658",
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
            "const:1e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f0610",
      "incomplete_value": false,
      "site": "004f0618",
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
            "const:f51:8"
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
      "definition_site": "004f068c",
      "incomplete_value": true,
      "site": "004f0698",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f064c",
      "incomplete_value": true,
      "site": "004f0658",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f0688",
      "incomplete_value": false,
      "site": "004f0698",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004f0648",
      "incomplete_value": false,
      "site": "004f0658",
      "value": [
        "leaf",
        "const:535828:8"
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
      "004f0650",
      "PARAM",
      [
        "storage",
        "0029ef51",
        null,
        "string"
      ]
    ],
    [
      "004f0688",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004f068c",
      "READ",
      [
        "storage",
        "00c9a930",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004f0650",
      "PARAM",
      [
        "storage",
        "0029f01e",
        null,
        "string"
      ]
    ],
    [
      "004f0688",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004f068c",
      "READ",
      [
        "storage",
        "00c9ad30",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f0618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f05a4.md#insn-004f0618) · [`004f0658`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f05a4.md#insn-004f0658) · [`004f0604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f05a4.md#insn-004f0604)
- 新版 [`004f0658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f0/004f05e4.md#insn-004f0658) · [`004f0698`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f0/004f05e4.md#insn-004f0698) · [`004f0644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f0/004f05e4.md#insn-004f0644)

~~~diff
- 004f0618 ["INT_ADD", "register:40f0:8", ["const:4f0618:8", "const:4:8"]]
- 004f0618 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004f0658 ["INT_ADD", "register:40f0:8", ["const:4f0658:8", "const:4:8"]]
+ 004f0658 ["CALL", null, ["callee:0043ddd8:8"]]
- 004f0618 bytes e035fd97
+ 004f0658 bytes e035fd97
- 004f0658 ["INT_ADD", "register:40f0:8", ["const:4f0658:8", "const:4:8"]]
- 004f0658 ["CALL", null, ["callee:00c57f10:8"]]
+ 004f0698 ["INT_ADD", "register:40f0:8", ["const:4f0698:8", "const:4:8"]]
+ 004f0698 ["CALL", null, ["callee:00c57f10:8"]]
- 004f0658 bytes 2e9d1d94
+ 004f0698 bytes 1e9e1d94
- 004f0604 ["INT_ADD", "register:40f0:8", ["const:4f0604:8", "const:4:8"]]
- 004f0604 ["CALL", null, ["callee:00c57ef0:8"]]
+ 004f0644 ["INT_ADD", "register:40f0:8", ["const:4f0644:8", "const:4:8"]]
+ 004f0644 ["CALL", null, ["callee:00c57ef0:8"]]
- 004f0604 bytes 3b9d1d94
+ 004f0644 bytes 2b9e1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73f6a99b557e69d27dd044fe64c027cb"></a>

### [`004f0704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0704.md) → [`004f0744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f0/004f0744.md) _ZN5Botan11PK_Verifier15check_signatureEPKhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58e60.md) · 呼出先 16件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`004f0b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0b40.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00c59260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59260.md) · 呼出先 16件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md) [`004f0b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f0/004f0b80.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.72% / 新版 93.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 4件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f0868",
      "incomplete_value": true,
      "site": "004f0868",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f0828",
      "incomplete_value": true,
      "site": "004f0828",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 9,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f0894",
      "incomplete_value": true,
      "site": "004f0894",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f0854",
      "incomplete_value": true,
      "site": "004f0854",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 11,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f08fc",
      "incomplete_value": true,
      "site": "004f08fc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f08bc",
      "incomplete_value": true,
      "site": "004f08bc",
      "value": [
        "LOAD",
        "8",
        [
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
      "004f0858",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004f0884",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004f08ec",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004f0858",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004f0884",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004f08ec",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f07e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0704.md#insn-004f07e8) · [`004f0828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0704.md#insn-004f0828) · [`004f0854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0704.md#insn-004f0854)
- 新版 [`004f0828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f0/004f0744.md#insn-004f0828) · [`004f0868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f0/004f0744.md#insn-004f0868) · [`004f0894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f0/004f0744.md#insn-004f0894)

~~~diff
- 004f07e8 ["INT_ADD", "register:40f0:8", ["const:4f07e8:8", "const:4:8"]]
- 004f07e8 ["CALL", null, ["callee:004b3508:8"]]
+ 004f0828 ["INT_ADD", "register:40f0:8", ["const:4f0828:8", "const:4:8"]]
+ 004f0828 ["CALL", null, ["callee:004b3508:8"]]
- 004f07e8 bytes 380bff97
+ 004f0828 bytes 380bff97
- 004f0828 ["COPY", "register:0:8", ["register:4048:8"]]
- 004f0828 ["INT_ADD", "register:40f0:8", ["const:4f0828:8", "const:4:8"]]
- 004f0828 ["CALLIND", null, ["register:0:8"]]
+ 004f0868 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f0868 ["INT_ADD", "register:40f0:8", ["const:4f0868:8", "const:4:8"]]
+ 004f0868 ["CALLIND", null, ["register:0:8"]]
- 004f0828 bytes 20013fd6
+ 004f0868 bytes 20013fd6
- 004f0854 ["COPY", "register:0:8", ["register:4048:8"]]
- 004f0854 ["INT_ADD", "register:40f0:8", ["const:4f0854:8", "const:4:8"]]
- 004f0854 ["CALLIND", null, ["register:0:8"]]
+ 004f0894 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f0894 ["INT_ADD", "register:40f0:8", ["const:4f0894:8", "const:4:8"]]
+ 004f0894 ["CALLIND", null, ["register:0:8"]]
- 004f0854 bytes 20013fd6
+ 004f0894 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0687bf58081ba5eb1391172c2329e457"></a>

### [`004f0c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0c68.md) → [`004f0ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f0/004f0ca8.md) _ZN5Botan14if_work_factorEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58040.md) [`00c592b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c592b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58440.md) [`00c596b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c596b0.md)

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "004f0cfc",
      "incomplete_value": true,
      "site": "004f0d08",
      "value": [
        "TRUNC",
        "8",
        [
          [
            "FLOAT_ADD",
            "8",
            [
              "LOAD",
              "FLOAT_MULT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f0cbc",
      "incomplete_value": true,
      "site": "004f0cc8",
      "value": [
        "TRUNC",
        "8",
        [
          [
            "FLOAT_ADD",
            "8",
            [
              "LOAD",
              "FLOAT_MULT"
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
      "004f0cbc",
      "READ",
      [
        "storage",
        "002c4318",
        null,
        "undefined8"
      ]
    ],
    [
      "004f0ce8",
      "READ",
      [
        "storage",
        "002c3ea0",
        null,
        "undefined8"
      ]
    ],
    [
      "004f0cf4",
      "READ",
      [
        "storage",
        "002c4348",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004f0cbc",
      "READ",
      [
        "storage",
        "002c4358",
        null,
        "undefined8"
      ]
    ],
    [
      "004f0ce8",
      "READ",
      [
        "storage",
        "002c3ee0",
        null,
        "undefined8"
      ]
    ],
    [
      "004f0cf4",
      "READ",
      [
        "storage",
        "002c4388",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f0c88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0c68.md#insn-004f0c88) · [`004f0c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0c68.md#insn-004f0c7c) · [`004f0ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0c68.md#insn-004f0ca0)
- 新版 [`004f0cc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f0/004f0ca8.md#insn-004f0cc8) · [`004f0cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f0/004f0ca8.md#insn-004f0cbc) · [`004f0ce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f0/004f0ca8.md#insn-004f0ce0)

~~~diff
- 004f0c88 ["INT_ADD", "register:40f0:8", ["const:4f0c88:8", "const:4:8"]]
- 004f0c88 ["CALL", null, ["callee:00c596b0:8"]]
+ 004f0cc8 ["INT_ADD", "register:40f0:8", ["const:4f0cc8:8", "const:4:8"]]
+ 004f0cc8 ["CALL", null, ["callee:00c596b0:8"]]
- 004f0c88 bytes 8aa11d94
+ 004f0cc8 bytes 7aa21d94
- 004f0c7c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:318:8"]]
- 004f0c7c ["LOAD", "register:5120:8", ["const:1b1:8", "tmp:0:8"]]
- 004f0c7c ["COPY", "register:5128:8", ["const:0:8"]]
- 004f0c7c ["COPY", "register:5130:8", ["const:0:8"]]
+ 004f0cbc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:358:8"]]
+ 004f0cbc ["LOAD", "register:5120:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f0cbc ["COPY", "register:5128:8", ["const:0:8"]]
+ 004f0cbc ["COPY", "register:5130:8", ["const:0:8"]]
- 004f0c7c bytes 098d41fd
+ 004f0cbc bytes 09ad41fd
- 004f0ca0 ["INT_ADD", "register:40f0:8", ["const:4f0ca0:8", "const:4:8"]]
- 004f0ca0 ["CALL", null, ["callee:00c58440:8"]]
+ 004f0ce0 ["INT_ADD", "register:40f0:8", ["const:4f0ce0:8", "const:4:8"]]
+ 004f0ce0 ["CALL", null, ["callee:00c58440:8"]]
- 004f0ca0 bytes e89c1d94
+ 004f0ce0 bytes d89d1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d17c4495b3a5ac79b9d8da04d661b0e"></a>

### [`004f0ccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0ccc.md) → [`004f0d0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f0/004f0d0c.md) _ZN5Botan14dl_work_factorEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58040.md) [`00c592b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c592b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58440.md) [`00c596b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c596b0.md)

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "004f0d60",
      "incomplete_value": true,
      "site": "004f0d6c",
      "value": [
        "TRUNC",
        "8",
        [
          [
            "FLOAT_ADD",
            "8",
            [
              "LOAD",
              "FLOAT_MULT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f0d20",
      "incomplete_value": true,
      "site": "004f0d2c",
      "value": [
        "TRUNC",
        "8",
        [
          [
            "FLOAT_ADD",
            "8",
            [
              "LOAD",
              "FLOAT_MULT"
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
      "004f0d20",
      "READ",
      [
        "storage",
        "002c4318",
        null,
        "undefined8"
      ]
    ],
    [
      "004f0d4c",
      "READ",
      [
        "storage",
        "002c3ea0",
        null,
        "undefined8"
      ]
    ],
    [
      "004f0d58",
      "READ",
      [
        "storage",
        "002c4348",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004f0d20",
      "READ",
      [
        "storage",
        "002c4358",
        null,
        "undefined8"
      ]
    ],
    [
      "004f0d4c",
      "READ",
      [
        "storage",
        "002c3ee0",
        null,
        "undefined8"
      ]
    ],
    [
      "004f0d58",
      "READ",
      [
        "storage",
        "002c4388",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f0cec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0ccc.md#insn-004f0cec) · [`004f0ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0ccc.md#insn-004f0ce0) · [`004f0d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0ccc.md#insn-004f0d04)
- 新版 [`004f0d2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f0/004f0d0c.md#insn-004f0d2c) · [`004f0d20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f0/004f0d0c.md#insn-004f0d20) · [`004f0d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f0/004f0d0c.md#insn-004f0d44)

~~~diff
- 004f0cec ["INT_ADD", "register:40f0:8", ["const:4f0cec:8", "const:4:8"]]
- 004f0cec ["CALL", null, ["callee:00c596b0:8"]]
+ 004f0d2c ["INT_ADD", "register:40f0:8", ["const:4f0d2c:8", "const:4:8"]]
+ 004f0d2c ["CALL", null, ["callee:00c596b0:8"]]
- 004f0cec bytes 71a11d94
+ 004f0d2c bytes 61a21d94
- 004f0ce0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:318:8"]]
- 004f0ce0 ["LOAD", "register:5120:8", ["const:1b1:8", "tmp:0:8"]]
- 004f0ce0 ["COPY", "register:5128:8", ["const:0:8"]]
- 004f0ce0 ["COPY", "register:5130:8", ["const:0:8"]]
+ 004f0d20 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:358:8"]]
+ 004f0d20 ["LOAD", "register:5120:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f0d20 ["COPY", "register:5128:8", ["const:0:8"]]
+ 004f0d20 ["COPY", "register:5130:8", ["const:0:8"]]
- 004f0ce0 bytes 098d41fd
+ 004f0d20 bytes 09ad41fd
- 004f0d04 ["INT_ADD", "register:40f0:8", ["const:4f0d04:8", "const:4:8"]]
- 004f0d04 ["CALL", null, ["callee:00c58440:8"]]
+ 004f0d44 ["INT_ADD", "register:40f0:8", ["const:4f0d44:8", "const:4:8"]]
+ 004f0d44 ["CALL", null, ["callee:00c58440:8"]]
- 004f0d04 bytes cf9c1d94
+ 004f0d44 bytes bf9d1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39a8c2e85b5843bbd0e15d51580a6cb8"></a>

### [`004f0db8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0db8.md) → [`004f0df8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f0/004f0df8.md) _ZN5Botan4X50910PEM_encodeERKNS_10Public_KeyE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c592c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c592c0.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59090.md) [`00c591d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c591d0.md)
- 新版 呼出元 1件 [`00c596c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c596c0.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59490.md) [`00c595d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c595d0.md)

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
      "definition_site": "004f0e48",
      "incomplete_value": true,
      "site": "004f0e48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e0c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f0e08",
      "incomplete_value": true,
      "site": "004f0e08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dcc:8"
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
      "004f0e34",
      "READ",
      [
        "storage",
        "002bfdcc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004f0e34",
      "READ",
      [
        "storage",
        "002bfe0c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f0ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0db8.md#insn-004f0ddc) · [`004f0de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0db8.md#insn-004f0de8) · [`004f0e18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0db8.md#insn-004f0e18)
- 新版 [`004f0e1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f0/004f0df8.md#insn-004f0e1c) · [`004f0e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f0/004f0df8.md#insn-004f0e28) · [`004f0e58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f0/004f0df8.md#insn-004f0e58)

~~~diff
- 004f0ddc ["INT_ADD", "register:40f0:8", ["const:4f0ddc:8", "const:4:8"]]
- 004f0ddc ["CALL", null, ["callee:00c595d0:8"]]
+ 004f0e1c ["INT_ADD", "register:40f0:8", ["const:4f0e1c:8", "const:4:8"]]
+ 004f0e1c ["CALL", null, ["callee:00c595d0:8"]]
- 004f0ddc bytes fda01d94
+ 004f0e1c bytes eda11d94
- 004f0de8 ["COPY", "tmp:0:8", ["const:dcc:8"]]
- 004f0de8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004f0de8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004f0de8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004f0e28 ["COPY", "tmp:0:8", ["const:e0c:8"]]
+ 004f0e28 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004f0e28 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004f0e28 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004f0de8 bytes 29313791
+ 004f0e28 bytes 29313891
- 004f0e18 ["INT_ADD", "register:40f0:8", ["const:4f0e18:8", "const:4:8"]]
- 004f0e18 ["CALL", null, ["callee:00c59490:8"]]
+ 004f0e58 ["INT_ADD", "register:40f0:8", ["const:4f0e58:8", "const:4:8"]]
+ 004f0e58 ["CALL", null, ["callee:00c59490:8"]]
- 004f0e18 bytes 9ea01d94
+ 004f0e58 bytes 8ea11d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b08d7afb0d59e5729e6b3be743dce66"></a>

### [`004f0e9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0e9c.md) → [`004f0edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f0/004f0edc.md) _ZN5Botan4X5098load_keyERNS_10DataSourceE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c592d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c592d0.md) · 呼出先 20件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004a573c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a573c.md) [`004a6f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6f5c.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00540264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540264.md)
- 新版 呼出元 1件 [`00c596d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c596d0.md) · 呼出先 20件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004a577c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a577c.md) [`004a6f9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6f9c.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`005402a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005402a4.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.39% / 新版 93.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 4件, `store_value` 2件

アドレスに依存する影響 `call_argument_candidate` 1件, `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f0f10",
      "incomplete_value": true,
      "site": "004f0f10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004f0ed0",
      "incomplete_value": true,
      "site": "004f0ed0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004f0f9c",
      "incomplete_value": true,
      "site": "004f0f9c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e0c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f0f5c",
      "incomplete_value": true,
      "site": "004f0f5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dcc:8"
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
      "definition_site": "004f0fc8",
      "incomplete_value": true,
      "site": "004f0fc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004f0f88",
      "incomplete_value": true,
      "site": "004f0f88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
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
      "004f0f00",
      "READ",
      [
        "storage",
        "00c9a938",
        null,
        "pointer"
      ]
    ],
    [
      "004f0f10",
      "DATA",
      [
        "storage",
        "00c65da8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004f0f8c",
      "READ",
      [
        "storage",
        "002bfdcc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004f0f00",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "004f0f10",
      "DATA",
      [
        "storage",
        "00c661a8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004f0f8c",
      "READ",
      [
        "storage",
        "002bfe0c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f0fc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0e9c.md#insn-004f0fc4) · [`004f106c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0e9c.md#insn-004f106c) · [`004f10b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f0/004f0e9c.md#insn-004f10b0)
- 新版 [`004f1004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f0/004f0edc.md#insn-004f1004) · [`004f10ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f0/004f0edc.md#insn-004f10ac) · [`004f10f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f0/004f0edc.md#insn-004f10f0)

~~~diff
- 004f0fc4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004f0fc4 ["INT_ADD", "register:40f0:8", ["const:4f0fc4:8", "const:4:8"]]
- 004f0fc4 ["CALLIND", null, ["register:0:8"]]
+ 004f1004 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f1004 ["INT_ADD", "register:40f0:8", ["const:4f1004:8", "const:4:8"]]
+ 004f1004 ["CALLIND", null, ["register:0:8"]]
- 004f0fc4 bytes 20013fd6
+ 004f1004 bytes 20013fd6
- 004f106c ["COPY", "register:0:8", ["register:4048:8"]]
- 004f106c ["INT_ADD", "register:40f0:8", ["const:4f106c:8", "const:4:8"]]
- 004f106c ["CALLIND", null, ["register:0:8"]]
+ 004f10ac ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f10ac ["INT_ADD", "register:40f0:8", ["const:4f10ac:8", "const:4:8"]]
+ 004f10ac ["CALLIND", null, ["register:0:8"]]
- 004f106c bytes 20013fd6
+ 004f10ac bytes 20013fd6
- 004f10b0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004f10b0 ["INT_ADD", "register:40f0:8", ["const:4f10b0:8", "const:4:8"]]
- 004f10b0 ["CALLIND", null, ["register:0:8"]]
+ 004f10f0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f10f0 ["INT_ADD", "register:40f0:8", ["const:4f10f0:8", "const:4:8"]]
+ 004f10f0 ["CALLIND", null, ["register:0:8"]]
- 004f10b0 bytes 20013fd6
+ 004f10f0 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1dd509ce8b350912255fcb4d2ac2ae7"></a>

### [`004f1594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1594.md) → [`004f15d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f15d4.md) _ZN5Botan4X5098load_keyERKNSt6__ndk16vectorIhNS1_9allocatorIhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c592f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c592f0.md) · 呼出先 5件 [`00536cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/00536cc4.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c592d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c592d0.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)
- 新版 呼出元 1件 [`00c596f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c596f0.md) · 呼出先 5件 [`00536d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536d04.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c596d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c596d0.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.56% / 新版 95.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f1604",
      "incomplete_value": true,
      "site": "004f1604",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004f15c4",
      "incomplete_value": true,
      "site": "004f15c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_target",
    "new": {
      "definition_site": "004f1650",
      "incomplete_value": true,
      "site": "004f1650",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f1610",
      "incomplete_value": true,
      "site": "004f1610",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004f15f0",
      "READ",
      [
        "storage",
        "00c9a9e0",
        null,
        "pointer"
      ]
    ],
    [
      "004f1604",
      "DATA",
      [
        "storage",
        "00c66f88",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004f1640",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004f15f0",
      "READ",
      [
        "storage",
        "00c9ade0",
        null,
        "pointer"
      ]
    ],
    [
      "004f1604",
      "DATA",
      [
        "storage",
        "00c67388",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004f1640",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f1610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1594.md#insn-004f1610) · [`004f15b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1594.md#insn-004f15b0) · [`004f15d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1594.md#insn-004f15d8)
- 新版 [`004f1650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f15d4.md#insn-004f1650) · [`004f15f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f15d4.md#insn-004f15f0) · [`004f1618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f15d4.md#insn-004f1618)

~~~diff
- 004f1610 ["COPY", "register:0:8", ["register:4048:8"]]
- 004f1610 ["INT_ADD", "register:40f0:8", ["const:4f1610:8", "const:4:8"]]
- 004f1610 ["CALLIND", null, ["register:0:8"]]
+ 004f1650 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f1650 ["INT_ADD", "register:40f0:8", ["const:4f1650:8", "const:4:8"]]
+ 004f1650 ["CALLIND", null, ["register:0:8"]]
- 004f1610 bytes 20013fd6
+ 004f1650 bytes 20013fd6
- 004f15b0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9e0:8"]]
- 004f15b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f15f0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:de0:8"]]
+ 004f15f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004f15b0 bytes 08f144f9
+ 004f15f0 bytes 08f146f9
- 004f15d8 ["INT_ADD", "register:40f0:8", ["const:4f15d8:8", "const:4:8"]]
- 004f15d8 ["CALL", null, ["callee:00536d04:8"]]
+ 004f1618 ["INT_ADD", "register:40f0:8", ["const:4f1618:8", "const:4:8"]]
+ 004f1618 ["CALL", null, ["callee:00536d04:8"]]
- 004f15d8 bytes bb150194
+ 004f1618 bytes bb150194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a6990638f0444cb11cb8f54c1f62f6c"></a>

### [`004f1670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1670.md) → [`004f16b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f16b0.md) _ZN5Botan4X5098copy_keyERKNS_10Public_KeyE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c590c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c590c0.md) [`00c592c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c592c0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c594c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c594c0.md) [`00c596c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c596c0.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f1724",
      "incomplete_value": true,
      "site": "004f1724",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f16e4",
      "incomplete_value": true,
      "site": "004f16e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004f1714",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004f1714",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f16e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1670.md#insn-004f16e4) · [`004f1694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1670.md#insn-004f1694) · [`004f16a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1670.md#insn-004f16a0)
- 新版 [`004f1724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f16b0.md#insn-004f1724) · [`004f16d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f16b0.md#insn-004f16d4) · [`004f16e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f16b0.md#insn-004f16e0)

~~~diff
- 004f16e4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004f16e4 ["INT_ADD", "register:40f0:8", ["const:4f16e4:8", "const:4:8"]]
- 004f16e4 ["CALLIND", null, ["register:0:8"]]
+ 004f1724 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f1724 ["INT_ADD", "register:40f0:8", ["const:4f1724:8", "const:4:8"]]
+ 004f1724 ["CALLIND", null, ["register:0:8"]]
- 004f16e4 bytes 20013fd6
+ 004f1724 bytes 20013fd6
- 004f1694 ["INT_ADD", "register:40f0:8", ["const:4f1694:8", "const:4:8"]]
- 004f1694 ["CALL", null, ["callee:00c596c0:8"]]
+ 004f16d4 ["INT_ADD", "register:40f0:8", ["const:4f16d4:8", "const:4:8"]]
+ 004f16d4 ["CALL", null, ["callee:00c596c0:8"]]
- 004f1694 bytes 0b9f1d94
+ 004f16d4 bytes fb9f1d94
- 004f16a0 ["INT_ADD", "register:40f0:8", ["const:4f16a0:8", "const:4:8"]]
- 004f16a0 ["CALL", null, ["callee:00c594c0:8"]]
+ 004f16e0 ["INT_ADD", "register:40f0:8", ["const:4f16e0:8", "const:4:8"]]
+ 004f16e0 ["CALL", null, ["callee:00c594c0:8"]]
- 004f16a0 bytes 889e1d94
+ 004f16e0 bytes 789f1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7cab4ea3717bda73b554a45032f0473a"></a>

### [`004f1af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1af8.md) → [`004f1b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f1b38.md) _ZN5Botan21RandomNumberGenerator8make_rngEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 77.50% / 新版 77.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 4件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f1b7c",
      "incomplete_value": true,
      "site": "004f1b88",
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
                "const:1a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f1b3c",
      "incomplete_value": true,
      "site": "004f1b48",
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
                "const:160:8"
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
      "definition_site": "004f1b78",
      "incomplete_value": true,
      "site": "004f1b8c",
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
                "const:dac:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f1b38",
      "incomplete_value": true,
      "site": "004f1b4c",
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
                "const:d6c:8"
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
      "definition_site": "004f1b78",
      "incomplete_value": true,
      "site": "004f1b8c",
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
      "definition_site": "004f1b38",
      "incomplete_value": true,
      "site": "004f1b4c",
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
      "004f1b78",
      "READ",
      [
        "storage",
        "002bed6c",
        null,
        "string"
      ]
    ],
    [
      "004f1b78",
      "READ",
      [
        "storage",
        "002bed7c",
        null,
        "string"
      ]
    ],
    [
      "004f1b7c",
      "READ",
      [
        "storage",
        "002c3160",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004f1b78",
      "READ",
      [
        "storage",
        "002bedac",
        null,
        "string"
      ]
    ],
    [
      "004f1b78",
      "READ",
      [
        "storage",
        "002bedbc",
        null,
        "string"
      ]
    ],
    [
      "004f1b7c",
      "READ",
      [
        "storage",
        "002c31a0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f1b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1af8.md#insn-004f1b90) · [`004f1b1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1af8.md#insn-004f1b1c) · [`004f1b28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1af8.md#insn-004f1b28)
- 新版 [`004f1bd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f1b38.md#insn-004f1bd0) · [`004f1b5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f1b38.md#insn-004f1b5c) · [`004f1b68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f1b38.md#insn-004f1b68)

~~~diff
- 004f1b90 ["INT_ADD", "register:40f0:8", ["const:4f1b90:8", "const:4:8"]]
- 004f1b90 ["CALL", null, ["callee:00c57f10:8"]]
+ 004f1bd0 ["INT_ADD", "register:40f0:8", ["const:4f1bd0:8", "const:4:8"]]
+ 004f1bd0 ["CALL", null, ["callee:00c57f10:8"]]
- 004f1b90 bytes e0971d94
+ 004f1bd0 bytes d0981d94
- 004f1b1c ["INT_ADD", "register:40f0:8", ["const:4f1b1c:8", "const:4:8"]]
- 004f1b1c ["CALL", null, ["callee:00c57ef0:8"]]
+ 004f1b5c ["INT_ADD", "register:40f0:8", ["const:4f1b5c:8", "const:4:8"]]
+ 004f1b5c ["CALL", null, ["callee:00c57ef0:8"]]
- 004f1b1c bytes f5971d94
+ 004f1b5c bytes e5981d94
- 004f1b28 ["INT_ADD", "register:40f0:8", ["const:4f1b28:8", "const:4:8"]]
- 004f1b28 ["CALL", null, ["callee:00c57e90:8"]]
+ 004f1b68 ["INT_ADD", "register:40f0:8", ["const:4f1b68:8", "const:4:8"]]
+ 004f1b68 ["CALL", null, ["callee:00c57e90:8"]]
- 004f1b28 bytes da971d94
+ 004f1b68 bytes ca981d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e2e0db7f5baadb10756889baa2e762a"></a>

### [`004f1be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1be0.md) → [`004f1c20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f1c20.md) _ZN5Botan14Serialized_RNGC1Ev

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 73.58% / 新版 73.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 7件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f1c54",
      "incomplete_value": true,
      "site": "004f1c5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004f1c14",
      "incomplete_value": true,
      "site": "004f1c1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004f1c90",
      "incomplete_value": true,
      "site": "004f1c9c",
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
                "const:d70:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f1c50",
      "incomplete_value": true,
      "site": "004f1c5c",
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
                "const:d30:8"
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
      "definition_site": "004f1c8c",
      "incomplete_value": true,
      "site": "004f1ca0",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f1c4c",
      "incomplete_value": true,
      "site": "004f1c60",
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
                "const:20:8"
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
      "004f1c44",
      "READ",
      [
        "storage",
        "00c9ac18",
        null,
        "pointer"
      ]
    ],
    [
      "004f1c5c",
      "DATA",
      [
        "storage",
        "00c66bd0",
        null,
        "undefined1[104]"
      ]
    ],
    [
      "004f1c8c",
      "READ",
      [
        "storage",
        "002bb39b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004f1c44",
      "READ",
      [
        "storage",
        "00c9b018",
        null,
        "pointer"
      ]
    ],
    [
      "004f1c5c",
      "DATA",
      [
        "storage",
        "00c66fd0",
        null,
        "undefined1[104]"
      ]
    ],
    [
      "004f1c8c",
      "READ",
      [
        "storage",
        "002bb3db",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f1c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1be0.md#insn-004f1c9c) · [`004f1ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1be0.md#insn-004f1ca0) · [`004f1cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1be0.md#insn-004f1cac)
- 新版 [`004f1cdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f1c20.md#insn-004f1cdc) · [`004f1ce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f1c20.md#insn-004f1ce0) · [`004f1cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f1c20.md#insn-004f1cec)

~~~diff
- 004f1c9c ["COPY", "register:4010:8", ["const:535828:8"]]
+ 004f1cdc ["COPY", "register:4010:8", ["const:535868:8"]]
- 004f1c9c bytes 62dc2110
+ 004f1cdc bytes 62dc2110
- 004f1ca0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:988:8"]]
- 004f1ca0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f1ce0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d88:8"]]
+ 004f1ce0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004f1ca0 bytes 21c444f9
+ 004f1ce0 bytes 21c446f9
- 004f1cac ["INT_ADD", "register:40f0:8", ["const:4f1cac:8", "const:4:8"]]
- 004f1cac ["CALL", null, ["callee:00c57f10:8"]]
+ 004f1cec ["INT_ADD", "register:40f0:8", ["const:4f1cec:8", "const:4:8"]]
+ 004f1cec ["CALL", null, ["callee:00c57f10:8"]]
- 004f1cac bytes 99971d94
+ 004f1cec bytes 89981d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4126df79f8b1d19d39e922d2035f563a"></a>

### [`004f1e18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1e18.md) → [`004f1e58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f1e58.md) _ZNK5Botan13RSA_PublicKey18estimated_strengthEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58040.md) [`00c592b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c592b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58440.md) [`00c596b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c596b0.md)

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "004f1eb8",
      "incomplete_value": true,
      "site": "004f1ec4",
      "value": [
        "TRUNC",
        "8",
        [
          [
            "FLOAT_ADD",
            "8",
            [
              "LOAD",
              "FLOAT_MULT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f1e78",
      "incomplete_value": true,
      "site": "004f1e84",
      "value": [
        "TRUNC",
        "8",
        [
          [
            "FLOAT_ADD",
            "8",
            [
              "LOAD",
              "FLOAT_MULT"
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
      "004f1e78",
      "READ",
      [
        "storage",
        "002c4318",
        null,
        "undefined8"
      ]
    ],
    [
      "004f1ea4",
      "READ",
      [
        "storage",
        "002c3ea0",
        null,
        "undefined8"
      ]
    ],
    [
      "004f1eb0",
      "READ",
      [
        "storage",
        "002c4348",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004f1e78",
      "READ",
      [
        "storage",
        "002c4358",
        null,
        "undefined8"
      ]
    ],
    [
      "004f1ea4",
      "READ",
      [
        "storage",
        "002c3ee0",
        null,
        "undefined8"
      ]
    ],
    [
      "004f1eb0",
      "READ",
      [
        "storage",
        "002c4388",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f1e44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1e18.md#insn-004f1e44) · [`004f1e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1e18.md#insn-004f1e2c) · [`004f1e38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1e18.md#insn-004f1e38)
- 新版 [`004f1e84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f1e58.md#insn-004f1e84) · [`004f1e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f1e58.md#insn-004f1e6c) · [`004f1e78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f1e58.md#insn-004f1e78)

~~~diff
- 004f1e44 ["INT_ADD", "register:40f0:8", ["const:4f1e44:8", "const:4:8"]]
- 004f1e44 ["CALL", null, ["callee:00c596b0:8"]]
+ 004f1e84 ["INT_ADD", "register:40f0:8", ["const:4f1e84:8", "const:4:8"]]
+ 004f1e84 ["CALL", null, ["callee:00c596b0:8"]]
- 004f1e44 bytes 1b9d1d94
+ 004f1e84 bytes 0b9e1d94
- 004f1e2c ["COPY", "register:0:8", ["register:4040:8"]]
- 004f1e2c ["INT_ADD", "register:40f0:8", ["const:4f1e2c:8", "const:4:8"]]
- 004f1e2c ["CALLIND", null, ["register:0:8"]]
+ 004f1e6c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004f1e6c ["INT_ADD", "register:40f0:8", ["const:4f1e6c:8", "const:4:8"]]
+ 004f1e6c ["CALLIND", null, ["register:0:8"]]
- 004f1e2c bytes 00013fd6
+ 004f1e6c bytes 00013fd6
- 004f1e38 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:318:8"]]
- 004f1e38 ["LOAD", "register:5120:8", ["const:1b1:8", "tmp:0:8"]]
- 004f1e38 ["COPY", "register:5128:8", ["const:0:8"]]
- 004f1e38 ["COPY", "register:5130:8", ["const:0:8"]]
+ 004f1e78 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:358:8"]]
+ 004f1e78 ["LOAD", "register:5120:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f1e78 ["COPY", "register:5128:8", ["const:0:8"]]
+ 004f1e78 ["COPY", "register:5130:8", ["const:0:8"]]
- 004f1e38 bytes 098d41fd
+ 004f1e78 bytes 09ad41fd
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1208adfbf2fde3cc553ff675e2dea788"></a>

### [`004f1e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1e88.md) → [`004f1ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f1ec8.md) _ZTv0_n40_NK5Botan13RSA_PublicKey18estimated_strengthEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58040.md) [`00c592b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c592b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58440.md) [`00c596b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c596b0.md)

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "004f1f34",
      "incomplete_value": true,
      "site": "004f1f40",
      "value": [
        "TRUNC",
        "8",
        [
          [
            "FLOAT_ADD",
            "8",
            [
              "LOAD",
              "FLOAT_MULT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f1ef4",
      "incomplete_value": true,
      "site": "004f1f00",
      "value": [
        "TRUNC",
        "8",
        [
          [
            "FLOAT_ADD",
            "8",
            [
              "LOAD",
              "FLOAT_MULT"
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
      "004f1ef4",
      "READ",
      [
        "storage",
        "002c4318",
        null,
        "undefined8"
      ]
    ],
    [
      "004f1f20",
      "READ",
      [
        "storage",
        "002c3ea0",
        null,
        "undefined8"
      ]
    ],
    [
      "004f1f2c",
      "READ",
      [
        "storage",
        "002c4348",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004f1ef4",
      "READ",
      [
        "storage",
        "002c4358",
        null,
        "undefined8"
      ]
    ],
    [
      "004f1f20",
      "READ",
      [
        "storage",
        "002c3ee0",
        null,
        "undefined8"
      ]
    ],
    [
      "004f1f2c",
      "READ",
      [
        "storage",
        "002c4388",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f1ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1e88.md#insn-004f1ec0) · [`004f1ea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1e88.md#insn-004f1ea8) · [`004f1eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f1/004f1e88.md#insn-004f1eb4)
- 新版 [`004f1f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f1ec8.md#insn-004f1f00) · [`004f1ee8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f1ec8.md#insn-004f1ee8) · [`004f1ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f1/004f1ec8.md#insn-004f1ef4)

~~~diff
- 004f1ec0 ["INT_ADD", "register:40f0:8", ["const:4f1ec0:8", "const:4:8"]]
- 004f1ec0 ["CALL", null, ["callee:00c596b0:8"]]
+ 004f1f00 ["INT_ADD", "register:40f0:8", ["const:4f1f00:8", "const:4:8"]]
+ 004f1f00 ["CALL", null, ["callee:00c596b0:8"]]
- 004f1ec0 bytes fc9c1d94
+ 004f1f00 bytes ec9d1d94
- 004f1ea8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004f1ea8 ["INT_ADD", "register:40f0:8", ["const:4f1ea8:8", "const:4:8"]]
- 004f1ea8 ["CALLIND", null, ["register:0:8"]]
+ 004f1ee8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f1ee8 ["INT_ADD", "register:40f0:8", ["const:4f1ee8:8", "const:4:8"]]
+ 004f1ee8 ["CALLIND", null, ["register:0:8"]]
- 004f1ea8 bytes 20013fd6
+ 004f1ee8 bytes 20013fd6
- 004f1eb4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:318:8"]]
- 004f1eb4 ["LOAD", "register:5120:8", ["const:1b1:8", "tmp:0:8"]]
- 004f1eb4 ["COPY", "register:5128:8", ["const:0:8"]]
- 004f1eb4 ["COPY", "register:5130:8", ["const:0:8"]]
+ 004f1ef4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:358:8"]]
+ 004f1ef4 ["LOAD", "register:5120:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f1ef4 ["COPY", "register:5128:8", ["const:0:8"]]
+ 004f1ef4 ["COPY", "register:5130:8", ["const:0:8"]]
- 004f1eb4 bytes 098d41fd
+ 004f1ef4 bytes 09ad41fd
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-061854f193b559c6b1d075ec01563228"></a>

### [`004f21c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f2/004f21c0.md) → [`004f2200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f2/004f2200.md) _ZN5Botan13RSA_PublicKeyC2ERKNS_19AlgorithmIdentifierERKNSt6__ndk16vectorIhNS4_9allocatorIhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58300.md) [`00c58310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58310.md) [`00c58480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58480.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c58700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58700.md) [`00c58710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58710.md) [`00c58880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58880.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.40% / 新版 95.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f22e4",
      "incomplete_value": true,
      "site": "004f22e4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f22a4",
      "incomplete_value": true,
      "site": "004f22a4",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f2328",
      "incomplete_value": true,
      "site": "004f2328",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f22e8",
      "incomplete_value": true,
      "site": "004f22e8",
      "value": [
        "LOAD",
        "8",
        [
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
      "004f22d4",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004f2318",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004f22d4",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004f2318",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f2264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f2/004f21c0.md#insn-004f2264) · [`004f22a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f2/004f21c0.md#insn-004f22a4) · [`004f22e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f2/004f21c0.md#insn-004f22e8)
- 新版 [`004f22a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f2/004f2200.md#insn-004f22a4) · [`004f22e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f2/004f2200.md#insn-004f22e4) · [`004f2328`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f2/004f2200.md#insn-004f2328)

~~~diff
- 004f2264 ["INT_ADD", "register:40f0:8", ["const:4f2264:8", "const:4:8"]]
- 004f2264 ["CALL", null, ["callee:00c58710:8"]]
+ 004f22a4 ["INT_ADD", "register:40f0:8", ["const:4f22a4:8", "const:4:8"]]
+ 004f22a4 ["CALL", null, ["callee:00c58710:8"]]
- 004f2264 bytes 2b981d94
+ 004f22a4 bytes 1b991d94
- 004f22a4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004f22a4 ["INT_ADD", "register:40f0:8", ["const:4f22a4:8", "const:4:8"]]
- 004f22a4 ["CALLIND", null, ["register:0:8"]]
+ 004f22e4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f22e4 ["INT_ADD", "register:40f0:8", ["const:4f22e4:8", "const:4:8"]]
+ 004f22e4 ["CALLIND", null, ["register:0:8"]]
- 004f22a4 bytes 20013fd6
+ 004f22e4 bytes 20013fd6
- 004f22e8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004f22e8 ["INT_ADD", "register:40f0:8", ["const:4f22e8:8", "const:4:8"]]
- 004f22e8 ["CALLIND", null, ["register:0:8"]]
+ 004f2328 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f2328 ["INT_ADD", "register:40f0:8", ["const:4f2328:8", "const:4:8"]]
+ 004f2328 ["CALLIND", null, ["register:0:8"]]
- 004f22e8 bytes 20013fd6
+ 004f2328 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b8c52483b7391950bbc91346dcd3d73"></a>

### [`004f24cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f2/004f24cc.md) → [`004f250c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f2/004f250c.md) _ZNK5Botan14RSA_PrivateKey16private_key_bitsEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 10件 [`00535b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b40.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c582b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582b0.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00535b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c586b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586b0.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.69% / 新版 96.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f2598",
      "incomplete_value": true,
      "site": "004f2598",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f2558",
      "incomplete_value": true,
      "site": "004f2558",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f26b8",
      "incomplete_value": true,
      "site": "004f26b8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f2678",
      "incomplete_value": true,
      "site": "004f2678",
      "value": [
        "LOAD",
        "8",
        [
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
      "004f2588",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004f26a8",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004f2588",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004f26a8",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f2558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f2/004f24cc.md#insn-004f2558) · [`004f2678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f2/004f24cc.md#insn-004f2678) · [`004f2510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f2/004f24cc.md#insn-004f2510)
- 新版 [`004f2598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f2/004f250c.md#insn-004f2598) · [`004f26b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f2/004f250c.md#insn-004f26b8) · [`004f2550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f2/004f250c.md#insn-004f2550)

~~~diff
- 004f2558 ["COPY", "register:0:8", ["register:4048:8"]]
- 004f2558 ["INT_ADD", "register:40f0:8", ["const:4f2558:8", "const:4:8"]]
- 004f2558 ["CALLIND", null, ["register:0:8"]]
+ 004f2598 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f2598 ["INT_ADD", "register:40f0:8", ["const:4f2598:8", "const:4:8"]]
+ 004f2598 ["CALLIND", null, ["register:0:8"]]
- 004f2558 bytes 20013fd6
+ 004f2598 bytes 20013fd6
- 004f2678 ["COPY", "register:0:8", ["register:4048:8"]]
- 004f2678 ["INT_ADD", "register:40f0:8", ["const:4f2678:8", "const:4:8"]]
- 004f2678 ["CALLIND", null, ["register:0:8"]]
+ 004f26b8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f26b8 ["INT_ADD", "register:40f0:8", ["const:4f26b8:8", "const:4:8"]]
+ 004f26b8 ["CALLIND", null, ["register:0:8"]]
- 004f2678 bytes 20013fd6
+ 004f26b8 bytes 20013fd6
- 004f2510 ["INT_ADD", "register:40f0:8", ["const:4f2510:8", "const:4:8"]]
- 004f2510 ["CALL", null, ["callee:00c586b0:8"]]
+ 004f2550 ["INT_ADD", "register:40f0:8", ["const:4f2550:8", "const:4:8"]]
+ 004f2550 ["CALL", null, ["callee:00c586b0:8"]]
- 004f2510 bytes 68971d94
+ 004f2550 bytes 58981d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99fb51cbf261d53cdc5f91dedecef87b"></a>

### [`004f26ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f2/004f26ec.md) → [`004f272c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f2/004f272c.md) _ZN5Botan14RSA_PrivateKeyC2ERKNS_19AlgorithmIdentifierERKNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 14件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.33% / 新版 94.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 2件, `store_value` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f2868",
      "incomplete_value": true,
      "site": "004f287c",
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
                "const:2a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f2828",
      "incomplete_value": true,
      "site": "004f283c",
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
    "ordinal": 56,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f2864",
      "incomplete_value": true,
      "site": "004f2880",
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
                "const:dd6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f2824",
      "incomplete_value": true,
      "site": "004f2840",
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
                "const:d96:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 57,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f2864",
      "incomplete_value": true,
      "site": "004f2880",
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
      "definition_site": "004f2824",
      "incomplete_value": true,
      "site": "004f2840",
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
    "ordinal": 58,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004f2864",
      "READ",
      [
        "storage",
        "002b4d96",
        null,
        "string"
      ]
    ],
    [
      "004f2864",
      "READ",
      [
        "storage",
        "002b4da6",
        null,
        "string"
      ]
    ],
    [
      "004f2868",
      "READ",
      [
        "storage",
        "002c3260",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004f2864",
      "READ",
      [
        "storage",
        "002b4dd6",
        null,
        "string"
      ]
    ],
    [
      "004f2864",
      "READ",
      [
        "storage",
        "002b4de6",
        null,
        "string"
      ]
    ],
    [
      "004f2868",
      "READ",
      [
        "storage",
        "002c32a0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f2880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f2/004f26ec.md#insn-004f2880) · [`004f28ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f2/004f26ec.md#insn-004f28ec) · [`004f292c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f2/004f26ec.md#insn-004f292c)
- 新版 [`004f28c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f2/004f272c.md#insn-004f28c0) · [`004f292c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f2/004f272c.md#insn-004f292c) · [`004f296c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f2/004f272c.md#insn-004f296c)

~~~diff
- 004f2880 ["INT_ADD", "register:40f0:8", ["const:4f2880:8", "const:4:8"]]
- 004f2880 ["CALL", null, ["callee:00c588c0:8"]]
+ 004f28c0 ["INT_ADD", "register:40f0:8", ["const:4f28c0:8", "const:4:8"]]
+ 004f28c0 ["CALL", null, ["callee:00c588c0:8"]]
- 004f2880 bytes 10971d94
+ 004f28c0 bytes 00981d94
- 004f28ec ["INT_ADD", "register:40f0:8", ["const:4f28ec:8", "const:4:8"]]
- 004f28ec ["CALL", null, ["callee:00c57eb0:8"]]
+ 004f292c ["INT_ADD", "register:40f0:8", ["const:4f292c:8", "const:4:8"]]
+ 004f292c ["CALL", null, ["callee:00c57eb0:8"]]
- 004f28ec bytes 71941d94
+ 004f292c bytes 61951d94
- 004f292c ["COPY", "register:0:8", ["register:4048:8"]]
- 004f292c ["INT_ADD", "register:40f0:8", ["const:4f292c:8", "const:4:8"]]
- 004f292c ["CALLIND", null, ["register:0:8"]]
+ 004f296c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f296c ["INT_ADD", "register:40f0:8", ["const:4f296c:8", "const:4:8"]]
+ 004f296c ["CALLIND", null, ["register:0:8"]]
- 004f292c bytes 20013fd6
+ 004f296c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b66ebb62ea2857f3f8d5efd501b9e5de"></a>

### [`004f2aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f2/004f2aa0.md) → [`004f2ae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f2/004f2ae0.md) FUN_004f2ae0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f2b2c",
      "incomplete_value": true,
      "site": "004f2b2c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f2aec",
      "incomplete_value": true,
      "site": "004f2aec",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f2b58",
      "incomplete_value": true,
      "site": "004f2b58",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f2b18",
      "incomplete_value": true,
      "site": "004f2b18",
      "value": [
        "LOAD",
        "8",
        [
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
      "004f2b1c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004f2b48",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004f2b1c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004f2b48",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f2aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f2/004f2aa0.md#insn-004f2aec) · [`004f2b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f2/004f2aa0.md#insn-004f2b18) · [`004f2adc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f2/004f2aa0.md#insn-004f2adc)
- 新版 [`004f2b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f2/004f2ae0.md#insn-004f2b2c) · [`004f2b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f2/004f2ae0.md#insn-004f2b58) · [`004f2b1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f2/004f2ae0.md#insn-004f2b1c)

~~~diff
- 004f2aec ["COPY", "register:0:8", ["register:4048:8"]]
- 004f2aec ["INT_ADD", "register:40f0:8", ["const:4f2aec:8", "const:4:8"]]
- 004f2aec ["CALLIND", null, ["register:0:8"]]
+ 004f2b2c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f2b2c ["INT_ADD", "register:40f0:8", ["const:4f2b2c:8", "const:4:8"]]
+ 004f2b2c ["CALLIND", null, ["register:0:8"]]
- 004f2aec bytes 20013fd6
+ 004f2b2c bytes 20013fd6
- 004f2b18 ["COPY", "register:0:8", ["register:4048:8"]]
- 004f2b18 ["INT_ADD", "register:40f0:8", ["const:4f2b18:8", "const:4:8"]]
- 004f2b18 ["CALLIND", null, ["register:0:8"]]
+ 004f2b58 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f2b58 ["INT_ADD", "register:40f0:8", ["const:4f2b58:8", "const:4:8"]]
+ 004f2b58 ["CALLIND", null, ["register:0:8"]]
- 004f2b18 bytes 20013fd6
+ 004f2b58 bytes 20013fd6
- 004f2adc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:338:8"]]
- 004f2adc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f2b1c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:738:8"]]
+ 004f2b1c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004f2adc bytes a99e41f9
+ 004f2b1c bytes a99e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca646a1610e5d2cec51c7f8cf0314341"></a>

### [`004f2b48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f2/004f2b48.md) → [`004f2b88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f2/004f2b88.md) _ZN5Botan14RSA_PrivateKeyC2ERKNS_6BigIntES3_S3_S3_S3_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`0054369c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/0054369c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58520.md) [`00c58720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58720.md)
- 新版 呼出元 0件  · 呼出先 12件 [`005436dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/005436dc.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c58920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58920.md) [`00c58b20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58b20.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.14% / 新版 93.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f2d40",
      "incomplete_value": true,
      "site": "004f2d40",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f2d00",
      "incomplete_value": true,
      "site": "004f2d00",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 7,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f2db0",
      "incomplete_value": true,
      "site": "004f2db0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f2d70",
      "incomplete_value": true,
      "site": "004f2d70",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 12,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f2e28",
      "incomplete_value": true,
      "site": "004f2e28",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f2de8",
      "incomplete_value": true,
      "site": "004f2de8",
      "value": [
        "LOAD",
        "8",
        [
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
      "004f2d30",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004f2da0",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004f2e18",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004f2d30",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004f2da0",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004f2e18",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f2d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f2/004f2b48.md#insn-004f2d00) · [`004f2d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f2/004f2b48.md#insn-004f2d70) · [`004f2de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f2/004f2b48.md#insn-004f2de8)
- 新版 [`004f2d40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f2/004f2b88.md#insn-004f2d40) · [`004f2db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f2/004f2b88.md#insn-004f2db0) · [`004f2e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f2/004f2b88.md#insn-004f2e28)

~~~diff
- 004f2d00 ["COPY", "register:0:8", ["register:4048:8"]]
- 004f2d00 ["INT_ADD", "register:40f0:8", ["const:4f2d00:8", "const:4:8"]]
- 004f2d00 ["CALLIND", null, ["register:0:8"]]
+ 004f2d40 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f2d40 ["INT_ADD", "register:40f0:8", ["const:4f2d40:8", "const:4:8"]]
+ 004f2d40 ["CALLIND", null, ["register:0:8"]]
- 004f2d00 bytes 20013fd6
+ 004f2d40 bytes 20013fd6
- 004f2d70 ["COPY", "register:0:8", ["register:4048:8"]]
- 004f2d70 ["INT_ADD", "register:40f0:8", ["const:4f2d70:8", "const:4:8"]]
- 004f2d70 ["CALLIND", null, ["register:0:8"]]
+ 004f2db0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f2db0 ["INT_ADD", "register:40f0:8", ["const:4f2db0:8", "const:4:8"]]
+ 004f2db0 ["CALLIND", null, ["register:0:8"]]
- 004f2d70 bytes 20013fd6
+ 004f2db0 bytes 20013fd6
- 004f2de8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004f2de8 ["INT_ADD", "register:40f0:8", ["const:4f2de8:8", "const:4:8"]]
- 004f2de8 ["CALLIND", null, ["register:0:8"]]
+ 004f2e28 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f2e28 ["INT_ADD", "register:40f0:8", ["const:4f2e28:8", "const:4:8"]]
+ 004f2e28 ["CALLIND", null, ["register:0:8"]]
- 004f2de8 bytes 20013fd6
+ 004f2e28 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b4b1c53f16a3602fd9ca8fb16082f65"></a>

### [`004f3358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f3/004f3358.md) → [`004f3398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f3/004f3398.md) _ZN5Botan14RSA_PrivateKeyC1ERKNS_6BigIntES3_S3_S3_S3_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`0054369c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/0054369c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58520.md) [`00c58720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58720.md)
- 新版 呼出元 0件  · 呼出先 12件 [`005436dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/005436dc.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c58920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58920.md) [`00c58b20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58b20.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.73% / 新版 91.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 14件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f3404",
      "incomplete_value": true,
      "site": "004f3404",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004f33c4",
      "incomplete_value": true,
      "site": "004f33c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004f33fc",
      "incomplete_value": true,
      "site": "004f3418",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004f33bc",
      "incomplete_value": true,
      "site": "004f33d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 22,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f351c",
      "incomplete_value": true,
      "site": "004f351c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f34dc",
      "incomplete_value": true,
      "site": "004f34dc",
      "value": [
        "LOAD",
        "8",
        [
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
      "004f33c8",
      "READ",
      [
        "storage",
        "00c9abe0",
        null,
        "pointer"
      ]
    ],
    [
      "004f3404",
      "DATA",
      [
        "storage",
        "00c66eb8",
        null,
        "undefined1[528]"
      ]
    ],
    [
      "004f3418",
      "DATA",
      [
        "storage",
        "00c66d98",
        null,
        "undefined1[528]"
      ]
    ]
  ],
  "added": [
    [
      "004f33c8",
      "READ",
      [
        "storage",
        "00c9afe0",
        null,
        "pointer"
      ]
    ],
    [
      "004f3404",
      "DATA",
      [
        "storage",
        "00c672b8",
        null,
        "undefined1[528]"
      ]
    ],
    [
      "004f3418",
      "DATA",
      [
        "storage",
        "00c67198",
        null,
        "undefined1[528]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f34dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f3/004f3358.md#insn-004f34dc) · [`004f354c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f3/004f3358.md#insn-004f354c) · [`004f35c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f3/004f3358.md#insn-004f35c4)
- 新版 [`004f351c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f3/004f3398.md#insn-004f351c) · [`004f358c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f3/004f3398.md#insn-004f358c) · [`004f3604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f3/004f3398.md#insn-004f3604)

~~~diff
- 004f34dc ["COPY", "register:0:8", ["register:4048:8"]]
- 004f34dc ["INT_ADD", "register:40f0:8", ["const:4f34dc:8", "const:4:8"]]
- 004f34dc ["CALLIND", null, ["register:0:8"]]
+ 004f351c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f351c ["INT_ADD", "register:40f0:8", ["const:4f351c:8", "const:4:8"]]
+ 004f351c ["CALLIND", null, ["register:0:8"]]
- 004f34dc bytes 20013fd6
+ 004f351c bytes 20013fd6
- 004f354c ["COPY", "register:0:8", ["register:4048:8"]]
- 004f354c ["INT_ADD", "register:40f0:8", ["const:4f354c:8", "const:4:8"]]
- 004f354c ["CALLIND", null, ["register:0:8"]]
+ 004f358c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f358c ["INT_ADD", "register:40f0:8", ["const:4f358c:8", "const:4:8"]]
+ 004f358c ["CALLIND", null, ["register:0:8"]]
- 004f354c bytes 20013fd6
+ 004f358c bytes 20013fd6
- 004f35c4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004f35c4 ["INT_ADD", "register:40f0:8", ["const:4f35c4:8", "const:4:8"]]
- 004f35c4 ["CALLIND", null, ["register:0:8"]]
+ 004f3604 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f3604 ["INT_ADD", "register:40f0:8", ["const:4f3604:8", "const:4:8"]]
+ 004f3604 ["CALLIND", null, ["register:0:8"]]
- 004f35c4 bytes 20013fd6
+ 004f3604 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7ac91031c67adf56113427dfa193e9f"></a>

### [`004f3b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f3/004f3b34.md) → [`004f3b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f3/004f3b74.md) _ZN5Botan14RSA_PrivateKeyC2ERNS_21RandomNumberGeneratorEmm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 17件 [`004a680c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a680c.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 0件  · 呼出先 17件 [`004a684c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a684c.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.22% / 新版 99.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

アドレスに依存する影響 `call_argument_candidate` 2件, `call_target` 17件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f3d14",
      "incomplete_value": true,
      "site": "004f3d14",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f3cd4",
      "incomplete_value": true,
      "site": "004f3cd4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f3db8",
      "incomplete_value": true,
      "site": "004f3db8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f3d78",
      "incomplete_value": true,
      "site": "004f3d78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f3eb4",
      "incomplete_value": true,
      "site": "004f3eb4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f3e74",
      "incomplete_value": true,
      "site": "004f3e74",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004f3d04",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004f3da8",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004f3ea4",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004f3d04",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004f3da8",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004f3ea4",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f3cd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f3/004f3b34.md#insn-004f3cd4) · [`004f3d14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f3/004f3b34.md#insn-004f3d14) · [`004f3d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f3/004f3b34.md#insn-004f3d78)
- 新版 [`004f3d14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f3/004f3b74.md#insn-004f3d14) · [`004f3d54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f3/004f3b74.md#insn-004f3d54) · [`004f3db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f3/004f3b74.md#insn-004f3db8)

~~~diff
- 004f3cd4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004f3cd4 ["INT_ADD", "register:40f0:8", ["const:4f3cd4:8", "const:4:8"]]
- 004f3cd4 ["CALLIND", null, ["register:0:8"]]
+ 004f3d14 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f3d14 ["INT_ADD", "register:40f0:8", ["const:4f3d14:8", "const:4:8"]]
+ 004f3d14 ["CALLIND", null, ["register:0:8"]]
- 004f3cd4 bytes 20013fd6
+ 004f3d14 bytes 20013fd6
- 004f3d14 ["INT_ADD", "register:40f0:8", ["const:4f3d14:8", "const:4:8"]]
- 004f3d14 ["CALL", null, ["callee:00c59340:8"]]
+ 004f3d54 ["INT_ADD", "register:40f0:8", ["const:4f3d54:8", "const:4:8"]]
+ 004f3d54 ["CALL", null, ["callee:00c59340:8"]]
- 004f3d14 bytes 8b941d94
+ 004f3d54 bytes 7b951d94
- 004f3d78 ["COPY", "register:0:8", ["register:4048:8"]]
- 004f3d78 ["INT_ADD", "register:40f0:8", ["const:4f3d78:8", "const:4:8"]]
- 004f3d78 ["CALLIND", null, ["register:0:8"]]
+ 004f3db8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f3db8 ["INT_ADD", "register:40f0:8", ["const:4f3db8:8", "const:4:8"]]
+ 004f3db8 ["CALLIND", null, ["register:0:8"]]
- 004f3d78 bytes 20013fd6
+ 004f3db8 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df42f704fb688d993ef128361b5716cc"></a>

### [`004f479c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f4/004f479c.md) → [`004f47dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f4/004f47dc.md) _ZNK5Botan14RSA_PrivateKey9check_keyERNS_21RandomNumberGeneratorEb

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c59350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59350.md) · 呼出先 13件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58520.md) [`00c58720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58720.md)
- 新版 呼出元 1件 [`00c59750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59750.md) · 呼出先 13件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c58920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58920.md) [`00c58b20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58b20.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.60% / 新版 95.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 5件, `store_value` 2件

アドレスに依存する影響 `call_target` 16件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f4eb0",
      "incomplete_value": true,
      "site": "004f4eb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bdd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f4e70",
      "incomplete_value": true,
      "site": "004f4e70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b9d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 34,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f4eb4",
      "incomplete_value": true,
      "site": "004f4eb4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004f4e74",
      "incomplete_value": true,
      "site": "004f4e74",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 35,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f4914",
      "incomplete_value": true,
      "site": "004f4914",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f48d4",
      "incomplete_value": true,
      "site": "004f48d4",
      "value": [
        "LOAD",
        "8",
        [
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
      "004f4904",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004f4930",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004f495c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004f4904",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004f4930",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004f495c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f48d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f4/004f479c.md#insn-004f48d4) · [`004f4900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f4/004f479c.md#insn-004f4900) · [`004f492c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f4/004f479c.md#insn-004f492c)
- 新版 [`004f4914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f4/004f47dc.md#insn-004f4914) · [`004f4940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f4/004f47dc.md#insn-004f4940) · [`004f496c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f4/004f47dc.md#insn-004f496c)

~~~diff
- 004f48d4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004f48d4 ["INT_ADD", "register:40f0:8", ["const:4f48d4:8", "const:4:8"]]
- 004f48d4 ["CALLIND", null, ["register:0:8"]]
+ 004f4914 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f4914 ["INT_ADD", "register:40f0:8", ["const:4f4914:8", "const:4:8"]]
+ 004f4914 ["CALLIND", null, ["register:0:8"]]
- 004f48d4 bytes 20013fd6
+ 004f4914 bytes 20013fd6
- 004f4900 ["COPY", "register:0:8", ["register:4048:8"]]
- 004f4900 ["INT_ADD", "register:40f0:8", ["const:4f4900:8", "const:4:8"]]
- 004f4900 ["CALLIND", null, ["register:0:8"]]
+ 004f4940 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f4940 ["INT_ADD", "register:40f0:8", ["const:4f4940:8", "const:4:8"]]
+ 004f4940 ["CALLIND", null, ["register:0:8"]]
- 004f4900 bytes 20013fd6
+ 004f4940 bytes 20013fd6
- 004f492c ["COPY", "register:0:8", ["register:4048:8"]]
- 004f492c ["INT_ADD", "register:40f0:8", ["const:4f492c:8", "const:4:8"]]
- 004f492c ["CALLIND", null, ["register:0:8"]]
+ 004f496c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f496c ["INT_ADD", "register:40f0:8", ["const:4f496c:8", "const:4:8"]]
+ 004f496c ["CALLIND", null, ["register:0:8"]]
- 004f492c bytes 20013fd6
+ 004f496c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28b4e7687f32758b64dbdba11972ee20"></a>

### [`004f5068`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f5068.md) → [`004f50a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f5/004f50a8.md) _ZNK5Botan13RSA_PublicKey20create_encryption_opERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorI

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59360.md) · 呼出先 6件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c58ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58ba0.md)
- 新版 呼出元 1件 [`00c59760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59760.md) · 呼出先 6件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c58fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58fa0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.01% / 新版 97.01%

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
      "definition_site": "004f513c",
      "incomplete_value": true,
      "site": "004f5144",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ed0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f50fc",
      "incomplete_value": true,
      "site": "004f5104",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f5138",
      "incomplete_value": false,
      "site": "004f5144",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004f50f8",
      "incomplete_value": false,
      "site": "004f5104",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "ordinal": 2,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f51a0",
      "incomplete_value": true,
      "site": "004f51ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f5160",
      "incomplete_value": true,
      "site": "004f516c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c20:8"
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
      "004f5138",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004f513c",
      "READ",
      [
        "storage",
        "00c9aad0",
        null,
        "pointer"
      ]
    ],
    [
      "004f513c",
      "PARAM",
      [
        "storage",
        "00c66618",
        "_ZTIN5Botan19Algorithm_Not_FoundE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004f5138",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004f513c",
      "READ",
      [
        "storage",
        "00c9aed0",
        null,
        "pointer"
      ]
    ],
    [
      "004f513c",
      "PARAM",
      [
        "storage",
        "00c66a18",
        "_ZTIN5Botan19Algorithm_Not_FoundE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f5104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f5068.md#insn-004f5104) · [`004f512c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f5068.md#insn-004f512c) · [`004f516c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f5068.md#insn-004f516c)
- 新版 [`004f5144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f5/004f50a8.md#insn-004f5144) · [`004f516c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f5/004f50a8.md#insn-004f516c) · [`004f51ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f5/004f50a8.md#insn-004f51ac)

~~~diff
- 004f5104 ["INT_ADD", "register:40f0:8", ["const:4f5104:8", "const:4:8"]]
- 004f5104 ["CALL", null, ["callee:00c57f10:8"]]
+ 004f5144 ["INT_ADD", "register:40f0:8", ["const:4f5144:8", "const:4:8"]]
+ 004f5144 ["CALL", null, ["callee:00c57f10:8"]]
- 004f5104 bytes 838a1d94
+ 004f5144 bytes 738b1d94
- 004f512c ["COPY", "register:0:8", ["register:4048:8"]]
- 004f512c ["INT_ADD", "register:40f0:8", ["const:4f512c:8", "const:4:8"]]
- 004f512c ["CALLIND", null, ["register:0:8"]]
+ 004f516c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f516c ["INT_ADD", "register:40f0:8", ["const:4f516c:8", "const:4:8"]]
+ 004f516c ["CALLIND", null, ["register:0:8"]]
- 004f512c bytes 20013fd6
+ 004f516c bytes 20013fd6
- 004f516c ["INT_ADD", "register:40f0:8", ["const:4f516c:8", "const:4:8"]]
- 004f516c ["CALL", null, ["callee:00c57f10:8"]]
+ 004f51ac ["INT_ADD", "register:40f0:8", ["const:4f51ac:8", "const:4:8"]]
+ 004f51ac ["CALL", null, ["callee:00c57f10:8"]]
- 004f516c bytes 698a1d94
+ 004f51ac bytes 598b1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f23de1b05d479a01cb1dedb11c34dbc6"></a>

### [`004f51e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f51e0.md) → [`004f5220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f5/004f5220.md) _ZNK5Botan13RSA_PublicKey24create_kem_encryption_opERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9alloca

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59380.md) · 呼出先 8件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`00c59780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59780.md) · 呼出先 8件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.98% / 新版 93.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004f52a4",
      "incomplete_value": false,
      "site": "004f52a4",
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
            "const:f18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f5264",
      "incomplete_value": false,
      "site": "004f5264",
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
            "const:b18:8"
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
      "definition_site": "004f52cc",
      "incomplete_value": false,
      "site": "004f52d4",
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
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f528c",
      "incomplete_value": false,
      "site": "004f5294",
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
            "const:ae8:8"
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
      "definition_site": "004f5358",
      "incomplete_value": true,
      "site": "004f5364",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f5318",
      "incomplete_value": true,
      "site": "004f5324",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c20:8"
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
      "004f52a4",
      "DATA",
      [
        "storage",
        "00c66b18",
        null,
        "undefined *"
      ]
    ],
    [
      "004f52d4",
      "DATA",
      [
        "storage",
        "00c69ae8",
        null,
        "undefined *"
      ]
    ],
    [
      "004f5354",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004f52a4",
      "DATA",
      [
        "storage",
        "00c66f18",
        null,
        "undefined *"
      ]
    ],
    [
      "004f52d4",
      "DATA",
      [
        "storage",
        "00c69ee8",
        null,
        "undefined *"
      ]
    ],
    [
      "004f5354",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f5254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f51e0.md#insn-004f5254) · [`004f52e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f51e0.md#insn-004f52e4) · [`004f5324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f51e0.md#insn-004f5324)
- 新版 [`004f5294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f5/004f5220.md#insn-004f5294) · [`004f5324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f5/004f5220.md#insn-004f5324) · [`004f5364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f5/004f5220.md#insn-004f5364)

~~~diff
- 004f5254 ["INT_ADD", "register:40f0:8", ["const:4f5254:8", "const:4:8"]]
- 004f5254 ["CALL", null, ["callee:00c57e90:8"]]
+ 004f5294 ["INT_ADD", "register:40f0:8", ["const:4f5294:8", "const:4:8"]]
+ 004f5294 ["CALL", null, ["callee:00c57e90:8"]]
- 004f5254 bytes 0f8a1d94
+ 004f5294 bytes ff8a1d94
- 004f52e4 ["COPY", "register:0:8", ["register:4050:8"]]
- 004f52e4 ["INT_ADD", "register:40f0:8", ["const:4f52e4:8", "const:4:8"]]
- 004f52e4 ["CALLIND", null, ["register:0:8"]]
+ 004f5324 ["COPY", "register:0:8", ["register:4050:8"]]
+ 004f5324 ["INT_ADD", "register:40f0:8", ["const:4f5324:8", "const:4:8"]]
+ 004f5324 ["CALLIND", null, ["register:0:8"]]
- 004f52e4 bytes 40013fd6
+ 004f5324 bytes 40013fd6
- 004f5324 ["INT_ADD", "register:40f0:8", ["const:4f5324:8", "const:4:8"]]
- 004f5324 ["CALL", null, ["callee:00c57f10:8"]]
+ 004f5364 ["INT_ADD", "register:40f0:8", ["const:4f5364:8", "const:4:8"]]
+ 004f5364 ["CALL", null, ["callee:00c57f10:8"]]
- 004f5324 bytes fb891d94
+ 004f5364 bytes eb8a1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c0716032dbdd071a795e2e4bd1cdb50"></a>

### [`004f53c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f53c0.md) → [`004f5400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f5/004f5400.md) _ZNK5Botan13RSA_PublicKey22create_verification_opERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59390.md) · 呼出先 8件 [`004eb428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004eb428.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 1件 [`00c59790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59790.md) · 呼出先 8件 [`004eb468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004eb/004eb468.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.25% / 新版 96.25%

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
      "definition_site": "004f54a0",
      "incomplete_value": false,
      "site": "004f54a8",
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
            "const:f50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f5460",
      "incomplete_value": false,
      "site": "004f5468",
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
            "const:b50:8"
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
      "definition_site": "004f552c",
      "incomplete_value": true,
      "site": "004f5538",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f54ec",
      "incomplete_value": true,
      "site": "004f54f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c20:8"
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
      "definition_site": "004f5528",
      "incomplete_value": false,
      "site": "004f5538",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004f54e8",
      "incomplete_value": false,
      "site": "004f54f8",
      "value": [
        "leaf",
        "const:535828:8"
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
      "004f54a8",
      "DATA",
      [
        "storage",
        "00c69b50",
        null,
        "undefined *"
      ]
    ],
    [
      "004f5528",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004f552c",
      "READ",
      [
        "storage",
        "00c9ac20",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004f54a8",
      "DATA",
      [
        "storage",
        "00c69f50",
        null,
        "undefined *"
      ]
    ],
    [
      "004f5528",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004f552c",
      "READ",
      [
        "storage",
        "00c9b020",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f54b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f53c0.md#insn-004f54b8) · [`004f54f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f53c0.md#insn-004f54f8) · [`004f5434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f53c0.md#insn-004f5434)
- 新版 [`004f54f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f5/004f5400.md#insn-004f54f8) · [`004f5538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f5/004f5400.md#insn-004f5538) · [`004f5474`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f5/004f5400.md#insn-004f5474)

~~~diff
- 004f54b8 ["COPY", "register:0:8", ["register:4050:8"]]
- 004f54b8 ["INT_ADD", "register:40f0:8", ["const:4f54b8:8", "const:4:8"]]
- 004f54b8 ["CALLIND", null, ["register:0:8"]]
+ 004f54f8 ["COPY", "register:0:8", ["register:4050:8"]]
+ 004f54f8 ["INT_ADD", "register:40f0:8", ["const:4f54f8:8", "const:4:8"]]
+ 004f54f8 ["CALLIND", null, ["register:0:8"]]
- 004f54b8 bytes 40013fd6
+ 004f54f8 bytes 40013fd6
- 004f54f8 ["INT_ADD", "register:40f0:8", ["const:4f54f8:8", "const:4:8"]]
- 004f54f8 ["CALL", null, ["callee:00c57f10:8"]]
+ 004f5538 ["INT_ADD", "register:40f0:8", ["const:4f5538:8", "const:4:8"]]
+ 004f5538 ["CALL", null, ["callee:00c57f10:8"]]
- 004f54f8 bytes 86891d94
+ 004f5538 bytes 768a1d94
- 004f5434 ["INT_ADD", "register:40f0:8", ["const:4f5434:8", "const:4:8"]]
- 004f5434 ["CALL", null, ["callee:00c57e90:8"]]
+ 004f5474 ["INT_ADD", "register:40f0:8", ["const:4f5474:8", "const:4:8"]]
+ 004f5474 ["CALL", null, ["callee:00c57e90:8"]]
- 004f5434 bytes 97891d94
+ 004f5474 bytes 878a1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f42d1369dae9a1f30c1d8ac797b84ff2"></a>

### [`004f5578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f5578.md) → [`004f55b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f5/004f55b8.md) _ZNK5Botan14RSA_PrivateKey20create_decryption_opERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocator

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c58ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58ba0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c58fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58fa0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.92% / 新版 96.92%

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
      "definition_site": "004f5650",
      "incomplete_value": true,
      "site": "004f5658",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ed0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f5610",
      "incomplete_value": true,
      "site": "004f5618",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f564c",
      "incomplete_value": false,
      "site": "004f5658",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004f560c",
      "incomplete_value": false,
      "site": "004f5618",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "ordinal": 2,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f56a8",
      "incomplete_value": true,
      "site": "004f56b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f5668",
      "incomplete_value": true,
      "site": "004f5674",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c20:8"
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
      "004f564c",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004f5650",
      "READ",
      [
        "storage",
        "00c9aad0",
        null,
        "pointer"
      ]
    ],
    [
      "004f5650",
      "PARAM",
      [
        "storage",
        "00c66618",
        "_ZTIN5Botan19Algorithm_Not_FoundE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004f564c",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004f5650",
      "READ",
      [
        "storage",
        "00c9aed0",
        null,
        "pointer"
      ]
    ],
    [
      "004f5650",
      "PARAM",
      [
        "storage",
        "00c66a18",
        "_ZTIN5Botan19Algorithm_Not_FoundE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f5618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f5578.md#insn-004f5618) · [`004f5674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f5578.md#insn-004f5674) · [`004f55e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f5578.md#insn-004f55e4)
- 新版 [`004f5658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f5/004f55b8.md#insn-004f5658) · [`004f56b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f5/004f55b8.md#insn-004f56b4) · [`004f5624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f5/004f55b8.md#insn-004f5624)

~~~diff
- 004f5618 ["INT_ADD", "register:40f0:8", ["const:4f5618:8", "const:4:8"]]
- 004f5618 ["CALL", null, ["callee:00c57f10:8"]]
+ 004f5658 ["INT_ADD", "register:40f0:8", ["const:4f5658:8", "const:4:8"]]
+ 004f5658 ["CALL", null, ["callee:00c57f10:8"]]
- 004f5618 bytes 3e891d94
+ 004f5658 bytes 2e8a1d94
- 004f5674 ["INT_ADD", "register:40f0:8", ["const:4f5674:8", "const:4:8"]]
- 004f5674 ["CALL", null, ["callee:00c57f10:8"]]
+ 004f56b4 ["INT_ADD", "register:40f0:8", ["const:4f56b4:8", "const:4:8"]]
+ 004f56b4 ["CALL", null, ["callee:00c57f10:8"]]
- 004f5674 bytes 27891d94
+ 004f56b4 bytes 178a1d94
- 004f55e4 ["INT_ADD", "register:40f0:8", ["const:4f55e4:8", "const:4:8"]]
- 004f55e4 ["CALL", null, ["callee:00c57ef0:8"]]
+ 004f5624 ["INT_ADD", "register:40f0:8", ["const:4f5624:8", "const:4:8"]]
+ 004f5624 ["CALL", null, ["callee:00c57ef0:8"]]
- 004f55e4 bytes 43891d94
+ 004f5624 bytes 338a1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64a6591175ac981e59b74fb08735aa17"></a>

### [`004f56c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f56c8.md) → [`004f5708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f5/004f5708.md) _ZNK5Botan14RSA_PrivateKey24create_kem_decryption_opERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9alloc

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`005376d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00537/005376d4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00537714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00537/00537714.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.98% / 新版 93.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004f5794",
      "incomplete_value": false,
      "site": "004f5794",
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
            "const:f48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f5754",
      "incomplete_value": false,
      "site": "004f5754",
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
            "const:b48:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004f57b8",
      "incomplete_value": false,
      "site": "004f57c0",
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
            "const:1b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f5778",
      "incomplete_value": false,
      "site": "004f5780",
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
            "const:db0:8"
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
      "definition_site": "004f5840",
      "incomplete_value": true,
      "site": "004f584c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f5800",
      "incomplete_value": true,
      "site": "004f580c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c20:8"
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
      "004f5794",
      "DATA",
      [
        "storage",
        "00c66b48",
        null,
        "undefined *"
      ]
    ],
    [
      "004f57c0",
      "DATA",
      [
        "storage",
        "00c69db0",
        null,
        "undefined *"
      ]
    ],
    [
      "004f5814",
      "DATA",
      [
        "storage",
        "00415352",
        null,
        "qword"
      ]
    ]
  ],
  "added": [
    [
      "004f5794",
      "DATA",
      [
        "storage",
        "00c66f48",
        null,
        "undefined *"
      ]
    ],
    [
      "004f57c0",
      "DATA",
      [
        "storage",
        "00c6a1b0",
        null,
        "undefined *"
      ]
    ],
    [
      "004f5814",
      "DATA",
      [
        "storage",
        "00415352",
        null,
        "dword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f580c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f56c8.md#insn-004f580c) · [`004f5744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f56c8.md#insn-004f5744) · [`004f5750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f56c8.md#insn-004f5750)
- 新版 [`004f584c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f5/004f5708.md#insn-004f584c) · [`004f5784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f5/004f5708.md#insn-004f5784) · [`004f5790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f5/004f5708.md#insn-004f5790)

~~~diff
- 004f580c ["INT_ADD", "register:40f0:8", ["const:4f580c:8", "const:4:8"]]
- 004f580c ["CALL", null, ["callee:00c57f10:8"]]
+ 004f584c ["INT_ADD", "register:40f0:8", ["const:4f584c:8", "const:4:8"]]
+ 004f584c ["CALL", null, ["callee:00c57f10:8"]]
- 004f580c bytes c1881d94
+ 004f584c bytes b1891d94
- 004f5744 ["INT_ADD", "register:40f0:8", ["const:4f5744:8", "const:4:8"]]
- 004f5744 ["CALL", null, ["callee:00c57e90:8"]]
+ 004f5784 ["INT_ADD", "register:40f0:8", ["const:4f5784:8", "const:4:8"]]
+ 004f5784 ["CALL", null, ["callee:00c57e90:8"]]
- 004f5744 bytes d3881d94
+ 004f5784 bytes c3891d94
- 004f5750 ["COPY", "tmp:0:8", ["const:b48:8"]]
- 004f5750 ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
- 004f5750 ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
- 004f5750 ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
+ 004f5790 ["COPY", "tmp:0:8", ["const:f48:8"]]
+ 004f5790 ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
+ 004f5790 ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
+ 004f5790 ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
- 004f5750 bytes 39232d91
+ 004f5790 bytes 39233d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-509d079bcfaad2d2a8c4e42951015eae"></a>

### [`004f5890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f5890.md) → [`004f58d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f5/004f58d0.md) _ZNK5Botan14RSA_PrivateKey19create_signature_opERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorI

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`004eb0e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004eb0e4.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`005376d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00537/005376d4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`004eb124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004eb/004eb124.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00537714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00537/00537714.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.10% / 新版 96.10%

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
      "definition_site": "004f596c",
      "incomplete_value": false,
      "site": "004f5974",
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
            "const:218:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f592c",
      "incomplete_value": false,
      "site": "004f5934",
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
            "const:e18:8"
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
      "definition_site": "004f59f0",
      "incomplete_value": true,
      "site": "004f59fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f59b0",
      "incomplete_value": true,
      "site": "004f59bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c20:8"
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
      "definition_site": "004f59ec",
      "incomplete_value": false,
      "site": "004f59fc",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004f59ac",
      "incomplete_value": false,
      "site": "004f59bc",
      "value": [
        "leaf",
        "const:535828:8"
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
      "004f5974",
      "DATA",
      [
        "storage",
        "00c69e18",
        null,
        "undefined *"
      ]
    ],
    [
      "004f59c4",
      "DATA",
      [
        "storage",
        "00415352",
        null,
        "qword"
      ]
    ],
    [
      "004f59ec",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004f5974",
      "DATA",
      [
        "storage",
        "00c6a218",
        null,
        "undefined *"
      ]
    ],
    [
      "004f59c4",
      "DATA",
      [
        "storage",
        "00415352",
        null,
        "dword"
      ]
    ],
    [
      "004f59ec",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f59bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f5890.md#insn-004f59bc) · [`004f5908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f5890.md#insn-004f5908) · [`004f5914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f5890.md#insn-004f5914)
- 新版 [`004f59fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f5/004f58d0.md#insn-004f59fc) · [`004f5948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f5/004f58d0.md#insn-004f5948) · [`004f5954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f5/004f58d0.md#insn-004f5954)

~~~diff
- 004f59bc ["INT_ADD", "register:40f0:8", ["const:4f59bc:8", "const:4:8"]]
- 004f59bc ["CALL", null, ["callee:00c57f10:8"]]
+ 004f59fc ["INT_ADD", "register:40f0:8", ["const:4f59fc:8", "const:4:8"]]
+ 004f59fc ["CALL", null, ["callee:00c57f10:8"]]
- 004f59bc bytes 55881d94
+ 004f59fc bytes 45891d94
- 004f5908 ["INT_ADD", "register:40f0:8", ["const:4f5908:8", "const:4:8"]]
- 004f5908 ["CALL", null, ["callee:00c57e90:8"]]
+ 004f5948 ["INT_ADD", "register:40f0:8", ["const:4f5948:8", "const:4:8"]]
+ 004f5948 ["CALL", null, ["callee:00c57e90:8"]]
- 004f5908 bytes 62881d94
+ 004f5948 bytes 52891d94
- 004f5914 ["INT_ADD", "register:40f0:8", ["const:4f5914:8", "const:4:8"]]
- 004f5914 ["CALL", null, ["callee:004eb124:8"]]
+ 004f5954 ["INT_ADD", "register:40f0:8", ["const:4f5954:8", "const:4:8"]]
+ 004f5954 ["CALL", null, ["callee:004eb124:8"]]
- 004f5914 bytes f4d5ff97
+ 004f5954 bytes f4d5ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30a7ccfbc5273be64c8c2fc7874677f7"></a>

### [`004f5a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f5a24.md) → [`004f5a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f5/004f5a64.md) _ZNK5Botan7SHA_16010copy_stateEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`0053616c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/0053616c.md) [`00540264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540264.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005361ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/005361ac.md) [`005402a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005402a4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "004f5a98",
      "incomplete_value": true,
      "site": "004f5a9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004f5a58",
      "incomplete_value": true,
      "site": "004f5a5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004f5ac4",
      "incomplete_value": true,
      "site": "004f5acc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004f5a84",
      "incomplete_value": true,
      "site": "004f5a8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004f5a8c",
      "READ",
      [
        "storage",
        "00c9ab38",
        null,
        "pointer"
      ]
    ],
    [
      "004f5a9c",
      "DATA",
      [
        "storage",
        "00c668d8",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "004f5ab4",
      "READ",
      [
        "storage",
        "00c9ab40",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004f5a8c",
      "READ",
      [
        "storage",
        "00c9af38",
        null,
        "pointer"
      ]
    ],
    [
      "004f5a9c",
      "DATA",
      [
        "storage",
        "00c66cd8",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "004f5ab4",
      "READ",
      [
        "storage",
        "00c9af40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f5a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f5a24.md#insn-004f5a4c) · [`004f5a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f5a24.md#insn-004f5a40) · [`004f5a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f5/004f5a24.md#insn-004f5a68)
- 新版 [`004f5a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f5/004f5a64.md#insn-004f5a8c) · [`004f5a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f5/004f5a64.md#insn-004f5a80) · [`004f5aa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f5/004f5a64.md#insn-004f5aa8)

~~~diff
- 004f5a4c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b38:8"]]
- 004f5a4c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f5a8c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f38:8"]]
+ 004f5a8c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004f5a4c bytes 089d45f9
+ 004f5a8c bytes 089d47f9
- 004f5a40 ["INT_ADD", "register:40f0:8", ["const:4f5a40:8", "const:4:8"]]
- 004f5a40 ["CALL", null, ["callee:00c57e90:8"]]
+ 004f5a80 ["INT_ADD", "register:40f0:8", ["const:4f5a80:8", "const:4:8"]]
+ 004f5a80 ["CALL", null, ["callee:00c57e90:8"]]
- 004f5a40 bytes 14881d94
+ 004f5a80 bytes 04891d94
- 004f5a68 ["INT_ADD", "register:40f0:8", ["const:4f5a68:8", "const:4:8"]]
- 004f5a68 ["CALL", null, ["callee:005402a4:8"]]
+ 004f5aa8 ["INT_ADD", "register:40f0:8", ["const:4f5aa8:8", "const:4:8"]]
+ 004f5aa8 ["CALL", null, ["callee:005402a4:8"]]
- 004f5a68 bytes ff290194
+ 004f5aa8 bytes ff290194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d75dd984ed07a1ea32fcc49b666fa706"></a>

### [`004f691c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f6/004f691c.md) → [`004f695c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f6/004f695c.md) _ZN5Botan7SHA_1605clearEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f69a4",
      "incomplete_value": true,
      "site": "004f69b0",
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
                "const:370:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f6964",
      "incomplete_value": true,
      "site": "004f6970",
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
      "004f69a4",
      "READ",
      [
        "storage",
        "002c2330",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004f69a4",
      "READ",
      [
        "storage",
        "002c2370",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f6940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f6/004f691c.md#insn-004f6940) · [`004f6958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f6/004f691c.md#insn-004f6958) · [`004f6964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f6/004f691c.md#insn-004f6964)
- 新版 [`004f6980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f6/004f695c.md#insn-004f6980) · [`004f6998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f6/004f695c.md#insn-004f6998) · [`004f69a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f6/004f695c.md#insn-004f69a4)

~~~diff
- 004f6940 ["INT_ADD", "register:40f0:8", ["const:4f6940:8", "const:4:8"]]
- 004f6940 ["CALL", null, ["callee:00c58090:8"]]
+ 004f6980 ["INT_ADD", "register:40f0:8", ["const:4f6980:8", "const:4:8"]]
+ 004f6980 ["CALL", null, ["callee:00c58090:8"]]
- 004f6940 bytes d4841d94
+ 004f6980 bytes c4851d94
- 004f6958 ["INT_ADD", "register:40f0:8", ["const:4f6958:8", "const:4:8"]]
- 004f6958 ["CALL", null, ["callee:00c58090:8"]]
+ 004f6998 ["INT_ADD", "register:40f0:8", ["const:4f6998:8", "const:4:8"]]
+ 004f6998 ["CALL", null, ["callee:00c58090:8"]]
- 004f6958 bytes ce841d94
+ 004f6998 bytes be851d94
- 004f6964 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:330:8"]]
- 004f6964 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 004f6964 ["COPY", "register:5010:8", ["const:0:8"]]
- 004f6964 ["COPY", "register:5018:8", ["const:0:8"]]
+ 004f69a4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:370:8"]]
+ 004f69a4 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
+ 004f69a4 ["COPY", "register:5010:8", ["const:0:8"]]
+ 004f69a4 ["COPY", "register:5018:8", ["const:0:8"]]
- 004f6964 bytes 00cdc03d
+ 004f69a4 bytes 00ddc03d
~~~


<a id="compare-d838910ef7c365e80ba444eeb2575f8e"></a>

### [`004f6984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f6/004f6984.md) → [`004f69c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f6/004f69c4.md) _ZNK5Botan7SHA_22410copy_stateEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`0053616c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/0053616c.md) [`00540264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540264.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005361ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/005361ac.md) [`005402a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005402a4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f69f8",
      "incomplete_value": true,
      "site": "004f69fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004f69b8",
      "incomplete_value": true,
      "site": "004f69bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004f6a24",
      "incomplete_value": true,
      "site": "004f6a2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004f69e4",
      "incomplete_value": true,
      "site": "004f69ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004f69ec",
      "READ",
      [
        "storage",
        "00c9ab38",
        null,
        "pointer"
      ]
    ],
    [
      "004f69fc",
      "DATA",
      [
        "storage",
        "00c668d8",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "004f6a14",
      "READ",
      [
        "storage",
        "00c9ab48",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004f69ec",
      "READ",
      [
        "storage",
        "00c9af38",
        null,
        "pointer"
      ]
    ],
    [
      "004f69fc",
      "DATA",
      [
        "storage",
        "00c66cd8",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "004f6a14",
      "READ",
      [
        "storage",
        "00c9af48",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f69ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f6/004f6984.md#insn-004f69ac) · [`004f69fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f6/004f6984.md#insn-004f69fc) · [`004f69a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f6/004f6984.md#insn-004f69a0)
- 新版 [`004f69ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f6/004f69c4.md#insn-004f69ec) · [`004f6a3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f6/004f69c4.md#insn-004f6a3c) · [`004f69e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f6/004f69c4.md#insn-004f69e0)

~~~diff
- 004f69ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b38:8"]]
- 004f69ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f69ec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f38:8"]]
+ 004f69ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004f69ac bytes 089d45f9
+ 004f69ec bytes 089d47f9
- 004f69fc ["INT_ADD", "register:40f0:8", ["const:4f69fc:8", "const:4:8"]]
- 004f69fc ["CALL", null, ["callee:005361ac:8"]]
+ 004f6a3c ["INT_ADD", "register:40f0:8", ["const:4f6a3c:8", "const:4:8"]]
+ 004f6a3c ["CALL", null, ["callee:005361ac:8"]]
- 004f69fc bytes dcfd0094
+ 004f6a3c bytes dcfd0094
- 004f69a0 ["INT_ADD", "register:40f0:8", ["const:4f69a0:8", "const:4:8"]]
- 004f69a0 ["CALL", null, ["callee:00c57e90:8"]]
+ 004f69e0 ["INT_ADD", "register:40f0:8", ["const:4f69e0:8", "const:4:8"]]
+ 004f69e0 ["CALL", null, ["callee:00c57e90:8"]]
- 004f69a0 bytes 3c841d94
+ 004f69e0 bytes 2c851d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7a886bceeb558ca3883b91306b9b1f0"></a>

### [`004f6a38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f6/004f6a38.md) → [`004f6a78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f6/004f6a78.md) _ZNK5Botan7SHA_25610copy_stateEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`0053616c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/0053616c.md) [`00540264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540264.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005361ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/005361ac.md) [`005402a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005402a4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f6aac",
      "incomplete_value": true,
      "site": "004f6ab0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004f6a6c",
      "incomplete_value": true,
      "site": "004f6a70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004f6ad8",
      "incomplete_value": true,
      "site": "004f6ae0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004f6a98",
      "incomplete_value": true,
      "site": "004f6aa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004f6aa0",
      "READ",
      [
        "storage",
        "00c9ab38",
        null,
        "pointer"
      ]
    ],
    [
      "004f6ab0",
      "DATA",
      [
        "storage",
        "00c668d8",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "004f6ac8",
      "READ",
      [
        "storage",
        "00c9ab50",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004f6aa0",
      "READ",
      [
        "storage",
        "00c9af38",
        null,
        "pointer"
      ]
    ],
    [
      "004f6ab0",
      "DATA",
      [
        "storage",
        "00c66cd8",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "004f6ac8",
      "READ",
      [
        "storage",
        "00c9af50",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f6a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f6/004f6a38.md#insn-004f6a60) · [`004f6ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f6/004f6a38.md#insn-004f6ab0) · [`004f6a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f6/004f6a38.md#insn-004f6a54)
- 新版 [`004f6aa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f6/004f6a78.md#insn-004f6aa0) · [`004f6af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f6/004f6a78.md#insn-004f6af0) · [`004f6a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f6/004f6a78.md#insn-004f6a94)

~~~diff
- 004f6a60 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b38:8"]]
- 004f6a60 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f6aa0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f38:8"]]
+ 004f6aa0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004f6a60 bytes 089d45f9
+ 004f6aa0 bytes 089d47f9
- 004f6ab0 ["INT_ADD", "register:40f0:8", ["const:4f6ab0:8", "const:4:8"]]
- 004f6ab0 ["CALL", null, ["callee:005361ac:8"]]
+ 004f6af0 ["INT_ADD", "register:40f0:8", ["const:4f6af0:8", "const:4:8"]]
+ 004f6af0 ["CALL", null, ["callee:005361ac:8"]]
- 004f6ab0 bytes affd0094
+ 004f6af0 bytes affd0094
- 004f6a54 ["INT_ADD", "register:40f0:8", ["const:4f6a54:8", "const:4:8"]]
- 004f6a54 ["CALL", null, ["callee:00c57e90:8"]]
+ 004f6a94 ["INT_ADD", "register:40f0:8", ["const:4f6a94:8", "const:4:8"]]
+ 004f6a94 ["CALL", null, ["callee:00c57e90:8"]]
- 004f6a54 bytes 0f841d94
+ 004f6a94 bytes ff841d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c40533b75133289265b40286e8f3026"></a>

### [`004f89b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f89b0.md) → [`004f89f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f8/004f89f0.md) _ZN5Botan7SHA_2245clearEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f8a24",
      "incomplete_value": true,
      "site": "004f8a30",
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
                "const:210:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f89e4",
      "incomplete_value": true,
      "site": "004f89f0",
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
                "const:1d0:8"
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
      "definition_site": "004f8a28",
      "incomplete_value": true,
      "site": "004f8a30",
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
                "const:c10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f89e8",
      "incomplete_value": true,
      "site": "004f89f0",
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
                "const:bd0:8"
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
      "004f8a24",
      "READ",
      [
        "storage",
        "002c31d0",
        null,
        null
      ]
    ],
    [
      "004f8a28",
      "READ",
      [
        "storage",
        "002c2bd0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004f8a24",
      "READ",
      [
        "storage",
        "002c3210",
        null,
        null
      ]
    ],
    [
      "004f8a28",
      "READ",
      [
        "storage",
        "002c2c10",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f89d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f89b0.md#insn-004f89d4) · [`004f89e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f89b0.md#insn-004f89e4) · [`004f89e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f89b0.md#insn-004f89e8)
- 新版 [`004f8a14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f8/004f89f0.md#insn-004f8a14) · [`004f8a24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f8/004f89f0.md#insn-004f8a24) · [`004f8a28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f8/004f89f0.md#insn-004f8a28)

~~~diff
- 004f89d4 ["INT_ADD", "register:40f0:8", ["const:4f89d4:8", "const:4:8"]]
- 004f89d4 ["CALL", null, ["callee:00c58090:8"]]
+ 004f8a14 ["INT_ADD", "register:40f0:8", ["const:4f8a14:8", "const:4:8"]]
+ 004f8a14 ["CALL", null, ["callee:00c58090:8"]]
- 004f89d4 bytes af7c1d94
+ 004f8a14 bytes 9f7d1d94
- 004f89e4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:1d0:8"]]
- 004f89e4 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 004f89e4 ["COPY", "register:5010:8", ["const:0:8"]]
- 004f89e4 ["COPY", "register:5018:8", ["const:0:8"]]
+ 004f8a24 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:210:8"]]
+ 004f8a24 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
+ 004f8a24 ["COPY", "register:5010:8", ["const:0:8"]]
+ 004f8a24 ["COPY", "register:5018:8", ["const:0:8"]]
- 004f89e4 bytes 2075c03d
+ 004f8a24 bytes 2085c03d
- 004f89e8 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:bd0:8"]]
- 004f89e8 ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
- 004f89e8 ["COPY", "register:5030:8", ["const:0:8"]]
- 004f89e8 ["COPY", "register:5038:8", ["const:0:8"]]
+ 004f8a28 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:c10:8"]]
+ 004f8a28 ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
+ 004f8a28 ["COPY", "register:5030:8", ["const:0:8"]]
+ 004f8a28 ["COPY", "register:5038:8", ["const:0:8"]]
- 004f89e8 bytes 41f5c23d
+ 004f8a28 bytes 4105c33d
~~~


<a id="compare-79f52bd8b55612ae5d371ee3308b150d"></a>

### [`004f8a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8a78.md) → [`004f8ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f8/004f8ab8.md) _ZN5Botan7SHA_2565clearEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f8aec",
      "incomplete_value": true,
      "site": "004f8af8",
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
                "const:160:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f8aac",
      "incomplete_value": true,
      "site": "004f8ab8",
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f8af0",
      "incomplete_value": true,
      "site": "004f8af8",
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
                "const:cf0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f8ab0",
      "incomplete_value": true,
      "site": "004f8ab8",
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
                "const:cb0:8"
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
      "004f8aec",
      "READ",
      [
        "storage",
        "002c3120",
        null,
        null
      ]
    ],
    [
      "004f8af0",
      "READ",
      [
        "storage",
        "002c2cb0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004f8aec",
      "READ",
      [
        "storage",
        "002c3160",
        null,
        null
      ]
    ],
    [
      "004f8af0",
      "READ",
      [
        "storage",
        "002c2cf0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f8a9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8a78.md#insn-004f8a9c) · [`004f8aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8a78.md#insn-004f8aac) · [`004f8ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8a78.md#insn-004f8ab0)
- 新版 [`004f8adc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f8/004f8ab8.md#insn-004f8adc) · [`004f8aec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f8/004f8ab8.md#insn-004f8aec) · [`004f8af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f8/004f8ab8.md#insn-004f8af0)

~~~diff
- 004f8a9c ["INT_ADD", "register:40f0:8", ["const:4f8a9c:8", "const:4:8"]]
- 004f8a9c ["CALL", null, ["callee:00c58090:8"]]
+ 004f8adc ["INT_ADD", "register:40f0:8", ["const:4f8adc:8", "const:4:8"]]
+ 004f8adc ["CALL", null, ["callee:00c58090:8"]]
- 004f8a9c bytes 7d7c1d94
+ 004f8adc bytes 6d7d1d94
- 004f8aac ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:120:8"]]
- 004f8aac ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 004f8aac ["COPY", "register:5010:8", ["const:0:8"]]
- 004f8aac ["COPY", "register:5018:8", ["const:0:8"]]
+ 004f8aec ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:160:8"]]
+ 004f8aec ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
+ 004f8aec ["COPY", "register:5010:8", ["const:0:8"]]
+ 004f8aec ["COPY", "register:5018:8", ["const:0:8"]]
- 004f8aac bytes 2049c03d
+ 004f8aec bytes 2059c03d
- 004f8ab0 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:cb0:8"]]
- 004f8ab0 ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
- 004f8ab0 ["COPY", "register:5030:8", ["const:0:8"]]
- 004f8ab0 ["COPY", "register:5038:8", ["const:0:8"]]
+ 004f8af0 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:cf0:8"]]
+ 004f8af0 ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
+ 004f8af0 ["COPY", "register:5030:8", ["const:0:8"]]
+ 004f8af0 ["COPY", "register:5038:8", ["const:0:8"]]
- 004f8ab0 bytes 412dc33d
+ 004f8af0 bytes 413dc33d
~~~


<a id="compare-70d045b30a32fac62ef7b526008c278d"></a>

### [`004f8d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8d68.md) → [`004f8da8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f8/004f8da8.md) _ZN5Botan10system_rngEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c593b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c593b0.md) · 呼出先 5件 [`004f8df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8df0.md) [`004f8f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8f2c.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 1件 [`00c597b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c597b0.md) · 呼出先 5件 [`004f8e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f8/004f8e30.md) [`004f8f6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f8/004f8f6c.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `return_value_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f8ddc",
      "incomplete_value": false,
      "site": "004f8de0",
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
            "const:290:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f8d9c",
      "incomplete_value": false,
      "site": "004f8da0",
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
            "const:e90:8"
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
      "definition_site": "004f8df0",
      "incomplete_value": false,
      "site": "004f8e04",
      "value": [
        "leaf",
        "const:4f8f6c:8"
      ]
    },
    "old": {
      "definition_site": "004f8db0",
      "incomplete_value": false,
      "site": "004f8dc4",
      "value": [
        "leaf",
        "const:4f8f2c:8"
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f8df8",
      "incomplete_value": false,
      "site": "004f8e04",
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
            "const:280:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f8db8",
      "incomplete_value": false,
      "site": "004f8dc4",
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
            "const:e80:8"
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
      "004f8dbc",
      "READ",
      [
        "storage",
        "00ca4e90",
        null,
        "undefined1"
      ]
    ],
    [
      "004f8dc8",
      "DATA",
      [
        "storage",
        "00ca4e80",
        null,
        "undefined8"
      ]
    ],
    [
      "004f8ddc",
      "PARAM",
      [
        "storage",
        "00ca4e90",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "004f8dbc",
      "READ",
      [
        "storage",
        "00ca5290",
        null,
        "undefined1"
      ]
    ],
    [
      "004f8dc8",
      "DATA",
      [
        "storage",
        "00ca5280",
        null,
        "undefined8"
      ]
    ],
    [
      "004f8ddc",
      "PARAM",
      [
        "storage",
        "00ca5290",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f8d84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8d68.md#insn-004f8d84) · [`004f8da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8d68.md#insn-004f8da0) · [`004f8dc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8d68.md#insn-004f8dc4)
- 新版 [`004f8dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f8/004f8da8.md#insn-004f8dc4) · [`004f8de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f8/004f8da8.md#insn-004f8de0) · [`004f8e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f8/004f8da8.md#insn-004f8e04)

~~~diff
- 004f8d84 ["COPY", "register:4000:8", ["const:ca4000:8"]]
+ 004f8dc4 ["COPY", "register:4000:8", ["const:ca5000:8"]]
- 004f8d84 bytes 603d0090
+ 004f8dc4 bytes 603d00b0
- 004f8da0 ["INT_ADD", "register:40f0:8", ["const:4f8da0:8", "const:4:8"]]
- 004f8da0 ["CALL", null, ["callee:00c57e50:8"]]
+ 004f8de0 ["INT_ADD", "register:40f0:8", ["const:4f8de0:8", "const:4:8"]]
+ 004f8de0 ["CALL", null, ["callee:00c57e50:8"]]
- 004f8da0 bytes 2c7b1d94
+ 004f8de0 bytes 1c7c1d94
- 004f8dc4 ["INT_ADD", "register:40f0:8", ["const:4f8dc4:8", "const:4:8"]]
- 004f8dc4 ["CALL", null, ["callee:00c57e30:8"]]
+ 004f8e04 ["INT_ADD", "register:40f0:8", ["const:4f8e04:8", "const:4:8"]]
+ 004f8e04 ["CALL", null, ["callee:00c57e30:8"]]
- 004f8dc4 bytes 1b7b1d94
+ 004f8e04 bytes 0b7c1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5f2aecf8bf9aa52b1eb281d01e2ff3e"></a>

### [`004f8df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8df0.md) → [`004f8e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f8/004f8e30.md) FUN_004f8e30

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`004f8d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8d68.md) [`00535f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535f24.md) · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 2件 [`004f8da8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f8/004f8da8.md) [`00535f64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535f64.md) · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 88.33% / 新版 88.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "004f8e6c",
      "incomplete_value": false,
      "site": "004f8e6c",
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
            "const:280:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f8e2c",
      "incomplete_value": false,
      "site": "004f8e2c",
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
            "const:e80:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004f8e68",
      "incomplete_value": false,
      "site": "004f8e6c",
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
            "const:2a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f8e28",
      "incomplete_value": false,
      "site": "004f8e2c",
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
            "const:ea0:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "004f8e90",
      "incomplete_value": false,
      "site": "004f8e90",
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
            "const:288:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f8e50",
      "incomplete_value": false,
      "site": "004f8e50",
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
            "const:e88:8"
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
      "004f8e58",
      "PARAM",
      [
        "storage",
        "002b8ddd",
        null,
        "string"
      ]
    ],
    [
      "004f8e6c",
      "WRITE",
      [
        "storage",
        "00ca4e80",
        null,
        "undefined8"
      ]
    ],
    [
      "004f8e6c",
      "DATA",
      [
        "storage",
        "00c69ea0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004f8e58",
      "PARAM",
      [
        "storage",
        "002b8e1d",
        null,
        "string"
      ]
    ],
    [
      "004f8e6c",
      "WRITE",
      [
        "storage",
        "00ca5280",
        null,
        "undefined8"
      ]
    ],
    [
      "004f8e6c",
      "DATA",
      [
        "storage",
        "00c6a2a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f8e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8df0.md#insn-004f8e08) · [`004f8e30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8df0.md#insn-004f8e30) · [`004f8e48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8df0.md#insn-004f8e48)
- 新版 [`004f8e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f8/004f8e30.md#insn-004f8e48) · [`004f8e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f8/004f8e30.md#insn-004f8e70) · [`004f8e88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f8/004f8e30.md#insn-004f8e88)

~~~diff
- 004f8e08 ["COPY", "register:40a0:8", ["const:ca4000:8"]]
+ 004f8e48 ["COPY", "register:40a0:8", ["const:ca5000:8"]]
- 004f8e08 bytes 743d0090
+ 004f8e48 bytes 743d00b0
- 004f8e30 ["INT_ADD", "register:40f0:8", ["const:4f8e30:8", "const:4:8"]]
- 004f8e30 ["CALL", null, ["callee:00c597c0:8"]]
+ 004f8e70 ["INT_ADD", "register:40f0:8", ["const:4f8e70:8", "const:4:8"]]
+ 004f8e70 ["CALL", null, ["callee:00c597c0:8"]]
- 004f8e30 bytes 64811d94
+ 004f8e70 bytes 54821d94
- 004f8e48 ["INT_ADD", "register:40f0:8", ["const:4f8e48:8", "const:4:8"]]
- 004f8e48 ["CALL", null, ["callee:00c597c0:8"]]
+ 004f8e88 ["INT_ADD", "register:40f0:8", ["const:4f8e88:8", "const:4:8"]]
+ 004f8e88 ["CALL", null, ["callee:00c597c0:8"]]
- 004f8e48 bytes 5e811d94
+ 004f8e88 bytes 4e821d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31de62ce9b7f3606ac3e4417fd37ab95"></a>

### [`004f8f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8f5c.md) → [`004f8f9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f8/004f8f9c.md) _ZNK5Botan14calendar_point9to_stringEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 12件 [`00451870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451870.md) [`00459490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ba0.md)
- 新版 呼出元 0件  · 呼出先 12件 [`004518b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004518b0.md) [`004594d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fa0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 95.62% / 新版 95.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

アドレスに依存する影響 `store_destination` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f9140",
      "incomplete_value": true,
      "site": "004f9148",
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
      "definition_site": "004f9100",
      "incomplete_value": true,
      "site": "004f9108",
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
      "definition_site": "004f9150",
      "incomplete_value": true,
      "site": "004f9150",
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
      "definition_site": "004f9110",
      "incomplete_value": true,
      "site": "004f9110",
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
      "definition_site": "004f9150",
      "incomplete_value": true,
      "site": "004f9150",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004f9110",
      "incomplete_value": true,
      "site": "004f9110",
      "value": [
        "LOAD",
        "8",
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
      "004f9004",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "004f9004",
      "PARAM",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "004f9050",
      "PARAM",
      [
        "storage",
        "002b8f1f",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004f9004",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      "004f9004",
      "PARAM",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "004f9050",
      "PARAM",
      [
        "storage",
        "002b8f5f",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f8fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8f5c.md#insn-004f8fc8) · [`004f8fd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8f5c.md#insn-004f8fd8) · [`004f9008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f8/004f8f5c.md#insn-004f9008)
- 新版 [`004f9008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f8/004f8f9c.md#insn-004f9008) · [`004f9018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f8/004f8f9c.md#insn-004f9018) · [`004f9048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f8/004f8f9c.md#insn-004f9048)

~~~diff
- 004f8fc8 ["INT_ADD", "register:40f0:8", ["const:4f8fc8:8", "const:4:8"]]
- 004f8fc8 ["CALL", null, ["callee:00c58280:8"]]
+ 004f9008 ["INT_ADD", "register:40f0:8", ["const:4f9008:8", "const:4:8"]]
+ 004f9008 ["CALL", null, ["callee:00c58280:8"]]
- 004f8fc8 bytes ae7b1d94
+ 004f9008 bytes 9e7c1d94
- 004f8fd8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004f8fd8 ["INT_ADD", "register:40f0:8", ["const:4f8fd8:8", "const:4:8"]]
- 004f8fd8 ["CALLIND", null, ["register:0:8"]]
+ 004f9018 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004f9018 ["INT_ADD", "register:40f0:8", ["const:4f9018:8", "const:4:8"]]
+ 004f9018 ["CALLIND", null, ["register:0:8"]]
- 004f8fd8 bytes 00013fd6
+ 004f9018 bytes 00013fd6
- 004f9008 ["INT_ADD", "register:40f0:8", ["const:4f9008:8", "const:4:8"]]
- 004f9008 ["CALL", null, ["callee:00c58960:8"]]
+ 004f9048 ["INT_ADD", "register:40f0:8", ["const:4f9048:8", "const:4:8"]]
+ 004f9048 ["CALL", null, ["callee:00c58960:8"]]
- 004f9008 bytes 567d1d94
+ 004f9048 bytes 467e1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-300e669458a5f88a244591e39937569d"></a>

### [`004f91d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f91d0.md) → [`004f9210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f9/004f9210.md) FUN_004f9210

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`004ad96c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004ad96c.md) [`004adaa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ad/004adaa4.md) · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 2件 [`004ad9ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004ad9ac.md) [`004adae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004adae4.md) · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.52% / 新版 96.52%

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
      "definition_site": "004f9338",
      "incomplete_value": false,
      "site": "004f9340",
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
            "const:195:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f92f8",
      "incomplete_value": false,
      "site": "004f9300",
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
            "const:155:8"
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
      "definition_site": "004f9370",
      "incomplete_value": true,
      "site": "004f937c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f9330",
      "incomplete_value": true,
      "site": "004f933c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f936c",
      "incomplete_value": false,
      "site": "004f937c",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004f932c",
      "incomplete_value": false,
      "site": "004f933c",
      "value": [
        "leaf",
        "const:535828:8"
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
      "004f9338",
      "PARAM",
      [
        "storage",
        "002b6155",
        null,
        "string"
      ]
    ],
    [
      "004f936c",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004f9370",
      "READ",
      [
        "storage",
        "00c9a950",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004f9338",
      "PARAM",
      [
        "storage",
        "002b6195",
        null,
        "string"
      ]
    ],
    [
      "004f936c",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004f9370",
      "READ",
      [
        "storage",
        "00c9ad50",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f9300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f91d0.md#insn-004f9300) · [`004f933c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f91d0.md#insn-004f933c) · [`004f935c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f91d0.md#insn-004f935c)
- 新版 [`004f9340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f9/004f9210.md#insn-004f9340) · [`004f937c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f9/004f9210.md#insn-004f937c) · [`004f939c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f9/004f9210.md#insn-004f939c)

~~~diff
- 004f9300 ["INT_ADD", "register:40f0:8", ["const:4f9300:8", "const:4:8"]]
- 004f9300 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004f9340 ["INT_ADD", "register:40f0:8", ["const:4f9340:8", "const:4:8"]]
+ 004f9340 ["CALL", null, ["callee:0043ddd8:8"]]
- 004f9300 bytes a612fd97
+ 004f9340 bytes a612fd97
- 004f933c ["INT_ADD", "register:40f0:8", ["const:4f933c:8", "const:4:8"]]
- 004f933c ["CALL", null, ["callee:00c57f10:8"]]
+ 004f937c ["INT_ADD", "register:40f0:8", ["const:4f937c:8", "const:4:8"]]
+ 004f937c ["CALL", null, ["callee:00c57f10:8"]]
- 004f933c bytes f5791d94
+ 004f937c bytes e57a1d94
- 004f935c ["INT_ADD", "register:40f0:8", ["const:4f935c:8", "const:4:8"]]
- 004f935c ["CALL", null, ["callee:0043ddd8:8"]]
+ 004f939c ["INT_ADD", "register:40f0:8", ["const:4f939c:8", "const:4:8"]]
+ 004f939c ["CALL", null, ["callee:0043ddd8:8"]]
- 004f935c bytes 8f12fd97
+ 004f939c bytes 8f12fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93742e1280ca5dec3f9d00f3fb33ee29"></a>

### [`004f93e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f93e8.md) → [`004f9428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f9/004f9428.md) _ZN5Botan7Charset9transcodeERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS_13Character_SetESA_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 14件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004a680c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a680c.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004a684c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a684c.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.03% / 新版 97.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f966c",
      "incomplete_value": false,
      "site": "004f9674",
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
            "const:9f1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f962c",
      "incomplete_value": false,
      "site": "004f9634",
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
            "const:9b1:8"
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
      "definition_site": "004f96a4",
      "incomplete_value": true,
      "site": "004f96b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f9664",
      "incomplete_value": true,
      "site": "004f9670",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f96a0",
      "incomplete_value": false,
      "site": "004f96b0",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004f9660",
      "incomplete_value": false,
      "site": "004f9670",
      "value": [
        "leaf",
        "const:535828:8"
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
      "004f966c",
      "PARAM",
      [
        "storage",
        "002ae9b1",
        null,
        "string"
      ]
    ],
    [
      "004f96a0",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004f96a4",
      "READ",
      [
        "storage",
        "00c9a950",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004f966c",
      "PARAM",
      [
        "storage",
        "002ae9f1",
        null,
        "string"
      ]
    ],
    [
      "004f96a0",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004f96a4",
      "READ",
      [
        "storage",
        "00c9ad50",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f9634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f93e8.md#insn-004f9634) · [`004f9664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f93e8.md#insn-004f9664) · [`004f9670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f93e8.md#insn-004f9670)
- 新版 [`004f9674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f9/004f9428.md#insn-004f9674) · [`004f96a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f9/004f9428.md#insn-004f96a4) · [`004f96b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f9/004f9428.md#insn-004f96b0)

~~~diff
- 004f9634 ["INT_ADD", "register:40f0:8", ["const:4f9634:8", "const:4:8"]]
- 004f9634 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004f9674 ["INT_ADD", "register:40f0:8", ["const:4f9674:8", "const:4:8"]]
+ 004f9674 ["CALL", null, ["callee:0043ddd8:8"]]
- 004f9634 bytes d911fd97
+ 004f9674 bytes d911fd97
- 004f9664 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:950:8"]]
- 004f9664 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f96a4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d50:8"]]
+ 004f96a4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004f9664 bytes 21a844f9
+ 004f96a4 bytes 21a846f9
- 004f9670 ["INT_ADD", "register:40f0:8", ["const:4f9670:8", "const:4:8"]]
- 004f9670 ["CALL", null, ["callee:00c57f10:8"]]
+ 004f96b0 ["INT_ADD", "register:40f0:8", ["const:4f96b0:8", "const:4:8"]]
+ 004f96b0 ["CALL", null, ["callee:00c57f10:8"]]
- 004f9670 bytes 28791d94
+ 004f96b0 bytes 187a1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-168627df70c51b2e0c3cdb0a954a90a5"></a>

### [`004f9ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f9ac8.md) → [`004f9b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f9/004f9b08.md) _ZN5Botan17DataSource_MemoryC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c590c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c590c0.md) · 呼出先 1件 [`00540388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540388.md)
- 新版 呼出元 1件 [`00c594c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c594c0.md) · 呼出先 1件 [`005403c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005403c8.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.96% / 新版 86.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004f9b20",
      "incomplete_value": true,
      "site": "004f9b24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004f9ae0",
      "incomplete_value": true,
      "site": "004f9ae4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004f9b1c",
      "READ",
      [
        "storage",
        "00c9a9e0",
        null,
        "pointer"
      ]
    ],
    [
      "004f9b24",
      "DATA",
      [
        "storage",
        "00c66f88",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "004f9b1c",
      "READ",
      [
        "storage",
        "00c9ade0",
        null,
        "pointer"
      ]
    ],
    [
      "004f9b24",
      "DATA",
      [
        "storage",
        "00c67388",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f9adc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f9ac8.md#insn-004f9adc) · [`004f9b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f9ac8.md#insn-004f9b10)
- 新版 [`004f9b1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f9/004f9b08.md#insn-004f9b1c) · [`004f9b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f9/004f9b08.md#insn-004f9b50)

~~~diff
- 004f9adc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9e0:8"]]
- 004f9adc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004f9b1c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:de0:8"]]
+ 004f9b1c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004f9adc bytes 08f144f9
+ 004f9b1c bytes 08f146f9
- 004f9b10 ["INT_ADD", "register:40f0:8", ["const:4f9b10:8", "const:4:8"]]
- 004f9b10 ["CALL", null, ["callee:005403c8:8"]]
+ 004f9b50 ["INT_ADD", "register:40f0:8", ["const:4f9b50:8", "const:4:8"]]
+ 004f9b50 ["CALL", null, ["callee:005403c8:8"]]
- 004f9b10 bytes 1e1a0194
+ 004f9b50 bytes 1e1a0194
~~~


<a id="compare-5b1b17517caf70abab0a1b345e2cfe36"></a>

### [`004f9b24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f9b24.md) → [`004f9b64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f9/004f9b64.md) _ZN5Botan17DataSource_Stream4readEPhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.36% / 新版 96.36%

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
      "definition_site": "004f9bf0",
      "incomplete_value": false,
      "site": "004f9bf8",
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
            "const:7de:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f9bb0",
      "incomplete_value": false,
      "site": "004f9bb8",
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
            "const:79e:8"
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
      "definition_site": "004f9c2c",
      "incomplete_value": true,
      "site": "004f9c38",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f9bec",
      "incomplete_value": true,
      "site": "004f9bf8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f9c28",
      "incomplete_value": false,
      "site": "004f9c38",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004f9be8",
      "incomplete_value": false,
      "site": "004f9bf8",
      "value": [
        "leaf",
        "const:535828:8"
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
      "004f9bf0",
      "PARAM",
      [
        "storage",
        "002ad79e",
        null,
        "string"
      ]
    ],
    [
      "004f9c28",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004f9c2c",
      "READ",
      [
        "storage",
        "00c9a980",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004f9bf0",
      "PARAM",
      [
        "storage",
        "002ad7de",
        null,
        "string"
      ]
    ],
    [
      "004f9c28",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004f9c2c",
      "READ",
      [
        "storage",
        "00c9ad80",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f9bb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f9b24.md#insn-004f9bb8) · [`004f9bf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f9b24.md#insn-004f9bf8) · [`004f9b4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f9b24.md#insn-004f9b4c)
- 新版 [`004f9bf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f9/004f9b64.md#insn-004f9bf8) · [`004f9c38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f9/004f9b64.md#insn-004f9c38) · [`004f9b8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f9/004f9b64.md#insn-004f9b8c)

~~~diff
- 004f9bb8 ["INT_ADD", "register:40f0:8", ["const:4f9bb8:8", "const:4:8"]]
- 004f9bb8 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004f9bf8 ["INT_ADD", "register:40f0:8", ["const:4f9bf8:8", "const:4:8"]]
+ 004f9bf8 ["CALL", null, ["callee:0043ddd8:8"]]
- 004f9bb8 bytes 7810fd97
+ 004f9bf8 bytes 7810fd97
- 004f9bf8 ["INT_ADD", "register:40f0:8", ["const:4f9bf8:8", "const:4:8"]]
- 004f9bf8 ["CALL", null, ["callee:00c57f10:8"]]
+ 004f9c38 ["INT_ADD", "register:40f0:8", ["const:4f9c38:8", "const:4:8"]]
+ 004f9c38 ["CALL", null, ["callee:00c57f10:8"]]
- 004f9bf8 bytes c6771d94
+ 004f9c38 bytes b6781d94
- 004f9b4c ["INT_ADD", "register:40f0:8", ["const:4f9b4c:8", "const:4:8"]]
- 004f9b4c ["CALL", null, ["callee:00c590d0:8"]]
+ 004f9b8c ["INT_ADD", "register:40f0:8", ["const:4f9b8c:8", "const:4:8"]]
+ 004f9b8c ["CALL", null, ["callee:00c590d0:8"]]
- 004f9b4c bytes 617c1d94
+ 004f9b8c bytes 517d1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a285aa55e01cc9e1574985576307ce95"></a>

### [`004f9cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f9cb8.md) → [`004f9cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f9/004f9cf8.md) _ZNK5Botan17DataSource_Stream4peekEPhmm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 13件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

アドレスに依存する影響 `call_argument_candidate` 3件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004f9da8",
      "incomplete_value": true,
      "site": "004f9da8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f9d68",
      "incomplete_value": true,
      "site": "004f9d68",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004f9e6c",
      "incomplete_value": false,
      "site": "004f9e74",
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
            "const:8d2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f9e2c",
      "incomplete_value": false,
      "site": "004f9e34",
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
            "const:892:8"
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
      "definition_site": "004f9ea4",
      "incomplete_value": true,
      "site": "004f9eb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004f9e64",
      "incomplete_value": true,
      "site": "004f9e70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004f9d98",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004f9e6c",
      "PARAM",
      [
        "storage",
        "002ae892",
        null,
        "string"
      ]
    ],
    [
      "004f9ea0",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004f9d98",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004f9e6c",
      "PARAM",
      [
        "storage",
        "002ae8d2",
        null,
        "string"
      ]
    ],
    [
      "004f9ea0",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004f9d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f9cb8.md#insn-004f9d68) · [`004f9e34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f9cb8.md#insn-004f9e34) · [`004f9e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f9cb8.md#insn-004f9e70)
- 新版 [`004f9da8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f9/004f9cf8.md#insn-004f9da8) · [`004f9e74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f9/004f9cf8.md#insn-004f9e74) · [`004f9eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f9/004f9cf8.md#insn-004f9eb0)

~~~diff
- 004f9d68 ["COPY", "register:0:8", ["register:4048:8"]]
- 004f9d68 ["INT_ADD", "register:40f0:8", ["const:4f9d68:8", "const:4:8"]]
- 004f9d68 ["CALLIND", null, ["register:0:8"]]
+ 004f9da8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004f9da8 ["INT_ADD", "register:40f0:8", ["const:4f9da8:8", "const:4:8"]]
+ 004f9da8 ["CALLIND", null, ["register:0:8"]]
- 004f9d68 bytes 20013fd6
+ 004f9da8 bytes 20013fd6
- 004f9e34 ["INT_ADD", "register:40f0:8", ["const:4f9e34:8", "const:4:8"]]
- 004f9e34 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004f9e74 ["INT_ADD", "register:40f0:8", ["const:4f9e74:8", "const:4:8"]]
+ 004f9e74 ["CALL", null, ["callee:0043ddd8:8"]]
- 004f9e34 bytes d90ffd97
+ 004f9e74 bytes d90ffd97
- 004f9e70 ["INT_ADD", "register:40f0:8", ["const:4f9e70:8", "const:4:8"]]
- 004f9e70 ["CALL", null, ["callee:00c57f10:8"]]
+ 004f9eb0 ["INT_ADD", "register:40f0:8", ["const:4f9eb0:8", "const:4:8"]]
+ 004f9eb0 ["CALL", null, ["callee:00c57f10:8"]]
- 004f9e70 bytes 28771d94
+ 004f9eb0 bytes 18781d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3e0eb04e66fe59b6290d241f071bc32"></a>

### [`004fa014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa014.md) → [`004fa054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fa054.md) _ZN5Botan17DataSource_StreamC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEb

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59260.md) · 呼出先 9件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`004fa1d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa1d0.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00c59660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59660.md) · 呼出先 9件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`004fa210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fa210.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.51% / 新版 93.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fa094",
      "incomplete_value": true,
      "site": "004fa094",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fa054",
      "incomplete_value": true,
      "site": "004fa054",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004fa138",
      "incomplete_value": false,
      "site": "004fa144",
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
            "const:902:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fa0f8",
      "incomplete_value": false,
      "site": "004fa104",
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
            "const:8c2:8"
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
      "definition_site": "004fa174",
      "incomplete_value": true,
      "site": "004fa180",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fa134",
      "incomplete_value": true,
      "site": "004fa140",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004fa078",
      "READ",
      [
        "storage",
        "00c9ac28",
        null,
        "pointer"
      ]
    ],
    [
      "004fa094",
      "DATA",
      [
        "storage",
        "00c66fd8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004fa138",
      "PARAM",
      [
        "storage",
        "002ae8c2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004fa078",
      "READ",
      [
        "storage",
        "00c9b028",
        null,
        "pointer"
      ]
    ],
    [
      "004fa094",
      "DATA",
      [
        "storage",
        "00c673d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004fa138",
      "PARAM",
      [
        "storage",
        "002ae902",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fa104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa014.md#insn-004fa104) · [`004fa140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa014.md#insn-004fa140) · [`004fa02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa014.md#insn-004fa02c)
- 新版 [`004fa144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fa054.md#insn-004fa144) · [`004fa180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fa054.md#insn-004fa180) · [`004fa06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fa054.md#insn-004fa06c)

~~~diff
- 004fa104 ["INT_ADD", "register:40f0:8", ["const:4fa104:8", "const:4:8"]]
- 004fa104 ["CALL", null, ["callee:00c580b0:8"]]
+ 004fa144 ["INT_ADD", "register:40f0:8", ["const:4fa144:8", "const:4:8"]]
+ 004fa144 ["CALL", null, ["callee:00c580b0:8"]]
- 004fa104 bytes eb761d94
+ 004fa144 bytes db771d94
- 004fa140 ["INT_ADD", "register:40f0:8", ["const:4fa140:8", "const:4:8"]]
- 004fa140 ["CALL", null, ["callee:00c57f10:8"]]
+ 004fa180 ["INT_ADD", "register:40f0:8", ["const:4fa180:8", "const:4:8"]]
+ 004fa180 ["CALL", null, ["callee:00c57f10:8"]]
- 004fa140 bytes 74761d94
+ 004fa180 bytes 64771d94
- 004fa02c ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 004fa06c ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 004fa02c bytes 083d0090
+ 004fa06c bytes 083d00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32356d63bf828ee5785935e311adab75"></a>

### [`004fa1d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa1d0.md) → [`004fa210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fa210.md) FUN_004fa210

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004fa014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa014.md) · 呼出先 4件 [`00c57de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57de0.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c58b00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58b00.md) [`00c58b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58b10.md)
- 新版 呼出元 1件 [`004fa054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fa054.md) · 呼出先 4件 [`00c581e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581e0.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c58f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58f00.md) [`00c58f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58f10.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fa254",
      "incomplete_value": true,
      "site": "004fa254",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004fa214",
      "incomplete_value": true,
      "site": "004fa214",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004fa24c",
      "incomplete_value": true,
      "site": "004fa258",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004fa20c",
      "incomplete_value": true,
      "site": "004fa218",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004fa264",
      "incomplete_value": true,
      "site": "004fa264",
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
      "definition_site": "004fa224",
      "incomplete_value": true,
      "site": "004fa224",
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
      "004fa234",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      "004fa238",
      "READ",
      [
        "storage",
        "00c9ac38",
        null,
        "pointer"
      ]
    ],
    [
      "004fa24c",
      "READ",
      [
        "storage",
        "00c92cb0",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "004fa234",
      "READ",
      [
        "storage",
        "00c9b030",
        null,
        "pointer"
      ]
    ],
    [
      "004fa238",
      "READ",
      [
        "storage",
        "00c9b038",
        null,
        "pointer"
      ]
    ],
    [
      "004fa24c",
      "READ",
      [
        "storage",
        "00c930b0",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fa1e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa1d0.md#insn-004fa1e8) · [`004fa1ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa1d0.md#insn-004fa1ec) · [`004fa1f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa1d0.md#insn-004fa1f4)
- 新版 [`004fa228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fa210.md#insn-004fa228) · [`004fa22c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fa210.md#insn-004fa22c) · [`004fa234`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fa210.md#insn-004fa234)

~~~diff
- 004fa1e8 ["COPY", "register:40c8:8", ["const:c9a000:8"]]
+ 004fa228 ["COPY", "register:40c8:8", ["const:c9b000:8"]]
- 004fa1e8 bytes 193d0090
+ 004fa228 bytes 193d00b0
- 004fa1ec ["COPY", "register:40c0:8", ["const:c9a000:8"]]
+ 004fa22c ["COPY", "register:40c0:8", ["const:c9b000:8"]]
- 004fa1ec bytes 183d0090
+ 004fa22c bytes 183d00b0
- 004fa1f4 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:c30:8"]]
- 004fa1f4 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fa234 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:30:8"]]
+ 004fa234 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
- 004fa1f4 bytes 391b46f9
+ 004fa234 bytes 391b40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc4b444b2490518eb310cb335653e383"></a>

### [`004fa2e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa2e8.md) → [`004fa328`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fa328.md) _ZN5Botan17DataSource_StreamC2ERNSt6__ndk113basic_istreamIcNS1_11char_traitsIcEEEERKNS1_12basic_stringIcS4_NS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.96% / 新版 86.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fa348",
      "incomplete_value": true,
      "site": "004fa348",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fa308",
      "incomplete_value": true,
      "site": "004fa308",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004fa340",
      "READ",
      [
        "storage",
        "00c9ac28",
        null,
        "pointer"
      ]
    ],
    [
      "004fa348",
      "DATA",
      [
        "storage",
        "00c66fd8",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "004fa340",
      "READ",
      [
        "storage",
        "00c9b028",
        null,
        "pointer"
      ]
    ],
    [
      "004fa348",
      "DATA",
      [
        "storage",
        "00c673d8",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fa2f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa2e8.md#insn-004fa2f4) · [`004fa300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa2e8.md#insn-004fa300) · [`004fa32c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa2e8.md#insn-004fa32c)
- 新版 [`004fa334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fa328.md#insn-004fa334) · [`004fa340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fa328.md#insn-004fa340) · [`004fa36c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fa328.md#insn-004fa36c)

~~~diff
- 004fa2f4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 004fa334 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 004fa2f4 bytes 083d0090
+ 004fa334 bytes 083d00b0
- 004fa300 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c28:8"]]
- 004fa300 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fa340 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:28:8"]]
+ 004fa340 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004fa300 bytes 081546f9
+ 004fa340 bytes 081540f9
- 004fa32c ["INT_ADD", "register:40f0:8", ["const:4fa32c:8", "const:4:8"]]
- 004fa32c ["CALL", null, ["callee:0043bb20:8"]]
+ 004fa36c ["INT_ADD", "register:40f0:8", ["const:4fa36c:8", "const:4:8"]]
+ 004fa36c ["CALL", null, ["callee:0043bb20:8"]]
- 004fa32c bytes ed05fd97
+ 004fa36c bytes ed05fd97
~~~


<a id="compare-5963b51dc76b1fd000f824596d963987"></a>

### [`004fa3b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa3b4.md) → [`004fa3f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fa3f4.md) _ZN5Botan9ExceptionC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c583c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c583c0.md) · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)
- 新版 呼出元 1件 [`00c587c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c587c0.md) · 呼出先 1件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)

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
      "definition_site": "004fa410",
      "incomplete_value": true,
      "site": "004fa410",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fa3d0",
      "incomplete_value": true,
      "site": "004fa3d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004fa408",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "004fa410",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004fa408",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "004fa410",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fa3c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa3b4.md#insn-004fa3c8) · [`004fa3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa3b4.md#insn-004fa3f8)
- 新版 [`004fa408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fa3f4.md#insn-004fa408) · [`004fa438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fa3f4.md#insn-004fa438)

~~~diff
- 004fa3c8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 004fa3c8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fa408 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 004fa408 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004fa3c8 bytes 08e944f9
+ 004fa408 bytes 08e946f9
- 004fa3f8 ["INT_ADD", "register:40f0:8", ["const:4fa3f8:8", "const:4:8"]]
- 004fa3f8 ["CALL", null, ["callee:0043bb20:8"]]
+ 004fa438 ["INT_ADD", "register:40f0:8", ["const:4fa438:8", "const:4:8"]]
+ 004fa438 ["CALL", null, ["callee:0043bb20:8"]]
- 004fa3f8 bytes ba05fd97
+ 004fa438 bytes ba05fd97
~~~


<a id="compare-1b48e7902b260a0056fecbed06cb4102"></a>

### [`004fa41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa41c.md) → [`004fa45c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fa45c.md) _ZN5Botan9ExceptionC1EPKcRKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58380.md) · 呼出先 8件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 1件 [`00c58780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58780.md) · 呼出先 8件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.92% / 新版 95.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fa4a4",
      "incomplete_value": true,
      "site": "004fa4a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fa464",
      "incomplete_value": true,
      "site": "004fa464",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fa520",
      "incomplete_value": false,
      "site": "004fa528",
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
            "const:fc7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fa4e0",
      "incomplete_value": false,
      "site": "004fa4e8",
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
            "const:efa:8"
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
      "004fa488",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "004fa4a4",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004fa520",
      "PARAM",
      [
        "storage",
        "002a0efa",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004fa488",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "004fa4a4",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004fa520",
      "PARAM",
      [
        "storage",
        "002a0fc7",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fa4e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa41c.md#insn-004fa4e8) · [`004fa448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa41c.md#insn-004fa448) · [`004fa468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa41c.md#insn-004fa468)
- 新版 [`004fa528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fa45c.md#insn-004fa528) · [`004fa488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fa45c.md#insn-004fa488) · [`004fa4a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fa45c.md#insn-004fa4a8)

~~~diff
- 004fa4e8 ["INT_ADD", "register:40f0:8", ["const:4fa4e8:8", "const:4:8"]]
- 004fa4e8 ["CALL", null, ["callee:00c57f70:8"]]
+ 004fa528 ["INT_ADD", "register:40f0:8", ["const:4fa528:8", "const:4:8"]]
+ 004fa528 ["CALL", null, ["callee:00c57f70:8"]]
- 004fa4e8 bytes a2751d94
+ 004fa528 bytes 92761d94
- 004fa448 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:9d0:8"]]
- 004fa448 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fa488 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:dd0:8"]]
+ 004fa488 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004fa448 bytes 29e944f9
+ 004fa488 bytes 29e946f9
- 004fa468 ["INT_ADD", "register:40f0:8", ["const:4fa468:8", "const:4:8"]]
- 004fa468 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004fa4a8 ["INT_ADD", "register:40f0:8", ["const:4fa4a8:8", "const:4:8"]]
+ 004fa4a8 ["CALL", null, ["callee:00c57fe0:8"]]
- 004fa468 bytes de751d94
+ 004fa4a8 bytes ce761d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcd6d41a93dd3116f3281c55a17ed8b3"></a>

### [`004fa5f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa5f8.md) → [`004fa638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fa638.md) _ZN5Botan16Invalid_ArgumentC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58270.md) · 呼出先 1件 [`00c58380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58380.md)
- 新版 呼出元 1件 [`00c58670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58670.md) · 呼出先 1件 [`00c58780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58780.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fa660",
      "incomplete_value": true,
      "site": "004fa664",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fa620",
      "incomplete_value": true,
      "site": "004fa624",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004fa64c",
      "incomplete_value": false,
      "site": "004fa654",
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
            "const:44e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fa60c",
      "incomplete_value": false,
      "site": "004fa614",
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
            "const:372:8"
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
      "004fa64c",
      "PARAM",
      [
        "storage",
        "002a6372",
        null,
        "string"
      ]
    ],
    [
      "004fa65c",
      "READ",
      [
        "storage",
        "00c9a960",
        null,
        "pointer"
      ]
    ],
    [
      "004fa664",
      "DATA",
      [
        "storage",
        "00c67050",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004fa64c",
      "PARAM",
      [
        "storage",
        "002a644e",
        null,
        "string"
      ]
    ],
    [
      "004fa65c",
      "READ",
      [
        "storage",
        "00c9ad60",
        null,
        "pointer"
      ]
    ],
    [
      "004fa664",
      "DATA",
      [
        "storage",
        "00c67450",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fa614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa5f8.md#insn-004fa614) · [`004fa60c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa5f8.md#insn-004fa60c) · [`004fa61c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa5f8.md#insn-004fa61c)
- 新版 [`004fa654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fa638.md#insn-004fa654) · [`004fa64c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fa638.md#insn-004fa64c) · [`004fa65c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fa638.md#insn-004fa65c)

~~~diff
- 004fa614 ["INT_ADD", "register:40f0:8", ["const:4fa614:8", "const:4:8"]]
- 004fa614 ["CALL", null, ["callee:00c58780:8"]]
+ 004fa654 ["INT_ADD", "register:40f0:8", ["const:4fa654:8", "const:4:8"]]
+ 004fa654 ["CALL", null, ["callee:00c58780:8"]]
- 004fa614 bytes 5b771d94
+ 004fa654 bytes 4b781d94
- 004fa60c ["COPY", "tmp:0:8", ["const:372:8"]]
- 004fa60c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004fa60c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004fa60c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004fa64c ["COPY", "tmp:0:8", ["const:44e:8"]]
+ 004fa64c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004fa64c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004fa64c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004fa60c bytes 21c80d91
+ 004fa64c bytes 21381191
- 004fa61c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:960:8"]]
- 004fa61c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fa65c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d60:8"]]
+ 004fa65c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004fa61c bytes 08b144f9
+ 004fa65c bytes 08b146f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f482bd799e0b0221eb6bac4e67008d65"></a>

### [`004fa634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa634.md) → [`004fa674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fa674.md) _ZN5Botan16Invalid_ArgumentC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.05% / 新版 99.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fa7c4",
      "incomplete_value": true,
      "site": "004fa7c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fa784",
      "incomplete_value": true,
      "site": "004fa788",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004fa78c",
      "incomplete_value": false,
      "site": "004fa798",
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
            "const:44e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fa74c",
      "incomplete_value": false,
      "site": "004fa758",
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
            "const:372:8"
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
      "004fa78c",
      "PARAM",
      [
        "storage",
        "002a6372",
        null,
        "string"
      ]
    ],
    [
      "004fa7c0",
      "READ",
      [
        "storage",
        "00c9a960",
        null,
        "pointer"
      ]
    ],
    [
      "004fa7c8",
      "DATA",
      [
        "storage",
        "00c67050",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004fa78c",
      "PARAM",
      [
        "storage",
        "002a644e",
        null,
        "string"
      ]
    ],
    [
      "004fa7c0",
      "READ",
      [
        "storage",
        "00c9ad60",
        null,
        "pointer"
      ]
    ],
    [
      "004fa7c8",
      "DATA",
      [
        "storage",
        "00c67450",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fa758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa634.md#insn-004fa758) · [`004fa6d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa634.md#insn-004fa6d0) · [`004fa6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa634.md#insn-004fa6f8)
- 新版 [`004fa798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fa674.md#insn-004fa798) · [`004fa710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fa674.md#insn-004fa710) · [`004fa738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fa674.md#insn-004fa738)

~~~diff
- 004fa758 ["INT_ADD", "register:40f0:8", ["const:4fa758:8", "const:4:8"]]
- 004fa758 ["CALL", null, ["callee:00c58780:8"]]
+ 004fa798 ["INT_ADD", "register:40f0:8", ["const:4fa798:8", "const:4:8"]]
+ 004fa798 ["CALL", null, ["callee:00c58780:8"]]
- 004fa758 bytes 0a771d94
+ 004fa798 bytes fa771d94
- 004fa6d0 ["INT_ADD", "register:40f0:8", ["const:4fa6d0:8", "const:4:8"]]
- 004fa6d0 ["CALL", null, ["callee:00c57e90:8"]]
+ 004fa710 ["INT_ADD", "register:40f0:8", ["const:4fa710:8", "const:4:8"]]
+ 004fa710 ["CALL", null, ["callee:00c57e90:8"]]
- 004fa6d0 bytes f0741d94
+ 004fa710 bytes e0751d94
- 004fa6f8 ["INT_ADD", "register:40f0:8", ["const:4fa6f8:8", "const:4:8"]]
- 004fa6f8 ["CALL", null, ["callee:00c57f40:8"]]
+ 004fa738 ["INT_ADD", "register:40f0:8", ["const:4fa738:8", "const:4:8"]]
+ 004fa738 ["CALL", null, ["callee:00c57f40:8"]]
- 004fa6f8 bytes 12751d94
+ 004fa738 bytes 02761d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9414037b8e07d11393650b9e788354d"></a>

### [`004fa81c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa81c.md) → [`004fa85c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fa85c.md) _ZN5Botan12Lookup_ErrorC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_S9_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58950.md) · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)
- 新版 呼出元 1件 [`00c58d50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58d50.md) · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.16% / 新版 95.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fa980",
      "incomplete_value": true,
      "site": "004fa980",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fa940",
      "incomplete_value": true,
      "site": "004fa940",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fa9d8",
      "incomplete_value": true,
      "site": "004fa9dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fa998",
      "incomplete_value": true,
      "site": "004fa99c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004fa87c",
      "incomplete_value": false,
      "site": "004fa894",
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
            "const:e17:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fa83c",
      "incomplete_value": false,
      "site": "004fa854",
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
            "const:dd7:8"
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
      "004fa87c",
      "PARAM",
      [
        "storage",
        "002bfdd7",
        null,
        "string"
      ]
    ],
    [
      "004fa89c",
      "PARAM",
      [
        "storage",
        "002a0efa",
        null,
        null
      ]
    ],
    [
      "004fa914",
      "PARAM",
      [
        "storage",
        "002ac800",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004fa87c",
      "PARAM",
      [
        "storage",
        "002bfe17",
        null,
        "string"
      ]
    ],
    [
      "004fa89c",
      "PARAM",
      [
        "storage",
        "002a0fc7",
        null,
        null
      ]
    ],
    [
      "004fa914",
      "PARAM",
      [
        "storage",
        "002ac840",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fa854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa81c.md#insn-004fa854) · [`004fa864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa81c.md#insn-004fa864) · [`004fa8e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fa81c.md#insn-004fa8e0)
- 新版 [`004fa894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fa85c.md#insn-004fa894) · [`004fa8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fa85c.md#insn-004fa8a4) · [`004fa920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fa85c.md#insn-004fa920)

~~~diff
- 004fa854 ["INT_ADD", "register:40f0:8", ["const:4fa854:8", "const:4:8"]]
- 004fa854 ["CALL", null, ["callee:00c580b0:8"]]
+ 004fa894 ["INT_ADD", "register:40f0:8", ["const:4fa894:8", "const:4:8"]]
+ 004fa894 ["CALL", null, ["callee:00c580b0:8"]]
- 004fa854 bytes 17751d94
+ 004fa894 bytes 07761d94
- 004fa864 ["INT_ADD", "register:40f0:8", ["const:4fa864:8", "const:4:8"]]
- 004fa864 ["CALL", null, ["callee:00c57f70:8"]]
+ 004fa8a4 ["INT_ADD", "register:40f0:8", ["const:4fa8a4:8", "const:4:8"]]
+ 004fa8a4 ["CALL", null, ["callee:00c57f70:8"]]
- 004fa864 bytes c3741d94
+ 004fa8a4 bytes b3751d94
- 004fa8e0 ["INT_ADD", "register:40f0:8", ["const:4fa8e0:8", "const:4:8"]]
- 004fa8e0 ["CALL", null, ["callee:00c580b0:8"]]
+ 004fa920 ["INT_ADD", "register:40f0:8", ["const:4fa920:8", "const:4:8"]]
+ 004fa920 ["CALL", null, ["callee:00c580b0:8"]]
- 004fa8e0 bytes f4741d94
+ 004fa920 bytes e4751d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e034a4c70a4d586d553d4edecf5d8fda"></a>

### [`004faacc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004faacc.md) → [`004fab0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fab0c.md) _ZN5Botan14Internal_ErrorC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00c58700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58700.md) [`00c59420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59420.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)
- 新版 呼出元 2件 [`00c58b00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58b00.md) [`00c59820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59820.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.11% / 新版 91.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fab54",
      "incomplete_value": true,
      "site": "004fab54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fab14",
      "incomplete_value": true,
      "site": "004fab14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fab90",
      "incomplete_value": true,
      "site": "004fab94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fab50",
      "incomplete_value": true,
      "site": "004fab54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004fab2c",
      "incomplete_value": false,
      "site": "004fab3c",
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
            "const:c32:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004faaec",
      "incomplete_value": false,
      "site": "004faafc",
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
            "const:bf2:8"
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
      "004fab2c",
      "PARAM",
      [
        "storage",
        "002b0bf2",
        null,
        "string"
      ]
    ],
    [
      "004fab48",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "004fab54",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004fab2c",
      "PARAM",
      [
        "storage",
        "002b0c32",
        null,
        "string"
      ]
    ],
    [
      "004fab48",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "004fab54",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004faafc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004faacc.md#insn-004faafc) · [`004faaec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004faacc.md#insn-004faaec) · [`004fab08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004faacc.md#insn-004fab08)
- 新版 [`004fab3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fab0c.md#insn-004fab3c) · [`004fab2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fab0c.md#insn-004fab2c) · [`004fab48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fab0c.md#insn-004fab48)

~~~diff
- 004faafc ["INT_ADD", "register:40f0:8", ["const:4faafc:8", "const:4:8"]]
- 004faafc ["CALL", null, ["callee:00c580b0:8"]]
+ 004fab3c ["INT_ADD", "register:40f0:8", ["const:4fab3c:8", "const:4:8"]]
+ 004fab3c ["CALL", null, ["callee:00c580b0:8"]]
- 004faafc bytes 6d741d94
+ 004fab3c bytes 5d751d94
- 004faaec ["COPY", "tmp:0:8", ["const:bf2:8"]]
- 004faaec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004faaec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004faaec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004fab2c ["COPY", "tmp:0:8", ["const:c32:8"]]
+ 004fab2c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004fab2c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004fab2c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004faaec bytes 00c82f91
+ 004fab2c bytes 00c83091
- 004fab08 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 004fab08 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fab48 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 004fab48 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004fab08 bytes 08e944f9
+ 004fab48 bytes 08e946f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6645d472a808ac0792a943ca2278e30d"></a>

### [`004fabb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fabb4.md) → [`004fabf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fabf4.md) _ZN5Botan18Invalid_Key_LengthC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58980.md) · 呼出先 8件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`00c58d80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58d80.md) · 呼出先 8件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.20% / 新版 95.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004facc8",
      "incomplete_value": true,
      "site": "004facd4",
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
                "const:1f3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fac88",
      "incomplete_value": true,
      "site": "004fac94",
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
                "const:126:8"
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
      "definition_site": "004faccc",
      "incomplete_value": true,
      "site": "004facd8",
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
                "const:f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fac8c",
      "incomplete_value": true,
      "site": "004fac98",
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
                "const:f:8"
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
      "definition_site": "004fad44",
      "incomplete_value": true,
      "site": "004fad48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fad04",
      "incomplete_value": true,
      "site": "004fad08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 27,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004facc8",
      "READ",
      [
        "storage",
        "002a4126",
        null,
        "string"
      ]
    ],
    [
      "004faccc",
      "READ",
      [
        "storage",
        "002a4135",
        null,
        "string"
      ]
    ],
    [
      "004fad28",
      "PARAM",
      [
        "storage",
        "002a6372",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004facc8",
      "READ",
      [
        "storage",
        "002a41f3",
        null,
        "string"
      ]
    ],
    [
      "004faccc",
      "READ",
      [
        "storage",
        "002a4202",
        null,
        "string"
      ]
    ],
    [
      "004fad28",
      "PARAM",
      [
        "storage",
        "002a644e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004facc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fabb4.md#insn-004facc8) · [`004facf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fabb4.md#insn-004facf4) · [`004fac4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fabb4.md#insn-004fac4c)
- 新版 [`004fad08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fabf4.md#insn-004fad08) · [`004fad34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fabf4.md#insn-004fad34) · [`004fac8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fabf4.md#insn-004fac8c)

~~~diff
- 004facc8 ["INT_ADD", "register:40f0:8", ["const:4facc8:8", "const:4:8"]]
- 004facc8 ["CALL", null, ["callee:00c57f80:8"]]
+ 004fad08 ["INT_ADD", "register:40f0:8", ["const:4fad08:8", "const:4:8"]]
+ 004fad08 ["CALL", null, ["callee:00c57f80:8"]]
- 004facc8 bytes ae731d94
+ 004fad08 bytes 9e741d94
- 004facf4 ["INT_ADD", "register:40f0:8", ["const:4facf4:8", "const:4:8"]]
- 004facf4 ["CALL", null, ["callee:00c58780:8"]]
+ 004fad34 ["INT_ADD", "register:40f0:8", ["const:4fad34:8", "const:4:8"]]
+ 004fad34 ["CALL", null, ["callee:00c58780:8"]]
- 004facf4 bytes a3751d94
+ 004fad34 bytes 93761d94
- 004fac4c ["INT_ADD", "register:40f0:8", ["const:4fac4c:8", "const:4:8"]]
- 004fac4c ["CALL", null, ["callee:00c57e90:8"]]
+ 004fac8c ["INT_ADD", "register:40f0:8", ["const:4fac8c:8", "const:4:8"]]
+ 004fac8c ["CALL", null, ["callee:00c57e90:8"]]
- 004fac4c bytes 91731d94
+ 004fac8c bytes 81741d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f83262de874d12ad2abec604da431868"></a>

### [`004fae28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fae28.md) → [`004fae68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fae68.md) _ZN5Botan17Invalid_IV_LengthC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58990.md) · 呼出先 7件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)
- 新版 呼出元 1件 [`00c58d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58d90.md) · 呼出先 7件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f60.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.81% / 新版 96.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004faf48",
      "incomplete_value": true,
      "site": "004faf4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004faf08",
      "incomplete_value": true,
      "site": "004faf0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004faf7c",
      "incomplete_value": true,
      "site": "004faf80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004faf3c",
      "incomplete_value": true,
      "site": "004faf40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004faea0",
      "incomplete_value": false,
      "site": "004faeac",
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
            "const:dfd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fae60",
      "incomplete_value": false,
      "site": "004fae6c",
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
            "const:dbd:8"
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
      "004faea0",
      "PARAM",
      [
        "storage",
        "002b4dbd",
        null,
        "string"
      ]
    ],
    [
      "004faecc",
      "PARAM",
      [
        "storage",
        "002ae8e4",
        null,
        "string"
      ]
    ],
    [
      "004faf2c",
      "PARAM",
      [
        "storage",
        "002a6372",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004faea0",
      "PARAM",
      [
        "storage",
        "002b4dfd",
        null,
        "string"
      ]
    ],
    [
      "004faecc",
      "PARAM",
      [
        "storage",
        "002ae924",
        null,
        "string"
      ]
    ],
    [
      "004faf2c",
      "PARAM",
      [
        "storage",
        "002a644e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fae6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fae28.md#insn-004fae6c) · [`004fae94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fae28.md#insn-004fae94) · [`004faecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fa/004fae28.md#insn-004faecc)
- 新版 [`004faeac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fae68.md#insn-004faeac) · [`004faed4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fae68.md#insn-004faed4) · [`004faf0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fa/004fae68.md#insn-004faf0c)

~~~diff
- 004fae6c ["INT_ADD", "register:40f0:8", ["const:4fae6c:8", "const:4:8"]]
- 004fae6c ["CALL", null, ["callee:00c57f60:8"]]
+ 004faeac ["INT_ADD", "register:40f0:8", ["const:4faeac:8", "const:4:8"]]
+ 004faeac ["CALL", null, ["callee:00c57f60:8"]]
- 004fae6c bytes 3d731d94
+ 004faeac bytes 2d741d94
- 004fae94 ["INT_ADD", "register:40f0:8", ["const:4fae94:8", "const:4:8"]]
- 004fae94 ["CALL", null, ["callee:00c57f70:8"]]
+ 004faed4 ["INT_ADD", "register:40f0:8", ["const:4faed4:8", "const:4:8"]]
+ 004faed4 ["CALL", null, ["callee:00c57f70:8"]]
- 004fae94 bytes 37731d94
+ 004faed4 bytes 27741d94
- 004faecc ["INT_ADD", "register:40f0:8", ["const:4faecc:8", "const:4:8"]]
- 004faecc ["CALL", null, ["callee:00c57f80:8"]]
+ 004faf0c ["INT_ADD", "register:40f0:8", ["const:4faf0c:8", "const:4:8"]]
+ 004faf0c ["CALL", null, ["callee:00c57f80:8"]]
- 004faecc bytes 2d731d94
+ 004faf0c bytes 1d741d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c73946becd93b3a0d5d0d5612891ec2"></a>

### [`004fb048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb048.md) → [`004fb088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fb088.md) _ZN5Botan11Key_Not_SetC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58240.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)
- 新版 呼出元 1件 [`00c58640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58640.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.79% / 新版 86.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fb0d0",
      "incomplete_value": true,
      "site": "004fb0d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fb090",
      "incomplete_value": true,
      "site": "004fb090",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fb0ec",
      "incomplete_value": true,
      "site": "004fb0f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fb0ac",
      "incomplete_value": true,
      "site": "004fb0b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fb110",
      "incomplete_value": true,
      "site": "004fb114",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fb0d0",
      "incomplete_value": true,
      "site": "004fb0d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004fb0a8",
      "PARAM",
      [
        "storage",
        "002a9b44",
        null,
        "string"
      ]
    ],
    [
      "004fb0c4",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "004fb0d0",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004fb0a8",
      "PARAM",
      [
        "storage",
        "002a9c11",
        null,
        "string"
      ]
    ],
    [
      "004fb0c4",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "004fb0d0",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fb078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb048.md#insn-004fb078) · [`004fb068`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb048.md#insn-004fb068) · [`004fb084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb048.md#insn-004fb084)
- 新版 [`004fb0b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fb088.md#insn-004fb0b8) · [`004fb0a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fb088.md#insn-004fb0a8) · [`004fb0c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fb088.md#insn-004fb0c4)

~~~diff
- 004fb078 ["INT_ADD", "register:40f0:8", ["const:4fb078:8", "const:4:8"]]
- 004fb078 ["CALL", null, ["callee:00c580b0:8"]]
+ 004fb0b8 ["INT_ADD", "register:40f0:8", ["const:4fb0b8:8", "const:4:8"]]
+ 004fb0b8 ["CALL", null, ["callee:00c580b0:8"]]
- 004fb078 bytes 0e731d94
+ 004fb0b8 bytes fe731d94
- 004fb068 ["COPY", "tmp:0:8", ["const:b44:8"]]
- 004fb068 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004fb068 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004fb068 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004fb0a8 ["COPY", "tmp:0:8", ["const:c11:8"]]
+ 004fb0a8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004fb0a8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004fb0a8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004fb068 bytes 00102d91
+ 004fb0a8 bytes 00443091
- 004fb084 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 004fb084 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fb0c4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 004fb0c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004fb084 bytes 08e944f9
+ 004fb0c4 bytes 08e946f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4c8412b9cdce4e8471c8a42dccdffb7"></a>

### [`004fb150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb150.md) → [`004fb190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fb190.md) _ZN5Botan16Policy_ViolationC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.79% / 新版 86.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fb1d8",
      "incomplete_value": true,
      "site": "004fb1d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fb198",
      "incomplete_value": true,
      "site": "004fb198",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fb1f4",
      "incomplete_value": true,
      "site": "004fb1fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fb1b4",
      "incomplete_value": true,
      "site": "004fb1bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fb218",
      "incomplete_value": true,
      "site": "004fb21c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fb1d8",
      "incomplete_value": true,
      "site": "004fb1dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004fb1b0",
      "PARAM",
      [
        "storage",
        "002ba2a2",
        null,
        "string"
      ]
    ],
    [
      "004fb1cc",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "004fb1d8",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004fb1b0",
      "PARAM",
      [
        "storage",
        "002ba2e2",
        null,
        "string"
      ]
    ],
    [
      "004fb1cc",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "004fb1d8",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fb180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb150.md#insn-004fb180) · [`004fb170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb150.md#insn-004fb170) · [`004fb18c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb150.md#insn-004fb18c)
- 新版 [`004fb1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fb190.md#insn-004fb1c0) · [`004fb1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fb190.md#insn-004fb1b0) · [`004fb1cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fb190.md#insn-004fb1cc)

~~~diff
- 004fb180 ["INT_ADD", "register:40f0:8", ["const:4fb180:8", "const:4:8"]]
- 004fb180 ["CALL", null, ["callee:00c580b0:8"]]
+ 004fb1c0 ["INT_ADD", "register:40f0:8", ["const:4fb1c0:8", "const:4:8"]]
+ 004fb1c0 ["CALL", null, ["callee:00c580b0:8"]]
- 004fb180 bytes cc721d94
+ 004fb1c0 bytes bc731d94
- 004fb170 ["COPY", "tmp:0:8", ["const:2a2:8"]]
- 004fb170 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004fb170 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004fb170 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004fb1b0 ["COPY", "tmp:0:8", ["const:2e2:8"]]
+ 004fb1b0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004fb1b0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004fb1b0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004fb170 bytes 00880a91
+ 004fb1b0 bytes 00880b91
- 004fb18c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 004fb18c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fb1cc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 004fb1cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004fb18c bytes 08e944f9
+ 004fb1cc bytes 08e946f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e727f5095ed4ca9104ef503bc695987"></a>

### [`004fb258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb258.md) → [`004fb298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fb298.md) _ZN5Botan13PRNG_UnseededC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59b80.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)
- 新版 呼出元 1件 [`00c59f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59f80.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.79% / 新版 86.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fb2e0",
      "incomplete_value": true,
      "site": "004fb2e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fb2a0",
      "incomplete_value": true,
      "site": "004fb2a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fb2fc",
      "incomplete_value": true,
      "site": "004fb304",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fb2bc",
      "incomplete_value": true,
      "site": "004fb2c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fb320",
      "incomplete_value": true,
      "site": "004fb324",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fb2e0",
      "incomplete_value": true,
      "site": "004fb2e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004fb2b8",
      "PARAM",
      [
        "storage",
        "002c1113",
        null,
        "string"
      ]
    ],
    [
      "004fb2d4",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "004fb2e0",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004fb2b8",
      "PARAM",
      [
        "storage",
        "002c1153",
        null,
        "string"
      ]
    ],
    [
      "004fb2d4",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "004fb2e0",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fb288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb258.md#insn-004fb288) · [`004fb278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb258.md#insn-004fb278) · [`004fb294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb258.md#insn-004fb294)
- 新版 [`004fb2c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fb298.md#insn-004fb2c8) · [`004fb2b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fb298.md#insn-004fb2b8) · [`004fb2d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fb298.md#insn-004fb2d4)

~~~diff
- 004fb288 ["INT_ADD", "register:40f0:8", ["const:4fb288:8", "const:4:8"]]
- 004fb288 ["CALL", null, ["callee:00c580b0:8"]]
+ 004fb2c8 ["INT_ADD", "register:40f0:8", ["const:4fb2c8:8", "const:4:8"]]
+ 004fb2c8 ["CALL", null, ["callee:00c580b0:8"]]
- 004fb288 bytes 8a721d94
+ 004fb2c8 bytes 7a731d94
- 004fb278 ["COPY", "tmp:0:8", ["const:113:8"]]
- 004fb278 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004fb278 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004fb278 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004fb2b8 ["COPY", "tmp:0:8", ["const:153:8"]]
+ 004fb2b8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004fb2b8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004fb2b8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004fb278 bytes 004c0491
+ 004fb2b8 bytes 004c0591
- 004fb294 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 004fb294 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fb2d4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 004fb2d4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004fb294 bytes 08e944f9
+ 004fb2d4 bytes 08e946f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e292b68e40af32e23ccfcea572b5108a"></a>

### [`004fb360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb360.md) → [`004fb3a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fb3a0.md) _ZN5Botan19Algorithm_Not_FoundC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58ba0.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)
- 新版 呼出元 1件 [`00c58fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58fa0.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.73% / 新版 88.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fb414",
      "incomplete_value": true,
      "site": "004fb414",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fb3d4",
      "incomplete_value": true,
      "site": "004fb3d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fb43c",
      "incomplete_value": true,
      "site": "004fb440",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fb3fc",
      "incomplete_value": true,
      "site": "004fb400",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "store_value",
    "new": {
      "definition_site": "004fb45c",
      "incomplete_value": true,
      "site": "004fb460",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fb41c",
      "incomplete_value": true,
      "site": "004fb420",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004fb3c0",
      "PARAM",
      [
        "storage",
        "002b1c63",
        null,
        "string"
      ]
    ],
    [
      "004fb3d8",
      "PARAM",
      [
        "storage",
        "002b5e4d",
        null,
        null
      ]
    ],
    [
      "004fb400",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004fb3c0",
      "PARAM",
      [
        "storage",
        "002b1ca3",
        null,
        "string"
      ]
    ],
    [
      "004fb3d8",
      "PARAM",
      [
        "storage",
        "002b5e8d",
        null,
        null
      ]
    ],
    [
      "004fb400",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fb390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb360.md#insn-004fb390) · [`004fb3a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb360.md#insn-004fb3a0) · [`004fb3c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb360.md#insn-004fb3c0)
- 新版 [`004fb3d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fb3a0.md#insn-004fb3d0) · [`004fb3e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fb3a0.md#insn-004fb3e0) · [`004fb400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fb3a0.md#insn-004fb400)

~~~diff
- 004fb390 ["INT_ADD", "register:40f0:8", ["const:4fb390:8", "const:4:8"]]
- 004fb390 ["CALL", null, ["callee:00c580b0:8"]]
+ 004fb3d0 ["INT_ADD", "register:40f0:8", ["const:4fb3d0:8", "const:4:8"]]
+ 004fb3d0 ["CALL", null, ["callee:00c580b0:8"]]
- 004fb390 bytes 48721d94
+ 004fb3d0 bytes 38731d94
- 004fb3a0 ["INT_ADD", "register:40f0:8", ["const:4fb3a0:8", "const:4:8"]]
- 004fb3a0 ["CALL", null, ["callee:00c57f70:8"]]
+ 004fb3e0 ["INT_ADD", "register:40f0:8", ["const:4fb3e0:8", "const:4:8"]]
+ 004fb3e0 ["CALL", null, ["callee:00c57f70:8"]]
- 004fb3a0 bytes f4711d94
+ 004fb3e0 bytes e4721d94
- 004fb3c0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 004fb3c0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fb400 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 004fb400 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004fb3c0 bytes 08e944f9
+ 004fb400 bytes 08e946f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c031467072f4e735113f46b47b681c85"></a>

### [`004fb4c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb4c0.md) → [`004fb500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fb500.md) _ZN5Botan17No_Provider_FoundC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.06% / 新版 92.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fb574",
      "incomplete_value": true,
      "site": "004fb574",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fb534",
      "incomplete_value": true,
      "site": "004fb534",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fb5ac",
      "incomplete_value": true,
      "site": "004fb5b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fb56c",
      "incomplete_value": true,
      "site": "004fb570",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fb520",
      "incomplete_value": false,
      "site": "004fb530",
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
            "const:57f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fb4e0",
      "incomplete_value": false,
      "site": "004fb4f0",
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
            "const:4a3:8"
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
      "004fb520",
      "PARAM",
      [
        "storage",
        "002a54a3",
        null,
        "string"
      ]
    ],
    [
      "004fb538",
      "PARAM",
      [
        "storage",
        "002b5e4d",
        null,
        null
      ]
    ],
    [
      "004fb560",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004fb520",
      "PARAM",
      [
        "storage",
        "002a557f",
        null,
        "string"
      ]
    ],
    [
      "004fb538",
      "PARAM",
      [
        "storage",
        "002b5e8d",
        null,
        null
      ]
    ],
    [
      "004fb560",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fb4f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb4c0.md#insn-004fb4f0) · [`004fb500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb4c0.md#insn-004fb500) · [`004fb4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb4c0.md#insn-004fb4e0)
- 新版 [`004fb530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fb500.md#insn-004fb530) · [`004fb540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fb500.md#insn-004fb540) · [`004fb520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fb500.md#insn-004fb520)

~~~diff
- 004fb4f0 ["INT_ADD", "register:40f0:8", ["const:4fb4f0:8", "const:4:8"]]
- 004fb4f0 ["CALL", null, ["callee:00c580b0:8"]]
+ 004fb530 ["INT_ADD", "register:40f0:8", ["const:4fb530:8", "const:4:8"]]
+ 004fb530 ["CALL", null, ["callee:00c580b0:8"]]
- 004fb4f0 bytes f0711d94
+ 004fb530 bytes e0721d94
- 004fb500 ["INT_ADD", "register:40f0:8", ["const:4fb500:8", "const:4:8"]]
- 004fb500 ["CALL", null, ["callee:00c57f70:8"]]
+ 004fb540 ["INT_ADD", "register:40f0:8", ["const:4fb540:8", "const:4:8"]]
+ 004fb540 ["CALL", null, ["callee:00c57f70:8"]]
- 004fb500 bytes 9c711d94
+ 004fb540 bytes 8c721d94
- 004fb4e0 ["COPY", "tmp:0:8", ["const:4a3:8"]]
- 004fb4e0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004fb4e0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004fb4e0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004fb520 ["COPY", "tmp:0:8", ["const:57f:8"]]
+ 004fb520 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004fb520 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004fb520 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004fb4e0 bytes 008c1291
+ 004fb520 bytes 00fc1591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d37ec2c352b16b9908d30f0f911e5c8"></a>

### [`004fb600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb600.md) → [`004fb640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fb640.md) _ZN5Botan18Provider_Not_FoundC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59370.md) · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)
- 新版 呼出元 1件 [`00c59770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59770.md) · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.21% / 新版 91.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fb6f4",
      "incomplete_value": true,
      "site": "004fb6f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fb6b4",
      "incomplete_value": true,
      "site": "004fb6b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fb71c",
      "incomplete_value": true,
      "site": "004fb720",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fb6dc",
      "incomplete_value": true,
      "site": "004fb6e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fb74c",
      "incomplete_value": true,
      "site": "004fb750",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fb70c",
      "incomplete_value": true,
      "site": "004fb710",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
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
      "004fb668",
      "PARAM",
      [
        "storage",
        "002a1f5e",
        null,
        "string"
      ]
    ],
    [
      "004fb680",
      "PARAM",
      [
        "storage",
        "002ac80f",
        null,
        "string"
      ]
    ],
    [
      "004fb6e0",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004fb668",
      "PARAM",
      [
        "storage",
        "002a202b",
        null,
        "string"
      ]
    ],
    [
      "004fb680",
      "PARAM",
      [
        "storage",
        "002ac84f",
        null,
        "string"
      ]
    ],
    [
      "004fb6e0",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fb638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb600.md#insn-004fb638) · [`004fb648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb600.md#insn-004fb648) · [`004fb6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb600.md#insn-004fb6a0)
- 新版 [`004fb678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fb640.md#insn-004fb678) · [`004fb688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fb640.md#insn-004fb688) · [`004fb6e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fb640.md#insn-004fb6e0)

~~~diff
- 004fb638 ["INT_ADD", "register:40f0:8", ["const:4fb638:8", "const:4:8"]]
- 004fb638 ["CALL", null, ["callee:00c580b0:8"]]
+ 004fb678 ["INT_ADD", "register:40f0:8", ["const:4fb678:8", "const:4:8"]]
+ 004fb678 ["CALL", null, ["callee:00c580b0:8"]]
- 004fb638 bytes 9e711d94
+ 004fb678 bytes 8e721d94
- 004fb648 ["INT_ADD", "register:40f0:8", ["const:4fb648:8", "const:4:8"]]
- 004fb648 ["CALL", null, ["callee:00c57f70:8"]]
+ 004fb688 ["INT_ADD", "register:40f0:8", ["const:4fb688:8", "const:4:8"]]
+ 004fb688 ["CALL", null, ["callee:00c57f70:8"]]
- 004fb648 bytes 4a711d94
+ 004fb688 bytes 3a721d94
- 004fb6a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 004fb6a0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fb6e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 004fb6e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004fb6a0 bytes 08e944f9
+ 004fb6e0 bytes 08e946f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3a96181012c1898be14fdecb3244698"></a>

### [`004fb7c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb7c8.md) → [`004fb808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fb808.md) _ZN5Botan22Invalid_Algorithm_NameC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58ea0.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c58380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58380.md)
- 新版 呼出元 1件 [`00c592a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c592a0.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c58780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58780.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fb858",
      "incomplete_value": true,
      "site": "004fb85c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fb818",
      "incomplete_value": true,
      "site": "004fb81c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fb874",
      "incomplete_value": true,
      "site": "004fb878",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fb834",
      "incomplete_value": true,
      "site": "004fb838",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004fb824",
      "incomplete_value": false,
      "site": "004fb834",
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
            "const:9c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fb7e4",
      "incomplete_value": false,
      "site": "004fb7f4",
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
            "const:988:8"
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
      "004fb824",
      "PARAM",
      [
        "storage",
        "002af988",
        null,
        "string"
      ]
    ],
    [
      "004fb83c",
      "PARAM",
      [
        "storage",
        "002a6372",
        null,
        "string"
      ]
    ],
    [
      "004fb850",
      "READ",
      [
        "storage",
        "00c9a960",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004fb824",
      "PARAM",
      [
        "storage",
        "002af9c8",
        null,
        "string"
      ]
    ],
    [
      "004fb83c",
      "PARAM",
      [
        "storage",
        "002a644e",
        null,
        "string"
      ]
    ],
    [
      "004fb850",
      "READ",
      [
        "storage",
        "00c9ad60",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fb7f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb7c8.md#insn-004fb7f4) · [`004fb808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb7c8.md#insn-004fb808) · [`004fb7e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb7c8.md#insn-004fb7e4)
- 新版 [`004fb834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fb808.md#insn-004fb834) · [`004fb848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fb808.md#insn-004fb848) · [`004fb824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fb808.md#insn-004fb824)

~~~diff
- 004fb7f4 ["INT_ADD", "register:40f0:8", ["const:4fb7f4:8", "const:4:8"]]
- 004fb7f4 ["CALL", null, ["callee:00c580b0:8"]]
+ 004fb834 ["INT_ADD", "register:40f0:8", ["const:4fb834:8", "const:4:8"]]
+ 004fb834 ["CALL", null, ["callee:00c580b0:8"]]
- 004fb7f4 bytes 2f711d94
+ 004fb834 bytes 1f721d94
- 004fb808 ["INT_ADD", "register:40f0:8", ["const:4fb808:8", "const:4:8"]]
- 004fb808 ["CALL", null, ["callee:00c58780:8"]]
+ 004fb848 ["INT_ADD", "register:40f0:8", ["const:4fb848:8", "const:4:8"]]
+ 004fb848 ["CALL", null, ["callee:00c58780:8"]]
- 004fb808 bytes de721d94
+ 004fb848 bytes ce731d94
- 004fb7e4 ["COPY", "tmp:0:8", ["const:988:8"]]
- 004fb7e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004fb7e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004fb7e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004fb824 ["COPY", "tmp:0:8", ["const:9c8:8"]]
+ 004fb824 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004fb824 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004fb824 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004fb7e4 bytes 00202691
+ 004fb824 bytes 00202791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e33e3154549730250bb521f0ea64faec"></a>

### [`004fb88c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb88c.md) → [`004fb8cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fb8cc.md) _ZN5Botan14Encoding_ErrorC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58430.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c58380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58380.md)
- 新版 呼出元 1件 [`00c58830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58830.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c58780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58780.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fb91c",
      "incomplete_value": true,
      "site": "004fb920",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fb8dc",
      "incomplete_value": true,
      "site": "004fb8e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fb938",
      "incomplete_value": true,
      "site": "004fb93c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fb8f8",
      "incomplete_value": true,
      "site": "004fb8fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004fb8e8",
      "incomplete_value": false,
      "site": "004fb8f8",
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
            "const:c9c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fb8a8",
      "incomplete_value": false,
      "site": "004fb8b8",
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
            "const:bcf:8"
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
      "004fb8e8",
      "PARAM",
      [
        "storage",
        "002a8bcf",
        null,
        "string"
      ]
    ],
    [
      "004fb900",
      "PARAM",
      [
        "storage",
        "002a6372",
        null,
        "string"
      ]
    ],
    [
      "004fb914",
      "READ",
      [
        "storage",
        "00c9a960",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004fb8e8",
      "PARAM",
      [
        "storage",
        "002a8c9c",
        null,
        "string"
      ]
    ],
    [
      "004fb900",
      "PARAM",
      [
        "storage",
        "002a644e",
        null,
        "string"
      ]
    ],
    [
      "004fb914",
      "READ",
      [
        "storage",
        "00c9ad60",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fb8b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb88c.md#insn-004fb8b8) · [`004fb8cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb88c.md#insn-004fb8cc) · [`004fb8a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb88c.md#insn-004fb8a8)
- 新版 [`004fb8f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fb8cc.md#insn-004fb8f8) · [`004fb90c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fb8cc.md#insn-004fb90c) · [`004fb8e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fb8cc.md#insn-004fb8e8)

~~~diff
- 004fb8b8 ["INT_ADD", "register:40f0:8", ["const:4fb8b8:8", "const:4:8"]]
- 004fb8b8 ["CALL", null, ["callee:00c580b0:8"]]
+ 004fb8f8 ["INT_ADD", "register:40f0:8", ["const:4fb8f8:8", "const:4:8"]]
+ 004fb8f8 ["CALL", null, ["callee:00c580b0:8"]]
- 004fb8b8 bytes fe701d94
+ 004fb8f8 bytes ee711d94
- 004fb8cc ["INT_ADD", "register:40f0:8", ["const:4fb8cc:8", "const:4:8"]]
- 004fb8cc ["CALL", null, ["callee:00c58780:8"]]
+ 004fb90c ["INT_ADD", "register:40f0:8", ["const:4fb90c:8", "const:4:8"]]
+ 004fb90c ["CALL", null, ["callee:00c58780:8"]]
- 004fb8cc bytes ad721d94
+ 004fb90c bytes 9d731d94
- 004fb8a8 ["COPY", "tmp:0:8", ["const:bcf:8"]]
- 004fb8a8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004fb8a8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004fb8a8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004fb8e8 ["COPY", "tmp:0:8", ["const:c9c:8"]]
+ 004fb8e8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004fb8e8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004fb8e8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004fb8a8 bytes 003c2f91
+ 004fb8e8 bytes 00703291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3930077be79f2d67b87bb9fa7e07127d"></a>

### [`004fb950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb950.md) → [`004fb990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fb990.md) _ZN5Botan14Decoding_ErrorC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEPKc

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c599f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599f0.md) · 呼出先 5件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c58380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58380.md)
- 新版 呼出元 1件 [`00c59df0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59df0.md) · 呼出先 5件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c58780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58780.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.89% / 新版 95.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fba34",
      "incomplete_value": true,
      "site": "004fba38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fb9f4",
      "incomplete_value": true,
      "site": "004fb9f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fba60",
      "incomplete_value": true,
      "site": "004fba64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fba20",
      "incomplete_value": true,
      "site": "004fba24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fb9b0",
      "incomplete_value": false,
      "site": "004fb9c4",
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
            "const:e24:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fb970",
      "incomplete_value": false,
      "site": "004fb984",
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
            "const:de4:8"
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
      "004fb9b0",
      "PARAM",
      [
        "storage",
        "002bfde4",
        null,
        "string"
      ]
    ],
    [
      "004fb9cc",
      "PARAM",
      [
        "storage",
        "002a1f78",
        null,
        "string"
      ]
    ],
    [
      "004fba18",
      "PARAM",
      [
        "storage",
        "002a6372",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004fb9b0",
      "PARAM",
      [
        "storage",
        "002bfe24",
        null,
        "string"
      ]
    ],
    [
      "004fb9cc",
      "PARAM",
      [
        "storage",
        "002a2045",
        null,
        "string"
      ]
    ],
    [
      "004fba18",
      "PARAM",
      [
        "storage",
        "002a644e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fb984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb950.md#insn-004fb984) · [`004fb994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb950.md#insn-004fb994) · [`004fb9b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fb950.md#insn-004fb9b8)
- 新版 [`004fb9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fb990.md#insn-004fb9c4) · [`004fb9d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fb990.md#insn-004fb9d4) · [`004fb9f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fb990.md#insn-004fb9f8)

~~~diff
- 004fb984 ["INT_ADD", "register:40f0:8", ["const:4fb984:8", "const:4:8"]]
- 004fb984 ["CALL", null, ["callee:00c580b0:8"]]
+ 004fb9c4 ["INT_ADD", "register:40f0:8", ["const:4fb9c4:8", "const:4:8"]]
+ 004fb9c4 ["CALL", null, ["callee:00c580b0:8"]]
- 004fb984 bytes cb701d94
+ 004fb9c4 bytes bb711d94
- 004fb994 ["INT_ADD", "register:40f0:8", ["const:4fb994:8", "const:4:8"]]
- 004fb994 ["CALL", null, ["callee:00c57f70:8"]]
+ 004fb9d4 ["INT_ADD", "register:40f0:8", ["const:4fb9d4:8", "const:4:8"]]
+ 004fb9d4 ["CALL", null, ["callee:00c57f70:8"]]
- 004fb994 bytes 77701d94
+ 004fb9d4 bytes 67711d94
- 004fb9b8 ["INT_ADD", "register:40f0:8", ["const:4fb9b8:8", "const:4:8"]]
- 004fb9b8 ["CALL", null, ["callee:00c57f70:8"]]
+ 004fb9f8 ["INT_ADD", "register:40f0:8", ["const:4fb9f8:8", "const:4:8"]]
+ 004fb9f8 ["CALL", null, ["callee:00c57f70:8"]]
- 004fb9b8 bytes 6e701d94
+ 004fb9f8 bytes 5e711d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-828d0d93014a4330d04630099ec1d7e6"></a>

### [`004fbaf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fbaf4.md) → [`004fbb34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fbb34.md) _ZN5Botan17Integrity_FailureC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.11% / 新版 91.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fbb7c",
      "incomplete_value": true,
      "site": "004fbb7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fbb3c",
      "incomplete_value": true,
      "site": "004fbb3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fbbb8",
      "incomplete_value": true,
      "site": "004fbbbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fbb78",
      "incomplete_value": true,
      "site": "004fbb7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004fbb54",
      "incomplete_value": false,
      "site": "004fbb64",
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
            "const:68c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fbb14",
      "incomplete_value": false,
      "site": "004fbb24",
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
            "const:5b0:8"
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
      "004fbb54",
      "PARAM",
      [
        "storage",
        "002a65b0",
        null,
        "string"
      ]
    ],
    [
      "004fbb70",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "004fbb7c",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004fbb54",
      "PARAM",
      [
        "storage",
        "002a668c",
        null,
        "string"
      ]
    ],
    [
      "004fbb70",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "004fbb7c",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fbb24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fbaf4.md#insn-004fbb24) · [`004fbb14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fbaf4.md#insn-004fbb14) · [`004fbb30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fbaf4.md#insn-004fbb30)
- 新版 [`004fbb64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fbb34.md#insn-004fbb64) · [`004fbb54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fbb34.md#insn-004fbb54) · [`004fbb70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fbb34.md#insn-004fbb70)

~~~diff
- 004fbb24 ["INT_ADD", "register:40f0:8", ["const:4fbb24:8", "const:4:8"]]
- 004fbb24 ["CALL", null, ["callee:00c580b0:8"]]
+ 004fbb64 ["INT_ADD", "register:40f0:8", ["const:4fbb64:8", "const:4:8"]]
+ 004fbb64 ["CALL", null, ["callee:00c580b0:8"]]
- 004fbb24 bytes 63701d94
+ 004fbb64 bytes 53711d94
- 004fbb14 ["COPY", "tmp:0:8", ["const:5b0:8"]]
- 004fbb14 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004fbb14 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004fbb14 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004fbb54 ["COPY", "tmp:0:8", ["const:68c:8"]]
+ 004fbb54 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004fbb54 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004fbb54 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004fbb14 bytes 00c01691
+ 004fbb54 bytes 00301a91
- 004fbb30 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 004fbb30 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fbb70 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 004fbb70 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004fbb30 bytes 08e944f9
+ 004fbb70 bytes 08e946f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0908535440588d15444709bdce91d972"></a>

### [`004fbbdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fbbdc.md) → [`004fbc1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fbc1c.md) _ZN5Botan11Invalid_OIDC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c583e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c583e0.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c58380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58380.md)
- 新版 呼出元 1件 [`00c587e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c587e0.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c58780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58780.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fbc80",
      "incomplete_value": true,
      "site": "004fbc84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fbc40",
      "incomplete_value": true,
      "site": "004fbc44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fbca0",
      "incomplete_value": true,
      "site": "004fbca4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fbc60",
      "incomplete_value": true,
      "site": "004fbc64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fbcbc",
      "incomplete_value": true,
      "site": "004fbcc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fbc7c",
      "incomplete_value": true,
      "site": "004fbc80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004fbc38",
      "PARAM",
      [
        "storage",
        "002ba2b5",
        null,
        "string"
      ]
    ],
    [
      "004fbc50",
      "PARAM",
      [
        "storage",
        "002bfde4",
        null,
        "string"
      ]
    ],
    [
      "004fbc64",
      "PARAM",
      [
        "storage",
        "002a6372",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004fbc38",
      "PARAM",
      [
        "storage",
        "002ba2f5",
        null,
        "string"
      ]
    ],
    [
      "004fbc50",
      "PARAM",
      [
        "storage",
        "002bfe24",
        null,
        "string"
      ]
    ],
    [
      "004fbc64",
      "PARAM",
      [
        "storage",
        "002a644e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fbc08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fbbdc.md#insn-004fbc08) · [`004fbc1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fbbdc.md#insn-004fbc1c) · [`004fbc24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fbbdc.md#insn-004fbc24)
- 新版 [`004fbc48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fbc1c.md#insn-004fbc48) · [`004fbc5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fbc1c.md#insn-004fbc5c) · [`004fbc64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fbc1c.md#insn-004fbc64)

~~~diff
- 004fbc08 ["INT_ADD", "register:40f0:8", ["const:4fbc08:8", "const:4:8"]]
- 004fbc08 ["CALL", null, ["callee:00c580b0:8"]]
+ 004fbc48 ["INT_ADD", "register:40f0:8", ["const:4fbc48:8", "const:4:8"]]
+ 004fbc48 ["CALL", null, ["callee:00c580b0:8"]]
- 004fbc08 bytes 2a701d94
+ 004fbc48 bytes 1a711d94
- 004fbc1c ["INT_ADD", "register:40f0:8", ["const:4fbc1c:8", "const:4:8"]]
- 004fbc1c ["CALL", null, ["callee:00c580b0:8"]]
+ 004fbc5c ["INT_ADD", "register:40f0:8", ["const:4fbc5c:8", "const:4:8"]]
+ 004fbc5c ["CALL", null, ["callee:00c580b0:8"]]
- 004fbc1c bytes 25701d94
+ 004fbc5c bytes 15711d94
- 004fbc24 ["COPY", "tmp:0:8", ["const:372:8"]]
- 004fbc24 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004fbc24 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004fbc24 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004fbc64 ["COPY", "tmp:0:8", ["const:44e:8"]]
+ 004fbc64 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004fbc64 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004fbc64 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004fbc24 bytes 21c80d91
+ 004fbc64 bytes 21381191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d91f2dcc838a480206d0e97de31f0656"></a>

### [`004fbcec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fbcec.md) → [`004fbd2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fbd2c.md) _ZN5Botan15Stream_IO_ErrorC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c583b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c583b0.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)
- 新版 呼出元 1件 [`00c587b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c587b0.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.11% / 新版 91.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fbd74",
      "incomplete_value": true,
      "site": "004fbd74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fbd34",
      "incomplete_value": true,
      "site": "004fbd34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fbdb0",
      "incomplete_value": true,
      "site": "004fbdb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fbd70",
      "incomplete_value": true,
      "site": "004fbd74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004fbd4c",
      "incomplete_value": false,
      "site": "004fbd5c",
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
            "const:e08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fbd0c",
      "incomplete_value": false,
      "site": "004fbd1c",
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
            "const:dc8:8"
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
      "004fbd4c",
      "PARAM",
      [
        "storage",
        "002b4dc8",
        null,
        "string"
      ]
    ],
    [
      "004fbd68",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "004fbd74",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004fbd4c",
      "PARAM",
      [
        "storage",
        "002b4e08",
        null,
        "string"
      ]
    ],
    [
      "004fbd68",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "004fbd74",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fbd1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fbcec.md#insn-004fbd1c) · [`004fbd0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fbcec.md#insn-004fbd0c) · [`004fbd28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fbcec.md#insn-004fbd28)
- 新版 [`004fbd5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fbd2c.md#insn-004fbd5c) · [`004fbd4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fbd2c.md#insn-004fbd4c) · [`004fbd68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fbd2c.md#insn-004fbd68)

~~~diff
- 004fbd1c ["INT_ADD", "register:40f0:8", ["const:4fbd1c:8", "const:4:8"]]
- 004fbd1c ["CALL", null, ["callee:00c580b0:8"]]
+ 004fbd5c ["INT_ADD", "register:40f0:8", ["const:4fbd5c:8", "const:4:8"]]
+ 004fbd5c ["CALL", null, ["callee:00c580b0:8"]]
- 004fbd1c bytes e56f1d94
+ 004fbd5c bytes d5701d94
- 004fbd0c ["COPY", "tmp:0:8", ["const:dc8:8"]]
- 004fbd0c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004fbd0c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004fbd0c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004fbd4c ["COPY", "tmp:0:8", ["const:e08:8"]]
+ 004fbd4c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004fbd4c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004fbd4c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004fbd0c bytes 00203791
+ 004fbd4c bytes 00203891
- 004fbd28 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 004fbd28 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fbd68 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 004fbd68 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004fbd28 bytes 08e944f9
+ 004fbd68 bytes 08e946f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e754c40559fe87a4a093d04f50ce139"></a>

### [`004fbdd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fbdd4.md) → [`004fbe14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fbe14.md) _ZN5Botan17Self_Test_FailureC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c59420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59420.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c59820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59820.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.88% / 新版 96.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fbe68",
      "incomplete_value": true,
      "site": "004fbe6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fbe28",
      "incomplete_value": true,
      "site": "004fbe2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004fbe30",
      "incomplete_value": false,
      "site": "004fbe40",
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
            "const:cc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fbdf0",
      "incomplete_value": false,
      "site": "004fbe00",
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
            "const:c88:8"
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
      "004fbe30",
      "PARAM",
      [
        "storage",
        "002b1c88",
        null,
        "string"
      ]
    ],
    [
      "004fbe64",
      "READ",
      [
        "storage",
        "00c9acb0",
        null,
        "pointer"
      ]
    ],
    [
      "004fbe6c",
      "DATA",
      [
        "storage",
        "00c672f8",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004fbe30",
      "PARAM",
      [
        "storage",
        "002b1cc8",
        null,
        "string"
      ]
    ],
    [
      "004fbe64",
      "READ",
      [
        "storage",
        "00c9b0b0",
        null,
        "pointer"
      ]
    ],
    [
      "004fbe6c",
      "DATA",
      [
        "storage",
        "00c676f8",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fbe00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fbdd4.md#insn-004fbe00) · [`004fbdf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fbdd4.md#insn-004fbdf0) · [`004fbe0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fbdd4.md#insn-004fbe0c)
- 新版 [`004fbe40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fbe14.md#insn-004fbe40) · [`004fbe30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fbe14.md#insn-004fbe30) · [`004fbe4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fbe14.md#insn-004fbe4c)

~~~diff
- 004fbe00 ["INT_ADD", "register:40f0:8", ["const:4fbe00:8", "const:4:8"]]
- 004fbe00 ["CALL", null, ["callee:00c580b0:8"]]
+ 004fbe40 ["INT_ADD", "register:40f0:8", ["const:4fbe40:8", "const:4:8"]]
+ 004fbe40 ["CALL", null, ["callee:00c580b0:8"]]
- 004fbe00 bytes ac6f1d94
+ 004fbe40 bytes 9c701d94
- 004fbdf0 ["COPY", "tmp:0:8", ["const:c88:8"]]
- 004fbdf0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004fbdf0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004fbdf0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004fbe30 ["COPY", "tmp:0:8", ["const:cc8:8"]]
+ 004fbe30 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004fbe30 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004fbe30 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004fbdf0 bytes 00203291
+ 004fbe30 bytes 00203391
- 004fbe0c ["INT_ADD", "register:40f0:8", ["const:4fbe0c:8", "const:4:8"]]
- 004fbe0c ["CALL", null, ["callee:00c59820:8"]]
+ 004fbe4c ["INT_ADD", "register:40f0:8", ["const:4fbe4c:8", "const:4:8"]]
+ 004fbe4c ["CALL", null, ["callee:00c59820:8"]]
- 004fbe0c bytes 85751d94
+ 004fbe4c bytes 75761d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52dc2792e4c7f9af87ff10b3d277e5ed"></a>

### [`004fbe80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fbe80.md) → [`004fbec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fbec0.md) _ZN5Botan15Not_ImplementedC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c590e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c590e0.md) · 呼出先 1件 [`00c58380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58380.md)
- 新版 呼出元 1件 [`00c594e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c594e0.md) · 呼出先 1件 [`00c58780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58780.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fbee8",
      "incomplete_value": true,
      "site": "004fbeec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004fbea8",
      "incomplete_value": true,
      "site": "004fbeac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004fbed4",
      "incomplete_value": false,
      "site": "004fbedc",
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
            "const:9e1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fbe94",
      "incomplete_value": false,
      "site": "004fbe9c",
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
            "const:9a1:8"
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
      "004fbed4",
      "PARAM",
      [
        "storage",
        "002af9a1",
        null,
        "string"
      ]
    ],
    [
      "004fbee4",
      "READ",
      [
        "storage",
        "00c9acb8",
        null,
        "pointer"
      ]
    ],
    [
      "004fbeec",
      "DATA",
      [
        "storage",
        "00c67320",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004fbed4",
      "PARAM",
      [
        "storage",
        "002af9e1",
        null,
        "string"
      ]
    ],
    [
      "004fbee4",
      "READ",
      [
        "storage",
        "00c9b0b8",
        null,
        "pointer"
      ]
    ],
    [
      "004fbeec",
      "DATA",
      [
        "storage",
        "00c67720",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fbe9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fbe80.md#insn-004fbe9c) · [`004fbe94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fbe80.md#insn-004fbe94) · [`004fbea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fbe80.md#insn-004fbea0)
- 新版 [`004fbedc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fbec0.md#insn-004fbedc) · [`004fbed4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fbec0.md#insn-004fbed4) · [`004fbee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fbec0.md#insn-004fbee0)

~~~diff
- 004fbe9c ["INT_ADD", "register:40f0:8", ["const:4fbe9c:8", "const:4:8"]]
- 004fbe9c ["CALL", null, ["callee:00c58780:8"]]
+ 004fbedc ["INT_ADD", "register:40f0:8", ["const:4fbedc:8", "const:4:8"]]
+ 004fbedc ["CALL", null, ["callee:00c58780:8"]]
- 004fbe9c bytes 39711d94
+ 004fbedc bytes 29721d94
- 004fbe94 ["COPY", "tmp:0:8", ["const:9a1:8"]]
- 004fbe94 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004fbe94 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004fbe94 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004fbed4 ["COPY", "tmp:0:8", ["const:9e1:8"]]
+ 004fbed4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004fbed4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004fbed4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004fbe94 bytes 21842691
+ 004fbed4 bytes 21842791
- 004fbea0 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 004fbee0 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 004fbea0 bytes e83c00f0
+ 004fbee0 bytes 083d0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-449dce8d90438f72ea9e96ec4ac1493a"></a>

### [`004fbebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fbebc.md) → [`004fbefc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fbefc.md) _ZN5Botan19get_files_recursiveERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59430.md) · 呼出先 20件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00539edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00539/00539edc.md) [`0053a074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053a074.md)
- 新版 呼出元 1件 [`00c59830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59830.md) · 呼出先 20件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00539f1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00539/00539f1c.md) [`0053a0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053a0b4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.11% / 新版 99.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004fc120",
      "incomplete_value": false,
      "site": "004fc120",
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
            "const:348:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fc0e0",
      "incomplete_value": false,
      "site": "004fc0e0",
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
            "const:f48:8"
          ]
        ]
      ]
    },
    "ordinal": 36,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fc134",
      "incomplete_value": true,
      "site": "004fc134",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fc0f4",
      "incomplete_value": true,
      "site": "004fc0f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
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
      "004fc120",
      "DATA",
      [
        "storage",
        "00c69f48",
        null,
        "undefined *"
      ]
    ],
    [
      "004fc130",
      "READ",
      [
        "storage",
        "00c9acc0",
        null,
        "pointer"
      ]
    ],
    [
      "004fc48c",
      "READ",
      [
        "storage",
        "00c69f78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004fc120",
      "DATA",
      [
        "storage",
        "00c6a348",
        null,
        "undefined *"
      ]
    ],
    [
      "004fc130",
      "READ",
      [
        "storage",
        "00c9b0c0",
        null,
        "pointer"
      ]
    ],
    [
      "004fc48c",
      "READ",
      [
        "storage",
        "00c6a378",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fc0a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fbebc.md#insn-004fc0a0) · [`004fbf18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fbebc.md#insn-004fbf18) · [`004fbf84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fb/004fbebc.md#insn-004fbf84)
- 新版 [`004fc0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fbefc.md#insn-004fc0e0) · [`004fbf58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fbefc.md#insn-004fbf58) · [`004fbfc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fb/004fbefc.md#insn-004fbfc4)

~~~diff
- 004fc0a0 ["INT_ADD", "register:40f0:8", ["const:4fc0a0:8", "const:4:8"]]
- 004fc0a0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 004fc0e0 ["INT_ADD", "register:40f0:8", ["const:4fc0e0:8", "const:4:8"]]
+ 004fc0e0 ["CALL", null, ["callee:00c57eb0:8"]]
- 004fc0a0 bytes 846e1d94
+ 004fc0e0 bytes 746f1d94
- 004fbf18 ["INT_ADD", "register:40f0:8", ["const:4fbf18:8", "const:4:8"]]
- 004fbf18 ["CALL", null, ["callee:0053a0b4:8"]]
+ 004fbf58 ["INT_ADD", "register:40f0:8", ["const:4fbf58:8", "const:4:8"]]
+ 004fbf58 ["CALL", null, ["callee:0053a0b4:8"]]
- 004fbf18 bytes 57f80094
+ 004fbf58 bytes 57f80094
- 004fbf84 ["INT_ADD", "register:40f0:8", ["const:4fbf84:8", "const:4:8"]]
- 004fbf84 ["CALL", null, ["callee:0043bb20:8"]]
+ 004fbfc4 ["INT_ADD", "register:40f0:8", ["const:4fbfc4:8", "const:4:8"]]
+ 004fbfc4 ["CALL", null, ["callee:0043bb20:8"]]
- 004fbf84 bytes d7fefc97
+ 004fbfc4 bytes d7fefc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a1d50367a90840b085ecb8dba88c92e"></a>

### [`004fc734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fc/004fc734.md) → [`004fc774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fc/004fc774.md) _ZN5Botan15allocate_memoryEmm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59470.md) · 呼出先 5件 [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c58630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58630.md) [`00c58640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58640.md)
- 新版 呼出元 1件 [`00c59870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59870.md) · 呼出先 5件 [`00c37ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ba4.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c58a30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58a30.md) [`00c58a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58a40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004fc7b0",
      "incomplete_value": true,
      "site": "004fc7b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:de8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fc770",
      "incomplete_value": true,
      "site": "004fc778",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004fc7b4",
      "incomplete_value": true,
      "site": "004fc7b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:df0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fc774",
      "incomplete_value": true,
      "site": "004fc778",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004fc7b0",
      "READ",
      [
        "storage",
        "00c9a9e8",
        null,
        "pointer"
      ]
    ],
    [
      "004fc7b0",
      "PARAM",
      [
        "storage",
        "00c96298",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "004fc7b4",
      "READ",
      [
        "storage",
        "00c9a9f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004fc7b0",
      "READ",
      [
        "storage",
        "00c9ade8",
        null,
        "pointer"
      ]
    ],
    [
      "004fc7b0",
      "PARAM",
      [
        "storage",
        "00c96698",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "004fc7b4",
      "READ",
      [
        "storage",
        "00c9adf0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fc778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fc/004fc734.md#insn-004fc778) · [`004fc740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fc/004fc734.md#insn-004fc740) · [`004fc758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fc/004fc734.md#insn-004fc758)
- 新版 [`004fc7b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fc/004fc774.md#insn-004fc7b8) · [`004fc780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fc/004fc774.md#insn-004fc780) · [`004fc798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fc/004fc774.md#insn-004fc798)

~~~diff
- 004fc778 ["INT_ADD", "register:40f0:8", ["const:4fc778:8", "const:4:8"]]
- 004fc778 ["CALL", null, ["callee:00c57f10:8"]]
+ 004fc7b8 ["INT_ADD", "register:40f0:8", ["const:4fc7b8:8", "const:4:8"]]
+ 004fc7b8 ["CALL", null, ["callee:00c57f10:8"]]
- 004fc778 bytes e66c1d94
+ 004fc7b8 bytes d66d1d94
- 004fc740 ["INT_ADD", "register:40f0:8", ["const:4fc740:8", "const:4:8"]]
- 004fc740 ["CALL", null, ["callee:00c58a30:8"]]
+ 004fc780 ["INT_ADD", "register:40f0:8", ["const:4fc780:8", "const:4:8"]]
+ 004fc780 ["CALL", null, ["callee:00c58a30:8"]]
- 004fc740 bytes bc6f1d94
+ 004fc780 bytes ac701d94
- 004fc758 ["INT_ADD", "register:40f0:8", ["const:4fc758:8", "const:4:8"]]
- 004fc758 ["CALL", null, ["callee:00c57ef0:8"]]
+ 004fc798 ["INT_ADD", "register:40f0:8", ["const:4fc798:8", "const:4:8"]]
+ 004fc798 ["CALL", null, ["callee:00c57ef0:8"]]
- 004fc758 bytes e66c1d94
+ 004fc798 bytes d66d1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

