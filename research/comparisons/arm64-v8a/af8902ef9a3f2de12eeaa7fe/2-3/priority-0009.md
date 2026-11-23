# v16.0.0 → v16.0.1 · 最優先の変更候補 (9)

[一覧の目次](README.md)

<a id="compare-7b8da0a49fb74fcff6df3c414bf29905"></a>

### [`004c9064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9064.md) → [`004c90a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c9/004c90a4.md) _ZN5Botan4Pipe3popEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

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
    "old": {
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c9188",
      "incomplete_value": false,
      "site": "004c9198",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004c9148",
      "incomplete_value": false,
      "site": "004c9158",
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
      "004c9150",
      "PARAM",
      [
        "storage",
        "002a544a",
        null,
        "string"
      ]
    ],
    [
      "004c9188",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004c918c",
      "READ",
      [
        "storage",
        "00c9a948",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c9150",
      "PARAM",
      [
        "storage",
        "002a5526",
        null,
        "string"
      ]
    ],
    [
      "004c9188",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004c918c",
      "READ",
      [
        "storage",
        "00c9ad48",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c9118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9064.md#insn-004c9118) · [`004c9158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9064.md#insn-004c9158) · [`004c917c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9064.md#insn-004c917c)
- 新版 `004c9158`（命令位置の公開資料なし） · `004c9198`（命令位置の公開資料なし） · `004c91bc`（命令位置の公開資料なし）

~~~diff
- 004c9118 ["INT_ADD", "register:40f0:8", ["const:4c9118:8", "const:4:8"]]
- 004c9118 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004c9158 ["INT_ADD", "register:40f0:8", ["const:4c9158:8", "const:4:8"]]
+ 004c9158 ["CALL", null, ["callee:0043ddd8:8"]]
- 004c9118 bytes 20d3fd97
+ 004c9158 bytes 20d3fd97
- 004c9158 ["INT_ADD", "register:40f0:8", ["const:4c9158:8", "const:4:8"]]
- 004c9158 ["CALL", null, ["callee:00c57f10:8"]]
+ 004c9198 ["INT_ADD", "register:40f0:8", ["const:4c9198:8", "const:4:8"]]
+ 004c9198 ["CALL", null, ["callee:00c57f10:8"]]
- 004c9158 bytes 6e3a1e94
+ 004c9198 bytes 5e3b1e94
- 004c917c ["INT_ADD", "register:40f0:8", ["const:4c917c:8", "const:4:8"]]
- 004c917c ["CALL", null, ["callee:0043ddd8:8"]]
+ 004c91bc ["INT_ADD", "register:40f0:8", ["const:4c91bc:8", "const:4:8"]]
+ 004c91bc ["CALL", null, ["callee:0043ddd8:8"]]
- 004c917c bytes 07d3fd97
+ 004c91bc bytes 07d3fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7f045214ac07aa556af8aadd0ca6d92"></a>

### [`004c9210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9210.md) → [`004c9250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c9/004c9250.md) _ZN5BotanlsERNSt6__ndk113basic_ostreamIcNS0_11char_traitsIcEEEERNS_4PipeE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 14件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c37ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ba4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

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
    "old": {
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "004c934c",
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
                "const:9f0:8"
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
      "004c9318",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004c9388",
      "READ",
      [
        "storage",
        "00c9a9e8",
        null,
        "pointer"
      ]
    ],
    [
      "004c9388",
      "PARAM",
      [
        "storage",
        "00c96298",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004c9318",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004c9388",
      "READ",
      [
        "storage",
        "00c9ade8",
        null,
        "pointer"
      ]
    ],
    [
      "004c9388",
      "PARAM",
      [
        "storage",
        "00c96698",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c92a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9210.md#insn-004c92a8) · [`004c92e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9210.md#insn-004c92e8) · [`004c9328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9210.md#insn-004c9328)
- 新版 `004c92e8`（命令位置の公開資料なし） · `004c9328`（命令位置の公開資料なし） · `004c9368`（命令位置の公開資料なし）

~~~diff
- 004c92a8 ["INT_ADD", "register:40f0:8", ["const:4c92a8:8", "const:4:8"]]
- 004c92a8 ["CALL", null, ["callee:00c58c70:8"]]
+ 004c92e8 ["INT_ADD", "register:40f0:8", ["const:4c92e8:8", "const:4:8"]]
+ 004c92e8 ["CALL", null, ["callee:00c58c70:8"]]
- 004c92a8 bytes 723d1e94
+ 004c92e8 bytes 623e1e94
- 004c92e8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c92e8 ["INT_ADD", "register:40f0:8", ["const:4c92e8:8", "const:4:8"]]
- 004c92e8 ["CALLIND", null, ["register:0:8"]]
+ 004c9328 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c9328 ["INT_ADD", "register:40f0:8", ["const:4c9328:8", "const:4:8"]]
+ 004c9328 ["CALLIND", null, ["register:0:8"]]
- 004c92e8 bytes 20013fd6
+ 004c9328 bytes 20013fd6
- 004c9328 ["INT_ADD", "register:40f0:8", ["const:4c9328:8", "const:4:8"]]
- 004c9328 ["CALL", null, ["callee:00c58a40:8"]]
+ 004c9368 ["INT_ADD", "register:40f0:8", ["const:4c9368:8", "const:4:8"]]
+ 004c9368 ["CALL", null, ["callee:00c58a40:8"]]
- 004c9328 bytes c63c1e94
+ 004c9368 bytes b63d1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f43473430537fdb50d25495163bf7f32"></a>

### [`004c9428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9428.md) → [`004c9468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c9/004c9468.md) _ZN5BotanrsERNSt6__ndk113basic_istreamIcNS0_11char_traitsIcEEEERNS_4PipeE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 13件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c37ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ba4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

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
    "old": {
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
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "004c954c",
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
                "const:9f0:8"
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
      "004c9518",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004c9588",
      "READ",
      [
        "storage",
        "00c9a9e8",
        null,
        "pointer"
      ]
    ],
    [
      "004c9588",
      "PARAM",
      [
        "storage",
        "00c96298",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004c9518",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004c9588",
      "READ",
      [
        "storage",
        "00c9ade8",
        null,
        "pointer"
      ]
    ],
    [
      "004c9588",
      "PARAM",
      [
        "storage",
        "00c96698",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c94e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9428.md#insn-004c94e8) · [`004c9528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9428.md#insn-004c9528) · [`004c9550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9428.md#insn-004c9550)
- 新版 `004c9528`（命令位置の公開資料なし） · `004c9568`（命令位置の公開資料なし） · `004c9590`（命令位置の公開資料なし）

~~~diff
- 004c94e8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c94e8 ["INT_ADD", "register:40f0:8", ["const:4c94e8:8", "const:4:8"]]
- 004c94e8 ["CALLIND", null, ["register:0:8"]]
+ 004c9528 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c9528 ["INT_ADD", "register:40f0:8", ["const:4c9528:8", "const:4:8"]]
+ 004c9528 ["CALLIND", null, ["register:0:8"]]
- 004c94e8 bytes 20013fd6
+ 004c9528 bytes 20013fd6
- 004c9528 ["INT_ADD", "register:40f0:8", ["const:4c9528:8", "const:4:8"]]
- 004c9528 ["CALL", null, ["callee:00c58a40:8"]]
+ 004c9568 ["INT_ADD", "register:40f0:8", ["const:4c9568:8", "const:4:8"]]
+ 004c9568 ["CALL", null, ["callee:00c58a40:8"]]
- 004c9528 bytes 463c1e94
+ 004c9568 bytes 363d1e94
- 004c9550 ["INT_ADD", "register:40f0:8", ["const:4c9550:8", "const:4:8"]]
- 004c9550 ["CALL", null, ["callee:00c57f10:8"]]
+ 004c9590 ["INT_ADD", "register:40f0:8", ["const:4c9590:8", "const:4:8"]]
+ 004c9590 ["CALL", null, ["callee:00c57f10:8"]]
- 004c9550 bytes 70391e94
+ 004c9590 bytes 603a1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-235cd0de6e735c90b96c4595f5af6eea"></a>

### [`004c9620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9620.md) → [`004c9660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c9/004c9660.md) _ZNK5Botan4Pipe14get_message_noERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`004c96cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c96cc.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004c970c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c9/004c970c.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
      "definition_site": "004c96ec",
      "incomplete_value": true,
      "site": "004c96f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c96e8",
      "incomplete_value": false,
      "site": "004c96f4",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004c96a8",
      "incomplete_value": false,
      "site": "004c96b4",
      "value": [
        "leaf",
        "const:535828:8"
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
      "004c96e8",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004c96ec",
      "READ",
      [
        "storage",
        "00c9ab10",
        null,
        "pointer"
      ]
    ],
    [
      "004c96ec",
      "PARAM",
      [
        "storage",
        "00c66798",
        "_ZTIN5Botan4Pipe22Invalid_Message_NumberE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004c96e8",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004c96ec",
      "READ",
      [
        "storage",
        "00c9af10",
        null,
        "pointer"
      ]
    ],
    [
      "004c96ec",
      "PARAM",
      [
        "storage",
        "00c66b98",
        "_ZTIN5Botan4Pipe22Invalid_Message_NumberE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c96b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9620.md#insn-004c96b4) · [`004c968c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9620.md#insn-004c968c) · [`004c969c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9620.md#insn-004c969c)
- 新版 `004c96f4`（命令位置の公開資料なし） · `004c96cc`（命令位置の公開資料なし） · `004c96dc`（命令位置の公開資料なし）

~~~diff
- 004c96b4 ["INT_ADD", "register:40f0:8", ["const:4c96b4:8", "const:4:8"]]
- 004c96b4 ["CALL", null, ["callee:00c57f10:8"]]
+ 004c96f4 ["INT_ADD", "register:40f0:8", ["const:4c96f4:8", "const:4:8"]]
+ 004c96f4 ["CALL", null, ["callee:00c57f10:8"]]
- 004c96b4 bytes 17391e94
+ 004c96f4 bytes 073a1e94
- 004c968c ["INT_ADD", "register:40f0:8", ["const:4c968c:8", "const:4:8"]]
- 004c968c ["CALL", null, ["callee:00c57ef0:8"]]
+ 004c96cc ["INT_ADD", "register:40f0:8", ["const:4c96cc:8", "const:4:8"]]
+ 004c96cc ["CALL", null, ["callee:00c57ef0:8"]]
- 004c968c bytes 19391e94
+ 004c96cc bytes 093a1e94
- 004c969c ["INT_ADD", "register:40f0:8", ["const:4c969c:8", "const:4:8"]]
- 004c969c ["CALL", null, ["callee:004c970c:8"]]
+ 004c96dc ["INT_ADD", "register:40f0:8", ["const:4c96dc:8", "const:4:8"]]
+ 004c96dc ["CALL", null, ["callee:004c970c:8"]]
- 004c969c bytes 0c000094
+ 004c96dc bytes 0c000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-871421fb066860daebc039e1b09dedaf"></a>

### [`004c96cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c96cc.md) → [`004c970c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c9/004c970c.md) FUN_004c970c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`004c8258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c8258.md) [`004c9620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9620.md) [`004c9940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9940.md) [`004c9cbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9cbc.md) · 呼出先 7件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)
- 新版 呼出元 4件 [`004c8298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8298.md) [`004c9660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c9/004c9660.md) [`004c9980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c9/004c9980.md) [`004c9cfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c9/004c9cfc.md) · 呼出先 7件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.59% / 新版 96.59%

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
      "definition_site": "004c97d4",
      "incomplete_value": true,
      "site": "004c97d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004c9808",
      "incomplete_value": true,
      "site": "004c980c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c972c",
      "incomplete_value": false,
      "site": "004c9740",
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
            "const:a01:8"
          ]
        ]
      ]
    },
    "old": {
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
      "004c972c",
      "PARAM",
      [
        "storage",
        "002bd9c1",
        null,
        "string"
      ]
    ],
    [
      "004c9748",
      "PARAM",
      [
        "storage",
        "002bb468",
        null,
        "string"
      ]
    ],
    [
      "004c97b8",
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
      "004c972c",
      "PARAM",
      [
        "storage",
        "002bda01",
        null,
        "string"
      ]
    ],
    [
      "004c9748",
      "PARAM",
      [
        "storage",
        "002bb4a8",
        null,
        "string"
      ]
    ],
    [
      "004c97b8",
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

- 旧版 [`004c9700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c96cc.md#insn-004c9700) · [`004c9710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c96cc.md#insn-004c9710) · [`004c9758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c96cc.md#insn-004c9758)
- 新版 `004c9740`（命令位置の公開資料なし） · `004c9750`（命令位置の公開資料なし） · `004c9798`（命令位置の公開資料なし）

~~~diff
- 004c9700 ["INT_ADD", "register:40f0:8", ["const:4c9700:8", "const:4:8"]]
- 004c9700 ["CALL", null, ["callee:00c580b0:8"]]
+ 004c9740 ["INT_ADD", "register:40f0:8", ["const:4c9740:8", "const:4:8"]]
+ 004c9740 ["CALL", null, ["callee:00c580b0:8"]]
- 004c9700 bytes 6c391e94
+ 004c9740 bytes 5c3a1e94
- 004c9710 ["INT_ADD", "register:40f0:8", ["const:4c9710:8", "const:4:8"]]
- 004c9710 ["CALL", null, ["callee:00c57f70:8"]]
+ 004c9750 ["INT_ADD", "register:40f0:8", ["const:4c9750:8", "const:4:8"]]
+ 004c9750 ["CALL", null, ["callee:00c57f70:8"]]
- 004c9710 bytes 18391e94
+ 004c9750 bytes 083a1e94
- 004c9758 ["INT_ADD", "register:40f0:8", ["const:4c9758:8", "const:4:8"]]
- 004c9758 ["CALL", null, ["callee:00c57f80:8"]]
+ 004c9798 ["INT_ADD", "register:40f0:8", ["const:4c9798:8", "const:4:8"]]
+ 004c9798 ["CALL", null, ["callee:00c57f80:8"]]
- 004c9758 bytes 0a391e94
+ 004c9798 bytes fa391e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-402d42e1ebe65f6a8ed64dd4713693cb"></a>

### [`004c9940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9940.md) → [`004c9980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c9/004c9980.md) _ZN5Botan4Pipe4readEPhmm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58cc0.md) · 呼出先 6件 [`004c96cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c96cc.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`00c590c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c590c0.md) · 呼出先 6件 [`004c970c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c9/004c970c.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
      "definition_site": "004c9a84",
      "incomplete_value": true,
      "site": "004c9a8c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c9a80",
      "incomplete_value": false,
      "site": "004c9a8c",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004c9a40",
      "incomplete_value": false,
      "site": "004c9a4c",
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
      "004c9a80",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004c9a84",
      "READ",
      [
        "storage",
        "00c9ab10",
        null,
        "pointer"
      ]
    ],
    [
      "004c9a84",
      "PARAM",
      [
        "storage",
        "00c66798",
        "_ZTIN5Botan4Pipe22Invalid_Message_NumberE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004c9a80",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004c9a84",
      "READ",
      [
        "storage",
        "00c9af10",
        null,
        "pointer"
      ]
    ],
    [
      "004c9a84",
      "PARAM",
      [
        "storage",
        "00c66b98",
        "_ZTIN5Botan4Pipe22Invalid_Message_NumberE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c9a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9940.md#insn-004c9a4c) · [`004c9a8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9940.md#insn-004c9a8c) · [`004c99e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9940.md#insn-004c99e4)
- 新版 `004c9a8c`（命令位置の公開資料なし） · `004c9acc`（命令位置の公開資料なし） · `004c9a24`（命令位置の公開資料なし）

~~~diff
- 004c9a4c ["INT_ADD", "register:40f0:8", ["const:4c9a4c:8", "const:4:8"]]
- 004c9a4c ["CALL", null, ["callee:00c57f10:8"]]
+ 004c9a8c ["INT_ADD", "register:40f0:8", ["const:4c9a8c:8", "const:4:8"]]
+ 004c9a8c ["CALL", null, ["callee:00c57f10:8"]]
- 004c9a4c bytes 31381e94
+ 004c9a8c bytes 21391e94
- 004c9a8c ["INT_ADD", "register:40f0:8", ["const:4c9a8c:8", "const:4:8"]]
- 004c9a8c ["CALL", null, ["callee:00c57ee0:8"]]
+ 004c9acc ["INT_ADD", "register:40f0:8", ["const:4c9acc:8", "const:4:8"]]
+ 004c9acc ["CALL", null, ["callee:00c57ee0:8"]]
- 004c9a8c bytes 15381e94
+ 004c9acc bytes 05391e94
- 004c99e4 ["INT_ADD", "register:40f0:8", ["const:4c99e4:8", "const:4:8"]]
- 004c99e4 ["CALL", null, ["callee:00c58ff0:8"]]
+ 004c9a24 ["INT_ADD", "register:40f0:8", ["const:4c9a24:8", "const:4:8"]]
+ 004c9a24 ["CALL", null, ["callee:00c58ff0:8"]]
- 004c99e4 bytes 833c1e94
+ 004c9a24 bytes 733d1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc859547a8aa6ec926b05f489ea5a9ad"></a>

### [`004c9b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9b34.md) → [`004c9b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c9/004c9b74.md) _ZN5Botan4Pipe18read_all_as_stringEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 12件 [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00c37ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ba4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.47% / 新版 97.47%

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
      "definition_site": "004c9c44",
      "incomplete_value": true,
      "site": "004c9c44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c9ca0",
      "incomplete_value": true,
      "site": "004c9ca8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c9ca4",
      "incomplete_value": true,
      "site": "004c9ca8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004c9c64",
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
                "const:9f0:8"
              ]
            ]
          ]
        ]
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
      "004c9c30",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004c9ca0",
      "READ",
      [
        "storage",
        "00c9a9e8",
        null,
        "pointer"
      ]
    ],
    [
      "004c9ca0",
      "PARAM",
      [
        "storage",
        "00c96298",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004c9c30",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004c9ca0",
      "READ",
      [
        "storage",
        "00c9ade8",
        null,
        "pointer"
      ]
    ],
    [
      "004c9ca0",
      "PARAM",
      [
        "storage",
        "00c96698",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c9bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9b34.md#insn-004c9bc4) · [`004c9c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9b34.md#insn-004c9c04) · [`004c9c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9b34.md#insn-004c9c68)
- 新版 `004c9c04`（命令位置の公開資料なし） · `004c9c44`（命令位置の公開資料なし） · `004c9ca8`（命令位置の公開資料なし）

~~~diff
- 004c9bc4 ["INT_ADD", "register:40f0:8", ["const:4c9bc4:8", "const:4:8"]]
- 004c9bc4 ["CALL", null, ["callee:00c590c0:8"]]
+ 004c9c04 ["INT_ADD", "register:40f0:8", ["const:4c9c04:8", "const:4:8"]]
+ 004c9c04 ["CALL", null, ["callee:00c590c0:8"]]
- 004c9bc4 bytes 3f3c1e94
+ 004c9c04 bytes 2f3d1e94
- 004c9c04 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c9c04 ["INT_ADD", "register:40f0:8", ["const:4c9c04:8", "const:4:8"]]
- 004c9c04 ["CALLIND", null, ["register:0:8"]]
+ 004c9c44 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c9c44 ["INT_ADD", "register:40f0:8", ["const:4c9c44:8", "const:4:8"]]
+ 004c9c44 ["CALLIND", null, ["register:0:8"]]
- 004c9c04 bytes 20013fd6
+ 004c9c44 bytes 20013fd6
- 004c9c68 ["INT_ADD", "register:40f0:8", ["const:4c9c68:8", "const:4:8"]]
- 004c9c68 ["CALL", null, ["callee:00c57f10:8"]]
+ 004c9ca8 ["INT_ADD", "register:40f0:8", ["const:4c9ca8:8", "const:4:8"]]
+ 004c9ca8 ["CALL", null, ["callee:00c57f10:8"]]
- 004c9c68 bytes aa371e94
+ 004c9ca8 bytes 9a381e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67a38751fa410deca3aa539c0db40d7d"></a>

### [`004c9cbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9cbc.md) → [`004c9cfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c9/004c9cfc.md) _ZNK5Botan4Pipe4peekEPhmmm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58ce0.md) · 呼出先 6件 [`004c96cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c96cc.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`00c590e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c590e0.md) · 呼出先 6件 [`004c970c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c9/004c970c.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
      "definition_site": "004c9e18",
      "incomplete_value": true,
      "site": "004c9e20",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c9e14",
      "incomplete_value": false,
      "site": "004c9e20",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004c9dd4",
      "incomplete_value": false,
      "site": "004c9de0",
      "value": [
        "leaf",
        "const:535828:8"
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
      "004c9e14",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004c9e18",
      "READ",
      [
        "storage",
        "00c9ab10",
        null,
        "pointer"
      ]
    ],
    [
      "004c9e18",
      "PARAM",
      [
        "storage",
        "00c66798",
        "_ZTIN5Botan4Pipe22Invalid_Message_NumberE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004c9e14",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004c9e18",
      "READ",
      [
        "storage",
        "00c9af10",
        null,
        "pointer"
      ]
    ],
    [
      "004c9e18",
      "PARAM",
      [
        "storage",
        "00c66b98",
        "_ZTIN5Botan4Pipe22Invalid_Message_NumberE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c9de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9cbc.md#insn-004c9de0) · [`004c9da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9cbc.md#insn-004c9da4) · [`004c9db4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9cbc.md#insn-004c9db4)
- 新版 `004c9e20`（命令位置の公開資料なし） · `004c9de4`（命令位置の公開資料なし） · `004c9df4`（命令位置の公開資料なし）

~~~diff
- 004c9de0 ["INT_ADD", "register:40f0:8", ["const:4c9de0:8", "const:4:8"]]
- 004c9de0 ["CALL", null, ["callee:00c57f10:8"]]
+ 004c9e20 ["INT_ADD", "register:40f0:8", ["const:4c9e20:8", "const:4:8"]]
+ 004c9e20 ["CALL", null, ["callee:00c57f10:8"]]
- 004c9de0 bytes 4c371e94
+ 004c9e20 bytes 3c381e94
- 004c9da4 ["INT_ADD", "register:40f0:8", ["const:4c9da4:8", "const:4:8"]]
- 004c9da4 ["CALL", null, ["callee:00c57ef0:8"]]
+ 004c9de4 ["INT_ADD", "register:40f0:8", ["const:4c9de4:8", "const:4:8"]]
+ 004c9de4 ["CALL", null, ["callee:00c57ef0:8"]]
- 004c9da4 bytes 53371e94
+ 004c9de4 bytes 43381e94
- 004c9db4 ["INT_ADD", "register:40f0:8", ["const:4c9db4:8", "const:4:8"]]
- 004c9db4 ["CALL", null, ["callee:004c970c:8"]]
+ 004c9df4 ["INT_ADD", "register:40f0:8", ["const:4c9df4:8", "const:4:8"]]
+ 004c9df4 ["CALL", null, ["callee:004c970c:8"]]
- 004c9db4 bytes 46feff97
+ 004c9df4 bytes 46feff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d432b16bba7e934c6e3a5bd538271ae"></a>

### [`004c9e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9e40.md) → [`004c9e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c9/004c9e80.md) _ZNK5Botan4Pipe14get_bytes_readEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58250.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58650.md)

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
      "definition_site": "004c9ee0",
      "incomplete_value": false,
      "site": "004c9f00",
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
            "const:2fd:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c9ee8",
      "incomplete_value": false,
      "site": "004c9f00",
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
            "const:3a0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c9ef0",
      "incomplete_value": false,
      "site": "004c9f00",
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
            "const:bc1:8"
          ]
        ]
      ]
    },
    "old": {
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
      "004c9ee0",
      "PARAM",
      [
        "storage",
        "002b72bd",
        null,
        "string"
      ]
    ],
    [
      "004c9ee8",
      "PARAM",
      [
        "storage",
        "002bb360",
        null,
        "string"
      ]
    ],
    [
      "004c9ef0",
      "PARAM",
      [
        "storage",
        "002a9af4",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004c9ee0",
      "PARAM",
      [
        "storage",
        "002b72fd",
        null,
        "string"
      ]
    ],
    [
      "004c9ee8",
      "PARAM",
      [
        "storage",
        "002bb3a0",
        null,
        "string"
      ]
    ],
    [
      "004c9ef0",
      "PARAM",
      [
        "storage",
        "002a9bc1",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c9ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9e40.md#insn-004c9ec0) · [`004c9ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9e40.md#insn-004c9ea0) · [`004c9ea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9e40.md#insn-004c9ea8)
- 新版 `004c9f00`（命令位置の公開資料なし） · `004c9ee0`（命令位置の公開資料なし） · `004c9ee8`（命令位置の公開資料なし）

~~~diff
- 004c9ec0 ["INT_ADD", "register:40f0:8", ["const:4c9ec0:8", "const:4:8"]]
- 004c9ec0 ["CALL", null, ["callee:00c58650:8"]]
+ 004c9f00 ["INT_ADD", "register:40f0:8", ["const:4c9f00:8", "const:4:8"]]
+ 004c9f00 ["CALL", null, ["callee:00c58650:8"]]
- 004c9ec0 bytes e4381e94
+ 004c9f00 bytes d4391e94
- 004c9ea0 ["COPY", "tmp:0:8", ["const:2bd:8"]]
- 004c9ea0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004c9ea0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004c9ea0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004c9ee0 ["COPY", "tmp:0:8", ["const:2fd:8"]]
+ 004c9ee0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004c9ee0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004c9ee0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004c9ea0 bytes 00f40a91
+ 004c9ee0 bytes 00f40b91
- 004c9ea8 ["COPY", "tmp:0:8", ["const:360:8"]]
- 004c9ea8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004c9ea8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004c9ea8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004c9ee8 ["COPY", "tmp:0:8", ["const:3a0:8"]]
+ 004c9ee8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004c9ee8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004c9ee8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004c9ea8 bytes 21800d91
+ 004c9ee8 bytes 21800e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7ee355ffc9ca428a824c9c2e53b6fa8"></a>

### [`004c9ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9ec4.md) → [`004c9f04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c9/004c9f04.md) _ZNK5Botan4Pipe14get_bytes_readEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58250.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58650.md)

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
      "definition_site": "004c9f64",
      "incomplete_value": false,
      "site": "004c9f84",
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
            "const:2fd:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c9f6c",
      "incomplete_value": false,
      "site": "004c9f84",
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
            "const:3a0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c9f74",
      "incomplete_value": false,
      "site": "004c9f84",
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
            "const:bc1:8"
          ]
        ]
      ]
    },
    "old": {
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
      "004c9f64",
      "PARAM",
      [
        "storage",
        "002b72bd",
        null,
        "string"
      ]
    ],
    [
      "004c9f6c",
      "PARAM",
      [
        "storage",
        "002bb360",
        null,
        "string"
      ]
    ],
    [
      "004c9f74",
      "PARAM",
      [
        "storage",
        "002a9af4",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004c9f64",
      "PARAM",
      [
        "storage",
        "002b72fd",
        null,
        "string"
      ]
    ],
    [
      "004c9f6c",
      "PARAM",
      [
        "storage",
        "002bb3a0",
        null,
        "string"
      ]
    ],
    [
      "004c9f74",
      "PARAM",
      [
        "storage",
        "002a9bc1",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c9f44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9ec4.md#insn-004c9f44) · [`004c9f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9ec4.md#insn-004c9f24) · [`004c9f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9ec4.md#insn-004c9f2c)
- 新版 `004c9f84`（命令位置の公開資料なし） · `004c9f64`（命令位置の公開資料なし） · `004c9f6c`（命令位置の公開資料なし）

~~~diff
- 004c9f44 ["INT_ADD", "register:40f0:8", ["const:4c9f44:8", "const:4:8"]]
- 004c9f44 ["CALL", null, ["callee:00c58650:8"]]
+ 004c9f84 ["INT_ADD", "register:40f0:8", ["const:4c9f84:8", "const:4:8"]]
+ 004c9f84 ["CALL", null, ["callee:00c58650:8"]]
- 004c9f44 bytes c3381e94
+ 004c9f84 bytes b3391e94
- 004c9f24 ["COPY", "tmp:0:8", ["const:2bd:8"]]
- 004c9f24 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004c9f24 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004c9f24 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004c9f64 ["COPY", "tmp:0:8", ["const:2fd:8"]]
+ 004c9f64 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004c9f64 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004c9f64 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004c9f24 bytes 00f40a91
+ 004c9f64 bytes 00f40b91
- 004c9f2c ["COPY", "tmp:0:8", ["const:360:8"]]
- 004c9f2c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004c9f2c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004c9f2c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004c9f6c ["COPY", "tmp:0:8", ["const:3a0:8"]]
+ 004c9f6c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004c9f6c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004c9f6c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004c9f2c bytes 21800d91
+ 004c9f6c bytes 21800e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07302739d22df1108172e064952e00f7"></a>

### [`004c9fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9fa4.md) → [`004c9fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c9/004c9fe4.md) _ZN5Botan11SecureQueueC1Ev

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58cb0.md) · 呼出先 8件 [`00543c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543c1c.md) [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 1件 [`00c590b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c590b0.md) · 呼出先 8件 [`00543c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543c5c.md) [`00c37ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.06% / 新版 93.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ca014",
      "incomplete_value": true,
      "site": "004ca01c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ca048",
      "incomplete_value": true,
      "site": "004ca050",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ca058",
      "incomplete_value": true,
      "site": "004ca058",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "004ca004",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "004ca01c",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004ca03c",
      "READ",
      [
        "storage",
        "00c9ab08",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ca004",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "004ca01c",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004ca03c",
      "READ",
      [
        "storage",
        "00c9af08",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ca0bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9fa4.md#insn-004ca0bc) · [`004c9fc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9fa4.md#insn-004c9fc4) · [`004c9ff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9fa4.md#insn-004c9ff4)
- 新版 `004ca0fc`（命令位置の公開資料なし） · `004ca004`（命令位置の公開資料なし） · `004ca034`（命令位置の公開資料なし）

~~~diff
- 004ca0bc ["INT_ADD", "register:40f0:8", ["const:4ca0bc:8", "const:4:8"]]
- 004ca0bc ["CALL", null, ["callee:00c57f10:8"]]
+ 004ca0fc ["INT_ADD", "register:40f0:8", ["const:4ca0fc:8", "const:4:8"]]
+ 004ca0fc ["CALL", null, ["callee:00c57f10:8"]]
- 004ca0bc bytes 95361e94
+ 004ca0fc bytes 85371e94
- 004c9fc4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a70:8"]]
- 004c9fc4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ca004 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 004ca004 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c9fc4 bytes 083945f9
+ 004ca004 bytes 083947f9
- 004c9ff4 ["INT_ADD", "register:40f0:8", ["const:4c9ff4:8", "const:4:8"]]
- 004c9ff4 ["CALL", null, ["callee:00543c5c:8"]]
+ 004ca034 ["INT_ADD", "register:40f0:8", ["const:4ca034:8", "const:4:8"]]
+ 004ca034 ["CALL", null, ["callee:00543c5c:8"]]
- 004c9ff4 bytes 0ae70194
+ 004ca034 bytes 0ae70194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce81e5bfcb334129e9746185337631ce"></a>

### [`004ca124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004ca124.md) → [`004ca164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ca/004ca164.md) _ZN5Botan11SecureQueueC2ERKS0_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`00543c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543c1c.md) [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00543c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543c5c.md) [`00c37ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.65% / 新版 97.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ca1a4",
      "incomplete_value": true,
      "site": "004ca1ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ca1d4",
      "incomplete_value": true,
      "site": "004ca1dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ca1e4",
      "incomplete_value": true,
      "site": "004ca1e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "004ca198",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "004ca1ac",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004ca1c8",
      "READ",
      [
        "storage",
        "00c9ab08",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ca198",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "004ca1ac",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004ca1c8",
      "READ",
      [
        "storage",
        "00c9af08",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ca270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004ca124.md#insn-004ca270) · [`004ca158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004ca124.md#insn-004ca158) · [`004ca180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004ca124.md#insn-004ca180)
- 新版 `004ca2b0`（命令位置の公開資料なし） · `004ca198`（命令位置の公開資料なし） · `004ca1c0`（命令位置の公開資料なし）

~~~diff
- 004ca270 ["INT_ADD", "register:40f0:8", ["const:4ca270:8", "const:4:8"]]
- 004ca270 ["CALL", null, ["callee:00c57f10:8"]]
+ 004ca2b0 ["INT_ADD", "register:40f0:8", ["const:4ca2b0:8", "const:4:8"]]
+ 004ca2b0 ["CALL", null, ["callee:00c57f10:8"]]
- 004ca270 bytes 28361e94
+ 004ca2b0 bytes 18371e94
- 004ca158 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a70:8"]]
- 004ca158 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ca198 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 004ca198 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004ca158 bytes 083945f9
+ 004ca198 bytes 083947f9
- 004ca180 ["INT_ADD", "register:40f0:8", ["const:4ca180:8", "const:4:8"]]
- 004ca180 ["CALL", null, ["callee:00543c5c:8"]]
+ 004ca1c0 ["INT_ADD", "register:40f0:8", ["const:4ca1c0:8", "const:4:8"]]
+ 004ca1c0 ["CALL", null, ["callee:00543c5c:8"]]
- 004ca180 bytes a7e60194
+ 004ca1c0 bytes a7e60194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05e6ad97b7855aad327b3e12d4c3d522"></a>

### [`004ca2dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004ca2dc.md) → [`004ca31c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ca/004ca31c.md) _ZN5Botan11SecureQueue5writeEPKhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58cf0.md) · 呼出先 8件 [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`00c590f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c590f0.md) · 呼出先 8件 [`00c37ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.43% / 新版 96.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ca494",
      "incomplete_value": true,
      "site": "004ca49c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ca498",
      "incomplete_value": true,
      "site": "004ca49c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 7,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ca4cc",
      "incomplete_value": true,
      "site": "004ca4d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004ca48c",
      "incomplete_value": true,
      "site": "004ca494",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004ca494",
      "READ",
      [
        "storage",
        "00c9a9e8",
        null,
        "pointer"
      ]
    ],
    [
      "004ca494",
      "PARAM",
      [
        "storage",
        "00c96298",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "004ca498",
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
      "004ca494",
      "READ",
      [
        "storage",
        "00c9ade8",
        null,
        "pointer"
      ]
    ],
    [
      "004ca494",
      "PARAM",
      [
        "storage",
        "00c96698",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "004ca498",
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

- 旧版 [`004ca454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004ca2dc.md#insn-004ca454) · [`004ca45c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004ca2dc.md#insn-004ca45c) · [`004ca494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004ca2dc.md#insn-004ca494)
- 新版 `004ca494`（命令位置の公開資料なし） · `004ca49c`（命令位置の公開資料なし） · `004ca4d4`（命令位置の公開資料なし）

~~~diff
- 004ca454 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:9e8:8"]]
- 004ca454 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ca494 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:de8:8"]]
+ 004ca494 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004ca454 bytes 21f444f9
+ 004ca494 bytes 21f446f9
- 004ca45c ["INT_ADD", "register:40f0:8", ["const:4ca45c:8", "const:4:8"]]
- 004ca45c ["CALL", null, ["callee:00c57f10:8"]]
+ 004ca49c ["INT_ADD", "register:40f0:8", ["const:4ca49c:8", "const:4:8"]]
+ 004ca49c ["CALL", null, ["callee:00c57f10:8"]]
- 004ca45c bytes ad351e94
+ 004ca49c bytes 9d361e94
- 004ca494 ["INT_ADD", "register:40f0:8", ["const:4ca494:8", "const:4:8"]]
- 004ca494 ["CALL", null, ["callee:00c57f10:8"]]
+ 004ca4d4 ["INT_ADD", "register:40f0:8", ["const:4ca4d4:8", "const:4:8"]]
+ 004ca4d4 ["CALL", null, ["callee:00c57f10:8"]]
- 004ca494 bytes 9f351e94
+ 004ca4d4 bytes 8f361e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-034b5da4c178bc6a5e140a286d37ec45"></a>

### [`004ca4cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004ca4cc.md) → [`004ca50c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ca/004ca50c.md) _ZN5Botan11SecureQueue7destroyEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)

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
      "definition_site": "004ca56c",
      "incomplete_value": true,
      "site": "004ca56c",
      "value": [
        "LOAD",
        "8",
        [
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
      "004ca55c",
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
      "004ca55c",
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

- 旧版 [`004ca52c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004ca4cc.md#insn-004ca52c) · [`004ca4f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004ca4cc.md#insn-004ca4f8) · [`004ca51c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004ca4cc.md#insn-004ca51c)
- 新版 `004ca56c`（命令位置の公開資料なし） · `004ca538`（命令位置の公開資料なし） · `004ca55c`（命令位置の公開資料なし）

~~~diff
- 004ca52c ["COPY", "register:0:8", ["register:4048:8"]]
- 004ca52c ["INT_ADD", "register:40f0:8", ["const:4ca52c:8", "const:4:8"]]
- 004ca52c ["CALLIND", null, ["register:0:8"]]
+ 004ca56c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004ca56c ["INT_ADD", "register:40f0:8", ["const:4ca56c:8", "const:4:8"]]
+ 004ca56c ["CALLIND", null, ["register:0:8"]]
- 004ca52c bytes 20013fd6
+ 004ca56c bytes 20013fd6
- 004ca4f8 ["INT_ADD", "register:40f0:8", ["const:4ca4f8:8", "const:4:8"]]
- 004ca4f8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 004ca538 ["INT_ADD", "register:40f0:8", ["const:4ca538:8", "const:4:8"]]
+ 004ca538 ["CALL", null, ["callee:00c57eb0:8"]]
- 004ca4f8 bytes 6e351e94
+ 004ca538 bytes 5e361e94
- 004ca51c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:338:8"]]
- 004ca51c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ca55c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:738:8"]]
+ 004ca55c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004ca51c bytes c99e41f9
+ 004ca55c bytes c99e43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0c79a3d27ea90c614e508963e1ddac7"></a>

### [`004ca558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004ca558.md) → [`004ca598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ca/004ca598.md) _ZN5Botan11SecureQueueaSERKS0_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 11件 [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00c37ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.74% / 新版 95.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004ca61c",
      "incomplete_value": true,
      "site": "004ca61c",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ca700",
      "incomplete_value": true,
      "site": "004ca708",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ca704",
      "incomplete_value": true,
      "site": "004ca708",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004ca6c4",
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
                "const:9f0:8"
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
      "004ca60c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004ca700",
      "READ",
      [
        "storage",
        "00c9a9e8",
        null,
        "pointer"
      ]
    ],
    [
      "004ca700",
      "PARAM",
      [
        "storage",
        "00c96298",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004ca60c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004ca700",
      "READ",
      [
        "storage",
        "00c9ade8",
        null,
        "pointer"
      ]
    ],
    [
      "004ca700",
      "PARAM",
      [
        "storage",
        "00c96698",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ca5dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004ca558.md#insn-004ca5dc) · [`004ca6c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004ca558.md#insn-004ca6c8) · [`004ca5a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004ca558.md#insn-004ca5a8)
- 新版 `004ca61c`（命令位置の公開資料なし） · `004ca708`（命令位置の公開資料なし） · `004ca5e8`（命令位置の公開資料なし）

~~~diff
- 004ca5dc ["COPY", "register:0:8", ["register:4048:8"]]
- 004ca5dc ["INT_ADD", "register:40f0:8", ["const:4ca5dc:8", "const:4:8"]]
- 004ca5dc ["CALLIND", null, ["register:0:8"]]
+ 004ca61c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004ca61c ["INT_ADD", "register:40f0:8", ["const:4ca61c:8", "const:4:8"]]
+ 004ca61c ["CALLIND", null, ["register:0:8"]]
- 004ca5dc bytes 20013fd6
+ 004ca61c bytes 20013fd6
- 004ca6c8 ["INT_ADD", "register:40f0:8", ["const:4ca6c8:8", "const:4:8"]]
- 004ca6c8 ["CALL", null, ["callee:00c57f10:8"]]
+ 004ca708 ["INT_ADD", "register:40f0:8", ["const:4ca708:8", "const:4:8"]]
+ 004ca708 ["CALL", null, ["callee:00c57f10:8"]]
- 004ca6c8 bytes 12351e94
+ 004ca708 bytes 02361e94
- 004ca5a8 ["INT_ADD", "register:40f0:8", ["const:4ca5a8:8", "const:4:8"]]
- 004ca5a8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 004ca5e8 ["INT_ADD", "register:40f0:8", ["const:4ca5e8:8", "const:4:8"]]
+ 004ca5e8 ["CALL", null, ["callee:00c57eb0:8"]]
- 004ca5a8 bytes 42351e94
+ 004ca5e8 bytes 32361e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20213eb3ec342509d3a11dc3a56f6ac1"></a>

### [`004ca7b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004ca7b4.md) → [`004ca7f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ca/004ca7f4.md) _ZN5Botan13Threaded_ForkC2EPNS_6FilterES2_S2_S2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00543c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543c1c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58d00.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00543c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543c5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59100.md)

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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ca87c",
      "incomplete_value": true,
      "site": "004ca884",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
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
      "004ca820",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "004ca844",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004ca86c",
      "READ",
      [
        "storage",
        "00c9ab20",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ca820",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "004ca844",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004ca86c",
      "READ",
      [
        "storage",
        "00c9af20",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ca7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004ca7b4.md#insn-004ca7e0) · [`004ca800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004ca7b4.md#insn-004ca800) · [`004ca81c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004ca7b4.md#insn-004ca81c)
- 新版 `004ca820`（命令位置の公開資料なし） · `004ca85c`（命令位置の公開資料なし）

~~~diff
- 004ca7e0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a70:8"]]
- 004ca7e0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ca820 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e70:8"]]
+ 004ca820 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004ca7e0 bytes 293945f9
+ 004ca820 bytes 293947f9
- 004ca800 ["COPY", "register:40c0:8", ["register:4000:8"]]
- 004ca800 bytes f80300aa
- 004ca81c ["INT_ADD", "register:40f0:8", ["const:4ca81c:8", "const:4:8"]]
- 004ca81c ["CALL", null, ["callee:00543c5c:8"]]
+ 004ca85c ["INT_ADD", "register:40f0:8", ["const:4ca85c:8", "const:4:8"]]
+ 004ca85c ["CALL", null, ["callee:00543c5c:8"]]
- 004ca81c bytes 00e50194
+ 004ca85c bytes 00e50194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-edaa09c5fd6b369b3776fd5c9cc77ff8"></a>

### [`004cac40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004cac40.md) → [`004cac80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ca/004cac80.md) _ZN5Botan13Threaded_ForkC2EPPNS_6FilterEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00543c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543c1c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c58d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58d00.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00543c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543c5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c59100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59100.md)

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
      "definition_site": "004cacac",
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004cace8",
      "incomplete_value": true,
      "site": "004cacf0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
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
      "004cac9c",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "004cacb0",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004cacd8",
      "READ",
      [
        "storage",
        "00c9ab20",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004cac9c",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "004cacb0",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004cacd8",
      "READ",
      [
        "storage",
        "00c9af20",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cac5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004cac40.md#insn-004cac5c) · [`004cac88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004cac40.md#insn-004cac88) · [`004cac98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004cac40.md#insn-004cac98)
- 新版 `004cac9c`（命令位置の公開資料なし） · `004cacc8`（命令位置の公開資料なし） · `004cacd8`（命令位置の公開資料なし）

~~~diff
- 004cac5c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a70:8"]]
- 004cac5c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004cac9c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 004cac9c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004cac5c bytes 083945f9
+ 004cac9c bytes 083947f9
- 004cac88 ["INT_ADD", "register:40f0:8", ["const:4cac88:8", "const:4:8"]]
- 004cac88 ["CALL", null, ["callee:00543c5c:8"]]
+ 004cacc8 ["INT_ADD", "register:40f0:8", ["const:4cacc8:8", "const:4:8"]]
+ 004cacc8 ["CALL", null, ["callee:00543c5c:8"]]
- 004cac88 bytes e5e30194
+ 004cacc8 bytes e5e30194
- 004cac98 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:b20:8"]]
- 004cac98 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004cacd8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f20:8"]]
+ 004cacd8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004cac98 bytes 299145f9
+ 004cacd8 bytes 299147f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f4a55f590f08efa534d7d467ca3f4c4"></a>

### [`004caf38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004caf38.md) → [`004caf78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ca/004caf78.md) _ZNK5Botan13Threaded_Fork4nameEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "004caf94",
      "incomplete_value": true,
      "site": "004caf94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:755:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004caf98",
      "incomplete_value": true,
      "site": "004caf98",
      "value": [
        "LOAD",
        "8",
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
      "004caf84",
      "READ",
      [
        "storage",
        "002ac715",
        null,
        "string"
      ]
    ],
    [
      "004caf8c",
      "READ",
      [
        "storage",
        "002ac71a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004caf84",
      "READ",
      [
        "storage",
        "002ac755",
        null,
        "string"
      ]
    ],
    [
      "004caf8c",
      "READ",
      [
        "storage",
        "002ac75a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004caf40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004caf38.md#insn-004caf40)
- 新版 `004caf80`（命令位置の公開資料なし）

~~~diff
- 004caf40 ["COPY", "tmp:0:8", ["const:715:8"]]
- 004caf40 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004caf40 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004caf40 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 004caf80 ["COPY", "tmp:0:8", ["const:755:8"]]
+ 004caf80 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 004caf80 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 004caf80 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004caf40 bytes 4a551c91
+ 004caf80 bytes 4a551d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c048b89d14ebc96bdccacce86cd6b63"></a>

### [`004cb1c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cb1c4.md) → [`004cb204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cb/004cb204.md) FUN_004cb204

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004ca930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004ca930.md) · 呼出先 6件 [`00544984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544984.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d00.md) [`00c57d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d10.md)
- 新版 呼出元 1件 [`004ca970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ca/004ca970.md) · 呼出先 6件 [`005449c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00544/005449c4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58100.md) [`00c58110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58110.md)

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
      "definition_site": "004cb264",
      "incomplete_value": false,
      "site": "004cb270",
      "value": [
        "leaf",
        "const:5449c4:8"
      ]
    },
    "old": {
      "definition_site": "004cb224",
      "incomplete_value": false,
      "site": "004cb230",
      "value": [
        "leaf",
        "const:544984:8"
      ]
    },
    "ordinal": 3,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004cb2b0",
      "incomplete_value": false,
      "site": "004cb2b4",
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
    "old": {
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
      "004cb264",
      "PARAM",
      [
        "storage",
        "00544984",
        null,
        null
      ]
    ],
    [
      "004cb2b0",
      "PARAM",
      [
        "storage",
        "002a3e5a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004cb264",
      "PARAM",
      [
        "storage",
        "005449c4",
        null,
        null
      ]
    ],
    [
      "004cb2b0",
      "PARAM",
      [
        "storage",
        "002a3f27",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cb1f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cb1c4.md#insn-004cb1f0) · [`004cb230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cb1c4.md#insn-004cb230) · [`004cb270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cb1c4.md#insn-004cb270)
- 新版 `004cb230`（命令位置の公開資料なし） · `004cb270`（命令位置の公開資料なし） · `004cb2b0`（命令位置の公開資料なし）

~~~diff
- 004cb1f0 ["INT_ADD", "register:40f0:8", ["const:4cb1f0:8", "const:4:8"]]
- 004cb1f0 ["CALL", null, ["callee:00c57e90:8"]]
+ 004cb230 ["INT_ADD", "register:40f0:8", ["const:4cb230:8", "const:4:8"]]
+ 004cb230 ["CALL", null, ["callee:00c57e90:8"]]
- 004cb1f0 bytes 28321e94
+ 004cb230 bytes 18331e94
- 004cb230 ["INT_ADD", "register:40f0:8", ["const:4cb230:8", "const:4:8"]]
- 004cb230 ["CALL", null, ["callee:00c58110:8"]]
+ 004cb270 ["INT_ADD", "register:40f0:8", ["const:4cb270:8", "const:4:8"]]
+ 004cb270 ["CALL", null, ["callee:00c58110:8"]]
- 004cb230 bytes b8321e94
+ 004cb270 bytes a8331e94
- 004cb270 ["COPY", "tmp:0:8", ["const:e5a:8"]]
- 004cb270 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004cb270 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004cb270 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004cb2b0 ["COPY", "tmp:0:8", ["const:f27:8"]]
+ 004cb2b0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004cb2b0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004cb2b0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004cb270 bytes 21683991
+ 004cb2b0 bytes 219c3c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8b96bd0503001d8094f5de46e5b44ea"></a>

### [`004cb6ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cb6ec.md) → [`004cb72c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cb/004cb72c.md) FUN_004cb72c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`004c128c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c128c.md) [`00530a2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530a2c.md) · 呼出先 6件 [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c58630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58630.md)
- 新版 呼出元 2件 [`004c12cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c1/004c12cc.md) [`00530a6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530a6c.md) · 呼出先 6件 [`00c37ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ba4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c58a30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58a30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.63% / 新版 92.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 1件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004cb758",
      "incomplete_value": true,
      "site": "004cb760",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004cb7c0",
      "incomplete_value": true,
      "site": "004cb7c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004cb7f0",
      "incomplete_value": true,
      "site": "004cb800",
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
      "004cb74c",
      "READ",
      [
        "storage",
        "00c9ab38",
        null,
        "pointer"
      ]
    ],
    [
      "004cb760",
      "DATA",
      [
        "storage",
        "00c668d8",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "004cb7ac",
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
      "004cb74c",
      "READ",
      [
        "storage",
        "00c9af38",
        null,
        "pointer"
      ]
    ],
    [
      "004cb760",
      "DATA",
      [
        "storage",
        "00c66cd8",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "004cb7ac",
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

- 旧版 [`004cb820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cb6ec.md#insn-004cb820) · [`004cb824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cb6ec.md#insn-004cb824) · [`004cb860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cb6ec.md#insn-004cb860)
- 新版 `004cb860`（命令位置の公開資料なし） · `004cb864`（命令位置の公開資料なし） · `004cb8a0`（命令位置の公開資料なし）

~~~diff
- 004cb820 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:9f0:8"]]
- 004cb820 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 004cb860 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:df0:8"]]
+ 004cb860 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 004cb820 bytes 42f844f9
+ 004cb860 bytes 42f846f9
- 004cb824 ["INT_ADD", "register:40f0:8", ["const:4cb824:8", "const:4:8"]]
- 004cb824 ["CALL", null, ["callee:00c57f10:8"]]
+ 004cb864 ["INT_ADD", "register:40f0:8", ["const:4cb864:8", "const:4:8"]]
+ 004cb864 ["CALL", null, ["callee:00c57f10:8"]]
- 004cb824 bytes bb301e94
+ 004cb864 bytes ab311e94
- 004cb860 ["INT_ADD", "register:40f0:8", ["const:4cb860:8", "const:4:8"]]
- 004cb860 ["CALL", null, ["callee:00c57f10:8"]]
+ 004cb8a0 ["INT_ADD", "register:40f0:8", ["const:4cb8a0:8", "const:4:8"]]
+ 004cb8a0 ["CALL", null, ["callee:00c57f10:8"]]
- 004cb860 bytes ac301e94
+ 004cb8a0 bytes 9c311e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07cbe698f0d4618239fad23159d7af08"></a>

### [`004cb8a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cb8a8.md) → [`004cb8e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cb/004cb8e8.md) FUN_004cb8e8

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`004c128c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c128c.md) [`00530bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530bd4.md) · 呼出先 6件 [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c58630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58630.md)
- 新版 呼出元 2件 [`004c12cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c1/004c12cc.md) [`00530c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530c14.md) · 呼出先 6件 [`00c37ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ba4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c58a30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58a30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.47% / 新版 92.47%

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
      "definition_site": "004cb914",
      "incomplete_value": true,
      "site": "004cb91c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cb8d4",
      "incomplete_value": true,
      "site": "004cb8dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004cb97c",
      "incomplete_value": true,
      "site": "004cb97c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004cb93c",
      "incomplete_value": true,
      "site": "004cb93c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004cb9ac",
      "incomplete_value": true,
      "site": "004cb9b8",
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
      "definition_site": "004cb96c",
      "incomplete_value": true,
      "site": "004cb978",
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
      "004cb908",
      "READ",
      [
        "storage",
        "00c9ab38",
        null,
        "pointer"
      ]
    ],
    [
      "004cb91c",
      "DATA",
      [
        "storage",
        "00c668d8",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "004cb968",
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
      "004cb908",
      "READ",
      [
        "storage",
        "00c9af38",
        null,
        "pointer"
      ]
    ],
    [
      "004cb91c",
      "DATA",
      [
        "storage",
        "00c66cd8",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "004cb968",
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

- 旧版 [`004cb9d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cb8a8.md#insn-004cb9d4) · [`004cb9d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cb8a8.md#insn-004cb9d8) · [`004cba14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cb8a8.md#insn-004cba14)
- 新版 `004cba14`（命令位置の公開資料なし） · `004cba18`（命令位置の公開資料なし） · `004cba54`（命令位置の公開資料なし）

~~~diff
- 004cb9d4 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:9f0:8"]]
- 004cb9d4 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 004cba14 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:df0:8"]]
+ 004cba14 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 004cb9d4 bytes 42f844f9
+ 004cba14 bytes 42f846f9
- 004cb9d8 ["INT_ADD", "register:40f0:8", ["const:4cb9d8:8", "const:4:8"]]
- 004cb9d8 ["CALL", null, ["callee:00c57f10:8"]]
+ 004cba18 ["INT_ADD", "register:40f0:8", ["const:4cba18:8", "const:4:8"]]
+ 004cba18 ["CALL", null, ["callee:00c57f10:8"]]
- 004cb9d8 bytes 4e301e94
+ 004cba18 bytes 3e311e94
- 004cba14 ["INT_ADD", "register:40f0:8", ["const:4cba14:8", "const:4:8"]]
- 004cba14 ["CALL", null, ["callee:00c57f10:8"]]
+ 004cba54 ["INT_ADD", "register:40f0:8", ["const:4cba54:8", "const:4:8"]]
+ 004cba54 ["CALL", null, ["callee:00c57f10:8"]]
- 004cba14 bytes 3f301e94
+ 004cba54 bytes 2f311e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e1baf05bf834f4cf77c165054f3516f"></a>

### [`004cba5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cba5c.md) → [`004cba9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cb/004cba9c.md) FUN_004cba9c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`004c128c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c128c.md) [`00530d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530d7c.md) · 呼出先 6件 [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c58630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58630.md)
- 新版 呼出元 2件 [`004c12cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c1/004c12cc.md) [`00530dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530dbc.md) · 呼出先 6件 [`00c37ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ba4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c58a30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58a30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.47% / 新版 92.47%

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
      "definition_site": "004cbac8",
      "incomplete_value": true,
      "site": "004cbad0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004cbb30",
      "incomplete_value": true,
      "site": "004cbb30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004cbb60",
      "incomplete_value": true,
      "site": "004cbb6c",
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
      "004cbabc",
      "READ",
      [
        "storage",
        "00c9ab38",
        null,
        "pointer"
      ]
    ],
    [
      "004cbad0",
      "DATA",
      [
        "storage",
        "00c668d8",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "004cbb1c",
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
      "004cbabc",
      "READ",
      [
        "storage",
        "00c9af38",
        null,
        "pointer"
      ]
    ],
    [
      "004cbad0",
      "DATA",
      [
        "storage",
        "00c66cd8",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "004cbb1c",
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

- 旧版 [`004cbb88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cba5c.md#insn-004cbb88) · [`004cbb8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cba5c.md#insn-004cbb8c) · [`004cbbc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cba5c.md#insn-004cbbc8)
- 新版 `004cbbc8`（命令位置の公開資料なし） · `004cbbcc`（命令位置の公開資料なし） · `004cbc08`（命令位置の公開資料なし）

~~~diff
- 004cbb88 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:9f0:8"]]
- 004cbb88 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 004cbbc8 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:df0:8"]]
+ 004cbbc8 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 004cbb88 bytes 42f844f9
+ 004cbbc8 bytes 42f846f9
- 004cbb8c ["INT_ADD", "register:40f0:8", ["const:4cbb8c:8", "const:4:8"]]
- 004cbb8c ["CALL", null, ["callee:00c57f10:8"]]
+ 004cbbcc ["INT_ADD", "register:40f0:8", ["const:4cbbcc:8", "const:4:8"]]
+ 004cbbcc ["CALL", null, ["callee:00c57f10:8"]]
- 004cbb8c bytes e12f1e94
+ 004cbbcc bytes d1301e94
- 004cbbc8 ["INT_ADD", "register:40f0:8", ["const:4cbbc8:8", "const:4:8"]]
- 004cbbc8 ["CALL", null, ["callee:00c57f10:8"]]
+ 004cbc08 ["INT_ADD", "register:40f0:8", ["const:4cbc08:8", "const:4:8"]]
+ 004cbc08 ["CALL", null, ["callee:00c57f10:8"]]
- 004cbbc8 bytes d22f1e94
+ 004cbc08 bytes c2301e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae419c0893cd16da8f249dcb0f27e434"></a>

### [`004cbc10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cbc10.md) → [`004cbc50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cb/004cbc50.md) FUN_004cbc50

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`004c128c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c128c.md) [`005303a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/005303a0.md) · 呼出先 6件 [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c58630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58630.md)
- 新版 呼出元 2件 [`004c12cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c1/004c12cc.md) [`005303e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/005303e0.md) · 呼出先 6件 [`00c37ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ba4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c58a30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58a30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.68% / 新版 90.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_value` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004cbc7c",
      "incomplete_value": true,
      "site": "004cbc84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004cbce8",
      "incomplete_value": true,
      "site": "004cbce8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 22,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004cbd54",
      "incomplete_value": true,
      "site": "004cbd58",
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
      "004cbc70",
      "READ",
      [
        "storage",
        "00c9ab38",
        null,
        "pointer"
      ]
    ],
    [
      "004cbc84",
      "DATA",
      [
        "storage",
        "00c668d8",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "004cbcd4",
      "READ",
      [
        "storage",
        "00c9ab58",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004cbc70",
      "READ",
      [
        "storage",
        "00c9af38",
        null,
        "pointer"
      ]
    ],
    [
      "004cbc84",
      "DATA",
      [
        "storage",
        "00c66cd8",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "004cbcd4",
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

- 旧版 [`004cbce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cbc10.md#insn-004cbce8) · [`004cbd64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cbc10.md#insn-004cbd64) · [`004cbd68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cbc10.md#insn-004cbd68)
- 新版 `004cbd28`（命令位置の公開資料なし） · `004cbda4`（命令位置の公開資料なし） · `004cbda8`（命令位置の公開資料なし）

~~~diff
- 004cbce8 ["INT_ADD", "register:40f0:8", ["const:4cbce8:8", "const:4:8"]]
- 004cbce8 ["CALL", null, ["callee:00c58a30:8"]]
+ 004cbd28 ["INT_ADD", "register:40f0:8", ["const:4cbd28:8", "const:4:8"]]
+ 004cbd28 ["CALL", null, ["callee:00c58a30:8"]]
- 004cbce8 bytes 52321e94
+ 004cbd28 bytes 42331e94
- 004cbd64 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:9f0:8"]]
- 004cbd64 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 004cbda4 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:df0:8"]]
+ 004cbda4 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 004cbd64 bytes 42f844f9
+ 004cbda4 bytes 42f846f9
- 004cbd68 ["INT_ADD", "register:40f0:8", ["const:4cbd68:8", "const:4:8"]]
- 004cbd68 ["CALL", null, ["callee:00c57f10:8"]]
+ 004cbda8 ["INT_ADD", "register:40f0:8", ["const:4cbda8:8", "const:4:8"]]
+ 004cbda8 ["CALL", null, ["callee:00c57f10:8"]]
- 004cbd68 bytes 6a2f1e94
+ 004cbda8 bytes 5a301e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4496a2d9e14c3be6b3d177e0e1958057"></a>

### [`004cc1d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc1d4.md) → [`004cc214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cc/004cc214.md) _ZN5Botan16ieee1363_hash_idERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00441e54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441e54.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00441e94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441e94.md)

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
      "definition_site": "004cc30c",
      "incomplete_value": false,
      "site": "004cc314",
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
            "const:2e9:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004cc328",
      "incomplete_value": false,
      "site": "004cc330",
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
            "const:665:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004cc36c",
      "incomplete_value": false,
      "site": "004cc374",
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
            "const:421:8"
          ]
        ]
      ]
    },
    "old": {
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
      "004cc30c",
      "PARAM",
      [
        "storage",
        "002bb2a9",
        null,
        "string"
      ]
    ],
    [
      "004cc328",
      "PARAM",
      [
        "storage",
        "002ac625",
        null,
        "string"
      ]
    ],
    [
      "004cc36c",
      "PARAM",
      [
        "storage",
        "002ab3e1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004cc30c",
      "PARAM",
      [
        "storage",
        "002bb2e9",
        null,
        "string"
      ]
    ],
    [
      "004cc328",
      "PARAM",
      [
        "storage",
        "002ac665",
        null,
        "string"
      ]
    ],
    [
      "004cc36c",
      "PARAM",
      [
        "storage",
        "002ab421",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cc2d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc1d4.md#insn-004cc2d4) · [`004cc2f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc1d4.md#insn-004cc2f0) · [`004cc334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc1d4.md#insn-004cc334)
- 新版 `004cc314`（命令位置の公開資料なし） · `004cc330`（命令位置の公開資料なし） · `004cc374`（命令位置の公開資料なし）

~~~diff
- 004cc2d4 ["INT_ADD", "register:40f0:8", ["const:4cc2d4:8", "const:4:8"]]
- 004cc2d4 ["CALL", null, ["callee:00441e94:8"]]
+ 004cc314 ["INT_ADD", "register:40f0:8", ["const:4cc314:8", "const:4:8"]]
+ 004cc314 ["CALL", null, ["callee:00441e94:8"]]
- 004cc2d4 bytes e0d6fd97
+ 004cc314 bytes e0d6fd97
- 004cc2f0 ["INT_ADD", "register:40f0:8", ["const:4cc2f0:8", "const:4:8"]]
- 004cc2f0 ["CALL", null, ["callee:00441e94:8"]]
+ 004cc330 ["INT_ADD", "register:40f0:8", ["const:4cc330:8", "const:4:8"]]
+ 004cc330 ["CALL", null, ["callee:00441e94:8"]]
- 004cc2f0 bytes d9d6fd97
+ 004cc330 bytes d9d6fd97
- 004cc334 ["INT_ADD", "register:40f0:8", ["const:4cc334:8", "const:4:8"]]
- 004cc334 ["CALL", null, ["callee:00441e94:8"]]
+ 004cc374 ["INT_ADD", "register:40f0:8", ["const:4cc374:8", "const:4:8"]]
+ 004cc374 ["CALL", null, ["callee:00441e94:8"]]
- 004cc334 bytes c8d6fd97
+ 004cc374 bytes c8d6fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75642645da7617d93d7057aa8f077d86"></a>

### [`004cc360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc360.md) → [`004cc3a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cc/004cc3a0.md) _ZN5Botan10hex_decodeEPhPKcmRmb

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58d40.md) · 呼出先 11件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00441e54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441e54.md) [`0044fc7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044fc7c.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00c59140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59140.md) · 呼出先 11件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00441e94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441e94.md) [`0044fcbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044fcbc.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

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
      "definition_site": "004cc468",
      "incomplete_value": false,
      "site": "004cc47c",
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
            "const:81c:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004cc4d8",
      "incomplete_value": false,
      "site": "004cc4e0",
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
    "old": {
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004cc508",
      "incomplete_value": false,
      "site": "004cc510",
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
            "const:96d:8"
          ]
        ]
      ]
    },
    "old": {
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
      "004cc448",
      "DATA",
      [
        "storage",
        "002caf86",
        null,
        null
      ]
    ],
    [
      "004cc468",
      "PARAM",
      [
        "storage",
        "002ae7dc",
        null,
        null
      ]
    ],
    [
      "004cc488",
      "PARAM",
      [
        "storage",
        "002bc4d5",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004cc448",
      "DATA",
      [
        "storage",
        "002cafc6",
        null,
        null
      ]
    ],
    [
      "004cc468",
      "PARAM",
      [
        "storage",
        "002ae81c",
        null,
        null
      ]
    ],
    [
      "004cc488",
      "PARAM",
      [
        "storage",
        "002bc515",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cc43c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc360.md#insn-004cc43c) · [`004cc4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc360.md#insn-004cc4a0) · [`004cc4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc360.md#insn-004cc4d0)
- 新版 `004cc47c`（命令位置の公開資料なし） · `004cc4e0`（命令位置の公開資料なし） · `004cc510`（命令位置の公開資料なし）

~~~diff
- 004cc43c ["INT_ADD", "register:40f0:8", ["const:4cc43c:8", "const:4:8"]]
- 004cc43c ["CALL", null, ["callee:00441e94:8"]]
+ 004cc47c ["INT_ADD", "register:40f0:8", ["const:4cc47c:8", "const:4:8"]]
+ 004cc47c ["CALL", null, ["callee:00441e94:8"]]
- 004cc43c bytes 86d6fd97
+ 004cc47c bytes 86d6fd97
- 004cc4a0 ["INT_ADD", "register:40f0:8", ["const:4cc4a0:8", "const:4:8"]]
- 004cc4a0 ["CALL", null, ["callee:00441e94:8"]]
+ 004cc4e0 ["INT_ADD", "register:40f0:8", ["const:4cc4e0:8", "const:4:8"]]
+ 004cc4e0 ["CALL", null, ["callee:00441e94:8"]]
- 004cc4a0 bytes 6dd6fd97
+ 004cc4e0 bytes 6dd6fd97
- 004cc4d0 ["INT_ADD", "register:40f0:8", ["const:4cc4d0:8", "const:4:8"]]
- 004cc4d0 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004cc510 ["INT_ADD", "register:40f0:8", ["const:4cc510:8", "const:4:8"]]
+ 004cc510 ["CALL", null, ["callee:0043ddd8:8"]]
- 004cc4d0 bytes 32c6fd97
+ 004cc510 bytes 32c6fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be8edbee22488410f3cdac2af15ef38d"></a>

### [`004cc608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc608.md) → [`004cc648`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cc/004cc648.md) _ZN5Botan10hex_decodeEPhPKcmb

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c586e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c586e0.md) · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`00c58ae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58ae0.md) · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
      "definition_site": "004cc6c0",
      "incomplete_value": false,
      "site": "004cc6c8",
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
            "const:83:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004cc6fc",
      "incomplete_value": true,
      "site": "004cc708",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004cc6f8",
      "incomplete_value": false,
      "site": "004cc708",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004cc6b8",
      "incomplete_value": false,
      "site": "004cc6c8",
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
      "004cc6c0",
      "PARAM",
      [
        "storage",
        "002b6043",
        null,
        "string"
      ]
    ],
    [
      "004cc6f8",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004cc6fc",
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
      "004cc6c0",
      "PARAM",
      [
        "storage",
        "002b6083",
        null,
        "string"
      ]
    ],
    [
      "004cc6f8",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004cc6fc",
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

- 旧版 [`004cc688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc608.md#insn-004cc688) · [`004cc6c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc608.md#insn-004cc6c8) · [`004cc638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc608.md#insn-004cc638)
- 新版 `004cc6c8`（命令位置の公開資料なし） · `004cc708`（命令位置の公開資料なし） · `004cc678`（命令位置の公開資料なし）

~~~diff
- 004cc688 ["INT_ADD", "register:40f0:8", ["const:4cc688:8", "const:4:8"]]
- 004cc688 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004cc6c8 ["INT_ADD", "register:40f0:8", ["const:4cc6c8:8", "const:4:8"]]
+ 004cc6c8 ["CALL", null, ["callee:0043ddd8:8"]]
- 004cc688 bytes c4c5fd97
+ 004cc6c8 bytes c4c5fd97
- 004cc6c8 ["INT_ADD", "register:40f0:8", ["const:4cc6c8:8", "const:4:8"]]
- 004cc6c8 ["CALL", null, ["callee:00c57f10:8"]]
+ 004cc708 ["INT_ADD", "register:40f0:8", ["const:4cc708:8", "const:4:8"]]
+ 004cc708 ["CALL", null, ["callee:00c57f10:8"]]
- 004cc6c8 bytes 122d1e94
+ 004cc708 bytes 022e1e94
- 004cc638 ["INT_ADD", "register:40f0:8", ["const:4cc638:8", "const:4:8"]]
- 004cc638 ["CALL", null, ["callee:00c59140:8"]]
+ 004cc678 ["INT_ADD", "register:40f0:8", ["const:4cc678:8", "const:4:8"]]
+ 004cc678 ["CALL", null, ["callee:00c59140:8"]]
- 004cc638 bytes c2311e94
+ 004cc678 bytes b2321e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af3bb162a5ced396f9cb37078e5d43bf"></a>

### [`004cc96c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc96c.md) → [`004cc9ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cc/004cc9ac.md) _ZN5Botan4HMAC8add_dataEPKhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c58240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58240.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c58640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58640.md)

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
      "definition_site": "004cca60",
      "incomplete_value": true,
      "site": "004cca6c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004cca5c",
      "incomplete_value": false,
      "site": "004cca6c",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004cca1c",
      "incomplete_value": false,
      "site": "004cca2c",
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
      "004cca5c",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004cca60",
      "READ",
      [
        "storage",
        "00c9a910",
        null,
        "pointer"
      ]
    ],
    [
      "004cca60",
      "PARAM",
      [
        "storage",
        "00c69758",
        "_ZTIN5Botan11Key_Not_SetE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004cca5c",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004cca60",
      "READ",
      [
        "storage",
        "00c9ad10",
        null,
        "pointer"
      ]
    ],
    [
      "004cca60",
      "PARAM",
      [
        "storage",
        "00c69b58",
        "_ZTIN5Botan11Key_Not_SetE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cc9ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc96c.md#insn-004cc9ec) · [`004cca2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc96c.md#insn-004cca2c) · [`004cc9d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc96c.md#insn-004cc9d4)
- 新版 `004cca2c`（命令位置の公開資料なし） · `004cca6c`（命令位置の公開資料なし） · `004cca14`（命令位置の公開資料なし）

~~~diff
- 004cc9ec ["COPY", "register:0:8", ["register:4048:8"]]
- 004cc9ec ["INT_ADD", "register:40f0:8", ["const:4cc9ec:8", "const:4:8"]]
- 004cc9ec ["CALLIND", null, ["register:0:8"]]
+ 004cca2c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004cca2c ["INT_ADD", "register:40f0:8", ["const:4cca2c:8", "const:4:8"]]
+ 004cca2c ["CALLIND", null, ["register:0:8"]]
- 004cc9ec bytes 20013fd6
+ 004cca2c bytes 20013fd6
- 004cca2c ["INT_ADD", "register:40f0:8", ["const:4cca2c:8", "const:4:8"]]
- 004cca2c ["CALL", null, ["callee:00c57f10:8"]]
+ 004cca6c ["INT_ADD", "register:40f0:8", ["const:4cca6c:8", "const:4:8"]]
+ 004cca6c ["CALL", null, ["callee:00c57f10:8"]]
- 004cca2c bytes 392c1e94
+ 004cca6c bytes 292d1e94
- 004cc9d4 ["INT_ADD", "register:40f0:8", ["const:4cc9d4:8", "const:4:8"]]
- 004cc9d4 ["CALL", null, ["callee:00c57ef0:8"]]
+ 004cca14 ["INT_ADD", "register:40f0:8", ["const:4cca14:8", "const:4:8"]]
+ 004cca14 ["CALL", null, ["callee:00c57ef0:8"]]
- 004cc9d4 bytes 472c1e94
+ 004cca14 bytes 372d1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-920fcb5be1de9d1a0845218cf428876a"></a>

### [`004cca80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cca80.md) → [`004ccac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cc/004ccac0.md) _ZN5Botan4HMAC12final_resultEPh

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c58240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58240.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c58640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58640.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.70% / 新版 98.70%

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
      "definition_site": "004ccbe0",
      "incomplete_value": true,
      "site": "004ccbec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ccbdc",
      "incomplete_value": false,
      "site": "004ccbec",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004ccb9c",
      "incomplete_value": false,
      "site": "004ccbac",
      "value": [
        "leaf",
        "const:535828:8"
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
      "004ccbdc",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004ccbe0",
      "READ",
      [
        "storage",
        "00c9a910",
        null,
        "pointer"
      ]
    ],
    [
      "004ccbe0",
      "PARAM",
      [
        "storage",
        "00c69758",
        "_ZTIN5Botan11Key_Not_SetE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004ccbdc",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004ccbe0",
      "READ",
      [
        "storage",
        "00c9ad10",
        null,
        "pointer"
      ]
    ],
    [
      "004ccbe0",
      "PARAM",
      [
        "storage",
        "00c69b58",
        "_ZTIN5Botan11Key_Not_SetE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ccbac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cca80.md#insn-004ccbac) · [`004ccac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cca80.md#insn-004ccac0) · [`004ccad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cca80.md#insn-004ccad8)
- 新版 `004ccbec`（命令位置の公開資料なし） · `004ccb00`（命令位置の公開資料なし） · `004ccb18`（命令位置の公開資料なし）

~~~diff
- 004ccbac ["INT_ADD", "register:40f0:8", ["const:4ccbac:8", "const:4:8"]]
- 004ccbac ["CALL", null, ["callee:00c57f10:8"]]
+ 004ccbec ["INT_ADD", "register:40f0:8", ["const:4ccbec:8", "const:4:8"]]
+ 004ccbec ["CALL", null, ["callee:00c57f10:8"]]
- 004ccbac bytes d92b1e94
+ 004ccbec bytes c92c1e94
- 004ccac0 ["COPY", "register:0:8", ["register:4040:8"]]
- 004ccac0 ["INT_ADD", "register:40f0:8", ["const:4ccac0:8", "const:4:8"]]
- 004ccac0 ["CALLIND", null, ["register:0:8"]]
+ 004ccb00 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004ccb00 ["INT_ADD", "register:40f0:8", ["const:4ccb00:8", "const:4:8"]]
+ 004ccb00 ["CALLIND", null, ["register:0:8"]]
- 004ccac0 bytes 00013fd6
+ 004ccb00 bytes 00013fd6
- 004ccad8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004ccad8 ["INT_ADD", "register:40f0:8", ["const:4ccad8:8", "const:4:8"]]
- 004ccad8 ["CALLIND", null, ["register:0:8"]]
+ 004ccb18 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004ccb18 ["INT_ADD", "register:40f0:8", ["const:4ccb18:8", "const:4:8"]]
+ 004ccb18 ["CALLIND", null, ["register:0:8"]]
- 004ccad8 bytes 00013fd6
+ 004ccb18 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e96a3c05b399313d45b5294faa447322"></a>

### [`004cd184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd184.md) → [`004cd1c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cd/004cd1c4.md) _ZNK5Botan4HMAC4nameEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58d90.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 1件 [`00c59190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59190.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f60.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

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
      "definition_site": "004cd1fc",
      "incomplete_value": false,
      "site": "004cd208",
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
            "const:8eb:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 1,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004cd228",
      "incomplete_value": false,
      "site": "004cd230",
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
    "old": {
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
      "004cd1fc",
      "PARAM",
      [
        "storage",
        "002bd8ab",
        null,
        "string"
      ]
    ],
    [
      "004cd228",
      "PARAM",
      [
        "storage",
        "002ab265",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004cd1fc",
      "PARAM",
      [
        "storage",
        "002bd8eb",
        null,
        "string"
      ]
    ],
    [
      "004cd228",
      "PARAM",
      [
        "storage",
        "002ab332",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cd1c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd184.md#insn-004cd1c8) · [`004cd1f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd184.md#insn-004cd1f0) · [`004cd1b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd184.md#insn-004cd1b4)
- 新版 `004cd208`（命令位置の公開資料なし） · `004cd230`（命令位置の公開資料なし） · `004cd1f4`（命令位置の公開資料なし）

~~~diff
- 004cd1c8 ["INT_ADD", "register:40f0:8", ["const:4cd1c8:8", "const:4:8"]]
- 004cd1c8 ["CALL", null, ["callee:00c57f60:8"]]
+ 004cd208 ["INT_ADD", "register:40f0:8", ["const:4cd208:8", "const:4:8"]]
+ 004cd208 ["CALL", null, ["callee:00c57f60:8"]]
- 004cd1c8 bytes 662a1e94
+ 004cd208 bytes 562b1e94
- 004cd1f0 ["INT_ADD", "register:40f0:8", ["const:4cd1f0:8", "const:4:8"]]
- 004cd1f0 ["CALL", null, ["callee:00c57f70:8"]]
+ 004cd230 ["INT_ADD", "register:40f0:8", ["const:4cd230:8", "const:4:8"]]
+ 004cd230 ["CALL", null, ["callee:00c57f70:8"]]
- 004cd1f0 bytes 602a1e94
+ 004cd230 bytes 502b1e94
- 004cd1b4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004cd1b4 ["INT_ADD", "register:40f0:8", ["const:4cd1b4:8", "const:4:8"]]
- 004cd1b4 ["CALLIND", null, ["register:0:8"]]
+ 004cd1f4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004cd1f4 ["INT_ADD", "register:40f0:8", ["const:4cd1f4:8", "const:4:8"]]
+ 004cd1f4 ["CALLIND", null, ["register:0:8"]]
- 004cd1b4 bytes 20013fd6
+ 004cd1f4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e8c0d4bc2eb77ddbc33ae5e9b10a17d"></a>

### [`004cd2fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd2fc.md) → [`004cd33c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cd/004cd33c.md) _ZN5Botan4HMACC2EPNS_12HashFunctionE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58da0.md) · 呼出先 6件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md)
- 新版 呼出元 1件 [`00c591a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c591a0.md) · 呼出先 6件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c57f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f60.md)

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
      "definition_site": "004cd37c",
      "incomplete_value": true,
      "site": "004cd37c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004cd37c",
      "incomplete_value": true,
      "site": "004cd37c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004cd3f4",
      "incomplete_value": false,
      "site": "004cd400",
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
            "const:254:8"
          ]
        ]
      ]
    },
    "old": {
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
      "004cd360",
      "READ",
      [
        "storage",
        "00c9ab60",
        null,
        "pointer"
      ]
    ],
    [
      "004cd37c",
      "DATA",
      [
        "storage",
        "00c66810",
        null,
        "undefined1[200]"
      ]
    ],
    [
      "004cd37c",
      "DATA",
      [
        "storage",
        "00c66898",
        null,
        "undefined1[200]"
      ]
    ]
  ],
  "added": [
    [
      "004cd360",
      "READ",
      [
        "storage",
        "00c9af60",
        null,
        "pointer"
      ]
    ],
    [
      "004cd37c",
      "DATA",
      [
        "storage",
        "00c66c10",
        null,
        "undefined1[200]"
      ]
    ],
    [
      "004cd37c",
      "DATA",
      [
        "storage",
        "00c66c98",
        null,
        "undefined1[200]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cd3c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd2fc.md#insn-004cd3c0) · [`004cd414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd2fc.md#insn-004cd414) · [`004cd320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd2fc.md#insn-004cd320)
- 新版 `004cd400`（命令位置の公開資料なし） · `004cd454`（命令位置の公開資料なし） · `004cd360`（命令位置の公開資料なし）

~~~diff
- 004cd3c0 ["INT_ADD", "register:40f0:8", ["const:4cd3c0:8", "const:4:8"]]
- 004cd3c0 ["CALL", null, ["callee:00c57f60:8"]]
+ 004cd400 ["INT_ADD", "register:40f0:8", ["const:4cd400:8", "const:4:8"]]
+ 004cd400 ["CALL", null, ["callee:00c57f60:8"]]
- 004cd3c0 bytes e8291e94
+ 004cd400 bytes d82a1e94
- 004cd414 ["INT_ADD", "register:40f0:8", ["const:4cd414:8", "const:4:8"]]
- 004cd414 ["CALL", null, ["callee:00c57f10:8"]]
+ 004cd454 ["INT_ADD", "register:40f0:8", ["const:4cd454:8", "const:4:8"]]
+ 004cd454 ["CALL", null, ["callee:00c57f10:8"]]
- 004cd414 bytes bf291e94
+ 004cd454 bytes af2a1e94
- 004cd320 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b60:8"]]
- 004cd320 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004cd360 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f60:8"]]
+ 004cd360 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004cd320 bytes 08b145f9
+ 004cd360 bytes 08b147f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a51975c98c755b2db39ebfe2929533b3"></a>

### [`004cd634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd634.md) → [`004cd674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cd/004cd674.md) _ZN5Botan3KDF15create_or_throwERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
      "definition_site": "004cd6ec",
      "incomplete_value": false,
      "site": "004cd6f4",
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
            "const:fa1:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004cd72c",
      "incomplete_value": true,
      "site": "004cd738",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004cd728",
      "incomplete_value": false,
      "site": "004cd738",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004cd6e8",
      "incomplete_value": false,
      "site": "004cd6f8",
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
      "004cd6ec",
      "PARAM",
      [
        "storage",
        "002a1ed4",
        null,
        null
      ]
    ],
    [
      "004cd728",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004cd72c",
      "READ",
      [
        "storage",
        "00c9aa28",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004cd6ec",
      "PARAM",
      [
        "storage",
        "002a1fa1",
        null,
        null
      ]
    ],
    [
      "004cd728",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004cd72c",
      "READ",
      [
        "storage",
        "00c9ae28",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cd6b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd634.md#insn-004cd6b4) · [`004cd6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd634.md#insn-004cd6f8) · [`004cd668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd634.md#insn-004cd668)
- 新版 `004cd6f4`（命令位置の公開資料なし） · `004cd738`（命令位置の公開資料なし） · `004cd6a8`（命令位置の公開資料なし）

~~~diff
- 004cd6b4 ["INT_ADD", "register:40f0:8", ["const:4cd6b4:8", "const:4:8"]]
- 004cd6b4 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004cd6f4 ["INT_ADD", "register:40f0:8", ["const:4cd6f4:8", "const:4:8"]]
+ 004cd6f4 ["CALL", null, ["callee:0043ddd8:8"]]
- 004cd6b4 bytes b9c1fd97
+ 004cd6f4 bytes b9c1fd97
- 004cd6f8 ["INT_ADD", "register:40f0:8", ["const:4cd6f8:8", "const:4:8"]]
- 004cd6f8 ["CALL", null, ["callee:00c57f10:8"]]
+ 004cd738 ["INT_ADD", "register:40f0:8", ["const:4cd738:8", "const:4:8"]]
+ 004cd738 ["CALL", null, ["callee:00c57f10:8"]]
- 004cd6f8 bytes 06291e94
+ 004cd738 bytes f6291e94
- 004cd668 ["INT_ADD", "register:40f0:8", ["const:4cd668:8", "const:4:8"]]
- 004cd668 ["CALL", null, ["callee:00c591b0:8"]]
+ 004cd6a8 ["INT_ADD", "register:40f0:8", ["const:4cd6a8:8", "const:4:8"]]
+ 004cd6a8 ["CALL", null, ["callee:00c591b0:8"]]
- 004cd668 bytes d22d1e94
+ 004cd6a8 bytes c22e1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07d9d8f617f2495b355a67d03134080b"></a>

### [`004cd9a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd9a4.md) → [`004cd9e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cd/004cd9e4.md) _ZN5Botan7get_kdfERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58dc0.md) · 呼出先 9件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 1件 [`00c591c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c591c0.md) · 呼出先 9件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

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
      "definition_site": "004cdbcc",
      "incomplete_value": true,
      "site": "004cdbd4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004cdbc8",
      "incomplete_value": false,
      "site": "004cdbd4",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004cdb88",
      "incomplete_value": false,
      "site": "004cdb94",
      "value": [
        "leaf",
        "const:535828:8"
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
      "004cdbc8",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004cdbcc",
      "READ",
      [
        "storage",
        "00c9aad0",
        null,
        "pointer"
      ]
    ],
    [
      "004cdbcc",
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
      "004cdbc8",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004cdbcc",
      "READ",
      [
        "storage",
        "00c9aed0",
        null,
        "pointer"
      ]
    ],
    [
      "004cdbcc",
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

- 旧版 [`004cdb94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd9a4.md#insn-004cdb94) · [`004cd9ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd9a4.md#insn-004cd9ec) · [`004cd9f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd9a4.md#insn-004cd9f8)
- 新版 `004cdbd4`（命令位置の公開資料なし） · `004cda2c`（命令位置の公開資料なし） · `004cda38`（命令位置の公開資料なし）

~~~diff
- 004cdb94 ["INT_ADD", "register:40f0:8", ["const:4cdb94:8", "const:4:8"]]
- 004cdb94 ["CALL", null, ["callee:00c57f10:8"]]
+ 004cdbd4 ["INT_ADD", "register:40f0:8", ["const:4cdbd4:8", "const:4:8"]]
+ 004cdbd4 ["CALL", null, ["callee:00c57f10:8"]]
- 004cdb94 bytes df271e94
+ 004cdbd4 bytes cf281e94
- 004cd9ec ["INT_ADD", "register:40f0:8", ["const:4cd9ec:8", "const:4:8"]]
- 004cd9ec ["CALL", null, ["callee:0043bb20:8"]]
+ 004cda2c ["INT_ADD", "register:40f0:8", ["const:4cda2c:8", "const:4:8"]]
+ 004cda2c ["CALL", null, ["callee:0043bb20:8"]]
- 004cd9ec bytes 3db8fd97
+ 004cda2c bytes 3db8fd97
- 004cd9f8 ["INT_ADD", "register:40f0:8", ["const:4cd9f8:8", "const:4:8"]]
- 004cd9f8 ["CALL", null, ["callee:00c58d40:8"]]
+ 004cda38 ["INT_ADD", "register:40f0:8", ["const:4cda38:8", "const:4:8"]]
+ 004cda38 ["CALL", null, ["callee:00c58d40:8"]]
- 004cd9f8 bytes d22b1e94
+ 004cda38 bytes c22c1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-460e056efa79db2aa0ee6a40f3c55bac"></a>

### [`004cdbec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cdbec.md) → [`004cdc2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cd/004cdc2c.md) _ZN5Botan7KeyPair28encryption_consistency_checkERNS_21RandomNumberGeneratorERKNS_11Private_KeyERKNS_10Public_KeyERKNSt6__ndk112basic_stringI

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 15件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 15件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.08% / 新版 98.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004cdd98",
      "incomplete_value": true,
      "site": "004cdd98",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
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
    "ordinal": 11,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004cde80",
      "incomplete_value": true,
      "site": "004cde80",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
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
      "004cdd88",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004cde70",
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
      "004cdd88",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004cde70",
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

- 旧版 [`004cdd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cdbec.md#insn-004cdd58) · [`004cde40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cdbec.md#insn-004cde40) · [`004cdc38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cdbec.md#insn-004cdc38)
- 新版 `004cdd98`（命令位置の公開資料なし） · `004cde80`（命令位置の公開資料なし） · `004cdc78`（命令位置の公開資料なし）

~~~diff
- 004cdd58 ["COPY", "register:0:8", ["register:4048:8"]]
- 004cdd58 ["INT_ADD", "register:40f0:8", ["const:4cdd58:8", "const:4:8"]]
- 004cdd58 ["CALLIND", null, ["register:0:8"]]
+ 004cdd98 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004cdd98 ["INT_ADD", "register:40f0:8", ["const:4cdd98:8", "const:4:8"]]
+ 004cdd98 ["CALLIND", null, ["register:0:8"]]
- 004cdd58 bytes 20013fd6
+ 004cdd98 bytes 20013fd6
- 004cde40 ["COPY", "register:0:8", ["register:4048:8"]]
- 004cde40 ["INT_ADD", "register:40f0:8", ["const:4cde40:8", "const:4:8"]]
- 004cde40 ["CALLIND", null, ["register:0:8"]]
+ 004cde80 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004cde80 ["INT_ADD", "register:40f0:8", ["const:4cde80:8", "const:4:8"]]
+ 004cde80 ["CALLIND", null, ["register:0:8"]]
- 004cde40 bytes 20013fd6
+ 004cde80 bytes 20013fd6
- 004cdc38 ["INT_ADD", "register:40f0:8", ["const:4cdc38:8", "const:4:8"]]
- 004cdc38 ["CALL", null, ["callee:00c591d0:8"]]
+ 004cdc78 ["INT_ADD", "register:40f0:8", ["const:4cdc78:8", "const:4:8"]]
+ 004cdc78 ["CALL", null, ["callee:00c591d0:8"]]
- 004cdc38 bytes 662c1e94
+ 004cdc78 bytes 562d1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81ce26e159b1ce9b380888baff42e91b"></a>

### [`004ce954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce954.md) → [`004ce994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ce/004ce994.md) _ZNK5Botan3MD510copy_stateEv

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
      "definition_site": "004ce9c8",
      "incomplete_value": true,
      "site": "004ce9cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ce9f4",
      "incomplete_value": true,
      "site": "004ce9fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
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
      "004ce9bc",
      "READ",
      [
        "storage",
        "00c9ab38",
        null,
        "pointer"
      ]
    ],
    [
      "004ce9cc",
      "DATA",
      [
        "storage",
        "00c668d8",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "004ce9e4",
      "READ",
      [
        "storage",
        "00c9ab58",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ce9bc",
      "READ",
      [
        "storage",
        "00c9af38",
        null,
        "pointer"
      ]
    ],
    [
      "004ce9cc",
      "DATA",
      [
        "storage",
        "00c66cd8",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "004ce9e4",
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

- 旧版 [`004ce97c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce954.md#insn-004ce97c) · [`004ce970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce954.md#insn-004ce970) · [`004ce998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce954.md#insn-004ce998)
- 新版 `004ce9bc`（命令位置の公開資料なし） · `004ce9b0`（命令位置の公開資料なし） · `004ce9d8`（命令位置の公開資料なし）

~~~diff
- 004ce97c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b38:8"]]
- 004ce97c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ce9bc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f38:8"]]
+ 004ce9bc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004ce97c bytes 089d45f9
+ 004ce9bc bytes 089d47f9
- 004ce970 ["INT_ADD", "register:40f0:8", ["const:4ce970:8", "const:4:8"]]
- 004ce970 ["CALL", null, ["callee:00c57e90:8"]]
+ 004ce9b0 ["INT_ADD", "register:40f0:8", ["const:4ce9b0:8", "const:4:8"]]
+ 004ce9b0 ["CALL", null, ["callee:00c57e90:8"]]
- 004ce970 bytes 48241e94
+ 004ce9b0 bytes 38251e94
- 004ce998 ["INT_ADD", "register:40f0:8", ["const:4ce998:8", "const:4:8"]]
- 004ce998 ["CALL", null, ["callee:005402a4:8"]]
+ 004ce9d8 ["INT_ADD", "register:40f0:8", ["const:4ce9d8:8", "const:4:8"]]
+ 004ce9d8 ["CALL", null, ["callee:005402a4:8"]]
- 004ce998 bytes 33c60194
+ 004ce9d8 bytes 33c60194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8d0b3cde9b48ad9b2c3e83984538d52"></a>

### [`004cf4b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf4b4.md) → [`004cf4f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cf/004cf4f4.md) _ZN5Botan3MD55clearEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)

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
      "definition_site": "004cf53c",
      "incomplete_value": true,
      "site": "004cf540",
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
      "004cf53c",
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
      "004cf53c",
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

- 旧版 [`004cf4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf4b4.md#insn-004cf4d8) · [`004cf4f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf4b4.md#insn-004cf4f0) · [`004cf4fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf4b4.md#insn-004cf4fc)
- 新版 `004cf518`（命令位置の公開資料なし） · `004cf530`（命令位置の公開資料なし） · `004cf53c`（命令位置の公開資料なし）

~~~diff
- 004cf4d8 ["INT_ADD", "register:40f0:8", ["const:4cf4d8:8", "const:4:8"]]
- 004cf4d8 ["CALL", null, ["callee:00c58090:8"]]
+ 004cf518 ["INT_ADD", "register:40f0:8", ["const:4cf518:8", "const:4:8"]]
+ 004cf518 ["CALL", null, ["callee:00c58090:8"]]
- 004cf4d8 bytes ee211e94
+ 004cf518 bytes de221e94
- 004cf4f0 ["INT_ADD", "register:40f0:8", ["const:4cf4f0:8", "const:4:8"]]
- 004cf4f0 ["CALL", null, ["callee:00c58090:8"]]
+ 004cf530 ["INT_ADD", "register:40f0:8", ["const:4cf530:8", "const:4:8"]]
+ 004cf530 ["CALL", null, ["callee:00c58090:8"]]
- 004cf4f0 bytes e8211e94
+ 004cf530 bytes d8221e94
- 004cf4fc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:330:8"]]
- 004cf4fc ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 004cf4fc ["COPY", "register:5010:8", ["const:0:8"]]
- 004cf4fc ["COPY", "register:5018:8", ["const:0:8"]]
+ 004cf53c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:370:8"]]
+ 004cf53c ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
+ 004cf53c ["COPY", "register:5010:8", ["const:0:8"]]
+ 004cf53c ["COPY", "register:5018:8", ["const:0:8"]]
- 004cf4fc bytes 00cdc03d
+ 004cf53c bytes 00ddc03d
~~~


<a id="compare-7c91793e7a44336a0abfc74353d9ec5a"></a>

### [`004cf548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf548.md) → [`004cf588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cf/004cf588.md) _ZN5Botan16MDx_HashFunctionC2Embbm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md)

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
      "definition_site": "004cf5b4",
      "incomplete_value": true,
      "site": "004cf5b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
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
      "004cf5a4",
      "READ",
      [
        "storage",
        "00c9ab38",
        null,
        "pointer"
      ]
    ],
    [
      "004cf5b4",
      "DATA",
      [
        "storage",
        "00c668d8",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "004cf5a4",
      "READ",
      [
        "storage",
        "00c9af38",
        null,
        "pointer"
      ]
    ],
    [
      "004cf5b4",
      "DATA",
      [
        "storage",
        "00c66cd8",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cf564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf548.md#insn-004cf564) · [`004cf578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf548.md#insn-004cf578)
- 新版 `004cf5a4`（命令位置の公開資料なし） · `004cf5b8`（命令位置の公開資料なし）

~~~diff
- 004cf564 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b38:8"]]
- 004cf564 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004cf5a4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f38:8"]]
+ 004cf5a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004cf564 bytes 089d45f9
+ 004cf5a4 bytes 089d47f9
- 004cf578 ["INT_ADD", "register:40f0:8", ["const:4cf578:8", "const:4:8"]]
- 004cf578 ["CALL", null, ["callee:004b3508:8"]]
+ 004cf5b8 ["INT_ADD", "register:40f0:8", ["const:4cf5b8:8", "const:4:8"]]
+ 004cf5b8 ["CALL", null, ["callee:004b3508:8"]]
- 004cf578 bytes d48fff97
+ 004cf5b8 bytes d48fff97
~~~


<a id="compare-55a8fe2320f4cfe98c3de1b4a34553f5"></a>

### [`004cf7c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf7c8.md) → [`004cf808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cf/004cf808.md) _ZN5Botan16MDx_HashFunction11write_countEPh

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

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
      "definition_site": "004cf8b8",
      "incomplete_value": false,
      "site": "004cf8c0",
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
            "const:aa:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004cf8f0",
      "incomplete_value": true,
      "site": "004cf8fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004cf8ec",
      "incomplete_value": false,
      "site": "004cf8fc",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004cf8ac",
      "incomplete_value": false,
      "site": "004cf8bc",
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
      "004cf8b8",
      "PARAM",
      [
        "storage",
        "002a0fdd",
        null,
        "string"
      ]
    ],
    [
      "004cf8ec",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004cf8f0",
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
      "004cf8b8",
      "PARAM",
      [
        "storage",
        "002a10aa",
        null,
        "string"
      ]
    ],
    [
      "004cf8ec",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004cf8f0",
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

- 旧版 [`004cf880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf7c8.md#insn-004cf880) · [`004cf8bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf7c8.md#insn-004cf8bc) · [`004cf8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf7c8.md#insn-004cf8dc)
- 新版 `004cf8c0`（命令位置の公開資料なし） · `004cf8fc`（命令位置の公開資料なし） · `004cf91c`（命令位置の公開資料なし）

~~~diff
- 004cf880 ["INT_ADD", "register:40f0:8", ["const:4cf880:8", "const:4:8"]]
- 004cf880 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004cf8c0 ["INT_ADD", "register:40f0:8", ["const:4cf8c0:8", "const:4:8"]]
+ 004cf8c0 ["CALL", null, ["callee:0043ddd8:8"]]
- 004cf880 bytes 46b9fd97
+ 004cf8c0 bytes 46b9fd97
- 004cf8bc ["INT_ADD", "register:40f0:8", ["const:4cf8bc:8", "const:4:8"]]
- 004cf8bc ["CALL", null, ["callee:00c57f10:8"]]
+ 004cf8fc ["INT_ADD", "register:40f0:8", ["const:4cf8fc:8", "const:4:8"]]
+ 004cf8fc ["CALL", null, ["callee:00c57f10:8"]]
- 004cf8bc bytes 95201e94
+ 004cf8fc bytes 85211e94
- 004cf8dc ["INT_ADD", "register:40f0:8", ["const:4cf8dc:8", "const:4:8"]]
- 004cf8dc ["CALL", null, ["callee:0043ddd8:8"]]
+ 004cf91c ["INT_ADD", "register:40f0:8", ["const:4cf91c:8", "const:4:8"]]
+ 004cf91c ["CALL", null, ["callee:0043ddd8:8"]]
- 004cf8dc bytes 2fb9fd97
+ 004cf91c bytes 2fb9fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d877fd9a835d0cb1a3085ccaa36e9360"></a>

### [`004cf968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf968.md) → [`004cf9a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cf/004cf9a8.md) _ZN5Botan9mgf1_maskERNS_12HashFunctionEPKhmPhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58a00.md) · 呼出先 4件 [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)
- 新版 呼出元 1件 [`00c58e00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58e00.md) · 呼出先 4件 [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)

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
      "definition_site": "004cfb7c",
      "incomplete_value": true,
      "site": "004cfb7c",
      "value": [
        "LOAD",
        "8",
        [
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
      "004cfb6c",
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
      "004cfb6c",
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

- 旧版 [`004cfb3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf968.md#insn-004cfb3c) · [`004cf9bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf968.md#insn-004cf9bc) · [`004cf9e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf968.md#insn-004cf9e4)
- 新版 `004cfb7c`（命令位置の公開資料なし） · `004cf9fc`（命令位置の公開資料なし） · `004cfa24`（命令位置の公開資料なし）

~~~diff
- 004cfb3c ["COPY", "register:0:8", ["register:4048:8"]]
- 004cfb3c ["INT_ADD", "register:40f0:8", ["const:4cfb3c:8", "const:4:8"]]
- 004cfb3c ["CALLIND", null, ["register:0:8"]]
+ 004cfb7c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004cfb7c ["INT_ADD", "register:40f0:8", ["const:4cfb7c:8", "const:4:8"]]
+ 004cfb7c ["CALLIND", null, ["register:0:8"]]
- 004cfb3c bytes 20013fd6
+ 004cfb7c bytes 20013fd6
- 004cf9bc ["INT_ADD", "register:40f0:8", ["const:4cf9bc:8", "const:4:8"]]
- 004cf9bc ["CALL", null, ["callee:00c58660:8"]]
+ 004cf9fc ["INT_ADD", "register:40f0:8", ["const:4cf9fc:8", "const:4:8"]]
+ 004cf9fc ["CALL", null, ["callee:00c58660:8"]]
- 004cf9bc bytes 29221e94
+ 004cf9fc bytes 19231e94
- 004cf9e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 004cf9e4 ["INT_ADD", "register:40f0:8", ["const:4cf9e4:8", "const:4:8"]]
- 004cf9e4 ["CALLIND", null, ["register:0:8"]]
+ 004cfa24 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004cfa24 ["INT_ADD", "register:40f0:8", ["const:4cfa24:8", "const:4:8"]]
+ 004cfa24 ["CALLIND", null, ["register:0:8"]]
- 004cf9e4 bytes 00013fd6
+ 004cfa24 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60e637b7aa9300a3d5e196b9ff518962"></a>

### [`004d0ea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d0ea8.md) → [`004d0ee8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d0/004d0ee8.md) _ZN5Botan8split_onERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEc

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58e90.md) · 呼出先 4件 [`00547b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547b2c.md) [`00547b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547b30.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58bb0.md)
- 新版 呼出元 1件 [`00c59290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59290.md) · 呼出先 4件 [`00547b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547b6c.md) [`00547b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547b70.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58fb0.md)

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
      "definition_site": "004d0f0c",
      "incomplete_value": false,
      "site": "004d0f10",
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
    "old": {
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
      "004d0f10",
      "DATA",
      [
        "storage",
        "00c6a2b0",
        null,
        "undefined *"
      ]
    ],
    [
      "004d0f48",
      "READ",
      [
        "storage",
        "00c6a2d0",
        null,
        "pointer"
      ]
    ],
    [
      "004d0f48",
      "READ",
      [
        "storage",
        "00c6a2d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004d0f10",
      "DATA",
      [
        "storage",
        "00c6a6b0",
        null,
        "undefined *"
      ]
    ],
    [
      "004d0f48",
      "READ",
      [
        "storage",
        "00c6a6d0",
        null,
        "pointer"
      ]
    ],
    [
      "004d0f48",
      "READ",
      [
        "storage",
        "00c6a6d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d0ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d0ea8.md#insn-004d0ecc) · [`004d0ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d0ea8.md#insn-004d0ee0) · [`004d0f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d0ea8.md#insn-004d0f0c)
- 新版 `004d0f0c`（命令位置の公開資料なし） · `004d0f20`（命令位置の公開資料なし） · `004d0f4c`（命令位置の公開資料なし）

~~~diff
- 004d0ecc ["COPY", "tmp:0:8", ["const:2b0:8"]]
- 004d0ecc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004d0ecc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004d0ecc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004d0f0c ["COPY", "tmp:0:8", ["const:6b0:8"]]
+ 004d0f0c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004d0f0c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004d0f0c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004d0ecc bytes 29c10a91
+ 004d0f0c bytes 29c11a91
- 004d0ee0 ["INT_ADD", "register:40f0:8", ["const:4d0ee0:8", "const:4:8"]]
- 004d0ee0 ["CALL", null, ["callee:00c58fb0:8"]]
+ 004d0f20 ["INT_ADD", "register:40f0:8", ["const:4d0f20:8", "const:4:8"]]
+ 004d0f20 ["CALL", null, ["callee:00c58fb0:8"]]
- 004d0ee0 bytes 341f1e94
+ 004d0f20 bytes 24201e94
- 004d0f0c ["COPY", "register:0:8", ["register:4040:8"]]
- 004d0f0c ["INT_ADD", "register:40f0:8", ["const:4d0f0c:8", "const:4:8"]]
- 004d0f0c ["CALLIND", null, ["register:0:8"]]
+ 004d0f4c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004d0f4c ["INT_ADD", "register:40f0:8", ["const:4d0f4c:8", "const:4:8"]]
+ 004d0f4c ["CALLIND", null, ["register:0:8"]]
- 004d0f0c bytes 00013fd6
+ 004d0f4c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d8d193a8e6a1010e3a1b4c00520922a"></a>

### [`004d0f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d0f80.md) → [`004d0fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d0/004d0fc0.md) _ZN5Botan20parse_algorithm_nameERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58bc0.md) · 呼出先 17件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00440f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f1c.md) [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md)
- 新版 呼出元 1件 [`00c58fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58fc0.md) · 呼出先 17件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00440f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f5c.md) [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md)

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
      "definition_site": "004d18bc",
      "incomplete_value": true,
      "site": "004d18c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 36,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004d18b8",
      "incomplete_value": false,
      "site": "004d18c4",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004d1878",
      "incomplete_value": false,
      "site": "004d1884",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "ordinal": 36,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004d199c",
      "incomplete_value": true,
      "site": "004d19a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "004d18b8",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004d18bc",
      "READ",
      [
        "storage",
        "00c9ab90",
        null,
        "pointer"
      ]
    ],
    [
      "004d18bc",
      "PARAM",
      [
        "storage",
        "00c67340",
        "_ZTIN5Botan22Invalid_Algorithm_NameE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004d18b8",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004d18bc",
      "READ",
      [
        "storage",
        "00c9af90",
        null,
        "pointer"
      ]
    ],
    [
      "004d18bc",
      "PARAM",
      [
        "storage",
        "00c67740",
        "_ZTIN5Botan22Invalid_Algorithm_NameE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d1884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d0f80.md#insn-004d1884) · [`004d1924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d0f80.md#insn-004d1924) · [`004d1964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d0f80.md#insn-004d1964)
- 新版 `004d18c4`（命令位置の公開資料なし） · `004d1964`（命令位置の公開資料なし） · `004d19a4`（命令位置の公開資料なし）

~~~diff
- 004d1884 ["INT_ADD", "register:40f0:8", ["const:4d1884:8", "const:4:8"]]
- 004d1884 ["CALL", null, ["callee:00c57f10:8"]]
+ 004d18c4 ["INT_ADD", "register:40f0:8", ["const:4d18c4:8", "const:4:8"]]
+ 004d18c4 ["CALL", null, ["callee:00c57f10:8"]]
- 004d1884 bytes a3181e94
+ 004d18c4 bytes 93191e94
- 004d1924 ["INT_ADD", "register:40f0:8", ["const:4d1924:8", "const:4:8"]]
- 004d1924 ["CALL", null, ["callee:00440f5c:8"]]
+ 004d1964 ["INT_ADD", "register:40f0:8", ["const:4d1964:8", "const:4:8"]]
+ 004d1964 ["CALL", null, ["callee:00440f5c:8"]]
- 004d1924 bytes 7ebdfd97
+ 004d1964 bytes 7ebdfd97
- 004d1964 ["INT_ADD", "register:40f0:8", ["const:4d1964:8", "const:4:8"]]
- 004d1964 ["CALL", null, ["callee:00c57f10:8"]]
+ 004d19a4 ["INT_ADD", "register:40f0:8", ["const:4d19a4:8", "const:4:8"]]
+ 004d19a4 ["CALL", null, ["callee:00c57f10:8"]]
- 004d1964 bytes 6b181e94
+ 004d19a4 bytes 5b191e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa22ad8d9142761cb5972be8109ab922"></a>

### [`004d6b84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d6/004d6b84.md) → [`004d6bc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d6/004d6bc4.md) FUN_004d6bc4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`004b7f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b7f88.md) [`004b8cd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8cd4.md) [`004d7350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7350.md) [`004d78c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d78c8.md) [`004db660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004db660.md) · 呼出先 1件 [`00c58250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58250.md)
- 新版 呼出元 5件 [`004b7fc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b7fc8.md) [`004b8d14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8d14.md) [`004d7390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d7/004d7390.md) [`004d7908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d7/004d7908.md) [`004db6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004db/004db6a0.md) · 呼出先 1件 [`00c58650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58650.md)

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
      "definition_site": "004d6cf0",
      "incomplete_value": false,
      "site": "004d6d10",
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
    "old": {
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004d6cf8",
      "incomplete_value": false,
      "site": "004d6d10",
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
    "old": {
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
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004d6d00",
      "incomplete_value": false,
      "site": "004d6d10",
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
            "const:c2d:8"
          ]
        ]
      ]
    },
    "old": {
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
      "004d6cf0",
      "PARAM",
      [
        "storage",
        "002a6504",
        null,
        "string"
      ]
    ],
    [
      "004d6cf8",
      "PARAM",
      [
        "storage",
        "002b606d",
        null,
        "string"
      ]
    ],
    [
      "004d6d00",
      "PARAM",
      [
        "storage",
        "002a8b60",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004d6cf0",
      "PARAM",
      [
        "storage",
        "002a65e0",
        null,
        "string"
      ]
    ],
    [
      "004d6cf8",
      "PARAM",
      [
        "storage",
        "002b60ad",
        null,
        "string"
      ]
    ],
    [
      "004d6d00",
      "PARAM",
      [
        "storage",
        "002a8c2d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d6cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d6/004d6b84.md#insn-004d6cd0) · [`004d6cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d6/004d6b84.md#insn-004d6cb0) · [`004d6cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d6/004d6b84.md#insn-004d6cb8)
- 新版 `004d6d10`（命令位置の公開資料なし） · `004d6cf0`（命令位置の公開資料なし） · `004d6cf8`（命令位置の公開資料なし）

~~~diff
- 004d6cd0 ["INT_ADD", "register:40f0:8", ["const:4d6cd0:8", "const:4:8"]]
- 004d6cd0 ["CALL", null, ["callee:00c58650:8"]]
+ 004d6d10 ["INT_ADD", "register:40f0:8", ["const:4d6d10:8", "const:4:8"]]
+ 004d6d10 ["CALL", null, ["callee:00c58650:8"]]
- 004d6cd0 bytes 60051e94
+ 004d6d10 bytes 50061e94
- 004d6cb0 ["COPY", "tmp:0:8", ["const:504:8"]]
- 004d6cb0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004d6cb0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004d6cb0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004d6cf0 ["COPY", "tmp:0:8", ["const:5e0:8"]]
+ 004d6cf0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004d6cf0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004d6cf0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004d6cb0 bytes 00101491
+ 004d6cf0 bytes 00801791
- 004d6cb8 ["COPY", "tmp:0:8", ["const:6d:8"]]
- 004d6cb8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004d6cb8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004d6cb8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004d6cf8 ["COPY", "tmp:0:8", ["const:ad:8"]]
+ 004d6cf8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004d6cf8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004d6cf8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004d6cb8 bytes 21b40191
+ 004d6cf8 bytes 21b40291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8cb138e0c7458da8345d69a63a9cf35b"></a>

### [`004d7684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7684.md) → [`004d76c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d7/004d76c4.md) FUN_004d76c4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`004db524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004db524.md) [`004e03e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e0/004e03e8.md) · 呼出先 9件 [`004d1e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d1/004d1e2c.md) [`004d20d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d2/004d20d8.md) [`004d26d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d2/004d26d4.md) [`004d3178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d3/004d3178.md) [`004d3ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d3/004d3ef4.md)
- 新版 呼出元 2件 [`004db564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004db/004db564.md) [`004e0428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e0/004e0428.md) · 呼出先 9件 [`004d1e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d1/004d1e6c.md) [`004d2118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d2/004d2118.md) [`004d2714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d2/004d2714.md) [`004d31b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d3/004d31b8.md) [`004d3f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d3/004d3f34.md)

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
      "definition_site": "004d7864",
      "incomplete_value": false,
      "site": "004d7884",
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
            "const:553:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004d786c",
      "incomplete_value": false,
      "site": "004d7884",
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
            "const:c3c:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004d7874",
      "incomplete_value": false,
      "site": "004d7884",
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
            "const:26e:8"
          ]
        ]
      ]
    },
    "old": {
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
      "004d7864",
      "PARAM",
      [
        "storage",
        "002a5477",
        null,
        "string"
      ]
    ],
    [
      "004d786c",
      "PARAM",
      [
        "storage",
        "002a8b6f",
        null,
        "string"
      ]
    ],
    [
      "004d7874",
      "PARAM",
      [
        "storage",
        "002ba22e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004d7864",
      "PARAM",
      [
        "storage",
        "002a5553",
        null,
        "string"
      ]
    ],
    [
      "004d786c",
      "PARAM",
      [
        "storage",
        "002a8c3c",
        null,
        "string"
      ]
    ],
    [
      "004d7874",
      "PARAM",
      [
        "storage",
        "002ba26e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d7844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7684.md#insn-004d7844) · [`004d77c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7684.md#insn-004d77c4) · [`004d7824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7684.md#insn-004d7824)
- 新版 `004d7884`（命令位置の公開資料なし） · `004d7804`（命令位置の公開資料なし） · `004d7864`（命令位置の公開資料なし）

~~~diff
- 004d7844 ["INT_ADD", "register:40f0:8", ["const:4d7844:8", "const:4:8"]]
- 004d7844 ["CALL", null, ["callee:00c58650:8"]]
+ 004d7884 ["INT_ADD", "register:40f0:8", ["const:4d7884:8", "const:4:8"]]
+ 004d7884 ["CALL", null, ["callee:00c58650:8"]]
- 004d7844 bytes 83021e94
+ 004d7884 bytes 73031e94
- 004d77c4 ["INT_ADD", "register:40f0:8", ["const:4d77c4:8", "const:4:8"]]
- 004d77c4 ["CALL", null, ["callee:004d7888:8"]]
+ 004d7804 ["INT_ADD", "register:40f0:8", ["const:4d7804:8", "const:4:8"]]
+ 004d7804 ["CALL", null, ["callee:004d7888:8"]]
- 004d77c4 bytes 21000094
+ 004d7804 bytes 21000094
- 004d7824 ["COPY", "tmp:0:8", ["const:477:8"]]
- 004d7824 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004d7824 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004d7824 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004d7864 ["COPY", "tmp:0:8", ["const:553:8"]]
+ 004d7864 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004d7864 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004d7864 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004d7824 bytes 00dc1191
+ 004d7864 bytes 004c1591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-509baac97403a5a4bd8a269fe9df275d"></a>

### [`004d7e9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7e9c.md) → [`004d7edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d7/004d7edc.md) _ZN5Botan19generate_dsa_primesERNS_21RandomNumberGeneratorERNS_6BigIntES3_mmRKNSt6__ndk16vectorIhNS4_9allocatorIhEEEEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58eb0.md) · 呼出先 25件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`004a680c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a680c.md) [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`005408e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005408e0.md)
- 新版 呼出元 1件 [`00c592b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c592b0.md) · 呼出先 25件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`004a684c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a684c.md) [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00540920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540920.md)

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
      "definition_site": "004d7f6c",
      "incomplete_value": false,
      "site": "004d7f78",
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
            "const:bc:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 2,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004d7f98",
      "incomplete_value": false,
      "site": "004d7fa0",
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
    "old": {
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004d7fdc",
      "incomplete_value": false,
      "site": "004d7fe4",
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
            "const:1a2:8"
          ]
        ]
      ]
    },
    "old": {
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
      "004d7f6c",
      "PARAM",
      [
        "storage",
        "002b607c",
        null,
        "string"
      ]
    ],
    [
      "004d7f98",
      "PARAM",
      [
        "storage",
        "002a5276",
        null,
        null
      ]
    ],
    [
      "004d7fdc",
      "PARAM",
      [
        "storage",
        "002b8162",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004d7f6c",
      "PARAM",
      [
        "storage",
        "002b60bc",
        null,
        "string"
      ]
    ],
    [
      "004d7f98",
      "PARAM",
      [
        "storage",
        "002a5352",
        null,
        null
      ]
    ],
    [
      "004d7fdc",
      "PARAM",
      [
        "storage",
        "002b81a2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d7f38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7e9c.md#insn-004d7f38) · [`004d7f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7e9c.md#insn-004d7f60) · [`004d7fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7e9c.md#insn-004d7fa4)
- 新版 `004d7f78`（命令位置の公開資料なし） · `004d7fa0`（命令位置の公開資料なし） · `004d7fe4`（命令位置の公開資料なし）

~~~diff
- 004d7f38 ["INT_ADD", "register:40f0:8", ["const:4d7f38:8", "const:4:8"]]
- 004d7f38 ["CALL", null, ["callee:00c57f60:8"]]
+ 004d7f78 ["INT_ADD", "register:40f0:8", ["const:4d7f78:8", "const:4:8"]]
+ 004d7f78 ["CALL", null, ["callee:00c57f60:8"]]
- 004d7f38 bytes 0aff1d94
+ 004d7f78 bytes faff1d94
- 004d7f60 ["INT_ADD", "register:40f0:8", ["const:4d7f60:8", "const:4:8"]]
- 004d7f60 ["CALL", null, ["callee:00c57f70:8"]]
+ 004d7fa0 ["INT_ADD", "register:40f0:8", ["const:4d7fa0:8", "const:4:8"]]
+ 004d7fa0 ["CALL", null, ["callee:00c57f70:8"]]
- 004d7f60 bytes 04ff1d94
+ 004d7fa0 bytes f4ff1d94
- 004d7fa4 ["INT_ADD", "register:40f0:8", ["const:4d7fa4:8", "const:4:8"]]
- 004d7fa4 ["CALL", null, ["callee:00c57f70:8"]]
+ 004d7fe4 ["INT_ADD", "register:40f0:8", ["const:4d7fe4:8", "const:4:8"]]
+ 004d7fe4 ["CALL", null, ["callee:00c57f70:8"]]
- 004d7fa4 bytes f3fe1d94
+ 004d7fe4 bytes e3ff1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a417991704fc4469ffc99a57be9ff80d"></a>

### [`004d8aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d8/004d8aac.md) → [`004d8aec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d8/004d8aec.md) _ZN5Botan8is_primeERKNS_6BigIntERNS_21RandomNumberGeneratorEmb

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c58ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58ec0.md) · 呼出先 14件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58520.md) [`00c58720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58720.md) [`00c588c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c588c0.md)
- 新版 呼出元 1件 [`00c592c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c592c0.md) · 呼出先 14件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c58920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58920.md) [`00c58b20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58b20.md) [`00c58cc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58cc0.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.36% / 新版 96.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 8件

アドレスに依存する影響 `call_target` 10件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004d92b8",
      "incomplete_value": true,
      "site": "004d92b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 36,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004d8b6c",
      "incomplete_value": true,
      "site": "004d8b6c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004d8bdc",
      "incomplete_value": true,
      "site": "004d8bdc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004d8b5c",
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
    ],
    [
      "004d8c0c",
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
      "004d8b5c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004d8bcc",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004d8c0c",
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

- 旧版 [`004d8b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d8/004d8aac.md#insn-004d8b2c) · [`004d8b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d8/004d8aac.md#insn-004d8b9c) · [`004d8bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d8/004d8aac.md#insn-004d8bdc)
- 新版 `004d8b6c`（命令位置の公開資料なし） · `004d8bdc`（命令位置の公開資料なし） · `004d8c1c`（命令位置の公開資料なし）

~~~diff
- 004d8b2c ["COPY", "register:0:8", ["register:4048:8"]]
- 004d8b2c ["INT_ADD", "register:40f0:8", ["const:4d8b2c:8", "const:4:8"]]
- 004d8b2c ["CALLIND", null, ["register:0:8"]]
+ 004d8b6c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004d8b6c ["INT_ADD", "register:40f0:8", ["const:4d8b6c:8", "const:4:8"]]
+ 004d8b6c ["CALLIND", null, ["register:0:8"]]
- 004d8b2c bytes 20013fd6
+ 004d8b6c bytes 20013fd6
- 004d8b9c ["COPY", "register:0:8", ["register:4048:8"]]
- 004d8b9c ["INT_ADD", "register:40f0:8", ["const:4d8b9c:8", "const:4:8"]]
- 004d8b9c ["CALLIND", null, ["register:0:8"]]
+ 004d8bdc ["COPY", "register:0:8", ["register:4048:8"]]
+ 004d8bdc ["INT_ADD", "register:40f0:8", ["const:4d8bdc:8", "const:4:8"]]
+ 004d8bdc ["CALLIND", null, ["register:0:8"]]
- 004d8b9c bytes 20013fd6
+ 004d8bdc bytes 20013fd6
- 004d8bdc ["COPY", "register:0:8", ["register:4048:8"]]
- 004d8bdc ["INT_ADD", "register:40f0:8", ["const:4d8bdc:8", "const:4:8"]]
- 004d8bdc ["CALLIND", null, ["register:0:8"]]
+ 004d8c1c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004d8c1c ["INT_ADD", "register:40f0:8", ["const:4d8c1c:8", "const:4:8"]]
+ 004d8c1c ["CALLIND", null, ["register:0:8"]]
- 004d8bdc bytes 20013fd6
+ 004d8c1c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-403392592efd3ee7bc87380d80001093"></a>

### [`004d94d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d9/004d94d8.md) → [`004d9518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d9/004d9518.md) _ZN5Botan6jacobiERKNS_6BigIntES2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c58f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58f30.md) · 呼出先 15件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004b9bf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b9bf8.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 1件 [`00c59330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59330.md) · 呼出先 15件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004b9c38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b9/004b9c38.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 93.51% / 新版 93.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 8件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004d95a8",
      "incomplete_value": true,
      "site": "004d95a8",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004d961c",
      "incomplete_value": true,
      "site": "004d961c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004d95dc",
      "incomplete_value": true,
      "site": "004d95dc",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 8,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004d9688",
      "incomplete_value": true,
      "site": "004d9688",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004d9648",
      "incomplete_value": true,
      "site": "004d9648",
      "value": [
        "LOAD",
        "8",
        [
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
      "004d9598",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004d960c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004d967c",
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
      "004d9598",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004d960c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004d967c",
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

- 旧版 [`004d9568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d9/004d94d8.md#insn-004d9568) · [`004d95dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d9/004d94d8.md#insn-004d95dc) · [`004d9648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d9/004d94d8.md#insn-004d9648)
- 新版 `004d95a8`（命令位置の公開資料なし） · `004d961c`（命令位置の公開資料なし） · `004d9688`（命令位置の公開資料なし）

~~~diff
- 004d9568 ["COPY", "register:0:8", ["register:4048:8"]]
- 004d9568 ["INT_ADD", "register:40f0:8", ["const:4d9568:8", "const:4:8"]]
- 004d9568 ["CALLIND", null, ["register:0:8"]]
+ 004d95a8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004d95a8 ["INT_ADD", "register:40f0:8", ["const:4d95a8:8", "const:4:8"]]
+ 004d95a8 ["CALLIND", null, ["register:0:8"]]
- 004d9568 bytes 20013fd6
+ 004d95a8 bytes 20013fd6
- 004d95dc ["COPY", "register:0:8", ["register:4048:8"]]
- 004d95dc ["INT_ADD", "register:40f0:8", ["const:4d95dc:8", "const:4:8"]]
- 004d95dc ["CALLIND", null, ["register:0:8"]]
+ 004d961c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004d961c ["INT_ADD", "register:40f0:8", ["const:4d961c:8", "const:4:8"]]
+ 004d961c ["CALLIND", null, ["register:0:8"]]
- 004d95dc bytes 20013fd6
+ 004d961c bytes 20013fd6
- 004d9648 ["COPY", "register:0:8", ["register:4048:8"]]
- 004d9648 ["INT_ADD", "register:40f0:8", ["const:4d9648:8", "const:4:8"]]
- 004d9648 ["CALLIND", null, ["register:0:8"]]
+ 004d9688 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004d9688 ["INT_ADD", "register:40f0:8", ["const:4d9688:8", "const:4:8"]]
+ 004d9688 ["CALLIND", null, ["register:0:8"]]
- 004d9648 bytes 20013fd6
+ 004d9688 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98edc3774a40115a5e4240968e6957d5"></a>

### [`004d9be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d9/004d9be8.md) → [`004d9c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d9/004d9c28.md) _ZN5Botan12random_primeERNS_21RandomNumberGeneratorEmRKNS_6BigIntEmm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58f40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58f40.md) · 呼出先 21件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004da570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004da/004da570.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`005408e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005408e0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00c59340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59340.md) · 呼出先 21件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004da5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004da/004da5b0.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00540920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540920.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.90% / 新版 94.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `call_target` 8件

アドレスに依存する影響 `call_argument_candidate` 4件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004d9cb4",
      "incomplete_value": true,
      "site": "004d9cb4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004d9f70",
      "incomplete_value": true,
      "site": "004d9f70",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 16,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004da00c",
      "incomplete_value": true,
      "site": "004da00c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004d9fcc",
      "incomplete_value": true,
      "site": "004d9fcc",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 22,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004d9ca4",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004d9e1c",
      "READ",
      [
        "storage",
        "00c9aba8",
        null,
        "pointer"
      ]
    ],
    [
      "004d9f60",
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
      "004d9ca4",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004d9e1c",
      "READ",
      [
        "storage",
        "00c9afa8",
        null,
        "pointer"
      ]
    ],
    [
      "004d9f60",
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

- 旧版 [`004d9c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d9/004d9be8.md#insn-004d9c74) · [`004d9ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d9/004d9be8.md#insn-004d9ef0) · [`004d9f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d9/004d9be8.md#insn-004d9f30)
- 新版 `004d9cb4`（命令位置の公開資料なし） · `004d9f30`（命令位置の公開資料なし） · `004d9f70`（命令位置の公開資料なし）

~~~diff
- 004d9c74 ["COPY", "register:0:8", ["register:4048:8"]]
- 004d9c74 ["INT_ADD", "register:40f0:8", ["const:4d9c74:8", "const:4:8"]]
- 004d9c74 ["CALLIND", null, ["register:0:8"]]
+ 004d9cb4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004d9cb4 ["INT_ADD", "register:40f0:8", ["const:4d9cb4:8", "const:4:8"]]
+ 004d9cb4 ["CALLIND", null, ["register:0:8"]]
- 004d9c74 bytes 20013fd6
+ 004d9cb4 bytes 20013fd6
- 004d9ef0 ["INT_ADD", "register:40f0:8", ["const:4d9ef0:8", "const:4:8"]]
- 004d9ef0 ["CALL", null, ["callee:00c58cd0:8"]]
+ 004d9f30 ["INT_ADD", "register:40f0:8", ["const:4d9f30:8", "const:4:8"]]
+ 004d9f30 ["CALL", null, ["callee:00c58cd0:8"]]
- 004d9ef0 bytes 78fa1d94
+ 004d9f30 bytes 68fb1d94
- 004d9f30 ["COPY", "register:0:8", ["register:4048:8"]]
- 004d9f30 ["INT_ADD", "register:40f0:8", ["const:4d9f30:8", "const:4:8"]]
- 004d9f30 ["CALLIND", null, ["register:0:8"]]
+ 004d9f70 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004d9f70 ["INT_ADD", "register:40f0:8", ["const:4d9f70:8", "const:4:8"]]
+ 004d9f70 ["CALLIND", null, ["register:0:8"]]
- 004d9f30 bytes 20013fd6
+ 004d9f70 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6457e863352cb3f404bf9919c88a8952"></a>

### [`004da570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004da/004da570.md) → [`004da5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004da/004da5b0.md) FUN_004da5b0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004d9be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d9/004d9be8.md) · 呼出先 7件 [`00544e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544e08.md) [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`004d9c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d9/004d9c28.md) · 呼出先 7件 [`00544e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00544/00544e48.md) [`00c37ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ba4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.23% / 新版 96.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004da674",
      "incomplete_value": true,
      "site": "004da67c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004da678",
      "incomplete_value": true,
      "site": "004da67c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004da674",
      "READ",
      [
        "storage",
        "00c9a9e8",
        null,
        "pointer"
      ]
    ],
    [
      "004da674",
      "PARAM",
      [
        "storage",
        "00c96298",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "004da678",
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
      "004da674",
      "READ",
      [
        "storage",
        "00c9ade8",
        null,
        "pointer"
      ]
    ],
    [
      "004da674",
      "PARAM",
      [
        "storage",
        "00c96698",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "004da678",
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

- 旧版 [`004da63c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004da/004da570.md#insn-004da63c) · [`004da5b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004da/004da570.md#insn-004da5b8) · [`004da604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004da/004da570.md#insn-004da604)
- 新版 `004da67c`（命令位置の公開資料なし） · `004da5f8`（命令位置の公開資料なし） · `004da644`（命令位置の公開資料なし）

~~~diff
- 004da63c ["INT_ADD", "register:40f0:8", ["const:4da63c:8", "const:4:8"]]
- 004da63c ["CALL", null, ["callee:00c57f10:8"]]
+ 004da67c ["INT_ADD", "register:40f0:8", ["const:4da67c:8", "const:4:8"]]
+ 004da67c ["CALL", null, ["callee:00c57f10:8"]]
- 004da63c bytes 35f51d94
+ 004da67c bytes 25f61d94
- 004da5b8 ["INT_ADD", "register:40f0:8", ["const:4da5b8:8", "const:4:8"]]
- 004da5b8 ["CALL", null, ["callee:00c58a30:8"]]
+ 004da5f8 ["INT_ADD", "register:40f0:8", ["const:4da5f8:8", "const:4:8"]]
+ 004da5f8 ["CALL", null, ["callee:00c58a30:8"]]
- 004da5b8 bytes 1ef81d94
+ 004da5f8 bytes 0ef91d94
- 004da604 ["INT_ADD", "register:40f0:8", ["const:4da604:8", "const:4:8"]]
- 004da604 ["CALL", null, ["callee:00544e48:8"]]
+ 004da644 ["INT_ADD", "register:40f0:8", ["const:4da644:8", "const:4:8"]]
+ 004da644 ["CALL", null, ["callee:00544e48:8"]]
- 004da604 bytes 01aa0194
+ 004da644 bytes 01aa0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5c3aa30d6025b2e1bdbc96f3516837b"></a>

### [`004da668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004da/004da668.md) → [`004da6a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004da/004da6a8.md) _ZN5Botan3gcdERKNS_6BigIntES2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58f60.md) · 呼出先 9件 [`004b9bf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b9bf8.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58520.md) [`00c58720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58720.md)
- 新版 呼出元 1件 [`00c59360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59360.md) · 呼出先 9件 [`004b9c38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b9/004b9c38.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c58920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58920.md) [`00c58b20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58b20.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.70% / 新版 98.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004da7fc",
      "incomplete_value": true,
      "site": "004da7fc",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004da828",
      "incomplete_value": true,
      "site": "004da828",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004dafe0",
      "incomplete_value": true,
      "site": "004dafe0",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004dafa0",
      "incomplete_value": true,
      "site": "004dafa0",
      "value": [
        "LOAD",
        "8",
        [
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
      "004da7ec",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004da818",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004dafd0",
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
      "004da7ec",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004da818",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004dafd0",
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

- 旧版 [`004da7bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004da/004da668.md#insn-004da7bc) · [`004da7e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004da/004da668.md#insn-004da7e8) · [`004dafa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004da/004da668.md#insn-004dafa0)
- 新版 `004da7fc`（命令位置の公開資料なし） · `004da828`（命令位置の公開資料なし） · `004dafe0`（命令位置の公開資料なし）

~~~diff
- 004da7bc ["COPY", "register:0:8", ["register:4048:8"]]
- 004da7bc ["INT_ADD", "register:40f0:8", ["const:4da7bc:8", "const:4:8"]]
- 004da7bc ["CALLIND", null, ["register:0:8"]]
+ 004da7fc ["COPY", "register:0:8", ["register:4048:8"]]
+ 004da7fc ["INT_ADD", "register:40f0:8", ["const:4da7fc:8", "const:4:8"]]
+ 004da7fc ["CALLIND", null, ["register:0:8"]]
- 004da7bc bytes 20013fd6
+ 004da7fc bytes 20013fd6
- 004da7e8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004da7e8 ["INT_ADD", "register:40f0:8", ["const:4da7e8:8", "const:4:8"]]
- 004da7e8 ["CALLIND", null, ["register:0:8"]]
+ 004da828 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004da828 ["INT_ADD", "register:40f0:8", ["const:4da828:8", "const:4:8"]]
+ 004da828 ["CALLIND", null, ["register:0:8"]]
- 004da7e8 bytes 20013fd6
+ 004da828 bytes 20013fd6
- 004dafa0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004dafa0 ["INT_ADD", "register:40f0:8", ["const:4dafa0:8", "const:4:8"]]
- 004dafa0 ["CALLIND", null, ["register:0:8"]]
+ 004dafe0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004dafe0 ["INT_ADD", "register:40f0:8", ["const:4dafe0:8", "const:4:8"]]
+ 004dafe0 ["CALLIND", null, ["register:0:8"]]
- 004dafa0 bytes 20013fd6
+ 004dafe0 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16eac68a1520549194c129f7b9247cff"></a>

### [`004db0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004db0a8.md) → [`004db0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004db/004db0e8.md) _ZN5Botan17random_safe_primeERNS_21RandomNumberGeneratorEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 15件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md)
- 新版 呼出元 0件  · 呼出先 15件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c57f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f60.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.09% / 新版 94.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 5件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004db2a8",
      "incomplete_value": true,
      "site": "004db2a8",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
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
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004db2d4",
      "incomplete_value": true,
      "site": "004db2d4",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
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
    "ordinal": 7,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004db300",
      "incomplete_value": true,
      "site": "004db300",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "004db2c0",
      "incomplete_value": true,
      "site": "004db2c0",
      "value": [
        "LOAD",
        "8",
        [
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
      "004db298",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004db2c4",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004db2f0",
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
      "004db298",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004db2c4",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004db2f0",
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

- 旧版 [`004db268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004db0a8.md#insn-004db268) · [`004db294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004db0a8.md#insn-004db294) · [`004db2c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004db0a8.md#insn-004db2c0)
- 新版 `004db2a8`（命令位置の公開資料なし） · `004db2d4`（命令位置の公開資料なし） · `004db300`（命令位置の公開資料なし）

~~~diff
- 004db268 ["COPY", "register:0:8", ["register:4048:8"]]
- 004db268 ["INT_ADD", "register:40f0:8", ["const:4db268:8", "const:4:8"]]
- 004db268 ["CALLIND", null, ["register:0:8"]]
+ 004db2a8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004db2a8 ["INT_ADD", "register:40f0:8", ["const:4db2a8:8", "const:4:8"]]
+ 004db2a8 ["CALLIND", null, ["register:0:8"]]
- 004db268 bytes 20013fd6
+ 004db2a8 bytes 20013fd6
- 004db294 ["COPY", "register:0:8", ["register:4048:8"]]
- 004db294 ["INT_ADD", "register:40f0:8", ["const:4db294:8", "const:4:8"]]
- 004db294 ["CALLIND", null, ["register:0:8"]]
+ 004db2d4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004db2d4 ["INT_ADD", "register:40f0:8", ["const:4db2d4:8", "const:4:8"]]
+ 004db2d4 ["CALLIND", null, ["register:0:8"]]
- 004db294 bytes 20013fd6
+ 004db2d4 bytes 20013fd6
- 004db2c0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004db2c0 ["INT_ADD", "register:40f0:8", ["const:4db2c0:8", "const:4:8"]]
- 004db2c0 ["CALLIND", null, ["register:0:8"]]
+ 004db300 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004db300 ["INT_ADD", "register:40f0:8", ["const:4db300:8", "const:4:8"]]
+ 004db300 ["CALLIND", null, ["register:0:8"]]
- 004db2c0 bytes 20013fd6
+ 004db300 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb29eb43c0f98e2c92f0db9c856f1329"></a>

### [`004db660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004db660.md) → [`004db6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004db/004db6a0.md) _ZN5Botan7mul_addERKNS_6BigIntES2_S2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58f70.md) · 呼出先 12件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004b8810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8810.md) [`004d6b84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d6/004d6b84.md) [`004d6e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d6/004d6e28.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md)
- 新版 呼出元 1件 [`00c59370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59370.md) · 呼出先 12件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004b8850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8850.md) [`004d6bc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d6/004d6bc4.md) [`004d6e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d6/004d6e68.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.70% / 新版 98.70%

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
      "definition_site": "004db878",
      "incomplete_value": true,
      "site": "004db878",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004db8bc",
      "incomplete_value": false,
      "site": "004db8c4",
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
            "const:c56:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004db8f4",
      "incomplete_value": true,
      "site": "004db900",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004db8b4",
      "incomplete_value": true,
      "site": "004db8c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004db868",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004db8bc",
      "PARAM",
      [
        "storage",
        "002a8b89",
        null,
        "string"
      ]
    ],
    [
      "004db8f0",
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
      "004db868",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004db8bc",
      "PARAM",
      [
        "storage",
        "002a8c56",
        null,
        "string"
      ]
    ],
    [
      "004db8f0",
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

- 旧版 [`004db838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004db660.md#insn-004db838) · [`004db884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004db660.md#insn-004db884) · [`004db8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004db660.md#insn-004db8c0)
- 新版 `004db878`（命令位置の公開資料なし） · `004db8c4`（命令位置の公開資料なし） · `004db900`（命令位置の公開資料なし）

~~~diff
- 004db838 ["COPY", "register:0:8", ["register:4048:8"]]
- 004db838 ["INT_ADD", "register:40f0:8", ["const:4db838:8", "const:4:8"]]
- 004db838 ["CALLIND", null, ["register:0:8"]]
+ 004db878 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004db878 ["INT_ADD", "register:40f0:8", ["const:4db878:8", "const:4:8"]]
+ 004db878 ["CALLIND", null, ["register:0:8"]]
- 004db838 bytes 20013fd6
+ 004db878 bytes 20013fd6
- 004db884 ["INT_ADD", "register:40f0:8", ["const:4db884:8", "const:4:8"]]
- 004db884 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004db8c4 ["INT_ADD", "register:40f0:8", ["const:4db8c4:8", "const:4:8"]]
+ 004db8c4 ["CALL", null, ["callee:0043ddd8:8"]]
- 004db884 bytes 4589fd97
+ 004db8c4 bytes 4589fd97
- 004db8c0 ["INT_ADD", "register:40f0:8", ["const:4db8c0:8", "const:4:8"]]
- 004db8c0 ["CALL", null, ["callee:00c57f10:8"]]
+ 004db900 ["INT_ADD", "register:40f0:8", ["const:4db900:8", "const:4:8"]]
+ 004db900 ["CALL", null, ["callee:00c57f10:8"]]
- 004db8c0 bytes 94f01d94
+ 004db900 bytes 84f11d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-230d6860fa3d1aae25d64cc39c685506"></a>

### [`004db938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004db938.md) → [`004db978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004db/004db978.md) _ZN5Botan7sub_mulERKNS_6BigIntES2_S2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58f80.md) · 呼出先 9件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`00c59380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59380.md) · 呼出先 9件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.43% / 新版 96.43%

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
      "definition_site": "004dba0c",
      "incomplete_value": false,
      "site": "004dba14",
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
            "const:455:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004dba44",
      "incomplete_value": true,
      "site": "004dba50",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004dba40",
      "incomplete_value": false,
      "site": "004dba50",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004dba00",
      "incomplete_value": false,
      "site": "004dba10",
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
      "004dba0c",
      "PARAM",
      [
        "storage",
        "002ab415",
        null,
        "string"
      ]
    ],
    [
      "004dba40",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004dba44",
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
      "004dba0c",
      "PARAM",
      [
        "storage",
        "002ab455",
        null,
        "string"
      ]
    ],
    [
      "004dba40",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004dba44",
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

- 旧版 [`004db994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004db938.md#insn-004db994) · [`004db9d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004db938.md#insn-004db9d4) · [`004dba10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004db938.md#insn-004dba10)
- 新版 `004db9d4`（命令位置の公開資料なし） · `004dba14`（命令位置の公開資料なし） · `004dba50`（命令位置の公開資料なし）

~~~diff
- 004db994 ["INT_ADD", "register:40f0:8", ["const:4db994:8", "const:4:8"]]
- 004db994 ["CALL", null, ["callee:00c58ac0:8"]]
+ 004db9d4 ["INT_ADD", "register:40f0:8", ["const:4db9d4:8", "const:4:8"]]
+ 004db9d4 ["CALL", null, ["callee:00c58ac0:8"]]
- 004db994 bytes 4bf31d94
+ 004db9d4 bytes 3bf41d94
- 004db9d4 ["INT_ADD", "register:40f0:8", ["const:4db9d4:8", "const:4:8"]]
- 004db9d4 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004dba14 ["INT_ADD", "register:40f0:8", ["const:4dba14:8", "const:4:8"]]
+ 004dba14 ["CALL", null, ["callee:0043ddd8:8"]]
- 004db9d4 bytes f188fd97
+ 004dba14 bytes f188fd97
- 004dba10 ["INT_ADD", "register:40f0:8", ["const:4dba10:8", "const:4:8"]]
- 004dba10 ["CALL", null, ["callee:00c57f10:8"]]
+ 004dba50 ["INT_ADD", "register:40f0:8", ["const:4dba50:8", "const:4:8"]]
+ 004dba50 ["CALL", null, ["callee:00c57f10:8"]]
- 004dba10 bytes 40f01d94
+ 004dba50 bytes 30f11d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8b99b74db4efa5d042f67c91de7b1f0"></a>

### [`004dba70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004dba70.md) → [`004dbab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004db/004dbab0.md) _ZN5Botan7mul_subERKNS_6BigIntES2_S2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
      "definition_site": "004dbb34",
      "incomplete_value": false,
      "site": "004dbb3c",
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
            "const:91f:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004dbb6c",
      "incomplete_value": true,
      "site": "004dbb78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004dbb68",
      "incomplete_value": false,
      "site": "004dbb78",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004dbb28",
      "incomplete_value": false,
      "site": "004dbb38",
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
      "004dbb34",
      "PARAM",
      [
        "storage",
        "002bd8df",
        null,
        "string"
      ]
    ],
    [
      "004dbb68",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004dbb6c",
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
      "004dbb34",
      "PARAM",
      [
        "storage",
        "002bd91f",
        null,
        "string"
      ]
    ],
    [
      "004dbb68",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004dbb6c",
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

- 旧版 [`004dbafc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004dba70.md#insn-004dbafc) · [`004dbb38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004dba70.md#insn-004dbb38) · [`004dbae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004dba70.md#insn-004dbae8)
- 新版 `004dbb3c`（命令位置の公開資料なし） · `004dbb78`（命令位置の公開資料なし） · `004dbb28`（命令位置の公開資料なし）

~~~diff
- 004dbafc ["INT_ADD", "register:40f0:8", ["const:4dbafc:8", "const:4:8"]]
- 004dbafc ["CALL", null, ["callee:0043ddd8:8"]]
+ 004dbb3c ["INT_ADD", "register:40f0:8", ["const:4dbb3c:8", "const:4:8"]]
+ 004dbb3c ["CALL", null, ["callee:0043ddd8:8"]]
- 004dbafc bytes a788fd97
+ 004dbb3c bytes a788fd97
- 004dbb38 ["INT_ADD", "register:40f0:8", ["const:4dbb38:8", "const:4:8"]]
- 004dbb38 ["CALL", null, ["callee:00c57f10:8"]]
+ 004dbb78 ["INT_ADD", "register:40f0:8", ["const:4dbb78:8", "const:4:8"]]
+ 004dbb78 ["CALL", null, ["callee:00c57f10:8"]]
- 004dbb38 bytes f6ef1d94
+ 004dbb78 bytes e6f01d94
- 004dbae8 ["INT_ADD", "register:40f0:8", ["const:4dbae8:8", "const:4:8"]]
- 004dbae8 ["CALL", null, ["callee:00c57ef0:8"]]
+ 004dbb28 ["INT_ADD", "register:40f0:8", ["const:4dbb28:8", "const:4:8"]]
+ 004dbb28 ["CALL", null, ["callee:00c57ef0:8"]]
- 004dbae8 bytes 02f01d94
+ 004dbb28 bytes f2f01d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-284ec9582ed41e5183061be5be372c30"></a>

### [`004dbbdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004dbbdc.md) → [`004dbc1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004db/004dbc1c.md) _ZN5Botan3lcmERKNS_6BigIntES2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58f90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58f90.md) · 呼出先 6件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58850.md) [`00c58890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58890.md) [`00c58f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58f60.md)
- 新版 呼出元 1件 [`00c59390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59390.md) · 呼出先 6件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c58c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58c50.md) [`00c58c90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58c90.md) [`00c59360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59360.md)

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
      "definition_site": "004dbc94",
      "incomplete_value": true,
      "site": "004dbc94",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004dbcc0",
      "incomplete_value": true,
      "site": "004dbcc0",
      "value": [
        "LOAD",
        "8",
        [
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
      "004dbc84",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004dbcb0",
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
      "004dbc84",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004dbcb0",
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

- 旧版 [`004dbc54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004dbbdc.md#insn-004dbc54) · [`004dbc80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004dbbdc.md#insn-004dbc80) · [`004dbc0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004dbbdc.md#insn-004dbc0c)
- 新版 `004dbc94`（命令位置の公開資料なし） · `004dbcc0`（命令位置の公開資料なし） · `004dbc4c`（命令位置の公開資料なし）

~~~diff
- 004dbc54 ["COPY", "register:0:8", ["register:4048:8"]]
- 004dbc54 ["INT_ADD", "register:40f0:8", ["const:4dbc54:8", "const:4:8"]]
- 004dbc54 ["CALLIND", null, ["register:0:8"]]
+ 004dbc94 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004dbc94 ["INT_ADD", "register:40f0:8", ["const:4dbc94:8", "const:4:8"]]
+ 004dbc94 ["CALLIND", null, ["register:0:8"]]
- 004dbc54 bytes 20013fd6
+ 004dbc94 bytes 20013fd6
- 004dbc80 ["COPY", "register:0:8", ["register:4048:8"]]
- 004dbc80 ["INT_ADD", "register:40f0:8", ["const:4dbc80:8", "const:4:8"]]
- 004dbc80 ["CALLIND", null, ["register:0:8"]]
+ 004dbcc0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004dbcc0 ["INT_ADD", "register:40f0:8", ["const:4dbcc0:8", "const:4:8"]]
+ 004dbcc0 ["CALLIND", null, ["register:0:8"]]
- 004dbc80 bytes 20013fd6
+ 004dbcc0 bytes 20013fd6
- 004dbc0c ["INT_ADD", "register:40f0:8", ["const:4dbc0c:8", "const:4:8"]]
- 004dbc0c ["CALL", null, ["callee:00c58c50:8"]]
+ 004dbc4c ["INT_ADD", "register:40f0:8", ["const:4dbc4c:8", "const:4:8"]]
+ 004dbc4c ["CALL", null, ["callee:00c58c50:8"]]
- 004dbc0c bytes 11f31d94
+ 004dbc4c bytes 01f41d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-282777cec163ac855f3c6c5e4cee6e19"></a>

### [`004dbcf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004dbcf0.md) → [`004dbd30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004db/004dbd30.md) _ZN5Botan25almost_montgomery_inverseERNS_6BigIntERKS0_S3_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c58fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58fa0.md) · 呼出先 10件 [`005408e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005408e0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58520.md) [`00c586d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c586d0.md)
- 新版 呼出元 1件 [`00c593a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c593a0.md) · 呼出先 10件 [`00540920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540920.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c58920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58920.md) [`00c58ad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58ad0.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.35% / 新版 97.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004dbdf0",
      "incomplete_value": true,
      "site": "004dbdf0",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
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
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004dc4a0",
      "incomplete_value": true,
      "site": "004dc4a0",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "004dc460",
      "incomplete_value": true,
      "site": "004dc460",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 19,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004dc518",
      "incomplete_value": true,
      "site": "004dc518",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "004dc4d8",
      "incomplete_value": true,
      "site": "004dc4d8",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 22,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004dbde0",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004dc494",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004dc508",
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
      "004dbde0",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004dc494",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004dc508",
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

- 旧版 [`004dbdb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004dbcf0.md#insn-004dbdb0) · [`004dc460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004dbcf0.md#insn-004dc460) · [`004dc4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004dbcf0.md#insn-004dc4d8)
- 新版 `004dbdf0`（命令位置の公開資料なし） · `004dc4a0`（命令位置の公開資料なし） · `004dc518`（命令位置の公開資料なし）

~~~diff
- 004dbdb0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004dbdb0 ["INT_ADD", "register:40f0:8", ["const:4dbdb0:8", "const:4:8"]]
- 004dbdb0 ["CALLIND", null, ["register:0:8"]]
+ 004dbdf0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004dbdf0 ["INT_ADD", "register:40f0:8", ["const:4dbdf0:8", "const:4:8"]]
+ 004dbdf0 ["CALLIND", null, ["register:0:8"]]
- 004dbdb0 bytes 20013fd6
+ 004dbdf0 bytes 20013fd6
- 004dc460 ["COPY", "register:0:8", ["register:4048:8"]]
- 004dc460 ["INT_ADD", "register:40f0:8", ["const:4dc460:8", "const:4:8"]]
- 004dc460 ["CALLIND", null, ["register:0:8"]]
+ 004dc4a0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004dc4a0 ["INT_ADD", "register:40f0:8", ["const:4dc4a0:8", "const:4:8"]]
+ 004dc4a0 ["CALLIND", null, ["register:0:8"]]
- 004dc460 bytes 20013fd6
+ 004dc4a0 bytes 20013fd6
- 004dc4d8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004dc4d8 ["INT_ADD", "register:40f0:8", ["const:4dc4d8:8", "const:4:8"]]
- 004dc4d8 ["CALLIND", null, ["register:0:8"]]
+ 004dc518 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004dc518 ["INT_ADD", "register:40f0:8", ["const:4dc518:8", "const:4:8"]]
+ 004dc518 ["CALLIND", null, ["register:0:8"]]
- 004dc4d8 bytes 20013fd6
+ 004dc518 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-973a6371141ba12c19b4f127ac2f1fe0"></a>

### [`004dc7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004dc/004dc7e0.md) → [`004dc820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004dc/004dc820.md) _ZN5Botan26ct_inverse_mod_odd_modulusERKNS_6BigIntES2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58fb0.md) · 呼出先 16件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004ac0e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ac/004ac0e4.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`005408e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005408e0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00c593b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c593b0.md) · 呼出先 16件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004ac124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ac/004ac124.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00540920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540920.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.28% / 新版 95.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `call_target` 9件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004dc8d0",
      "incomplete_value": true,
      "site": "004dc8d0",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004dc92c",
      "incomplete_value": true,
      "site": "004dc92c",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 7,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004dc958",
      "incomplete_value": true,
      "site": "004dc958",
      "value": [
        "LOAD",
        "8",
        [
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
      "004dc8c0",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004dc91c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004dc948",
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
      "004dc8c0",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004dc91c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004dc948",
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

- 旧版 [`004dc890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004dc/004dc7e0.md#insn-004dc890) · [`004dc8ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004dc/004dc7e0.md#insn-004dc8ec) · [`004dc918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004dc/004dc7e0.md#insn-004dc918)
- 新版 `004dc8d0`（命令位置の公開資料なし） · `004dc92c`（命令位置の公開資料なし） · `004dc958`（命令位置の公開資料なし）

~~~diff
- 004dc890 ["COPY", "register:0:8", ["register:4048:8"]]
- 004dc890 ["INT_ADD", "register:40f0:8", ["const:4dc890:8", "const:4:8"]]
- 004dc890 ["CALLIND", null, ["register:0:8"]]
+ 004dc8d0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004dc8d0 ["INT_ADD", "register:40f0:8", ["const:4dc8d0:8", "const:4:8"]]
+ 004dc8d0 ["CALLIND", null, ["register:0:8"]]
- 004dc890 bytes 20013fd6
+ 004dc8d0 bytes 20013fd6
- 004dc8ec ["COPY", "register:0:8", ["register:4048:8"]]
- 004dc8ec ["INT_ADD", "register:40f0:8", ["const:4dc8ec:8", "const:4:8"]]
- 004dc8ec ["CALLIND", null, ["register:0:8"]]
+ 004dc92c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004dc92c ["INT_ADD", "register:40f0:8", ["const:4dc92c:8", "const:4:8"]]
+ 004dc92c ["CALLIND", null, ["register:0:8"]]
- 004dc8ec bytes 20013fd6
+ 004dc92c bytes 20013fd6
- 004dc918 ["COPY", "register:0:8", ["register:4048:8"]]
- 004dc918 ["INT_ADD", "register:40f0:8", ["const:4dc918:8", "const:4:8"]]
- 004dc918 ["CALLIND", null, ["register:0:8"]]
+ 004dc958 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004dc958 ["INT_ADD", "register:40f0:8", ["const:4dc958:8", "const:4:8"]]
+ 004dc958 ["CALLIND", null, ["register:0:8"]]
- 004dc918 bytes 20013fd6
+ 004dc958 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e9be5435f197467f239b7b6786275a2"></a>

### [`004dd2c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004dd/004dd2c8.md) → [`004dd308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004dd/004dd308.md) _ZN5Botan11inverse_modERKNS_6BigIntES2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58fc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58fc0.md) · 呼出先 15件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004b9bf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b9bf8.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 1件 [`00c593c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c593c0.md) · 呼出先 15件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004b9c38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b9/004b9c38.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.19% / 新版 97.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 7件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004dd3cc",
      "incomplete_value": true,
      "site": "004dd3d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004dd3f0",
      "incomplete_value": true,
      "site": "004dd3f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
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
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004dd3ec",
      "incomplete_value": false,
      "site": "004dd3f4",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004dd3ac",
      "incomplete_value": false,
      "site": "004dd3b4",
      "value": [
        "leaf",
        "const:535828:8"
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
      "004dd3b8",
      "READ",
      [
        "storage",
        "00c9aa00",
        null,
        "pointer"
      ]
    ],
    [
      "004dd3d0",
      "DATA",
      [
        "storage",
        "00c69860",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004dd3ec",
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
      "004dd3b8",
      "READ",
      [
        "storage",
        "00c9ae00",
        null,
        "pointer"
      ]
    ],
    [
      "004dd3d0",
      "DATA",
      [
        "storage",
        "00c69c60",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004dd3ec",
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

- 旧版 [`004dd3b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004dd/004dd2c8.md#insn-004dd3b4) · [`004ddbe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004dd/004dd2c8.md#insn-004ddbe4) · [`004ddc20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004dd/004dd2c8.md#insn-004ddc20)
- 新版 `004dd3f4`（命令位置の公開資料なし） · `004ddc24`（命令位置の公開資料なし） · `004ddc60`（命令位置の公開資料なし）

~~~diff
- 004dd3b4 ["INT_ADD", "register:40f0:8", ["const:4dd3b4:8", "const:4:8"]]
- 004dd3b4 ["CALL", null, ["callee:00c57f10:8"]]
+ 004dd3f4 ["INT_ADD", "register:40f0:8", ["const:4dd3f4:8", "const:4:8"]]
+ 004dd3f4 ["CALL", null, ["callee:00c57f10:8"]]
- 004dd3b4 bytes d7e91d94
+ 004dd3f4 bytes c7ea1d94
- 004ddbe4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004ddbe4 ["INT_ADD", "register:40f0:8", ["const:4ddbe4:8", "const:4:8"]]
- 004ddbe4 ["CALLIND", null, ["register:0:8"]]
+ 004ddc24 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004ddc24 ["INT_ADD", "register:40f0:8", ["const:4ddc24:8", "const:4:8"]]
+ 004ddc24 ["CALLIND", null, ["register:0:8"]]
- 004ddbe4 bytes 20013fd6
+ 004ddc24 bytes 20013fd6
- 004ddc20 ["COPY", "register:0:8", ["register:4048:8"]]
- 004ddc20 ["INT_ADD", "register:40f0:8", ["const:4ddc20:8", "const:4:8"]]
- 004ddc20 ["CALLIND", null, ["register:0:8"]]
+ 004ddc60 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004ddc60 ["INT_ADD", "register:40f0:8", ["const:4ddc60:8", "const:4:8"]]
+ 004ddc60 ["CALLIND", null, ["register:0:8"]]
- 004ddc20 bytes 20013fd6
+ 004ddc60 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5c94a860b67c9eb32a9d669e88abdf5"></a>

### [`004ddec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004dd/004ddec8.md) → [`004ddf08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004dd/004ddf08.md) _ZN5Botan13monty_inverseEj

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58fd0.md) · 呼出先 8件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004bbb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bbb2c.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 1件 [`00c593d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c593d0.md) · 呼出先 8件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004bbb6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bbb6c.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

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
      "definition_site": "004ddfc4",
      "incomplete_value": false,
      "site": "004ddfcc",
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
            "const:843:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004de000",
      "incomplete_value": true,
      "site": "004de00c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ddffc",
      "incomplete_value": false,
      "site": "004de00c",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004ddfbc",
      "incomplete_value": false,
      "site": "004ddfcc",
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
      "004ddfc4",
      "PARAM",
      [
        "storage",
        "002a7767",
        null,
        "string"
      ]
    ],
    [
      "004ddffc",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004de000",
      "READ",
      [
        "storage",
        "00c9a988",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ddfc4",
      "PARAM",
      [
        "storage",
        "002a7843",
        null,
        "string"
      ]
    ],
    [
      "004ddffc",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004de000",
      "READ",
      [
        "storage",
        "00c9ad88",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ddf8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004dd/004ddec8.md#insn-004ddf8c) · [`004ddfcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004dd/004ddec8.md#insn-004ddfcc) · [`004de004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004dd/004ddec8.md#insn-004de004)
- 新版 `004ddfcc`（命令位置の公開資料なし） · `004de00c`（命令位置の公開資料なし） · `004de044`（命令位置の公開資料なし）

~~~diff
- 004ddf8c ["INT_ADD", "register:40f0:8", ["const:4ddf8c:8", "const:4:8"]]
- 004ddf8c ["CALL", null, ["callee:0043ddd8:8"]]
+ 004ddfcc ["INT_ADD", "register:40f0:8", ["const:4ddfcc:8", "const:4:8"]]
+ 004ddfcc ["CALL", null, ["callee:0043ddd8:8"]]
- 004ddf8c bytes 837ffd97
+ 004ddfcc bytes 837ffd97
- 004ddfcc ["INT_ADD", "register:40f0:8", ["const:4ddfcc:8", "const:4:8"]]
- 004ddfcc ["CALL", null, ["callee:00c57f10:8"]]
+ 004de00c ["INT_ADD", "register:40f0:8", ["const:4de00c:8", "const:4:8"]]
+ 004de00c ["CALL", null, ["callee:00c57f10:8"]]
- 004ddfcc bytes d1e61d94
+ 004de00c bytes c1e71d94
- 004de004 ["INT_ADD", "register:40f0:8", ["const:4de004:8", "const:4:8"]]
- 004de004 ["CALL", null, ["callee:00c58650:8"]]
+ 004de044 ["INT_ADD", "register:40f0:8", ["const:4de044:8", "const:4:8"]]
+ 004de044 ["CALL", null, ["callee:00c58650:8"]]
- 004de004 bytes 93e81d94
+ 004de044 bytes 83e91d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4fc0f68c89750c5bd007386df340a6d9"></a>

### [`004de288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de288.md) → [`004de2c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004de/004de2c8.md) _ZNK5Botan9Power_Mod8set_baseERKNS_6BigIntE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58ef0.md) · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`00c592f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c592f0.md) · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
      "definition_site": "004de338",
      "incomplete_value": false,
      "site": "004de340",
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
            "const:616:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004de374",
      "incomplete_value": true,
      "site": "004de380",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004de370",
      "incomplete_value": false,
      "site": "004de380",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004de330",
      "incomplete_value": false,
      "site": "004de340",
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
      "004de338",
      "PARAM",
      [
        "storage",
        "002a653a",
        null,
        "string"
      ]
    ],
    [
      "004de370",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004de374",
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
      "004de338",
      "PARAM",
      [
        "storage",
        "002a6616",
        null,
        "string"
      ]
    ],
    [
      "004de370",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004de374",
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

- 旧版 [`004de300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de288.md#insn-004de300) · [`004de340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de288.md#insn-004de340) · [`004de3a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de288.md#insn-004de3a0)
- 新版 `004de340`（命令位置の公開資料なし） · `004de380`（命令位置の公開資料なし） · `004de3e0`（命令位置の公開資料なし）

~~~diff
- 004de300 ["INT_ADD", "register:40f0:8", ["const:4de300:8", "const:4:8"]]
- 004de300 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004de340 ["INT_ADD", "register:40f0:8", ["const:4de340:8", "const:4:8"]]
+ 004de340 ["CALL", null, ["callee:0043ddd8:8"]]
- 004de300 bytes a67efd97
+ 004de340 bytes a67efd97
- 004de340 ["INT_ADD", "register:40f0:8", ["const:4de340:8", "const:4:8"]]
- 004de340 ["CALL", null, ["callee:00c57f10:8"]]
+ 004de380 ["INT_ADD", "register:40f0:8", ["const:4de380:8", "const:4:8"]]
+ 004de380 ["CALL", null, ["callee:00c57f10:8"]]
- 004de340 bytes f4e51d94
+ 004de380 bytes e4e61d94
- 004de3a0 ["INT_ADD", "register:40f0:8", ["const:4de3a0:8", "const:4:8"]]
- 004de3a0 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004de3e0 ["INT_ADD", "register:40f0:8", ["const:4de3e0:8", "const:4:8"]]
+ 004de3e0 ["CALL", null, ["callee:0043ddd8:8"]]
- 004de3a0 bytes 7e7efd97
+ 004de3e0 bytes 7e7efd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21319ce78d61cb737ad9c12d87ee1056"></a>

### [`004de434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de434.md) → [`004de474`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004de/004de474.md) _ZNK5Botan9Power_Mod12set_exponentERKNS_6BigIntE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59000.md) · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`00c59400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59400.md) · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
      "definition_site": "004de4e4",
      "incomplete_value": false,
      "site": "004de4ec",
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
            "const:d85:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004de520",
      "incomplete_value": true,
      "site": "004de52c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004de51c",
      "incomplete_value": false,
      "site": "004de52c",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004de4dc",
      "incomplete_value": false,
      "site": "004de4ec",
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
      "004de4e4",
      "PARAM",
      [
        "storage",
        "002bfd45",
        null,
        "string"
      ]
    ],
    [
      "004de51c",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004de520",
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
      "004de4e4",
      "PARAM",
      [
        "storage",
        "002bfd85",
        null,
        "string"
      ]
    ],
    [
      "004de51c",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004de520",
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

- 旧版 [`004de4ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de434.md#insn-004de4ac) · [`004de4ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de434.md#insn-004de4ec) · [`004de510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de434.md#insn-004de510)
- 新版 `004de4ec`（命令位置の公開資料なし） · `004de52c`（命令位置の公開資料なし） · `004de550`（命令位置の公開資料なし）

~~~diff
- 004de4ac ["INT_ADD", "register:40f0:8", ["const:4de4ac:8", "const:4:8"]]
- 004de4ac ["CALL", null, ["callee:0043ddd8:8"]]
+ 004de4ec ["INT_ADD", "register:40f0:8", ["const:4de4ec:8", "const:4:8"]]
+ 004de4ec ["CALL", null, ["callee:0043ddd8:8"]]
- 004de4ac bytes 3b7efd97
+ 004de4ec bytes 3b7efd97
- 004de4ec ["INT_ADD", "register:40f0:8", ["const:4de4ec:8", "const:4:8"]]
- 004de4ec ["CALL", null, ["callee:00c57f10:8"]]
+ 004de52c ["INT_ADD", "register:40f0:8", ["const:4de52c:8", "const:4:8"]]
+ 004de52c ["CALL", null, ["callee:00c57f10:8"]]
- 004de4ec bytes 89e51d94
+ 004de52c bytes 79e61d94
- 004de510 ["INT_ADD", "register:40f0:8", ["const:4de510:8", "const:4:8"]]
- 004de510 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004de550 ["INT_ADD", "register:40f0:8", ["const:4de550:8", "const:4:8"]]
+ 004de550 ["CALL", null, ["callee:0043ddd8:8"]]
- 004de510 bytes 227efd97
+ 004de550 bytes 227efd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7bf07f6b9d5e178186c244dea3bd3133"></a>

### [`004de5a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de5a4.md) → [`004de5e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004de/004de5e4.md) _ZNK5Botan9Power_Mod7executeEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58f00.md) · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`00c59300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59300.md) · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
      "definition_site": "004de64c",
      "incomplete_value": false,
      "site": "004de654",
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
            "const:faf:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004de688",
      "incomplete_value": true,
      "site": "004de694",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:df8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004de684",
      "incomplete_value": false,
      "site": "004de694",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004de644",
      "incomplete_value": false,
      "site": "004de654",
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
      "004de64c",
      "PARAM",
      [
        "storage",
        "002a1ee2",
        null,
        "string"
      ]
    ],
    [
      "004de684",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004de688",
      "READ",
      [
        "storage",
        "00c9a9f8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004de64c",
      "PARAM",
      [
        "storage",
        "002a1faf",
        null,
        "string"
      ]
    ],
    [
      "004de684",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004de688",
      "READ",
      [
        "storage",
        "00c9adf8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004de614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de5a4.md#insn-004de614) · [`004de654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de5a4.md#insn-004de654) · [`004de600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de5a4.md#insn-004de600)
- 新版 `004de654`（命令位置の公開資料なし） · `004de694`（命令位置の公開資料なし） · `004de640`（命令位置の公開資料なし）

~~~diff
- 004de614 ["INT_ADD", "register:40f0:8", ["const:4de614:8", "const:4:8"]]
- 004de614 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004de654 ["INT_ADD", "register:40f0:8", ["const:4de654:8", "const:4:8"]]
+ 004de654 ["CALL", null, ["callee:0043ddd8:8"]]
- 004de614 bytes e17dfd97
+ 004de654 bytes e17dfd97
- 004de654 ["INT_ADD", "register:40f0:8", ["const:4de654:8", "const:4:8"]]
- 004de654 ["CALL", null, ["callee:00c57f10:8"]]
+ 004de694 ["INT_ADD", "register:40f0:8", ["const:4de694:8", "const:4:8"]]
+ 004de694 ["CALL", null, ["callee:00c57f10:8"]]
- 004de654 bytes 2fe51d94
+ 004de694 bytes 1fe61d94
- 004de600 ["INT_ADD", "register:40f0:8", ["const:4de600:8", "const:4:8"]]
- 004de600 ["CALL", null, ["callee:00c57ef0:8"]]
+ 004de640 ["INT_ADD", "register:40f0:8", ["const:4de640:8", "const:4:8"]]
+ 004de640 ["CALL", null, ["callee:00c57ef0:8"]]
- 004de600 bytes 3ce51d94
+ 004de640 bytes 2ce61d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bacf0e45d4966844b88edb0aa1465c9e"></a>

### [`004de6a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de6a8.md) → [`004de6e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004de/004de6e8.md) FUN_004de6e8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 7件 [`00532e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532e3c.md) [`00532f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532f78.md) [`00537a6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00537/00537a6c.md) [`00539194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00539/00539194.md) [`0053924c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00539/0053924c.md) · 呼出先 2件 [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)
- 新版 呼出元 7件 [`00532e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532e7c.md) [`00532fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00532/00532fb8.md) [`00537aac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00537/00537aac.md) [`005391d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00539/005391d4.md) [`0053928c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00539/0053928c.md) · 呼出先 2件 [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)

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
      "definition_site": "004de720",
      "incomplete_value": true,
      "site": "004de720",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004de74c",
      "incomplete_value": true,
      "site": "004de74c",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004de778",
      "incomplete_value": true,
      "site": "004de778",
      "value": [
        "LOAD",
        "8",
        [
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
      "004de710",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004de73c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004de768",
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
      "004de710",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004de73c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004de768",
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

- 旧版 [`004de6e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de6a8.md#insn-004de6e0) · [`004de70c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de6a8.md#insn-004de70c) · [`004de738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de6a8.md#insn-004de738)
- 新版 `004de720`（命令位置の公開資料なし） · `004de74c`（命令位置の公開資料なし） · `004de778`（命令位置の公開資料なし）

~~~diff
- 004de6e0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004de6e0 ["INT_ADD", "register:40f0:8", ["const:4de6e0:8", "const:4:8"]]
- 004de6e0 ["CALLIND", null, ["register:0:8"]]
+ 004de720 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004de720 ["INT_ADD", "register:40f0:8", ["const:4de720:8", "const:4:8"]]
+ 004de720 ["CALLIND", null, ["register:0:8"]]
- 004de6e0 bytes 20013fd6
+ 004de720 bytes 20013fd6
- 004de70c ["COPY", "register:0:8", ["register:4048:8"]]
- 004de70c ["INT_ADD", "register:40f0:8", ["const:4de70c:8", "const:4:8"]]
- 004de70c ["CALLIND", null, ["register:0:8"]]
+ 004de74c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004de74c ["INT_ADD", "register:40f0:8", ["const:4de74c:8", "const:4:8"]]
+ 004de74c ["CALLIND", null, ["register:0:8"]]
- 004de70c bytes 20013fd6
+ 004de74c bytes 20013fd6
- 004de738 ["COPY", "register:0:8", ["register:4048:8"]]
- 004de738 ["INT_ADD", "register:40f0:8", ["const:4de738:8", "const:4:8"]]
- 004de738 ["CALLIND", null, ["register:0:8"]]
+ 004de778 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004de778 ["INT_ADD", "register:40f0:8", ["const:4de778:8", "const:4:8"]]
+ 004de778 ["CALLIND", null, ["register:0:8"]]
- 004de738 bytes 20013fd6
+ 004de778 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0ae91df9cf7d0271611f17200f17e75"></a>

### [`004de76c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de76c.md) → [`004de7ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004de/004de7ac.md) _ZN5Botan9Power_ModC2ERKNS_6BigIntENS0_11Usage_HintsEb

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58ff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58ff0.md) · 呼出先 1件 [`00c59010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59010.md)
- 新版 呼出元 1件 [`00c593f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c593f0.md) · 呼出先 1件 [`00c59410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59410.md)

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
      "definition_site": "004de7c8",
      "incomplete_value": true,
      "site": "004de7c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
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
      "004de7c0",
      "READ",
      [
        "storage",
        "00c9abb0",
        null,
        "pointer"
      ]
    ],
    [
      "004de7c8",
      "DATA",
      [
        "storage",
        "00c66958",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      "004de7c0",
      "READ",
      [
        "storage",
        "00c9afb0",
        null,
        "pointer"
      ]
    ],
    [
      "004de7c8",
      "DATA",
      [
        "storage",
        "00c66d58",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004de780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de76c.md#insn-004de780) · [`004de78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de76c.md#insn-004de78c)
- 新版 `004de7c0`（命令位置の公開資料なし） · `004de7cc`（命令位置の公開資料なし）

~~~diff
- 004de780 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bb0:8"]]
- 004de780 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004de7c0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fb0:8"]]
+ 004de7c0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004de780 bytes 08d945f9
+ 004de7c0 bytes 08d947f9
- 004de78c ["INT_ADD", "register:40f0:8", ["const:4de78c:8", "const:4:8"]]
- 004de78c ["CALL", null, ["callee:00c59410:8"]]
+ 004de7cc ["INT_ADD", "register:40f0:8", ["const:4de7cc:8", "const:4:8"]]
+ 004de7cc ["CALL", null, ["callee:00c59410:8"]]
- 004de78c bytes 21ea1d94
+ 004de7cc bytes 11eb1d94
~~~


<a id="compare-95ee3d38ad74ee53a941167ae9f1c81a"></a>

### [`004de7c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de7c0.md) → [`004de800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004de/004de800.md) _ZNK5Botan9Power_Mod11set_modulusERKNS_6BigIntENS0_11Usage_HintsEb

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59010.md) · 呼出先 8件 [`004e076c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e0/004e076c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58520.md)
- 新版 呼出元 1件 [`00c59410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59410.md) · 呼出先 8件 [`004e07ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e0/004e07ac.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c58920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58920.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.75% / 新版 97.75%

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
      "definition_site": "004de8f8",
      "incomplete_value": false,
      "site": "004de8f8",
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
            "const:db8:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004de894",
      "incomplete_value": true,
      "site": "004de894",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004de884",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004de8f8",
      "DATA",
      [
        "storage",
        "00c669b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004de884",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004de8f8",
      "DATA",
      [
        "storage",
        "00c66db8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004de854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de7c0.md#insn-004de854) · [`004de80c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de7c0.md#insn-004de80c) · [`004de818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de7c0.md#insn-004de818)
- 新版 `004de894`（命令位置の公開資料なし） · `004de84c`（命令位置の公開資料なし） · `004de858`（命令位置の公開資料なし）

~~~diff
- 004de854 ["COPY", "register:0:8", ["register:4048:8"]]
- 004de854 ["INT_ADD", "register:40f0:8", ["const:4de854:8", "const:4:8"]]
- 004de854 ["CALLIND", null, ["register:0:8"]]
+ 004de894 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004de894 ["INT_ADD", "register:40f0:8", ["const:4de894:8", "const:4:8"]]
+ 004de894 ["CALLIND", null, ["register:0:8"]]
- 004de854 bytes 20013fd6
+ 004de894 bytes 20013fd6
- 004de80c ["COPY", "register:0:8", ["register:4040:8"]]
- 004de80c ["INT_ADD", "register:40f0:8", ["const:4de80c:8", "const:4:8"]]
- 004de80c ["CALLIND", null, ["register:0:8"]]
+ 004de84c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004de84c ["INT_ADD", "register:40f0:8", ["const:4de84c:8", "const:4:8"]]
+ 004de84c ["CALLIND", null, ["register:0:8"]]
- 004de80c bytes 00013fd6
+ 004de84c bytes 00013fd6
- 004de818 ["INT_ADD", "register:40f0:8", ["const:4de818:8", "const:4:8"]]
- 004de818 ["CALL", null, ["callee:00c58920:8"]]
+ 004de858 ["INT_ADD", "register:40f0:8", ["const:4de858:8", "const:4:8"]]
+ 004de858 ["CALL", null, ["callee:00c58920:8"]]
- 004de818 bytes 42e71d94
+ 004de858 bytes 32e81d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-384edc59617b3579cf39a1a919e5b932"></a>

### [`004de950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de950.md) → [`004de990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004de/004de990.md) _ZN5Botan9Power_ModC1ERKS0_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "004de9b0",
      "incomplete_value": true,
      "site": "004de9b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
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
      "004de9a4",
      "READ",
      [
        "storage",
        "00c9abb0",
        null,
        "pointer"
      ]
    ],
    [
      "004de9b4",
      "DATA",
      [
        "storage",
        "00c66958",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      "004de9a4",
      "READ",
      [
        "storage",
        "00c9afb0",
        null,
        "pointer"
      ]
    ],
    [
      "004de9b4",
      "DATA",
      [
        "storage",
        "00c66d58",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004de964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de950.md#insn-004de964) · [`004de984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de950.md#insn-004de984)
- 新版 `004de9a4`（命令位置の公開資料なし） · `004de9c4`（命令位置の公開資料なし）

~~~diff
- 004de964 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bb0:8"]]
- 004de964 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004de9a4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fb0:8"]]
+ 004de9a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004de964 bytes 08d945f9
+ 004de9a4 bytes 08d947f9
- 004de984 ["COPY", "register:0:8", ["register:4040:8"]]
- 004de984 ["INT_ADD", "register:40f0:8", ["const:4de984:8", "const:4:8"]]
- 004de984 ["CALLIND", null, ["register:0:8"]]
+ 004de9c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004de9c4 ["INT_ADD", "register:40f0:8", ["const:4de9c4:8", "const:4:8"]]
+ 004de9c4 ["CALLIND", null, ["register:0:8"]]
- 004de984 bytes 00013fd6
+ 004de9c4 bytes 00013fd6
~~~


<a id="compare-47db9f9cb4ea3288e0a9a44347d38fc7"></a>

### [`004dec70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004dec70.md) → [`004decb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004de/004decb0.md) _ZN5Botan20Fixed_Base_Power_ModC2ERKNS_6BigIntES3_NS_9Power_Mod11Usage_HintsE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58520.md) [`00c58720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58720.md) [`00c58ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58ef0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c58920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58920.md) [`00c58b20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58b20.md) [`00c592f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c592f0.md)

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
      "definition_site": "004dee54",
      "incomplete_value": true,
      "site": "004dee54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004dee74",
      "incomplete_value": true,
      "site": "004dee78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004ded2c",
      "incomplete_value": true,
      "site": "004ded2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004ded1c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004dee4c",
      "READ",
      [
        "storage",
        "00c9abb0",
        null,
        "pointer"
      ]
    ],
    [
      "004dee54",
      "DATA",
      [
        "storage",
        "00c66958",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      "004ded1c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004dee4c",
      "READ",
      [
        "storage",
        "00c9afb0",
        null,
        "pointer"
      ]
    ],
    [
      "004dee54",
      "DATA",
      [
        "storage",
        "00c66d58",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004decec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004dec70.md#insn-004decec) · [`004decb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004dec70.md#insn-004decb0) · [`004decc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004dec70.md#insn-004decc0)
- 新版 `004ded2c`（命令位置の公開資料なし） · `004decf0`（命令位置の公開資料なし） · `004ded00`（命令位置の公開資料なし）

~~~diff
- 004decec ["COPY", "register:0:8", ["register:4048:8"]]
- 004decec ["INT_ADD", "register:40f0:8", ["const:4decec:8", "const:4:8"]]
- 004decec ["CALLIND", null, ["register:0:8"]]
+ 004ded2c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004ded2c ["INT_ADD", "register:40f0:8", ["const:4ded2c:8", "const:4:8"]]
+ 004ded2c ["CALLIND", null, ["register:0:8"]]
- 004decec bytes 20013fd6
+ 004ded2c bytes 20013fd6
- 004decb0 ["INT_ADD", "register:40f0:8", ["const:4decb0:8", "const:4:8"]]
- 004decb0 ["CALL", null, ["callee:00c58920:8"]]
+ 004decf0 ["INT_ADD", "register:40f0:8", ["const:4decf0:8", "const:4:8"]]
+ 004decf0 ["CALL", null, ["callee:00c58920:8"]]
- 004decb0 bytes 1ce61d94
+ 004decf0 bytes 0ce71d94
- 004decc0 ["INT_ADD", "register:40f0:8", ["const:4decc0:8", "const:4:8"]]
- 004decc0 ["CALL", null, ["callee:00c58b20:8"]]
+ 004ded00 ["INT_ADD", "register:40f0:8", ["const:4ded00:8", "const:4:8"]]
+ 004ded00 ["CALL", null, ["callee:00c58b20:8"]]
- 004decc0 bytes 98e61d94
+ 004ded00 bytes 88e71d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a26958788af65d2d90a3a1ab086408c8"></a>

### [`004def08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004def08.md) → [`004def48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004de/004def48.md) FUN_004def48

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`0054369c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/0054369c.md) [`00544e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544e1c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58520.md)
- 新版 呼出元 0件  · 呼出先 8件 [`005436dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/005436dc.md) [`00544e5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00544/00544e5c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c58920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58920.md)

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
      "definition_site": "004df0e0",
      "incomplete_value": true,
      "site": "004df0e0",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004df16c",
      "incomplete_value": true,
      "site": "004df16c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004df250",
      "incomplete_value": true,
      "site": "004df250",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
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
      "004df058",
      "READ",
      [
        "storage",
        "002cb0c0",
        null,
        "undefined8"
      ]
    ],
    [
      "004df058",
      "READ",
      [
        "storage",
        "002cb0b0",
        null,
        "undefined8"
      ]
    ],
    [
      "004df058",
      "READ",
      [
        "storage",
        "002cb0a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004df058",
      "READ",
      [
        "storage",
        "002cb110",
        null,
        "undefined8"
      ]
    ],
    [
      "004df058",
      "READ",
      [
        "storage",
        "002cb100",
        null,
        "undefined8"
      ]
    ],
    [
      "004df058",
      "READ",
      [
        "storage",
        "002cb0f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004df0a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004def08.md#insn-004df0a0) · [`004df12c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004def08.md#insn-004df12c) · [`004df210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004def08.md#insn-004df210)
- 新版 `004df0e0`（命令位置の公開資料なし） · `004df16c`（命令位置の公開資料なし） · `004df250`（命令位置の公開資料なし）

~~~diff
- 004df0a0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004df0a0 ["INT_ADD", "register:40f0:8", ["const:4df0a0:8", "const:4:8"]]
- 004df0a0 ["CALLIND", null, ["register:0:8"]]
+ 004df0e0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004df0e0 ["INT_ADD", "register:40f0:8", ["const:4df0e0:8", "const:4:8"]]
+ 004df0e0 ["CALLIND", null, ["register:0:8"]]
- 004df0a0 bytes 20013fd6
+ 004df0e0 bytes 20013fd6
- 004df12c ["COPY", "register:0:8", ["register:4048:8"]]
- 004df12c ["INT_ADD", "register:40f0:8", ["const:4df12c:8", "const:4:8"]]
- 004df12c ["CALLIND", null, ["register:0:8"]]
+ 004df16c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004df16c ["INT_ADD", "register:40f0:8", ["const:4df16c:8", "const:4:8"]]
+ 004df16c ["CALLIND", null, ["register:0:8"]]
- 004df12c bytes 20013fd6
+ 004df16c bytes 20013fd6
- 004df210 ["COPY", "register:0:8", ["register:4048:8"]]
- 004df210 ["INT_ADD", "register:40f0:8", ["const:4df210:8", "const:4:8"]]
- 004df210 ["CALLIND", null, ["register:0:8"]]
+ 004df250 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004df250 ["INT_ADD", "register:40f0:8", ["const:4df250:8", "const:4:8"]]
+ 004df250 ["CALLIND", null, ["register:0:8"]]
- 004df210 bytes 20013fd6
+ 004df250 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-419b5fdc3d20511711fe9f110dd58ee2"></a>

### [`004df2d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004df/004df2d8.md) → [`004df318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004df/004df318.md) FUN_004df318

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58520.md) [`00c58850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58850.md) [`00c58910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58910.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c58920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58920.md) [`00c58c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58c50.md) [`00c58d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58d10.md)

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
      "definition_site": "004df494",
      "incomplete_value": true,
      "site": "004df494",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004df4f8",
      "incomplete_value": true,
      "site": "004df4f8",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 7,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004df560",
      "incomplete_value": true,
      "site": "004df560",
      "value": [
        "LOAD",
        "8",
        [
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
      "004df484",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004df4e8",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004df550",
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
      "004df484",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004df4e8",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004df550",
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

- 旧版 [`004df454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004df/004df2d8.md#insn-004df454) · [`004df4b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004df/004df2d8.md#insn-004df4b8) · [`004df520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004df/004df2d8.md#insn-004df520)
- 新版 `004df494`（命令位置の公開資料なし） · `004df4f8`（命令位置の公開資料なし） · `004df560`（命令位置の公開資料なし）

~~~diff
- 004df454 ["COPY", "register:0:8", ["register:4048:8"]]
- 004df454 ["INT_ADD", "register:40f0:8", ["const:4df454:8", "const:4:8"]]
- 004df454 ["CALLIND", null, ["register:0:8"]]
+ 004df494 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004df494 ["INT_ADD", "register:40f0:8", ["const:4df494:8", "const:4:8"]]
+ 004df494 ["CALLIND", null, ["register:0:8"]]
- 004df454 bytes 20013fd6
+ 004df494 bytes 20013fd6
- 004df4b8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004df4b8 ["INT_ADD", "register:40f0:8", ["const:4df4b8:8", "const:4:8"]]
- 004df4b8 ["CALLIND", null, ["register:0:8"]]
+ 004df4f8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004df4f8 ["INT_ADD", "register:40f0:8", ["const:4df4f8:8", "const:4:8"]]
+ 004df4f8 ["CALLIND", null, ["register:0:8"]]
- 004df4b8 bytes 20013fd6
+ 004df4f8 bytes 20013fd6
- 004df520 ["COPY", "register:0:8", ["register:4048:8"]]
- 004df520 ["INT_ADD", "register:40f0:8", ["const:4df520:8", "const:4:8"]]
- 004df520 ["CALLIND", null, ["register:0:8"]]
+ 004df560 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004df560 ["INT_ADD", "register:40f0:8", ["const:4df560:8", "const:4:8"]]
+ 004df560 ["CALLIND", null, ["register:0:8"]]
- 004df520 bytes 20013fd6
+ 004df560 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-569bcb6b3eab9b475c726c377174b121"></a>

### [`004df69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004df/004df69c.md) → [`004df6dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004df/004df6dc.md) FUN_004df6dc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 12件 [`004b8810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8810.md) [`004d6e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d6/004d6e28.md) [`004d7b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7b2c.md) [`005408e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005408e0.md) [`0054369c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/0054369c.md)
- 新版 呼出元 0件  · 呼出先 12件 [`004b8850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8850.md) [`004d6e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d6/004d6e68.md) [`004d7b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d7/004d7b6c.md) [`00540920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540920.md) [`005436dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/005436dc.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.39% / 新版 98.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

アドレスに依存する影響 `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004df874",
      "incomplete_value": true,
      "site": "004df874",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004df92c",
      "incomplete_value": true,
      "site": "004df92c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004dfa78",
      "incomplete_value": true,
      "site": "004dfa78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004dfa38",
      "incomplete_value": true,
      "site": "004dfa38",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004df7f0",
      "READ",
      [
        "storage",
        "002cb0c0",
        null,
        "undefined8"
      ]
    ],
    [
      "004df7f0",
      "READ",
      [
        "storage",
        "002cb0b0",
        null,
        "undefined8"
      ]
    ],
    [
      "004df7f0",
      "READ",
      [
        "storage",
        "002cb0a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004df7f0",
      "READ",
      [
        "storage",
        "002cb110",
        null,
        "undefined8"
      ]
    ],
    [
      "004df7f0",
      "READ",
      [
        "storage",
        "002cb100",
        null,
        "undefined8"
      ]
    ],
    [
      "004df7f0",
      "READ",
      [
        "storage",
        "002cb0f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004df834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004df/004df69c.md#insn-004df834) · [`004df8ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004df/004df69c.md#insn-004df8ec) · [`004dfa38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004df/004df69c.md#insn-004dfa38)
- 新版 `004df874`（命令位置の公開資料なし） · `004df92c`（命令位置の公開資料なし） · `004dfa78`（命令位置の公開資料なし）

~~~diff
- 004df834 ["COPY", "register:0:8", ["register:4048:8"]]
- 004df834 ["INT_ADD", "register:40f0:8", ["const:4df834:8", "const:4:8"]]
- 004df834 ["CALLIND", null, ["register:0:8"]]
+ 004df874 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004df874 ["INT_ADD", "register:40f0:8", ["const:4df874:8", "const:4:8"]]
+ 004df874 ["CALLIND", null, ["register:0:8"]]
- 004df834 bytes 20013fd6
+ 004df874 bytes 20013fd6
- 004df8ec ["COPY", "register:0:8", ["register:4048:8"]]
- 004df8ec ["INT_ADD", "register:40f0:8", ["const:4df8ec:8", "const:4:8"]]
- 004df8ec ["CALLIND", null, ["register:0:8"]]
+ 004df92c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004df92c ["INT_ADD", "register:40f0:8", ["const:4df92c:8", "const:4:8"]]
+ 004df92c ["CALLIND", null, ["register:0:8"]]
- 004df8ec bytes 20013fd6
+ 004df92c bytes 20013fd6
- 004dfa38 ["COPY", "register:0:8", ["register:4048:8"]]
- 004dfa38 ["INT_ADD", "register:40f0:8", ["const:4dfa38:8", "const:4:8"]]
- 004dfa38 ["CALLIND", null, ["register:0:8"]]
+ 004dfa78 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004dfa78 ["INT_ADD", "register:40f0:8", ["const:4dfa78:8", "const:4:8"]]
+ 004dfa78 ["CALLIND", null, ["register:0:8"]]
- 004dfa38 bytes 20013fd6
+ 004dfa78 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27f90b113aafaf47693d401e87defc4c"></a>

### [`004dfdbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004df/004dfdbc.md) → [`004dfdfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004df/004dfdfc.md) _ZNK5Botan15Modular_Reducer6reduceERKNS_6BigIntE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58f20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58f20.md) · 呼出先 20件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`004b8774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8774.md) [`004b9bf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b9bf8.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md)
- 新版 呼出元 1件 [`00c59320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59320.md) · 呼出先 20件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`004b87b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b87b4.md) [`004b9c38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b9/004b9c38.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.44% / 新版 99.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件, `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004e023c",
      "incomplete_value": true,
      "site": "004e023c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 15,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004e02d0",
      "incomplete_value": true,
      "site": "004e02d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004e0290",
      "incomplete_value": true,
      "site": "004e0290",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 20,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004e0300",
      "incomplete_value": true,
      "site": "004e0300",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004e02c0",
      "incomplete_value": true,
      "site": "004e02c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 22,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004e022c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004e02c0",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004e02f0",
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
      "004e022c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004e02c0",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004e02f0",
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

- 旧版 [`004e01fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004df/004dfdbc.md#insn-004e01fc) · [`004e0280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004df/004dfdbc.md#insn-004e0280) · [`004e0290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004df/004dfdbc.md#insn-004e0290)
- 新版 `004e023c`（命令位置の公開資料なし） · `004e02c0`（命令位置の公開資料なし） · `004e02d0`（命令位置の公開資料なし）

~~~diff
- 004e01fc ["COPY", "register:0:8", ["register:4048:8"]]
- 004e01fc ["INT_ADD", "register:40f0:8", ["const:4e01fc:8", "const:4:8"]]
- 004e01fc ["CALLIND", null, ["register:0:8"]]
+ 004e023c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e023c ["INT_ADD", "register:40f0:8", ["const:4e023c:8", "const:4:8"]]
+ 004e023c ["CALLIND", null, ["register:0:8"]]
- 004e01fc bytes 20013fd6
+ 004e023c bytes 20013fd6
- 004e0280 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:338:8"]]
- 004e0280 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e02c0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:738:8"]]
+ 004e02c0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004e0280 bytes 299d41f9
+ 004e02c0 bytes 299d43f9
- 004e0290 ["COPY", "register:0:8", ["register:4048:8"]]
- 004e0290 ["INT_ADD", "register:40f0:8", ["const:4e0290:8", "const:4:8"]]
- 004e0290 ["CALLIND", null, ["register:0:8"]]
+ 004e02d0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e02d0 ["INT_ADD", "register:40f0:8", ["const:4e02d0:8", "const:4:8"]]
+ 004e02d0 ["CALLIND", null, ["register:0:8"]]
- 004e0290 bytes 20013fd6
+ 004e02d0 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3fffb978793aeea0d0103b867caba9f7"></a>

### [`004e03e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e0/004e03e8.md) → [`004e0428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e0/004e0428.md) FUN_004e0428

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 13件 [`004b8810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8810.md) [`004d6e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d6/004d6e28.md) [`004d7684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7684.md) [`004d7b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7b2c.md) [`005408e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005408e0.md)
- 新版 呼出元 0件  · 呼出先 13件 [`004b8850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8850.md) [`004d6e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d6/004d6e68.md) [`004d76c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d7/004d76c4.md) [`004d7b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d7/004d7b6c.md) [`00540920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540920.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.98% / 新版 96.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004e06ac",
      "incomplete_value": true,
      "site": "004e06ac",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 14,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004e06d8",
      "incomplete_value": true,
      "site": "004e06d8",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004e0698",
      "incomplete_value": true,
      "site": "004e0698",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 16,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004e0704",
      "incomplete_value": true,
      "site": "004e0704",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004e06c4",
      "incomplete_value": true,
      "site": "004e06c4",
      "value": [
        "LOAD",
        "8",
        [
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
      "004e069c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004e06c8",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004e06f4",
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
      "004e069c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004e06c8",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004e06f4",
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

- 旧版 [`004e066c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e0/004e03e8.md#insn-004e066c) · [`004e0698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e0/004e03e8.md#insn-004e0698) · [`004e06c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e0/004e03e8.md#insn-004e06c4)
- 新版 `004e06ac`（命令位置の公開資料なし） · `004e06d8`（命令位置の公開資料なし） · `004e0704`（命令位置の公開資料なし）

~~~diff
- 004e066c ["COPY", "register:0:8", ["register:4048:8"]]
- 004e066c ["INT_ADD", "register:40f0:8", ["const:4e066c:8", "const:4:8"]]
- 004e066c ["CALLIND", null, ["register:0:8"]]
+ 004e06ac ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e06ac ["INT_ADD", "register:40f0:8", ["const:4e06ac:8", "const:4:8"]]
+ 004e06ac ["CALLIND", null, ["register:0:8"]]
- 004e066c bytes 20013fd6
+ 004e06ac bytes 20013fd6
- 004e0698 ["COPY", "register:0:8", ["register:4048:8"]]
- 004e0698 ["INT_ADD", "register:40f0:8", ["const:4e0698:8", "const:4:8"]]
- 004e0698 ["CALLIND", null, ["register:0:8"]]
+ 004e06d8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e06d8 ["INT_ADD", "register:40f0:8", ["const:4e06d8:8", "const:4:8"]]
+ 004e06d8 ["CALLIND", null, ["register:0:8"]]
- 004e0698 bytes 20013fd6
+ 004e06d8 bytes 20013fd6
- 004e06c4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004e06c4 ["INT_ADD", "register:40f0:8", ["const:4e06c4:8", "const:4:8"]]
- 004e06c4 ["CALLIND", null, ["register:0:8"]]
+ 004e0704 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e0704 ["INT_ADD", "register:40f0:8", ["const:4e0704:8", "const:4:8"]]
+ 004e0704 ["CALLIND", null, ["register:0:8"]]
- 004e06c4 bytes 20013fd6
+ 004e0704 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c15c3696af34f64ecc72cb00f0683988"></a>

### [`004e076c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e0/004e076c.md) → [`004e07ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e0/004e07ac.md) FUN_004e07ac

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004de7c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004de/004de7c0.md) · 呼出先 14件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`005408e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005408e0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 1件 [`004de800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004de/004de800.md) · 呼出先 14件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00540920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540920.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.15% / 新版 94.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 4件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004e07e0",
      "incomplete_value": false,
      "site": "004e07f0",
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
            "const:df8:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004e096c",
      "incomplete_value": true,
      "site": "004e096c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004e092c",
      "incomplete_value": true,
      "site": "004e092c",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004e09b4",
      "incomplete_value": true,
      "site": "004e09b4",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004e0974",
      "incomplete_value": true,
      "site": "004e0974",
      "value": [
        "LOAD",
        "8",
        [
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
      "004e07f0",
      "DATA",
      [
        "storage",
        "00c669f8",
        null,
        "undefined *"
      ]
    ],
    [
      "004e095c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004e09a4",
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
      "004e07f0",
      "DATA",
      [
        "storage",
        "00c66df8",
        null,
        "undefined *"
      ]
    ],
    [
      "004e095c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004e09a4",
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

- 旧版 [`004e07f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e0/004e076c.md#insn-004e07f0) · [`004e092c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e0/004e076c.md#insn-004e092c) · [`004e0934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e0/004e076c.md#insn-004e0934)
- 新版 `004e0830`（命令位置の公開資料なし） · `004e096c`（命令位置の公開資料なし） · `004e0974`（命令位置の公開資料なし）

~~~diff
- 004e07f0 ["INT_ADD", "register:40f0:8", ["const:4e07f0:8", "const:4:8"]]
- 004e07f0 ["CALL", null, ["callee:00c592e0:8"]]
+ 004e0830 ["INT_ADD", "register:40f0:8", ["const:4e0830:8", "const:4:8"]]
+ 004e0830 ["CALL", null, ["callee:00c592e0:8"]]
- 004e07f0 bytes bce11d94
+ 004e0830 bytes ace21d94
- 004e092c ["COPY", "register:0:8", ["register:4048:8"]]
- 004e092c ["INT_ADD", "register:40f0:8", ["const:4e092c:8", "const:4:8"]]
- 004e092c ["CALLIND", null, ["register:0:8"]]
+ 004e096c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e096c ["INT_ADD", "register:40f0:8", ["const:4e096c:8", "const:4:8"]]
+ 004e096c ["CALLIND", null, ["register:0:8"]]
- 004e092c bytes 20013fd6
+ 004e096c bytes 20013fd6
- 004e0934 ["INT_ADD", "register:40f0:8", ["const:4e0934:8", "const:4:8"]]
- 004e0934 ["CALL", null, ["callee:00c58660:8"]]
+ 004e0974 ["INT_ADD", "register:40f0:8", ["const:4e0974:8", "const:4:8"]]
+ 004e0974 ["CALL", null, ["callee:00c58660:8"]]
- 004e0934 bytes 4bde1d94
+ 004e0974 bytes 3bdf1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca7f6870b42bc9c8ae17bca9d1a05d80"></a>

### [`004e0b68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e0/004e0b68.md) → [`004e0ba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e0/004e0ba8.md) FUN_004e0ba8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)

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
      "definition_site": "004e0c10",
      "incomplete_value": true,
      "site": "004e0c10",
      "value": [
        "LOAD",
        "8",
        [
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
      "004e0c00",
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
      "004e0c00",
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

- 旧版 [`004e0bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e0/004e0b68.md#insn-004e0bd0) · [`004e0bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e0/004e0b68.md#insn-004e0bc0) · [`004e0bd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e0/004e0b68.md#insn-004e0bd8)
- 新版 `004e0c10`（命令位置の公開資料なし） · `004e0c00`（命令位置の公開資料なし） · `004e0c18`（命令位置の公開資料なし）

~~~diff
- 004e0bd0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004e0bd0 ["INT_ADD", "register:40f0:8", ["const:4e0bd0:8", "const:4:8"]]
- 004e0bd0 ["CALLIND", null, ["register:0:8"]]
+ 004e0c10 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e0c10 ["INT_ADD", "register:40f0:8", ["const:4e0c10:8", "const:4:8"]]
+ 004e0c10 ["CALLIND", null, ["register:0:8"]]
- 004e0bd0 bytes 20013fd6
+ 004e0c10 bytes 20013fd6
- 004e0bc0 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:338:8"]]
- 004e0bc0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e0c00 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:738:8"]]
+ 004e0c00 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004e0bc0 bytes c99e41f9
+ 004e0c00 bytes c99e43f9
- 004e0bd8 ["INT_ADD", "register:40f0:8", ["const:4e0bd8:8", "const:4:8"]]
- 004e0bd8 ["CALL", null, ["callee:00c58660:8"]]
+ 004e0c18 ["INT_ADD", "register:40f0:8", ["const:4e0c18:8", "const:4:8"]]
+ 004e0c18 ["CALL", null, ["callee:00c58660:8"]]
- 004e0bd8 bytes a2dd1d94
+ 004e0c18 bytes 92de1d94
~~~


<a id="compare-1c448a054c4de74cd33cef953ad8ed31"></a>

### [`004e0c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e0/004e0c14.md) → [`004e0c54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e0/004e0c54.md) _ZN5Botan15Modular_ReducerC1ERKNS_6BigIntE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58ee0.md) · 呼出先 14件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`005408e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005408e0.md) [`0054369c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/0054369c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00c592e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c592e0.md) · 呼出先 14件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00540920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540920.md) [`005436dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/005436dc.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

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
      "definition_site": "004e0cf8",
      "incomplete_value": true,
      "site": "004e0cf8",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004e0dc0",
      "incomplete_value": true,
      "site": "004e0dc0",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
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
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004e0e78",
      "incomplete_value": true,
      "site": "004e0e78",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
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
      "004e0ce8",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004e0db0",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004e0e68",
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
      "004e0ce8",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004e0db0",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004e0e68",
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

- 旧版 [`004e0cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e0/004e0c14.md#insn-004e0cb8) · [`004e0d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e0/004e0c14.md#insn-004e0d80) · [`004e0e38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e0/004e0c14.md#insn-004e0e38)
- 新版 `004e0cf8`（命令位置の公開資料なし） · `004e0dc0`（命令位置の公開資料なし） · `004e0e78`（命令位置の公開資料なし）

~~~diff
- 004e0cb8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004e0cb8 ["INT_ADD", "register:40f0:8", ["const:4e0cb8:8", "const:4:8"]]
- 004e0cb8 ["CALLIND", null, ["register:0:8"]]
+ 004e0cf8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e0cf8 ["INT_ADD", "register:40f0:8", ["const:4e0cf8:8", "const:4:8"]]
+ 004e0cf8 ["CALLIND", null, ["register:0:8"]]
- 004e0cb8 bytes 20013fd6
+ 004e0cf8 bytes 20013fd6
- 004e0d80 ["COPY", "register:0:8", ["register:4048:8"]]
- 004e0d80 ["INT_ADD", "register:40f0:8", ["const:4e0d80:8", "const:4:8"]]
- 004e0d80 ["CALLIND", null, ["register:0:8"]]
+ 004e0dc0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e0dc0 ["INT_ADD", "register:40f0:8", ["const:4e0dc0:8", "const:4:8"]]
+ 004e0dc0 ["CALLIND", null, ["register:0:8"]]
- 004e0d80 bytes 20013fd6
+ 004e0dc0 bytes 20013fd6
- 004e0e38 ["COPY", "register:0:8", ["register:4048:8"]]
- 004e0e38 ["INT_ADD", "register:40f0:8", ["const:4e0e38:8", "const:4:8"]]
- 004e0e38 ["CALLIND", null, ["register:0:8"]]
+ 004e0e78 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e0e78 ["INT_ADD", "register:40f0:8", ["const:4e0e78:8", "const:4:8"]]
+ 004e0e78 ["CALLIND", null, ["register:0:8"]]
- 004e0e38 bytes 20013fd6
+ 004e0e78 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d95c7a27d416cd70cdf27eec78a78560"></a>

### [`004e0f8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e0/004e0f8c.md) → [`004e0fcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e0/004e0fcc.md) _ZN5Botan6ressolERKNS_6BigIntES2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 25件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`005408e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005408e0.md) [`0054369c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/0054369c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 25件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00540920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540920.md) [`005436dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/005436dc.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 90.84% / 新版 90.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `call_target` 42件

アドレスに依存する影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004e1048",
      "incomplete_value": true,
      "site": "004e1048",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004e1098",
      "incomplete_value": true,
      "site": "004e1098",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
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
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004e10fc",
      "incomplete_value": true,
      "site": "004e10fc",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
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
      "004e1038",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004e1088",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004e10ec",
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
      "004e1038",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004e1088",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004e10ec",
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

- 旧版 [`004e1008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e0/004e0f8c.md#insn-004e1008) · [`004e1048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e0/004e0f8c.md#insn-004e1048) · [`004e1058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e0/004e0f8c.md#insn-004e1058)
- 新版 `004e1048`（命令位置の公開資料なし） · `004e1088`（命令位置の公開資料なし） · `004e1098`（命令位置の公開資料なし）

~~~diff
- 004e1008 ["COPY", "register:0:8", ["register:4048:8"]]
- 004e1008 ["INT_ADD", "register:40f0:8", ["const:4e1008:8", "const:4:8"]]
- 004e1008 ["CALLIND", null, ["register:0:8"]]
+ 004e1048 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e1048 ["INT_ADD", "register:40f0:8", ["const:4e1048:8", "const:4:8"]]
+ 004e1048 ["CALLIND", null, ["register:0:8"]]
- 004e1008 bytes 20013fd6
+ 004e1048 bytes 20013fd6
- 004e1048 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:338:8"]]
- 004e1048 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e1088 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:738:8"]]
+ 004e1088 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004e1048 bytes 299f41f9
+ 004e1088 bytes 299f43f9
- 004e1058 ["COPY", "register:0:8", ["register:4048:8"]]
- 004e1058 ["INT_ADD", "register:40f0:8", ["const:4e1058:8", "const:4:8"]]
- 004e1058 ["CALLIND", null, ["register:0:8"]]
+ 004e1098 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e1098 ["INT_ADD", "register:40f0:8", ["const:4e1098:8", "const:4:8"]]
+ 004e1098 ["CALLIND", null, ["register:0:8"]]
- 004e1058 bytes 20013fd6
+ 004e1098 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26e8ee29ce1519b9cbf5be490a3ccbba"></a>

### [`004e2414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e2/004e2414.md) → [`004e2454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e2/004e2454.md) FUN_004e2454

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`004e23b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e2/004e23b8.md) [`004e33b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e3/004e33b8.md) [`004e346c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e3/004e346c.md) [`004ebc2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004eb/004ebc2c.md) [`004ec378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ec/004ec378.md) · 呼出先 40件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`004a6d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6d70.md) [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00535b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b40.md)
- 新版 呼出元 6件 [`004e23f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e2/004e23f8.md) [`004e33f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e3/004e33f8.md) [`004e34ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e3/004e34ac.md) [`004ebc6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004eb/004ebc6c.md) [`004ec3b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ec3b8.md) · 呼出先 40件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`004a6db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6db0.md) [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00535b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b80.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.47% / 新版 94.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `call_target` 11件, `store_value` 3件

アドレスに依存する影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004e24fc",
      "incomplete_value": false,
      "site": "004e24fc",
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
    "old": {
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
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e2894",
      "incomplete_value": true,
      "site": "004e2894",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:348:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 52,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e28f0",
      "incomplete_value": true,
      "site": "004e28f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c68:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "004e248c",
      "PARAM",
      [
        "storage",
        "002bd8ab",
        null,
        "string"
      ]
    ],
    [
      "004e24b8",
      "PARAM",
      [
        "storage",
        "002ab265",
        null,
        null
      ]
    ],
    [
      "004e24fc",
      "DATA",
      [
        "storage",
        "00c6a2b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004e248c",
      "PARAM",
      [
        "storage",
        "002bd8eb",
        null,
        "string"
      ]
    ],
    [
      "004e24b8",
      "PARAM",
      [
        "storage",
        "002ab332",
        null,
        null
      ]
    ],
    [
      "004e24fc",
      "DATA",
      [
        "storage",
        "00c6a6b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e2470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e2/004e2414.md#insn-004e2470) · [`004e2480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e2/004e2414.md#insn-004e2480) · [`004e25f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e2/004e2414.md#insn-004e25f4)
- 新版 `004e24b0`（命令位置の公開資料なし） · `004e24c0`（命令位置の公開資料なし） · `004e2634`（命令位置の公開資料なし）

~~~diff
- 004e2470 ["INT_ADD", "register:40f0:8", ["const:4e2470:8", "const:4:8"]]
- 004e2470 ["CALL", null, ["callee:00c580b0:8"]]
+ 004e24b0 ["INT_ADD", "register:40f0:8", ["const:4e24b0:8", "const:4:8"]]
+ 004e24b0 ["CALL", null, ["callee:00c580b0:8"]]
- 004e2470 bytes 10d61d94
+ 004e24b0 bytes 00d71d94
- 004e2480 ["INT_ADD", "register:40f0:8", ["const:4e2480:8", "const:4:8"]]
- 004e2480 ["CALL", null, ["callee:00c57f70:8"]]
+ 004e24c0 ["INT_ADD", "register:40f0:8", ["const:4e24c0:8", "const:4:8"]]
+ 004e24c0 ["CALL", null, ["callee:00c57f70:8"]]
- 004e2480 bytes bcd51d94
+ 004e24c0 bytes acd61d94
- 004e25f4 ["INT_ADD", "register:40f0:8", ["const:4e25f4:8", "const:4:8"]]
- 004e25f4 ["CALL", null, ["callee:00c580b0:8"]]
+ 004e2634 ["INT_ADD", "register:40f0:8", ["const:4e2634:8", "const:4:8"]]
+ 004e2634 ["CALL", null, ["callee:00c580b0:8"]]
- 004e25f4 bytes afd51d94
+ 004e2634 bytes 9fd61d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43faf884b0e5b390fabd25445acedabc"></a>

### [`004e3484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e3/004e3484.md) → [`004e34c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e3/004e34c4.md) _ZN5Botan13pbes2_decryptERKNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEERKNS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEERKNS

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59050.md) · 呼出先 36件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004a573c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a573c.md) [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00535fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535fd0.md)
- 新版 呼出元 1件 [`00c59450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59450.md) · 呼出先 36件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004a577c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a577c.md) [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00536010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536010.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.78% / 新版 93.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `call_target` 8件, `store_value` 5件

アドレスに依存する影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e3514",
      "incomplete_value": true,
      "site": "004e3514",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e36a8",
      "incomplete_value": true,
      "site": "004e36a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c68:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 35,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e37c8",
      "incomplete_value": true,
      "site": "004e37c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7af:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "004e3500",
      "READ",
      [
        "storage",
        "00c9a938",
        null,
        "pointer"
      ]
    ],
    [
      "004e3514",
      "DATA",
      [
        "storage",
        "00c65da8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004e3548",
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
      "004e3500",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "004e3514",
      "DATA",
      [
        "storage",
        "00c661a8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004e3548",
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

- 旧版 [`004e3580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e3/004e3484.md#insn-004e3580) · [`004e35c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e3/004e3484.md#insn-004e35c0) · [`004e3604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e3/004e3484.md#insn-004e3604)
- 新版 `004e35c0`（命令位置の公開資料なし） · `004e3600`（命令位置の公開資料なし） · `004e3644`（命令位置の公開資料なし）

~~~diff
- 004e3580 ["INT_ADD", "register:40f0:8", ["const:4e3580:8", "const:4:8"]]
- 004e3580 ["CALL", null, ["callee:00c58710:8"]]
+ 004e35c0 ["INT_ADD", "register:40f0:8", ["const:4e35c0:8", "const:4:8"]]
+ 004e35c0 ["CALL", null, ["callee:00c58710:8"]]
- 004e3580 bytes 64d31d94
+ 004e35c0 bytes 54d41d94
- 004e35c0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004e35c0 ["INT_ADD", "register:40f0:8", ["const:4e35c0:8", "const:4:8"]]
- 004e35c0 ["CALLIND", null, ["register:0:8"]]
+ 004e3600 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e3600 ["INT_ADD", "register:40f0:8", ["const:4e3600:8", "const:4:8"]]
+ 004e3600 ["CALLIND", null, ["register:0:8"]]
- 004e35c0 bytes 20013fd6
+ 004e3600 bytes 20013fd6
- 004e3604 ["COPY", "register:0:8", ["register:4048:8"]]
- 004e3604 ["INT_ADD", "register:40f0:8", ["const:4e3604:8", "const:4:8"]]
- 004e3604 ["CALLIND", null, ["register:0:8"]]
+ 004e3644 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e3644 ["INT_ADD", "register:40f0:8", ["const:4e3644:8", "const:4:8"]]
+ 004e3644 ["CALLIND", null, ["register:0:8"]]
- 004e3604 bytes 20013fd6
+ 004e3644 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd652daebdf179b8ba5d26a664eb8573"></a>

### [`004e469c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e469c.md) → [`004e46dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e4/004e46dc.md) _ZN5Botan5PBKDF6createERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59020.md) · 呼出先 9件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md)
- 新版 呼出元 1件 [`00c59420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59420.md) · 呼出先 9件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f60.md)

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
      "definition_site": "004e49e4",
      "incomplete_value": true,
      "site": "004e49e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 25,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e4914",
      "incomplete_value": false,
      "site": "004e4920",
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
            "const:8eb:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 14,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e4940",
      "incomplete_value": false,
      "site": "004e4948",
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
    "old": {
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
      "004e4914",
      "PARAM",
      [
        "storage",
        "002bd8ab",
        null,
        "string"
      ]
    ],
    [
      "004e4940",
      "PARAM",
      [
        "storage",
        "002ab265",
        null,
        null
      ]
    ],
    [
      "004e49d8",
      "READ",
      [
        "storage",
        "00c9abc8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004e4914",
      "PARAM",
      [
        "storage",
        "002bd8eb",
        null,
        "string"
      ]
    ],
    [
      "004e4940",
      "PARAM",
      [
        "storage",
        "002ab332",
        null,
        null
      ]
    ],
    [
      "004e49d8",
      "READ",
      [
        "storage",
        "00c9afc8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e48e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e469c.md#insn-004e48e0) · [`004e4908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e469c.md#insn-004e4908) · [`004e46e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e469c.md#insn-004e46e8)
- 新版 `004e4920`（命令位置の公開資料なし） · `004e4948`（命令位置の公開資料なし） · `004e4728`（命令位置の公開資料なし）

~~~diff
- 004e48e0 ["INT_ADD", "register:40f0:8", ["const:4e48e0:8", "const:4:8"]]
- 004e48e0 ["CALL", null, ["callee:00c57f60:8"]]
+ 004e4920 ["INT_ADD", "register:40f0:8", ["const:4e4920:8", "const:4:8"]]
+ 004e4920 ["CALL", null, ["callee:00c57f60:8"]]
- 004e48e0 bytes a0cc1d94
+ 004e4920 bytes 90cd1d94
- 004e4908 ["INT_ADD", "register:40f0:8", ["const:4e4908:8", "const:4:8"]]
- 004e4908 ["CALL", null, ["callee:00c57f70:8"]]
+ 004e4948 ["INT_ADD", "register:40f0:8", ["const:4e4948:8", "const:4:8"]]
+ 004e4948 ["CALL", null, ["callee:00c57f70:8"]]
- 004e4908 bytes 9acc1d94
+ 004e4948 bytes 8acd1d94
- 004e46e8 ["INT_ADD", "register:40f0:8", ["const:4e46e8:8", "const:4:8"]]
- 004e46e8 ["CALL", null, ["callee:0043bb20:8"]]
+ 004e4728 ["INT_ADD", "register:40f0:8", ["const:4e4728:8", "const:4:8"]]
+ 004e4728 ["CALL", null, ["callee:0043bb20:8"]]
- 004e46e8 bytes fe5cfd97
+ 004e4728 bytes fe5cfd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e593da160902d572f8e82828d19edb5"></a>

### [`004e4a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e4a98.md) → [`004e4ad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e4/004e4ad8.md) _ZN5Botan5PBKDF15create_or_throwERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
      "definition_site": "004e4b50",
      "incomplete_value": false,
      "site": "004e4b58",
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
            "const:c7c:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e4b90",
      "incomplete_value": true,
      "site": "004e4b9c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e4b8c",
      "incomplete_value": false,
      "site": "004e4b9c",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004e4b4c",
      "incomplete_value": false,
      "site": "004e4b5c",
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
      "004e4b50",
      "PARAM",
      [
        "storage",
        "002b1c3c",
        null,
        "string"
      ]
    ],
    [
      "004e4b8c",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004e4b90",
      "READ",
      [
        "storage",
        "00c9aa28",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004e4b50",
      "PARAM",
      [
        "storage",
        "002b1c7c",
        null,
        "string"
      ]
    ],
    [
      "004e4b8c",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004e4b90",
      "READ",
      [
        "storage",
        "00c9ae28",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e4b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e4a98.md#insn-004e4b18) · [`004e4b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e4a98.md#insn-004e4b5c) · [`004e4acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e4a98.md#insn-004e4acc)
- 新版 `004e4b58`（命令位置の公開資料なし） · `004e4b9c`（命令位置の公開資料なし） · `004e4b0c`（命令位置の公開資料なし）

~~~diff
- 004e4b18 ["INT_ADD", "register:40f0:8", ["const:4e4b18:8", "const:4:8"]]
- 004e4b18 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004e4b58 ["INT_ADD", "register:40f0:8", ["const:4e4b58:8", "const:4:8"]]
+ 004e4b58 ["CALL", null, ["callee:0043ddd8:8"]]
- 004e4b18 bytes a064fd97
+ 004e4b58 bytes a064fd97
- 004e4b5c ["INT_ADD", "register:40f0:8", ["const:4e4b5c:8", "const:4:8"]]
- 004e4b5c ["CALL", null, ["callee:00c57f10:8"]]
+ 004e4b9c ["INT_ADD", "register:40f0:8", ["const:4e4b9c:8", "const:4:8"]]
+ 004e4b9c ["CALL", null, ["callee:00c57f10:8"]]
- 004e4b5c bytes edcb1d94
+ 004e4b9c bytes ddcc1d94
- 004e4acc ["INT_ADD", "register:40f0:8", ["const:4e4acc:8", "const:4:8"]]
- 004e4acc ["CALL", null, ["callee:00c59420:8"]]
+ 004e4b0c ["INT_ADD", "register:40f0:8", ["const:4e4b0c:8", "const:4:8"]]
+ 004e4b0c ["CALL", null, ["callee:00c59420:8"]]
- 004e4acc bytes 55d11d94
+ 004e4b0c bytes 45d21d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1ede9d57dd8067322fffb380ea4c5f7"></a>

### [`004e4e84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e4e84.md) → [`004e4ec4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e4/004e4ec4.md) _ZNK5Botan5PBKDF16pbkdf_iterationsEPhmRKNSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEPKhmm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59030.md) · 呼出先 7件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 1件 [`00c59430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59430.md) · 呼出先 7件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

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
      "definition_site": "004e4f54",
      "incomplete_value": false,
      "site": "004e4f5c",
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
            "const:560:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e4fa8",
      "incomplete_value": true,
      "site": "004e4fb4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e4fa4",
      "incomplete_value": false,
      "site": "004e4fb4",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004e4f64",
      "incomplete_value": false,
      "site": "004e4f74",
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
      "004e4f54",
      "PARAM",
      [
        "storage",
        "002bc520",
        null,
        "string"
      ]
    ],
    [
      "004e4fa4",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004e4fa8",
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
      "004e4f54",
      "PARAM",
      [
        "storage",
        "002bc560",
        null,
        "string"
      ]
    ],
    [
      "004e4fa4",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004e4fa8",
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

- 旧版 [`004e4f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e4e84.md#insn-004e4f1c) · [`004e4f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e4e84.md#insn-004e4f74) · [`004e4fac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e4/004e4e84.md#insn-004e4fac)
- 新版 `004e4f5c`（命令位置の公開資料なし） · `004e4fb4`（命令位置の公開資料なし） · `004e4fec`（命令位置の公開資料なし）

~~~diff
- 004e4f1c ["INT_ADD", "register:40f0:8", ["const:4e4f1c:8", "const:4:8"]]
- 004e4f1c ["CALL", null, ["callee:00c57f70:8"]]
+ 004e4f5c ["INT_ADD", "register:40f0:8", ["const:4e4f5c:8", "const:4:8"]]
+ 004e4f5c ["CALL", null, ["callee:00c57f70:8"]]
- 004e4f1c bytes 15cb1d94
+ 004e4f5c bytes 05cc1d94
- 004e4f74 ["INT_ADD", "register:40f0:8", ["const:4e4f74:8", "const:4:8"]]
- 004e4f74 ["CALL", null, ["callee:00c57f10:8"]]
+ 004e4fb4 ["INT_ADD", "register:40f0:8", ["const:4e4fb4:8", "const:4:8"]]
+ 004e4fb4 ["CALL", null, ["callee:00c57f10:8"]]
- 004e4f74 bytes e7ca1d94
+ 004e4fb4 bytes d7cb1d94
- 004e4fac ["INT_ADD", "register:40f0:8", ["const:4e4fac:8", "const:4:8"]]
- 004e4fac ["CALL", null, ["callee:00c58650:8"]]
+ 004e4fec ["INT_ADD", "register:40f0:8", ["const:4e4fec:8", "const:4:8"]]
+ 004e4fec ["CALL", null, ["callee:00c58650:8"]]
- 004e4fac bytes a9cc1d94
+ 004e4fec bytes 99cd1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85e806184795125459986e967c61605c"></a>

### [`004e50c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e5/004e50c4.md) → [`004e5104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e5/004e5104.md) _ZN5Botan6pbkdf2ERNS_25MessageAuthenticationCodeEPhmRKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPKhmmNS3_6chrono8du

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59080.md) · 呼出先 8件 [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`004bc9c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc9c0.md) [`00c57ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ac0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)
- 新版 呼出元 1件 [`00c59480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59480.md) · 呼出先 8件 [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md) [`004bca00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bca00.md) [`00c57ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ec0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)

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
      "definition_site": "004e55bc",
      "incomplete_value": true,
      "site": "004e55bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 16,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e561c",
      "incomplete_value": false,
      "site": "004e563c",
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
    "old": {
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
    "ordinal": 18,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e5624",
      "incomplete_value": false,
      "site": "004e563c",
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
    "old": {
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
      "004e55ac",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004e561c",
      "PARAM",
      [
        "storage",
        "002a1ff2",
        null,
        "string"
      ]
    ],
    [
      "004e5624",
      "PARAM",
      [
        "storage",
        "002ab57d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004e55ac",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004e561c",
      "PARAM",
      [
        "storage",
        "002a20bf",
        null,
        "string"
      ]
    ],
    [
      "004e5624",
      "PARAM",
      [
        "storage",
        "002ab5bd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e557c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e5/004e50c4.md#insn-004e557c) · [`004e55fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e5/004e50c4.md#insn-004e55fc) · [`004e5118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e5/004e50c4.md#insn-004e5118)
- 新版 `004e55bc`（命令位置の公開資料なし） · `004e563c`（命令位置の公開資料なし） · `004e5158`（命令位置の公開資料なし）

~~~diff
- 004e557c ["COPY", "register:0:8", ["register:4048:8"]]
- 004e557c ["INT_ADD", "register:40f0:8", ["const:4e557c:8", "const:4:8"]]
- 004e557c ["CALLIND", null, ["register:0:8"]]
+ 004e55bc ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e55bc ["INT_ADD", "register:40f0:8", ["const:4e55bc:8", "const:4:8"]]
+ 004e55bc ["CALLIND", null, ["register:0:8"]]
- 004e557c bytes 20013fd6
+ 004e55bc bytes 20013fd6
- 004e55fc ["INT_ADD", "register:40f0:8", ["const:4e55fc:8", "const:4:8"]]
- 004e55fc ["CALL", null, ["callee:00c58650:8"]]
+ 004e563c ["INT_ADD", "register:40f0:8", ["const:4e563c:8", "const:4:8"]]
+ 004e563c ["CALL", null, ["callee:00c58650:8"]]
- 004e55fc bytes 15cb1d94
+ 004e563c bytes 05cc1d94
- 004e5118 ["INT_ADD", "register:40f0:8", ["const:4e5118:8", "const:4:8"]]
- 004e5118 ["CALL", null, ["callee:00c58090:8"]]
+ 004e5158 ["INT_ADD", "register:40f0:8", ["const:4e5158:8", "const:4:8"]]
+ 004e5158 ["CALL", null, ["callee:00c58090:8"]]
- 004e5118 bytes deca1d94
+ 004e5158 bytes cecb1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d50284e7dc66721c666a32051d157598"></a>

### [`004e5828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e5/004e5828.md) → [`004e5868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e5/004e5868.md) _ZN5Botan8PEM_Code6encodeEPKhmRKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59090.md) · 呼出先 8件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)
- 新版 呼出元 1件 [`00c59490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59490.md) · 呼出先 8件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md)

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
      "definition_site": "004e5898",
      "incomplete_value": false,
      "site": "004e58b0",
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
            "const:7cb:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e58b8",
      "incomplete_value": false,
      "site": "004e58c0",
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
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e58f0",
      "incomplete_value": false,
      "site": "004e58fc",
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
            "const:b98:8"
          ]
        ]
      ]
    },
    "old": {
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
      "004e5898",
      "PARAM",
      [
        "storage",
        "002ac78b",
        null,
        "string"
      ]
    ],
    [
      "004e58b8",
      "PARAM",
      [
        "storage",
        "002bc53a",
        null,
        "string"
      ]
    ],
    [
      "004e58f0",
      "PARAM",
      [
        "storage",
        "002b0b58",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004e5898",
      "PARAM",
      [
        "storage",
        "002ac7cb",
        null,
        "string"
      ]
    ],
    [
      "004e58b8",
      "PARAM",
      [
        "storage",
        "002bc57a",
        null,
        "string"
      ]
    ],
    [
      "004e58f0",
      "PARAM",
      [
        "storage",
        "002b0b98",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e5870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e5/004e5828.md#insn-004e5870) · [`004e5880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e5/004e5828.md#insn-004e5880) · [`004e58b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e5/004e5828.md#insn-004e58b0)
- 新版 `004e58b0`（命令位置の公開資料なし） · `004e58c0`（命令位置の公開資料なし） · `004e58f0`（命令位置の公開資料なし）

~~~diff
- 004e5870 ["INT_ADD", "register:40f0:8", ["const:4e5870:8", "const:4:8"]]
- 004e5870 ["CALL", null, ["callee:00c580b0:8"]]
+ 004e58b0 ["INT_ADD", "register:40f0:8", ["const:4e58b0:8", "const:4:8"]]
+ 004e58b0 ["CALL", null, ["callee:00c580b0:8"]]
- 004e5870 bytes 10c91d94
+ 004e58b0 bytes 00ca1d94
- 004e5880 ["INT_ADD", "register:40f0:8", ["const:4e5880:8", "const:4:8"]]
- 004e5880 ["CALL", null, ["callee:00c57f70:8"]]
+ 004e58c0 ["INT_ADD", "register:40f0:8", ["const:4e58c0:8", "const:4:8"]]
+ 004e58c0 ["CALL", null, ["callee:00c57f70:8"]]
- 004e5880 bytes bcc81d94
+ 004e58c0 bytes acc91d94
- 004e58b0 ["COPY", "tmp:0:8", ["const:b58:8"]]
- 004e58b0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004e58b0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004e58b0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004e58f0 ["COPY", "tmp:0:8", ["const:b98:8"]]
+ 004e58f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004e58f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004e58f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004e58b0 bytes 00602d91
+ 004e58f0 bytes 00602e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3691d5e30da47d2f205ae342a952378b"></a>

### [`004e5bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e5/004e5bd4.md) → [`004e5c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e5/004e5c14.md) _ZN5Botan8PEM_Code18decode_check_labelERNS_10DataSourceERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c590a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c590a0.md) · 呼出先 11件 [`0044fc7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044fc7c.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 1件 [`00c594a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c594a0.md) · 呼出先 11件 [`0044fcbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044fcbc.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

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
      "definition_site": "004e5d18",
      "incomplete_value": false,
      "site": "004e5d20",
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
            "const:47f:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e5d28",
      "incomplete_value": false,
      "site": "004e5d30",
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
            "const:88a:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e5d88",
      "incomplete_value": true,
      "site": "004e5d94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004e5d18",
      "PARAM",
      [
        "storage",
        "002ab43f",
        null,
        "string"
      ]
    ],
    [
      "004e5d28",
      "PARAM",
      [
        "storage",
        "002a77ae",
        null,
        "string"
      ]
    ],
    [
      "004e5d84",
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
      "004e5d18",
      "PARAM",
      [
        "storage",
        "002ab47f",
        null,
        "string"
      ]
    ],
    [
      "004e5d28",
      "PARAM",
      [
        "storage",
        "002a788a",
        null,
        "string"
      ]
    ],
    [
      "004e5d84",
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

- 旧版 [`004e5ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e5/004e5bd4.md#insn-004e5ce0) · [`004e5cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e5/004e5bd4.md#insn-004e5cf0) · [`004e5d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e5/004e5bd4.md#insn-004e5d54)
- 新版 `004e5d20`（命令位置の公開資料なし） · `004e5d30`（命令位置の公開資料なし） · `004e5d94`（命令位置の公開資料なし）

~~~diff
- 004e5ce0 ["INT_ADD", "register:40f0:8", ["const:4e5ce0:8", "const:4:8"]]
- 004e5ce0 ["CALL", null, ["callee:00c580b0:8"]]
+ 004e5d20 ["INT_ADD", "register:40f0:8", ["const:4e5d20:8", "const:4:8"]]
+ 004e5d20 ["CALL", null, ["callee:00c580b0:8"]]
- 004e5ce0 bytes f4c71d94
+ 004e5d20 bytes e4c81d94
- 004e5cf0 ["INT_ADD", "register:40f0:8", ["const:4e5cf0:8", "const:4:8"]]
- 004e5cf0 ["CALL", null, ["callee:00c57f70:8"]]
+ 004e5d30 ["INT_ADD", "register:40f0:8", ["const:4e5d30:8", "const:4:8"]]
+ 004e5d30 ["CALL", null, ["callee:00c57f70:8"]]
- 004e5cf0 bytes a0c71d94
+ 004e5d30 bytes 90c81d94
- 004e5d54 ["INT_ADD", "register:40f0:8", ["const:4e5d54:8", "const:4:8"]]
- 004e5d54 ["CALL", null, ["callee:00c57f10:8"]]
+ 004e5d94 ["INT_ADD", "register:40f0:8", ["const:4e5d94:8", "const:4:8"]]
+ 004e5d94 ["CALL", null, ["callee:00c57f10:8"]]
- 004e5d54 bytes 6fc71d94
+ 004e5d94 bytes 5fc81d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-127365099de458b769031d89b182970a"></a>

### [`004e5e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e5/004e5e20.md) → [`004e5e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e5/004e5e60.md) _ZN5Botan8PEM_Code6decodeERNS_10DataSourceERNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c590b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c590b0.md) · 呼出先 16件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00449978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00449/00449978.md) [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md)
- 新版 呼出元 1件 [`00c594b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c594b0.md) · 呼出先 16件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004499b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00449/004499b8.md) [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md)

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
      "definition_site": "004e5ee0",
      "incomplete_value": true,
      "site": "004e5ee0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7cb:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e5fc0",
      "incomplete_value": false,
      "site": "004e5fcc",
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
            "const:b98:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e5fd4",
      "incomplete_value": false,
      "site": "004e5fdc",
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
            "const:2:8"
          ]
        ]
      ]
    },
    "old": {
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
      "004e5ecc",
      "READ",
      [
        "storage",
        "002ac78b",
        null,
        "string"
      ]
    ],
    [
      "004e5fc0",
      "PARAM",
      [
        "storage",
        "002b0b58",
        null,
        "string"
      ]
    ],
    [
      "004e5fd4",
      "PARAM",
      [
        "storage",
        "002a1f35",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004e5ecc",
      "READ",
      [
        "storage",
        "002ac7cb",
        null,
        "string"
      ]
    ],
    [
      "004e5fc0",
      "PARAM",
      [
        "storage",
        "002b0b98",
        null,
        "string"
      ]
    ],
    [
      "004e5fd4",
      "PARAM",
      [
        "storage",
        "002a2002",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e5f8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e5/004e5e20.md#insn-004e5f8c) · [`004e5f9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e5/004e5e20.md#insn-004e5f9c) · [`004e61dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e5/004e5e20.md#insn-004e61dc)
- 新版 `004e5fcc`（命令位置の公開資料なし） · `004e5fdc`（命令位置の公開資料なし） · `004e621c`（命令位置の公開資料なし）

~~~diff
- 004e5f8c ["INT_ADD", "register:40f0:8", ["const:4e5f8c:8", "const:4:8"]]
- 004e5f8c ["CALL", null, ["callee:00c580b0:8"]]
+ 004e5fcc ["INT_ADD", "register:40f0:8", ["const:4e5fcc:8", "const:4:8"]]
+ 004e5fcc ["CALL", null, ["callee:00c580b0:8"]]
- 004e5f8c bytes 49c71d94
+ 004e5fcc bytes 39c81d94
- 004e5f9c ["INT_ADD", "register:40f0:8", ["const:4e5f9c:8", "const:4:8"]]
- 004e5f9c ["CALL", null, ["callee:00c57f70:8"]]
+ 004e5fdc ["INT_ADD", "register:40f0:8", ["const:4e5fdc:8", "const:4:8"]]
+ 004e5fdc ["CALL", null, ["callee:00c57f70:8"]]
- 004e5f9c bytes f5c61d94
+ 004e5fdc bytes e5c71d94
- 004e61dc ["INT_ADD", "register:40f0:8", ["const:4e61dc:8", "const:4:8"]]
- 004e61dc ["CALL", null, ["callee:0043ddd8:8"]]
+ 004e621c ["INT_ADD", "register:40f0:8", ["const:4e621c:8", "const:4:8"]]
+ 004e621c ["CALL", null, ["callee:0043ddd8:8"]]
- 004e61dc bytes ef5efd97
+ 004e621c bytes ef5efd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad7a26e373adb3694175b5d66828db45"></a>

### [`004e6728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e6/004e6728.md) → [`004e6768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e6/004e6768.md) _ZN5Botan8PEM_Code7matchesERNS_10DataSourceERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c590d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c590d0.md) · 呼出先 6件 [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md)
- 新版 呼出元 1件 [`00c594d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c594d0.md) · 呼出先 6件 [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md)

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
      "definition_site": "004e6788",
      "incomplete_value": false,
      "site": "004e679c",
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
            "const:7cb:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004e6854",
      "incomplete_value": true,
      "site": "004e6854",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004e6788",
      "PARAM",
      [
        "storage",
        "002ac78b",
        null,
        "string"
      ]
    ],
    [
      "004e6844",
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
      "004e6788",
      "PARAM",
      [
        "storage",
        "002ac7cb",
        null,
        "string"
      ]
    ],
    [
      "004e6844",
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

- 旧版 [`004e675c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e6/004e6728.md#insn-004e675c) · [`004e6814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e6/004e6728.md#insn-004e6814) · [`004e6748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e6/004e6728.md#insn-004e6748)
- 新版 `004e679c`（命令位置の公開資料なし） · `004e6854`（命令位置の公開資料なし） · `004e6788`（命令位置の公開資料なし）

~~~diff
- 004e675c ["INT_ADD", "register:40f0:8", ["const:4e675c:8", "const:4:8"]]
- 004e675c ["CALL", null, ["callee:00c580b0:8"]]
+ 004e679c ["INT_ADD", "register:40f0:8", ["const:4e679c:8", "const:4:8"]]
+ 004e679c ["CALL", null, ["callee:00c580b0:8"]]
- 004e675c bytes 55c51d94
+ 004e679c bytes 45c61d94
- 004e6814 ["COPY", "register:0:8", ["register:4048:8"]]
- 004e6814 ["INT_ADD", "register:40f0:8", ["const:4e6814:8", "const:4:8"]]
- 004e6814 ["CALLIND", null, ["register:0:8"]]
+ 004e6854 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e6854 ["INT_ADD", "register:40f0:8", ["const:4e6854:8", "const:4:8"]]
+ 004e6854 ["CALLIND", null, ["register:0:8"]]
- 004e6814 bytes 20013fd6
+ 004e6854 bytes 20013fd6
- 004e6748 ["COPY", "tmp:0:8", ["const:78b:8"]]
- 004e6748 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004e6748 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004e6748 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004e6788 ["COPY", "tmp:0:8", ["const:7cb:8"]]
+ 004e6788 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004e6788 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004e6788 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004e6748 bytes 002c1e91
+ 004e6788 bytes 002c1f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a01aa5aa52d82afe25d704d0d1bac4a"></a>

### [`004e68a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e6/004e68a0.md) → [`004e68e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e6/004e68e0.md) _ZN5Botan7get_emeERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c58ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58ba0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c58fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58fa0.md)

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
      "definition_site": "004e6910",
      "incomplete_value": true,
      "site": "004e6918",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e690c",
      "incomplete_value": false,
      "site": "004e6918",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004e68cc",
      "incomplete_value": false,
      "site": "004e68d8",
      "value": [
        "leaf",
        "const:535828:8"
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
      "004e690c",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004e6910",
      "READ",
      [
        "storage",
        "00c9aad0",
        null,
        "pointer"
      ]
    ],
    [
      "004e6910",
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
      "004e690c",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004e6910",
      "READ",
      [
        "storage",
        "00c9aed0",
        null,
        "pointer"
      ]
    ],
    [
      "004e6910",
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

- 旧版 [`004e68d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e6/004e68a0.md#insn-004e68d8) · [`004e68b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e6/004e68a0.md#insn-004e68b4) · [`004e68c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e6/004e68a0.md#insn-004e68c0)
- 新版 `004e6918`（命令位置の公開資料なし） · `004e68f4`（命令位置の公開資料なし） · `004e6900`（命令位置の公開資料なし）

~~~diff
- 004e68d8 ["INT_ADD", "register:40f0:8", ["const:4e68d8:8", "const:4:8"]]
- 004e68d8 ["CALL", null, ["callee:00c57f10:8"]]
+ 004e6918 ["INT_ADD", "register:40f0:8", ["const:4e6918:8", "const:4:8"]]
+ 004e6918 ["CALL", null, ["callee:00c57f10:8"]]
- 004e68d8 bytes 8ec41d94
+ 004e6918 bytes 7ec51d94
- 004e68b4 ["INT_ADD", "register:40f0:8", ["const:4e68b4:8", "const:4:8"]]
- 004e68b4 ["CALL", null, ["callee:00c57ef0:8"]]
+ 004e68f4 ["INT_ADD", "register:40f0:8", ["const:4e68f4:8", "const:4:8"]]
+ 004e68f4 ["CALL", null, ["callee:00c57ef0:8"]]
- 004e68b4 bytes 8fc41d94
+ 004e68f4 bytes 7fc51d94
- 004e68c0 ["INT_ADD", "register:40f0:8", ["const:4e68c0:8", "const:4:8"]]
- 004e68c0 ["CALL", null, ["callee:00c58fa0:8"]]
+ 004e6900 ["INT_ADD", "register:40f0:8", ["const:4e6900:8", "const:4:8"]]
+ 004e6900 ["CALL", null, ["callee:00c58fa0:8"]]
- 004e68c0 bytes b8c81d94
+ 004e6900 bytes a8c91d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce8f0b8a13352948e8d586ddf1cb1724"></a>

### [`004e691c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e6/004e691c.md) → [`004e695c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e6/004e695c.md) _ZNK5Botan4EMSA15config_for_x509ERKNS_11Private_KeyERKNSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c57f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

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
      "definition_site": "004e69a4",
      "incomplete_value": false,
      "site": "004e69b0",
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
            "const:63b:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 2,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e69d0",
      "incomplete_value": false,
      "site": "004e69d8",
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
            "const:be9:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e6a20",
      "incomplete_value": true,
      "site": "004e6a2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004e69e0",
      "incomplete_value": true,
      "site": "004e69ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bd0:8"
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
      "004e69a4",
      "PARAM",
      [
        "storage",
        "002a655f",
        null,
        "string"
      ]
    ],
    [
      "004e69d0",
      "PARAM",
      [
        "storage",
        "002a9b1c",
        null,
        "string"
      ]
    ],
    [
      "004e6a1c",
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
      "004e69a4",
      "PARAM",
      [
        "storage",
        "002a663b",
        null,
        "string"
      ]
    ],
    [
      "004e69d0",
      "PARAM",
      [
        "storage",
        "002a9be9",
        null,
        "string"
      ]
    ],
    [
      "004e6a1c",
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

- 旧版 [`004e6970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e6/004e691c.md#insn-004e6970) · [`004e6998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e6/004e691c.md#insn-004e6998) · [`004e69ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e6/004e691c.md#insn-004e69ec)
- 新版 `004e69b0`（命令位置の公開資料なし） · `004e69d8`（命令位置の公開資料なし） · `004e6a2c`（命令位置の公開資料なし）

~~~diff
- 004e6970 ["INT_ADD", "register:40f0:8", ["const:4e6970:8", "const:4:8"]]
- 004e6970 ["CALL", null, ["callee:00c57f60:8"]]
+ 004e69b0 ["INT_ADD", "register:40f0:8", ["const:4e69b0:8", "const:4:8"]]
+ 004e69b0 ["CALL", null, ["callee:00c57f60:8"]]
- 004e6970 bytes 7cc41d94
+ 004e69b0 bytes 6cc51d94
- 004e6998 ["INT_ADD", "register:40f0:8", ["const:4e6998:8", "const:4:8"]]
- 004e6998 ["CALL", null, ["callee:00c57f70:8"]]
+ 004e69d8 ["INT_ADD", "register:40f0:8", ["const:4e69d8:8", "const:4:8"]]
+ 004e69d8 ["CALL", null, ["callee:00c57f70:8"]]
- 004e6998 bytes 76c41d94
+ 004e69d8 bytes 66c51d94
- 004e69ec ["INT_ADD", "register:40f0:8", ["const:4e69ec:8", "const:4:8"]]
- 004e69ec ["CALL", null, ["callee:00c57f10:8"]]
+ 004e6a2c ["INT_ADD", "register:40f0:8", ["const:4e6a2c:8", "const:4:8"]]
+ 004e6a2c ["CALL", null, ["callee:00c57f10:8"]]
- 004e69ec bytes 49c41d94
+ 004e6a2c bytes 39c51d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bec9a48ce5118f1dc50823f144b0366e"></a>

### [`004e6a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e6/004e6a98.md) → [`004e6ad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e6/004e6ad8.md) _ZN5Botan8get_emsaERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c590f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c590f0.md) · 呼出先 16件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00c594f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c594f0.md) · 呼出先 16件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.78% / 新版 99.78%

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
      "definition_site": "004e71bc",
      "incomplete_value": true,
      "site": "004e71c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 37,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e71b8",
      "incomplete_value": false,
      "site": "004e71c4",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004e7178",
      "incomplete_value": false,
      "site": "004e7184",
      "value": [
        "leaf",
        "const:535828:8"
      ]
    },
    "ordinal": 37,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004e71b8",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004e71bc",
      "READ",
      [
        "storage",
        "00c9aad0",
        null,
        "pointer"
      ]
    ],
    [
      "004e71bc",
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
      "004e71b8",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004e71bc",
      "READ",
      [
        "storage",
        "00c9aed0",
        null,
        "pointer"
      ]
    ],
    [
      "004e71bc",
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

- 旧版 [`004e7144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e6/004e6a98.md#insn-004e7144) · [`004e7184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e6/004e6a98.md#insn-004e7184) · [`004e6ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e6/004e6a98.md#insn-004e6ae0)
- 新版 `004e7184`（命令位置の公開資料なし） · `004e71c4`（命令位置の公開資料なし） · `004e6b20`（命令位置の公開資料なし）

~~~diff
- 004e7144 ["INT_ADD", "register:40f0:8", ["const:4e7144:8", "const:4:8"]]
- 004e7144 ["CALL", null, ["callee:00c59530:8"]]
+ 004e7184 ["INT_ADD", "register:40f0:8", ["const:4e7184:8", "const:4:8"]]
+ 004e7184 ["CALL", null, ["callee:00c59530:8"]]
- 004e7144 bytes fbc71d94
+ 004e7184 bytes ebc81d94
- 004e7184 ["INT_ADD", "register:40f0:8", ["const:4e7184:8", "const:4:8"]]
- 004e7184 ["CALL", null, ["callee:00c57f10:8"]]
+ 004e71c4 ["INT_ADD", "register:40f0:8", ["const:4e71c4:8", "const:4:8"]]
+ 004e71c4 ["CALL", null, ["callee:00c57f10:8"]]
- 004e7184 bytes 63c21d94
+ 004e71c4 bytes 53c31d94
- 004e6ae0 ["INT_ADD", "register:40f0:8", ["const:4e6ae0:8", "const:4:8"]]
- 004e6ae0 ["CALL", null, ["callee:0043bb20:8"]]
+ 004e6b20 ["INT_ADD", "register:40f0:8", ["const:4e6b20:8", "const:4:8"]]
+ 004e6b20 ["CALL", null, ["callee:0043bb20:8"]]
- 004e6ae0 bytes 0054fd97
+ 004e6b20 bytes 0054fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53e1fd82e5a67a0e3110f4574fd1b35d"></a>

### [`004e7604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e7604.md) → [`004e7644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e7/004e7644.md) _ZN5Botan16get_sig_paddingsENSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c589d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c589d0.md) · 呼出先 5件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`0054071c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/0054071c.md) [`005454fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/005454fc.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00c58dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58dd0.md) · 呼出先 5件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`0054075c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/0054075c.md) [`0054553c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00545/0054553c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.02% / 新版 98.02%

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
      "definition_site": "004e767c",
      "incomplete_value": true,
      "site": "004e767c",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e7748",
      "incomplete_value": false,
      "site": "004e7754",
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
            "const:268:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e77cc",
      "incomplete_value": false,
      "site": "004e77d0",
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
            "const:1bd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004e778c",
      "incomplete_value": false,
      "site": "004e7790",
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
            "const:f0:8"
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
      "004e7678",
      "READ",
      [
        "storage",
        "00ca4e70",
        null,
        "undefined8"
      ]
    ],
    [
      "004e7748",
      "PARAM",
      [
        "storage",
        "00ca4e68",
        null,
        null
      ]
    ],
    [
      "004e77cc",
      "PARAM",
      [
        "storage",
        "002a00f0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004e7678",
      "READ",
      [
        "storage",
        "00ca5270",
        null,
        "undefined8"
      ]
    ],
    [
      "004e7748",
      "PARAM",
      [
        "storage",
        "00ca5268",
        null,
        null
      ]
    ],
    [
      "004e77cc",
      "PARAM",
      [
        "storage",
        "002a01bd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e7714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e7604.md#insn-004e7714) · [`004e7790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e7604.md#insn-004e7790) · [`004e7634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e7604.md#insn-004e7634)
- 新版 `004e7754`（命令位置の公開資料なし） · `004e77d0`（命令位置の公開資料なし） · `004e7674`（命令位置の公開資料なし）

~~~diff
- 004e7714 ["INT_ADD", "register:40f0:8", ["const:4e7714:8", "const:4:8"]]
- 004e7714 ["CALL", null, ["callee:0054553c:8"]]
+ 004e7754 ["INT_ADD", "register:40f0:8", ["const:4e7754:8", "const:4:8"]]
+ 004e7754 ["CALL", null, ["callee:0054553c:8"]]
- 004e7714 bytes 7a770194
+ 004e7754 bytes 7a770194
- 004e7790 ["INT_ADD", "register:40f0:8", ["const:4e7790:8", "const:4:8"]]
- 004e7790 ["CALL", null, ["callee:00442930:8"]]
+ 004e77d0 ["INT_ADD", "register:40f0:8", ["const:4e77d0:8", "const:4:8"]]
+ 004e77d0 ["CALL", null, ["callee:00442930:8"]]
- 004e7790 bytes 586cfd97
+ 004e77d0 bytes 586cfd97
- 004e7634 ["COPY", "register:4048:8", ["const:ca4000:8"]]
+ 004e7674 ["COPY", "register:4048:8", ["const:ca5000:8"]]
- 004e7634 bytes e93d00b0
+ 004e7674 bytes e93d00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82676db37d092c482802b1441111b9b0"></a>

### [`004e7798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e7798.md) → [`004e77d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e7/004e77d8.md) _ZN5Botan7BlinderC2ERKNS_6BigIntERNS_21RandomNumberGeneratorENSt6__ndk18functionIFS1_S3_EEES9_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59b90.md) · 呼出先 6件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58ee0.md) [`00c58f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58f50.md)
- 新版 呼出元 1件 [`00c59f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59f90.md) · 呼出先 6件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c592e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c592e0.md) [`00c59350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59350.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.92% / 新版 96.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004e79d0",
      "incomplete_value": true,
      "site": "004e79d0",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
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
    "ordinal": 7,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004e7a54",
      "incomplete_value": true,
      "site": "004e7a54",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "004e7a14",
      "incomplete_value": true,
      "site": "004e7a14",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 10,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004e7a80",
      "incomplete_value": true,
      "site": "004e7a80",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "004e7a40",
      "incomplete_value": true,
      "site": "004e7a40",
      "value": [
        "LOAD",
        "8",
        [
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
      "004e79c0",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004e7a44",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004e7a70",
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
      "004e79c0",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004e7a44",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004e7a70",
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

- 旧版 [`004e7990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e7798.md#insn-004e7990) · [`004e7a14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e7798.md#insn-004e7a14) · [`004e7a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e7798.md#insn-004e7a40)
- 新版 `004e79d0`（命令位置の公開資料なし） · `004e7a54`（命令位置の公開資料なし） · `004e7a80`（命令位置の公開資料なし）

~~~diff
- 004e7990 ["COPY", "register:0:8", ["register:4048:8"]]
- 004e7990 ["INT_ADD", "register:40f0:8", ["const:4e7990:8", "const:4:8"]]
- 004e7990 ["CALLIND", null, ["register:0:8"]]
+ 004e79d0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e79d0 ["INT_ADD", "register:40f0:8", ["const:4e79d0:8", "const:4:8"]]
+ 004e79d0 ["CALLIND", null, ["register:0:8"]]
- 004e7990 bytes 20013fd6
+ 004e79d0 bytes 20013fd6
- 004e7a14 ["COPY", "register:0:8", ["register:4048:8"]]
- 004e7a14 ["INT_ADD", "register:40f0:8", ["const:4e7a14:8", "const:4:8"]]
- 004e7a14 ["CALLIND", null, ["register:0:8"]]
+ 004e7a54 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e7a54 ["INT_ADD", "register:40f0:8", ["const:4e7a54:8", "const:4:8"]]
+ 004e7a54 ["CALLIND", null, ["register:0:8"]]
- 004e7a14 bytes 20013fd6
+ 004e7a54 bytes 20013fd6
- 004e7a40 ["COPY", "register:0:8", ["register:4048:8"]]
- 004e7a40 ["INT_ADD", "register:40f0:8", ["const:4e7a40:8", "const:4:8"]]
- 004e7a40 ["CALLIND", null, ["register:0:8"]]
+ 004e7a80 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e7a80 ["INT_ADD", "register:40f0:8", ["const:4e7a80:8", "const:4:8"]]
+ 004e7a80 ["CALLIND", null, ["register:0:8"]]
- 004e7a40 bytes 20013fd6
+ 004e7a80 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a25ec4a4a9ad7e4f60ed08fc7c5a68a"></a>

### [`004e7b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e7b80.md) → [`004e7bc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e7/004e7bc0.md) _ZNK5Botan7Blinder5blindERKNS_6BigIntE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c59150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59150.md) · 呼出先 13件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 1件 [`00c59550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59550.md) · 呼出先 13件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 8件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004e7ca8",
      "incomplete_value": true,
      "site": "004e7ca8",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004e7d30",
      "incomplete_value": true,
      "site": "004e7d30",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
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
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004e7d60",
      "incomplete_value": true,
      "site": "004e7d60",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "004e7d20",
      "incomplete_value": true,
      "site": "004e7d20",
      "value": [
        "LOAD",
        "8",
        [
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
      "004e7c98",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004e7d20",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004e7d50",
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
      "004e7c98",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004e7d20",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004e7d50",
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

- 旧版 [`004e7c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e7b80.md#insn-004e7c68) · [`004e7ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e7b80.md#insn-004e7ce0) · [`004e7cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e7b80.md#insn-004e7cf0)
- 新版 `004e7ca8`（命令位置の公開資料なし） · `004e7d20`（命令位置の公開資料なし） · `004e7d30`（命令位置の公開資料なし）

~~~diff
- 004e7c68 ["COPY", "register:0:8", ["register:4048:8"]]
- 004e7c68 ["INT_ADD", "register:40f0:8", ["const:4e7c68:8", "const:4:8"]]
- 004e7c68 ["CALLIND", null, ["register:0:8"]]
+ 004e7ca8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e7ca8 ["INT_ADD", "register:40f0:8", ["const:4e7ca8:8", "const:4:8"]]
+ 004e7ca8 ["CALLIND", null, ["register:0:8"]]
- 004e7c68 bytes 20013fd6
+ 004e7ca8 bytes 20013fd6
- 004e7ce0 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:338:8"]]
- 004e7ce0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004e7d20 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:738:8"]]
+ 004e7d20 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004e7ce0 bytes 299f41f9
+ 004e7d20 bytes 299f43f9
- 004e7cf0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004e7cf0 ["INT_ADD", "register:40f0:8", ["const:4e7cf0:8", "const:4:8"]]
- 004e7cf0 ["CALLIND", null, ["register:0:8"]]
+ 004e7d30 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e7d30 ["INT_ADD", "register:40f0:8", ["const:4e7d30:8", "const:4:8"]]
+ 004e7d30 ["CALLIND", null, ["register:0:8"]]
- 004e7cf0 bytes 20013fd6
+ 004e7d30 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1db219ca0b6fdff0db8f1558170f7412"></a>

### [`004e8018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8018.md) → [`004e8058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e8/004e8058.md) _ZNK5Botan7Blinder7unblindERKNS_6BigIntE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59160.md) · 呼出先 10件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`00c59560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59560.md) · 呼出先 10件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
      "definition_site": "004e80d0",
      "incomplete_value": true,
      "site": "004e80d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e8110",
      "incomplete_value": false,
      "site": "004e8118",
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
    "old": {
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e8148",
      "incomplete_value": true,
      "site": "004e8154",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
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
      "004e80c0",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004e8110",
      "PARAM",
      [
        "storage",
        "002ae852",
        null,
        "string"
      ]
    ],
    [
      "004e8144",
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
      "004e80c0",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004e8110",
      "PARAM",
      [
        "storage",
        "002ae892",
        null,
        "string"
      ]
    ],
    [
      "004e8144",
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

- 旧版 [`004e8090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8018.md#insn-004e8090) · [`004e8098`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8018.md#insn-004e8098) · [`004e80d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8018.md#insn-004e80d0)
- 新版 `004e80d0`（命令位置の公開資料なし） · `004e80d8`（命令位置の公開資料なし） · `004e8110`（命令位置の公開資料なし）

~~~diff
- 004e8090 ["COPY", "register:0:8", ["register:4048:8"]]
- 004e8090 ["INT_ADD", "register:40f0:8", ["const:4e8090:8", "const:4:8"]]
- 004e8090 ["CALLIND", null, ["register:0:8"]]
+ 004e80d0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e80d0 ["INT_ADD", "register:40f0:8", ["const:4e80d0:8", "const:4:8"]]
+ 004e80d0 ["CALLIND", null, ["register:0:8"]]
- 004e8090 bytes 20013fd6
+ 004e80d0 bytes 20013fd6
- 004e8098 ["INT_ADD", "register:40f0:8", ["const:4e8098:8", "const:4:8"]]
- 004e8098 ["CALL", null, ["callee:00c58660:8"]]
+ 004e80d8 ["INT_ADD", "register:40f0:8", ["const:4e80d8:8", "const:4:8"]]
+ 004e80d8 ["CALL", null, ["callee:00c58660:8"]]
- 004e8098 bytes 72c01d94
+ 004e80d8 bytes 62c11d94
- 004e80d0 ["COPY", "tmp:0:8", ["const:852:8"]]
- 004e80d0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004e80d0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004e80d0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004e8110 ["COPY", "tmp:0:8", ["const:892:8"]]
+ 004e8110 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004e8110 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004e8110 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004e80d0 bytes 21482191
+ 004e8110 bytes 21482291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d84ac51698fdef63001e431c4381b57"></a>

### [`004e8178`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8178.md) → [`004e81b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e8/004e81b8.md) _ZN5Botan15load_public_keyERKNS_19AlgorithmIdentifierERKNSt6__ndk16vectorIhNS3_9allocatorIhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59170.md) · 呼出先 16件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00547b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547b2c.md) [`00547b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547b30.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00c59570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59570.md) · 呼出先 16件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00547b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547b6c.md) [`00547b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547b70.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "004e81f8",
      "incomplete_value": false,
      "site": "004e8200",
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
    "old": {
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e8390",
      "incomplete_value": false,
      "site": "004e839c",
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
            "const:101:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 11,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e83cc",
      "incomplete_value": true,
      "site": "004e83d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004e8200",
      "DATA",
      [
        "storage",
        "00c6a2b0",
        null,
        "undefined *"
      ]
    ],
    [
      "004e8244",
      "READ",
      [
        "storage",
        "00c6a2d0",
        null,
        "pointer"
      ]
    ],
    [
      "004e8244",
      "READ",
      [
        "storage",
        "00c6a2d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004e8200",
      "DATA",
      [
        "storage",
        "00c6a6b0",
        null,
        "undefined *"
      ]
    ],
    [
      "004e8244",
      "READ",
      [
        "storage",
        "00c6a6d0",
        null,
        "pointer"
      ]
    ],
    [
      "004e8244",
      "READ",
      [
        "storage",
        "00c6a6d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e835c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8178.md#insn-004e835c) · [`004e8388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8178.md#insn-004e8388) · [`004e8398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8178.md#insn-004e8398)
- 新版 `004e839c`（命令位置の公開資料なし） · `004e83c8`（命令位置の公開資料なし） · `004e83d8`（命令位置の公開資料なし）

~~~diff
- 004e835c ["INT_ADD", "register:40f0:8", ["const:4e835c:8", "const:4:8"]]
- 004e835c ["CALL", null, ["callee:00c580b0:8"]]
+ 004e839c ["INT_ADD", "register:40f0:8", ["const:4e839c:8", "const:4:8"]]
+ 004e839c ["CALL", null, ["callee:00c580b0:8"]]
- 004e835c bytes 55be1d94
+ 004e839c bytes 45bf1d94
- 004e8388 ["COPY", "register:4010:8", ["const:535828:8"]]
+ 004e83c8 ["COPY", "register:4010:8", ["const:535868:8"]]
- 004e8388 bytes 02a52610
+ 004e83c8 bytes 02a52610
- 004e8398 ["INT_ADD", "register:40f0:8", ["const:4e8398:8", "const:4:8"]]
- 004e8398 ["CALL", null, ["callee:00c57f10:8"]]
+ 004e83d8 ["INT_ADD", "register:40f0:8", ["const:4e83d8:8", "const:4:8"]]
+ 004e83d8 ["CALL", null, ["callee:00c57f10:8"]]
- 004e8398 bytes debd1d94
+ 004e83d8 bytes cebe1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53bc8cbee07de59a43ec8c5325c431f1"></a>

### [`004e8548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8548.md) → [`004e8588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e8/004e8588.md) _ZN5Botan13RSA_PublicKeyC1ERKNS_19AlgorithmIdentifierERKNSt6__ndk16vectorIhNS4_9allocatorIhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59180.md) · 呼出先 7件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58300.md) [`00c58310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58310.md) [`00c58480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58480.md)
- 新版 呼出元 1件 [`00c59580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59580.md) · 呼出先 7件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c58700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58700.md) [`00c58710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58710.md) [`00c58880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58880.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.86% / 新版 91.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e85b8",
      "incomplete_value": true,
      "site": "004e85c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004e8668",
      "incomplete_value": true,
      "site": "004e8668",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004e86ac",
      "incomplete_value": true,
      "site": "004e86ac",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004e866c",
      "incomplete_value": true,
      "site": "004e866c",
      "value": [
        "LOAD",
        "8",
        [
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
      "004e85a8",
      "READ",
      [
        "storage",
        "00c9abd8",
        null,
        "pointer"
      ]
    ],
    [
      "004e85c0",
      "DATA",
      [
        "storage",
        "00c66ca8",
        null,
        "undefined1[240]"
      ]
    ],
    [
      "004e8658",
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
      "004e85a8",
      "READ",
      [
        "storage",
        "00c9afd8",
        null,
        "pointer"
      ]
    ],
    [
      "004e85c0",
      "DATA",
      [
        "storage",
        "00c670a8",
        null,
        "undefined1[240]"
      ]
    ],
    [
      "004e8658",
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

- 旧版 [`004e85e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8548.md#insn-004e85e8) · [`004e8628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8548.md#insn-004e8628) · [`004e866c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8548.md#insn-004e866c)
- 新版 `004e8628`（命令位置の公開資料なし） · `004e8668`（命令位置の公開資料なし） · `004e86ac`（命令位置の公開資料なし）

~~~diff
- 004e85e8 ["INT_ADD", "register:40f0:8", ["const:4e85e8:8", "const:4:8"]]
- 004e85e8 ["CALL", null, ["callee:00c58710:8"]]
+ 004e8628 ["INT_ADD", "register:40f0:8", ["const:4e8628:8", "const:4:8"]]
+ 004e8628 ["CALL", null, ["callee:00c58710:8"]]
- 004e85e8 bytes 4abf1d94
+ 004e8628 bytes 3ac01d94
- 004e8628 ["COPY", "register:0:8", ["register:4048:8"]]
- 004e8628 ["INT_ADD", "register:40f0:8", ["const:4e8628:8", "const:4:8"]]
- 004e8628 ["CALLIND", null, ["register:0:8"]]
+ 004e8668 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e8668 ["INT_ADD", "register:40f0:8", ["const:4e8668:8", "const:4:8"]]
+ 004e8668 ["CALLIND", null, ["register:0:8"]]
- 004e8628 bytes 20013fd6
+ 004e8668 bytes 20013fd6
- 004e866c ["COPY", "register:0:8", ["register:4048:8"]]
- 004e866c ["INT_ADD", "register:40f0:8", ["const:4e866c:8", "const:4:8"]]
- 004e866c ["CALLIND", null, ["register:0:8"]]
+ 004e86ac ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e86ac ["INT_ADD", "register:40f0:8", ["const:4e86ac:8", "const:4:8"]]
+ 004e86ac ["CALLIND", null, ["register:0:8"]]
- 004e866c bytes 20013fd6
+ 004e86ac bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-969087977d3e3e0034fa8d055b4c2f26"></a>

### [`004e86f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e86f4.md) → [`004e8734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e8/004e8734.md) _ZN5Botan16load_private_keyERKNS_19AlgorithmIdentifierERKNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59190.md) · 呼出先 12件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 1件 [`00c59590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59590.md) · 呼出先 12件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

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
      "definition_site": "004e8828",
      "incomplete_value": false,
      "site": "004e8834",
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
            "const:ba2:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 6,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e887c",
      "incomplete_value": true,
      "site": "004e8888",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004e8878",
      "incomplete_value": false,
      "site": "004e8888",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004e8838",
      "incomplete_value": false,
      "site": "004e8848",
      "value": [
        "leaf",
        "const:535828:8"
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
      "004e8828",
      "PARAM",
      [
        "storage",
        "002b0b62",
        null,
        "string"
      ]
    ],
    [
      "004e8878",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004e887c",
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
      "004e8828",
      "PARAM",
      [
        "storage",
        "002b0ba2",
        null,
        "string"
      ]
    ],
    [
      "004e8878",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004e887c",
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

- 旧版 [`004e87f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e86f4.md#insn-004e87f4) · [`004e8848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e86f4.md#insn-004e8848) · [`004e886c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e86f4.md#insn-004e886c)
- 新版 `004e8834`（命令位置の公開資料なし） · `004e8888`（命令位置の公開資料なし） · `004e88ac`（命令位置の公開資料なし）

~~~diff
- 004e87f4 ["INT_ADD", "register:40f0:8", ["const:4e87f4:8", "const:4:8"]]
- 004e87f4 ["CALL", null, ["callee:00c57f60:8"]]
+ 004e8834 ["INT_ADD", "register:40f0:8", ["const:4e8834:8", "const:4:8"]]
+ 004e8834 ["CALL", null, ["callee:00c57f60:8"]]
- 004e87f4 bytes dbbc1d94
+ 004e8834 bytes cbbd1d94
- 004e8848 ["INT_ADD", "register:40f0:8", ["const:4e8848:8", "const:4:8"]]
- 004e8848 ["CALL", null, ["callee:00c57f10:8"]]
+ 004e8888 ["INT_ADD", "register:40f0:8", ["const:4e8888:8", "const:4:8"]]
+ 004e8888 ["CALL", null, ["callee:00c57f10:8"]]
- 004e8848 bytes b2bc1d94
+ 004e8888 bytes a2bd1d94
- 004e886c ["INT_ADD", "register:40f0:8", ["const:4e886c:8", "const:4:8"]]
- 004e886c ["CALL", null, ["callee:00c580b0:8"]]
+ 004e88ac ["INT_ADD", "register:40f0:8", ["const:4e88ac:8", "const:4:8"]]
+ 004e88ac ["CALL", null, ["callee:00c580b0:8"]]
- 004e886c bytes 11bd1d94
+ 004e88ac bytes 01be1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba36c0552375b5be4ff6885817e7442a"></a>

### [`004e8960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8960.md) → [`004e89a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e8/004e89a0.md) _ZN5Botan14RSA_PrivateKeyC1ERKNS_19AlgorithmIdentifierERKNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c591a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c591a0.md) · 呼出先 14件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 1件 [`00c595a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c595a0.md) · 呼出先 14件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.61% / 新版 90.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 2件, `store_value` 5件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e8a10",
      "incomplete_value": true,
      "site": "004e8a10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e89ec",
      "incomplete_value": true,
      "site": "004e8a2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 24,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e8aa8",
      "incomplete_value": true,
      "site": "004e8abc",
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
      "004e89cc",
      "READ",
      [
        "storage",
        "00c9abe0",
        null,
        "pointer"
      ]
    ],
    [
      "004e8a10",
      "DATA",
      [
        "storage",
        "00c66eb8",
        null,
        "undefined1[528]"
      ]
    ],
    [
      "004e8a2c",
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
      "004e89cc",
      "READ",
      [
        "storage",
        "00c9afe0",
        null,
        "pointer"
      ]
    ],
    [
      "004e8a10",
      "DATA",
      [
        "storage",
        "00c672b8",
        null,
        "undefined1[528]"
      ]
    ],
    [
      "004e8a2c",
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

- 旧版 [`004e8ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8960.md#insn-004e8ac0) · [`004e8b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8960.md#insn-004e8b2c) · [`004e8b6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8960.md#insn-004e8b6c)
- 新版 `004e8b00`（命令位置の公開資料なし） · `004e8b6c`（命令位置の公開資料なし） · `004e8bac`（命令位置の公開資料なし）

~~~diff
- 004e8ac0 ["INT_ADD", "register:40f0:8", ["const:4e8ac0:8", "const:4:8"]]
- 004e8ac0 ["CALL", null, ["callee:00c588c0:8"]]
+ 004e8b00 ["INT_ADD", "register:40f0:8", ["const:4e8b00:8", "const:4:8"]]
+ 004e8b00 ["CALL", null, ["callee:00c588c0:8"]]
- 004e8ac0 bytes 80be1d94
+ 004e8b00 bytes 70bf1d94
- 004e8b2c ["INT_ADD", "register:40f0:8", ["const:4e8b2c:8", "const:4:8"]]
- 004e8b2c ["CALL", null, ["callee:00c57eb0:8"]]
+ 004e8b6c ["INT_ADD", "register:40f0:8", ["const:4e8b6c:8", "const:4:8"]]
+ 004e8b6c ["CALL", null, ["callee:00c57eb0:8"]]
- 004e8b2c bytes e1bb1d94
+ 004e8b6c bytes d1bc1d94
- 004e8b6c ["COPY", "register:0:8", ["register:4048:8"]]
- 004e8b6c ["INT_ADD", "register:40f0:8", ["const:4e8b6c:8", "const:4:8"]]
- 004e8b6c ["CALLIND", null, ["register:0:8"]]
+ 004e8bac ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e8bac ["INT_ADD", "register:40f0:8", ["const:4e8bac:8", "const:4:8"]]
+ 004e8bac ["CALLIND", null, ["register:0:8"]]
- 004e8b6c bytes 20013fd6
+ 004e8bac bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-287242845f2fadfe7644d66d2be6a83b"></a>

### [`004e8dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8dc0.md) → [`004e8e00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004e8/004e8e00.md) _ZN5Botan14RSA_PrivateKeyC1ERNS_21RandomNumberGeneratorEmm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c591b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c591b0.md) · 呼出先 17件 [`004a680c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a680c.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`00c595b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c595b0.md) · 呼出先 17件 [`004a684c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a684c.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
      "definition_site": "004e8e50",
      "incomplete_value": true,
      "site": "004e8e58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004e8e70",
      "incomplete_value": true,
      "site": "004e8e70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004e8f70",
      "incomplete_value": true,
      "site": "004e8f70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004e8e3c",
      "READ",
      [
        "storage",
        "00c9abe0",
        null,
        "pointer"
      ]
    ],
    [
      "004e8e58",
      "DATA",
      [
        "storage",
        "00c66d98",
        null,
        "undefined1[528]"
      ]
    ],
    [
      "004e8e70",
      "DATA",
      [
        "storage",
        "00c66eb8",
        null,
        "undefined1[528]"
      ]
    ]
  ],
  "added": [
    [
      "004e8e3c",
      "READ",
      [
        "storage",
        "00c9afe0",
        null,
        "pointer"
      ]
    ],
    [
      "004e8e58",
      "DATA",
      [
        "storage",
        "00c67198",
        null,
        "undefined1[528]"
      ]
    ],
    [
      "004e8e70",
      "DATA",
      [
        "storage",
        "00c672b8",
        null,
        "undefined1[528]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004e8f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8dc0.md#insn-004e8f30) · [`004e8fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8dc0.md#insn-004e8fd0) · [`004e90cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e8/004e8dc0.md#insn-004e90cc)
- 新版 `004e8f70`（命令位置の公開資料なし） · `004e9010`（命令位置の公開資料なし） · `004e910c`（命令位置の公開資料なし）

~~~diff
- 004e8f30 ["COPY", "register:0:8", ["register:4048:8"]]
- 004e8f30 ["INT_ADD", "register:40f0:8", ["const:4e8f30:8", "const:4:8"]]
- 004e8f30 ["CALLIND", null, ["register:0:8"]]
+ 004e8f70 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e8f70 ["INT_ADD", "register:40f0:8", ["const:4e8f70:8", "const:4:8"]]
+ 004e8f70 ["CALLIND", null, ["register:0:8"]]
- 004e8f30 bytes 20013fd6
+ 004e8f70 bytes 20013fd6
- 004e8fd0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004e8fd0 ["INT_ADD", "register:40f0:8", ["const:4e8fd0:8", "const:4:8"]]
- 004e8fd0 ["CALLIND", null, ["register:0:8"]]
+ 004e9010 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e9010 ["INT_ADD", "register:40f0:8", ["const:4e9010:8", "const:4:8"]]
+ 004e9010 ["CALLIND", null, ["register:0:8"]]
- 004e8fd0 bytes 20013fd6
+ 004e9010 bytes 20013fd6
- 004e90cc ["COPY", "register:0:8", ["register:4048:8"]]
- 004e90cc ["INT_ADD", "register:40f0:8", ["const:4e90cc:8", "const:4:8"]]
- 004e90cc ["CALLIND", null, ["register:0:8"]]
+ 004e910c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004e910c ["INT_ADD", "register:40f0:8", ["const:4e910c:8", "const:4:8"]]
+ 004e910c ["CALLIND", null, ["register:0:8"]]
- 004e90cc bytes 20013fd6
+ 004e910c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-515639a38fafdd13ca7eda718ed13dea"></a>

### [`004ea1e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004ea1e4.md) → [`004ea224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ea/004ea224.md) FUN_004ea224

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)

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
      "definition_site": "004ea240",
      "incomplete_value": true,
      "site": "004ea240",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ea274",
      "incomplete_value": true,
      "site": "004ea278",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
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
      "004ea238",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "004ea240",
      "DATA",
      [
        "storage",
        "00c67028",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004ea270",
      "READ",
      [
        "storage",
        "00c9abf0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ea238",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "004ea240",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004ea270",
      "READ",
      [
        "storage",
        "00c9aff0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ea1f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004ea1e4.md#insn-004ea1f8) · [`004ea228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004ea1e4.md#insn-004ea228) · [`004ea230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004ea1e4.md#insn-004ea230)
- 新版 `004ea238`（命令位置の公開資料なし） · `004ea268`（命令位置の公開資料なし） · `004ea270`（命令位置の公開資料なし）

~~~diff
- 004ea1f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d0:8"]]
- 004ea1f8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ea238 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 004ea238 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004ea1f8 bytes 08e944f9
+ 004ea238 bytes 08e946f9
- 004ea228 ["INT_ADD", "register:40f0:8", ["const:4ea228:8", "const:4:8"]]
- 004ea228 ["CALL", null, ["callee:0043bb20:8"]]
+ 004ea268 ["INT_ADD", "register:40f0:8", ["const:4ea268:8", "const:4:8"]]
+ 004ea268 ["CALL", null, ["callee:0043bb20:8"]]
- 004ea228 bytes 2e46fd97
+ 004ea268 bytes 2e46fd97
- 004ea230 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bf0:8"]]
- 004ea230 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ea270 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ff0:8"]]
+ 004ea270 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004ea230 bytes 08f945f9
+ 004ea270 bytes 08f947f9
~~~


<a id="compare-4d311b8e88268c57149cbfacf6da78d2"></a>

### [`004ea25c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004ea25c.md) → [`004ea29c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ea/004ea29c.md) _ZNK5Botan11Private_Key16private_key_infoEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c591e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c591e0.md) · 呼出先 11件 [`00535b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b40.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c582b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c582b0.md)
- 新版 呼出元 1件 [`00c595e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c595e0.md) · 呼出先 11件 [`00535b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c586b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586b0.md)

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
      "definition_site": "004ea328",
      "incomplete_value": true,
      "site": "004ea328",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004ea3bc",
      "incomplete_value": true,
      "site": "004ea3bc",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 11,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004ea448",
      "incomplete_value": true,
      "site": "004ea448",
      "value": [
        "LOAD",
        "8",
        [
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
      "004ea318",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004ea3ac",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004ea438",
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
      "004ea318",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004ea3ac",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004ea438",
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

- 旧版 [`004ea2e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004ea25c.md#insn-004ea2e8) · [`004ea37c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004ea25c.md#insn-004ea37c) · [`004ea408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004ea25c.md#insn-004ea408)
- 新版 `004ea328`（命令位置の公開資料なし） · `004ea3bc`（命令位置の公開資料なし） · `004ea448`（命令位置の公開資料なし）

~~~diff
- 004ea2e8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004ea2e8 ["INT_ADD", "register:40f0:8", ["const:4ea2e8:8", "const:4:8"]]
- 004ea2e8 ["CALLIND", null, ["register:0:8"]]
+ 004ea328 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004ea328 ["INT_ADD", "register:40f0:8", ["const:4ea328:8", "const:4:8"]]
+ 004ea328 ["CALLIND", null, ["register:0:8"]]
- 004ea2e8 bytes 20013fd6
+ 004ea328 bytes 20013fd6
- 004ea37c ["COPY", "register:0:8", ["register:4048:8"]]
- 004ea37c ["INT_ADD", "register:40f0:8", ["const:4ea37c:8", "const:4:8"]]
- 004ea37c ["CALLIND", null, ["register:0:8"]]
+ 004ea3bc ["COPY", "register:0:8", ["register:4048:8"]]
+ 004ea3bc ["INT_ADD", "register:40f0:8", ["const:4ea3bc:8", "const:4:8"]]
+ 004ea3bc ["CALLIND", null, ["register:0:8"]]
- 004ea37c bytes 20013fd6
+ 004ea3bc bytes 20013fd6
- 004ea408 ["COPY", "register:0:8", ["register:4048:8"]]
- 004ea408 ["INT_ADD", "register:40f0:8", ["const:4ea408:8", "const:4:8"]]
- 004ea408 ["CALLIND", null, ["register:0:8"]]
+ 004ea448 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004ea448 ["INT_ADD", "register:40f0:8", ["const:4ea448:8", "const:4:8"]]
+ 004ea448 ["CALLIND", null, ["register:0:8"]]
- 004ea408 bytes 20013fd6
+ 004ea448 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d41bdd025967447473b2ca11ba1f1c56"></a>

### [`004ea628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004ea628.md) → [`004ea668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ea/004ea668.md) _ZNK5Botan10Public_Key20create_encryption_opERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEE

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
      "definition_site": "004ea6f0",
      "incomplete_value": true,
      "site": "004ea6f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ea728",
      "incomplete_value": true,
      "site": "004ea72c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ea6b4",
      "incomplete_value": false,
      "site": "004ea6bc",
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
      "004ea6b4",
      "PARAM",
      [
        "storage",
        "002bed28",
        null,
        "string"
      ]
    ],
    [
      "004ea6dc",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "004ea6f0",
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
      "004ea6b4",
      "PARAM",
      [
        "storage",
        "002bed68",
        null,
        "string"
      ]
    ],
    [
      "004ea6dc",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "004ea6f0",
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

- 旧版 [`004ea67c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004ea628.md#insn-004ea67c) · [`004ea714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004ea628.md#insn-004ea714) · [`004ea654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004ea628.md#insn-004ea654)
- 新版 `004ea6bc`（命令位置の公開資料なし） · `004ea754`（命令位置の公開資料なし） · `004ea694`（命令位置の公開資料なし）

~~~diff
- 004ea67c ["INT_ADD", "register:40f0:8", ["const:4ea67c:8", "const:4:8"]]
- 004ea67c ["CALL", null, ["callee:00c57f70:8"]]
+ 004ea6bc ["INT_ADD", "register:40f0:8", ["const:4ea6bc:8", "const:4:8"]]
+ 004ea6bc ["CALL", null, ["callee:00c57f70:8"]]
- 004ea67c bytes 3db51d94
+ 004ea6bc bytes 2db61d94
- 004ea714 ["INT_ADD", "register:40f0:8", ["const:4ea714:8", "const:4:8"]]
- 004ea714 ["CALL", null, ["callee:00c57f10:8"]]
+ 004ea754 ["INT_ADD", "register:40f0:8", ["const:4ea754:8", "const:4:8"]]
+ 004ea754 ["CALL", null, ["callee:00c57f10:8"]]
- 004ea714 bytes ffb41d94
+ 004ea754 bytes efb51d94
- 004ea654 ["INT_ADD", "register:40f0:8", ["const:4ea654:8", "const:4:8"]]
- 004ea654 ["CALL", null, ["callee:00c57ef0:8"]]
+ 004ea694 ["INT_ADD", "register:40f0:8", ["const:4ea694:8", "const:4:8"]]
+ 004ea694 ["CALL", null, ["callee:00c57ef0:8"]]
- 004ea654 bytes 27b51d94
+ 004ea694 bytes 17b61d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99ed45119b2f4dc325cf66be33329b09"></a>

### [`004ea7ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004ea7ac.md) → [`004ea7ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ea/004ea7ec.md) _ZNK5Botan10Public_Key24create_kem_encryption_opERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocator

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
      "definition_site": "004ea874",
      "incomplete_value": true,
      "site": "004ea874",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ea8ac",
      "incomplete_value": true,
      "site": "004ea8b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ea838",
      "incomplete_value": false,
      "site": "004ea840",
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
      "004ea838",
      "PARAM",
      [
        "storage",
        "002b3abc",
        null,
        "string"
      ]
    ],
    [
      "004ea860",
      "READ",
      [
        "storage",
        "00c9a9d0",
        null,
        "pointer"
      ]
    ],
    [
      "004ea874",
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
      "004ea838",
      "PARAM",
      [
        "storage",
        "002b3afc",
        null,
        "string"
      ]
    ],
    [
      "004ea860",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "004ea874",
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

- 旧版 [`004ea800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004ea7ac.md#insn-004ea800) · [`004ea898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004ea7ac.md#insn-004ea898) · [`004ea7d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ea/004ea7ac.md#insn-004ea7d8)
- 新版 `004ea840`（命令位置の公開資料なし） · `004ea8d8`（命令位置の公開資料なし） · `004ea818`（命令位置の公開資料なし）

~~~diff
- 004ea800 ["INT_ADD", "register:40f0:8", ["const:4ea800:8", "const:4:8"]]
- 004ea800 ["CALL", null, ["callee:00c57f70:8"]]
+ 004ea840 ["INT_ADD", "register:40f0:8", ["const:4ea840:8", "const:4:8"]]
+ 004ea840 ["CALL", null, ["callee:00c57f70:8"]]
- 004ea800 bytes dcb41d94
+ 004ea840 bytes ccb51d94
- 004ea898 ["INT_ADD", "register:40f0:8", ["const:4ea898:8", "const:4:8"]]
- 004ea898 ["CALL", null, ["callee:00c57f10:8"]]
+ 004ea8d8 ["INT_ADD", "register:40f0:8", ["const:4ea8d8:8", "const:4:8"]]
+ 004ea8d8 ["CALL", null, ["callee:00c57f10:8"]]
- 004ea898 bytes 9eb41d94
+ 004ea8d8 bytes 8eb51d94
- 004ea7d8 ["INT_ADD", "register:40f0:8", ["const:4ea7d8:8", "const:4:8"]]
- 004ea7d8 ["CALL", null, ["callee:00c57ef0:8"]]
+ 004ea818 ["INT_ADD", "register:40f0:8", ["const:4ea818:8", "const:4:8"]]
+ 004ea818 ["CALL", null, ["callee:00c57ef0:8"]]
- 004ea7d8 bytes c6b41d94
+ 004ea818 bytes b6b51d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

