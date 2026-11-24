# v16.0.1 → v16.0.2 · 最優先の変更候補 (8)

[一覧の目次](README.md)

<a id="compare-32eeef43ef12d8cd7abbf27696c21ddd"></a>

### [`004b8250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8250.md) → [`004b8290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8290.md) _ZN5BotanlsERNSt6__ndk113basic_ostreamIcNS0_11char_traitsIcEEEERKNS_6BigIntE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 14件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.67% / 新版 93.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 2件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b8328",
      "incomplete_value": true,
      "site": "004b8328",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004b82e8",
      "incomplete_value": true,
      "site": "004b82e8",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b8378",
      "incomplete_value": true,
      "site": "004b8378",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004b8338",
      "incomplete_value": true,
      "site": "004b8338",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b838c",
      "incomplete_value": false,
      "site": "004b8398",
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
            "const:f0b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b834c",
      "incomplete_value": false,
      "site": "004b8358",
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
            "const:f5f:8"
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
      "004b8318",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004b8368",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004b838c",
      "PARAM",
      [
        "storage",
        "002b8f5f",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004b8318",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "004b8368",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "004b838c",
      "PARAM",
      [
        "storage",
        "002b8f0b",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b82e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8250.md#insn-004b82e8) · [`004b8328`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8250.md#insn-004b8328) · [`004b8338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8250.md#insn-004b8338)
- 新版 [`004b8328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8290.md#insn-004b8328) · [`004b8368`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8290.md#insn-004b8368) · [`004b8378`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8290.md#insn-004b8378)

~~~diff
- 004b82e8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b82e8 ["INT_ADD", "register:40f0:8", ["const:4b82e8:8", "const:4:8"]]
- 004b82e8 ["CALLIND", null, ["register:0:8"]]
+ 004b8328 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b8328 ["INT_ADD", "register:40f0:8", ["const:4b8328:8", "const:4:8"]]
+ 004b8328 ["CALLIND", null, ["register:0:8"]]
- 004b82e8 bytes 20013fd6
+ 004b8328 bytes 20013fd6
- 004b8328 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:738:8"]]
- 004b8328 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004b8368 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:808:8"]]
+ 004b8368 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004b8328 bytes 299f43f9
+ 004b8368 bytes 290744f9
- 004b8338 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b8338 ["INT_ADD", "register:40f0:8", ["const:4b8338:8", "const:4:8"]]
- 004b8338 ["CALLIND", null, ["register:0:8"]]
+ 004b8378 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b8378 ["INT_ADD", "register:40f0:8", ["const:4b8378:8", "const:4:8"]]
+ 004b8378 ["CALLIND", null, ["register:0:8"]]
- 004b8338 bytes 20013fd6
+ 004b8378 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f839374d6d16d4739d6a0428dd86f430"></a>

### [`004b8540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8540.md) → [`004b8580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8580.md) _ZN5BotanrsERNSt6__ndk113basic_istreamIcNS0_11char_traitsIcEEEERNS_6BigIntE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00543528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543528.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00543568`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543568.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.25% / 新版 97.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b85d0",
      "incomplete_value": true,
      "site": "004b85d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b8590",
      "incomplete_value": true,
      "site": "004b8594",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c30:8"
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
      "definition_site": "004b8690",
      "incomplete_value": true,
      "site": "004b8690",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004b8650",
      "incomplete_value": true,
      "site": "004b8650",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b86e8",
      "incomplete_value": false,
      "site": "004b86f0",
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
            "const:54b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b86a8",
      "incomplete_value": false,
      "site": "004b86b0",
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
            "const:5a7:8"
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
      "004b85d0",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      "004b85d0",
      "PARAM",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "004b8680",
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
      "004b85d0",
      "READ",
      [
        "storage",
        "00c9ad00",
        null,
        "pointer"
      ]
    ],
    [
      "004b85d0",
      "PARAM",
      [
        "storage",
        "01127f18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "004b8680",
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

- 旧版 [`004b8594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8540.md#insn-004b8594) · [`004b8650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8540.md#insn-004b8650) · [`004b86b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8540.md#insn-004b86b0)
- 新版 [`004b85d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8580.md#insn-004b85d4) · [`004b8690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8580.md#insn-004b8690) · [`004b86f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8580.md#insn-004b86f0)

~~~diff
- 004b8594 ["INT_ADD", "register:40f0:8", ["const:4b8594:8", "const:4:8"]]
- 004b8594 ["CALL", null, ["callee:00c58350:8"]]
+ 004b85d4 ["INT_ADD", "register:40f0:8", ["const:4b85d4:8", "const:4:8"]]
+ 004b85d4 ["CALL", null, ["callee:00c58350:8"]]
- 004b8594 bytes 3b7f1e94
+ 004b85d4 bytes 5f7f1e94
- 004b8650 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b8650 ["INT_ADD", "register:40f0:8", ["const:4b8650:8", "const:4:8"]]
- 004b8650 ["CALLIND", null, ["register:0:8"]]
+ 004b8690 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b8690 ["INT_ADD", "register:40f0:8", ["const:4b8690:8", "const:4:8"]]
+ 004b8690 ["CALLIND", null, ["register:0:8"]]
- 004b8650 bytes 20013fd6
+ 004b8690 bytes 20013fd6
- 004b86b0 ["INT_ADD", "register:40f0:8", ["const:4b86b0:8", "const:4:8"]]
- 004b86b0 ["CALL", null, ["callee:0043de18:8"]]
+ 004b86f0 ["INT_ADD", "register:40f0:8", ["const:4b86f0:8", "const:4:8"]]
+ 004b86f0 ["CALL", null, ["callee:0043de18:8"]]
- 004b86b0 bytes ca15fe97
+ 004b86f0 bytes ca15fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b42fb3b66eee128458055ba75f5decf"></a>

### [`004b8850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8850.md) → [`004b8890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8890.md) FUN_004b8890

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 8件 [`004a1354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1354.md) [`004b7c10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b7c10.md) [`004b7fc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b7fc8.md) [`004ba1f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ba/004ba1f4.md) [`004db564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004db/004db564.md) · 呼出先 7件 [`00536334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536334.md) [`00c37ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ba4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 8件 [`004a1394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a1/004a1394.md) [`004b7c50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b7/004b7c50.md) [`004b8008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8008.md) [`004ba234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ba/004ba234.md) [`004db5a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004db/004db5a4.md) · 呼出先 7件 [`00536374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536374.md) [`00c37c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c40.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b8958",
      "incomplete_value": true,
      "site": "004b8960",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eb8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b8918",
      "incomplete_value": true,
      "site": "004b8920",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b895c",
      "incomplete_value": true,
      "site": "004b8960",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b891c",
      "incomplete_value": true,
      "site": "004b8920",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004b8958",
      "READ",
      [
        "storage",
        "00c9ade8",
        null,
        "pointer"
      ]
    ],
    [
      "004b8958",
      "PARAM",
      [
        "storage",
        "00c96698",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "004b895c",
      "READ",
      [
        "storage",
        "00c9adf0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004b8958",
      "READ",
      [
        "storage",
        "00c9aeb8",
        null,
        "pointer"
      ]
    ],
    [
      "004b8958",
      "PARAM",
      [
        "storage",
        "00c96768",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "004b895c",
      "READ",
      [
        "storage",
        "00c9aec0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b8920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8850.md#insn-004b8920) · [`004b889c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8850.md#insn-004b889c) · [`004b88e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8850.md#insn-004b88e8)
- 新版 [`004b8960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8890.md#insn-004b8960) · [`004b88dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8890.md#insn-004b88dc) · [`004b8928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8890.md#insn-004b8928)

~~~diff
- 004b8920 ["INT_ADD", "register:40f0:8", ["const:4b8920:8", "const:4:8"]]
- 004b8920 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004b8960 ["INT_ADD", "register:40f0:8", ["const:4b8960:8", "const:4:8"]]
+ 004b8960 ["CALL", null, ["callee:00c57fe0:8"]]
- 004b8920 bytes 7c7d1e94
+ 004b8960 bytes a07d1e94
- 004b889c ["INT_ADD", "register:40f0:8", ["const:4b889c:8", "const:4:8"]]
- 004b889c ["CALL", null, ["callee:00c58b00:8"]]
+ 004b88dc ["INT_ADD", "register:40f0:8", ["const:4b88dc:8", "const:4:8"]]
+ 004b88dc ["CALL", null, ["callee:00c58b00:8"]]
- 004b889c bytes 65801e94
+ 004b88dc bytes 89801e94
- 004b88e8 ["INT_ADD", "register:40f0:8", ["const:4b88e8:8", "const:4:8"]]
- 004b88e8 ["CALL", null, ["callee:00536374:8"]]
+ 004b8928 ["INT_ADD", "register:40f0:8", ["const:4b8928:8", "const:4:8"]]
+ 004b8928 ["CALL", null, ["callee:00536374:8"]]
- 004b88e8 bytes 93f60194
+ 004b8928 bytes 93f60194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8619d877979cdba4d2a776638cf6729d"></a>

### [`004b894c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b894c.md) → [`004b898c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b898c.md) FUN_004b898c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`004b7fc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b7fc8.md) [`004b9db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b9/004b9db8.md) [`004b9f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b9/004b9f40.md) [`004d7390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d7/004d7390.md) [`004d7908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d7/004d7908.md) · 呼出先 1件 [`00c58650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58650.md)
- 新版 呼出元 5件 [`004b8008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8008.md) [`004b9df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b9df8.md) [`004b9f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b9f80.md) [`004d73d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d7/004d73d0.md) [`004d7948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d7/004d7948.md) · 呼出先 1件 [`00c58720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58720.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.52% / 新版 96.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b8b34",
      "incomplete_value": false,
      "site": "004b8b54",
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
            "const:584:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b8af4",
      "incomplete_value": false,
      "site": "004b8b14",
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
            "const:5e0:8"
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
      "definition_site": "004b8b3c",
      "incomplete_value": false,
      "site": "004b8b54",
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
            "const:ed:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b8afc",
      "incomplete_value": false,
      "site": "004b8b14",
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
            "const:ad:8"
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
      "definition_site": "004b8b44",
      "incomplete_value": false,
      "site": "004b8b54",
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
            "const:dc9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b8b04",
      "incomplete_value": false,
      "site": "004b8b14",
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
            "const:d98:8"
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
      "004b8b34",
      "PARAM",
      [
        "storage",
        "002a65e0",
        null,
        "string"
      ]
    ],
    [
      "004b8b3c",
      "PARAM",
      [
        "storage",
        "002b60ad",
        null,
        "string"
      ]
    ],
    [
      "004b8b44",
      "PARAM",
      [
        "storage",
        "002b4d98",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004b8b34",
      "PARAM",
      [
        "storage",
        "002a6584",
        null,
        "string"
      ]
    ],
    [
      "004b8b3c",
      "PARAM",
      [
        "storage",
        "002b60ed",
        null,
        "string"
      ]
    ],
    [
      "004b8b44",
      "PARAM",
      [
        "storage",
        "002b4dc9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b8b14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b894c.md#insn-004b8b14) · [`004b8af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b894c.md#insn-004b8af4) · [`004b8afc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b894c.md#insn-004b8afc)
- 新版 [`004b8b54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b898c.md#insn-004b8b54) · [`004b8b34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b898c.md#insn-004b8b34) · [`004b8b3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b898c.md#insn-004b8b3c)

~~~diff
- 004b8b14 ["INT_ADD", "register:40f0:8", ["const:4b8b14:8", "const:4:8"]]
- 004b8b14 ["CALL", null, ["callee:00c58720:8"]]
+ 004b8b54 ["INT_ADD", "register:40f0:8", ["const:4b8b54:8", "const:4:8"]]
+ 004b8b54 ["CALL", null, ["callee:00c58720:8"]]
- 004b8b14 bytes cf7e1e94
+ 004b8b54 bytes f37e1e94
- 004b8af4 ["COPY", "tmp:0:8", ["const:5e0:8"]]
- 004b8af4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004b8af4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004b8af4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004b8b34 ["COPY", "tmp:0:8", ["const:584:8"]]
+ 004b8b34 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004b8b34 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004b8b34 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004b8af4 bytes 00801791
+ 004b8b34 bytes 00101691
- 004b8afc ["COPY", "tmp:0:8", ["const:ad:8"]]
- 004b8afc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004b8afc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004b8afc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004b8b3c ["COPY", "tmp:0:8", ["const:ed:8"]]
+ 004b8b3c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004b8b3c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004b8b3c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004b8afc bytes 21b40291
+ 004b8b3c bytes 21b40391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7af6b2b32c151a5ec2b3da45ce5fbb6e"></a>

### [`004b8b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8b6c.md) → [`004b8bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8bac.md) FUN_004b8bac

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`004b7fc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b7fc8.md) [`004b8d14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8d14.md) [`004d7390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d7/004d7390.md) [`004d7908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d7/004d7908.md) · 呼出先 1件 [`00c58650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58650.md)
- 新版 呼出元 4件 [`004b8008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8008.md) [`004b8d54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8d54.md) [`004d73d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d7/004d73d0.md) [`004d7948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d7/004d7948.md) · 呼出先 1件 [`00c58720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58720.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.23% / 新版 96.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b8d30",
      "incomplete_value": false,
      "site": "004b8d50",
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
            "const:584:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b8cf0",
      "incomplete_value": false,
      "site": "004b8d10",
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
            "const:5e0:8"
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
      "definition_site": "004b8d38",
      "incomplete_value": false,
      "site": "004b8d50",
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
            "const:ed:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b8cf8",
      "incomplete_value": false,
      "site": "004b8d10",
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
            "const:ad:8"
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
      "definition_site": "004b8d40",
      "incomplete_value": false,
      "site": "004b8d50",
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
            "const:935:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b8d00",
      "incomplete_value": false,
      "site": "004b8d10",
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
            "const:991:8"
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
      "004b8d30",
      "PARAM",
      [
        "storage",
        "002a65e0",
        null,
        "string"
      ]
    ],
    [
      "004b8d38",
      "PARAM",
      [
        "storage",
        "002b60ad",
        null,
        "string"
      ]
    ],
    [
      "004b8d40",
      "PARAM",
      [
        "storage",
        "002af991",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004b8d30",
      "PARAM",
      [
        "storage",
        "002a6584",
        null,
        "string"
      ]
    ],
    [
      "004b8d38",
      "PARAM",
      [
        "storage",
        "002b60ed",
        null,
        "string"
      ]
    ],
    [
      "004b8d40",
      "PARAM",
      [
        "storage",
        "002af935",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b8d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8b6c.md#insn-004b8d10) · [`004b8cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8b6c.md#insn-004b8cf0) · [`004b8cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8b6c.md#insn-004b8cf8)
- 新版 [`004b8d50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8bac.md#insn-004b8d50) · [`004b8d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8bac.md#insn-004b8d30) · [`004b8d38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8bac.md#insn-004b8d38)

~~~diff
- 004b8d10 ["INT_ADD", "register:40f0:8", ["const:4b8d10:8", "const:4:8"]]
- 004b8d10 ["CALL", null, ["callee:00c58720:8"]]
+ 004b8d50 ["INT_ADD", "register:40f0:8", ["const:4b8d50:8", "const:4:8"]]
+ 004b8d50 ["CALL", null, ["callee:00c58720:8"]]
- 004b8d10 bytes 507e1e94
+ 004b8d50 bytes 747e1e94
- 004b8cf0 ["COPY", "tmp:0:8", ["const:5e0:8"]]
- 004b8cf0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004b8cf0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004b8cf0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004b8d30 ["COPY", "tmp:0:8", ["const:584:8"]]
+ 004b8d30 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004b8d30 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004b8d30 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004b8cf0 bytes 00801791
+ 004b8d30 bytes 00101691
- 004b8cf8 ["COPY", "tmp:0:8", ["const:ad:8"]]
- 004b8cf8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004b8cf8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004b8cf8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004b8d38 ["COPY", "tmp:0:8", ["const:ed:8"]]
+ 004b8d38 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004b8d38 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004b8d38 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004b8cf8 bytes 21b40291
+ 004b8d38 bytes 21b40391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1650c1de051f9e5bea5b7f913f357980"></a>

### [`004b8d14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8d14.md) → [`004b8d54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8d54.md) _ZN5Botan6BigIntmIERKS0_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58c40.md) · 呼出先 6件 [`004b87b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b87b4.md) [`004b8b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8b6c.md) [`004b8f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8f54.md) [`004d6bc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d6/004d6bc4.md) [`00540920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540920.md)
- 新版 呼出元 1件 [`00c58d10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58d10.md) · 呼出先 6件 [`004b87f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b87f4.md) [`004b8bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8bac.md) [`004b8f94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8f94.md) [`004d6c04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d6/004d6c04.md) [`00540960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540960.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.31% / 新版 99.31%

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
      "site": "004b8e84",
      "value": [
        "leaf",
        "ram:4b8f94:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004b8e44",
      "value": [
        "leaf",
        "ram:4b8f54:8"
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
      "004b8e84",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "004b8f54"
      ]
    ]
  ],
  "added": [
    [
      "004b8e84",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "004b8f94"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b8e44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8d14.md#insn-004b8e44) · [`004b8d94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8d14.md#insn-004b8d94) · [`004b8dd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8d14.md#insn-004b8dd4)
- 新版 [`004b8e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8d54.md#insn-004b8e84) · [`004b8dd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8d54.md#insn-004b8dd4) · [`004b8e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8d54.md#insn-004b8e14)

~~~diff
- 004b8e44 ["INT_ADD", "register:40f0:8", ["const:4b8e44:8", "const:4:8"]]
- 004b8e44 ["CALL", null, ["ram:4b8f54:8"]]
+ 004b8e84 ["INT_ADD", "register:40f0:8", ["const:4b8e84:8", "const:4:8"]]
+ 004b8e84 ["CALL", null, ["ram:4b8f94:8"]]
- 004b8e44 bytes 44000094
+ 004b8e84 bytes 44000094
- 004b8d94 ["INT_ADD", "register:40f0:8", ["const:4b8d94:8", "const:4:8"]]
- 004b8d94 ["CALL", null, ["callee:004b87f4:8"]]
+ 004b8dd4 ["INT_ADD", "register:40f0:8", ["const:4b8dd4:8", "const:4:8"]]
+ 004b8dd4 ["CALL", null, ["callee:004b87f4:8"]]
- 004b8d94 bytes 88feff97
+ 004b8dd4 bytes 88feff97
- 004b8dd4 ["INT_ADD", "register:40f0:8", ["const:4b8dd4:8", "const:4:8"]]
- 004b8dd4 ["CALL", null, ["callee:00540960:8"]]
+ 004b8e14 ["INT_ADD", "register:40f0:8", ["const:4b8e14:8", "const:4:8"]]
+ 004b8e14 ["CALL", null, ["callee:00540960:8"]]
- 004b8dd4 bytes d31e0294
+ 004b8e14 bytes d31e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e24fbe71a7d9cef41563cc9c3b3808be"></a>

### [`004b967c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b9/004b967c.md) → [`004b96bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b96bc.md) _ZN5BotanrmERKNS_6BigIntES2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58ca0.md) · 呼出先 11件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`00c58d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58d70.md) · 呼出先 11件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.56% / 新版 95.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 2件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004b9770",
      "incomplete_value": true,
      "site": "004b9774",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b9730",
      "incomplete_value": true,
      "site": "004b9734",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004b9794",
      "incomplete_value": true,
      "site": "004b9798",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ed8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b9754",
      "incomplete_value": true,
      "site": "004b9758",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e08:8"
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
      "definition_site": "004b9790",
      "incomplete_value": false,
      "site": "004b9798",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004b9750",
      "incomplete_value": false,
      "site": "004b9758",
      "value": [
        "leaf",
        "const:535868:8"
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
      "004b975c",
      "READ",
      [
        "storage",
        "00c9ae00",
        null,
        "pointer"
      ]
    ],
    [
      "004b9774",
      "DATA",
      [
        "storage",
        "00c69c60",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004b9790",
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
      "004b975c",
      "READ",
      [
        "storage",
        "00c9aed0",
        null,
        "pointer"
      ]
    ],
    [
      "004b9774",
      "DATA",
      [
        "storage",
        "00c69d30",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004b9790",
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

- 旧版 [`004b9758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b9/004b967c.md#insn-004b9758) · [`004b97e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b9/004b967c.md#insn-004b97e0) · [`004b9854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b9/004b967c.md#insn-004b9854)
- 新版 [`004b9798`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b96bc.md#insn-004b9798) · [`004b9820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b96bc.md#insn-004b9820) · [`004b9894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b96bc.md#insn-004b9894)

~~~diff
- 004b9758 ["INT_ADD", "register:40f0:8", ["const:4b9758:8", "const:4:8"]]
- 004b9758 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004b9798 ["INT_ADD", "register:40f0:8", ["const:4b9798:8", "const:4:8"]]
+ 004b9798 ["CALL", null, ["callee:00c57fe0:8"]]
- 004b9758 bytes ee791e94
+ 004b9798 bytes 127a1e94
- 004b97e0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b97e0 ["INT_ADD", "register:40f0:8", ["const:4b97e0:8", "const:4:8"]]
- 004b97e0 ["CALLIND", null, ["register:0:8"]]
+ 004b9820 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b9820 ["INT_ADD", "register:40f0:8", ["const:4b9820:8", "const:4:8"]]
+ 004b9820 ["CALLIND", null, ["register:0:8"]]
- 004b97e0 bytes 20013fd6
+ 004b9820 bytes 20013fd6
- 004b9854 ["INT_ADD", "register:40f0:8", ["const:4b9854:8", "const:4:8"]]
- 004b9854 ["CALL", null, ["callee:0043de18:8"]]
+ 004b9894 ["INT_ADD", "register:40f0:8", ["const:4b9894:8", "const:4:8"]]
+ 004b9894 ["CALL", null, ["callee:0043de18:8"]]
- 004b9854 bytes 6111fe97
+ 004b9894 bytes 6111fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-822cadddac93a745e5eeabcb4356eead"></a>

### [`004b98fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b9/004b98fc.md) → [`004b993c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b993c.md) _ZN5Botan6BigIntrMEj

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`004bbb6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bbb6c.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00540920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540920.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`004bbbac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bbbac.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00540960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540960.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.95% / 新版 96.95%

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
      "definition_site": "004b9b38",
      "incomplete_value": true,
      "site": "004b9b3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b9af8",
      "incomplete_value": true,
      "site": "004b9afc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004b9b40",
      "incomplete_value": true,
      "site": "004b9b44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ed8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b9b00",
      "incomplete_value": true,
      "site": "004b9b04",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e08:8"
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
      "definition_site": "004b9b2c",
      "incomplete_value": false,
      "site": "004b9b44",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004b9aec",
      "incomplete_value": false,
      "site": "004b9b04",
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
      "004b9b18",
      "READ",
      [
        "storage",
        "00c9ae00",
        null,
        "pointer"
      ]
    ],
    [
      "004b9b2c",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004b9b3c",
      "DATA",
      [
        "storage",
        "00c69c60",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004b9b18",
      "READ",
      [
        "storage",
        "00c9aed0",
        null,
        "pointer"
      ]
    ],
    [
      "004b9b2c",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004b9b3c",
      "DATA",
      [
        "storage",
        "00c69d30",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b9b04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b9/004b98fc.md#insn-004b9b04) · [`004b9950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b9/004b98fc.md#insn-004b9950) · [`004b99a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b9/004b98fc.md#insn-004b99a4)
- 新版 [`004b9b44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b993c.md#insn-004b9b44) · [`004b9990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b993c.md#insn-004b9990) · [`004b99e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b993c.md#insn-004b99e4)

~~~diff
- 004b9b04 ["INT_ADD", "register:40f0:8", ["const:4b9b04:8", "const:4:8"]]
- 004b9b04 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004b9b44 ["INT_ADD", "register:40f0:8", ["const:4b9b44:8", "const:4:8"]]
+ 004b9b44 ["CALL", null, ["callee:00c57fe0:8"]]
- 004b9b04 bytes 03791e94
+ 004b9b44 bytes 27791e94
- 004b9950 ["INT_ADD", "register:40f0:8", ["const:4b9950:8", "const:4:8"]]
- 004b9950 ["CALL", null, ["callee:00c58160:8"]]
+ 004b9990 ["INT_ADD", "register:40f0:8", ["const:4b9990:8", "const:4:8"]]
+ 004b9990 ["CALL", null, ["callee:00c58160:8"]]
- 004b9950 bytes d0791e94
+ 004b9990 bytes f4791e94
- 004b99a4 ["INT_ADD", "register:40f0:8", ["const:4b99a4:8", "const:4:8"]]
- 004b99a4 ["CALL", null, ["callee:004bbbac:8"]]
+ 004b99e4 ["INT_ADD", "register:40f0:8", ["const:4b99e4:8", "const:4:8"]]
+ 004b99e4 ["CALL", null, ["callee:004bbbac:8"]]
- 004b99a4 bytes 72080094
+ 004b99e4 bytes 72080094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aed85830cd3e5b70b763f3531b33d8bc"></a>

### [`004ba498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ba/004ba498.md) → [`004ba4d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ba/004ba4d8.md) _ZN5BotanrmERKNS_6BigIntEj

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58cd0.md) · 呼出先 4件 [`004bbb6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bbb6c.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`00c58da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58da0.md) · 呼出先 4件 [`004bbbac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bbbac.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.51% / 新版 95.51%

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
      "definition_site": "004ba62c",
      "incomplete_value": true,
      "site": "004ba630",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ba5ec",
      "incomplete_value": true,
      "site": "004ba5f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004ba634",
      "incomplete_value": true,
      "site": "004ba638",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ed8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ba5f4",
      "incomplete_value": true,
      "site": "004ba5f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e08:8"
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
      "definition_site": "004ba620",
      "incomplete_value": false,
      "site": "004ba638",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004ba5e0",
      "incomplete_value": false,
      "site": "004ba5f8",
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
      "004ba60c",
      "READ",
      [
        "storage",
        "00c9ae00",
        null,
        "pointer"
      ]
    ],
    [
      "004ba620",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004ba630",
      "DATA",
      [
        "storage",
        "00c69c60",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004ba60c",
      "READ",
      [
        "storage",
        "00c9aed0",
        null,
        "pointer"
      ]
    ],
    [
      "004ba620",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004ba630",
      "DATA",
      [
        "storage",
        "00c69d30",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ba5f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ba/004ba498.md#insn-004ba5f8) · [`004ba534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ba/004ba498.md#insn-004ba534) · [`004ba594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ba/004ba498.md#insn-004ba594)
- 新版 [`004ba638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ba/004ba4d8.md#insn-004ba638) · [`004ba574`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ba/004ba4d8.md#insn-004ba574) · [`004ba5d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ba/004ba4d8.md#insn-004ba5d4)

~~~diff
- 004ba5f8 ["INT_ADD", "register:40f0:8", ["const:4ba5f8:8", "const:4:8"]]
- 004ba5f8 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004ba638 ["INT_ADD", "register:40f0:8", ["const:4ba638:8", "const:4:8"]]
+ 004ba638 ["CALL", null, ["callee:00c57fe0:8"]]
- 004ba5f8 bytes 46761e94
+ 004ba638 bytes 6a761e94
- 004ba534 ["INT_ADD", "register:40f0:8", ["const:4ba534:8", "const:4:8"]]
- 004ba534 ["CALL", null, ["callee:004bbbac:8"]]
+ 004ba574 ["INT_ADD", "register:40f0:8", ["const:4ba574:8", "const:4:8"]]
+ 004ba574 ["CALL", null, ["callee:004bbbac:8"]]
- 004ba534 bytes 8e050094
+ 004ba574 bytes 8e050094
- 004ba594 ["INT_ADD", "register:40f0:8", ["const:4ba594:8", "const:4:8"]]
- 004ba594 ["CALL", null, ["callee:00c57fc0:8"]]
+ 004ba5d4 ["INT_ADD", "register:40f0:8", ["const:4ba5d4:8", "const:4:8"]]
+ 004ba5d4 ["CALL", null, ["callee:00c57fc0:8"]]
- 004ba594 bytes 57761e94
+ 004ba5d4 bytes 7b761e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f9242d71197e337f7a05c53adac4ab6"></a>

### [`004bb12c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bb12c.md) → [`004bb16c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb16c.md) _ZNK5Botan6BigInt13get_substringEmm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58d10.md) · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`00c58de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58de0.md) · 呼出先 6件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.52% / 新版 98.52%

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
      "definition_site": "004bb338",
      "incomplete_value": false,
      "site": "004bb340",
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
            "const:f44:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bb2f8",
      "incomplete_value": false,
      "site": "004bb300",
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
            "const:f91:8"
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
      "definition_site": "004bb374",
      "incomplete_value": true,
      "site": "004bb380",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004bb334",
      "incomplete_value": true,
      "site": "004bb340",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bb370",
      "incomplete_value": false,
      "site": "004bb380",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004bb330",
      "incomplete_value": false,
      "site": "004bb340",
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
      "004bb338",
      "PARAM",
      [
        "storage",
        "0029ef91",
        null,
        "string"
      ]
    ],
    [
      "004bb370",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004bb374",
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
      "004bb338",
      "PARAM",
      [
        "storage",
        "0029ef44",
        null,
        "string"
      ]
    ],
    [
      "004bb370",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004bb374",
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

- 旧版 [`004bb300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bb12c.md#insn-004bb300) · [`004bb340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bb12c.md#insn-004bb340) · [`004bb2ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bb12c.md#insn-004bb2ec)
- 新版 [`004bb340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb16c.md#insn-004bb340) · [`004bb380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb16c.md#insn-004bb380) · [`004bb32c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb16c.md#insn-004bb32c)

~~~diff
- 004bb300 ["INT_ADD", "register:40f0:8", ["const:4bb300:8", "const:4:8"]]
- 004bb300 ["CALL", null, ["callee:0043de18:8"]]
+ 004bb340 ["INT_ADD", "register:40f0:8", ["const:4bb340:8", "const:4:8"]]
+ 004bb340 ["CALL", null, ["callee:0043de18:8"]]
- 004bb300 bytes b60afe97
+ 004bb340 bytes b60afe97
- 004bb340 ["INT_ADD", "register:40f0:8", ["const:4bb340:8", "const:4:8"]]
- 004bb340 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004bb380 ["INT_ADD", "register:40f0:8", ["const:4bb380:8", "const:4:8"]]
+ 004bb380 ["CALL", null, ["callee:00c57fe0:8"]]
- 004bb340 bytes f4721e94
+ 004bb380 bytes 18731e94
- 004bb2ec ["INT_ADD", "register:40f0:8", ["const:4bb2ec:8", "const:4:8"]]
- 004bb2ec ["CALL", null, ["callee:00c57fc0:8"]]
+ 004bb32c ["INT_ADD", "register:40f0:8", ["const:4bb32c:8", "const:4:8"]]
+ 004bb32c ["CALL", null, ["callee:00c57fc0:8"]]
- 004bb2ec bytes 01731e94
+ 004bb32c bytes 25731e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80bf6481ca39c7ab46e61202db5f725c"></a>

### [`004bb394`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bb394.md) → [`004bb3d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb3d4.md) _ZNK5Botan6BigInt9to_u32bitEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.08% / 新版 96.08%

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
      "definition_site": "004bb4bc",
      "incomplete_value": false,
      "site": "004bb4c4",
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
            "const:849:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bb47c",
      "incomplete_value": false,
      "site": "004bb484",
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
            "const:89d:8"
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
      "definition_site": "004bb4f8",
      "incomplete_value": true,
      "site": "004bb504",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004bb4b8",
      "incomplete_value": true,
      "site": "004bb4c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bb4f4",
      "incomplete_value": false,
      "site": "004bb504",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004bb4b4",
      "incomplete_value": false,
      "site": "004bb4c4",
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
      "004bb4bc",
      "PARAM",
      [
        "storage",
        "002bd89d",
        null,
        "string"
      ]
    ],
    [
      "004bb4f4",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004bb4f8",
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
      "004bb4bc",
      "PARAM",
      [
        "storage",
        "002bd849",
        null,
        "string"
      ]
    ],
    [
      "004bb4f4",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004bb4f8",
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

- 旧版 [`004bb484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bb394.md#insn-004bb484) · [`004bb4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bb394.md#insn-004bb4c4) · [`004bb4e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bb394.md#insn-004bb4e8)
- 新版 [`004bb4c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb3d4.md#insn-004bb4c4) · [`004bb504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb3d4.md#insn-004bb504) · [`004bb528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb3d4.md#insn-004bb528)

~~~diff
- 004bb484 ["INT_ADD", "register:40f0:8", ["const:4bb484:8", "const:4:8"]]
- 004bb484 ["CALL", null, ["callee:0043de18:8"]]
+ 004bb4c4 ["INT_ADD", "register:40f0:8", ["const:4bb4c4:8", "const:4:8"]]
+ 004bb4c4 ["CALL", null, ["callee:0043de18:8"]]
- 004bb484 bytes 550afe97
+ 004bb4c4 bytes 550afe97
- 004bb4c4 ["INT_ADD", "register:40f0:8", ["const:4bb4c4:8", "const:4:8"]]
- 004bb4c4 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004bb504 ["INT_ADD", "register:40f0:8", ["const:4bb504:8", "const:4:8"]]
+ 004bb504 ["CALL", null, ["callee:00c57fe0:8"]]
- 004bb4c4 bytes 93721e94
+ 004bb504 bytes b7721e94
- 004bb4e8 ["INT_ADD", "register:40f0:8", ["const:4bb4e8:8", "const:4:8"]]
- 004bb4e8 ["CALL", null, ["callee:0043de18:8"]]
+ 004bb528 ["INT_ADD", "register:40f0:8", ["const:4bb528:8", "const:4:8"]]
+ 004bb528 ["CALL", null, ["callee:0043de18:8"]]
- 004bb4e8 bytes 3c0afe97
+ 004bb528 bytes 3c0afe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88abc880aa3bad40805927238742bb42"></a>

### [`004bb730`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bb730.md) → [`004bb770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb770.md) _ZN5Botan6BigInt17const_time_lookupERNSt6__ndk16vectorIjNS_16secure_allocatorIjEEEERKNS2_IS0_NS1_9allocatorIS0_EEEEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58d20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58d20.md) · 呼出先 2件 [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md) [`00c58650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58650.md)
- 新版 呼出元 1件 [`00c58df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58df0.md) · 呼出先 2件 [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md) [`00c58720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58720.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.04% / 新版 96.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bb8e0",
      "incomplete_value": false,
      "site": "004bb900",
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
            "const:1cb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bb8a0",
      "incomplete_value": false,
      "site": "004bb8c0",
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
            "const:18b:8"
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
      "definition_site": "004bb8e8",
      "incomplete_value": false,
      "site": "004bb900",
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
            "const:f72:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bb8a8",
      "incomplete_value": false,
      "site": "004bb8c0",
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
            "const:fbf:8"
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
      "definition_site": "004bb8f0",
      "incomplete_value": false,
      "site": "004bb900",
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
            "const:4e3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bb8b0",
      "incomplete_value": false,
      "site": "004bb8c0",
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
            "const:537:8"
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
      "004bb8e0",
      "PARAM",
      [
        "storage",
        "002b818b",
        null,
        "string"
      ]
    ],
    [
      "004bb8e8",
      "PARAM",
      [
        "storage",
        "0029efbf",
        null,
        "string"
      ]
    ],
    [
      "004bb8f0",
      "PARAM",
      [
        "storage",
        "002bc537",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bb8e0",
      "PARAM",
      [
        "storage",
        "002b81cb",
        null,
        "string"
      ]
    ],
    [
      "004bb8e8",
      "PARAM",
      [
        "storage",
        "0029ef72",
        null,
        "string"
      ]
    ],
    [
      "004bb8f0",
      "PARAM",
      [
        "storage",
        "002bc4e3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bb8c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bb730.md#insn-004bb8c0) · [`004bb768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bb730.md#insn-004bb768) · [`004bb8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bb730.md#insn-004bb8a0)
- 新版 [`004bb900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb770.md#insn-004bb900) · [`004bb7a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb770.md#insn-004bb7a8) · [`004bb8e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb770.md#insn-004bb8e0)

~~~diff
- 004bb8c0 ["INT_ADD", "register:40f0:8", ["const:4bb8c0:8", "const:4:8"]]
- 004bb8c0 ["CALL", null, ["callee:00c58720:8"]]
+ 004bb900 ["INT_ADD", "register:40f0:8", ["const:4bb900:8", "const:4:8"]]
+ 004bb900 ["CALL", null, ["callee:00c58720:8"]]
- 004bb8c0 bytes 64731e94
+ 004bb900 bytes 88731e94
- 004bb768 ["INT_ADD", "register:40f0:8", ["const:4bb768:8", "const:4:8"]]
- 004bb768 ["CALL", null, ["callee:00c58160:8"]]
+ 004bb7a8 ["INT_ADD", "register:40f0:8", ["const:4bb7a8:8", "const:4:8"]]
+ 004bb7a8 ["CALL", null, ["callee:00c58160:8"]]
- 004bb768 bytes 4a721e94
+ 004bb7a8 bytes 6e721e94
- 004bb8a0 ["COPY", "tmp:0:8", ["const:18b:8"]]
- 004bb8a0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004bb8a0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004bb8a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004bb8e0 ["COPY", "tmp:0:8", ["const:1cb:8"]]
+ 004bb8e0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004bb8e0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004bb8e0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004bb8a0 bytes 002c0691
+ 004bb8e0 bytes 002c0791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f369cdd4e96da87640059dc86e2ebc04"></a>

### [`004bb8c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bb8c4.md) → [`004bb904`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb904.md) FUN_004bb904

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004b6728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b6/004b6728.md) · 呼出先 7件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c58920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58920.md) [`00c58b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58b40.md) [`00c58c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58c40.md)
- 新版 呼出元 1件 [`004b6768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b6/004b6768.md) · 呼出先 7件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c589f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c589f0.md) [`00c58c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58c10.md) [`00c58d10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58d10.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.13% / 新版 96.13%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004bba94",
      "incomplete_value": true,
      "site": "004bba94",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bba54",
      "incomplete_value": true,
      "site": "004bba54",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004bbb24",
      "incomplete_value": true,
      "site": "004bbb24",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bbae4",
      "incomplete_value": true,
      "site": "004bbae4",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004bbb54",
      "incomplete_value": true,
      "site": "004bbb54",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bbb14",
      "incomplete_value": true,
      "site": "004bbb14",
      "value": [
        "LOAD",
        "8",
        [
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
      "004bba84",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004bbb14",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004bbb44",
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
      "004bba84",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "004bbb14",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "004bbb44",
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

- 旧版 [`004bba54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bb8c4.md#insn-004bba54) · [`004bbad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bb8c4.md#insn-004bbad4) · [`004bbae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bb8c4.md#insn-004bbae4)
- 新版 [`004bba94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb904.md#insn-004bba94) · [`004bbb14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb904.md#insn-004bbb14) · [`004bbb24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb904.md#insn-004bbb24)

~~~diff
- 004bba54 ["COPY", "register:0:8", ["register:4048:8"]]
- 004bba54 ["INT_ADD", "register:40f0:8", ["const:4bba54:8", "const:4:8"]]
- 004bba54 ["CALLIND", null, ["register:0:8"]]
+ 004bba94 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004bba94 ["INT_ADD", "register:40f0:8", ["const:4bba94:8", "const:4:8"]]
+ 004bba94 ["CALLIND", null, ["register:0:8"]]
- 004bba54 bytes 20013fd6
+ 004bba94 bytes 20013fd6
- 004bbad4 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:738:8"]]
- 004bbad4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004bbb14 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:808:8"]]
+ 004bbb14 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004bbad4 bytes 099f43f9
+ 004bbb14 bytes 090744f9
- 004bbae4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004bbae4 ["INT_ADD", "register:40f0:8", ["const:4bbae4:8", "const:4:8"]]
- 004bbae4 ["CALLIND", null, ["register:0:8"]]
+ 004bbb24 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004bbb24 ["INT_ADD", "register:40f0:8", ["const:4bbb24:8", "const:4:8"]]
+ 004bbb24 ["CALLIND", null, ["register:0:8"]]
- 004bbae4 bytes 20013fd6
+ 004bbb24 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-955d90c2fe55c550376382be79e5f69b"></a>

### [`004bbb6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bbb6c.md) → [`004bbbac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bbbac.md) FUN_004bbbac

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`004b6728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b6/004b6728.md) [`004b98fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b9/004b98fc.md) [`004ba498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ba/004ba498.md) [`004ddf08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004dd/004ddf08.md) · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 4件 [`004b6768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b6/004b6768.md) [`004b993c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b993c.md) [`004ba4d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ba/004ba4d8.md) [`004ddf48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004dd/004ddf48.md) · 呼出先 6件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

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
      "definition_site": "004bbc18",
      "incomplete_value": false,
      "site": "004bbc20",
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
            "const:dd5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bbbd8",
      "incomplete_value": false,
      "site": "004bbbe0",
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
            "const:da4:8"
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
      "definition_site": "004bbc54",
      "incomplete_value": true,
      "site": "004bbc60",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004bbc14",
      "incomplete_value": true,
      "site": "004bbc20",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bbc50",
      "incomplete_value": false,
      "site": "004bbc60",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004bbc10",
      "incomplete_value": false,
      "site": "004bbc20",
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
      "004bbc18",
      "PARAM",
      [
        "storage",
        "002b4da4",
        null,
        "string"
      ]
    ],
    [
      "004bbc50",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004bbc54",
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
      "004bbc18",
      "PARAM",
      [
        "storage",
        "002b4dd5",
        null,
        "string"
      ]
    ],
    [
      "004bbc50",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004bbc54",
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

- 旧版 [`004bbbe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bbb6c.md#insn-004bbbe0) · [`004bbc20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bbb6c.md#insn-004bbc20) · [`004bbbcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bbb6c.md#insn-004bbbcc)
- 新版 [`004bbc20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bbbac.md#insn-004bbc20) · [`004bbc60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bbbac.md#insn-004bbc60) · [`004bbc0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bbbac.md#insn-004bbc0c)

~~~diff
- 004bbbe0 ["INT_ADD", "register:40f0:8", ["const:4bbbe0:8", "const:4:8"]]
- 004bbbe0 ["CALL", null, ["callee:0043de18:8"]]
+ 004bbc20 ["INT_ADD", "register:40f0:8", ["const:4bbc20:8", "const:4:8"]]
+ 004bbc20 ["CALL", null, ["callee:0043de18:8"]]
- 004bbbe0 bytes 7e08fe97
+ 004bbc20 bytes 7e08fe97
- 004bbc20 ["INT_ADD", "register:40f0:8", ["const:4bbc20:8", "const:4:8"]]
- 004bbc20 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004bbc60 ["INT_ADD", "register:40f0:8", ["const:4bbc60:8", "const:4:8"]]
+ 004bbc60 ["CALL", null, ["callee:00c57fe0:8"]]
- 004bbc20 bytes bc701e94
+ 004bbc60 bytes e0701e94
- 004bbbcc ["INT_ADD", "register:40f0:8", ["const:4bbbcc:8", "const:4:8"]]
- 004bbbcc ["CALL", null, ["callee:00c57fc0:8"]]
+ 004bbc0c ["INT_ADD", "register:40f0:8", ["const:4bbc0c:8", "const:4:8"]]
+ 004bbc0c ["CALL", null, ["callee:00c57fc0:8"]]
- 004bbbcc bytes c9701e94
+ 004bbc0c bytes ed701e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d033781d00201254eaf7d2a467a5414"></a>

### [`004bc000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bc000.md) → [`004bc040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc040.md) _ZN5Botan11BlockCipher15create_or_throwERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

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
      "definition_site": "004bc0b8",
      "incomplete_value": false,
      "site": "004bc0c0",
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
            "const:c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bc078",
      "incomplete_value": false,
      "site": "004bc080",
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
            "const:10d:8"
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
      "definition_site": "004bc0f8",
      "incomplete_value": true,
      "site": "004bc104",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bc0b8",
      "incomplete_value": true,
      "site": "004bc0c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e28:8"
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
      "definition_site": "004bc0f4",
      "incomplete_value": false,
      "site": "004bc104",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004bc0b4",
      "incomplete_value": false,
      "site": "004bc0c4",
      "value": [
        "leaf",
        "const:535868:8"
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
      "004bc0b8",
      "PARAM",
      [
        "storage",
        "002a410d",
        null,
        "string"
      ]
    ],
    [
      "004bc0f4",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004bc0f8",
      "READ",
      [
        "storage",
        "00c9ae28",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004bc0b8",
      "PARAM",
      [
        "storage",
        "002a40c0",
        null,
        "string"
      ]
    ],
    [
      "004bc0f4",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004bc0f8",
      "READ",
      [
        "storage",
        "00c9aef8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bc080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bc000.md#insn-004bc080) · [`004bc0c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bc000.md#insn-004bc0c4) · [`004bc034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bc000.md#insn-004bc034)
- 新版 [`004bc0c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc040.md#insn-004bc0c0) · [`004bc104`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc040.md#insn-004bc104) · [`004bc074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc040.md#insn-004bc074)

~~~diff
- 004bc080 ["INT_ADD", "register:40f0:8", ["const:4bc080:8", "const:4:8"]]
- 004bc080 ["CALL", null, ["callee:0043de18:8"]]
+ 004bc0c0 ["INT_ADD", "register:40f0:8", ["const:4bc0c0:8", "const:4:8"]]
+ 004bc0c0 ["CALL", null, ["callee:0043de18:8"]]
- 004bc080 bytes 5607fe97
+ 004bc0c0 bytes 5607fe97
- 004bc0c4 ["INT_ADD", "register:40f0:8", ["const:4bc0c4:8", "const:4:8"]]
- 004bc0c4 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004bc104 ["INT_ADD", "register:40f0:8", ["const:4bc104:8", "const:4:8"]]
+ 004bc104 ["CALL", null, ["callee:00c57fe0:8"]]
- 004bc0c4 bytes 936f1e94
+ 004bc104 bytes b76f1e94
- 004bc034 ["INT_ADD", "register:40f0:8", ["const:4bc034:8", "const:4:8"]]
- 004bc034 ["CALL", null, ["callee:00c58e00:8"]]
+ 004bc074 ["INT_ADD", "register:40f0:8", ["const:4bc074:8", "const:4:8"]]
+ 004bc074 ["CALL", null, ["callee:00c58e00:8"]]
- 004bc034 bytes 3f731e94
+ 004bc074 bytes 63731e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-583060207114494b08ba9fec917891e4"></a>

### [`004bc3b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bc3b8.md) → [`004bc3f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc3f8.md) _ZN5Botan8CBC_ModeC2EPNS_11BlockCipherEPNS_28BlockCipherModePaddingMethodE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58d60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58d60.md) · 呼出先 9件 [`004a684c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a684c.md) [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)
- 新版 呼出元 1件 [`00c58e30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58e30.md) · 呼出先 9件 [`004a688c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a688c.md) [`004b3548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3548.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.64% / 新版 93.64%

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
      "definition_site": "004bc430",
      "incomplete_value": true,
      "site": "004bc430",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bc3f0",
      "incomplete_value": true,
      "site": "004bc3f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004bc4d4",
      "incomplete_value": false,
      "site": "004bc4e0",
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
            "const:333:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bc494",
      "incomplete_value": false,
      "site": "004bc4a0",
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
            "const:387:8"
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
      "definition_site": "004bc500",
      "incomplete_value": false,
      "site": "004bc508",
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
            "const:bba:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bc4c0",
      "incomplete_value": false,
      "site": "004bc4c8",
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
            "const:b8b:8"
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
      "004bc420",
      "READ",
      [
        "storage",
        "00c9ae30",
        null,
        "pointer"
      ]
    ],
    [
      "004bc430",
      "DATA",
      [
        "storage",
        "00c66420",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "004bc4d4",
      "PARAM",
      [
        "storage",
        "002bb387",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bc420",
      "READ",
      [
        "storage",
        "00c9af00",
        null,
        "pointer"
      ]
    ],
    [
      "004bc430",
      "DATA",
      [
        "storage",
        "00c664f0",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "004bc4d4",
      "PARAM",
      [
        "storage",
        "002bb333",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bc4a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bc3b8.md#insn-004bc4a0) · [`004bc4c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bc3b8.md#insn-004bc4c8) · [`004bc514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bc3b8.md#insn-004bc514)
- 新版 [`004bc4e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc3f8.md#insn-004bc4e0) · [`004bc508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc3f8.md#insn-004bc508) · [`004bc554`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc3f8.md#insn-004bc554)

~~~diff
- 004bc4a0 ["INT_ADD", "register:40f0:8", ["const:4bc4a0:8", "const:4:8"]]
- 004bc4a0 ["CALL", null, ["callee:00c58030:8"]]
+ 004bc4e0 ["INT_ADD", "register:40f0:8", ["const:4bc4e0:8", "const:4:8"]]
+ 004bc4e0 ["CALL", null, ["callee:00c58030:8"]]
- 004bc4a0 bytes b06e1e94
+ 004bc4e0 bytes d46e1e94
- 004bc4c8 ["INT_ADD", "register:40f0:8", ["const:4bc4c8:8", "const:4:8"]]
- 004bc4c8 ["CALL", null, ["callee:00c58040:8"]]
+ 004bc508 ["INT_ADD", "register:40f0:8", ["const:4bc508:8", "const:4:8"]]
+ 004bc508 ["CALL", null, ["callee:00c58040:8"]]
- 004bc4c8 bytes aa6e1e94
+ 004bc508 bytes ce6e1e94
- 004bc514 ["INT_ADD", "register:40f0:8", ["const:4bc514:8", "const:4:8"]]
- 004bc514 ["CALL", null, ["callee:00c58040:8"]]
+ 004bc554 ["INT_ADD", "register:40f0:8", ["const:4bc554:8", "const:4:8"]]
+ 004bc554 ["CALL", null, ["callee:00c58040:8"]]
- 004bc514 bytes 976e1e94
+ 004bc554 bytes bb6e1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-169a2c35d0ac8f01b565fbe33b091bef"></a>

### [`004bc738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bc738.md) → [`004bc778`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc778.md) _ZNK5Botan8CBC_Mode4nameEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58d70.md) · 呼出先 5件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c58650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58650.md)
- 新版 呼出元 1件 [`00c58e40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58e40.md) · 呼出先 5件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c58720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58720.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bc7c0",
      "incomplete_value": false,
      "site": "004bc7c8",
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
            "const:cd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bc780",
      "incomplete_value": false,
      "site": "004bc788",
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
            "const:11a:8"
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
      "definition_site": "004bc86c",
      "incomplete_value": false,
      "site": "004bc874",
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
            "const:fdd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bc82c",
      "incomplete_value": false,
      "site": "004bc834",
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
            "const:2a:8"
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
      "definition_site": "004bc900",
      "incomplete_value": false,
      "site": "004bc920",
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
            "const:846:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bc8c0",
      "incomplete_value": false,
      "site": "004bc8e0",
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
            "const:8a2:8"
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
      "004bc7c0",
      "PARAM",
      [
        "storage",
        "002a411a",
        null,
        "string"
      ]
    ],
    [
      "004bc86c",
      "PARAM",
      [
        "storage",
        "002a002a",
        null,
        "string"
      ]
    ],
    [
      "004bc900",
      "PARAM",
      [
        "storage",
        "002ac8a2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bc7c0",
      "PARAM",
      [
        "storage",
        "002a40cd",
        null,
        "string"
      ]
    ],
    [
      "004bc86c",
      "PARAM",
      [
        "storage",
        "0029ffdd",
        null,
        "string"
      ]
    ],
    [
      "004bc900",
      "PARAM",
      [
        "storage",
        "002ac846",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bc788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bc738.md#insn-004bc788) · [`004bc834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bc738.md#insn-004bc834) · [`004bc874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bc738.md#insn-004bc874)
- 新版 [`004bc7c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc778.md#insn-004bc7c8) · [`004bc874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc778.md#insn-004bc874) · [`004bc8b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bc778.md#insn-004bc8b4)

~~~diff
- 004bc788 ["INT_ADD", "register:40f0:8", ["const:4bc788:8", "const:4:8"]]
- 004bc788 ["CALL", null, ["callee:00c58040:8"]]
+ 004bc7c8 ["INT_ADD", "register:40f0:8", ["const:4bc7c8:8", "const:4:8"]]
+ 004bc7c8 ["CALL", null, ["callee:00c58040:8"]]
- 004bc788 bytes fa6d1e94
+ 004bc7c8 bytes 1e6e1e94
- 004bc834 ["INT_ADD", "register:40f0:8", ["const:4bc834:8", "const:4:8"]]
- 004bc834 ["CALL", null, ["callee:00c58040:8"]]
+ 004bc874 ["INT_ADD", "register:40f0:8", ["const:4bc874:8", "const:4:8"]]
+ 004bc874 ["CALL", null, ["callee:00c58040:8"]]
- 004bc834 bytes cf6d1e94
+ 004bc874 bytes f36d1e94
- 004bc874 ["INT_ADD", "register:40f0:8", ["const:4bc874:8", "const:4:8"]]
- 004bc874 ["CALL", null, ["callee:00c57f80:8"]]
+ 004bc8b4 ["INT_ADD", "register:40f0:8", ["const:4bc8b4:8", "const:4:8"]]
+ 004bc8b4 ["CALL", null, ["callee:00c57f80:8"]]
- 004bc874 bytes 8f6d1e94
+ 004bc8b4 bytes b36d1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64fc5fc2f2f9ebc39f3f34f1c9352acb"></a>

### [`004bca00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bca00.md) → [`004bca40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bca40.md) FUN_004bca40

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 10件 [`004bc9f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bc9f8.md) [`004bf444`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bf444.md) [`004c4068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c4068.md) [`004c44a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c44a8.md) [`004c4d0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c4d0c.md) · 呼出先 5件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c58d80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58d80.md)
- 新版 呼出元 10件 [`004bca38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bca38.md) [`004bf484`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf484.md) [`004c40a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c40a8.md) [`004c44e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c44e8.md) [`004c4d4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4d4c.md) · 呼出先 5件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c58e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58e50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.51% / 新版 98.51%

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
      "definition_site": "004bcb38",
      "incomplete_value": true,
      "site": "004bcb44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bcaf8",
      "incomplete_value": true,
      "site": "004bcb04",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e38:8"
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
      "definition_site": "004bcb34",
      "incomplete_value": false,
      "site": "004bcb44",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004bcaf4",
      "incomplete_value": false,
      "site": "004bcb04",
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
      "004bcb34",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004bcb38",
      "READ",
      [
        "storage",
        "00c9ae38",
        null,
        "pointer"
      ]
    ],
    [
      "004bcb38",
      "PARAM",
      [
        "storage",
        "00c66e28",
        "_ZTIN5Botan18Invalid_Key_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004bcb34",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004bcb38",
      "READ",
      [
        "storage",
        "00c9af08",
        null,
        "pointer"
      ]
    ],
    [
      "004bcb38",
      "PARAM",
      [
        "storage",
        "00c66ef8",
        "_ZTIN5Botan18Invalid_Key_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bcac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bca00.md#insn-004bcac4) · [`004bcb04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bca00.md#insn-004bcb04) · [`004bca38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bca00.md#insn-004bca38)
- 新版 [`004bcb04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bca40.md#insn-004bcb04) · [`004bcb44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bca40.md#insn-004bcb44) · [`004bca78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bca40.md#insn-004bca78)

~~~diff
- 004bcac4 ["COPY", "register:0:8", ["register:4050:8"]]
- 004bcac4 ["INT_ADD", "register:40f0:8", ["const:4bcac4:8", "const:4:8"]]
- 004bcac4 ["CALLIND", null, ["register:0:8"]]
+ 004bcb04 ["COPY", "register:0:8", ["register:4050:8"]]
+ 004bcb04 ["INT_ADD", "register:40f0:8", ["const:4bcb04:8", "const:4:8"]]
+ 004bcb04 ["CALLIND", null, ["register:0:8"]]
- 004bcac4 bytes 40013fd6
+ 004bcb04 bytes 40013fd6
- 004bcb04 ["INT_ADD", "register:40f0:8", ["const:4bcb04:8", "const:4:8"]]
- 004bcb04 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004bcb44 ["INT_ADD", "register:40f0:8", ["const:4bcb44:8", "const:4:8"]]
+ 004bcb44 ["CALL", null, ["callee:00c57fe0:8"]]
- 004bcb04 bytes 036d1e94
+ 004bcb44 bytes 276d1e94
- 004bca38 ["COPY", "register:0:8", ["register:4048:8"]]
- 004bca38 ["INT_ADD", "register:40f0:8", ["const:4bca38:8", "const:4:8"]]
- 004bca38 ["CALLIND", null, ["register:0:8"]]
+ 004bca78 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004bca78 ["INT_ADD", "register:40f0:8", ["const:4bca78:8", "const:4:8"]]
+ 004bca78 ["CALLIND", null, ["register:0:8"]]
- 004bca38 bytes 20013fd6
+ 004bca78 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-943bdef2f0efaaad44299437df872de9"></a>

### [`004bcb54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bcb54.md) → [`004bcb94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bcb94.md) _ZN5Botan8CBC_Mode9start_msgEPKhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`005433c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/005433c0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00543400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543400.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.46% / 新版 98.46%

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
      "definition_site": "004bcc84",
      "incomplete_value": true,
      "site": "004bcc90",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bcc44",
      "incomplete_value": true,
      "site": "004bcc50",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e40:8"
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
      "definition_site": "004bcc80",
      "incomplete_value": false,
      "site": "004bcc90",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004bcc40",
      "incomplete_value": false,
      "site": "004bcc50",
      "value": [
        "leaf",
        "const:535868:8"
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
      "004bcc80",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004bcc84",
      "READ",
      [
        "storage",
        "00c9ae40",
        null,
        "pointer"
      ]
    ],
    [
      "004bcc84",
      "PARAM",
      [
        "storage",
        "00c664b0",
        "_ZTIN5Botan17Invalid_IV_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004bcc80",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004bcc84",
      "READ",
      [
        "storage",
        "00c9af10",
        null,
        "pointer"
      ]
    ],
    [
      "004bcc84",
      "PARAM",
      [
        "storage",
        "00c66580",
        "_ZTIN5Botan17Invalid_IV_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bcc10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bcb54.md#insn-004bcc10) · [`004bcc50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bcb54.md#insn-004bcc50) · [`004bcb8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bcb54.md#insn-004bcb8c)
- 新版 [`004bcc50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bcb94.md#insn-004bcc50) · [`004bcc90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bcb94.md#insn-004bcc90) · [`004bcbcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bcb94.md#insn-004bcbcc)

~~~diff
- 004bcc10 ["COPY", "register:0:8", ["register:4050:8"]]
- 004bcc10 ["INT_ADD", "register:40f0:8", ["const:4bcc10:8", "const:4:8"]]
- 004bcc10 ["CALLIND", null, ["register:0:8"]]
+ 004bcc50 ["COPY", "register:0:8", ["register:4050:8"]]
+ 004bcc50 ["INT_ADD", "register:40f0:8", ["const:4bcc50:8", "const:4:8"]]
+ 004bcc50 ["CALLIND", null, ["register:0:8"]]
- 004bcc10 bytes 40013fd6
+ 004bcc50 bytes 40013fd6
- 004bcc50 ["INT_ADD", "register:40f0:8", ["const:4bcc50:8", "const:4:8"]]
- 004bcc50 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004bcc90 ["INT_ADD", "register:40f0:8", ["const:4bcc90:8", "const:4:8"]]
+ 004bcc90 ["CALL", null, ["callee:00c57fe0:8"]]
- 004bcc50 bytes b06c1e94
+ 004bcc90 bytes d46c1e94
- 004bcb8c ["COPY", "register:0:8", ["register:4040:8"]]
- 004bcb8c ["INT_ADD", "register:40f0:8", ["const:4bcb8c:8", "const:4:8"]]
- 004bcb8c ["CALLIND", null, ["register:0:8"]]
+ 004bcbcc ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bcbcc ["INT_ADD", "register:40f0:8", ["const:4bcbcc:8", "const:4:8"]]
+ 004bcbcc ["CALLIND", null, ["register:0:8"]]
- 004bcb8c bytes 00013fd6
+ 004bcbcc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97472bf957b88c28dc99a205c753961b"></a>

### [`004bcca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bcca8.md) → [`004bcce8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bcce8.md) _ZNK5Botan14CBC_Encryption13output_lengthEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58650.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58720.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 84.00% / 新版 84.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bcd28",
      "incomplete_value": false,
      "site": "004bcd48",
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
            "const:72:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bcce8",
      "incomplete_value": false,
      "site": "004bcd08",
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
            "const:bf:8"
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
      "definition_site": "004bcd30",
      "incomplete_value": false,
      "site": "004bcd48",
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
            "const:561:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bccf0",
      "incomplete_value": false,
      "site": "004bcd08",
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
            "const:5bd:8"
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
      "definition_site": "004bcd38",
      "incomplete_value": false,
      "site": "004bcd48",
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
            "const:2e5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bccf8",
      "incomplete_value": false,
      "site": "004bcd08",
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
            "const:2a5:8"
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
      "004bcd28",
      "PARAM",
      [
        "storage",
        "002a20bf",
        null,
        "string"
      ]
    ],
    [
      "004bcd30",
      "PARAM",
      [
        "storage",
        "002ab5bd",
        null,
        "string"
      ]
    ],
    [
      "004bcd38",
      "PARAM",
      [
        "storage",
        "002b82a5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bcd28",
      "PARAM",
      [
        "storage",
        "002a2072",
        null,
        "string"
      ]
    ],
    [
      "004bcd30",
      "PARAM",
      [
        "storage",
        "002ab561",
        null,
        "string"
      ]
    ],
    [
      "004bcd38",
      "PARAM",
      [
        "storage",
        "002b82e5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bcd08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bcca8.md#insn-004bcd08) · [`004bcce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bcca8.md#insn-004bcce8) · [`004bccf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bcca8.md#insn-004bccf0)
- 新版 [`004bcd48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bcce8.md#insn-004bcd48) · [`004bcd28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bcce8.md#insn-004bcd28) · [`004bcd30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bcce8.md#insn-004bcd30)

~~~diff
- 004bcd08 ["INT_ADD", "register:40f0:8", ["const:4bcd08:8", "const:4:8"]]
- 004bcd08 ["CALL", null, ["callee:00c58720:8"]]
+ 004bcd48 ["INT_ADD", "register:40f0:8", ["const:4bcd48:8", "const:4:8"]]
+ 004bcd48 ["CALL", null, ["callee:00c58720:8"]]
- 004bcd08 bytes 526e1e94
+ 004bcd48 bytes 766e1e94
- 004bcce8 ["COPY", "tmp:0:8", ["const:bf:8"]]
- 004bcce8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004bcce8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004bcce8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004bcd28 ["COPY", "tmp:0:8", ["const:72:8"]]
+ 004bcd28 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004bcd28 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004bcd28 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004bcce8 bytes 00fc0291
+ 004bcd28 bytes 00c80191
- 004bccf0 ["COPY", "tmp:0:8", ["const:5bd:8"]]
- 004bccf0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004bccf0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004bccf0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004bcd30 ["COPY", "tmp:0:8", ["const:561:8"]]
+ 004bcd30 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004bcd30 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004bcd30 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004bccf0 bytes 21f41691
+ 004bcd30 bytes 21841591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbe8d67aa45ccc3a8b4fe7d18de3742b"></a>

### [`004bcd0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bcd0c.md) → [`004bcd4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bcd4c.md) _ZN5Botan14CBC_Encryption7processEPhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00543858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543858.md) [`00c58650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58650.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00543898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543898.md) [`00c58720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58720.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.42% / 新版 97.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bcf94",
      "incomplete_value": false,
      "site": "004bcfb4",
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
            "const:bc4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bcf54",
      "incomplete_value": false,
      "site": "004bcf74",
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
            "const:c20:8"
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
      "definition_site": "004bcf9c",
      "incomplete_value": false,
      "site": "004bcfb4",
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
            "const:fe6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bcf5c",
      "incomplete_value": false,
      "site": "004bcf74",
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
            "const:33:8"
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
      "definition_site": "004bcfa4",
      "incomplete_value": false,
      "site": "004bcfb4",
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
            "const:d3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bcf64",
      "incomplete_value": false,
      "site": "004bcf74",
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
            "const:120:8"
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
      "004bcf94",
      "PARAM",
      [
        "storage",
        "002a8c20",
        null,
        "string"
      ]
    ],
    [
      "004bcf9c",
      "PARAM",
      [
        "storage",
        "002a0033",
        null,
        "string"
      ]
    ],
    [
      "004bcfa4",
      "PARAM",
      [
        "storage",
        "002a4120",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bcf94",
      "PARAM",
      [
        "storage",
        "002a8bc4",
        null,
        "string"
      ]
    ],
    [
      "004bcf9c",
      "PARAM",
      [
        "storage",
        "0029ffe6",
        null,
        "string"
      ]
    ],
    [
      "004bcfa4",
      "PARAM",
      [
        "storage",
        "002a40d3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bcf74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bcd0c.md#insn-004bcf74) · [`004bcdec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bcd0c.md#insn-004bcdec) · [`004bce08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bcd0c.md#insn-004bce08)
- 新版 [`004bcfb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bcd4c.md#insn-004bcfb4) · [`004bce2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bcd4c.md#insn-004bce2c) · [`004bce48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bcd4c.md#insn-004bce48)

~~~diff
- 004bcf74 ["INT_ADD", "register:40f0:8", ["const:4bcf74:8", "const:4:8"]]
- 004bcf74 ["CALL", null, ["callee:00c58720:8"]]
+ 004bcfb4 ["INT_ADD", "register:40f0:8", ["const:4bcfb4:8", "const:4:8"]]
+ 004bcfb4 ["CALL", null, ["callee:00c58720:8"]]
- 004bcf74 bytes b76d1e94
+ 004bcfb4 bytes db6d1e94
- 004bcdec ["COPY", "register:0:8", ["register:4040:8"]]
- 004bcdec ["INT_ADD", "register:40f0:8", ["const:4bcdec:8", "const:4:8"]]
- 004bcdec ["CALLIND", null, ["register:0:8"]]
+ 004bce2c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bce2c ["INT_ADD", "register:40f0:8", ["const:4bce2c:8", "const:4:8"]]
+ 004bce2c ["CALLIND", null, ["register:0:8"]]
- 004bcdec bytes 00013fd6
+ 004bce2c bytes 00013fd6
- 004bce08 ["INT_ADD", "register:40f0:8", ["const:4bce08:8", "const:4:8"]]
- 004bce08 ["CALL", null, ["callee:00543898:8"]]
+ 004bce48 ["INT_ADD", "register:40f0:8", ["const:4bce48:8", "const:4:8"]]
+ 004bce48 ["CALL", null, ["callee:00543898:8"]]
- 004bce08 bytes 941a0294
+ 004bce48 bytes 941a0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fec7480d772153e33dffef2d99b63d1"></a>

### [`004bcf78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bcf78.md) → [`004bcfb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bcfb8.md) _ZN5Botan14CBC_Encryption6finishERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 0件  · 呼出先 8件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.34% / 新版 90.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 14件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bd0dc",
      "incomplete_value": false,
      "site": "004bd0fc",
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
            "const:709:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bd09c",
      "incomplete_value": false,
      "site": "004bd0bc",
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
            "const:765:8"
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
      "definition_site": "004bd0e4",
      "incomplete_value": false,
      "site": "004bd0fc",
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
            "const:d4e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bd0a4",
      "incomplete_value": false,
      "site": "004bd0bc",
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
            "const:d1d:8"
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
      "definition_site": "004bd0ec",
      "incomplete_value": false,
      "site": "004bd0fc",
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
            "const:1f9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bd0ac",
      "incomplete_value": false,
      "site": "004bd0bc",
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
            "const:24d:8"
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
      "004bd0dc",
      "PARAM",
      [
        "storage",
        "002ad765",
        null,
        "string"
      ]
    ],
    [
      "004bd0e4",
      "PARAM",
      [
        "storage",
        "002b4d1d",
        null,
        "string"
      ]
    ],
    [
      "004bd0ec",
      "PARAM",
      [
        "storage",
        "002ba24d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bd0dc",
      "PARAM",
      [
        "storage",
        "002ad709",
        null,
        "string"
      ]
    ],
    [
      "004bd0e4",
      "PARAM",
      [
        "storage",
        "002b4d4e",
        null,
        "string"
      ]
    ],
    [
      "004bd0ec",
      "PARAM",
      [
        "storage",
        "002ba1f9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bd0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bcf78.md#insn-004bd0b4) · [`004bd0bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bcf78.md#insn-004bd0bc) · [`004bd0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bcf78.md#insn-004bd0e8)
- 新版 [`004bd0f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bcfb8.md#insn-004bd0f4) · [`004bd0fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bcfb8.md#insn-004bd0fc) · [`004bd128`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bcfb8.md#insn-004bd128)

~~~diff
- 004bd0b4 ["COPY", "tmp:0:8", ["const:dcb:8"]]
- 004bd0b4 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 004bd0b4 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 004bd0b4 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 004bd0f4 ["COPY", "tmp:0:8", ["const:973:8"]]
+ 004bd0f4 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 004bd0f4 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 004bd0f4 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 004bd0b4 bytes 632c3791
+ 004bd0f4 bytes 63cc2591
- 004bd0bc ["INT_ADD", "register:40f0:8", ["const:4bd0bc:8", "const:4:8"]]
- 004bd0bc ["CALL", null, ["callee:00c58720:8"]]
+ 004bd0fc ["INT_ADD", "register:40f0:8", ["const:4bd0fc:8", "const:4:8"]]
+ 004bd0fc ["CALL", null, ["callee:00c58720:8"]]
- 004bd0bc bytes 656d1e94
+ 004bd0fc bytes 896d1e94
- 004bd0e8 ["COPY", "register:4018:8", ["const:2a9000:8"]]
+ 004bd128 ["COPY", "register:4018:8", ["const:2a8000:8"]]
- 004bd0e8 bytes 63efff90
+ 004bd128 bytes 43effff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d081af23a3b33a5779f778a1c1a5741"></a>

### [`004bd258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bd/004bd258.md) → [`004bd298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bd/004bd298.md) _ZN5Botan14CTS_Encryption6finishERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 13件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`005402a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005402a4.md) [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)
- 新版 呼出元 0件  · 呼出先 13件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`005402e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/005402e4.md) [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.19% / 新版 95.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 14件

アドレスに依存する影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004bd550",
      "incomplete_value": true,
      "site": "004bd550",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004bd510",
      "incomplete_value": true,
      "site": "004bd510",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 10,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bd610",
      "incomplete_value": false,
      "site": "004bd630",
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
            "const:709:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bd5d0",
      "incomplete_value": false,
      "site": "004bd5f0",
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
            "const:765:8"
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
      "definition_site": "004bd618",
      "incomplete_value": false,
      "site": "004bd630",
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
            "const:d4e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bd5d8",
      "incomplete_value": false,
      "site": "004bd5f0",
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
            "const:d1d:8"
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
      "004bd540",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004bd610",
      "PARAM",
      [
        "storage",
        "002ad765",
        null,
        "string"
      ]
    ],
    [
      "004bd618",
      "PARAM",
      [
        "storage",
        "002b4d1d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bd540",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "004bd610",
      "PARAM",
      [
        "storage",
        "002ad709",
        null,
        "string"
      ]
    ],
    [
      "004bd618",
      "PARAM",
      [
        "storage",
        "002b4d4e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bd510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bd/004bd258.md#insn-004bd510) · [`004bd5d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bd/004bd258.md#insn-004bd5d8) · [`004bd5f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bd/004bd258.md#insn-004bd5f0)
- 新版 [`004bd550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bd/004bd298.md#insn-004bd550) · [`004bd618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bd/004bd298.md#insn-004bd618) · [`004bd630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bd/004bd298.md#insn-004bd630)

~~~diff
- 004bd510 ["COPY", "register:0:8", ["register:4048:8"]]
- 004bd510 ["INT_ADD", "register:40f0:8", ["const:4bd510:8", "const:4:8"]]
- 004bd510 ["CALLIND", null, ["register:0:8"]]
+ 004bd550 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004bd550 ["INT_ADD", "register:40f0:8", ["const:4bd550:8", "const:4:8"]]
+ 004bd550 ["CALLIND", null, ["register:0:8"]]
- 004bd510 bytes 20013fd6
+ 004bd550 bytes 20013fd6
- 004bd5d8 ["COPY", "tmp:0:8", ["const:d1d:8"]]
- 004bd5d8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004bd5d8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004bd5d8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004bd618 ["COPY", "tmp:0:8", ["const:d4e:8"]]
+ 004bd618 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004bd618 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004bd618 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004bd5d8 bytes 21743491
+ 004bd618 bytes 21383591
- 004bd5f0 ["INT_ADD", "register:40f0:8", ["const:4bd5f0:8", "const:4:8"]]
- 004bd5f0 ["CALL", null, ["callee:00c58720:8"]]
+ 004bd630 ["INT_ADD", "register:40f0:8", ["const:4bd630:8", "const:4:8"]]
+ 004bd630 ["CALL", null, ["callee:00c58720:8"]]
- 004bd5f0 bytes 186c1e94
+ 004bd630 bytes 3c6c1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0f6e29958c70dd8f1d7a981d8488cb0"></a>

### [`004bd77c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bd/004bd77c.md) → [`004bd7bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bd/004bd7bc.md) _ZN5Botan14CBC_Decryption7processEPhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58650.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c58720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58720.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.32% / 新版 97.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bd9ec",
      "incomplete_value": false,
      "site": "004bda0c",
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
            "const:bc4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bd9ac",
      "incomplete_value": false,
      "site": "004bd9cc",
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
            "const:c20:8"
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
      "definition_site": "004bd9f4",
      "incomplete_value": false,
      "site": "004bda0c",
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
            "const:acb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bd9b4",
      "incomplete_value": false,
      "site": "004bd9cc",
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
            "const:b27:8"
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
      "definition_site": "004bd9fc",
      "incomplete_value": false,
      "site": "004bda0c",
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
            "const:d3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bd9bc",
      "incomplete_value": false,
      "site": "004bd9cc",
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
            "const:120:8"
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
      "004bd9ec",
      "PARAM",
      [
        "storage",
        "002a8c20",
        null,
        "string"
      ]
    ],
    [
      "004bd9f4",
      "PARAM",
      [
        "storage",
        "002b0b27",
        null,
        "string"
      ]
    ],
    [
      "004bd9fc",
      "PARAM",
      [
        "storage",
        "002a4120",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bd9ec",
      "PARAM",
      [
        "storage",
        "002a8bc4",
        null,
        "string"
      ]
    ],
    [
      "004bd9f4",
      "PARAM",
      [
        "storage",
        "002b0acb",
        null,
        "string"
      ]
    ],
    [
      "004bd9fc",
      "PARAM",
      [
        "storage",
        "002a40d3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bd9cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bd/004bd77c.md#insn-004bd9cc) · [`004bd814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bd/004bd77c.md#insn-004bd814) · [`004bd91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bd/004bd77c.md#insn-004bd91c)
- 新版 [`004bda0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bd/004bd7bc.md#insn-004bda0c) · [`004bd854`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bd/004bd7bc.md#insn-004bd854) · [`004bd95c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bd/004bd7bc.md#insn-004bd95c)

~~~diff
- 004bd9cc ["INT_ADD", "register:40f0:8", ["const:4bd9cc:8", "const:4:8"]]
- 004bd9cc ["CALL", null, ["callee:00c58720:8"]]
+ 004bda0c ["INT_ADD", "register:40f0:8", ["const:4bda0c:8", "const:4:8"]]
+ 004bda0c ["CALL", null, ["callee:00c58720:8"]]
- 004bd9cc bytes 216b1e94
+ 004bda0c bytes 456b1e94
- 004bd814 ["COPY", "register:0:8", ["register:4040:8"]]
- 004bd814 ["INT_ADD", "register:40f0:8", ["const:4bd814:8", "const:4:8"]]
- 004bd814 ["CALLIND", null, ["register:0:8"]]
+ 004bd854 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bd854 ["INT_ADD", "register:40f0:8", ["const:4bd854:8", "const:4:8"]]
+ 004bd854 ["CALLIND", null, ["register:0:8"]]
- 004bd814 bytes 00013fd6
+ 004bd854 bytes 00013fd6
- 004bd91c ["INT_ADD", "register:40f0:8", ["const:4bd91c:8", "const:4:8"]]
- 004bd91c ["CALL", null, ["callee:00c58010:8"]]
+ 004bd95c ["INT_ADD", "register:40f0:8", ["const:4bd95c:8", "const:4:8"]]
+ 004bd95c ["CALL", null, ["callee:00c58010:8"]]
- 004bd91c bytes 89691e94
+ 004bd95c bytes ad691e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b19ee7e8fe06cb7e9dd27f480fefe672"></a>

### [`004bd9d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bd/004bd9d0.md) → [`004bda10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bd/004bda10.md) _ZN5Botan14CBC_Decryption6finishERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.30% / 新版 94.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bdbe0",
      "incomplete_value": false,
      "site": "004bdbe8",
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
            "const:93:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bdba0",
      "incomplete_value": false,
      "site": "004bdba8",
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
            "const:53:8"
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
      "definition_site": "004bdc30",
      "incomplete_value": true,
      "site": "004bdc3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004bdbf0",
      "incomplete_value": true,
      "site": "004bdbfc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bdc2c",
      "incomplete_value": false,
      "site": "004bdc3c",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004bdbec",
      "incomplete_value": false,
      "site": "004bdbfc",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "ordinal": 10,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004bdbe0",
      "PARAM",
      [
        "storage",
        "002c1053",
        null,
        "string"
      ]
    ],
    [
      "004bdc2c",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004bdc30",
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
      "004bdbe0",
      "PARAM",
      [
        "storage",
        "002c1093",
        null,
        "string"
      ]
    ],
    [
      "004bdc2c",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004bdc30",
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

- 旧版 [`004bdba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bd/004bd9d0.md#insn-004bdba8) · [`004bdbfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bd/004bd9d0.md#insn-004bdbfc) · [`004bdc30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bd/004bd9d0.md#insn-004bdc30)
- 新版 [`004bdbe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bd/004bda10.md#insn-004bdbe8) · [`004bdc3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bd/004bda10.md#insn-004bdc3c) · [`004bdc70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bd/004bda10.md#insn-004bdc70)

~~~diff
- 004bdba8 ["INT_ADD", "register:40f0:8", ["const:4bdba8:8", "const:4:8"]]
- 004bdba8 ["CALL", null, ["callee:00c58040:8"]]
+ 004bdbe8 ["INT_ADD", "register:40f0:8", ["const:4bdbe8:8", "const:4:8"]]
+ 004bdbe8 ["CALL", null, ["callee:00c58040:8"]]
- 004bdba8 bytes f2681e94
+ 004bdbe8 bytes 16691e94
- 004bdbfc ["INT_ADD", "register:40f0:8", ["const:4bdbfc:8", "const:4:8"]]
- 004bdbfc ["CALL", null, ["callee:00c57fe0:8"]]
+ 004bdc3c ["INT_ADD", "register:40f0:8", ["const:4bdc3c:8", "const:4:8"]]
+ 004bdc3c ["CALL", null, ["callee:00c57fe0:8"]]
- 004bdbfc bytes c5681e94
+ 004bdc3c bytes e9681e94
- 004bdc30 ["COPY", "tmp:0:8", ["const:c67:8"]]
- 004bdc30 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 004bdc30 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 004bdc30 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 004bdc70 ["COPY", "tmp:0:8", ["const:cc2:8"]]
+ 004bdc70 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 004bdc70 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 004bdc70 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 004bdc30 bytes 639c3191
+ 004bdc70 bytes 63083391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aabbf0eab19b8d1a8d779b185bc442cc"></a>

### [`004bdddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bd/004bdddc.md) → [`004bde1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bd/004bde1c.md) _ZN5Botan14CTS_Decryption6finishERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 13件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`005402a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005402a4.md) [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)
- 新版 呼出元 0件  · 呼出先 13件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`005402e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/005402e4.md) [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)

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
      "definition_site": "004be1a0",
      "incomplete_value": true,
      "site": "004be1a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004be160",
      "incomplete_value": true,
      "site": "004be160",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 9,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004be26c",
      "incomplete_value": false,
      "site": "004be28c",
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
            "const:709:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004be22c",
      "incomplete_value": false,
      "site": "004be24c",
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
            "const:765:8"
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
      "definition_site": "004be274",
      "incomplete_value": false,
      "site": "004be28c",
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
            "const:d4e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004be234",
      "incomplete_value": false,
      "site": "004be24c",
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
            "const:d1d:8"
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
      "004be190",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004be26c",
      "PARAM",
      [
        "storage",
        "002ad765",
        null,
        "string"
      ]
    ],
    [
      "004be274",
      "PARAM",
      [
        "storage",
        "002b4d1d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004be190",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "004be26c",
      "PARAM",
      [
        "storage",
        "002ad709",
        null,
        "string"
      ]
    ],
    [
      "004be274",
      "PARAM",
      [
        "storage",
        "002b4d4e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004be160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bd/004bdddc.md#insn-004be160) · [`004be234`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bd/004bdddc.md#insn-004be234) · [`004be24c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bd/004bdddc.md#insn-004be24c)
- 新版 [`004be1a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bd/004bde1c.md#insn-004be1a0) · [`004be274`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bd/004bde1c.md#insn-004be274) · [`004be28c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bd/004bde1c.md#insn-004be28c)

~~~diff
- 004be160 ["COPY", "register:0:8", ["register:4048:8"]]
- 004be160 ["INT_ADD", "register:40f0:8", ["const:4be160:8", "const:4:8"]]
- 004be160 ["CALLIND", null, ["register:0:8"]]
+ 004be1a0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004be1a0 ["INT_ADD", "register:40f0:8", ["const:4be1a0:8", "const:4:8"]]
+ 004be1a0 ["CALLIND", null, ["register:0:8"]]
- 004be160 bytes 20013fd6
+ 004be1a0 bytes 20013fd6
- 004be234 ["COPY", "tmp:0:8", ["const:d1d:8"]]
- 004be234 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004be234 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004be234 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004be274 ["COPY", "tmp:0:8", ["const:d4e:8"]]
+ 004be274 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004be274 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004be274 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004be234 bytes 21743491
+ 004be274 bytes 21383591
- 004be24c ["INT_ADD", "register:40f0:8", ["const:4be24c:8", "const:4:8"]]
- 004be24c ["CALL", null, ["callee:00c58720:8"]]
+ 004be28c ["INT_ADD", "register:40f0:8", ["const:4be28c:8", "const:4:8"]]
+ 004be28c ["CALL", null, ["callee:00c58720:8"]]
- 004be24c bytes 01691e94
+ 004be28c bytes 25691e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4fbcee7dd7b11bb6eae0c96096989c2c"></a>

### [`004be424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004be/004be424.md) → [`004be464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004be464.md) _ZN5Botan5CPUID9to_stringEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58da0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58da0.md) · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00440f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00c58e70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58e70.md) · 呼出先 8件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00440f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f9c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

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
      "definition_site": "004be814",
      "incomplete_value": true,
      "site": "004be814",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004be7d4",
      "incomplete_value": true,
      "site": "004be7d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:998:8"
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
      "definition_site": "004be8d4",
      "incomplete_value": true,
      "site": "004be8d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004be894",
      "incomplete_value": true,
      "site": "004be894",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:998:8"
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
      "definition_site": "004be4a8",
      "incomplete_value": true,
      "site": "004be4a8",
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
      "definition_site": "004be468",
      "incomplete_value": true,
      "site": "004be468",
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
      "004be494",
      "READ",
      [
        "storage",
        "00c9ad18",
        null,
        "pointer"
      ]
    ],
    [
      "004be49c",
      "READ",
      [
        "storage",
        "00ca5238",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ],
    [
      "004be5b4",
      "READ",
      [
        "storage",
        "00ca5238",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004be494",
      "READ",
      [
        "storage",
        "00c9ade8",
        null,
        "pointer"
      ]
    ],
    [
      "004be49c",
      "READ",
      [
        "storage",
        "00ca5338",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ],
    [
      "004be5b4",
      "READ",
      [
        "storage",
        "00ca5338",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004be854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004be/004be424.md#insn-004be854) · [`004be454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004be/004be424.md#insn-004be454) · [`004be488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004be/004be424.md#insn-004be488)
- 新版 [`004be894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004be464.md#insn-004be894) · [`004be494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004be464.md#insn-004be494) · [`004be4c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004be464.md#insn-004be4c8)

~~~diff
- 004be854 ["INT_ADD", "register:40f0:8", ["const:4be854:8", "const:4:8"]]
- 004be854 ["CALL", null, ["callee:00c57f60:8"]]
+ 004be894 ["INT_ADD", "register:40f0:8", ["const:4be894:8", "const:4:8"]]
+ 004be894 ["CALL", null, ["callee:00c57f60:8"]]
- 004be854 bytes 8f651e94
+ 004be894 bytes b3651e94
- 004be454 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:d18:8"]]
- 004be454 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 004be494 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:de8:8"]]
+ 004be494 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 004be454 bytes 188f46f9
+ 004be494 bytes 18f746f9
- 004be488 ["INT_ADD", "register:40f0:8", ["const:4be488:8", "const:4:8"]]
- 004be488 ["CALL", null, ["callee:00c57f60:8"]]
+ 004be4c8 ["INT_ADD", "register:40f0:8", ["const:4be4c8:8", "const:4:8"]]
+ 004be4c8 ["CALL", null, ["callee:00c57f60:8"]]
- 004be488 bytes 82661e94
+ 004be4c8 bytes a6661e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af31856286bb128235a7a6c92acccb9c"></a>

### [`004beb9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004be/004beb9c.md) → [`004bebdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004bebdc.md) _ZN5Botan5CPUID5printERNSt6__ndk113basic_ostreamIcNS1_11char_traitsIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`004594d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58da0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58da0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00459510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459510.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58e70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58e70.md)

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
      "definition_site": "004bebf8",
      "incomplete_value": false,
      "site": "004bec08",
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
            "const:56c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bebb8",
      "incomplete_value": false,
      "site": "004bebc8",
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
            "const:5c8:8"
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
      "definition_site": "004bec40",
      "incomplete_value": false,
      "site": "004bec48",
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
            "const:c11:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bec00",
      "incomplete_value": false,
      "site": "004bec08",
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
            "const:be0:8"
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
      "004bebf8",
      "PARAM",
      [
        "storage",
        "002a65c8",
        null,
        "string"
      ]
    ],
    [
      "004bec40",
      "PARAM",
      [
        "storage",
        "002b4be0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004bebf8",
      "PARAM",
      [
        "storage",
        "002a656c",
        null,
        "string"
      ]
    ],
    [
      "004bec40",
      "PARAM",
      [
        "storage",
        "002b4c11",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bebc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004be/004beb9c.md#insn-004bebc8) · [`004bec08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004be/004beb9c.md#insn-004bec08) · [`004bebb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004be/004beb9c.md#insn-004bebb8)
- 新版 [`004bec08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004bebdc.md#insn-004bec08) · [`004bec48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004bebdc.md#insn-004bec48) · [`004bebf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004bebdc.md#insn-004bebf8)

~~~diff
- 004bebc8 ["INT_ADD", "register:40f0:8", ["const:4bebc8:8", "const:4:8"]]
- 004bebc8 ["CALL", null, ["callee:00459510:8"]]
+ 004bec08 ["INT_ADD", "register:40f0:8", ["const:4bec08:8", "const:4:8"]]
+ 004bec08 ["CALL", null, ["callee:00459510:8"]]
- 004bebc8 bytes 426afe97
+ 004bec08 bytes 426afe97
- 004bec08 ["INT_ADD", "register:40f0:8", ["const:4bec08:8", "const:4:8"]]
- 004bec08 ["CALL", null, ["callee:00459510:8"]]
+ 004bec48 ["INT_ADD", "register:40f0:8", ["const:4bec48:8", "const:4:8"]]
+ 004bec48 ["CALL", null, ["callee:00459510:8"]]
- 004bec08 bytes 326afe97
+ 004bec48 bytes 326afe97
- 004bebb8 ["COPY", "tmp:0:8", ["const:5c8:8"]]
- 004bebb8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004bebb8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004bebb8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004bebf8 ["COPY", "tmp:0:8", ["const:56c:8"]]
+ 004bebf8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004bebf8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004bebf8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004bebb8 bytes 21201791
+ 004bebf8 bytes 21b01591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4532aa645b7213c11f2424a215bfd685"></a>

### [`004bec70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004be/004bec70.md) → [`004becb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004becb0.md) _ZN5Botan5CPUID10initializeEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "004becbc",
      "incomplete_value": true,
      "site": "004becbc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004bec7c",
      "incomplete_value": true,
      "site": "004bec7c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d18:8"
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
      "004becb8",
      "READ",
      [
        "storage",
        "00c9ad18",
        null,
        "pointer"
      ]
    ],
    [
      "004becbc",
      "WRITE",
      [
        "storage",
        "00ca5238",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004becb8",
      "READ",
      [
        "storage",
        "00c9ade8",
        null,
        "pointer"
      ]
    ],
    [
      "004becbc",
      "WRITE",
      [
        "storage",
        "00ca5338",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bec78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004be/004bec70.md#insn-004bec78)
- 新版 [`004becb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004becb0.md#insn-004becb8)

~~~diff
- 004bec78 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d18:8"]]
- 004bec78 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004becb8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:de8:8"]]
+ 004becb8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004bec78 bytes 088d46f9
+ 004becb8 bytes 08f546f9
~~~


<a id="compare-e011b82ec487d6ed82ed1ae4d26b335c"></a>

### [`004bef2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004be/004bef2c.md) → [`004bef6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004bef6c.md) _ZN5Botan8ECB_ModeC2EPNS_11BlockCipherEPNS_28BlockCipherModePaddingMethodE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58db0.md) · 呼出先 8件 [`004a684c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a684c.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`00c58e80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58e80.md) · 呼出先 8件 [`004a688c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a688c.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

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
      "definition_site": "004befa8",
      "incomplete_value": true,
      "site": "004befa8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bef68",
      "incomplete_value": true,
      "site": "004bef68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004bf028",
      "incomplete_value": false,
      "site": "004bf034",
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
            "const:333:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004befe8",
      "incomplete_value": false,
      "site": "004beff4",
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
            "const:387:8"
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
      "definition_site": "004bf054",
      "incomplete_value": false,
      "site": "004bf05c",
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
            "const:bba:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bf014",
      "incomplete_value": false,
      "site": "004bf01c",
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
            "const:b8b:8"
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
      "004bef94",
      "READ",
      [
        "storage",
        "00c9ae48",
        null,
        "pointer"
      ]
    ],
    [
      "004befa8",
      "DATA",
      [
        "storage",
        "00c664d8",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "004bf028",
      "PARAM",
      [
        "storage",
        "002bb387",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bef94",
      "READ",
      [
        "storage",
        "00c9af18",
        null,
        "pointer"
      ]
    ],
    [
      "004befa8",
      "DATA",
      [
        "storage",
        "00c665a8",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "004bf028",
      "PARAM",
      [
        "storage",
        "002bb333",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004beff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004be/004bef2c.md#insn-004beff4) · [`004bf01c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004be/004bef2c.md#insn-004bf01c) · [`004bf068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004be/004bef2c.md#insn-004bf068)
- 新版 [`004bf034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004bef6c.md#insn-004bf034) · [`004bf05c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004bef6c.md#insn-004bf05c) · [`004bf0a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004be/004bef6c.md#insn-004bf0a8)

~~~diff
- 004beff4 ["INT_ADD", "register:40f0:8", ["const:4beff4:8", "const:4:8"]]
- 004beff4 ["CALL", null, ["callee:00c58030:8"]]
+ 004bf034 ["INT_ADD", "register:40f0:8", ["const:4bf034:8", "const:4:8"]]
+ 004bf034 ["CALL", null, ["callee:00c58030:8"]]
- 004beff4 bytes db631e94
+ 004bf034 bytes ff631e94
- 004bf01c ["INT_ADD", "register:40f0:8", ["const:4bf01c:8", "const:4:8"]]
- 004bf01c ["CALL", null, ["callee:00c58040:8"]]
+ 004bf05c ["INT_ADD", "register:40f0:8", ["const:4bf05c:8", "const:4:8"]]
+ 004bf05c ["CALL", null, ["callee:00c58040:8"]]
- 004bf01c bytes d5631e94
+ 004bf05c bytes f9631e94
- 004bf068 ["INT_ADD", "register:40f0:8", ["const:4bf068:8", "const:4:8"]]
- 004bf068 ["CALL", null, ["callee:00c58040:8"]]
+ 004bf0a8 ["INT_ADD", "register:40f0:8", ["const:4bf0a8:8", "const:4:8"]]
+ 004bf0a8 ["CALL", null, ["callee:00c58040:8"]]
- 004bf068 bytes c2631e94
+ 004bf0a8 bytes e6631e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4420d7dc5170c5c20b76a2574e8642a7"></a>

### [`004bf238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bf238.md) → [`004bf278`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf278.md) _ZNK5Botan8ECB_Mode4nameEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58dc0.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00c58e90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58e90.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md)

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
      "definition_site": "004bf2b8",
      "incomplete_value": false,
      "site": "004bf2c0",
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
            "const:57a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bf278",
      "incomplete_value": false,
      "site": "004bf280",
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
            "const:5d6:8"
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
      "004bf2b8",
      "PARAM",
      [
        "storage",
        "002a65d6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bf2b8",
      "PARAM",
      [
        "storage",
        "002a657a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bf280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bf238.md#insn-004bf280) · [`004bf270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bf238.md#insn-004bf270) · [`004bf278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bf238.md#insn-004bf278)
- 新版 [`004bf2c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf278.md#insn-004bf2c0) · [`004bf2b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf278.md#insn-004bf2b0) · [`004bf2b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf278.md#insn-004bf2b8)

~~~diff
- 004bf280 ["INT_ADD", "register:40f0:8", ["const:4bf280:8", "const:4:8"]]
- 004bf280 ["CALL", null, ["callee:00c58040:8"]]
+ 004bf2c0 ["INT_ADD", "register:40f0:8", ["const:4bf2c0:8", "const:4:8"]]
+ 004bf2c0 ["CALL", null, ["callee:00c58040:8"]]
- 004bf280 bytes 3c631e94
+ 004bf2c0 bytes 60631e94
- 004bf270 ["COPY", "register:0:8", ["register:4048:8"]]
- 004bf270 ["INT_ADD", "register:40f0:8", ["const:4bf270:8", "const:4:8"]]
- 004bf270 ["CALLIND", null, ["register:0:8"]]
+ 004bf2b0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004bf2b0 ["INT_ADD", "register:40f0:8", ["const:4bf2b0:8", "const:4:8"]]
+ 004bf2b0 ["CALLIND", null, ["register:0:8"]]
- 004bf270 bytes 20013fd6
+ 004bf2b0 bytes 20013fd6
- 004bf278 ["COPY", "tmp:0:8", ["const:5d6:8"]]
- 004bf278 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004bf278 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004bf278 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004bf2b8 ["COPY", "tmp:0:8", ["const:57a:8"]]
+ 004bf2b8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004bf2b8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004bf2b8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004bf278 bytes 21581791
+ 004bf2b8 bytes 21e81591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66275826fb1a6bece33a16c36b43b0db"></a>

### [`004bf44c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bf44c.md) → [`004bf48c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf48c.md) _ZN5Botan8ECB_Mode9start_msgEPKhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c58d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58d90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c58e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58e60.md)

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
      "definition_site": "004bf534",
      "incomplete_value": true,
      "site": "004bf540",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bf4f4",
      "incomplete_value": true,
      "site": "004bf500",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e40:8"
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
      "definition_site": "004bf530",
      "incomplete_value": false,
      "site": "004bf540",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004bf4f0",
      "incomplete_value": false,
      "site": "004bf500",
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
      "004bf530",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004bf534",
      "READ",
      [
        "storage",
        "00c9ae40",
        null,
        "pointer"
      ]
    ],
    [
      "004bf534",
      "PARAM",
      [
        "storage",
        "00c664b0",
        "_ZTIN5Botan17Invalid_IV_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004bf530",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004bf534",
      "READ",
      [
        "storage",
        "00c9af10",
        null,
        "pointer"
      ]
    ],
    [
      "004bf534",
      "PARAM",
      [
        "storage",
        "00c66580",
        "_ZTIN5Botan17Invalid_IV_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bf500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bf44c.md#insn-004bf500) · [`004bf4a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bf44c.md#insn-004bf4a4) · [`004bf4bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bf44c.md#insn-004bf4bc)
- 新版 [`004bf540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf48c.md#insn-004bf540) · [`004bf4e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf48c.md#insn-004bf4e4) · [`004bf4fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf48c.md#insn-004bf4fc)

~~~diff
- 004bf500 ["INT_ADD", "register:40f0:8", ["const:4bf500:8", "const:4:8"]]
- 004bf500 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004bf540 ["INT_ADD", "register:40f0:8", ["const:4bf540:8", "const:4:8"]]
+ 004bf540 ["CALL", null, ["callee:00c57fe0:8"]]
- 004bf500 bytes 84621e94
+ 004bf540 bytes a8621e94
- 004bf4a4 ["INT_ADD", "register:40f0:8", ["const:4bf4a4:8", "const:4:8"]]
- 004bf4a4 ["CALL", null, ["callee:00c57fc0:8"]]
+ 004bf4e4 ["INT_ADD", "register:40f0:8", ["const:4bf4e4:8", "const:4:8"]]
+ 004bf4e4 ["CALL", null, ["callee:00c57fc0:8"]]
- 004bf4a4 bytes 93621e94
+ 004bf4e4 bytes b7621e94
- 004bf4bc ["COPY", "register:0:8", ["register:4048:8"]]
- 004bf4bc ["INT_ADD", "register:40f0:8", ["const:4bf4bc:8", "const:4:8"]]
- 004bf4bc ["CALLIND", null, ["register:0:8"]]
+ 004bf4fc ["COPY", "register:0:8", ["register:4048:8"]]
+ 004bf4fc ["INT_ADD", "register:40f0:8", ["const:4bf4fc:8", "const:4:8"]]
+ 004bf4fc ["CALLIND", null, ["register:0:8"]]
- 004bf4bc bytes 20013fd6
+ 004bf4fc bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2716dc1acd9062580ea8df614286c6ca"></a>

### [`004bf55c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bf55c.md) → [`004bf59c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf59c.md) _ZNK5Botan14ECB_Encryption13output_lengthEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58650.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58720.md)

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
      "definition_site": "004bf5ec",
      "incomplete_value": false,
      "site": "004bf60c",
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
            "const:72:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bf5ac",
      "incomplete_value": false,
      "site": "004bf5cc",
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
      "definition_site": "004bf5f4",
      "incomplete_value": false,
      "site": "004bf60c",
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
            "const:561:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bf5b4",
      "incomplete_value": false,
      "site": "004bf5cc",
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
            "const:5bd:8"
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
      "definition_site": "004bf5fc",
      "incomplete_value": false,
      "site": "004bf60c",
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
            "const:2e5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bf5bc",
      "incomplete_value": false,
      "site": "004bf5cc",
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
            "const:2a5:8"
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
      "004bf5ec",
      "PARAM",
      [
        "storage",
        "002a20bf",
        null,
        "string"
      ]
    ],
    [
      "004bf5f4",
      "PARAM",
      [
        "storage",
        "002ab5bd",
        null,
        "string"
      ]
    ],
    [
      "004bf5fc",
      "PARAM",
      [
        "storage",
        "002b82a5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bf5ec",
      "PARAM",
      [
        "storage",
        "002a2072",
        null,
        "string"
      ]
    ],
    [
      "004bf5f4",
      "PARAM",
      [
        "storage",
        "002ab561",
        null,
        "string"
      ]
    ],
    [
      "004bf5fc",
      "PARAM",
      [
        "storage",
        "002b82e5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bf5cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bf55c.md#insn-004bf5cc) · [`004bf578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bf55c.md#insn-004bf578) · [`004bf5ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bf55c.md#insn-004bf5ac)
- 新版 [`004bf60c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf59c.md#insn-004bf60c) · [`004bf5b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf59c.md#insn-004bf5b8) · [`004bf5ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf59c.md#insn-004bf5ec)

~~~diff
- 004bf5cc ["INT_ADD", "register:40f0:8", ["const:4bf5cc:8", "const:4:8"]]
- 004bf5cc ["CALL", null, ["callee:00c58720:8"]]
+ 004bf60c ["INT_ADD", "register:40f0:8", ["const:4bf60c:8", "const:4:8"]]
+ 004bf60c ["CALL", null, ["callee:00c58720:8"]]
- 004bf5cc bytes 21641e94
+ 004bf60c bytes 45641e94
- 004bf578 ["COPY", "register:0:8", ["register:4040:8"]]
- 004bf578 ["INT_ADD", "register:40f0:8", ["const:4bf578:8", "const:4:8"]]
- 004bf578 ["CALLIND", null, ["register:0:8"]]
+ 004bf5b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bf5b8 ["INT_ADD", "register:40f0:8", ["const:4bf5b8:8", "const:4:8"]]
+ 004bf5b8 ["CALLIND", null, ["register:0:8"]]
- 004bf578 bytes 00013fd6
+ 004bf5b8 bytes 00013fd6
- 004bf5ac ["COPY", "tmp:0:8", ["const:bf:8"]]
- 004bf5ac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004bf5ac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004bf5ac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004bf5ec ["COPY", "tmp:0:8", ["const:72:8"]]
+ 004bf5ec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004bf5ec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004bf5ec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004bf5ac bytes 00fc0291
+ 004bf5ec bytes 00c80191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ca7a119524167ac35ef8017a1bb4c4a"></a>

### [`004bf5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bf5d0.md) → [`004bf610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf610.md) _ZN5Botan14ECB_Encryption7processEPhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58650.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58720.md)

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
      "definition_site": "004bf678",
      "incomplete_value": false,
      "site": "004bf698",
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
            "const:bc4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bf638",
      "incomplete_value": false,
      "site": "004bf658",
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
            "const:c20:8"
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
      "definition_site": "004bf680",
      "incomplete_value": false,
      "site": "004bf698",
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
            "const:a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bf640",
      "incomplete_value": false,
      "site": "004bf658",
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
            "const:f5:8"
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
      "definition_site": "004bf688",
      "incomplete_value": false,
      "site": "004bf698",
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
            "const:d3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bf648",
      "incomplete_value": false,
      "site": "004bf658",
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
            "const:120:8"
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
      "004bf678",
      "PARAM",
      [
        "storage",
        "002a8c20",
        null,
        "string"
      ]
    ],
    [
      "004bf680",
      "PARAM",
      [
        "storage",
        "002a30f5",
        null,
        "string"
      ]
    ],
    [
      "004bf688",
      "PARAM",
      [
        "storage",
        "002a4120",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bf678",
      "PARAM",
      [
        "storage",
        "002a8bc4",
        null,
        "string"
      ]
    ],
    [
      "004bf680",
      "PARAM",
      [
        "storage",
        "002a30a8",
        null,
        "string"
      ]
    ],
    [
      "004bf688",
      "PARAM",
      [
        "storage",
        "002a40d3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bf658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bf5d0.md#insn-004bf658) · [`004bf5f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bf5d0.md#insn-004bf5f8) · [`004bf61c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bf5d0.md#insn-004bf61c)
- 新版 [`004bf698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf610.md#insn-004bf698) · [`004bf638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf610.md#insn-004bf638) · [`004bf65c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf610.md#insn-004bf65c)

~~~diff
- 004bf658 ["INT_ADD", "register:40f0:8", ["const:4bf658:8", "const:4:8"]]
- 004bf658 ["CALL", null, ["callee:00c58720:8"]]
+ 004bf698 ["INT_ADD", "register:40f0:8", ["const:4bf698:8", "const:4:8"]]
+ 004bf698 ["CALL", null, ["callee:00c58720:8"]]
- 004bf658 bytes fe631e94
+ 004bf698 bytes 22641e94
- 004bf5f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004bf5f8 ["INT_ADD", "register:40f0:8", ["const:4bf5f8:8", "const:4:8"]]
- 004bf5f8 ["CALLIND", null, ["register:0:8"]]
+ 004bf638 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bf638 ["INT_ADD", "register:40f0:8", ["const:4bf638:8", "const:4:8"]]
+ 004bf638 ["CALLIND", null, ["register:0:8"]]
- 004bf5f8 bytes 00013fd6
+ 004bf638 bytes 00013fd6
- 004bf61c ["COPY", "register:0:8", ["register:4040:8"]]
- 004bf61c ["INT_ADD", "register:40f0:8", ["const:4bf61c:8", "const:4:8"]]
- 004bf61c ["CALLIND", null, ["register:0:8"]]
+ 004bf65c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bf65c ["INT_ADD", "register:40f0:8", ["const:4bf65c:8", "const:4:8"]]
+ 004bf65c ["CALLIND", null, ["register:0:8"]]
- 004bf61c bytes 00013fd6
+ 004bf65c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e852585d0f3b104eb2d739592861b8d"></a>

### [`004bf65c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bf65c.md) → [`004bf69c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf69c.md) _ZN5Botan14ECB_Encryption6finishERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 0件  · 呼出先 9件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

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
      "definition_site": "004bf7c8",
      "incomplete_value": false,
      "site": "004bf7e8",
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
            "const:709:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bf788",
      "incomplete_value": false,
      "site": "004bf7a8",
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
            "const:765:8"
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
      "definition_site": "004bf7d0",
      "incomplete_value": false,
      "site": "004bf7e8",
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
            "const:d4e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bf790",
      "incomplete_value": false,
      "site": "004bf7a8",
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
            "const:d1d:8"
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
      "definition_site": "004bf7d8",
      "incomplete_value": false,
      "site": "004bf7e8",
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
            "const:1f9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bf798",
      "incomplete_value": false,
      "site": "004bf7a8",
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
            "const:24d:8"
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
      "004bf7c8",
      "PARAM",
      [
        "storage",
        "002ad765",
        null,
        "string"
      ]
    ],
    [
      "004bf7d0",
      "PARAM",
      [
        "storage",
        "002b4d1d",
        null,
        "string"
      ]
    ],
    [
      "004bf7d8",
      "PARAM",
      [
        "storage",
        "002ba24d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bf7c8",
      "PARAM",
      [
        "storage",
        "002ad709",
        null,
        "string"
      ]
    ],
    [
      "004bf7d0",
      "PARAM",
      [
        "storage",
        "002b4d4e",
        null,
        "string"
      ]
    ],
    [
      "004bf7d8",
      "PARAM",
      [
        "storage",
        "002ba1f9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bf7a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bf65c.md#insn-004bf7a8) · [`004bf7d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bf65c.md#insn-004bf7d4) · [`004bf828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bf65c.md#insn-004bf828)
- 新版 [`004bf7e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf69c.md#insn-004bf7e8) · [`004bf814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf69c.md#insn-004bf814) · [`004bf868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf69c.md#insn-004bf868)

~~~diff
- 004bf7a8 ["INT_ADD", "register:40f0:8", ["const:4bf7a8:8", "const:4:8"]]
- 004bf7a8 ["CALL", null, ["callee:00c58720:8"]]
+ 004bf7e8 ["INT_ADD", "register:40f0:8", ["const:4bf7e8:8", "const:4:8"]]
+ 004bf7e8 ["CALL", null, ["callee:00c58720:8"]]
- 004bf7a8 bytes aa631e94
+ 004bf7e8 bytes ce631e94
- 004bf7d4 ["INT_ADD", "register:40f0:8", ["const:4bf7d4:8", "const:4:8"]]
- 004bf7d4 ["CALL", null, ["callee:00c58030:8"]]
+ 004bf814 ["INT_ADD", "register:40f0:8", ["const:4bf814:8", "const:4:8"]]
+ 004bf814 ["CALL", null, ["callee:00c58030:8"]]
- 004bf7d4 bytes e3611e94
+ 004bf814 bytes 07621e94
- 004bf828 ["INT_ADD", "register:40f0:8", ["const:4bf828:8", "const:4:8"]]
- 004bf828 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004bf868 ["INT_ADD", "register:40f0:8", ["const:4bf868:8", "const:4:8"]]
+ 004bf868 ["CALL", null, ["callee:00c57fe0:8"]]
- 004bf828 bytes ba611e94
+ 004bf868 bytes de611e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eca2c13057fcbceb27e1bf403c332629"></a>

### [`004bf8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bf8f0.md) → [`004bf930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf930.md) _ZN5Botan14ECB_Decryption7processEPhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58650.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58720.md)

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
      "definition_site": "004bf998",
      "incomplete_value": false,
      "site": "004bf9b8",
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
            "const:bc4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bf958",
      "incomplete_value": false,
      "site": "004bf978",
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
            "const:c20:8"
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
      "definition_site": "004bf9a0",
      "incomplete_value": false,
      "site": "004bf9b8",
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
            "const:acb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bf960",
      "incomplete_value": false,
      "site": "004bf978",
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
            "const:b27:8"
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
      "definition_site": "004bf9a8",
      "incomplete_value": false,
      "site": "004bf9b8",
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
            "const:d3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bf968",
      "incomplete_value": false,
      "site": "004bf978",
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
            "const:120:8"
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
      "004bf998",
      "PARAM",
      [
        "storage",
        "002a8c20",
        null,
        "string"
      ]
    ],
    [
      "004bf9a0",
      "PARAM",
      [
        "storage",
        "002b0b27",
        null,
        "string"
      ]
    ],
    [
      "004bf9a8",
      "PARAM",
      [
        "storage",
        "002a4120",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bf998",
      "PARAM",
      [
        "storage",
        "002a8bc4",
        null,
        "string"
      ]
    ],
    [
      "004bf9a0",
      "PARAM",
      [
        "storage",
        "002b0acb",
        null,
        "string"
      ]
    ],
    [
      "004bf9a8",
      "PARAM",
      [
        "storage",
        "002a40d3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bf978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bf8f0.md#insn-004bf978) · [`004bf918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bf8f0.md#insn-004bf918) · [`004bf93c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bf8f0.md#insn-004bf93c)
- 新版 [`004bf9b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf930.md#insn-004bf9b8) · [`004bf958`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf930.md#insn-004bf958) · [`004bf97c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf930.md#insn-004bf97c)

~~~diff
- 004bf978 ["INT_ADD", "register:40f0:8", ["const:4bf978:8", "const:4:8"]]
- 004bf978 ["CALL", null, ["callee:00c58720:8"]]
+ 004bf9b8 ["INT_ADD", "register:40f0:8", ["const:4bf9b8:8", "const:4:8"]]
+ 004bf9b8 ["CALL", null, ["callee:00c58720:8"]]
- 004bf978 bytes 36631e94
+ 004bf9b8 bytes 5a631e94
- 004bf918 ["COPY", "register:0:8", ["register:4040:8"]]
- 004bf918 ["INT_ADD", "register:40f0:8", ["const:4bf918:8", "const:4:8"]]
- 004bf918 ["CALLIND", null, ["register:0:8"]]
+ 004bf958 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bf958 ["INT_ADD", "register:40f0:8", ["const:4bf958:8", "const:4:8"]]
+ 004bf958 ["CALLIND", null, ["register:0:8"]]
- 004bf918 bytes 00013fd6
+ 004bf958 bytes 00013fd6
- 004bf93c ["COPY", "register:0:8", ["register:4040:8"]]
- 004bf93c ["INT_ADD", "register:40f0:8", ["const:4bf93c:8", "const:4:8"]]
- 004bf93c ["CALLIND", null, ["register:0:8"]]
+ 004bf97c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bf97c ["INT_ADD", "register:40f0:8", ["const:4bf97c:8", "const:4:8"]]
+ 004bf97c ["CALLIND", null, ["register:0:8"]]
- 004bf93c bytes 00013fd6
+ 004bf97c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4317ce12ae41904fbdb95557b545699"></a>

### [`004bf97c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bf97c.md) → [`004bf9bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf9bc.md) _ZN5Botan14ECB_Decryption6finishERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 0件  · 呼出先 9件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

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
      "definition_site": "004bfb2c",
      "incomplete_value": false,
      "site": "004bfb34",
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
            "const:93:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bfaec",
      "incomplete_value": false,
      "site": "004bfaf4",
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
            "const:53:8"
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
      "definition_site": "004bfb7c",
      "incomplete_value": true,
      "site": "004bfb88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004bfb3c",
      "incomplete_value": true,
      "site": "004bfb48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bfb78",
      "incomplete_value": false,
      "site": "004bfb88",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004bfb38",
      "incomplete_value": false,
      "site": "004bfb48",
      "value": [
        "leaf",
        "const:535868:8"
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
      "004bfb2c",
      "PARAM",
      [
        "storage",
        "002c1053",
        null,
        "string"
      ]
    ],
    [
      "004bfb78",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004bfb7c",
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
      "004bfb2c",
      "PARAM",
      [
        "storage",
        "002c1093",
        null,
        "string"
      ]
    ],
    [
      "004bfb78",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004bfb7c",
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

- 旧版 [`004bfaf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bf97c.md#insn-004bfaf4) · [`004bfb48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bf97c.md#insn-004bfb48) · [`004bfb78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bf97c.md#insn-004bfb78)
- 新版 [`004bfb34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf9bc.md#insn-004bfb34) · [`004bfb88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf9bc.md#insn-004bfb88) · [`004bfbb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf9bc.md#insn-004bfbb8)

~~~diff
- 004bfaf4 ["INT_ADD", "register:40f0:8", ["const:4bfaf4:8", "const:4:8"]]
- 004bfaf4 ["CALL", null, ["callee:00c58040:8"]]
+ 004bfb34 ["INT_ADD", "register:40f0:8", ["const:4bfb34:8", "const:4:8"]]
+ 004bfb34 ["CALL", null, ["callee:00c58040:8"]]
- 004bfaf4 bytes 1f611e94
+ 004bfb34 bytes 43611e94
- 004bfb48 ["INT_ADD", "register:40f0:8", ["const:4bfb48:8", "const:4:8"]]
- 004bfb48 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004bfb88 ["INT_ADD", "register:40f0:8", ["const:4bfb88:8", "const:4:8"]]
+ 004bfb88 ["CALL", null, ["callee:00c57fe0:8"]]
- 004bfb48 bytes f2601e94
+ 004bfb88 bytes 16611e94
- 004bfb78 ["COPY", "tmp:0:8", ["const:dcb:8"]]
- 004bfb78 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 004bfb78 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 004bfb78 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 004bfbb8 ["COPY", "tmp:0:8", ["const:973:8"]]
+ 004bfbb8 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 004bfbb8 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 004bfbb8 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 004bfb78 bytes 632c3791
+ 004bfbb8 bytes 63cc2591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0810bf3cc7e2b66940c7042be5f41f39"></a>

### [`004bfd04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bfd04.md) → [`004bfd44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bfd44.md) _ZN5Botan13EMSA_PKCS1v1511encoding_ofERKNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEmRNS_21RandomNumberGeneratorE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004bfe38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bfe38.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004bfe78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bfe78.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)

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
      "definition_site": "004bfde4",
      "incomplete_value": false,
      "site": "004bfdec",
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
            "const:d5d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bfda4",
      "incomplete_value": false,
      "site": "004bfdac",
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
            "const:d2c:8"
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
      "definition_site": "004bfe1c",
      "incomplete_value": true,
      "site": "004bfe28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004bfddc",
      "incomplete_value": true,
      "site": "004bfde8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bfe18",
      "incomplete_value": false,
      "site": "004bfe28",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004bfdd8",
      "incomplete_value": false,
      "site": "004bfde8",
      "value": [
        "leaf",
        "const:535868:8"
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
      "004bfde4",
      "PARAM",
      [
        "storage",
        "002b4d2c",
        null,
        "string"
      ]
    ],
    [
      "004bfe18",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004bfe1c",
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
      "004bfde4",
      "PARAM",
      [
        "storage",
        "002b4d5d",
        null,
        "string"
      ]
    ],
    [
      "004bfe18",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004bfe1c",
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

- 旧版 [`004bfdac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bfd04.md#insn-004bfdac) · [`004bfde8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bfd04.md#insn-004bfde8) · [`004bfd4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bfd04.md#insn-004bfd4c)
- 新版 [`004bfdec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bfd44.md#insn-004bfdec) · [`004bfe28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bfd44.md#insn-004bfe28) · [`004bfd8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bfd44.md#insn-004bfd8c)

~~~diff
- 004bfdac ["INT_ADD", "register:40f0:8", ["const:4bfdac:8", "const:4:8"]]
- 004bfdac ["CALL", null, ["callee:0043de18:8"]]
+ 004bfdec ["INT_ADD", "register:40f0:8", ["const:4bfdec:8", "const:4:8"]]
+ 004bfdec ["CALL", null, ["callee:0043de18:8"]]
- 004bfdac bytes 0bf8fd97
+ 004bfdec bytes 0bf8fd97
- 004bfde8 ["INT_ADD", "register:40f0:8", ["const:4bfde8:8", "const:4:8"]]
- 004bfde8 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004bfe28 ["INT_ADD", "register:40f0:8", ["const:4bfe28:8", "const:4:8"]]
+ 004bfe28 ["CALL", null, ["callee:00c57fe0:8"]]
- 004bfde8 bytes 4a601e94
+ 004bfe28 bytes 6e601e94
- 004bfd4c ["COPY", "register:0:8", ["register:4040:8"]]
- 004bfd4c ["INT_ADD", "register:40f0:8", ["const:4bfd4c:8", "const:4:8"]]
- 004bfd4c ["CALLIND", null, ["register:0:8"]]
+ 004bfd8c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bfd8c ["INT_ADD", "register:40f0:8", ["const:4bfd8c:8", "const:4:8"]]
+ 004bfd8c ["CALLIND", null, ["register:0:8"]]
- 004bfd4c bytes 00013fd6
+ 004bfd8c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-502f58da085217d431c816d8a84f914e"></a>

### [`004bfe38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bfe38.md) → [`004bfe78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bfe78.md) FUN_004bfe78

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`004bfd04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bfd04.md) [`004c0074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c0074.md) [`004c170c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c1/004c170c.md) [`004c1724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c1/004c1724.md) · 呼出先 10件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)
- 新版 呼出元 4件 [`004bfd44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bfd44.md) [`004c00b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c00b4.md) [`004c174c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c174c.md) [`004c1764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c1764.md) · 呼出先 10件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004b3548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3548.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)

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
      "definition_site": "004bffd8",
      "incomplete_value": false,
      "site": "004bffe0",
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
            "const:d4d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004bff98",
      "incomplete_value": false,
      "site": "004bffa0",
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
            "const:d1e:8"
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
      "definition_site": "004c0010",
      "incomplete_value": true,
      "site": "004c001c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004bffd0",
      "incomplete_value": true,
      "site": "004bffdc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c000c",
      "incomplete_value": false,
      "site": "004c001c",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004bffcc",
      "incomplete_value": false,
      "site": "004bffdc",
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
      "004bffd8",
      "PARAM",
      [
        "storage",
        "002a8d1e",
        null,
        "string"
      ]
    ],
    [
      "004c000c",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004c0010",
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
      "004bffd8",
      "PARAM",
      [
        "storage",
        "002a8d4d",
        null,
        "string"
      ]
    ],
    [
      "004c000c",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004c0010",
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

- 旧版 [`004bffa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bfe38.md#insn-004bffa0) · [`004bffdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bfe38.md#insn-004bffdc) · [`004c0014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bfe38.md#insn-004c0014)
- 新版 [`004bffe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bfe78.md#insn-004bffe0) · [`004c001c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bfe78.md#insn-004c001c) · [`004c0054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bfe78.md#insn-004c0054)

~~~diff
- 004bffa0 ["INT_ADD", "register:40f0:8", ["const:4bffa0:8", "const:4:8"]]
- 004bffa0 ["CALL", null, ["callee:0043de18:8"]]
+ 004bffe0 ["INT_ADD", "register:40f0:8", ["const:4bffe0:8", "const:4:8"]]
+ 004bffe0 ["CALL", null, ["callee:0043de18:8"]]
- 004bffa0 bytes 8ef7fd97
+ 004bffe0 bytes 8ef7fd97
- 004bffdc ["INT_ADD", "register:40f0:8", ["const:4bffdc:8", "const:4:8"]]
- 004bffdc ["CALL", null, ["callee:00c57fe0:8"]]
+ 004c001c ["INT_ADD", "register:40f0:8", ["const:4c001c:8", "const:4:8"]]
+ 004c001c ["CALL", null, ["callee:00c57fe0:8"]]
- 004bffdc bytes cd5f1e94
+ 004c001c bytes f15f1e94
- 004c0014 ["INT_ADD", "register:40f0:8", ["const:4c0014:8", "const:4:8"]]
- 004c0014 ["CALL", null, ["callee:00c58720:8"]]
+ 004c0054 ["INT_ADD", "register:40f0:8", ["const:4c0054:8", "const:4:8"]]
+ 004c0054 ["CALL", null, ["callee:00c58720:8"]]
- 004c0014 bytes 8f611e94
+ 004c0054 bytes b3611e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75ce6e5d196ac09210d53eb0a960a79e"></a>

### [`004c0074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c0074.md) → [`004c00b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c00b4.md) _ZN5Botan13EMSA_PKCS1v156verifyERKNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEES7_m

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`004bfe38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bfe38.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004bfe78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bfe78.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)

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
      "definition_site": "004c0178",
      "incomplete_value": true,
      "site": "004c0178",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c0138",
      "incomplete_value": true,
      "site": "004c0138",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004c0168",
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
      "004c0168",
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

- 旧版 [`004c0138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c0074.md#insn-004c0138) · [`004c00bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c0074.md#insn-004c00bc) · [`004c00dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c0074.md#insn-004c00dc)
- 新版 [`004c0178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c00b4.md#insn-004c0178) · [`004c00fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c00b4.md#insn-004c00fc) · [`004c011c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c00b4.md#insn-004c011c)

~~~diff
- 004c0138 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c0138 ["INT_ADD", "register:40f0:8", ["const:4c0138:8", "const:4:8"]]
- 004c0138 ["CALLIND", null, ["register:0:8"]]
+ 004c0178 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c0178 ["INT_ADD", "register:40f0:8", ["const:4c0178:8", "const:4:8"]]
+ 004c0178 ["CALLIND", null, ["register:0:8"]]
- 004c0138 bytes 20013fd6
+ 004c0178 bytes 20013fd6
- 004c00bc ["COPY", "register:0:8", ["register:4040:8"]]
- 004c00bc ["INT_ADD", "register:40f0:8", ["const:4c00bc:8", "const:4:8"]]
- 004c00bc ["CALLIND", null, ["register:0:8"]]
+ 004c00fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c00fc ["INT_ADD", "register:40f0:8", ["const:4c00fc:8", "const:4:8"]]
+ 004c00fc ["CALLIND", null, ["register:0:8"]]
- 004c00bc bytes 00013fd6
+ 004c00fc bytes 00013fd6
- 004c00dc ["INT_ADD", "register:40f0:8", ["const:4c00dc:8", "const:4:8"]]
- 004c00dc ["CALL", null, ["callee:004bfe78:8"]]
+ 004c011c ["INT_ADD", "register:40f0:8", ["const:4c011c:8", "const:4:8"]]
+ 004c011c ["CALL", null, ["callee:004bfe78:8"]]
- 004c00dc bytes 57ffff97
+ 004c011c bytes 57ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2aef24a2b4622a765160b7e91560d396"></a>

### [`004c0188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c0188.md) → [`004c01c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c01c8.md) _ZNK5Botan13EMSA_PKCS1v1515config_for_x509ERKNS_11Private_KeyERKNSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 15件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004c07b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c07b4.md) [`004c0968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c0968.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 15件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004c07f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c07f4.md) [`004c09a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c09a8.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "004c0304",
      "incomplete_value": true,
      "site": "004c0304",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c02c4",
      "incomplete_value": true,
      "site": "004c02c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c034c",
      "incomplete_value": false,
      "site": "004c0354",
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
            "const:2f6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c030c",
      "incomplete_value": false,
      "site": "004c0314",
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
            "const:352:8"
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
      "definition_site": "004c0508",
      "incomplete_value": false,
      "site": "004c0510",
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
            "const:db:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c04c8",
      "incomplete_value": false,
      "site": "004c04d0",
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
            "const:128:8"
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
      "004c02f8",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "004c0304",
      "DATA",
      [
        "storage",
        "00c661a8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004c034c",
      "PARAM",
      [
        "storage",
        "002a5352",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004c02f8",
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ],
    [
      "004c0304",
      "DATA",
      [
        "storage",
        "00c66278",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004c034c",
      "PARAM",
      [
        "storage",
        "002a52f6",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c0304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c0188.md#insn-004c0304) · [`004c0314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c0188.md#insn-004c0314) · [`004c04d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c0188.md#insn-004c04d0)
- 新版 [`004c0344`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c01c8.md#insn-004c0344) · [`004c0354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c01c8.md#insn-004c0354) · [`004c0510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c01c8.md#insn-004c0510)

~~~diff
- 004c0304 ["COPY", "register:0:8", ["register:4050:8"]]
- 004c0304 ["INT_ADD", "register:40f0:8", ["const:4c0304:8", "const:4:8"]]
- 004c0304 ["CALLIND", null, ["register:0:8"]]
+ 004c0344 ["COPY", "register:0:8", ["register:4050:8"]]
+ 004c0344 ["INT_ADD", "register:40f0:8", ["const:4c0344:8", "const:4:8"]]
+ 004c0344 ["CALLIND", null, ["register:0:8"]]
- 004c0304 bytes 40013fd6
+ 004c0344 bytes 40013fd6
- 004c0314 ["INT_ADD", "register:40f0:8", ["const:4c0314:8", "const:4:8"]]
- 004c0314 ["CALL", null, ["callee:00c58040:8"]]
+ 004c0354 ["INT_ADD", "register:40f0:8", ["const:4c0354:8", "const:4:8"]]
+ 004c0354 ["CALL", null, ["callee:00c58040:8"]]
- 004c0314 bytes 175f1e94
+ 004c0354 bytes 3b5f1e94
- 004c04d0 ["INT_ADD", "register:40f0:8", ["const:4c04d0:8", "const:4:8"]]
- 004c04d0 ["CALL", null, ["callee:0043de18:8"]]
+ 004c0510 ["INT_ADD", "register:40f0:8", ["const:4c0510:8", "const:4:8"]]
+ 004c0510 ["CALL", null, ["callee:0043de18:8"]]
- 004c04d0 bytes 42f6fd97
+ 004c0510 bytes 42f6fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-122adb0bc6b8298434d2414430161e42"></a>

### [`004c0968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c0968.md) → [`004c09a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c09a8.md) FUN_004c09a8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004c0188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c0188.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f60.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)
- 新版 呼出元 1件 [`004c01c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c01c8.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58030.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)

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
      "definition_site": "004c09e0",
      "incomplete_value": false,
      "site": "004c09ec",
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
            "const:db8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c09a0",
      "incomplete_value": false,
      "site": "004c09ac",
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
            "const:e0c:8"
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
      "definition_site": "004c0a0c",
      "incomplete_value": false,
      "site": "004c0a14",
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
            "const:2d6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c09cc",
      "incomplete_value": false,
      "site": "004c09d4",
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
            "const:332:8"
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
      "004c09e0",
      "PARAM",
      [
        "storage",
        "002bee0c",
        null,
        "string"
      ]
    ],
    [
      "004c0a0c",
      "PARAM",
      [
        "storage",
        "002ab332",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004c09e0",
      "PARAM",
      [
        "storage",
        "002bedb8",
        null,
        "string"
      ]
    ],
    [
      "004c0a0c",
      "PARAM",
      [
        "storage",
        "002ab2d6",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c09ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c0968.md#insn-004c09ac) · [`004c09d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c0968.md#insn-004c09d4) · [`004c0998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c0968.md#insn-004c0998)
- 新版 [`004c09ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c09a8.md#insn-004c09ec) · [`004c0a14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c09a8.md#insn-004c0a14) · [`004c09d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c09a8.md#insn-004c09d8)

~~~diff
- 004c09ac ["INT_ADD", "register:40f0:8", ["const:4c09ac:8", "const:4:8"]]
- 004c09ac ["CALL", null, ["callee:00c58030:8"]]
+ 004c09ec ["INT_ADD", "register:40f0:8", ["const:4c09ec:8", "const:4:8"]]
+ 004c09ec ["CALL", null, ["callee:00c58030:8"]]
- 004c09ac bytes 6d5d1e94
+ 004c09ec bytes 915d1e94
- 004c09d4 ["INT_ADD", "register:40f0:8", ["const:4c09d4:8", "const:4:8"]]
- 004c09d4 ["CALL", null, ["callee:00c58040:8"]]
+ 004c0a14 ["INT_ADD", "register:40f0:8", ["const:4c0a14:8", "const:4:8"]]
+ 004c0a14 ["CALL", null, ["callee:00c58040:8"]]
- 004c09d4 bytes 675d1e94
+ 004c0a14 bytes 8b5d1e94
- 004c0998 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c0998 ["INT_ADD", "register:40f0:8", ["const:4c0998:8", "const:4:8"]]
- 004c0998 ["CALLIND", null, ["register:0:8"]]
+ 004c09d8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c09d8 ["INT_ADD", "register:40f0:8", ["const:4c09d8:8", "const:4:8"]]
+ 004c09d8 ["CALLIND", null, ["register:0:8"]]
- 004c0998 bytes 20013fd6
+ 004c09d8 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b87a42ce8f7ef283720f7e4d659ff79d"></a>

### [`004c0abc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c0abc.md) → [`004c0afc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c0afc.md) _ZN5Botan13EMSA_PKCS1v15C2EPNS_12HashFunctionE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c59510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59510.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58de0.md)
- 新版 呼出元 1件 [`00c595e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c595e0.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58eb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58eb0.md)

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
      "definition_site": "004c0b2c",
      "incomplete_value": true,
      "site": "004c0b38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c0aec",
      "incomplete_value": true,
      "site": "004c0af8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004c0b20",
      "READ",
      [
        "storage",
        "00c9ae50",
        null,
        "pointer"
      ]
    ],
    [
      "004c0b38",
      "DATA",
      [
        "storage",
        "00c66578",
        null,
        "undefined1[88]"
      ]
    ]
  ],
  "added": [
    [
      "004c0b20",
      "READ",
      [
        "storage",
        "00c9af20",
        null,
        "pointer"
      ]
    ],
    [
      "004c0b38",
      "DATA",
      [
        "storage",
        "00c66648",
        null,
        "undefined1[88]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c0ae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c0abc.md#insn-004c0ae0) · [`004c0ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c0abc.md#insn-004c0ae4) · [`004c0b10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c0abc.md#insn-004c0b10)
- 新版 [`004c0b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c0afc.md#insn-004c0b20) · [`004c0b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c0afc.md#insn-004c0b50)

~~~diff
- 004c0ae0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e50:8"]]
- 004c0ae0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c0b20 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f20:8"]]
+ 004c0b20 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c0ae0 bytes 292947f9
+ 004c0b20 bytes 299147f9
- 004c0ae4 ["COPY", "register:4098:8", ["register:4000:8"]]
- 004c0ae4 bytes f30300aa
- 004c0b10 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c0b10 ["INT_ADD", "register:40f0:8", ["const:4c0b10:8", "const:4:8"]]
- 004c0b10 ["CALLIND", null, ["register:0:8"]]
+ 004c0b50 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c0b50 ["INT_ADD", "register:40f0:8", ["const:4c0b50:8", "const:4:8"]]
+ 004c0b50 ["CALLIND", null, ["register:0:8"]]
- 004c0b10 bytes 20013fd6
+ 004c0b50 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4dd3d95f41faa60573dd8a164cffd66"></a>

### [`004c0be4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c0be4.md) → [`004c0c24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c0c24.md) _ZN5Botan12pkcs_hash_idERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58de0.md) · 呼出先 9件 [`00441e94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441e94.md) [`004cc18c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cc/004cc18c.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00c58eb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58eb0.md) · 呼出先 9件 [`00441ed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441ed4.md) [`004cc1cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cc/004cc1cc.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

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
      "definition_site": "004c0d7c",
      "incomplete_value": true,
      "site": "004c0d8c",
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
                "const:f06:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c0d3c",
      "incomplete_value": true,
      "site": "004c0d4c",
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
                "const:ec6:8"
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
      "definition_site": "004c0e3c",
      "incomplete_value": false,
      "site": "004c0e44",
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
            "const:762:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c0dfc",
      "incomplete_value": false,
      "site": "004c0e04",
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
            "const:7be:8"
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
      "definition_site": "004c0e6c",
      "incomplete_value": false,
      "site": "004c0e74",
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
            "const:b52:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c0e2c",
      "incomplete_value": false,
      "site": "004c0e34",
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
      "004c0d7c",
      "READ",
      [
        "storage",
        "002caec6",
        null,
        null
      ]
    ],
    [
      "004c0e3c",
      "PARAM",
      [
        "storage",
        "002ae7be",
        null,
        "string"
      ]
    ],
    [
      "004c0e60",
      "PARAM",
      [
        "storage",
        "002caef6",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004c0d7c",
      "READ",
      [
        "storage",
        "002caf06",
        null,
        null
      ]
    ],
    [
      "004c0e3c",
      "PARAM",
      [
        "storage",
        "002ae762",
        null,
        "string"
      ]
    ],
    [
      "004c0e60",
      "PARAM",
      [
        "storage",
        "002caf36",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c0e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c0be4.md#insn-004c0e04) · [`004c0e34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c0be4.md#insn-004c0e34) · [`004c0e64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c0be4.md#insn-004c0e64)
- 新版 [`004c0e44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c0c24.md#insn-004c0e44) · [`004c0e74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c0c24.md#insn-004c0e74) · [`004c0ea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c0c24.md#insn-004c0ea4)

~~~diff
- 004c0e04 ["INT_ADD", "register:40f0:8", ["const:4c0e04:8", "const:4:8"]]
- 004c0e04 ["CALL", null, ["callee:00441ed4:8"]]
+ 004c0e44 ["INT_ADD", "register:40f0:8", ["const:4c0e44:8", "const:4:8"]]
+ 004c0e44 ["CALL", null, ["callee:00441ed4:8"]]
- 004c0e04 bytes 2404fe97
+ 004c0e44 bytes 2404fe97
- 004c0e34 ["INT_ADD", "register:40f0:8", ["const:4c0e34:8", "const:4:8"]]
- 004c0e34 ["CALL", null, ["callee:00441ed4:8"]]
+ 004c0e74 ["INT_ADD", "register:40f0:8", ["const:4c0e74:8", "const:4:8"]]
+ 004c0e74 ["CALL", null, ["callee:00441ed4:8"]]
- 004c0e34 bytes 1804fe97
+ 004c0e74 bytes 1804fe97
- 004c0e64 ["INT_ADD", "register:40f0:8", ["const:4c0e64:8", "const:4:8"]]
- 004c0e64 ["CALL", null, ["callee:00441ed4:8"]]
+ 004c0ea4 ["INT_ADD", "register:40f0:8", ["const:4c0ea4:8", "const:4:8"]]
+ 004c0ea4 ["CALL", null, ["callee:00441ed4:8"]]
- 004c0e64 bytes 0c04fe97
+ 004c0ea4 bytes 0c04fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09de1d2fc1186232df590eda8b69f781"></a>

### [`004c1124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c1/004c1124.md) → [`004c1164`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c1164.md) _ZN5Botan17EMSA_PKCS1v15_RawC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59500.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58de0.md) [`00c58df0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58df0.md)
- 新版 呼出元 1件 [`00c595d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c595d0.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58eb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58eb0.md) [`00c58ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ec0.md)

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
      "definition_site": "004c1198",
      "incomplete_value": true,
      "site": "004c11a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c1158",
      "incomplete_value": true,
      "site": "004c1160",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004c1188",
      "READ",
      [
        "storage",
        "00c9ae58",
        null,
        "pointer"
      ]
    ],
    [
      "004c11a0",
      "DATA",
      [
        "storage",
        "00c665d0",
        null,
        "undefined1[88]"
      ]
    ]
  ],
  "added": [
    [
      "004c1188",
      "READ",
      [
        "storage",
        "00c9af28",
        null,
        "pointer"
      ]
    ],
    [
      "004c11a0",
      "DATA",
      [
        "storage",
        "00c666a0",
        null,
        "undefined1[88]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c11a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c1/004c1124.md#insn-004c11a0) · [`004c1148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c1/004c1124.md#insn-004c1148) · [`004c11b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c1/004c1124.md#insn-004c11b0)
- 新版 [`004c11e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c1164.md#insn-004c11e0) · [`004c1188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c1164.md#insn-004c1188) · [`004c11f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c1164.md#insn-004c11f0)

~~~diff
- 004c11a0 ["INT_ADD", "register:40f0:8", ["const:4c11a0:8", "const:4:8"]]
- 004c11a0 ["CALL", null, ["callee:00c58eb0:8"]]
+ 004c11e0 ["INT_ADD", "register:40f0:8", ["const:4c11e0:8", "const:4:8"]]
+ 004c11e0 ["CALL", null, ["callee:00c58eb0:8"]]
- 004c11a0 bytes 105f1e94
+ 004c11e0 bytes 345f1e94
- 004c1148 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e58:8"]]
- 004c1148 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c1188 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f28:8"]]
+ 004c1188 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c1148 bytes 082d47f9
+ 004c1188 bytes 089547f9
- 004c11b0 ["INT_ADD", "register:40f0:8", ["const:4c11b0:8", "const:4:8"]]
- 004c11b0 ["CALL", null, ["callee:00c57f80:8"]]
+ 004c11f0 ["INT_ADD", "register:40f0:8", ["const:4c11f0:8", "const:4:8"]]
+ 004c11f0 ["CALL", null, ["callee:00c57f80:8"]]
- 004c11b0 bytes 405b1e94
+ 004c11f0 bytes 645b1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-319d261bec0a979897c1cac59dca7351"></a>

### [`004c15e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c1/004c15e0.md) → [`004c1620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c1620.md) _ZN5Botan17EMSA_PKCS1v15_Raw8raw_dataEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

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
      "definition_site": "004c16a8",
      "incomplete_value": false,
      "site": "004c16b0",
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
            "const:4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c1668",
      "incomplete_value": false,
      "site": "004c1670",
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
            "const:fc4:8"
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
      "definition_site": "004c16e4",
      "incomplete_value": true,
      "site": "004c16f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c16a4",
      "incomplete_value": true,
      "site": "004c16b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c16e0",
      "incomplete_value": false,
      "site": "004c16f0",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004c16a0",
      "incomplete_value": false,
      "site": "004c16b0",
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
      "004c16a8",
      "PARAM",
      [
        "storage",
        "002b5fc4",
        null,
        "string"
      ]
    ],
    [
      "004c16e0",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004c16e4",
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
      "004c16a8",
      "PARAM",
      [
        "storage",
        "002b6004",
        null,
        "string"
      ]
    ],
    [
      "004c16e0",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004c16e4",
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

- 旧版 [`004c1670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c1/004c15e0.md#insn-004c1670) · [`004c16b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c1/004c15e0.md#insn-004c16b0) · [`004c165c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c1/004c15e0.md#insn-004c165c)
- 新版 [`004c16b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c1620.md#insn-004c16b0) · [`004c16f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c1620.md#insn-004c16f0) · [`004c169c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c1620.md#insn-004c169c)

~~~diff
- 004c1670 ["INT_ADD", "register:40f0:8", ["const:4c1670:8", "const:4:8"]]
- 004c1670 ["CALL", null, ["callee:0043de18:8"]]
+ 004c16b0 ["INT_ADD", "register:40f0:8", ["const:4c16b0:8", "const:4:8"]]
+ 004c16b0 ["CALL", null, ["callee:0043de18:8"]]
- 004c1670 bytes daf1fd97
+ 004c16b0 bytes daf1fd97
- 004c16b0 ["INT_ADD", "register:40f0:8", ["const:4c16b0:8", "const:4:8"]]
- 004c16b0 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004c16f0 ["INT_ADD", "register:40f0:8", ["const:4c16f0:8", "const:4:8"]]
+ 004c16f0 ["CALL", null, ["callee:00c57fe0:8"]]
- 004c16b0 bytes 185a1e94
+ 004c16f0 bytes 3c5a1e94
- 004c165c ["INT_ADD", "register:40f0:8", ["const:4c165c:8", "const:4:8"]]
- 004c165c ["CALL", null, ["callee:00c57fc0:8"]]
+ 004c169c ["INT_ADD", "register:40f0:8", ["const:4c169c:8", "const:4:8"]]
+ 004c169c ["CALL", null, ["callee:00c57fc0:8"]]
- 004c165c bytes 255a1e94
+ 004c169c bytes 495a1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e84e907fcfeb67ceefa39811b7f4201"></a>

### [`004c1820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c1/004c1820.md) → [`004c1860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c1860.md) _ZN5Botan4PSSRC2EPNS_12HashFunctionE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "004c1880",
      "incomplete_value": true,
      "site": "004c1884",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c1840",
      "incomplete_value": true,
      "site": "004c1844",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004c1878",
      "READ",
      [
        "storage",
        "00c9ae60",
        null,
        "pointer"
      ]
    ],
    [
      "004c1884",
      "DATA",
      [
        "storage",
        "00c66628",
        null,
        "undefined1[88]"
      ]
    ]
  ],
  "added": [
    [
      "004c1878",
      "READ",
      [
        "storage",
        "00c9af30",
        null,
        "pointer"
      ]
    ],
    [
      "004c1884",
      "DATA",
      [
        "storage",
        "00c666f8",
        null,
        "undefined1[88]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c1838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c1/004c1820.md#insn-004c1838) · [`004c1850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c1/004c1820.md#insn-004c1850)
- 新版 [`004c1878`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c1860.md#insn-004c1878) · [`004c1890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c1860.md#insn-004c1890)

~~~diff
- 004c1838 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e60:8"]]
- 004c1838 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c1878 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f30:8"]]
+ 004c1878 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c1838 bytes 083147f9
+ 004c1878 bytes 089947f9
- 004c1850 ["COPY", "register:0:8", ["register:4040:8"]]
- 004c1850 ["INT_ADD", "register:40f0:8", ["const:4c1850:8", "const:4:8"]]
- 004c1850 ["CALLIND", null, ["register:0:8"]]
+ 004c1890 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c1890 ["INT_ADD", "register:40f0:8", ["const:4c1890:8", "const:4:8"]]
+ 004c1890 ["CALLIND", null, ["register:0:8"]]
- 004c1850 bytes 00013fd6
+ 004c1890 bytes 00013fd6
~~~


<a id="compare-e2e26eea020f1395a9dfddeaa425d6ba"></a>

### [`004c1a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c1/004c1a10.md) → [`004c1a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c1a50.md) FUN_004c1a50

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`004c1914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c1/004c1914.md) [`004c2e9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c2/004c2e9c.md) · 呼出先 11件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)
- 新版 呼出元 2件 [`004c1954`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c1954.md) [`004c2edc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c2/004c2edc.md) · 呼出先 11件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004b3548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3548.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)

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
      "definition_site": "004c1d00",
      "incomplete_value": true,
      "site": "004c1d00",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c1cc0",
      "incomplete_value": true,
      "site": "004c1cc0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 18,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c1d50",
      "incomplete_value": false,
      "site": "004c1d58",
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
            "const:64e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c1d10",
      "incomplete_value": false,
      "site": "004c1d18",
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
            "const:6a2:8"
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
      "definition_site": "004c1d8c",
      "incomplete_value": true,
      "site": "004c1d98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c1d4c",
      "incomplete_value": true,
      "site": "004c1d58",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004c1cf0",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004c1d50",
      "PARAM",
      [
        "storage",
        "002bc6a2",
        null,
        "string"
      ]
    ],
    [
      "004c1d88",
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
      "004c1cf0",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "004c1d50",
      "PARAM",
      [
        "storage",
        "002bc64e",
        null,
        "string"
      ]
    ],
    [
      "004c1d88",
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

- 旧版 [`004c1cc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c1/004c1a10.md#insn-004c1cc0) · [`004c1d18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c1/004c1a10.md#insn-004c1d18) · [`004c1d58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c1/004c1a10.md#insn-004c1d58)
- 新版 [`004c1d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c1a50.md#insn-004c1d00) · [`004c1d58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c1a50.md#insn-004c1d58) · [`004c1d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c1a50.md#insn-004c1d98)

~~~diff
- 004c1cc0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c1cc0 ["INT_ADD", "register:40f0:8", ["const:4c1cc0:8", "const:4:8"]]
- 004c1cc0 ["CALLIND", null, ["register:0:8"]]
+ 004c1d00 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c1d00 ["INT_ADD", "register:40f0:8", ["const:4c1d00:8", "const:4:8"]]
+ 004c1d00 ["CALLIND", null, ["register:0:8"]]
- 004c1cc0 bytes 20013fd6
+ 004c1d00 bytes 20013fd6
- 004c1d18 ["INT_ADD", "register:40f0:8", ["const:4c1d18:8", "const:4:8"]]
- 004c1d18 ["CALL", null, ["callee:0043de18:8"]]
+ 004c1d58 ["INT_ADD", "register:40f0:8", ["const:4c1d58:8", "const:4:8"]]
+ 004c1d58 ["CALL", null, ["callee:0043de18:8"]]
- 004c1d18 bytes 30f0fd97
+ 004c1d58 bytes 30f0fd97
- 004c1d58 ["INT_ADD", "register:40f0:8", ["const:4c1d58:8", "const:4:8"]]
- 004c1d58 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004c1d98 ["INT_ADD", "register:40f0:8", ["const:4c1d98:8", "const:4:8"]]
+ 004c1d98 ["CALL", null, ["callee:00c57fe0:8"]]
- 004c1d58 bytes 6e581e94
+ 004c1d98 bytes 92581e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1e762bbd10d7ac78039d175b7a96db2"></a>

### [`004c1e44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c1/004c1e44.md) → [`004c1e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c1e84.md) FUN_004c1e84

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`004c1e3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c1/004c1e3c.md) [`004c2f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c2/004c2f98.md) · 呼出先 10件 [`004b13f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b1/004b13f4.md) [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md) [`004bfca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bfca4.md) [`005402a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005402a4.md) [`00543858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543858.md)
- 新版 呼出元 2件 [`004c1e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c1e7c.md) [`004c2fd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c2/004c2fd8.md) · 呼出先 10件 [`004b1434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b1/004b1434.md) [`004b3548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3548.md) [`004bfce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bfce4.md) [`005402e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/005402e4.md) [`00543898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543898.md)

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
      "definition_site": "004c2270",
      "incomplete_value": true,
      "site": "004c2270",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c2230",
      "incomplete_value": true,
      "site": "004c2230",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004c2260",
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
      "004c2260",
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

- 旧版 [`004c2230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c1/004c1e44.md#insn-004c2230) · [`004c1e84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c1/004c1e44.md#insn-004c1e84) · [`004c1eec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c1/004c1e44.md#insn-004c1eec)
- 新版 [`004c2270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c1e84.md#insn-004c2270) · [`004c1ec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c1e84.md#insn-004c1ec4) · [`004c1f2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c1/004c1e84.md#insn-004c1f2c)

~~~diff
- 004c2230 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c2230 ["INT_ADD", "register:40f0:8", ["const:4c2230:8", "const:4:8"]]
- 004c2230 ["CALLIND", null, ["register:0:8"]]
+ 004c2270 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c2270 ["INT_ADD", "register:40f0:8", ["const:4c2270:8", "const:4:8"]]
+ 004c2270 ["CALLIND", null, ["register:0:8"]]
- 004c2230 bytes 20013fd6
+ 004c2270 bytes 20013fd6
- 004c1e84 ["COPY", "register:0:8", ["register:4040:8"]]
- 004c1e84 ["INT_ADD", "register:40f0:8", ["const:4c1e84:8", "const:4:8"]]
- 004c1e84 ["CALLIND", null, ["register:0:8"]]
+ 004c1ec4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c1ec4 ["INT_ADD", "register:40f0:8", ["const:4c1ec4:8", "const:4:8"]]
+ 004c1ec4 ["CALLIND", null, ["register:0:8"]]
- 004c1e84 bytes 00013fd6
+ 004c1ec4 bytes 00013fd6
- 004c1eec ["INT_ADD", "register:40f0:8", ["const:4c1eec:8", "const:4:8"]]
- 004c1eec ["CALL", null, ["callee:005402e4:8"]]
+ 004c1f2c ["INT_ADD", "register:40f0:8", ["const:4c1f2c:8", "const:4:8"]]
+ 004c1f2c ["CALL", null, ["callee:005402e4:8"]]
- 004c1eec bytes eef80194
+ 004c1f2c bytes eef80194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fee7580ee9cdcb94f740ae40f05fabae"></a>

### [`004c2290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c2/004c2290.md) → [`004c22d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c2/004c22d0.md) _ZNK5Botan4PSSR4nameEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f60.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58030.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md)

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
      "definition_site": "004c2310",
      "incomplete_value": false,
      "site": "004c231c",
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
            "const:f0d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c22d0",
      "incomplete_value": false,
      "site": "004c22dc",
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
            "const:f61:8"
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
      "definition_site": "004c233c",
      "incomplete_value": false,
      "site": "004c2344",
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
            "const:742:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c22fc",
      "incomplete_value": false,
      "site": "004c2304",
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
      "definition_site": "004c23ac",
      "incomplete_value": false,
      "site": "004c23b4",
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
            "const:2d6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c236c",
      "incomplete_value": false,
      "site": "004c2374",
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
            "const:332:8"
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
      "004c2310",
      "PARAM",
      [
        "storage",
        "002b8f61",
        null,
        "string"
      ]
    ],
    [
      "004c233c",
      "PARAM",
      [
        "storage",
        "002ad79e",
        null,
        "string"
      ]
    ],
    [
      "004c23ac",
      "PARAM",
      [
        "storage",
        "002ab332",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004c2310",
      "PARAM",
      [
        "storage",
        "002b8f0d",
        null,
        "string"
      ]
    ],
    [
      "004c233c",
      "PARAM",
      [
        "storage",
        "002ad742",
        null,
        "string"
      ]
    ],
    [
      "004c23ac",
      "PARAM",
      [
        "storage",
        "002ab2d6",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c22dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c2/004c2290.md#insn-004c22dc) · [`004c2304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c2/004c2290.md#insn-004c2304) · [`004c2374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c2/004c2290.md#insn-004c2374)
- 新版 [`004c231c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c2/004c22d0.md#insn-004c231c) · [`004c2344`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c2/004c22d0.md#insn-004c2344) · [`004c23b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c2/004c22d0.md#insn-004c23b4)

~~~diff
- 004c22dc ["INT_ADD", "register:40f0:8", ["const:4c22dc:8", "const:4:8"]]
- 004c22dc ["CALL", null, ["callee:00c58030:8"]]
+ 004c231c ["INT_ADD", "register:40f0:8", ["const:4c231c:8", "const:4:8"]]
+ 004c231c ["CALL", null, ["callee:00c58030:8"]]
- 004c22dc bytes 21571e94
+ 004c231c bytes 45571e94
- 004c2304 ["INT_ADD", "register:40f0:8", ["const:4c2304:8", "const:4:8"]]
- 004c2304 ["CALL", null, ["callee:00c58040:8"]]
+ 004c2344 ["INT_ADD", "register:40f0:8", ["const:4c2344:8", "const:4:8"]]
+ 004c2344 ["CALL", null, ["callee:00c58040:8"]]
- 004c2304 bytes 1b571e94
+ 004c2344 bytes 3f571e94
- 004c2374 ["INT_ADD", "register:40f0:8", ["const:4c2374:8", "const:4:8"]]
- 004c2374 ["CALL", null, ["callee:00c58040:8"]]
+ 004c23b4 ["INT_ADD", "register:40f0:8", ["const:4c23b4:8", "const:4:8"]]
+ 004c23b4 ["CALL", null, ["callee:00c58040:8"]]
- 004c2374 bytes ff561e94
+ 004c23b4 bytes 23571e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f6b7c4a5ae70a36b08eac76560c48b8"></a>

### [`004c24fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c2/004c24fc.md) → [`004c253c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c2/004c253c.md) _ZNK5Botan4PSSR15config_for_x509ERKNS_11Private_KeyERKNSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 22件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004a6db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6db0.md) [`004c07b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c07b4.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00535b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b80.md)
- 新版 呼出元 0件  · 呼出先 22件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004a6df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a6df0.md) [`004c07f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c0/004c07f4.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00535bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bc0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.99% / 新版 94.99%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 4件, `store_value` 2件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c2678",
      "incomplete_value": true,
      "site": "004c2678",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c2638",
      "incomplete_value": true,
      "site": "004c2638",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c26b8",
      "incomplete_value": true,
      "site": "004c26b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a6f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c2678",
      "incomplete_value": true,
      "site": "004c2678",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a3e:8"
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
      "definition_site": "004c2834",
      "incomplete_value": true,
      "site": "004c2834",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004c27f4",
      "incomplete_value": true,
      "site": "004c27f4",
      "value": [
        "LOAD",
        "8",
        [
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
      "004c266c",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "004c2678",
      "DATA",
      [
        "storage",
        "00c661a8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004c26a0",
      "READ",
      [
        "storage",
        "002b1a3e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004c266c",
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ],
    [
      "004c2678",
      "DATA",
      [
        "storage",
        "00c66278",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004c26a0",
      "READ",
      [
        "storage",
        "002b1a6f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c27f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c2/004c24fc.md#insn-004c27f4) · [`004c2854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c2/004c24fc.md#insn-004c2854) · [`004c294c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c2/004c24fc.md#insn-004c294c)
- 新版 [`004c2834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c2/004c253c.md#insn-004c2834) · [`004c2894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c2/004c253c.md#insn-004c2894) · [`004c298c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c2/004c253c.md#insn-004c298c)

~~~diff
- 004c27f4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c27f4 ["INT_ADD", "register:40f0:8", ["const:4c27f4:8", "const:4:8"]]
- 004c27f4 ["CALLIND", null, ["register:0:8"]]
+ 004c2834 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c2834 ["INT_ADD", "register:40f0:8", ["const:4c2834:8", "const:4:8"]]
+ 004c2834 ["CALLIND", null, ["register:0:8"]]
- 004c27f4 bytes 20013fd6
+ 004c2834 bytes 20013fd6
- 004c2854 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c2854 ["INT_ADD", "register:40f0:8", ["const:4c2854:8", "const:4:8"]]
- 004c2854 ["CALLIND", null, ["register:0:8"]]
+ 004c2894 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c2894 ["INT_ADD", "register:40f0:8", ["const:4c2894:8", "const:4:8"]]
+ 004c2894 ["CALLIND", null, ["register:0:8"]]
- 004c2854 bytes 20013fd6
+ 004c2894 bytes 20013fd6
- 004c294c ["COPY", "register:0:8", ["register:4048:8"]]
- 004c294c ["INT_ADD", "register:40f0:8", ["const:4c294c:8", "const:4:8"]]
- 004c294c ["CALLIND", null, ["register:0:8"]]
+ 004c298c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c298c ["INT_ADD", "register:40f0:8", ["const:4c298c:8", "const:4:8"]]
+ 004c298c ["CALLIND", null, ["register:0:8"]]
- 004c294c bytes 20013fd6
+ 004c298c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ad28d13cc8d9b1776180f5726ca5634"></a>

### [`004c2cb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c2/004c2cb4.md) → [`004c2cf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c2/004c2cf4.md) _ZN5Botan8PSSR_RawC1EPNS_12HashFunctionE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "004c2d14",
      "incomplete_value": true,
      "site": "004c2d18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c2cd4",
      "incomplete_value": true,
      "site": "004c2cd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004c2d0c",
      "READ",
      [
        "storage",
        "00c9ae68",
        null,
        "pointer"
      ]
    ],
    [
      "004c2d18",
      "DATA",
      [
        "storage",
        "00c66680",
        null,
        "undefined1[88]"
      ]
    ]
  ],
  "added": [
    [
      "004c2d0c",
      "READ",
      [
        "storage",
        "00c9af38",
        null,
        "pointer"
      ]
    ],
    [
      "004c2d18",
      "DATA",
      [
        "storage",
        "00c66750",
        null,
        "undefined1[88]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c2ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c2/004c2cb4.md#insn-004c2ccc) · [`004c2ce4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c2/004c2cb4.md#insn-004c2ce4)
- 新版 [`004c2d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c2/004c2cf4.md#insn-004c2d0c) · [`004c2d24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c2/004c2cf4.md#insn-004c2d24)

~~~diff
- 004c2ccc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e68:8"]]
- 004c2ccc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c2d0c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f38:8"]]
+ 004c2d0c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c2ccc bytes 083547f9
+ 004c2d0c bytes 089d47f9
- 004c2ce4 ["COPY", "register:0:8", ["register:4040:8"]]
- 004c2ce4 ["INT_ADD", "register:40f0:8", ["const:4c2ce4:8", "const:4:8"]]
- 004c2ce4 ["CALLIND", null, ["register:0:8"]]
+ 004c2d24 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c2d24 ["INT_ADD", "register:40f0:8", ["const:4c2d24:8", "const:4:8"]]
+ 004c2d24 ["CALLIND", null, ["register:0:8"]]
- 004c2ce4 bytes 00013fd6
+ 004c2d24 bytes 00013fd6
~~~


<a id="compare-b3d3e65b4360449db8587f8d7832bd58"></a>

### [`004c2d54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c2/004c2d54.md) → [`004c2d94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c2/004c2d94.md) _ZN5Botan8PSSR_Raw8raw_dataEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

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
      "definition_site": "004c2e38",
      "incomplete_value": false,
      "site": "004c2e40",
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
            "const:c1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c2df8",
      "incomplete_value": false,
      "site": "004c2e00",
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
            "const:10e:8"
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
      "definition_site": "004c2e70",
      "incomplete_value": true,
      "site": "004c2e7c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c2e30",
      "incomplete_value": true,
      "site": "004c2e3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c2e6c",
      "incomplete_value": false,
      "site": "004c2e7c",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004c2e2c",
      "incomplete_value": false,
      "site": "004c2e3c",
      "value": [
        "leaf",
        "const:535868:8"
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
      "004c2e38",
      "PARAM",
      [
        "storage",
        "002a310e",
        null,
        "string"
      ]
    ],
    [
      "004c2e6c",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004c2e70",
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
      "004c2e38",
      "PARAM",
      [
        "storage",
        "002a30c1",
        null,
        "string"
      ]
    ],
    [
      "004c2e6c",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004c2e70",
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

- 旧版 [`004c2e00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c2/004c2d54.md#insn-004c2e00) · [`004c2e3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c2/004c2d54.md#insn-004c2e3c) · [`004c2da8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c2/004c2d54.md#insn-004c2da8)
- 新版 [`004c2e40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c2/004c2d94.md#insn-004c2e40) · [`004c2e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c2/004c2d94.md#insn-004c2e7c) · [`004c2de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c2/004c2d94.md#insn-004c2de8)

~~~diff
- 004c2e00 ["INT_ADD", "register:40f0:8", ["const:4c2e00:8", "const:4:8"]]
- 004c2e00 ["CALL", null, ["callee:0043de18:8"]]
+ 004c2e40 ["INT_ADD", "register:40f0:8", ["const:4c2e40:8", "const:4:8"]]
+ 004c2e40 ["CALL", null, ["callee:0043de18:8"]]
- 004c2e00 bytes f6ebfd97
+ 004c2e40 bytes f6ebfd97
- 004c2e3c ["INT_ADD", "register:40f0:8", ["const:4c2e3c:8", "const:4:8"]]
- 004c2e3c ["CALL", null, ["callee:00c57fe0:8"]]
+ 004c2e7c ["INT_ADD", "register:40f0:8", ["const:4c2e7c:8", "const:4:8"]]
+ 004c2e7c ["CALL", null, ["callee:00c57fe0:8"]]
- 004c2e3c bytes 35541e94
+ 004c2e7c bytes 59541e94
- 004c2da8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c2da8 ["INT_ADD", "register:40f0:8", ["const:4c2da8:8", "const:4:8"]]
- 004c2da8 ["CALLIND", null, ["register:0:8"]]
+ 004c2de8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c2de8 ["INT_ADD", "register:40f0:8", ["const:4c2de8:8", "const:4:8"]]
+ 004c2de8 ["CALLIND", null, ["register:0:8"]]
- 004c2da8 bytes 20013fd6
+ 004c2de8 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4183d42145f4261d1c33c870565ebe66"></a>

### [`004c2fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c2/004c2fa0.md) → [`004c2fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c2/004c2fe0.md) _ZNK5Botan8PSSR_Raw4nameEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f60.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58030.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md)

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
      "definition_site": "004c3020",
      "incomplete_value": false,
      "site": "004c302c",
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
            "const:21:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c2fe0",
      "incomplete_value": false,
      "site": "004c2fec",
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
            "const:6e:8"
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
      "definition_site": "004c304c",
      "incomplete_value": false,
      "site": "004c3054",
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
            "const:742:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c300c",
      "incomplete_value": false,
      "site": "004c3014",
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
      "definition_site": "004c30bc",
      "incomplete_value": false,
      "site": "004c30c4",
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
            "const:2d6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c307c",
      "incomplete_value": false,
      "site": "004c3084",
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
            "const:332:8"
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
      "004c3020",
      "PARAM",
      [
        "storage",
        "002a106e",
        null,
        "string"
      ]
    ],
    [
      "004c304c",
      "PARAM",
      [
        "storage",
        "002ad79e",
        null,
        "string"
      ]
    ],
    [
      "004c30bc",
      "PARAM",
      [
        "storage",
        "002ab332",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004c3020",
      "PARAM",
      [
        "storage",
        "002a1021",
        null,
        "string"
      ]
    ],
    [
      "004c304c",
      "PARAM",
      [
        "storage",
        "002ad742",
        null,
        "string"
      ]
    ],
    [
      "004c30bc",
      "PARAM",
      [
        "storage",
        "002ab2d6",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c2fec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c2/004c2fa0.md#insn-004c2fec) · [`004c3014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c2/004c2fa0.md#insn-004c3014) · [`004c3084`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c2/004c2fa0.md#insn-004c3084)
- 新版 [`004c302c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c2/004c2fe0.md#insn-004c302c) · [`004c3054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c2/004c2fe0.md#insn-004c3054) · [`004c30c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c2/004c2fe0.md#insn-004c30c4)

~~~diff
- 004c2fec ["INT_ADD", "register:40f0:8", ["const:4c2fec:8", "const:4:8"]]
- 004c2fec ["CALL", null, ["callee:00c58030:8"]]
+ 004c302c ["INT_ADD", "register:40f0:8", ["const:4c302c:8", "const:4:8"]]
+ 004c302c ["CALL", null, ["callee:00c58030:8"]]
- 004c2fec bytes dd531e94
+ 004c302c bytes 01541e94
- 004c3014 ["INT_ADD", "register:40f0:8", ["const:4c3014:8", "const:4:8"]]
- 004c3014 ["CALL", null, ["callee:00c58040:8"]]
+ 004c3054 ["INT_ADD", "register:40f0:8", ["const:4c3054:8", "const:4:8"]]
+ 004c3054 ["CALL", null, ["callee:00c58040:8"]]
- 004c3014 bytes d7531e94
+ 004c3054 bytes fb531e94
- 004c3084 ["INT_ADD", "register:40f0:8", ["const:4c3084:8", "const:4:8"]]
- 004c3084 ["CALL", null, ["callee:00c58040:8"]]
+ 004c30c4 ["INT_ADD", "register:40f0:8", ["const:4c30c4:8", "const:4:8"]]
+ 004c30c4 ["CALL", null, ["callee:00c58040:8"]]
- 004c3084 bytes bb531e94
+ 004c30c4 bytes df531e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcbff70f895694ba147c71b5b3eab565"></a>

### [`004c320c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c3/004c320c.md) → [`004c324c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c324c.md) _ZN5Botan14Entropy_Source6createERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "004c3310",
      "incomplete_value": false,
      "site": "004c3318",
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
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c32d0",
      "incomplete_value": false,
      "site": "004c32d8",
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
            "const:c88:8"
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
      "004c3318",
      "DATA",
      [
        "storage",
        "00c69c88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004c3318",
      "DATA",
      [
        "storage",
        "00c69d58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c32c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c3/004c320c.md#insn-004c32c8) · [`004c32d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c3/004c320c.md#insn-004c32d0)
- 新版 [`004c3308`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c324c.md#insn-004c3308) · [`004c3310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c324c.md#insn-004c3310)

~~~diff
- 004c32c8 ["INT_ADD", "register:40f0:8", ["const:4c32c8:8", "const:4:8"]]
- 004c32c8 ["CALL", null, ["callee:00c57f60:8"]]
+ 004c3308 ["INT_ADD", "register:40f0:8", ["const:4c3308:8", "const:4:8"]]
+ 004c3308 ["CALL", null, ["callee:00c57f60:8"]]
- 004c32c8 bytes f2521e94
+ 004c3308 bytes 16531e94
- 004c32d0 ["COPY", "tmp:0:8", ["const:c88:8"]]
- 004c32d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004c32d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004c32d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004c3310 ["COPY", "tmp:0:8", ["const:d58:8"]]
+ 004c3310 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004c3310 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004c3310 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004c32d0 bytes 29213291
+ 004c3310 bytes 29613591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48f1f3edc345e24111dada208850f464"></a>

### [`004c3b3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c3/004c3b3c.md) → [`004c3b7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3b7c.md) _ZN5Botan15Entropy_Sources14global_sourcesEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 10件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440b00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440b00.md) [`00473540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473540.md) [`004c3e9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c3/004c3e9c.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440b40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440b40.md) [`00473580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/00473580.md) [`004c3edc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3edc.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 87.94% / 新版 87.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `return_value_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c3be4",
      "incomplete_value": false,
      "site": "004c3be8",
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
            "const:360:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c3ba4",
      "incomplete_value": false,
      "site": "004c3ba8",
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
            "const:260:8"
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
      "definition_site": "004c3bf4",
      "incomplete_value": false,
      "site": "004c3c00",
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
            "const:d8a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c3bb4",
      "incomplete_value": false,
      "site": "004c3bc0",
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
            "const:d59:8"
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
      "definition_site": "004c3c0c",
      "incomplete_value": false,
      "site": "004c3c14",
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
            "const:bd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c3bcc",
      "incomplete_value": false,
      "site": "004c3bd4",
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
            "const:ba1:8"
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
      "004c3ba8",
      "READ",
      [
        "storage",
        "00ca5260",
        null,
        "undefined1"
      ]
    ],
    [
      "004c3bc4",
      "DATA",
      [
        "storage",
        "00ca5248",
        null,
        null
      ]
    ],
    [
      "004c3be4",
      "PARAM",
      [
        "storage",
        "00ca5260",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "004c3ba8",
      "READ",
      [
        "storage",
        "00ca5360",
        null,
        "undefined1"
      ]
    ],
    [
      "004c3bc4",
      "DATA",
      [
        "storage",
        "00ca5348",
        null,
        null
      ]
    ],
    [
      "004c3be4",
      "PARAM",
      [
        "storage",
        "00ca5360",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c3ba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c3/004c3b3c.md#insn-004c3ba8) · [`004c3bc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c3/004c3b3c.md#insn-004c3bc0) · [`004c3bd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c3/004c3b3c.md#insn-004c3bd4)
- 新版 [`004c3be8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3b7c.md#insn-004c3be8) · [`004c3c00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3b7c.md#insn-004c3c00) · [`004c3c14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3b7c.md#insn-004c3c14)

~~~diff
- 004c3ba8 ["INT_ADD", "register:40f0:8", ["const:4c3ba8:8", "const:4:8"]]
- 004c3ba8 ["CALL", null, ["callee:00c57f20:8"]]
+ 004c3be8 ["INT_ADD", "register:40f0:8", ["const:4c3be8:8", "const:4:8"]]
+ 004c3be8 ["CALL", null, ["callee:00c57f20:8"]]
- 004c3ba8 bytes aa501e94
+ 004c3be8 bytes ce501e94
- 004c3bc0 ["INT_ADD", "register:40f0:8", ["const:4c3bc0:8", "const:4:8"]]
- 004c3bc0 ["CALL", null, ["callee:0043de18:8"]]
+ 004c3c00 ["INT_ADD", "register:40f0:8", ["const:4c3c00:8", "const:4:8"]]
+ 004c3c00 ["CALL", null, ["callee:0043de18:8"]]
- 004c3bc0 bytes 86e8fd97
+ 004c3c00 bytes 86e8fd97
- 004c3bd4 ["INT_ADD", "register:40f0:8", ["const:4c3bd4:8", "const:4:8"]]
- 004c3bd4 ["CALL", null, ["callee:0043de18:8"]]
+ 004c3c14 ["INT_ADD", "register:40f0:8", ["const:4c3c14:8", "const:4:8"]]
+ 004c3c14 ["CALL", null, ["callee:0043de18:8"]]
- 004c3bd4 bytes 81e8fd97
+ 004c3c14 bytes 81e8fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10a6f8816799aa8554859541583414d1"></a>

### [`004c3f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c3/004c3f18.md) → [`004c3f58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3f58.md) _ZN5Botan19StreamCipher_FilterC1EPNS_12StreamCipherE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00543c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543c5c.md) [`00c37ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ba4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00543c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543c9c.md) [`00c37c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c40.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c3f8c",
      "incomplete_value": true,
      "site": "004c3f94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c3f4c",
      "incomplete_value": true,
      "site": "004c3f54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c3fc8",
      "incomplete_value": true,
      "site": "004c3fd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c3f88",
      "incomplete_value": true,
      "site": "004c3f90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c4048",
      "incomplete_value": true,
      "site": "004c4050",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eb8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c4008",
      "incomplete_value": true,
      "site": "004c4010",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004c3f78",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "004c3f94",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c3fbc",
      "READ",
      [
        "storage",
        "00c9ae78",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c3f78",
      "READ",
      [
        "storage",
        "00c9af40",
        null,
        "pointer"
      ]
    ],
    [
      "004c3f94",
      "DATA",
      [
        "storage",
        "00c66aa8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c3fbc",
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

- 旧版 [`004c4010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c3/004c3f18.md#insn-004c4010) · [`004c3f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c3/004c3f18.md#insn-004c3f38) · [`004c3f6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c3/004c3f18.md#insn-004c3f6c)
- 新版 [`004c4050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3f58.md#insn-004c4050) · [`004c3f78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3f58.md#insn-004c3f78) · [`004c3fac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c3/004c3f58.md#insn-004c3fac)

~~~diff
- 004c4010 ["INT_ADD", "register:40f0:8", ["const:4c4010:8", "const:4:8"]]
- 004c4010 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004c4050 ["INT_ADD", "register:40f0:8", ["const:4c4050:8", "const:4:8"]]
+ 004c4050 ["CALL", null, ["callee:00c57fe0:8"]]
- 004c4010 bytes c04f1e94
+ 004c4050 bytes e44f1e94
- 004c3f38 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
- 004c3f38 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c3f78 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f40:8"]]
+ 004c3f78 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c3f38 bytes 083947f9
+ 004c3f78 bytes 08a147f9
- 004c3f6c ["INT_ADD", "register:40f0:8", ["const:4c3f6c:8", "const:4:8"]]
- 004c3f6c ["CALL", null, ["callee:00543c9c:8"]]
+ 004c3fac ["INT_ADD", "register:40f0:8", ["const:4c3fac:8", "const:4:8"]]
+ 004c3fac ["CALL", null, ["callee:00543c9c:8"]]
- 004c3f6c bytes 3cff0194
+ 004c3fac bytes 3cff0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7dfdda951c59c2d630d574af585ff5e6"></a>

### [`004c4068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c4068.md) → [`004c40a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c40a8.md) _ZN5Botan19StreamCipher_FilterC1EPNS_12StreamCipherERKNS_11OctetStringE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`004bca00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bca00.md) [`00543c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543c5c.md) [`00c37ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ba4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`004bca40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bca40.md) [`00543c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543c9c.md) [`00c37c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c40.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c40e4",
      "incomplete_value": true,
      "site": "004c40ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c4124",
      "incomplete_value": true,
      "site": "004c412c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c40e4",
      "incomplete_value": true,
      "site": "004c40ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c41b8",
      "incomplete_value": true,
      "site": "004c41c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eb8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c4178",
      "incomplete_value": true,
      "site": "004c4180",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004c40d0",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "004c40ec",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c4114",
      "READ",
      [
        "storage",
        "00c9ae78",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c40d0",
      "READ",
      [
        "storage",
        "00c9af40",
        null,
        "pointer"
      ]
    ],
    [
      "004c40ec",
      "DATA",
      [
        "storage",
        "00c66aa8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c4114",
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

- 旧版 [`004c4180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c4068.md#insn-004c4180) · [`004c4090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c4068.md#insn-004c4090) · [`004c40c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c4068.md#insn-004c40c4)
- 新版 [`004c41c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c40a8.md#insn-004c41c0) · [`004c40d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c40a8.md#insn-004c40d0) · [`004c4104`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c40a8.md#insn-004c4104)

~~~diff
- 004c4180 ["INT_ADD", "register:40f0:8", ["const:4c4180:8", "const:4:8"]]
- 004c4180 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004c41c0 ["INT_ADD", "register:40f0:8", ["const:4c41c0:8", "const:4:8"]]
+ 004c41c0 ["CALL", null, ["callee:00c57fe0:8"]]
- 004c4180 bytes 644f1e94
+ 004c41c0 bytes 884f1e94
- 004c4090 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e70:8"]]
- 004c4090 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c40d0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f40:8"]]
+ 004c40d0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c4090 bytes 293947f9
+ 004c40d0 bytes 29a147f9
- 004c40c4 ["INT_ADD", "register:40f0:8", ["const:4c40c4:8", "const:4:8"]]
- 004c40c4 ["CALL", null, ["callee:00543c9c:8"]]
+ 004c4104 ["INT_ADD", "register:40f0:8", ["const:4c4104:8", "const:4:8"]]
+ 004c4104 ["CALL", null, ["callee:00543c9c:8"]]
- 004c40c4 bytes e6fe0194
+ 004c4104 bytes e6fe0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99471a894b83dbe6cdd167e79ef645b4"></a>

### [`004c4200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c4200.md) → [`004c4240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4240.md) _ZN5Botan19StreamCipher_FilterC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`00543c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543c5c.md) [`00c37ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ba4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00543c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543c9c.md) [`00c37c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c40.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.04% / 新版 89.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c4274",
      "incomplete_value": true,
      "site": "004c427c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c42b4",
      "incomplete_value": true,
      "site": "004c42bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c4274",
      "incomplete_value": true,
      "site": "004c427c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c4354",
      "incomplete_value": true,
      "site": "004c435c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eb8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c4314",
      "incomplete_value": true,
      "site": "004c431c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004c4260",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "004c427c",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c42a4",
      "READ",
      [
        "storage",
        "00c9ae78",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c4260",
      "READ",
      [
        "storage",
        "00c9af40",
        null,
        "pointer"
      ]
    ],
    [
      "004c427c",
      "DATA",
      [
        "storage",
        "00c66aa8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c42a4",
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

- 旧版 [`004c431c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c4200.md#insn-004c431c) · [`004c4220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c4200.md#insn-004c4220) · [`004c4254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c4200.md#insn-004c4254)
- 新版 [`004c435c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4240.md#insn-004c435c) · [`004c4260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4240.md#insn-004c4260) · [`004c4294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4240.md#insn-004c4294)

~~~diff
- 004c431c ["INT_ADD", "register:40f0:8", ["const:4c431c:8", "const:4:8"]]
- 004c431c ["CALL", null, ["callee:00c57fe0:8"]]
+ 004c435c ["INT_ADD", "register:40f0:8", ["const:4c435c:8", "const:4:8"]]
+ 004c435c ["CALL", null, ["callee:00c57fe0:8"]]
- 004c431c bytes fd4e1e94
+ 004c435c bytes 214f1e94
- 004c4220 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
- 004c4220 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c4260 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f40:8"]]
+ 004c4260 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c4220 bytes 083947f9
+ 004c4260 bytes 08a147f9
- 004c4254 ["INT_ADD", "register:40f0:8", ["const:4c4254:8", "const:4:8"]]
- 004c4254 ["CALL", null, ["callee:00543c9c:8"]]
+ 004c4294 ["INT_ADD", "register:40f0:8", ["const:4c4294:8", "const:4:8"]]
+ 004c4294 ["CALL", null, ["callee:00543c9c:8"]]
- 004c4254 bytes 82fe0194
+ 004c4294 bytes 82fe0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50c901d1d7770b583a2c5e8c77e14680"></a>

### [`004c4394`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c4394.md) → [`004c43d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c43d4.md) _ZN5Botan12StreamCipher15create_or_throwERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58e50.md) · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`00c58f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58f20.md) · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

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
      "definition_site": "004c444c",
      "incomplete_value": false,
      "site": "004c4454",
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
            "const:260:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c440c",
      "incomplete_value": false,
      "site": "004c4414",
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
            "const:2b4:8"
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
      "definition_site": "004c448c",
      "incomplete_value": true,
      "site": "004c4498",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c444c",
      "incomplete_value": true,
      "site": "004c4458",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e28:8"
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
      "definition_site": "004c4488",
      "incomplete_value": false,
      "site": "004c4498",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004c4448",
      "incomplete_value": false,
      "site": "004c4458",
      "value": [
        "leaf",
        "const:535868:8"
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
      "004c444c",
      "PARAM",
      [
        "storage",
        "002ba2b4",
        null,
        "string"
      ]
    ],
    [
      "004c4488",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004c448c",
      "READ",
      [
        "storage",
        "00c9ae28",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c444c",
      "PARAM",
      [
        "storage",
        "002ba260",
        null,
        "string"
      ]
    ],
    [
      "004c4488",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004c448c",
      "READ",
      [
        "storage",
        "00c9aef8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c4414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c4394.md#insn-004c4414) · [`004c4458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c4394.md#insn-004c4458) · [`004c43c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c4394.md#insn-004c43c8)
- 新版 [`004c4454`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c43d4.md#insn-004c4454) · [`004c4498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c43d4.md#insn-004c4498) · [`004c4408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c43d4.md#insn-004c4408)

~~~diff
- 004c4414 ["INT_ADD", "register:40f0:8", ["const:4c4414:8", "const:4:8"]]
- 004c4414 ["CALL", null, ["callee:0043de18:8"]]
+ 004c4454 ["INT_ADD", "register:40f0:8", ["const:4c4454:8", "const:4:8"]]
+ 004c4454 ["CALL", null, ["callee:0043de18:8"]]
- 004c4414 bytes 71e6fd97
+ 004c4454 bytes 71e6fd97
- 004c4458 ["INT_ADD", "register:40f0:8", ["const:4c4458:8", "const:4:8"]]
- 004c4458 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004c4498 ["INT_ADD", "register:40f0:8", ["const:4c4498:8", "const:4:8"]]
+ 004c4498 ["CALL", null, ["callee:00c57fe0:8"]]
- 004c4458 bytes ae4e1e94
+ 004c4498 bytes d24e1e94
- 004c43c8 ["INT_ADD", "register:40f0:8", ["const:4c43c8:8", "const:4:8"]]
- 004c43c8 ["CALL", null, ["callee:00c58f30:8"]]
+ 004c4408 ["INT_ADD", "register:40f0:8", ["const:4c4408:8", "const:4:8"]]
+ 004c4408 ["CALL", null, ["callee:00c58f30:8"]]
- 004c43c8 bytes a6521e94
+ 004c4408 bytes ca521e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f62b933e43fc6b7a3ea4a6f40733e6f6"></a>

### [`004c44a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c44a8.md) → [`004c44e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c44e8.md) _ZN5Botan19StreamCipher_FilterC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERKNS_11OctetStringE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 10件 [`004bca00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bca00.md) [`00543c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543c5c.md) [`00c37ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ba4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 10件 [`004bca40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bca40.md) [`00543c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543c9c.md) [`00c37c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c40.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c4524",
      "incomplete_value": true,
      "site": "004c452c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c4564",
      "incomplete_value": true,
      "site": "004c456c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c4524",
      "incomplete_value": true,
      "site": "004c452c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c4618",
      "incomplete_value": true,
      "site": "004c4620",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eb8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c45d8",
      "incomplete_value": true,
      "site": "004c45e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004c4510",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "004c452c",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c4554",
      "READ",
      [
        "storage",
        "00c9ae78",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c4510",
      "READ",
      [
        "storage",
        "00c9af40",
        null,
        "pointer"
      ]
    ],
    [
      "004c452c",
      "DATA",
      [
        "storage",
        "00c66aa8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c4554",
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

- 旧版 [`004c45e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c44a8.md#insn-004c45e0) · [`004c44d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c44a8.md#insn-004c44d0) · [`004c4504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c44a8.md#insn-004c4504)
- 新版 [`004c4620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c44e8.md#insn-004c4620) · [`004c4510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c44e8.md#insn-004c4510) · [`004c4544`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c44e8.md#insn-004c4544)

~~~diff
- 004c45e0 ["INT_ADD", "register:40f0:8", ["const:4c45e0:8", "const:4:8"]]
- 004c45e0 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004c4620 ["INT_ADD", "register:40f0:8", ["const:4c4620:8", "const:4:8"]]
+ 004c4620 ["CALL", null, ["callee:00c57fe0:8"]]
- 004c45e0 bytes 4c4e1e94
+ 004c4620 bytes 704e1e94
- 004c44d0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e70:8"]]
- 004c44d0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c4510 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f40:8"]]
+ 004c4510 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c44d0 bytes 293947f9
+ 004c4510 bytes 29a147f9
- 004c4504 ["INT_ADD", "register:40f0:8", ["const:4c4504:8", "const:4:8"]]
- 004c4504 ["CALL", null, ["callee:00543c9c:8"]]
+ 004c4544 ["INT_ADD", "register:40f0:8", ["const:4c4544:8", "const:4:8"]]
+ 004c4544 ["CALL", null, ["callee:00543c9c:8"]]
- 004c4504 bytes d6fd0194
+ 004c4544 bytes d6fd0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44f1ea240886115603ee6761d113a0d4"></a>

### [`004c46f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c46f4.md) → [`004c4734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4734.md) _ZN5Botan11Hash_FilterC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00543c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543c5c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58e70.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00543c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543c9c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58f40.md)

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
      "definition_site": "004c4770",
      "incomplete_value": true,
      "site": "004c4778",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c4730",
      "incomplete_value": true,
      "site": "004c4738",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c47a4",
      "incomplete_value": true,
      "site": "004c47ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c4764",
      "incomplete_value": true,
      "site": "004c476c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004c475c",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "004c4778",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c4798",
      "READ",
      [
        "storage",
        "00c9ae80",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c475c",
      "READ",
      [
        "storage",
        "00c9af40",
        null,
        "pointer"
      ]
    ],
    [
      "004c4778",
      "DATA",
      [
        "storage",
        "00c66aa8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c4798",
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

- 旧版 [`004c471c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c46f4.md#insn-004c471c) · [`004c4750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c46f4.md#insn-004c4750) · [`004c4758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c46f4.md#insn-004c4758)
- 新版 [`004c475c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4734.md#insn-004c475c) · [`004c4790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4734.md#insn-004c4790) · [`004c4798`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4734.md#insn-004c4798)

~~~diff
- 004c471c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e70:8"]]
- 004c471c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c475c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f40:8"]]
+ 004c475c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c471c bytes 293947f9
+ 004c475c bytes 29a147f9
- 004c4750 ["INT_ADD", "register:40f0:8", ["const:4c4750:8", "const:4:8"]]
- 004c4750 ["CALL", null, ["callee:00543c9c:8"]]
+ 004c4790 ["INT_ADD", "register:40f0:8", ["const:4c4790:8", "const:4:8"]]
+ 004c4790 ["CALL", null, ["callee:00543c9c:8"]]
- 004c4750 bytes 43fd0194
+ 004c4790 bytes 43fd0194
- 004c4758 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e80:8"]]
- 004c4758 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c4798 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f50:8"]]
+ 004c4798 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c4758 bytes 084147f9
+ 004c4798 bytes 08a947f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-473d92e6c7282418b8f1315148e83a6f"></a>

### [`004c4818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c4818.md) → [`004c4858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4858.md) _ZN5Botan6FilterC2Ev

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00543c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543c5c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00543c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543c9c.md)

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
      "definition_site": "004c487c",
      "incomplete_value": true,
      "site": "004c4880",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c483c",
      "incomplete_value": true,
      "site": "004c4840",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004c4874",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "004c4880",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "004c4874",
      "READ",
      [
        "storage",
        "00c9af40",
        null,
        "pointer"
      ]
    ],
    [
      "004c4880",
      "DATA",
      [
        "storage",
        "00c66aa8",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c4834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c4818.md#insn-004c4834) · [`004c4838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c4818.md#insn-004c4838) · [`004c4858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c4818.md#insn-004c4858)
- 新版 [`004c4874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4858.md#insn-004c4874) · [`004c4898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4858.md#insn-004c4898)

~~~diff
- 004c4834 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
- 004c4834 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c4874 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f40:8"]]
+ 004c4874 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c4834 bytes 083947f9
+ 004c4874 bytes 08a147f9
- 004c4838 ["COPY", "register:40a0:8", ["register:4000:8"]]
- 004c4838 bytes f40300aa
- 004c4858 ["INT_ADD", "register:40f0:8", ["const:4c4858:8", "const:4:8"]]
- 004c4858 ["CALL", null, ["callee:00543c9c:8"]]
+ 004c4898 ["INT_ADD", "register:40f0:8", ["const:4c4898:8", "const:4:8"]]
+ 004c4898 ["CALL", null, ["callee:00543c9c:8"]]
- 004c4858 bytes 01fd0194
+ 004c4898 bytes 01fd0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9cf0f5798a0edcc7126a63f6b6d4cab0"></a>

### [`004c489c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c489c.md) → [`004c48dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c48dc.md) _ZN5Botan12HashFunction15create_or_throwERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58e70.md) · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`00c58f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58f40.md) · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

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
      "definition_site": "004c4954",
      "incomplete_value": false,
      "site": "004c495c",
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
            "const:f4f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c4914",
      "incomplete_value": false,
      "site": "004c491c",
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
            "const:f9c:8"
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
      "definition_site": "004c4994",
      "incomplete_value": true,
      "site": "004c49a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c4954",
      "incomplete_value": true,
      "site": "004c4960",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e28:8"
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
      "definition_site": "004c4990",
      "incomplete_value": false,
      "site": "004c49a0",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004c4950",
      "incomplete_value": false,
      "site": "004c4960",
      "value": [
        "leaf",
        "const:535868:8"
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
      "004c4954",
      "PARAM",
      [
        "storage",
        "002a1f9c",
        null,
        null
      ]
    ],
    [
      "004c4990",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004c4994",
      "READ",
      [
        "storage",
        "00c9ae28",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c4954",
      "PARAM",
      [
        "storage",
        "002a1f4f",
        null,
        null
      ]
    ],
    [
      "004c4990",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004c4994",
      "READ",
      [
        "storage",
        "00c9aef8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c491c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c489c.md#insn-004c491c) · [`004c4960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c489c.md#insn-004c4960) · [`004c48d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c489c.md#insn-004c48d0)
- 新版 [`004c495c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c48dc.md#insn-004c495c) · [`004c49a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c48dc.md#insn-004c49a0) · [`004c4910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c48dc.md#insn-004c4910)

~~~diff
- 004c491c ["INT_ADD", "register:40f0:8", ["const:4c491c:8", "const:4:8"]]
- 004c491c ["CALL", null, ["callee:0043de18:8"]]
+ 004c495c ["INT_ADD", "register:40f0:8", ["const:4c495c:8", "const:4:8"]]
+ 004c495c ["CALL", null, ["callee:0043de18:8"]]
- 004c491c bytes 2fe5fd97
+ 004c495c bytes 2fe5fd97
- 004c4960 ["INT_ADD", "register:40f0:8", ["const:4c4960:8", "const:4:8"]]
- 004c4960 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004c49a0 ["INT_ADD", "register:40f0:8", ["const:4c49a0:8", "const:4:8"]]
+ 004c49a0 ["CALL", null, ["callee:00c57fe0:8"]]
- 004c4960 bytes 6c4d1e94
+ 004c49a0 bytes 904d1e94
- 004c48d0 ["INT_ADD", "register:40f0:8", ["const:4c48d0:8", "const:4:8"]]
- 004c48d0 ["CALL", null, ["callee:00c58ec0:8"]]
+ 004c4910 ["INT_ADD", "register:40f0:8", ["const:4c4910:8", "const:4:8"]]
+ 004c4910 ["CALL", null, ["callee:00c58ec0:8"]]
- 004c48d0 bytes 48511e94
+ 004c4910 bytes 6c511e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3130312e51d65a2758ce950d26b96bdd"></a>

### [`004c4ad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c4ad4.md) → [`004c4b14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4b14.md) _ZN5Botan10MAC_FilterC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00543c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543c5c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58e80.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00543c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543c9c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58f50.md)

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
      "definition_site": "004c4b50",
      "incomplete_value": true,
      "site": "004c4b58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c4b10",
      "incomplete_value": true,
      "site": "004c4b18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c4b84",
      "incomplete_value": true,
      "site": "004c4b8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c4b44",
      "incomplete_value": true,
      "site": "004c4b4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004c4b3c",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "004c4b58",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c4b78",
      "READ",
      [
        "storage",
        "00c9ae88",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c4b3c",
      "READ",
      [
        "storage",
        "00c9af40",
        null,
        "pointer"
      ]
    ],
    [
      "004c4b58",
      "DATA",
      [
        "storage",
        "00c66aa8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c4b78",
      "READ",
      [
        "storage",
        "00c9af58",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c4afc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c4ad4.md#insn-004c4afc) · [`004c4b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c4ad4.md#insn-004c4b30) · [`004c4b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c4ad4.md#insn-004c4b38)
- 新版 [`004c4b3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4b14.md#insn-004c4b3c) · [`004c4b70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4b14.md#insn-004c4b70) · [`004c4b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4b14.md#insn-004c4b78)

~~~diff
- 004c4afc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e70:8"]]
- 004c4afc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c4b3c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f40:8"]]
+ 004c4b3c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c4afc bytes 293947f9
+ 004c4b3c bytes 29a147f9
- 004c4b30 ["INT_ADD", "register:40f0:8", ["const:4c4b30:8", "const:4:8"]]
- 004c4b30 ["CALL", null, ["callee:00543c9c:8"]]
+ 004c4b70 ["INT_ADD", "register:40f0:8", ["const:4c4b70:8", "const:4:8"]]
+ 004c4b70 ["CALL", null, ["callee:00543c9c:8"]]
- 004c4b30 bytes 4bfc0194
+ 004c4b70 bytes 4bfc0194
- 004c4b38 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e88:8"]]
- 004c4b38 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c4b78 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f58:8"]]
+ 004c4b78 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c4b38 bytes 084547f9
+ 004c4b78 bytes 08ad47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6130bc03cf86fbcb5ed9bb162c0064ef"></a>

### [`004c4bf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c4bf8.md) → [`004c4c38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4c38.md) _ZN5Botan25MessageAuthenticationCode15create_or_throwERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58e80.md) · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`00c58f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58f50.md) · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

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
      "definition_site": "004c4cb0",
      "incomplete_value": false,
      "site": "004c4cb8",
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
            "const:707:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c4c70",
      "incomplete_value": false,
      "site": "004c4c78",
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
            "const:763:8"
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
      "definition_site": "004c4cf0",
      "incomplete_value": true,
      "site": "004c4cfc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c4cb0",
      "incomplete_value": true,
      "site": "004c4cbc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e28:8"
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
      "definition_site": "004c4cec",
      "incomplete_value": false,
      "site": "004c4cfc",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004c4cac",
      "incomplete_value": false,
      "site": "004c4cbc",
      "value": [
        "leaf",
        "const:535868:8"
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
      "004c4cb0",
      "PARAM",
      [
        "storage",
        "002ac763",
        null,
        null
      ]
    ],
    [
      "004c4cec",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004c4cf0",
      "READ",
      [
        "storage",
        "00c9ae28",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c4cb0",
      "PARAM",
      [
        "storage",
        "002ac707",
        null,
        null
      ]
    ],
    [
      "004c4cec",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004c4cf0",
      "READ",
      [
        "storage",
        "00c9aef8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c4c78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c4bf8.md#insn-004c4c78) · [`004c4cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c4bf8.md#insn-004c4cbc) · [`004c4c2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c4bf8.md#insn-004c4c2c)
- 新版 [`004c4cb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4c38.md#insn-004c4cb8) · [`004c4cfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4c38.md#insn-004c4cfc) · [`004c4c6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4c38.md#insn-004c4c6c)

~~~diff
- 004c4c78 ["INT_ADD", "register:40f0:8", ["const:4c4c78:8", "const:4:8"]]
- 004c4c78 ["CALL", null, ["callee:0043de18:8"]]
+ 004c4cb8 ["INT_ADD", "register:40f0:8", ["const:4c4cb8:8", "const:4:8"]]
+ 004c4cb8 ["CALL", null, ["callee:0043de18:8"]]
- 004c4c78 bytes 58e4fd97
+ 004c4cb8 bytes 58e4fd97
- 004c4cbc ["INT_ADD", "register:40f0:8", ["const:4c4cbc:8", "const:4:8"]]
- 004c4cbc ["CALL", null, ["callee:00c57fe0:8"]]
+ 004c4cfc ["INT_ADD", "register:40f0:8", ["const:4c4cfc:8", "const:4:8"]]
+ 004c4cfc ["CALL", null, ["callee:00c57fe0:8"]]
- 004c4cbc bytes 954c1e94
+ 004c4cfc bytes b94c1e94
- 004c4c2c ["INT_ADD", "register:40f0:8", ["const:4c4c2c:8", "const:4:8"]]
- 004c4c2c ["CALL", null, ["callee:00c58f60:8"]]
+ 004c4c6c ["INT_ADD", "register:40f0:8", ["const:4c4c6c:8", "const:4:8"]]
+ 004c4c6c ["CALL", null, ["callee:00c58f60:8"]]
- 004c4c2c bytes 99501e94
+ 004c4c6c bytes bd501e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2239e8c3bc625ff0944aa2ff999a0155"></a>

### [`004c4d0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c4d0c.md) → [`004c4d4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4d4c.md) _ZN5Botan10MAC_FilterC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERKNS_11OctetStringEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`004bca00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bca00.md) [`00543c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543c5c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58e80.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004bca40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bc/004bca40.md) [`00543c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543c9c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58f50.md)

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
      "definition_site": "004c4d8c",
      "incomplete_value": true,
      "site": "004c4d94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c4d4c",
      "incomplete_value": true,
      "site": "004c4d54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c4dc0",
      "incomplete_value": true,
      "site": "004c4dc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c4d80",
      "incomplete_value": true,
      "site": "004c4d88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004c4d74",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "004c4d94",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c4db4",
      "READ",
      [
        "storage",
        "00c9ae88",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c4d74",
      "READ",
      [
        "storage",
        "00c9af40",
        null,
        "pointer"
      ]
    ],
    [
      "004c4d94",
      "DATA",
      [
        "storage",
        "00c66aa8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c4db4",
      "READ",
      [
        "storage",
        "00c9af58",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c4d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c4d0c.md#insn-004c4d34) · [`004c4d50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c4d0c.md#insn-004c4d50) · [`004c4d6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c4d0c.md#insn-004c4d6c)
- 新版 [`004c4d74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4d4c.md#insn-004c4d74) · [`004c4dac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4d4c.md#insn-004c4dac)

~~~diff
- 004c4d34 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e70:8"]]
- 004c4d34 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c4d74 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f40:8"]]
+ 004c4d74 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c4d34 bytes 293947f9
+ 004c4d74 bytes 29a147f9
- 004c4d50 ["COPY", "register:40b8:8", ["register:4000:8"]]
- 004c4d50 bytes f70300aa
- 004c4d6c ["INT_ADD", "register:40f0:8", ["const:4c4d6c:8", "const:4:8"]]
- 004c4d6c ["CALL", null, ["callee:00543c9c:8"]]
+ 004c4dac ["INT_ADD", "register:40f0:8", ["const:4c4dac:8", "const:4:8"]]
+ 004c4dac ["CALL", null, ["callee:00543c9c:8"]]
- 004c4d6c bytes bcfb0194
+ 004c4dac bytes bcfb0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0cb295c2da53f6626b43a9d408c4d82a"></a>

### [`004c4f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c4f8c.md) → [`004c4fcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4fcc.md) _ZN5Botan12Keyed_Filter6set_ivERKNS_11OctetStringE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c58d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58d90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c58e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58e60.md)

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
      "definition_site": "004c5080",
      "incomplete_value": true,
      "site": "004c508c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c5040",
      "incomplete_value": true,
      "site": "004c504c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e40:8"
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
      "definition_site": "004c507c",
      "incomplete_value": false,
      "site": "004c508c",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004c503c",
      "incomplete_value": false,
      "site": "004c504c",
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
      "004c507c",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004c5080",
      "READ",
      [
        "storage",
        "00c9ae40",
        null,
        "pointer"
      ]
    ],
    [
      "004c5080",
      "PARAM",
      [
        "storage",
        "00c664b0",
        "_ZTIN5Botan17Invalid_IV_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004c507c",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004c5080",
      "READ",
      [
        "storage",
        "00c9af10",
        null,
        "pointer"
      ]
    ],
    [
      "004c5080",
      "PARAM",
      [
        "storage",
        "00c66580",
        "_ZTIN5Botan17Invalid_IV_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c504c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c4f8c.md#insn-004c504c) · [`004c4fec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c4f8c.md#insn-004c4fec) · [`004c5004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c4f8c.md#insn-004c5004)
- 新版 [`004c508c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4fcc.md#insn-004c508c) · [`004c502c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4fcc.md#insn-004c502c) · [`004c5044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c4/004c4fcc.md#insn-004c5044)

~~~diff
- 004c504c ["INT_ADD", "register:40f0:8", ["const:4c504c:8", "const:4:8"]]
- 004c504c ["CALL", null, ["callee:00c57fe0:8"]]
+ 004c508c ["INT_ADD", "register:40f0:8", ["const:4c508c:8", "const:4:8"]]
+ 004c508c ["CALL", null, ["callee:00c57fe0:8"]]
- 004c504c bytes b14b1e94
+ 004c508c bytes d54b1e94
- 004c4fec ["INT_ADD", "register:40f0:8", ["const:4c4fec:8", "const:4:8"]]
- 004c4fec ["CALL", null, ["callee:00c57fc0:8"]]
+ 004c502c ["INT_ADD", "register:40f0:8", ["const:4c502c:8", "const:4:8"]]
+ 004c502c ["CALL", null, ["callee:00c57fc0:8"]]
- 004c4fec bytes c14b1e94
+ 004c502c bytes e54b1e94
- 004c5004 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c5004 ["INT_ADD", "register:40f0:8", ["const:4c5004:8", "const:4:8"]]
- 004c5004 ["CALLIND", null, ["register:0:8"]]
+ 004c5044 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c5044 ["INT_ADD", "register:40f0:8", ["const:4c5044:8", "const:4:8"]]
+ 004c5044 ["CALLIND", null, ["register:0:8"]]
- 004c5004 bytes 20013fd6
+ 004c5044 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a3778269b3d3a3c495f64c43dd79a3f"></a>

### [`004c50a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c50a0.md) → [`004c50e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c50e0.md) _ZN5Botan5ChainC1EPNS_6FilterES2_S2_S2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00543c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543c5c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00543c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543c9c.md)

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
      "definition_site": "004c5118",
      "incomplete_value": true,
      "site": "004c511c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c50d8",
      "incomplete_value": true,
      "site": "004c50dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c5148",
      "incomplete_value": true,
      "site": "004c514c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c5108",
      "incomplete_value": true,
      "site": "004c510c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004c5100",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "004c511c",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c513c",
      "READ",
      [
        "storage",
        "00c9ae90",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c5100",
      "READ",
      [
        "storage",
        "00c9af40",
        null,
        "pointer"
      ]
    ],
    [
      "004c511c",
      "DATA",
      [
        "storage",
        "00c66aa8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c513c",
      "READ",
      [
        "storage",
        "00c9af60",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c50c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c50a0.md#insn-004c50c0) · [`004c50f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c50a0.md#insn-004c50f4) · [`004c50fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c50a0.md#insn-004c50fc)
- 新版 [`004c5100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c50e0.md#insn-004c5100) · [`004c5134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c50e0.md#insn-004c5134) · [`004c513c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c50e0.md#insn-004c513c)

~~~diff
- 004c50c0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
- 004c50c0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c5100 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f40:8"]]
+ 004c5100 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c50c0 bytes 083947f9
+ 004c5100 bytes 08a147f9
- 004c50f4 ["INT_ADD", "register:40f0:8", ["const:4c50f4:8", "const:4:8"]]
- 004c50f4 ["CALL", null, ["callee:00543c9c:8"]]
+ 004c5134 ["INT_ADD", "register:40f0:8", ["const:4c5134:8", "const:4:8"]]
+ 004c5134 ["CALL", null, ["callee:00543c9c:8"]]
- 004c50f4 bytes dafa0194
+ 004c5134 bytes dafa0194
- 004c50fc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e90:8"]]
- 004c50fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c513c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f60:8"]]
+ 004c513c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c50fc bytes 084947f9
+ 004c513c bytes 08b147f9
~~~


<a id="compare-3baa179513db8cd8e74ca166677cf420"></a>

### [`004c5268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c5268.md) → [`004c52a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c52a8.md) _ZN5Botan5ChainC1EPPNS_6FilterEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00543c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543c5c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00543c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543c9c.md)

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
      "definition_site": "004c52d4",
      "incomplete_value": true,
      "site": "004c52d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c5294",
      "incomplete_value": true,
      "site": "004c5298",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c5304",
      "incomplete_value": true,
      "site": "004c5308",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c52c4",
      "incomplete_value": true,
      "site": "004c52c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004c52c4",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "004c52d8",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c52f8",
      "READ",
      [
        "storage",
        "00c9ae90",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c52c4",
      "READ",
      [
        "storage",
        "00c9af40",
        null,
        "pointer"
      ]
    ],
    [
      "004c52d8",
      "DATA",
      [
        "storage",
        "00c66aa8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c52f8",
      "READ",
      [
        "storage",
        "00c9af60",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c5284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c5268.md#insn-004c5284) · [`004c52b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c5268.md#insn-004c52b0) · [`004c52b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c5268.md#insn-004c52b8)
- 新版 [`004c52c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c52a8.md#insn-004c52c4) · [`004c52f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c52a8.md#insn-004c52f0) · [`004c52f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c52a8.md#insn-004c52f8)

~~~diff
- 004c5284 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
- 004c5284 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c52c4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f40:8"]]
+ 004c52c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c5284 bytes 083947f9
+ 004c52c4 bytes 08a147f9
- 004c52b0 ["INT_ADD", "register:40f0:8", ["const:4c52b0:8", "const:4:8"]]
- 004c52b0 ["CALL", null, ["callee:00543c9c:8"]]
+ 004c52f0 ["INT_ADD", "register:40f0:8", ["const:4c52f0:8", "const:4:8"]]
+ 004c52f0 ["CALL", null, ["callee:00543c9c:8"]]
- 004c52b0 bytes 6bfa0194
+ 004c52f0 bytes 6bfa0194
- 004c52b8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e90:8"]]
- 004c52b8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c52f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f60:8"]]
+ 004c52f8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c52b8 bytes 084947f9
+ 004c52f8 bytes 08b147f9
~~~


<a id="compare-6419b87c7f5ca10bddddb7d1f2f91c65"></a>

### [`004c5388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c5388.md) → [`004c53c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c53c8.md) _ZN5Botan4ForkC1EPNS_6FilterES2_S2_S2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00543c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543c5c.md) [`00543d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543d9c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00543c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543c9c.md) [`00543ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543ddc.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

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
      "definition_site": "004c5410",
      "incomplete_value": true,
      "site": "004c5418",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c53d0",
      "incomplete_value": true,
      "site": "004c53d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c5448",
      "incomplete_value": true,
      "site": "004c5450",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c5408",
      "incomplete_value": true,
      "site": "004c5410",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004c53f4",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "004c5418",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c543c",
      "READ",
      [
        "storage",
        "00c9ae98",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c53f4",
      "READ",
      [
        "storage",
        "00c9af40",
        null,
        "pointer"
      ]
    ],
    [
      "004c5418",
      "DATA",
      [
        "storage",
        "00c66aa8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c543c",
      "READ",
      [
        "storage",
        "00c9af68",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c53b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c5388.md#insn-004c53b4) · [`004c53d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c5388.md#insn-004c53d4) · [`004c53f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c5388.md#insn-004c53f0)
- 新版 [`004c53f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c53c8.md#insn-004c53f4) · [`004c5430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c53c8.md#insn-004c5430)

~~~diff
- 004c53b4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e70:8"]]
- 004c53b4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c53f4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f40:8"]]
+ 004c53f4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c53b4 bytes 293947f9
+ 004c53f4 bytes 29a147f9
- 004c53d4 ["COPY", "register:40c0:8", ["register:4000:8"]]
- 004c53d4 bytes f80300aa
- 004c53f0 ["INT_ADD", "register:40f0:8", ["const:4c53f0:8", "const:4:8"]]
- 004c53f0 ["CALL", null, ["callee:00543c9c:8"]]
+ 004c5430 ["INT_ADD", "register:40f0:8", ["const:4c5430:8", "const:4:8"]]
+ 004c5430 ["CALL", null, ["callee:00543c9c:8"]]
- 004c53f0 bytes 1bfa0194
+ 004c5430 bytes 1bfa0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e2a56be1747b9af2c92924f7cb5d560"></a>

### [`004c54e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c54e0.md) → [`004c5520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c5520.md) _ZN5Botan4ForkC1EPPNS_6FilterEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00543c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543c5c.md) [`00543d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543d9c.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00543c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543c9c.md) [`00543ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543ddc.md)

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
      "definition_site": "004c554c",
      "incomplete_value": true,
      "site": "004c5550",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c550c",
      "incomplete_value": true,
      "site": "004c5510",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c5580",
      "incomplete_value": true,
      "site": "004c5588",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c5540",
      "incomplete_value": true,
      "site": "004c5548",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004c553c",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "004c5550",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c5570",
      "READ",
      [
        "storage",
        "00c9ae98",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c553c",
      "READ",
      [
        "storage",
        "00c9af40",
        null,
        "pointer"
      ]
    ],
    [
      "004c5550",
      "DATA",
      [
        "storage",
        "00c66aa8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c5570",
      "READ",
      [
        "storage",
        "00c9af68",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c54fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c54e0.md#insn-004c54fc) · [`004c5528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c54e0.md#insn-004c5528) · [`004c5530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c54e0.md#insn-004c5530)
- 新版 [`004c553c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c5520.md#insn-004c553c) · [`004c5568`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c5520.md#insn-004c5568) · [`004c5570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c5520.md#insn-004c5570)

~~~diff
- 004c54fc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
- 004c54fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c553c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f40:8"]]
+ 004c553c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c54fc bytes 083947f9
+ 004c553c bytes 08a147f9
- 004c5528 ["INT_ADD", "register:40f0:8", ["const:4c5528:8", "const:4:8"]]
- 004c5528 ["CALL", null, ["callee:00543c9c:8"]]
+ 004c5568 ["INT_ADD", "register:40f0:8", ["const:4c5568:8", "const:4:8"]]
+ 004c5568 ["CALL", null, ["callee:00543c9c:8"]]
- 004c5528 bytes cdf90194
+ 004c5568 bytes cdf90194
- 004c5530 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e98:8"]]
- 004c5530 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c5570 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f68:8"]]
+ 004c5570 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c5530 bytes 084d47f9
+ 004c5570 bytes 08b547f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6b015e9a31f88b91ead41bece520fff"></a>

### [`004c55e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c55e8.md) → [`004c5628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c5628.md) _ZN5Botan15Buffered_FilterC2Emm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58ea0.md) · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)
- 新版 呼出元 1件 [`00c58f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58f70.md) · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)

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
      "definition_site": "004c565c",
      "incomplete_value": true,
      "site": "004c565c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c561c",
      "incomplete_value": true,
      "site": "004c561c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c56c8",
      "incomplete_value": false,
      "site": "004c56d0",
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
            "const:11d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c5688",
      "incomplete_value": false,
      "site": "004c5690",
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
            "const:16a:8"
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
      "definition_site": "004c5700",
      "incomplete_value": true,
      "site": "004c570c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c56c0",
      "incomplete_value": true,
      "site": "004c56cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004c5650",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "004c565c",
      "DATA",
      [
        "storage",
        "00c668a8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004c56c8",
      "PARAM",
      [
        "storage",
        "002a416a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004c5650",
      "READ",
      [
        "storage",
        "00c9af70",
        null,
        "pointer"
      ]
    ],
    [
      "004c565c",
      "DATA",
      [
        "storage",
        "00c66978",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004c56c8",
      "PARAM",
      [
        "storage",
        "002a411d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c5690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c55e8.md#insn-004c5690) · [`004c56cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c55e8.md#insn-004c56cc) · [`004c56ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c55e8.md#insn-004c56ec)
- 新版 [`004c56d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c5628.md#insn-004c56d0) · [`004c570c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c5628.md#insn-004c570c) · [`004c572c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c5628.md#insn-004c572c)

~~~diff
- 004c5690 ["INT_ADD", "register:40f0:8", ["const:4c5690:8", "const:4:8"]]
- 004c5690 ["CALL", null, ["callee:0043de18:8"]]
+ 004c56d0 ["INT_ADD", "register:40f0:8", ["const:4c56d0:8", "const:4:8"]]
+ 004c56d0 ["CALL", null, ["callee:0043de18:8"]]
- 004c5690 bytes d2e1fd97
+ 004c56d0 bytes d2e1fd97
- 004c56cc ["INT_ADD", "register:40f0:8", ["const:4c56cc:8", "const:4:8"]]
- 004c56cc ["CALL", null, ["callee:00c57fe0:8"]]
+ 004c570c ["INT_ADD", "register:40f0:8", ["const:4c570c:8", "const:4:8"]]
+ 004c570c ["CALL", null, ["callee:00c57fe0:8"]]
- 004c56cc bytes 114a1e94
+ 004c570c bytes 354a1e94
- 004c56ec ["INT_ADD", "register:40f0:8", ["const:4c56ec:8", "const:4:8"]]
- 004c56ec ["CALL", null, ["callee:0043de18:8"]]
+ 004c572c ["INT_ADD", "register:40f0:8", ["const:4c572c:8", "const:4:8"]]
+ 004c572c ["CALL", null, ["callee:0043de18:8"]]
- 004c56ec bytes bbe1fd97
+ 004c572c bytes bbe1fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78902a4246ce6ca09d3cf51c9115ef8b"></a>

### [`004c58d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c58d4.md) → [`004c5914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c5914.md) _ZN5Botan15Buffered_Filter7end_msgEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58ec0.md) · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`00c58f90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58f90.md) · 呼出先 6件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

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
      "definition_site": "004c59dc",
      "incomplete_value": false,
      "site": "004c59e4",
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
            "const:ef:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c599c",
      "incomplete_value": false,
      "site": "004c59a4",
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
            "const:13c:8"
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
      "definition_site": "004c5a14",
      "incomplete_value": true,
      "site": "004c5a20",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c59d4",
      "incomplete_value": true,
      "site": "004c59e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c5a10",
      "incomplete_value": false,
      "site": "004c5a20",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004c59d0",
      "incomplete_value": false,
      "site": "004c59e0",
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
      "004c59dc",
      "PARAM",
      [
        "storage",
        "002a313c",
        null,
        "string"
      ]
    ],
    [
      "004c5a10",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004c5a14",
      "READ",
      [
        "storage",
        "00c9ad88",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c59dc",
      "PARAM",
      [
        "storage",
        "002a30ef",
        null,
        "string"
      ]
    ],
    [
      "004c5a10",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004c5a14",
      "READ",
      [
        "storage",
        "00c9ae58",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c59a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c58d4.md#insn-004c59a4) · [`004c59e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c58d4.md#insn-004c59e0) · [`004c5940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c58d4.md#insn-004c5940)
- 新版 [`004c59e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c5914.md#insn-004c59e4) · [`004c5a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c5914.md#insn-004c5a20) · [`004c5980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c5914.md#insn-004c5980)

~~~diff
- 004c59a4 ["INT_ADD", "register:40f0:8", ["const:4c59a4:8", "const:4:8"]]
- 004c59a4 ["CALL", null, ["callee:0043de18:8"]]
+ 004c59e4 ["INT_ADD", "register:40f0:8", ["const:4c59e4:8", "const:4:8"]]
+ 004c59e4 ["CALL", null, ["callee:0043de18:8"]]
- 004c59a4 bytes 0de1fd97
+ 004c59e4 bytes 0de1fd97
- 004c59e0 ["INT_ADD", "register:40f0:8", ["const:4c59e0:8", "const:4:8"]]
- 004c59e0 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004c5a20 ["INT_ADD", "register:40f0:8", ["const:4c5a20:8", "const:4:8"]]
+ 004c5a20 ["CALL", null, ["callee:00c57fe0:8"]]
- 004c59e0 bytes 4c491e94
+ 004c5a20 bytes 70491e94
- 004c5940 ["COPY", "register:0:8", ["register:4040:8"]]
- 004c5940 ["INT_ADD", "register:40f0:8", ["const:4c5940:8", "const:4:8"]]
- 004c5940 ["CALLIND", null, ["register:0:8"]]
+ 004c5980 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c5980 ["INT_ADD", "register:40f0:8", ["const:4c5980:8", "const:4:8"]]
+ 004c5980 ["CALLIND", null, ["register:0:8"]]
- 004c5940 bytes 00013fd6
+ 004c5980 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f3774522653493a271fca78985b98ad"></a>

### [`004c5a30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c5a30.md) → [`004c5a70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c5a70.md) _ZN5Botan18Cipher_Mode_FilterC1EPNS_11Cipher_ModeE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c58f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58f90.md) · 呼出先 7件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md) [`00543c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543c5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)
- 新版 呼出元 1件 [`00c59060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59060.md) · 呼出先 7件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`004b3548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3548.md) [`00543c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543c9c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)

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
      "definition_site": "004c5a98",
      "incomplete_value": true,
      "site": "004c5a9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c5a58",
      "incomplete_value": true,
      "site": "004c5a5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c5ac8",
      "incomplete_value": true,
      "site": "004c5acc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c5a88",
      "incomplete_value": true,
      "site": "004c5a8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c5b3c",
      "incomplete_value": true,
      "site": "004c5b44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c5afc",
      "incomplete_value": true,
      "site": "004c5b04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004c5a8c",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "004c5a9c",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c5abc",
      "READ",
      [
        "storage",
        "00c9aea8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c5a8c",
      "READ",
      [
        "storage",
        "00c9af40",
        null,
        "pointer"
      ]
    ],
    [
      "004c5a9c",
      "DATA",
      [
        "storage",
        "00c66aa8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c5abc",
      "READ",
      [
        "storage",
        "00c9af78",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c5a4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c5a30.md#insn-004c5a4c) · [`004c5a9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c5a30.md#insn-004c5a9c) · [`004c5b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c5a30.md#insn-004c5b6c)
- 新版 [`004c5a8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c5a70.md#insn-004c5a8c) · [`004c5adc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c5a70.md#insn-004c5adc) · [`004c5bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c5a70.md#insn-004c5bac)

~~~diff
- 004c5a4c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
- 004c5a4c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c5a8c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f40:8"]]
+ 004c5a8c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c5a4c bytes 083947f9
+ 004c5a8c bytes 08a147f9
- 004c5a9c ["COPY", "register:0:8", ["register:4040:8"]]
- 004c5a9c ["INT_ADD", "register:40f0:8", ["const:4c5a9c:8", "const:4:8"]]
- 004c5a9c ["CALLIND", null, ["register:0:8"]]
+ 004c5adc ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c5adc ["INT_ADD", "register:40f0:8", ["const:4c5adc:8", "const:4:8"]]
+ 004c5adc ["CALLIND", null, ["register:0:8"]]
- 004c5a9c bytes 00013fd6
+ 004c5adc bytes 00013fd6
- 004c5b6c ["INT_ADD", "register:40f0:8", ["const:4c5b6c:8", "const:4:8"]]
- 004c5b6c ["CALL", null, ["callee:004b3548:8"]]
+ 004c5bac ["INT_ADD", "register:40f0:8", ["const:4c5bac:8", "const:4:8"]]
+ 004c5bac ["CALL", null, ["callee:004b3548:8"]]
- 004c5b6c bytes 67b6ff97
+ 004c5bac bytes 67b6ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dcf04283ca209c9f19e45ec2ad166cc7"></a>

### [`004c5df8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c5df8.md) → [`004c5e38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c5e38.md) _ZN5Botan18Cipher_Mode_Filter9start_msgEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 0件  · 呼出先 7件 [`004aeca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

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
      "definition_site": "004c5ef0",
      "incomplete_value": false,
      "site": "004c5efc",
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
            "const:310:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c5eb0",
      "incomplete_value": false,
      "site": "004c5ebc",
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
            "const:2d0:8"
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
      "definition_site": "004c5f1c",
      "incomplete_value": false,
      "site": "004c5f24",
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
            "const:6d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c5edc",
      "incomplete_value": false,
      "site": "004c5ee4",
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
            "const:72c:8"
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
      "definition_site": "004c5f70",
      "incomplete_value": true,
      "site": "004c5f7c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c5f30",
      "incomplete_value": true,
      "site": "004c5f3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004c5ef0",
      "PARAM",
      [
        "storage",
        "002b72d0",
        null,
        "string"
      ]
    ],
    [
      "004c5f1c",
      "PARAM",
      [
        "storage",
        "002ac72c",
        null,
        "string"
      ]
    ],
    [
      "004c5f6c",
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
      "004c5ef0",
      "PARAM",
      [
        "storage",
        "002b7310",
        null,
        "string"
      ]
    ],
    [
      "004c5f1c",
      "PARAM",
      [
        "storage",
        "002ac6d0",
        null,
        "string"
      ]
    ],
    [
      "004c5f6c",
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

- 旧版 [`004c5ebc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c5df8.md#insn-004c5ebc) · [`004c5ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c5df8.md#insn-004c5ee4) · [`004c5f3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c5df8.md#insn-004c5f3c)
- 新版 [`004c5efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c5e38.md#insn-004c5efc) · [`004c5f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c5e38.md#insn-004c5f24) · [`004c5f7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c5/004c5e38.md#insn-004c5f7c)

~~~diff
- 004c5ebc ["INT_ADD", "register:40f0:8", ["const:4c5ebc:8", "const:4:8"]]
- 004c5ebc ["CALL", null, ["callee:00c58030:8"]]
+ 004c5efc ["INT_ADD", "register:40f0:8", ["const:4c5efc:8", "const:4:8"]]
+ 004c5efc ["CALL", null, ["callee:00c58030:8"]]
- 004c5ebc bytes 29481e94
+ 004c5efc bytes 4d481e94
- 004c5ee4 ["INT_ADD", "register:40f0:8", ["const:4c5ee4:8", "const:4:8"]]
- 004c5ee4 ["CALL", null, ["callee:00c58040:8"]]
+ 004c5f24 ["INT_ADD", "register:40f0:8", ["const:4c5f24:8", "const:4:8"]]
+ 004c5f24 ["CALL", null, ["callee:00c58040:8"]]
- 004c5ee4 bytes 23481e94
+ 004c5f24 bytes 47481e94
- 004c5f3c ["INT_ADD", "register:40f0:8", ["const:4c5f3c:8", "const:4:8"]]
- 004c5f3c ["CALL", null, ["callee:00c57fe0:8"]]
+ 004c5f7c ["INT_ADD", "register:40f0:8", ["const:4c5f7c:8", "const:4:8"]]
+ 004c5f7c ["CALL", null, ["callee:00c57fe0:8"]]
- 004c5f3c bytes f5471e94
+ 004c5f7c bytes 19481e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-592c3dca0055969889a91887ca32a154"></a>

### [`004c61b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c61b4.md) → [`004c61f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c61f4.md) _ZN5Botan15DataSink_Stream5writeEPKhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md)

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
      "definition_site": "004c6270",
      "incomplete_value": false,
      "site": "004c627c",
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
            "const:318:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c6230",
      "incomplete_value": false,
      "site": "004c623c",
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
            "const:2d8:8"
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
      "definition_site": "004c62b0",
      "incomplete_value": true,
      "site": "004c62bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c6270",
      "incomplete_value": true,
      "site": "004c627c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c62ac",
      "incomplete_value": false,
      "site": "004c62bc",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004c626c",
      "incomplete_value": false,
      "site": "004c627c",
      "value": [
        "leaf",
        "const:535868:8"
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
      "004c6270",
      "PARAM",
      [
        "storage",
        "002b72d8",
        null,
        "string"
      ]
    ],
    [
      "004c62ac",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004c62b0",
      "READ",
      [
        "storage",
        "00c9ad80",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c6270",
      "PARAM",
      [
        "storage",
        "002b7318",
        null,
        "string"
      ]
    ],
    [
      "004c62ac",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004c62b0",
      "READ",
      [
        "storage",
        "00c9ae50",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c623c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c61b4.md#insn-004c623c) · [`004c627c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c61b4.md#insn-004c627c) · [`004c61dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c61b4.md#insn-004c61dc)
- 新版 [`004c627c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c61f4.md#insn-004c627c) · [`004c62bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c61f4.md#insn-004c62bc) · [`004c621c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c61f4.md#insn-004c621c)

~~~diff
- 004c623c ["INT_ADD", "register:40f0:8", ["const:4c623c:8", "const:4:8"]]
- 004c623c ["CALL", null, ["callee:00c58180:8"]]
+ 004c627c ["INT_ADD", "register:40f0:8", ["const:4c627c:8", "const:4:8"]]
+ 004c627c ["CALL", null, ["callee:00c58180:8"]]
- 004c623c bytes 9d471e94
+ 004c627c bytes c1471e94
- 004c627c ["INT_ADD", "register:40f0:8", ["const:4c627c:8", "const:4:8"]]
- 004c627c ["CALL", null, ["callee:00c57fe0:8"]]
+ 004c62bc ["INT_ADD", "register:40f0:8", ["const:4c62bc:8", "const:4:8"]]
+ 004c62bc ["CALL", null, ["callee:00c57fe0:8"]]
- 004c627c bytes 25471e94
+ 004c62bc bytes 49471e94
- 004c61dc ["INT_ADD", "register:40f0:8", ["const:4c61dc:8", "const:4:8"]]
- 004c61dc ["CALL", null, ["callee:00c58d40:8"]]
+ 004c621c ["INT_ADD", "register:40f0:8", ["const:4c621c:8", "const:4:8"]]
+ 004c621c ["CALL", null, ["callee:00c58d40:8"]]
- 004c61dc bytes a54a1e94
+ 004c621c bytes c94a1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b009a5c2d6df979d0f96ad9c6ebfb0b8"></a>

### [`004c62d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c62d8.md) → [`004c6318`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6318.md) _ZN5Botan15DataSink_StreamC2ERNSt6__ndk113basic_ostreamIcNS1_11char_traitsIcEEEERKNS1_12basic_stringIcS4_NS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00543c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543c5c.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00543c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543c9c.md)

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
      "definition_site": "004c6344",
      "incomplete_value": true,
      "site": "004c6348",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c6304",
      "incomplete_value": true,
      "site": "004c6308",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c6374",
      "incomplete_value": true,
      "site": "004c6378",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c6334",
      "incomplete_value": true,
      "site": "004c6338",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004c6334",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "004c6348",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c6368",
      "READ",
      [
        "storage",
        "00c9aeb8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c6334",
      "READ",
      [
        "storage",
        "00c9af40",
        null,
        "pointer"
      ]
    ],
    [
      "004c6348",
      "DATA",
      [
        "storage",
        "00c66aa8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c6368",
      "READ",
      [
        "storage",
        "00c9af88",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c62f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c62d8.md#insn-004c62f4) · [`004c6320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c62d8.md#insn-004c6320) · [`004c6328`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c62d8.md#insn-004c6328)
- 新版 [`004c6334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6318.md#insn-004c6334) · [`004c6360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6318.md#insn-004c6360) · [`004c6368`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6318.md#insn-004c6368)

~~~diff
- 004c62f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
- 004c62f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c6334 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f40:8"]]
+ 004c6334 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c62f4 bytes 083947f9
+ 004c6334 bytes 08a147f9
- 004c6320 ["INT_ADD", "register:40f0:8", ["const:4c6320:8", "const:4:8"]]
- 004c6320 ["CALL", null, ["callee:00543c9c:8"]]
+ 004c6360 ["INT_ADD", "register:40f0:8", ["const:4c6360:8", "const:4:8"]]
+ 004c6360 ["CALL", null, ["callee:00543c9c:8"]]
- 004c6320 bytes 4ff60194
+ 004c6360 bytes 4ff60194
- 004c6328 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:eb8:8"]]
- 004c6328 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c6368 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f88:8"]]
+ 004c6368 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c6328 bytes 085d47f9
+ 004c6368 bytes 08c547f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0aa2adab4e0b721bf776d47e1c2ebf3"></a>

### [`004c63b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c63b4.md) → [`004c63f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c63f4.md) _ZN5Botan15DataSink_StreamC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEb

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 10件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`004c65d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c65d4.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00543c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543c5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`004c6614`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6614.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00543c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543c9c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "004c6430",
      "incomplete_value": true,
      "site": "004c6438",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c63f0",
      "incomplete_value": true,
      "site": "004c63f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c6464",
      "incomplete_value": true,
      "site": "004c6468",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c6424",
      "incomplete_value": true,
      "site": "004c6428",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c6508",
      "incomplete_value": false,
      "site": "004c6514",
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
            "const:ae0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c64c8",
      "incomplete_value": false,
      "site": "004c64d4",
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
            "const:b3c:8"
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
      "004c641c",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "004c6438",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c6458",
      "READ",
      [
        "storage",
        "00c9aeb8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c641c",
      "READ",
      [
        "storage",
        "00c9af40",
        null,
        "pointer"
      ]
    ],
    [
      "004c6438",
      "DATA",
      [
        "storage",
        "00c66aa8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c6458",
      "READ",
      [
        "storage",
        "00c9af88",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c64d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c63b4.md#insn-004c64d4) · [`004c6510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c63b4.md#insn-004c6510) · [`004c63dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c63b4.md#insn-004c63dc)
- 新版 [`004c6514`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c63f4.md#insn-004c6514) · [`004c6550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c63f4.md#insn-004c6550) · [`004c641c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c63f4.md#insn-004c641c)

~~~diff
- 004c64d4 ["INT_ADD", "register:40f0:8", ["const:4c64d4:8", "const:4:8"]]
- 004c64d4 ["CALL", null, ["callee:00c58180:8"]]
+ 004c6514 ["INT_ADD", "register:40f0:8", ["const:4c6514:8", "const:4:8"]]
+ 004c6514 ["CALL", null, ["callee:00c58180:8"]]
- 004c64d4 bytes f7461e94
+ 004c6514 bytes 1b471e94
- 004c6510 ["INT_ADD", "register:40f0:8", ["const:4c6510:8", "const:4:8"]]
- 004c6510 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004c6550 ["INT_ADD", "register:40f0:8", ["const:4c6550:8", "const:4:8"]]
+ 004c6550 ["CALL", null, ["callee:00c57fe0:8"]]
- 004c6510 bytes 80461e94
+ 004c6550 bytes a4461e94
- 004c63dc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e70:8"]]
- 004c63dc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c641c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f40:8"]]
+ 004c641c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c63dc bytes 293947f9
+ 004c641c bytes 29a147f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a8773221a9317212392637333c2e6fc"></a>

### [`004c65d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c65d4.md) → [`004c6614`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6614.md) FUN_004c6614

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004c63b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c63b4.md) · 呼出先 4件 [`00c581e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581e0.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c58f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58f00.md) [`00c58f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58f10.md)
- 新版 呼出元 1件 [`004c63f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c63f4.md) · 呼出先 4件 [`00c582b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c582b0.md) [`00c58370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58370.md) [`00c58fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58fd0.md) [`00c58fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58fe0.md)

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
      "definition_site": "004c6658",
      "incomplete_value": true,
      "site": "004c6658",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004c6618",
      "incomplete_value": true,
      "site": "004c6618",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004c6650",
      "incomplete_value": true,
      "site": "004c665c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004c6610",
      "incomplete_value": true,
      "site": "004c661c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004c6664",
      "incomplete_value": true,
      "site": "004c6664",
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
      "definition_site": "004c6624",
      "incomplete_value": true,
      "site": "004c6624",
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
      "004c6638",
      "READ",
      [
        "storage",
        "00c9aec0",
        null,
        "pointer"
      ]
    ],
    [
      "004c663c",
      "READ",
      [
        "storage",
        "00c9aec8",
        null,
        "pointer"
      ]
    ],
    [
      "004c6650",
      "READ",
      [
        "storage",
        "00c930d0",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "004c6638",
      "READ",
      [
        "storage",
        "00c9af90",
        null,
        "pointer"
      ]
    ],
    [
      "004c663c",
      "READ",
      [
        "storage",
        "00c9af98",
        null,
        "pointer"
      ]
    ],
    [
      "004c6650",
      "READ",
      [
        "storage",
        "00c931a0",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c665c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c65d4.md#insn-004c665c) · [`004c65f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c65d4.md#insn-004c65f8) · [`004c65fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c65d4.md#insn-004c65fc)
- 新版 [`004c669c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6614.md#insn-004c669c) · [`004c6638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6614.md#insn-004c6638) · [`004c663c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6614.md#insn-004c663c)

~~~diff
- 004c665c ["INT_ADD", "register:40f0:8", ["const:4c665c:8", "const:4:8"]]
- 004c665c ["CALL", null, ["callee:00c58fd0:8"]]
+ 004c669c ["INT_ADD", "register:40f0:8", ["const:4c669c:8", "const:4:8"]]
+ 004c669c ["CALL", null, ["callee:00c58fd0:8"]]
- 004c665c bytes 294a1e94
+ 004c669c bytes 4d4a1e94
- 004c65f8 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:ec0:8"]]
- 004c65f8 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c6638 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:f90:8"]]
+ 004c6638 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
- 004c65f8 bytes 396347f9
+ 004c6638 bytes 39cb47f9
- 004c65fc ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:ec8:8"]]
- 004c65fc ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c663c ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:f98:8"]]
+ 004c663c ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 004c65fc bytes 186747f9
+ 004c663c bytes 18cf47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16f32c73449e2b1519a1c32b24173e55"></a>

### [`004c6a04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c6a04.md) → [`004c6a44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6a44.md) _ZN5Botan6Filter8set_portEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

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
      "definition_site": "004c6ab0",
      "incomplete_value": false,
      "site": "004c6ab8",
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
            "const:bd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c6a70",
      "incomplete_value": false,
      "site": "004c6a78",
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
            "const:7d:8"
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
      "definition_site": "004c6aec",
      "incomplete_value": true,
      "site": "004c6af8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c6aac",
      "incomplete_value": true,
      "site": "004c6ab8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c6ae8",
      "incomplete_value": false,
      "site": "004c6af8",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004c6aa8",
      "incomplete_value": false,
      "site": "004c6ab8",
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
      "004c6ab0",
      "PARAM",
      [
        "storage",
        "002c107d",
        null,
        "string"
      ]
    ],
    [
      "004c6ae8",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004c6aec",
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
      "004c6ab0",
      "PARAM",
      [
        "storage",
        "002c10bd",
        null,
        "string"
      ]
    ],
    [
      "004c6ae8",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004c6aec",
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

- 旧版 [`004c6a78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c6a04.md#insn-004c6a78) · [`004c6ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c6a04.md#insn-004c6ab8) · [`004c6a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c6a04.md#insn-004c6a64)
- 新版 [`004c6ab8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6a44.md#insn-004c6ab8) · [`004c6af8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6a44.md#insn-004c6af8) · [`004c6aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6a44.md#insn-004c6aa4)

~~~diff
- 004c6a78 ["INT_ADD", "register:40f0:8", ["const:4c6a78:8", "const:4:8"]]
- 004c6a78 ["CALL", null, ["callee:0043de18:8"]]
+ 004c6ab8 ["INT_ADD", "register:40f0:8", ["const:4c6ab8:8", "const:4:8"]]
+ 004c6ab8 ["CALL", null, ["callee:0043de18:8"]]
- 004c6a78 bytes d8dcfd97
+ 004c6ab8 bytes d8dcfd97
- 004c6ab8 ["INT_ADD", "register:40f0:8", ["const:4c6ab8:8", "const:4:8"]]
- 004c6ab8 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004c6af8 ["INT_ADD", "register:40f0:8", ["const:4c6af8:8", "const:4:8"]]
+ 004c6af8 ["CALL", null, ["callee:00c57fe0:8"]]
- 004c6ab8 bytes 16451e94
+ 004c6af8 bytes 3a451e94
- 004c6a64 ["INT_ADD", "register:40f0:8", ["const:4c6a64:8", "const:4:8"]]
- 004c6a64 ["CALL", null, ["callee:00c57fc0:8"]]
+ 004c6aa4 ["INT_ADD", "register:40f0:8", ["const:4c6aa4:8", "const:4:8"]]
+ 004c6aa4 ["CALL", null, ["callee:00c57fc0:8"]]
- 004c6a64 bytes 23451e94
+ 004c6aa4 bytes 47451e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3141ae5058e08a1a5018b1a49eabcc24"></a>

### [`004c6b44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c6b44.md) → [`004c6b84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6b84.md) _ZN5Botan10get_cipherERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEENS_10Cipher_DirE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58f70.md) · 呼出先 8件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`00c59040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59040.md) · 呼出先 8件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

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
      "definition_site": "004c6c28",
      "incomplete_value": true,
      "site": "004c6c30",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fa0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c6be8",
      "incomplete_value": true,
      "site": "004c6bf0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c6c24",
      "incomplete_value": false,
      "site": "004c6c30",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004c6be4",
      "incomplete_value": false,
      "site": "004c6bf0",
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
      "004c6c24",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004c6c28",
      "READ",
      [
        "storage",
        "00c9aed0",
        null,
        "pointer"
      ]
    ],
    [
      "004c6c28",
      "PARAM",
      [
        "storage",
        "00c66a18",
        "_ZTIN5Botan19Algorithm_Not_FoundE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004c6c24",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004c6c28",
      "READ",
      [
        "storage",
        "00c9afa0",
        null,
        "pointer"
      ]
    ],
    [
      "004c6c28",
      "PARAM",
      [
        "storage",
        "00c66ae8",
        "_ZTIN5Botan19Algorithm_Not_FoundE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c6bf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c6b44.md#insn-004c6bf0) · [`004c6b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c6b44.md#insn-004c6b70) · [`004c6b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c6b44.md#insn-004c6b80)
- 新版 [`004c6c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6b84.md#insn-004c6c30) · [`004c6bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6b84.md#insn-004c6bb0) · [`004c6bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6b84.md#insn-004c6bc0)

~~~diff
- 004c6bf0 ["INT_ADD", "register:40f0:8", ["const:4c6bf0:8", "const:4:8"]]
- 004c6bf0 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004c6c30 ["INT_ADD", "register:40f0:8", ["const:4c6c30:8", "const:4:8"]]
+ 004c6c30 ["CALL", null, ["callee:00c57fe0:8"]]
- 004c6bf0 bytes c8441e94
+ 004c6c30 bytes ec441e94
- 004c6b70 ["INT_ADD", "register:40f0:8", ["const:4c6b70:8", "const:4:8"]]
- 004c6b70 ["CALL", null, ["callee:00c59050:8"]]
+ 004c6bb0 ["INT_ADD", "register:40f0:8", ["const:4c6bb0:8", "const:4:8"]]
+ 004c6bb0 ["CALL", null, ["callee:00c59050:8"]]
- 004c6b70 bytes 04491e94
+ 004c6bb0 bytes 28491e94
- 004c6b80 ["INT_ADD", "register:40f0:8", ["const:4c6b80:8", "const:4:8"]]
- 004c6b80 ["CALL", null, ["callee:00c57f60:8"]]
+ 004c6bc0 ["INT_ADD", "register:40f0:8", ["const:4c6bc0:8", "const:4:8"]]
+ 004c6bc0 ["CALL", null, ["callee:00c57f60:8"]]
- 004c6b80 bytes c4441e94
+ 004c6bc0 bytes e8441e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01aa642b7394a748aa4d6de13517cc7d"></a>

### [`004c6c48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c6c48.md) → [`004c6c88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6c88.md) _ZN5Botan15get_cipher_modeERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEENS_10Cipher_DirES8_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c58f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58f80.md) · 呼出先 27件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`004594d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) [`004d1b24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d1/004d1b24.md) [`004d1bbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d1/004d1bbc.md) [`00547b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547b6c.md)
- 新版 呼出元 1件 [`00c59050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59050.md) · 呼出先 27件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00459510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459510.md) [`004d1b64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d1/004d1b64.md) [`004d1bfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d1/004d1bfc.md) [`00547bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00547/00547bac.md)

変更の種類 constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 97.17% / 新版 97.17%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c6ce8",
      "incomplete_value": true,
      "site": "004c6ce8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c6ca8",
      "incomplete_value": true,
      "site": "004c6ca8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c6d44",
      "incomplete_value": false,
      "site": "004c6d50",
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
      "definition_site": "004c6d04",
      "incomplete_value": false,
      "site": "004c6d10",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c6e14",
      "incomplete_value": true,
      "site": "004c6e18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "004c6dd4",
      "incomplete_value": true,
      "site": "004c6dd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "004c6ce0",
      "READ",
      [
        "storage",
        "00c9aed8",
        null,
        "pointer"
      ]
    ],
    [
      "004c6ce8",
      "DATA",
      [
        "storage",
        "00c69d60",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "004c6d50",
      "DATA",
      [
        "storage",
        "00c6a6b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004c6ce0",
      "READ",
      [
        "storage",
        "00c9afa8",
        null,
        "pointer"
      ]
    ],
    [
      "004c6ce8",
      "DATA",
      [
        "storage",
        "00c69e30",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "004c6d50",
      "DATA",
      [
        "storage",
        "00c6a780",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c6d98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c6c48.md#insn-004c6d98) · [`004c6e1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c6c48.md#insn-004c6e1c) · [`004c6e78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c6c48.md#insn-004c6e78)
- 新版 [`004c6dd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6c88.md#insn-004c6dd8) · [`004c6e5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6c88.md#insn-004c6e5c) · [`004c6eb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c6/004c6c88.md#insn-004c6eb8)

~~~diff
- 004c6d98 ["INT_ADD", "register:40f0:8", ["const:4c6d98:8", "const:4:8"]]
- 004c6d98 ["CALL", null, ["callee:0043bb60:8"]]
+ 004c6dd8 ["INT_ADD", "register:40f0:8", ["const:4c6dd8:8", "const:4:8"]]
+ 004c6dd8 ["CALL", null, ["callee:0043bb60:8"]]
- 004c6d98 bytes 62d3fd97
+ 004c6dd8 bytes 62d3fd97
- 004c6e1c ["INT_ADD", "register:40f0:8", ["const:4c6e1c:8", "const:4:8"]]
- 004c6e1c ["CALL", null, ["callee:00c582c0:8"]]
+ 004c6e5c ["INT_ADD", "register:40f0:8", ["const:4c6e5c:8", "const:4:8"]]
+ 004c6e5c ["CALL", null, ["callee:00c582c0:8"]]
- 004c6e1c bytes f5441e94
+ 004c6e5c bytes 19451e94
- 004c6e78 ["INT_ADD", "register:40f0:8", ["const:4c6e78:8", "const:4:8"]]
- 004c6e78 ["CALL", null, ["callee:00459510:8"]]
+ 004c6eb8 ["INT_ADD", "register:40f0:8", ["const:4c6eb8:8", "const:4:8"]]
+ 004c6eb8 ["CALL", null, ["callee:00459510:8"]]
- 004c6e78 bytes 9649fe97
+ 004c6eb8 bytes 9649fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef1290331801064b13bb8ab60ba5a6a1"></a>

### [`004c784c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c7/004c784c.md) → [`004c788c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c788c.md) _ZN5Botan11SecureQueue4readEPhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58ff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58ff0.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)
- 新版 呼出元 1件 [`00c590c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c590c0.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)

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
      "definition_site": "004c7960",
      "incomplete_value": true,
      "site": "004c7960",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c7920",
      "incomplete_value": true,
      "site": "004c7920",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
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
      "004c7950",
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
      "004c7950",
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

- 旧版 [`004c7920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c7/004c784c.md#insn-004c7920) · [`004c78d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c7/004c784c.md#insn-004c78d0) · [`004c7910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c7/004c784c.md#insn-004c7910)
- 新版 [`004c7960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c788c.md#insn-004c7960) · [`004c7910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c788c.md#insn-004c7910) · [`004c7950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c788c.md#insn-004c7950)

~~~diff
- 004c7920 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c7920 ["INT_ADD", "register:40f0:8", ["const:4c7920:8", "const:4:8"]]
- 004c7920 ["CALLIND", null, ["register:0:8"]]
+ 004c7960 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c7960 ["INT_ADD", "register:40f0:8", ["const:4c7960:8", "const:4:8"]]
+ 004c7960 ["CALLIND", null, ["register:0:8"]]
- 004c7920 bytes 20013fd6
+ 004c7960 bytes 20013fd6
- 004c78d0 ["INT_ADD", "register:40f0:8", ["const:4c78d0:8", "const:4:8"]]
- 004c78d0 ["CALL", null, ["callee:00c58010:8"]]
+ 004c7910 ["INT_ADD", "register:40f0:8", ["const:4c7910:8", "const:4:8"]]
+ 004c7910 ["CALL", null, ["callee:00c58010:8"]]
- 004c78d0 bytes 9c411e94
+ 004c7910 bytes c0411e94
- 004c7910 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:738:8"]]
- 004c7910 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c7950 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:808:8"]]
+ 004c7950 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c7910 bytes 499f43f9
+ 004c7950 bytes 490744f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0563b8aabcfc9fb93692453ace703d72"></a>

### [`004c7ac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c7/004c7ac8.md) → [`004c7b08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7b08.md) FUN_004c7b08

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004c8c18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8c18.md) · 呼出先 3件 [`00543ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543ecc.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58650.md)
- 新版 呼出元 1件 [`004c8c58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8c58.md) · 呼出先 3件 [`00543f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543f0c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58720.md)

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
      "definition_site": "004c7be0",
      "incomplete_value": false,
      "site": "004c7c00",
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
            "const:bd7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c7ba0",
      "incomplete_value": false,
      "site": "004c7bc0",
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
            "const:ba8:8"
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
      "definition_site": "004c7be8",
      "incomplete_value": false,
      "site": "004c7c00",
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
            "const:bdd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c7ba8",
      "incomplete_value": false,
      "site": "004c7bc0",
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
            "const:bae:8"
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
      "definition_site": "004c7bf0",
      "incomplete_value": false,
      "site": "004c7c00",
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
            "const:580:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c7bb0",
      "incomplete_value": false,
      "site": "004c7bc0",
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
            "const:5dc:8"
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
      "004c7be0",
      "PARAM",
      [
        "storage",
        "002a9ba8",
        null,
        "string"
      ]
    ],
    [
      "004c7be8",
      "PARAM",
      [
        "storage",
        "002a9bae",
        null,
        "string"
      ]
    ],
    [
      "004c7bf0",
      "PARAM",
      [
        "storage",
        "002a65dc",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004c7be0",
      "PARAM",
      [
        "storage",
        "002a9bd7",
        null,
        "string"
      ]
    ],
    [
      "004c7be8",
      "PARAM",
      [
        "storage",
        "002a9bdd",
        null,
        "string"
      ]
    ],
    [
      "004c7bf0",
      "PARAM",
      [
        "storage",
        "002a6580",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c7bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c7/004c7ac8.md#insn-004c7bb8) · [`004c7bc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c7/004c7ac8.md#insn-004c7bc0) · [`004c7bf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c7/004c7ac8.md#insn-004c7bf8)
- 新版 [`004c7bf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7b08.md#insn-004c7bf8) · [`004c7c00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7b08.md#insn-004c7c00) · [`004c7c38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7b08.md#insn-004c7c38)

~~~diff
- 004c7bb8 ["COPY", "tmp:0:8", ["const:dcb:8"]]
- 004c7bb8 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 004c7bb8 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 004c7bb8 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 004c7bf8 ["COPY", "tmp:0:8", ["const:973:8"]]
+ 004c7bf8 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 004c7bf8 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 004c7bf8 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 004c7bb8 bytes 632c3791
+ 004c7bf8 bytes 63cc2591
- 004c7bc0 ["INT_ADD", "register:40f0:8", ["const:4c7bc0:8", "const:4:8"]]
- 004c7bc0 ["CALL", null, ["callee:00c58720:8"]]
+ 004c7c00 ["INT_ADD", "register:40f0:8", ["const:4c7c00:8", "const:4:8"]]
+ 004c7c00 ["CALL", null, ["callee:00c58720:8"]]
- 004c7bc0 bytes a4421e94
+ 004c7c00 bytes c8421e94
- 004c7bf8 ["INT_ADD", "register:40f0:8", ["const:4c7bf8:8", "const:4:8"]]
- 004c7bf8 ["CALL", null, ["callee:00c58720:8"]]
+ 004c7c38 ["INT_ADD", "register:40f0:8", ["const:4c7c38:8", "const:4:8"]]
+ 004c7c38 ["CALL", null, ["callee:00c58720:8"]]
- 004c7bf8 bytes 96421e94
+ 004c7c38 bytes ba421e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29dcf37614fe6994917742cdc92ab162"></a>

### [`004c7d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c7/004c7d78.md) → [`004c7db8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7db8.md) _ZN5Botan4PipeC1EPNS_6FilterES2_S2_S2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c59010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c590e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c590e0.md)

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
      "definition_site": "004c7dec",
      "incomplete_value": true,
      "site": "004c7df4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c7dac",
      "incomplete_value": true,
      "site": "004c7db4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004c7dd8",
      "READ",
      [
        "storage",
        "00c9af00",
        null,
        "pointer"
      ]
    ],
    [
      "004c7df4",
      "DATA",
      [
        "storage",
        "00c66a40",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "004c7dd8",
      "READ",
      [
        "storage",
        "00c9afd0",
        null,
        "pointer"
      ]
    ],
    [
      "004c7df4",
      "DATA",
      [
        "storage",
        "00c66b10",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c7d98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c7/004c7d78.md#insn-004c7d98) · [`004c7dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c7/004c7d78.md#insn-004c7dbc) · [`004c7de4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c7/004c7d78.md#insn-004c7de4)
- 新版 [`004c7dd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7db8.md#insn-004c7dd8) · [`004c7dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7db8.md#insn-004c7dfc) · [`004c7e24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7db8.md#insn-004c7e24)

~~~diff
- 004c7d98 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f00:8"]]
- 004c7d98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c7dd8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fd0:8"]]
+ 004c7dd8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c7d98 bytes 088147f9
+ 004c7dd8 bytes 08e947f9
- 004c7dbc ["INT_ADD", "register:40f0:8", ["const:4c7dbc:8", "const:4:8"]]
- 004c7dbc ["CALL", null, ["callee:00c57f60:8"]]
+ 004c7dfc ["INT_ADD", "register:40f0:8", ["const:4c7dfc:8", "const:4:8"]]
+ 004c7dfc ["CALL", null, ["callee:00c57f60:8"]]
- 004c7dbc bytes 35401e94
+ 004c7dfc bytes 59401e94
- 004c7de4 ["INT_ADD", "register:40f0:8", ["const:4c7de4:8", "const:4:8"]]
- 004c7de4 ["CALL", null, ["callee:00c590e0:8"]]
+ 004c7e24 ["INT_ADD", "register:40f0:8", ["const:4c7e24:8", "const:4:8"]]
+ 004c7e24 ["CALL", null, ["callee:00c590e0:8"]]
- 004c7de4 bytes 8b441e94
+ 004c7e24 bytes af441e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aef9f9a4584ad3463fdc10e9743216b0"></a>

### [`004c7e38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c7/004c7e38.md) → [`004c7e78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7e78.md) _ZN5Botan4PipeC2ESt16initializer_listIPNS_6FilterEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c59010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c590e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c590e0.md)

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
      "definition_site": "004c7ea4",
      "incomplete_value": true,
      "site": "004c7ea8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c7e64",
      "incomplete_value": true,
      "site": "004c7e68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004c7e94",
      "READ",
      [
        "storage",
        "00c9af00",
        null,
        "pointer"
      ]
    ],
    [
      "004c7ea8",
      "DATA",
      [
        "storage",
        "00c66a40",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "004c7e94",
      "READ",
      [
        "storage",
        "00c9afd0",
        null,
        "pointer"
      ]
    ],
    [
      "004c7ea8",
      "DATA",
      [
        "storage",
        "00c66b10",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c7e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c7/004c7e38.md#insn-004c7e54) · [`004c7e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c7/004c7e38.md#insn-004c7e70) · [`004c7ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c7/004c7e38.md#insn-004c7ea0)
- 新版 [`004c7e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7e78.md#insn-004c7e94) · [`004c7eb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7e78.md#insn-004c7eb0) · [`004c7ee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7e78.md#insn-004c7ee0)

~~~diff
- 004c7e54 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f00:8"]]
- 004c7e54 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c7e94 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fd0:8"]]
+ 004c7e94 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c7e54 bytes 088147f9
+ 004c7e94 bytes 08e947f9
- 004c7e70 ["INT_ADD", "register:40f0:8", ["const:4c7e70:8", "const:4:8"]]
- 004c7e70 ["CALL", null, ["callee:00c57f60:8"]]
+ 004c7eb0 ["INT_ADD", "register:40f0:8", ["const:4c7eb0:8", "const:4:8"]]
+ 004c7eb0 ["CALL", null, ["callee:00c57f60:8"]]
- 004c7e70 bytes 08401e94
+ 004c7eb0 bytes 2c401e94
- 004c7ea0 ["INT_ADD", "register:40f0:8", ["const:4c7ea0:8", "const:4:8"]]
- 004c7ea0 ["CALL", null, ["callee:00c590e0:8"]]
+ 004c7ee0 ["INT_ADD", "register:40f0:8", ["const:4c7ee0:8", "const:4:8"]]
+ 004c7ee0 ["CALL", null, ["callee:00c590e0:8"]]
- 004c7ea0 bytes 5c441e94
+ 004c7ee0 bytes 80441e94
~~~


<a id="compare-1537b3a0f0b91ef5c9ea58a3ced19d0c"></a>

### [`004c7ed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c7/004c7ed8.md) → [`004c7f18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7f18.md) _ZN5Botan4Pipe9do_appendEPNS_6FilterE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59010.md) · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)
- 新版 呼出元 1件 [`00c590e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c590e0.md) · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004aeca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)

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
      "definition_site": "004c7f4c",
      "incomplete_value": true,
      "site": "004c7f50",
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
      "definition_site": "004c7f0c",
      "incomplete_value": true,
      "site": "004c7f10",
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
      "definition_site": "004c7fe4",
      "incomplete_value": false,
      "site": "004c7fec",
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
            "const:ad1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c7fa4",
      "incomplete_value": false,
      "site": "004c7fac",
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
            "const:aa0:8"
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
      "definition_site": "004c8020",
      "incomplete_value": true,
      "site": "004c802c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c7fe0",
      "incomplete_value": true,
      "site": "004c7fec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004c7f40",
      "READ",
      [
        "storage",
        "00c9af08",
        null,
        "pointer"
      ]
    ],
    [
      "004c7fe4",
      "PARAM",
      [
        "storage",
        "002b2aa0",
        null,
        "string"
      ]
    ],
    [
      "004c801c",
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
      "004c7f40",
      "READ",
      [
        "storage",
        "00c9afd8",
        null,
        "pointer"
      ]
    ],
    [
      "004c7fe4",
      "PARAM",
      [
        "storage",
        "002b2ad1",
        null,
        "string"
      ]
    ],
    [
      "004c801c",
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

- 旧版 [`004c7fac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c7/004c7ed8.md#insn-004c7fac) · [`004c7fec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c7/004c7ed8.md#insn-004c7fec) · [`004c8010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c7/004c7ed8.md#insn-004c8010)
- 新版 [`004c7fec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7f18.md#insn-004c7fec) · [`004c802c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7f18.md#insn-004c802c) · [`004c8050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7f18.md#insn-004c8050)

~~~diff
- 004c7fac ["INT_ADD", "register:40f0:8", ["const:4c7fac:8", "const:4:8"]]
- 004c7fac ["CALL", null, ["callee:0043de18:8"]]
+ 004c7fec ["INT_ADD", "register:40f0:8", ["const:4c7fec:8", "const:4:8"]]
+ 004c7fec ["CALL", null, ["callee:0043de18:8"]]
- 004c7fac bytes 8bd7fd97
+ 004c7fec bytes 8bd7fd97
- 004c7fec ["INT_ADD", "register:40f0:8", ["const:4c7fec:8", "const:4:8"]]
- 004c7fec ["CALL", null, ["callee:00c57fe0:8"]]
+ 004c802c ["INT_ADD", "register:40f0:8", ["const:4c802c:8", "const:4:8"]]
+ 004c802c ["CALL", null, ["callee:00c57fe0:8"]]
- 004c7fec bytes c93f1e94
+ 004c802c bytes ed3f1e94
- 004c8010 ["INT_ADD", "register:40f0:8", ["const:4c8010:8", "const:4:8"]]
- 004c8010 ["CALL", null, ["callee:0043de18:8"]]
+ 004c8050 ["INT_ADD", "register:40f0:8", ["const:4c8050:8", "const:4:8"]]
+ 004c8050 ["CALL", null, ["callee:0043de18:8"]]
- 004c8010 bytes 72d7fd97
+ 004c8050 bytes 72d7fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-131716d8818f2d0b12431c9f30619da5"></a>

### [`004c8198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8198.md) → [`004c81d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c81d8.md) _ZN5Botan4Pipe8destructEPNS_6FilterE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59020.md) · 呼出先 1件 [`00c59020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59020.md)
- 新版 呼出元 1件 [`00c590f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c590f0.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c590f0.md)

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
      "definition_site": "004c8200",
      "incomplete_value": true,
      "site": "004c8204",
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
      "definition_site": "004c81c0",
      "incomplete_value": true,
      "site": "004c81c4",
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
      "004c81f4",
      "READ",
      [
        "storage",
        "00c9af08",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c81f4",
      "READ",
      [
        "storage",
        "00c9afd8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c81b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8198.md#insn-004c81b4) · [`004c81e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8198.md#insn-004c81e4)
- 新版 [`004c81f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c81d8.md#insn-004c81f4) · [`004c8224`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c81d8.md#insn-004c8224)

~~~diff
- 004c81b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f08:8"]]
- 004c81b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c81f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fd8:8"]]
+ 004c81f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c81b4 bytes 088547f9
+ 004c81f4 bytes 08ed47f9
- 004c81e4 ["INT_ADD", "register:40f0:8", ["const:4c81e4:8", "const:4:8"]]
- 004c81e4 ["CALL", null, ["callee:00c590f0:8"]]
+ 004c8224 ["INT_ADD", "register:40f0:8", ["const:4c8224:8", "const:4:8"]]
+ 004c8224 ["CALL", null, ["callee:00c590f0:8"]]
- 004c81e4 bytes 8f431e94
+ 004c8224 bytes b3431e94
~~~


<a id="compare-654ef1e719ab3d232e459106acd32450"></a>

### [`004c8298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8298.md) → [`004c82d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c82d8.md) _ZNK5Botan4Pipe9remainingEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59040.md) · 呼出先 5件 [`004c970c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c9/004c970c.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`00c59110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59110.md) · 呼出先 5件 [`004c974c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c974c.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

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
      "definition_site": "004c830c",
      "incomplete_value": true,
      "site": "004c830c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d91:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c82cc",
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
                "const:2b4000:8"
              ],
              [
                "leaf",
                "const:d60:8"
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
      "definition_site": "004c8400",
      "incomplete_value": true,
      "site": "004c8408",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fe0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c83c0",
      "incomplete_value": true,
      "site": "004c83c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f10:8"
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
      "definition_site": "004c83fc",
      "incomplete_value": false,
      "site": "004c8408",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004c83bc",
      "incomplete_value": false,
      "site": "004c83c8",
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
      "004c82f8",
      "READ",
      [
        "storage",
        "002b4d60",
        null,
        "string"
      ]
    ],
    [
      "004c83fc",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004c8400",
      "READ",
      [
        "storage",
        "00c9af10",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c82f8",
      "READ",
      [
        "storage",
        "002b4d91",
        null,
        "string"
      ]
    ],
    [
      "004c83fc",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004c8400",
      "READ",
      [
        "storage",
        "00c9afe0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c83c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8298.md#insn-004c83c8) · [`004c82b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8298.md#insn-004c82b0) · [`004c838c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8298.md#insn-004c838c)
- 新版 [`004c8408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c82d8.md#insn-004c8408) · [`004c82f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c82d8.md#insn-004c82f0) · [`004c83cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c82d8.md#insn-004c83cc)

~~~diff
- 004c83c8 ["INT_ADD", "register:40f0:8", ["const:4c83c8:8", "const:4:8"]]
- 004c83c8 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004c8408 ["INT_ADD", "register:40f0:8", ["const:4c8408:8", "const:4:8"]]
+ 004c8408 ["CALL", null, ["callee:00c57fe0:8"]]
- 004c83c8 bytes d23e1e94
+ 004c8408 bytes f63e1e94
- 004c82b0 ["COPY", "tmp:0:8", ["const:d60:8"]]
- 004c82b0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004c82b0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004c82b0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 004c82f0 ["COPY", "tmp:0:8", ["const:d91:8"]]
+ 004c82f0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 004c82f0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 004c82f0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004c82b0 bytes 4a813591
+ 004c82f0 bytes 4a453691
- 004c838c ["INT_ADD", "register:40f0:8", ["const:4c838c:8", "const:4:8"]]
- 004c838c ["CALL", null, ["callee:00c57fc0:8"]]
+ 004c83cc ["INT_ADD", "register:40f0:8", ["const:4c83cc:8", "const:4:8"]]
+ 004c83cc ["CALL", null, ["callee:00c57fc0:8"]]
- 004c838c bytes d93e1e94
+ 004c83cc bytes fd3e1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1df0ac46666b7248b241fb12d32d7628"></a>

### [`004c8410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8410.md) → [`004c8450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8450.md) _ZN5Botan4Pipe15set_default_msgEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

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
      "definition_site": "004c84c0",
      "incomplete_value": false,
      "site": "004c84c8",
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
            "const:c03:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c8480",
      "incomplete_value": false,
      "site": "004c8488",
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
            "const:bd2:8"
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
      "definition_site": "004c84fc",
      "incomplete_value": true,
      "site": "004c8508",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c84bc",
      "incomplete_value": true,
      "site": "004c84c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c84f8",
      "incomplete_value": false,
      "site": "004c8508",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004c84b8",
      "incomplete_value": false,
      "site": "004c84c8",
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
      "004c84c0",
      "PARAM",
      [
        "storage",
        "002b1bd2",
        null,
        "string"
      ]
    ],
    [
      "004c84f8",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004c84fc",
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
      "004c84c0",
      "PARAM",
      [
        "storage",
        "002b1c03",
        null,
        "string"
      ]
    ],
    [
      "004c84f8",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004c84fc",
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

- 旧版 [`004c8488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8410.md#insn-004c8488) · [`004c84c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8410.md#insn-004c84c8) · [`004c8474`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8410.md#insn-004c8474)
- 新版 [`004c84c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8450.md#insn-004c84c8) · [`004c8508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8450.md#insn-004c8508) · [`004c84b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8450.md#insn-004c84b4)

~~~diff
- 004c8488 ["INT_ADD", "register:40f0:8", ["const:4c8488:8", "const:4:8"]]
- 004c8488 ["CALL", null, ["callee:0043de18:8"]]
+ 004c84c8 ["INT_ADD", "register:40f0:8", ["const:4c84c8:8", "const:4:8"]]
+ 004c84c8 ["CALL", null, ["callee:0043de18:8"]]
- 004c8488 bytes 54d6fd97
+ 004c84c8 bytes 54d6fd97
- 004c84c8 ["INT_ADD", "register:40f0:8", ["const:4c84c8:8", "const:4:8"]]
- 004c84c8 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004c8508 ["INT_ADD", "register:40f0:8", ["const:4c8508:8", "const:4:8"]]
+ 004c8508 ["CALL", null, ["callee:00c57fe0:8"]]
- 004c84c8 bytes 923e1e94
+ 004c8508 bytes b63e1e94
- 004c8474 ["INT_ADD", "register:40f0:8", ["const:4c8474:8", "const:4:8"]]
- 004c8474 ["CALL", null, ["callee:00c57fc0:8"]]
+ 004c84b4 ["INT_ADD", "register:40f0:8", ["const:4c84b4:8", "const:4:8"]]
+ 004c84b4 ["CALL", null, ["callee:00c57fc0:8"]]
- 004c8474 bytes 9f3e1e94
+ 004c84b4 bytes c33e1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afcbea120c736e5f5126339613bb4a1c"></a>

### [`004c8570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8570.md) → [`004c85b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c85b0.md) _ZN5Botan4Pipe9start_msgEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c59050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59050.md) · 呼出先 10件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00543c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543c5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00c59120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59120.md) · 呼出先 10件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004aeca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00543c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543c9c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "004c8604",
      "incomplete_value": true,
      "site": "004c8608",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c85c4",
      "incomplete_value": true,
      "site": "004c85c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c8628",
      "incomplete_value": false,
      "site": "004c8634",
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
            "const:c28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c85e8",
      "incomplete_value": false,
      "site": "004c85f4",
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
            "const:b58:8"
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
      "definition_site": "004c8690",
      "incomplete_value": false,
      "site": "004c8698",
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
            "const:790:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c8650",
      "incomplete_value": false,
      "site": "004c8658",
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
            "const:7ec:8"
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
      "004c85fc",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "004c8608",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c8634",
      "DATA",
      [
        "storage",
        "00c66b58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004c85fc",
      "READ",
      [
        "storage",
        "00c9af40",
        null,
        "pointer"
      ]
    ],
    [
      "004c8608",
      "DATA",
      [
        "storage",
        "00c66aa8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c8634",
      "DATA",
      [
        "storage",
        "00c66c28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c8658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8570.md#insn-004c8658) · [`004c8694`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8570.md#insn-004c8694) · [`004c85ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8570.md#insn-004c85ac)
- 新版 [`004c8698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c85b0.md#insn-004c8698) · [`004c86d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c85b0.md#insn-004c86d4) · [`004c85ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c85b0.md#insn-004c85ec)

~~~diff
- 004c8658 ["INT_ADD", "register:40f0:8", ["const:4c8658:8", "const:4:8"]]
- 004c8658 ["CALL", null, ["callee:0043de18:8"]]
+ 004c8698 ["INT_ADD", "register:40f0:8", ["const:4c8698:8", "const:4:8"]]
+ 004c8698 ["CALL", null, ["callee:0043de18:8"]]
- 004c8658 bytes e0d5fd97
+ 004c8698 bytes e0d5fd97
- 004c8694 ["INT_ADD", "register:40f0:8", ["const:4c8694:8", "const:4:8"]]
- 004c8694 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004c86d4 ["INT_ADD", "register:40f0:8", ["const:4c86d4:8", "const:4:8"]]
+ 004c86d4 ["CALL", null, ["callee:00c57fe0:8"]]
- 004c8694 bytes 1f3e1e94
+ 004c86d4 bytes 433e1e94
- 004c85ac ["INT_ADD", "register:40f0:8", ["const:4c85ac:8", "const:4:8"]]
- 004c85ac ["CALL", null, ["callee:00c57f60:8"]]
+ 004c85ec ["INT_ADD", "register:40f0:8", ["const:4c85ec:8", "const:4:8"]]
+ 004c85ec ["CALL", null, ["callee:00c57f60:8"]]
- 004c85ac bytes 393e1e94
+ 004c85ec bytes 5d3e1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0ebee1e639d2f93729054013c8e5ad3"></a>

### [`004c8710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8710.md) → [`004c8750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8750.md) _ZN5Botan4Pipe5writeEPKhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59060.md) · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)
- 新版 呼出元 1件 [`00c59130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59130.md) · 呼出先 6件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004aeca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)

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
      "definition_site": "004c87bc",
      "incomplete_value": false,
      "site": "004c87c4",
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
            "const:2b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c877c",
      "incomplete_value": false,
      "site": "004c8784",
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
            "const:78:8"
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
      "definition_site": "004c87f8",
      "incomplete_value": true,
      "site": "004c8804",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c87b8",
      "incomplete_value": true,
      "site": "004c87c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c87f4",
      "incomplete_value": false,
      "site": "004c8804",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004c87b4",
      "incomplete_value": false,
      "site": "004c87c4",
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
      "004c87bc",
      "PARAM",
      [
        "storage",
        "002a1078",
        null,
        "string"
      ]
    ],
    [
      "004c87f4",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004c87f8",
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
      "004c87bc",
      "PARAM",
      [
        "storage",
        "002a102b",
        null,
        "string"
      ]
    ],
    [
      "004c87f4",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004c87f8",
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

- 旧版 [`004c8784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8710.md#insn-004c8784) · [`004c87c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8710.md#insn-004c87c4) · [`004c8770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8710.md#insn-004c8770)
- 新版 [`004c87c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8750.md#insn-004c87c4) · [`004c8804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8750.md#insn-004c8804) · [`004c87b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8750.md#insn-004c87b0)

~~~diff
- 004c8784 ["INT_ADD", "register:40f0:8", ["const:4c8784:8", "const:4:8"]]
- 004c8784 ["CALL", null, ["callee:0043de18:8"]]
+ 004c87c4 ["INT_ADD", "register:40f0:8", ["const:4c87c4:8", "const:4:8"]]
+ 004c87c4 ["CALL", null, ["callee:0043de18:8"]]
- 004c8784 bytes 95d5fd97
+ 004c87c4 bytes 95d5fd97
- 004c87c4 ["INT_ADD", "register:40f0:8", ["const:4c87c4:8", "const:4:8"]]
- 004c87c4 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004c8804 ["INT_ADD", "register:40f0:8", ["const:4c8804:8", "const:4:8"]]
+ 004c8804 ["CALL", null, ["callee:00c57fe0:8"]]
- 004c87c4 bytes d33d1e94
+ 004c8804 bytes f73d1e94
- 004c8770 ["INT_ADD", "register:40f0:8", ["const:4c8770:8", "const:4:8"]]
- 004c8770 ["CALL", null, ["callee:00c57fc0:8"]]
+ 004c87b0 ["INT_ADD", "register:40f0:8", ["const:4c87b0:8", "const:4:8"]]
+ 004c87b0 ["CALL", null, ["callee:00c57fc0:8"]]
- 004c8770 bytes e03d1e94
+ 004c87b0 bytes 043e1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f5bdd4e604a66ce2a3e5adf7cfdb569"></a>

### [`004c8818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8818.md) → [`004c8858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8858.md) _ZN5Botan4Pipe7end_msgEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59070.md) · 呼出先 12件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`004c7c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c7/004c7c60.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00c59140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59140.md) · 呼出先 12件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004aeca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`004c7ca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c7/004c7ca0.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "004c88c0",
      "incomplete_value": true,
      "site": "004c88c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c8880",
      "incomplete_value": true,
      "site": "004c8884",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004c88b0",
      "incomplete_value": true,
      "site": "004c88b0",
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
      "definition_site": "004c8870",
      "incomplete_value": true,
      "site": "004c8870",
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
      "definition_site": "004c88f8",
      "incomplete_value": true,
      "site": "004c88f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c88b8",
      "incomplete_value": true,
      "site": "004c88b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004c88b8",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "004c88c4",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c88e8",
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
      "004c88b8",
      "READ",
      [
        "storage",
        "00c9af40",
        null,
        "pointer"
      ]
    ],
    [
      "004c88c4",
      "DATA",
      [
        "storage",
        "00c66aa8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c88e8",
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

- 旧版 [`004c8878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8818.md#insn-004c8878) · [`004c88b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8818.md#insn-004c88b8) · [`004c8914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8818.md#insn-004c8914)
- 新版 [`004c88b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8858.md#insn-004c88b8) · [`004c88f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8858.md#insn-004c88f8) · [`004c8954`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8858.md#insn-004c8954)

~~~diff
- 004c8878 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
- 004c8878 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c88b8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f40:8"]]
+ 004c88b8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c8878 bytes 083947f9
+ 004c88b8 bytes 08a147f9
- 004c88b8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c88b8 ["INT_ADD", "register:40f0:8", ["const:4c88b8:8", "const:4:8"]]
- 004c88b8 ["CALLIND", null, ["register:0:8"]]
+ 004c88f8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c88f8 ["INT_ADD", "register:40f0:8", ["const:4c88f8:8", "const:4:8"]]
+ 004c88f8 ["CALLIND", null, ["register:0:8"]]
- 004c88b8 bytes 20013fd6
+ 004c88f8 bytes 20013fd6
- 004c8914 ["INT_ADD", "register:40f0:8", ["const:4c8914:8", "const:4:8"]]
- 004c8914 ["CALL", null, ["callee:0043de18:8"]]
+ 004c8954 ["INT_ADD", "register:40f0:8", ["const:4c8954:8", "const:4:8"]]
+ 004c8954 ["CALL", null, ["callee:0043de18:8"]]
- 004c8914 bytes 31d5fd97
+ 004c8954 bytes 31d5fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e02a2af34cc8abef30f794595e8e1085"></a>

### [`004c8ab4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8ab4.md) → [`004c8af4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8af4.md) _ZN5Botan4Pipe5writeERNS_10DataSourceE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c590a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c590a0.md) · 呼出先 9件 [`00c37ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ba4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md)
- 新版 呼出元 1件 [`00c59170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59170.md) · 呼出先 9件 [`00c37c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c40.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.30% / 新版 97.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004c8bb0",
      "incomplete_value": true,
      "site": "004c8bb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c8b70",
      "incomplete_value": true,
      "site": "004c8b70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c8c0c",
      "incomplete_value": true,
      "site": "004c8c14",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eb8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c8bcc",
      "incomplete_value": true,
      "site": "004c8bd4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c8c10",
      "incomplete_value": true,
      "site": "004c8c14",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c8bd0",
      "incomplete_value": true,
      "site": "004c8bd4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004c8b9c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004c8c0c",
      "READ",
      [
        "storage",
        "00c9ade8",
        null,
        "pointer"
      ]
    ],
    [
      "004c8c0c",
      "PARAM",
      [
        "storage",
        "00c96698",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004c8b9c",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "004c8c0c",
      "READ",
      [
        "storage",
        "00c9aeb8",
        null,
        "pointer"
      ]
    ],
    [
      "004c8c0c",
      "PARAM",
      [
        "storage",
        "00c96768",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c8b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8ab4.md#insn-004c8b70) · [`004c8bd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8ab4.md#insn-004c8bd4) · [`004c8c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8ab4.md#insn-004c8c14)
- 新版 [`004c8bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8af4.md#insn-004c8bb0) · [`004c8c14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8af4.md#insn-004c8c14) · [`004c8c54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8af4.md#insn-004c8c54)

~~~diff
- 004c8b70 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c8b70 ["INT_ADD", "register:40f0:8", ["const:4c8b70:8", "const:4:8"]]
- 004c8b70 ["CALLIND", null, ["register:0:8"]]
+ 004c8bb0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c8bb0 ["INT_ADD", "register:40f0:8", ["const:4c8bb0:8", "const:4:8"]]
+ 004c8bb0 ["CALLIND", null, ["register:0:8"]]
- 004c8b70 bytes 20013fd6
+ 004c8bb0 bytes 20013fd6
- 004c8bd4 ["INT_ADD", "register:40f0:8", ["const:4c8bd4:8", "const:4:8"]]
- 004c8bd4 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004c8c14 ["INT_ADD", "register:40f0:8", ["const:4c8c14:8", "const:4:8"]]
+ 004c8c14 ["CALL", null, ["callee:00c57fe0:8"]]
- 004c8bd4 bytes cf3c1e94
+ 004c8c14 bytes f33c1e94
- 004c8c14 ["INT_ADD", "register:40f0:8", ["const:4c8c14:8", "const:4:8"]]
- 004c8c14 ["CALL", null, ["callee:00c57fb0:8"]]
+ 004c8c54 ["INT_ADD", "register:40f0:8", ["const:4c8c54:8", "const:4:8"]]
+ 004c8c54 ["CALL", null, ["callee:00c57fb0:8"]]
- 004c8c14 bytes b33c1e94
+ 004c8c54 bytes d73c1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2747439275369c5768a8df4c1b34b676"></a>

### [`004c8d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8d68.md) → [`004c8da8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8da8.md) _ZN5Botan4Pipe13append_filterEPNS_6FilterE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004aeca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)

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
      "definition_site": "004c8e10",
      "incomplete_value": false,
      "site": "004c8e18",
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
            "const:46b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c8dd0",
      "incomplete_value": false,
      "site": "004c8dd8",
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
            "const:4c7:8"
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
      "definition_site": "004c8e4c",
      "incomplete_value": true,
      "site": "004c8e58",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c8e0c",
      "incomplete_value": true,
      "site": "004c8e18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c8e48",
      "incomplete_value": false,
      "site": "004c8e58",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004c8e08",
      "incomplete_value": false,
      "site": "004c8e18",
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
      "004c8e10",
      "PARAM",
      [
        "storage",
        "002a54c7",
        null,
        "string"
      ]
    ],
    [
      "004c8e48",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004c8e4c",
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
      "004c8e10",
      "PARAM",
      [
        "storage",
        "002a546b",
        null,
        "string"
      ]
    ],
    [
      "004c8e48",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004c8e4c",
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

- 旧版 [`004c8dd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8d68.md#insn-004c8dd8) · [`004c8e18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8d68.md#insn-004c8e18) · [`004c8dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8d68.md#insn-004c8dc4)
- 新版 [`004c8e18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8da8.md#insn-004c8e18) · [`004c8e58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8da8.md#insn-004c8e58) · [`004c8e04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8da8.md#insn-004c8e04)

~~~diff
- 004c8dd8 ["INT_ADD", "register:40f0:8", ["const:4c8dd8:8", "const:4:8"]]
- 004c8dd8 ["CALL", null, ["callee:0043de18:8"]]
+ 004c8e18 ["INT_ADD", "register:40f0:8", ["const:4c8e18:8", "const:4:8"]]
+ 004c8e18 ["CALL", null, ["callee:0043de18:8"]]
- 004c8dd8 bytes 00d4fd97
+ 004c8e18 bytes 00d4fd97
- 004c8e18 ["INT_ADD", "register:40f0:8", ["const:4c8e18:8", "const:4:8"]]
- 004c8e18 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004c8e58 ["INT_ADD", "register:40f0:8", ["const:4c8e58:8", "const:4:8"]]
+ 004c8e58 ["CALL", null, ["callee:00c57fe0:8"]]
- 004c8e18 bytes 3e3c1e94
+ 004c8e58 bytes 623c1e94
- 004c8dc4 ["INT_ADD", "register:40f0:8", ["const:4c8dc4:8", "const:4:8"]]
- 004c8dc4 ["CALL", null, ["callee:00c57fc0:8"]]
+ 004c8e04 ["INT_ADD", "register:40f0:8", ["const:4c8e04:8", "const:4:8"]]
+ 004c8e04 ["CALL", null, ["callee:00c57fc0:8"]]
- 004c8dc4 bytes 4b3c1e94
+ 004c8e04 bytes 6f3c1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3fbf96ed7318c4df7a2343329a384be9"></a>

### [`004c8e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8e6c.md) → [`004c8eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8eac.md) _ZN5Botan4Pipe7prependEPNS_6FilterE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004aeca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)

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
      "definition_site": "004c8ee8",
      "incomplete_value": true,
      "site": "004c8eec",
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
      "definition_site": "004c8ea8",
      "incomplete_value": true,
      "site": "004c8eac",
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
      "definition_site": "004c8f78",
      "incomplete_value": false,
      "site": "004c8f80",
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
            "const:93:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c8f38",
      "incomplete_value": false,
      "site": "004c8f40",
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
            "const:53:8"
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
      "definition_site": "004c8fb4",
      "incomplete_value": true,
      "site": "004c8fc0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c8f74",
      "incomplete_value": true,
      "site": "004c8f80",
      "value": [
        "LOAD",
        "8",
        [
          [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004c8edc",
      "READ",
      [
        "storage",
        "00c9af08",
        null,
        "pointer"
      ]
    ],
    [
      "004c8f78",
      "PARAM",
      [
        "storage",
        "002b6053",
        null,
        "string"
      ]
    ],
    [
      "004c8fb0",
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
      "004c8edc",
      "READ",
      [
        "storage",
        "00c9afd8",
        null,
        "pointer"
      ]
    ],
    [
      "004c8f78",
      "PARAM",
      [
        "storage",
        "002b6093",
        null,
        "string"
      ]
    ],
    [
      "004c8fb0",
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

- 旧版 [`004c8f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8e6c.md#insn-004c8f40) · [`004c8f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8e6c.md#insn-004c8f80) · [`004c8fa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8e6c.md#insn-004c8fa4)
- 新版 [`004c8f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8eac.md#insn-004c8f80) · [`004c8fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8eac.md#insn-004c8fc0) · [`004c8fe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c8/004c8eac.md#insn-004c8fe4)

~~~diff
- 004c8f40 ["INT_ADD", "register:40f0:8", ["const:4c8f40:8", "const:4:8"]]
- 004c8f40 ["CALL", null, ["callee:0043de18:8"]]
+ 004c8f80 ["INT_ADD", "register:40f0:8", ["const:4c8f80:8", "const:4:8"]]
+ 004c8f80 ["CALL", null, ["callee:0043de18:8"]]
- 004c8f40 bytes a6d3fd97
+ 004c8f80 bytes a6d3fd97
- 004c8f80 ["INT_ADD", "register:40f0:8", ["const:4c8f80:8", "const:4:8"]]
- 004c8f80 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004c8fc0 ["INT_ADD", "register:40f0:8", ["const:4c8fc0:8", "const:4:8"]]
+ 004c8fc0 ["CALL", null, ["callee:00c57fe0:8"]]
- 004c8f80 bytes e43b1e94
+ 004c8fc0 bytes 083c1e94
- 004c8fa4 ["INT_ADD", "register:40f0:8", ["const:4c8fa4:8", "const:4:8"]]
- 004c8fa4 ["CALL", null, ["callee:0043de18:8"]]
+ 004c8fe4 ["INT_ADD", "register:40f0:8", ["const:4c8fe4:8", "const:4:8"]]
+ 004c8fe4 ["CALL", null, ["callee:0043de18:8"]]
- 004c8fa4 bytes 8dd3fd97
+ 004c8fe4 bytes 8dd3fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5948b64635fe38c11116f7e0a6653e6b"></a>

### [`004c90a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c9/004c90a4.md) → [`004c90e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c90e4.md) _ZN5Botan4Pipe3popEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004aeca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)

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
      "definition_site": "004c9190",
      "incomplete_value": false,
      "site": "004c9198",
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
            "const:4ca:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c9150",
      "incomplete_value": false,
      "site": "004c9158",
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
            "const:526:8"
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
      "definition_site": "004c91cc",
      "incomplete_value": true,
      "site": "004c91d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c918c",
      "incomplete_value": true,
      "site": "004c9198",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c91c8",
      "incomplete_value": false,
      "site": "004c91d8",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004c9188",
      "incomplete_value": false,
      "site": "004c9198",
      "value": [
        "leaf",
        "const:535868:8"
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
      "004c9190",
      "PARAM",
      [
        "storage",
        "002a5526",
        null,
        "string"
      ]
    ],
    [
      "004c91c8",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004c91cc",
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
      "004c9190",
      "PARAM",
      [
        "storage",
        "002a54ca",
        null,
        "string"
      ]
    ],
    [
      "004c91c8",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004c91cc",
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

- 旧版 [`004c9158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c9/004c90a4.md#insn-004c9158) · [`004c9198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c9/004c90a4.md#insn-004c9198) · [`004c91bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c9/004c90a4.md#insn-004c91bc)
- 新版 [`004c9198`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c90e4.md#insn-004c9198) · [`004c91d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c90e4.md#insn-004c91d8) · [`004c91fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c90e4.md#insn-004c91fc)

~~~diff
- 004c9158 ["INT_ADD", "register:40f0:8", ["const:4c9158:8", "const:4:8"]]
- 004c9158 ["CALL", null, ["callee:0043de18:8"]]
+ 004c9198 ["INT_ADD", "register:40f0:8", ["const:4c9198:8", "const:4:8"]]
+ 004c9198 ["CALL", null, ["callee:0043de18:8"]]
- 004c9158 bytes 20d3fd97
+ 004c9198 bytes 20d3fd97
- 004c9198 ["INT_ADD", "register:40f0:8", ["const:4c9198:8", "const:4:8"]]
- 004c9198 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004c91d8 ["INT_ADD", "register:40f0:8", ["const:4c91d8:8", "const:4:8"]]
+ 004c91d8 ["CALL", null, ["callee:00c57fe0:8"]]
- 004c9198 bytes 5e3b1e94
+ 004c91d8 bytes 823b1e94
- 004c91bc ["INT_ADD", "register:40f0:8", ["const:4c91bc:8", "const:4:8"]]
- 004c91bc ["CALL", null, ["callee:0043de18:8"]]
+ 004c91fc ["INT_ADD", "register:40f0:8", ["const:4c91fc:8", "const:4:8"]]
+ 004c91fc ["CALL", null, ["callee:0043de18:8"]]
- 004c91bc bytes 07d3fd97
+ 004c91fc bytes 07d3fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d048c1f52ed6766c0eb9d2b5fce29b5d"></a>

### [`004c9250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c9/004c9250.md) → [`004c9290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c9290.md) _ZN5BotanlsERNSt6__ndk113basic_ostreamIcNS0_11char_traitsIcEEEERNS_4PipeE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 14件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c37ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ba4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c37c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c40.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004c9368",
      "incomplete_value": true,
      "site": "004c9368",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c9328",
      "incomplete_value": true,
      "site": "004c9328",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c93c8",
      "incomplete_value": true,
      "site": "004c93d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eb8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c9388",
      "incomplete_value": true,
      "site": "004c9390",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c93cc",
      "incomplete_value": true,
      "site": "004c93d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c938c",
      "incomplete_value": true,
      "site": "004c9390",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004c9358",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004c93c8",
      "READ",
      [
        "storage",
        "00c9ade8",
        null,
        "pointer"
      ]
    ],
    [
      "004c93c8",
      "PARAM",
      [
        "storage",
        "00c96698",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004c9358",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "004c93c8",
      "READ",
      [
        "storage",
        "00c9aeb8",
        null,
        "pointer"
      ]
    ],
    [
      "004c93c8",
      "PARAM",
      [
        "storage",
        "00c96768",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c92e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c9/004c9250.md#insn-004c92e8) · [`004c9328`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c9/004c9250.md#insn-004c9328) · [`004c9368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c9/004c9250.md#insn-004c9368)
- 新版 [`004c9328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c9290.md#insn-004c9328) · [`004c9368`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c9290.md#insn-004c9368) · [`004c93a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c9290.md#insn-004c93a8)

~~~diff
- 004c92e8 ["INT_ADD", "register:40f0:8", ["const:4c92e8:8", "const:4:8"]]
- 004c92e8 ["CALL", null, ["callee:00c58d40:8"]]
+ 004c9328 ["INT_ADD", "register:40f0:8", ["const:4c9328:8", "const:4:8"]]
+ 004c9328 ["CALL", null, ["callee:00c58d40:8"]]
- 004c92e8 bytes 623e1e94
+ 004c9328 bytes 863e1e94
- 004c9328 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c9328 ["INT_ADD", "register:40f0:8", ["const:4c9328:8", "const:4:8"]]
- 004c9328 ["CALLIND", null, ["register:0:8"]]
+ 004c9368 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c9368 ["INT_ADD", "register:40f0:8", ["const:4c9368:8", "const:4:8"]]
+ 004c9368 ["CALLIND", null, ["register:0:8"]]
- 004c9328 bytes 20013fd6
+ 004c9368 bytes 20013fd6
- 004c9368 ["INT_ADD", "register:40f0:8", ["const:4c9368:8", "const:4:8"]]
- 004c9368 ["CALL", null, ["callee:00c58b10:8"]]
+ 004c93a8 ["INT_ADD", "register:40f0:8", ["const:4c93a8:8", "const:4:8"]]
+ 004c93a8 ["CALL", null, ["callee:00c58b10:8"]]
- 004c9368 bytes b63d1e94
+ 004c93a8 bytes da3d1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7618cf79294d023c7ee5110d98d6f26d"></a>

### [`004c9468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c9/004c9468.md) → [`004c94a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c94a8.md) _ZN5BotanrsERNSt6__ndk113basic_istreamIcNS0_11char_traitsIcEEEERNS_4PipeE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 13件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c37ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ba4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c37c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c40.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.92% / 新版 95.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004c9568",
      "incomplete_value": true,
      "site": "004c9568",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c9528",
      "incomplete_value": true,
      "site": "004c9528",
      "value": [
        "LOAD",
        "8",
        [
          [
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c95c8",
      "incomplete_value": true,
      "site": "004c95d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eb8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c9588",
      "incomplete_value": true,
      "site": "004c9590",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c95cc",
      "incomplete_value": true,
      "site": "004c95d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004c958c",
      "incomplete_value": true,
      "site": "004c9590",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004c9558",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004c95c8",
      "READ",
      [
        "storage",
        "00c9ade8",
        null,
        "pointer"
      ]
    ],
    [
      "004c95c8",
      "PARAM",
      [
        "storage",
        "00c96698",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004c9558",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "004c95c8",
      "READ",
      [
        "storage",
        "00c9aeb8",
        null,
        "pointer"
      ]
    ],
    [
      "004c95c8",
      "PARAM",
      [
        "storage",
        "00c96768",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c9528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c9/004c9468.md#insn-004c9528) · [`004c9568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c9/004c9468.md#insn-004c9568) · [`004c9590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c9/004c9468.md#insn-004c9590)
- 新版 [`004c9568`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c94a8.md#insn-004c9568) · [`004c95a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c94a8.md#insn-004c95a8) · [`004c95d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004c9/004c94a8.md#insn-004c95d0)

~~~diff
- 004c9528 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c9528 ["INT_ADD", "register:40f0:8", ["const:4c9528:8", "const:4:8"]]
- 004c9528 ["CALLIND", null, ["register:0:8"]]
+ 004c9568 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c9568 ["INT_ADD", "register:40f0:8", ["const:4c9568:8", "const:4:8"]]
+ 004c9568 ["CALLIND", null, ["register:0:8"]]
- 004c9528 bytes 20013fd6
+ 004c9568 bytes 20013fd6
- 004c9568 ["INT_ADD", "register:40f0:8", ["const:4c9568:8", "const:4:8"]]
- 004c9568 ["CALL", null, ["callee:00c58b10:8"]]
+ 004c95a8 ["INT_ADD", "register:40f0:8", ["const:4c95a8:8", "const:4:8"]]
+ 004c95a8 ["CALL", null, ["callee:00c58b10:8"]]
- 004c9568 bytes 363d1e94
+ 004c95a8 bytes 5a3d1e94
- 004c9590 ["INT_ADD", "register:40f0:8", ["const:4c9590:8", "const:4:8"]]
- 004c9590 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004c95d0 ["INT_ADD", "register:40f0:8", ["const:4c95d0:8", "const:4:8"]]
+ 004c95d0 ["CALL", null, ["callee:00c57fe0:8"]]
- 004c9590 bytes 603a1e94
+ 004c95d0 bytes 843a1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

