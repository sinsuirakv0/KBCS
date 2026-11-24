# v16.0.1 → v16.0.2 · 最優先の変更候補 (11)

[一覧の目次](README.md)

<a id="compare-08f520f866d2846d07c931992844fd74"></a>

### [`004fcb30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fc/004fcb30.md) → [`004fcb70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fc/004fcb70.md) _ZN5Botan18timespec_to_u32bitERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 12件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 12件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.51% / 新版 98.51%

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
      "definition_site": "004fcd38",
      "incomplete_value": false,
      "site": "004fcd44",
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
            "const:e45:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fccf8",
      "incomplete_value": false,
      "site": "004fcd04",
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
            "const:e14:8"
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
      "definition_site": "004fcd74",
      "incomplete_value": true,
      "site": "004fcd80",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fcd34",
      "incomplete_value": true,
      "site": "004fcd40",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004fcd70",
      "incomplete_value": false,
      "site": "004fcd80",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004fcd30",
      "incomplete_value": false,
      "site": "004fcd40",
      "value": [
        "leaf",
        "const:535868:8"
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
      "004fcd38",
      "PARAM",
      [
        "storage",
        "002b4e14",
        null,
        "string"
      ]
    ],
    [
      "004fcd70",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004fcd74",
      "READ",
      [
        "storage",
        "00c9ad50",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004fcd38",
      "PARAM",
      [
        "storage",
        "002b4e45",
        null,
        "string"
      ]
    ],
    [
      "004fcd70",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004fcd74",
      "READ",
      [
        "storage",
        "00c9ae20",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fcd04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fc/004fcb30.md#insn-004fcd04) · [`004fcd40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fc/004fcb30.md#insn-004fcd40) · [`004fcbd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fc/004fcb30.md#insn-004fcbd4)
- 新版 [`004fcd44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fc/004fcb70.md#insn-004fcd44) · [`004fcd80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fc/004fcb70.md#insn-004fcd80) · [`004fcc14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fc/004fcb70.md#insn-004fcc14)

~~~diff
- 004fcd04 ["INT_ADD", "register:40f0:8", ["const:4fcd04:8", "const:4:8"]]
- 004fcd04 ["CALL", null, ["callee:00c58180:8"]]
+ 004fcd44 ["INT_ADD", "register:40f0:8", ["const:4fcd44:8", "const:4:8"]]
+ 004fcd44 ["CALL", null, ["callee:00c58180:8"]]
- 004fcd04 bytes eb6c1d94
+ 004fcd44 bytes 0f6d1d94
- 004fcd40 ["INT_ADD", "register:40f0:8", ["const:4fcd40:8", "const:4:8"]]
- 004fcd40 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004fcd80 ["INT_ADD", "register:40f0:8", ["const:4fcd80:8", "const:4:8"]]
+ 004fcd80 ["CALL", null, ["callee:00c57fe0:8"]]
- 004fcd40 bytes 746c1d94
+ 004fcd80 bytes 986c1d94
- 004fcbd4 ["INT_ADD", "register:40f0:8", ["const:4fcbd4:8", "const:4:8"]]
- 004fcbd4 ["CALL", null, ["callee:00c57f60:8"]]
+ 004fcc14 ["INT_ADD", "register:40f0:8", ["const:4fcc14:8", "const:4:8"]]
+ 004fcc14 ["CALL", null, ["callee:00c57f60:8"]]
- 004fcbd4 bytes af6c1d94
+ 004fcc14 bytes d36c1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-941ed445288c67d2ae896fbc7a9ee46f"></a>

### [`004fcda8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fc/004fcda8.md) → [`004fcde8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fc/004fcde8.md) _ZN5Botan13split_on_predERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEENS0_8functionIFbcEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58fb0.md) · 呼出先 11件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00540d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540d7c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00c59080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59080.md) · 呼出先 11件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00540dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540dbc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.68% / 新版 98.68%

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
      "definition_site": "004fcff8",
      "incomplete_value": false,
      "site": "004fd004",
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
            "const:7c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fcfb8",
      "incomplete_value": false,
      "site": "004fcfc4",
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
            "const:81c:8"
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
      "definition_site": "004fd034",
      "incomplete_value": true,
      "site": "004fd040",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fcff4",
      "incomplete_value": true,
      "site": "004fd000",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004fd030",
      "incomplete_value": false,
      "site": "004fd040",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004fcff0",
      "incomplete_value": false,
      "site": "004fd000",
      "value": [
        "leaf",
        "const:535868:8"
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
      "004fcff8",
      "PARAM",
      [
        "storage",
        "002ad81c",
        null,
        "string"
      ]
    ],
    [
      "004fd030",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004fd034",
      "READ",
      [
        "storage",
        "00c9ad30",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004fcff8",
      "PARAM",
      [
        "storage",
        "002ad7c0",
        null,
        "string"
      ]
    ],
    [
      "004fd030",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004fd034",
      "READ",
      [
        "storage",
        "00c9ae00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fcfc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fc/004fcda8.md#insn-004fcfc4) · [`004fd000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fc/004fcda8.md#insn-004fd000) · [`004fce20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fc/004fcda8.md#insn-004fce20)
- 新版 [`004fd004`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fc/004fcde8.md#insn-004fd004) · [`004fd040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fc/004fcde8.md#insn-004fd040) · [`004fce60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fc/004fcde8.md#insn-004fce60)

~~~diff
- 004fcfc4 ["INT_ADD", "register:40f0:8", ["const:4fcfc4:8", "const:4:8"]]
- 004fcfc4 ["CALL", null, ["callee:00c58180:8"]]
+ 004fd004 ["INT_ADD", "register:40f0:8", ["const:4fd004:8", "const:4:8"]]
+ 004fd004 ["CALL", null, ["callee:00c58180:8"]]
- 004fcfc4 bytes 3b6c1d94
+ 004fd004 bytes 5f6c1d94
- 004fd000 ["INT_ADD", "register:40f0:8", ["const:4fd000:8", "const:4:8"]]
- 004fd000 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004fd040 ["INT_ADD", "register:40f0:8", ["const:4fd040:8", "const:4:8"]]
+ 004fd040 ["CALL", null, ["callee:00c57fe0:8"]]
- 004fd000 bytes c46b1d94
+ 004fd040 bytes e86b1d94
- 004fce20 ["INT_ADD", "register:40f0:8", ["const:4fce20:8", "const:4:8"]]
- 004fce20 ["CALL", null, ["callee:00c586d0:8"]]
+ 004fce60 ["INT_ADD", "register:40f0:8", ["const:4fce60:8", "const:4:8"]]
+ 004fce60 ["CALL", null, ["callee:00c586d0:8"]]
- 004fce20 bytes f86d1d94
+ 004fce60 bytes 1c6e1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc4208b3fad11f4ffc21086776d1328f"></a>

### [`004fd34c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fd/004fd34c.md) → [`004fd38c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fd/004fd38c.md) _ZN5Botan14string_to_ipv4ERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59900.md) · 呼出先 11件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00547b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547b6c.md) [`00547b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547b70.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00c599d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c599d0.md) · 呼出先 11件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00547bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00547/00547bac.md) [`00547bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00547/00547bb0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.28% / 新版 95.28%

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
      "definition_site": "004fd3b0",
      "incomplete_value": false,
      "site": "004fd3c4",
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
            "const:780:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fd370",
      "incomplete_value": false,
      "site": "004fd384",
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
            "const:6b0:8"
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
      "definition_site": "004fd4dc",
      "incomplete_value": false,
      "site": "004fd4e8",
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
            "const:baf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fd49c",
      "incomplete_value": false,
      "site": "004fd4a8",
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
            "const:b7e:8"
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
      "definition_site": "004fd518",
      "incomplete_value": true,
      "site": "004fd524",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fd4d8",
      "incomplete_value": true,
      "site": "004fd4e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004fd3c4",
      "DATA",
      [
        "storage",
        "00c6a6b0",
        null,
        "undefined *"
      ]
    ],
    [
      "004fd400",
      "READ",
      [
        "storage",
        "00c6a6d0",
        null,
        "pointer"
      ]
    ],
    [
      "004fd400",
      "READ",
      [
        "storage",
        "00c6a6d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004fd3c4",
      "DATA",
      [
        "storage",
        "00c6a780",
        null,
        "undefined *"
      ]
    ],
    [
      "004fd400",
      "READ",
      [
        "storage",
        "00c6a7a0",
        null,
        "pointer"
      ]
    ],
    [
      "004fd400",
      "READ",
      [
        "storage",
        "00c6a7a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fd3c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fd/004fd34c.md#insn-004fd3c4) · [`004fd4a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fd/004fd34c.md#insn-004fd4a8) · [`004fd4e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fd/004fd34c.md#insn-004fd4e4)
- 新版 [`004fd404`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fd/004fd38c.md#insn-004fd404) · [`004fd4e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fd/004fd38c.md#insn-004fd4e8) · [`004fd524`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fd/004fd38c.md#insn-004fd524)

~~~diff
- 004fd3c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 004fd3c4 ["INT_ADD", "register:40f0:8", ["const:4fd3c4:8", "const:4:8"]]
- 004fd3c4 ["CALLIND", null, ["register:0:8"]]
+ 004fd404 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004fd404 ["INT_ADD", "register:40f0:8", ["const:4fd404:8", "const:4:8"]]
+ 004fd404 ["CALLIND", null, ["register:0:8"]]
- 004fd3c4 bytes 00013fd6
+ 004fd404 bytes 00013fd6
- 004fd4a8 ["INT_ADD", "register:40f0:8", ["const:4fd4a8:8", "const:4:8"]]
- 004fd4a8 ["CALL", null, ["callee:00c58180:8"]]
+ 004fd4e8 ["INT_ADD", "register:40f0:8", ["const:4fd4e8:8", "const:4:8"]]
+ 004fd4e8 ["CALL", null, ["callee:00c58180:8"]]
- 004fd4a8 bytes 026b1d94
+ 004fd4e8 bytes 266b1d94
- 004fd4e4 ["INT_ADD", "register:40f0:8", ["const:4fd4e4:8", "const:4:8"]]
- 004fd4e4 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004fd524 ["INT_ADD", "register:40f0:8", ["const:4fd524:8", "const:4:8"]]
+ 004fd524 ["CALL", null, ["callee:00c57fe0:8"]]
- 004fd4e4 bytes 8b6a1d94
+ 004fd524 bytes af6a1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-537ee8e56deb96685d13553fe3981ee2"></a>

### [`004fd97c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fd/004fd97c.md) → [`004fd9bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fd/004fd9bc.md) _ZN5Botan19host_wildcard_matchERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEES8_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59920.md) · 呼出先 15件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440b00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440b00.md) [`00441dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441dc0.md) [`00441e94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441e94.md)
- 新版 呼出元 1件 [`00c599f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c599f0.md) · 呼出先 15件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440b40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440b40.md) [`00441e00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441e00.md) [`00441ed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441ed4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.42% / 新版 99.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004fde34",
      "incomplete_value": false,
      "site": "004fde40",
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
            "const:3ca:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fddf4",
      "incomplete_value": false,
      "site": "004fde00",
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
            "const:38a:8"
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
      "definition_site": "004fde88",
      "incomplete_value": false,
      "site": "004fde94",
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
      "definition_site": "004fde48",
      "incomplete_value": false,
      "site": "004fde54",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004fdf08",
      "incomplete_value": false,
      "site": "004fdf10",
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
      "definition_site": "004fdec8",
      "incomplete_value": false,
      "site": "004fded0",
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
      "004fde34",
      "PARAM",
      [
        "storage",
        "002b738a",
        null,
        null
      ]
    ],
    [
      "004fde88",
      "PARAM",
      [
        "storage",
        "002a63ea",
        null,
        "undefined1"
      ]
    ],
    [
      "004fdf08",
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
      "004fde34",
      "PARAM",
      [
        "storage",
        "002b73ca",
        null,
        null
      ]
    ],
    [
      "004fde88",
      "PARAM",
      [
        "storage",
        "002a638e",
        null,
        "undefined1"
      ]
    ],
    [
      "004fdf08",
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

- 旧版 [`004fddc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fd/004fd97c.md#insn-004fddc0) · [`004fde00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fd/004fd97c.md#insn-004fde00) · [`004fde54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fd/004fd97c.md#insn-004fde54)
- 新版 [`004fde00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fd/004fd9bc.md#insn-004fde00) · [`004fde40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fd/004fd9bc.md#insn-004fde40) · [`004fde94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fd/004fd9bc.md#insn-004fde94)

~~~diff
- 004fddc0 ["INT_ADD", "register:40f0:8", ["const:4fddc0:8", "const:4:8"]]
- 004fddc0 ["CALL", null, ["callee:00441e00:8"]]
+ 004fde00 ["INT_ADD", "register:40f0:8", ["const:4fde00:8", "const:4:8"]]
+ 004fde00 ["CALL", null, ["callee:00441e00:8"]]
- 004fddc0 bytes 0010fd97
+ 004fde00 bytes 0010fd97
- 004fde00 ["INT_ADD", "register:40f0:8", ["const:4fde00:8", "const:4:8"]]
- 004fde00 ["CALL", null, ["callee:00441ed4:8"]]
+ 004fde40 ["INT_ADD", "register:40f0:8", ["const:4fde40:8", "const:4:8"]]
+ 004fde40 ["CALL", null, ["callee:00441ed4:8"]]
- 004fde00 bytes 2510fd97
+ 004fde40 bytes 2510fd97
- 004fde54 ["INT_ADD", "register:40f0:8", ["const:4fde54:8", "const:4:8"]]
- 004fde54 ["CALL", null, ["callee:0043de18:8"]]
+ 004fde94 ["INT_ADD", "register:40f0:8", ["const:4fde94:8", "const:4:8"]]
+ 004fde94 ["CALL", null, ["callee:0043de18:8"]]
- 004fde54 bytes e1fffc97
+ 004fde94 bytes e1fffc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb9c6f52d29be4fec9a31ec2b65453b8"></a>

### [`004fe428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fe/004fe428.md) → [`004fe468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fe/004fe468.md) _ZN5Botan8read_cfgERNSt6__ndk113basic_istreamIcNS0_11char_traitsIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 23件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`00494c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494c7c.md) [`004a684c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a684c.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md)
- 新版 呼出元 0件  · 呼出先 23件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`00494cbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494cbc.md) [`004a688c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a688c.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.55% / 新版 98.55%

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
      "definition_site": "004fe86c",
      "incomplete_value": false,
      "site": "004fe870",
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
      "definition_site": "004fe82c",
      "incomplete_value": false,
      "site": "004fe830",
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
    "ordinal": 20,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004fe8c8",
      "incomplete_value": false,
      "site": "004fe8d4",
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
            "const:555:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fe888",
      "incomplete_value": false,
      "site": "004fe894",
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
            "const:5b1:8"
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
      "definition_site": "004fe8dc",
      "incomplete_value": false,
      "site": "004fe8e4",
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
            "const:8b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fe89c",
      "incomplete_value": false,
      "site": "004fe8a4",
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
            "const:d8:8"
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
      "004fe520",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      "004fe554",
      "PARAM",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "004fe86c",
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
      "004fe520",
      "READ",
      [
        "storage",
        "00c9ad00",
        null,
        "pointer"
      ]
    ],
    [
      "004fe554",
      "PARAM",
      [
        "storage",
        "01127f18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "004fe86c",
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

- 旧版 [`004fe830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fe/004fe428.md#insn-004fe830) · [`004fe870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fe/004fe428.md#insn-004fe870) · [`004fe894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fe/004fe428.md#insn-004fe894)
- 新版 [`004fe870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fe/004fe468.md#insn-004fe870) · [`004fe8b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fe/004fe468.md#insn-004fe8b0) · [`004fe8d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fe/004fe468.md#insn-004fe8d4)

~~~diff
- 004fe830 ["INT_ADD", "register:40f0:8", ["const:4fe830:8", "const:4:8"]]
- 004fe830 ["CALL", null, ["callee:00494cbc:8"]]
+ 004fe870 ["INT_ADD", "register:40f0:8", ["const:4fe870:8", "const:4:8"]]
+ 004fe870 ["CALL", null, ["callee:00494cbc:8"]]
- 004fe830 bytes 1359fe97
+ 004fe870 bytes 1359fe97
- 004fe870 ["INT_ADD", "register:40f0:8", ["const:4fe870:8", "const:4:8"]]
- 004fe870 ["CALL", null, ["callee:00c57f80:8"]]
+ 004fe8b0 ["INT_ADD", "register:40f0:8", ["const:4fe8b0:8", "const:4:8"]]
+ 004fe8b0 ["CALL", null, ["callee:00c57f80:8"]]
- 004fe870 bytes 90651d94
+ 004fe8b0 bytes b4651d94
- 004fe894 ["INT_ADD", "register:40f0:8", ["const:4fe894:8", "const:4:8"]]
- 004fe894 ["CALL", null, ["callee:00c58180:8"]]
+ 004fe8d4 ["INT_ADD", "register:40f0:8", ["const:4fe8d4:8", "const:4:8"]]
+ 004fe8d4 ["CALL", null, ["callee:00c58180:8"]]
- 004fe894 bytes 07661d94
+ 004fe8d4 bytes 2b661d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7bcfc793da440c63c5fda4c59e282f5"></a>

### [`004feb18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fe/004feb18.md) → [`004feb58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fe/004feb58.md) _ZN5Botan18short_version_cstrEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "004feb5c",
      "incomplete_value": false,
      "site": "004feb60",
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
            "const:9c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004feb1c",
      "incomplete_value": false,
      "site": "004feb20",
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
            "const:a1c:8"
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
      "004feb5c",
      "DATA",
      [
        "storage",
        "002afa1c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004feb5c",
      "DATA",
      [
        "storage",
        "002af9c0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004feb1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fe/004feb18.md#insn-004feb1c)
- 新版 [`004feb5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fe/004feb58.md#insn-004feb5c)

~~~diff
- 004feb1c ["COPY", "tmp:0:8", ["const:a1c:8"]]
- 004feb1c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004feb1c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004feb1c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004feb5c ["COPY", "tmp:0:8", ["const:9c0:8"]]
+ 004feb5c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004feb5c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004feb5c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004feb1c bytes 00702891
+ 004feb5c bytes 00002791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f9bcfc20baf0cf8df1bc43195e5218a"></a>

### [`004feb24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fe/004feb24.md) → [`004feb64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fe/004feb64.md) _ZN5Botan12version_cstrEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "004feb68",
      "incomplete_value": false,
      "site": "004feb6c",
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
            "const:57a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004feb28",
      "incomplete_value": false,
      "site": "004feb2c",
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
            "const:5ce:8"
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
      "004feb68",
      "DATA",
      [
        "storage",
        "002bc5ce",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004feb68",
      "DATA",
      [
        "storage",
        "002bc57a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004feb28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fe/004feb24.md#insn-004feb28)
- 新版 [`004feb68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fe/004feb64.md#insn-004feb68)

~~~diff
- 004feb28 ["COPY", "tmp:0:8", ["const:5ce:8"]]
- 004feb28 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004feb28 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004feb28 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004feb68 ["COPY", "tmp:0:8", ["const:57a:8"]]
+ 004feb68 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004feb68 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004feb68 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004feb28 bytes 00381791
+ 004feb68 bytes 00e81591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3c7d44ec27e5ee865d6d000053fedfb"></a>

### [`004febdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fe/004febdc.md) → [`004fec1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fe/004fec1c.md) _ZN5Botan21runtime_version_checkEjjj

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 10件 [`004594d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fa0.md) [`00c57fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00459510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459510.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58070.md) [`00c58080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58080.md)

変更の種類 call_argument_candidate, constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 89.36% / 新版 89.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fec64",
      "incomplete_value": true,
      "site": "004fec74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004fec24",
      "incomplete_value": true,
      "site": "004fec34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004fec6c",
      "incomplete_value": true,
      "site": "004fec7c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004fec2c",
      "incomplete_value": true,
      "site": "004fec3c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004fec84",
      "incomplete_value": true,
      "site": "004fec84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_SUB",
              [
                "leaf",
                "const:28:8"
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
      "definition_site": "004fec44",
      "incomplete_value": true,
      "site": "004fec44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_SUB",
              [
                "leaf",
                "const:28:8"
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
      "unmatched:004fec14",
      "READ",
      [
        "storage",
        "00c9abb8",
        null,
        "pointer"
      ]
    ],
    [
      "004fec6c",
      "READ",
      [
        "storage",
        "00c93208",
        null,
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "004fec6c",
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
      "004fec50",
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      "004fec6c",
      "READ",
      [
        "storage",
        "00c932d8",
        null,
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "004fec6c",
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

- 旧版 [`004fec7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fe/004febdc.md#insn-004fec7c) · [`004fecc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fe/004febdc.md#insn-004fecc4) · [`004fed00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fe/004febdc.md#insn-004fed00)
- 新版 [`004fecbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fe/004fec1c.md#insn-004fecbc) · [`004fed04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fe/004fec1c.md#insn-004fed04) · [`004fed40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fe/004fec1c.md#insn-004fed40)

~~~diff
- 004fec7c ["INT_ADD", "register:40f0:8", ["const:4fec7c:8", "const:4:8"]]
- 004fec7c ["CALL", null, ["callee:00c582c0:8"]]
+ 004fecbc ["INT_ADD", "register:40f0:8", ["const:4fecbc:8", "const:4:8"]]
+ 004fecbc ["CALL", null, ["callee:00c582c0:8"]]
- 004fec7c bytes 5d651d94
+ 004fecbc bytes 81651d94
- 004fecc4 ["INT_ADD", "register:40f0:8", ["const:4fecc4:8", "const:4:8"]]
- 004fecc4 ["CALL", null, ["callee:00459510:8"]]
+ 004fed04 ["INT_ADD", "register:40f0:8", ["const:4fed04:8", "const:4:8"]]
+ 004fed04 ["CALL", null, ["callee:00459510:8"]]
- 004fecc4 bytes 036afd97
+ 004fed04 bytes 036afd97
- 004fed00 ["INT_ADD", "register:40f0:8", ["const:4fed00:8", "const:4:8"]]
- 004fed00 ["CALL", null, ["callee:00459510:8"]]
+ 004fed40 ["INT_ADD", "register:40f0:8", ["const:4fed40:8", "const:4:8"]]
+ 004fed40 ["CALL", null, ["callee:00459510:8"]]
- 004fed00 bytes f469fd97
+ 004fed40 bytes f469fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18e032e3c203dad035b0e8d8f537bca9"></a>

### [`004fee70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fe/004fee70.md) → [`004feeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fe/004feeb0.md) _ZN5Botan15AlternativeNameC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_S9_S9_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59b10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59b10.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59950.md)
- 新版 呼出元 1件 [`00c59be0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59be0.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c59a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59a20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.88% / 新版 96.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004feefc",
      "incomplete_value": true,
      "site": "004fef24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004feebc",
      "incomplete_value": true,
      "site": "004feee4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004feee0",
      "READ",
      [
        "storage",
        "00c9b0c8",
        null,
        "pointer"
      ]
    ],
    [
      "004fef24",
      "DATA",
      [
        "storage",
        "00c67768",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004feee0",
      "READ",
      [
        "storage",
        "00c9b198",
        null,
        "pointer"
      ]
    ],
    [
      "004fef24",
      "DATA",
      [
        "storage",
        "00c67838",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004feea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fe/004fee70.md#insn-004feea0) · [`004fef0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fe/004fee70.md#insn-004fef0c) · [`004fef1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fe/004fee70.md#insn-004fef1c)
- 新版 [`004feee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fe/004feeb0.md#insn-004feee0) · [`004fef4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fe/004feeb0.md#insn-004fef4c) · [`004fef5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fe/004feeb0.md#insn-004fef5c)

~~~diff
- 004feea0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c8:8"]]
- 004feea0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004feee0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:198:8"]]
+ 004feee0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004feea0 bytes 296540f9
+ 004feee0 bytes 29cd40f9
- 004fef0c ["INT_ADD", "register:40f0:8", ["const:4fef0c:8", "const:4:8"]]
- 004fef0c ["CALL", null, ["callee:00c59a20:8"]]
+ 004fef4c ["INT_ADD", "register:40f0:8", ["const:4fef4c:8", "const:4:8"]]
+ 004fef4c ["CALL", null, ["callee:00c59a20:8"]]
- 004fef0c bytes 916a1d94
+ 004fef4c bytes b56a1d94
- 004fef1c ["INT_ADD", "register:40f0:8", ["const:4fef1c:8", "const:4:8"]]
- 004fef1c ["CALL", null, ["callee:00c57f80:8"]]
+ 004fef5c ["INT_ADD", "register:40f0:8", ["const:4fef5c:8", "const:4:8"]]
+ 004fef5c ["CALL", null, ["callee:00c57f80:8"]]
- 004fef1c bytes e5631d94
+ 004fef5c bytes 09641d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eafc4c9e90bf5f5944a050e572aab298"></a>

### [`004ffaac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ffaac.md) → [`004ffaec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ffaec.md) FUN_004ffaec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`004ff838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff838.md) · 呼出先 13件 [`005085bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00508/005085bc.md) [`00514da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00514/00514da4.md) [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md) [`00548098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548098.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`004ff878`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff878.md) · 呼出先 13件 [`005085fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/005085fc.md) [`00514de4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/00514de4.md) [`0053afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053afd0.md) [`005480d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00548/005480d8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.15% / 新版 94.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ffb70",
      "incomplete_value": true,
      "site": "004ffb70",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004ffb30",
      "incomplete_value": true,
      "site": "004ffb30",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ffb70",
      "incomplete_value": true,
      "site": "004ffb70",
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
      "definition_site": "004ffb30",
      "incomplete_value": true,
      "site": "004ffb30",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ffb64",
      "incomplete_value": true,
      "site": "004ffb78",
      "value": [
        "LOAD",
        "8",
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
                "const:8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ffb24",
      "incomplete_value": true,
      "site": "004ffb38",
      "value": [
        "LOAD",
        "8",
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
                "const:8:8"
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
      "004ffb48",
      "READ",
      [
        "storage",
        "00c9ac10",
        null,
        "pointer"
      ]
    ],
    [
      "004ffb60",
      "READ",
      [
        "storage",
        "00c930e8",
        "_ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "004ffb64",
      "READ",
      [
        "storage",
        "00c93128",
        null,
        "pointer __((offset(0x68)))"
      ]
    ]
  ],
  "added": [
    [
      "004ffb48",
      "READ",
      [
        "storage",
        "00c9ace0",
        null,
        "pointer"
      ]
    ],
    [
      "004ffb60",
      "READ",
      [
        "storage",
        "00c931b8",
        "_ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "004ffb64",
      "READ",
      [
        "storage",
        "00c931f8",
        null,
        "pointer __((offset(0x68)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ffaf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ffaac.md#insn-004ffaf0) · [`004ffd38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ffaac.md#insn-004ffd38) · [`004ffb08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ffaac.md#insn-004ffb08)
- 新版 [`004ffb30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ffaec.md#insn-004ffb30) · [`004ffd78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ffaec.md#insn-004ffd78) · [`004ffb48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ffaec.md#insn-004ffb48)

~~~diff
- 004ffaf0 ["INT_ADD", "register:40f0:8", ["const:4ffaf0:8", "const:4:8"]]
- 004ffaf0 ["CALL", null, ["callee:005480d8:8"]]
+ 004ffb30 ["INT_ADD", "register:40f0:8", ["const:4ffb30:8", "const:4:8"]]
+ 004ffb30 ["CALL", null, ["callee:005480d8:8"]]
- 004ffaf0 bytes 6a210194
+ 004ffb30 bytes 6a210194
- 004ffd38 ["INT_ADD", "register:40f0:8", ["const:4ffd38:8", "const:4:8"]]
- 004ffd38 ["CALL", null, ["callee:00c58290:8"]]
+ 004ffd78 ["INT_ADD", "register:40f0:8", ["const:4ffd78:8", "const:4:8"]]
+ 004ffd78 ["CALL", null, ["callee:00c58290:8"]]
- 004ffd38 bytes 22611d94
+ 004ffd78 bytes 46611d94
- 004ffb08 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c10:8"]]
- 004ffb08 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ffb48 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ce0:8"]]
+ 004ffb48 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004ffb08 bytes 080946f9
+ 004ffb48 bytes 087146f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9a1fe489b7e4204759f98c64b09ef84"></a>

### [`004ffe20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ffe20.md) → [`004ffe60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ffe60.md) _ZN5Botan15AlternativeName11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 28件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004518b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004518b0.md) [`004ff37c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff37c.md) [`00506f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00506/00506f90.md)
- 新版 呼出元 0件  · 呼出先 28件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004518f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004518f0.md) [`004ff3bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff3bc.md) [`00506fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00506/00506fd0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.29% / 新版 96.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 7件, `store_value` 4件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ffed0",
      "incomplete_value": true,
      "site": "004ffed4",
      "value": [
        "LOAD",
        "8",
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
                "const:8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ffe90",
      "incomplete_value": true,
      "site": "004ffe94",
      "value": [
        "LOAD",
        "8",
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
                "const:8:8"
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
      "definition_site": "004ffee0",
      "incomplete_value": true,
      "site": "004ffee0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004ffea0",
      "incomplete_value": true,
      "site": "004ffea0",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ffee0",
      "incomplete_value": true,
      "site": "004ffee0",
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
      "definition_site": "004ffea0",
      "incomplete_value": true,
      "site": "004ffea0",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004ffeb4",
      "READ",
      [
        "storage",
        "00c9ac10",
        null,
        "pointer"
      ]
    ],
    [
      "004ffecc",
      "READ",
      [
        "storage",
        "00c930e8",
        "_ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "004ffed0",
      "READ",
      [
        "storage",
        "00c93128",
        null,
        "pointer __((offset(0x68)))"
      ]
    ]
  ],
  "added": [
    [
      "004ffeb4",
      "READ",
      [
        "storage",
        "00c9ace0",
        null,
        "pointer"
      ]
    ],
    [
      "004ffecc",
      "READ",
      [
        "storage",
        "00c931b8",
        "_ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "004ffed0",
      "READ",
      [
        "storage",
        "00c931f8",
        null,
        "pointer __((offset(0x68)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ffee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ffe20.md#insn-004ffee0) · [`00500274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ffe20.md#insn-00500274) · [`005002d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ffe20.md#insn-005002d4)
- 新版 [`004fff20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ffe60.md#insn-004fff20) · [`005002b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ffe60.md#insn-005002b4) · [`00500314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ffe60.md#insn-00500314)

~~~diff
- 004ffee0 ["COPY", "register:0:8", ["register:4040:8"]]
- 004ffee0 ["INT_ADD", "register:40f0:8", ["const:4ffee0:8", "const:4:8"]]
- 004ffee0 ["CALLIND", null, ["register:0:8"]]
+ 004fff20 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004fff20 ["INT_ADD", "register:40f0:8", ["const:4fff20:8", "const:4:8"]]
+ 004fff20 ["CALLIND", null, ["register:0:8"]]
- 004ffee0 bytes 00013fd6
+ 004fff20 bytes 00013fd6
- 00500274 ["INT_ADD", "register:40f0:8", ["const:500274:8", "const:4:8"]]
- 00500274 ["CALL", null, ["callee:00c58290:8"]]
+ 005002b4 ["INT_ADD", "register:40f0:8", ["const:5002b4:8", "const:4:8"]]
+ 005002b4 ["CALL", null, ["callee:00c58290:8"]]
- 00500274 bytes d35f1d94
+ 005002b4 bytes f75f1d94
- 005002d4 ["COPY", "register:0:8", ["register:4048:8"]]
- 005002d4 ["INT_ADD", "register:40f0:8", ["const:5002d4:8", "const:4:8"]]
- 005002d4 ["CALLIND", null, ["register:0:8"]]
+ 00500314 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00500314 ["INT_ADD", "register:40f0:8", ["const:500314:8", "const:4:8"]]
+ 00500314 ["CALLIND", null, ["register:0:8"]]
- 005002d4 bytes 20013fd6
+ 00500314 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10971c606b6dc3f6e55a8026005eef5e"></a>

### [`00500afc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00500/00500afc.md) → [`00500b3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00500/00500b3c.md) _ZN5BotanlsERNSt6__ndk113basic_ostreamIcNS0_11char_traitsIcEEEERKNS_7X509_DNE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c599a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599a0.md) · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`004594d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00c59a70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59a70.md) · 呼出先 6件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00459510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459510.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.51% / 新版 97.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00500e7c",
      "incomplete_value": false,
      "site": "00500e84",
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
            "const:a8b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00500e3c",
      "incomplete_value": false,
      "site": "00500e44",
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
            "const:a5c:8"
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
      "00500da8",
      "PARAM",
      [
        "storage",
        "002b8fe4",
        null,
        null
      ]
    ],
    [
      "00500dfc",
      "PARAM",
      [
        "storage",
        "002a6752",
        null,
        null
      ]
    ],
    [
      "00500e2c",
      "PARAM",
      [
        "storage",
        "002b5e8d",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00500da8",
      "PARAM",
      [
        "storage",
        "002b8f90",
        null,
        null
      ]
    ],
    [
      "00500dfc",
      "PARAM",
      [
        "storage",
        "002a66f6",
        null,
        null
      ]
    ],
    [
      "00500e2c",
      "PARAM",
      [
        "storage",
        "002b5ecd",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00500e44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00500/00500afc.md#insn-00500e44) · [`00500b3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00500/00500afc.md#insn-00500b3c) · [`00500b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00500/00500afc.md#insn-00500b58)
- 新版 [`00500e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00500/00500b3c.md#insn-00500e84) · [`00500b7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00500/00500b3c.md#insn-00500b7c) · [`00500b98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00500/00500b3c.md#insn-00500b98)

~~~diff
- 00500e44 ["INT_ADD", "register:40f0:8", ["const:500e44:8", "const:4:8"]]
- 00500e44 ["CALL", null, ["callee:00459510:8"]]
+ 00500e84 ["INT_ADD", "register:40f0:8", ["const:500e84:8", "const:4:8"]]
+ 00500e84 ["CALL", null, ["callee:00459510:8"]]
- 00500e44 bytes a361fd97
+ 00500e84 bytes a361fd97
- 00500b3c ["INT_ADD", "register:40f0:8", ["const:500b3c:8", "const:4:8"]]
- 00500b3c ["CALL", null, ["callee:00c59a80:8"]]
+ 00500b7c ["INT_ADD", "register:40f0:8", ["const:500b7c:8", "const:4:8"]]
+ 00500b7c ["CALL", null, ["callee:00c59a80:8"]]
- 00500b3c bytes 9d631d94
+ 00500b7c bytes c1631d94
- 00500b58 ["COPY", "tmp:0:8", ["const:fe4:8"]]
- 00500b58 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 00500b58 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 00500b58 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 00500b98 ["COPY", "tmp:0:8", ["const:f90:8"]]
+ 00500b98 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 00500b98 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 00500b98 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 00500b58 bytes 94923f91
+ 00500b98 bytes 94423e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cba35f52de6ced77a19d5154837aaf76"></a>

### [`00500f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00500/00500f40.md) → [`00500f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00500/00500f80.md) _ZN5Botan9to_stringENS_23Certificate_Status_CodeE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c599c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599c0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c59a90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59a90.md) · 呼出先 0件 

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_return_alignment

命令の説明率　旧版 82.72% / 新版 82.72%

CFGの説明率　旧版 96.67% / 新版 96.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 41件, `unresolved_return_alignment` 2件

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00500fd4",
      "incomplete_value": false,
      "site": "00500fd8",
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
            "const:9d1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00500f94",
      "incomplete_value": false,
      "site": "00500f98",
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
            "const:a2d:8"
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
      "definition_site": "00501010",
      "incomplete_value": false,
      "site": "00501014",
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
            "const:d89:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00500fd0",
      "incomplete_value": false,
      "site": "00500fd4",
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
            "const:ddd:8"
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
      "definition_site": "00501044",
      "incomplete_value": false,
      "site": "00501048",
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
            "const:6a6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00501004",
      "incomplete_value": false,
      "site": "00501008",
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
            "const:702:8"
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
      "00500fd4",
      "DATA",
      [
        "storage",
        "002afa2d",
        null,
        "string"
      ]
    ],
    [
      "00501010",
      "DATA",
      [
        "storage",
        "002beddd",
        null,
        "string"
      ]
    ],
    [
      "00501044",
      "DATA",
      [
        "storage",
        "002a6702",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00500fd4",
      "DATA",
      [
        "storage",
        "002af9d1",
        null,
        "string"
      ]
    ],
    [
      "00501010",
      "DATA",
      [
        "storage",
        "002bed89",
        null,
        "string"
      ]
    ],
    [
      "00501044",
      "DATA",
      [
        "storage",
        "002a66a6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00500f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00500/00500f40.md#insn-00500f94) · [`00501038`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00500/00500f40.md#insn-00501038) · [`005010fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00500/00500f40.md#insn-005010fc)
- 新版 [`00500fd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00500/00500f80.md#insn-00500fd4) · [`00501078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00500/00500f80.md#insn-00501078)

~~~diff
- 00500f94 ["COPY", "tmp:0:8", ["const:a2d:8"]]
- 00500f94 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00500f94 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00500f94 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00500fd4 ["COPY", "tmp:0:8", ["const:9d1:8"]]
+ 00500fd4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00500fd4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00500fd4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00500f94 bytes 00b42891
+ 00500fd4 bytes 00442791
- 00501038 ["COPY", "tmp:0:8", ["const:c56:8"]]
- 00501038 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00501038 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00501038 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00501078 ["COPY", "tmp:0:8", ["const:bfa:8"]]
+ 00501078 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00501078 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00501078 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00501038 bytes 00583191
+ 00501078 bytes 00e82f91
- 005010fc ["COPY", "register:0:8", ["register:40f0:8"]]
- 005010fc ["RETURN", null, ["register:0:8"]]
- 005010fc bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27fd397d80626e682f11cde56e2aab2d"></a>

### [`00501388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501388.md) → [`005013c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/005013c8.md) _ZN5Botan27Certificate_Store_In_Memory15add_certificateERKNS_16X509_CertificateE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c599d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599d0.md) · 呼出先 10件 [`0053b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053b000.md) [`005483a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/005483a8.md) [`005483b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/005483b8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)
- 新版 呼出元 1件 [`00c59aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59aa0.md) · 呼出先 10件 [`0053b040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053b040.md) [`005483e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00548/005483e8.md) [`005483f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00548/005483f8.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.20% / 新版 97.20%

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
      "definition_site": "005014a4",
      "incomplete_value": true,
      "site": "005014a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00501464",
      "incomplete_value": true,
      "site": "00501468",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005014c0",
      "incomplete_value": true,
      "site": "005014c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00501480",
      "incomplete_value": true,
      "site": "00501488",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "0050149c",
      "READ",
      [
        "storage",
        "00c9b0d8",
        null,
        "pointer"
      ]
    ],
    [
      "005014a8",
      "DATA",
      [
        "storage",
        "00c6a740",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "005014bc",
      "READ",
      [
        "storage",
        "00c9b0e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050149c",
      "READ",
      [
        "storage",
        "00c9b1a8",
        null,
        "pointer"
      ]
    ],
    [
      "005014a8",
      "DATA",
      [
        "storage",
        "00c6a810",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "005014bc",
      "READ",
      [
        "storage",
        "00c9b1b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050140c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501388.md#insn-0050140c) · [`0050141c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501388.md#insn-0050141c) · [`0050143c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501388.md#insn-0050143c)
- 新版 [`0050144c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/005013c8.md#insn-0050144c) · [`0050145c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/005013c8.md#insn-0050145c) · [`0050147c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/005013c8.md#insn-0050147c)

~~~diff
- 0050140c ["INT_ADD", "register:40f0:8", ["const:50140c:8", "const:4:8"]]
- 0050140c ["CALL", null, ["callee:00c58120:8"]]
+ 0050144c ["INT_ADD", "register:40f0:8", ["const:50144c:8", "const:4:8"]]
+ 0050144c ["CALL", null, ["callee:00c58120:8"]]
- 0050140c bytes 115b1d94
+ 0050144c bytes 355b1d94
- 0050141c ["INT_ADD", "register:40f0:8", ["const:50141c:8", "const:4:8"]]
- 0050141c ["CALL", null, ["callee:00c58770:8"]]
+ 0050145c ["INT_ADD", "register:40f0:8", ["const:50145c:8", "const:4:8"]]
+ 0050145c ["CALL", null, ["callee:00c58770:8"]]
- 0050141c bytes a15c1d94
+ 0050145c bytes c55c1d94
- 0050143c ["INT_ADD", "register:40f0:8", ["const:50143c:8", "const:4:8"]]
- 0050143c ["CALL", null, ["callee:00c58120:8"]]
+ 0050147c ["INT_ADD", "register:40f0:8", ["const:50147c:8", "const:4:8"]]
+ 0050147c ["CALL", null, ["callee:00c58120:8"]]
- 0050143c bytes 055b1d94
+ 0050147c bytes 295b1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8d381fe88f7537d38ff79fad835fda8"></a>

### [`00501e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501e50.md) → [`00501e90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/00501e90.md) _ZNK5Botan27Certificate_Store_In_Memory24find_cert_by_pubkey_sha1ERKNSt6__ndk16vectorIhNS1_9allocatorIhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.69% / 新版 98.69%

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
      "definition_site": "005020a8",
      "incomplete_value": false,
      "site": "005020b0",
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
            "const:b5a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00502068",
      "incomplete_value": false,
      "site": "00502070",
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
            "const:b29:8"
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
      "definition_site": "005020e0",
      "incomplete_value": true,
      "site": "005020ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005020a0",
      "incomplete_value": true,
      "site": "005020ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005020dc",
      "incomplete_value": false,
      "site": "005020ec",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "0050209c",
      "incomplete_value": false,
      "site": "005020ac",
      "value": [
        "leaf",
        "const:535868:8"
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
      "005020a8",
      "PARAM",
      [
        "storage",
        "002b2b29",
        null,
        "string"
      ]
    ],
    [
      "005020dc",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "005020e0",
      "READ",
      [
        "storage",
        "00c9ad30",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005020a8",
      "PARAM",
      [
        "storage",
        "002b2b5a",
        null,
        "string"
      ]
    ],
    [
      "005020dc",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "005020e0",
      "READ",
      [
        "storage",
        "00c9ae00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00502070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501e50.md#insn-00502070) · [`005020ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501e50.md#insn-005020ac) · [`00501ec4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501e50.md#insn-00501ec4)
- 新版 [`005020b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/00501e90.md#insn-005020b0) · [`005020ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/00501e90.md#insn-005020ec) · [`00501f04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/00501e90.md#insn-00501f04)

~~~diff
- 00502070 ["INT_ADD", "register:40f0:8", ["const:502070:8", "const:4:8"]]
- 00502070 ["CALL", null, ["callee:0043de18:8"]]
+ 005020b0 ["INT_ADD", "register:40f0:8", ["const:5020b0:8", "const:4:8"]]
+ 005020b0 ["CALL", null, ["callee:0043de18:8"]]
- 00502070 bytes 5aeffc97
+ 005020b0 bytes 5aeffc97
- 005020ac ["INT_ADD", "register:40f0:8", ["const:5020ac:8", "const:4:8"]]
- 005020ac ["CALL", null, ["callee:00c57fe0:8"]]
+ 005020ec ["INT_ADD", "register:40f0:8", ["const:5020ec:8", "const:4:8"]]
+ 005020ec ["CALL", null, ["callee:00c57fe0:8"]]
- 005020ac bytes 99571d94
+ 005020ec bytes bd571d94
- 00501ec4 ["INT_ADD", "register:40f0:8", ["const:501ec4:8", "const:4:8"]]
- 00501ec4 ["CALL", null, ["callee:00c58ec0:8"]]
+ 00501f04 ["INT_ADD", "register:40f0:8", ["const:501f04:8", "const:4:8"]]
+ 00501f04 ["CALL", null, ["callee:00c58ec0:8"]]
- 00501ec4 bytes cb5b1d94
+ 00501f04 bytes ef5b1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53350316ff7217ce983dc2c2506af929"></a>

### [`00502168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502168.md) → [`005021a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/005021a8.md) _ZNK5Botan27Certificate_Store_In_Memory34find_cert_by_raw_subject_dn_sha256ERKNSt6__ndk16vectorIhNS1_9allocatorIhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.71% / 新版 98.71%

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
      "definition_site": "005023c8",
      "incomplete_value": false,
      "site": "005023d0",
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
            "const:585:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00502388",
      "incomplete_value": false,
      "site": "00502390",
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
            "const:5e1:8"
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
      "definition_site": "00502400",
      "incomplete_value": true,
      "site": "0050240c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005023c0",
      "incomplete_value": true,
      "site": "005023cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005023fc",
      "incomplete_value": false,
      "site": "0050240c",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "005023bc",
      "incomplete_value": false,
      "site": "005023cc",
      "value": [
        "leaf",
        "const:535868:8"
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
      "005023c8",
      "PARAM",
      [
        "storage",
        "002a55e1",
        null,
        "string"
      ]
    ],
    [
      "005023fc",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "00502400",
      "READ",
      [
        "storage",
        "00c9ad30",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005023c8",
      "PARAM",
      [
        "storage",
        "002a5585",
        null,
        "string"
      ]
    ],
    [
      "005023fc",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "00502400",
      "READ",
      [
        "storage",
        "00c9ae00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00502390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502168.md#insn-00502390) · [`005023cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502168.md#insn-005023cc) · [`005021e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502168.md#insn-005021e4)
- 新版 [`005023d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/005021a8.md#insn-005023d0) · [`0050240c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/005021a8.md#insn-0050240c) · [`00502224`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/005021a8.md#insn-00502224)

~~~diff
- 00502390 ["INT_ADD", "register:40f0:8", ["const:502390:8", "const:4:8"]]
- 00502390 ["CALL", null, ["callee:0043de18:8"]]
+ 005023d0 ["INT_ADD", "register:40f0:8", ["const:5023d0:8", "const:4:8"]]
+ 005023d0 ["CALL", null, ["callee:0043de18:8"]]
- 00502390 bytes 92eefc97
+ 005023d0 bytes 92eefc97
- 005023cc ["INT_ADD", "register:40f0:8", ["const:5023cc:8", "const:4:8"]]
- 005023cc ["CALL", null, ["callee:00c57fe0:8"]]
+ 0050240c ["INT_ADD", "register:40f0:8", ["const:50240c:8", "const:4:8"]]
+ 0050240c ["CALL", null, ["callee:00c57fe0:8"]]
- 005023cc bytes d1561d94
+ 0050240c bytes f5561d94
- 005021e4 ["INT_ADD", "register:40f0:8", ["const:5021e4:8", "const:4:8"]]
- 005021e4 ["CALL", null, ["callee:00c58ec0:8"]]
+ 00502224 ["INT_ADD", "register:40f0:8", ["const:502224:8", "const:4:8"]]
+ 00502224 ["CALL", null, ["callee:00c58ec0:8"]]
- 005021e4 bytes 035b1d94
+ 00502224 bytes 275b1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0cba154ee4ee8fc77829fc3f837c403"></a>

### [`00502488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502488.md) → [`005024c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/005024c8.md) _ZN5Botan27Certificate_Store_In_Memory7add_crlERKNS_8X509_CRLE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`0053b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053b000.md) [`00548ac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548ac8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0053b040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053b040.md) [`00548b08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00548/00548b08.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.05% / 新版 96.05%

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
      "definition_site": "00502510",
      "incomplete_value": true,
      "site": "00502514",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005024d0",
      "incomplete_value": true,
      "site": "005024d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0050252c",
      "incomplete_value": true,
      "site": "00502534",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005024ec",
      "incomplete_value": true,
      "site": "005024f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00502508",
      "READ",
      [
        "storage",
        "00c9b0e8",
        null,
        "pointer"
      ]
    ],
    [
      "00502514",
      "DATA",
      [
        "storage",
        "00c6a790",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "00502528",
      "READ",
      [
        "storage",
        "00c9b0f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00502508",
      "READ",
      [
        "storage",
        "00c9b1b8",
        null,
        "pointer"
      ]
    ],
    [
      "00502514",
      "DATA",
      [
        "storage",
        "00c6a860",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "00502528",
      "READ",
      [
        "storage",
        "00c9b1c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005024b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502488.md#insn-005024b8) · [`005024c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502488.md#insn-005024c8) · [`005024e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502488.md#insn-005024e0)
- 新版 [`005024f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/005024c8.md#insn-005024f8) · [`00502508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/005024c8.md#insn-00502508) · [`00502520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/005024c8.md#insn-00502520)

~~~diff
- 005024b8 ["INT_ADD", "register:40f0:8", ["const:5024b8:8", "const:4:8"]]
- 005024b8 ["CALL", null, ["callee:00c57f60:8"]]
+ 005024f8 ["INT_ADD", "register:40f0:8", ["const:5024f8:8", "const:4:8"]]
+ 005024f8 ["CALL", null, ["callee:00c57f60:8"]]
- 005024b8 bytes 76561d94
+ 005024f8 bytes 9a561d94
- 005024c8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e8:8"]]
- 005024c8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00502508 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1b8:8"]]
+ 00502508 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005024c8 bytes 087540f9
+ 00502508 bytes 08dd40f9
- 005024e0 ["INT_ADD", "register:40f0:8", ["const:5024e0:8", "const:4:8"]]
- 005024e0 ["CALL", null, ["callee:0053b040:8"]]
+ 00502520 ["INT_ADD", "register:40f0:8", ["const:502520:8", "const:4:8"]]
+ 00502520 ["CALL", null, ["callee:0053b040:8"]]
- 005024e0 bytes c8e20094
+ 00502520 bytes c8e20094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abda60e5206f358e115c1f24fe006887"></a>

### [`005027f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/005027f8.md) → [`00502838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502838.md) FUN_00502838

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`00501740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501740.md) [`005025fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/005025fc.md) [`00529334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00529/00529334.md) [`00529db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00529/00529db8.md) [`005486f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/005486f4.md) · 呼出先 4件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`0053aaa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053aaa4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 5件 [`00501780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/00501780.md) [`0050263c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/0050263c.md) [`00529374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00529/00529374.md) [`00529df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00529/00529df8.md) [`00548734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00548/00548734.md) · 呼出先 4件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`0053aae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053aae4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.16% / 新版 95.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00502878",
      "incomplete_value": true,
      "site": "00502880",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00502838",
      "incomplete_value": true,
      "site": "00502840",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00502868",
      "READ",
      [
        "storage",
        "00c9b0d0",
        null,
        "pointer"
      ]
    ],
    [
      "00502880",
      "DATA",
      [
        "storage",
        "00c679f8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00502868",
      "READ",
      [
        "storage",
        "00c9b1a0",
        null,
        "pointer"
      ]
    ],
    [
      "00502880",
      "DATA",
      [
        "storage",
        "00c67ac8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00502880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/005027f8.md#insn-00502880) · [`00502828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/005027f8.md#insn-00502828) · [`00502868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/005027f8.md#insn-00502868)
- 新版 [`005028c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502838.md#insn-005028c0) · [`00502868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502838.md#insn-00502868) · [`005028a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502838.md#insn-005028a8)

~~~diff
- 00502880 ["INT_ADD", "register:40f0:8", ["const:502880:8", "const:4:8"]]
- 00502880 ["CALL", null, ["callee:00c580d0:8"]]
+ 005028c0 ["INT_ADD", "register:40f0:8", ["const:5028c0:8", "const:4:8"]]
+ 005028c0 ["CALL", null, ["callee:00c580d0:8"]]
- 00502880 bytes e0551d94
+ 005028c0 bytes 04561d94
- 00502828 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d0:8"]]
- 00502828 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00502868 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1a0:8"]]
+ 00502868 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00502828 bytes 086940f9
+ 00502868 bytes 08d140f9
- 00502868 ["INT_ADD", "register:40f0:8", ["const:502868:8", "const:4:8"]]
- 00502868 ["CALL", null, ["callee:00c57f60:8"]]
+ 005028a8 ["INT_ADD", "register:40f0:8", ["const:5028a8:8", "const:4:8"]]
+ 005028a8 ["CALL", null, ["callee:00c57f60:8"]]
- 00502868 bytes 8a551d94
+ 005028a8 bytes ae551d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f09f613e64ffe41b7c5e61d7b26f4ea3"></a>

### [`00502b3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502b3c.md) → [`00502b7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502b7c.md) _ZN5Botan27Certificate_Store_In_MemoryC1ERKNS_16X509_CertificateE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c599d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59aa0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 78.95% / 新版 78.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00502ba0",
      "incomplete_value": true,
      "site": "00502ba4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00502b60",
      "incomplete_value": true,
      "site": "00502b64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00502b98",
      "READ",
      [
        "storage",
        "00c9b0f8",
        null,
        "pointer"
      ]
    ],
    [
      "00502ba4",
      "DATA",
      [
        "storage",
        "00c67798",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00502b98",
      "READ",
      [
        "storage",
        "00c9b1c8",
        null,
        "pointer"
      ]
    ],
    [
      "00502ba4",
      "DATA",
      [
        "storage",
        "00c67868",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00502b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502b3c.md#insn-00502b58) · [`00502b5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502b3c.md#insn-00502b5c) · [`00502b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502b3c.md#insn-00502b74)
- 新版 [`00502b98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502b7c.md#insn-00502b98) · [`00502bb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502b7c.md#insn-00502bb4)

~~~diff
- 00502b58 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f8:8"]]
- 00502b58 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00502b98 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1c8:8"]]
+ 00502b98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00502b58 bytes 087d40f9
+ 00502b98 bytes 08e540f9
- 00502b5c ["COPY", "register:40a0:8", ["register:4000:8"]]
- 00502b5c bytes f40300aa
- 00502b74 ["INT_ADD", "register:40f0:8", ["const:502b74:8", "const:4:8"]]
- 00502b74 ["CALL", null, ["callee:00c59aa0:8"]]
+ 00502bb4 ["INT_ADD", "register:40f0:8", ["const:502bb4:8", "const:4:8"]]
+ 00502bb4 ["CALL", null, ["callee:00c59aa0:8"]]
- 00502b74 bytes 975b1d94
+ 00502bb4 bytes bb5b1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb7f1adbf83847dcb1f0721f62fcf386"></a>

### [`00502c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502c3c.md) → [`00502c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502c7c.md) _ZN5Botan27Certificate_Store_In_MemoryC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`005483b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/005483b8.md) [`00548d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548d78.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 9件 [`005483f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00548/005483f8.md) [`00548db8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00548/00548db8.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.58% / 新版 97.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00502cb4",
      "incomplete_value": true,
      "site": "00502cbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00502c74",
      "incomplete_value": true,
      "site": "00502c7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00502ca8",
      "READ",
      [
        "storage",
        "00c9b0f8",
        null,
        "pointer"
      ]
    ],
    [
      "00502cbc",
      "DATA",
      [
        "storage",
        "00c67798",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00502d04",
      "READ",
      [
        "storage",
        "00c9b100",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00502ca8",
      "READ",
      [
        "storage",
        "00c9b1c8",
        null,
        "pointer"
      ]
    ],
    [
      "00502cbc",
      "DATA",
      [
        "storage",
        "00c67868",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00502d04",
      "READ",
      [
        "storage",
        "00c9b1d0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00502c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502c3c.md#insn-00502c68) · [`00502cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502c3c.md#insn-00502cb0) · [`00502cc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502c3c.md#insn-00502cc4)
- 新版 [`00502ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502c7c.md#insn-00502ca8) · [`00502cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502c7c.md#insn-00502cf0) · [`00502d04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502c7c.md#insn-00502d04)

~~~diff
- 00502c68 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f8:8"]]
- 00502c68 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00502ca8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1c8:8"]]
+ 00502ca8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00502c68 bytes 087d40f9
+ 00502ca8 bytes 08e540f9
- 00502cb0 ["INT_ADD", "register:40f0:8", ["const:502cb0:8", "const:4:8"]]
- 00502cb0 ["CALL", null, ["callee:00c59900:8"]]
+ 00502cf0 ["INT_ADD", "register:40f0:8", ["const:502cf0:8", "const:4:8"]]
+ 00502cf0 ["CALL", null, ["callee:00c59900:8"]]
- 00502cb0 bytes e05a1d94
+ 00502cf0 bytes 045b1d94
- 00502cc4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:100:8"]]
- 00502cc4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00502d04 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1d0:8"]]
+ 00502d04 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00502cc4 bytes 088140f9
+ 00502d04 bytes 08e940f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09839a6e214e9383a6ea40ac9529e6ea"></a>

### [`00502f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502f10.md) → [`00502f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502f50.md) _ZN5Botan9CRL_EntryC2ERKNS_16X509_CertificateENS_8CRL_CodeE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00548e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548e68.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58580.md) [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00548ea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00548/00548ea8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58650.md) [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00502f88",
      "incomplete_value": true,
      "site": "00502f90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00502f48",
      "incomplete_value": true,
      "site": "00502f50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00502fbc",
      "incomplete_value": true,
      "site": "00502fbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00502f7c",
      "incomplete_value": true,
      "site": "00502f7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00502fe0",
      "incomplete_value": true,
      "site": "00502fe0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00502fa0",
      "incomplete_value": true,
      "site": "00502fa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00502f78",
      "READ",
      [
        "storage",
        "00c9b108",
        null,
        "pointer"
      ]
    ],
    [
      "00502f90",
      "DATA",
      [
        "storage",
        "00c677e8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00502fac",
      "READ",
      [
        "storage",
        "00c9adb0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00502f78",
      "READ",
      [
        "storage",
        "00c9b1d8",
        null,
        "pointer"
      ]
    ],
    [
      "00502f90",
      "DATA",
      [
        "storage",
        "00c678b8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00502fac",
      "READ",
      [
        "storage",
        "00c9ae80",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00502f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502f10.md#insn-00502f60) · [`00503004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502f10.md#insn-00503004) · [`00502f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502f10.md#insn-00502f38)
- 新版 [`00502fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502f50.md#insn-00502fa0) · [`00503044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502f50.md#insn-00503044) · [`00502f78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502f50.md#insn-00502f78)

~~~diff
- 00502f60 ["INT_ADD", "register:40f0:8", ["const:502f60:8", "const:4:8"]]
- 00502f60 ["CALL", null, ["callee:00c57f60:8"]]
+ 00502fa0 ["INT_ADD", "register:40f0:8", ["const:502fa0:8", "const:4:8"]]
+ 00502fa0 ["CALL", null, ["callee:00c57f60:8"]]
- 00502f60 bytes cc531d94
+ 00502fa0 bytes f0531d94
- 00503004 ["INT_ADD", "register:40f0:8", ["const:503004:8", "const:4:8"]]
- 00503004 ["CALL", null, ["callee:00c59b40:8"]]
+ 00503044 ["INT_ADD", "register:40f0:8", ["const:503044:8", "const:4:8"]]
+ 00503044 ["CALL", null, ["callee:00c59b40:8"]]
- 00503004 bytes 9b5a1d94
+ 00503044 bytes bf5a1d94
- 00502f38 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:108:8"]]
- 00502f38 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00502f78 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:1d8:8"]]
+ 00502f78 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00502f38 bytes 298540f9
+ 00502f78 bytes 29ed40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-673116f9a125fc012cd4b980863875dc"></a>

### [`005030c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/005030c4.md) → [`00503104`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503104.md) _ZN5Botan10Extensions3addEPNS_21Certificate_ExtensionEb

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59a80.md) · 呼出先 17件 [`00516bc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516bc4.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`0053d728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053d/0053d728.md) [`0054b944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054b944.md)
- 新版 呼出元 1件 [`00c59b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b50.md) · 呼出先 17件 [`00516c04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516c04.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00535bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bac.md) [`0053d768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053d/0053d768.md) [`0054b984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054b/0054b984.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.75% / 新版 97.75%

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
      "definition_site": "005032d8",
      "incomplete_value": true,
      "site": "005032d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00503298",
      "incomplete_value": true,
      "site": "00503298",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
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
      "definition_site": "0050331c",
      "incomplete_value": true,
      "site": "00503320",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005032dc",
      "incomplete_value": true,
      "site": "005032e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0050322c",
      "incomplete_value": false,
      "site": "00503234",
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
            "const:c40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005031ec",
      "incomplete_value": false,
      "site": "005031f4",
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
            "const:c9c:8"
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
      "0050322c",
      "PARAM",
      [
        "storage",
        "002b0c9c",
        null,
        "string"
      ]
    ],
    [
      "00503278",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "0050327c",
      "READ",
      [
        "storage",
        "00c9ad30",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050322c",
      "PARAM",
      [
        "storage",
        "002b0c40",
        null,
        "string"
      ]
    ],
    [
      "00503278",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "0050327c",
      "READ",
      [
        "storage",
        "00c9ae00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005031f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/005030c4.md#insn-005031f4) · [`00503248`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/005030c4.md#insn-00503248) · [`00503288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/005030c4.md#insn-00503288)
- 新版 [`00503234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503104.md#insn-00503234) · [`00503288`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503104.md#insn-00503288) · [`005032c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503104.md#insn-005032c8)

~~~diff
- 005031f4 ["INT_ADD", "register:40f0:8", ["const:5031f4:8", "const:4:8"]]
- 005031f4 ["CALL", null, ["callee:00c58040:8"]]
+ 00503234 ["INT_ADD", "register:40f0:8", ["const:503234:8", "const:4:8"]]
+ 00503234 ["CALL", null, ["callee:00c58040:8"]]
- 005031f4 bytes 5f531d94
+ 00503234 bytes 83531d94
- 00503248 ["INT_ADD", "register:40f0:8", ["const:503248:8", "const:4:8"]]
- 00503248 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00503288 ["INT_ADD", "register:40f0:8", ["const:503288:8", "const:4:8"]]
+ 00503288 ["CALL", null, ["callee:00c57fe0:8"]]
- 00503248 bytes 32531d94
+ 00503288 bytes 56531d94
- 00503288 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:120:8"]]
- 00503288 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005032c8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1f0:8"]]
+ 005032c8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00503288 bytes 089140f9
+ 005032c8 bytes 08f940f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a628e9aa7465839b1f02283e253fa845"></a>

### [`0050376c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/0050376c.md) → [`005037ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/005037ac.md) _ZN5Botan9CRL_Entry11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59ab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59ab0.md) · 呼出先 16件 [`004aea74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aea74.md) [`00503ae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/00503ae0.md) [`00517650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517650.md) [`00548dd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548dd4.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)
- 新版 呼出元 1件 [`00c59b80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b80.md) · 呼出先 16件 [`004aeab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeab4.md) [`00503b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503b20.md) [`00517690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/00517690.md) [`00548e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00548/00548e14.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.94% / 新版 94.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 2件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00503800",
      "incomplete_value": true,
      "site": "00503800",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005037c0",
      "incomplete_value": true,
      "site": "005037c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00503824",
      "incomplete_value": true,
      "site": "00503824",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005037e4",
      "incomplete_value": true,
      "site": "005037e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0050390c",
      "incomplete_value": true,
      "site": "0050390c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:518:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005038cc",
      "incomplete_value": true,
      "site": "005038cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:574:8"
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
      "005037f0",
      "READ",
      [
        "storage",
        "00c9adb0",
        null,
        "pointer"
      ]
    ],
    [
      "00503800",
      "DATA",
      [
        "storage",
        "00c66378",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00503810",
      "READ",
      [
        "storage",
        "00c9b110",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005037f0",
      "READ",
      [
        "storage",
        "00c9ae80",
        null,
        "pointer"
      ]
    ],
    [
      "00503800",
      "DATA",
      [
        "storage",
        "00c66448",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00503810",
      "READ",
      [
        "storage",
        "00c9b1e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050390c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/0050376c.md#insn-0050390c) · [`00503980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/0050376c.md#insn-00503980) · [`005039c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/0050376c.md#insn-005039c0)
- 新版 [`0050394c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/005037ac.md#insn-0050394c) · [`005039c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/005037ac.md#insn-005039c0) · [`00503a00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/005037ac.md#insn-00503a00)

~~~diff
- 0050390c ["INT_ADD", "register:40f0:8", ["const:50390c:8", "const:4:8"]]
- 0050390c ["CALL", null, ["callee:00c57f80:8"]]
+ 0050394c ["INT_ADD", "register:40f0:8", ["const:50394c:8", "const:4:8"]]
+ 0050394c ["CALL", null, ["callee:00c57f80:8"]]
- 0050390c bytes 69511d94
+ 0050394c bytes 8d511d94
- 00503980 ["INT_ADD", "register:40f0:8", ["const:503980:8", "const:4:8"]]
- 00503980 ["CALL", null, ["callee:00c57f50:8"]]
+ 005039c0 ["INT_ADD", "register:40f0:8", ["const:5039c0:8", "const:4:8"]]
+ 005039c0 ["CALL", null, ["callee:00c57f50:8"]]
- 00503980 bytes 40511d94
+ 005039c0 bytes 64511d94
- 005039c0 ["COPY", "register:0:8", ["register:4048:8"]]
- 005039c0 ["INT_ADD", "register:40f0:8", ["const:5039c0:8", "const:4:8"]]
- 005039c0 ["CALLIND", null, ["register:0:8"]]
+ 00503a00 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00503a00 ["INT_ADD", "register:40f0:8", ["const:503a00:8", "const:4:8"]]
+ 00503a00 ["CALLIND", null, ["register:0:8"]]
- 005039c0 bytes 20013fd6
+ 00503a00 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-adb2b94669b9c3a848667577d49f7104"></a>

### [`00503ae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/00503ae0.md) → [`00503b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503b20.md) FUN_00503b20

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0050376c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/0050376c.md) · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`005037ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/005037ac.md) · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00503b5c",
      "incomplete_value": true,
      "site": "00503b5c",
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
      "definition_site": "00503b1c",
      "incomplete_value": true,
      "site": "00503b1c",
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00503b98",
      "incomplete_value": false,
      "site": "00503ba0",
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
            "const:2c3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00503b58",
      "incomplete_value": false,
      "site": "00503b60",
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
            "const:310:8"
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
      "definition_site": "00503bd4",
      "incomplete_value": true,
      "site": "00503be0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00503b94",
      "incomplete_value": true,
      "site": "00503ba0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d88:8"
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
      "00503b4c",
      "READ",
      [
        "storage",
        "00c9b118",
        null,
        "pointer"
      ]
    ],
    [
      "00503b98",
      "PARAM",
      [
        "storage",
        "002a4310",
        null,
        "string"
      ]
    ],
    [
      "00503bd0",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00503b4c",
      "READ",
      [
        "storage",
        "00c9b1e8",
        null,
        "pointer"
      ]
    ],
    [
      "00503b98",
      "PARAM",
      [
        "storage",
        "002a42c3",
        null,
        "string"
      ]
    ],
    [
      "00503bd0",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00503b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/00503ae0.md#insn-00503b60) · [`00503ba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/00503ae0.md#insn-00503ba0) · [`00503b00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/00503ae0.md#insn-00503b00)
- 新版 [`00503ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503b20.md#insn-00503ba0) · [`00503be0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503b20.md#insn-00503be0) · [`00503b40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503b20.md#insn-00503b40)

~~~diff
- 00503b60 ["INT_ADD", "register:40f0:8", ["const:503b60:8", "const:4:8"]]
- 00503b60 ["CALL", null, ["callee:0043de18:8"]]
+ 00503ba0 ["INT_ADD", "register:40f0:8", ["const:503ba0:8", "const:4:8"]]
+ 00503ba0 ["CALL", null, ["callee:0043de18:8"]]
- 00503b60 bytes 9ee8fc97
+ 00503ba0 bytes 9ee8fc97
- 00503ba0 ["INT_ADD", "register:40f0:8", ["const:503ba0:8", "const:4:8"]]
- 00503ba0 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00503be0 ["INT_ADD", "register:40f0:8", ["const:503be0:8", "const:4:8"]]
+ 00503be0 ["CALL", null, ["callee:00c57fe0:8"]]
- 00503ba0 bytes dc501d94
+ 00503be0 bytes 00511d94
- 00503b00 ["INT_ADD", "register:40f0:8", ["const:503b00:8", "const:4:8"]]
- 00503b00 ["CALL", null, ["callee:00c59b90:8"]]
+ 00503b40 ["INT_ADD", "register:40f0:8", ["const:503b40:8", "const:4:8"]]
+ 00503b40 ["CALL", null, ["callee:00c59b90:8"]]
- 00503b00 bytes f0571d94
+ 00503b40 bytes 14581d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbcaef49e7222a644b5e4fdd286efc20"></a>

### [`00503bf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/00503bf4.md) → [`00503c34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503c34.md) FUN_00503c34

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005156c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/005156c4.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md)
- 新版 呼出元 1件 [`00515704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/00515704.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md)

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
      "definition_site": "00503c6c",
      "incomplete_value": true,
      "site": "00503c6c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:518:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00503c2c",
      "incomplete_value": true,
      "site": "00503c2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:574:8"
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
      "00503c5c",
      "READ",
      [
        "storage",
        "002a6574",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00503c5c",
      "READ",
      [
        "storage",
        "002a6518",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00503c10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/00503bf4.md#insn-00503c10) · [`00503c38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/00503bf4.md#insn-00503c38) · [`00503c48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/00503bf4.md#insn-00503c48)
- 新版 [`00503c50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503c34.md#insn-00503c50) · [`00503c78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503c34.md#insn-00503c78) · [`00503c88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503c34.md#insn-00503c88)

~~~diff
- 00503c10 ["COPY", "tmp:0:8", ["const:574:8"]]
- 00503c10 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00503c10 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00503c10 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00503c50 ["COPY", "tmp:0:8", ["const:518:8"]]
+ 00503c50 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00503c50 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00503c50 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00503c10 bytes 29d11591
+ 00503c50 bytes 29611491
- 00503c38 ["INT_ADD", "register:40f0:8", ["const:503c38:8", "const:4:8"]]
- 00503c38 ["CALL", null, ["callee:00c58760:8"]]
+ 00503c78 ["INT_ADD", "register:40f0:8", ["const:503c78:8", "const:4:8"]]
+ 00503c78 ["CALL", null, ["callee:00c58760:8"]]
- 00503c38 bytes 96521d94
+ 00503c78 bytes ba521d94
- 00503c48 ["INT_ADD", "register:40f0:8", ["const:503c48:8", "const:4:8"]]
- 00503c48 ["CALL", null, ["callee:00c57f80:8"]]
+ 00503c88 ["INT_ADD", "register:40f0:8", ["const:503c88:8", "const:4:8"]]
+ 00503c88 ["CALL", null, ["callee:00c57f80:8"]]
- 00503c48 bytes 9a501d94
+ 00503c88 bytes be501d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3429d200d25b65f0e22ab55a830cc8a1"></a>

### [`00503c9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/00503c9c.md) → [`00503cdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503cdc.md) _ZNK5Botan9CRL_Entry4dataEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59aa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59aa0.md) · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)
- 新版 呼出元 1件 [`00c59b70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b70.md) · 呼出先 6件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004aeca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.45% / 新版 95.45%

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
      "definition_site": "00503d3c",
      "incomplete_value": false,
      "site": "00503d44",
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
            "const:180:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00503cfc",
      "incomplete_value": false,
      "site": "00503d04",
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
            "const:1cd:8"
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
      "definition_site": "00503d78",
      "incomplete_value": true,
      "site": "00503d84",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00503d38",
      "incomplete_value": true,
      "site": "00503d44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00503d74",
      "incomplete_value": false,
      "site": "00503d84",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "00503d34",
      "incomplete_value": false,
      "site": "00503d44",
      "value": [
        "leaf",
        "const:535868:8"
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
      "00503d3c",
      "PARAM",
      [
        "storage",
        "002a11cd",
        null,
        "string"
      ]
    ],
    [
      "00503d74",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "00503d78",
      "READ",
      [
        "storage",
        "00c9ad48",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00503d3c",
      "PARAM",
      [
        "storage",
        "002a1180",
        null,
        "string"
      ]
    ],
    [
      "00503d74",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "00503d78",
      "READ",
      [
        "storage",
        "00c9ae18",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00503d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/00503c9c.md#insn-00503d04) · [`00503d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/00503c9c.md#insn-00503d44) · [`00503cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/00503c9c.md#insn-00503cf0)
- 新版 [`00503d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503cdc.md#insn-00503d44) · [`00503d84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503cdc.md#insn-00503d84) · [`00503d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503cdc.md#insn-00503d30)

~~~diff
- 00503d04 ["INT_ADD", "register:40f0:8", ["const:503d04:8", "const:4:8"]]
- 00503d04 ["CALL", null, ["callee:0043de18:8"]]
+ 00503d44 ["INT_ADD", "register:40f0:8", ["const:503d44:8", "const:4:8"]]
+ 00503d44 ["CALL", null, ["callee:0043de18:8"]]
- 00503d04 bytes 35e8fc97
+ 00503d44 bytes 35e8fc97
- 00503d44 ["INT_ADD", "register:40f0:8", ["const:503d44:8", "const:4:8"]]
- 00503d44 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00503d84 ["INT_ADD", "register:40f0:8", ["const:503d84:8", "const:4:8"]]
+ 00503d84 ["CALL", null, ["callee:00c57fe0:8"]]
- 00503d44 bytes 73501d94
+ 00503d84 bytes 97501d94
- 00503cf0 ["INT_ADD", "register:40f0:8", ["const:503cf0:8", "const:4:8"]]
- 00503cf0 ["CALL", null, ["callee:00c57fc0:8"]]
+ 00503d30 ["INT_ADD", "register:40f0:8", ["const:503d30:8", "const:4:8"]]
+ 00503d30 ["CALL", null, ["callee:00c57fc0:8"]]
- 00503cf0 bytes 80501d94
+ 00503d30 bytes a4501d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e731946003ab4cdfe2f217a486c7449"></a>

### [`005042b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/005042b8.md) → [`005042f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/005042f8.md) _ZNK5Botan10Data_Store4get1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`004aeca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.26% / 新版 96.26%

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
      "definition_site": "005043f8",
      "incomplete_value": false,
      "site": "00504404",
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
            "const:1f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005043b8",
      "incomplete_value": false,
      "site": "005043c4",
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
            "const:23d:8"
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
      "definition_site": "00504434",
      "incomplete_value": true,
      "site": "00504440",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005043f4",
      "incomplete_value": true,
      "site": "00504400",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00504430",
      "incomplete_value": false,
      "site": "00504440",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "005043f0",
      "incomplete_value": false,
      "site": "00504400",
      "value": [
        "leaf",
        "const:535868:8"
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
      "005043f8",
      "PARAM",
      [
        "storage",
        "002a423d",
        null,
        "string"
      ]
    ],
    [
      "00504430",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "00504434",
      "READ",
      [
        "storage",
        "00c9ad48",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005043f8",
      "PARAM",
      [
        "storage",
        "002a41f0",
        null,
        "string"
      ]
    ],
    [
      "00504430",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "00504434",
      "READ",
      [
        "storage",
        "00c9ae18",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005043c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/005042b8.md#insn-005043c4) · [`00504400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/005042b8.md#insn-00504400) · [`00504424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/005042b8.md#insn-00504424)
- 新版 [`00504404`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/005042f8.md#insn-00504404) · [`00504440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/005042f8.md#insn-00504440) · [`00504464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/005042f8.md#insn-00504464)

~~~diff
- 005043c4 ["INT_ADD", "register:40f0:8", ["const:5043c4:8", "const:4:8"]]
- 005043c4 ["CALL", null, ["callee:00c58180:8"]]
+ 00504404 ["INT_ADD", "register:40f0:8", ["const:504404:8", "const:4:8"]]
+ 00504404 ["CALL", null, ["callee:00c58180:8"]]
- 005043c4 bytes 3b4f1d94
+ 00504404 bytes 5f4f1d94
- 00504400 ["INT_ADD", "register:40f0:8", ["const:504400:8", "const:4:8"]]
- 00504400 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00504440 ["INT_ADD", "register:40f0:8", ["const:504440:8", "const:4:8"]]
+ 00504440 ["CALL", null, ["callee:00c57fe0:8"]]
- 00504400 bytes c44e1d94
+ 00504440 bytes e84e1d94
- 00504424 ["INT_ADD", "register:40f0:8", ["const:504424:8", "const:4:8"]]
- 00504424 ["CALL", null, ["callee:00c58180:8"]]
+ 00504464 ["INT_ADD", "register:40f0:8", ["const:504464:8", "const:4:8"]]
+ 00504464 ["CALL", null, ["callee:00c58180:8"]]
- 00504424 bytes 234f1d94
+ 00504464 bytes 474f1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2a744a47a1e3674dd527d221eedd033"></a>

### [`005044c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/005044c8.md) → [`00504508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/00504508.md) _ZNK5Botan10Data_Store4get1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`004aeca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.73% / 新版 97.73%

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
      "definition_site": "00504618",
      "incomplete_value": false,
      "site": "00504624",
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
            "const:853:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005045d8",
      "incomplete_value": false,
      "site": "005045e4",
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
            "const:8af:8"
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
      "definition_site": "00504654",
      "incomplete_value": true,
      "site": "00504660",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00504614",
      "incomplete_value": true,
      "site": "00504620",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00504650",
      "incomplete_value": false,
      "site": "00504660",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "00504610",
      "incomplete_value": false,
      "site": "00504620",
      "value": [
        "leaf",
        "const:535868:8"
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
      "00504618",
      "PARAM",
      [
        "storage",
        "002a78af",
        null,
        "string"
      ]
    ],
    [
      "00504650",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "00504654",
      "READ",
      [
        "storage",
        "00c9ad48",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00504618",
      "PARAM",
      [
        "storage",
        "002a7853",
        null,
        "string"
      ]
    ],
    [
      "00504650",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "00504654",
      "READ",
      [
        "storage",
        "00c9ae18",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005045e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/005044c8.md#insn-005045e4) · [`00504620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/005044c8.md#insn-00504620) · [`005044f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/005044c8.md#insn-005044f8)
- 新版 [`00504624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/00504508.md#insn-00504624) · [`00504660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/00504508.md#insn-00504660) · [`00504538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/00504508.md#insn-00504538)

~~~diff
- 005045e4 ["INT_ADD", "register:40f0:8", ["const:5045e4:8", "const:4:8"]]
- 005045e4 ["CALL", null, ["callee:00c58180:8"]]
+ 00504624 ["INT_ADD", "register:40f0:8", ["const:504624:8", "const:4:8"]]
+ 00504624 ["CALL", null, ["callee:00c58180:8"]]
- 005045e4 bytes b34e1d94
+ 00504624 bytes d74e1d94
- 00504620 ["INT_ADD", "register:40f0:8", ["const:504620:8", "const:4:8"]]
- 00504620 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00504660 ["INT_ADD", "register:40f0:8", ["const:504660:8", "const:4:8"]]
+ 00504660 ["CALL", null, ["callee:00c57fe0:8"]]
- 00504620 bytes 3c4e1d94
+ 00504660 bytes 604e1d94
- 005044f8 ["INT_ADD", "register:40f0:8", ["const:5044f8:8", "const:4:8"]]
- 005044f8 ["CALL", null, ["callee:00c59bb0:8"]]
+ 00504538 ["INT_ADD", "register:40f0:8", ["const:504538:8", "const:4:8"]]
+ 00504538 ["CALL", null, ["callee:00c59bb0:8"]]
- 005044f8 bytes 7a551d94
+ 00504538 bytes 9e551d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d382eebee4540b69fbee53a6a8d0a30"></a>

### [`00504680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/00504680.md) → [`005046c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/005046c0.md) _ZNK5Botan10Data_Store11get1_memvecERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`004aeca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.70% / 新版 97.70%

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
      "definition_site": "005047cc",
      "incomplete_value": false,
      "site": "005047d8",
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
            "const:de1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050478c",
      "incomplete_value": false,
      "site": "00504798",
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
            "const:e35:8"
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
      "definition_site": "00504808",
      "incomplete_value": true,
      "site": "00504814",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005047c8",
      "incomplete_value": true,
      "site": "005047d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00504804",
      "incomplete_value": false,
      "site": "00504814",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "005047c4",
      "incomplete_value": false,
      "site": "005047d4",
      "value": [
        "leaf",
        "const:535868:8"
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
      "005047cc",
      "PARAM",
      [
        "storage",
        "002bfe35",
        null,
        "string"
      ]
    ],
    [
      "00504804",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "00504808",
      "READ",
      [
        "storage",
        "00c9ad48",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005047cc",
      "PARAM",
      [
        "storage",
        "002bfde1",
        null,
        "string"
      ]
    ],
    [
      "00504804",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "00504808",
      "READ",
      [
        "storage",
        "00c9ae18",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00504798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/00504680.md#insn-00504798) · [`005047d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/00504680.md#insn-005047d4) · [`005046ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/00504680.md#insn-005046ac)
- 新版 [`005047d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/005046c0.md#insn-005047d8) · [`00504814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/005046c0.md#insn-00504814) · [`005046ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/005046c0.md#insn-005046ec)

~~~diff
- 00504798 ["INT_ADD", "register:40f0:8", ["const:504798:8", "const:4:8"]]
- 00504798 ["CALL", null, ["callee:00c58180:8"]]
+ 005047d8 ["INT_ADD", "register:40f0:8", ["const:5047d8:8", "const:4:8"]]
+ 005047d8 ["CALL", null, ["callee:00c58180:8"]]
- 00504798 bytes 464e1d94
+ 005047d8 bytes 6a4e1d94
- 005047d4 ["INT_ADD", "register:40f0:8", ["const:5047d4:8", "const:4:8"]]
- 005047d4 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00504814 ["INT_ADD", "register:40f0:8", ["const:504814:8", "const:4:8"]]
+ 00504814 ["CALL", null, ["callee:00c57fe0:8"]]
- 005047d4 bytes cf4d1d94
+ 00504814 bytes f34d1d94
- 005046ac ["INT_ADD", "register:40f0:8", ["const:5046ac:8", "const:4:8"]]
- 005046ac ["CALL", null, ["callee:00c59bb0:8"]]
+ 005046ec ["INT_ADD", "register:40f0:8", ["const:5046ec:8", "const:4:8"]]
+ 005046ec ["CALL", null, ["callee:00c59bb0:8"]]
- 005046ac bytes 0d551d94
+ 005046ec bytes 31551d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-584df4dcdc8d0636e7c5c418c718d12d"></a>

### [`00504834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/00504834.md) → [`00504874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/00504874.md) _ZNK5Botan10Data_Store11get1_uint32ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEj

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`004aeca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.44% / 新版 97.44%

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
      "definition_site": "0050495c",
      "incomplete_value": false,
      "site": "00504968",
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
            "const:5d2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050491c",
      "incomplete_value": false,
      "site": "00504928",
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
            "const:62e:8"
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
      "definition_site": "00504998",
      "incomplete_value": true,
      "site": "005049a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00504958",
      "incomplete_value": true,
      "site": "00504964",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00504994",
      "incomplete_value": false,
      "site": "005049a4",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "00504954",
      "incomplete_value": false,
      "site": "00504964",
      "value": [
        "leaf",
        "const:535868:8"
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
      "0050495c",
      "PARAM",
      [
        "storage",
        "002a562e",
        null,
        "string"
      ]
    ],
    [
      "00504994",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "00504998",
      "READ",
      [
        "storage",
        "00c9ad48",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050495c",
      "PARAM",
      [
        "storage",
        "002a55d2",
        null,
        "string"
      ]
    ],
    [
      "00504994",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "00504998",
      "READ",
      [
        "storage",
        "00c9ae18",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00504928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/00504834.md#insn-00504928) · [`00504964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/00504834.md#insn-00504964) · [`00504860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/00504834.md#insn-00504860)
- 新版 [`00504968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/00504874.md#insn-00504968) · [`005049a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/00504874.md#insn-005049a4) · [`005048a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/00504874.md#insn-005048a0)

~~~diff
- 00504928 ["INT_ADD", "register:40f0:8", ["const:504928:8", "const:4:8"]]
- 00504928 ["CALL", null, ["callee:00c58180:8"]]
+ 00504968 ["INT_ADD", "register:40f0:8", ["const:504968:8", "const:4:8"]]
+ 00504968 ["CALL", null, ["callee:00c58180:8"]]
- 00504928 bytes e24d1d94
+ 00504968 bytes 064e1d94
- 00504964 ["INT_ADD", "register:40f0:8", ["const:504964:8", "const:4:8"]]
- 00504964 ["CALL", null, ["callee:00c57fe0:8"]]
+ 005049a4 ["INT_ADD", "register:40f0:8", ["const:5049a4:8", "const:4:8"]]
+ 005049a4 ["CALL", null, ["callee:00c57fe0:8"]]
- 00504964 bytes 6b4d1d94
+ 005049a4 bytes 8f4d1d94
- 00504860 ["INT_ADD", "register:40f0:8", ["const:504860:8", "const:4:8"]]
- 00504860 ["CALL", null, ["callee:00c59bb0:8"]]
+ 005048a0 ["INT_ADD", "register:40f0:8", ["const:5048a0:8", "const:4:8"]]
+ 005048a0 ["CALL", null, ["callee:00c59bb0:8"]]
- 00504860 bytes a0541d94
+ 005048a0 bytes c4541d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afc076c74cff1d398ebcc56a5e615293"></a>

### [`00504e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/00504e10.md) → [`00504e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/00504e50.md) _ZN5Botan9create_dnERKNS_10Data_StoreE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0054924c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/0054924c.md) [`00549250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549250.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0054928c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00549/0054928c.md) [`00549290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00549/00549290.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00504e70",
      "incomplete_value": false,
      "site": "00504e80",
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
            "const:950:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00504e30",
      "incomplete_value": false,
      "site": "00504e40",
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
            "const:880:8"
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
      "definition_site": "00504eec",
      "incomplete_value": true,
      "site": "00504eec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00504eac",
      "incomplete_value": true,
      "site": "00504eac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00504e80",
      "DATA",
      [
        "storage",
        "00c6a880",
        null,
        "undefined *"
      ]
    ],
    [
      "00504eb8",
      "READ",
      [
        "storage",
        "00c6a8a0",
        null,
        "pointer"
      ]
    ],
    [
      "00504eb8",
      "READ",
      [
        "storage",
        "00c6a8a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00504e80",
      "DATA",
      [
        "storage",
        "00c6a950",
        null,
        "undefined *"
      ]
    ],
    [
      "00504eb8",
      "READ",
      [
        "storage",
        "00c6a970",
        null,
        "pointer"
      ]
    ],
    [
      "00504eb8",
      "READ",
      [
        "storage",
        "00c6a978",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00504e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/00504e10.md#insn-00504e30) · [`00504e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/00504e10.md#insn-00504e50) · [`00504e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/00504e10.md#insn-00504e7c)
- 新版 [`00504e70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/00504e50.md#insn-00504e70) · [`00504e90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/00504e50.md#insn-00504e90) · [`00504ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/00504e50.md#insn-00504ebc)

~~~diff
- 00504e30 ["COPY", "tmp:0:8", ["const:880:8"]]
- 00504e30 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00504e30 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00504e30 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00504e70 ["COPY", "tmp:0:8", ["const:950:8"]]
+ 00504e70 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00504e70 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00504e70 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00504e30 bytes 29012291
+ 00504e70 bytes 29412591
- 00504e50 ["INT_ADD", "register:40f0:8", ["const:504e50:8", "const:4:8"]]
- 00504e50 ["CALL", null, ["callee:00c59ba0:8"]]
+ 00504e90 ["INT_ADD", "register:40f0:8", ["const:504e90:8", "const:4:8"]]
+ 00504e90 ["CALL", null, ["callee:00c59ba0:8"]]
- 00504e50 bytes 20531d94
+ 00504e90 bytes 44531d94
- 00504e7c ["COPY", "register:0:8", ["register:4040:8"]]
- 00504e7c ["INT_ADD", "register:40f0:8", ["const:504e7c:8", "const:4:8"]]
- 00504e7c ["CALLIND", null, ["register:0:8"]]
+ 00504ebc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00504ebc ["INT_ADD", "register:40f0:8", ["const:504ebc:8", "const:4:8"]]
+ 00504ebc ["CALLIND", null, ["register:0:8"]]
- 00504e7c bytes 00013fd6
+ 00504ebc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9a4ddadcb2c362a2c6db2d90b3f66dc"></a>

### [`00505080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00505/00505080.md) → [`005050c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00505/005050c0.md) _ZN5Botan15create_alt_nameERKNS_10Data_StoreE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`00549354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549354.md) [`00549358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549358.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`00549394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00549/00549394.md) [`00549398`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00549/00549398.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.96% / 新版 97.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005050f0",
      "incomplete_value": false,
      "site": "005050f0",
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
            "const:9e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005050b0",
      "incomplete_value": false,
      "site": "005050b0",
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
            "const:910:8"
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
      "005050f0",
      "DATA",
      [
        "storage",
        "00c6a910",
        null,
        "undefined *"
      ]
    ],
    [
      "00505128",
      "READ",
      [
        "storage",
        "00c6a930",
        null,
        "pointer"
      ]
    ],
    [
      "00505128",
      "READ",
      [
        "storage",
        "00c6a938",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005050f0",
      "DATA",
      [
        "storage",
        "00c6a9e0",
        null,
        "undefined *"
      ]
    ],
    [
      "00505128",
      "READ",
      [
        "storage",
        "00c6aa00",
        null,
        "pointer"
      ]
    ],
    [
      "00505128",
      "READ",
      [
        "storage",
        "00c6aa08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005050a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00505/00505080.md#insn-005050a0) · [`005050c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00505/00505080.md#insn-005050c0) · [`005050ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00505/00505080.md#insn-005050ec)
- 新版 [`005050e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00505/005050c0.md#insn-005050e0) · [`00505100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00505/005050c0.md#insn-00505100) · [`0050512c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00505/005050c0.md#insn-0050512c)

~~~diff
- 005050a0 ["COPY", "tmp:0:8", ["const:910:8"]]
- 005050a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005050a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005050a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005050e0 ["COPY", "tmp:0:8", ["const:9e0:8"]]
+ 005050e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005050e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005050e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005050a0 bytes 29412491
+ 005050e0 bytes 29812791
- 005050c0 ["INT_ADD", "register:40f0:8", ["const:5050c0:8", "const:4:8"]]
- 005050c0 ["CALL", null, ["callee:00c59ba0:8"]]
+ 00505100 ["INT_ADD", "register:40f0:8", ["const:505100:8", "const:4:8"]]
+ 00505100 ["CALL", null, ["callee:00c59ba0:8"]]
- 005050c0 bytes 84521d94
+ 00505100 bytes a8521d94
- 005050ec ["COPY", "register:0:8", ["register:4040:8"]]
- 005050ec ["INT_ADD", "register:40f0:8", ["const:5050ec:8", "const:4:8"]]
- 005050ec ["CALLIND", null, ["register:0:8"]]
+ 0050512c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0050512c ["INT_ADD", "register:40f0:8", ["const:50512c:8", "const:4:8"]]
+ 0050512c ["CALLIND", null, ["register:0:8"]]
- 005050ec bytes 00013fd6
+ 0050512c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9791e6cc333c9fd616ac3e3af2b059a"></a>

### [`00505304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00505/00505304.md) → [`00505344`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00505/00505344.md) _ZN5Botan25key_constraints_to_stringENS_15Key_ConstraintsE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c59b20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59b20.md) · 呼出先 9件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00440f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00c59bf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59bf0.md) · 呼出先 9件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00440f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f9c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.80% / 新版 88.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 33件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005053b0",
      "incomplete_value": true,
      "site": "005053b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:87e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00505370",
      "incomplete_value": true,
      "site": "00505370",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8da:8"
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
      "definition_site": "005053b4",
      "incomplete_value": true,
      "site": "005053b4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00505374",
      "incomplete_value": true,
      "site": "00505374",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005053e8",
      "incomplete_value": true,
      "site": "005053e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b9d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005053a8",
      "incomplete_value": true,
      "site": "005053a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b6c:8"
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
      "005053a0",
      "READ",
      [
        "storage",
        "002a78da",
        null,
        "string"
      ]
    ],
    [
      "005053a4",
      "READ",
      [
        "storage",
        "002a78e0",
        null,
        "string"
      ]
    ],
    [
      "005053d0",
      "READ",
      [
        "storage",
        "002b2b6c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005053a0",
      "READ",
      [
        "storage",
        "002a787e",
        null,
        "string"
      ]
    ],
    [
      "005053a4",
      "READ",
      [
        "storage",
        "002a7884",
        null,
        "string"
      ]
    ],
    [
      "005053d0",
      "READ",
      [
        "storage",
        "002b2b9d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00505358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00505/00505304.md#insn-00505358) · [`00505380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00505/00505304.md#insn-00505380) · [`00505388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00505/00505304.md#insn-00505388)
- 新版 [`00505398`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00505/00505344.md#insn-00505398) · [`005053c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00505/00505344.md#insn-005053c0) · [`005053c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00505/00505344.md#insn-005053c8)

~~~diff
- 00505358 ["COPY", "tmp:0:8", ["const:8da:8"]]
- 00505358 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00505358 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00505358 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00505398 ["COPY", "tmp:0:8", ["const:87e:8"]]
+ 00505398 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00505398 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00505398 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00505358 bytes 29692391
+ 00505398 bytes 29f92191
- 00505380 ["INT_ADD", "register:40f0:8", ["const:505380:8", "const:4:8"]]
- 00505380 ["CALL", null, ["callee:00c57f60:8"]]
+ 005053c0 ["INT_ADD", "register:40f0:8", ["const:5053c0:8", "const:4:8"]]
+ 005053c0 ["CALL", null, ["callee:00c57f60:8"]]
- 00505380 bytes c44a1d94
+ 005053c0 bytes e84a1d94
- 00505388 ["COPY", "tmp:0:8", ["const:b6c:8"]]
- 00505388 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00505388 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00505388 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005053c8 ["COPY", "tmp:0:8", ["const:b9d:8"]]
+ 005053c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005053c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005053c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00505388 bytes 29b12d91
+ 005053c8 bytes 29752e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-635dfb4b912afcedf37489b6fbe6bfd7"></a>

### [`00505efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00505/00505efc.md) → [`00505f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00505/00505f3c.md) _ZN5Botan42verify_cert_constraints_valid_for_key_typeERKNS_10Public_KeyENS_15Key_ConstraintsE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59b30.md) · 呼出先 10件 [`004a684c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a684c.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)
- 新版 呼出元 1件 [`00c59c00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59c00.md) · 呼出先 10件 [`004a688c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a688c.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.58% / 新版 98.58%

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
      "definition_site": "005061f4",
      "incomplete_value": false,
      "site": "00506200",
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
            "const:109:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005061b4",
      "incomplete_value": false,
      "site": "005061c0",
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
            "const:156:8"
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
      "definition_site": "00506208",
      "incomplete_value": false,
      "site": "00506210",
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
            "const:6e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005061c8",
      "incomplete_value": false,
      "site": "005061d0",
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
            "const:744:8"
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
      "definition_site": "00506278",
      "incomplete_value": true,
      "site": "00506284",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00506238",
      "incomplete_value": true,
      "site": "00506244",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d88:8"
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
      "005061f4",
      "PARAM",
      [
        "storage",
        "002a0156",
        null,
        "string"
      ]
    ],
    [
      "00506208",
      "PARAM",
      [
        "storage",
        "002a6744",
        null,
        "string"
      ]
    ],
    [
      "00506274",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005061f4",
      "PARAM",
      [
        "storage",
        "002a0109",
        null,
        "string"
      ]
    ],
    [
      "00506208",
      "PARAM",
      [
        "storage",
        "002a66e8",
        null,
        "string"
      ]
    ],
    [
      "00506274",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005061c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00505/00505efc.md#insn-005061c0) · [`005061d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00505/00505efc.md#insn-005061d0) · [`00506204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00505/00505efc.md#insn-00506204)
- 新版 [`00506200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00505/00505f3c.md#insn-00506200) · [`00506210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00505/00505f3c.md#insn-00506210) · [`00506244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00505/00505f3c.md#insn-00506244)

~~~diff
- 005061c0 ["INT_ADD", "register:40f0:8", ["const:5061c0:8", "const:4:8"]]
- 005061c0 ["CALL", null, ["callee:00c58180:8"]]
+ 00506200 ["INT_ADD", "register:40f0:8", ["const:506200:8", "const:4:8"]]
+ 00506200 ["CALL", null, ["callee:00c58180:8"]]
- 005061c0 bytes bc471d94
+ 00506200 bytes e0471d94
- 005061d0 ["INT_ADD", "register:40f0:8", ["const:5061d0:8", "const:4:8"]]
- 005061d0 ["CALL", null, ["callee:00c58040:8"]]
+ 00506210 ["INT_ADD", "register:40f0:8", ["const:506210:8", "const:4:8"]]
+ 00506210 ["CALL", null, ["callee:00c58040:8"]]
- 005061d0 bytes 68471d94
+ 00506210 bytes 8c471d94
- 00506204 ["INT_ADD", "register:40f0:8", ["const:506204:8", "const:4:8"]]
- 00506204 ["CALL", null, ["callee:004a688c:8"]]
+ 00506244 ["INT_ADD", "register:40f0:8", ["const:506244:8", "const:4:8"]]
+ 00506244 ["CALL", null, ["callee:004a688c:8"]]
- 00506204 bytes 9281fe97
+ 00506244 bytes 9281fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-edffdb43043035414e81ff648a3ea6a0"></a>

### [`00506330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00506/00506330.md) → [`00506370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00506/00506370.md) _ZN5Botan11GeneralNameC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59b80.md) · 呼出先 12件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00c59c50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59c50.md) · 呼出先 12件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.14% / 新版 97.14%

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
      "definition_site": "005063b4",
      "incomplete_value": true,
      "site": "005063bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00506374",
      "incomplete_value": true,
      "site": "0050637c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00506598",
      "incomplete_value": false,
      "site": "005065a0",
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
            "const:d6c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00506558",
      "incomplete_value": false,
      "site": "00506560",
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
            "const:d3b:8"
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
      "definition_site": "005065d0",
      "incomplete_value": true,
      "site": "005065dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00506590",
      "incomplete_value": true,
      "site": "0050659c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0050639c",
      "READ",
      [
        "storage",
        "00c9b128",
        null,
        "pointer"
      ]
    ],
    [
      "005063bc",
      "DATA",
      [
        "storage",
        "00c680d0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00506598",
      "PARAM",
      [
        "storage",
        "002b1d3b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0050639c",
      "READ",
      [
        "storage",
        "00c9b1f8",
        null,
        "pointer"
      ]
    ],
    [
      "005063bc",
      "DATA",
      [
        "storage",
        "00c681a0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00506598",
      "PARAM",
      [
        "storage",
        "002b1d6c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00506560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00506/00506330.md#insn-00506560) · [`0050659c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00506/00506330.md#insn-0050659c) · [`0050635c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00506/00506330.md#insn-0050635c)
- 新版 [`005065a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00506/00506370.md#insn-005065a0) · [`005065dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00506/00506370.md#insn-005065dc) · [`0050639c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00506/00506370.md#insn-0050639c)

~~~diff
- 00506560 ["INT_ADD", "register:40f0:8", ["const:506560:8", "const:4:8"]]
- 00506560 ["CALL", null, ["callee:0043de18:8"]]
+ 005065a0 ["INT_ADD", "register:40f0:8", ["const:5065a0:8", "const:4:8"]]
+ 005065a0 ["CALL", null, ["callee:0043de18:8"]]
- 00506560 bytes 1edefc97
+ 005065a0 bytes 1edefc97
- 0050659c ["INT_ADD", "register:40f0:8", ["const:50659c:8", "const:4:8"]]
- 0050659c ["CALL", null, ["callee:00c57fe0:8"]]
+ 005065dc ["INT_ADD", "register:40f0:8", ["const:5065dc:8", "const:4:8"]]
+ 005065dc ["CALL", null, ["callee:00c57fe0:8"]]
- 0050659c bytes 5d461d94
+ 005065dc bytes 81461d94
- 0050635c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:128:8"]]
- 0050635c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050639c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1f8:8"]]
+ 0050639c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050635c bytes 089540f9
+ 0050639c bytes 08fd40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebf7f824aebee6a6993a490fb133e91f"></a>

### [`00506648`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00506/00506648.md) → [`00506688`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00506/00506688.md) _ZNK5Botan11GeneralName11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c594e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c594e0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c595b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c595b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

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
      "definition_site": "005066bc",
      "incomplete_value": true,
      "site": "005066d8",
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
                "const:da3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050667c",
      "incomplete_value": true,
      "site": "00506698",
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
                "const:df7:8"
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
      "definition_site": "00506704",
      "incomplete_value": true,
      "site": "00506710",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005066c4",
      "incomplete_value": true,
      "site": "005066d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fd0:8"
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
      "definition_site": "00506700",
      "incomplete_value": false,
      "site": "00506710",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "005066c0",
      "incomplete_value": false,
      "site": "005066d0",
      "value": [
        "leaf",
        "const:535868:8"
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
      "005066bc",
      "READ",
      [
        "storage",
        "002bedf7",
        null,
        "string"
      ]
    ],
    [
      "00506700",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "00506704",
      "READ",
      [
        "storage",
        "00c9afd0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005066bc",
      "READ",
      [
        "storage",
        "002beda3",
        null,
        "string"
      ]
    ],
    [
      "00506700",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "00506704",
      "READ",
      [
        "storage",
        "00c9b0a0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005066d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00506/00506648.md#insn-005066d0) · [`0050666c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00506/00506648.md#insn-0050666c) · [`00506674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00506/00506648.md#insn-00506674)
- 新版 [`00506710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00506/00506688.md#insn-00506710) · [`005066ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00506/00506688.md#insn-005066ac) · [`005066b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00506/00506688.md#insn-005066b4)

~~~diff
- 005066d0 ["INT_ADD", "register:40f0:8", ["const:5066d0:8", "const:4:8"]]
- 005066d0 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00506710 ["INT_ADD", "register:40f0:8", ["const:506710:8", "const:4:8"]]
+ 00506710 ["CALL", null, ["callee:00c57fe0:8"]]
- 005066d0 bytes 10461d94
+ 00506710 bytes 34461d94
- 0050666c ["INT_ADD", "register:40f0:8", ["const:50666c:8", "const:4:8"]]
- 0050666c ["CALL", null, ["callee:00c57fc0:8"]]
+ 005066ac ["INT_ADD", "register:40f0:8", ["const:5066ac:8", "const:4:8"]]
+ 005066ac ["CALL", null, ["callee:00c57fc0:8"]]
- 0050666c bytes 21461d94
+ 005066ac bytes 45461d94
- 00506674 ["COPY", "tmp:0:8", ["const:df7:8"]]
- 00506674 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00506674 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00506674 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005066b4 ["COPY", "tmp:0:8", ["const:da3:8"]]
+ 005066b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005066b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005066b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00506674 bytes 29dd3791
+ 005066b4 bytes 298d3691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3f667ced09717c28adc7452c6e620db"></a>

### [`00506718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00506/00506718.md) → [`00506758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00506/00506758.md) _ZN5Botan11GeneralName11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 29件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004518b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004518b0.md) [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md)
- 新版 呼出元 0件  · 呼出先 29件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004518f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004518f0.md) [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 94.50% / 新版 94.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `store_destination` 1件, `store_value` 4件

アドレスに依存する影響 `call_argument_candidate` 4件, `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005067e4",
      "incomplete_value": true,
      "site": "005067e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005067a4",
      "incomplete_value": true,
      "site": "005067a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00506868",
      "incomplete_value": true,
      "site": "00506870",
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
      "definition_site": "00506828",
      "incomplete_value": true,
      "site": "00506830",
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
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00506878",
      "incomplete_value": true,
      "site": "00506878",
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
                "const:b0:8"
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
      "definition_site": "00506838",
      "incomplete_value": true,
      "site": "00506838",
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
                "const:b0:8"
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
      "005067cc",
      "READ",
      [
        "storage",
        "00c9b0d0",
        null,
        "pointer"
      ]
    ],
    [
      "005067e4",
      "DATA",
      [
        "storage",
        "00c679f8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00506850",
      "PARAM",
      [
        "storage",
        "002ba32a",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005067cc",
      "READ",
      [
        "storage",
        "00c9b1a0",
        null,
        "pointer"
      ]
    ],
    [
      "005067e4",
      "DATA",
      [
        "storage",
        "00c67ac8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00506850",
      "PARAM",
      [
        "storage",
        "002ba2d6",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005067d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00506/00506718.md#insn-005067d8) · [`005067e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00506/00506718.md#insn-005067e4) · [`005067f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00506/00506718.md#insn-005067f8)
- 新版 [`00506818`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00506/00506758.md#insn-00506818) · [`00506824`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00506/00506758.md#insn-00506824) · [`00506838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00506/00506758.md#insn-00506838)

~~~diff
- 005067d8 ["INT_ADD", "register:40f0:8", ["const:5067d8:8", "const:4:8"]]
- 005067d8 ["CALL", null, ["callee:00c59a70:8"]]
+ 00506818 ["INT_ADD", "register:40f0:8", ["const:506818:8", "const:4:8"]]
+ 00506818 ["CALL", null, ["callee:00c59a70:8"]]
- 005067d8 bytes 724c1d94
+ 00506818 bytes 964c1d94
- 005067e4 ["INT_ADD", "register:40f0:8", ["const:5067e4:8", "const:4:8"]]
- 005067e4 ["CALL", null, ["callee:00c58280:8"]]
+ 00506824 ["INT_ADD", "register:40f0:8", ["const:506824:8", "const:4:8"]]
+ 00506824 ["CALL", null, ["callee:00c58280:8"]]
- 005067e4 bytes 73461d94
+ 00506824 bytes 97461d94
- 005067f8 ["INT_ADD", "register:40f0:8", ["const:5067f8:8", "const:4:8"]]
- 005067f8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00506838 ["INT_ADD", "register:40f0:8", ["const:506838:8", "const:4:8"]]
+ 00506838 ["CALL", null, ["callee:00c57f80:8"]]
- 005067f8 bytes ae451d94
+ 00506838 bytes d2451d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e223700c26c048f0d7b5af805a69ce9d"></a>

### [`00506f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00506/00506f90.md) → [`00506fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00506/00506fd0.md) _ZN5Botan7X509_DN11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`004ffe20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ffe20.md) [`005132b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00513/005132b0.md) [`00c59b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59b40.md) · 呼出先 12件 [`004a5980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5980.md) [`00548e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548e68.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md)
- 新版 呼出元 3件 [`004ffe60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ffe60.md) [`005132f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00513/005132f0.md) [`00c59c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59c10.md) · 呼出先 12件 [`004a59c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a59c0.md) [`00548ea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00548/00548ea8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.85% / 新版 95.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00507064",
      "incomplete_value": true,
      "site": "00507064",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00507024",
      "incomplete_value": true,
      "site": "00507024",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0050719c",
      "incomplete_value": true,
      "site": "0050719c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050715c",
      "incomplete_value": true,
      "site": "0050715c",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 19,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00507224",
      "incomplete_value": true,
      "site": "00507224",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005071e4",
      "incomplete_value": true,
      "site": "005071e4",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 26,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00507054",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "0050718c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "00507214",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00507054",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "0050718c",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00507214",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00506fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00506/00506f90.md#insn-00506fe4) · [`00507024`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00506/00506f90.md#insn-00507024) · [`0050715c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00506/00506f90.md#insn-0050715c)
- 新版 [`00507024`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00506/00506fd0.md#insn-00507024) · [`00507064`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00506/00506fd0.md#insn-00507064) · [`0050719c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00506/00506fd0.md#insn-0050719c)

~~~diff
- 00506fe4 ["INT_ADD", "register:40f0:8", ["const:506fe4:8", "const:4:8"]]
- 00506fe4 ["CALL", null, ["callee:00c587e0:8"]]
+ 00507024 ["INT_ADD", "register:40f0:8", ["const:507024:8", "const:4:8"]]
+ 00507024 ["CALL", null, ["callee:00c587e0:8"]]
- 00506fe4 bytes cb451d94
+ 00507024 bytes ef451d94
- 00507024 ["COPY", "register:0:8", ["register:4048:8"]]
- 00507024 ["INT_ADD", "register:40f0:8", ["const:507024:8", "const:4:8"]]
- 00507024 ["CALLIND", null, ["register:0:8"]]
+ 00507064 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00507064 ["INT_ADD", "register:40f0:8", ["const:507064:8", "const:4:8"]]
+ 00507064 ["CALLIND", null, ["register:0:8"]]
- 00507024 bytes 20013fd6
+ 00507064 bytes 20013fd6
- 0050715c ["COPY", "register:0:8", ["register:4048:8"]]
- 0050715c ["INT_ADD", "register:40f0:8", ["const:50715c:8", "const:4:8"]]
- 0050715c ["CALLIND", null, ["register:0:8"]]
+ 0050719c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050719c ["INT_ADD", "register:40f0:8", ["const:50719c:8", "const:4:8"]]
+ 0050719c ["CALLIND", null, ["register:0:8"]]
- 0050715c bytes 20013fd6
+ 0050719c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bec1c96f4df0ef1fb006217a476bdf10"></a>

### [`0050736c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00507/0050736c.md) → [`005073ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00507/005073ac.md) _ZNK5Botan11GeneralName7matchesERKNS_16X509_CertificateE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59b50.md) · 呼出先 23件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00440f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f5c.md) [`004518b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004518b0.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00507ab4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00507/00507ab4.md)
- 新版 呼出元 1件 [`00c59c20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59c20.md) · 呼出先 23件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00440f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f9c.md) [`004518f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004518f0.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00507af4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00507/00507af4.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 95.49% / 新版 95.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 9件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050747c",
      "incomplete_value": true,
      "site": "0050747c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0050743c",
      "incomplete_value": true,
      "site": "0050743c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0050747c",
      "incomplete_value": true,
      "site": "0050747c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:208:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050743c",
      "incomplete_value": true,
      "site": "0050743c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:138:8"
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
      "definition_site": "005074fc",
      "incomplete_value": true,
      "site": "005074fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005074bc",
      "incomplete_value": true,
      "site": "005074bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0050745c",
      "READ",
      [
        "storage",
        "00c9b130",
        null,
        "pointer"
      ]
    ],
    [
      "00507460",
      "READ",
      [
        "storage",
        "00c9b138",
        null,
        "pointer"
      ]
    ],
    [
      "0050747c",
      "DATA",
      [
        "storage",
        "00c6a990",
        null,
        "undefined1[88]"
      ]
    ]
  ],
  "added": [
    [
      "0050745c",
      "READ",
      [
        "storage",
        "00c9b200",
        null,
        "pointer"
      ]
    ],
    [
      "00507460",
      "READ",
      [
        "storage",
        "00c9b208",
        null,
        "pointer"
      ]
    ],
    [
      "0050747c",
      "DATA",
      [
        "storage",
        "00c6aa60",
        null,
        "undefined1[88]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005073b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00507/0050736c.md#insn-005073b0) · [`005073bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00507/0050736c.md#insn-005073bc) · [`0050741c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00507/0050736c.md#insn-0050741c)
- 新版 [`005073f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00507/005073ac.md#insn-005073f0) · [`005073fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00507/005073ac.md#insn-005073fc) · [`0050745c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00507/005073ac.md#insn-0050745c)

~~~diff
- 005073b0 ["INT_ADD", "register:40f0:8", ["const:5073b0:8", "const:4:8"]]
- 005073b0 ["CALL", null, ["callee:00c59ac0:8"]]
+ 005073f0 ["INT_ADD", "register:40f0:8", ["const:5073f0:8", "const:4:8"]]
+ 005073f0 ["CALL", null, ["callee:00c59ac0:8"]]
- 005073b0 bytes 90491d94
+ 005073f0 bytes b4491d94
- 005073bc ["INT_ADD", "register:40f0:8", ["const:5073bc:8", "const:4:8"]]
- 005073bc ["CALL", null, ["callee:00c59ac0:8"]]
+ 005073fc ["INT_ADD", "register:40f0:8", ["const:5073fc:8", "const:4:8"]]
+ 005073fc ["CALL", null, ["callee:00c59ac0:8"]]
- 005073bc bytes 8d491d94
+ 005073fc bytes b1491d94
- 0050741c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:130:8"]]
- 0050741c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050745c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:200:8"]]
+ 0050745c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050741c bytes 089940f9
+ 0050745c bytes 080141f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-898616a741295231f3771a447745ab31"></a>

### [`00507acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00507/00507acc.md) → [`00507b0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00507/00507b0c.md) _ZNK5Botan11GeneralName11matches_dnsERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0050736c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00507/0050736c.md) · 呼出先 9件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`005073ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00507/005073ac.md) · 呼出先 9件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.49% / 新版 99.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00507c18",
      "incomplete_value": false,
      "site": "00507c28",
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
      "definition_site": "00507bd8",
      "incomplete_value": false,
      "site": "00507be8",
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
      "00507c18",
      "PARAM",
      [
        "storage",
        "002a63eb",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00507c18",
      "PARAM",
      [
        "storage",
        "002a638f",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00507be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00507/00507acc.md#insn-00507be8) · [`00507b64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00507/00507acc.md#insn-00507b64) · [`00507bd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00507/00507acc.md#insn-00507bd8)
- 新版 [`00507c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00507/00507b0c.md#insn-00507c28) · [`00507ba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00507/00507b0c.md#insn-00507ba4) · [`00507c18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00507/00507b0c.md#insn-00507c18)

~~~diff
- 00507be8 ["INT_ADD", "register:40f0:8", ["const:507be8:8", "const:4:8"]]
- 00507be8 ["CALL", null, ["callee:00c58180:8"]]
+ 00507c28 ["INT_ADD", "register:40f0:8", ["const:507c28:8", "const:4:8"]]
+ 00507c28 ["CALL", null, ["callee:00c58180:8"]]
- 00507be8 bytes 32411d94
+ 00507c28 bytes 56411d94
- 00507b64 ["INT_ADD", "register:40f0:8", ["const:507b64:8", "const:4:8"]]
- 00507b64 ["CALL", null, ["callee:00c58120:8"]]
+ 00507ba4 ["INT_ADD", "register:40f0:8", ["const:507ba4:8", "const:4:8"]]
+ 00507ba4 ["CALL", null, ["callee:00c58120:8"]]
- 00507b64 bytes 3b411d94
+ 00507ba4 bytes 5f411d94
- 00507bd8 ["COPY", "tmp:0:8", ["const:3eb:8"]]
- 00507bd8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00507bd8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00507bd8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00507c18 ["COPY", "tmp:0:8", ["const:38f:8"]]
+ 00507c18 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00507c18 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00507c18 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00507bd8 bytes 00ac0f91
+ 00507c18 bytes 003c0e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b470ddcac906cd87bceb796771f1e738"></a>

### [`00507fa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00507/00507fa8.md) → [`00507fe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00507/00507fe8.md) _ZNK5Botan11GeneralName10matches_dnERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0050736c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00507/0050736c.md) · 呼出先 13件 [`005085bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00508/005085bc.md) [`00508c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00508/00508c28.md) [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md) [`00549668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549668.md) [`005496c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/005496c8.md)
- 新版 呼出元 1件 [`005073ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00507/005073ac.md) · 呼出先 13件 [`005085fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/005085fc.md) [`00508c68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/00508c68.md) [`0053afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053afd0.md) [`005496a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00549/005496a8.md) [`00549708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00549/00549708.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 94.66% / 新版 94.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00508058",
      "incomplete_value": true,
      "site": "00508058",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00508018",
      "incomplete_value": true,
      "site": "00508018",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00508064",
      "incomplete_value": true,
      "site": "00508064",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00508024",
      "incomplete_value": true,
      "site": "00508024",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00508254",
      "incomplete_value": true,
      "site": "0050825c",
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
      "definition_site": "00508214",
      "incomplete_value": true,
      "site": "0050821c",
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
      "00508040",
      "READ",
      [
        "storage",
        "00c9b0d0",
        null,
        "pointer"
      ]
    ],
    [
      "00508058",
      "DATA",
      [
        "storage",
        "00c679f8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00508064",
      "DATA",
      [
        "storage",
        "00c679f8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00508040",
      "READ",
      [
        "storage",
        "00c9b1a0",
        null,
        "pointer"
      ]
    ],
    [
      "00508058",
      "DATA",
      [
        "storage",
        "00c67ac8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00508064",
      "DATA",
      [
        "storage",
        "00c67ac8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005081dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00507/00507fa8.md#insn-005081dc) · [`005081f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00507/00507fa8.md#insn-005081f8) · [`00507fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00507/00507fa8.md#insn-00507fe0)
- 新版 [`0050821c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00507/00507fe8.md#insn-0050821c) · [`00508238`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00507/00507fe8.md#insn-00508238) · [`00508020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00507/00507fe8.md#insn-00508020)

~~~diff
- 005081dc ["INT_ADD", "register:40f0:8", ["const:5081dc:8", "const:4:8"]]
- 005081dc ["CALL", null, ["callee:00c57f80:8"]]
+ 0050821c ["INT_ADD", "register:40f0:8", ["const:50821c:8", "const:4:8"]]
+ 0050821c ["CALL", null, ["callee:00c57f80:8"]]
- 005081dc bytes 353f1d94
+ 0050821c bytes 593f1d94
- 005081f8 ["INT_ADD", "register:40f0:8", ["const:5081f8:8", "const:4:8"]]
- 005081f8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00508238 ["INT_ADD", "register:40f0:8", ["const:508238:8", "const:4:8"]]
+ 00508238 ["CALL", null, ["callee:00c57f80:8"]]
- 005081f8 bytes 2e3f1d94
+ 00508238 bytes 523f1d94
- 00507fe0 ["INT_ADD", "register:40f0:8", ["const:507fe0:8", "const:4:8"]]
- 00507fe0 ["CALL", null, ["callee:005085fc:8"]]
+ 00508020 ["INT_ADD", "register:40f0:8", ["const:508020:8", "const:4:8"]]
+ 00508020 ["CALL", null, ["callee:005085fc:8"]]
- 00507fe0 bytes 77010094
+ 00508020 bytes 77010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5d8a2c73621d81260e287dc33c8d662"></a>

### [`00508364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00508/00508364.md) → [`005083a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/005083a4.md) _ZNK5Botan11GeneralName10matches_ipERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0050736c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00507/0050736c.md) · 呼出先 12件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00486d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486d78.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00547b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547b6c.md) [`00547b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547b70.md)
- 新版 呼出元 1件 [`005073ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00507/005073ac.md) · 呼出先 12件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00486db8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00486/00486db8.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00547bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00547/00547bac.md) [`00547bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00547/00547bb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.46% / 新版 96.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005083d8",
      "incomplete_value": false,
      "site": "005083e0",
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
            "const:780:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00508398",
      "incomplete_value": false,
      "site": "005083a0",
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
            "const:6b0:8"
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
      "definition_site": "00508504",
      "incomplete_value": false,
      "site": "0050850c",
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
            "const:112:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005084c4",
      "incomplete_value": false,
      "site": "005084cc",
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
            "const:15f:8"
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
      "definition_site": "0050853c",
      "incomplete_value": true,
      "site": "00508548",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005084fc",
      "incomplete_value": true,
      "site": "00508508",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "005083e0",
      "DATA",
      [
        "storage",
        "00c6a6b0",
        null,
        "undefined *"
      ]
    ],
    [
      "00508428",
      "READ",
      [
        "storage",
        "00c6a6d0",
        null,
        "pointer"
      ]
    ],
    [
      "00508428",
      "READ",
      [
        "storage",
        "00c6a6d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005083e0",
      "DATA",
      [
        "storage",
        "00c6a780",
        null,
        "undefined *"
      ]
    ],
    [
      "00508428",
      "READ",
      [
        "storage",
        "00c6a7a0",
        null,
        "pointer"
      ]
    ],
    [
      "00508428",
      "READ",
      [
        "storage",
        "00c6a7a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005084cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00508/00508364.md#insn-005084cc) · [`00508508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00508/00508364.md#insn-00508508) · [`00508390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00508/00508364.md#insn-00508390)
- 新版 [`0050850c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/005083a4.md#insn-0050850c) · [`00508548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/005083a4.md#insn-00508548) · [`005083d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/005083a4.md#insn-005083d0)

~~~diff
- 005084cc ["INT_ADD", "register:40f0:8", ["const:5084cc:8", "const:4:8"]]
- 005084cc ["CALL", null, ["callee:0043de18:8"]]
+ 0050850c ["INT_ADD", "register:40f0:8", ["const:50850c:8", "const:4:8"]]
+ 0050850c ["CALL", null, ["callee:0043de18:8"]]
- 005084cc bytes 43d6fc97
+ 0050850c bytes 43d6fc97
- 00508508 ["INT_ADD", "register:40f0:8", ["const:508508:8", "const:4:8"]]
- 00508508 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00508548 ["INT_ADD", "register:40f0:8", ["const:508548:8", "const:4:8"]]
+ 00508548 ["CALL", null, ["callee:00c57fe0:8"]]
- 00508508 bytes 823e1d94
+ 00508548 bytes a63e1d94
- 00508390 ["INT_ADD", "register:40f0:8", ["const:508390:8", "const:4:8"]]
- 00508390 ["CALL", null, ["callee:00c599d0:8"]]
+ 005083d0 ["INT_ADD", "register:40f0:8", ["const:5083d0:8", "const:4:8"]]
+ 005083d0 ["CALL", null, ["callee:00c599d0:8"]]
- 00508390 bytes 5c451d94
+ 005083d0 bytes 80451d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-045da3ab2ee668d151d642edb1397870"></a>

### [`005085bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00508/005085bc.md) → [`005085fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/005085fc.md) FUN_005085fc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`004ffaac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ffaac.md) [`00507fa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00507/00507fa8.md) · 呼出先 4件 [`00548258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548258.md) [`00c581e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581e0.md) [`00c581f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581f0.md) [`00c58430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58430.md)
- 新版 呼出元 2件 [`004ffaec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ffaec.md) [`00507fe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00507/00507fe8.md) · 呼出先 4件 [`00548298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00548/00548298.md) [`00c582b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c582b0.md) [`00c582c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c582c0.md) [`00c58500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58500.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 78.08% / 新版 78.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050864c",
      "incomplete_value": true,
      "site": "0050864c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050860c",
      "incomplete_value": true,
      "site": "0050860c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:68:8"
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
      "definition_site": "00508650",
      "incomplete_value": true,
      "site": "00508650",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00508610",
      "incomplete_value": true,
      "site": "00508610",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00508648",
      "incomplete_value": true,
      "site": "00508658",
      "value": [
        "LOAD",
        "8",
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
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00508608",
      "incomplete_value": true,
      "site": "00508618",
      "value": [
        "LOAD",
        "8",
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
      "00508624",
      "READ",
      [
        "storage",
        "00c9ac18",
        null,
        "pointer"
      ]
    ],
    [
      "00508630",
      "READ",
      [
        "storage",
        "00c9ac10",
        null,
        "pointer"
      ]
    ],
    [
      "00508648",
      "READ",
      [
        "storage",
        "00c930f8",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "00508624",
      "READ",
      [
        "storage",
        "00c9ace8",
        null,
        "pointer"
      ]
    ],
    [
      "00508630",
      "READ",
      [
        "storage",
        "00c9ace0",
        null,
        "pointer"
      ]
    ],
    [
      "00508648",
      "READ",
      [
        "storage",
        "00c931c8",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005085e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00508/005085bc.md#insn-005085e4) · [`005085ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00508/005085bc.md#insn-005085ec) · [`005085f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00508/005085bc.md#insn-005085f0)
- 新版 [`00508624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/005085fc.md#insn-00508624) · [`00508630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/005085fc.md#insn-00508630)

~~~diff
- 005085e4 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:c18:8"]]
- 005085e4 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00508624 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:ce8:8"]]
+ 00508624 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
- 005085e4 bytes 390f46f9
+ 00508624 bytes 397746f9
- 005085ec ["COPY", "register:40e0:8", ["register:4000:8"]]
- 005085ec bytes fc0300aa
- 005085f0 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:c10:8"]]
- 005085f0 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00508630 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:ce0:8"]]
+ 00508630 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 005085f0 bytes 180b46f9
+ 00508630 bytes 187346f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-841d66b11c5624108cee30ff5d0f85c2"></a>

### [`00508728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00508/00508728.md) → [`00508768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/00508768.md) _ZN5BotanrsERNSt6__ndk113basic_istreamIcNS0_11char_traitsIcEEEERNS_7X509_DNE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59990.md) · 呼出先 12件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00515370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/00515370.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00c59a60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59a60.md) · 呼出先 12件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005153b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/005153b0.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.02% / 新版 99.02%

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
      "definition_site": "00508a4c",
      "incomplete_value": false,
      "site": "00508a54",
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
            "const:6f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00508a0c",
      "incomplete_value": false,
      "site": "00508a14",
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
            "const:754:8"
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
      "definition_site": "00508a84",
      "incomplete_value": true,
      "site": "00508a90",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00508a44",
      "incomplete_value": true,
      "site": "00508a50",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00508a80",
      "incomplete_value": false,
      "site": "00508a90",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "00508a40",
      "incomplete_value": false,
      "site": "00508a50",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "ordinal": 18,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00508a4c",
      "PARAM",
      [
        "storage",
        "002a6754",
        null,
        "string"
      ]
    ],
    [
      "00508a80",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "00508a84",
      "READ",
      [
        "storage",
        "00c9ad30",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00508a4c",
      "PARAM",
      [
        "storage",
        "002a66f8",
        null,
        "string"
      ]
    ],
    [
      "00508a80",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "00508a84",
      "READ",
      [
        "storage",
        "00c9ae00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00508a14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00508/00508728.md#insn-00508a14) · [`00508a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00508/00508728.md#insn-00508a50) · [`005087b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00508/00508728.md#insn-005087b4)
- 新版 [`00508a54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/00508768.md#insn-00508a54) · [`00508a90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/00508768.md#insn-00508a90) · [`005087f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/00508768.md#insn-005087f4)

~~~diff
- 00508a14 ["INT_ADD", "register:40f0:8", ["const:508a14:8", "const:4:8"]]
- 00508a14 ["CALL", null, ["callee:0043de18:8"]]
+ 00508a54 ["INT_ADD", "register:40f0:8", ["const:508a54:8", "const:4:8"]]
+ 00508a54 ["CALL", null, ["callee:0043de18:8"]]
- 00508a14 bytes f1d4fc97
+ 00508a54 bytes f1d4fc97
- 00508a50 ["INT_ADD", "register:40f0:8", ["const:508a50:8", "const:4:8"]]
- 00508a50 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00508a90 ["INT_ADD", "register:40f0:8", ["const:508a90:8", "const:4:8"]]
+ 00508a90 ["CALL", null, ["callee:00c57fe0:8"]]
- 00508a50 bytes 303d1d94
+ 00508a90 bytes 543d1d94
- 005087b4 ["INT_ADD", "register:40f0:8", ["const:5087b4:8", "const:4:8"]]
- 005087b4 ["CALL", null, ["callee:005153b0:8"]]
+ 005087f4 ["INT_ADD", "register:40f0:8", ["const:5087f4:8", "const:4:8"]]
+ 005087f4 ["CALL", null, ["callee:005153b0:8"]]
- 005087b4 bytes ef320094
+ 005087f4 bytes ef320094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ac495d7ed5866ad22b5ade321b7bbe3"></a>

### [`00508c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00508/00508c28.md) → [`00508c68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/00508c68.md) FUN_00508c68

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00507fa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00507/00507fa8.md) · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00507fe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00507/00507fe8.md) · 呼出先 6件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00535bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bac.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00508ca0",
      "incomplete_value": true,
      "site": "00508ca4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00508c60",
      "incomplete_value": true,
      "site": "00508c64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00508c90",
      "READ",
      [
        "storage",
        "00c9ad40",
        null,
        "pointer"
      ]
    ],
    [
      "00508ca4",
      "DATA",
      [
        "storage",
        "00c66288",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00508c90",
      "READ",
      [
        "storage",
        "00c9ae10",
        null,
        "pointer"
      ]
    ],
    [
      "00508ca4",
      "DATA",
      [
        "storage",
        "00c66358",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00508c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00508/00508c28.md#insn-00508c50) · [`00508c78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00508/00508c28.md#insn-00508c78) · [`00508c90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00508/00508c28.md#insn-00508c90)
- 新版 [`00508c90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/00508c68.md#insn-00508c90) · [`00508cb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/00508c68.md#insn-00508cb8) · [`00508cd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/00508c68.md#insn-00508cd0)

~~~diff
- 00508c50 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d40:8"]]
- 00508c50 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00508c90 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e10:8"]]
+ 00508c90 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00508c50 bytes 08a146f9
+ 00508c90 bytes 080947f9
- 00508c78 ["INT_ADD", "register:40f0:8", ["const:508c78:8", "const:4:8"]]
- 00508c78 ["CALL", null, ["callee:00c57f60:8"]]
+ 00508cb8 ["INT_ADD", "register:40f0:8", ["const:508cb8:8", "const:4:8"]]
+ 00508cb8 ["CALL", null, ["callee:00c57f60:8"]]
- 00508c78 bytes 863c1d94
+ 00508cb8 bytes aa3c1d94
- 00508c90 ["INT_ADD", "register:40f0:8", ["const:508c90:8", "const:4:8"]]
- 00508c90 ["CALL", null, ["callee:00c580d0:8"]]
+ 00508cd0 ["INT_ADD", "register:40f0:8", ["const:508cd0:8", "const:4:8"]]
+ 00508cd0 ["CALL", null, ["callee:00c580d0:8"]]
- 00508c90 bytes dc3c1d94
+ 00508cd0 bytes 003d1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10cd0c1dfe9b6d12d3f2bcc75886d06c"></a>

### [`00508d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00508/00508d48.md) → [`00508d88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/00508d88.md) _ZN5Botan14GeneralSubtreeC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 14件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.63% / 新版 96.63%

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
      "definition_site": "00508dd8",
      "incomplete_value": true,
      "site": "00508dd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00508d98",
      "incomplete_value": true,
      "site": "00508d98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00508dd8",
      "incomplete_value": true,
      "site": "00508dd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00508d98",
      "incomplete_value": true,
      "site": "00508d98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0050907c",
      "incomplete_value": false,
      "site": "00509084",
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
            "const:d6c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050903c",
      "incomplete_value": false,
      "site": "00509044",
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
            "const:d3b:8"
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
      "00508db4",
      "READ",
      [
        "storage",
        "00c9b150",
        null,
        "pointer"
      ]
    ],
    [
      "00508dbc",
      "READ",
      [
        "storage",
        "00c9b128",
        null,
        "pointer"
      ]
    ],
    [
      "00508dd8",
      "DATA",
      [
        "storage",
        "00c68118",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00508db4",
      "READ",
      [
        "storage",
        "00c9b220",
        null,
        "pointer"
      ]
    ],
    [
      "00508dbc",
      "READ",
      [
        "storage",
        "00c9b1f8",
        null,
        "pointer"
      ]
    ],
    [
      "00508dd8",
      "DATA",
      [
        "storage",
        "00c681e8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00509044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00508/00508d48.md#insn-00509044) · [`00509080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00508/00508d48.md#insn-00509080) · [`00508d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00508/00508d48.md#insn-00508d74)
- 新版 [`00509084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/00508d88.md#insn-00509084) · [`005090c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/00508d88.md#insn-005090c0) · [`00508db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/00508d88.md#insn-00508db4)

~~~diff
- 00509044 ["INT_ADD", "register:40f0:8", ["const:509044:8", "const:4:8"]]
- 00509044 ["CALL", null, ["callee:0043de18:8"]]
+ 00509084 ["INT_ADD", "register:40f0:8", ["const:509084:8", "const:4:8"]]
+ 00509084 ["CALL", null, ["callee:0043de18:8"]]
- 00509044 bytes 65d3fc97
+ 00509084 bytes 65d3fc97
- 00509080 ["INT_ADD", "register:40f0:8", ["const:509080:8", "const:4:8"]]
- 00509080 ["CALL", null, ["callee:00c57fe0:8"]]
+ 005090c0 ["INT_ADD", "register:40f0:8", ["const:5090c0:8", "const:4:8"]]
+ 005090c0 ["CALL", null, ["callee:00c57fe0:8"]]
- 00509080 bytes a43b1d94
+ 005090c0 bytes c83b1d94
- 00508d74 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:150:8"]]
- 00508d74 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00508db4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:220:8"]]
+ 00508db4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00508d74 bytes 08a940f9
+ 00508db4 bytes 081141f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0b44e635ac2285c5674b41f7fbeb87b"></a>

### [`0050916c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/0050916c.md) → [`005091ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/005091ac.md) _ZNK5Botan14GeneralSubtree11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 77.50% / 新版 77.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005091ec",
      "incomplete_value": true,
      "site": "00509200",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005091ac",
      "incomplete_value": true,
      "site": "005091c0",
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
                "const:6d:8"
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
      "definition_site": "005091f0",
      "incomplete_value": true,
      "site": "00509204",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005091b0",
      "incomplete_value": true,
      "site": "005091c4",
      "value": [
        "LOAD",
        "8",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005091f4",
      "incomplete_value": true,
      "site": "00509208",
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
                "const:2e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005091b4",
      "incomplete_value": true,
      "site": "005091c8",
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
                "const:2a0:8"
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
      "005091ec",
      "READ",
      [
        "storage",
        "002a206d",
        null,
        "string"
      ]
    ],
    [
      "005091f0",
      "READ",
      [
        "storage",
        "002a207d",
        null,
        "string"
      ]
    ],
    [
      "005091f4",
      "READ",
      [
        "storage",
        "002c22a0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005091ec",
      "READ",
      [
        "storage",
        "002a2020",
        null,
        "string"
      ]
    ],
    [
      "005091f0",
      "READ",
      [
        "storage",
        "002a2030",
        null,
        "string"
      ]
    ],
    [
      "005091f4",
      "READ",
      [
        "storage",
        "002c22e0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00509204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/0050916c.md#insn-00509204) · [`00509190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/0050916c.md#insn-00509190) · [`0050919c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/0050916c.md#insn-0050919c)
- 新版 [`00509244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/005091ac.md#insn-00509244) · [`005091d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/005091ac.md#insn-005091d0) · [`005091dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/005091ac.md#insn-005091dc)

~~~diff
- 00509204 ["INT_ADD", "register:40f0:8", ["const:509204:8", "const:4:8"]]
- 00509204 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00509244 ["INT_ADD", "register:40f0:8", ["const:509244:8", "const:4:8"]]
+ 00509244 ["CALL", null, ["callee:00c57fe0:8"]]
- 00509204 bytes 433b1d94
+ 00509244 bytes 673b1d94
- 00509190 ["INT_ADD", "register:40f0:8", ["const:509190:8", "const:4:8"]]
- 00509190 ["CALL", null, ["callee:00c57fc0:8"]]
+ 005091d0 ["INT_ADD", "register:40f0:8", ["const:5091d0:8", "const:4:8"]]
+ 005091d0 ["CALL", null, ["callee:00c57fc0:8"]]
- 00509190 bytes 583b1d94
+ 005091d0 bytes 7c3b1d94
- 0050919c ["INT_ADD", "register:40f0:8", ["const:50919c:8", "const:4:8"]]
- 0050919c ["CALL", null, ["callee:00c57f60:8"]]
+ 005091dc ["INT_ADD", "register:40f0:8", ["const:5091dc:8", "const:4:8"]]
+ 005091dc ["CALL", null, ["callee:00c57f60:8"]]
- 0050919c bytes 3d3b1d94
+ 005091dc bytes 613b1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-974ab0f1caff7355a3e94068ae239933"></a>

### [`00509254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/00509254.md) → [`00509294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/00509294.md) _ZN5Botan14GeneralSubtree11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59b90.md) · 呼出先 11件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`00c59c60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59c60.md) · 呼出先 11件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.53% / 新版 97.53%

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
      "definition_site": "0050933c",
      "incomplete_value": true,
      "site": "0050933c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005092fc",
      "incomplete_value": true,
      "site": "005092fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0050938c",
      "incomplete_value": false,
      "site": "00509394",
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
      "definition_site": "0050934c",
      "incomplete_value": false,
      "site": "00509354",
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
            "const:cad:8"
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
      "definition_site": "005093c4",
      "incomplete_value": true,
      "site": "005093d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00509384",
      "incomplete_value": true,
      "site": "00509390",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0050932c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "0050938c",
      "PARAM",
      [
        "storage",
        "002a8cad",
        null,
        "string"
      ]
    ],
    [
      "005093c0",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0050932c",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "0050938c",
      "PARAM",
      [
        "storage",
        "002a8c51",
        null,
        "string"
      ]
    ],
    [
      "005093c0",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005092bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/00509254.md#insn-005092bc) · [`005092fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/00509254.md#insn-005092fc) · [`00509354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/00509254.md#insn-00509354)
- 新版 [`005092fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/00509294.md#insn-005092fc) · [`0050933c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/00509294.md#insn-0050933c) · [`00509394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/00509294.md#insn-00509394)

~~~diff
- 005092bc ["INT_ADD", "register:40f0:8", ["const:5092bc:8", "const:4:8"]]
- 005092bc ["CALL", null, ["callee:00c587e0:8"]]
+ 005092fc ["INT_ADD", "register:40f0:8", ["const:5092fc:8", "const:4:8"]]
+ 005092fc ["CALL", null, ["callee:00c587e0:8"]]
- 005092bc bytes 153d1d94
+ 005092fc bytes 393d1d94
- 005092fc ["COPY", "register:0:8", ["register:4048:8"]]
- 005092fc ["INT_ADD", "register:40f0:8", ["const:5092fc:8", "const:4:8"]]
- 005092fc ["CALLIND", null, ["register:0:8"]]
+ 0050933c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050933c ["INT_ADD", "register:40f0:8", ["const:50933c:8", "const:4:8"]]
+ 0050933c ["CALLIND", null, ["register:0:8"]]
- 005092fc bytes 20013fd6
+ 0050933c bytes 20013fd6
- 00509354 ["INT_ADD", "register:40f0:8", ["const:509354:8", "const:4:8"]]
- 00509354 ["CALL", null, ["callee:0043de18:8"]]
+ 00509394 ["INT_ADD", "register:40f0:8", ["const:509394:8", "const:4:8"]]
+ 00509394 ["CALL", null, ["callee:0043de18:8"]]
- 00509354 bytes a1d2fc97
+ 00509394 bytes a1d2fc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e1c6459ed2c4871dd39a9f2cb1efbf6"></a>

### [`005093f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/005093f8.md) → [`00509438`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/00509438.md) FUN_00509438

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0051ae2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051ae2c.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`004594d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58200.md)
- 新版 呼出元 1件 [`0051ae6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051ae6c.md) · 呼出先 5件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00459510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459510.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c582d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c582d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.47% / 新版 92.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005094a4",
      "incomplete_value": true,
      "site": "005094a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00509464",
      "incomplete_value": true,
      "site": "00509468",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00509474",
      "incomplete_value": false,
      "site": "00509478",
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
            "const:a8b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00509434",
      "incomplete_value": false,
      "site": "00509438",
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
            "const:a5c:8"
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
      "definition_site": "00509530",
      "incomplete_value": false,
      "site": "00509538",
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
            "const:96b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005094f0",
      "incomplete_value": false,
      "site": "005094f8",
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
            "const:9c7:8"
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
      "00509474",
      "PARAM",
      [
        "storage",
        "002a9a5c",
        null,
        null
      ]
    ],
    [
      "00509484",
      "PARAM",
      [
        "storage",
        "002a9a5c",
        null,
        null
      ]
    ],
    [
      "0050949c",
      "READ",
      [
        "storage",
        "00c9b128",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00509474",
      "PARAM",
      [
        "storage",
        "002a9a8b",
        null,
        null
      ]
    ],
    [
      "00509484",
      "PARAM",
      [
        "storage",
        "002a9a8b",
        null,
        null
      ]
    ],
    [
      "0050949c",
      "READ",
      [
        "storage",
        "00c9b1f8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00509438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/005093f8.md#insn-00509438) · [`005094f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/005093f8.md#insn-005094f8) · [`00509424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/005093f8.md#insn-00509424)
- 新版 [`00509478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/00509438.md#insn-00509478) · [`00509538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/00509438.md#insn-00509538) · [`00509464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/00509438.md#insn-00509464)

~~~diff
- 00509438 ["INT_ADD", "register:40f0:8", ["const:509438:8", "const:4:8"]]
- 00509438 ["CALL", null, ["callee:00459510:8"]]
+ 00509478 ["INT_ADD", "register:40f0:8", ["const:509478:8", "const:4:8"]]
+ 00509478 ["CALL", null, ["callee:00459510:8"]]
- 00509438 bytes 2640fd97
+ 00509478 bytes 2640fd97
- 005094f8 ["INT_ADD", "register:40f0:8", ["const:5094f8:8", "const:4:8"]]
- 005094f8 ["CALL", null, ["callee:00459510:8"]]
+ 00509538 ["INT_ADD", "register:40f0:8", ["const:509538:8", "const:4:8"]]
+ 00509538 ["CALL", null, ["callee:00459510:8"]]
- 005094f8 bytes f63ffd97
+ 00509538 bytes f63ffd97
- 00509424 ["INT_ADD", "register:40f0:8", ["const:509424:8", "const:4:8"]]
- 00509424 ["CALL", null, ["callee:00c582d0:8"]]
+ 00509464 ["INT_ADD", "register:40f0:8", ["const:509464:8", "const:4:8"]]
+ 00509464 ["CALL", null, ["callee:00c582d0:8"]]
- 00509424 bytes 773b1d94
+ 00509464 bytes 9b3b1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67af5592caca7e66d14b475142f7d5fd"></a>

### [`005095a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/005095a8.md) → [`005095e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/005095e8.md) _ZN5Botan4OCSP7RequestC2ERKNS_16X509_CertificateES4_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 14件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`0053b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053b000.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`0053b040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053b040.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.87% / 新版 97.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00509624",
      "incomplete_value": true,
      "site": "00509628",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005095e4",
      "incomplete_value": true,
      "site": "005095e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005096a8",
      "incomplete_value": true,
      "site": "005096a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00509668",
      "incomplete_value": true,
      "site": "00509668",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00509714",
      "incomplete_value": false,
      "site": "0050971c",
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
            "const:e91:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005096d4",
      "incomplete_value": false,
      "site": "005096dc",
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
            "const:e60:8"
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
      "00509620",
      "READ",
      [
        "storage",
        "00c9b0e0",
        null,
        "pointer"
      ]
    ],
    [
      "00509628",
      "DATA",
      [
        "storage",
        "00c67a88",
        null,
        "undefined1[72]"
      ]
    ],
    [
      "00509698",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00509620",
      "READ",
      [
        "storage",
        "00c9b1b0",
        null,
        "pointer"
      ]
    ],
    [
      "00509628",
      "DATA",
      [
        "storage",
        "00c67b58",
        null,
        "undefined1[72]"
      ]
    ],
    [
      "00509698",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00509668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/005095a8.md#insn-00509668) · [`005096dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/005095a8.md#insn-005096dc) · [`00509718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/005095a8.md#insn-00509718)
- 新版 [`005096a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/005095e8.md#insn-005096a8) · [`0050971c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/005095e8.md#insn-0050971c) · [`00509758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/005095e8.md#insn-00509758)

~~~diff
- 00509668 ["COPY", "register:0:8", ["register:4048:8"]]
- 00509668 ["INT_ADD", "register:40f0:8", ["const:509668:8", "const:4:8"]]
- 00509668 ["CALLIND", null, ["register:0:8"]]
+ 005096a8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005096a8 ["INT_ADD", "register:40f0:8", ["const:5096a8:8", "const:4:8"]]
+ 005096a8 ["CALLIND", null, ["register:0:8"]]
- 00509668 bytes 20013fd6
+ 005096a8 bytes 20013fd6
- 005096dc ["INT_ADD", "register:40f0:8", ["const:5096dc:8", "const:4:8"]]
- 005096dc ["CALL", null, ["callee:0043de18:8"]]
+ 0050971c ["INT_ADD", "register:40f0:8", ["const:50971c:8", "const:4:8"]]
+ 0050971c ["CALL", null, ["callee:0043de18:8"]]
- 005096dc bytes bfd1fc97
+ 0050971c bytes bfd1fc97
- 00509718 ["INT_ADD", "register:40f0:8", ["const:509718:8", "const:4:8"]]
- 00509718 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00509758 ["INT_ADD", "register:40f0:8", ["const:509758:8", "const:4:8"]]
+ 00509758 ["CALL", null, ["callee:00c57fe0:8"]]
- 00509718 bytes fe391d94
+ 00509758 bytes 223a1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f76a4a28375885ab8d13b6cf90e1cd67"></a>

### [`00509854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/00509854.md) → [`00509894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/00509894.md) FUN_00509894

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.33% / 新版 93.33%

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
      "definition_site": "005098b0",
      "incomplete_value": true,
      "site": "005098b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00509870",
      "incomplete_value": true,
      "site": "00509874",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005098f0",
      "incomplete_value": true,
      "site": "005098f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005098b0",
      "incomplete_value": true,
      "site": "005098b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005098a8",
      "READ",
      [
        "storage",
        "00c9b0e0",
        null,
        "pointer"
      ]
    ],
    [
      "005098b4",
      "DATA",
      [
        "storage",
        "00c67a88",
        null,
        "undefined1[72]"
      ]
    ],
    [
      "005098e8",
      "READ",
      [
        "storage",
        "00c9b158",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005098a8",
      "READ",
      [
        "storage",
        "00c9b1b0",
        null,
        "pointer"
      ]
    ],
    [
      "005098b4",
      "DATA",
      [
        "storage",
        "00c67b58",
        null,
        "undefined1[72]"
      ]
    ],
    [
      "005098e8",
      "READ",
      [
        "storage",
        "00c9b228",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00509868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/00509854.md#insn-00509868) · [`00509884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/00509854.md#insn-00509884) · [`00509898`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/00509854.md#insn-00509898)
- 新版 [`005098a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/00509894.md#insn-005098a8) · [`005098c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/00509894.md#insn-005098c4) · [`005098d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/00509894.md#insn-005098d8)

~~~diff
- 00509868 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e0:8"]]
- 00509868 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005098a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1b0:8"]]
+ 005098a8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00509868 bytes 087140f9
+ 005098a8 bytes 08d940f9
- 00509884 ["INT_ADD", "register:40f0:8", ["const:509884:8", "const:4:8"]]
- 00509884 ["CALL", null, ["callee:00c53da0:8"]]
+ 005098c4 ["INT_ADD", "register:40f0:8", ["const:5098c4:8", "const:4:8"]]
+ 005098c4 ["CALL", null, ["callee:00c53da0:8"]]
- 00509884 bytes 1f291d94
+ 005098c4 bytes 37291d94
- 00509898 ["COPY", "register:0:8", ["register:4040:8"]]
- 00509898 ["INT_ADD", "register:40f0:8", ["const:509898:8", "const:4:8"]]
- 00509898 ["CALLIND", null, ["register:0:8"]]
+ 005098d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005098d8 ["INT_ADD", "register:40f0:8", ["const:5098d8:8", "const:4:8"]]
+ 005098d8 ["CALLIND", null, ["register:0:8"]]
- 00509898 bytes 00013fd6
+ 005098d8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ab28d578ff2ead2e127e8f17a6e5b56"></a>

### [`00509984`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/00509984.md) → [`005099c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/005099c4.md) _ZNK5Botan4OCSP7Request10BER_encodeEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59bb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59bb0.md) · 呼出先 10件 [`004a6db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6db0.md) [`00535b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md)
- 新版 呼出元 1件 [`00c59c80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59c80.md) · 呼出先 10件 [`004a6df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a6df0.md) [`00535bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bc0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.36% / 新版 96.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00509a70",
      "incomplete_value": true,
      "site": "00509a70",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00509a30",
      "incomplete_value": true,
      "site": "00509a30",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00509b44",
      "incomplete_value": true,
      "site": "00509b44",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00509b04",
      "incomplete_value": true,
      "site": "00509b04",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 18,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00509a60",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "00509b34",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00509a60",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00509b34",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00509a30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/00509984.md#insn-00509a30) · [`00509b04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/00509984.md#insn-00509b04) · [`005099c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/00509984.md#insn-005099c8)
- 新版 [`00509a70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/005099c4.md#insn-00509a70) · [`00509b44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/005099c4.md#insn-00509b44) · [`00509a08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/005099c4.md#insn-00509a08)

~~~diff
- 00509a30 ["COPY", "register:0:8", ["register:4048:8"]]
- 00509a30 ["INT_ADD", "register:40f0:8", ["const:509a30:8", "const:4:8"]]
- 00509a30 ["CALLIND", null, ["register:0:8"]]
+ 00509a70 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00509a70 ["INT_ADD", "register:40f0:8", ["const:509a70:8", "const:4:8"]]
+ 00509a70 ["CALLIND", null, ["register:0:8"]]
- 00509a30 bytes 20013fd6
+ 00509a70 bytes 20013fd6
- 00509b04 ["COPY", "register:0:8", ["register:4048:8"]]
- 00509b04 ["INT_ADD", "register:40f0:8", ["const:509b04:8", "const:4:8"]]
- 00509b04 ["CALLIND", null, ["register:0:8"]]
+ 00509b44 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00509b44 ["INT_ADD", "register:40f0:8", ["const:509b44:8", "const:4:8"]]
+ 00509b44 ["CALLIND", null, ["register:0:8"]]
- 00509b04 bytes 20013fd6
+ 00509b44 bytes 20013fd6
- 005099c8 ["INT_ADD", "register:40f0:8", ["const:5099c8:8", "const:4:8"]]
- 005099c8 ["CALL", null, ["callee:00c58780:8"]]
+ 00509a08 ["INT_ADD", "register:40f0:8", ["const:509a08:8", "const:4:8"]]
+ 00509a08 ["CALL", null, ["callee:00c58780:8"]]
- 005099c8 bytes 3a3b1d94
+ 00509a08 bytes 5e3b1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c71486013502ae62cf8b21522b366e5"></a>

### [`00509c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/00509c14.md) → [`00509c54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/00509c54.md) _ZN5Botan4OCSP8ResponseC2EPKhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 41件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`004a577c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a577c.md) [`004a5980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5980.md) [`004aea74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aea74.md) [`0050a97c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050a/0050a97c.md)
- 新版 呼出元 0件  · 呼出先 41件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`004a57bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a57bc.md) [`004a59c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a59c0.md) [`004aeab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeab4.md) [`0050a9bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050a/0050a9bc.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.76% / 新版 94.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 10件

アドレスに依存する影響 `call_argument_candidate` 1件, `call_target` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00509cdc",
      "incomplete_value": true,
      "site": "00509cdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00509c9c",
      "incomplete_value": true,
      "site": "00509c9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00509d04",
      "incomplete_value": true,
      "site": "00509d04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00509cc4",
      "incomplete_value": true,
      "site": "00509cc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00509d30",
      "incomplete_value": true,
      "site": "00509d30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00509cf0",
      "incomplete_value": true,
      "site": "00509cf0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
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
      "00509cd0",
      "READ",
      [
        "storage",
        "00c9adb0",
        null,
        "pointer"
      ]
    ],
    [
      "00509cdc",
      "DATA",
      [
        "storage",
        "00c66378",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00509cec",
      "READ",
      [
        "storage",
        "00c9b0d0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00509cd0",
      "READ",
      [
        "storage",
        "00c9ae80",
        null,
        "pointer"
      ]
    ],
    [
      "00509cdc",
      "DATA",
      [
        "storage",
        "00c66448",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00509cec",
      "READ",
      [
        "storage",
        "00c9b1a0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00509d50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/00509c14.md#insn-00509d50) · [`00509d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/00509c14.md#insn-00509d90) · [`00509e0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/00509c14.md#insn-00509e0c)
- 新版 [`00509d90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/00509c54.md#insn-00509d90) · [`00509dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/00509c54.md#insn-00509dd0) · [`00509e4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/00509c54.md#insn-00509e4c)

~~~diff
- 00509d50 ["INT_ADD", "register:40f0:8", ["const:509d50:8", "const:4:8"]]
- 00509d50 ["CALL", null, ["callee:00c587d0:8"]]
+ 00509d90 ["INT_ADD", "register:40f0:8", ["const:509d90:8", "const:4:8"]]
+ 00509d90 ["CALL", null, ["callee:00c587d0:8"]]
- 00509d50 bytes 6c3a1d94
+ 00509d90 bytes 903a1d94
- 00509d90 ["COPY", "register:0:8", ["register:4048:8"]]
- 00509d90 ["INT_ADD", "register:40f0:8", ["const:509d90:8", "const:4:8"]]
- 00509d90 ["CALLIND", null, ["register:0:8"]]
+ 00509dd0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00509dd0 ["INT_ADD", "register:40f0:8", ["const:509dd0:8", "const:4:8"]]
+ 00509dd0 ["CALLIND", null, ["register:0:8"]]
- 00509d90 bytes 20013fd6
+ 00509dd0 bytes 20013fd6
- 00509e0c ["INT_ADD", "register:40f0:8", ["const:509e0c:8", "const:4:8"]]
- 00509e0c ["CALL", null, ["callee:00c587d0:8"]]
+ 00509e4c ["INT_ADD", "register:40f0:8", ["const:509e4c:8", "const:4:8"]]
+ 00509e4c ["CALL", null, ["callee:00c587d0:8"]]
- 00509e0c bytes 3d3a1d94
+ 00509e4c bytes 613a1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f9778ca56162ecf45f9b8e7eeb753c5"></a>

### [`0050a97c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050a/0050a97c.md) → [`0050a9bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050a/0050a9bc.md) FUN_0050a9bc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00509c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/00509c14.md) · 呼出先 7件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`00509c54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/00509c54.md) · 呼出先 7件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.57% / 新版 98.57%

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
      "definition_site": "0050aac4",
      "incomplete_value": true,
      "site": "0050aacc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050aa84",
      "incomplete_value": true,
      "site": "0050aa8c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0050aac0",
      "incomplete_value": false,
      "site": "0050aacc",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "0050aa80",
      "incomplete_value": false,
      "site": "0050aa8c",
      "value": [
        "leaf",
        "const:535868:8"
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
      "0050aac0",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "0050aac4",
      "READ",
      [
        "storage",
        "00c9ad50",
        null,
        "pointer"
      ]
    ],
    [
      "0050aac4",
      "PARAM",
      [
        "storage",
        "00c662c0",
        "_ZTIN5Botan14Decoding_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0050aac0",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "0050aac4",
      "READ",
      [
        "storage",
        "00c9ae20",
        null,
        "pointer"
      ]
    ],
    [
      "0050aac4",
      "PARAM",
      [
        "storage",
        "00c66390",
        "_ZTIN5Botan14Decoding_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050aa8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050a/0050a97c.md#insn-0050aa8c) · [`0050a9b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050a/0050a97c.md#insn-0050a9b4) · [`0050a9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050a/0050a97c.md#insn-0050a9c4)
- 新版 [`0050aacc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050a/0050a9bc.md#insn-0050aacc) · [`0050a9f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050a/0050a9bc.md#insn-0050a9f4) · [`0050aa04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050a/0050a9bc.md#insn-0050aa04)

~~~diff
- 0050aa8c ["INT_ADD", "register:40f0:8", ["const:50aa8c:8", "const:4:8"]]
- 0050aa8c ["CALL", null, ["callee:00c57fe0:8"]]
+ 0050aacc ["INT_ADD", "register:40f0:8", ["const:50aacc:8", "const:4:8"]]
+ 0050aacc ["CALL", null, ["callee:00c57fe0:8"]]
- 0050aa8c bytes 21351d94
+ 0050aacc bytes 45351d94
- 0050a9b4 ["INT_ADD", "register:40f0:8", ["const:50a9b4:8", "const:4:8"]]
- 0050a9b4 ["CALL", null, ["callee:00c58760:8"]]
+ 0050a9f4 ["INT_ADD", "register:40f0:8", ["const:50a9f4:8", "const:4:8"]]
+ 0050a9f4 ["CALL", null, ["callee:00c58760:8"]]
- 0050a9b4 bytes 37371d94
+ 0050a9f4 bytes 5b371d94
- 0050a9c4 ["INT_ADD", "register:40f0:8", ["const:50a9c4:8", "const:4:8"]]
- 0050a9c4 ["CALL", null, ["callee:00c57f80:8"]]
+ 0050aa04 ["INT_ADD", "register:40f0:8", ["const:50aa04:8", "const:4:8"]]
+ 0050aa04 ["CALL", null, ["callee:00c57f80:8"]]
- 0050a9c4 bytes 3b351d94
+ 0050aa04 bytes 5f351d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da8854520f3b69b7e5a97b07ab7794b4"></a>

### [`0050ae78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050a/0050ae78.md) → [`0050aeb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050a/0050aeb8.md) _ZN5Botan11BER_Decoder11decode_listINS_4OCSP14SingleResponseEEERS0_RNSt6__ndk16vectorIT_NS5_9allocatorIS7_EEEENS_8ASN1_TagESC_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c59be0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59be0.md) · 呼出先 10件 [`0050ceb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050c/0050ceb4.md) [`00549888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549888.md) [`00549a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549a8c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00c59cb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59cb0.md) · 呼出先 10件 [`0050cef4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050cef4.md) [`005498c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00549/005498c8.md) [`00549acc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00549/00549acc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.53% / 新版 90.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

アドレスに依存する影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050affc",
      "incomplete_value": true,
      "site": "0050affc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0050afbc",
      "incomplete_value": true,
      "site": "0050afbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 37,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050b01c",
      "incomplete_value": true,
      "site": "0050b01c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0050afdc",
      "incomplete_value": true,
      "site": "0050afdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0050b018",
      "incomplete_value": true,
      "site": "0050b028",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0050afd8",
      "incomplete_value": true,
      "site": "0050afe8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0050af0c",
      "READ",
      [
        "storage",
        "00c9b160",
        null,
        "pointer"
      ]
    ],
    [
      "0050af10",
      "READ",
      [
        "storage",
        "00c9b168",
        null,
        "pointer"
      ]
    ],
    [
      "0050af14",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050af0c",
      "READ",
      [
        "storage",
        "00c9b230",
        null,
        "pointer"
      ]
    ],
    [
      "0050af10",
      "READ",
      [
        "storage",
        "00c9b238",
        null,
        "pointer"
      ]
    ],
    [
      "0050af14",
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050af9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050a/0050ae78.md#insn-0050af9c) · [`0050b040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050a/0050ae78.md#insn-0050b040) · [`0050b094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050a/0050ae78.md#insn-0050b094)
- 新版 [`0050afdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050a/0050aeb8.md#insn-0050afdc) · [`0050b080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050a/0050aeb8.md#insn-0050b080) · [`0050b0d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050a/0050aeb8.md#insn-0050b0d4)

~~~diff
- 0050af9c ["COPY", "register:0:8", ["register:4040:8"]]
- 0050af9c ["INT_ADD", "register:40f0:8", ["const:50af9c:8", "const:4:8"]]
- 0050af9c ["CALLIND", null, ["register:0:8"]]
+ 0050afdc ["COPY", "register:0:8", ["register:4040:8"]]
+ 0050afdc ["INT_ADD", "register:40f0:8", ["const:50afdc:8", "const:4:8"]]
+ 0050afdc ["CALLIND", null, ["register:0:8"]]
- 0050af9c bytes 00013fd6
+ 0050afdc bytes 00013fd6
- 0050b040 ["COPY", "register:0:8", ["register:4048:8"]]
- 0050b040 ["INT_ADD", "register:40f0:8", ["const:50b040:8", "const:4:8"]]
- 0050b040 ["CALLIND", null, ["register:0:8"]]
+ 0050b080 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050b080 ["INT_ADD", "register:40f0:8", ["const:50b080:8", "const:4:8"]]
+ 0050b080 ["CALLIND", null, ["register:0:8"]]
- 0050b040 bytes 20013fd6
+ 0050b080 bytes 20013fd6
- 0050b094 ["INT_ADD", "register:40f0:8", ["const:50b094:8", "const:4:8"]]
- 0050b094 ["CALL", null, ["callee:00c587e0:8"]]
+ 0050b0d4 ["INT_ADD", "register:40f0:8", ["const:50b0d4:8", "const:4:8"]]
+ 0050b0d4 ["CALL", null, ["callee:00c587e0:8"]]
- 0050b094 bytes 9f351d94
+ 0050b0d4 bytes c3351d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9776aa723b50178a6b3d8f3e05b390f"></a>

### [`0050b4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050b/0050b4c4.md) → [`0050b504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050b/0050b504.md) _ZNK5Botan4OCSP8Response16verify_signatureERKNS_16X509_CertificateE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59c00.md) · 呼出先 14件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`004a6c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6c1c.md) [`00547b14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547b14.md) [`00547b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547b6c.md) [`00547b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547b70.md)
- 新版 呼出元 1件 [`00c59cd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59cd0.md) · 呼出先 14件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`004a6c5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a6c5c.md) [`00547b54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00547/00547b54.md) [`00547bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00547/00547bac.md) [`00547bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00547/00547bb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.95% / 新版 98.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0050b554",
      "incomplete_value": false,
      "site": "0050b554",
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
            "const:780:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050b514",
      "incomplete_value": false,
      "site": "0050b514",
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
            "const:6b0:8"
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
      "0050b554",
      "DATA",
      [
        "storage",
        "00c6a6b0",
        null,
        "undefined *"
      ]
    ],
    [
      "0050b598",
      "READ",
      [
        "storage",
        "00c6a6d0",
        null,
        "pointer"
      ]
    ],
    [
      "0050b598",
      "READ",
      [
        "storage",
        "00c6a6d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0050b554",
      "DATA",
      [
        "storage",
        "00c6a780",
        null,
        "undefined *"
      ]
    ],
    [
      "0050b598",
      "READ",
      [
        "storage",
        "00c6a7a0",
        null,
        "pointer"
      ]
    ],
    [
      "0050b598",
      "READ",
      [
        "storage",
        "00c6a7a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050b4f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050b/0050b4c4.md#insn-0050b4f4) · [`0050b504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050b/0050b4c4.md#insn-0050b504) · [`0050b50c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050b/0050b4c4.md#insn-0050b50c)
- 新版 [`0050b534`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050b/0050b504.md#insn-0050b534) · [`0050b544`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050b/0050b504.md#insn-0050b544) · [`0050b54c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050b/0050b504.md#insn-0050b54c)

~~~diff
- 0050b4f4 ["INT_ADD", "register:40f0:8", ["const:50b4f4:8", "const:4:8"]]
- 0050b4f4 ["CALL", null, ["callee:00c59ce0:8"]]
+ 0050b534 ["INT_ADD", "register:40f0:8", ["const:50b534:8", "const:4:8"]]
+ 0050b534 ["CALL", null, ["callee:00c59ce0:8"]]
- 0050b4f4 bytes c7391d94
+ 0050b534 bytes eb391d94
- 0050b504 ["INT_ADD", "register:40f0:8", ["const:50b504:8", "const:4:8"]]
- 0050b504 ["CALL", null, ["callee:00c58980:8"]]
+ 0050b544 ["INT_ADD", "register:40f0:8", ["const:50b544:8", "const:4:8"]]
+ 0050b544 ["CALL", null, ["callee:00c58980:8"]]
- 0050b504 bytes eb341d94
+ 0050b544 bytes 0f351d94
- 0050b50c ["COPY", "tmp:0:8", ["const:6b0:8"]]
- 0050b50c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0050b50c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0050b50c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0050b54c ["COPY", "tmp:0:8", ["const:780:8"]]
+ 0050b54c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0050b54c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0050b54c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0050b50c bytes 08c11a91
+ 0050b54c bytes 08011e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b5069c81c68eb99631e41e7b43a4a5e"></a>

### [`0050b8ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050b/0050b8ec.md) → [`0050b92c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050b/0050b92c.md) _ZNK5Botan4OCSP8Response15check_signatureERKNSt6__ndk16vectorIPNS_17Certificate_StoreENS2_9allocatorIS5_EEEERKNS3_INS2_10shared_ptrIKNS_16X5

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59c20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59c20.md) · 呼出先 13件 [`0053b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053b000.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00c59cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59cf0.md) · 呼出先 13件 [`0053b040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053b040.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.35% / 新版 97.35%

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
      "definition_site": "0050bc30",
      "incomplete_value": true,
      "site": "0050bc3c",
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
                "const:ceb:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050bbf0",
      "incomplete_value": true,
      "site": "0050bbfc",
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
                "const:cba:8"
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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050bdc4",
      "incomplete_value": true,
      "site": "0050bdc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0050bd84",
      "incomplete_value": true,
      "site": "0050bd88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 28,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050bdf8",
      "incomplete_value": true,
      "site": "0050bdfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0050bdb8",
      "incomplete_value": true,
      "site": "0050bdbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
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
      "0050bc30",
      "READ",
      [
        "storage",
        "002b4cba",
        null,
        "string"
      ]
    ],
    [
      "0050bdbc",
      "READ",
      [
        "storage",
        "00c9b0d8",
        null,
        "pointer"
      ]
    ],
    [
      "0050bdc8",
      "DATA",
      [
        "storage",
        "00c6a740",
        null,
        "undefined1[56]"
      ]
    ]
  ],
  "added": [
    [
      "0050bc30",
      "READ",
      [
        "storage",
        "002b4ceb",
        null,
        "string"
      ]
    ],
    [
      "0050bdbc",
      "READ",
      [
        "storage",
        "00c9b1a8",
        null,
        "pointer"
      ]
    ],
    [
      "0050bdc8",
      "DATA",
      [
        "storage",
        "00c6a810",
        null,
        "undefined1[56]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050bd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050b/0050b8ec.md#insn-0050bd7c) · [`0050bdc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050b/0050b8ec.md#insn-0050bdc8) · [`0050bdfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050b/0050b8ec.md#insn-0050bdfc)
- 新版 [`0050bdbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050b/0050b92c.md#insn-0050bdbc) · [`0050be08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050b/0050b92c.md#insn-0050be08) · [`0050be3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050b/0050b92c.md#insn-0050be3c)

~~~diff
- 0050bd7c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d8:8"]]
- 0050bd7c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050bdbc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1a8:8"]]
+ 0050bdbc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050bd7c bytes 086d40f9
+ 0050bdbc bytes 08d540f9
- 0050bdc8 ["INT_ADD", "register:40f0:8", ["const:50bdc8:8", "const:4:8"]]
- 0050bdc8 ["CALL", null, ["callee:0053b040:8"]]
+ 0050be08 ["INT_ADD", "register:40f0:8", ["const:50be08:8", "const:4:8"]]
+ 0050be08 ["CALL", null, ["callee:0053b040:8"]]
- 0050bdc8 bytes 8ebc0094
+ 0050be08 bytes 8ebc0094
- 0050bdfc ["INT_ADD", "register:40f0:8", ["const:50bdfc:8", "const:4:8"]]
- 0050bdfc ["CALL", null, ["callee:00c53d70:8"]]
+ 0050be3c ["INT_ADD", "register:40f0:8", ["const:50be3c:8", "const:4:8"]]
+ 0050be3c ["CALL", null, ["callee:00c53d70:8"]]
- 0050bdfc bytes b51f1d94
+ 0050be3c bytes cd1f1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a39fb1bd477f6c7ba9c781df1be77aa"></a>

### [`0050bec4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050b/0050bec4.md) → [`0050bf04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050b/0050bf04.md) _ZNK5Botan16X509_Certificate33subject_public_key_bitstring_sha1Ev

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59c30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59c30.md) · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`00c59d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59d00.md) · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

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
      "definition_site": "0050bf7c",
      "incomplete_value": false,
      "site": "0050bf84",
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
            "const:1ef:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050bf3c",
      "incomplete_value": false,
      "site": "0050bf44",
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
            "const:1af:8"
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
      "definition_site": "0050bfb8",
      "incomplete_value": true,
      "site": "0050bfc4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e68:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050bf78",
      "incomplete_value": true,
      "site": "0050bf84",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d98:8"
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
      "definition_site": "0050bfb4",
      "incomplete_value": false,
      "site": "0050bfc4",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "0050bf74",
      "incomplete_value": false,
      "site": "0050bf84",
      "value": [
        "leaf",
        "const:535868:8"
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
      "0050bf7c",
      "PARAM",
      [
        "storage",
        "002c11af",
        null,
        "string"
      ]
    ],
    [
      "0050bfb4",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "0050bfb8",
      "READ",
      [
        "storage",
        "00c9ad98",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050bf7c",
      "PARAM",
      [
        "storage",
        "002c11ef",
        null,
        "string"
      ]
    ],
    [
      "0050bfb4",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "0050bfb8",
      "READ",
      [
        "storage",
        "00c9ae68",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050bf44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050b/0050bec4.md#insn-0050bf44) · [`0050bf84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050b/0050bec4.md#insn-0050bf84) · [`0050bee8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050b/0050bec4.md#insn-0050bee8)
- 新版 [`0050bf84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050b/0050bf04.md#insn-0050bf84) · [`0050bfc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050b/0050bf04.md#insn-0050bfc4) · [`0050bf28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050b/0050bf04.md#insn-0050bf28)

~~~diff
- 0050bf44 ["INT_ADD", "register:40f0:8", ["const:50bf44:8", "const:4:8"]]
- 0050bf44 ["CALL", null, ["callee:0043de18:8"]]
+ 0050bf84 ["INT_ADD", "register:40f0:8", ["const:50bf84:8", "const:4:8"]]
+ 0050bf84 ["CALL", null, ["callee:0043de18:8"]]
- 0050bf44 bytes a5c7fc97
+ 0050bf84 bytes a5c7fc97
- 0050bf84 ["INT_ADD", "register:40f0:8", ["const:50bf84:8", "const:4:8"]]
- 0050bf84 ["CALL", null, ["callee:00c57fe0:8"]]
+ 0050bfc4 ["INT_ADD", "register:40f0:8", ["const:50bfc4:8", "const:4:8"]]
+ 0050bfc4 ["CALL", null, ["callee:00c57fe0:8"]]
- 0050bf84 bytes e32f1d94
+ 0050bfc4 bytes 07301d94
- 0050bee8 ["INT_ADD", "register:40f0:8", ["const:50bee8:8", "const:4:8"]]
- 0050bee8 ["CALL", null, ["callee:00c59ac0:8"]]
+ 0050bf28 ["INT_ADD", "register:40f0:8", ["const:50bf28:8", "const:4:8"]]
+ 0050bf28 ["CALL", null, ["callee:00c59ac0:8"]]
- 0050bee8 bytes c2361d94
+ 0050bf28 bytes e6361d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec7d99413802adf113267ba93e0f96ff"></a>

### [`0050c138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050c/0050c138.md) → [`0050c178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050c178.md) _ZNK5Botan4OCSP8Response10status_forERKNS_16X509_CertificateES4_NSt6__ndk16chrono10time_pointINS6_12system_clockENS6_8durationIxNS5_5ratioIL

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59c50.md) · 呼出先 4件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c589e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c589e0.md) [`00c59a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59a70.md) [`00c59c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59c60.md)
- 新版 呼出元 1件 [`00c59d20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59d20.md) · 呼出先 4件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58ab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ab0.md) [`00c59b40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b40.md) [`00c59d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59d30.md)

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
      "definition_site": "0050c238",
      "incomplete_value": true,
      "site": "0050c240",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0050c1f8",
      "incomplete_value": true,
      "site": "0050c200",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "0050c22c",
      "READ",
      [
        "storage",
        "00c9adb0",
        null,
        "pointer"
      ]
    ],
    [
      "0050c240",
      "DATA",
      [
        "storage",
        "00c66378",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0050c27c",
      "DATA",
      [
        "storage",
        "00c66378",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "0050c22c",
      "READ",
      [
        "storage",
        "00c9ae80",
        null,
        "pointer"
      ]
    ],
    [
      "0050c240",
      "DATA",
      [
        "storage",
        "00c66448",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0050c27c",
      "DATA",
      [
        "storage",
        "00c66448",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050c180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050c/0050c138.md#insn-0050c180) · [`0050c1c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050c/0050c138.md#insn-0050c1c8) · [`0050c1ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050c/0050c138.md#insn-0050c1ec)
- 新版 [`0050c1c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050c178.md#insn-0050c1c0) · [`0050c208`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050c178.md#insn-0050c208) · [`0050c22c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050c178.md#insn-0050c22c)

~~~diff
- 0050c180 ["INT_ADD", "register:40f0:8", ["const:50c180:8", "const:4:8"]]
- 0050c180 ["CALL", null, ["callee:00c59d30:8"]]
+ 0050c1c0 ["INT_ADD", "register:40f0:8", ["const:50c1c0:8", "const:4:8"]]
+ 0050c1c0 ["CALL", null, ["callee:00c59d30:8"]]
- 0050c180 bytes b8361d94
+ 0050c1c0 bytes dc361d94
- 0050c1c8 ["INT_ADD", "register:40f0:8", ["const:50c1c8:8", "const:4:8"]]
- 0050c1c8 ["CALL", null, ["callee:00c59b40:8"]]
+ 0050c208 ["INT_ADD", "register:40f0:8", ["const:50c208:8", "const:4:8"]]
+ 0050c208 ["CALL", null, ["callee:00c59b40:8"]]
- 0050c1c8 bytes 2a361d94
+ 0050c208 bytes 4e361d94
- 0050c1ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:db0:8"]]
- 0050c1ec ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050c22c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e80:8"]]
+ 0050c22c ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
- 0050c1ec bytes 73da46f9
+ 0050c22c bytes 734247f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e82aa27551bc42f53e129fb8163b0d87"></a>

### [`0050c6b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050c/0050c6b8.md) → [`0050c6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050c6f8.md) _ZN5Botan4OCSP6CertIDC2ERKNS_16X509_CertificateERKNS_6BigIntE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c59ba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59ba0.md) · 呼出先 14件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md) [`005436dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/005436dc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00c59c70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59c70.md) · 呼出先 14件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`004b3548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3548.md) [`0054371c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/0054371c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call_target, constant, operands_and_dependencies, operation_sequence, store_value

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
      "definition_site": "0050c744",
      "incomplete_value": true,
      "site": "0050c750",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0050c704",
      "incomplete_value": true,
      "site": "0050c710",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0050c754",
      "incomplete_value": true,
      "site": "0050c754",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0050c714",
      "incomplete_value": true,
      "site": "0050c714",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0050c988",
      "incomplete_value": true,
      "site": "0050c988",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050c948",
      "incomplete_value": true,
      "site": "0050c948",
      "value": [
        "LOAD",
        "8",
        [
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
      "0050c734",
      "READ",
      [
        "storage",
        "00c9b168",
        null,
        "pointer"
      ]
    ],
    [
      "0050c738",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "0050c750",
      "DATA",
      [
        "storage",
        "00c67818",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "0050c734",
      "READ",
      [
        "storage",
        "00c9b238",
        null,
        "pointer"
      ]
    ],
    [
      "0050c738",
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ],
    [
      "0050c750",
      "DATA",
      [
        "storage",
        "00c678e8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050c908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050c/0050c6b8.md#insn-0050c908) · [`0050c948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050c/0050c6b8.md#insn-0050c948) · [`0050ca30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050c/0050c6b8.md#insn-0050ca30)
- 新版 [`0050c948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050c6f8.md#insn-0050c948) · [`0050c988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050c6f8.md#insn-0050c988) · [`0050ca70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050c6f8.md#insn-0050ca70)

~~~diff
- 0050c908 ["INT_ADD", "register:40f0:8", ["const:50c908:8", "const:4:8"]]
- 0050c908 ["CALL", null, ["callee:00c57f80:8"]]
+ 0050c948 ["INT_ADD", "register:40f0:8", ["const:50c948:8", "const:4:8"]]
+ 0050c948 ["CALL", null, ["callee:00c57f80:8"]]
- 0050c908 bytes 6a2d1d94
+ 0050c948 bytes 8e2d1d94
- 0050c948 ["COPY", "register:0:8", ["register:4048:8"]]
- 0050c948 ["INT_ADD", "register:40f0:8", ["const:50c948:8", "const:4:8"]]
- 0050c948 ["CALLIND", null, ["register:0:8"]]
+ 0050c988 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050c988 ["INT_ADD", "register:40f0:8", ["const:50c988:8", "const:4:8"]]
+ 0050c988 ["CALLIND", null, ["register:0:8"]]
- 0050c948 bytes 20013fd6
+ 0050c988 bytes 20013fd6
- 0050ca30 ["COPY", "register:0:8", ["register:4048:8"]]
- 0050ca30 ["INT_ADD", "register:40f0:8", ["const:50ca30:8", "const:4:8"]]
- 0050ca30 ["CALLIND", null, ["register:0:8"]]
+ 0050ca70 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050ca70 ["INT_ADD", "register:40f0:8", ["const:50ca70:8", "const:4:8"]]
+ 0050ca70 ["CALLIND", null, ["register:0:8"]]
- 0050ca30 bytes 20013fd6
+ 0050ca70 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51346d1f9d48aef977d0657c1cf85f60"></a>

### [`0050cdcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050c/0050cdcc.md) → [`0050ce0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050ce0c.md) _ZNK5Botan4OCSP14SingleResponse11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 77.50% / 新版 77.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050ce4c",
      "incomplete_value": true,
      "site": "0050ce60",
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
                "const:2c1000:8"
              ],
              [
                "leaf",
                "const:1b7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050ce0c",
      "incomplete_value": true,
      "site": "0050ce20",
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
                "const:2c1000:8"
              ],
              [
                "leaf",
                "const:177:8"
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
      "definition_site": "0050ce50",
      "incomplete_value": true,
      "site": "0050ce64",
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
                "const:b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050ce10",
      "incomplete_value": true,
      "site": "0050ce24",
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
                "const:b:8"
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
      "definition_site": "0050ce54",
      "incomplete_value": true,
      "site": "0050ce68",
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
      "definition_site": "0050ce14",
      "incomplete_value": true,
      "site": "0050ce28",
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
                "const:680:8"
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
      "0050ce4c",
      "READ",
      [
        "storage",
        "002c1177",
        null,
        "string"
      ]
    ],
    [
      "0050ce50",
      "READ",
      [
        "storage",
        "002c1182",
        null,
        "string"
      ]
    ],
    [
      "0050ce54",
      "READ",
      [
        "storage",
        "002c2680",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0050ce4c",
      "READ",
      [
        "storage",
        "002c11b7",
        null,
        "string"
      ]
    ],
    [
      "0050ce50",
      "READ",
      [
        "storage",
        "002c11c2",
        null,
        "string"
      ]
    ],
    [
      "0050ce54",
      "READ",
      [
        "storage",
        "002c26c0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050ce64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050c/0050cdcc.md#insn-0050ce64) · [`0050cdf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050c/0050cdcc.md#insn-0050cdf0) · [`0050cdfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050c/0050cdcc.md#insn-0050cdfc)
- 新版 [`0050cea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050ce0c.md#insn-0050cea4) · [`0050ce30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050ce0c.md#insn-0050ce30) · [`0050ce3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050ce0c.md#insn-0050ce3c)

~~~diff
- 0050ce64 ["INT_ADD", "register:40f0:8", ["const:50ce64:8", "const:4:8"]]
- 0050ce64 ["CALL", null, ["callee:00c57fe0:8"]]
+ 0050cea4 ["INT_ADD", "register:40f0:8", ["const:50cea4:8", "const:4:8"]]
+ 0050cea4 ["CALL", null, ["callee:00c57fe0:8"]]
- 0050ce64 bytes 2b2c1d94
+ 0050cea4 bytes 4f2c1d94
- 0050cdf0 ["INT_ADD", "register:40f0:8", ["const:50cdf0:8", "const:4:8"]]
- 0050cdf0 ["CALL", null, ["callee:00c57fc0:8"]]
+ 0050ce30 ["INT_ADD", "register:40f0:8", ["const:50ce30:8", "const:4:8"]]
+ 0050ce30 ["CALL", null, ["callee:00c57fc0:8"]]
- 0050cdf0 bytes 402c1d94
+ 0050ce30 bytes 642c1d94
- 0050cdfc ["INT_ADD", "register:40f0:8", ["const:50cdfc:8", "const:4:8"]]
- 0050cdfc ["CALL", null, ["callee:00c57f60:8"]]
+ 0050ce3c ["INT_ADD", "register:40f0:8", ["const:50ce3c:8", "const:4:8"]]
+ 0050ce3c ["CALL", null, ["callee:00c57f60:8"]]
- 0050cdfc bytes 252c1d94
+ 0050ce3c bytes 492c1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4758c2383a5541cf39320d12d9b618f5"></a>

### [`0050ceb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050c/0050ceb4.md) → [`0050cef4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050cef4.md) _ZN5Botan4OCSP14SingleResponse11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0050ae78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050a/0050ae78.md) · 呼出先 10件 [`0053b424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053b424.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c58700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58700.md)
- 新版 呼出元 1件 [`0050aeb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050a/0050aeb8.md) · 呼出先 10件 [`0053b464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053b464.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c587d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c587d0.md)

変更の種類 call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.97% / 新版 94.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050cf3c",
      "incomplete_value": true,
      "site": "0050cf3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0050cefc",
      "incomplete_value": true,
      "site": "0050cefc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0050cfc4",
      "incomplete_value": true,
      "site": "0050cfc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0050cf84",
      "incomplete_value": true,
      "site": "0050cf84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 28,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0050d0ac",
      "incomplete_value": true,
      "site": "0050d0ac",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050d06c",
      "incomplete_value": true,
      "site": "0050d06c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
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
      "0050cf28",
      "READ",
      [
        "storage",
        "00c9b110",
        null,
        "pointer"
      ]
    ],
    [
      "0050cf3c",
      "DATA",
      [
        "storage",
        "00c688c0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0050cfb4",
      "READ",
      [
        "storage",
        "00c9adb0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050cf28",
      "READ",
      [
        "storage",
        "00c9b1e0",
        null,
        "pointer"
      ]
    ],
    [
      "0050cf3c",
      "DATA",
      [
        "storage",
        "00c68990",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0050cfb4",
      "READ",
      [
        "storage",
        "00c9ae80",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050cf3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050c/0050ceb4.md#insn-0050cf3c) · [`0050d02c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050c/0050ceb4.md#insn-0050d02c) · [`0050d06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050c/0050ceb4.md#insn-0050d06c)
- 新版 [`0050cf7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050cef4.md#insn-0050cf7c) · [`0050d06c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050cef4.md#insn-0050d06c) · [`0050d0ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050cef4.md#insn-0050d0ac)

~~~diff
- 0050cf3c ["INT_ADD", "register:40f0:8", ["const:50cf3c:8", "const:4:8"]]
- 0050cf3c ["CALL", null, ["callee:00c587f0:8"]]
+ 0050cf7c ["INT_ADD", "register:40f0:8", ["const:50cf7c:8", "const:4:8"]]
+ 0050cf7c ["CALL", null, ["callee:00c587f0:8"]]
- 0050cf3c bytes f92d1d94
+ 0050cf7c bytes 1d2e1d94
- 0050d02c ["INT_ADD", "register:40f0:8", ["const:50d02c:8", "const:4:8"]]
- 0050d02c ["CALL", null, ["callee:00c57f80:8"]]
+ 0050d06c ["INT_ADD", "register:40f0:8", ["const:50d06c:8", "const:4:8"]]
+ 0050d06c ["CALL", null, ["callee:00c57f80:8"]]
- 0050d02c bytes a12b1d94
+ 0050d06c bytes c52b1d94
- 0050d06c ["COPY", "register:0:8", ["register:4048:8"]]
- 0050d06c ["INT_ADD", "register:40f0:8", ["const:50d06c:8", "const:4:8"]]
- 0050d06c ["CALLIND", null, ["register:0:8"]]
+ 0050d0ac ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050d0ac ["INT_ADD", "register:40f0:8", ["const:50d0ac:8", "const:4:8"]]
+ 0050d0ac ["CALLIND", null, ["register:0:8"]]
- 0050d06c bytes 20013fd6
+ 0050d0ac bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-657feb8b96a8737fa05a64627d037c25"></a>

### [`0050d344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050d/0050d344.md) → [`0050d384`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050d/0050d384.md) _ZNK5Botan14PKCS10_Request9PEM_labelEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 72.73% / 新版 72.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050d390",
      "incomplete_value": true,
      "site": "0050d3a4",
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
                "const:29:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050d350",
      "incomplete_value": true,
      "site": "0050d364",
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
                "const:76:8"
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
      "0050d390",
      "READ",
      [
        "storage",
        "0029f076",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0050d390",
      "READ",
      [
        "storage",
        "0029f029",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050d348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050d/0050d344.md#insn-0050d348)
- 新版 [`0050d388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050d/0050d384.md#insn-0050d388)

~~~diff
- 0050d348 ["COPY", "tmp:0:8", ["const:76:8"]]
- 0050d348 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0050d348 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0050d348 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0050d388 ["COPY", "tmp:0:8", ["const:29:8"]]
+ 0050d388 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0050d388 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0050d388 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0050d348 bytes 4ad90191
+ 0050d388 bytes 4aa50091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-496d4554b53b2723036dd4d76e881c8d"></a>

### [`0050d370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050d/0050d370.md) → [`0050d3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050d/0050d3b0.md) _ZNK5Botan14PKCS10_Request20alternate_PEM_labelsEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00473540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473540.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00473580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/00473580.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 78.95% / 新版 78.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050d3e4",
      "incomplete_value": true,
      "site": "0050d3f4",
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
                "const:980:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050d3a4",
      "incomplete_value": true,
      "site": "0050d3b4",
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
                "const:9d4:8"
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
      "definition_site": "0050d3f8",
      "incomplete_value": true,
      "site": "0050d3f8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0050d3b8",
      "incomplete_value": true,
      "site": "0050d3b8",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050d3ec",
      "incomplete_value": true,
      "site": "0050d3fc",
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
                "const:490:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050d3ac",
      "incomplete_value": true,
      "site": "0050d3bc",
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
                "const:450:8"
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
      "0050d3e4",
      "READ",
      [
        "storage",
        "002bd9d4",
        null,
        "string"
      ]
    ],
    [
      "0050d3e8",
      "READ",
      [
        "storage",
        "002bd9e3",
        null,
        "string"
      ]
    ],
    [
      "0050d3ec",
      "READ",
      [
        "storage",
        "002c2450",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0050d3e4",
      "READ",
      [
        "storage",
        "002bd980",
        null,
        "string"
      ]
    ],
    [
      "0050d3e8",
      "READ",
      [
        "storage",
        "002bd98f",
        null,
        "string"
      ]
    ],
    [
      "0050d3ec",
      "READ",
      [
        "storage",
        "002c2490",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050d394`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050d/0050d370.md#insn-0050d394) · [`0050d39c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050d/0050d370.md#insn-0050d39c) · [`0050d3a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050d/0050d370.md#insn-0050d3a0)
- 新版 [`0050d3d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050d/0050d3b0.md#insn-0050d3d4) · [`0050d3dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050d/0050d3b0.md#insn-0050d3dc)

~~~diff
- 0050d394 ["INT_ADD", "register:40f0:8", ["const:50d394:8", "const:4:8"]]
- 0050d394 ["CALL", null, ["callee:00c57f60:8"]]
+ 0050d3d4 ["INT_ADD", "register:40f0:8", ["const:50d3d4:8", "const:4:8"]]
+ 0050d3d4 ["CALL", null, ["callee:00c57f60:8"]]
- 0050d394 bytes bf2a1d94
+ 0050d3d4 bytes e32a1d94
- 0050d39c ["COPY", "tmp:0:8", ["const:9d4:8"]]
- 0050d39c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0050d39c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0050d39c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0050d3dc ["COPY", "tmp:0:8", ["const:980:8"]]
+ 0050d3dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0050d3dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0050d3dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0050d39c bytes 08512791
+ 0050d3dc bytes 08012691
- 0050d3a0 ["COPY", "register:4048:8", ["const:2c2000:8"]]
- 0050d3a0 bytes a9edffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d45fec68d8ce5d6db0fb1e9ffef7c477"></a>

### [`0050d434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050d/0050d434.md) → [`0050d474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050d/0050d474.md) _ZN5Botan14PKCS10_RequestC2ERNS_10DataSourceE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md) [`00c59c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59c80.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md) [`00c59d50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59d50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050d4b4",
      "incomplete_value": true,
      "site": "0050d4b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0050d474",
      "incomplete_value": true,
      "site": "0050d474",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0050d4b4",
      "incomplete_value": true,
      "site": "0050d4b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0050d474",
      "incomplete_value": true,
      "site": "0050d474",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0050d4f4",
      "incomplete_value": true,
      "site": "0050d4fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0050d4b4",
      "incomplete_value": true,
      "site": "0050d4bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "0050d494",
      "READ",
      [
        "storage",
        "00c9b158",
        null,
        "pointer"
      ]
    ],
    [
      "0050d49c",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "0050d4b4",
      "DATA",
      [
        "storage",
        "00c69a20",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "0050d494",
      "READ",
      [
        "storage",
        "00c9b228",
        null,
        "pointer"
      ]
    ],
    [
      "0050d49c",
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ],
    [
      "0050d4b4",
      "DATA",
      [
        "storage",
        "00c69af0",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050d454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050d/0050d434.md#insn-0050d454) · [`0050d45c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050d/0050d434.md#insn-0050d45c) · [`0050d480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050d/0050d434.md#insn-0050d480)
- 新版 [`0050d494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050d/0050d474.md#insn-0050d494) · [`0050d49c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050d/0050d474.md#insn-0050d49c) · [`0050d4c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050d/0050d474.md#insn-0050d4c0)

~~~diff
- 0050d454 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:158:8"]]
- 0050d454 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050d494 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:228:8"]]
+ 0050d494 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050d454 bytes 08ad40f9
+ 0050d494 bytes 081541f9
- 0050d45c ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:d38:8"]]
- 0050d45c ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050d49c ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:e08:8"]]
+ 0050d49c ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 0050d45c bytes 4a9d46f9
+ 0050d49c bytes 4a0547f9
- 0050d480 ["INT_ADD", "register:40f0:8", ["const:50d480:8", "const:4:8"]]
- 0050d480 ["CALL", null, ["callee:00c58760:8"]]
+ 0050d4c0 ["INT_ADD", "register:40f0:8", ["const:50d4c0:8", "const:4:8"]]
+ 0050d4c0 ["CALL", null, ["callee:00c58760:8"]]
- 0050d480 bytes 842c1d94
+ 0050d4c0 bytes a82c1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d445cefe2398d8377e75903d454544ee"></a>

### [`0050d538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050d/0050d538.md) → [`0050d578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050d/0050d578.md) _ZN5Botan11X509_Object9load_dataERNS_10DataSourceE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59c80.md) · 呼出先 18件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044fcbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044fcbc.md) [`004a6f9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6f9c.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`005402a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005402a4.md)
- 新版 呼出元 1件 [`00c59d50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59d50.md) · 呼出先 18件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0044fcfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044fcfc.md) [`004a6fdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a6fdc.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`005402e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/005402e4.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.22% / 新版 97.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 3件

アドレスに依存する影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050d610",
      "incomplete_value": true,
      "site": "0050d610",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0050d5d0",
      "incomplete_value": true,
      "site": "0050d5d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_target",
    "new": {
      "definition_site": "0050d64c",
      "incomplete_value": true,
      "site": "0050d64c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050d60c",
      "incomplete_value": true,
      "site": "0050d60c",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0050d724",
      "incomplete_value": true,
      "site": "0050d724",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050d6e4",
      "incomplete_value": true,
      "site": "0050d6e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0050d600",
      "READ",
      [
        "storage",
        "00c9ade0",
        null,
        "pointer"
      ]
    ],
    [
      "0050d610",
      "DATA",
      [
        "storage",
        "00c67388",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "0050d63c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050d600",
      "READ",
      [
        "storage",
        "00c9aeb0",
        null,
        "pointer"
      ]
    ],
    [
      "0050d610",
      "DATA",
      [
        "storage",
        "00c67458",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "0050d63c",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050d60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050d/0050d538.md#insn-0050d60c) · [`0050d6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050d/0050d538.md#insn-0050d6a4) · [`0050d6e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050d/0050d538.md#insn-0050d6e4)
- 新版 [`0050d64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050d/0050d578.md#insn-0050d64c) · [`0050d6e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050d/0050d578.md#insn-0050d6e4) · [`0050d724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050d/0050d578.md#insn-0050d724)

~~~diff
- 0050d60c ["COPY", "register:0:8", ["register:4048:8"]]
- 0050d60c ["INT_ADD", "register:40f0:8", ["const:50d60c:8", "const:4:8"]]
- 0050d60c ["CALLIND", null, ["register:0:8"]]
+ 0050d64c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050d64c ["INT_ADD", "register:40f0:8", ["const:50d64c:8", "const:4:8"]]
+ 0050d64c ["CALLIND", null, ["register:0:8"]]
- 0050d60c bytes 20013fd6
+ 0050d64c bytes 20013fd6
- 0050d6a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0050d6a4 ["INT_ADD", "register:40f0:8", ["const:50d6a4:8", "const:4:8"]]
- 0050d6a4 ["CALLIND", null, ["register:0:8"]]
+ 0050d6e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0050d6e4 ["INT_ADD", "register:40f0:8", ["const:50d6e4:8", "const:4:8"]]
+ 0050d6e4 ["CALLIND", null, ["register:0:8"]]
- 0050d6a4 bytes 00013fd6
+ 0050d6e4 bytes 00013fd6
- 0050d6e4 ["COPY", "register:0:8", ["register:4048:8"]]
- 0050d6e4 ["INT_ADD", "register:40f0:8", ["const:50d6e4:8", "const:4:8"]]
- 0050d6e4 ["CALLIND", null, ["register:0:8"]]
+ 0050d724 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050d724 ["INT_ADD", "register:40f0:8", ["const:50d724:8", "const:4:8"]]
+ 0050d724 ["CALLIND", null, ["register:0:8"]]
- 0050d6e4 bytes 20013fd6
+ 0050d724 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-760baa76ce3fdd65c7230cf388122863"></a>

### [`0050dda0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050d/0050dda0.md) → [`0050dde0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050d/0050dde0.md) _ZN5Botan14PKCS10_RequestC1ERKNSt6__ndk16vectorIhNS1_9allocatorIhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59f70.md) · 呼出先 7件 [`005403c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005403c8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md)
- 新版 呼出元 1件 [`00c5a040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a040.md) · 呼出先 7件 [`00540408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540408.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.72% / 新版 84.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050de20",
      "incomplete_value": true,
      "site": "0050de20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0050dde0",
      "incomplete_value": true,
      "site": "0050dde0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0050de20",
      "incomplete_value": true,
      "site": "0050de20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0050dde0",
      "incomplete_value": true,
      "site": "0050dde0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0050de68",
      "incomplete_value": true,
      "site": "0050de74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0050de28",
      "incomplete_value": true,
      "site": "0050de34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "0050de00",
      "READ",
      [
        "storage",
        "00c9b158",
        null,
        "pointer"
      ]
    ],
    [
      "0050de08",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "0050de20",
      "DATA",
      [
        "storage",
        "00c69a20",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "0050de00",
      "READ",
      [
        "storage",
        "00c9b228",
        null,
        "pointer"
      ]
    ],
    [
      "0050de08",
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ],
    [
      "0050de20",
      "DATA",
      [
        "storage",
        "00c69af0",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050de8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050d/0050dda0.md#insn-0050de8c) · [`0050ddc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050d/0050dda0.md#insn-0050ddc0) · [`0050ddc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050d/0050dda0.md#insn-0050ddc8)
- 新版 [`0050decc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050d/0050dde0.md#insn-0050decc) · [`0050de00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050d/0050dde0.md#insn-0050de00) · [`0050de08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050d/0050dde0.md#insn-0050de08)

~~~diff
- 0050de8c ["COPY", "register:0:8", ["register:4048:8"]]
- 0050de8c ["INT_ADD", "register:40f0:8", ["const:50de8c:8", "const:4:8"]]
- 0050de8c ["CALLIND", null, ["register:0:8"]]
+ 0050decc ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050decc ["INT_ADD", "register:40f0:8", ["const:50decc:8", "const:4:8"]]
+ 0050decc ["CALLIND", null, ["register:0:8"]]
- 0050de8c bytes 20013fd6
+ 0050decc bytes 20013fd6
- 0050ddc0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:158:8"]]
- 0050ddc0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050de00 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:228:8"]]
+ 0050de00 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050ddc0 bytes 08ad40f9
+ 0050de00 bytes 081541f9
- 0050ddc8 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:d38:8"]]
- 0050ddc8 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050de08 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:e08:8"]]
+ 0050de08 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 0050ddc8 bytes 4a9d46f9
+ 0050de08 bytes 4a0547f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9abbb4c470ca488a90289c01c0ed59f9"></a>

### [`0050df18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050d/0050df18.md) → [`0050df58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050d/0050df58.md) _ZN5Botan14PKCS10_RequestC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md) [`00c59660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59660.md) [`00c59670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59670.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md) [`00c59730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59730.md) [`00c59740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59740.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.19% / 新版 85.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050df98",
      "incomplete_value": true,
      "site": "0050df98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0050df58",
      "incomplete_value": true,
      "site": "0050df58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0050df98",
      "incomplete_value": true,
      "site": "0050df98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0050df58",
      "incomplete_value": true,
      "site": "0050df58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0050dfd8",
      "incomplete_value": true,
      "site": "0050dfe0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0050df98",
      "incomplete_value": true,
      "site": "0050dfa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "0050df78",
      "READ",
      [
        "storage",
        "00c9b158",
        null,
        "pointer"
      ]
    ],
    [
      "0050df80",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "0050df98",
      "DATA",
      [
        "storage",
        "00c69a20",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "0050df78",
      "READ",
      [
        "storage",
        "00c9b228",
        null,
        "pointer"
      ]
    ],
    [
      "0050df80",
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ],
    [
      "0050df98",
      "DATA",
      [
        "storage",
        "00c69af0",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050df38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050d/0050df18.md#insn-0050df38) · [`0050df40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050d/0050df18.md#insn-0050df40) · [`0050df64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050d/0050df18.md#insn-0050df64)
- 新版 [`0050df78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050d/0050df58.md#insn-0050df78) · [`0050df80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050d/0050df58.md#insn-0050df80) · [`0050dfa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050d/0050df58.md#insn-0050dfa4)

~~~diff
- 0050df38 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:158:8"]]
- 0050df38 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050df78 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:228:8"]]
+ 0050df78 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050df38 bytes 08ad40f9
+ 0050df78 bytes 081541f9
- 0050df40 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:d38:8"]]
- 0050df40 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050df80 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:e08:8"]]
+ 0050df80 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 0050df40 bytes 4a9d46f9
+ 0050df80 bytes 4a0547f9
- 0050df64 ["INT_ADD", "register:40f0:8", ["const:50df64:8", "const:4:8"]]
- 0050df64 ["CALL", null, ["callee:00c58760:8"]]
+ 0050dfa4 ["INT_ADD", "register:40f0:8", ["const:50dfa4:8", "const:4:8"]]
+ 0050dfa4 ["CALL", null, ["callee:00c58760:8"]]
- 0050df64 bytes cb291d94
+ 0050dfa4 bytes ef291d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-430a15b3665a30f1bd0fe198a98cd186"></a>

### [`0050e044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050e/0050e044.md) → [`0050e084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050e/0050e084.md) _ZN5Botan14PKCS10_Request12force_decodeEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 40件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`004a5fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5fa0.md) [`004a6c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6c1c.md)
- 新版 呼出元 0件  · 呼出先 40件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`004a5fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a5fe0.md) [`004a6c5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a6c5c.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.45% / 新版 96.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_value` 4件

アドレスに依存する影響 `call_argument_candidate` 4件, `call_target` 5件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050e25c",
      "incomplete_value": true,
      "site": "0050e27c",
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
                "const:490:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050e21c",
      "incomplete_value": true,
      "site": "0050e23c",
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
                "const:450:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "0050e4f4",
      "incomplete_value": true,
      "site": "0050e504",
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
                "const:ffd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050e4b4",
      "incomplete_value": true,
      "site": "0050e4c4",
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
                "const:4a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 58,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050e508",
      "incomplete_value": true,
      "site": "0050e508",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0050e4c8",
      "incomplete_value": true,
      "site": "0050e4c8",
      "value": [
        "LOAD",
        "8",
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
      "0050e250",
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      "0050e25c",
      "READ",
      [
        "storage",
        "002c2450",
        null,
        null
      ]
    ],
    [
      "0050e2a4",
      "DATA",
      [
        "storage",
        "00c661d8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "0050e250",
      "READ",
      [
        "storage",
        "00c9ae28",
        null,
        "pointer"
      ]
    ],
    [
      "0050e25c",
      "READ",
      [
        "storage",
        "002c2490",
        null,
        null
      ]
    ],
    [
      "0050e2a4",
      "DATA",
      [
        "storage",
        "00c662a8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050e568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050e/0050e044.md#insn-0050e568) · [`0050e5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050e/0050e044.md#insn-0050e5a8) · [`0050e5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050e/0050e044.md#insn-0050e5e8)
- 新版 [`0050e5a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050e/0050e084.md#insn-0050e5a8) · [`0050e5e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050e/0050e084.md#insn-0050e5e8) · [`0050e628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050e/0050e084.md#insn-0050e628)

~~~diff
- 0050e568 ["INT_ADD", "register:40f0:8", ["const:50e568:8", "const:4:8"]]
- 0050e568 ["CALL", null, ["callee:00c58af0:8"]]
+ 0050e5a8 ["INT_ADD", "register:40f0:8", ["const:50e5a8:8", "const:4:8"]]
+ 0050e5a8 ["CALL", null, ["callee:00c58af0:8"]]
- 0050e568 bytes 2e291d94
+ 0050e5a8 bytes 52291d94
- 0050e5a8 ["COPY", "register:0:8", ["register:4048:8"]]
- 0050e5a8 ["INT_ADD", "register:40f0:8", ["const:50e5a8:8", "const:4:8"]]
- 0050e5a8 ["CALLIND", null, ["register:0:8"]]
+ 0050e5e8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050e5e8 ["INT_ADD", "register:40f0:8", ["const:50e5e8:8", "const:4:8"]]
+ 0050e5e8 ["CALLIND", null, ["register:0:8"]]
- 0050e5a8 bytes 20013fd6
+ 0050e5e8 bytes 20013fd6
- 0050e5e8 ["INT_ADD", "register:40f0:8", ["const:50e5e8:8", "const:4:8"]]
- 0050e5e8 ["CALL", null, ["callee:00c57fc0:8"]]
+ 0050e628 ["INT_ADD", "register:40f0:8", ["const:50e628:8", "const:4:8"]]
+ 0050e628 ["CALL", null, ["callee:00c57fc0:8"]]
- 0050e5e8 bytes 42261d94
+ 0050e628 bytes 66261d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7cae9dec3756a1d56efa0eecf43cb01b"></a>

### [`0050edac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050e/0050edac.md) → [`0050edec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050e/0050edec.md) _ZNK5Botan11X509_Object15check_signatureEPKNS_10Public_KeyE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59ca0.md) · 呼出先 8件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c57f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`00c59d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59d70.md) · 呼出先 8件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c58030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58030.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.89% / 新版 95.89%

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
      "definition_site": "0050ee80",
      "incomplete_value": false,
      "site": "0050ee8c",
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
            "const:e25:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050ee40",
      "incomplete_value": false,
      "site": "0050ee4c",
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
            "const:e79:8"
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
      "definition_site": "0050eeac",
      "incomplete_value": false,
      "site": "0050eeb4",
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
            "const:a5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050ee6c",
      "incomplete_value": false,
      "site": "0050ee74",
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
            "const:f2:8"
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
      "definition_site": "0050eefc",
      "incomplete_value": true,
      "site": "0050ef08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050eebc",
      "incomplete_value": true,
      "site": "0050eec8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d88:8"
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
      "0050ee80",
      "PARAM",
      [
        "storage",
        "002bfe79",
        null,
        "string"
      ]
    ],
    [
      "0050eeac",
      "PARAM",
      [
        "storage",
        "0029f0f2",
        null,
        "string"
      ]
    ],
    [
      "0050eef8",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0050ee80",
      "PARAM",
      [
        "storage",
        "002bfe25",
        null,
        "string"
      ]
    ],
    [
      "0050eeac",
      "PARAM",
      [
        "storage",
        "0029f0a5",
        null,
        "string"
      ]
    ],
    [
      "0050eef8",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050ee4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050e/0050edac.md#insn-0050ee4c) · [`0050ee74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050e/0050edac.md#insn-0050ee74) · [`0050eec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050e/0050edac.md#insn-0050eec8)
- 新版 [`0050ee8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050e/0050edec.md#insn-0050ee8c) · [`0050eeb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050e/0050edec.md#insn-0050eeb4) · [`0050ef08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050e/0050edec.md#insn-0050ef08)

~~~diff
- 0050ee4c ["INT_ADD", "register:40f0:8", ["const:50ee4c:8", "const:4:8"]]
- 0050ee4c ["CALL", null, ["callee:00c58030:8"]]
+ 0050ee8c ["INT_ADD", "register:40f0:8", ["const:50ee8c:8", "const:4:8"]]
+ 0050ee8c ["CALL", null, ["callee:00c58030:8"]]
- 0050ee4c bytes 45241d94
+ 0050ee8c bytes 69241d94
- 0050ee74 ["INT_ADD", "register:40f0:8", ["const:50ee74:8", "const:4:8"]]
- 0050ee74 ["CALL", null, ["callee:00c58040:8"]]
+ 0050eeb4 ["INT_ADD", "register:40f0:8", ["const:50eeb4:8", "const:4:8"]]
+ 0050eeb4 ["CALL", null, ["callee:00c58040:8"]]
- 0050ee74 bytes 3f241d94
+ 0050eeb4 bytes 63241d94
- 0050eec8 ["INT_ADD", "register:40f0:8", ["const:50eec8:8", "const:4:8"]]
- 0050eec8 ["CALL", null, ["callee:00c57fe0:8"]]
+ 0050ef08 ["INT_ADD", "register:40f0:8", ["const:50ef08:8", "const:4:8"]]
+ 0050ef08 ["CALL", null, ["callee:00c57fe0:8"]]
- 0050eec8 bytes 12241d94
+ 0050ef08 bytes 36241d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a96df3a5a92d49bc098110a1354e679a"></a>

### [`0050ef8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050e/0050ef8c.md) → [`0050efcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050e/0050efcc.md) _ZNK5Botan14PKCS10_Request18subject_public_keyEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59c90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59c90.md) · 呼出先 6件 [`00536d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536d04.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c596d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c596d0.md) [`00c59cc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59cc0.md)
- 新版 呼出元 1件 [`00c59d60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59d60.md) · 呼出先 6件 [`00536d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536d44.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c597a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c597a0.md) [`00c59d90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59d90.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.65% / 新版 95.65%

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
      "definition_site": "0050f004",
      "incomplete_value": true,
      "site": "0050f004",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0050efc4",
      "incomplete_value": true,
      "site": "0050efc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0050f04c",
      "incomplete_value": true,
      "site": "0050f04c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050f00c",
      "incomplete_value": true,
      "site": "0050f00c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0050eff4",
      "READ",
      [
        "storage",
        "00c9ade0",
        null,
        "pointer"
      ]
    ],
    [
      "0050f004",
      "DATA",
      [
        "storage",
        "00c67388",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "0050f03c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050eff4",
      "READ",
      [
        "storage",
        "00c9aeb0",
        null,
        "pointer"
      ]
    ],
    [
      "0050f004",
      "DATA",
      [
        "storage",
        "00c67458",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "0050f03c",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050f00c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050e/0050ef8c.md#insn-0050f00c) · [`0050efac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050e/0050ef8c.md#insn-0050efac) · [`0050efb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050e/0050ef8c.md#insn-0050efb4)
- 新版 [`0050f04c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050e/0050efcc.md#insn-0050f04c) · [`0050efec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050e/0050efcc.md#insn-0050efec) · [`0050eff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050e/0050efcc.md#insn-0050eff4)

~~~diff
- 0050f00c ["COPY", "register:0:8", ["register:4048:8"]]
- 0050f00c ["INT_ADD", "register:40f0:8", ["const:50f00c:8", "const:4:8"]]
- 0050f00c ["CALLIND", null, ["register:0:8"]]
+ 0050f04c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050f04c ["INT_ADD", "register:40f0:8", ["const:50f04c:8", "const:4:8"]]
+ 0050f04c ["CALLIND", null, ["register:0:8"]]
- 0050f00c bytes 20013fd6
+ 0050f04c bytes 20013fd6
- 0050efac ["INT_ADD", "register:40f0:8", ["const:50efac:8", "const:4:8"]]
- 0050efac ["CALL", null, ["callee:00c59d90:8"]]
+ 0050efec ["INT_ADD", "register:40f0:8", ["const:50efec:8", "const:4:8"]]
+ 0050efec ["CALL", null, ["callee:00c59d90:8"]]
- 0050efac bytes 452b1d94
+ 0050efec bytes 692b1d94
- 0050efb4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:de0:8"]]
- 0050efb4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050eff4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:eb0:8"]]
+ 0050eff4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050efb4 bytes 08f146f9
+ 0050eff4 bytes 085947f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2745355ce3b14734777e57879b57a48"></a>

### [`0050f0a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f0a8.md) → [`0050f0e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f0e8.md) _ZNK5Botan14PKCS10_Request4dataEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59cc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59cc0.md) · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`00c59d90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59d90.md) · 呼出先 6件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.45% / 新版 95.45%

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
      "definition_site": "0050f148",
      "incomplete_value": false,
      "site": "0050f150",
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
            "const:19d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050f108",
      "incomplete_value": false,
      "site": "0050f110",
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
            "const:1ea:8"
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
      "definition_site": "0050f184",
      "incomplete_value": true,
      "site": "0050f190",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050f144",
      "incomplete_value": true,
      "site": "0050f150",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0050f180",
      "incomplete_value": false,
      "site": "0050f190",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "0050f140",
      "incomplete_value": false,
      "site": "0050f150",
      "value": [
        "leaf",
        "const:535868:8"
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
      "0050f148",
      "PARAM",
      [
        "storage",
        "002a11ea",
        null,
        "string"
      ]
    ],
    [
      "0050f180",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "0050f184",
      "READ",
      [
        "storage",
        "00c9ad50",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050f148",
      "PARAM",
      [
        "storage",
        "002a119d",
        null,
        "string"
      ]
    ],
    [
      "0050f180",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "0050f184",
      "READ",
      [
        "storage",
        "00c9ae20",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050f110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f0a8.md#insn-0050f110) · [`0050f150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f0a8.md#insn-0050f150) · [`0050f0fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f0a8.md#insn-0050f0fc)
- 新版 [`0050f150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f0e8.md#insn-0050f150) · [`0050f190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f0e8.md#insn-0050f190) · [`0050f13c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f0e8.md#insn-0050f13c)

~~~diff
- 0050f110 ["INT_ADD", "register:40f0:8", ["const:50f110:8", "const:4:8"]]
- 0050f110 ["CALL", null, ["callee:0043de18:8"]]
+ 0050f150 ["INT_ADD", "register:40f0:8", ["const:50f150:8", "const:4:8"]]
+ 0050f150 ["CALL", null, ["callee:0043de18:8"]]
- 0050f110 bytes 32bbfc97
+ 0050f150 bytes 32bbfc97
- 0050f150 ["INT_ADD", "register:40f0:8", ["const:50f150:8", "const:4:8"]]
- 0050f150 ["CALL", null, ["callee:00c57fe0:8"]]
+ 0050f190 ["INT_ADD", "register:40f0:8", ["const:50f190:8", "const:4:8"]]
+ 0050f190 ["CALL", null, ["callee:00c57fe0:8"]]
- 0050f150 bytes 70231d94
+ 0050f190 bytes 94231d94
- 0050f0fc ["INT_ADD", "register:40f0:8", ["const:50f0fc:8", "const:4:8"]]
- 0050f0fc ["CALL", null, ["callee:00c57fc0:8"]]
+ 0050f13c ["INT_ADD", "register:40f0:8", ["const:50f13c:8", "const:4:8"]]
+ 0050f13c ["CALL", null, ["callee:00c57fc0:8"]]
- 0050f0fc bytes 7d231d94
+ 0050f13c bytes a1231d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4d7ef0310336b2a28a7d9b43bf2584e"></a>

### [`0050f240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f240.md) → [`0050f280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f280.md) _ZNK5Botan14PKCS10_Request11constraintsEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59cd0.md) · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58680.md) [`00c59ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59ac0.md) [`00c59cc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59cc0.md)
- 新版 呼出元 1件 [`00c59da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59da0.md) · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58750.md) [`00c59b90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b90.md) [`00c59d90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59d90.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050f2c4",
      "incomplete_value": true,
      "site": "0050f2c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b89:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050f284",
      "incomplete_value": true,
      "site": "0050f284",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b5a:8"
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
      "definition_site": "0050f2b8",
      "incomplete_value": true,
      "site": "0050f2c8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0050f278",
      "incomplete_value": true,
      "site": "0050f288",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0050f330",
      "incomplete_value": true,
      "site": "0050f330",
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
      "definition_site": "0050f2f0",
      "incomplete_value": true,
      "site": "0050f2f0",
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
      "0050f2b0",
      "READ",
      [
        "storage",
        "002a9b5a",
        null,
        "string"
      ]
    ],
    [
      "0050f2b8",
      "READ",
      [
        "storage",
        "002a9b61",
        null,
        "string"
      ]
    ],
    [
      "0050f320",
      "READ",
      [
        "storage",
        "00c9b178",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050f2b0",
      "READ",
      [
        "storage",
        "002a9b89",
        null,
        "string"
      ]
    ],
    [
      "0050f2b8",
      "READ",
      [
        "storage",
        "002a9b90",
        null,
        "string"
      ]
    ],
    [
      "0050f320",
      "READ",
      [
        "storage",
        "00c9b248",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050f2b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f240.md#insn-0050f2b0) · [`0050f2c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f240.md#insn-0050f2c4) · [`0050f260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f240.md#insn-0050f260)
- 新版 [`0050f2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f280.md#insn-0050f2f0) · [`0050f304`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f280.md#insn-0050f304) · [`0050f2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f280.md#insn-0050f2a0)

~~~diff
- 0050f2b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0050f2b0 ["INT_ADD", "register:40f0:8", ["const:50f2b0:8", "const:4:8"]]
- 0050f2b0 ["CALLIND", null, ["register:0:8"]]
+ 0050f2f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0050f2f0 ["INT_ADD", "register:40f0:8", ["const:50f2f0:8", "const:4:8"]]
+ 0050f2f0 ["CALLIND", null, ["register:0:8"]]
- 0050f2b0 bytes 00013fd6
+ 0050f2f0 bytes 00013fd6
- 0050f2c4 ["INT_ADD", "register:40f0:8", ["const:50f2c4:8", "const:4:8"]]
- 0050f2c4 ["CALL", null, ["callee:00c57f80:8"]]
+ 0050f304 ["INT_ADD", "register:40f0:8", ["const:50f304:8", "const:4:8"]]
+ 0050f304 ["CALL", null, ["callee:00c57f80:8"]]
- 0050f2c4 bytes fb221d94
+ 0050f304 bytes 1f231d94
- 0050f260 ["INT_ADD", "register:40f0:8", ["const:50f260:8", "const:4:8"]]
- 0050f260 ["CALL", null, ["callee:00c59d90:8"]]
+ 0050f2a0 ["INT_ADD", "register:40f0:8", ["const:50f2a0:8", "const:4:8"]]
+ 0050f2a0 ["CALL", null, ["callee:00c59d90:8"]]
- 0050f260 bytes 982a1d94
+ 0050f2a0 bytes bc2a1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55901ccc188cb988783902d3ec51f625"></a>

### [`0050f3ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f3ec.md) → [`0050f42c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f42c.md) _ZNK5Botan14PKCS10_Request14ex_constraintsEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c59cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59cf0.md) · 呼出先 12件 [`00531b84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531b84.md) [`0053ee70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053e/0053ee70.md) [`0053f004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053f004.md) [`005406d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005406d4.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md)
- 新版 呼出元 1件 [`00c59dc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59dc0.md) · 呼出先 12件 [`00531bc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531bc4.md) [`0053eeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053e/0053eeb0.md) [`0053f044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053f044.md) [`00540714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540714.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_condition, store_value

命令の説明率　旧版 93.50% / 新版 93.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050f474",
      "incomplete_value": true,
      "site": "0050f484",
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
                "const:2ba000:8"
              ],
              [
                "leaf",
                "const:1a5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050f434",
      "incomplete_value": true,
      "site": "0050f444",
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
                "const:2ba000:8"
              ],
              [
                "leaf",
                "const:1f9:8"
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
      "definition_site": "0050f488",
      "incomplete_value": true,
      "site": "0050f488",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0050f448",
      "incomplete_value": true,
      "site": "0050f448",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050f47c",
      "incomplete_value": true,
      "site": "0050f48c",
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
                "const:490:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050f43c",
      "incomplete_value": true,
      "site": "0050f44c",
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
                "const:450:8"
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
      "0050f474",
      "READ",
      [
        "storage",
        "002ba1f9",
        null,
        "string"
      ]
    ],
    [
      "0050f478",
      "READ",
      [
        "storage",
        "002ba208",
        null,
        "string"
      ]
    ],
    [
      "0050f47c",
      "READ",
      [
        "storage",
        "002c2450",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0050f474",
      "READ",
      [
        "storage",
        "002ba1a5",
        null,
        "string"
      ]
    ],
    [
      "0050f478",
      "READ",
      [
        "storage",
        "002ba1b4",
        null,
        "string"
      ]
    ],
    [
      "0050f47c",
      "READ",
      [
        "storage",
        "002c2490",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050f478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f3ec.md#insn-0050f478) · [`0050f48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f3ec.md#insn-0050f48c) · [`0050f418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f3ec.md#insn-0050f418)
- 新版 [`0050f4b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f42c.md#insn-0050f4b8) · [`0050f4cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f42c.md#insn-0050f4cc) · [`0050f458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f42c.md#insn-0050f458)

~~~diff
- 0050f478 ["COPY", "register:0:8", ["register:4040:8"]]
- 0050f478 ["INT_ADD", "register:40f0:8", ["const:50f478:8", "const:4:8"]]
- 0050f478 ["CALLIND", null, ["register:0:8"]]
+ 0050f4b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0050f4b8 ["INT_ADD", "register:40f0:8", ["const:50f4b8:8", "const:4:8"]]
+ 0050f4b8 ["CALLIND", null, ["register:0:8"]]
- 0050f478 bytes 00013fd6
+ 0050f4b8 bytes 00013fd6
- 0050f48c ["INT_ADD", "register:40f0:8", ["const:50f48c:8", "const:4:8"]]
- 0050f48c ["CALL", null, ["callee:00c57f80:8"]]
+ 0050f4cc ["INT_ADD", "register:40f0:8", ["const:50f4cc:8", "const:4:8"]]
+ 0050f4cc ["CALL", null, ["callee:00c57f80:8"]]
- 0050f48c bytes 89221d94
+ 0050f4cc bytes ad221d94
- 0050f418 ["INT_ADD", "register:40f0:8", ["const:50f418:8", "const:4:8"]]
- 0050f418 ["CALL", null, ["callee:00c59d90:8"]]
+ 0050f458 ["INT_ADD", "register:40f0:8", ["const:50f458:8", "const:4:8"]]
+ 0050f458 ["CALL", null, ["callee:00c59d90:8"]]
- 0050f418 bytes 2a2a1d94
+ 0050f458 bytes 4e2a1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5010569c3de4579e0fdc81e2d5751942"></a>

### [`0050f614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f614.md) → [`0050f654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f654.md) _ZNK5Botan14PKCS10_Request5is_CAEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c59d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59d00.md) · 呼出先 7件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58680.md) [`00c59ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59ac0.md)
- 新版 呼出元 1件 [`00c59dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59dd0.md) · 呼出先 7件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58750.md) [`00c59b90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b90.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.33% / 新版 89.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050f690",
      "incomplete_value": true,
      "site": "0050f6a0",
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
                "const:2c1000:8"
              ],
              [
                "leaf",
                "const:67:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050f650",
      "incomplete_value": true,
      "site": "0050f660",
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
                "const:2c1000:8"
              ],
              [
                "leaf",
                "const:27:8"
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
      "definition_site": "0050f6a4",
      "incomplete_value": true,
      "site": "0050f6a4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0050f664",
      "incomplete_value": true,
      "site": "0050f664",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050f698",
      "incomplete_value": true,
      "site": "0050f6a8",
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
                "const:490:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050f658",
      "incomplete_value": true,
      "site": "0050f668",
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
                "const:450:8"
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
      "0050f690",
      "READ",
      [
        "storage",
        "002c1027",
        null,
        "string"
      ]
    ],
    [
      "0050f694",
      "READ",
      [
        "storage",
        "002c1036",
        null,
        "string"
      ]
    ],
    [
      "0050f698",
      "READ",
      [
        "storage",
        "002c2450",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0050f690",
      "READ",
      [
        "storage",
        "002c1067",
        null,
        "string"
      ]
    ],
    [
      "0050f694",
      "READ",
      [
        "storage",
        "002c1076",
        null,
        "string"
      ]
    ],
    [
      "0050f698",
      "READ",
      [
        "storage",
        "002c2490",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050f694`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f614.md#insn-0050f694) · [`0050f6a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f614.md#insn-0050f6a8) · [`0050f634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f614.md#insn-0050f634)
- 新版 [`0050f6d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f654.md#insn-0050f6d4) · [`0050f6e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f654.md#insn-0050f6e8) · [`0050f674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f654.md#insn-0050f674)

~~~diff
- 0050f694 ["COPY", "register:0:8", ["register:4040:8"]]
- 0050f694 ["INT_ADD", "register:40f0:8", ["const:50f694:8", "const:4:8"]]
- 0050f694 ["CALLIND", null, ["register:0:8"]]
+ 0050f6d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0050f6d4 ["INT_ADD", "register:40f0:8", ["const:50f6d4:8", "const:4:8"]]
+ 0050f6d4 ["CALLIND", null, ["register:0:8"]]
- 0050f694 bytes 00013fd6
+ 0050f6d4 bytes 00013fd6
- 0050f6a8 ["INT_ADD", "register:40f0:8", ["const:50f6a8:8", "const:4:8"]]
- 0050f6a8 ["CALL", null, ["callee:00c57f80:8"]]
+ 0050f6e8 ["INT_ADD", "register:40f0:8", ["const:50f6e8:8", "const:4:8"]]
+ 0050f6e8 ["CALL", null, ["callee:00c57f80:8"]]
- 0050f6a8 bytes 02221d94
+ 0050f6e8 bytes 26221d94
- 0050f634 ["INT_ADD", "register:40f0:8", ["const:50f634:8", "const:4:8"]]
- 0050f634 ["CALL", null, ["callee:00c59d90:8"]]
+ 0050f674 ["INT_ADD", "register:40f0:8", ["const:50f674:8", "const:4:8"]]
+ 0050f674 ["CALL", null, ["callee:00c59d90:8"]]
- 0050f634 bytes a3291d94
+ 0050f674 bytes c7291d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d9e8d7b7be6a43817465d80e7a71db1"></a>

### [`0050f7a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f7a0.md) → [`0050f7e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f7e0.md) _ZNK5Botan14PKCS10_Request10path_limitEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c59d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59d10.md) · 呼出先 9件 [`00530fe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530fe8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58680.md)
- 新版 呼出元 1件 [`00c59de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59de0.md) · 呼出先 9件 [`00531028`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531028.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58750.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.24% / 新版 90.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050f81c",
      "incomplete_value": true,
      "site": "0050f82c",
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
                "const:2c1000:8"
              ],
              [
                "leaf",
                "const:67:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050f7dc",
      "incomplete_value": true,
      "site": "0050f7ec",
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
                "const:2c1000:8"
              ],
              [
                "leaf",
                "const:27:8"
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
      "definition_site": "0050f830",
      "incomplete_value": true,
      "site": "0050f830",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0050f7f0",
      "incomplete_value": true,
      "site": "0050f7f0",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050f824",
      "incomplete_value": true,
      "site": "0050f834",
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
                "const:490:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050f7e4",
      "incomplete_value": true,
      "site": "0050f7f4",
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
                "const:450:8"
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
      "0050f81c",
      "READ",
      [
        "storage",
        "002c1027",
        null,
        "string"
      ]
    ],
    [
      "0050f820",
      "READ",
      [
        "storage",
        "002c1036",
        null,
        "string"
      ]
    ],
    [
      "0050f824",
      "READ",
      [
        "storage",
        "002c2450",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0050f81c",
      "READ",
      [
        "storage",
        "002c1067",
        null,
        "string"
      ]
    ],
    [
      "0050f820",
      "READ",
      [
        "storage",
        "002c1076",
        null,
        "string"
      ]
    ],
    [
      "0050f824",
      "READ",
      [
        "storage",
        "002c2490",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050f820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f7a0.md#insn-0050f820) · [`0050f834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f7a0.md#insn-0050f834) · [`0050f7c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f7a0.md#insn-0050f7c0)
- 新版 [`0050f860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f7e0.md#insn-0050f860) · [`0050f874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f7e0.md#insn-0050f874) · [`0050f800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f7e0.md#insn-0050f800)

~~~diff
- 0050f820 ["COPY", "register:0:8", ["register:4040:8"]]
- 0050f820 ["INT_ADD", "register:40f0:8", ["const:50f820:8", "const:4:8"]]
- 0050f820 ["CALLIND", null, ["register:0:8"]]
+ 0050f860 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0050f860 ["INT_ADD", "register:40f0:8", ["const:50f860:8", "const:4:8"]]
+ 0050f860 ["CALLIND", null, ["register:0:8"]]
- 0050f820 bytes 00013fd6
+ 0050f860 bytes 00013fd6
- 0050f834 ["INT_ADD", "register:40f0:8", ["const:50f834:8", "const:4:8"]]
- 0050f834 ["CALL", null, ["callee:00c57f80:8"]]
+ 0050f874 ["INT_ADD", "register:40f0:8", ["const:50f874:8", "const:4:8"]]
+ 0050f874 ["CALL", null, ["callee:00c57f80:8"]]
- 0050f834 bytes 9f211d94
+ 0050f874 bytes c3211d94
- 0050f7c0 ["INT_ADD", "register:40f0:8", ["const:50f7c0:8", "const:4:8"]]
- 0050f7c0 ["CALL", null, ["callee:00c59d90:8"]]
+ 0050f800 ["INT_ADD", "register:40f0:8", ["const:50f800:8", "const:4:8"]]
+ 0050f800 ["CALL", null, ["callee:00c59d90:8"]]
- 0050f7c0 bytes 40291d94
+ 0050f800 bytes 64291d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f7a48deb929633203d46d3a11c0b4bc"></a>

### [`0050f948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f948.md) → [`0050f988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f988.md) _ZNK5Botan14Cert_Extension17Basic_Constraints14get_path_limitEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59d20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59d20.md) · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)
- 新版 呼出元 1件 [`00c59df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59df0.md) · 呼出先 6件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004aeca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.56% / 新版 95.56%

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
      "definition_site": "0050f9ec",
      "incomplete_value": false,
      "site": "0050f9f4",
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
            "const:c11:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050f9ac",
      "incomplete_value": false,
      "site": "0050f9b4",
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
            "const:be0:8"
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
      "definition_site": "0050fa28",
      "incomplete_value": true,
      "site": "0050fa34",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050f9e8",
      "incomplete_value": true,
      "site": "0050f9f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0050fa24",
      "incomplete_value": false,
      "site": "0050fa34",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "0050f9e4",
      "incomplete_value": false,
      "site": "0050f9f4",
      "value": [
        "leaf",
        "const:535868:8"
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
      "0050f9ec",
      "PARAM",
      [
        "storage",
        "002b2be0",
        null,
        "string"
      ]
    ],
    [
      "0050fa24",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "0050fa28",
      "READ",
      [
        "storage",
        "00c9ad48",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050f9ec",
      "PARAM",
      [
        "storage",
        "002b2c11",
        null,
        "string"
      ]
    ],
    [
      "0050fa24",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "0050fa28",
      "READ",
      [
        "storage",
        "00c9ae18",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050f9b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f948.md#insn-0050f9b4) · [`0050f9f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f948.md#insn-0050f9f4) · [`0050f9a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f948.md#insn-0050f9a0)
- 新版 [`0050f9f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f988.md#insn-0050f9f4) · [`0050fa34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f988.md#insn-0050fa34) · [`0050f9e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f988.md#insn-0050f9e0)

~~~diff
- 0050f9b4 ["INT_ADD", "register:40f0:8", ["const:50f9b4:8", "const:4:8"]]
- 0050f9b4 ["CALL", null, ["callee:0043de18:8"]]
+ 0050f9f4 ["INT_ADD", "register:40f0:8", ["const:50f9f4:8", "const:4:8"]]
+ 0050f9f4 ["CALL", null, ["callee:0043de18:8"]]
- 0050f9b4 bytes 09b9fc97
+ 0050f9f4 bytes 09b9fc97
- 0050f9f4 ["INT_ADD", "register:40f0:8", ["const:50f9f4:8", "const:4:8"]]
- 0050f9f4 ["CALL", null, ["callee:00c57fe0:8"]]
+ 0050fa34 ["INT_ADD", "register:40f0:8", ["const:50fa34:8", "const:4:8"]]
+ 0050fa34 ["CALL", null, ["callee:00c57fe0:8"]]
- 0050f9f4 bytes 47211d94
+ 0050fa34 bytes 6b211d94
- 0050f9a0 ["INT_ADD", "register:40f0:8", ["const:50f9a0:8", "const:4:8"]]
- 0050f9a0 ["CALL", null, ["callee:00c57fc0:8"]]
+ 0050f9e0 ["INT_ADD", "register:40f0:8", ["const:50f9e0:8", "const:4:8"]]
+ 0050f9e0 ["CALL", null, ["callee:00c57fc0:8"]]
- 0050f9a0 bytes 54211d94
+ 0050f9e0 bytes 78211d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ecefaaff59eeb256fcb7e6e1f1679c0e"></a>

### [`0050fa48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050fa48.md) → [`0050fa88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050fa88.md) _ZN5Botan7X509_CAC2ERKNS_16X509_CertificateERKNS_11Private_KeyERKNSt6__ndk112basic_stringIcNS7_11char_traitsIcEENS7_9allocatorIcEEEERNS_21Ra

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 19件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0050ff28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050ff28.md) [`00510060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00510/00510060.md)
- 新版 呼出元 0件  · 呼出先 19件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0050ff68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050ff68.md) [`005100a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00510/005100a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.38% / 新版 97.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050fad0",
      "incomplete_value": true,
      "site": "0050fad0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0050fa90",
      "incomplete_value": true,
      "site": "0050fa90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0050fb0c",
      "incomplete_value": true,
      "site": "0050fb10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0050facc",
      "incomplete_value": true,
      "site": "0050fad0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0050fc28",
      "incomplete_value": false,
      "site": "0050fc34",
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
            "const:c30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050fbe8",
      "incomplete_value": false,
      "site": "0050fbf4",
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
            "const:c8c:8"
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
      "0050fab4",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "0050fad0",
      "DATA",
      [
        "storage",
        "00c661a8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0050fb08",
      "READ",
      [
        "storage",
        "00c9b0e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050fab4",
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ],
    [
      "0050fad0",
      "DATA",
      [
        "storage",
        "00c66278",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0050fb08",
      "READ",
      [
        "storage",
        "00c9b1b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050fbf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050fa48.md#insn-0050fbf4) · [`0050fd98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050fa48.md#insn-0050fd98) · [`0050fdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050fa48.md#insn-0050fdd4)
- 新版 [`0050fc34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050fa88.md#insn-0050fc34) · [`0050fdd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050fa88.md#insn-0050fdd8) · [`0050fe14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050fa88.md#insn-0050fe14)

~~~diff
- 0050fbf4 ["INT_ADD", "register:40f0:8", ["const:50fbf4:8", "const:4:8"]]
- 0050fbf4 ["CALL", null, ["callee:0050ff68:8"]]
+ 0050fc34 ["INT_ADD", "register:40f0:8", ["const:50fc34:8", "const:4:8"]]
+ 0050fc34 ["CALL", null, ["callee:0050ff68:8"]]
- 0050fbf4 bytes cd000094
+ 0050fc34 bytes cd000094
- 0050fd98 ["INT_ADD", "register:40f0:8", ["const:50fd98:8", "const:4:8"]]
- 0050fd98 ["CALL", null, ["callee:0043de18:8"]]
+ 0050fdd8 ["INT_ADD", "register:40f0:8", ["const:50fdd8:8", "const:4:8"]]
+ 0050fdd8 ["CALL", null, ["callee:0043de18:8"]]
- 0050fd98 bytes 10b8fc97
+ 0050fdd8 bytes 10b8fc97
- 0050fdd4 ["INT_ADD", "register:40f0:8", ["const:50fdd4:8", "const:4:8"]]
- 0050fdd4 ["CALL", null, ["callee:00c57fe0:8"]]
+ 0050fe14 ["INT_ADD", "register:40f0:8", ["const:50fe14:8", "const:4:8"]]
+ 0050fe14 ["CALL", null, ["callee:00c57fe0:8"]]
- 0050fdd4 bytes 4f201d94
+ 0050fe14 bytes 73201d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e63fac5195258efc974d8a46783f85f"></a>

### [`00510060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00510/00510060.md) → [`005100a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00510/005100a0.md) FUN_005100a0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`0050fa48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050fa48.md) [`005109fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00510/005109fc.md) [`005127ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/005127ac.md) [`0052d510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052d510.md) [`0052e334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052e/0052e334.md) · 呼出先 16件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`0046d5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d5a8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 5件 [`0050fa88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050fa88.md) [`00510a3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00510/00510a3c.md) [`005127ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/005127ec.md) [`0052d550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052d550.md) [`0052e374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052e/0052e374.md) · 呼出先 16件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`0046d5e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d5e8.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.76% / 新版 97.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00510208",
      "incomplete_value": false,
      "site": "00510214",
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
            "const:375:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005101c8",
      "incomplete_value": false,
      "site": "005101d4",
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
            "const:3c9:8"
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
      "definition_site": "00510248",
      "incomplete_value": true,
      "site": "00510254",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00510208",
      "incomplete_value": true,
      "site": "00510214",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00510244",
      "incomplete_value": false,
      "site": "00510254",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "00510204",
      "incomplete_value": false,
      "site": "00510214",
      "value": [
        "leaf",
        "const:535868:8"
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
      "00510208",
      "PARAM",
      [
        "storage",
        "002ba3c9",
        null,
        "string"
      ]
    ],
    [
      "00510244",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "00510248",
      "READ",
      [
        "storage",
        "00c9ad30",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00510208",
      "PARAM",
      [
        "storage",
        "002ba375",
        null,
        "string"
      ]
    ],
    [
      "00510244",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "00510248",
      "READ",
      [
        "storage",
        "00c9ae00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005101d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00510/00510060.md#insn-005101d4) · [`00510214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00510/00510060.md#insn-00510214) · [`00510254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00510/00510060.md#insn-00510254)
- 新版 [`00510214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00510/005100a0.md#insn-00510214) · [`00510254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00510/005100a0.md#insn-00510254) · [`00510294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00510/005100a0.md#insn-00510294)

~~~diff
- 005101d4 ["INT_ADD", "register:40f0:8", ["const:5101d4:8", "const:4:8"]]
- 005101d4 ["CALL", null, ["callee:00c58180:8"]]
+ 00510214 ["INT_ADD", "register:40f0:8", ["const:510214:8", "const:4:8"]]
+ 00510214 ["CALL", null, ["callee:00c58180:8"]]
- 005101d4 bytes b71f1d94
+ 00510214 bytes db1f1d94
- 00510214 ["INT_ADD", "register:40f0:8", ["const:510214:8", "const:4:8"]]
- 00510214 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00510254 ["INT_ADD", "register:40f0:8", ["const:510254:8", "const:4:8"]]
+ 00510254 ["CALL", null, ["callee:00c57fe0:8"]]
- 00510214 bytes 3f1f1d94
+ 00510254 bytes 631f1d94
- 00510254 ["COPY", "tmp:0:8", ["const:66d:8"]]
- 00510254 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00510254 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00510254 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00510294 ["COPY", "tmp:0:8", ["const:619:8"]]
+ 00510294 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00510294 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00510294 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00510254 bytes 00b41991
+ 00510294 bytes 00641891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e14a8db0afde8599bb5f680c7744284f"></a>

### [`005109fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00510/005109fc.md) → [`00510a3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00510/00510a3c.md) _ZN5Botan7X509_CAC1ERKNS_16X509_CertificateERKNS_11Private_KeyERKNSt6__ndk13mapINS7_12basic_stringIcNS7_11char_traitsIcEENS7_9allocatorIcEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 14件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00510060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00510/00510060.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`0053b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053b000.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005100a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00510/005100a0.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`0053b040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053b040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.28% / 新版 95.28%

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
      "definition_site": "00510a88",
      "incomplete_value": true,
      "site": "00510a88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00510a48",
      "incomplete_value": true,
      "site": "00510a48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00510ac4",
      "incomplete_value": true,
      "site": "00510ac8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00510a84",
      "incomplete_value": true,
      "site": "00510a88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00510b98",
      "incomplete_value": false,
      "site": "00510ba0",
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
            "const:3d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00510b58",
      "incomplete_value": false,
      "site": "00510b60",
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
            "const:8a:8"
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
      "00510a68",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "00510a88",
      "DATA",
      [
        "storage",
        "00c661a8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00510ac0",
      "READ",
      [
        "storage",
        "00c9b0e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00510a68",
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ],
    [
      "00510a88",
      "DATA",
      [
        "storage",
        "00c66278",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00510ac0",
      "READ",
      [
        "storage",
        "00c9b1b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00510b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00510/005109fc.md#insn-00510b60) · [`00510b9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00510/005109fc.md#insn-00510b9c) · [`00510a28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00510/005109fc.md#insn-00510a28)
- 新版 [`00510ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00510/00510a3c.md#insn-00510ba0) · [`00510bdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00510/00510a3c.md#insn-00510bdc) · [`00510a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00510/00510a3c.md#insn-00510a68)

~~~diff
- 00510b60 ["INT_ADD", "register:40f0:8", ["const:510b60:8", "const:4:8"]]
- 00510b60 ["CALL", null, ["callee:0043de18:8"]]
+ 00510ba0 ["INT_ADD", "register:40f0:8", ["const:510ba0:8", "const:4:8"]]
+ 00510ba0 ["CALL", null, ["callee:0043de18:8"]]
- 00510b60 bytes 9eb4fc97
+ 00510ba0 bytes 9eb4fc97
- 00510b9c ["INT_ADD", "register:40f0:8", ["const:510b9c:8", "const:4:8"]]
- 00510b9c ["CALL", null, ["callee:00c57fe0:8"]]
+ 00510bdc ["INT_ADD", "register:40f0:8", ["const:510bdc:8", "const:4:8"]]
+ 00510bdc ["CALL", null, ["callee:00c57fe0:8"]]
- 00510b9c bytes dd1c1d94
+ 00510bdc bytes 011d1d94
- 00510a28 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d38:8"]]
- 00510a28 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00510a68 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e08:8"]]
+ 00510a68 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00510a28 bytes 299d46f9
+ 00510a68 bytes 290547f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b8097173028a87a9fc1b6c7598601c8"></a>

### [`00510d58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00510/00510d58.md) → [`00510d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00510/00510d98.md) _ZNK5Botan7X509_CA12sign_requestERKNS_14PKCS10_RequestERNS_21RandomNumberGeneratorERKNS_9X509_TimeES8_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 25件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`0050b35c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050b/0050b35c.md) [`00511224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00511/00511224.md) [`00511638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00511/00511638.md) [`0053b424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053b424.md)
- 新版 呼出元 0件  · 呼出先 25件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`0050b39c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050b/0050b39c.md) [`00511264`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00511/00511264.md) [`00511678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00511/00511678.md) [`0053b464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053b464.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.79% / 新版 96.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00510e84",
      "incomplete_value": true,
      "site": "00510e88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00510e44",
      "incomplete_value": true,
      "site": "00510e48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00510eb8",
      "incomplete_value": true,
      "site": "00510ebc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00510e78",
      "incomplete_value": true,
      "site": "00510e7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
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
      "definition_site": "00510ef8",
      "incomplete_value": true,
      "site": "00510f04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00510eb8",
      "incomplete_value": true,
      "site": "00510ec4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00510e78",
      "READ",
      [
        "storage",
        "00c9b188",
        null,
        "pointer"
      ]
    ],
    [
      "00510e88",
      "DATA",
      [
        "storage",
        "00c67950",
        null,
        "undefined1[96]"
      ]
    ],
    [
      "00510eb0",
      "READ",
      [
        "storage",
        "00c9b178",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00510e78",
      "READ",
      [
        "storage",
        "00c9b258",
        null,
        "pointer"
      ]
    ],
    [
      "00510e88",
      "DATA",
      [
        "storage",
        "00c67a20",
        null,
        "undefined1[96]"
      ]
    ],
    [
      "00510eb0",
      "READ",
      [
        "storage",
        "00c9b248",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00510e88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00510/00510d58.md#insn-00510e88) · [`00510f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00510/00510d58.md#insn-00510f78) · [`00510ff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00510/00510d58.md#insn-00510ff8)
- 新版 [`00510ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00510/00510d98.md#insn-00510ec8) · [`00510fb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00510/00510d98.md#insn-00510fb8) · [`00511038`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00510/00510d98.md#insn-00511038)

~~~diff
- 00510e88 ["INT_ADD", "register:40f0:8", ["const:510e88:8", "const:4:8"]]
- 00510e88 ["CALL", null, ["callee:00c59e00:8"]]
+ 00510ec8 ["INT_ADD", "register:40f0:8", ["const:510ec8:8", "const:4:8"]]
+ 00510ec8 ["CALL", null, ["callee:00c59e00:8"]]
- 00510e88 bytes aa231d94
+ 00510ec8 bytes ce231d94
- 00510f78 ["INT_ADD", "register:40f0:8", ["const:510f78:8", "const:4:8"]]
- 00510f78 ["CALL", null, ["callee:00c59e00:8"]]
+ 00510fb8 ["INT_ADD", "register:40f0:8", ["const:510fb8:8", "const:4:8"]]
+ 00510fb8 ["CALL", null, ["callee:00c59e00:8"]]
- 00510f78 bytes 6e231d94
+ 00510fb8 bytes 92231d94
- 00510ff8 ["INT_ADD", "register:40f0:8", ["const:510ff8:8", "const:4:8"]]
- 00510ff8 ["CALL", null, ["callee:0053eeb0:8"]]
+ 00511038 ["INT_ADD", "register:40f0:8", ["const:511038:8", "const:4:8"]]
+ 00511038 ["CALL", null, ["callee:0053eeb0:8"]]
- 00510ff8 bytes 9eb70094
+ 00511038 bytes 9eb70094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6721d4eb29ddd7496e76fd771f727434"></a>

### [`00511224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00511/00511224.md) → [`00511264`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00511/00511264.md) FUN_00511264

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00510d58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00510/00510d58.md) [`005269d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00526/005269d0.md) [`0052d510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052d510.md) [`0052e334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052e/0052e334.md) · 呼出先 7件 [`0053c40c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053c/0053c40c.md) [`0053ee70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053e/0053ee70.md) [`0053f004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053f004.md) [`005406d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005406d4.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md)
- 新版 呼出元 4件 [`00510d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00510/00510d98.md) [`00526a10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00526/00526a10.md) [`0052d550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052d550.md) [`0052e374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052e/0052e374.md) · 呼出先 7件 [`0053c44c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053c/0053c44c.md) [`0053eeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053e/0053eeb0.md) [`0053f044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053f044.md) [`00540714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540714.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005112a8",
      "incomplete_value": true,
      "site": "005112bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00511268",
      "incomplete_value": true,
      "site": "0051127c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00511298",
      "READ",
      [
        "storage",
        "00c9b110",
        null,
        "pointer"
      ]
    ],
    [
      "005112bc",
      "DATA",
      [
        "storage",
        "00c688c0",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00511298",
      "READ",
      [
        "storage",
        "00c9b1e0",
        null,
        "pointer"
      ]
    ],
    [
      "005112bc",
      "DATA",
      [
        "storage",
        "00c68990",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005112bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00511/00511224.md#insn-005112bc) · [`00511258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00511/00511224.md#insn-00511258) · [`00511298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00511/00511224.md#insn-00511298)
- 新版 [`005112fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00511/00511264.md#insn-005112fc) · [`00511298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00511/00511264.md#insn-00511298) · [`005112d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00511/00511264.md#insn-005112d8)

~~~diff
- 005112bc ["INT_ADD", "register:40f0:8", ["const:5112bc:8", "const:4:8"]]
- 005112bc ["CALL", null, ["callee:0053eeb0:8"]]
+ 005112fc ["INT_ADD", "register:40f0:8", ["const:5112fc:8", "const:4:8"]]
+ 005112fc ["CALL", null, ["callee:0053eeb0:8"]]
- 005112bc bytes edb60094
+ 005112fc bytes edb60094
- 00511258 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:110:8"]]
- 00511258 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00511298 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:1e0:8"]]
+ 00511298 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00511258 bytes 298940f9
+ 00511298 bytes 29f140f9
- 00511298 ["INT_ADD", "register:40f0:8", ["const:511298:8", "const:4:8"]]
- 00511298 ["CALL", null, ["callee:00c57f60:8"]]
+ 005112d8 ["INT_ADD", "register:40f0:8", ["const:5112d8:8", "const:4:8"]]
+ 005112d8 ["CALL", null, ["callee:00c57f60:8"]]
- 00511298 bytes fe1a1d94
+ 005112d8 bytes 221b1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df163ce450b12835ac1581d28ec3dc16"></a>

### [`005113cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00511/005113cc.md) → [`0051140c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00511/0051140c.md) _ZN5Botan10Extensions7replaceEPNS_21Certificate_ExtensionEb

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59d30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59d30.md) · 呼出先 13件 [`00516bc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516bc4.md) [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`0053d728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053d/0053d728.md) [`0054b944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054b944.md) [`0054bbfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054bbfc.md)
- 新版 呼出元 1件 [`00c59e00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59e00.md) · 呼出先 13件 [`00516c04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516c04.md) [`00535bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bac.md) [`0053d768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053d/0053d768.md) [`0054b984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054b/0054b984.md) [`0054bc3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054b/0054bc3c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.83% / 新版 97.83%

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
      "definition_site": "005114a0",
      "incomplete_value": true,
      "site": "005114a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00511460",
      "incomplete_value": true,
      "site": "00511460",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005114e4",
      "incomplete_value": true,
      "site": "005114e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005114a4",
      "incomplete_value": true,
      "site": "005114a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00511490",
      "READ",
      [
        "storage",
        "00c9b120",
        null,
        "pointer"
      ]
    ],
    [
      "005114a0",
      "DATA",
      [
        "storage",
        "00c6a438",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "005114d8",
      "READ",
      [
        "storage",
        "00c9ad40",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00511490",
      "READ",
      [
        "storage",
        "00c9b1f0",
        null,
        "pointer"
      ]
    ],
    [
      "005114a0",
      "DATA",
      [
        "storage",
        "00c6a508",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "005114d8",
      "READ",
      [
        "storage",
        "00c9ae10",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051140c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00511/005113cc.md#insn-0051140c) · [`00511418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00511/005113cc.md#insn-00511418) · [`00511428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00511/005113cc.md#insn-00511428)
- 新版 [`0051144c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00511/0051140c.md#insn-0051144c) · [`00511458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00511/0051140c.md#insn-00511458) · [`00511468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00511/0051140c.md#insn-00511468)

~~~diff
- 0051140c ["COPY", "register:0:8", ["register:4048:8"]]
- 0051140c ["INT_ADD", "register:40f0:8", ["const:51140c:8", "const:4:8"]]
- 0051140c ["CALLIND", null, ["register:0:8"]]
+ 0051144c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051144c ["INT_ADD", "register:40f0:8", ["const:51144c:8", "const:4:8"]]
+ 0051144c ["CALLIND", null, ["register:0:8"]]
- 0051140c bytes 20013fd6
+ 0051144c bytes 20013fd6
- 00511418 ["INT_ADD", "register:40f0:8", ["const:511418:8", "const:4:8"]]
- 00511418 ["CALL", null, ["callee:0054bf54:8"]]
+ 00511458 ["INT_ADD", "register:40f0:8", ["const:511458:8", "const:4:8"]]
+ 00511458 ["CALL", null, ["callee:0054bf54:8"]]
- 00511418 bytes bfea0094
+ 00511458 bytes bfea0094
- 00511428 ["INT_ADD", "register:40f0:8", ["const:511428:8", "const:4:8"]]
- 00511428 ["CALL", null, ["callee:00c57f80:8"]]
+ 00511468 ["INT_ADD", "register:40f0:8", ["const:511468:8", "const:4:8"]]
+ 00511468 ["CALL", null, ["callee:00c57f80:8"]]
- 00511428 bytes a21a1d94
+ 00511468 bytes c61a1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40ce4ae069413b942b7f1258910924d8"></a>

### [`005116b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00511/005116b0.md) → [`005116f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00511/005116f0.md) _ZN5Botan7X509_CA9make_certEPNS_9PK_SignerERNS_21RandomNumberGeneratorERKNS_19AlgorithmIdentifierERKNSt6__ndk16vectorIhNS8_9allocatorIhEEEER

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59d50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59d50.md) · 呼出先 16件 [`00535b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b80.md) [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`00c59e20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59e20.md) · 呼出先 16件 [`00535bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bc0.md) [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.40% / 新版 96.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005117c4",
      "incomplete_value": true,
      "site": "005117c4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00511784",
      "incomplete_value": true,
      "site": "00511784",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
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
      "definition_site": "0051198c",
      "incomplete_value": true,
      "site": "0051198c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051194c",
      "incomplete_value": true,
      "site": "0051194c",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 29,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005119f8",
      "incomplete_value": true,
      "site": "005119f8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005119b8",
      "incomplete_value": true,
      "site": "005119b8",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 33,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005117b4",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "0051197c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "005119e8",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005117b4",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "0051197c",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "005119e8",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00511784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00511/005116b0.md#insn-00511784) · [`0051190c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00511/005116b0.md#insn-0051190c) · [`0051194c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00511/005116b0.md#insn-0051194c)
- 新版 [`005117c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00511/005116f0.md#insn-005117c4) · [`0051194c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00511/005116f0.md#insn-0051194c) · [`0051198c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00511/005116f0.md#insn-0051198c)

~~~diff
- 00511784 ["COPY", "register:0:8", ["register:4048:8"]]
- 00511784 ["INT_ADD", "register:40f0:8", ["const:511784:8", "const:4:8"]]
- 00511784 ["CALLIND", null, ["register:0:8"]]
+ 005117c4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005117c4 ["INT_ADD", "register:40f0:8", ["const:5117c4:8", "const:4:8"]]
+ 005117c4 ["CALLIND", null, ["register:0:8"]]
- 00511784 bytes 20013fd6
+ 005117c4 bytes 20013fd6
- 0051190c ["INT_ADD", "register:40f0:8", ["const:51190c:8", "const:4:8"]]
- 0051190c ["CALL", null, ["callee:00c59e30:8"]]
+ 0051194c ["INT_ADD", "register:40f0:8", ["const:51194c:8", "const:4:8"]]
+ 0051194c ["CALL", null, ["callee:00c59e30:8"]]
- 0051190c bytes 15211d94
+ 0051194c bytes 39211d94
- 0051194c ["COPY", "register:0:8", ["register:4048:8"]]
- 0051194c ["INT_ADD", "register:40f0:8", ["const:51194c:8", "const:4:8"]]
- 0051194c ["CALLIND", null, ["register:0:8"]]
+ 0051198c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051198c ["INT_ADD", "register:40f0:8", ["const:51198c:8", "const:4:8"]]
+ 0051198c ["CALLIND", null, ["register:0:8"]]
- 0051194c bytes 20013fd6
+ 0051198c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0463544924b8739c70a31a3fd74e7d7"></a>

### [`005120dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/005120dc.md) → [`0051211c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/0051211c.md) _ZNK5Botan7X509_CA8make_crlERKNSt6__ndk16vectorINS_9CRL_EntryENS1_9allocatorIS3_EEEEjRNS_21RandomNumberGeneratorENS1_6chrono10time_pointINSB

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59d70.md) · 呼出先 21件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00517290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517290.md) [`00535b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b80.md) [`0053b424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053b424.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00c59e40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59e40.md) · 呼出先 21件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`005172d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/005172d0.md) [`00535bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bc0.md) [`0053b464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053b464.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.50% / 新版 94.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00512170",
      "incomplete_value": true,
      "site": "00512170",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00512130",
      "incomplete_value": true,
      "site": "00512130",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005121c0",
      "incomplete_value": true,
      "site": "005121cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00512180",
      "incomplete_value": true,
      "site": "0051218c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00512230",
      "incomplete_value": true,
      "site": "00512234",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005121f0",
      "incomplete_value": true,
      "site": "005121f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
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
      "00512158",
      "READ",
      [
        "storage",
        "00c9b110",
        null,
        "pointer"
      ]
    ],
    [
      "00512170",
      "DATA",
      [
        "storage",
        "00c688c0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005121b0",
      "READ",
      [
        "storage",
        "00c9b190",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00512158",
      "READ",
      [
        "storage",
        "00c9b1e0",
        null,
        "pointer"
      ]
    ],
    [
      "00512170",
      "DATA",
      [
        "storage",
        "00c68990",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005121b0",
      "READ",
      [
        "storage",
        "00c9b260",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00512170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/005120dc.md#insn-00512170) · [`005121b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/005120dc.md#insn-005121b4) · [`00512268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/005120dc.md#insn-00512268)
- 新版 [`005121b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/0051211c.md#insn-005121b0) · [`005121f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/0051211c.md#insn-005121f4) · [`005122a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/0051211c.md#insn-005122a8)

~~~diff
- 00512170 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:190:8"]]
- 00512170 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005121b0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:260:8"]]
+ 005121b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00512170 bytes 08c940f9
+ 005121b0 bytes 083141f9
- 005121b4 ["INT_ADD", "register:40f0:8", ["const:5121b4:8", "const:4:8"]]
- 005121b4 ["CALL", null, ["callee:00c580d0:8"]]
+ 005121f4 ["INT_ADD", "register:40f0:8", ["const:5121f4:8", "const:4:8"]]
+ 005121f4 ["CALL", null, ["callee:00c580d0:8"]]
- 005121b4 bytes 93171d94
+ 005121f4 bytes b7171d94
- 00512268 ["COPY", "register:0:8", ["register:4048:8"]]
- 00512268 ["INT_ADD", "register:40f0:8", ["const:512268:8", "const:4:8"]]
- 00512268 ["CALLIND", null, ["register:0:8"]]
+ 005122a8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005122a8 ["INT_ADD", "register:40f0:8", ["const:5122a8:8", "const:4:8"]]
+ 005122a8 ["CALLIND", null, ["register:0:8"]]
- 00512268 bytes 20013fd6
+ 005122a8 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-548b998c2305b2199759cb51cf700ac3"></a>

### [`00512910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/00512910.md) → [`00512950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/00512950.md) _ZN5Botan8X509_CRLC1ERNS_10DataSourceE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md) [`00c59c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59c80.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md) [`00c59d50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59d50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00512990",
      "incomplete_value": true,
      "site": "00512990",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00512950",
      "incomplete_value": true,
      "site": "00512950",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00512990",
      "incomplete_value": true,
      "site": "00512990",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00512950",
      "incomplete_value": true,
      "site": "00512950",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005129d0",
      "incomplete_value": true,
      "site": "005129d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00512990",
      "incomplete_value": true,
      "site": "00512998",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00512970",
      "READ",
      [
        "storage",
        "00c9b158",
        null,
        "pointer"
      ]
    ],
    [
      "00512978",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "00512990",
      "DATA",
      [
        "storage",
        "00c69a20",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "00512970",
      "READ",
      [
        "storage",
        "00c9b228",
        null,
        "pointer"
      ]
    ],
    [
      "00512978",
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ],
    [
      "00512990",
      "DATA",
      [
        "storage",
        "00c69af0",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00512930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/00512910.md#insn-00512930) · [`00512938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/00512910.md#insn-00512938) · [`0051295c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/00512910.md#insn-0051295c)
- 新版 [`00512970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/00512950.md#insn-00512970) · [`00512978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/00512950.md#insn-00512978) · [`0051299c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/00512950.md#insn-0051299c)

~~~diff
- 00512930 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:158:8"]]
- 00512930 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00512970 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:228:8"]]
+ 00512970 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00512930 bytes 08ad40f9
+ 00512970 bytes 081541f9
- 00512938 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:d38:8"]]
- 00512938 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 00512978 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:e08:8"]]
+ 00512978 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 00512938 bytes 4a9d46f9
+ 00512978 bytes 4a0547f9
- 0051295c ["INT_ADD", "register:40f0:8", ["const:51295c:8", "const:4:8"]]
- 0051295c ["CALL", null, ["callee:00c58760:8"]]
+ 0051299c ["INT_ADD", "register:40f0:8", ["const:51299c:8", "const:4:8"]]
+ 0051299c ["CALL", null, ["callee:00c58760:8"]]
- 0051295c bytes 4d171d94
+ 0051299c bytes 71171d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-736ab03af410ceeeee16e8c625370ea9"></a>

### [`00512a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/00512a64.md) → [`00512aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/00512aa4.md) _ZN5Botan8X509_CRLC1ERKNSt6__ndk16vectorIhNS1_9allocatorIhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59d90.md) · 呼出先 7件 [`005403c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005403c8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md)
- 新版 呼出元 1件 [`00c59e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59e60.md) · 呼出先 7件 [`00540408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540408.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.72% / 新版 84.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00512ae4",
      "incomplete_value": true,
      "site": "00512ae4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00512aa4",
      "incomplete_value": true,
      "site": "00512aa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00512ae4",
      "incomplete_value": true,
      "site": "00512ae4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00512aa4",
      "incomplete_value": true,
      "site": "00512aa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00512b2c",
      "incomplete_value": true,
      "site": "00512b38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00512aec",
      "incomplete_value": true,
      "site": "00512af8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00512ac4",
      "READ",
      [
        "storage",
        "00c9b158",
        null,
        "pointer"
      ]
    ],
    [
      "00512acc",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "00512ae4",
      "DATA",
      [
        "storage",
        "00c69a20",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "00512ac4",
      "READ",
      [
        "storage",
        "00c9b228",
        null,
        "pointer"
      ]
    ],
    [
      "00512acc",
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ],
    [
      "00512ae4",
      "DATA",
      [
        "storage",
        "00c69af0",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00512b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/00512a64.md#insn-00512b50) · [`00512a84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/00512a64.md#insn-00512a84) · [`00512a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/00512a64.md#insn-00512a8c)
- 新版 [`00512b90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/00512aa4.md#insn-00512b90) · [`00512ac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/00512aa4.md#insn-00512ac4) · [`00512acc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/00512aa4.md#insn-00512acc)

~~~diff
- 00512b50 ["COPY", "register:0:8", ["register:4048:8"]]
- 00512b50 ["INT_ADD", "register:40f0:8", ["const:512b50:8", "const:4:8"]]
- 00512b50 ["CALLIND", null, ["register:0:8"]]
+ 00512b90 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00512b90 ["INT_ADD", "register:40f0:8", ["const:512b90:8", "const:4:8"]]
+ 00512b90 ["CALLIND", null, ["register:0:8"]]
- 00512b50 bytes 20013fd6
+ 00512b90 bytes 20013fd6
- 00512a84 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:158:8"]]
- 00512a84 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00512ac4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:228:8"]]
+ 00512ac4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00512a84 bytes 08ad40f9
+ 00512ac4 bytes 081541f9
- 00512a8c ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:d38:8"]]
- 00512a8c ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 00512acc ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:e08:8"]]
+ 00512acc ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 00512a8c bytes 4a9d46f9
+ 00512acc bytes 4a0547f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1de51dd1d4f3b801fe30df4ce4b5aaf3"></a>

### [`00512bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/00512bdc.md) → [`00512c1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/00512c1c.md) _ZN5Botan8X509_CRLC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md) [`00c59660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59660.md) [`00c59670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59670.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md) [`00c59730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59730.md) [`00c59740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59740.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.19% / 新版 85.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00512c5c",
      "incomplete_value": true,
      "site": "00512c5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00512c1c",
      "incomplete_value": true,
      "site": "00512c1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00512c5c",
      "incomplete_value": true,
      "site": "00512c5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00512c1c",
      "incomplete_value": true,
      "site": "00512c1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00512c9c",
      "incomplete_value": true,
      "site": "00512ca4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00512c5c",
      "incomplete_value": true,
      "site": "00512c64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00512c3c",
      "READ",
      [
        "storage",
        "00c9b158",
        null,
        "pointer"
      ]
    ],
    [
      "00512c44",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "00512c5c",
      "DATA",
      [
        "storage",
        "00c69a20",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "00512c3c",
      "READ",
      [
        "storage",
        "00c9b228",
        null,
        "pointer"
      ]
    ],
    [
      "00512c44",
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ],
    [
      "00512c5c",
      "DATA",
      [
        "storage",
        "00c69af0",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00512bfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/00512bdc.md#insn-00512bfc) · [`00512c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/00512bdc.md#insn-00512c04) · [`00512c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/00512bdc.md#insn-00512c28)
- 新版 [`00512c3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/00512c1c.md#insn-00512c3c) · [`00512c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/00512c1c.md#insn-00512c44) · [`00512c68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/00512c1c.md#insn-00512c68)

~~~diff
- 00512bfc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:158:8"]]
- 00512bfc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00512c3c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:228:8"]]
+ 00512c3c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00512bfc bytes 08ad40f9
+ 00512c3c bytes 081541f9
- 00512c04 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:d38:8"]]
- 00512c04 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 00512c44 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:e08:8"]]
+ 00512c44 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 00512c04 bytes 4a9d46f9
+ 00512c44 bytes 4a0547f9
- 00512c28 ["INT_ADD", "register:40f0:8", ["const:512c28:8", "const:4:8"]]
- 00512c28 ["CALL", null, ["callee:00c58760:8"]]
+ 00512c68 ["INT_ADD", "register:40f0:8", ["const:512c68:8", "const:4:8"]]
+ 00512c68 ["CALL", null, ["callee:00c58760:8"]]
- 00512c28 bytes 9a161d94
+ 00512c68 bytes be161d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da7b7488077ce6fe1109f1a8c8beef7c"></a>

### [`00512d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/00512d08.md) → [`00512d48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/00512d48.md) _ZN5Botan8X509_CRLC1ERKNS_7X509_DNERKNS_9X509_TimeES6_RKNSt6__ndk16vectorINS_9CRL_EntryENS7_9allocatorIS9_EEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0053bd78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053bd78.md) [`00548e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548e68.md) [`0054ab64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054ab64.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0053bdb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053bdb8.md) [`00548ea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00548/00548ea8.md) [`0054aba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054a/0054aba4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.61% / 新版 85.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00512dbc",
      "incomplete_value": true,
      "site": "00512dbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00512d7c",
      "incomplete_value": true,
      "site": "00512d7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00512dbc",
      "incomplete_value": true,
      "site": "00512dbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00512d7c",
      "incomplete_value": true,
      "site": "00512d7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00512df8",
      "incomplete_value": true,
      "site": "00512e00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00512db8",
      "incomplete_value": true,
      "site": "00512dc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
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
      "00512da4",
      "READ",
      [
        "storage",
        "00c9b158",
        null,
        "pointer"
      ]
    ],
    [
      "00512da8",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "00512dbc",
      "DATA",
      [
        "storage",
        "00c69a20",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "00512da4",
      "READ",
      [
        "storage",
        "00c9b228",
        null,
        "pointer"
      ]
    ],
    [
      "00512da8",
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ],
    [
      "00512dbc",
      "DATA",
      [
        "storage",
        "00c69af0",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00512d64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/00512d08.md#insn-00512d64) · [`00512d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/00512d08.md#insn-00512d68) · [`00512d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/00512d08.md#insn-00512d84)
- 新版 [`00512da4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/00512d48.md#insn-00512da4) · [`00512da8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/00512d48.md#insn-00512da8) · [`00512dc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/00512d48.md#insn-00512dc4)

~~~diff
- 00512d64 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:158:8"]]
- 00512d64 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00512da4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:228:8"]]
+ 00512da4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00512d64 bytes 08ad40f9
+ 00512da4 bytes 081541f9
- 00512d68 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d38:8"]]
- 00512d68 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00512da8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e08:8"]]
+ 00512da8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00512d68 bytes 299d46f9
+ 00512da8 bytes 290547f9
- 00512d84 ["INT_ADD", "register:40f0:8", ["const:512d84:8", "const:4:8"]]
- 00512d84 ["CALL", null, ["callee:00c58760:8"]]
+ 00512dc4 ["INT_ADD", "register:40f0:8", ["const:512dc4:8", "const:4:8"]]
+ 00512dc4 ["CALL", null, ["callee:00c58760:8"]]
- 00512d84 bytes 43161d94
+ 00512dc4 bytes 67161d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-316fffe812e494754a619e14c83867f7"></a>

### [`005132b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00513/005132b0.md) → [`005132f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00513/005132f0.md) _ZN5Botan8X509_CRL12force_decodeEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 42件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004518b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004518b0.md) [`004594d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`004a577c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a577c.md)
- 新版 呼出元 0件  · 呼出先 42件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004518f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004518f0.md) [`00459510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459510.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`004a57bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a57bc.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 90.77% / 新版 90.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 6件, `store_destination` 1件, `store_value` 11件

アドレスに依存する影響 `call_argument_candidate` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00513350",
      "incomplete_value": true,
      "site": "00513350",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00513310",
      "incomplete_value": true,
      "site": "00513310",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00513370",
      "incomplete_value": true,
      "site": "00513370",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00513330",
      "incomplete_value": true,
      "site": "00513330",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00513378",
      "incomplete_value": true,
      "site": "00513378",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00513338",
      "incomplete_value": true,
      "site": "00513338",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00513334",
      "READ",
      [
        "storage",
        "00c9b0d0",
        null,
        "pointer"
      ]
    ],
    [
      "00513350",
      "DATA",
      [
        "storage",
        "00c679f8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0051335c",
      "READ",
      [
        "storage",
        "00c9adb0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00513334",
      "READ",
      [
        "storage",
        "00c9b1a0",
        null,
        "pointer"
      ]
    ],
    [
      "00513350",
      "DATA",
      [
        "storage",
        "00c67ac8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0051335c",
      "READ",
      [
        "storage",
        "00c9ae80",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051358c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00513/005132b0.md#insn-0051358c) · [`005135e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00513/005132b0.md#insn-005135e0) · [`0051361c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00513/005132b0.md#insn-0051361c)
- 新版 [`005135cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00513/005132f0.md#insn-005135cc) · [`00513620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00513/005132f0.md#insn-00513620) · [`0051365c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00513/005132f0.md#insn-0051365c)

~~~diff
- 0051358c ["COPY", "register:0:8", ["register:4048:8"]]
- 0051358c ["INT_ADD", "register:40f0:8", ["const:51358c:8", "const:4:8"]]
- 0051358c ["CALLIND", null, ["register:0:8"]]
+ 005135cc ["COPY", "register:0:8", ["register:4048:8"]]
+ 005135cc ["INT_ADD", "register:40f0:8", ["const:5135cc:8", "const:4:8"]]
+ 005135cc ["CALLIND", null, ["register:0:8"]]
- 0051358c bytes 20013fd6
+ 005135cc bytes 20013fd6
- 005135e0 ["COPY", "register:0:8", ["register:4048:8"]]
- 005135e0 ["INT_ADD", "register:40f0:8", ["const:5135e0:8", "const:4:8"]]
- 005135e0 ["CALLIND", null, ["register:0:8"]]
+ 00513620 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00513620 ["INT_ADD", "register:40f0:8", ["const:513620:8", "const:4:8"]]
+ 00513620 ["CALLIND", null, ["register:0:8"]]
- 005135e0 bytes 20013fd6
+ 00513620 bytes 20013fd6
- 0051361c ["COPY", "register:0:8", ["register:4040:8"]]
- 0051361c ["INT_ADD", "register:40f0:8", ["const:51361c:8", "const:4:8"]]
- 0051361c ["CALLIND", null, ["register:0:8"]]
+ 0051365c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0051365c ["INT_ADD", "register:40f0:8", ["const:51365c:8", "const:4:8"]]
+ 0051365c ["CALLIND", null, ["register:0:8"]]
- 0051361c bytes 00013fd6
+ 0051365c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f543cd377e69b2607ac51dacbf32fee3"></a>

### [`00513e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00513/00513e50.md) → [`00513e90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00513/00513e90.md) _ZNK5Botan8X509_CRL4dataEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59a50.md) · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)
- 新版 呼出元 1件 [`00c59b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b20.md) · 呼出先 6件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004aeca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.45% / 新版 95.45%

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
      "definition_site": "00513ef0",
      "incomplete_value": false,
      "site": "00513ef8",
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
            "const:dbf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00513eb0",
      "incomplete_value": false,
      "site": "00513eb8",
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
            "const:e13:8"
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
      "definition_site": "00513f2c",
      "incomplete_value": true,
      "site": "00513f38",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00513eec",
      "incomplete_value": true,
      "site": "00513ef8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00513f28",
      "incomplete_value": false,
      "site": "00513f38",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "00513ee8",
      "incomplete_value": false,
      "site": "00513ef8",
      "value": [
        "leaf",
        "const:535868:8"
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
      "00513ef0",
      "PARAM",
      [
        "storage",
        "002bee13",
        null,
        "string"
      ]
    ],
    [
      "00513f28",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "00513f2c",
      "READ",
      [
        "storage",
        "00c9ad48",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00513ef0",
      "PARAM",
      [
        "storage",
        "002bedbf",
        null,
        "string"
      ]
    ],
    [
      "00513f28",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "00513f2c",
      "READ",
      [
        "storage",
        "00c9ae18",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00513eb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00513/00513e50.md#insn-00513eb8) · [`00513ef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00513/00513e50.md#insn-00513ef8) · [`00513ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00513/00513e50.md#insn-00513ea4)
- 新版 [`00513ef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00513/00513e90.md#insn-00513ef8) · [`00513f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00513/00513e90.md#insn-00513f38) · [`00513ee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00513/00513e90.md#insn-00513ee4)

~~~diff
- 00513eb8 ["INT_ADD", "register:40f0:8", ["const:513eb8:8", "const:4:8"]]
- 00513eb8 ["CALL", null, ["callee:0043de18:8"]]
+ 00513ef8 ["INT_ADD", "register:40f0:8", ["const:513ef8:8", "const:4:8"]]
+ 00513ef8 ["CALL", null, ["callee:0043de18:8"]]
- 00513eb8 bytes c8a7fc97
+ 00513ef8 bytes c8a7fc97
- 00513ef8 ["INT_ADD", "register:40f0:8", ["const:513ef8:8", "const:4:8"]]
- 00513ef8 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00513f38 ["INT_ADD", "register:40f0:8", ["const:513f38:8", "const:4:8"]]
+ 00513f38 ["CALL", null, ["callee:00c57fe0:8"]]
- 00513ef8 bytes 06101d94
+ 00513f38 bytes 2a101d94
- 00513ea4 ["INT_ADD", "register:40f0:8", ["const:513ea4:8", "const:4:8"]]
- 00513ea4 ["CALL", null, ["callee:00c57fc0:8"]]
+ 00513ee4 ["INT_ADD", "register:40f0:8", ["const:513ee4:8", "const:4:8"]]
+ 00513ee4 ["CALL", null, ["callee:00c57fc0:8"]]
- 00513ea4 bytes 13101d94
+ 00513ee4 bytes 37101d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb2e9e06cd9cd419d710e1af95a2611b"></a>

### [`00513fcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00513/00513fcc.md) → [`0051400c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/0051400c.md) _ZN5Botan7X509_DNC2ERKNSt6__ndk18multimapINS_3OIDENS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS1_4lessIS3_EENS7_INS1_4pair

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59b00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59b00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59bd0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00514054",
      "incomplete_value": true,
      "site": "0051405c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00514014",
      "incomplete_value": true,
      "site": "0051401c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00514048",
      "READ",
      [
        "storage",
        "00c9b0d0",
        null,
        "pointer"
      ]
    ],
    [
      "0051405c",
      "DATA",
      [
        "storage",
        "00c679f8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00514048",
      "READ",
      [
        "storage",
        "00c9b1a0",
        null,
        "pointer"
      ]
    ],
    [
      "0051405c",
      "DATA",
      [
        "storage",
        "00c67ac8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00514008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00513/00513fcc.md#insn-00514008) · [`00514044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00513/00513fcc.md#insn-00514044)
- 新版 [`00514048`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/0051400c.md#insn-00514048) · [`00514084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/0051400c.md#insn-00514084)

~~~diff
- 00514008 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d0:8"]]
- 00514008 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00514048 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1a0:8"]]
+ 00514048 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00514008 bytes 086940f9
+ 00514048 bytes 08d140f9
- 00514044 ["INT_ADD", "register:40f0:8", ["const:514044:8", "const:4:8"]]
- 00514044 ["CALL", null, ["callee:00c59bd0:8"]]
+ 00514084 ["INT_ADD", "register:40f0:8", ["const:514084:8", "const:4:8"]]
+ 00514084 ["CALL", null, ["callee:00c59bd0:8"]]
- 00514044 bytes af161d94
+ 00514084 bytes d3161d94
~~~


<a id="compare-aba9e49aef832ddf23fcd8cb0db30b5c"></a>

### [`0051426c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00514/0051426c.md) → [`005142ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/005142ac.md) _ZN5Botan7X509_DNC1ERKNSt6__ndk18multimapINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES8_NS1_4lessIS8_EENS6_INS1_4pairIKS8_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58680.md) [`00c59b00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59b00.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58750.md) [`00c59bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59bd0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.52% / 新版 95.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00514308",
      "incomplete_value": true,
      "site": "00514310",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "005142c8",
      "incomplete_value": true,
      "site": "005142d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005142fc",
      "READ",
      [
        "storage",
        "00c9b0d0",
        null,
        "pointer"
      ]
    ],
    [
      "00514310",
      "DATA",
      [
        "storage",
        "00c679f8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "005142fc",
      "READ",
      [
        "storage",
        "00c9b1a0",
        null,
        "pointer"
      ]
    ],
    [
      "00514310",
      "DATA",
      [
        "storage",
        "00c67ac8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005142bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00514/0051426c.md#insn-005142bc) · [`005142f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00514/0051426c.md#insn-005142f4) · [`00514304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00514/0051426c.md#insn-00514304)
- 新版 [`005142fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/005142ac.md#insn-005142fc) · [`00514334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/005142ac.md#insn-00514334) · [`00514344`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/005142ac.md#insn-00514344)

~~~diff
- 005142bc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d0:8"]]
- 005142bc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005142fc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1a0:8"]]
+ 005142fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005142bc bytes 086940f9
+ 005142fc bytes 08d140f9
- 005142f4 ["INT_ADD", "register:40f0:8", ["const:5142f4:8", "const:4:8"]]
- 005142f4 ["CALL", null, ["callee:00c58750:8"]]
+ 00514334 ["INT_ADD", "register:40f0:8", ["const:514334:8", "const:4:8"]]
+ 00514334 ["CALL", null, ["callee:00c58750:8"]]
- 005142f4 bytes e3101d94
+ 00514334 bytes 07111d94
- 00514304 ["INT_ADD", "register:40f0:8", ["const:514304:8", "const:4:8"]]
- 00514304 ["CALL", null, ["callee:00c59bd0:8"]]
+ 00514344 ["INT_ADD", "register:40f0:8", ["const:514344:8", "const:4:8"]]
+ 00514344 ["CALL", null, ["callee:00c59bd0:8"]]
- 00514304 bytes ff151d94
+ 00514344 bytes 23161d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97fca5254619e19a0a00066795464295"></a>

### [`0051460c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00514/0051460c.md) → [`0051464c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/0051464c.md) _ZN5Botan7X509_DN16deref_info_fieldERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59b70.md) · 呼出先 3件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00441e94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441e94.md)
- 新版 呼出元 1件 [`00c59c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59c40.md) · 呼出先 3件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00441ed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441ed4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.41% / 新版 86.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005147d0",
      "incomplete_value": true,
      "site": "005147d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2d6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00514790",
      "incomplete_value": true,
      "site": "00514790",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:32a:8"
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
      "definition_site": "0051482c",
      "incomplete_value": true,
      "site": "0051482c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:522:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005147ec",
      "incomplete_value": true,
      "site": "005147ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:57e:8"
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
      "definition_site": "00514820",
      "incomplete_value": true,
      "site": "00514830",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005147e0",
      "incomplete_value": true,
      "site": "005147f0",
      "value": [
        "LOAD",
        "8",
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
      "005147a0",
      "PARAM",
      [
        "storage",
        "002b617c",
        null,
        null
      ]
    ],
    [
      "005147bc",
      "READ",
      [
        "storage",
        "002bb32a",
        null,
        "string"
      ]
    ],
    [
      "005147e0",
      "PARAM",
      [
        "storage",
        "002c1193",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005147a0",
      "PARAM",
      [
        "storage",
        "002b61bc",
        null,
        null
      ]
    ],
    [
      "005147bc",
      "READ",
      [
        "storage",
        "002bb2d6",
        null,
        "string"
      ]
    ],
    [
      "005147e0",
      "PARAM",
      [
        "storage",
        "002c11d3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00514768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00514/0051460c.md#insn-00514768) · [`005147a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00514/0051460c.md#insn-005147a8) · [`005147bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00514/0051460c.md#insn-005147bc)
- 新版 [`005147a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/0051464c.md#insn-005147a8) · [`005147e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/0051464c.md#insn-005147e8) · [`005147fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/0051464c.md#insn-005147fc)

~~~diff
- 00514768 ["INT_ADD", "register:40f0:8", ["const:514768:8", "const:4:8"]]
- 00514768 ["CALL", null, ["callee:00441ed4:8"]]
+ 005147a8 ["INT_ADD", "register:40f0:8", ["const:5147a8:8", "const:4:8"]]
+ 005147a8 ["CALL", null, ["callee:00441ed4:8"]]
- 00514768 bytes cbb5fc97
+ 005147a8 bytes cbb5fc97
- 005147a8 ["INT_ADD", "register:40f0:8", ["const:5147a8:8", "const:4:8"]]
- 005147a8 ["CALL", null, ["callee:00441ed4:8"]]
+ 005147e8 ["INT_ADD", "register:40f0:8", ["const:5147e8:8", "const:4:8"]]
+ 005147e8 ["CALL", null, ["callee:00441ed4:8"]]
- 005147a8 bytes bbb5fc97
+ 005147e8 bytes bbb5fc97
- 005147bc ["INT_ADD", "register:40f0:8", ["const:5147bc:8", "const:4:8"]]
- 005147bc ["CALL", null, ["callee:00441ed4:8"]]
+ 005147fc ["INT_ADD", "register:40f0:8", ["const:5147fc:8", "const:4:8"]]
+ 005147fc ["CALL", null, ["callee:00441ed4:8"]]
- 005147bc bytes b6b5fc97
+ 005147fc bytes b6b5fc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48823845c4bbc80a2bdd99e85c3ada13"></a>

### [`00514da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00514/00514da4.md) → [`00514de4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/00514de4.md) _ZNK5Botan7X509_DN11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`004ffaac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ffaac.md) [`0052e334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052e/0052e334.md) · 呼出先 11件 [`00515100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/00515100.md) [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00549668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549668.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`004ffaec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ffaec.md) [`0052e374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052e/0052e374.md) · 呼出先 11件 [`00515140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/00515140.md) [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`005496a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00549/005496a8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 84.38% / 新版 84.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00514e74",
      "incomplete_value": true,
      "site": "00514e74",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2d6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00514e34",
      "incomplete_value": true,
      "site": "00514e34",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:32a:8"
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
      "definition_site": "00514ebc",
      "incomplete_value": true,
      "site": "00514ebc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:532:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00514e7c",
      "incomplete_value": true,
      "site": "00514e7c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:58e:8"
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
      "definition_site": "00514f04",
      "incomplete_value": true,
      "site": "00514f04",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b5000:8"
              ],
              [
                "leaf",
                "const:fa6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00514ec4",
      "incomplete_value": true,
      "site": "00514ec4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b5000:8"
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
      "00514e60",
      "READ",
      [
        "storage",
        "002bb32a",
        null,
        "string"
      ]
    ],
    [
      "00514eac",
      "READ",
      [
        "storage",
        "002a658e",
        null,
        "string"
      ]
    ],
    [
      "00514ef4",
      "READ",
      [
        "storage",
        "002b5f66",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00514e60",
      "READ",
      [
        "storage",
        "002bb2d6",
        null,
        "string"
      ]
    ],
    [
      "00514eac",
      "READ",
      [
        "storage",
        "002a6532",
        null,
        "string"
      ]
    ],
    [
      "00514ef4",
      "READ",
      [
        "storage",
        "002b5fa6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00514f20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00514/00514da4.md#insn-00514f20) · [`00514dd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00514/00514da4.md#insn-00514dd4) · [`00514de4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00514/00514da4.md#insn-00514de4)
- 新版 [`00514f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/00514de4.md#insn-00514f60) · [`00514e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/00514de4.md#insn-00514e14) · [`00514e24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/00514de4.md#insn-00514e24)

~~~diff
- 00514f20 ["INT_ADD", "register:40f0:8", ["const:514f20:8", "const:4:8"]]
- 00514f20 ["CALL", null, ["callee:00515140:8"]]
+ 00514f60 ["INT_ADD", "register:40f0:8", ["const:514f60:8", "const:4:8"]]
+ 00514f60 ["CALL", null, ["callee:00515140:8"]]
- 00514f20 bytes 78000094
+ 00514f60 bytes 78000094
- 00514dd4 ["INT_ADD", "register:40f0:8", ["const:514dd4:8", "const:4:8"]]
- 00514dd4 ["CALL", null, ["callee:00c59af0:8"]]
+ 00514e14 ["INT_ADD", "register:40f0:8", ["const:514e14:8", "const:4:8"]]
+ 00514e14 ["CALL", null, ["callee:00c59af0:8"]]
- 00514dd4 bytes 13131d94
+ 00514e14 bytes 37131d94
- 00514de4 ["INT_ADD", "register:40f0:8", ["const:514de4:8", "const:4:8"]]
- 00514de4 ["CALL", null, ["callee:00c58780:8"]]
+ 00514e24 ["INT_ADD", "register:40f0:8", ["const:514e24:8", "const:4:8"]]
+ 00514e24 ["CALL", null, ["callee:00c58780:8"]]
- 00514de4 bytes 330e1d94
+ 00514e24 bytes 570e1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11bef9ee1bf8088fb11e4d7f341da277"></a>

### [`005156c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/005156c4.md) → [`00515704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/00515704.md) _ZN5Botan10Extensions15create_extn_objERKNS_3OIDEbRKNSt6__ndk16vectorIhNS4_9allocatorIhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c59de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59de0.md) · 呼出先 27件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`00503bf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/00503bf4.md) [`00516660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516660.md) [`00516708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516708.md) [`005167b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/005167b0.md)
- 新版 呼出元 1件 [`00c59eb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59eb0.md) · 呼出先 27件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`00503c34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503c34.md) [`005166a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/005166a0.md) [`00516748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516748.md) [`005167f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/005167f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00515768",
      "incomplete_value": true,
      "site": "00515768",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d3c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00515728",
      "incomplete_value": true,
      "site": "00515728",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d0b:8"
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
      "definition_site": "00515838",
      "incomplete_value": true,
      "site": "00515838",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:781:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005157f8",
      "incomplete_value": true,
      "site": "005157f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7dd:8"
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
      "definition_site": "00515958",
      "incomplete_value": true,
      "site": "00515958",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2cc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00515918",
      "incomplete_value": true,
      "site": "00515918",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:320:8"
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
      "00515758",
      "READ",
      [
        "storage",
        "002b4d0b",
        null,
        "string"
      ]
    ],
    [
      "00515800",
      "READ",
      [
        "storage",
        "00c9b1b0",
        null,
        "pointer"
      ]
    ],
    [
      "0051580c",
      "DATA",
      [
        "storage",
        "00c67a28",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "00515758",
      "READ",
      [
        "storage",
        "002b4d3c",
        null,
        "string"
      ]
    ],
    [
      "00515800",
      "READ",
      [
        "storage",
        "00c9b280",
        null,
        "pointer"
      ]
    ],
    [
      "0051580c",
      "DATA",
      [
        "storage",
        "00c67af8",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00515708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/005156c4.md#insn-00515708) · [`00515710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/005156c4.md#insn-00515710) · [`00515738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/005156c4.md#insn-00515738)
- 新版 [`00515748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/00515704.md#insn-00515748) · [`00515750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/00515704.md#insn-00515750) · [`00515778`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/00515704.md#insn-00515778)

~~~diff
- 00515708 ["INT_ADD", "register:40f0:8", ["const:515708:8", "const:4:8"]]
- 00515708 ["CALL", null, ["callee:00c588d0:8"]]
+ 00515748 ["INT_ADD", "register:40f0:8", ["const:515748:8", "const:4:8"]]
+ 00515748 ["CALL", null, ["callee:00c588d0:8"]]
- 00515708 bytes 3e0c1d94
+ 00515748 bytes 620c1d94
- 00515710 ["COPY", "tmp:0:8", ["const:d0b:8"]]
- 00515710 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00515710 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00515710 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00515750 ["COPY", "tmp:0:8", ["const:d3c:8"]]
+ 00515750 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00515750 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00515750 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00515710 bytes 292d3491
+ 00515750 bytes 29f13491
- 00515738 ["INT_ADD", "register:40f0:8", ["const:515738:8", "const:4:8"]]
- 00515738 ["CALL", null, ["callee:00c58760:8"]]
+ 00515778 ["INT_ADD", "register:40f0:8", ["const:515778:8", "const:4:8"]]
+ 00515778 ["CALL", null, ["callee:00c58760:8"]]
- 00515738 bytes d60b1d94
+ 00515778 bytes fa0b1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6a5f8ed686bfa42a6a4c5826b7319df"></a>

### [`00516660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516660.md) → [`005166a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/005166a0.md) FUN_005166a0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005156c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/005156c4.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md)
- 新版 呼出元 1件 [`00515704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/00515704.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md)

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
      "definition_site": "005166d8",
      "incomplete_value": true,
      "site": "005166d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00516698",
      "incomplete_value": true,
      "site": "00516698",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:103:8"
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
      "005166c8",
      "READ",
      [
        "storage",
        "002a4103",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005166c8",
      "READ",
      [
        "storage",
        "002a40b6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051667c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516660.md#insn-0051667c) · [`005166a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516660.md#insn-005166a4) · [`005166b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516660.md#insn-005166b4)
- 新版 [`005166bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/005166a0.md#insn-005166bc) · [`005166e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/005166a0.md#insn-005166e4) · [`005166f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/005166a0.md#insn-005166f4)

~~~diff
- 0051667c ["COPY", "tmp:0:8", ["const:103:8"]]
- 0051667c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0051667c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0051667c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005166bc ["COPY", "tmp:0:8", ["const:b6:8"]]
+ 005166bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005166bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005166bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0051667c bytes 290d0491
+ 005166bc bytes 29d90291
- 005166a4 ["INT_ADD", "register:40f0:8", ["const:5166a4:8", "const:4:8"]]
- 005166a4 ["CALL", null, ["callee:00c58760:8"]]
+ 005166e4 ["INT_ADD", "register:40f0:8", ["const:5166e4:8", "const:4:8"]]
+ 005166e4 ["CALL", null, ["callee:00c58760:8"]]
- 005166a4 bytes fb071d94
+ 005166e4 bytes 1f081d94
- 005166b4 ["INT_ADD", "register:40f0:8", ["const:5166b4:8", "const:4:8"]]
- 005166b4 ["CALL", null, ["callee:00c57f80:8"]]
+ 005166f4 ["INT_ADD", "register:40f0:8", ["const:5166f4:8", "const:4:8"]]
+ 005166f4 ["CALL", null, ["callee:00c57f80:8"]]
- 005166b4 bytes ff051d94
+ 005166f4 bytes 23061d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-417f5089be98bd5a8a8f13c6adbef1d7"></a>

### [`00516708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516708.md) → [`00516748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516748.md) FUN_00516748

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005156c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/005156c4.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md)
- 新版 呼出元 1件 [`00515704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/00515704.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md)

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
      "definition_site": "00516780",
      "incomplete_value": true,
      "site": "00516780",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00516740",
      "incomplete_value": true,
      "site": "00516740",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f6d:8"
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
      "00516770",
      "READ",
      [
        "storage",
        "0029ef6d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00516770",
      "READ",
      [
        "storage",
        "0029ef20",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00516724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516708.md#insn-00516724) · [`0051674c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516708.md#insn-0051674c) · [`0051675c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516708.md#insn-0051675c)
- 新版 [`00516764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516748.md#insn-00516764) · [`0051678c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516748.md#insn-0051678c) · [`0051679c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516748.md#insn-0051679c)

~~~diff
- 00516724 ["COPY", "tmp:0:8", ["const:f6d:8"]]
- 00516724 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00516724 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00516724 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00516764 ["COPY", "tmp:0:8", ["const:f20:8"]]
+ 00516764 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00516764 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00516764 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00516724 bytes 29b53d91
+ 00516764 bytes 29813c91
- 0051674c ["INT_ADD", "register:40f0:8", ["const:51674c:8", "const:4:8"]]
- 0051674c ["CALL", null, ["callee:00c58760:8"]]
+ 0051678c ["INT_ADD", "register:40f0:8", ["const:51678c:8", "const:4:8"]]
+ 0051678c ["CALL", null, ["callee:00c58760:8"]]
- 0051674c bytes d1071d94
+ 0051678c bytes f5071d94
- 0051675c ["INT_ADD", "register:40f0:8", ["const:51675c:8", "const:4:8"]]
- 0051675c ["CALL", null, ["callee:00c57f80:8"]]
+ 0051679c ["INT_ADD", "register:40f0:8", ["const:51679c:8", "const:4:8"]]
+ 0051679c ["CALL", null, ["callee:00c57f80:8"]]
- 0051675c bytes d5051d94
+ 0051679c bytes f9051d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c86d35b39c8cac9d0b644d064626a77"></a>

### [`005167b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/005167b0.md) → [`005167f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/005167f0.md) FUN_005167f0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005156c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/005156c4.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md)
- 新版 呼出元 1件 [`00515704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/00515704.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md)

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
      "definition_site": "00516828",
      "incomplete_value": true,
      "site": "00516828",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:72d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005167e8",
      "incomplete_value": true,
      "site": "005167e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:789:8"
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
      "00516818",
      "READ",
      [
        "storage",
        "002a7789",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00516818",
      "READ",
      [
        "storage",
        "002a772d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005167cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/005167b0.md#insn-005167cc) · [`005167f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/005167b0.md#insn-005167f4) · [`00516804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/005167b0.md#insn-00516804)
- 新版 [`0051680c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/005167f0.md#insn-0051680c) · [`00516834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/005167f0.md#insn-00516834) · [`00516844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/005167f0.md#insn-00516844)

~~~diff
- 005167cc ["COPY", "tmp:0:8", ["const:789:8"]]
- 005167cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005167cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005167cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0051680c ["COPY", "tmp:0:8", ["const:72d:8"]]
+ 0051680c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0051680c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0051680c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005167cc bytes 29251e91
+ 0051680c bytes 29b51c91
- 005167f4 ["INT_ADD", "register:40f0:8", ["const:5167f4:8", "const:4:8"]]
- 005167f4 ["CALL", null, ["callee:00c58760:8"]]
+ 00516834 ["INT_ADD", "register:40f0:8", ["const:516834:8", "const:4:8"]]
+ 00516834 ["CALL", null, ["callee:00c58760:8"]]
- 005167f4 bytes a7071d94
+ 00516834 bytes cb071d94
- 00516804 ["INT_ADD", "register:40f0:8", ["const:516804:8", "const:4:8"]]
- 00516804 ["CALL", null, ["callee:00c57f80:8"]]
+ 00516844 ["INT_ADD", "register:40f0:8", ["const:516844:8", "const:4:8"]]
+ 00516844 ["CALL", null, ["callee:00c57f80:8"]]
- 00516804 bytes ab051d94
+ 00516844 bytes cf051d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd8e3c067c272dab0b8a2aa77a28f57b"></a>

### [`00516858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516858.md) → [`00516898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516898.md) FUN_00516898

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005156c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/005156c4.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md)
- 新版 呼出元 1件 [`00515704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/00515704.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md)

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
      "definition_site": "005168d0",
      "incomplete_value": true,
      "site": "005168d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:489:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00516890",
      "incomplete_value": true,
      "site": "00516890",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4dd:8"
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
      "005168c0",
      "READ",
      [
        "storage",
        "002bc4dd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005168c0",
      "READ",
      [
        "storage",
        "002bc489",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00516874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516858.md#insn-00516874) · [`0051689c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516858.md#insn-0051689c) · [`005168ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516858.md#insn-005168ac)
- 新版 [`005168b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516898.md#insn-005168b4) · [`005168dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516898.md#insn-005168dc) · [`005168ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516898.md#insn-005168ec)

~~~diff
- 00516874 ["COPY", "tmp:0:8", ["const:4dd:8"]]
- 00516874 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00516874 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00516874 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005168b4 ["COPY", "tmp:0:8", ["const:489:8"]]
+ 005168b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005168b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005168b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00516874 bytes 29751391
+ 005168b4 bytes 29251291
- 0051689c ["INT_ADD", "register:40f0:8", ["const:51689c:8", "const:4:8"]]
- 0051689c ["CALL", null, ["callee:00c58760:8"]]
+ 005168dc ["INT_ADD", "register:40f0:8", ["const:5168dc:8", "const:4:8"]]
+ 005168dc ["CALL", null, ["callee:00c58760:8"]]
- 0051689c bytes 7d071d94
+ 005168dc bytes a1071d94
- 005168ac ["INT_ADD", "register:40f0:8", ["const:5168ac:8", "const:4:8"]]
- 005168ac ["CALL", null, ["callee:00c57f80:8"]]
+ 005168ec ["INT_ADD", "register:40f0:8", ["const:5168ec:8", "const:4:8"]]
+ 005168ec ["CALL", null, ["callee:00c57f80:8"]]
- 005168ac bytes 81051d94
+ 005168ec bytes a5051d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

