# v16.0.1 → v16.0.2 · 最優先の変更候補 (26)

[一覧の目次](README.md)

<a id="compare-dc75ea283f1f3d17ad5bd33046939106"></a>

### [`0061304c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00613/0061304c.md) → [`0061308c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00613/0061308c.md) FUN_0061308c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) · 呼出先 43件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047c968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047c968.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md)
- 新版 呼出元 1件 [`00700b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700b50.md) · 呼出先 43件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047c9a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047c9a8.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.18% / 新版 91.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `call_target` 6件, `store_value` 11件

アドレスに依存する影響 `branch_value` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00613174",
      "incomplete_value": true,
      "site": "00613180",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00613134",
      "incomplete_value": true,
      "site": "00613140",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f40:8"
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
      "definition_site": "006131c0",
      "incomplete_value": true,
      "site": "006131dc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00613180",
      "incomplete_value": true,
      "site": "0061319c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d40:8"
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
      "definition_site": "0061341c",
      "incomplete_value": false,
      "site": "0061341c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:eb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006133dc",
      "incomplete_value": false,
      "site": "006133dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:de8:8"
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
      "00613108",
      "DATA",
      [
        "storage",
        "003c764c",
        "fde_003c764c",
        "dword"
      ]
    ],
    [
      "00613114",
      "DATA",
      [
        "storage",
        "003c764c",
        "fde_003c764c",
        "dword"
      ]
    ],
    [
      "00613174",
      "READ",
      [
        "storage",
        "002c3f40",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00613108",
      "DATA",
      [
        "storage",
        "003c764c",
        null,
        "dword"
      ]
    ],
    [
      "00613114",
      "DATA",
      [
        "storage",
        "003c764c",
        null,
        "dword"
      ]
    ],
    [
      "00613174",
      "READ",
      [
        "storage",
        "002c3f80",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00613180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00613/0061304c.md#insn-00613180) · [`00613220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00613/0061304c.md#insn-00613220) · [`00613260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00613/0061304c.md#insn-00613260)
- 新版 [`006131c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00613/0061308c.md#insn-006131c0) · [`00613260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00613/0061308c.md#insn-00613260) · [`006132a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00613/0061308c.md#insn-006132a0)

~~~diff
- 00613180 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d40:8"]]
- 00613180 ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
- 00613180 ["COPY", "register:5008:8", ["const:0:8"]]
- 00613180 ["COPY", "register:5010:8", ["const:0:8"]]
+ 006131c0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d80:8"]]
+ 006131c0 ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
+ 006131c0 ["COPY", "register:5008:8", ["const:0:8"]]
+ 006131c0 ["COPY", "register:5010:8", ["const:0:8"]]
- 00613180 bytes 00a146fd
+ 006131c0 bytes 00c146fd
- 00613220 ["INT_ADD", "register:40f0:8", ["const:613220:8", "const:4:8"]]
- 00613220 ["CALL", null, ["ram:48ccf8:8"]]
+ 00613260 ["INT_ADD", "register:40f0:8", ["const:613260:8", "const:4:8"]]
+ 00613260 ["CALL", null, ["ram:48cd38:8"]]
- 00613220 bytes b6e6f997
+ 00613260 bytes b6e6f997
- 00613260 ["INT_ADD", "register:40f0:8", ["const:613260:8", "const:4:8"]]
- 00613260 ["CALL", null, ["callee:004936d0:8"]]
+ 006132a0 ["INT_ADD", "register:40f0:8", ["const:6132a0:8", "const:4:8"]]
+ 006132a0 ["CALL", null, ["callee:004936d0:8"]]
- 00613260 bytes 0c01fa97
+ 006132a0 bytes 0c01fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8abc292b5b50d1d916d4f8d04e948f0"></a>

### [`00613c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00613/00613c64.md) → [`00613ca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00613/00613ca4.md) FUN_00613ca4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00707ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707ee0.md) · 呼出先 25件 [`00467af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467af0.md) [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f54.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`0046965c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/0046965c.md)
- 新版 呼出元 1件 [`00707f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00707/00707f38.md) · 呼出先 25件 [`00467b30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467b30.md) [`00467b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467b6c.md) [`00467f94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467f94.md) [`00468fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468fc8.md) [`0046969c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00469/0046969c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.22% / 新版 98.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006143fc",
      "incomplete_value": true,
      "site": "00614404",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006143bc",
      "incomplete_value": true,
      "site": "006143c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b68:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 54,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006144c8",
      "incomplete_value": true,
      "site": "006144cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00614488",
      "incomplete_value": true,
      "site": "0061448c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:978:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 62,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006144b4",
      "incomplete_value": false,
      "site": "006144cc",
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
            "const:f28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00614474",
      "incomplete_value": false,
      "site": "0061448c",
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
            "const:e58:8"
          ]
        ]
      ]
    },
    "ordinal": 62,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00613d34",
      "READ",
      [
        "storage",
        "00c9b4e8",
        null,
        "pointer"
      ]
    ],
    [
      "00613d4c",
      "READ",
      [
        "storage",
        "00ca406c",
        null,
        "undefined4"
      ]
    ],
    [
      "00613da8",
      "READ",
      [
        "storage",
        "00ca406c",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00613d34",
      "READ",
      [
        "storage",
        "00c9b5b8",
        null,
        "pointer"
      ]
    ],
    [
      "00613d4c",
      "READ",
      [
        "storage",
        "00ca413c",
        null,
        "undefined4"
      ]
    ],
    [
      "00613da8",
      "READ",
      [
        "storage",
        "00ca413c",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006143c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00613/00613c64.md#insn-006143c4) · [`0061448c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00613/00613c64.md#insn-0061448c) · [`006144cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00613/00613c64.md#insn-006144cc)
- 新版 [`00614404`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00613/00613ca4.md#insn-00614404) · [`006144cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00613/00613ca4.md#insn-006144cc) · [`0061450c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00613/00613ca4.md#insn-0061450c)

~~~diff
- 006143c4 ["INT_ADD", "register:40f0:8", ["const:6143c4:8", "const:4:8"]]
- 006143c4 ["CALL", null, ["callee:0046ccb4:8"]]
+ 00614404 ["INT_ADD", "register:40f0:8", ["const:614404:8", "const:4:8"]]
+ 00614404 ["CALL", null, ["callee:0046ccb4:8"]]
- 006143c4 bytes 2c62f997
+ 00614404 bytes 2c62f997
- 0061448c ["INT_ADD", "register:40f0:8", ["const:61448c:8", "const:4:8"]]
- 0061448c ["CALL", null, ["callee:00c586e0:8"]]
+ 006144cc ["INT_ADD", "register:40f0:8", ["const:6144cc:8", "const:4:8"]]
+ 006144cc ["CALL", null, ["callee:00c586e0:8"]]
- 0061448c bytes 61101994
+ 006144cc bytes 85101994
- 006144cc ["INT_ADD", "register:40f0:8", ["const:6144cc:8", "const:4:8"]]
- 006144cc ["CALL", null, ["callee:008b7a20:8"]]
+ 0061450c ["INT_ADD", "register:40f0:8", ["const:61450c:8", "const:4:8"]]
+ 0061450c ["CALL", null, ["callee:008b7a20:8"]]
- 006144cc bytes 3f8d0a94
+ 0061450c bytes 458d0a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90c0f400340794f58fc9e13c3e092907"></a>

### [`0061452c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00614/0061452c.md) → [`0061456c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00614/0061456c.md) FUN_0061456c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) · 呼出先 55件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046cc74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046cc74.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md)
- 新版 呼出元 1件 [`00700b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700b50.md) · 呼出先 55件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0046ccb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ccb4.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.29% / 新版 96.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `call_target` 5件, `store_value` 6件

アドレスに依存する影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006146b4",
      "incomplete_value": true,
      "site": "006146c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00614674",
      "incomplete_value": true,
      "site": "00614680",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f40:8"
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
      "definition_site": "00614730",
      "incomplete_value": true,
      "site": "00614734",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006146f0",
      "incomplete_value": true,
      "site": "006146f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00614788",
      "incomplete_value": true,
      "site": "00614790",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00614748",
      "incomplete_value": true,
      "site": "00614750",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 32,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006145fc",
      "DATA",
      [
        "storage",
        "003c764c",
        "fde_003c764c",
        "dword"
      ]
    ],
    [
      "00614608",
      "DATA",
      [
        "storage",
        "003c764c",
        "fde_003c764c",
        "dword"
      ]
    ],
    [
      "00614668",
      "DATA",
      [
        "storage",
        "00393ca8",
        null,
        "uleb128"
      ]
    ]
  ],
  "added": [
    [
      "006145fc",
      "DATA",
      [
        "storage",
        "003c764c",
        null,
        "dword"
      ]
    ],
    [
      "00614608",
      "DATA",
      [
        "storage",
        "003c764c",
        null,
        "dword"
      ]
    ],
    [
      "00614668",
      "DATA",
      [
        "storage",
        "00393ca8",
        null,
        "byte[59]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00614754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00614/0061452c.md#insn-00614754) · [`006147c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00614/0061452c.md#insn-006147c4) · [`006147c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00614/0061452c.md#insn-006147c8)
- 新版 [`00614794`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00614/0061456c.md#insn-00614794) · [`00614804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00614/0061456c.md#insn-00614804) · [`00614808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00614/0061456c.md#insn-00614808)

~~~diff
- 00614754 ["INT_ADD", "register:40f0:8", ["const:614754:8", "const:4:8"]]
- 00614754 ["CALL", null, ["ram:47acf4:8"]]
+ 00614794 ["INT_ADD", "register:40f0:8", ["const:614794:8", "const:4:8"]]
+ 00614794 ["CALL", null, ["ram:47ad34:8"]]
- 00614754 bytes 6899f997
+ 00614794 bytes 6899f997
- 006147c4 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:b68:8"]]
- 006147c4 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00614804 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:c38:8"]]
+ 00614804 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 006147c4 bytes 00b445f9
+ 00614804 bytes 001c46f9
- 006147c8 ["INT_ADD", "register:40f0:8", ["const:6147c8:8", "const:4:8"]]
- 006147c8 ["CALL", null, ["callee:0046ccb4:8"]]
+ 00614808 ["INT_ADD", "register:40f0:8", ["const:614808:8", "const:4:8"]]
+ 00614808 ["CALL", null, ["callee:0046ccb4:8"]]
- 006147c8 bytes 2b61f997
+ 00614808 bytes 2b61f997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d8c027a1e4ef0351ac53bca9c1b38c9"></a>

### [`00615910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00615/00615910.md) → [`00615950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00615/00615950.md) FUN_00615950

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`00604fec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00604/00604fec.md) [`007cb5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cb/007cb5e0.md) [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) [`00ad6a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad6/00ad6a88.md) · 呼出先 12件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00800378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/00800378.md) [`0080062c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/0080062c.md) [`00802630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802630.md)
- 新版 呼出元 4件 [`0060502c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00605/0060502c.md) [`007cb638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cb/007cb638.md) [`0089e8d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089e/0089e8d4.md) [`00ad6af8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ad6/00ad6af8.md) · 呼出先 12件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`008003d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00800/008003d0.md) [`00800684`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00800/00800684.md) [`00802688`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802688.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.36% / 新版 99.36%

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
      "site": "00615ab0",
      "value": [
        "leaf",
        "ram:a65e5c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00615a70",
      "value": [
        "leaf",
        "ram:a65dec:8"
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
      "00615ab0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65dec"
      ]
    ]
  ],
  "added": [
    [
      "00615ab0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65e5c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00615a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00615/00615910.md#insn-00615a70) · [`00615ab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00615/00615910.md#insn-00615ab0) · [`0061593c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00615/00615910.md#insn-0061593c)
- 新版 [`00615ab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00615/00615950.md#insn-00615ab0) · [`00615af0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00615/00615950.md#insn-00615af0) · [`0061597c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00615/00615950.md#insn-0061597c)

~~~diff
- 00615a70 ["INT_ADD", "register:40f0:8", ["const:615a70:8", "const:4:8"]]
- 00615a70 ["CALL", null, ["ram:a65dec:8"]]
+ 00615ab0 ["INT_ADD", "register:40f0:8", ["const:615ab0:8", "const:4:8"]]
+ 00615ab0 ["CALL", null, ["ram:a65e5c:8"]]
- 00615a70 bytes df401194
+ 00615ab0 bytes eb401194
- 00615ab0 ["INT_ADD", "register:40f0:8", ["const:615ab0:8", "const:4:8"]]
- 00615ab0 ["CALL", null, ["callee:008003d0:8"]]
+ 00615af0 ["INT_ADD", "register:40f0:8", ["const:615af0:8", "const:4:8"]]
+ 00615af0 ["CALL", null, ["callee:008003d0:8"]]
- 00615ab0 bytes 32aa0794
+ 00615af0 bytes 38aa0794
- 0061593c ["INT_ADD", "register:40f0:8", ["const:61593c:8", "const:4:8"]]
- 0061593c ["CALL", null, ["callee:008003d0:8"]]
+ 0061597c ["INT_ADD", "register:40f0:8", ["const:61597c:8", "const:4:8"]]
+ 0061597c ["CALL", null, ["callee:008003d0:8"]]
- 0061593c bytes 8faa0794
+ 0061597c bytes 95aa0794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad1c555bde61941484255515be27a925"></a>

### [`00615ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00615/00615ecc.md) → [`00615f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00615/00615f0c.md) FUN_00615f0c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 7件 [`00615cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00615/00615cd0.md) [`00615ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00615/00615ee0.md) [`006412fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00641/006412fc.md) [`0079065c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00790/0079065c.md) [`00793908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00793/00793908.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 7件 [`00615d10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00615/00615d10.md) [`00615f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00615/00615f20.md) [`0064133c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00641/0064133c.md) [`007906b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00790/007906b4.md) [`00793960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00793/00793960.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "00615f18",
      "incomplete_value": false,
      "site": "00615f1c",
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
      "definition_site": "00615ed8",
      "incomplete_value": false,
      "site": "00615edc",
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
      "00615f18",
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
      "00615f18",
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

- 旧版 [`00615edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00615/00615ecc.md#insn-00615edc) · [`00615ed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00615/00615ecc.md#insn-00615ed8)
- 新版 [`00615f1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00615/00615f0c.md#insn-00615f1c) · [`00615f18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00615/00615f0c.md#insn-00615f18)

~~~diff
- 00615edc ["INT_ADD", "register:40f0:8", ["const:615edc:8", "const:4:8"]]
- 00615edc ["CALL", null, ["callee:0043b7b8:8"]]
+ 00615f1c ["INT_ADD", "register:40f0:8", ["const:615f1c:8", "const:4:8"]]
+ 00615f1c ["CALL", null, ["callee:0043b7b8:8"]]
- 00615edc bytes 2796f897
+ 00615f1c bytes 2796f897
- 00615ed8 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00615ed8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00615ed8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00615ed8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00615f18 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00615f18 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00615f18 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00615f18 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00615ed8 bytes 00303d91
+ 00615f18 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-688c429d363f15f18b2db5465ff85735"></a>

### [`006161ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/006161ec.md) → [`0061622c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00616/0061622c.md) FUN_0061622c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0061624c",
      "incomplete_value": false,
      "site": "00616250",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:a88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061620c",
      "incomplete_value": false,
      "site": "00616210",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:9b8:8"
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
      "00616250",
      "DATA",
      [
        "storage",
        "00c719b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00616250",
      "DATA",
      [
        "storage",
        "00c71a88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00616200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/006161ec.md#insn-00616200) · [`0061620c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/006161ec.md#insn-0061620c)
- 新版 [`00616240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00616/0061622c.md#insn-00616240) · [`0061624c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00616/0061622c.md#insn-0061624c)

~~~diff
- 00616200 ["INT_ADD", "register:40f0:8", ["const:616200:8", "const:4:8"]]
- 00616200 ["CALL", null, ["callee:00c57f60:8"]]
+ 00616240 ["INT_ADD", "register:40f0:8", ["const:616240:8", "const:4:8"]]
+ 00616240 ["CALL", null, ["callee:00c57f60:8"]]
- 00616200 bytes 24071994
+ 00616240 bytes 48071994
- 0061620c ["COPY", "tmp:0:8", ["const:9b8:8"]]
- 0061620c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061620c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061620c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061624c ["COPY", "tmp:0:8", ["const:a88:8"]]
+ 0061624c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061624c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061624c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061620c bytes 08e12691
+ 0061624c bytes 08212a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1375ef58131d7eb9cd57875a10943522"></a>

### [`00616244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/00616244.md) → [`00616284`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00616/00616284.md) FUN_00616284

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 18件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`0052dd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052dd00.md)
- 新版 呼出元 0件  · 呼出先 18件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`0052dd40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052dd40.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00616348",
      "incomplete_value": true,
      "site": "00616348",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:ea7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00616308",
      "incomplete_value": true,
      "site": "00616308",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:e76:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00616490",
      "incomplete_value": false,
      "site": "00616490",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:af8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00616450",
      "incomplete_value": false,
      "site": "00616450",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:a28:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006162c8",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00616288",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "006162c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "006162e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00616330",
      "READ",
      [
        "storage",
        "002b1e76",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006162c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "006162e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00616330",
      "READ",
      [
        "storage",
        "002b1ea7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00616288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/00616244.md#insn-00616288) · [`006162a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/00616244.md#insn-006162a4) · [`00616348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/00616244.md#insn-00616348)
- 新版 [`006162c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00616/00616284.md#insn-006162c8) · [`006162e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00616/00616284.md#insn-006162e4) · [`00616388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00616/00616284.md#insn-00616388)

~~~diff
- 00616288 ["INT_ADD", "register:40f0:8", ["const:616288:8", "const:4:8"]]
- 00616288 ["CALL", null, ["ram:47acf4:8"]]
+ 006162c8 ["INT_ADD", "register:40f0:8", ["const:6162c8:8", "const:4:8"]]
+ 006162c8 ["CALL", null, ["ram:47ad34:8"]]
- 00616288 bytes 9b92f997
+ 006162c8 bytes 9b92f997
- 006162a4 ["INT_ADD", "register:40f0:8", ["const:6162a4:8", "const:4:8"]]
- 006162a4 ["CALL", null, ["ram:47acf4:8"]]
+ 006162e4 ["INT_ADD", "register:40f0:8", ["const:6162e4:8", "const:4:8"]]
+ 006162e4 ["CALL", null, ["ram:47ad34:8"]]
- 006162a4 bytes 9492f997
+ 006162e4 bytes 9492f997
- 00616348 ["INT_ADD", "register:40f0:8", ["const:616348:8", "const:4:8"]]
- 00616348 ["CALL", null, ["callee:008b6f70:8"]]
+ 00616388 ["INT_ADD", "register:40f0:8", ["const:616388:8", "const:4:8"]]
+ 00616388 ["CALL", null, ["callee:008b6f70:8"]]
- 00616348 bytes f4820a94
+ 00616388 bytes fa820a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd27b34b80e24f8d05288ffaaa8f85f6"></a>

### [`006166b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/006166b4.md) → [`006166f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00616/006166f4.md) FUN_006166f4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00616718",
      "incomplete_value": true,
      "site": "0061671c",
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
            "const:af8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006166d8",
      "incomplete_value": true,
      "site": "006166dc",
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
            "const:a28:8"
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
      "0061671c",
      "DATA",
      [
        "storage",
        "00c71a28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061671c",
      "DATA",
      [
        "storage",
        "00c71af8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006166c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/006166b4.md#insn-006166c8) · [`006166d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/006166b4.md#insn-006166d8)
- 新版 [`00616708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00616/006166f4.md#insn-00616708) · [`00616718`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00616/006166f4.md#insn-00616718)

~~~diff
- 006166c8 ["INT_ADD", "register:40f0:8", ["const:6166c8:8", "const:4:8"]]
- 006166c8 ["CALL", null, ["callee:00c57f60:8"]]
+ 00616708 ["INT_ADD", "register:40f0:8", ["const:616708:8", "const:4:8"]]
+ 00616708 ["CALL", null, ["callee:00c57f60:8"]]
- 006166c8 bytes f2051994
+ 00616708 bytes 16061994
- 006166d8 ["COPY", "tmp:0:8", ["const:a28:8"]]
- 006166d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006166d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006166d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00616718 ["COPY", "tmp:0:8", ["const:af8:8"]]
+ 00616718 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00616718 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00616718 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006166d8 bytes 08a12891
+ 00616718 bytes 08e12b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93d99fe1ba2bb97e71fedf299bc2a962"></a>

### [`006166f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/006166f4.md) → [`00616734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00616/00616734.md) FUN_00616734

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00616738",
      "incomplete_value": false,
      "site": "0061673c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:af8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006166f8",
      "incomplete_value": false,
      "site": "006166fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:a28:8"
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
      "0061673c",
      "DATA",
      [
        "storage",
        "00c71a28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061673c",
      "DATA",
      [
        "storage",
        "00c71af8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006166f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/006166f4.md#insn-006166f8)
- 新版 [`00616738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00616/00616734.md#insn-00616738)

~~~diff
- 006166f8 ["COPY", "tmp:0:8", ["const:a28:8"]]
- 006166f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006166f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006166f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00616738 ["COPY", "tmp:0:8", ["const:af8:8"]]
+ 00616738 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00616738 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00616738 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006166f8 bytes 08a12891
+ 00616738 bytes 08e12b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ce6584d6bb5fdbf66eb4ce7c328065d"></a>

### [`0061671c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/0061671c.md) → [`0061675c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00616/0061675c.md) FUN_0061675c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0047ce28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047ce28.md) [`00616948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/00616948.md) [`0061694c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/0061694c.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0047ce68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce68.md) [`00616988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00616/00616988.md) [`0061698c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00616/0061698c.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.29% / 新版 95.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00616828",
      "incomplete_value": false,
      "site": "00616828",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:b68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006167e8",
      "incomplete_value": false,
      "site": "006167e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:a98:8"
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
      "site": "006167a0",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00616760",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "site": "00616808",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006167c8",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "006167a0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00616808",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00616828",
      "DATA",
      [
        "storage",
        "00c71a98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006167a0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00616808",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00616828",
      "DATA",
      [
        "storage",
        "00c71b68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00616760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/0061671c.md#insn-00616760) · [`006167c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/0061671c.md#insn-006167c8) · [`0061676c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/0061671c.md#insn-0061676c)
- 新版 [`006167a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00616/0061675c.md#insn-006167a0) · [`00616808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00616/0061675c.md#insn-00616808) · [`006167ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00616/0061675c.md#insn-006167ac)

~~~diff
- 00616760 ["INT_ADD", "register:40f0:8", ["const:616760:8", "const:4:8"]]
- 00616760 ["CALL", null, ["ram:47acf4:8"]]
+ 006167a0 ["INT_ADD", "register:40f0:8", ["const:6167a0:8", "const:4:8"]]
+ 006167a0 ["CALL", null, ["ram:47ad34:8"]]
- 00616760 bytes 6591f997
+ 006167a0 bytes 6591f997
- 006167c8 ["INT_ADD", "register:40f0:8", ["const:6167c8:8", "const:4:8"]]
- 006167c8 ["CALL", null, ["ram:47acf4:8"]]
+ 00616808 ["INT_ADD", "register:40f0:8", ["const:616808:8", "const:4:8"]]
+ 00616808 ["CALL", null, ["ram:47ad34:8"]]
- 006167c8 bytes 4b91f997
+ 00616808 bytes 4b91f997
- 0061676c ["INT_ADD", "register:40f0:8", ["const:61676c:8", "const:4:8"]]
- 0061676c ["CALL", null, ["callee:0047ce14:8"]]
+ 006167ac ["INT_ADD", "register:40f0:8", ["const:6167ac:8", "const:4:8"]]
+ 006167ac ["CALL", null, ["callee:0047ce14:8"]]
- 0061676c bytes 9a99f997
+ 006167ac bytes 9a99f997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d6c1a5ffd16a89a7292d340c9981367"></a>

### [`006168e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/006168e8.md) → [`00616928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00616/00616928.md) FUN_00616928

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0061694c",
      "incomplete_value": false,
      "site": "00616950",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:b68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061690c",
      "incomplete_value": false,
      "site": "00616910",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:a98:8"
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
      "00616950",
      "DATA",
      [
        "storage",
        "00c71a98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00616950",
      "DATA",
      [
        "storage",
        "00c71b68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006168fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/006168e8.md#insn-006168fc) · [`0061690c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/006168e8.md#insn-0061690c)
- 新版 [`0061693c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00616/00616928.md#insn-0061693c) · [`0061694c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00616/00616928.md#insn-0061694c)

~~~diff
- 006168fc ["INT_ADD", "register:40f0:8", ["const:6168fc:8", "const:4:8"]]
- 006168fc ["CALL", null, ["callee:00c57f60:8"]]
+ 0061693c ["INT_ADD", "register:40f0:8", ["const:61693c:8", "const:4:8"]]
+ 0061693c ["CALL", null, ["callee:00c57f60:8"]]
- 006168fc bytes 65051994
+ 0061693c bytes 89051994
- 0061690c ["COPY", "tmp:0:8", ["const:a98:8"]]
- 0061690c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061690c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061690c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061694c ["COPY", "tmp:0:8", ["const:b68:8"]]
+ 0061694c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061694c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061694c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061690c bytes 08612a91
+ 0061694c bytes 08a12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b0f6a546fafb85136a4400e940e34eb"></a>

### [`00616928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/00616928.md) → [`00616968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00616/00616968.md) FUN_00616968

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0061696c",
      "incomplete_value": false,
      "site": "00616970",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:b68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061692c",
      "incomplete_value": false,
      "site": "00616930",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:a98:8"
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
      "00616970",
      "DATA",
      [
        "storage",
        "00c71a98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00616970",
      "DATA",
      [
        "storage",
        "00c71b68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061692c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/00616928.md#insn-0061692c)
- 新版 [`0061696c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00616/00616968.md#insn-0061696c)

~~~diff
- 0061692c ["COPY", "tmp:0:8", ["const:a98:8"]]
- 0061692c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061692c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061692c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061696c ["COPY", "tmp:0:8", ["const:b68:8"]]
+ 0061696c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061696c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061696c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061692c bytes 08612a91
+ 0061696c bytes 08a12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb02d8dce1bcca246423f99814645151"></a>

### [`00616950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/00616950.md) → [`00616990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00616/00616990.md) FUN_00616990

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 23件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0047cf08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cf08.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)
- 新版 呼出元 0件  · 呼出先 23件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0047cf48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047cf48.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.57% / 新版 94.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00616ae8",
      "incomplete_value": false,
      "site": "00616ae8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:bd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00616aa8",
      "incomplete_value": false,
      "site": "00616aa8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:b08:8"
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
      "definition_site": "00616b74",
      "incomplete_value": true,
      "site": "00616b88",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:bc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00616b34",
      "incomplete_value": true,
      "site": "00616b48",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:110:8"
              ]
            ]
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
      "definition_site": "00616ba8",
      "incomplete_value": false,
      "site": "00616ba8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:c58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00616b68",
      "incomplete_value": false,
      "site": "00616b68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:b88:8"
          ]
        ]
      ]
    },
    "ordinal": 32,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006169cc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "006169fc",
      "DATA",
      [
        "storage",
        "00436b50",
        null,
        "byte[55]"
      ]
    ],
    [
      "00616a10",
      "DATA",
      [
        "storage",
        "00436b50",
        null,
        "byte[55]"
      ]
    ]
  ],
  "added": [
    [
      "006169cc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "006169fc",
      "DATA",
      [
        "storage",
        "00436b50",
        "fde_00436b50",
        "dword"
      ]
    ],
    [
      "00616a10",
      "DATA",
      [
        "storage",
        "00436b50",
        "fde_00436b50",
        "dword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061698c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/00616950.md#insn-0061698c) · [`006169d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/00616950.md#insn-006169d8) · [`00616b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/00616950.md#insn-00616b08)
- 新版 [`006169cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00616/00616990.md#insn-006169cc) · [`00616a18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00616/00616990.md#insn-00616a18) · [`00616b48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00616/00616990.md#insn-00616b48)

~~~diff
- 0061698c ["INT_ADD", "register:40f0:8", ["const:61698c:8", "const:4:8"]]
- 0061698c ["CALL", null, ["ram:47acf4:8"]]
+ 006169cc ["INT_ADD", "register:40f0:8", ["const:6169cc:8", "const:4:8"]]
+ 006169cc ["CALL", null, ["ram:47ad34:8"]]
- 0061698c bytes da90f997
+ 006169cc bytes da90f997
- 006169d8 ["INT_ADD", "register:40f0:8", ["const:6169d8:8", "const:4:8"]]
- 006169d8 ["CALL", null, ["ram:47acf4:8"]]
+ 00616a18 ["INT_ADD", "register:40f0:8", ["const:616a18:8", "const:4:8"]]
+ 00616a18 ["CALL", null, ["ram:47ad34:8"]]
- 006169d8 bytes c790f997
+ 00616a18 bytes c790f997
- 00616b08 ["INT_ADD", "register:40f0:8", ["const:616b08:8", "const:4:8"]]
- 00616b08 ["CALL", null, ["callee:00888304:8"]]
+ 00616b48 ["INT_ADD", "register:40f0:8", ["const:616b48:8", "const:4:8"]]
+ 00616b48 ["CALL", null, ["callee:00888304:8"]]
- 00616b08 bytes e9c50994
+ 00616b48 bytes efc50994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53ca24494a4eb14d030301c874b8f4fd"></a>

### [`00616e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/00616e4c.md) → [`00616e8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00616/00616e8c.md) FUN_00616e8c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00616eac",
      "incomplete_value": false,
      "site": "00616eb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:bd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00616e6c",
      "incomplete_value": false,
      "site": "00616e70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:b08:8"
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
      "00616eb0",
      "DATA",
      [
        "storage",
        "00c71b08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00616eb0",
      "DATA",
      [
        "storage",
        "00c71bd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00616e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/00616e4c.md#insn-00616e60) · [`00616e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/00616e4c.md#insn-00616e6c)
- 新版 [`00616ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00616/00616e8c.md#insn-00616ea0) · [`00616eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00616/00616e8c.md#insn-00616eac)

~~~diff
- 00616e60 ["INT_ADD", "register:40f0:8", ["const:616e60:8", "const:4:8"]]
- 00616e60 ["CALL", null, ["callee:00c57f60:8"]]
+ 00616ea0 ["INT_ADD", "register:40f0:8", ["const:616ea0:8", "const:4:8"]]
+ 00616ea0 ["CALL", null, ["callee:00c57f60:8"]]
- 00616e60 bytes 0c041994
+ 00616ea0 bytes 30041994
- 00616e6c ["COPY", "tmp:0:8", ["const:b08:8"]]
- 00616e6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00616e6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00616e6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00616eac ["COPY", "tmp:0:8", ["const:bd8:8"]]
+ 00616eac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00616eac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00616eac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00616e6c bytes 08212c91
+ 00616eac bytes 08612f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a708b6c6ba9d7f3433d30b6113fdb104"></a>

### [`00616e84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/00616e84.md) → [`00616ec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00616/00616ec4.md) FUN_00616ec4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00616ec8",
      "incomplete_value": false,
      "site": "00616ecc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:bd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00616e88",
      "incomplete_value": false,
      "site": "00616e8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:b08:8"
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
      "00616ecc",
      "DATA",
      [
        "storage",
        "00c71b08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00616ecc",
      "DATA",
      [
        "storage",
        "00c71bd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00616e88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/00616e84.md#insn-00616e88)
- 新版 [`00616ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00616/00616ec4.md#insn-00616ec8)

~~~diff
- 00616e88 ["COPY", "tmp:0:8", ["const:b08:8"]]
- 00616e88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00616e88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00616e88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00616ec8 ["COPY", "tmp:0:8", ["const:bd8:8"]]
+ 00616ec8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00616ec8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00616ec8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00616e88 bytes 08212c91
+ 00616ec8 bytes 08612f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70c5e17e1607226e18aa60418b1dc733"></a>

### [`00616f04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/00616f04.md) → [`00616f44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00616/00616f44.md) FUN_00616f44

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00616f64",
      "incomplete_value": false,
      "site": "00616f68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:c58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00616f24",
      "incomplete_value": false,
      "site": "00616f28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:b88:8"
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
      "00616f68",
      "DATA",
      [
        "storage",
        "00c71b88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00616f68",
      "DATA",
      [
        "storage",
        "00c71c58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00616f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/00616f04.md#insn-00616f18) · [`00616f24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/00616f04.md#insn-00616f24)
- 新版 [`00616f58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00616/00616f44.md#insn-00616f58) · [`00616f64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00616/00616f44.md#insn-00616f64)

~~~diff
- 00616f18 ["INT_ADD", "register:40f0:8", ["const:616f18:8", "const:4:8"]]
- 00616f18 ["CALL", null, ["callee:00c57f60:8"]]
+ 00616f58 ["INT_ADD", "register:40f0:8", ["const:616f58:8", "const:4:8"]]
+ 00616f58 ["CALL", null, ["callee:00c57f60:8"]]
- 00616f18 bytes de031994
+ 00616f58 bytes 02041994
- 00616f24 ["COPY", "tmp:0:8", ["const:b88:8"]]
- 00616f24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00616f24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00616f24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00616f64 ["COPY", "tmp:0:8", ["const:c58:8"]]
+ 00616f64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00616f64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00616f64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00616f24 bytes 08212e91
+ 00616f64 bytes 08613191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d29ae925b59e69fb612d14d2c581a89a"></a>

### [`00616f3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/00616f3c.md) → [`00616f7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00616/00616f7c.md) FUN_00616f7c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00616f80",
      "incomplete_value": false,
      "site": "00616f84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:c58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00616f40",
      "incomplete_value": false,
      "site": "00616f44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:b88:8"
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
      "00616f84",
      "DATA",
      [
        "storage",
        "00c71b88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00616f84",
      "DATA",
      [
        "storage",
        "00c71c58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00616f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/00616f3c.md#insn-00616f40)
- 新版 [`00616f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00616/00616f7c.md#insn-00616f80)

~~~diff
- 00616f40 ["COPY", "tmp:0:8", ["const:b88:8"]]
- 00616f40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00616f40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00616f40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00616f80 ["COPY", "tmp:0:8", ["const:c58:8"]]
+ 00616f80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00616f80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00616f80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00616f40 bytes 08212e91
+ 00616f80 bytes 08613191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ea0e72f3eddd58fa006721407c65594"></a>

### [`00616f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/00616f5c.md) → [`00616f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00616/00616f9c.md) FUN_00616f9c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.15% / 新版 96.15%

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
      "site": "00616fcc",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00616f8c",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "00616fcc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "00616fcc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00616f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/00616f5c.md#insn-00616f8c) · [`00616f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/00616f5c.md#insn-00616f98) · [`00616fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/00616f5c.md#insn-00616fa0)
- 新版 [`00616fcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00616/00616f9c.md#insn-00616fcc) · [`00616fd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00616/00616f9c.md#insn-00616fd8) · [`00616fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00616/00616f9c.md#insn-00616fe0)

~~~diff
- 00616f8c ["INT_ADD", "register:40f0:8", ["const:616f8c:8", "const:4:8"]]
- 00616f8c ["CALL", null, ["ram:47acf4:8"]]
+ 00616fcc ["INT_ADD", "register:40f0:8", ["const:616fcc:8", "const:4:8"]]
+ 00616fcc ["CALL", null, ["ram:47ad34:8"]]
- 00616f8c bytes 5a8ff997
+ 00616fcc bytes 5a8ff997
- 00616f98 ["INT_ADD", "register:40f0:8", ["const:616f98:8", "const:4:8"]]
- 00616f98 ["CALL", null, ["callee:0047ce14:8"]]
+ 00616fd8 ["INT_ADD", "register:40f0:8", ["const:616fd8:8", "const:4:8"]]
+ 00616fd8 ["CALL", null, ["callee:0047ce14:8"]]
- 00616f98 bytes 8f97f997
+ 00616fd8 bytes 8f97f997
- 00616fa0 ["INT_ADD", "register:40f0:8", ["const:616fa0:8", "const:4:8"]]
- 00616fa0 ["CALL", null, ["callee:008b91d0:8"]]
+ 00616fe0 ["INT_ADD", "register:40f0:8", ["const:616fe0:8", "const:4:8"]]
+ 00616fe0 ["CALL", null, ["callee:008b91d0:8"]]
- 00616fa0 bytes 76880a94
+ 00616fe0 bytes 7c880a94
~~~


<a id="compare-fb519b26aa3c69338109cef06d1b4897"></a>

### [`00616ff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/00616ff0.md) → [`00617030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00617/00617030.md) FUN_00617030

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
      "definition_site": "00617044",
      "incomplete_value": false,
      "site": "00617048",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:d08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00617004",
      "incomplete_value": false,
      "site": "00617008",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:c38:8"
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
      "00617048",
      "DATA",
      [
        "storage",
        "00c71c38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00617048",
      "DATA",
      [
        "storage",
        "00c71d08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00616ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/00616ff0.md#insn-00616ffc) · [`00617004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00616/00616ff0.md#insn-00617004)
- 新版 [`0061703c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00617/00617030.md#insn-0061703c) · [`00617044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00617/00617030.md#insn-00617044)

~~~diff
- 00616ffc ["INT_ADD", "register:40f0:8", ["const:616ffc:8", "const:4:8"]]
- 00616ffc ["CALL", null, ["callee:00c57f60:8"]]
+ 0061703c ["INT_ADD", "register:40f0:8", ["const:61703c:8", "const:4:8"]]
+ 0061703c ["CALL", null, ["callee:00c57f60:8"]]
- 00616ffc bytes a5031994
+ 0061703c bytes c9031994
- 00617004 ["COPY", "tmp:0:8", ["const:c38:8"]]
- 00617004 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00617004 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00617004 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00617044 ["COPY", "tmp:0:8", ["const:d08:8"]]
+ 00617044 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00617044 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00617044 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00617004 bytes 08e13091
+ 00617044 bytes 08213491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00a7d598562cf22db12778bc300699c3"></a>

### [`0061705c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00617/0061705c.md) → [`0061709c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00617/0061709c.md) FUN_0061709c

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
      "definition_site": "006170c0",
      "incomplete_value": false,
      "site": "006170c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00617080",
      "incomplete_value": false,
      "site": "00617080",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:cc8:8"
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
      "006170c0",
      "DATA",
      [
        "storage",
        "00c71cc8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006170c0",
      "DATA",
      [
        "storage",
        "00c71d98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00617070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00617/0061705c.md#insn-00617070) · [`0061707c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00617/0061705c.md#insn-0061707c)
- 新版 [`006170b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00617/0061709c.md#insn-006170b0) · [`006170bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00617/0061709c.md#insn-006170bc)

~~~diff
- 00617070 ["INT_ADD", "register:40f0:8", ["const:617070:8", "const:4:8"]]
- 00617070 ["CALL", null, ["callee:00c57f60:8"]]
+ 006170b0 ["INT_ADD", "register:40f0:8", ["const:6170b0:8", "const:4:8"]]
+ 006170b0 ["CALL", null, ["callee:00c57f60:8"]]
- 00617070 bytes 88031994
+ 006170b0 bytes ac031994
- 0061707c ["COPY", "tmp:0:8", ["const:cc8:8"]]
- 0061707c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061707c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061707c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006170bc ["COPY", "tmp:0:8", ["const:d98:8"]]
+ 006170bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006170bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006170bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061707c bytes 08213391
+ 006170bc bytes 08613691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86d522fcb1fb9a742cc94f824b9e4f45"></a>

### [`00617090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00617/00617090.md) → [`006170d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00617/006170d0.md) FUN_006170d0

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
      "definition_site": "006170dc",
      "incomplete_value": false,
      "site": "006170dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061709c",
      "incomplete_value": false,
      "site": "0061709c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:cc8:8"
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
      "006170dc",
      "DATA",
      [
        "storage",
        "00c71cc8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006170dc",
      "DATA",
      [
        "storage",
        "00c71d98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00617098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00617/00617090.md#insn-00617098)
- 新版 [`006170d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00617/006170d0.md#insn-006170d8)

~~~diff
- 00617098 ["COPY", "tmp:0:8", ["const:cc8:8"]]
- 00617098 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00617098 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00617098 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006170d8 ["COPY", "tmp:0:8", ["const:d98:8"]]
+ 006170d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006170d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006170d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00617098 bytes 29213391
+ 006170d8 bytes 29613691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2dcc07d3796a16a53f148859ff69f994"></a>

### [`006170ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00617/006170ac.md) → [`006170ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00617/006170ec.md) FUN_006170ec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0060e0c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0060e/0060e0c4.md) [`008200b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00820/008200b4.md) [`008b6f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f18.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0060e104`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0060e/0060e104.md) [`0082010c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00820/0082010c.md) [`008b6f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6f70.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00617110",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006170d0",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "site": "0061712c",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006170ec",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "site": "0061715c",
      "value": [
        "leaf",
        "ram:82010c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0061711c",
      "value": [
        "leaf",
        "ram:8200b4:8"
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
      "00617110",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "0061712c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "0061715c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "008200b4"
      ]
    ]
  ],
  "added": [
    [
      "00617110",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "0061712c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "0061715c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0082010c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006170d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00617/006170ac.md#insn-006170d0) · [`006170ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00617/006170ac.md#insn-006170ec) · [`0061711c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00617/006170ac.md#insn-0061711c)
- 新版 [`00617110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00617/006170ec.md#insn-00617110) · [`0061712c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00617/006170ec.md#insn-0061712c) · [`0061715c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00617/006170ec.md#insn-0061715c)

~~~diff
- 006170d0 ["INT_ADD", "register:40f0:8", ["const:6170d0:8", "const:4:8"]]
- 006170d0 ["CALL", null, ["ram:47acf4:8"]]
+ 00617110 ["INT_ADD", "register:40f0:8", ["const:617110:8", "const:4:8"]]
+ 00617110 ["CALL", null, ["ram:47ad34:8"]]
- 006170d0 bytes 098ff997
+ 00617110 bytes 098ff997
- 006170ec ["INT_ADD", "register:40f0:8", ["const:6170ec:8", "const:4:8"]]
- 006170ec ["CALL", null, ["ram:47acf4:8"]]
+ 0061712c ["INT_ADD", "register:40f0:8", ["const:61712c:8", "const:4:8"]]
+ 0061712c ["CALL", null, ["ram:47ad34:8"]]
- 006170ec bytes 028ff997
+ 0061712c bytes 028ff997
- 0061711c ["INT_ADD", "register:40f0:8", ["const:61711c:8", "const:4:8"]]
- 0061711c ["CALL", null, ["ram:8200b4:8"]]
+ 0061715c ["INT_ADD", "register:40f0:8", ["const:61715c:8", "const:4:8"]]
+ 0061715c ["CALL", null, ["ram:82010c:8"]]
- 0061711c bytes e6230894
+ 0061715c bytes ec230894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4bbabbb9863d378d4e3dd7a331038107"></a>

### [`00617370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00617/00617370.md) → [`006173b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00617/006173b0.md) FUN_006173b0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`006171ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00617/006171ac.md) [`00617370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00617/00617370.md) [`0061bbd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061b/0061bbd0.md) · 呼出先 21件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`004412b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/004412b8.md)
- 新版 呼出元 3件 [`006171ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00617/006171ec.md) [`006173b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00617/006173b0.md) [`0061bc10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061b/0061bc10.md) · 呼出先 21件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`004412f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004412f8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.92% / 新版 98.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00617520",
      "incomplete_value": true,
      "site": "0061752c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4008:8"
          ],
          [
            "leaf",
            "const:f93:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006174e0",
      "incomplete_value": true,
      "site": "006174ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4008:8"
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
      "definition_site": "006175d8",
      "incomplete_value": false,
      "site": "006175e0",
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
      "definition_site": "00617598",
      "incomplete_value": false,
      "site": "006175a0",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006176a4",
      "incomplete_value": false,
      "site": "006176b4",
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
      "definition_site": "00617664",
      "incomplete_value": false,
      "site": "00617674",
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
      "00617520",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "006175d8",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ],
    [
      "006175f0",
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
      "00617520",
      "PARAM",
      [
        "storage",
        "002b7f93",
        null,
        null
      ]
    ],
    [
      "006175d8",
      "PARAM",
      [
        "storage",
        "002b5e27",
        null,
        null
      ]
    ],
    [
      "006175f0",
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

- 旧版 [`006174ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00617/00617370.md#insn-006174ec) · [`006175a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00617/00617370.md#insn-006175a0) · [`00617674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00617/00617370.md#insn-00617674)
- 新版 [`0061752c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00617/006173b0.md#insn-0061752c) · [`006175e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00617/006173b0.md#insn-006175e0) · [`006176b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00617/006173b0.md#insn-006176b4)

~~~diff
- 006174ec ["INT_ADD", "register:40f0:8", ["const:6174ec:8", "const:4:8"]]
- 006174ec ["CALL", null, ["callee:00441ed4:8"]]
+ 0061752c ["INT_ADD", "register:40f0:8", ["const:61752c:8", "const:4:8"]]
+ 0061752c ["CALL", null, ["callee:00441ed4:8"]]
- 006174ec bytes 6aaaf897
+ 0061752c bytes 6aaaf897
- 006175a0 ["INT_ADD", "register:40f0:8", ["const:6175a0:8", "const:4:8"]]
- 006175a0 ["CALL", null, ["callee:00441ed4:8"]]
+ 006175e0 ["INT_ADD", "register:40f0:8", ["const:6175e0:8", "const:4:8"]]
+ 006175e0 ["CALL", null, ["callee:00441ed4:8"]]
- 006175a0 bytes 3daaf897
+ 006175e0 bytes 3daaf897
- 00617674 ["INT_ADD", "register:40f0:8", ["const:617674:8", "const:4:8"]]
- 00617674 ["CALL", null, ["callee:00442834:8"]]
+ 006176b4 ["INT_ADD", "register:40f0:8", ["const:6176b4:8", "const:4:8"]]
+ 006176b4 ["CALL", null, ["callee:00442834:8"]]
- 00617674 bytes 60acf897
+ 006176b4 bytes 60acf897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02164bb9f944ab8660762142bc21e2d7"></a>

### [`00617f44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00617/00617f44.md) → [`00617f84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00617/00617f84.md) FUN_00617f84

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
      "definition_site": "00617fa8",
      "incomplete_value": false,
      "site": "00617fa8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:e18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00617f68",
      "incomplete_value": false,
      "site": "00617f68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:d48:8"
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
      "00617fa8",
      "DATA",
      [
        "storage",
        "00c71d48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00617fa8",
      "DATA",
      [
        "storage",
        "00c71e18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00617f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00617/00617f44.md#insn-00617f58) · [`00617f64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00617/00617f44.md#insn-00617f64)
- 新版 [`00617f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00617/00617f84.md#insn-00617f98) · [`00617fa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00617/00617f84.md#insn-00617fa4)

~~~diff
- 00617f58 ["INT_ADD", "register:40f0:8", ["const:617f58:8", "const:4:8"]]
- 00617f58 ["CALL", null, ["callee:00c57f60:8"]]
+ 00617f98 ["INT_ADD", "register:40f0:8", ["const:617f98:8", "const:4:8"]]
+ 00617f98 ["CALL", null, ["callee:00c57f60:8"]]
- 00617f58 bytes ceff1894
+ 00617f98 bytes f2ff1894
- 00617f64 ["COPY", "tmp:0:8", ["const:d48:8"]]
- 00617f64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00617f64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00617f64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00617fa4 ["COPY", "tmp:0:8", ["const:e18:8"]]
+ 00617fa4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00617fa4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00617fa4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00617f64 bytes 08213591
+ 00617fa4 bytes 08613891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bcee768d83ca00ab80cd258a98267d99"></a>

### [`00617f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00617/00617f94.md) → [`00617fd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00617/00617fd4.md) FUN_00617fd4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`00597644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597644.md) [`006181c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00618/006181c8.md) [`006181cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00618/006181cc.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00597684`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597684.md) [`00618208`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00618/00618208.md) [`0061820c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00618/0061820c.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.40% / 新版 95.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006180c4",
      "incomplete_value": false,
      "site": "006180c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:e88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00618084",
      "incomplete_value": false,
      "site": "00618084",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:db8:8"
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
      "site": "00618010",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00617fd0",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "site": "0061802c",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00617fec",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "00618010",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "0061802c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "006180c4",
      "DATA",
      [
        "storage",
        "00c71db8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00618010",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "0061802c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "006180c4",
      "DATA",
      [
        "storage",
        "00c71e88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00617fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00617/00617f94.md#insn-00617fd0) · [`00617fec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00617/00617f94.md#insn-00617fec) · [`00618044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00617/00617f94.md#insn-00618044)
- 新版 [`00618010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00617/00617fd4.md#insn-00618010) · [`0061802c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00617/00617fd4.md#insn-0061802c) · [`00618084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00617/00617fd4.md#insn-00618084)

~~~diff
- 00617fd0 ["INT_ADD", "register:40f0:8", ["const:617fd0:8", "const:4:8"]]
- 00617fd0 ["CALL", null, ["ram:47acf4:8"]]
+ 00618010 ["INT_ADD", "register:40f0:8", ["const:618010:8", "const:4:8"]]
+ 00618010 ["CALL", null, ["ram:47ad34:8"]]
- 00617fd0 bytes 498bf997
+ 00618010 bytes 498bf997
- 00617fec ["INT_ADD", "register:40f0:8", ["const:617fec:8", "const:4:8"]]
- 00617fec ["CALL", null, ["ram:47acf4:8"]]
+ 0061802c ["INT_ADD", "register:40f0:8", ["const:61802c:8", "const:4:8"]]
+ 0061802c ["CALL", null, ["ram:47ad34:8"]]
- 00617fec bytes 428bf997
+ 0061802c bytes 428bf997
- 00618044 ["INT_ADD", "register:40f0:8", ["const:618044:8", "const:4:8"]]
- 00618044 ["CALL", null, ["callee:008b7a20:8"]]
+ 00618084 ["INT_ADD", "register:40f0:8", ["const:618084:8", "const:4:8"]]
+ 00618084 ["CALL", null, ["callee:008b7a20:8"]]
- 00618044 bytes 617e0a94
+ 00618084 bytes 677e0a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df45747122383b0eafaa2d24522753e2"></a>

### [`00618168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00618/00618168.md) → [`006181a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00618/006181a8.md) FUN_006181a8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006181cc",
      "incomplete_value": false,
      "site": "006181d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:e88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061818c",
      "incomplete_value": false,
      "site": "00618190",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:db8:8"
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
      "006181d0",
      "DATA",
      [
        "storage",
        "00c71db8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006181d0",
      "DATA",
      [
        "storage",
        "00c71e88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061817c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00618/00618168.md#insn-0061817c) · [`0061818c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00618/00618168.md#insn-0061818c)
- 新版 [`006181bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00618/006181a8.md#insn-006181bc) · [`006181cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00618/006181a8.md#insn-006181cc)

~~~diff
- 0061817c ["INT_ADD", "register:40f0:8", ["const:61817c:8", "const:4:8"]]
- 0061817c ["CALL", null, ["callee:00c57f60:8"]]
+ 006181bc ["INT_ADD", "register:40f0:8", ["const:6181bc:8", "const:4:8"]]
+ 006181bc ["CALL", null, ["callee:00c57f60:8"]]
- 0061817c bytes 45ff1894
+ 006181bc bytes 69ff1894
- 0061818c ["COPY", "tmp:0:8", ["const:db8:8"]]
- 0061818c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061818c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061818c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006181cc ["COPY", "tmp:0:8", ["const:e88:8"]]
+ 006181cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006181cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006181cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061818c bytes 08e13691
+ 006181cc bytes 08213a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db8fde1683688f47d91c750ca23eae68"></a>

### [`006181a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00618/006181a8.md) → [`006181e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00618/006181e8.md) FUN_006181e8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006181ec",
      "incomplete_value": false,
      "site": "006181f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:e88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006181ac",
      "incomplete_value": false,
      "site": "006181b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:db8:8"
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
      "006181f0",
      "DATA",
      [
        "storage",
        "00c71db8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006181f0",
      "DATA",
      [
        "storage",
        "00c71e88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006181ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00618/006181a8.md#insn-006181ac)
- 新版 [`006181ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00618/006181e8.md#insn-006181ec)

~~~diff
- 006181ac ["COPY", "tmp:0:8", ["const:db8:8"]]
- 006181ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006181ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006181ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006181ec ["COPY", "tmp:0:8", ["const:e88:8"]]
+ 006181ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006181ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006181ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006181ac bytes 08e13691
+ 006181ec bytes 08213a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22bd94177edf6780d9f59941c6e42da4"></a>

### [`00618200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00618/00618200.md) → [`00618240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00618/00618240.md) FUN_00618240

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006181d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00618/006181d0.md) · 呼出先 31件 [`0043dba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dba4.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0043e828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e828.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00550c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550c28.md)
- 新版 呼出元 1件 [`00618210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00618/00618210.md) · 呼出先 31件 [`0043dbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043dbe4.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`0043e868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043e868.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00550c68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550c68.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.02% / 新版 94.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 19件, `call_target` 3件, `store_value` 8件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00618304",
      "incomplete_value": false,
      "site": "00618304",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006182c4",
      "incomplete_value": false,
      "site": "006182c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:e28:8"
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
      "definition_site": "006184d4",
      "incomplete_value": true,
      "site": "006184d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e83:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00618494",
      "incomplete_value": true,
      "site": "00618494",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:edf:8"
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
      "definition_site": "00618508",
      "incomplete_value": true,
      "site": "00618508",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8b4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006184c8",
      "incomplete_value": true,
      "site": "006184c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:910:8"
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
      "00618270",
      "READ",
      [
        "storage",
        "00c9ab68",
        null,
        "pointer"
      ]
    ],
    [
      "00618280",
      "READ",
      [
        "storage",
        "00ca4c78",
        null,
        "undefined4"
      ]
    ],
    [
      "00618280",
      "READ",
      [
        "storage",
        "00ca4c7c",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00618270",
      "READ",
      [
        "storage",
        "00c9ac38",
        null,
        "pointer"
      ]
    ],
    [
      "00618280",
      "READ",
      [
        "storage",
        "00ca4d78",
        null,
        "undefined4"
      ]
    ],
    [
      "00618280",
      "READ",
      [
        "storage",
        "00ca4d7c",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006183b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00618/00618200.md#insn-006183b4) · [`00618660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00618/00618200.md#insn-00618660) · [`0061881c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00618/00618200.md#insn-0061881c)
- 新版 [`006183f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00618/00618240.md#insn-006183f4) · [`006186a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00618/00618240.md#insn-006186a0) · [`0061885c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00618/00618240.md#insn-0061885c)

~~~diff
- 006183b4 ["INT_ADD", "register:40f0:8", ["const:6183b4:8", "const:4:8"]]
- 006183b4 ["CALL", null, ["ram:803a38:8"]]
+ 006183f4 ["INT_ADD", "register:40f0:8", ["const:6183f4:8", "const:4:8"]]
+ 006183f4 ["CALL", null, ["ram:803a90:8"]]
- 006183b4 bytes a1ad0794
+ 006183f4 bytes a7ad0794
- 00618660 ["COPY", "register:0:8", ["register:4040:8"]]
- 00618660 ["INT_ADD", "register:40f0:8", ["const:618660:8", "const:4:8"]]
- 00618660 ["CALLIND", null, ["register:0:8"]]
+ 006186a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 006186a0 ["INT_ADD", "register:40f0:8", ["const:6186a0:8", "const:4:8"]]
+ 006186a0 ["CALLIND", null, ["register:0:8"]]
- 00618660 bytes 00013fd6
+ 006186a0 bytes 00013fd6
- 0061881c ["INT_ADD", "register:40f0:8", ["const:61881c:8", "const:4:8"]]
- 0061881c ["CALL", null, ["ram:807c58:8"]]
+ 0061885c ["INT_ADD", "register:40f0:8", ["const:61885c:8", "const:4:8"]]
+ 0061885c ["CALL", null, ["ram:807cb0:8"]]
- 0061881c bytes 0fbd0794
+ 0061885c bytes 15bd0794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02014f3f421f537e74d910b76c7aa1bd"></a>

### [`0061a074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061a/0061a074.md) → [`0061a0b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061a/0061a0b4.md) FUN_0061a0b4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0061a0d4",
      "incomplete_value": false,
      "site": "0061a0d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061a094",
      "incomplete_value": false,
      "site": "0061a098",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:e28:8"
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
      "0061a0d8",
      "DATA",
      [
        "storage",
        "00c71e28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061a0d8",
      "DATA",
      [
        "storage",
        "00c71ef8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061a088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061a/0061a074.md#insn-0061a088) · [`0061a094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061a/0061a074.md#insn-0061a094)
- 新版 [`0061a0c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061a/0061a0b4.md#insn-0061a0c8) · [`0061a0d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061a/0061a0b4.md#insn-0061a0d4)

~~~diff
- 0061a088 ["INT_ADD", "register:40f0:8", ["const:61a088:8", "const:4:8"]]
- 0061a088 ["CALL", null, ["callee:00c57f60:8"]]
+ 0061a0c8 ["INT_ADD", "register:40f0:8", ["const:61a0c8:8", "const:4:8"]]
+ 0061a0c8 ["CALL", null, ["callee:00c57f60:8"]]
- 0061a088 bytes 82f71894
+ 0061a0c8 bytes a6f71894
- 0061a094 ["COPY", "tmp:0:8", ["const:e28:8"]]
- 0061a094 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061a094 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061a094 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061a0d4 ["COPY", "tmp:0:8", ["const:ef8:8"]]
+ 0061a0d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061a0d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061a0d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061a094 bytes 08a13891
+ 0061a0d4 bytes 08e13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d946b2ebabb62f4ecf05b4a2eb69640"></a>

### [`0061a0ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061a/0061a0ac.md) → [`0061a0ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061a/0061a0ec.md) FUN_0061a0ec

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0061a0f0",
      "incomplete_value": false,
      "site": "0061a0f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061a0b0",
      "incomplete_value": false,
      "site": "0061a0b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:e28:8"
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
      "0061a0f4",
      "DATA",
      [
        "storage",
        "00c71e28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061a0f4",
      "DATA",
      [
        "storage",
        "00c71ef8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061a0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061a/0061a0ac.md#insn-0061a0b0)
- 新版 [`0061a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061a/0061a0ec.md#insn-0061a0f0)

~~~diff
- 0061a0b0 ["COPY", "tmp:0:8", ["const:e28:8"]]
- 0061a0b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061a0b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061a0b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061a0f0 ["COPY", "tmp:0:8", ["const:ef8:8"]]
+ 0061a0f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061a0f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061a0f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061a0b0 bytes 08a13891
+ 0061a0f0 bytes 08e13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa16bac7893f7f0f3e1c2b543f274769"></a>

### [`0061a314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061a/0061a314.md) → [`0061a354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061a/0061a354.md) FUN_0061a354

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`0061a148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061a/0061a148.md) [`0061a314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061a/0061a314.md) [`0097c4a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097c/0097c4a8.md) · 呼出先 21件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)
- 新版 呼出元 3件 [`0061a188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061a/0061a188.md) [`0061a354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061a/0061a354.md) [`0097c4fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0097c/0097c4fc.md) · 呼出先 21件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`00441d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441d2c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.93% / 新版 98.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0061a580",
      "incomplete_value": false,
      "site": "0061a588",
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
      "definition_site": "0061a540",
      "incomplete_value": false,
      "site": "0061a548",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0061a598",
      "incomplete_value": false,
      "site": "0061a5a8",
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
      "definition_site": "0061a558",
      "incomplete_value": false,
      "site": "0061a568",
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
      "definition_site": "0061a64c",
      "incomplete_value": false,
      "site": "0061a65c",
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
      "definition_site": "0061a60c",
      "incomplete_value": false,
      "site": "0061a61c",
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
      "0061a4c8",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "0061a580",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ],
    [
      "0061a598",
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
      "0061a4c8",
      "PARAM",
      [
        "storage",
        "002b7f93",
        null,
        null
      ]
    ],
    [
      "0061a580",
      "PARAM",
      [
        "storage",
        "002b5e27",
        null,
        null
      ]
    ],
    [
      "0061a598",
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

- 旧版 [`0061a548`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061a/0061a314.md#insn-0061a548) · [`0061a568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061a/0061a314.md#insn-0061a568) · [`0061a61c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061a/0061a314.md#insn-0061a61c)
- 新版 [`0061a588`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061a/0061a354.md#insn-0061a588) · [`0061a5a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061a/0061a354.md#insn-0061a5a8) · [`0061a65c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061a/0061a354.md#insn-0061a65c)

~~~diff
- 0061a548 ["INT_ADD", "register:40f0:8", ["const:61a548:8", "const:4:8"]]
- 0061a548 ["CALL", null, ["callee:00441ed4:8"]]
+ 0061a588 ["INT_ADD", "register:40f0:8", ["const:61a588:8", "const:4:8"]]
+ 0061a588 ["CALL", null, ["callee:00441ed4:8"]]
- 0061a548 bytes 539ef897
+ 0061a588 bytes 539ef897
- 0061a568 ["INT_ADD", "register:40f0:8", ["const:61a568:8", "const:4:8"]]
- 0061a568 ["CALL", null, ["callee:00442834:8"]]
+ 0061a5a8 ["INT_ADD", "register:40f0:8", ["const:61a5a8:8", "const:4:8"]]
+ 0061a5a8 ["CALL", null, ["callee:00442834:8"]]
- 0061a568 bytes a3a0f897
+ 0061a5a8 bytes a3a0f897
- 0061a61c ["INT_ADD", "register:40f0:8", ["const:61a61c:8", "const:4:8"]]
- 0061a61c ["CALL", null, ["callee:00442834:8"]]
+ 0061a65c ["INT_ADD", "register:40f0:8", ["const:61a65c:8", "const:4:8"]]
+ 0061a65c ["CALL", null, ["callee:00442834:8"]]
- 0061a61c bytes 76a0f897
+ 0061a65c bytes 76a0f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c968dcb8d76b93439f70cd7f7c65b678"></a>

### [`0061aef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061a/0061aef8.md) → [`0061af38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061a/0061af38.md) FUN_0061af38

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`0061a314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061a/0061a314.md) [`0061aef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061a/0061aef8.md) [`0072c380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072c/0072c380.md) [`007f0dd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f0/007f0dd4.md) · 呼出先 22件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`004412b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/004412b8.md)
- 新版 呼出元 4件 [`0061a354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061a/0061a354.md) [`0061af38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061a/0061af38.md) [`0072c3d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0072c/0072c3d8.md) [`007f0e2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f0/007f0e2c.md) · 呼出先 22件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`004412f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004412f8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.82% / 新版 98.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0061b094",
      "incomplete_value": false,
      "site": "0061b09c",
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
      "definition_site": "0061b054",
      "incomplete_value": false,
      "site": "0061b05c",
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
      "definition_site": "0061b0b8",
      "incomplete_value": false,
      "site": "0061b0c4",
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
      "definition_site": "0061b078",
      "incomplete_value": false,
      "site": "0061b084",
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
      "definition_site": "0061b204",
      "incomplete_value": false,
      "site": "0061b210",
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
      "definition_site": "0061b1c4",
      "incomplete_value": false,
      "site": "0061b1d0",
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
      "0061b094",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "0061b0b8",
      "PARAM",
      [
        "storage",
        "002c0ee9",
        null,
        "string"
      ]
    ],
    [
      "0061b1ec",
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
      "0061b094",
      "PARAM",
      [
        "storage",
        "002b7f93",
        null,
        null
      ]
    ],
    [
      "0061b0b8",
      "PARAM",
      [
        "storage",
        "002c0f29",
        null,
        "string"
      ]
    ],
    [
      "0061b1ec",
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

- 旧版 [`0061b05c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061a/0061aef8.md#insn-0061b05c) · [`0061b084`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061a/0061aef8.md#insn-0061b084) · [`0061b1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061a/0061aef8.md#insn-0061b1d0)
- 新版 [`0061b09c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061a/0061af38.md#insn-0061b09c) · [`0061b0c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061a/0061af38.md#insn-0061b0c4) · [`0061b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061a/0061af38.md#insn-0061b210)

~~~diff
- 0061b05c ["INT_ADD", "register:40f0:8", ["const:61b05c:8", "const:4:8"]]
- 0061b05c ["CALL", null, ["callee:00441ed4:8"]]
+ 0061b09c ["INT_ADD", "register:40f0:8", ["const:61b09c:8", "const:4:8"]]
+ 0061b09c ["CALL", null, ["callee:00441ed4:8"]]
- 0061b05c bytes 8e9bf897
+ 0061b09c bytes 8e9bf897
- 0061b084 ["INT_ADD", "register:40f0:8", ["const:61b084:8", "const:4:8"]]
- 0061b084 ["CALL", null, ["callee:00442834:8"]]
+ 0061b0c4 ["INT_ADD", "register:40f0:8", ["const:61b0c4:8", "const:4:8"]]
+ 0061b0c4 ["CALL", null, ["callee:00442834:8"]]
- 0061b084 bytes dc9df897
+ 0061b0c4 bytes dc9df897
- 0061b1d0 ["INT_ADD", "register:40f0:8", ["const:61b1d0:8", "const:4:8"]]
- 0061b1d0 ["CALL", null, ["callee:00442834:8"]]
+ 0061b210 ["INT_ADD", "register:40f0:8", ["const:61b210:8", "const:4:8"]]
+ 0061b210 ["CALL", null, ["callee:00442834:8"]]
- 0061b1d0 bytes 899df897
+ 0061b210 bytes 899df897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b17ae4ef6264dbba5abbe21e12d7683"></a>

### [`0061bbd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061b/0061bbd0.md) → [`0061bc10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061b/0061bc10.md) FUN_0061bc10

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`0061b99c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061b/0061b99c.md) [`0061bbd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061b/0061bbd0.md) [`00b31b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b31/00b31b58.md) · 呼出先 21件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)
- 新版 呼出元 3件 [`0061b9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061b/0061b9dc.md) [`0061bc10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061b/0061bc10.md) [`00b31bf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b31/00b31bf4.md) · 呼出先 21件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`00441d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441d2c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.05% / 新版 99.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0061bd84",
      "incomplete_value": false,
      "site": "0061bd8c",
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
      "definition_site": "0061bd44",
      "incomplete_value": false,
      "site": "0061bd4c",
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
      "definition_site": "0061be38",
      "incomplete_value": false,
      "site": "0061be40",
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
      "definition_site": "0061bdf8",
      "incomplete_value": false,
      "site": "0061be00",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0061be50",
      "incomplete_value": false,
      "site": "0061be60",
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
      "definition_site": "0061be10",
      "incomplete_value": false,
      "site": "0061be20",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0061bd84",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "0061be38",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ],
    [
      "0061be50",
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
      "0061bd84",
      "PARAM",
      [
        "storage",
        "002b7f93",
        null,
        null
      ]
    ],
    [
      "0061be38",
      "PARAM",
      [
        "storage",
        "002b5e27",
        null,
        null
      ]
    ],
    [
      "0061be50",
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

- 旧版 [`0061bd4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061b/0061bbd0.md#insn-0061bd4c) · [`0061be00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061b/0061bbd0.md#insn-0061be00) · [`0061be20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061b/0061bbd0.md#insn-0061be20)
- 新版 [`0061bd8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061b/0061bc10.md#insn-0061bd8c) · [`0061be40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061b/0061bc10.md#insn-0061be40) · [`0061be60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061b/0061bc10.md#insn-0061be60)

~~~diff
- 0061bd4c ["INT_ADD", "register:40f0:8", ["const:61bd4c:8", "const:4:8"]]
- 0061bd4c ["CALL", null, ["callee:00441ed4:8"]]
+ 0061bd8c ["INT_ADD", "register:40f0:8", ["const:61bd8c:8", "const:4:8"]]
+ 0061bd8c ["CALL", null, ["callee:00441ed4:8"]]
- 0061bd4c bytes 5298f897
+ 0061bd8c bytes 5298f897
- 0061be00 ["INT_ADD", "register:40f0:8", ["const:61be00:8", "const:4:8"]]
- 0061be00 ["CALL", null, ["callee:00441ed4:8"]]
+ 0061be40 ["INT_ADD", "register:40f0:8", ["const:61be40:8", "const:4:8"]]
+ 0061be40 ["CALL", null, ["callee:00441ed4:8"]]
- 0061be00 bytes 2598f897
+ 0061be40 bytes 2598f897
- 0061be20 ["INT_ADD", "register:40f0:8", ["const:61be20:8", "const:4:8"]]
- 0061be20 ["CALL", null, ["callee:00442834:8"]]
+ 0061be60 ["INT_ADD", "register:40f0:8", ["const:61be60:8", "const:4:8"]]
+ 0061be60 ["CALL", null, ["callee:00442834:8"]]
- 0061be20 bytes 759af897
+ 0061be60 bytes 759af897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcfdc8349abee52dda01bc46a0caf02c"></a>

### [`0061c9dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061c/0061c9dc.md) → [`0061ca1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061c/0061ca1c.md) FUN_0061ca1c

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
      "definition_site": "0061ca30",
      "incomplete_value": false,
      "site": "0061ca34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:f98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061c9f0",
      "incomplete_value": false,
      "site": "0061c9f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:ec8:8"
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
      "0061ca34",
      "DATA",
      [
        "storage",
        "00c71ec8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061ca34",
      "DATA",
      [
        "storage",
        "00c71f98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061c9e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061c/0061c9dc.md#insn-0061c9e8) · [`0061c9f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061c/0061c9dc.md#insn-0061c9f0)
- 新版 [`0061ca28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061c/0061ca1c.md#insn-0061ca28) · [`0061ca30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061c/0061ca1c.md#insn-0061ca30)

~~~diff
- 0061c9e8 ["INT_ADD", "register:40f0:8", ["const:61c9e8:8", "const:4:8"]]
- 0061c9e8 ["CALL", null, ["callee:00c57f60:8"]]
+ 0061ca28 ["INT_ADD", "register:40f0:8", ["const:61ca28:8", "const:4:8"]]
+ 0061ca28 ["CALL", null, ["callee:00c57f60:8"]]
- 0061c9e8 bytes 2aed1894
+ 0061ca28 bytes 4eed1894
- 0061c9f0 ["COPY", "tmp:0:8", ["const:ec8:8"]]
- 0061c9f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061c9f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061c9f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061ca30 ["COPY", "tmp:0:8", ["const:f98:8"]]
+ 0061ca30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061ca30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061ca30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061c9f0 bytes 08213b91
+ 0061ca30 bytes 08613e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a8b9bf05c0a7aa78f76df6186352760"></a>

### [`0061ca00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061c/0061ca00.md) → [`0061ca40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061c/0061ca40.md) FUN_0061ca40

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
      "definition_site": "0061ca44",
      "incomplete_value": false,
      "site": "0061ca48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:f98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061ca04",
      "incomplete_value": false,
      "site": "0061ca08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:ec8:8"
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
      "0061ca48",
      "DATA",
      [
        "storage",
        "00c71ec8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061ca48",
      "DATA",
      [
        "storage",
        "00c71f98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061ca04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061c/0061ca00.md#insn-0061ca04)
- 新版 [`0061ca44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061c/0061ca40.md#insn-0061ca44)

~~~diff
- 0061ca04 ["COPY", "tmp:0:8", ["const:ec8:8"]]
- 0061ca04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061ca04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061ca04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061ca44 ["COPY", "tmp:0:8", ["const:f98:8"]]
+ 0061ca44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061ca44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061ca44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061ca04 bytes 08213b91
+ 0061ca44 bytes 08613e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56be3f74dbdd5b55e6aeecc6ef3c122f"></a>

### [`0061ca18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061c/0061ca18.md) → [`0061ca58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061c/0061ca58.md) FUN_0061ca58

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

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
      "site": "0061ca7c",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0061ca3c",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "0061ca7c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "0061ca7c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061ca3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061c/0061ca18.md#insn-0061ca3c) · [`0061ca48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061c/0061ca18.md#insn-0061ca48)
- 新版 [`0061ca7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061c/0061ca58.md#insn-0061ca7c) · [`0061ca88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061c/0061ca58.md#insn-0061ca88)

~~~diff
- 0061ca3c ["INT_ADD", "register:40f0:8", ["const:61ca3c:8", "const:4:8"]]
- 0061ca3c ["CALL", null, ["ram:47acf4:8"]]
+ 0061ca7c ["INT_ADD", "register:40f0:8", ["const:61ca7c:8", "const:4:8"]]
+ 0061ca7c ["CALL", null, ["ram:47ad34:8"]]
- 0061ca3c bytes ae78f997
+ 0061ca7c bytes ae78f997
- 0061ca48 ["INT_ADD", "register:40f0:8", ["const:61ca48:8", "const:4:8"]]
- 0061ca48 ["CALL", null, ["callee:0047ce14:8"]]
+ 0061ca88 ["INT_ADD", "register:40f0:8", ["const:61ca88:8", "const:4:8"]]
+ 0061ca88 ["CALL", null, ["callee:0047ce14:8"]]
- 0061ca48 bytes e380f997
+ 0061ca88 bytes e380f997
~~~


<a id="compare-f8e25b534bd888b93293154cce4226ca"></a>

### [`0061cac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061c/0061cac0.md) → [`0061cb00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061c/0061cb00.md) FUN_0061cb00

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
      "definition_site": "0061cb0c",
      "incomplete_value": false,
      "site": "0061cb0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061cacc",
      "incomplete_value": false,
      "site": "0061cacc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c71000:8"
          ],
          [
            "leaf",
            "const:f48:8"
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
      "0061cb0c",
      "DATA",
      [
        "storage",
        "00c71f48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061cb0c",
      "DATA",
      [
        "storage",
        "00c72018",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061cac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061c/0061cac0.md#insn-0061cac4) · [`0061cac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061c/0061cac0.md#insn-0061cac8)
- 新版 [`0061cb04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061c/0061cb00.md#insn-0061cb04) · [`0061cb08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061c/0061cb00.md#insn-0061cb08)

~~~diff
- 0061cac4 ["COPY", "register:4048:8", ["const:c71000:8"]]
+ 0061cb04 ["COPY", "register:4048:8", ["const:c72000:8"]]
- 0061cac4 bytes a93200b0
+ 0061cb04 bytes a93200d0
- 0061cac8 ["COPY", "tmp:0:8", ["const:f48:8"]]
- 0061cac8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0061cac8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0061cac8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0061cb08 ["COPY", "tmp:0:8", ["const:18:8"]]
+ 0061cb08 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0061cb08 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0061cb08 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0061cac8 bytes 29213d91
+ 0061cb08 bytes 29610091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ddad2638187a8e015f0bd0a762185322"></a>

### [`0061cb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061c/0061cb20.md) → [`0061cb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061c/0061cb60.md) FUN_0061cb60

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0061cb74",
      "incomplete_value": true,
      "site": "0061cb78",
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
            "const:a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061cb34",
      "incomplete_value": true,
      "site": "0061cb38",
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
            "const:fd8:8"
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
      "0061cb78",
      "DATA",
      [
        "storage",
        "00c71fd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061cb78",
      "DATA",
      [
        "storage",
        "00c720a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061cb2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061c/0061cb20.md#insn-0061cb2c) · [`0061cb30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061c/0061cb20.md#insn-0061cb30) · [`0061cb34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061c/0061cb20.md#insn-0061cb34)
- 新版 [`0061cb6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061c/0061cb60.md#insn-0061cb6c) · [`0061cb70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061c/0061cb60.md#insn-0061cb70) · [`0061cb74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061c/0061cb60.md#insn-0061cb74)

~~~diff
- 0061cb2c ["INT_ADD", "register:40f0:8", ["const:61cb2c:8", "const:4:8"]]
- 0061cb2c ["CALL", null, ["callee:00c57f60:8"]]
+ 0061cb6c ["INT_ADD", "register:40f0:8", ["const:61cb6c:8", "const:4:8"]]
+ 0061cb6c ["CALL", null, ["callee:00c57f60:8"]]
- 0061cb2c bytes d9ec1894
+ 0061cb6c bytes fdec1894
- 0061cb30 ["COPY", "register:4040:8", ["const:c71000:8"]]
+ 0061cb70 ["COPY", "register:4040:8", ["const:c72000:8"]]
- 0061cb30 bytes a83200b0
+ 0061cb70 bytes a83200d0
- 0061cb34 ["COPY", "tmp:0:8", ["const:fd8:8"]]
- 0061cb34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061cb34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061cb34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061cb74 ["COPY", "tmp:0:8", ["const:a8:8"]]
+ 0061cb74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061cb74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061cb74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061cb34 bytes 08613f91
+ 0061cb74 bytes 08a10291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8588ea5f7855d038bb64f19cd8e52557"></a>

### [`0061cb44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061c/0061cb44.md) → [`0061cb84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061c/0061cb84.md) FUN_0061cb84

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0061cb88",
      "incomplete_value": true,
      "site": "0061cb8c",
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
            "const:a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061cb48",
      "incomplete_value": true,
      "site": "0061cb4c",
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
            "const:fd8:8"
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
      "0061cb8c",
      "DATA",
      [
        "storage",
        "00c71fd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061cb8c",
      "DATA",
      [
        "storage",
        "00c720a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061cb44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061c/0061cb44.md#insn-0061cb44) · [`0061cb48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061c/0061cb44.md#insn-0061cb48)
- 新版 [`0061cb84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061c/0061cb84.md#insn-0061cb84) · [`0061cb88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061c/0061cb84.md#insn-0061cb88)

~~~diff
- 0061cb44 ["COPY", "register:4040:8", ["const:c71000:8"]]
+ 0061cb84 ["COPY", "register:4040:8", ["const:c72000:8"]]
- 0061cb44 bytes a83200b0
+ 0061cb84 bytes a83200d0
- 0061cb48 ["COPY", "tmp:0:8", ["const:fd8:8"]]
- 0061cb48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061cb48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061cb48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061cb88 ["COPY", "tmp:0:8", ["const:a8:8"]]
+ 0061cb88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061cb88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061cb88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061cb48 bytes 08613f91
+ 0061cb88 bytes 08a10291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb4bf93af04589ae62922a13cb85165c"></a>

### [`0061cb5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061c/0061cb5c.md) → [`0061cb9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061c/0061cb9c.md) FUN_0061cb9c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.68% / 新版 98.68%

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
      "site": "0061cbc4",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0061cb84",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "0061cbc4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "0061cbc4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061cb84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061c/0061cb5c.md#insn-0061cb84) · [`0061cb90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061c/0061cb5c.md#insn-0061cb90) · [`0061cba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061c/0061cb5c.md#insn-0061cba8)
- 新版 [`0061cbc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061c/0061cb9c.md#insn-0061cbc4) · [`0061cbd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061c/0061cb9c.md#insn-0061cbd0) · [`0061cbe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061c/0061cb9c.md#insn-0061cbe8)

~~~diff
- 0061cb84 ["INT_ADD", "register:40f0:8", ["const:61cb84:8", "const:4:8"]]
- 0061cb84 ["CALL", null, ["ram:47acf4:8"]]
+ 0061cbc4 ["INT_ADD", "register:40f0:8", ["const:61cbc4:8", "const:4:8"]]
+ 0061cbc4 ["CALL", null, ["ram:47ad34:8"]]
- 0061cb84 bytes 5c78f997
+ 0061cbc4 bytes 5c78f997
- 0061cb90 ["INT_ADD", "register:40f0:8", ["const:61cb90:8", "const:4:8"]]
- 0061cb90 ["CALL", null, ["callee:0047ce14:8"]]
+ 0061cbd0 ["INT_ADD", "register:40f0:8", ["const:61cbd0:8", "const:4:8"]]
+ 0061cbd0 ["CALL", null, ["callee:0047ce14:8"]]
- 0061cb90 bytes 9180f997
+ 0061cbd0 bytes 9180f997
- 0061cba8 ["INT_ADD", "register:40f0:8", ["const:61cba8:8", "const:4:8"]]
- 0061cba8 ["CALL", null, ["callee:00851550:8"]]
+ 0061cbe8 ["INT_ADD", "register:40f0:8", ["const:61cbe8:8", "const:4:8"]]
+ 0061cbe8 ["CALL", null, ["callee:00851550:8"]]
- 0061cba8 bytes 54d20894
+ 0061cbe8 bytes 5ad20894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed0d6ff809cd596beb35cbf0c56266d2"></a>

### [`0061ccb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061c/0061ccb8.md) → [`0061ccf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061c/0061ccf8.md) FUN_0061ccf8

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
      "definition_site": "0061cd0c",
      "incomplete_value": false,
      "site": "0061cd10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:128:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061cccc",
      "incomplete_value": false,
      "site": "0061ccd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:58:8"
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
      "0061cd10",
      "DATA",
      [
        "storage",
        "00c72058",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061cd10",
      "DATA",
      [
        "storage",
        "00c72128",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061ccc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061c/0061ccb8.md#insn-0061ccc4) · [`0061cccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061c/0061ccb8.md#insn-0061cccc)
- 新版 [`0061cd04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061c/0061ccf8.md#insn-0061cd04) · [`0061cd0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061c/0061ccf8.md#insn-0061cd0c)

~~~diff
- 0061ccc4 ["INT_ADD", "register:40f0:8", ["const:61ccc4:8", "const:4:8"]]
- 0061ccc4 ["CALL", null, ["callee:00c57f60:8"]]
+ 0061cd04 ["INT_ADD", "register:40f0:8", ["const:61cd04:8", "const:4:8"]]
+ 0061cd04 ["CALL", null, ["callee:00c57f60:8"]]
- 0061ccc4 bytes 73ec1894
+ 0061cd04 bytes 97ec1894
- 0061cccc ["COPY", "tmp:0:8", ["const:58:8"]]
- 0061cccc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061cccc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061cccc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061cd0c ["COPY", "tmp:0:8", ["const:128:8"]]
+ 0061cd0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061cd0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061cd0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061cccc bytes 08610191
+ 0061cd0c bytes 08a10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49bbeec5cb72322e27311fba0ba7632e"></a>

### [`0061ccdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061c/0061ccdc.md) → [`0061cd1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061c/0061cd1c.md) FUN_0061cd1c

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
      "definition_site": "0061cd20",
      "incomplete_value": false,
      "site": "0061cd24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:128:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061cce0",
      "incomplete_value": false,
      "site": "0061cce4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:58:8"
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
      "0061cd24",
      "DATA",
      [
        "storage",
        "00c72058",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061cd24",
      "DATA",
      [
        "storage",
        "00c72128",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061cce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061c/0061ccdc.md#insn-0061cce0)
- 新版 [`0061cd20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061c/0061cd1c.md#insn-0061cd20)

~~~diff
- 0061cce0 ["COPY", "tmp:0:8", ["const:58:8"]]
- 0061cce0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061cce0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061cce0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061cd20 ["COPY", "tmp:0:8", ["const:128:8"]]
+ 0061cd20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061cd20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061cd20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061cce0 bytes 08610191
+ 0061cd20 bytes 08a10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9b56738e6720165403d454fc771af7f"></a>

### [`0061ccf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061c/0061ccf4.md) → [`0061cd34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061c/0061cd34.md) FUN_0061cd34

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.68% / 新版 98.68%

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
      "site": "0061cd5c",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0061cd1c",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "0061cd5c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "0061cd5c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061cd1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061c/0061ccf4.md#insn-0061cd1c) · [`0061cd28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061c/0061ccf4.md#insn-0061cd28) · [`0061cd40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061c/0061ccf4.md#insn-0061cd40)
- 新版 [`0061cd5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061c/0061cd34.md#insn-0061cd5c) · [`0061cd68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061c/0061cd34.md#insn-0061cd68) · [`0061cd80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061c/0061cd34.md#insn-0061cd80)

~~~diff
- 0061cd1c ["INT_ADD", "register:40f0:8", ["const:61cd1c:8", "const:4:8"]]
- 0061cd1c ["CALL", null, ["ram:47acf4:8"]]
+ 0061cd5c ["INT_ADD", "register:40f0:8", ["const:61cd5c:8", "const:4:8"]]
+ 0061cd5c ["CALL", null, ["ram:47ad34:8"]]
- 0061cd1c bytes f677f997
+ 0061cd5c bytes f677f997
- 0061cd28 ["INT_ADD", "register:40f0:8", ["const:61cd28:8", "const:4:8"]]
- 0061cd28 ["CALL", null, ["callee:0047ce14:8"]]
+ 0061cd68 ["INT_ADD", "register:40f0:8", ["const:61cd68:8", "const:4:8"]]
+ 0061cd68 ["CALL", null, ["callee:0047ce14:8"]]
- 0061cd28 bytes 2b80f997
+ 0061cd68 bytes 2b80f997
- 0061cd40 ["INT_ADD", "register:40f0:8", ["const:61cd40:8", "const:4:8"]]
- 0061cd40 ["CALL", null, ["callee:00851550:8"]]
+ 0061cd80 ["INT_ADD", "register:40f0:8", ["const:61cd80:8", "const:4:8"]]
+ 0061cd80 ["CALL", null, ["callee:00851550:8"]]
- 0061cd40 bytes eed10894
+ 0061cd80 bytes f4d10894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6db980a3e8ea4511cab003dcc407ca42"></a>

### [`0061ce50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061c/0061ce50.md) → [`0061ce90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061c/0061ce90.md) FUN_0061ce90

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
      "definition_site": "0061cea4",
      "incomplete_value": false,
      "site": "0061cea8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:1a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061ce64",
      "incomplete_value": false,
      "site": "0061ce68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:d8:8"
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
      "0061cea8",
      "DATA",
      [
        "storage",
        "00c720d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061cea8",
      "DATA",
      [
        "storage",
        "00c721a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061ce5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061c/0061ce50.md#insn-0061ce5c) · [`0061ce64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061c/0061ce50.md#insn-0061ce64)
- 新版 [`0061ce9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061c/0061ce90.md#insn-0061ce9c) · [`0061cea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061c/0061ce90.md#insn-0061cea4)

~~~diff
- 0061ce5c ["INT_ADD", "register:40f0:8", ["const:61ce5c:8", "const:4:8"]]
- 0061ce5c ["CALL", null, ["callee:00c57f60:8"]]
+ 0061ce9c ["INT_ADD", "register:40f0:8", ["const:61ce9c:8", "const:4:8"]]
+ 0061ce9c ["CALL", null, ["callee:00c57f60:8"]]
- 0061ce5c bytes 0dec1894
+ 0061ce9c bytes 31ec1894
- 0061ce64 ["COPY", "tmp:0:8", ["const:d8:8"]]
- 0061ce64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061ce64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061ce64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061cea4 ["COPY", "tmp:0:8", ["const:1a8:8"]]
+ 0061cea4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061cea4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061cea4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061ce64 bytes 08610391
+ 0061cea4 bytes 08a10691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c867ed9e44cf7bfcb513e57327577e0"></a>

### [`0061ce74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061c/0061ce74.md) → [`0061ceb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061c/0061ceb4.md) FUN_0061ceb4

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
      "definition_site": "0061ceb8",
      "incomplete_value": false,
      "site": "0061cebc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:1a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061ce78",
      "incomplete_value": false,
      "site": "0061ce7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:d8:8"
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
      "0061cebc",
      "DATA",
      [
        "storage",
        "00c720d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061cebc",
      "DATA",
      [
        "storage",
        "00c721a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061ce78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061c/0061ce74.md#insn-0061ce78)
- 新版 [`0061ceb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061c/0061ceb4.md#insn-0061ceb8)

~~~diff
- 0061ce78 ["COPY", "tmp:0:8", ["const:d8:8"]]
- 0061ce78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061ce78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061ce78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061ceb8 ["COPY", "tmp:0:8", ["const:1a8:8"]]
+ 0061ceb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061ceb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061ceb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061ce78 bytes 08610391
+ 0061ceb8 bytes 08a10691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-011bde1b62a07422463eda2a455712ed"></a>

### [`0061ce8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061c/0061ce8c.md) → [`0061cecc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061c/0061cecc.md) FUN_0061cecc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.68% / 新版 98.68%

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
      "site": "0061cef4",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0061ceb4",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "0061cef4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "0061cef4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061ceb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061c/0061ce8c.md#insn-0061ceb4) · [`0061cec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061c/0061ce8c.md#insn-0061cec0) · [`0061ced8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061c/0061ce8c.md#insn-0061ced8)
- 新版 [`0061cef4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061c/0061cecc.md#insn-0061cef4) · [`0061cf00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061c/0061cecc.md#insn-0061cf00) · [`0061cf18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061c/0061cecc.md#insn-0061cf18)

~~~diff
- 0061ceb4 ["INT_ADD", "register:40f0:8", ["const:61ceb4:8", "const:4:8"]]
- 0061ceb4 ["CALL", null, ["ram:47acf4:8"]]
+ 0061cef4 ["INT_ADD", "register:40f0:8", ["const:61cef4:8", "const:4:8"]]
+ 0061cef4 ["CALL", null, ["ram:47ad34:8"]]
- 0061ceb4 bytes 9077f997
+ 0061cef4 bytes 9077f997
- 0061cec0 ["INT_ADD", "register:40f0:8", ["const:61cec0:8", "const:4:8"]]
- 0061cec0 ["CALL", null, ["callee:0047ce14:8"]]
+ 0061cf00 ["INT_ADD", "register:40f0:8", ["const:61cf00:8", "const:4:8"]]
+ 0061cf00 ["CALL", null, ["callee:0047ce14:8"]]
- 0061cec0 bytes c57ff997
+ 0061cf00 bytes c57ff997
- 0061ced8 ["INT_ADD", "register:40f0:8", ["const:61ced8:8", "const:4:8"]]
- 0061ced8 ["CALL", null, ["callee:00851550:8"]]
+ 0061cf18 ["INT_ADD", "register:40f0:8", ["const:61cf18:8", "const:4:8"]]
+ 0061cf18 ["CALL", null, ["callee:00851550:8"]]
- 0061ced8 bytes 88d10894
+ 0061cf18 bytes 8ed10894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3646259b1e3dd5ca708e69aca76800e"></a>

### [`0061d024`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d024.md) → [`0061d064`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061d064.md) FUN_0061d064

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.68% / 新版 98.68%

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
      "site": "0061d08c",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0061d04c",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "0061d08c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "0061d08c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061d04c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d024.md#insn-0061d04c) · [`0061d058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d024.md#insn-0061d058) · [`0061d070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d024.md#insn-0061d070)
- 新版 [`0061d08c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061d064.md#insn-0061d08c) · [`0061d098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061d064.md#insn-0061d098) · [`0061d0b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061d064.md#insn-0061d0b0)

~~~diff
- 0061d04c ["INT_ADD", "register:40f0:8", ["const:61d04c:8", "const:4:8"]]
- 0061d04c ["CALL", null, ["ram:47acf4:8"]]
+ 0061d08c ["INT_ADD", "register:40f0:8", ["const:61d08c:8", "const:4:8"]]
+ 0061d08c ["CALL", null, ["ram:47ad34:8"]]
- 0061d04c bytes 2a77f997
+ 0061d08c bytes 2a77f997
- 0061d058 ["INT_ADD", "register:40f0:8", ["const:61d058:8", "const:4:8"]]
- 0061d058 ["CALL", null, ["callee:0047ce14:8"]]
+ 0061d098 ["INT_ADD", "register:40f0:8", ["const:61d098:8", "const:4:8"]]
+ 0061d098 ["CALL", null, ["callee:0047ce14:8"]]
- 0061d058 bytes 5f7ff997
+ 0061d098 bytes 5f7ff997
- 0061d070 ["INT_ADD", "register:40f0:8", ["const:61d070:8", "const:4:8"]]
- 0061d070 ["CALL", null, ["callee:00851550:8"]]
+ 0061d0b0 ["INT_ADD", "register:40f0:8", ["const:61d0b0:8", "const:4:8"]]
+ 0061d0b0 ["CALL", null, ["callee:00851550:8"]]
- 0061d070 bytes 22d10894
+ 0061d0b0 bytes 28d10894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a5243abeac9390cf32600e080cbb725"></a>

### [`0061d180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d180.md) → [`0061d1c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061d1c0.md) FUN_0061d1c0

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
      "definition_site": "0061d1d4",
      "incomplete_value": false,
      "site": "0061d1d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:2a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061d194",
      "incomplete_value": false,
      "site": "0061d198",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:1d8:8"
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
      "0061d1d8",
      "DATA",
      [
        "storage",
        "00c721d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061d1d8",
      "DATA",
      [
        "storage",
        "00c722a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061d18c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d180.md#insn-0061d18c) · [`0061d194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d180.md#insn-0061d194)
- 新版 [`0061d1cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061d1c0.md#insn-0061d1cc) · [`0061d1d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061d1c0.md#insn-0061d1d4)

~~~diff
- 0061d18c ["INT_ADD", "register:40f0:8", ["const:61d18c:8", "const:4:8"]]
- 0061d18c ["CALL", null, ["callee:00c57f60:8"]]
+ 0061d1cc ["INT_ADD", "register:40f0:8", ["const:61d1cc:8", "const:4:8"]]
+ 0061d1cc ["CALL", null, ["callee:00c57f60:8"]]
- 0061d18c bytes 41eb1894
+ 0061d1cc bytes 65eb1894
- 0061d194 ["COPY", "tmp:0:8", ["const:1d8:8"]]
- 0061d194 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061d194 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061d194 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061d1d4 ["COPY", "tmp:0:8", ["const:2a8:8"]]
+ 0061d1d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061d1d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061d1d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061d194 bytes 08610791
+ 0061d1d4 bytes 08a10a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-236c164cbbc5bb7b9f1ace026e34004c"></a>

### [`0061d1a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d1a4.md) → [`0061d1e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061d1e4.md) FUN_0061d1e4

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
      "definition_site": "0061d1e8",
      "incomplete_value": false,
      "site": "0061d1ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:2a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061d1a8",
      "incomplete_value": false,
      "site": "0061d1ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:1d8:8"
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
      "0061d1ec",
      "DATA",
      [
        "storage",
        "00c721d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061d1ec",
      "DATA",
      [
        "storage",
        "00c722a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061d1a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d1a4.md#insn-0061d1a8)
- 新版 [`0061d1e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061d1e4.md#insn-0061d1e8)

~~~diff
- 0061d1a8 ["COPY", "tmp:0:8", ["const:1d8:8"]]
- 0061d1a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061d1a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061d1a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061d1e8 ["COPY", "tmp:0:8", ["const:2a8:8"]]
+ 0061d1e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061d1e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061d1e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061d1a8 bytes 08610791
+ 0061d1e8 bytes 08a10a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3dd4e215e26184ada6eba395b575cc5"></a>

### [`0061d1bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d1bc.md) → [`0061d1fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061d1fc.md) FUN_0061d1fc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.68% / 新版 98.68%

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
      "site": "0061d224",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0061d1e4",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "0061d224",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "0061d224",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061d1e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d1bc.md#insn-0061d1e4) · [`0061d1f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d1bc.md#insn-0061d1f0) · [`0061d208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d1bc.md#insn-0061d208)
- 新版 [`0061d224`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061d1fc.md#insn-0061d224) · [`0061d230`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061d1fc.md#insn-0061d230) · [`0061d248`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061d1fc.md#insn-0061d248)

~~~diff
- 0061d1e4 ["INT_ADD", "register:40f0:8", ["const:61d1e4:8", "const:4:8"]]
- 0061d1e4 ["CALL", null, ["ram:47acf4:8"]]
+ 0061d224 ["INT_ADD", "register:40f0:8", ["const:61d224:8", "const:4:8"]]
+ 0061d224 ["CALL", null, ["ram:47ad34:8"]]
- 0061d1e4 bytes c476f997
+ 0061d224 bytes c476f997
- 0061d1f0 ["INT_ADD", "register:40f0:8", ["const:61d1f0:8", "const:4:8"]]
- 0061d1f0 ["CALL", null, ["callee:0047ce14:8"]]
+ 0061d230 ["INT_ADD", "register:40f0:8", ["const:61d230:8", "const:4:8"]]
+ 0061d230 ["CALL", null, ["callee:0047ce14:8"]]
- 0061d1f0 bytes f97ef997
+ 0061d230 bytes f97ef997
- 0061d208 ["INT_ADD", "register:40f0:8", ["const:61d208:8", "const:4:8"]]
- 0061d208 ["CALL", null, ["callee:00851550:8"]]
+ 0061d248 ["INT_ADD", "register:40f0:8", ["const:61d248:8", "const:4:8"]]
+ 0061d248 ["CALL", null, ["callee:00851550:8"]]
- 0061d208 bytes bcd00894
+ 0061d248 bytes c2d00894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10bbaf732f8114d04bbada4f74b0b90b"></a>

### [`0061d318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d318.md) → [`0061d358`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061d358.md) FUN_0061d358

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
      "definition_site": "0061d36c",
      "incomplete_value": false,
      "site": "0061d370",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:328:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061d32c",
      "incomplete_value": false,
      "site": "0061d330",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:258:8"
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
      "0061d370",
      "DATA",
      [
        "storage",
        "00c72258",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061d370",
      "DATA",
      [
        "storage",
        "00c72328",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061d324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d318.md#insn-0061d324) · [`0061d32c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d318.md#insn-0061d32c)
- 新版 [`0061d364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061d358.md#insn-0061d364) · [`0061d36c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061d358.md#insn-0061d36c)

~~~diff
- 0061d324 ["INT_ADD", "register:40f0:8", ["const:61d324:8", "const:4:8"]]
- 0061d324 ["CALL", null, ["callee:00c57f60:8"]]
+ 0061d364 ["INT_ADD", "register:40f0:8", ["const:61d364:8", "const:4:8"]]
+ 0061d364 ["CALL", null, ["callee:00c57f60:8"]]
- 0061d324 bytes dbea1894
+ 0061d364 bytes ffea1894
- 0061d32c ["COPY", "tmp:0:8", ["const:258:8"]]
- 0061d32c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061d32c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061d32c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061d36c ["COPY", "tmp:0:8", ["const:328:8"]]
+ 0061d36c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061d36c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061d36c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061d32c bytes 08610991
+ 0061d36c bytes 08a10c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c8f3e1322e0c24616240a17a1a80689"></a>

### [`0061d33c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d33c.md) → [`0061d37c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061d37c.md) FUN_0061d37c

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
      "definition_site": "0061d380",
      "incomplete_value": false,
      "site": "0061d384",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:328:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061d340",
      "incomplete_value": false,
      "site": "0061d344",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:258:8"
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
      "0061d384",
      "DATA",
      [
        "storage",
        "00c72258",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061d384",
      "DATA",
      [
        "storage",
        "00c72328",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061d340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d33c.md#insn-0061d340)
- 新版 [`0061d380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061d37c.md#insn-0061d380)

~~~diff
- 0061d340 ["COPY", "tmp:0:8", ["const:258:8"]]
- 0061d340 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061d340 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061d340 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061d380 ["COPY", "tmp:0:8", ["const:328:8"]]
+ 0061d380 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061d380 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061d380 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061d340 bytes 08610991
+ 0061d380 bytes 08a10c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-714f3a6dae2be6f8eb617a6116f37924"></a>

### [`0061d354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d354.md) → [`0061d394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061d394.md) FUN_0061d394

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.29% / 新版 99.29%

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
      "site": "0061d52c",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0061d4ec",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "0061d52c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "0061d52c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061d4ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d354.md#insn-0061d4ec) · [`0061d378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d354.md#insn-0061d378) · [`0061d3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d354.md#insn-0061d3b4)
- 新版 [`0061d52c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061d394.md#insn-0061d52c) · [`0061d3b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061d394.md#insn-0061d3b8) · [`0061d3f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061d394.md#insn-0061d3f4)

~~~diff
- 0061d4ec ["INT_ADD", "register:40f0:8", ["const:61d4ec:8", "const:4:8"]]
- 0061d4ec ["CALL", null, ["ram:47acf4:8"]]
+ 0061d52c ["INT_ADD", "register:40f0:8", ["const:61d52c:8", "const:4:8"]]
+ 0061d52c ["CALL", null, ["ram:47ad34:8"]]
- 0061d4ec bytes 0276f997
+ 0061d52c bytes 0276f997
- 0061d378 ["INT_ADD", "register:40f0:8", ["const:61d378:8", "const:4:8"]]
- 0061d378 ["CALL", null, ["callee:00851550:8"]]
+ 0061d3b8 ["INT_ADD", "register:40f0:8", ["const:61d3b8:8", "const:4:8"]]
+ 0061d3b8 ["CALL", null, ["callee:00851550:8"]]
- 0061d378 bytes 60d00894
+ 0061d3b8 bytes 66d00894
- 0061d3b4 ["INT_ADD", "register:40f0:8", ["const:61d3b4:8", "const:4:8"]]
- 0061d3b4 ["CALL", null, ["callee:00851550:8"]]
+ 0061d3f4 ["INT_ADD", "register:40f0:8", ["const:61d3f4:8", "const:4:8"]]
+ 0061d3f4 ["CALL", null, ["callee:00851550:8"]]
- 0061d3b4 bytes 51d00894
+ 0061d3f4 bytes 57d00894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11ff5cb7fd5cc63de18b853acd9a4099"></a>

### [`0061d5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d5b0.md) → [`0061d5f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061d5f0.md) FUN_0061d5f0

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
      "definition_site": "0061d604",
      "incomplete_value": false,
      "site": "0061d608",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:3a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061d5c4",
      "incomplete_value": false,
      "site": "0061d5c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:2d8:8"
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
      "0061d608",
      "DATA",
      [
        "storage",
        "00c722d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061d608",
      "DATA",
      [
        "storage",
        "00c723a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061d5bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d5b0.md#insn-0061d5bc) · [`0061d5c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d5b0.md#insn-0061d5c4)
- 新版 [`0061d5fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061d5f0.md#insn-0061d5fc) · [`0061d604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061d5f0.md#insn-0061d604)

~~~diff
- 0061d5bc ["INT_ADD", "register:40f0:8", ["const:61d5bc:8", "const:4:8"]]
- 0061d5bc ["CALL", null, ["callee:00c57f60:8"]]
+ 0061d5fc ["INT_ADD", "register:40f0:8", ["const:61d5fc:8", "const:4:8"]]
+ 0061d5fc ["CALL", null, ["callee:00c57f60:8"]]
- 0061d5bc bytes 35ea1894
+ 0061d5fc bytes 59ea1894
- 0061d5c4 ["COPY", "tmp:0:8", ["const:2d8:8"]]
- 0061d5c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061d5c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061d5c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061d604 ["COPY", "tmp:0:8", ["const:3a8:8"]]
+ 0061d604 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061d604 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061d604 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061d5c4 bytes 08610b91
+ 0061d604 bytes 08a10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9643a982099a3338c1bfc565b78d6bc4"></a>

### [`0061d5d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d5d4.md) → [`0061d614`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061d614.md) FUN_0061d614

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
      "definition_site": "0061d618",
      "incomplete_value": false,
      "site": "0061d61c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:3a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061d5d8",
      "incomplete_value": false,
      "site": "0061d5dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:2d8:8"
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
      "0061d61c",
      "DATA",
      [
        "storage",
        "00c722d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061d61c",
      "DATA",
      [
        "storage",
        "00c723a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061d5d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d5d4.md#insn-0061d5d8)
- 新版 [`0061d618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061d614.md#insn-0061d618)

~~~diff
- 0061d5d8 ["COPY", "tmp:0:8", ["const:2d8:8"]]
- 0061d5d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061d5d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061d5d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061d618 ["COPY", "tmp:0:8", ["const:3a8:8"]]
+ 0061d618 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061d618 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061d618 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061d5d8 bytes 08610b91
+ 0061d618 bytes 08a10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5af4fd7e3d7bf35ca1a8e6efe8ec363a"></a>

### [`0061d5ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d5ec.md) → [`0061d62c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061d62c.md) FUN_0061d62c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.68% / 新版 98.68%

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
      "site": "0061d654",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0061d614",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "0061d654",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "0061d654",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061d614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d5ec.md#insn-0061d614) · [`0061d620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d5ec.md#insn-0061d620) · [`0061d638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d5ec.md#insn-0061d638)
- 新版 [`0061d654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061d62c.md#insn-0061d654) · [`0061d660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061d62c.md#insn-0061d660) · [`0061d678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061d62c.md#insn-0061d678)

~~~diff
- 0061d614 ["INT_ADD", "register:40f0:8", ["const:61d614:8", "const:4:8"]]
- 0061d614 ["CALL", null, ["ram:47acf4:8"]]
+ 0061d654 ["INT_ADD", "register:40f0:8", ["const:61d654:8", "const:4:8"]]
+ 0061d654 ["CALL", null, ["ram:47ad34:8"]]
- 0061d614 bytes b875f997
+ 0061d654 bytes b875f997
- 0061d620 ["INT_ADD", "register:40f0:8", ["const:61d620:8", "const:4:8"]]
- 0061d620 ["CALL", null, ["callee:0047ce14:8"]]
+ 0061d660 ["INT_ADD", "register:40f0:8", ["const:61d660:8", "const:4:8"]]
+ 0061d660 ["CALL", null, ["callee:0047ce14:8"]]
- 0061d620 bytes ed7df997
+ 0061d660 bytes ed7df997
- 0061d638 ["INT_ADD", "register:40f0:8", ["const:61d638:8", "const:4:8"]]
- 0061d638 ["CALL", null, ["callee:00851550:8"]]
+ 0061d678 ["INT_ADD", "register:40f0:8", ["const:61d678:8", "const:4:8"]]
+ 0061d678 ["CALL", null, ["callee:00851550:8"]]
- 0061d638 bytes b0cf0894
+ 0061d678 bytes b6cf0894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-269dcf8d8e521ebc1ebf187e1b4d2315"></a>

### [`0061d76c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d76c.md) → [`0061d7ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061d7ac.md) FUN_0061d7ac

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
      "definition_site": "0061d7b0",
      "incomplete_value": false,
      "site": "0061d7b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:428:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061d770",
      "incomplete_value": false,
      "site": "0061d774",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
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
      "0061d7b4",
      "DATA",
      [
        "storage",
        "00c72358",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061d7b4",
      "DATA",
      [
        "storage",
        "00c72428",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061d770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d76c.md#insn-0061d770)
- 新版 [`0061d7b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061d7ac.md#insn-0061d7b0)

~~~diff
- 0061d770 ["COPY", "tmp:0:8", ["const:358:8"]]
- 0061d770 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061d770 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061d770 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061d7b0 ["COPY", "tmp:0:8", ["const:428:8"]]
+ 0061d7b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061d7b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061d7b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061d770 bytes 08610d91
+ 0061d7b0 bytes 08a11091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8fa4c6880ba31f35fe913af2315c186"></a>

### [`0061d784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d784.md) → [`0061d7c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061d7c4.md) FUN_0061d7c4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.68% / 新版 98.68%

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
      "site": "0061d7ec",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0061d7ac",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "0061d7ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "0061d7ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061d7ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d784.md#insn-0061d7ac) · [`0061d7b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d784.md#insn-0061d7b8) · [`0061d7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d784.md#insn-0061d7d0)
- 新版 [`0061d7ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061d7c4.md#insn-0061d7ec) · [`0061d7f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061d7c4.md#insn-0061d7f8) · [`0061d810`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061d7c4.md#insn-0061d810)

~~~diff
- 0061d7ac ["INT_ADD", "register:40f0:8", ["const:61d7ac:8", "const:4:8"]]
- 0061d7ac ["CALL", null, ["ram:47acf4:8"]]
+ 0061d7ec ["INT_ADD", "register:40f0:8", ["const:61d7ec:8", "const:4:8"]]
+ 0061d7ec ["CALL", null, ["ram:47ad34:8"]]
- 0061d7ac bytes 5275f997
+ 0061d7ec bytes 5275f997
- 0061d7b8 ["INT_ADD", "register:40f0:8", ["const:61d7b8:8", "const:4:8"]]
- 0061d7b8 ["CALL", null, ["callee:0047ce14:8"]]
+ 0061d7f8 ["INT_ADD", "register:40f0:8", ["const:61d7f8:8", "const:4:8"]]
+ 0061d7f8 ["CALL", null, ["callee:0047ce14:8"]]
- 0061d7b8 bytes 877df997
+ 0061d7f8 bytes 877df997
- 0061d7d0 ["INT_ADD", "register:40f0:8", ["const:61d7d0:8", "const:4:8"]]
- 0061d7d0 ["CALL", null, ["callee:00851550:8"]]
+ 0061d810 ["INT_ADD", "register:40f0:8", ["const:61d810:8", "const:4:8"]]
+ 0061d810 ["CALL", null, ["callee:00851550:8"]]
- 0061d7d0 bytes 4acf0894
+ 0061d810 bytes 50cf0894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4b0e88c2973640a1440548b85f9f750"></a>

### [`0061d91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d91c.md) → [`0061d95c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061d95c.md) FUN_0061d95c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.68% / 新版 98.68%

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
      "site": "0061d984",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0061d944",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "0061d984",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "0061d984",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061d944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d91c.md#insn-0061d944) · [`0061d950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d91c.md#insn-0061d950) · [`0061d968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061d91c.md#insn-0061d968)
- 新版 [`0061d984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061d95c.md#insn-0061d984) · [`0061d990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061d95c.md#insn-0061d990) · [`0061d9a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061d95c.md#insn-0061d9a8)

~~~diff
- 0061d944 ["INT_ADD", "register:40f0:8", ["const:61d944:8", "const:4:8"]]
- 0061d944 ["CALL", null, ["ram:47acf4:8"]]
+ 0061d984 ["INT_ADD", "register:40f0:8", ["const:61d984:8", "const:4:8"]]
+ 0061d984 ["CALL", null, ["ram:47ad34:8"]]
- 0061d944 bytes ec74f997
+ 0061d984 bytes ec74f997
- 0061d950 ["INT_ADD", "register:40f0:8", ["const:61d950:8", "const:4:8"]]
- 0061d950 ["CALL", null, ["callee:0047ce14:8"]]
+ 0061d990 ["INT_ADD", "register:40f0:8", ["const:61d990:8", "const:4:8"]]
+ 0061d990 ["CALL", null, ["callee:0047ce14:8"]]
- 0061d950 bytes 217df997
+ 0061d990 bytes 217df997
- 0061d968 ["INT_ADD", "register:40f0:8", ["const:61d968:8", "const:4:8"]]
- 0061d968 ["CALL", null, ["callee:00851550:8"]]
+ 0061d9a8 ["INT_ADD", "register:40f0:8", ["const:61d9a8:8", "const:4:8"]]
+ 0061d9a8 ["CALL", null, ["callee:00851550:8"]]
- 0061d968 bytes e4ce0894
+ 0061d9a8 bytes eace0894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83e68664cd12ba9fef2cdf3fcc6991ef"></a>

### [`0061da78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061da78.md) → [`0061dab8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061dab8.md) FUN_0061dab8

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
      "definition_site": "0061dacc",
      "incomplete_value": false,
      "site": "0061dad0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:528:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061da8c",
      "incomplete_value": false,
      "site": "0061da90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:458:8"
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
      "0061dad0",
      "DATA",
      [
        "storage",
        "00c72458",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061dad0",
      "DATA",
      [
        "storage",
        "00c72528",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061da84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061da78.md#insn-0061da84) · [`0061da8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061da78.md#insn-0061da8c)
- 新版 [`0061dac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061dab8.md#insn-0061dac4) · [`0061dacc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061dab8.md#insn-0061dacc)

~~~diff
- 0061da84 ["INT_ADD", "register:40f0:8", ["const:61da84:8", "const:4:8"]]
- 0061da84 ["CALL", null, ["callee:00c57f60:8"]]
+ 0061dac4 ["INT_ADD", "register:40f0:8", ["const:61dac4:8", "const:4:8"]]
+ 0061dac4 ["CALL", null, ["callee:00c57f60:8"]]
- 0061da84 bytes 03e91894
+ 0061dac4 bytes 27e91894
- 0061da8c ["COPY", "tmp:0:8", ["const:458:8"]]
- 0061da8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061da8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061da8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061dacc ["COPY", "tmp:0:8", ["const:528:8"]]
+ 0061dacc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061dacc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061dacc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061da8c bytes 08611191
+ 0061dacc bytes 08a11491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd258c2eafec94bea7727b09758fc1b8"></a>

### [`0061dab4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061dab4.md) → [`0061daf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061daf4.md) FUN_0061daf4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.68% / 新版 98.68%

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
      "site": "0061db1c",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0061dadc",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "0061db1c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "0061db1c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061dadc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061dab4.md#insn-0061dadc) · [`0061dae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061dab4.md#insn-0061dae8) · [`0061db00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061dab4.md#insn-0061db00)
- 新版 [`0061db1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061daf4.md#insn-0061db1c) · [`0061db28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061daf4.md#insn-0061db28) · [`0061db40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061daf4.md#insn-0061db40)

~~~diff
- 0061dadc ["INT_ADD", "register:40f0:8", ["const:61dadc:8", "const:4:8"]]
- 0061dadc ["CALL", null, ["ram:47acf4:8"]]
+ 0061db1c ["INT_ADD", "register:40f0:8", ["const:61db1c:8", "const:4:8"]]
+ 0061db1c ["CALL", null, ["ram:47ad34:8"]]
- 0061dadc bytes 8674f997
+ 0061db1c bytes 8674f997
- 0061dae8 ["INT_ADD", "register:40f0:8", ["const:61dae8:8", "const:4:8"]]
- 0061dae8 ["CALL", null, ["callee:0047ce14:8"]]
+ 0061db28 ["INT_ADD", "register:40f0:8", ["const:61db28:8", "const:4:8"]]
+ 0061db28 ["CALL", null, ["callee:0047ce14:8"]]
- 0061dae8 bytes bb7cf997
+ 0061db28 bytes bb7cf997
- 0061db00 ["INT_ADD", "register:40f0:8", ["const:61db00:8", "const:4:8"]]
- 0061db00 ["CALL", null, ["callee:00851550:8"]]
+ 0061db40 ["INT_ADD", "register:40f0:8", ["const:61db40:8", "const:4:8"]]
+ 0061db40 ["CALL", null, ["callee:00851550:8"]]
- 0061db00 bytes 7ece0894
+ 0061db40 bytes 84ce0894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-139f3ebe7513ed719d68fc90669420fa"></a>

### [`0061dc34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061dc34.md) → [`0061dc74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061dc74.md) FUN_0061dc74

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
      "definition_site": "0061dc78",
      "incomplete_value": false,
      "site": "0061dc7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:5a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061dc38",
      "incomplete_value": false,
      "site": "0061dc3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:4d8:8"
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
      "0061dc7c",
      "DATA",
      [
        "storage",
        "00c724d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061dc7c",
      "DATA",
      [
        "storage",
        "00c725a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061dc38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061dc34.md#insn-0061dc38)
- 新版 [`0061dc78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061dc74.md#insn-0061dc78)

~~~diff
- 0061dc38 ["COPY", "tmp:0:8", ["const:4d8:8"]]
- 0061dc38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061dc38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061dc38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061dc78 ["COPY", "tmp:0:8", ["const:5a8:8"]]
+ 0061dc78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061dc78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061dc78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061dc38 bytes 08611391
+ 0061dc78 bytes 08a11691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1339b8ec22775a4f277f5f9136777390"></a>

### [`0061dc4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061dc4c.md) → [`0061dc8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061dc8c.md) FUN_0061dc8c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.72% / 新版 98.72%

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
      "site": "0061dcb4",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0061dc74",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "0061dcb4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "0061dcb4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061dc74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061dc4c.md#insn-0061dc74) · [`0061dc80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061dc4c.md#insn-0061dc80) · [`0061dca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061dc4c.md#insn-0061dca0)
- 新版 [`0061dcb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061dc8c.md#insn-0061dcb4) · [`0061dcc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061dc8c.md#insn-0061dcc0) · [`0061dce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061dc8c.md#insn-0061dce0)

~~~diff
- 0061dc74 ["INT_ADD", "register:40f0:8", ["const:61dc74:8", "const:4:8"]]
- 0061dc74 ["CALL", null, ["ram:47acf4:8"]]
+ 0061dcb4 ["INT_ADD", "register:40f0:8", ["const:61dcb4:8", "const:4:8"]]
+ 0061dcb4 ["CALL", null, ["ram:47ad34:8"]]
- 0061dc74 bytes 2074f997
+ 0061dcb4 bytes 2074f997
- 0061dc80 ["INT_ADD", "register:40f0:8", ["const:61dc80:8", "const:4:8"]]
- 0061dc80 ["CALL", null, ["callee:0047ce14:8"]]
+ 0061dcc0 ["INT_ADD", "register:40f0:8", ["const:61dcc0:8", "const:4:8"]]
+ 0061dcc0 ["CALL", null, ["callee:0047ce14:8"]]
- 0061dc80 bytes 557cf997
+ 0061dcc0 bytes 557cf997
- 0061dca0 ["INT_ADD", "register:40f0:8", ["const:61dca0:8", "const:4:8"]]
- 0061dca0 ["CALL", null, ["callee:00851550:8"]]
+ 0061dce0 ["INT_ADD", "register:40f0:8", ["const:61dce0:8", "const:4:8"]]
+ 0061dce0 ["CALL", null, ["callee:00851550:8"]]
- 0061dca0 bytes 16ce0894
+ 0061dce0 bytes 1cce0894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5465ce42dff49e98627866282d18f033"></a>

### [`0061ddb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061ddb0.md) → [`0061ddf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061ddf0.md) FUN_0061ddf0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0061de04",
      "incomplete_value": true,
      "site": "0061de08",
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
            "const:628:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061ddc4",
      "incomplete_value": true,
      "site": "0061ddc8",
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
            "const:558:8"
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
      "0061de08",
      "DATA",
      [
        "storage",
        "00c72558",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061de08",
      "DATA",
      [
        "storage",
        "00c72628",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061ddbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061ddb0.md#insn-0061ddbc) · [`0061ddc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061ddb0.md#insn-0061ddc4)
- 新版 [`0061ddfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061ddf0.md#insn-0061ddfc) · [`0061de04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061ddf0.md#insn-0061de04)

~~~diff
- 0061ddbc ["INT_ADD", "register:40f0:8", ["const:61ddbc:8", "const:4:8"]]
- 0061ddbc ["CALL", null, ["callee:00c57f60:8"]]
+ 0061ddfc ["INT_ADD", "register:40f0:8", ["const:61ddfc:8", "const:4:8"]]
+ 0061ddfc ["CALL", null, ["callee:00c57f60:8"]]
- 0061ddbc bytes 35e81894
+ 0061ddfc bytes 59e81894
- 0061ddc4 ["COPY", "tmp:0:8", ["const:558:8"]]
- 0061ddc4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061ddc4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061ddc4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061de04 ["COPY", "tmp:0:8", ["const:628:8"]]
+ 0061de04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061de04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061de04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061ddc4 bytes 08611591
+ 0061de04 bytes 08a11891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a5c115ec9950ac56faddd46ac49796b"></a>

### [`0061ddd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061ddd4.md) → [`0061de14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061de14.md) FUN_0061de14

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
      "definition_site": "0061de18",
      "incomplete_value": false,
      "site": "0061de1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:628:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061ddd8",
      "incomplete_value": false,
      "site": "0061dddc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:558:8"
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
      "0061de1c",
      "DATA",
      [
        "storage",
        "00c72558",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061de1c",
      "DATA",
      [
        "storage",
        "00c72628",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061ddd4.md#insn-0061ddd8)
- 新版 [`0061de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061de14.md#insn-0061de18)

~~~diff
- 0061ddd8 ["COPY", "tmp:0:8", ["const:558:8"]]
- 0061ddd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061ddd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061ddd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061de18 ["COPY", "tmp:0:8", ["const:628:8"]]
+ 0061de18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061de18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061de18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061ddd8 bytes 08611591
+ 0061de18 bytes 08a11891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a4fa9d944afce6eea32fd39602dfc1d"></a>

### [`0061ddec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061ddec.md) → [`0061de2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061de2c.md) FUN_0061de2c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.68% / 新版 98.68%

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
      "site": "0061de54",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0061de14",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "0061de54",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "0061de54",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061de14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061ddec.md#insn-0061de14) · [`0061de20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061ddec.md#insn-0061de20) · [`0061de38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061ddec.md#insn-0061de38)
- 新版 [`0061de54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061de2c.md#insn-0061de54) · [`0061de60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061de2c.md#insn-0061de60) · [`0061de78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061de2c.md#insn-0061de78)

~~~diff
- 0061de14 ["INT_ADD", "register:40f0:8", ["const:61de14:8", "const:4:8"]]
- 0061de14 ["CALL", null, ["ram:47acf4:8"]]
+ 0061de54 ["INT_ADD", "register:40f0:8", ["const:61de54:8", "const:4:8"]]
+ 0061de54 ["CALL", null, ["ram:47ad34:8"]]
- 0061de14 bytes b873f997
+ 0061de54 bytes b873f997
- 0061de20 ["INT_ADD", "register:40f0:8", ["const:61de20:8", "const:4:8"]]
- 0061de20 ["CALL", null, ["callee:0047ce14:8"]]
+ 0061de60 ["INT_ADD", "register:40f0:8", ["const:61de60:8", "const:4:8"]]
+ 0061de60 ["CALL", null, ["callee:0047ce14:8"]]
- 0061de20 bytes ed7bf997
+ 0061de60 bytes ed7bf997
- 0061de38 ["INT_ADD", "register:40f0:8", ["const:61de38:8", "const:4:8"]]
- 0061de38 ["CALL", null, ["callee:00851550:8"]]
+ 0061de78 ["INT_ADD", "register:40f0:8", ["const:61de78:8", "const:4:8"]]
+ 0061de78 ["CALL", null, ["callee:00851550:8"]]
- 0061de38 bytes b0cd0894
+ 0061de78 bytes b6cd0894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b09121de726e4bfce14ad5666abd72b2"></a>

### [`0061df48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061df48.md) → [`0061df88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061df88.md) FUN_0061df88

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
      "definition_site": "0061df9c",
      "incomplete_value": false,
      "site": "0061dfa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061df5c",
      "incomplete_value": false,
      "site": "0061df60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:5d8:8"
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
      "0061dfa0",
      "DATA",
      [
        "storage",
        "00c725d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061dfa0",
      "DATA",
      [
        "storage",
        "00c726a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061df54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061df48.md#insn-0061df54) · [`0061df5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061df48.md#insn-0061df5c)
- 新版 [`0061df94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061df88.md#insn-0061df94) · [`0061df9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061df88.md#insn-0061df9c)

~~~diff
- 0061df54 ["INT_ADD", "register:40f0:8", ["const:61df54:8", "const:4:8"]]
- 0061df54 ["CALL", null, ["callee:00c57f60:8"]]
+ 0061df94 ["INT_ADD", "register:40f0:8", ["const:61df94:8", "const:4:8"]]
+ 0061df94 ["CALL", null, ["callee:00c57f60:8"]]
- 0061df54 bytes cfe71894
+ 0061df94 bytes f3e71894
- 0061df5c ["COPY", "tmp:0:8", ["const:5d8:8"]]
- 0061df5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061df5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061df5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061df9c ["COPY", "tmp:0:8", ["const:6a8:8"]]
+ 0061df9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061df9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061df9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061df5c bytes 08611791
+ 0061df9c bytes 08a11a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-405d0236faf35857f43bbbe70f8dce7c"></a>

### [`0061df6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061df6c.md) → [`0061dfac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061dfac.md) FUN_0061dfac

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
      "definition_site": "0061dfb0",
      "incomplete_value": false,
      "site": "0061dfb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061df70",
      "incomplete_value": false,
      "site": "0061df74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:5d8:8"
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
      "0061dfb4",
      "DATA",
      [
        "storage",
        "00c725d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061dfb4",
      "DATA",
      [
        "storage",
        "00c726a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061df70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061df6c.md#insn-0061df70)
- 新版 [`0061dfb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061dfac.md#insn-0061dfb0)

~~~diff
- 0061df70 ["COPY", "tmp:0:8", ["const:5d8:8"]]
- 0061df70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061df70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061df70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061dfb0 ["COPY", "tmp:0:8", ["const:6a8:8"]]
+ 0061dfb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061dfb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061dfb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061df70 bytes 08611791
+ 0061dfb0 bytes 08a11a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75cdb1b12aca8c04316bb2bbed183e1f"></a>

### [`0061df84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061df84.md) → [`0061dfc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061dfc4.md) FUN_0061dfc4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.68% / 新版 98.68%

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
      "site": "0061dfec",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0061dfac",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "0061dfec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "0061dfec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061dfac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061df84.md#insn-0061dfac) · [`0061dfb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061df84.md#insn-0061dfb8) · [`0061dfd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061d/0061df84.md#insn-0061dfd0)
- 新版 [`0061dfec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061dfc4.md#insn-0061dfec) · [`0061dff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061dfc4.md#insn-0061dff8) · [`0061e010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061d/0061dfc4.md#insn-0061e010)

~~~diff
- 0061dfac ["INT_ADD", "register:40f0:8", ["const:61dfac:8", "const:4:8"]]
- 0061dfac ["CALL", null, ["ram:47acf4:8"]]
+ 0061dfec ["INT_ADD", "register:40f0:8", ["const:61dfec:8", "const:4:8"]]
+ 0061dfec ["CALL", null, ["ram:47ad34:8"]]
- 0061dfac bytes 5273f997
+ 0061dfec bytes 5273f997
- 0061dfb8 ["INT_ADD", "register:40f0:8", ["const:61dfb8:8", "const:4:8"]]
- 0061dfb8 ["CALL", null, ["callee:0047ce14:8"]]
+ 0061dff8 ["INT_ADD", "register:40f0:8", ["const:61dff8:8", "const:4:8"]]
+ 0061dff8 ["CALL", null, ["callee:0047ce14:8"]]
- 0061dfb8 bytes 877bf997
+ 0061dff8 bytes 877bf997
- 0061dfd0 ["INT_ADD", "register:40f0:8", ["const:61dfd0:8", "const:4:8"]]
- 0061dfd0 ["CALL", null, ["callee:00851550:8"]]
+ 0061e010 ["INT_ADD", "register:40f0:8", ["const:61e010:8", "const:4:8"]]
+ 0061e010 ["CALL", null, ["callee:00851550:8"]]
- 0061dfd0 bytes 4acd0894
+ 0061e010 bytes 50cd0894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b29c8423bf6669c6ed77b2ff31d5d46c"></a>

### [`0061e0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e0e0.md) → [`0061e120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061e120.md) FUN_0061e120

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
      "definition_site": "0061e134",
      "incomplete_value": false,
      "site": "0061e138",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:728:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061e0f4",
      "incomplete_value": false,
      "site": "0061e0f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:658:8"
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
      "0061e138",
      "DATA",
      [
        "storage",
        "00c72658",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061e138",
      "DATA",
      [
        "storage",
        "00c72728",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061e0ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e0e0.md#insn-0061e0ec) · [`0061e0f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e0e0.md#insn-0061e0f4)
- 新版 [`0061e12c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061e120.md#insn-0061e12c) · [`0061e134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061e120.md#insn-0061e134)

~~~diff
- 0061e0ec ["INT_ADD", "register:40f0:8", ["const:61e0ec:8", "const:4:8"]]
- 0061e0ec ["CALL", null, ["callee:00c57f60:8"]]
+ 0061e12c ["INT_ADD", "register:40f0:8", ["const:61e12c:8", "const:4:8"]]
+ 0061e12c ["CALL", null, ["callee:00c57f60:8"]]
- 0061e0ec bytes 69e71894
+ 0061e12c bytes 8de71894
- 0061e0f4 ["COPY", "tmp:0:8", ["const:658:8"]]
- 0061e0f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061e0f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061e0f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061e134 ["COPY", "tmp:0:8", ["const:728:8"]]
+ 0061e134 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061e134 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061e134 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061e0f4 bytes 08611991
+ 0061e134 bytes 08a11c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cd2c1870a3c7bbb788cbd1ac0f4ccc4"></a>

### [`0061e104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e104.md) → [`0061e144`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061e144.md) FUN_0061e144

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
      "definition_site": "0061e148",
      "incomplete_value": false,
      "site": "0061e14c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:728:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061e108",
      "incomplete_value": false,
      "site": "0061e10c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:658:8"
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
      "0061e14c",
      "DATA",
      [
        "storage",
        "00c72658",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061e14c",
      "DATA",
      [
        "storage",
        "00c72728",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061e108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e104.md#insn-0061e108)
- 新版 [`0061e148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061e144.md#insn-0061e148)

~~~diff
- 0061e108 ["COPY", "tmp:0:8", ["const:658:8"]]
- 0061e108 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061e108 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061e108 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061e148 ["COPY", "tmp:0:8", ["const:728:8"]]
+ 0061e148 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061e148 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061e148 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061e108 bytes 08611991
+ 0061e148 bytes 08a11c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2ccd9468f71f87bed638a7fe08d52e3"></a>

### [`0061e11c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e11c.md) → [`0061e15c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061e15c.md) FUN_0061e15c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.68% / 新版 98.68%

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
      "site": "0061e184",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0061e144",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "0061e184",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "0061e184",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061e144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e11c.md#insn-0061e144) · [`0061e150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e11c.md#insn-0061e150) · [`0061e168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e11c.md#insn-0061e168)
- 新版 [`0061e184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061e15c.md#insn-0061e184) · [`0061e190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061e15c.md#insn-0061e190) · [`0061e1a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061e15c.md#insn-0061e1a8)

~~~diff
- 0061e144 ["INT_ADD", "register:40f0:8", ["const:61e144:8", "const:4:8"]]
- 0061e144 ["CALL", null, ["ram:47acf4:8"]]
+ 0061e184 ["INT_ADD", "register:40f0:8", ["const:61e184:8", "const:4:8"]]
+ 0061e184 ["CALL", null, ["ram:47ad34:8"]]
- 0061e144 bytes ec72f997
+ 0061e184 bytes ec72f997
- 0061e150 ["INT_ADD", "register:40f0:8", ["const:61e150:8", "const:4:8"]]
- 0061e150 ["CALL", null, ["callee:0047ce14:8"]]
+ 0061e190 ["INT_ADD", "register:40f0:8", ["const:61e190:8", "const:4:8"]]
+ 0061e190 ["CALL", null, ["callee:0047ce14:8"]]
- 0061e150 bytes 217bf997
+ 0061e190 bytes 217bf997
- 0061e168 ["INT_ADD", "register:40f0:8", ["const:61e168:8", "const:4:8"]]
- 0061e168 ["CALL", null, ["callee:00851550:8"]]
+ 0061e1a8 ["INT_ADD", "register:40f0:8", ["const:61e1a8:8", "const:4:8"]]
+ 0061e1a8 ["CALL", null, ["callee:00851550:8"]]
- 0061e168 bytes e4cc0894
+ 0061e1a8 bytes eacc0894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b590896ad9e31bd226552be730cd8f9f"></a>

### [`0061e278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e278.md) → [`0061e2b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061e2b8.md) FUN_0061e2b8

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
      "definition_site": "0061e2cc",
      "incomplete_value": false,
      "site": "0061e2d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:7a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061e28c",
      "incomplete_value": false,
      "site": "0061e290",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:6d8:8"
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
      "0061e2d0",
      "DATA",
      [
        "storage",
        "00c726d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061e2d0",
      "DATA",
      [
        "storage",
        "00c727a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061e284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e278.md#insn-0061e284) · [`0061e28c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e278.md#insn-0061e28c)
- 新版 [`0061e2c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061e2b8.md#insn-0061e2c4) · [`0061e2cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061e2b8.md#insn-0061e2cc)

~~~diff
- 0061e284 ["INT_ADD", "register:40f0:8", ["const:61e284:8", "const:4:8"]]
- 0061e284 ["CALL", null, ["callee:00c57f60:8"]]
+ 0061e2c4 ["INT_ADD", "register:40f0:8", ["const:61e2c4:8", "const:4:8"]]
+ 0061e2c4 ["CALL", null, ["callee:00c57f60:8"]]
- 0061e284 bytes 03e71894
+ 0061e2c4 bytes 27e71894
- 0061e28c ["COPY", "tmp:0:8", ["const:6d8:8"]]
- 0061e28c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061e28c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061e28c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061e2cc ["COPY", "tmp:0:8", ["const:7a8:8"]]
+ 0061e2cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061e2cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061e2cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061e28c bytes 08611b91
+ 0061e2cc bytes 08a11e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-042f1d078bec7b8a0fcaeae8fd5c315c"></a>

### [`0061e29c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e29c.md) → [`0061e2dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061e2dc.md) FUN_0061e2dc

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
      "definition_site": "0061e2e0",
      "incomplete_value": false,
      "site": "0061e2e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:7a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061e2a0",
      "incomplete_value": false,
      "site": "0061e2a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:6d8:8"
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
      "0061e2e4",
      "DATA",
      [
        "storage",
        "00c726d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061e2e4",
      "DATA",
      [
        "storage",
        "00c727a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061e2a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e29c.md#insn-0061e2a0)
- 新版 [`0061e2e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061e2dc.md#insn-0061e2e0)

~~~diff
- 0061e2a0 ["COPY", "tmp:0:8", ["const:6d8:8"]]
- 0061e2a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061e2a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061e2a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061e2e0 ["COPY", "tmp:0:8", ["const:7a8:8"]]
+ 0061e2e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061e2e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061e2e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061e2a0 bytes 08611b91
+ 0061e2e0 bytes 08a11e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f99439d143af810201e5dfad4686b7f"></a>

### [`0061e2b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e2b4.md) → [`0061e2f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061e2f4.md) FUN_0061e2f4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00a1a6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a6a4.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`00a1a6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a1a/00a1a6f8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.80% / 新版 98.80%

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
      "site": "0061e31c",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0061e2dc",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "0061e31c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "0061e31c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061e2dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e2b4.md#insn-0061e2dc) · [`0061e2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e2b4.md#insn-0061e2e8) · [`0061e308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e2b4.md#insn-0061e308)
- 新版 [`0061e31c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061e2f4.md#insn-0061e31c) · [`0061e328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061e2f4.md#insn-0061e328) · [`0061e348`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061e2f4.md#insn-0061e348)

~~~diff
- 0061e2dc ["INT_ADD", "register:40f0:8", ["const:61e2dc:8", "const:4:8"]]
- 0061e2dc ["CALL", null, ["ram:47acf4:8"]]
+ 0061e31c ["INT_ADD", "register:40f0:8", ["const:61e31c:8", "const:4:8"]]
+ 0061e31c ["CALL", null, ["ram:47ad34:8"]]
- 0061e2dc bytes 8672f997
+ 0061e31c bytes 8672f997
- 0061e2e8 ["INT_ADD", "register:40f0:8", ["const:61e2e8:8", "const:4:8"]]
- 0061e2e8 ["CALL", null, ["callee:0047ce14:8"]]
+ 0061e328 ["INT_ADD", "register:40f0:8", ["const:61e328:8", "const:4:8"]]
+ 0061e328 ["CALL", null, ["callee:0047ce14:8"]]
- 0061e2e8 bytes bb7af997
+ 0061e328 bytes bb7af997
- 0061e308 ["INT_ADD", "register:40f0:8", ["const:61e308:8", "const:4:8"]]
- 0061e308 ["CALL", null, ["callee:00851550:8"]]
+ 0061e348 ["INT_ADD", "register:40f0:8", ["const:61e348:8", "const:4:8"]]
+ 0061e348 ["CALL", null, ["callee:00851550:8"]]
- 0061e308 bytes 7ccc0894
+ 0061e348 bytes 82cc0894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-883990cdfaa6f342fda60b3dcbcf9a67"></a>

### [`0061e42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e42c.md) → [`0061e46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061e46c.md) FUN_0061e46c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0061e480",
      "incomplete_value": true,
      "site": "0061e484",
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
            "const:828:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061e440",
      "incomplete_value": true,
      "site": "0061e444",
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
            "const:758:8"
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
      "0061e484",
      "DATA",
      [
        "storage",
        "00c72758",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061e484",
      "DATA",
      [
        "storage",
        "00c72828",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061e438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e42c.md#insn-0061e438) · [`0061e440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e42c.md#insn-0061e440)
- 新版 [`0061e478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061e46c.md#insn-0061e478) · [`0061e480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061e46c.md#insn-0061e480)

~~~diff
- 0061e438 ["INT_ADD", "register:40f0:8", ["const:61e438:8", "const:4:8"]]
- 0061e438 ["CALL", null, ["callee:00c57f60:8"]]
+ 0061e478 ["INT_ADD", "register:40f0:8", ["const:61e478:8", "const:4:8"]]
+ 0061e478 ["CALL", null, ["callee:00c57f60:8"]]
- 0061e438 bytes 96e61894
+ 0061e478 bytes bae61894
- 0061e440 ["COPY", "tmp:0:8", ["const:758:8"]]
- 0061e440 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061e440 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061e440 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061e480 ["COPY", "tmp:0:8", ["const:828:8"]]
+ 0061e480 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061e480 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061e480 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061e440 bytes 08611d91
+ 0061e480 bytes 08a12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87a967bf813c1f6f86a771f191171cf1"></a>

### [`0061e450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e450.md) → [`0061e490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061e490.md) FUN_0061e490

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
      "definition_site": "0061e494",
      "incomplete_value": false,
      "site": "0061e498",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:828:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061e454",
      "incomplete_value": false,
      "site": "0061e458",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:758:8"
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
      "0061e498",
      "DATA",
      [
        "storage",
        "00c72758",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061e498",
      "DATA",
      [
        "storage",
        "00c72828",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061e454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e450.md#insn-0061e454)
- 新版 [`0061e494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061e490.md#insn-0061e494)

~~~diff
- 0061e454 ["COPY", "tmp:0:8", ["const:758:8"]]
- 0061e454 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061e454 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061e454 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061e494 ["COPY", "tmp:0:8", ["const:828:8"]]
+ 0061e494 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061e494 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061e494 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061e454 bytes 08611d91
+ 0061e494 bytes 08a12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9ed2f2829c97fc06a93a17ee15ef765"></a>

### [`0061e548`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e548.md) → [`0061e588`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061e588.md) FUN_0061e588

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
      "definition_site": "0061e5ac",
      "incomplete_value": false,
      "site": "0061e5ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:8a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061e56c",
      "incomplete_value": false,
      "site": "0061e56c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:7d8:8"
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
      "0061e5ac",
      "DATA",
      [
        "storage",
        "00c727d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061e5ac",
      "DATA",
      [
        "storage",
        "00c728a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061e55c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e548.md#insn-0061e55c) · [`0061e568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e548.md#insn-0061e568)
- 新版 [`0061e59c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061e588.md#insn-0061e59c) · [`0061e5a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061e588.md#insn-0061e5a8)

~~~diff
- 0061e55c ["INT_ADD", "register:40f0:8", ["const:61e55c:8", "const:4:8"]]
- 0061e55c ["CALL", null, ["callee:00c57f60:8"]]
+ 0061e59c ["INT_ADD", "register:40f0:8", ["const:61e59c:8", "const:4:8"]]
+ 0061e59c ["CALL", null, ["callee:00c57f60:8"]]
- 0061e55c bytes 4de61894
+ 0061e59c bytes 71e61894
- 0061e568 ["COPY", "tmp:0:8", ["const:7d8:8"]]
- 0061e568 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061e568 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061e568 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061e5a8 ["COPY", "tmp:0:8", ["const:8a8:8"]]
+ 0061e5a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061e5a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061e5a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061e568 bytes 08611f91
+ 0061e5a8 bytes 08a12291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9dd367bb425d1ae94673acc3c28f8c9a"></a>

### [`0061e57c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e57c.md) → [`0061e5bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061e5bc.md) FUN_0061e5bc

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
      "definition_site": "0061e5c8",
      "incomplete_value": false,
      "site": "0061e5c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:8a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061e588",
      "incomplete_value": false,
      "site": "0061e588",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:7d8:8"
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
      "0061e5c8",
      "DATA",
      [
        "storage",
        "00c727d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061e5c8",
      "DATA",
      [
        "storage",
        "00c728a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061e584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e57c.md#insn-0061e584)
- 新版 [`0061e5c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061e5bc.md#insn-0061e5c4)

~~~diff
- 0061e584 ["COPY", "tmp:0:8", ["const:7d8:8"]]
- 0061e584 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0061e584 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0061e584 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0061e5c4 ["COPY", "tmp:0:8", ["const:8a8:8"]]
+ 0061e5c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0061e5c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0061e5c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0061e584 bytes 29611f91
+ 0061e5c4 bytes 29a12291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9d6643ee62e236b596399ca3738b688"></a>

### [`0061e598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e598.md) → [`0061e5d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061e5d8.md) FUN_0061e5d8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`007473d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00747/007473d0.md) [`007473d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00747/007473d8.md) [`008b6ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6ea4.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00747428`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00747/00747428.md) [`00747430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00747/00747430.md) [`008b6efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6efc.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.12% / 新版 95.12%

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
      "site": "0061e5f4",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0061e5b4",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "site": "0061e614",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0061e5d4",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "0061e5f4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "0061e614",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "0061e5f4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "0061e614",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061e5b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e598.md#insn-0061e5b4) · [`0061e5d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e598.md#insn-0061e5d4) · [`0061e5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e598.md#insn-0061e5e0)
- 新版 [`0061e5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061e5d8.md#insn-0061e5f4) · [`0061e614`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061e5d8.md#insn-0061e614) · [`0061e620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061e5d8.md#insn-0061e620)

~~~diff
- 0061e5b4 ["INT_ADD", "register:40f0:8", ["const:61e5b4:8", "const:4:8"]]
- 0061e5b4 ["CALL", null, ["ram:47acf4:8"]]
+ 0061e5f4 ["INT_ADD", "register:40f0:8", ["const:61e5f4:8", "const:4:8"]]
+ 0061e5f4 ["CALL", null, ["ram:47ad34:8"]]
- 0061e5b4 bytes d071f997
+ 0061e5f4 bytes d071f997
- 0061e5d4 ["INT_ADD", "register:40f0:8", ["const:61e5d4:8", "const:4:8"]]
- 0061e5d4 ["CALL", null, ["ram:47acf4:8"]]
+ 0061e614 ["INT_ADD", "register:40f0:8", ["const:61e614:8", "const:4:8"]]
+ 0061e614 ["CALL", null, ["ram:47ad34:8"]]
- 0061e5d4 bytes c871f997
+ 0061e614 bytes c871f997
- 0061e5e0 ["INT_ADD", "register:40f0:8", ["const:61e5e0:8", "const:4:8"]]
- 0061e5e0 ["CALL", null, ["callee:0047ce14:8"]]
+ 0061e620 ["INT_ADD", "register:40f0:8", ["const:61e620:8", "const:4:8"]]
+ 0061e620 ["CALL", null, ["callee:0047ce14:8"]]
- 0061e5e0 bytes fd79f997
+ 0061e620 bytes fd79f997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abbd42b376bca8f5e9067774105b712c"></a>

### [`0061e66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e66c.md) → [`0061e6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061e6ac.md) FUN_0061e6ac

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
      "definition_site": "0061e6c0",
      "incomplete_value": false,
      "site": "0061e6c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:928:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061e680",
      "incomplete_value": false,
      "site": "0061e684",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:858:8"
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
      "0061e6c4",
      "DATA",
      [
        "storage",
        "00c72858",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061e6c4",
      "DATA",
      [
        "storage",
        "00c72928",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061e678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e66c.md#insn-0061e678) · [`0061e680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e66c.md#insn-0061e680)
- 新版 [`0061e6b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061e6ac.md#insn-0061e6b8) · [`0061e6c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061e6ac.md#insn-0061e6c0)

~~~diff
- 0061e678 ["INT_ADD", "register:40f0:8", ["const:61e678:8", "const:4:8"]]
- 0061e678 ["CALL", null, ["callee:00c57f60:8"]]
+ 0061e6b8 ["INT_ADD", "register:40f0:8", ["const:61e6b8:8", "const:4:8"]]
+ 0061e6b8 ["CALL", null, ["callee:00c57f60:8"]]
- 0061e678 bytes 06e61894
+ 0061e6b8 bytes 2ae61894
- 0061e680 ["COPY", "tmp:0:8", ["const:858:8"]]
- 0061e680 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061e680 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061e680 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061e6c0 ["COPY", "tmp:0:8", ["const:928:8"]]
+ 0061e6c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061e6c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061e6c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061e680 bytes 08612191
+ 0061e6c0 bytes 08a12491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-882365a7275ddd25ca86924f268d3723"></a>

### [`0061e690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e690.md) → [`0061e6d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061e6d0.md) FUN_0061e6d0

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
      "definition_site": "0061e6d4",
      "incomplete_value": false,
      "site": "0061e6d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:928:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061e694",
      "incomplete_value": false,
      "site": "0061e698",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:858:8"
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
      "0061e6d8",
      "DATA",
      [
        "storage",
        "00c72858",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061e6d8",
      "DATA",
      [
        "storage",
        "00c72928",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061e694`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e690.md#insn-0061e694)
- 新版 [`0061e6d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061e6d0.md#insn-0061e6d4)

~~~diff
- 0061e694 ["COPY", "tmp:0:8", ["const:858:8"]]
- 0061e694 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061e694 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061e694 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061e6d4 ["COPY", "tmp:0:8", ["const:928:8"]]
+ 0061e6d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061e6d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061e6d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061e694 bytes 08612191
+ 0061e6d4 bytes 08a12491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f4a583836f7cbbbcc561a2967dac8ce"></a>

### [`0061e6a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e6a8.md) → [`0061e6e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061e6e8.md) FUN_0061e6e8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 24件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md)
- 新版 呼出元 0件  · 呼出先 24件 [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0047e64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e64c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 88.18% / 新版 88.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 3件, `store_destination` 2件, `store_value` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0061e7cc",
      "incomplete_value": false,
      "site": "0061e7d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061e78c",
      "incomplete_value": false,
      "site": "0061e794",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:8c8:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0061e9e0",
      "incomplete_value": false,
      "site": "0061e9e0",
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
                "const:0:8"
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
      "definition_site": "0061e9a0",
      "incomplete_value": false,
      "site": "0061e9a0",
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
                "const:f00:8"
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
    "ordinal": 21,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0061e9e4",
      "incomplete_value": false,
      "site": "0061e9e4",
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
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061e9a4",
      "incomplete_value": false,
      "site": "0061e9a4",
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
            "const:f00:8"
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0061e70c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "0061e720",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "0061e768",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0061e70c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ],
    [
      "0061e720",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "0061e768",
      "READ",
      [
        "storage",
        "00ca4a78",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061e6cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e6a8.md#insn-0061e6cc) · [`0061e6e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e6a8.md#insn-0061e6e0) · [`0061e6ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061e6a8.md#insn-0061e6ec)
- 新版 [`0061e70c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061e6e8.md#insn-0061e70c) · [`0061e720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061e6e8.md#insn-0061e720) · [`0061e72c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061e6e8.md#insn-0061e72c)

~~~diff
- 0061e6cc ["INT_ADD", "register:40f0:8", ["const:61e6cc:8", "const:4:8"]]
- 0061e6cc ["CALL", null, ["ram:48ccf8:8"]]
+ 0061e70c ["INT_ADD", "register:40f0:8", ["const:61e70c:8", "const:4:8"]]
+ 0061e70c ["CALL", null, ["ram:48cd38:8"]]
- 0061e6cc bytes 8bb9f997
+ 0061e70c bytes 8bb9f997
- 0061e6e0 ["INT_ADD", "register:40f0:8", ["const:61e6e0:8", "const:4:8"]]
- 0061e6e0 ["CALL", null, ["ram:47acf4:8"]]
+ 0061e720 ["INT_ADD", "register:40f0:8", ["const:61e720:8", "const:4:8"]]
+ 0061e720 ["CALL", null, ["ram:47ad34:8"]]
- 0061e6e0 bytes 8571f997
+ 0061e720 bytes 8571f997
- 0061e6ec ["INT_ADD", "register:40f0:8", ["const:61e6ec:8", "const:4:8"]]
- 0061e6ec ["CALL", null, ["callee:0047ce14:8"]]
+ 0061e72c ["INT_ADD", "register:40f0:8", ["const:61e72c:8", "const:4:8"]]
+ 0061e72c ["CALL", null, ["callee:0047ce14:8"]]
- 0061e6ec bytes ba79f997
+ 0061e72c bytes ba79f997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89105bbff2a2a1ce6a8898bcf98fd3f8"></a>

### [`0061eae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061eae8.md) → [`0061eb28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061eb28.md) FUN_0061eb28

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
      "definition_site": "0061eb3c",
      "incomplete_value": false,
      "site": "0061eb40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061eafc",
      "incomplete_value": false,
      "site": "0061eb00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:8c8:8"
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
      "0061eb40",
      "DATA",
      [
        "storage",
        "00c728c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061eb40",
      "DATA",
      [
        "storage",
        "00c72998",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061eaf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061eae8.md#insn-0061eaf4) · [`0061eafc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061eae8.md#insn-0061eafc)
- 新版 [`0061eb34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061eb28.md#insn-0061eb34) · [`0061eb3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061eb28.md#insn-0061eb3c)

~~~diff
- 0061eaf4 ["INT_ADD", "register:40f0:8", ["const:61eaf4:8", "const:4:8"]]
- 0061eaf4 ["CALL", null, ["callee:00c57f60:8"]]
+ 0061eb34 ["INT_ADD", "register:40f0:8", ["const:61eb34:8", "const:4:8"]]
+ 0061eb34 ["CALL", null, ["callee:00c57f60:8"]]
- 0061eaf4 bytes e7e41894
+ 0061eb34 bytes 0be51894
- 0061eafc ["COPY", "tmp:0:8", ["const:8c8:8"]]
- 0061eafc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061eafc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061eafc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061eb3c ["COPY", "tmp:0:8", ["const:998:8"]]
+ 0061eb3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061eb3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061eb3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061eafc bytes 08212391
+ 0061eb3c bytes 08612691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e981e09b35969248e82adc8707774419"></a>

### [`0061eb0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061eb0c.md) → [`0061eb4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061eb4c.md) FUN_0061eb4c

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
      "definition_site": "0061eb50",
      "incomplete_value": false,
      "site": "0061eb54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061eb10",
      "incomplete_value": false,
      "site": "0061eb14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:8c8:8"
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
      "0061eb54",
      "DATA",
      [
        "storage",
        "00c728c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061eb54",
      "DATA",
      [
        "storage",
        "00c72998",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061eb10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061eb0c.md#insn-0061eb10)
- 新版 [`0061eb50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061eb4c.md#insn-0061eb50)

~~~diff
- 0061eb10 ["COPY", "tmp:0:8", ["const:8c8:8"]]
- 0061eb10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061eb10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061eb10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061eb50 ["COPY", "tmp:0:8", ["const:998:8"]]
+ 0061eb50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061eb50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061eb50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061eb10 bytes 08212391
+ 0061eb50 bytes 08612691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-069591e534ce7e2074839ed7a6a91cd0"></a>

### [`0061eba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061eba8.md) → [`0061ebe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061ebe8.md) FUN_0061ebe8

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
      "definition_site": "0061ebfc",
      "incomplete_value": false,
      "site": "0061ec00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:a28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061ebbc",
      "incomplete_value": false,
      "site": "0061ebc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:958:8"
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
      "0061ec00",
      "DATA",
      [
        "storage",
        "00c72958",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061ec00",
      "DATA",
      [
        "storage",
        "00c72a28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061ebb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061eba8.md#insn-0061ebb4) · [`0061ebbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061eba8.md#insn-0061ebbc)
- 新版 [`0061ebf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061ebe8.md#insn-0061ebf4) · [`0061ebfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061ebe8.md#insn-0061ebfc)

~~~diff
- 0061ebb4 ["INT_ADD", "register:40f0:8", ["const:61ebb4:8", "const:4:8"]]
- 0061ebb4 ["CALL", null, ["callee:00c57f60:8"]]
+ 0061ebf4 ["INT_ADD", "register:40f0:8", ["const:61ebf4:8", "const:4:8"]]
+ 0061ebf4 ["CALL", null, ["callee:00c57f60:8"]]
- 0061ebb4 bytes b7e41894
+ 0061ebf4 bytes dbe41894
- 0061ebbc ["COPY", "tmp:0:8", ["const:958:8"]]
- 0061ebbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061ebbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061ebbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061ebfc ["COPY", "tmp:0:8", ["const:a28:8"]]
+ 0061ebfc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061ebfc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061ebfc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061ebbc bytes 08612591
+ 0061ebfc bytes 08a12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f915fa3f63b68ff61617f126eedcc26"></a>

### [`0061ebcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061ebcc.md) → [`0061ec0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061ec0c.md) FUN_0061ec0c

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
      "definition_site": "0061ec10",
      "incomplete_value": false,
      "site": "0061ec14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:a28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061ebd0",
      "incomplete_value": false,
      "site": "0061ebd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:958:8"
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
      "0061ec14",
      "DATA",
      [
        "storage",
        "00c72958",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061ec14",
      "DATA",
      [
        "storage",
        "00c72a28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0061ebd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061ebcc.md#insn-0061ebd0)
- 新版 [`0061ec10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061ec0c.md#insn-0061ec10)

~~~diff
- 0061ebd0 ["COPY", "tmp:0:8", ["const:958:8"]]
- 0061ebd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0061ebd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0061ebd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0061ec10 ["COPY", "tmp:0:8", ["const:a28:8"]]
+ 0061ec10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0061ec10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0061ec10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0061ebd0 bytes 08612591
+ 0061ec10 bytes 08a12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3475cb91ef90ff7407f9de152c86aa80"></a>

### [`0061edf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061edf4.md) → [`0061ee34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061ee34.md) FUN_0061ee34

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0061ec10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061ec10.md) [`0061edf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061edf4.md) · 呼出先 21件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)
- 新版 呼出元 2件 [`0061ec50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061ec50.md) [`0061ee34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061ee34.md) · 呼出先 21件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`00441d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441d2c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.93% / 新版 98.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0061efac",
      "incomplete_value": false,
      "site": "0061efb8",
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
      "definition_site": "0061ef6c",
      "incomplete_value": false,
      "site": "0061ef78",
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
      "definition_site": "0061f064",
      "incomplete_value": false,
      "site": "0061f06c",
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
      "definition_site": "0061f024",
      "incomplete_value": false,
      "site": "0061f02c",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0061f12c",
      "incomplete_value": false,
      "site": "0061f138",
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
      "definition_site": "0061f0ec",
      "incomplete_value": false,
      "site": "0061f0f8",
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
      "0061efac",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "0061f064",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ],
    [
      "0061f07c",
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
      "0061efac",
      "PARAM",
      [
        "storage",
        "002b7f93",
        null,
        null
      ]
    ],
    [
      "0061f064",
      "PARAM",
      [
        "storage",
        "002b5e27",
        null,
        null
      ]
    ],
    [
      "0061f07c",
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

- 旧版 [`0061ef78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061edf4.md#insn-0061ef78) · [`0061f02c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061edf4.md#insn-0061f02c) · [`0061f0f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061edf4.md#insn-0061f0f8)
- 新版 [`0061efb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061ee34.md#insn-0061efb8) · [`0061f06c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061ee34.md#insn-0061f06c) · [`0061f138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061ee34.md#insn-0061f138)

~~~diff
- 0061ef78 ["INT_ADD", "register:40f0:8", ["const:61ef78:8", "const:4:8"]]
- 0061ef78 ["CALL", null, ["callee:00441ed4:8"]]
+ 0061efb8 ["INT_ADD", "register:40f0:8", ["const:61efb8:8", "const:4:8"]]
+ 0061efb8 ["CALL", null, ["callee:00441ed4:8"]]
- 0061ef78 bytes c78bf897
+ 0061efb8 bytes c78bf897
- 0061f02c ["INT_ADD", "register:40f0:8", ["const:61f02c:8", "const:4:8"]]
- 0061f02c ["CALL", null, ["callee:00441ed4:8"]]
+ 0061f06c ["INT_ADD", "register:40f0:8", ["const:61f06c:8", "const:4:8"]]
+ 0061f06c ["CALL", null, ["callee:00441ed4:8"]]
- 0061f02c bytes 9a8bf897
+ 0061f06c bytes 9a8bf897
- 0061f0f8 ["INT_ADD", "register:40f0:8", ["const:61f0f8:8", "const:4:8"]]
- 0061f0f8 ["CALL", null, ["callee:00442834:8"]]
+ 0061f138 ["INT_ADD", "register:40f0:8", ["const:61f138:8", "const:4:8"]]
+ 0061f138 ["CALL", null, ["callee:00442834:8"]]
- 0061f0f8 bytes bf8df897
+ 0061f138 bytes bf8df897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ba51482c187e3b9c74645872492a4a3"></a>

### [`0061f9d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061f/0061f9d4.md) → [`0061fa14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061f/0061fa14.md) FUN_0061fa14

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0061edf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061e/0061edf4.md) [`0061f9d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061f/0061f9d4.md) · 呼出先 21件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)
- 新版 呼出元 2件 [`0061ee34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061e/0061ee34.md) [`0061fa14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061f/0061fa14.md) · 呼出先 21件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`00441d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441d2c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.82% / 新版 98.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0061fb8c",
      "incomplete_value": false,
      "site": "0061fb94",
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
      "definition_site": "0061fb4c",
      "incomplete_value": false,
      "site": "0061fb54",
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
      "definition_site": "0061fc40",
      "incomplete_value": true,
      "site": "0061fc48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4008:8"
          ],
          [
            "leaf",
            "const:e27:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0061fc00",
      "incomplete_value": true,
      "site": "0061fc08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4008:8"
          ],
          [
            "leaf",
            "const:de7:8"
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
      "definition_site": "0061fd0c",
      "incomplete_value": false,
      "site": "0061fd1c",
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
      "definition_site": "0061fccc",
      "incomplete_value": false,
      "site": "0061fcdc",
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
      "0061fb8c",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "0061fc40",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ],
    [
      "0061fc58",
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
      "0061fb8c",
      "PARAM",
      [
        "storage",
        "002b7f93",
        null,
        null
      ]
    ],
    [
      "0061fc40",
      "PARAM",
      [
        "storage",
        "002b5e27",
        null,
        null
      ]
    ],
    [
      "0061fc58",
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

- 旧版 [`0061fb54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061f/0061f9d4.md#insn-0061fb54) · [`0061fc08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061f/0061f9d4.md#insn-0061fc08) · [`0061fcdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061f/0061f9d4.md#insn-0061fcdc)
- 新版 [`0061fb94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061f/0061fa14.md#insn-0061fb94) · [`0061fc48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061f/0061fa14.md#insn-0061fc48) · [`0061fd1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061f/0061fa14.md#insn-0061fd1c)

~~~diff
- 0061fb54 ["INT_ADD", "register:40f0:8", ["const:61fb54:8", "const:4:8"]]
- 0061fb54 ["CALL", null, ["callee:00441ed4:8"]]
+ 0061fb94 ["INT_ADD", "register:40f0:8", ["const:61fb94:8", "const:4:8"]]
+ 0061fb94 ["CALL", null, ["callee:00441ed4:8"]]
- 0061fb54 bytes d088f897
+ 0061fb94 bytes d088f897
- 0061fc08 ["INT_ADD", "register:40f0:8", ["const:61fc08:8", "const:4:8"]]
- 0061fc08 ["CALL", null, ["callee:00441ed4:8"]]
+ 0061fc48 ["INT_ADD", "register:40f0:8", ["const:61fc48:8", "const:4:8"]]
+ 0061fc48 ["CALL", null, ["callee:00441ed4:8"]]
- 0061fc08 bytes a388f897
+ 0061fc48 bytes a388f897
- 0061fcdc ["INT_ADD", "register:40f0:8", ["const:61fcdc:8", "const:4:8"]]
- 0061fcdc ["CALL", null, ["callee:00442834:8"]]
+ 0061fd1c ["INT_ADD", "register:40f0:8", ["const:61fd1c:8", "const:4:8"]]
+ 0061fd1c ["CALL", null, ["callee:00442834:8"]]
- 0061fcdc bytes c68af897
+ 0061fd1c bytes c68af897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fd25f1c21e6f698a926ccc2940ed2a8"></a>

### [`00620430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00620/00620430.md) → [`00620470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00620/00620470.md) FUN_00620470

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0061f9d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0061f/0061f9d4.md) [`00620430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00620/00620430.md) · 呼出先 21件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)
- 新版 呼出元 2件 [`0061fa14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0061f/0061fa14.md) [`00620470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00620/00620470.md) · 呼出先 21件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`00441d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441d2c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.66% / 新版 98.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006205e0",
      "incomplete_value": false,
      "site": "006205e8",
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
      "definition_site": "006205a0",
      "incomplete_value": false,
      "site": "006205a8",
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
      "definition_site": "00620694",
      "incomplete_value": false,
      "site": "0062069c",
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
      "definition_site": "00620654",
      "incomplete_value": false,
      "site": "0062065c",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006206ac",
      "incomplete_value": false,
      "site": "006206bc",
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
      "definition_site": "0062066c",
      "incomplete_value": false,
      "site": "0062067c",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006205e0",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "00620694",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ],
    [
      "006206ac",
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
      "006205e0",
      "PARAM",
      [
        "storage",
        "002b7f93",
        null,
        null
      ]
    ],
    [
      "00620694",
      "PARAM",
      [
        "storage",
        "002b5e27",
        null,
        null
      ]
    ],
    [
      "006206ac",
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

- 旧版 [`006205a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00620/00620430.md#insn-006205a8) · [`0062065c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00620/00620430.md#insn-0062065c) · [`0062067c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00620/00620430.md#insn-0062067c)
- 新版 [`006205e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00620/00620470.md#insn-006205e8) · [`0062069c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00620/00620470.md#insn-0062069c) · [`006206bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00620/00620470.md#insn-006206bc)

~~~diff
- 006205a8 ["INT_ADD", "register:40f0:8", ["const:6205a8:8", "const:4:8"]]
- 006205a8 ["CALL", null, ["callee:00441ed4:8"]]
+ 006205e8 ["INT_ADD", "register:40f0:8", ["const:6205e8:8", "const:4:8"]]
+ 006205e8 ["CALL", null, ["callee:00441ed4:8"]]
- 006205a8 bytes 3b86f897
+ 006205e8 bytes 3b86f897
- 0062065c ["INT_ADD", "register:40f0:8", ["const:62065c:8", "const:4:8"]]
- 0062065c ["CALL", null, ["callee:00441ed4:8"]]
+ 0062069c ["INT_ADD", "register:40f0:8", ["const:62069c:8", "const:4:8"]]
+ 0062069c ["CALL", null, ["callee:00441ed4:8"]]
- 0062065c bytes 0e86f897
+ 0062069c bytes 0e86f897
- 0062067c ["INT_ADD", "register:40f0:8", ["const:62067c:8", "const:4:8"]]
- 0062067c ["CALL", null, ["callee:00442834:8"]]
+ 006206bc ["INT_ADD", "register:40f0:8", ["const:6206bc:8", "const:4:8"]]
+ 006206bc ["CALL", null, ["callee:00442834:8"]]
- 0062067c bytes 5e88f897
+ 006206bc bytes 5e88f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8bddb7b718c6909b6381dfece8f06f3"></a>

### [`00620f24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00620/00620f24.md) → [`00620f64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00620/00620f64.md) FUN_00620f64

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00620d30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00620/00620d30.md) [`00620f24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00620/00620f24.md) · 呼出先 21件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)
- 新版 呼出元 2件 [`00620d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00620/00620d70.md) [`00620f64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00620/00620f64.md) · 呼出先 21件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`00441d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441d2c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.94% / 新版 98.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0062119c",
      "incomplete_value": true,
      "site": "006211a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4008:8"
          ],
          [
            "leaf",
            "const:e27:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0062115c",
      "incomplete_value": true,
      "site": "00621164",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4008:8"
          ],
          [
            "leaf",
            "const:de7:8"
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
      "definition_site": "006211b4",
      "incomplete_value": false,
      "site": "006211c0",
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
      "definition_site": "00621174",
      "incomplete_value": false,
      "site": "00621180",
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
      "definition_site": "00621500",
      "incomplete_value": false,
      "site": "00621510",
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
            "const:d75:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006214c0",
      "incomplete_value": false,
      "site": "006214d0",
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
            "const:dc2:8"
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006210e4",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "0062119c",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ],
    [
      "006211b4",
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
      "006210e4",
      "PARAM",
      [
        "storage",
        "002b7f93",
        null,
        null
      ]
    ],
    [
      "0062119c",
      "PARAM",
      [
        "storage",
        "002b5e27",
        null,
        null
      ]
    ],
    [
      "006211b4",
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

- 旧版 [`00621164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00620/00620f24.md#insn-00621164) · [`00621180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00620/00620f24.md#insn-00621180) · [`00621490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00620/00620f24.md#insn-00621490)
- 新版 [`006211a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00620/00620f64.md#insn-006211a4) · [`006211c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00620/00620f64.md#insn-006211c0) · [`006214d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00620/00620f64.md#insn-006214d0)

~~~diff
- 00621164 ["INT_ADD", "register:40f0:8", ["const:621164:8", "const:4:8"]]
- 00621164 ["CALL", null, ["callee:00441ed4:8"]]
+ 006211a4 ["INT_ADD", "register:40f0:8", ["const:6211a4:8", "const:4:8"]]
+ 006211a4 ["CALL", null, ["callee:00441ed4:8"]]
- 00621164 bytes 4c83f897
+ 006211a4 bytes 4c83f897
- 00621180 ["INT_ADD", "register:40f0:8", ["const:621180:8", "const:4:8"]]
- 00621180 ["CALL", null, ["callee:00442834:8"]]
+ 006211c0 ["INT_ADD", "register:40f0:8", ["const:6211c0:8", "const:4:8"]]
+ 006211c0 ["CALL", null, ["callee:00442834:8"]]
- 00621180 bytes 9d85f897
+ 006211c0 bytes 9d85f897
- 00621490 ["INT_ADD", "register:40f0:8", ["const:621490:8", "const:4:8"]]
- 00621490 ["CALL", null, ["callee:00c57f60:8"]]
+ 006214d0 ["INT_ADD", "register:40f0:8", ["const:6214d0:8", "const:4:8"]]
+ 006214d0 ["CALL", null, ["callee:00c57f60:8"]]
- 00621490 bytes 80da1894
+ 006214d0 bytes a4da1894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad2bcf290a603c1fd8f82a9e257c69ae"></a>

### [`00621b10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00621/00621b10.md) → [`00621b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00621/00621b50.md) FUN_00621b50

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00620f24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00620/00620f24.md) [`00621b10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00621/00621b10.md) · 呼出先 21件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)
- 新版 呼出元 2件 [`00620f64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00620/00620f64.md) [`00621b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00621/00621b50.md) · 呼出先 21件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`00441d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441d2c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.81% / 新版 98.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00621d80",
      "incomplete_value": false,
      "site": "00621d88",
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
      "definition_site": "00621d40",
      "incomplete_value": false,
      "site": "00621d48",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00621d9c",
      "incomplete_value": false,
      "site": "00621da8",
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
      "definition_site": "00621d5c",
      "incomplete_value": false,
      "site": "00621d68",
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
      "definition_site": "00621e50",
      "incomplete_value": false,
      "site": "00621e5c",
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
      "definition_site": "00621e10",
      "incomplete_value": false,
      "site": "00621e1c",
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
      "00621cc8",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "00621d80",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ],
    [
      "00621d9c",
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
      "00621cc8",
      "PARAM",
      [
        "storage",
        "002b7f93",
        null,
        null
      ]
    ],
    [
      "00621d80",
      "PARAM",
      [
        "storage",
        "002b5e27",
        null,
        null
      ]
    ],
    [
      "00621d9c",
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

- 旧版 [`00621d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00621/00621b10.md#insn-00621d48) · [`00621d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00621/00621b10.md#insn-00621d68) · [`00621e1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00621/00621b10.md#insn-00621e1c)
- 新版 [`00621d88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00621/00621b50.md#insn-00621d88) · [`00621da8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00621/00621b50.md#insn-00621da8) · [`00621e5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00621/00621b50.md#insn-00621e5c)

~~~diff
- 00621d48 ["INT_ADD", "register:40f0:8", ["const:621d48:8", "const:4:8"]]
- 00621d48 ["CALL", null, ["callee:00441ed4:8"]]
+ 00621d88 ["INT_ADD", "register:40f0:8", ["const:621d88:8", "const:4:8"]]
+ 00621d88 ["CALL", null, ["callee:00441ed4:8"]]
- 00621d48 bytes 5380f897
+ 00621d88 bytes 5380f897
- 00621d68 ["INT_ADD", "register:40f0:8", ["const:621d68:8", "const:4:8"]]
- 00621d68 ["CALL", null, ["callee:00442834:8"]]
+ 00621da8 ["INT_ADD", "register:40f0:8", ["const:621da8:8", "const:4:8"]]
+ 00621da8 ["CALL", null, ["callee:00442834:8"]]
- 00621d68 bytes a382f897
+ 00621da8 bytes a382f897
- 00621e1c ["INT_ADD", "register:40f0:8", ["const:621e1c:8", "const:4:8"]]
- 00621e1c ["CALL", null, ["callee:00442834:8"]]
+ 00621e5c ["INT_ADD", "register:40f0:8", ["const:621e5c:8", "const:4:8"]]
+ 00621e5c ["CALL", null, ["callee:00442834:8"]]
- 00621e1c bytes 7682f897
+ 00621e5c bytes 7682f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f98bfb3b114c7d40d94bd88bfaf34f6"></a>

### [`00622560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00622/00622560.md) → [`006225a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00622/006225a0.md) FUN_006225a0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00621b10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00621/00621b10.md) [`00622560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00622/00622560.md) · 呼出先 21件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)
- 新版 呼出元 2件 [`00621b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00621/00621b50.md) [`006225a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00622/006225a0.md) · 呼出先 21件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`00441d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441d2c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.66% / 新版 98.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00622710",
      "incomplete_value": false,
      "site": "00622718",
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
      "definition_site": "006226d0",
      "incomplete_value": false,
      "site": "006226d8",
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
      "definition_site": "006227c4",
      "incomplete_value": true,
      "site": "006227cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4008:8"
          ],
          [
            "leaf",
            "const:e27:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00622784",
      "incomplete_value": true,
      "site": "0062278c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4008:8"
          ],
          [
            "leaf",
            "const:de7:8"
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
      "definition_site": "00622890",
      "incomplete_value": false,
      "site": "006228a0",
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
      "definition_site": "00622850",
      "incomplete_value": false,
      "site": "00622860",
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
      "00622710",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "006227c4",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ],
    [
      "006227dc",
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
      "00622710",
      "PARAM",
      [
        "storage",
        "002b7f93",
        null,
        null
      ]
    ],
    [
      "006227c4",
      "PARAM",
      [
        "storage",
        "002b5e27",
        null,
        null
      ]
    ],
    [
      "006227dc",
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

- 旧版 [`006226d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00622/00622560.md#insn-006226d8) · [`0062278c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00622/00622560.md#insn-0062278c) · [`00622860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00622/00622560.md#insn-00622860)
- 新版 [`00622718`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00622/006225a0.md#insn-00622718) · [`006227cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00622/006225a0.md#insn-006227cc) · [`006228a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00622/006225a0.md#insn-006228a0)

~~~diff
- 006226d8 ["INT_ADD", "register:40f0:8", ["const:6226d8:8", "const:4:8"]]
- 006226d8 ["CALL", null, ["callee:00441ed4:8"]]
+ 00622718 ["INT_ADD", "register:40f0:8", ["const:622718:8", "const:4:8"]]
+ 00622718 ["CALL", null, ["callee:00441ed4:8"]]
- 006226d8 bytes ef7df897
+ 00622718 bytes ef7df897
- 0062278c ["INT_ADD", "register:40f0:8", ["const:62278c:8", "const:4:8"]]
- 0062278c ["CALL", null, ["callee:00441ed4:8"]]
+ 006227cc ["INT_ADD", "register:40f0:8", ["const:6227cc:8", "const:4:8"]]
+ 006227cc ["CALL", null, ["callee:00441ed4:8"]]
- 0062278c bytes c27df897
+ 006227cc bytes c27df897
- 00622860 ["INT_ADD", "register:40f0:8", ["const:622860:8", "const:4:8"]]
- 00622860 ["CALL", null, ["callee:00442834:8"]]
+ 006228a0 ["INT_ADD", "register:40f0:8", ["const:6228a0:8", "const:4:8"]]
+ 006228a0 ["CALL", null, ["callee:00442834:8"]]
- 00622860 bytes e57ff897
+ 006228a0 bytes e57ff897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0658a2c87f7e32930ce88703f2d62d9a"></a>

### [`00622e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00622/00622e60.md) → [`00622ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00622/00622ea0.md) FUN_00622ea0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00622560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00622/00622560.md) [`00622e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00622/00622e60.md) [`00630284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00630/00630284.md) [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) · 呼出先 22件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)
- 新版 呼出元 4件 [`006225a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00622/006225a0.md) [`00622ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00622/00622ea0.md) [`006302c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00630/006302c4.md) [`0089e8d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089e/0089e8d4.md) · 呼出先 22件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`00441d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441d2c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.50% / 新版 98.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00622ffc",
      "incomplete_value": false,
      "site": "00623004",
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
      "definition_site": "00622fbc",
      "incomplete_value": false,
      "site": "00622fc4",
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
      "definition_site": "00623020",
      "incomplete_value": false,
      "site": "0062302c",
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
      "definition_site": "00622fe0",
      "incomplete_value": false,
      "site": "00622fec",
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
      "definition_site": "00623154",
      "incomplete_value": false,
      "site": "0062315c",
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
      "definition_site": "00623114",
      "incomplete_value": false,
      "site": "0062311c",
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
      "00622ffc",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "00623020",
      "PARAM",
      [
        "storage",
        "002c0ee9",
        null,
        "string"
      ]
    ],
    [
      "00623154",
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
      "00622ffc",
      "PARAM",
      [
        "storage",
        "002b7f93",
        null,
        null
      ]
    ],
    [
      "00623020",
      "PARAM",
      [
        "storage",
        "002c0f29",
        null,
        "string"
      ]
    ],
    [
      "00623154",
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

- 旧版 [`00622fc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00622/00622e60.md#insn-00622fc4) · [`00622fec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00622/00622e60.md#insn-00622fec) · [`0062311c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00622/00622e60.md#insn-0062311c)
- 新版 [`00623004`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00622/00622ea0.md#insn-00623004) · [`0062302c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00622/00622ea0.md#insn-0062302c) · [`0062315c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00622/00622ea0.md#insn-0062315c)

~~~diff
- 00622fc4 ["INT_ADD", "register:40f0:8", ["const:622fc4:8", "const:4:8"]]
- 00622fc4 ["CALL", null, ["callee:00441ed4:8"]]
+ 00623004 ["INT_ADD", "register:40f0:8", ["const:623004:8", "const:4:8"]]
+ 00623004 ["CALL", null, ["callee:00441ed4:8"]]
- 00622fc4 bytes b47bf897
+ 00623004 bytes b47bf897
- 00622fec ["INT_ADD", "register:40f0:8", ["const:622fec:8", "const:4:8"]]
- 00622fec ["CALL", null, ["callee:00442834:8"]]
+ 0062302c ["INT_ADD", "register:40f0:8", ["const:62302c:8", "const:4:8"]]
+ 0062302c ["CALL", null, ["callee:00442834:8"]]
- 00622fec bytes 027ef897
+ 0062302c bytes 027ef897
- 0062311c ["INT_ADD", "register:40f0:8", ["const:62311c:8", "const:4:8"]]
- 0062311c ["CALL", null, ["callee:00441ed4:8"]]
+ 0062315c ["INT_ADD", "register:40f0:8", ["const:62315c:8", "const:4:8"]]
+ 0062315c ["CALL", null, ["callee:00441ed4:8"]]
- 0062311c bytes 5e7bf897
+ 0062315c bytes 5e7bf897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62494baebe6f287eb8a357aa3aca2aae"></a>

### [`00623678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00623/00623678.md) → [`006236b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00623/006236b8.md) FUN_006236b8

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00611bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00611/00611bdc.md) [`00623678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00623/00623678.md) [`00625718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00625/00625718.md) · 呼出先 21件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)
- 新版 呼出元 3件 [`00611c1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00611/00611c1c.md) [`006236b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00623/006236b8.md) [`00625758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00625/00625758.md) · 呼出先 21件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`00441d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441d2c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.65% / 新版 98.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006238e8",
      "incomplete_value": false,
      "site": "006238f0",
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
      "definition_site": "006238a8",
      "incomplete_value": false,
      "site": "006238b0",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00623904",
      "incomplete_value": false,
      "site": "00623910",
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
      "definition_site": "006238c4",
      "incomplete_value": false,
      "site": "006238d0",
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
      "definition_site": "00623bc4",
      "incomplete_value": false,
      "site": "00623bd4",
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
            "const:d75:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00623b84",
      "incomplete_value": false,
      "site": "00623b94",
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
            "const:dc2:8"
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00623828",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "006238e8",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ],
    [
      "00623904",
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
      "00623828",
      "PARAM",
      [
        "storage",
        "002b7f93",
        null,
        null
      ]
    ],
    [
      "006238e8",
      "PARAM",
      [
        "storage",
        "002b5e27",
        null,
        null
      ]
    ],
    [
      "00623904",
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

- 旧版 [`006238b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00623/00623678.md#insn-006238b0) · [`006238d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00623/00623678.md#insn-006238d0) · [`00623b54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00623/00623678.md#insn-00623b54)
- 新版 [`006238f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00623/006236b8.md#insn-006238f0) · [`00623910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00623/006236b8.md#insn-00623910) · [`00623b94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00623/006236b8.md#insn-00623b94)

~~~diff
- 006238b0 ["INT_ADD", "register:40f0:8", ["const:6238b0:8", "const:4:8"]]
- 006238b0 ["CALL", null, ["callee:00441ed4:8"]]
+ 006238f0 ["INT_ADD", "register:40f0:8", ["const:6238f0:8", "const:4:8"]]
+ 006238f0 ["CALL", null, ["callee:00441ed4:8"]]
- 006238b0 bytes 7979f897
+ 006238f0 bytes 7979f897
- 006238d0 ["INT_ADD", "register:40f0:8", ["const:6238d0:8", "const:4:8"]]
- 006238d0 ["CALL", null, ["callee:00442834:8"]]
+ 00623910 ["INT_ADD", "register:40f0:8", ["const:623910:8", "const:4:8"]]
+ 00623910 ["CALL", null, ["callee:00442834:8"]]
- 006238d0 bytes c97bf897
+ 00623910 bytes c97bf897
- 00623b54 ["INT_ADD", "register:40f0:8", ["const:623b54:8", "const:4:8"]]
- 00623b54 ["CALL", null, ["callee:00c57f60:8"]]
+ 00623b94 ["INT_ADD", "register:40f0:8", ["const:623b94:8", "const:4:8"]]
+ 00623b94 ["CALL", null, ["callee:00c57f60:8"]]
- 00623b54 bytes cfd01894
+ 00623b94 bytes f3d01894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9c56cd59ec36fba0379f11bf183e9c7"></a>

### [`00623f68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00623/00623f68.md) → [`00623fa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00623/00623fa8.md) FUN_00623fa8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00623678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00623/00623678.md) [`00623f68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00623/00623f68.md) [`0093b770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093b/0093b770.md) [`009dd104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dd/009dd104.md) · 呼出先 22件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)
- 新版 呼出元 4件 [`006236b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00623/006236b8.md) [`00623fa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00623/00623fa8.md) [`0093b7c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0093b/0093b7c4.md) [`009dd158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dd/009dd158.md) · 呼出先 22件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`00441d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441d2c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.48% / 新版 98.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00624254",
      "incomplete_value": false,
      "site": "0062425c",
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
      "definition_site": "00624214",
      "incomplete_value": false,
      "site": "0062421c",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006242fc",
      "incomplete_value": false,
      "site": "00624308",
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
            "const:38f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006242bc",
      "incomplete_value": false,
      "site": "006242c8",
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
            "const:3eb:8"
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
      "definition_site": "00624518",
      "incomplete_value": false,
      "site": "00624528",
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
            "const:d75:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006244d8",
      "incomplete_value": false,
      "site": "006244e8",
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
            "const:dc2:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006240fc",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "00624120",
      "PARAM",
      [
        "storage",
        "002c0ee9",
        null,
        "string"
      ]
    ],
    [
      "00624254",
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
      "006240fc",
      "PARAM",
      [
        "storage",
        "002b7f93",
        null,
        null
      ]
    ],
    [
      "00624120",
      "PARAM",
      [
        "storage",
        "002c0f29",
        null,
        "string"
      ]
    ],
    [
      "00624254",
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

- 旧版 [`0062421c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00623/00623f68.md#insn-0062421c) · [`006242c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00623/00623f68.md#insn-006242c8) · [`006244e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00623/00623f68.md#insn-006244e8)
- 新版 [`0062425c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00623/00623fa8.md#insn-0062425c) · [`00624308`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00623/00623fa8.md#insn-00624308) · [`00624528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00623/00623fa8.md#insn-00624528)

~~~diff
- 0062421c ["INT_ADD", "register:40f0:8", ["const:62421c:8", "const:4:8"]]
- 0062421c ["CALL", null, ["callee:00441ed4:8"]]
+ 0062425c ["INT_ADD", "register:40f0:8", ["const:62425c:8", "const:4:8"]]
+ 0062425c ["CALL", null, ["callee:00441ed4:8"]]
- 0062421c bytes 1e77f897
+ 0062425c bytes 1e77f897
- 006242c8 ["INT_ADD", "register:40f0:8", ["const:6242c8:8", "const:4:8"]]
- 006242c8 ["CALL", null, ["callee:00441d2c:8"]]
+ 00624308 ["INT_ADD", "register:40f0:8", ["const:624308:8", "const:4:8"]]
+ 00624308 ["CALL", null, ["callee:00441d2c:8"]]
- 006242c8 bytes 8976f897
+ 00624308 bytes 8976f897
- 006244e8 ["INT_ADD", "register:40f0:8", ["const:6244e8:8", "const:4:8"]]
- 006244e8 ["CALL", null, ["callee:00c58150:8"]]
+ 00624528 ["INT_ADD", "register:40f0:8", ["const:624528:8", "const:4:8"]]
+ 00624528 ["CALL", null, ["callee:00c58150:8"]]
- 006244e8 bytes e6ce1894
+ 00624528 bytes 0acf1894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a2318c711dbc61b119097911816b5f4"></a>

### [`0062476c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00624/0062476c.md) → [`006247ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00624/006247ac.md) FUN_006247ac

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
      "definition_site": "006247c0",
      "incomplete_value": false,
      "site": "006247c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:aa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00624780",
      "incomplete_value": false,
      "site": "00624784",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:9d8:8"
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
      "006247c4",
      "DATA",
      [
        "storage",
        "00c729d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006247c4",
      "DATA",
      [
        "storage",
        "00c72aa8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00624778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00624/0062476c.md#insn-00624778) · [`00624780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00624/0062476c.md#insn-00624780)
- 新版 [`006247b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00624/006247ac.md#insn-006247b8) · [`006247c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00624/006247ac.md#insn-006247c0)

~~~diff
- 00624778 ["INT_ADD", "register:40f0:8", ["const:624778:8", "const:4:8"]]
- 00624778 ["CALL", null, ["callee:00c57f60:8"]]
+ 006247b8 ["INT_ADD", "register:40f0:8", ["const:6247b8:8", "const:4:8"]]
+ 006247b8 ["CALL", null, ["callee:00c57f60:8"]]
- 00624778 bytes c6cd1894
+ 006247b8 bytes eacd1894
- 00624780 ["COPY", "tmp:0:8", ["const:9d8:8"]]
- 00624780 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00624780 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00624780 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006247c0 ["COPY", "tmp:0:8", ["const:aa8:8"]]
+ 006247c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006247c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006247c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00624780 bytes 08612791
+ 006247c0 bytes 08a12a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a17447dab436a616203c07601c7a44b0"></a>

### [`00624790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00624/00624790.md) → [`006247d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00624/006247d0.md) FUN_006247d0

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
      "definition_site": "006247d4",
      "incomplete_value": false,
      "site": "006247d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:aa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00624794",
      "incomplete_value": false,
      "site": "00624798",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c72000:8"
          ],
          [
            "leaf",
            "const:9d8:8"
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
      "006247d8",
      "DATA",
      [
        "storage",
        "00c729d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006247d8",
      "DATA",
      [
        "storage",
        "00c72aa8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00624794`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00624/00624790.md#insn-00624794)
- 新版 [`006247d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00624/006247d0.md#insn-006247d4)

~~~diff
- 00624794 ["COPY", "tmp:0:8", ["const:9d8:8"]]
- 00624794 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00624794 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00624794 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006247d4 ["COPY", "tmp:0:8", ["const:aa8:8"]]
+ 006247d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006247d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006247d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00624794 bytes 08612791
+ 006247d4 bytes 08a12a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81edbc1d33ef077795110dc7c4782c3c"></a>

### [`00624cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00624/00624cbc.md) → [`00624cfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00624/00624cfc.md) FUN_00624cfc

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00624b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00624/00624b6c.md) [`00624cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00624/00624cbc.md) · 呼出先 21件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)
- 新版 呼出元 2件 [`00624bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00624/00624bac.md) [`00624cfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00624/00624cfc.md) · 呼出先 21件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`00441d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441d2c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.82% / 新版 98.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00624f28",
      "incomplete_value": false,
      "site": "00624f30",
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
      "definition_site": "00624ee8",
      "incomplete_value": false,
      "site": "00624ef0",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00625258",
      "incomplete_value": false,
      "site": "00625264",
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
            "const:d75:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00625218",
      "incomplete_value": false,
      "site": "00625224",
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
            "const:dc2:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006253cc",
      "incomplete_value": false,
      "site": "006253d8",
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
            "const:38f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0062538c",
      "incomplete_value": false,
      "site": "00625398",
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
            "const:3eb:8"
          ]
        ]
      ]
    },
    "ordinal": 31,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00624e74",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "00624f28",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ],
    [
      "00624f40",
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
      "00624e74",
      "PARAM",
      [
        "storage",
        "002b7f93",
        null,
        null
      ]
    ],
    [
      "00624f28",
      "PARAM",
      [
        "storage",
        "002b5e27",
        null,
        null
      ]
    ],
    [
      "00624f40",
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

- 旧版 [`00624ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00624/00624cbc.md#insn-00624ef0) · [`00625224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00624/00624cbc.md#insn-00625224) · [`00625398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00624/00624cbc.md#insn-00625398)
- 新版 [`00624f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00624/00624cfc.md#insn-00624f30) · [`00625264`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00624/00624cfc.md#insn-00625264) · [`006253d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00624/00624cfc.md#insn-006253d8)

~~~diff
- 00624ef0 ["INT_ADD", "register:40f0:8", ["const:624ef0:8", "const:4:8"]]
- 00624ef0 ["CALL", null, ["callee:00441ed4:8"]]
+ 00624f30 ["INT_ADD", "register:40f0:8", ["const:624f30:8", "const:4:8"]]
+ 00624f30 ["CALL", null, ["callee:00441ed4:8"]]
- 00624ef0 bytes e973f897
+ 00624f30 bytes e973f897
- 00625224 ["INT_ADD", "register:40f0:8", ["const:625224:8", "const:4:8"]]
- 00625224 ["CALL", null, ["callee:00c58150:8"]]
+ 00625264 ["INT_ADD", "register:40f0:8", ["const:625264:8", "const:4:8"]]
+ 00625264 ["CALL", null, ["callee:00c58150:8"]]
- 00625224 bytes 97cb1894
+ 00625264 bytes bbcb1894
- 00625398 ["INT_ADD", "register:40f0:8", ["const:625398:8", "const:4:8"]]
- 00625398 ["CALL", null, ["callee:00441d2c:8"]]
+ 006253d8 ["INT_ADD", "register:40f0:8", ["const:6253d8:8", "const:4:8"]]
+ 006253d8 ["CALL", null, ["callee:00441d2c:8"]]
- 00625398 bytes 5572f897
+ 006253d8 bytes 5572f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d813acfdb5d62c90bcd4cc556fab109"></a>

### [`00625718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00625/00625718.md) → [`00625758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00625/00625758.md) FUN_00625758

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00624cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00624/00624cbc.md) [`00625718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00625/00625718.md) · 呼出先 23件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)
- 新版 呼出元 2件 [`00624cfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00624/00624cfc.md) [`00625758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00625/00625758.md) · 呼出先 23件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440fb0.md) [`00441d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441d2c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.85% / 新版 98.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006258b8",
      "incomplete_value": false,
      "site": "006258c0",
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
      "definition_site": "00625878",
      "incomplete_value": false,
      "site": "00625880",
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
      "definition_site": "00625974",
      "incomplete_value": false,
      "site": "0062597c",
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
      "definition_site": "00625934",
      "incomplete_value": false,
      "site": "0062593c",
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
      "definition_site": "0062598c",
      "incomplete_value": false,
      "site": "00625998",
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
      "definition_site": "0062594c",
      "incomplete_value": false,
      "site": "00625958",
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
      "006258b8",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "00625974",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ],
    [
      "0062598c",
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
      "006258b8",
      "PARAM",
      [
        "storage",
        "002b7f93",
        null,
        null
      ]
    ],
    [
      "00625974",
      "PARAM",
      [
        "storage",
        "002b5e27",
        null,
        null
      ]
    ],
    [
      "0062598c",
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

- 旧版 [`00625880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00625/00625718.md#insn-00625880) · [`0062593c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00625/00625718.md#insn-0062593c) · [`00625958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00625/00625718.md#insn-00625958)
- 新版 [`006258c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00625/00625758.md#insn-006258c0) · [`0062597c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00625/00625758.md#insn-0062597c) · [`00625998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00625/00625758.md#insn-00625998)

~~~diff
- 00625880 ["INT_ADD", "register:40f0:8", ["const:625880:8", "const:4:8"]]
- 00625880 ["CALL", null, ["callee:00441ed4:8"]]
+ 006258c0 ["INT_ADD", "register:40f0:8", ["const:6258c0:8", "const:4:8"]]
+ 006258c0 ["CALL", null, ["callee:00441ed4:8"]]
- 00625880 bytes 8571f897
+ 006258c0 bytes 8571f897
- 0062593c ["INT_ADD", "register:40f0:8", ["const:62593c:8", "const:4:8"]]
- 0062593c ["CALL", null, ["callee:00441ed4:8"]]
+ 0062597c ["INT_ADD", "register:40f0:8", ["const:62597c:8", "const:4:8"]]
+ 0062597c ["CALL", null, ["callee:00441ed4:8"]]
- 0062593c bytes 5671f897
+ 0062597c bytes 5671f897
- 00625958 ["INT_ADD", "register:40f0:8", ["const:625958:8", "const:4:8"]]
- 00625958 ["CALL", null, ["callee:00442834:8"]]
+ 00625998 ["INT_ADD", "register:40f0:8", ["const:625998:8", "const:4:8"]]
+ 00625998 ["CALL", null, ["callee:00442834:8"]]
- 00625958 bytes a773f897
+ 00625998 bytes a773f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

