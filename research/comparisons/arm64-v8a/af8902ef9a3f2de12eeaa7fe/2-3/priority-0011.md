# v16.0.0 → v16.0.1 · 最優先の変更候補 (11)

[一覧の目次](README.md)

<a id="compare-08b923dafd31102e68ee98183591559b"></a>

### [`004fc77c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fc/004fc77c.md) → [`004fc7bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fc/004fc7bc.md) _ZN5Botan17deallocate_memoryEPvmm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59480.md) · 呼出先 2件 [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)
- 新版 呼出元 1件 [`00c59880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59880.md) · 呼出先 2件 [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004fc7e0",
      "incomplete_value": true,
      "site": "004fc7e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004fc7a0",
      "incomplete_value": true,
      "site": "004fc7a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004fc7d8",
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
      "004fc7d8",
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

- 旧版 [`004fc7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fc/004fc77c.md#insn-004fc7a0) · [`004fc798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fc/004fc77c.md#insn-004fc798)
- 新版 `004fc7e0`（命令位置の公開資料なし） · `004fc7d8`（命令位置の公開資料なし）

~~~diff
- 004fc7a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 004fc7a0 ["INT_ADD", "register:40f0:8", ["const:4fc7a0:8", "const:4:8"]]
- 004fc7a0 ["CALLIND", null, ["register:0:8"]]
+ 004fc7e0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004fc7e0 ["INT_ADD", "register:40f0:8", ["const:4fc7e0:8", "const:4:8"]]
+ 004fc7e0 ["CALLIND", null, ["register:0:8"]]
- 004fc7a0 bytes 00013fd6
+ 004fc7e0 bytes 00013fd6
- 004fc798 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:338:8"]]
- 004fc798 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004fc7d8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:738:8"]]
+ 004fc7d8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004fc798 bytes 089d41f9
+ 004fc7d8 bytes 089d43f9
~~~


<a id="compare-1de93a95c81d0c9e5991fec1c6db1e0e"></a>

### [`004fc7d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fc/004fc7d8.md) → [`004fc818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fc/004fc818.md) _ZN5Botan2OS25run_cpu_instruction_probeENSt6__ndk18functionIFivEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`004fc9d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fc/004fc9d8.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`004fca18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fc/004fca18.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.28% / 新版 95.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

アドレスに依存する影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004fc84c",
      "incomplete_value": false,
      "site": "004fc854",
      "value": [
        "leaf",
        "const:4fca18:8"
      ]
    },
    "old": {
      "definition_site": "004fc80c",
      "incomplete_value": false,
      "site": "004fc814",
      "value": [
        "leaf",
        "const:4fc9d8:8"
      ]
    },
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004fc878",
      "incomplete_value": false,
      "site": "004fc880",
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
            "const:298:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fc838",
      "incomplete_value": false,
      "site": "004fc840",
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
            "const:e98:8"
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
      "definition_site": "004fc904",
      "incomplete_value": false,
      "site": "004fc90c",
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
            "const:9f1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fc8c4",
      "incomplete_value": false,
      "site": "004fc8cc",
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
            "const:9b1:8"
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
      "004fc854",
      "DATA",
      [
        "storage",
        "004fc9d8",
        null,
        null
      ]
    ],
    [
      "004fc878",
      "PARAM",
      [
        "storage",
        "00ca4e98",
        null,
        null
      ]
    ],
    [
      "004fc904",
      "PARAM",
      [
        "storage",
        "002af9b1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004fc854",
      "DATA",
      [
        "storage",
        "004fca18",
        null,
        null
      ]
    ],
    [
      "004fc878",
      "PARAM",
      [
        "storage",
        "00ca5298",
        null,
        null
      ]
    ],
    [
      "004fc904",
      "PARAM",
      [
        "storage",
        "002af9f1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fc840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fc/004fc7d8.md#insn-004fc840) · [`004fc880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fc/004fc7d8.md#insn-004fc880) · [`004fc8cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fc/004fc7d8.md#insn-004fc8cc)
- 新版 `004fc880`（命令位置の公開資料なし） · `004fc8c0`（命令位置の公開資料なし） · `004fc90c`（命令位置の公開資料なし）

~~~diff
- 004fc840 ["INT_ADD", "register:40f0:8", ["const:4fc840:8", "const:4:8"]]
- 004fc840 ["CALL", null, ["callee:00c598d0:8"]]
+ 004fc880 ["INT_ADD", "register:40f0:8", ["const:4fc880:8", "const:4:8"]]
+ 004fc880 ["CALL", null, ["callee:00c598d0:8"]]
- 004fc840 bytes 24731d94
+ 004fc880 bytes 14741d94
- 004fc880 ["INT_ADD", "register:40f0:8", ["const:4fc880:8", "const:4:8"]]
- 004fc880 ["CALL", null, ["callee:00c598c0:8"]]
+ 004fc8c0 ["INT_ADD", "register:40f0:8", ["const:4fc8c0:8", "const:4:8"]]
+ 004fc8c0 ["CALL", null, ["callee:00c598c0:8"]]
- 004fc880 bytes 10731d94
+ 004fc8c0 bytes 00741d94
- 004fc8cc ["INT_ADD", "register:40f0:8", ["const:4fc8cc:8", "const:4:8"]]
- 004fc8cc ["CALL", null, ["callee:0043ddd8:8"]]
+ 004fc90c ["INT_ADD", "register:40f0:8", ["const:4fc90c:8", "const:4:8"]]
+ 004fc90c ["CALL", null, ["callee:0043ddd8:8"]]
- 004fc8cc bytes 3305fd97
+ 004fc90c bytes 3305fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8cc13e1aa8f5bef2015e1aadd7368773"></a>

### [`004fc9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fc/004fc9f0.md) → [`004fca30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fc/004fca30.md) _ZN5Botan9to_uint16ERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
      "definition_site": "004fca94",
      "incomplete_value": false,
      "site": "004fca9c",
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
            "const:1e2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fca54",
      "incomplete_value": false,
      "site": "004fca5c",
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
            "const:115:8"
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
      "definition_site": "004fcad0",
      "incomplete_value": true,
      "site": "004fcadc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
      "definition_site": "004fca90",
      "incomplete_value": true,
      "site": "004fca9c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
      "definition_site": "004fcacc",
      "incomplete_value": false,
      "site": "004fcadc",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004fca8c",
      "incomplete_value": false,
      "site": "004fca9c",
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
      "004fca94",
      "PARAM",
      [
        "storage",
        "002a3115",
        null,
        "string"
      ]
    ],
    [
      "004fcacc",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004fcad0",
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
      "004fca94",
      "PARAM",
      [
        "storage",
        "002a31e2",
        null,
        "string"
      ]
    ],
    [
      "004fcacc",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004fcad0",
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

- 旧版 [`004fca5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fc/004fc9f0.md#insn-004fca5c) · [`004fca9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fc/004fc9f0.md#insn-004fca9c) · [`004fca10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fc/004fc9f0.md#insn-004fca10)
- 新版 `004fca9c`（命令位置の公開資料なし） · `004fcadc`（命令位置の公開資料なし） · `004fca50`（命令位置の公開資料なし）

~~~diff
- 004fca5c ["INT_ADD", "register:40f0:8", ["const:4fca5c:8", "const:4:8"]]
- 004fca5c ["CALL", null, ["callee:0043ddd8:8"]]
+ 004fca9c ["INT_ADD", "register:40f0:8", ["const:4fca9c:8", "const:4:8"]]
+ 004fca9c ["CALL", null, ["callee:0043ddd8:8"]]
- 004fca5c bytes cf04fd97
+ 004fca9c bytes cf04fd97
- 004fca9c ["INT_ADD", "register:40f0:8", ["const:4fca9c:8", "const:4:8"]]
- 004fca9c ["CALL", null, ["callee:00c57f10:8"]]
+ 004fcadc ["INT_ADD", "register:40f0:8", ["const:4fcadc:8", "const:4:8"]]
+ 004fcadc ["CALL", null, ["callee:00c57f10:8"]]
- 004fca9c bytes 1d6c1d94
+ 004fcadc bytes 0d6d1d94
- 004fca10 ["INT_ADD", "register:40f0:8", ["const:4fca10:8", "const:4:8"]]
- 004fca10 ["CALL", null, ["callee:00c587f0:8"]]
+ 004fca50 ["INT_ADD", "register:40f0:8", ["const:4fca50:8", "const:4:8"]]
+ 004fca50 ["CALL", null, ["callee:00c587f0:8"]]
- 004fca10 bytes 786e1d94
+ 004fca50 bytes 686f1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ce8ed299e7f8a6efee991feabf3dbb4"></a>

### [`004fcaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fc/004fcaf0.md) → [`004fcb30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fc/004fcb30.md) _ZN5Botan18timespec_to_u32bitERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 12件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 12件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

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
    "old": {
      "definition_site": "004fccb8",
      "incomplete_value": false,
      "site": "004fccc4",
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
            "const:dd4:8"
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
    "old": {
      "definition_site": "004fccf4",
      "incomplete_value": true,
      "site": "004fcd00",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
      "definition_site": "004fcd30",
      "incomplete_value": false,
      "site": "004fcd40",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004fccf0",
      "incomplete_value": false,
      "site": "004fcd00",
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
      "004fccf8",
      "PARAM",
      [
        "storage",
        "002b4dd4",
        null,
        "string"
      ]
    ],
    [
      "004fcd30",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004fcd34",
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
      "004fccf8",
      "PARAM",
      [
        "storage",
        "002b4e14",
        null,
        "string"
      ]
    ],
    [
      "004fcd30",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004fcd34",
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

- 旧版 [`004fccc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fc/004fcaf0.md#insn-004fccc4) · [`004fcd00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fc/004fcaf0.md#insn-004fcd00) · [`004fcb94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fc/004fcaf0.md#insn-004fcb94)
- 新版 `004fcd04`（命令位置の公開資料なし） · `004fcd40`（命令位置の公開資料なし） · `004fcbd4`（命令位置の公開資料なし）

~~~diff
- 004fccc4 ["INT_ADD", "register:40f0:8", ["const:4fccc4:8", "const:4:8"]]
- 004fccc4 ["CALL", null, ["callee:00c580b0:8"]]
+ 004fcd04 ["INT_ADD", "register:40f0:8", ["const:4fcd04:8", "const:4:8"]]
+ 004fcd04 ["CALL", null, ["callee:00c580b0:8"]]
- 004fccc4 bytes fb6b1d94
+ 004fcd04 bytes eb6c1d94
- 004fcd00 ["INT_ADD", "register:40f0:8", ["const:4fcd00:8", "const:4:8"]]
- 004fcd00 ["CALL", null, ["callee:00c57f10:8"]]
+ 004fcd40 ["INT_ADD", "register:40f0:8", ["const:4fcd40:8", "const:4:8"]]
+ 004fcd40 ["CALL", null, ["callee:00c57f10:8"]]
- 004fcd00 bytes 846b1d94
+ 004fcd40 bytes 746c1d94
- 004fcb94 ["INT_ADD", "register:40f0:8", ["const:4fcb94:8", "const:4:8"]]
- 004fcb94 ["CALL", null, ["callee:00c57e90:8"]]
+ 004fcbd4 ["INT_ADD", "register:40f0:8", ["const:4fcbd4:8", "const:4:8"]]
+ 004fcbd4 ["CALL", null, ["callee:00c57e90:8"]]
- 004fcb94 bytes bf6b1d94
+ 004fcbd4 bytes af6c1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-703169814dfb24f680837d95b95bbe90"></a>

### [`004fcd68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fc/004fcd68.md) → [`004fcda8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fc/004fcda8.md) _ZN5Botan13split_on_predERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEENS0_8functionIFbcEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58bb0.md) · 呼出先 11件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00540d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540d3c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00c58fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58fb0.md) · 呼出先 11件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00540d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540d7c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
    "old": {
      "definition_site": "004fcf78",
      "incomplete_value": false,
      "site": "004fcf84",
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
            "const:7dc:8"
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
    "old": {
      "definition_site": "004fcfb4",
      "incomplete_value": true,
      "site": "004fcfc0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004fcff0",
      "incomplete_value": false,
      "site": "004fd000",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004fcfb0",
      "incomplete_value": false,
      "site": "004fcfc0",
      "value": [
        "leaf",
        "const:535828:8"
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
      "004fcfb8",
      "PARAM",
      [
        "storage",
        "002ad7dc",
        null,
        "string"
      ]
    ],
    [
      "004fcff0",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004fcff4",
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
      "004fcfb8",
      "PARAM",
      [
        "storage",
        "002ad81c",
        null,
        "string"
      ]
    ],
    [
      "004fcff0",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004fcff4",
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

- 旧版 [`004fcf84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fc/004fcd68.md#insn-004fcf84) · [`004fcfc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fc/004fcd68.md#insn-004fcfc0) · [`004fcde0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fc/004fcd68.md#insn-004fcde0)
- 新版 `004fcfc4`（命令位置の公開資料なし） · `004fd000`（命令位置の公開資料なし） · `004fce20`（命令位置の公開資料なし）

~~~diff
- 004fcf84 ["INT_ADD", "register:40f0:8", ["const:4fcf84:8", "const:4:8"]]
- 004fcf84 ["CALL", null, ["callee:00c580b0:8"]]
+ 004fcfc4 ["INT_ADD", "register:40f0:8", ["const:4fcfc4:8", "const:4:8"]]
+ 004fcfc4 ["CALL", null, ["callee:00c580b0:8"]]
- 004fcf84 bytes 4b6b1d94
+ 004fcfc4 bytes 3b6c1d94
- 004fcfc0 ["INT_ADD", "register:40f0:8", ["const:4fcfc0:8", "const:4:8"]]
- 004fcfc0 ["CALL", null, ["callee:00c57f10:8"]]
+ 004fd000 ["INT_ADD", "register:40f0:8", ["const:4fd000:8", "const:4:8"]]
+ 004fd000 ["CALL", null, ["callee:00c57f10:8"]]
- 004fcfc0 bytes d46a1d94
+ 004fd000 bytes c46b1d94
- 004fcde0 ["INT_ADD", "register:40f0:8", ["const:4fcde0:8", "const:4:8"]]
- 004fcde0 ["CALL", null, ["callee:00c58600:8"]]
+ 004fce20 ["INT_ADD", "register:40f0:8", ["const:4fce20:8", "const:4:8"]]
+ 004fce20 ["CALL", null, ["callee:00c58600:8"]]
- 004fcde0 bytes 086d1d94
+ 004fce20 bytes f86d1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4ca28251a839b3a525d4e54eb2e900f"></a>

### [`004fd30c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fd/004fd30c.md) → [`004fd34c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fd/004fd34c.md) _ZN5Botan14string_to_ipv4ERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59500.md) · 呼出先 11件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00547b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547b2c.md) [`00547b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547b30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00c59900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59900.md) · 呼出先 11件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00547b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547b6c.md) [`00547b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547b70.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

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
    "old": {
      "definition_site": "004fd330",
      "incomplete_value": false,
      "site": "004fd344",
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
    "old": {
      "definition_site": "004fd45c",
      "incomplete_value": false,
      "site": "004fd468",
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
            "const:b3e:8"
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
    "old": {
      "definition_site": "004fd498",
      "incomplete_value": true,
      "site": "004fd4a4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
      "004fd384",
      "DATA",
      [
        "storage",
        "00c6a2b0",
        null,
        "undefined *"
      ]
    ],
    [
      "004fd3c0",
      "READ",
      [
        "storage",
        "00c6a2d0",
        null,
        "pointer"
      ]
    ],
    [
      "004fd3c0",
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
      "004fd384",
      "DATA",
      [
        "storage",
        "00c6a6b0",
        null,
        "undefined *"
      ]
    ],
    [
      "004fd3c0",
      "READ",
      [
        "storage",
        "00c6a6d0",
        null,
        "pointer"
      ]
    ],
    [
      "004fd3c0",
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

- 旧版 [`004fd384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fd/004fd30c.md#insn-004fd384) · [`004fd468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fd/004fd30c.md#insn-004fd468) · [`004fd4a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fd/004fd30c.md#insn-004fd4a4)
- 新版 `004fd3c4`（命令位置の公開資料なし） · `004fd4a8`（命令位置の公開資料なし） · `004fd4e4`（命令位置の公開資料なし）

~~~diff
- 004fd384 ["COPY", "register:0:8", ["register:4040:8"]]
- 004fd384 ["INT_ADD", "register:40f0:8", ["const:4fd384:8", "const:4:8"]]
- 004fd384 ["CALLIND", null, ["register:0:8"]]
+ 004fd3c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004fd3c4 ["INT_ADD", "register:40f0:8", ["const:4fd3c4:8", "const:4:8"]]
+ 004fd3c4 ["CALLIND", null, ["register:0:8"]]
- 004fd384 bytes 00013fd6
+ 004fd3c4 bytes 00013fd6
- 004fd468 ["INT_ADD", "register:40f0:8", ["const:4fd468:8", "const:4:8"]]
- 004fd468 ["CALL", null, ["callee:00c580b0:8"]]
+ 004fd4a8 ["INT_ADD", "register:40f0:8", ["const:4fd4a8:8", "const:4:8"]]
+ 004fd4a8 ["CALL", null, ["callee:00c580b0:8"]]
- 004fd468 bytes 126a1d94
+ 004fd4a8 bytes 026b1d94
- 004fd4a4 ["INT_ADD", "register:40f0:8", ["const:4fd4a4:8", "const:4:8"]]
- 004fd4a4 ["CALL", null, ["callee:00c57f10:8"]]
+ 004fd4e4 ["INT_ADD", "register:40f0:8", ["const:4fd4e4:8", "const:4:8"]]
+ 004fd4e4 ["CALL", null, ["callee:00c57f10:8"]]
- 004fd4a4 bytes 9b691d94
+ 004fd4e4 bytes 8b6a1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28f16764b2a01b84e78ee962cf2e45b4"></a>

### [`004fd93c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fd/004fd93c.md) → [`004fd97c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fd/004fd97c.md) _ZN5Botan19host_wildcard_matchERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEES8_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59520.md) · 呼出先 15件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440ac0.md) [`00441d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441d80.md) [`00441e54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441e54.md)
- 新版 呼出元 1件 [`00c59920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59920.md) · 呼出先 15件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440b00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440b00.md) [`00441dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441dc0.md) [`00441e94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441e94.md)

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
    "old": {
      "definition_site": "004fddb4",
      "incomplete_value": false,
      "site": "004fddc0",
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
            "const:34a:8"
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
    "old": {
      "definition_site": "004fde08",
      "incomplete_value": false,
      "site": "004fde14",
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
            "const:30e:8"
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
    "old": {
      "definition_site": "004fde88",
      "incomplete_value": false,
      "site": "004fde90",
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
            "const:30e:8"
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
      "004fddf4",
      "PARAM",
      [
        "storage",
        "002b734a",
        null,
        null
      ]
    ],
    [
      "004fde48",
      "PARAM",
      [
        "storage",
        "002a630e",
        null,
        "undefined1"
      ]
    ],
    [
      "004fdec8",
      "PARAM",
      [
        "storage",
        "002a630e",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "004fddf4",
      "PARAM",
      [
        "storage",
        "002b738a",
        null,
        null
      ]
    ],
    [
      "004fde48",
      "PARAM",
      [
        "storage",
        "002a63ea",
        null,
        "undefined1"
      ]
    ],
    [
      "004fdec8",
      "PARAM",
      [
        "storage",
        "002a63ea",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fdd80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fd/004fd93c.md#insn-004fdd80) · [`004fddc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fd/004fd93c.md#insn-004fddc0) · [`004fde14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fd/004fd93c.md#insn-004fde14)
- 新版 `004fddc0`（命令位置の公開資料なし） · `004fde00`（命令位置の公開資料なし） · `004fde54`（命令位置の公開資料なし）

~~~diff
- 004fdd80 ["INT_ADD", "register:40f0:8", ["const:4fdd80:8", "const:4:8"]]
- 004fdd80 ["CALL", null, ["callee:00441dc0:8"]]
+ 004fddc0 ["INT_ADD", "register:40f0:8", ["const:4fddc0:8", "const:4:8"]]
+ 004fddc0 ["CALL", null, ["callee:00441dc0:8"]]
- 004fdd80 bytes 0010fd97
+ 004fddc0 bytes 0010fd97
- 004fddc0 ["INT_ADD", "register:40f0:8", ["const:4fddc0:8", "const:4:8"]]
- 004fddc0 ["CALL", null, ["callee:00441e94:8"]]
+ 004fde00 ["INT_ADD", "register:40f0:8", ["const:4fde00:8", "const:4:8"]]
+ 004fde00 ["CALL", null, ["callee:00441e94:8"]]
- 004fddc0 bytes 2510fd97
+ 004fde00 bytes 2510fd97
- 004fde14 ["INT_ADD", "register:40f0:8", ["const:4fde14:8", "const:4:8"]]
- 004fde14 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004fde54 ["INT_ADD", "register:40f0:8", ["const:4fde54:8", "const:4:8"]]
+ 004fde54 ["CALL", null, ["callee:0043ddd8:8"]]
- 004fde14 bytes e1fffc97
+ 004fde54 bytes e1fffc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24b8a79558886955040641baa13a51be"></a>

### [`004fe3e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fe/004fe3e8.md) → [`004fe428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fe/004fe428.md) _ZN5Botan8read_cfgERNSt6__ndk113basic_istreamIcNS0_11char_traitsIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 23件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md) [`00494c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/00494c3c.md) [`004a680c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a680c.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md)
- 新版 呼出元 0件  · 呼出先 23件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`00494c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494c7c.md) [`004a684c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a684c.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md)

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
    "old": {
      "definition_site": "004fe7ec",
      "incomplete_value": false,
      "site": "004fe7f0",
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
            "const:6b5:8"
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
    "old": {
      "definition_site": "004fe848",
      "incomplete_value": false,
      "site": "004fe854",
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
            "const:4d5:8"
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
    "old": {
      "definition_site": "004fe85c",
      "incomplete_value": false,
      "site": "004fe864",
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
            "const:b:8"
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
      "004fe4e0",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "004fe514",
      "PARAM",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "004fe82c",
      "PARAM",
      [
        "storage",
        "002c86b5",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004fe4e0",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      "004fe514",
      "PARAM",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "004fe82c",
      "PARAM",
      [
        "storage",
        "002c86f5",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fe7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fe/004fe3e8.md#insn-004fe7f0) · [`004fe830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fe/004fe3e8.md#insn-004fe830) · [`004fe854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fe/004fe3e8.md#insn-004fe854)
- 新版 `004fe830`（命令位置の公開資料なし） · `004fe870`（命令位置の公開資料なし） · `004fe894`（命令位置の公開資料なし）

~~~diff
- 004fe7f0 ["INT_ADD", "register:40f0:8", ["const:4fe7f0:8", "const:4:8"]]
- 004fe7f0 ["CALL", null, ["callee:00494c7c:8"]]
+ 004fe830 ["INT_ADD", "register:40f0:8", ["const:4fe830:8", "const:4:8"]]
+ 004fe830 ["CALL", null, ["callee:00494c7c:8"]]
- 004fe7f0 bytes 1359fe97
+ 004fe830 bytes 1359fe97
- 004fe830 ["INT_ADD", "register:40f0:8", ["const:4fe830:8", "const:4:8"]]
- 004fe830 ["CALL", null, ["callee:00c57eb0:8"]]
+ 004fe870 ["INT_ADD", "register:40f0:8", ["const:4fe870:8", "const:4:8"]]
+ 004fe870 ["CALL", null, ["callee:00c57eb0:8"]]
- 004fe830 bytes a0641d94
+ 004fe870 bytes 90651d94
- 004fe854 ["INT_ADD", "register:40f0:8", ["const:4fe854:8", "const:4:8"]]
- 004fe854 ["CALL", null, ["callee:00c580b0:8"]]
+ 004fe894 ["INT_ADD", "register:40f0:8", ["const:4fe894:8", "const:4:8"]]
+ 004fe894 ["CALL", null, ["callee:00c580b0:8"]]
- 004fe854 bytes 17651d94
+ 004fe894 bytes 07661d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86ad403ddada006496efc2404e44320a"></a>

### [`004fead8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fe/004fead8.md) → [`004feb18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fe/004feb18.md) _ZN5Botan18short_version_cstrEv

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
    "old": {
      "definition_site": "004feadc",
      "incomplete_value": false,
      "site": "004feae0",
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
            "const:9dc:8"
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
      "004feb1c",
      "DATA",
      [
        "storage",
        "002af9dc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004feb1c",
      "DATA",
      [
        "storage",
        "002afa1c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004feadc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fe/004fead8.md#insn-004feadc)
- 新版 `004feb1c`（命令位置の公開資料なし）

~~~diff
- 004feadc ["COPY", "tmp:0:8", ["const:9dc:8"]]
- 004feadc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004feadc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004feadc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004feb1c ["COPY", "tmp:0:8", ["const:a1c:8"]]
+ 004feb1c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004feb1c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004feb1c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004feadc bytes 00702791
+ 004feb1c bytes 00702891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e3998e67b2d8ce6929add412ffda49c"></a>

### [`004feae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fe/004feae4.md) → [`004feb24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fe/004feb24.md) _ZN5Botan12version_cstrEv

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
    "old": {
      "definition_site": "004feae8",
      "incomplete_value": false,
      "site": "004feaec",
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
            "const:58e:8"
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
      "004feb28",
      "DATA",
      [
        "storage",
        "002bc58e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004feb28",
      "DATA",
      [
        "storage",
        "002bc5ce",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004feae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fe/004feae4.md#insn-004feae8)
- 新版 `004feb28`（命令位置の公開資料なし）

~~~diff
- 004feae8 ["COPY", "tmp:0:8", ["const:58e:8"]]
- 004feae8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004feae8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004feae8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004feb28 ["COPY", "tmp:0:8", ["const:5ce:8"]]
+ 004feb28 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004feb28 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004feb28 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004feae8 bytes 00381691
+ 004feb28 bytes 00381791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19be97769ccf95193791c7b7cf6faebd"></a>

### [`004feb9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fe/004feb9c.md) → [`004febdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fe/004febdc.md) _ZN5Botan21runtime_version_checkEjjj

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 10件 [`00459490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ba0.md) [`00c57bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bb0.md)
- 新版 呼出元 0件  · 呼出先 10件 [`004594d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fa0.md) [`00c57fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 88.65% / 新版 88.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "004febe4",
      "incomplete_value": true,
      "site": "004febf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "old": {
      "definition_site": "004febec",
      "incomplete_value": true,
      "site": "004febfc",
      "value": [
        "LOAD",
        "8",
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
    "old": {
      "definition_site": "004fec04",
      "incomplete_value": true,
      "site": "004fec04",
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
      "004fec10",
      "READ",
      [
        "storage",
        "00c9a888",
        null,
        "pointer"
      ]
    ],
    [
      "004fec14",
      "READ",
      [
        "storage",
        "00c9a7b8",
        null,
        "pointer"
      ]
    ],
    [
      "004fec2c",
      "READ",
      [
        "storage",
        "00c92e08",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "004fec10",
      "READ",
      [
        "storage",
        "00c9ac88",
        null,
        "pointer"
      ]
    ],
    [
      "004fec14",
      "READ",
      [
        "storage",
        "00c9abb8",
        null,
        "pointer"
      ]
    ],
    [
      "004fec2c",
      "READ",
      [
        "storage",
        "00c93208",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fec3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fe/004feb9c.md#insn-004fec3c) · [`004fec84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fe/004feb9c.md#insn-004fec84) · [`004fecc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fe/004feb9c.md#insn-004fecc0)
- 新版 `004fec7c`（命令位置の公開資料なし） · `004fecc4`（命令位置の公開資料なし） · `004fed00`（命令位置の公開資料なし）

~~~diff
- 004fec3c ["INT_ADD", "register:40f0:8", ["const:4fec3c:8", "const:4:8"]]
- 004fec3c ["CALL", null, ["callee:00c581f0:8"]]
+ 004fec7c ["INT_ADD", "register:40f0:8", ["const:4fec7c:8", "const:4:8"]]
+ 004fec7c ["CALL", null, ["callee:00c581f0:8"]]
- 004fec3c bytes 6d641d94
+ 004fec7c bytes 5d651d94
- 004fec84 ["INT_ADD", "register:40f0:8", ["const:4fec84:8", "const:4:8"]]
- 004fec84 ["CALL", null, ["callee:004594d0:8"]]
+ 004fecc4 ["INT_ADD", "register:40f0:8", ["const:4fecc4:8", "const:4:8"]]
+ 004fecc4 ["CALL", null, ["callee:004594d0:8"]]
- 004fec84 bytes 036afd97
+ 004fecc4 bytes 036afd97
- 004fecc0 ["INT_ADD", "register:40f0:8", ["const:4fecc0:8", "const:4:8"]]
- 004fecc0 ["CALL", null, ["callee:004594d0:8"]]
+ 004fed00 ["INT_ADD", "register:40f0:8", ["const:4fed00:8", "const:4:8"]]
+ 004fed00 ["CALL", null, ["callee:004594d0:8"]]
- 004fecc0 bytes f469fd97
+ 004fed00 bytes f469fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-763209c9af50dc5feedd4637714d7d5e"></a>

### [`004fee30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fe/004fee30.md) → [`004fee70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fe/004fee70.md) _ZN5Botan15AlternativeNameC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_S9_S9_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59710.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c59550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59550.md)
- 新版 呼出元 1件 [`00c59b10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59b10.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c59950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59950.md)

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
    "old": {
      "definition_site": "004fee7c",
      "incomplete_value": true,
      "site": "004feea4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "004feea0",
      "READ",
      [
        "storage",
        "00c9acc8",
        null,
        "pointer"
      ]
    ],
    [
      "004feee4",
      "DATA",
      [
        "storage",
        "00c67368",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004feea0",
      "READ",
      [
        "storage",
        "00c9b0c8",
        null,
        "pointer"
      ]
    ],
    [
      "004feee4",
      "DATA",
      [
        "storage",
        "00c67768",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004fef64",
      "DATA",
      [
        "storage",
        "00495255",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fee54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fe/004fee30.md#insn-004fee54) · [`004fee60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fe/004fee30.md#insn-004fee60) · [`004feecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fe/004fee30.md#insn-004feecc)
- 新版 `004fee94`（命令位置の公開資料なし） · `004feea0`（命令位置の公開資料なし） · `004fef0c`（命令位置の公開資料なし）

~~~diff
- 004fee54 ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 004fee94 ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 004fee54 bytes e93c0090
+ 004fee94 bytes e93c00b0
- 004fee60 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:cc8:8"]]
- 004fee60 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004feea0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c8:8"]]
+ 004feea0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004fee60 bytes 296546f9
+ 004feea0 bytes 296540f9
- 004feecc ["INT_ADD", "register:40f0:8", ["const:4feecc:8", "const:4:8"]]
- 004feecc ["CALL", null, ["callee:00c59950:8"]]
+ 004fef0c ["INT_ADD", "register:40f0:8", ["const:4fef0c:8", "const:4:8"]]
+ 004fef0c ["CALL", null, ["callee:00c59950:8"]]
- 004feecc bytes a1691d94
+ 004fef0c bytes 916a1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e4af4e0de5092a70159474fa52ca69d"></a>

### [`004ffa6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ffa6c.md) → [`004ffaac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ffaac.md) FUN_004ffaac

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`004ff7f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff7f8.md) · 呼出先 13件 [`0050857c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/0050857c.md) [`00514d64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/00514d64.md) [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`00548058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548058.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`004ff838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff838.md) · 呼出先 13件 [`005085bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00508/005085bc.md) [`00514da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00514/00514da4.md) [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md) [`00548098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548098.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
    "old": {
      "definition_site": "004ffaf0",
      "incomplete_value": true,
      "site": "004ffaf0",
      "value": [
        "LOAD",
        "8",
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
    "old": {
      "definition_site": "004ffaf0",
      "incomplete_value": true,
      "site": "004ffaf0",
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
    "old": {
      "definition_site": "004ffae4",
      "incomplete_value": true,
      "site": "004ffaf8",
      "value": [
        "LOAD",
        "8",
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
      "004ffb08",
      "READ",
      [
        "storage",
        "00c9a810",
        null,
        "pointer"
      ]
    ],
    [
      "004ffb20",
      "READ",
      [
        "storage",
        "00c92ce8",
        "_ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "004ffb24",
      "READ",
      [
        "storage",
        "00c92d28",
        null,
        "pointer __((offset(0x68)))"
      ]
    ]
  ],
  "added": [
    [
      "004ffb08",
      "READ",
      [
        "storage",
        "00c9ac10",
        null,
        "pointer"
      ]
    ],
    [
      "004ffb20",
      "READ",
      [
        "storage",
        "00c930e8",
        "_ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "004ffb24",
      "READ",
      [
        "storage",
        "00c93128",
        null,
        "pointer __((offset(0x68)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ffab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ffa6c.md#insn-004ffab0) · [`004ffcf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ffa6c.md#insn-004ffcf8) · [`004ffac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ffa6c.md#insn-004ffac8)
- 新版 `004ffaf0`（命令位置の公開資料なし） · `004ffd38`（命令位置の公開資料なし） · `004ffb08`（命令位置の公開資料なし）

~~~diff
- 004ffab0 ["INT_ADD", "register:40f0:8", ["const:4ffab0:8", "const:4:8"]]
- 004ffab0 ["CALL", null, ["callee:00548098:8"]]
+ 004ffaf0 ["INT_ADD", "register:40f0:8", ["const:4ffaf0:8", "const:4:8"]]
+ 004ffaf0 ["CALL", null, ["callee:00548098:8"]]
- 004ffab0 bytes 6a210194
+ 004ffaf0 bytes 6a210194
- 004ffcf8 ["INT_ADD", "register:40f0:8", ["const:4ffcf8:8", "const:4:8"]]
- 004ffcf8 ["CALL", null, ["callee:00c581c0:8"]]
+ 004ffd38 ["INT_ADD", "register:40f0:8", ["const:4ffd38:8", "const:4:8"]]
+ 004ffd38 ["CALL", null, ["callee:00c581c0:8"]]
- 004ffcf8 bytes 32601d94
+ 004ffd38 bytes 22611d94
- 004ffac8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:810:8"]]
- 004ffac8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ffb08 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c10:8"]]
+ 004ffb08 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004ffac8 bytes 080944f9
+ 004ffb08 bytes 080946f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-feb6b305d4c01a53de8fd17f47e5dbe4"></a>

### [`004ffde0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ffde0.md) → [`004ffe20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ffe20.md) _ZN5Botan15AlternativeName11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 28件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00451870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451870.md) [`004ff33c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ff33c.md) [`00506f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00506/00506f50.md)
- 新版 呼出元 0件  · 呼出先 28件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004518b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004518b0.md) [`004ff37c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ff37c.md) [`00506f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00506/00506f90.md)

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
    "old": {
      "definition_site": "004ffe50",
      "incomplete_value": true,
      "site": "004ffe54",
      "value": [
        "LOAD",
        "8",
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
    "old": {
      "definition_site": "004ffe60",
      "incomplete_value": true,
      "site": "004ffe60",
      "value": [
        "LOAD",
        "8",
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
    "old": {
      "definition_site": "004ffe60",
      "incomplete_value": true,
      "site": "004ffe60",
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
      "004ffe74",
      "READ",
      [
        "storage",
        "00c9a810",
        null,
        "pointer"
      ]
    ],
    [
      "004ffe8c",
      "READ",
      [
        "storage",
        "00c92ce8",
        "_ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "004ffe90",
      "READ",
      [
        "storage",
        "00c92d28",
        null,
        "pointer __((offset(0x68)))"
      ]
    ]
  ],
  "added": [
    [
      "004ffe74",
      "READ",
      [
        "storage",
        "00c9ac10",
        null,
        "pointer"
      ]
    ],
    [
      "004ffe8c",
      "READ",
      [
        "storage",
        "00c930e8",
        "_ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "004ffe90",
      "READ",
      [
        "storage",
        "00c93128",
        null,
        "pointer __((offset(0x68)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ffea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ffde0.md#insn-004ffea0) · [`00500234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ffde0.md#insn-00500234) · [`00500294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ffde0.md#insn-00500294)
- 新版 `004ffee0`（命令位置の公開資料なし） · `00500274`（命令位置の公開資料なし） · `005002d4`（命令位置の公開資料なし）

~~~diff
- 004ffea0 ["COPY", "register:0:8", ["register:4040:8"]]
- 004ffea0 ["INT_ADD", "register:40f0:8", ["const:4ffea0:8", "const:4:8"]]
- 004ffea0 ["CALLIND", null, ["register:0:8"]]
+ 004ffee0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004ffee0 ["INT_ADD", "register:40f0:8", ["const:4ffee0:8", "const:4:8"]]
+ 004ffee0 ["CALLIND", null, ["register:0:8"]]
- 004ffea0 bytes 00013fd6
+ 004ffee0 bytes 00013fd6
- 00500234 ["INT_ADD", "register:40f0:8", ["const:500234:8", "const:4:8"]]
- 00500234 ["CALL", null, ["callee:00c581c0:8"]]
+ 00500274 ["INT_ADD", "register:40f0:8", ["const:500274:8", "const:4:8"]]
+ 00500274 ["CALL", null, ["callee:00c581c0:8"]]
- 00500234 bytes e35e1d94
+ 00500274 bytes d35f1d94
- 00500294 ["COPY", "register:0:8", ["register:4048:8"]]
- 00500294 ["INT_ADD", "register:40f0:8", ["const:500294:8", "const:4:8"]]
- 00500294 ["CALLIND", null, ["register:0:8"]]
+ 005002d4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005002d4 ["INT_ADD", "register:40f0:8", ["const:5002d4:8", "const:4:8"]]
+ 005002d4 ["CALLIND", null, ["register:0:8"]]
- 00500294 bytes 20013fd6
+ 005002d4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95ddf35c247275146adb25a82fd256b8"></a>

### [`00500abc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00500/00500abc.md) → [`00500afc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00500/00500afc.md) _ZN5BotanlsERNSt6__ndk113basic_ostreamIcNS0_11char_traitsIcEEEERKNS_7X509_DNE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c595a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595a0.md) · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00459490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md) [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00c599a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599a0.md) · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`004594d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

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
    "old": {
      "definition_site": "00500dfc",
      "incomplete_value": false,
      "site": "00500e04",
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
            "const:98f:8"
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
      "00500d68",
      "PARAM",
      [
        "storage",
        "002b8fa4",
        null,
        null
      ]
    ],
    [
      "00500dbc",
      "PARAM",
      [
        "storage",
        "002a6676",
        null,
        null
      ]
    ],
    [
      "00500dec",
      "PARAM",
      [
        "storage",
        "002b5e4d",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00500d68",
      "PARAM",
      [
        "storage",
        "002b8fe4",
        null,
        null
      ]
    ],
    [
      "00500dbc",
      "PARAM",
      [
        "storage",
        "002a6752",
        null,
        null
      ]
    ],
    [
      "00500dec",
      "PARAM",
      [
        "storage",
        "002b5e8d",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00500e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00500/00500abc.md#insn-00500e04) · [`00500afc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00500/00500abc.md#insn-00500afc) · [`00500b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00500/00500abc.md#insn-00500b18)
- 新版 `00500e44`（命令位置の公開資料なし） · `00500b3c`（命令位置の公開資料なし） · `00500b58`（命令位置の公開資料なし）

~~~diff
- 00500e04 ["INT_ADD", "register:40f0:8", ["const:500e04:8", "const:4:8"]]
- 00500e04 ["CALL", null, ["callee:004594d0:8"]]
+ 00500e44 ["INT_ADD", "register:40f0:8", ["const:500e44:8", "const:4:8"]]
+ 00500e44 ["CALL", null, ["callee:004594d0:8"]]
- 00500e04 bytes a361fd97
+ 00500e44 bytes a361fd97
- 00500afc ["INT_ADD", "register:40f0:8", ["const:500afc:8", "const:4:8"]]
- 00500afc ["CALL", null, ["callee:00c599b0:8"]]
+ 00500b3c ["INT_ADD", "register:40f0:8", ["const:500b3c:8", "const:4:8"]]
+ 00500b3c ["CALL", null, ["callee:00c599b0:8"]]
- 00500afc bytes ad621d94
+ 00500b3c bytes 9d631d94
- 00500b18 ["COPY", "tmp:0:8", ["const:fa4:8"]]
- 00500b18 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 00500b18 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 00500b18 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 00500b58 ["COPY", "tmp:0:8", ["const:fe4:8"]]
+ 00500b58 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 00500b58 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 00500b58 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 00500b18 bytes 94923e91
+ 00500b58 bytes 94923f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b55c39be0664fd9cef464e1a84804343"></a>

### [`00500f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00500/00500f00.md) → [`00500f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00500/00500f40.md) _ZN5Botan9to_stringENS_23Certificate_Status_CodeE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c595c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595c0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c599c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599c0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 83.46% / 新版 83.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 45件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
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
    "old": {
      "definition_site": "00500f54",
      "incomplete_value": false,
      "site": "00500f58",
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
            "const:9ed:8"
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
    "old": {
      "definition_site": "00500f90",
      "incomplete_value": false,
      "site": "00500f94",
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
            "const:d9d:8"
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
    "old": {
      "definition_site": "00500fc4",
      "incomplete_value": false,
      "site": "00500fc8",
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
            "const:626:8"
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
      "00500f94",
      "DATA",
      [
        "storage",
        "002af9ed",
        null,
        "string"
      ]
    ],
    [
      "00500fd0",
      "DATA",
      [
        "storage",
        "002bed9d",
        null,
        "string"
      ]
    ],
    [
      "00501004",
      "DATA",
      [
        "storage",
        "002a6626",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00500f94",
      "DATA",
      [
        "storage",
        "002afa2d",
        null,
        "string"
      ]
    ],
    [
      "00500fd0",
      "DATA",
      [
        "storage",
        "002beddd",
        null,
        "string"
      ]
    ],
    [
      "00501004",
      "DATA",
      [
        "storage",
        "002a6702",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00500f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00500/00500f00.md#insn-00500f54) · [`00500ff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00500/00500f00.md#insn-00500ff8) · [`005011d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00500/00500f00.md#insn-005011d4)
- 新版 `00500f94`（命令位置の公開資料なし） · `00501038`（命令位置の公開資料なし） · `00501214`（命令位置の公開資料なし）

~~~diff
- 00500f54 ["COPY", "tmp:0:8", ["const:9ed:8"]]
- 00500f54 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00500f54 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00500f54 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00500f94 ["COPY", "tmp:0:8", ["const:a2d:8"]]
+ 00500f94 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00500f94 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00500f94 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00500f54 bytes 00b42791
+ 00500f94 bytes 00b42891
- 00500ff8 ["COPY", "tmp:0:8", ["const:c16:8"]]
- 00500ff8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00500ff8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00500ff8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00501038 ["COPY", "tmp:0:8", ["const:c56:8"]]
+ 00501038 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00501038 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00501038 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00500ff8 bytes 00583091
+ 00501038 bytes 00583191
- 005011d4 ["COPY", "tmp:0:8", ["const:146:8"]]
- 005011d4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 005011d4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 005011d4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00501214 ["COPY", "tmp:0:8", ["const:213:8"]]
+ 00501214 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00501214 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00501214 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 005011d4 bytes 00180591
+ 00501214 bytes 004c0891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7d1c8a0aa989979bf7205aea26aa657"></a>

### [`00501348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501348.md) → [`00501388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501388.md) _ZN5Botan27Certificate_Store_In_Memory15add_certificateERKNS_16X509_CertificateE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c595d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595d0.md) · 呼出先 10件 [`0053afc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053afc0.md) [`00548368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548368.md) [`00548378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548378.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00c599d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599d0.md) · 呼出先 10件 [`0053b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053b000.md) [`005483a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/005483a8.md) [`005483b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/005483b8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

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
    "old": {
      "definition_site": "00501424",
      "incomplete_value": true,
      "site": "00501428",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00501440",
      "incomplete_value": true,
      "site": "00501448",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "0050145c",
      "READ",
      [
        "storage",
        "00c9acd8",
        null,
        "pointer"
      ]
    ],
    [
      "00501468",
      "DATA",
      [
        "storage",
        "00c6a340",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "0050147c",
      "READ",
      [
        "storage",
        "00c9ace0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050145c",
      "READ",
      [
        "storage",
        "00c9b0d8",
        null,
        "pointer"
      ]
    ],
    [
      "00501468",
      "DATA",
      [
        "storage",
        "00c6a740",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "0050147c",
      "READ",
      [
        "storage",
        "00c9b0e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005013cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501348.md#insn-005013cc) · [`005013dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501348.md#insn-005013dc) · [`005013fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501348.md#insn-005013fc)
- 新版 `0050140c`（命令位置の公開資料なし） · `0050141c`（命令位置の公開資料なし） · `0050143c`（命令位置の公開資料なし）

~~~diff
- 005013cc ["INT_ADD", "register:40f0:8", ["const:5013cc:8", "const:4:8"]]
- 005013cc ["CALL", null, ["callee:00c58050:8"]]
+ 0050140c ["INT_ADD", "register:40f0:8", ["const:50140c:8", "const:4:8"]]
+ 0050140c ["CALL", null, ["callee:00c58050:8"]]
- 005013cc bytes 215a1d94
+ 0050140c bytes 115b1d94
- 005013dc ["INT_ADD", "register:40f0:8", ["const:5013dc:8", "const:4:8"]]
- 005013dc ["CALL", null, ["callee:00c586a0:8"]]
+ 0050141c ["INT_ADD", "register:40f0:8", ["const:50141c:8", "const:4:8"]]
+ 0050141c ["CALL", null, ["callee:00c586a0:8"]]
- 005013dc bytes b15b1d94
+ 0050141c bytes a15c1d94
- 005013fc ["INT_ADD", "register:40f0:8", ["const:5013fc:8", "const:4:8"]]
- 005013fc ["CALL", null, ["callee:00c58050:8"]]
+ 0050143c ["INT_ADD", "register:40f0:8", ["const:50143c:8", "const:4:8"]]
+ 0050143c ["CALL", null, ["callee:00c58050:8"]]
- 005013fc bytes 155a1d94
+ 0050143c bytes 055b1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5ef4e748b17c086e6a0f202b92ee1a3"></a>

### [`00501e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501e10.md) → [`00501e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501e50.md) _ZNK5Botan27Certificate_Store_In_Memory24find_cert_by_pubkey_sha1ERKNSt6__ndk16vectorIhNS1_9allocatorIhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
    "old": {
      "definition_site": "00502028",
      "incomplete_value": false,
      "site": "00502030",
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
            "const:ae9:8"
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
    "old": {
      "definition_site": "00502060",
      "incomplete_value": true,
      "site": "0050206c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0050209c",
      "incomplete_value": false,
      "site": "005020ac",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "0050205c",
      "incomplete_value": false,
      "site": "0050206c",
      "value": [
        "leaf",
        "const:535828:8"
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
      "00502068",
      "PARAM",
      [
        "storage",
        "002b2ae9",
        null,
        "string"
      ]
    ],
    [
      "0050209c",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "005020a0",
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
      "00502068",
      "PARAM",
      [
        "storage",
        "002b2b29",
        null,
        "string"
      ]
    ],
    [
      "0050209c",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "005020a0",
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

- 旧版 [`00502030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501e10.md#insn-00502030) · [`0050206c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501e10.md#insn-0050206c) · [`00501e84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501e10.md#insn-00501e84)
- 新版 `00502070`（命令位置の公開資料なし） · `005020ac`（命令位置の公開資料なし） · `00501ec4`（命令位置の公開資料なし）

~~~diff
- 00502030 ["INT_ADD", "register:40f0:8", ["const:502030:8", "const:4:8"]]
- 00502030 ["CALL", null, ["callee:0043ddd8:8"]]
+ 00502070 ["INT_ADD", "register:40f0:8", ["const:502070:8", "const:4:8"]]
+ 00502070 ["CALL", null, ["callee:0043ddd8:8"]]
- 00502030 bytes 5aeffc97
+ 00502070 bytes 5aeffc97
- 0050206c ["INT_ADD", "register:40f0:8", ["const:50206c:8", "const:4:8"]]
- 0050206c ["CALL", null, ["callee:00c57f10:8"]]
+ 005020ac ["INT_ADD", "register:40f0:8", ["const:5020ac:8", "const:4:8"]]
+ 005020ac ["CALL", null, ["callee:00c57f10:8"]]
- 0050206c bytes a9561d94
+ 005020ac bytes 99571d94
- 00501e84 ["INT_ADD", "register:40f0:8", ["const:501e84:8", "const:4:8"]]
- 00501e84 ["CALL", null, ["callee:00c58df0:8"]]
+ 00501ec4 ["INT_ADD", "register:40f0:8", ["const:501ec4:8", "const:4:8"]]
+ 00501ec4 ["CALL", null, ["callee:00c58df0:8"]]
- 00501e84 bytes db5a1d94
+ 00501ec4 bytes cb5b1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8b0cfad8cf55ada67effb8d2c63d129"></a>

### [`00502128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502128.md) → [`00502168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502168.md) _ZNK5Botan27Certificate_Store_In_Memory34find_cert_by_raw_subject_dn_sha256ERKNSt6__ndk16vectorIhNS1_9allocatorIhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
    "old": {
      "definition_site": "00502348",
      "incomplete_value": false,
      "site": "00502350",
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
            "const:505:8"
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
    "old": {
      "definition_site": "00502380",
      "incomplete_value": true,
      "site": "0050238c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005023bc",
      "incomplete_value": false,
      "site": "005023cc",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "0050237c",
      "incomplete_value": false,
      "site": "0050238c",
      "value": [
        "leaf",
        "const:535828:8"
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
      "00502388",
      "PARAM",
      [
        "storage",
        "002a5505",
        null,
        "string"
      ]
    ],
    [
      "005023bc",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "005023c0",
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
      "00502388",
      "PARAM",
      [
        "storage",
        "002a55e1",
        null,
        "string"
      ]
    ],
    [
      "005023bc",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "005023c0",
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

- 旧版 [`00502350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502128.md#insn-00502350) · [`0050238c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502128.md#insn-0050238c) · [`005021a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502128.md#insn-005021a4)
- 新版 `00502390`（命令位置の公開資料なし） · `005023cc`（命令位置の公開資料なし） · `005021e4`（命令位置の公開資料なし）

~~~diff
- 00502350 ["INT_ADD", "register:40f0:8", ["const:502350:8", "const:4:8"]]
- 00502350 ["CALL", null, ["callee:0043ddd8:8"]]
+ 00502390 ["INT_ADD", "register:40f0:8", ["const:502390:8", "const:4:8"]]
+ 00502390 ["CALL", null, ["callee:0043ddd8:8"]]
- 00502350 bytes 92eefc97
+ 00502390 bytes 92eefc97
- 0050238c ["INT_ADD", "register:40f0:8", ["const:50238c:8", "const:4:8"]]
- 0050238c ["CALL", null, ["callee:00c57f10:8"]]
+ 005023cc ["INT_ADD", "register:40f0:8", ["const:5023cc:8", "const:4:8"]]
+ 005023cc ["CALL", null, ["callee:00c57f10:8"]]
- 0050238c bytes e1551d94
+ 005023cc bytes d1561d94
- 005021a4 ["INT_ADD", "register:40f0:8", ["const:5021a4:8", "const:4:8"]]
- 005021a4 ["CALL", null, ["callee:00c58df0:8"]]
+ 005021e4 ["INT_ADD", "register:40f0:8", ["const:5021e4:8", "const:4:8"]]
+ 005021e4 ["CALL", null, ["callee:00c58df0:8"]]
- 005021a4 bytes 135a1d94
+ 005021e4 bytes 035b1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48c251742e3f9639d10073c64e0f16e3"></a>

### [`00502448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502448.md) → [`00502488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502488.md) _ZN5Botan27Certificate_Store_In_Memory7add_crlERKNS_8X509_CRLE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`0053afc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053afc0.md) [`00548a88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548a88.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0053b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053b000.md) [`00548ac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548ac8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

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
    "old": {
      "definition_site": "00502490",
      "incomplete_value": true,
      "site": "00502494",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "005024ac",
      "incomplete_value": true,
      "site": "005024b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005024c8",
      "READ",
      [
        "storage",
        "00c9ace8",
        null,
        "pointer"
      ]
    ],
    [
      "005024d4",
      "DATA",
      [
        "storage",
        "00c6a390",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "005024e8",
      "READ",
      [
        "storage",
        "00c9acf0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005024c8",
      "READ",
      [
        "storage",
        "00c9b0e8",
        null,
        "pointer"
      ]
    ],
    [
      "005024d4",
      "DATA",
      [
        "storage",
        "00c6a790",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "005024e8",
      "READ",
      [
        "storage",
        "00c9b0f0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00502478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502448.md#insn-00502478) · [`0050247c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502448.md#insn-0050247c) · [`00502488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502448.md#insn-00502488)
- 新版 `005024b8`（命令位置の公開資料なし） · `005024bc`（命令位置の公開資料なし） · `005024c8`（命令位置の公開資料なし）

~~~diff
- 00502478 ["INT_ADD", "register:40f0:8", ["const:502478:8", "const:4:8"]]
- 00502478 ["CALL", null, ["callee:00c57e90:8"]]
+ 005024b8 ["INT_ADD", "register:40f0:8", ["const:5024b8:8", "const:4:8"]]
+ 005024b8 ["CALL", null, ["callee:00c57e90:8"]]
- 00502478 bytes 86551d94
+ 005024b8 bytes 76561d94
- 0050247c ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 005024bc ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 0050247c bytes c83c0090
+ 005024bc bytes c83c00b0
- 00502488 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ce8:8"]]
- 00502488 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005024c8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e8:8"]]
+ 005024c8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00502488 bytes 087546f9
+ 005024c8 bytes 087540f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e341af2c21b8f7021fe453c81d0a153f"></a>

### [`005027b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/005027b8.md) → [`005027f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/005027f8.md) FUN_005027f8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`00501700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501700.md) [`005025bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/005025bc.md) [`005292f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00529/005292f4.md) [`00529d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00529/00529d78.md) [`005486b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/005486b4.md) · 呼出先 4件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`0053aa64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053aa64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 5件 [`00501740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00501/00501740.md) [`005025fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/005025fc.md) [`00529334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00529/00529334.md) [`00529db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00529/00529db8.md) [`005486f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/005486f4.md) · 呼出先 4件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`0053aaa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053aaa4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

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
    "old": {
      "definition_site": "005027f8",
      "incomplete_value": true,
      "site": "00502800",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00502828",
      "READ",
      [
        "storage",
        "00c9acd0",
        null,
        "pointer"
      ]
    ],
    [
      "00502840",
      "DATA",
      [
        "storage",
        "00c675f8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00502828",
      "READ",
      [
        "storage",
        "00c9b0d0",
        null,
        "pointer"
      ]
    ],
    [
      "00502840",
      "DATA",
      [
        "storage",
        "00c679f8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00502840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/005027b8.md#insn-00502840) · [`005027dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/005027b8.md#insn-005027dc) · [`005027e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/005027b8.md#insn-005027e8)
- 新版 `00502880`（命令位置の公開資料なし） · `0050281c`（命令位置の公開資料なし） · `00502828`（命令位置の公開資料なし）

~~~diff
- 00502840 ["INT_ADD", "register:40f0:8", ["const:502840:8", "const:4:8"]]
- 00502840 ["CALL", null, ["callee:00c58000:8"]]
+ 00502880 ["INT_ADD", "register:40f0:8", ["const:502880:8", "const:4:8"]]
+ 00502880 ["CALL", null, ["callee:00c58000:8"]]
- 00502840 bytes f0541d94
+ 00502880 bytes e0551d94
- 005027dc ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 0050281c ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 005027dc bytes c83c0090
+ 0050281c bytes c83c00b0
- 005027e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cd0:8"]]
- 005027e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00502828 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d0:8"]]
+ 00502828 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005027e8 bytes 086946f9
+ 00502828 bytes 086940f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aef49ddd52abaa1b75b9a64a4ebf6055"></a>

### [`00502afc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502afc.md) → [`00502b3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502b3c.md) _ZN5Botan27Certificate_Store_In_MemoryC1ERKNS_16X509_CertificateE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c595d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c599d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599d0.md)

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
    "old": {
      "definition_site": "00502b20",
      "incomplete_value": true,
      "site": "00502b24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00502b58",
      "READ",
      [
        "storage",
        "00c9acf8",
        null,
        "pointer"
      ]
    ],
    [
      "00502b64",
      "DATA",
      [
        "storage",
        "00c67398",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00502b58",
      "READ",
      [
        "storage",
        "00c9b0f8",
        null,
        "pointer"
      ]
    ],
    [
      "00502b64",
      "DATA",
      [
        "storage",
        "00c67798",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00502b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502afc.md#insn-00502b10) · [`00502b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502afc.md#insn-00502b18) · [`00502b1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502afc.md#insn-00502b1c)
- 新版 `00502b50`（命令位置の公開資料なし） · `00502b58`（命令位置の公開資料なし）

~~~diff
- 00502b10 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00502b50 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00502b10 bytes c83c0090
+ 00502b50 bytes c83c00b0
- 00502b18 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cf8:8"]]
- 00502b18 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00502b58 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f8:8"]]
+ 00502b58 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00502b18 bytes 087d46f9
+ 00502b58 bytes 087d40f9
- 00502b1c ["COPY", "register:40a0:8", ["register:4000:8"]]
- 00502b1c bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d49eacbd031fb60262e9a8014fa9e971"></a>

### [`00502bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502bfc.md) → [`00502c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502c3c.md) _ZN5Botan27Certificate_Store_In_MemoryC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00548378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548378.md) [`00548d38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548d38.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 9件 [`005483b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/005483b8.md) [`00548d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548d78.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
    "old": {
      "definition_site": "00502c34",
      "incomplete_value": true,
      "site": "00502c3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00502c68",
      "READ",
      [
        "storage",
        "00c9acf8",
        null,
        "pointer"
      ]
    ],
    [
      "00502c7c",
      "DATA",
      [
        "storage",
        "00c67398",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00502cc4",
      "READ",
      [
        "storage",
        "00c9ad00",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00502c68",
      "READ",
      [
        "storage",
        "00c9b0f8",
        null,
        "pointer"
      ]
    ],
    [
      "00502c7c",
      "DATA",
      [
        "storage",
        "00c67798",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00502cc4",
      "READ",
      [
        "storage",
        "00c9b100",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00502c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502bfc.md#insn-00502c1c) · [`00502c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502bfc.md#insn-00502c28) · [`00502c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502bfc.md#insn-00502c70)
- 新版 `00502c5c`（命令位置の公開資料なし） · `00502c68`（命令位置の公開資料なし） · `00502cb0`（命令位置の公開資料なし）

~~~diff
- 00502c1c ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00502c5c ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00502c1c bytes c83c0090
+ 00502c5c bytes c83c00b0
- 00502c28 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cf8:8"]]
- 00502c28 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00502c68 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f8:8"]]
+ 00502c68 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00502c28 bytes 087d46f9
+ 00502c68 bytes 087d40f9
- 00502c70 ["INT_ADD", "register:40f0:8", ["const:502c70:8", "const:4:8"]]
- 00502c70 ["CALL", null, ["callee:00c59830:8"]]
+ 00502cb0 ["INT_ADD", "register:40f0:8", ["const:502cb0:8", "const:4:8"]]
+ 00502cb0 ["CALL", null, ["callee:00c59830:8"]]
- 00502c70 bytes f0591d94
+ 00502cb0 bytes e05a1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-284579b3d0a1062d646fa34d90dbc78d"></a>

### [`00502ed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502ed0.md) → [`00502f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00502/00502f10.md) _ZN5Botan9CRL_EntryC2ERKNS_16X509_CertificateENS_8CRL_CodeE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00548e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548e28.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58180.md) [`00c595f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c595f0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00548e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548e68.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58580.md) [`00c599f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c599f0.md)

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
    "old": {
      "definition_site": "00502f08",
      "incomplete_value": true,
      "site": "00502f10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00502f3c",
      "incomplete_value": true,
      "site": "00502f3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00502f60",
      "incomplete_value": true,
      "site": "00502f60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00502f38",
      "READ",
      [
        "storage",
        "00c9ad08",
        null,
        "pointer"
      ]
    ],
    [
      "00502f50",
      "DATA",
      [
        "storage",
        "00c673e8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00502f6c",
      "READ",
      [
        "storage",
        "00c9a9b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00502f38",
      "READ",
      [
        "storage",
        "00c9b108",
        null,
        "pointer"
      ]
    ],
    [
      "00502f50",
      "DATA",
      [
        "storage",
        "00c677e8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00502f6c",
      "READ",
      [
        "storage",
        "00c9adb0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00502f20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502ed0.md#insn-00502f20) · [`00502f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502ed0.md#insn-00502f48) · [`00502fc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502ed0.md#insn-00502fc4)
- 新版 `00502f60`（命令位置の公開資料なし） · `00502f88`（命令位置の公開資料なし） · `00503004`（命令位置の公開資料なし）

~~~diff
- 00502f20 ["INT_ADD", "register:40f0:8", ["const:502f20:8", "const:4:8"]]
- 00502f20 ["CALL", null, ["callee:00c57e90:8"]]
+ 00502f60 ["INT_ADD", "register:40f0:8", ["const:502f60:8", "const:4:8"]]
+ 00502f60 ["CALL", null, ["callee:00c57e90:8"]]
- 00502f20 bytes dc521d94
+ 00502f60 bytes cc531d94
- 00502f48 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00502f88 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00502f48 bytes c83c0090
+ 00502f88 bytes c83c00b0
- 00502fc4 ["INT_ADD", "register:40f0:8", ["const:502fc4:8", "const:4:8"]]
- 00502fc4 ["CALL", null, ["callee:00c59a70:8"]]
+ 00503004 ["INT_ADD", "register:40f0:8", ["const:503004:8", "const:4:8"]]
+ 00503004 ["CALL", null, ["callee:00c59a70:8"]]
- 00502fc4 bytes ab591d94
+ 00503004 bytes 9b5a1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-103b1a8d90198af8a566aad7e7598821"></a>

### [`00503084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503084.md) → [`005030c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/005030c4.md) _ZN5Botan10Extensions3addEPNS_21Certificate_ExtensionEb

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59680.md) · 呼出先 17件 [`00516b84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516b84.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00535b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`0053d6e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053d6e8.md) [`0054b904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b904.md)
- 新版 呼出元 1件 [`00c59a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59a80.md) · 呼出先 17件 [`00516bc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516bc4.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`0053d728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053d/0053d728.md) [`0054b944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054b944.md)

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
    "old": {
      "definition_site": "00503258",
      "incomplete_value": true,
      "site": "00503258",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "0050329c",
      "incomplete_value": true,
      "site": "005032a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "005031ac",
      "incomplete_value": false,
      "site": "005031b4",
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
            "const:c5c:8"
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
      "005031ec",
      "PARAM",
      [
        "storage",
        "002b0c5c",
        null,
        "string"
      ]
    ],
    [
      "00503238",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "0050323c",
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
      "005031ec",
      "PARAM",
      [
        "storage",
        "002b0c9c",
        null,
        "string"
      ]
    ],
    [
      "00503238",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "0050323c",
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

- 旧版 [`005031b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503084.md#insn-005031b4) · [`00503208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503084.md#insn-00503208) · [`00503248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503084.md#insn-00503248)
- 新版 `005031f4`（命令位置の公開資料なし） · `00503248`（命令位置の公開資料なし） · `00503288`（命令位置の公開資料なし）

~~~diff
- 005031b4 ["INT_ADD", "register:40f0:8", ["const:5031b4:8", "const:4:8"]]
- 005031b4 ["CALL", null, ["callee:00c57f70:8"]]
+ 005031f4 ["INT_ADD", "register:40f0:8", ["const:5031f4:8", "const:4:8"]]
+ 005031f4 ["CALL", null, ["callee:00c57f70:8"]]
- 005031b4 bytes 6f521d94
+ 005031f4 bytes 5f531d94
- 00503208 ["INT_ADD", "register:40f0:8", ["const:503208:8", "const:4:8"]]
- 00503208 ["CALL", null, ["callee:00c57f10:8"]]
+ 00503248 ["INT_ADD", "register:40f0:8", ["const:503248:8", "const:4:8"]]
+ 00503248 ["CALL", null, ["callee:00c57f10:8"]]
- 00503208 bytes 42521d94
+ 00503248 bytes 32531d94
- 00503248 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d20:8"]]
- 00503248 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00503288 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:120:8"]]
+ 00503288 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00503248 bytes 089146f9
+ 00503288 bytes 089140f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0859a7e0cd8d4bfedc33150ff388e1c"></a>

### [`0050372c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/0050372c.md) → [`0050376c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/0050376c.md) _ZN5Botan9CRL_Entry11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c596b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c596b0.md) · 呼出先 16件 [`004aea34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aea34.md) [`00503aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503aa0.md) [`00517610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/00517610.md) [`00548d94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548d94.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00c59ab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59ab0.md) · 呼出先 16件 [`004aea74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aea74.md) [`00503ae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/00503ae0.md) [`00517650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517650.md) [`00548dd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548dd4.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

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
    "old": {
      "definition_site": "00503780",
      "incomplete_value": true,
      "site": "00503780",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "005037a4",
      "incomplete_value": true,
      "site": "005037a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "0050388c",
      "incomplete_value": true,
      "site": "0050388c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:498:8"
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
      "005037b0",
      "READ",
      [
        "storage",
        "00c9a9b0",
        null,
        "pointer"
      ]
    ],
    [
      "005037c0",
      "DATA",
      [
        "storage",
        "00c65f78",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005037d0",
      "READ",
      [
        "storage",
        "00c9ad10",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005037b0",
      "READ",
      [
        "storage",
        "00c9adb0",
        null,
        "pointer"
      ]
    ],
    [
      "005037c0",
      "DATA",
      [
        "storage",
        "00c66378",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005037d0",
      "READ",
      [
        "storage",
        "00c9b110",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005038cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/0050372c.md#insn-005038cc) · [`00503940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/0050372c.md#insn-00503940) · [`00503980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/0050372c.md#insn-00503980)
- 新版 `0050390c`（命令位置の公開資料なし） · `00503980`（命令位置の公開資料なし） · `005039c0`（命令位置の公開資料なし）

~~~diff
- 005038cc ["INT_ADD", "register:40f0:8", ["const:5038cc:8", "const:4:8"]]
- 005038cc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0050390c ["INT_ADD", "register:40f0:8", ["const:50390c:8", "const:4:8"]]
+ 0050390c ["CALL", null, ["callee:00c57eb0:8"]]
- 005038cc bytes 79501d94
+ 0050390c bytes 69511d94
- 00503940 ["INT_ADD", "register:40f0:8", ["const:503940:8", "const:4:8"]]
- 00503940 ["CALL", null, ["callee:00c57e80:8"]]
+ 00503980 ["INT_ADD", "register:40f0:8", ["const:503980:8", "const:4:8"]]
+ 00503980 ["CALL", null, ["callee:00c57e80:8"]]
- 00503940 bytes 50501d94
+ 00503980 bytes 40511d94
- 00503980 ["COPY", "register:0:8", ["register:4048:8"]]
- 00503980 ["INT_ADD", "register:40f0:8", ["const:503980:8", "const:4:8"]]
- 00503980 ["CALLIND", null, ["register:0:8"]]
+ 005039c0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005039c0 ["INT_ADD", "register:40f0:8", ["const:5039c0:8", "const:4:8"]]
+ 005039c0 ["CALLIND", null, ["register:0:8"]]
- 00503980 bytes 20013fd6
+ 005039c0 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca6098abb695f2dbc8692ef271739e0f"></a>

### [`00503aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503aa0.md) → [`00503ae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/00503ae0.md) FUN_00503ae0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0050372c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/0050372c.md) · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`0050376c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/0050376c.md) · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
    "old": {
      "definition_site": "00503adc",
      "incomplete_value": true,
      "site": "00503adc",
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
    "old": {
      "definition_site": "00503b18",
      "incomplete_value": false,
      "site": "00503b20",
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
            "const:243:8"
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
    "old": {
      "definition_site": "00503b54",
      "incomplete_value": true,
      "site": "00503b60",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00503b0c",
      "READ",
      [
        "storage",
        "00c9ad18",
        null,
        "pointer"
      ]
    ],
    [
      "00503b58",
      "PARAM",
      [
        "storage",
        "002a4243",
        null,
        "string"
      ]
    ],
    [
      "00503b90",
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
      "00503b0c",
      "READ",
      [
        "storage",
        "00c9b118",
        null,
        "pointer"
      ]
    ],
    [
      "00503b58",
      "PARAM",
      [
        "storage",
        "002a4310",
        null,
        "string"
      ]
    ],
    [
      "00503b90",
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

- 旧版 [`00503ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503aa0.md#insn-00503ac8) · [`00503b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503aa0.md#insn-00503b20) · [`00503b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503aa0.md#insn-00503b60)
- 新版 `00503b08`（命令位置の公開資料なし） · `00503b60`（命令位置の公開資料なし） · `00503ba0`（命令位置の公開資料なし）

~~~diff
- 00503ac8 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00503b08 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00503ac8 bytes a83c00f0
+ 00503b08 bytes c83c0090
- 00503b20 ["INT_ADD", "register:40f0:8", ["const:503b20:8", "const:4:8"]]
- 00503b20 ["CALL", null, ["callee:0043ddd8:8"]]
+ 00503b60 ["INT_ADD", "register:40f0:8", ["const:503b60:8", "const:4:8"]]
+ 00503b60 ["CALL", null, ["callee:0043ddd8:8"]]
- 00503b20 bytes 9ee8fc97
+ 00503b60 bytes 9ee8fc97
- 00503b60 ["INT_ADD", "register:40f0:8", ["const:503b60:8", "const:4:8"]]
- 00503b60 ["CALL", null, ["callee:00c57f10:8"]]
+ 00503ba0 ["INT_ADD", "register:40f0:8", ["const:503ba0:8", "const:4:8"]]
+ 00503ba0 ["CALL", null, ["callee:00c57f10:8"]]
- 00503b60 bytes ec4f1d94
+ 00503ba0 bytes dc501d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2eaf9cfdca297574dc26b894bd995587"></a>

### [`00503bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503bb4.md) → [`00503bf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/00503bf4.md) FUN_00503bf4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00515684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515684.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)
- 新版 呼出元 1件 [`005156c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/005156c4.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md)

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
    "old": {
      "definition_site": "00503bec",
      "incomplete_value": true,
      "site": "00503bec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:498:8"
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
      "00503c1c",
      "READ",
      [
        "storage",
        "002a6498",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00503c1c",
      "READ",
      [
        "storage",
        "002a6574",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00503bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503bb4.md#insn-00503bd0) · [`00503bf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503bb4.md#insn-00503bf8) · [`00503c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503bb4.md#insn-00503c08)
- 新版 `00503c10`（命令位置の公開資料なし） · `00503c38`（命令位置の公開資料なし） · `00503c48`（命令位置の公開資料なし）

~~~diff
- 00503bd0 ["COPY", "tmp:0:8", ["const:498:8"]]
- 00503bd0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00503bd0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00503bd0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00503c10 ["COPY", "tmp:0:8", ["const:574:8"]]
+ 00503c10 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00503c10 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00503c10 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00503bd0 bytes 29611291
+ 00503c10 bytes 29d11591
- 00503bf8 ["INT_ADD", "register:40f0:8", ["const:503bf8:8", "const:4:8"]]
- 00503bf8 ["CALL", null, ["callee:00c58690:8"]]
+ 00503c38 ["INT_ADD", "register:40f0:8", ["const:503c38:8", "const:4:8"]]
+ 00503c38 ["CALL", null, ["callee:00c58690:8"]]
- 00503bf8 bytes a6511d94
+ 00503c38 bytes 96521d94
- 00503c08 ["INT_ADD", "register:40f0:8", ["const:503c08:8", "const:4:8"]]
- 00503c08 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00503c48 ["INT_ADD", "register:40f0:8", ["const:503c48:8", "const:4:8"]]
+ 00503c48 ["CALL", null, ["callee:00c57eb0:8"]]
- 00503c08 bytes aa4f1d94
+ 00503c48 bytes 9a501d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74fb8f842fe08c21a64af721ca3446ff"></a>

### [`00503c5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503c5c.md) → [`00503c9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/00503c9c.md) _ZNK5Botan9CRL_Entry4dataEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c596a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c596a0.md) · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 1件 [`00c59aa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59aa0.md) · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

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
    "old": {
      "definition_site": "00503cbc",
      "incomplete_value": false,
      "site": "00503cc4",
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
            "const:100:8"
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
    "old": {
      "definition_site": "00503cf8",
      "incomplete_value": true,
      "site": "00503d04",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00503d34",
      "incomplete_value": false,
      "site": "00503d44",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "00503cf4",
      "incomplete_value": false,
      "site": "00503d04",
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
      "00503cfc",
      "PARAM",
      [
        "storage",
        "002a1100",
        null,
        "string"
      ]
    ],
    [
      "00503d34",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "00503d38",
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
      "00503cfc",
      "PARAM",
      [
        "storage",
        "002a11cd",
        null,
        "string"
      ]
    ],
    [
      "00503d34",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "00503d38",
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

- 旧版 [`00503cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503c5c.md#insn-00503cc4) · [`00503d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503c5c.md#insn-00503d04) · [`00503cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503c5c.md#insn-00503cb0)
- 新版 `00503d04`（命令位置の公開資料なし） · `00503d44`（命令位置の公開資料なし） · `00503cf0`（命令位置の公開資料なし）

~~~diff
- 00503cc4 ["INT_ADD", "register:40f0:8", ["const:503cc4:8", "const:4:8"]]
- 00503cc4 ["CALL", null, ["callee:0043ddd8:8"]]
+ 00503d04 ["INT_ADD", "register:40f0:8", ["const:503d04:8", "const:4:8"]]
+ 00503d04 ["CALL", null, ["callee:0043ddd8:8"]]
- 00503cc4 bytes 35e8fc97
+ 00503d04 bytes 35e8fc97
- 00503d04 ["INT_ADD", "register:40f0:8", ["const:503d04:8", "const:4:8"]]
- 00503d04 ["CALL", null, ["callee:00c57f10:8"]]
+ 00503d44 ["INT_ADD", "register:40f0:8", ["const:503d44:8", "const:4:8"]]
+ 00503d44 ["CALL", null, ["callee:00c57f10:8"]]
- 00503d04 bytes 834f1d94
+ 00503d44 bytes 73501d94
- 00503cb0 ["INT_ADD", "register:40f0:8", ["const:503cb0:8", "const:4:8"]]
- 00503cb0 ["CALL", null, ["callee:00c57ef0:8"]]
+ 00503cf0 ["INT_ADD", "register:40f0:8", ["const:503cf0:8", "const:4:8"]]
+ 00503cf0 ["CALL", null, ["callee:00c57ef0:8"]]
- 00503cb0 bytes 904f1d94
+ 00503cf0 bytes 80501d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23bbf9972063bb38210700a289ed47c6"></a>

### [`00504278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504278.md) → [`005042b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/005042b8.md) _ZNK5Botan10Data_Store4get1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

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
    "old": {
      "definition_site": "00504378",
      "incomplete_value": false,
      "site": "00504384",
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
            "const:170:8"
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
    "old": {
      "definition_site": "005043b4",
      "incomplete_value": true,
      "site": "005043c0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005043f0",
      "incomplete_value": false,
      "site": "00504400",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "005043b0",
      "incomplete_value": false,
      "site": "005043c0",
      "value": [
        "leaf",
        "const:535828:8"
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
      "005043b8",
      "PARAM",
      [
        "storage",
        "002a4170",
        null,
        "string"
      ]
    ],
    [
      "005043f0",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "005043f4",
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
      "005043b8",
      "PARAM",
      [
        "storage",
        "002a423d",
        null,
        "string"
      ]
    ],
    [
      "005043f0",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "005043f4",
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

- 旧版 [`00504384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504278.md#insn-00504384) · [`005043c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504278.md#insn-005043c0) · [`005043e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504278.md#insn-005043e4)
- 新版 `005043c4`（命令位置の公開資料なし） · `00504400`（命令位置の公開資料なし） · `00504424`（命令位置の公開資料なし）

~~~diff
- 00504384 ["INT_ADD", "register:40f0:8", ["const:504384:8", "const:4:8"]]
- 00504384 ["CALL", null, ["callee:00c580b0:8"]]
+ 005043c4 ["INT_ADD", "register:40f0:8", ["const:5043c4:8", "const:4:8"]]
+ 005043c4 ["CALL", null, ["callee:00c580b0:8"]]
- 00504384 bytes 4b4e1d94
+ 005043c4 bytes 3b4f1d94
- 005043c0 ["INT_ADD", "register:40f0:8", ["const:5043c0:8", "const:4:8"]]
- 005043c0 ["CALL", null, ["callee:00c57f10:8"]]
+ 00504400 ["INT_ADD", "register:40f0:8", ["const:504400:8", "const:4:8"]]
+ 00504400 ["CALL", null, ["callee:00c57f10:8"]]
- 005043c0 bytes d44d1d94
+ 00504400 bytes c44e1d94
- 005043e4 ["INT_ADD", "register:40f0:8", ["const:5043e4:8", "const:4:8"]]
- 005043e4 ["CALL", null, ["callee:00c580b0:8"]]
+ 00504424 ["INT_ADD", "register:40f0:8", ["const:504424:8", "const:4:8"]]
+ 00504424 ["CALL", null, ["callee:00c580b0:8"]]
- 005043e4 bytes 334e1d94
+ 00504424 bytes 234f1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d803f30f74bcb48b0634ab0f80d004d1"></a>

### [`00504488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504488.md) → [`005044c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/005044c8.md) _ZNK5Botan10Data_Store4get1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

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
    "old": {
      "definition_site": "00504598",
      "incomplete_value": false,
      "site": "005045a4",
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
            "const:7d3:8"
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
    "old": {
      "definition_site": "005045d4",
      "incomplete_value": true,
      "site": "005045e0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00504610",
      "incomplete_value": false,
      "site": "00504620",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "005045d0",
      "incomplete_value": false,
      "site": "005045e0",
      "value": [
        "leaf",
        "const:535828:8"
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
      "005045d8",
      "PARAM",
      [
        "storage",
        "002a77d3",
        null,
        "string"
      ]
    ],
    [
      "00504610",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "00504614",
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
      "005045d8",
      "PARAM",
      [
        "storage",
        "002a78af",
        null,
        "string"
      ]
    ],
    [
      "00504610",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "00504614",
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

- 旧版 [`005045a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504488.md#insn-005045a4) · [`005045e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504488.md#insn-005045e0) · [`005044b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504488.md#insn-005044b8)
- 新版 `005045e4`（命令位置の公開資料なし） · `00504620`（命令位置の公開資料なし） · `005044f8`（命令位置の公開資料なし）

~~~diff
- 005045a4 ["INT_ADD", "register:40f0:8", ["const:5045a4:8", "const:4:8"]]
- 005045a4 ["CALL", null, ["callee:00c580b0:8"]]
+ 005045e4 ["INT_ADD", "register:40f0:8", ["const:5045e4:8", "const:4:8"]]
+ 005045e4 ["CALL", null, ["callee:00c580b0:8"]]
- 005045a4 bytes c34d1d94
+ 005045e4 bytes b34e1d94
- 005045e0 ["INT_ADD", "register:40f0:8", ["const:5045e0:8", "const:4:8"]]
- 005045e0 ["CALL", null, ["callee:00c57f10:8"]]
+ 00504620 ["INT_ADD", "register:40f0:8", ["const:504620:8", "const:4:8"]]
+ 00504620 ["CALL", null, ["callee:00c57f10:8"]]
- 005045e0 bytes 4c4d1d94
+ 00504620 bytes 3c4e1d94
- 005044b8 ["INT_ADD", "register:40f0:8", ["const:5044b8:8", "const:4:8"]]
- 005044b8 ["CALL", null, ["callee:00c59ae0:8"]]
+ 005044f8 ["INT_ADD", "register:40f0:8", ["const:5044f8:8", "const:4:8"]]
+ 005044f8 ["CALL", null, ["callee:00c59ae0:8"]]
- 005044b8 bytes 8a541d94
+ 005044f8 bytes 7a551d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9997487eb9938cfb8197624a788b166a"></a>

### [`00504640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504640.md) → [`00504680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/00504680.md) _ZNK5Botan10Data_Store11get1_memvecERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

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
    "old": {
      "definition_site": "0050474c",
      "incomplete_value": false,
      "site": "00504758",
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
            "const:df5:8"
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
    "old": {
      "definition_site": "00504788",
      "incomplete_value": true,
      "site": "00504794",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005047c4",
      "incomplete_value": false,
      "site": "005047d4",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "00504784",
      "incomplete_value": false,
      "site": "00504794",
      "value": [
        "leaf",
        "const:535828:8"
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
      "0050478c",
      "PARAM",
      [
        "storage",
        "002bfdf5",
        null,
        "string"
      ]
    ],
    [
      "005047c4",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "005047c8",
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
      "0050478c",
      "PARAM",
      [
        "storage",
        "002bfe35",
        null,
        "string"
      ]
    ],
    [
      "005047c4",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "005047c8",
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

- 旧版 [`00504758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504640.md#insn-00504758) · [`00504794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504640.md#insn-00504794) · [`0050466c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504640.md#insn-0050466c)
- 新版 `00504798`（命令位置の公開資料なし） · `005047d4`（命令位置の公開資料なし） · `005046ac`（命令位置の公開資料なし）

~~~diff
- 00504758 ["INT_ADD", "register:40f0:8", ["const:504758:8", "const:4:8"]]
- 00504758 ["CALL", null, ["callee:00c580b0:8"]]
+ 00504798 ["INT_ADD", "register:40f0:8", ["const:504798:8", "const:4:8"]]
+ 00504798 ["CALL", null, ["callee:00c580b0:8"]]
- 00504758 bytes 564d1d94
+ 00504798 bytes 464e1d94
- 00504794 ["INT_ADD", "register:40f0:8", ["const:504794:8", "const:4:8"]]
- 00504794 ["CALL", null, ["callee:00c57f10:8"]]
+ 005047d4 ["INT_ADD", "register:40f0:8", ["const:5047d4:8", "const:4:8"]]
+ 005047d4 ["CALL", null, ["callee:00c57f10:8"]]
- 00504794 bytes df4c1d94
+ 005047d4 bytes cf4d1d94
- 0050466c ["INT_ADD", "register:40f0:8", ["const:50466c:8", "const:4:8"]]
- 0050466c ["CALL", null, ["callee:00c59ae0:8"]]
+ 005046ac ["INT_ADD", "register:40f0:8", ["const:5046ac:8", "const:4:8"]]
+ 005046ac ["CALL", null, ["callee:00c59ae0:8"]]
- 0050466c bytes 1d541d94
+ 005046ac bytes 0d551d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9e42402682ecbb087b2685386102479"></a>

### [`005047f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/005047f4.md) → [`00504834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/00504834.md) _ZNK5Botan10Data_Store11get1_uint32ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEj

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

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
    "old": {
      "definition_site": "005048dc",
      "incomplete_value": false,
      "site": "005048e8",
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
            "const:552:8"
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
    "old": {
      "definition_site": "00504918",
      "incomplete_value": true,
      "site": "00504924",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00504954",
      "incomplete_value": false,
      "site": "00504964",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "00504914",
      "incomplete_value": false,
      "site": "00504924",
      "value": [
        "leaf",
        "const:535828:8"
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
      "0050491c",
      "PARAM",
      [
        "storage",
        "002a5552",
        null,
        "string"
      ]
    ],
    [
      "00504954",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "00504958",
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
      "0050491c",
      "PARAM",
      [
        "storage",
        "002a562e",
        null,
        "string"
      ]
    ],
    [
      "00504954",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "00504958",
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

- 旧版 [`005048e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/005047f4.md#insn-005048e8) · [`00504924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/005047f4.md#insn-00504924) · [`00504820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/005047f4.md#insn-00504820)
- 新版 `00504928`（命令位置の公開資料なし） · `00504964`（命令位置の公開資料なし） · `00504860`（命令位置の公開資料なし）

~~~diff
- 005048e8 ["INT_ADD", "register:40f0:8", ["const:5048e8:8", "const:4:8"]]
- 005048e8 ["CALL", null, ["callee:00c580b0:8"]]
+ 00504928 ["INT_ADD", "register:40f0:8", ["const:504928:8", "const:4:8"]]
+ 00504928 ["CALL", null, ["callee:00c580b0:8"]]
- 005048e8 bytes f24c1d94
+ 00504928 bytes e24d1d94
- 00504924 ["INT_ADD", "register:40f0:8", ["const:504924:8", "const:4:8"]]
- 00504924 ["CALL", null, ["callee:00c57f10:8"]]
+ 00504964 ["INT_ADD", "register:40f0:8", ["const:504964:8", "const:4:8"]]
+ 00504964 ["CALL", null, ["callee:00c57f10:8"]]
- 00504924 bytes 7b4c1d94
+ 00504964 bytes 6b4d1d94
- 00504820 ["INT_ADD", "register:40f0:8", ["const:504820:8", "const:4:8"]]
- 00504820 ["CALL", null, ["callee:00c59ae0:8"]]
+ 00504860 ["INT_ADD", "register:40f0:8", ["const:504860:8", "const:4:8"]]
+ 00504860 ["CALL", null, ["callee:00c59ae0:8"]]
- 00504820 bytes b0531d94
+ 00504860 bytes a0541d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06d34a7f1b6c2121c9b7a5412ce4241d"></a>

### [`00504dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504dd0.md) → [`00504e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00504/00504e10.md) _ZN5Botan9create_dnERKNS_10Data_StoreE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0054920c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/0054920c.md) [`00549210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549210.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0054924c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/0054924c.md) [`00549250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549250.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

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
    "old": {
      "definition_site": "00504df0",
      "incomplete_value": false,
      "site": "00504e00",
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
            "const:480:8"
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
    "old": {
      "definition_site": "00504e6c",
      "incomplete_value": true,
      "site": "00504e6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00504e40",
      "DATA",
      [
        "storage",
        "00c6a480",
        null,
        "undefined *"
      ]
    ],
    [
      "00504e78",
      "READ",
      [
        "storage",
        "00c6a4a0",
        null,
        "pointer"
      ]
    ],
    [
      "00504e78",
      "READ",
      [
        "storage",
        "00c6a4a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00504e40",
      "DATA",
      [
        "storage",
        "00c6a880",
        null,
        "undefined *"
      ]
    ],
    [
      "00504e78",
      "READ",
      [
        "storage",
        "00c6a8a0",
        null,
        "pointer"
      ]
    ],
    [
      "00504e78",
      "READ",
      [
        "storage",
        "00c6a8a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00504e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504dd0.md#insn-00504e40) · [`00504df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504dd0.md#insn-00504df0) · [`00504e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504dd0.md#insn-00504e10)
- 新版 `00504e80`（命令位置の公開資料なし） · `00504e30`（命令位置の公開資料なし） · `00504e50`（命令位置の公開資料なし）

~~~diff
- 00504e40 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00504e80 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00504e40 bytes a83c00d0
+ 00504e80 bytes a83c00f0
- 00504df0 ["COPY", "tmp:0:8", ["const:480:8"]]
- 00504df0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00504df0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00504df0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00504e30 ["COPY", "tmp:0:8", ["const:880:8"]]
+ 00504e30 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00504e30 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00504e30 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00504df0 bytes 29011291
+ 00504e30 bytes 29012291
- 00504e10 ["INT_ADD", "register:40f0:8", ["const:504e10:8", "const:4:8"]]
- 00504e10 ["CALL", null, ["callee:00c59ad0:8"]]
+ 00504e50 ["INT_ADD", "register:40f0:8", ["const:504e50:8", "const:4:8"]]
+ 00504e50 ["CALL", null, ["callee:00c59ad0:8"]]
- 00504e10 bytes 30521d94
+ 00504e50 bytes 20531d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-486a6baba4608b89bba2d7f88dc24e8f"></a>

### [`00505040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00505/00505040.md) → [`00505080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00505/00505080.md) _ZN5Botan15create_alt_nameERKNS_10Data_StoreE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`00549314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549314.md) [`00549318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549318.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`00549354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549354.md) [`00549358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549358.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

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
    "old": {
      "definition_site": "00505070",
      "incomplete_value": false,
      "site": "00505070",
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
            "const:510:8"
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
      "005050b0",
      "DATA",
      [
        "storage",
        "00c6a510",
        null,
        "undefined *"
      ]
    ],
    [
      "005050e8",
      "READ",
      [
        "storage",
        "00c6a530",
        null,
        "pointer"
      ]
    ],
    [
      "005050e8",
      "READ",
      [
        "storage",
        "00c6a538",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005050b0",
      "DATA",
      [
        "storage",
        "00c6a910",
        null,
        "undefined *"
      ]
    ],
    [
      "005050e8",
      "READ",
      [
        "storage",
        "00c6a930",
        null,
        "pointer"
      ]
    ],
    [
      "005050e8",
      "READ",
      [
        "storage",
        "00c6a938",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00505060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00505/00505040.md#insn-00505060) · [`00505080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00505/00505040.md#insn-00505080) · [`005050ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00505/00505040.md#insn-005050ac)
- 新版 `005050a0`（命令位置の公開資料なし） · `005050c0`（命令位置の公開資料なし） · `005050ec`（命令位置の公開資料なし）

~~~diff
- 00505060 ["COPY", "tmp:0:8", ["const:510:8"]]
- 00505060 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00505060 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00505060 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005050a0 ["COPY", "tmp:0:8", ["const:910:8"]]
+ 005050a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005050a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005050a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00505060 bytes 29411491
+ 005050a0 bytes 29412491
- 00505080 ["INT_ADD", "register:40f0:8", ["const:505080:8", "const:4:8"]]
- 00505080 ["CALL", null, ["callee:00c59ad0:8"]]
+ 005050c0 ["INT_ADD", "register:40f0:8", ["const:5050c0:8", "const:4:8"]]
+ 005050c0 ["CALL", null, ["callee:00c59ad0:8"]]
- 00505080 bytes 94511d94
+ 005050c0 bytes 84521d94
- 005050ac ["COPY", "register:0:8", ["register:4040:8"]]
- 005050ac ["INT_ADD", "register:40f0:8", ["const:5050ac:8", "const:4:8"]]
- 005050ac ["CALLIND", null, ["register:0:8"]]
+ 005050ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 005050ec ["INT_ADD", "register:40f0:8", ["const:5050ec:8", "const:4:8"]]
+ 005050ec ["CALLIND", null, ["register:0:8"]]
- 005050ac bytes 00013fd6
+ 005050ec bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5916aeb74f7bf7cbd23e4be3272323b"></a>

### [`005052c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00505/005052c4.md) → [`00505304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00505/00505304.md) _ZN5Botan25key_constraints_to_stringENS_15Key_ConstraintsE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c59720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59720.md) · 呼出先 9件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00440f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f1c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00c59b20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59b20.md) · 呼出先 9件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00440f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
    "old": {
      "definition_site": "00505330",
      "incomplete_value": true,
      "site": "00505330",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7fe:8"
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
    "old": {
      "definition_site": "00505334",
      "incomplete_value": true,
      "site": "00505334",
      "value": [
        "LOAD",
        "8",
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
    "old": {
      "definition_site": "00505368",
      "incomplete_value": true,
      "site": "00505368",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b2c:8"
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
      "00505360",
      "READ",
      [
        "storage",
        "002a77fe",
        null,
        "string"
      ]
    ],
    [
      "00505364",
      "READ",
      [
        "storage",
        "002a7804",
        null,
        "string"
      ]
    ],
    [
      "00505390",
      "READ",
      [
        "storage",
        "002b2b2c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00505360",
      "READ",
      [
        "storage",
        "002a78da",
        null,
        "string"
      ]
    ],
    [
      "00505364",
      "READ",
      [
        "storage",
        "002a78e0",
        null,
        "string"
      ]
    ],
    [
      "00505390",
      "READ",
      [
        "storage",
        "002b2b6c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00505318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00505/005052c4.md#insn-00505318) · [`00505340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00505/005052c4.md#insn-00505340) · [`00505348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00505/005052c4.md#insn-00505348)
- 新版 `00505358`（命令位置の公開資料なし） · `00505380`（命令位置の公開資料なし） · `00505388`（命令位置の公開資料なし）

~~~diff
- 00505318 ["COPY", "tmp:0:8", ["const:7fe:8"]]
- 00505318 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00505318 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00505318 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00505358 ["COPY", "tmp:0:8", ["const:8da:8"]]
+ 00505358 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00505358 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00505358 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00505318 bytes 29f91f91
+ 00505358 bytes 29692391
- 00505340 ["INT_ADD", "register:40f0:8", ["const:505340:8", "const:4:8"]]
- 00505340 ["CALL", null, ["callee:00c57e90:8"]]
+ 00505380 ["INT_ADD", "register:40f0:8", ["const:505380:8", "const:4:8"]]
+ 00505380 ["CALL", null, ["callee:00c57e90:8"]]
- 00505340 bytes d4491d94
+ 00505380 bytes c44a1d94
- 00505348 ["COPY", "tmp:0:8", ["const:b2c:8"]]
- 00505348 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00505348 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00505348 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00505388 ["COPY", "tmp:0:8", ["const:b6c:8"]]
+ 00505388 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00505388 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00505388 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00505348 bytes 29b12c91
+ 00505388 bytes 29b12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83737316cdc3685495f94e54e00d69c7"></a>

### [`00505ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00505/00505ebc.md) → [`00505efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00505/00505efc.md) _ZN5Botan42verify_cert_constraints_valid_for_key_typeERKNS_10Public_KeyENS_15Key_ConstraintsE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59730.md) · 呼出先 10件 [`004a680c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a680c.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 1件 [`00c59b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59b30.md) · 呼出先 10件 [`004a684c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a684c.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

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
    "old": {
      "definition_site": "00506174",
      "incomplete_value": false,
      "site": "00506180",
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
            "const:89:8"
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
    "old": {
      "definition_site": "00506188",
      "incomplete_value": false,
      "site": "00506190",
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
            "const:668:8"
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
    "old": {
      "definition_site": "005061f8",
      "incomplete_value": true,
      "site": "00506204",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
      "005061b4",
      "PARAM",
      [
        "storage",
        "002a0089",
        null,
        "string"
      ]
    ],
    [
      "005061c8",
      "PARAM",
      [
        "storage",
        "002a6668",
        null,
        "string"
      ]
    ],
    [
      "00506234",
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
      "005061b4",
      "PARAM",
      [
        "storage",
        "002a0156",
        null,
        "string"
      ]
    ],
    [
      "005061c8",
      "PARAM",
      [
        "storage",
        "002a6744",
        null,
        "string"
      ]
    ],
    [
      "00506234",
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

- 旧版 [`00506180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00505/00505ebc.md#insn-00506180) · [`00506190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00505/00505ebc.md#insn-00506190) · [`005061c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00505/00505ebc.md#insn-005061c4)
- 新版 `005061c0`（命令位置の公開資料なし） · `005061d0`（命令位置の公開資料なし） · `00506204`（命令位置の公開資料なし）

~~~diff
- 00506180 ["INT_ADD", "register:40f0:8", ["const:506180:8", "const:4:8"]]
- 00506180 ["CALL", null, ["callee:00c580b0:8"]]
+ 005061c0 ["INT_ADD", "register:40f0:8", ["const:5061c0:8", "const:4:8"]]
+ 005061c0 ["CALL", null, ["callee:00c580b0:8"]]
- 00506180 bytes cc461d94
+ 005061c0 bytes bc471d94
- 00506190 ["INT_ADD", "register:40f0:8", ["const:506190:8", "const:4:8"]]
- 00506190 ["CALL", null, ["callee:00c57f70:8"]]
+ 005061d0 ["INT_ADD", "register:40f0:8", ["const:5061d0:8", "const:4:8"]]
+ 005061d0 ["CALL", null, ["callee:00c57f70:8"]]
- 00506190 bytes 78461d94
+ 005061d0 bytes 68471d94
- 005061c4 ["INT_ADD", "register:40f0:8", ["const:5061c4:8", "const:4:8"]]
- 005061c4 ["CALL", null, ["callee:004a684c:8"]]
+ 00506204 ["INT_ADD", "register:40f0:8", ["const:506204:8", "const:4:8"]]
+ 00506204 ["CALL", null, ["callee:004a684c:8"]]
- 005061c4 bytes 9281fe97
+ 00506204 bytes 9281fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-535c4685e4cf93d1ad24ae3650b09bf3"></a>

### [`005062f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00506/005062f0.md) → [`00506330`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00506/00506330.md) _ZN5Botan11GeneralNameC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59780.md) · 呼出先 12件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00c59b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59b80.md) · 呼出先 12件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
    "old": {
      "definition_site": "00506334",
      "incomplete_value": true,
      "site": "0050633c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00506518",
      "incomplete_value": false,
      "site": "00506520",
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
            "const:cfb:8"
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
    "old": {
      "definition_site": "00506550",
      "incomplete_value": true,
      "site": "0050655c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
      "0050635c",
      "READ",
      [
        "storage",
        "00c9ad28",
        null,
        "pointer"
      ]
    ],
    [
      "0050637c",
      "DATA",
      [
        "storage",
        "00c67cd0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00506558",
      "PARAM",
      [
        "storage",
        "002b1cfb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0050635c",
      "READ",
      [
        "storage",
        "00c9b128",
        null,
        "pointer"
      ]
    ],
    [
      "0050637c",
      "DATA",
      [
        "storage",
        "00c680d0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00506558",
      "PARAM",
      [
        "storage",
        "002b1d3b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00506520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00506/005062f0.md#insn-00506520) · [`0050655c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00506/005062f0.md#insn-0050655c) · [`00506310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00506/005062f0.md#insn-00506310)
- 新版 `00506560`（命令位置の公開資料なし） · `0050659c`（命令位置の公開資料なし） · `00506350`（命令位置の公開資料なし）

~~~diff
- 00506520 ["INT_ADD", "register:40f0:8", ["const:506520:8", "const:4:8"]]
- 00506520 ["CALL", null, ["callee:0043ddd8:8"]]
+ 00506560 ["INT_ADD", "register:40f0:8", ["const:506560:8", "const:4:8"]]
+ 00506560 ["CALL", null, ["callee:0043ddd8:8"]]
- 00506520 bytes 1edefc97
+ 00506560 bytes 1edefc97
- 0050655c ["INT_ADD", "register:40f0:8", ["const:50655c:8", "const:4:8"]]
- 0050655c ["CALL", null, ["callee:00c57f10:8"]]
+ 0050659c ["INT_ADD", "register:40f0:8", ["const:50659c:8", "const:4:8"]]
+ 0050659c ["CALL", null, ["callee:00c57f10:8"]]
- 0050655c bytes 6d451d94
+ 0050659c bytes 5d461d94
- 00506310 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00506350 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00506310 bytes a83c0090
+ 00506350 bytes a83c00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55c73a0d5d3e680f8487439f7b05d6df"></a>

### [`00506608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00506/00506608.md) → [`00506648`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00506/00506648.md) _ZNK5Botan11GeneralName11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c590e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c590e0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c594e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c594e0.md)

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
    "old": {
      "definition_site": "0050663c",
      "incomplete_value": true,
      "site": "00506658",
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
                "const:db7:8"
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
    "old": {
      "definition_site": "00506684",
      "incomplete_value": true,
      "site": "00506690",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005066c0",
      "incomplete_value": false,
      "site": "005066d0",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "00506680",
      "incomplete_value": false,
      "site": "00506690",
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
      "0050667c",
      "READ",
      [
        "storage",
        "002bedb7",
        null,
        "string"
      ]
    ],
    [
      "005066c0",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "005066c4",
      "READ",
      [
        "storage",
        "00c9abd0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050667c",
      "READ",
      [
        "storage",
        "002bedf7",
        null,
        "string"
      ]
    ],
    [
      "005066c0",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "005066c4",
      "READ",
      [
        "storage",
        "00c9afd0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00506690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00506/00506608.md#insn-00506690) · [`0050662c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00506/00506608.md#insn-0050662c) · [`00506634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00506/00506608.md#insn-00506634)
- 新版 `005066d0`（命令位置の公開資料なし） · `0050666c`（命令位置の公開資料なし） · `00506674`（命令位置の公開資料なし）

~~~diff
- 00506690 ["INT_ADD", "register:40f0:8", ["const:506690:8", "const:4:8"]]
- 00506690 ["CALL", null, ["callee:00c57f10:8"]]
+ 005066d0 ["INT_ADD", "register:40f0:8", ["const:5066d0:8", "const:4:8"]]
+ 005066d0 ["CALL", null, ["callee:00c57f10:8"]]
- 00506690 bytes 20451d94
+ 005066d0 bytes 10461d94
- 0050662c ["INT_ADD", "register:40f0:8", ["const:50662c:8", "const:4:8"]]
- 0050662c ["CALL", null, ["callee:00c57ef0:8"]]
+ 0050666c ["INT_ADD", "register:40f0:8", ["const:50666c:8", "const:4:8"]]
+ 0050666c ["CALL", null, ["callee:00c57ef0:8"]]
- 0050662c bytes 31451d94
+ 0050666c bytes 21461d94
- 00506634 ["COPY", "tmp:0:8", ["const:db7:8"]]
- 00506634 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00506634 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00506634 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00506674 ["COPY", "tmp:0:8", ["const:df7:8"]]
+ 00506674 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00506674 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00506674 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00506634 bytes 29dd3691
+ 00506674 bytes 29dd3791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5da4e59e5b7878353c278e713af10efc"></a>

### [`005066d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00506/005066d8.md) → [`00506718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00506/00506718.md) _ZN5Botan11GeneralName11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 29件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00451870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451870.md) [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md)
- 新版 呼出元 0件  · 呼出先 29件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004518b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004518b0.md) [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md)

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
    "old": {
      "definition_site": "00506764",
      "incomplete_value": true,
      "site": "00506764",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "005067e8",
      "incomplete_value": true,
      "site": "005067f0",
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
    "old": {
      "definition_site": "005067f8",
      "incomplete_value": true,
      "site": "005067f8",
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
      "0050678c",
      "READ",
      [
        "storage",
        "00c9acd0",
        null,
        "pointer"
      ]
    ],
    [
      "005067a4",
      "DATA",
      [
        "storage",
        "00c675f8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00506810",
      "PARAM",
      [
        "storage",
        "002ba2ea",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0050678c",
      "READ",
      [
        "storage",
        "00c9b0d0",
        null,
        "pointer"
      ]
    ],
    [
      "005067a4",
      "DATA",
      [
        "storage",
        "00c679f8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00506810",
      "PARAM",
      [
        "storage",
        "002ba32a",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00506798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00506/005066d8.md#insn-00506798) · [`005067a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00506/005066d8.md#insn-005067a4) · [`005067b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00506/005066d8.md#insn-005067b8)
- 新版 `005067d8`（命令位置の公開資料なし） · `005067e4`（命令位置の公開資料なし） · `005067f8`（命令位置の公開資料なし）

~~~diff
- 00506798 ["INT_ADD", "register:40f0:8", ["const:506798:8", "const:4:8"]]
- 00506798 ["CALL", null, ["callee:00c599a0:8"]]
+ 005067d8 ["INT_ADD", "register:40f0:8", ["const:5067d8:8", "const:4:8"]]
+ 005067d8 ["CALL", null, ["callee:00c599a0:8"]]
- 00506798 bytes 824b1d94
+ 005067d8 bytes 724c1d94
- 005067a4 ["INT_ADD", "register:40f0:8", ["const:5067a4:8", "const:4:8"]]
- 005067a4 ["CALL", null, ["callee:00c581b0:8"]]
+ 005067e4 ["INT_ADD", "register:40f0:8", ["const:5067e4:8", "const:4:8"]]
+ 005067e4 ["CALL", null, ["callee:00c581b0:8"]]
- 005067a4 bytes 83451d94
+ 005067e4 bytes 73461d94
- 005067b8 ["INT_ADD", "register:40f0:8", ["const:5067b8:8", "const:4:8"]]
- 005067b8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005067f8 ["INT_ADD", "register:40f0:8", ["const:5067f8:8", "const:4:8"]]
+ 005067f8 ["CALL", null, ["callee:00c57eb0:8"]]
- 005067b8 bytes be441d94
+ 005067f8 bytes ae451d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84d55d4d338e502f08653e1958bf0e93"></a>

### [`00506f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00506/00506f50.md) → [`00506f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00506/00506f90.md) _ZN5Botan7X509_DN11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`004ffde0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ffde0.md) [`00513270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00513/00513270.md) [`00c59740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59740.md) · 呼出先 12件 [`004a5940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5940.md) [`00548e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548e28.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md)
- 新版 呼出元 3件 [`004ffe20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ffe20.md) [`005132b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00513/005132b0.md) [`00c59b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59b40.md) · 呼出先 12件 [`004a5980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5980.md) [`00548e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548e68.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md)

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
    "old": {
      "definition_site": "00506fe4",
      "incomplete_value": true,
      "site": "00506fe4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
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
    "old": {
      "definition_site": "0050711c",
      "incomplete_value": true,
      "site": "0050711c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 19,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
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
    "old": {
      "definition_site": "005071a4",
      "incomplete_value": true,
      "site": "005071a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00507014",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "0050714c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "005071d4",
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
      "00507014",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "0050714c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "005071d4",
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

- 旧版 [`00506fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00506/00506f50.md#insn-00506fa4) · [`00506fe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00506/00506f50.md#insn-00506fe4) · [`0050711c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00506/00506f50.md#insn-0050711c)
- 新版 `00506fe4`（命令位置の公開資料なし） · `00507024`（命令位置の公開資料なし） · `0050715c`（命令位置の公開資料なし）

~~~diff
- 00506fa4 ["INT_ADD", "register:40f0:8", ["const:506fa4:8", "const:4:8"]]
- 00506fa4 ["CALL", null, ["callee:00c58710:8"]]
+ 00506fe4 ["INT_ADD", "register:40f0:8", ["const:506fe4:8", "const:4:8"]]
+ 00506fe4 ["CALL", null, ["callee:00c58710:8"]]
- 00506fa4 bytes db441d94
+ 00506fe4 bytes cb451d94
- 00506fe4 ["COPY", "register:0:8", ["register:4048:8"]]
- 00506fe4 ["INT_ADD", "register:40f0:8", ["const:506fe4:8", "const:4:8"]]
- 00506fe4 ["CALLIND", null, ["register:0:8"]]
+ 00507024 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00507024 ["INT_ADD", "register:40f0:8", ["const:507024:8", "const:4:8"]]
+ 00507024 ["CALLIND", null, ["register:0:8"]]
- 00506fe4 bytes 20013fd6
+ 00507024 bytes 20013fd6
- 0050711c ["COPY", "register:0:8", ["register:4048:8"]]
- 0050711c ["INT_ADD", "register:40f0:8", ["const:50711c:8", "const:4:8"]]
- 0050711c ["CALLIND", null, ["register:0:8"]]
+ 0050715c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050715c ["INT_ADD", "register:40f0:8", ["const:50715c:8", "const:4:8"]]
+ 0050715c ["CALLIND", null, ["register:0:8"]]
- 0050711c bytes 20013fd6
+ 0050715c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4db173fd4a5f00b4afd10b08122ea149"></a>

### [`0050732c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/0050732c.md) → [`0050736c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00507/0050736c.md) _ZNK5Botan11GeneralName7matchesERKNS_16X509_CertificateE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59750.md) · 呼出先 23件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00440f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f1c.md) [`00451870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451870.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00507a74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/00507a74.md)
- 新版 呼出元 1件 [`00c59b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59b50.md) · 呼出先 23件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00440f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f5c.md) [`004518b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004518b0.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00507ab4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00507/00507ab4.md)

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
    "old": {
      "definition_site": "005073fc",
      "incomplete_value": true,
      "site": "005073fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "005073fc",
      "incomplete_value": true,
      "site": "005073fc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9a000:8"
              ],
              [
                "leaf",
                "const:d38:8"
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
    "old": {
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
      "0050741c",
      "READ",
      [
        "storage",
        "00c9ad30",
        null,
        "pointer"
      ]
    ],
    [
      "00507420",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "0050743c",
      "DATA",
      [
        "storage",
        "00c6a590",
        null,
        "undefined1[88]"
      ]
    ]
  ],
  "added": [
    [
      "0050741c",
      "READ",
      [
        "storage",
        "00c9b130",
        null,
        "pointer"
      ]
    ],
    [
      "00507420",
      "READ",
      [
        "storage",
        "00c9b138",
        null,
        "pointer"
      ]
    ],
    [
      "0050743c",
      "DATA",
      [
        "storage",
        "00c6a990",
        null,
        "undefined1[88]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00507370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/0050732c.md#insn-00507370) · [`0050737c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/0050732c.md#insn-0050737c) · [`005073d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/0050732c.md#insn-005073d0)
- 新版 `005073b0`（命令位置の公開資料なし） · `005073bc`（命令位置の公開資料なし） · `00507410`（命令位置の公開資料なし）

~~~diff
- 00507370 ["INT_ADD", "register:40f0:8", ["const:507370:8", "const:4:8"]]
- 00507370 ["CALL", null, ["callee:00c599f0:8"]]
+ 005073b0 ["INT_ADD", "register:40f0:8", ["const:5073b0:8", "const:4:8"]]
+ 005073b0 ["CALL", null, ["callee:00c599f0:8"]]
- 00507370 bytes a0481d94
+ 005073b0 bytes 90491d94
- 0050737c ["INT_ADD", "register:40f0:8", ["const:50737c:8", "const:4:8"]]
- 0050737c ["CALL", null, ["callee:00c599f0:8"]]
+ 005073bc ["INT_ADD", "register:40f0:8", ["const:5073bc:8", "const:4:8"]]
+ 005073bc ["CALL", null, ["callee:00c599f0:8"]]
- 0050737c bytes 9d481d94
+ 005073bc bytes 8d491d94
- 005073d0 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00507410 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 005073d0 bytes 883c00f0
+ 00507410 bytes a83c0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b326527e695a2f971e2f094e551b86ff"></a>

### [`00507a8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/00507a8c.md) → [`00507acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00507/00507acc.md) _ZNK5Botan11GeneralName11matches_dnsERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0050732c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/0050732c.md) · 呼出先 9件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0050736c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00507/0050736c.md) · 呼出先 9件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
    "old": {
      "definition_site": "00507b98",
      "incomplete_value": false,
      "site": "00507ba8",
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
            "const:30f:8"
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
      "00507bd8",
      "PARAM",
      [
        "storage",
        "002a630f",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00507bd8",
      "PARAM",
      [
        "storage",
        "002a63eb",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00507ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/00507a8c.md#insn-00507ba8) · [`00507b24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/00507a8c.md#insn-00507b24) · [`00507b98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/00507a8c.md#insn-00507b98)
- 新版 `00507be8`（命令位置の公開資料なし） · `00507b64`（命令位置の公開資料なし） · `00507bd8`（命令位置の公開資料なし）

~~~diff
- 00507ba8 ["INT_ADD", "register:40f0:8", ["const:507ba8:8", "const:4:8"]]
- 00507ba8 ["CALL", null, ["callee:00c580b0:8"]]
+ 00507be8 ["INT_ADD", "register:40f0:8", ["const:507be8:8", "const:4:8"]]
+ 00507be8 ["CALL", null, ["callee:00c580b0:8"]]
- 00507ba8 bytes 42401d94
+ 00507be8 bytes 32411d94
- 00507b24 ["INT_ADD", "register:40f0:8", ["const:507b24:8", "const:4:8"]]
- 00507b24 ["CALL", null, ["callee:00c58050:8"]]
+ 00507b64 ["INT_ADD", "register:40f0:8", ["const:507b64:8", "const:4:8"]]
+ 00507b64 ["CALL", null, ["callee:00c58050:8"]]
- 00507b24 bytes 4b401d94
+ 00507b64 bytes 3b411d94
- 00507b98 ["COPY", "tmp:0:8", ["const:30f:8"]]
- 00507b98 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00507b98 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00507b98 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00507bd8 ["COPY", "tmp:0:8", ["const:3eb:8"]]
+ 00507bd8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00507bd8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00507bd8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00507b98 bytes 003c0c91
+ 00507bd8 bytes 00ac0f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1fac4ca79fb6c0219e437ae92a655a59"></a>

### [`00507f68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/00507f68.md) → [`00507fa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00507/00507fa8.md) _ZNK5Botan11GeneralName10matches_dnERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0050732c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/0050732c.md) · 呼出先 13件 [`0050857c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/0050857c.md) [`00508be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/00508be8.md) [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`00549628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549628.md) [`00549688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549688.md)
- 新版 呼出元 1件 [`0050736c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00507/0050736c.md) · 呼出先 13件 [`005085bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00508/005085bc.md) [`00508c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00508/00508c28.md) [`0053af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053a/0053af90.md) [`00549668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549668.md) [`005496c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/005496c8.md)

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
    "old": {
      "definition_site": "00507fd8",
      "incomplete_value": true,
      "site": "00507fd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00507fe4",
      "incomplete_value": true,
      "site": "00507fe4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "005081d4",
      "incomplete_value": true,
      "site": "005081dc",
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
      "00508000",
      "READ",
      [
        "storage",
        "00c9acd0",
        null,
        "pointer"
      ]
    ],
    [
      "00508018",
      "DATA",
      [
        "storage",
        "00c675f8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00508024",
      "DATA",
      [
        "storage",
        "00c675f8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00508000",
      "READ",
      [
        "storage",
        "00c9b0d0",
        null,
        "pointer"
      ]
    ],
    [
      "00508018",
      "DATA",
      [
        "storage",
        "00c679f8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00508024",
      "DATA",
      [
        "storage",
        "00c679f8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050819c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/00507f68.md#insn-0050819c) · [`005081b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/00507f68.md#insn-005081b8) · [`00507fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/00507f68.md#insn-00507fa0)
- 新版 `005081dc`（命令位置の公開資料なし） · `005081f8`（命令位置の公開資料なし） · `00507fe0`（命令位置の公開資料なし）

~~~diff
- 0050819c ["INT_ADD", "register:40f0:8", ["const:50819c:8", "const:4:8"]]
- 0050819c ["CALL", null, ["callee:00c57eb0:8"]]
+ 005081dc ["INT_ADD", "register:40f0:8", ["const:5081dc:8", "const:4:8"]]
+ 005081dc ["CALL", null, ["callee:00c57eb0:8"]]
- 0050819c bytes 453e1d94
+ 005081dc bytes 353f1d94
- 005081b8 ["INT_ADD", "register:40f0:8", ["const:5081b8:8", "const:4:8"]]
- 005081b8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005081f8 ["INT_ADD", "register:40f0:8", ["const:5081f8:8", "const:4:8"]]
+ 005081f8 ["CALL", null, ["callee:00c57eb0:8"]]
- 005081b8 bytes 3e3e1d94
+ 005081f8 bytes 2e3f1d94
- 00507fa0 ["INT_ADD", "register:40f0:8", ["const:507fa0:8", "const:4:8"]]
- 00507fa0 ["CALL", null, ["callee:005085bc:8"]]
+ 00507fe0 ["INT_ADD", "register:40f0:8", ["const:507fe0:8", "const:4:8"]]
+ 00507fe0 ["CALL", null, ["callee:005085bc:8"]]
- 00507fa0 bytes 77010094
+ 00507fe0 bytes 77010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ef48234e519bb93f54ae4dc62450995"></a>

### [`00508324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/00508324.md) → [`00508364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00508/00508364.md) _ZNK5Botan11GeneralName10matches_ipERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0050732c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/0050732c.md) · 呼出先 12件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00486d38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00486/00486d38.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00547b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547b2c.md) [`00547b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547b30.md)
- 新版 呼出元 1件 [`0050736c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00507/0050736c.md) · 呼出先 12件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00486d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00486/00486d78.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00547b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547b6c.md) [`00547b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547b70.md)

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
    "old": {
      "definition_site": "00508358",
      "incomplete_value": false,
      "site": "00508360",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00508484",
      "incomplete_value": false,
      "site": "0050848c",
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
            "const:92:8"
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
    "old": {
      "definition_site": "005084bc",
      "incomplete_value": true,
      "site": "005084c8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
      "005083a0",
      "DATA",
      [
        "storage",
        "00c6a2b0",
        null,
        "undefined *"
      ]
    ],
    [
      "005083e8",
      "READ",
      [
        "storage",
        "00c6a2d0",
        null,
        "pointer"
      ]
    ],
    [
      "005083e8",
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
      "005083a0",
      "DATA",
      [
        "storage",
        "00c6a6b0",
        null,
        "undefined *"
      ]
    ],
    [
      "005083e8",
      "READ",
      [
        "storage",
        "00c6a6d0",
        null,
        "pointer"
      ]
    ],
    [
      "005083e8",
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

- 旧版 [`0050848c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/00508324.md#insn-0050848c) · [`005084c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/00508324.md#insn-005084c8) · [`00508350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/00508324.md#insn-00508350)
- 新版 `005084cc`（命令位置の公開資料なし） · `00508508`（命令位置の公開資料なし） · `00508390`（命令位置の公開資料なし）

~~~diff
- 0050848c ["INT_ADD", "register:40f0:8", ["const:50848c:8", "const:4:8"]]
- 0050848c ["CALL", null, ["callee:0043ddd8:8"]]
+ 005084cc ["INT_ADD", "register:40f0:8", ["const:5084cc:8", "const:4:8"]]
+ 005084cc ["CALL", null, ["callee:0043ddd8:8"]]
- 0050848c bytes 43d6fc97
+ 005084cc bytes 43d6fc97
- 005084c8 ["INT_ADD", "register:40f0:8", ["const:5084c8:8", "const:4:8"]]
- 005084c8 ["CALL", null, ["callee:00c57f10:8"]]
+ 00508508 ["INT_ADD", "register:40f0:8", ["const:508508:8", "const:4:8"]]
+ 00508508 ["CALL", null, ["callee:00c57f10:8"]]
- 005084c8 bytes 923d1d94
+ 00508508 bytes 823e1d94
- 00508350 ["INT_ADD", "register:40f0:8", ["const:508350:8", "const:4:8"]]
- 00508350 ["CALL", null, ["callee:00c59900:8"]]
+ 00508390 ["INT_ADD", "register:40f0:8", ["const:508390:8", "const:4:8"]]
+ 00508390 ["CALL", null, ["callee:00c59900:8"]]
- 00508350 bytes 6c441d94
+ 00508390 bytes 5c451d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da0da723da560d8a6836c9ec6559092c"></a>

### [`0050857c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/0050857c.md) → [`005085bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00508/005085bc.md) FUN_005085bc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`004ffa6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ffa6c.md) [`00507f68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/00507f68.md) · 呼出先 4件 [`00548218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548218.md) [`00c57de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57de0.md) [`00c57df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57df0.md) [`00c58030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58030.md)
- 新版 呼出元 2件 [`004ffaac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ffaac.md) [`00507fa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00507/00507fa8.md) · 呼出先 4件 [`00548258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548258.md) [`00c581e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581e0.md) [`00c581f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581f0.md) [`00c58430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58430.md)

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
    "old": {
      "definition_site": "005085cc",
      "incomplete_value": true,
      "site": "005085cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "old": {
      "definition_site": "005085d0",
      "incomplete_value": true,
      "site": "005085d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "old": {
      "definition_site": "005085c8",
      "incomplete_value": true,
      "site": "005085d8",
      "value": [
        "LOAD",
        "8",
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
      "005085e4",
      "READ",
      [
        "storage",
        "00c9a818",
        null,
        "pointer"
      ]
    ],
    [
      "005085f0",
      "READ",
      [
        "storage",
        "00c9a810",
        null,
        "pointer"
      ]
    ],
    [
      "00508608",
      "READ",
      [
        "storage",
        "00c92cf8",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "005085e4",
      "READ",
      [
        "storage",
        "00c9ac18",
        null,
        "pointer"
      ]
    ],
    [
      "005085f0",
      "READ",
      [
        "storage",
        "00c9ac10",
        null,
        "pointer"
      ]
    ],
    [
      "00508608",
      "READ",
      [
        "storage",
        "00c930f8",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005085a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/0050857c.md#insn-005085a4) · [`005085ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/0050857c.md#insn-005085ac) · [`005085b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/0050857c.md#insn-005085b0)
- 新版 `005085e4`（命令位置の公開資料なし） · `005085f0`（命令位置の公開資料なし）

~~~diff
- 005085a4 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:818:8"]]
- 005085a4 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
+ 005085e4 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:c18:8"]]
+ 005085e4 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
- 005085a4 bytes 390f44f9
+ 005085e4 bytes 390f46f9
- 005085ac ["COPY", "register:40e0:8", ["register:4000:8"]]
- 005085ac bytes fc0300aa
- 005085b0 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:810:8"]]
- 005085b0 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 005085f0 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:c10:8"]]
+ 005085f0 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 005085b0 bytes 180b44f9
+ 005085f0 bytes 180b46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2a8ebb91c3eb85671717b292bb52a57"></a>

### [`005086e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/005086e8.md) → [`00508728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00508/00508728.md) _ZN5BotanrsERNSt6__ndk113basic_istreamIcNS0_11char_traitsIcEEEERNS_7X509_DNE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59590.md) · 呼出先 12件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00515330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515330.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00c59990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59990.md) · 呼出先 12件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00515370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/00515370.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

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
    "old": {
      "definition_site": "005089cc",
      "incomplete_value": false,
      "site": "005089d4",
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
            "const:678:8"
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
    "old": {
      "definition_site": "00508a04",
      "incomplete_value": true,
      "site": "00508a10",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00508a40",
      "incomplete_value": false,
      "site": "00508a50",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "00508a00",
      "incomplete_value": false,
      "site": "00508a10",
      "value": [
        "leaf",
        "const:535828:8"
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
      "00508a0c",
      "PARAM",
      [
        "storage",
        "002a6678",
        null,
        "string"
      ]
    ],
    [
      "00508a40",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "00508a44",
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
      "00508a0c",
      "PARAM",
      [
        "storage",
        "002a6754",
        null,
        "string"
      ]
    ],
    [
      "00508a40",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "00508a44",
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

- 旧版 [`005089d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/005086e8.md#insn-005089d4) · [`00508a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/005086e8.md#insn-00508a10) · [`00508774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/005086e8.md#insn-00508774)
- 新版 `00508a14`（命令位置の公開資料なし） · `00508a50`（命令位置の公開資料なし） · `005087b4`（命令位置の公開資料なし）

~~~diff
- 005089d4 ["INT_ADD", "register:40f0:8", ["const:5089d4:8", "const:4:8"]]
- 005089d4 ["CALL", null, ["callee:0043ddd8:8"]]
+ 00508a14 ["INT_ADD", "register:40f0:8", ["const:508a14:8", "const:4:8"]]
+ 00508a14 ["CALL", null, ["callee:0043ddd8:8"]]
- 005089d4 bytes f1d4fc97
+ 00508a14 bytes f1d4fc97
- 00508a10 ["INT_ADD", "register:40f0:8", ["const:508a10:8", "const:4:8"]]
- 00508a10 ["CALL", null, ["callee:00c57f10:8"]]
+ 00508a50 ["INT_ADD", "register:40f0:8", ["const:508a50:8", "const:4:8"]]
+ 00508a50 ["CALL", null, ["callee:00c57f10:8"]]
- 00508a10 bytes 403c1d94
+ 00508a50 bytes 303d1d94
- 00508774 ["INT_ADD", "register:40f0:8", ["const:508774:8", "const:4:8"]]
- 00508774 ["CALL", null, ["callee:00515370:8"]]
+ 005087b4 ["INT_ADD", "register:40f0:8", ["const:5087b4:8", "const:4:8"]]
+ 005087b4 ["CALL", null, ["callee:00515370:8"]]
- 00508774 bytes ef320094
+ 005087b4 bytes ef320094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2713eaf9894deebd6d41c55eb95869a1"></a>

### [`00508be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/00508be8.md) → [`00508c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00508/00508c28.md) FUN_00508c28

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00507f68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/00507f68.md) · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00535b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00507fa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00507/00507fa8.md) · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
    "old": {
      "definition_site": "00508c20",
      "incomplete_value": true,
      "site": "00508c24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00508c50",
      "READ",
      [
        "storage",
        "00c9a940",
        null,
        "pointer"
      ]
    ],
    [
      "00508c64",
      "DATA",
      [
        "storage",
        "00c65e88",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00508c50",
      "READ",
      [
        "storage",
        "00c9ad40",
        null,
        "pointer"
      ]
    ],
    [
      "00508c64",
      "DATA",
      [
        "storage",
        "00c66288",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00508c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/00508be8.md#insn-00508c10) · [`00508c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/00508be8.md#insn-00508c38) · [`00508c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/00508be8.md#insn-00508c50)
- 新版 `00508c50`（命令位置の公開資料なし） · `00508c78`（命令位置の公開資料なし） · `00508c90`（命令位置の公開資料なし）

~~~diff
- 00508c10 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:940:8"]]
- 00508c10 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00508c50 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d40:8"]]
+ 00508c50 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00508c10 bytes 08a144f9
+ 00508c50 bytes 08a146f9
- 00508c38 ["INT_ADD", "register:40f0:8", ["const:508c38:8", "const:4:8"]]
- 00508c38 ["CALL", null, ["callee:00c57e90:8"]]
+ 00508c78 ["INT_ADD", "register:40f0:8", ["const:508c78:8", "const:4:8"]]
+ 00508c78 ["CALL", null, ["callee:00c57e90:8"]]
- 00508c38 bytes 963b1d94
+ 00508c78 bytes 863c1d94
- 00508c50 ["INT_ADD", "register:40f0:8", ["const:508c50:8", "const:4:8"]]
- 00508c50 ["CALL", null, ["callee:00c58000:8"]]
+ 00508c90 ["INT_ADD", "register:40f0:8", ["const:508c90:8", "const:4:8"]]
+ 00508c90 ["CALL", null, ["callee:00c58000:8"]]
- 00508c50 bytes ec3b1d94
+ 00508c90 bytes dc3c1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7f218cad7d3504099440b44c261ad3f"></a>

### [`00508d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/00508d08.md) → [`00508d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00508/00508d48.md) _ZN5Botan14GeneralSubtreeC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 14件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
    "old": {
      "definition_site": "00508d58",
      "incomplete_value": true,
      "site": "00508d58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00508d58",
      "incomplete_value": true,
      "site": "00508d58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00508ffc",
      "incomplete_value": false,
      "site": "00509004",
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
            "const:cfb:8"
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
      "00508d74",
      "READ",
      [
        "storage",
        "00c9ad50",
        null,
        "pointer"
      ]
    ],
    [
      "00508d7c",
      "READ",
      [
        "storage",
        "00c9ad28",
        null,
        "pointer"
      ]
    ],
    [
      "00508d98",
      "DATA",
      [
        "storage",
        "00c67d18",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00508d74",
      "READ",
      [
        "storage",
        "00c9b150",
        null,
        "pointer"
      ]
    ],
    [
      "00508d7c",
      "READ",
      [
        "storage",
        "00c9b128",
        null,
        "pointer"
      ]
    ],
    [
      "00508d98",
      "DATA",
      [
        "storage",
        "00c68118",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00509004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/00508d08.md#insn-00509004) · [`00509040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/00508d08.md#insn-00509040) · [`00508d2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/00508d08.md#insn-00508d2c)
- 新版 `00509044`（命令位置の公開資料なし） · `00509080`（命令位置の公開資料なし） · `00508d6c`（命令位置の公開資料なし）

~~~diff
- 00509004 ["INT_ADD", "register:40f0:8", ["const:509004:8", "const:4:8"]]
- 00509004 ["CALL", null, ["callee:0043ddd8:8"]]
+ 00509044 ["INT_ADD", "register:40f0:8", ["const:509044:8", "const:4:8"]]
+ 00509044 ["CALL", null, ["callee:0043ddd8:8"]]
- 00509004 bytes 65d3fc97
+ 00509044 bytes 65d3fc97
- 00509040 ["INT_ADD", "register:40f0:8", ["const:509040:8", "const:4:8"]]
- 00509040 ["CALL", null, ["callee:00c57f10:8"]]
+ 00509080 ["INT_ADD", "register:40f0:8", ["const:509080:8", "const:4:8"]]
+ 00509080 ["CALL", null, ["callee:00c57f10:8"]]
- 00509040 bytes b43a1d94
+ 00509080 bytes a43b1d94
- 00508d2c ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00508d6c ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00508d2c bytes 883c00d0
+ 00508d6c bytes 883c00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf9b8174f568be76871a15d64ff1a18f"></a>

### [`0050912c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/0050912c.md) → [`0050916c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/0050916c.md) _ZNK5Botan14GeneralSubtree11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
    "old": {
      "definition_site": "0050916c",
      "incomplete_value": true,
      "site": "00509180",
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
                "const:2a1000:8"
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "00509170",
      "incomplete_value": true,
      "site": "00509184",
      "value": [
        "LOAD",
        "8",
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
    "old": {
      "definition_site": "00509174",
      "incomplete_value": true,
      "site": "00509188",
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
                "const:260:8"
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
      "005091ac",
      "READ",
      [
        "storage",
        "002a1fa0",
        null,
        "string"
      ]
    ],
    [
      "005091b0",
      "READ",
      [
        "storage",
        "002a1fb0",
        null,
        "string"
      ]
    ],
    [
      "005091b4",
      "READ",
      [
        "storage",
        "002c2260",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005091ac",
      "READ",
      [
        "storage",
        "002a206d",
        null,
        "string"
      ]
    ],
    [
      "005091b0",
      "READ",
      [
        "storage",
        "002a207d",
        null,
        "string"
      ]
    ],
    [
      "005091b4",
      "READ",
      [
        "storage",
        "002c22a0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005091c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/0050912c.md#insn-005091c4) · [`00509150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/0050912c.md#insn-00509150) · [`0050915c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/0050912c.md#insn-0050915c)
- 新版 `00509204`（命令位置の公開資料なし） · `00509190`（命令位置の公開資料なし） · `0050919c`（命令位置の公開資料なし）

~~~diff
- 005091c4 ["INT_ADD", "register:40f0:8", ["const:5091c4:8", "const:4:8"]]
- 005091c4 ["CALL", null, ["callee:00c57f10:8"]]
+ 00509204 ["INT_ADD", "register:40f0:8", ["const:509204:8", "const:4:8"]]
+ 00509204 ["CALL", null, ["callee:00c57f10:8"]]
- 005091c4 bytes 533a1d94
+ 00509204 bytes 433b1d94
- 00509150 ["INT_ADD", "register:40f0:8", ["const:509150:8", "const:4:8"]]
- 00509150 ["CALL", null, ["callee:00c57ef0:8"]]
+ 00509190 ["INT_ADD", "register:40f0:8", ["const:509190:8", "const:4:8"]]
+ 00509190 ["CALL", null, ["callee:00c57ef0:8"]]
- 00509150 bytes 683a1d94
+ 00509190 bytes 583b1d94
- 0050915c ["INT_ADD", "register:40f0:8", ["const:50915c:8", "const:4:8"]]
- 0050915c ["CALL", null, ["callee:00c57e90:8"]]
+ 0050919c ["INT_ADD", "register:40f0:8", ["const:50919c:8", "const:4:8"]]
+ 0050919c ["CALL", null, ["callee:00c57e90:8"]]
- 0050915c bytes 4d3a1d94
+ 0050919c bytes 3d3b1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c9b7699d6479cb0ae680ab2c1e05d46"></a>

### [`00509214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509214.md) → [`00509254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/00509254.md) _ZN5Botan14GeneralSubtree11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59790.md) · 呼出先 11件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`00c59b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59b90.md) · 呼出先 11件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
    "old": {
      "definition_site": "005092bc",
      "incomplete_value": true,
      "site": "005092bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "0050930c",
      "incomplete_value": false,
      "site": "00509314",
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
            "const:be0:8"
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
    "old": {
      "definition_site": "00509344",
      "incomplete_value": true,
      "site": "00509350",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
      "005092ec",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "0050934c",
      "PARAM",
      [
        "storage",
        "002a8be0",
        null,
        "string"
      ]
    ],
    [
      "00509380",
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
      "005092ec",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "0050934c",
      "PARAM",
      [
        "storage",
        "002a8cad",
        null,
        "string"
      ]
    ],
    [
      "00509380",
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

- 旧版 [`0050927c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509214.md#insn-0050927c) · [`005092bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509214.md#insn-005092bc) · [`00509314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509214.md#insn-00509314)
- 新版 `005092bc`（命令位置の公開資料なし） · `005092fc`（命令位置の公開資料なし） · `00509354`（命令位置の公開資料なし）

~~~diff
- 0050927c ["INT_ADD", "register:40f0:8", ["const:50927c:8", "const:4:8"]]
- 0050927c ["CALL", null, ["callee:00c58710:8"]]
+ 005092bc ["INT_ADD", "register:40f0:8", ["const:5092bc:8", "const:4:8"]]
+ 005092bc ["CALL", null, ["callee:00c58710:8"]]
- 0050927c bytes 253c1d94
+ 005092bc bytes 153d1d94
- 005092bc ["COPY", "register:0:8", ["register:4048:8"]]
- 005092bc ["INT_ADD", "register:40f0:8", ["const:5092bc:8", "const:4:8"]]
- 005092bc ["CALLIND", null, ["register:0:8"]]
+ 005092fc ["COPY", "register:0:8", ["register:4048:8"]]
+ 005092fc ["INT_ADD", "register:40f0:8", ["const:5092fc:8", "const:4:8"]]
+ 005092fc ["CALLIND", null, ["register:0:8"]]
- 005092bc bytes 20013fd6
+ 005092fc bytes 20013fd6
- 00509314 ["INT_ADD", "register:40f0:8", ["const:509314:8", "const:4:8"]]
- 00509314 ["CALL", null, ["callee:0043ddd8:8"]]
+ 00509354 ["INT_ADD", "register:40f0:8", ["const:509354:8", "const:4:8"]]
+ 00509354 ["CALL", null, ["callee:0043ddd8:8"]]
- 00509314 bytes a1d2fc97
+ 00509354 bytes a1d2fc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db536bd3c5b1841468bcb1880aaf278e"></a>

### [`005093b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/005093b8.md) → [`005093f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/005093f8.md) FUN_005093f8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0051adec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051adec.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00459490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57e00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e00.md)
- 新版 呼出元 1件 [`0051ae2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0051a/0051ae2c.md) · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`004594d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58200.md)

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
    "old": {
      "definition_site": "00509424",
      "incomplete_value": true,
      "site": "00509428",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "005093f4",
      "incomplete_value": false,
      "site": "005093f8",
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
            "const:98f:8"
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
    "old": {
      "definition_site": "005094b0",
      "incomplete_value": false,
      "site": "005094b8",
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
            "const:987:8"
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
      "00509434",
      "PARAM",
      [
        "storage",
        "002a998f",
        null,
        null
      ]
    ],
    [
      "00509444",
      "PARAM",
      [
        "storage",
        "002a998f",
        null,
        null
      ]
    ],
    [
      "0050945c",
      "READ",
      [
        "storage",
        "00c9ad28",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00509434",
      "PARAM",
      [
        "storage",
        "002a9a5c",
        null,
        null
      ]
    ],
    [
      "00509444",
      "PARAM",
      [
        "storage",
        "002a9a5c",
        null,
        null
      ]
    ],
    [
      "0050945c",
      "READ",
      [
        "storage",
        "00c9b128",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005093f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/005093b8.md#insn-005093f8) · [`005094b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/005093b8.md#insn-005094b8) · [`005093e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/005093b8.md#insn-005093e4)
- 新版 `00509438`（命令位置の公開資料なし） · `005094f8`（命令位置の公開資料なし） · `00509424`（命令位置の公開資料なし）

~~~diff
- 005093f8 ["INT_ADD", "register:40f0:8", ["const:5093f8:8", "const:4:8"]]
- 005093f8 ["CALL", null, ["callee:004594d0:8"]]
+ 00509438 ["INT_ADD", "register:40f0:8", ["const:509438:8", "const:4:8"]]
+ 00509438 ["CALL", null, ["callee:004594d0:8"]]
- 005093f8 bytes 2640fd97
+ 00509438 bytes 2640fd97
- 005094b8 ["INT_ADD", "register:40f0:8", ["const:5094b8:8", "const:4:8"]]
- 005094b8 ["CALL", null, ["callee:004594d0:8"]]
+ 005094f8 ["INT_ADD", "register:40f0:8", ["const:5094f8:8", "const:4:8"]]
+ 005094f8 ["CALL", null, ["callee:004594d0:8"]]
- 005094b8 bytes f63ffd97
+ 005094f8 bytes f63ffd97
- 005093e4 ["INT_ADD", "register:40f0:8", ["const:5093e4:8", "const:4:8"]]
- 005093e4 ["CALL", null, ["callee:00c58200:8"]]
+ 00509424 ["INT_ADD", "register:40f0:8", ["const:509424:8", "const:4:8"]]
+ 00509424 ["CALL", null, ["callee:00c58200:8"]]
- 005093e4 bytes 873a1d94
+ 00509424 bytes 773b1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b81540fd7dfd7b646cc43c305533ab4"></a>

### [`00509568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509568.md) → [`005095a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/005095a8.md) _ZN5Botan4OCSP7RequestC2ERKNS_16X509_CertificateES4_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 14件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`0053afc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053afc0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`0053b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053b000.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

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
    "old": {
      "definition_site": "005095a4",
      "incomplete_value": true,
      "site": "005095a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00509628",
      "incomplete_value": true,
      "site": "00509628",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00509694",
      "incomplete_value": false,
      "site": "0050969c",
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
            "const:e20:8"
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
      "005095e0",
      "READ",
      [
        "storage",
        "00c9ace0",
        null,
        "pointer"
      ]
    ],
    [
      "005095e8",
      "DATA",
      [
        "storage",
        "00c67688",
        null,
        "undefined1[72]"
      ]
    ],
    [
      "00509658",
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
      "005095e0",
      "READ",
      [
        "storage",
        "00c9b0e0",
        null,
        "pointer"
      ]
    ],
    [
      "005095e8",
      "DATA",
      [
        "storage",
        "00c67a88",
        null,
        "undefined1[72]"
      ]
    ],
    [
      "00509658",
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

- 旧版 [`00509628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509568.md#insn-00509628) · [`0050969c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509568.md#insn-0050969c) · [`005096d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509568.md#insn-005096d8)
- 新版 `00509668`（命令位置の公開資料なし） · `005096dc`（命令位置の公開資料なし） · `00509718`（命令位置の公開資料なし）

~~~diff
- 00509628 ["COPY", "register:0:8", ["register:4048:8"]]
- 00509628 ["INT_ADD", "register:40f0:8", ["const:509628:8", "const:4:8"]]
- 00509628 ["CALLIND", null, ["register:0:8"]]
+ 00509668 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00509668 ["INT_ADD", "register:40f0:8", ["const:509668:8", "const:4:8"]]
+ 00509668 ["CALLIND", null, ["register:0:8"]]
- 00509628 bytes 20013fd6
+ 00509668 bytes 20013fd6
- 0050969c ["INT_ADD", "register:40f0:8", ["const:50969c:8", "const:4:8"]]
- 0050969c ["CALL", null, ["callee:0043ddd8:8"]]
+ 005096dc ["INT_ADD", "register:40f0:8", ["const:5096dc:8", "const:4:8"]]
+ 005096dc ["CALL", null, ["callee:0043ddd8:8"]]
- 0050969c bytes bfd1fc97
+ 005096dc bytes bfd1fc97
- 005096d8 ["INT_ADD", "register:40f0:8", ["const:5096d8:8", "const:4:8"]]
- 005096d8 ["CALL", null, ["callee:00c57f10:8"]]
+ 00509718 ["INT_ADD", "register:40f0:8", ["const:509718:8", "const:4:8"]]
+ 00509718 ["CALL", null, ["callee:00c57f10:8"]]
- 005096d8 bytes 0e391d94
+ 00509718 bytes fe391d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ef09da6b79299bb609303aedaff6f42"></a>

### [`00509814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509814.md) → [`00509854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/00509854.md) FUN_00509854

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
    "old": {
      "definition_site": "00509830",
      "incomplete_value": true,
      "site": "00509834",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00509868",
      "READ",
      [
        "storage",
        "00c9ace0",
        null,
        "pointer"
      ]
    ],
    [
      "00509874",
      "DATA",
      [
        "storage",
        "00c67688",
        null,
        "undefined1[72]"
      ]
    ],
    [
      "005098a8",
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00509868",
      "READ",
      [
        "storage",
        "00c9b0e0",
        null,
        "pointer"
      ]
    ],
    [
      "00509874",
      "DATA",
      [
        "storage",
        "00c67a88",
        null,
        "undefined1[72]"
      ]
    ],
    [
      "005098a8",
      "READ",
      [
        "storage",
        "00c9b158",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00509820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509814.md#insn-00509820) · [`00509828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509814.md#insn-00509828) · [`00509844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509814.md#insn-00509844)
- 新版 `00509860`（命令位置の公開資料なし） · `00509868`（命令位置の公開資料なし） · `00509884`（命令位置の公開資料なし）

~~~diff
- 00509820 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00509860 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00509820 bytes 883c00b0
+ 00509860 bytes 883c00d0
- 00509828 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ce0:8"]]
- 00509828 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00509868 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e0:8"]]
+ 00509868 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00509828 bytes 087146f9
+ 00509868 bytes 087140f9
- 00509844 ["INT_ADD", "register:40f0:8", ["const:509844:8", "const:4:8"]]
- 00509844 ["CALL", null, ["callee:00c53d00:8"]]
+ 00509884 ["INT_ADD", "register:40f0:8", ["const:509884:8", "const:4:8"]]
+ 00509884 ["CALL", null, ["callee:00c53d00:8"]]
- 00509844 bytes 27281d94
+ 00509884 bytes 1f291d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ebc3eb58a1bcac10330eca52a11bfc6"></a>

### [`00509944`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509944.md) → [`00509984`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/00509984.md) _ZNK5Botan4OCSP7Request10BER_encodeEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c597b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c597b0.md) · 呼出先 10件 [`004a6d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6d70.md) [`00535b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b40.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md)
- 新版 呼出元 1件 [`00c59bb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59bb0.md) · 呼出先 10件 [`004a6db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6db0.md) [`00535b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md)

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
    "old": {
      "definition_site": "005099f0",
      "incomplete_value": true,
      "site": "005099f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
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
    "old": {
      "definition_site": "00509ac4",
      "incomplete_value": true,
      "site": "00509ac4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00509a20",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "00509af4",
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
      "00509a20",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "00509af4",
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

- 旧版 [`005099f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509944.md#insn-005099f0) · [`00509ac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509944.md#insn-00509ac4) · [`00509988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509944.md#insn-00509988)
- 新版 `00509a30`（命令位置の公開資料なし） · `00509b04`（命令位置の公開資料なし） · `005099c8`（命令位置の公開資料なし）

~~~diff
- 005099f0 ["COPY", "register:0:8", ["register:4048:8"]]
- 005099f0 ["INT_ADD", "register:40f0:8", ["const:5099f0:8", "const:4:8"]]
- 005099f0 ["CALLIND", null, ["register:0:8"]]
+ 00509a30 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00509a30 ["INT_ADD", "register:40f0:8", ["const:509a30:8", "const:4:8"]]
+ 00509a30 ["CALLIND", null, ["register:0:8"]]
- 005099f0 bytes 20013fd6
+ 00509a30 bytes 20013fd6
- 00509ac4 ["COPY", "register:0:8", ["register:4048:8"]]
- 00509ac4 ["INT_ADD", "register:40f0:8", ["const:509ac4:8", "const:4:8"]]
- 00509ac4 ["CALLIND", null, ["register:0:8"]]
+ 00509b04 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00509b04 ["INT_ADD", "register:40f0:8", ["const:509b04:8", "const:4:8"]]
+ 00509b04 ["CALLIND", null, ["register:0:8"]]
- 00509ac4 bytes 20013fd6
+ 00509b04 bytes 20013fd6
- 00509988 ["INT_ADD", "register:40f0:8", ["const:509988:8", "const:4:8"]]
- 00509988 ["CALL", null, ["callee:00c586b0:8"]]
+ 005099c8 ["INT_ADD", "register:40f0:8", ["const:5099c8:8", "const:4:8"]]
+ 005099c8 ["CALL", null, ["callee:00c586b0:8"]]
- 00509988 bytes 4a3a1d94
+ 005099c8 bytes 3a3b1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e661aa0de911729287cbdf8d17d0d1d"></a>

### [`00509bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509bd4.md) → [`00509c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/00509c14.md) _ZN5Botan4OCSP8ResponseC2EPKhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 41件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`004a573c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a573c.md) [`004a5940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5940.md) [`004aea34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aea34.md) [`0050a93c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050a/0050a93c.md)
- 新版 呼出元 0件  · 呼出先 41件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`004a577c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a577c.md) [`004a5980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5980.md) [`004aea74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aea74.md) [`0050a97c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050a/0050a97c.md)

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
    "old": {
      "definition_site": "00509c5c",
      "incomplete_value": true,
      "site": "00509c5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00509c84",
      "incomplete_value": true,
      "site": "00509c84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00509cb0",
      "incomplete_value": true,
      "site": "00509cb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00509c90",
      "READ",
      [
        "storage",
        "00c9a9b0",
        null,
        "pointer"
      ]
    ],
    [
      "00509c9c",
      "DATA",
      [
        "storage",
        "00c65f78",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00509cac",
      "READ",
      [
        "storage",
        "00c9acd0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00509c90",
      "READ",
      [
        "storage",
        "00c9adb0",
        null,
        "pointer"
      ]
    ],
    [
      "00509c9c",
      "DATA",
      [
        "storage",
        "00c66378",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00509cac",
      "READ",
      [
        "storage",
        "00c9b0d0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00509d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509bd4.md#insn-00509d10) · [`00509d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509bd4.md#insn-00509d50) · [`00509dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509bd4.md#insn-00509dcc)
- 新版 `00509d50`（命令位置の公開資料なし） · `00509d90`（命令位置の公開資料なし） · `00509e0c`（命令位置の公開資料なし）

~~~diff
- 00509d10 ["INT_ADD", "register:40f0:8", ["const:509d10:8", "const:4:8"]]
- 00509d10 ["CALL", null, ["callee:00c58700:8"]]
+ 00509d50 ["INT_ADD", "register:40f0:8", ["const:509d50:8", "const:4:8"]]
+ 00509d50 ["CALL", null, ["callee:00c58700:8"]]
- 00509d10 bytes 7c391d94
+ 00509d50 bytes 6c3a1d94
- 00509d50 ["COPY", "register:0:8", ["register:4048:8"]]
- 00509d50 ["INT_ADD", "register:40f0:8", ["const:509d50:8", "const:4:8"]]
- 00509d50 ["CALLIND", null, ["register:0:8"]]
+ 00509d90 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00509d90 ["INT_ADD", "register:40f0:8", ["const:509d90:8", "const:4:8"]]
+ 00509d90 ["CALLIND", null, ["register:0:8"]]
- 00509d50 bytes 20013fd6
+ 00509d90 bytes 20013fd6
- 00509dcc ["INT_ADD", "register:40f0:8", ["const:509dcc:8", "const:4:8"]]
- 00509dcc ["CALL", null, ["callee:00c58700:8"]]
+ 00509e0c ["INT_ADD", "register:40f0:8", ["const:509e0c:8", "const:4:8"]]
+ 00509e0c ["CALL", null, ["callee:00c58700:8"]]
- 00509dcc bytes 4d391d94
+ 00509e0c bytes 3d3a1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48e1597c2a8f05481ea226604cafab5b"></a>

### [`0050a93c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050a/0050a93c.md) → [`0050a97c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050a/0050a97c.md) FUN_0050a97c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00509bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00509/00509bd4.md) · 呼出先 7件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`00509c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00509/00509c14.md) · 呼出先 7件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
    "old": {
      "definition_site": "0050aa44",
      "incomplete_value": true,
      "site": "0050aa4c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
      "definition_site": "0050aa80",
      "incomplete_value": false,
      "site": "0050aa8c",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "0050aa40",
      "incomplete_value": false,
      "site": "0050aa4c",
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
      "0050aa80",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "0050aa84",
      "READ",
      [
        "storage",
        "00c9a950",
        null,
        "pointer"
      ]
    ],
    [
      "0050aa84",
      "PARAM",
      [
        "storage",
        "00c65ec0",
        "_ZTIN5Botan14Decoding_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0050aa80",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "0050aa84",
      "READ",
      [
        "storage",
        "00c9ad50",
        null,
        "pointer"
      ]
    ],
    [
      "0050aa84",
      "PARAM",
      [
        "storage",
        "00c662c0",
        "_ZTIN5Botan14Decoding_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050aa4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050a/0050a93c.md#insn-0050aa4c) · [`0050a974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050a/0050a93c.md#insn-0050a974) · [`0050a984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050a/0050a93c.md#insn-0050a984)
- 新版 `0050aa8c`（命令位置の公開資料なし） · `0050a9b4`（命令位置の公開資料なし） · `0050a9c4`（命令位置の公開資料なし）

~~~diff
- 0050aa4c ["INT_ADD", "register:40f0:8", ["const:50aa4c:8", "const:4:8"]]
- 0050aa4c ["CALL", null, ["callee:00c57f10:8"]]
+ 0050aa8c ["INT_ADD", "register:40f0:8", ["const:50aa8c:8", "const:4:8"]]
+ 0050aa8c ["CALL", null, ["callee:00c57f10:8"]]
- 0050aa4c bytes 31341d94
+ 0050aa8c bytes 21351d94
- 0050a974 ["INT_ADD", "register:40f0:8", ["const:50a974:8", "const:4:8"]]
- 0050a974 ["CALL", null, ["callee:00c58690:8"]]
+ 0050a9b4 ["INT_ADD", "register:40f0:8", ["const:50a9b4:8", "const:4:8"]]
+ 0050a9b4 ["CALL", null, ["callee:00c58690:8"]]
- 0050a974 bytes 47361d94
+ 0050a9b4 bytes 37371d94
- 0050a984 ["INT_ADD", "register:40f0:8", ["const:50a984:8", "const:4:8"]]
- 0050a984 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0050a9c4 ["INT_ADD", "register:40f0:8", ["const:50a9c4:8", "const:4:8"]]
+ 0050a9c4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0050a984 bytes 4b341d94
+ 0050a9c4 bytes 3b351d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9788567f403a643987be2f8cbeb0434"></a>

### [`0050ae38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050a/0050ae38.md) → [`0050ae78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050a/0050ae78.md) _ZN5Botan11BER_Decoder11decode_listINS_4OCSP14SingleResponseEEERS0_RNSt6__ndk16vectorIT_NS5_9allocatorIS7_EEEENS_8ASN1_TagESC_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c597e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c597e0.md) · 呼出先 10件 [`0050ce74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050c/0050ce74.md) [`00549848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549848.md) [`00549a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549a4c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00c59be0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59be0.md) · 呼出先 10件 [`0050ceb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050c/0050ceb4.md) [`00549888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549888.md) [`00549a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549a8c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

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
    "old": {
      "definition_site": "0050af7c",
      "incomplete_value": true,
      "site": "0050af7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "0050af9c",
      "incomplete_value": true,
      "site": "0050af9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "0050af98",
      "incomplete_value": true,
      "site": "0050afa8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "0050aecc",
      "READ",
      [
        "storage",
        "00c9ad60",
        null,
        "pointer"
      ]
    ],
    [
      "0050aed0",
      "READ",
      [
        "storage",
        "00c9ad68",
        null,
        "pointer"
      ]
    ],
    [
      "0050aed4",
      "READ",
      [
        "storage",
        "00c9a938",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050aecc",
      "READ",
      [
        "storage",
        "00c9b160",
        null,
        "pointer"
      ]
    ],
    [
      "0050aed0",
      "READ",
      [
        "storage",
        "00c9b168",
        null,
        "pointer"
      ]
    ],
    [
      "0050aed4",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050af5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050a/0050ae38.md#insn-0050af5c) · [`0050b000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050a/0050ae38.md#insn-0050b000) · [`0050b054`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050a/0050ae38.md#insn-0050b054)
- 新版 `0050af9c`（命令位置の公開資料なし） · `0050b040`（命令位置の公開資料なし） · `0050b094`（命令位置の公開資料なし）

~~~diff
- 0050af5c ["COPY", "register:0:8", ["register:4040:8"]]
- 0050af5c ["INT_ADD", "register:40f0:8", ["const:50af5c:8", "const:4:8"]]
- 0050af5c ["CALLIND", null, ["register:0:8"]]
+ 0050af9c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0050af9c ["INT_ADD", "register:40f0:8", ["const:50af9c:8", "const:4:8"]]
+ 0050af9c ["CALLIND", null, ["register:0:8"]]
- 0050af5c bytes 00013fd6
+ 0050af9c bytes 00013fd6
- 0050b000 ["COPY", "register:0:8", ["register:4048:8"]]
- 0050b000 ["INT_ADD", "register:40f0:8", ["const:50b000:8", "const:4:8"]]
- 0050b000 ["CALLIND", null, ["register:0:8"]]
+ 0050b040 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050b040 ["INT_ADD", "register:40f0:8", ["const:50b040:8", "const:4:8"]]
+ 0050b040 ["CALLIND", null, ["register:0:8"]]
- 0050b000 bytes 20013fd6
+ 0050b040 bytes 20013fd6
- 0050b054 ["INT_ADD", "register:40f0:8", ["const:50b054:8", "const:4:8"]]
- 0050b054 ["CALL", null, ["callee:00c58710:8"]]
+ 0050b094 ["INT_ADD", "register:40f0:8", ["const:50b094:8", "const:4:8"]]
+ 0050b094 ["CALL", null, ["callee:00c58710:8"]]
- 0050b054 bytes af341d94
+ 0050b094 bytes 9f351d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b4e3861287455edb873784e9fe24194"></a>

### [`0050b484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050b484.md) → [`0050b4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050b/0050b4c4.md) _ZNK5Botan4OCSP8Response16verify_signatureERKNS_16X509_CertificateE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59800.md) · 呼出先 14件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`004a6bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6bdc.md) [`00547ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547ad4.md) [`00547b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547b2c.md) [`00547b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547b30.md)
- 新版 呼出元 1件 [`00c59c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59c00.md) · 呼出先 14件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`004a6c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6c1c.md) [`00547b14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547b14.md) [`00547b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547b6c.md) [`00547b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547b70.md)

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
    "old": {
      "definition_site": "0050b4d4",
      "incomplete_value": false,
      "site": "0050b4d4",
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
      "0050b514",
      "DATA",
      [
        "storage",
        "00c6a2b0",
        null,
        "undefined *"
      ]
    ],
    [
      "0050b558",
      "READ",
      [
        "storage",
        "00c6a2d0",
        null,
        "pointer"
      ]
    ],
    [
      "0050b558",
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
      "0050b514",
      "DATA",
      [
        "storage",
        "00c6a6b0",
        null,
        "undefined *"
      ]
    ],
    [
      "0050b558",
      "READ",
      [
        "storage",
        "00c6a6d0",
        null,
        "pointer"
      ]
    ],
    [
      "0050b558",
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

- 旧版 [`0050b4b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050b484.md#insn-0050b4b4) · [`0050b4c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050b484.md#insn-0050b4c4) · [`0050b4cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050b484.md#insn-0050b4cc)
- 新版 `0050b4f4`（命令位置の公開資料なし） · `0050b504`（命令位置の公開資料なし） · `0050b50c`（命令位置の公開資料なし）

~~~diff
- 0050b4b4 ["INT_ADD", "register:40f0:8", ["const:50b4b4:8", "const:4:8"]]
- 0050b4b4 ["CALL", null, ["callee:00c59c10:8"]]
+ 0050b4f4 ["INT_ADD", "register:40f0:8", ["const:50b4f4:8", "const:4:8"]]
+ 0050b4f4 ["CALL", null, ["callee:00c59c10:8"]]
- 0050b4b4 bytes d7381d94
+ 0050b4f4 bytes c7391d94
- 0050b4c4 ["INT_ADD", "register:40f0:8", ["const:50b4c4:8", "const:4:8"]]
- 0050b4c4 ["CALL", null, ["callee:00c588b0:8"]]
+ 0050b504 ["INT_ADD", "register:40f0:8", ["const:50b504:8", "const:4:8"]]
+ 0050b504 ["CALL", null, ["callee:00c588b0:8"]]
- 0050b4c4 bytes fb331d94
+ 0050b504 bytes eb341d94
- 0050b4cc ["COPY", "tmp:0:8", ["const:2b0:8"]]
- 0050b4cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0050b4cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0050b4cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0050b50c ["COPY", "tmp:0:8", ["const:6b0:8"]]
+ 0050b50c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0050b50c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0050b50c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0050b4cc bytes 08c10a91
+ 0050b50c bytes 08c11a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2de04fcaf72958eb45b31b1d0f13d724"></a>

### [`0050b8ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050b8ac.md) → [`0050b8ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050b/0050b8ec.md) _ZNK5Botan4OCSP8Response15check_signatureERKNSt6__ndk16vectorIPNS_17Certificate_StoreENS2_9allocatorIS5_EEEERKNS3_INS2_10shared_ptrIKNS_16X5

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59820.md) · 呼出先 13件 [`0053afc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053afc0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00c59c20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59c20.md) · 呼出先 13件 [`0053b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053b000.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
    "old": {
      "definition_site": "0050bbb0",
      "incomplete_value": true,
      "site": "0050bbbc",
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
                "const:c7a:8"
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
    "old": {
      "definition_site": "0050bd44",
      "incomplete_value": true,
      "site": "0050bd48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "0050bd78",
      "incomplete_value": true,
      "site": "0050bd7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "0050bbf0",
      "READ",
      [
        "storage",
        "002b4c7a",
        null,
        "string"
      ]
    ],
    [
      "0050bd7c",
      "READ",
      [
        "storage",
        "00c9acd8",
        null,
        "pointer"
      ]
    ],
    [
      "0050bd88",
      "DATA",
      [
        "storage",
        "00c6a340",
        null,
        "undefined1[56]"
      ]
    ]
  ],
  "added": [
    [
      "0050bbf0",
      "READ",
      [
        "storage",
        "002b4cba",
        null,
        "string"
      ]
    ],
    [
      "0050bd7c",
      "READ",
      [
        "storage",
        "00c9b0d8",
        null,
        "pointer"
      ]
    ],
    [
      "0050bd88",
      "DATA",
      [
        "storage",
        "00c6a740",
        null,
        "undefined1[56]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050bd3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050b8ac.md#insn-0050bd3c) · [`0050bd88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050b8ac.md#insn-0050bd88) · [`0050bdbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050b8ac.md#insn-0050bdbc)
- 新版 `0050bd7c`（命令位置の公開資料なし） · `0050bdc8`（命令位置の公開資料なし） · `0050bdfc`（命令位置の公開資料なし）

~~~diff
- 0050bd3c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cd8:8"]]
- 0050bd3c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050bd7c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d8:8"]]
+ 0050bd7c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050bd3c bytes 086d46f9
+ 0050bd7c bytes 086d40f9
- 0050bd88 ["INT_ADD", "register:40f0:8", ["const:50bd88:8", "const:4:8"]]
- 0050bd88 ["CALL", null, ["callee:0053b000:8"]]
+ 0050bdc8 ["INT_ADD", "register:40f0:8", ["const:50bdc8:8", "const:4:8"]]
+ 0050bdc8 ["CALL", null, ["callee:0053b000:8"]]
- 0050bd88 bytes 8ebc0094
+ 0050bdc8 bytes 8ebc0094
- 0050bdbc ["INT_ADD", "register:40f0:8", ["const:50bdbc:8", "const:4:8"]]
- 0050bdbc ["CALL", null, ["callee:00c53cd0:8"]]
+ 0050bdfc ["INT_ADD", "register:40f0:8", ["const:50bdfc:8", "const:4:8"]]
+ 0050bdfc ["CALL", null, ["callee:00c53cd0:8"]]
- 0050bdbc bytes bd1e1d94
+ 0050bdfc bytes b51f1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0aae0568de130c6232eb0aaea747b61f"></a>

### [`0050be84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050be84.md) → [`0050bec4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050b/0050bec4.md) _ZNK5Botan16X509_Certificate33subject_public_key_bitstring_sha1Ev

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59830.md) · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`00c59c30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59c30.md) · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
    "old": {
      "definition_site": "0050befc",
      "incomplete_value": false,
      "site": "0050bf04",
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
            "const:16f:8"
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
    "old": {
      "definition_site": "0050bf38",
      "incomplete_value": true,
      "site": "0050bf44",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0050bf74",
      "incomplete_value": false,
      "site": "0050bf84",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "0050bf34",
      "incomplete_value": false,
      "site": "0050bf44",
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
      "0050bf3c",
      "PARAM",
      [
        "storage",
        "002c116f",
        null,
        "string"
      ]
    ],
    [
      "0050bf74",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "0050bf78",
      "READ",
      [
        "storage",
        "00c9a998",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050bf3c",
      "PARAM",
      [
        "storage",
        "002c11af",
        null,
        "string"
      ]
    ],
    [
      "0050bf74",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "0050bf78",
      "READ",
      [
        "storage",
        "00c9ad98",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050bf04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050be84.md#insn-0050bf04) · [`0050bf44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050be84.md#insn-0050bf44) · [`0050bea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050be84.md#insn-0050bea8)
- 新版 `0050bf44`（命令位置の公開資料なし） · `0050bf84`（命令位置の公開資料なし） · `0050bee8`（命令位置の公開資料なし）

~~~diff
- 0050bf04 ["INT_ADD", "register:40f0:8", ["const:50bf04:8", "const:4:8"]]
- 0050bf04 ["CALL", null, ["callee:0043ddd8:8"]]
+ 0050bf44 ["INT_ADD", "register:40f0:8", ["const:50bf44:8", "const:4:8"]]
+ 0050bf44 ["CALL", null, ["callee:0043ddd8:8"]]
- 0050bf04 bytes a5c7fc97
+ 0050bf44 bytes a5c7fc97
- 0050bf44 ["INT_ADD", "register:40f0:8", ["const:50bf44:8", "const:4:8"]]
- 0050bf44 ["CALL", null, ["callee:00c57f10:8"]]
+ 0050bf84 ["INT_ADD", "register:40f0:8", ["const:50bf84:8", "const:4:8"]]
+ 0050bf84 ["CALL", null, ["callee:00c57f10:8"]]
- 0050bf44 bytes f32e1d94
+ 0050bf84 bytes e32f1d94
- 0050bea8 ["INT_ADD", "register:40f0:8", ["const:50bea8:8", "const:4:8"]]
- 0050bea8 ["CALL", null, ["callee:00c599f0:8"]]
+ 0050bee8 ["INT_ADD", "register:40f0:8", ["const:50bee8:8", "const:4:8"]]
+ 0050bee8 ["CALL", null, ["callee:00c599f0:8"]]
- 0050bea8 bytes d2351d94
+ 0050bee8 bytes c2361d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5f744b210a6b78bd2ec4952e9e09d71"></a>

### [`0050c0f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050c/0050c0f8.md) → [`0050c138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050c/0050c138.md) _ZNK5Botan4OCSP8Response10status_forERKNS_16X509_CertificateES4_NSt6__ndk16chrono10time_pointINS6_12system_clockENS6_8durationIxNS5_5ratioIL

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59850.md) · 呼出先 4件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c585e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c585e0.md) [`00c59670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59670.md) [`00c59860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59860.md)
- 新版 呼出元 1件 [`00c59c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59c50.md) · 呼出先 4件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c589e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c589e0.md) [`00c59a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59a70.md) [`00c59c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59c60.md)

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
    "old": {
      "definition_site": "0050c1b8",
      "incomplete_value": true,
      "site": "0050c1c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "0050c1ec",
      "READ",
      [
        "storage",
        "00c9a9b0",
        null,
        "pointer"
      ]
    ],
    [
      "0050c200",
      "DATA",
      [
        "storage",
        "00c65f78",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0050c23c",
      "DATA",
      [
        "storage",
        "00c65f78",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "0050c1ec",
      "READ",
      [
        "storage",
        "00c9adb0",
        null,
        "pointer"
      ]
    ],
    [
      "0050c200",
      "DATA",
      [
        "storage",
        "00c66378",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0050c23c",
      "DATA",
      [
        "storage",
        "00c66378",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050c140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050c/0050c0f8.md#insn-0050c140) · [`0050c188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050c/0050c0f8.md#insn-0050c188) · [`0050c1ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050c/0050c0f8.md#insn-0050c1ac)
- 新版 `0050c180`（命令位置の公開資料なし） · `0050c1c8`（命令位置の公開資料なし） · `0050c1ec`（命令位置の公開資料なし）

~~~diff
- 0050c140 ["INT_ADD", "register:40f0:8", ["const:50c140:8", "const:4:8"]]
- 0050c140 ["CALL", null, ["callee:00c59c60:8"]]
+ 0050c180 ["INT_ADD", "register:40f0:8", ["const:50c180:8", "const:4:8"]]
+ 0050c180 ["CALL", null, ["callee:00c59c60:8"]]
- 0050c140 bytes c8351d94
+ 0050c180 bytes b8361d94
- 0050c188 ["INT_ADD", "register:40f0:8", ["const:50c188:8", "const:4:8"]]
- 0050c188 ["CALL", null, ["callee:00c59a70:8"]]
+ 0050c1c8 ["INT_ADD", "register:40f0:8", ["const:50c1c8:8", "const:4:8"]]
+ 0050c1c8 ["CALL", null, ["callee:00c59a70:8"]]
- 0050c188 bytes 3a351d94
+ 0050c1c8 bytes 2a361d94
- 0050c1ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9b0:8"]]
- 0050c1ac ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050c1ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:db0:8"]]
+ 0050c1ec ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
- 0050c1ac bytes 73da44f9
+ 0050c1ec bytes 73da46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9059736079de8b43229ab7d33d0911d"></a>

### [`0050c678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050c/0050c678.md) → [`0050c6b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050c/0050c6b8.md) _ZN5Botan4OCSP6CertIDC2ERKNS_16X509_CertificateERKNS_6BigIntE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c597a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c597a0.md) · 呼出先 14件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`0054369c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/0054369c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00c59ba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59ba0.md) · 呼出先 14件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md) [`005436dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/005436dc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
    "old": {
      "definition_site": "0050c6c4",
      "incomplete_value": true,
      "site": "0050c6d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "0050c6d4",
      "incomplete_value": true,
      "site": "0050c6d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "0050c908",
      "incomplete_value": true,
      "site": "0050c908",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0050c6f4",
      "READ",
      [
        "storage",
        "00c9ad68",
        null,
        "pointer"
      ]
    ],
    [
      "0050c6f8",
      "READ",
      [
        "storage",
        "00c9a938",
        null,
        "pointer"
      ]
    ],
    [
      "0050c710",
      "DATA",
      [
        "storage",
        "00c67418",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "0050c6f4",
      "READ",
      [
        "storage",
        "00c9b168",
        null,
        "pointer"
      ]
    ],
    [
      "0050c6f8",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "0050c710",
      "DATA",
      [
        "storage",
        "00c67818",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050c8c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050c/0050c678.md#insn-0050c8c8) · [`0050c908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050c/0050c678.md#insn-0050c908) · [`0050c9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050c/0050c678.md#insn-0050c9f0)
- 新版 `0050c908`（命令位置の公開資料なし） · `0050c948`（命令位置の公開資料なし） · `0050ca30`（命令位置の公開資料なし）

~~~diff
- 0050c8c8 ["INT_ADD", "register:40f0:8", ["const:50c8c8:8", "const:4:8"]]
- 0050c8c8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0050c908 ["INT_ADD", "register:40f0:8", ["const:50c908:8", "const:4:8"]]
+ 0050c908 ["CALL", null, ["callee:00c57eb0:8"]]
- 0050c8c8 bytes 7a2c1d94
+ 0050c908 bytes 6a2d1d94
- 0050c908 ["COPY", "register:0:8", ["register:4048:8"]]
- 0050c908 ["INT_ADD", "register:40f0:8", ["const:50c908:8", "const:4:8"]]
- 0050c908 ["CALLIND", null, ["register:0:8"]]
+ 0050c948 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050c948 ["INT_ADD", "register:40f0:8", ["const:50c948:8", "const:4:8"]]
+ 0050c948 ["CALLIND", null, ["register:0:8"]]
- 0050c908 bytes 20013fd6
+ 0050c948 bytes 20013fd6
- 0050c9f0 ["COPY", "register:0:8", ["register:4048:8"]]
- 0050c9f0 ["INT_ADD", "register:40f0:8", ["const:50c9f0:8", "const:4:8"]]
- 0050c9f0 ["CALLIND", null, ["register:0:8"]]
+ 0050ca30 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050ca30 ["INT_ADD", "register:40f0:8", ["const:50ca30:8", "const:4:8"]]
+ 0050ca30 ["CALLIND", null, ["register:0:8"]]
- 0050c9f0 bytes 20013fd6
+ 0050ca30 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f995af62be8a024ee6539e3d23d18fa"></a>

### [`0050cd8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050c/0050cd8c.md) → [`0050cdcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050c/0050cdcc.md) _ZNK5Botan4OCSP14SingleResponse11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
    "old": {
      "definition_site": "0050cdcc",
      "incomplete_value": true,
      "site": "0050cde0",
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
                "const:137:8"
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
    "old": {
      "definition_site": "0050cdd0",
      "incomplete_value": true,
      "site": "0050cde4",
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
    "old": {
      "definition_site": "0050cdd4",
      "incomplete_value": true,
      "site": "0050cde8",
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
                "const:640:8"
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
      "0050ce0c",
      "READ",
      [
        "storage",
        "002c1137",
        null,
        "string"
      ]
    ],
    [
      "0050ce10",
      "READ",
      [
        "storage",
        "002c1142",
        null,
        "string"
      ]
    ],
    [
      "0050ce14",
      "READ",
      [
        "storage",
        "002c2640",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0050ce0c",
      "READ",
      [
        "storage",
        "002c1177",
        null,
        "string"
      ]
    ],
    [
      "0050ce10",
      "READ",
      [
        "storage",
        "002c1182",
        null,
        "string"
      ]
    ],
    [
      "0050ce14",
      "READ",
      [
        "storage",
        "002c2680",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050ce24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050c/0050cd8c.md#insn-0050ce24) · [`0050cdb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050c/0050cd8c.md#insn-0050cdb0) · [`0050cdbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050c/0050cd8c.md#insn-0050cdbc)
- 新版 `0050ce64`（命令位置の公開資料なし） · `0050cdf0`（命令位置の公開資料なし） · `0050cdfc`（命令位置の公開資料なし）

~~~diff
- 0050ce24 ["INT_ADD", "register:40f0:8", ["const:50ce24:8", "const:4:8"]]
- 0050ce24 ["CALL", null, ["callee:00c57f10:8"]]
+ 0050ce64 ["INT_ADD", "register:40f0:8", ["const:50ce64:8", "const:4:8"]]
+ 0050ce64 ["CALL", null, ["callee:00c57f10:8"]]
- 0050ce24 bytes 3b2b1d94
+ 0050ce64 bytes 2b2c1d94
- 0050cdb0 ["INT_ADD", "register:40f0:8", ["const:50cdb0:8", "const:4:8"]]
- 0050cdb0 ["CALL", null, ["callee:00c57ef0:8"]]
+ 0050cdf0 ["INT_ADD", "register:40f0:8", ["const:50cdf0:8", "const:4:8"]]
+ 0050cdf0 ["CALL", null, ["callee:00c57ef0:8"]]
- 0050cdb0 bytes 502b1d94
+ 0050cdf0 bytes 402c1d94
- 0050cdbc ["INT_ADD", "register:40f0:8", ["const:50cdbc:8", "const:4:8"]]
- 0050cdbc ["CALL", null, ["callee:00c57e90:8"]]
+ 0050cdfc ["INT_ADD", "register:40f0:8", ["const:50cdfc:8", "const:4:8"]]
+ 0050cdfc ["CALL", null, ["callee:00c57e90:8"]]
- 0050cdbc bytes 352b1d94
+ 0050cdfc bytes 252c1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f56b9edc13e66a55cd2f0639b33e8be2"></a>

### [`0050ce74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050c/0050ce74.md) → [`0050ceb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050c/0050ceb4.md) _ZN5Botan4OCSP14SingleResponse11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0050ae38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050a/0050ae38.md) · 呼出先 10件 [`0053b3e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053b3e4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58300.md)
- 新版 呼出元 1件 [`0050ae78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050a/0050ae78.md) · 呼出先 10件 [`0053b424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053b424.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c58700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58700.md)

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
    "old": {
      "definition_site": "0050cebc",
      "incomplete_value": true,
      "site": "0050cebc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "0050cf44",
      "incomplete_value": true,
      "site": "0050cf44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "0050d02c",
      "incomplete_value": true,
      "site": "0050d02c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0050cee8",
      "READ",
      [
        "storage",
        "00c9ad10",
        null,
        "pointer"
      ]
    ],
    [
      "0050cefc",
      "DATA",
      [
        "storage",
        "00c684c0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0050cf74",
      "READ",
      [
        "storage",
        "00c9a9b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050cee8",
      "READ",
      [
        "storage",
        "00c9b110",
        null,
        "pointer"
      ]
    ],
    [
      "0050cefc",
      "DATA",
      [
        "storage",
        "00c688c0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0050cf74",
      "READ",
      [
        "storage",
        "00c9adb0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050cefc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050c/0050ce74.md#insn-0050cefc) · [`0050cfec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050c/0050ce74.md#insn-0050cfec) · [`0050d02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050c/0050ce74.md#insn-0050d02c)
- 新版 `0050cf3c`（命令位置の公開資料なし） · `0050d02c`（命令位置の公開資料なし） · `0050d06c`（命令位置の公開資料なし）

~~~diff
- 0050cefc ["INT_ADD", "register:40f0:8", ["const:50cefc:8", "const:4:8"]]
- 0050cefc ["CALL", null, ["callee:00c58720:8"]]
+ 0050cf3c ["INT_ADD", "register:40f0:8", ["const:50cf3c:8", "const:4:8"]]
+ 0050cf3c ["CALL", null, ["callee:00c58720:8"]]
- 0050cefc bytes 092d1d94
+ 0050cf3c bytes f92d1d94
- 0050cfec ["INT_ADD", "register:40f0:8", ["const:50cfec:8", "const:4:8"]]
- 0050cfec ["CALL", null, ["callee:00c57eb0:8"]]
+ 0050d02c ["INT_ADD", "register:40f0:8", ["const:50d02c:8", "const:4:8"]]
+ 0050d02c ["CALL", null, ["callee:00c57eb0:8"]]
- 0050cfec bytes b12a1d94
+ 0050d02c bytes a12b1d94
- 0050d02c ["COPY", "register:0:8", ["register:4048:8"]]
- 0050d02c ["INT_ADD", "register:40f0:8", ["const:50d02c:8", "const:4:8"]]
- 0050d02c ["CALLIND", null, ["register:0:8"]]
+ 0050d06c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050d06c ["INT_ADD", "register:40f0:8", ["const:50d06c:8", "const:4:8"]]
+ 0050d06c ["CALLIND", null, ["register:0:8"]]
- 0050d02c bytes 20013fd6
+ 0050d06c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-528b28de259e61c1694ad38692ccb68a"></a>

### [`0050d304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050d304.md) → [`0050d344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050d/0050d344.md) _ZNK5Botan14PKCS10_Request9PEM_labelEv

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
    "old": {
      "definition_site": "0050d310",
      "incomplete_value": true,
      "site": "0050d324",
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
                "const:29e000:8"
              ],
              [
                "leaf",
                "const:fa9:8"
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
      "0050d350",
      "READ",
      [
        "storage",
        "0029efa9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0050d350",
      "READ",
      [
        "storage",
        "0029f076",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050d304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050d304.md#insn-0050d304) · [`0050d308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050d304.md#insn-0050d308)
- 新版 `0050d344`（命令位置の公開資料なし） · `0050d348`（命令位置の公開資料なし）

~~~diff
- 0050d304 ["COPY", "register:4050:8", ["const:29e000:8"]]
+ 0050d344 ["COPY", "register:4050:8", ["const:29f000:8"]]
- 0050d304 bytes 8aecffb0
+ 0050d344 bytes 8aecffd0
- 0050d308 ["COPY", "tmp:0:8", ["const:fa9:8"]]
- 0050d308 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0050d308 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0050d308 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0050d348 ["COPY", "tmp:0:8", ["const:76:8"]]
+ 0050d348 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0050d348 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0050d348 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0050d308 bytes 4aa53e91
+ 0050d348 bytes 4ad90191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99b2760828dc414f3fe019bdf26a9a86"></a>

### [`0050d330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050d330.md) → [`0050d370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050d/0050d370.md) _ZNK5Botan14PKCS10_Request20alternate_PEM_labelsEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00473500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473500.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00473540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473540.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

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
    "old": {
      "definition_site": "0050d364",
      "incomplete_value": true,
      "site": "0050d374",
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
                "const:994:8"
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
    "old": {
      "definition_site": "0050d378",
      "incomplete_value": true,
      "site": "0050d378",
      "value": [
        "LOAD",
        "8",
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
    "old": {
      "definition_site": "0050d36c",
      "incomplete_value": true,
      "site": "0050d37c",
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
                "const:410:8"
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
      "0050d3a4",
      "READ",
      [
        "storage",
        "002bd994",
        null,
        "string"
      ]
    ],
    [
      "0050d3a8",
      "READ",
      [
        "storage",
        "002bd9a3",
        null,
        "string"
      ]
    ],
    [
      "0050d3ac",
      "READ",
      [
        "storage",
        "002c2410",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0050d3a4",
      "READ",
      [
        "storage",
        "002bd9d4",
        null,
        "string"
      ]
    ],
    [
      "0050d3a8",
      "READ",
      [
        "storage",
        "002bd9e3",
        null,
        "string"
      ]
    ],
    [
      "0050d3ac",
      "READ",
      [
        "storage",
        "002c2450",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050d354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050d330.md#insn-0050d354) · [`0050d35c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050d330.md#insn-0050d35c) · [`0050d360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050d330.md#insn-0050d360)
- 新版 `0050d394`（命令位置の公開資料なし） · `0050d39c`（命令位置の公開資料なし）

~~~diff
- 0050d354 ["INT_ADD", "register:40f0:8", ["const:50d354:8", "const:4:8"]]
- 0050d354 ["CALL", null, ["callee:00c57e90:8"]]
+ 0050d394 ["INT_ADD", "register:40f0:8", ["const:50d394:8", "const:4:8"]]
+ 0050d394 ["CALL", null, ["callee:00c57e90:8"]]
- 0050d354 bytes cf291d94
+ 0050d394 bytes bf2a1d94
- 0050d35c ["COPY", "tmp:0:8", ["const:994:8"]]
- 0050d35c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0050d35c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0050d35c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0050d39c ["COPY", "tmp:0:8", ["const:9d4:8"]]
+ 0050d39c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0050d39c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0050d39c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0050d35c bytes 08512691
+ 0050d39c bytes 08512791
- 0050d360 ["COPY", "register:4048:8", ["const:2c2000:8"]]
- 0050d360 bytes a9edffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d37790830cc48cfd4ed8cbaaee8ad7c"></a>

### [`0050d3f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050d3f4.md) → [`0050d434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050d/0050d434.md) _ZN5Botan14PKCS10_RequestC2ERNS_10DataSourceE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md) [`00c59880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59880.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md) [`00c59c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59c80.md)

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
    "old": {
      "definition_site": "0050d434",
      "incomplete_value": true,
      "site": "0050d434",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "0050d434",
      "incomplete_value": true,
      "site": "0050d434",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "0050d474",
      "incomplete_value": true,
      "site": "0050d47c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "0050d454",
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      "0050d45c",
      "READ",
      [
        "storage",
        "00c9a938",
        null,
        "pointer"
      ]
    ],
    [
      "0050d474",
      "DATA",
      [
        "storage",
        "00c69620",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "0050d454",
      "READ",
      [
        "storage",
        "00c9b158",
        null,
        "pointer"
      ]
    ],
    [
      "0050d45c",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "0050d474",
      "DATA",
      [
        "storage",
        "00c69a20",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050d40c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050d3f4.md#insn-0050d40c) · [`0050d414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050d3f4.md#insn-0050d414) · [`0050d41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050d3f4.md#insn-0050d41c)
- 新版 `0050d44c`（命令位置の公開資料なし） · `0050d454`（命令位置の公開資料なし） · `0050d45c`（命令位置の公開資料なし）

~~~diff
- 0050d40c ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 0050d44c ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 0050d40c bytes 683c00b0
+ 0050d44c bytes 683c00d0
- 0050d414 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d58:8"]]
- 0050d414 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050d454 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:158:8"]]
+ 0050d454 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050d414 bytes 08ad46f9
+ 0050d454 bytes 08ad40f9
- 0050d41c ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:938:8"]]
- 0050d41c ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050d45c ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:d38:8"]]
+ 0050d45c ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 0050d41c bytes 4a9d44f9
+ 0050d45c bytes 4a9d46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d250cc32a2e312f96586770dae79d235"></a>

### [`0050d4f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050d4f8.md) → [`0050d538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050d/0050d538.md) _ZN5Botan11X509_Object9load_dataERNS_10DataSourceE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59880.md) · 呼出先 18件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044fc7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044fc7c.md) [`004a6f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6f5c.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00540264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540264.md)
- 新版 呼出元 1件 [`00c59c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59c80.md) · 呼出先 18件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044fcbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044fcbc.md) [`004a6f9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6f9c.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`005402a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005402a4.md)

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
    "old": {
      "definition_site": "0050d590",
      "incomplete_value": true,
      "site": "0050d590",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "0050d5cc",
      "incomplete_value": true,
      "site": "0050d5cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
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
    "old": {
      "definition_site": "0050d6a4",
      "incomplete_value": true,
      "site": "0050d6a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0050d5c0",
      "READ",
      [
        "storage",
        "00c9a9e0",
        null,
        "pointer"
      ]
    ],
    [
      "0050d5d0",
      "DATA",
      [
        "storage",
        "00c66f88",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "0050d5fc",
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
      "0050d5c0",
      "READ",
      [
        "storage",
        "00c9ade0",
        null,
        "pointer"
      ]
    ],
    [
      "0050d5d0",
      "DATA",
      [
        "storage",
        "00c67388",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "0050d5fc",
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

- 旧版 [`0050d5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050d4f8.md#insn-0050d5cc) · [`0050d664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050d4f8.md#insn-0050d664) · [`0050d6a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050d4f8.md#insn-0050d6a4)
- 新版 `0050d60c`（命令位置の公開資料なし） · `0050d6a4`（命令位置の公開資料なし） · `0050d6e4`（命令位置の公開資料なし）

~~~diff
- 0050d5cc ["COPY", "register:0:8", ["register:4048:8"]]
- 0050d5cc ["INT_ADD", "register:40f0:8", ["const:50d5cc:8", "const:4:8"]]
- 0050d5cc ["CALLIND", null, ["register:0:8"]]
+ 0050d60c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050d60c ["INT_ADD", "register:40f0:8", ["const:50d60c:8", "const:4:8"]]
+ 0050d60c ["CALLIND", null, ["register:0:8"]]
- 0050d5cc bytes 20013fd6
+ 0050d60c bytes 20013fd6
- 0050d664 ["COPY", "register:0:8", ["register:4040:8"]]
- 0050d664 ["INT_ADD", "register:40f0:8", ["const:50d664:8", "const:4:8"]]
- 0050d664 ["CALLIND", null, ["register:0:8"]]
+ 0050d6a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0050d6a4 ["INT_ADD", "register:40f0:8", ["const:50d6a4:8", "const:4:8"]]
+ 0050d6a4 ["CALLIND", null, ["register:0:8"]]
- 0050d664 bytes 00013fd6
+ 0050d6a4 bytes 00013fd6
- 0050d6a4 ["COPY", "register:0:8", ["register:4048:8"]]
- 0050d6a4 ["INT_ADD", "register:40f0:8", ["const:50d6a4:8", "const:4:8"]]
- 0050d6a4 ["CALLIND", null, ["register:0:8"]]
+ 0050d6e4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050d6e4 ["INT_ADD", "register:40f0:8", ["const:50d6e4:8", "const:4:8"]]
+ 0050d6e4 ["CALLIND", null, ["register:0:8"]]
- 0050d6a4 bytes 20013fd6
+ 0050d6e4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee3025dd0f7460781a30ccac4ea2ce46"></a>

### [`0050dd60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050dd60.md) → [`0050dda0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050d/0050dda0.md) _ZN5Botan14PKCS10_RequestC1ERKNSt6__ndk16vectorIhNS1_9allocatorIhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59b70.md) · 呼出先 7件 [`00540388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540388.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)
- 新版 呼出元 1件 [`00c59f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59f70.md) · 呼出先 7件 [`005403c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005403c8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md)

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
    "old": {
      "definition_site": "0050dda0",
      "incomplete_value": true,
      "site": "0050dda0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "0050dda0",
      "incomplete_value": true,
      "site": "0050dda0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "0050dde8",
      "incomplete_value": true,
      "site": "0050ddf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "0050ddc0",
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      "0050ddc8",
      "READ",
      [
        "storage",
        "00c9a938",
        null,
        "pointer"
      ]
    ],
    [
      "0050dde0",
      "DATA",
      [
        "storage",
        "00c69620",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "0050ddc0",
      "READ",
      [
        "storage",
        "00c9b158",
        null,
        "pointer"
      ]
    ],
    [
      "0050ddc8",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "0050dde0",
      "DATA",
      [
        "storage",
        "00c69a20",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050de4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050dd60.md#insn-0050de4c) · [`0050dd78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050dd60.md#insn-0050dd78) · [`0050dd80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050dd60.md#insn-0050dd80)
- 新版 `0050de8c`（命令位置の公開資料なし） · `0050ddb8`（命令位置の公開資料なし） · `0050ddc0`（命令位置の公開資料なし）

~~~diff
- 0050de4c ["COPY", "register:0:8", ["register:4048:8"]]
- 0050de4c ["INT_ADD", "register:40f0:8", ["const:50de4c:8", "const:4:8"]]
- 0050de4c ["CALLIND", null, ["register:0:8"]]
+ 0050de8c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050de8c ["INT_ADD", "register:40f0:8", ["const:50de8c:8", "const:4:8"]]
+ 0050de8c ["CALLIND", null, ["register:0:8"]]
- 0050de4c bytes 20013fd6
+ 0050de8c bytes 20013fd6
- 0050dd78 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 0050ddb8 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 0050dd78 bytes 683c00b0
+ 0050ddb8 bytes 683c00d0
- 0050dd80 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d58:8"]]
- 0050dd80 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050ddc0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:158:8"]]
+ 0050ddc0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050dd80 bytes 08ad46f9
+ 0050ddc0 bytes 08ad40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf803d91f30cfb9baffb6ba292245350"></a>

### [`0050ded8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050ded8.md) → [`0050df18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050d/0050df18.md) _ZN5Botan14PKCS10_RequestC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md) [`00c59260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59260.md) [`00c59270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59270.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md) [`00c59660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59660.md) [`00c59670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59670.md)

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
    "old": {
      "definition_site": "0050df18",
      "incomplete_value": true,
      "site": "0050df18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "0050df18",
      "incomplete_value": true,
      "site": "0050df18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "0050df58",
      "incomplete_value": true,
      "site": "0050df60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "0050df38",
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      "0050df40",
      "READ",
      [
        "storage",
        "00c9a938",
        null,
        "pointer"
      ]
    ],
    [
      "0050df58",
      "DATA",
      [
        "storage",
        "00c69620",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "0050df38",
      "READ",
      [
        "storage",
        "00c9b158",
        null,
        "pointer"
      ]
    ],
    [
      "0050df40",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "0050df58",
      "DATA",
      [
        "storage",
        "00c69a20",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050def0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050ded8.md#insn-0050def0) · [`0050def8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050ded8.md#insn-0050def8) · [`0050df00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050d/0050ded8.md#insn-0050df00)
- 新版 `0050df30`（命令位置の公開資料なし） · `0050df38`（命令位置の公開資料なし） · `0050df40`（命令位置の公開資料なし）

~~~diff
- 0050def0 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 0050df30 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 0050def0 bytes 683c00b0
+ 0050df30 bytes 683c00d0
- 0050def8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d58:8"]]
- 0050def8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050df38 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:158:8"]]
+ 0050df38 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050def8 bytes 08ad46f9
+ 0050df38 bytes 08ad40f9
- 0050df00 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:938:8"]]
- 0050df00 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050df40 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:d38:8"]]
+ 0050df40 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 0050df00 bytes 4a9d44f9
+ 0050df40 bytes 4a9d46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ae17416498430aaf0f6ee591d9421de"></a>

### [`0050e004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050e/0050e004.md) → [`0050e044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050e/0050e044.md) _ZN5Botan14PKCS10_Request12force_decodeEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 40件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`004a5f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5f60.md) [`004a6bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6bdc.md)
- 新版 呼出元 0件  · 呼出先 40件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`004a5fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5fa0.md) [`004a6c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6c1c.md)

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
    "old": {
      "definition_site": "0050e1dc",
      "incomplete_value": true,
      "site": "0050e1fc",
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
                "const:410:8"
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
    "old": {
      "definition_site": "0050e474",
      "incomplete_value": true,
      "site": "0050e484",
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
                "const:f7d:8"
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
    "old": {
      "definition_site": "0050e488",
      "incomplete_value": true,
      "site": "0050e488",
      "value": [
        "LOAD",
        "8",
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
      "0050e210",
      "READ",
      [
        "storage",
        "00c9a958",
        null,
        "pointer"
      ]
    ],
    [
      "0050e21c",
      "READ",
      [
        "storage",
        "002c2410",
        null,
        null
      ]
    ],
    [
      "0050e264",
      "DATA",
      [
        "storage",
        "00c65dd8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "0050e210",
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      "0050e21c",
      "READ",
      [
        "storage",
        "002c2450",
        null,
        null
      ]
    ],
    [
      "0050e264",
      "DATA",
      [
        "storage",
        "00c661d8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050e528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050e/0050e004.md#insn-0050e528) · [`0050e568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050e/0050e004.md#insn-0050e568) · [`0050e5a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050e/0050e004.md#insn-0050e5a8)
- 新版 `0050e568`（命令位置の公開資料なし） · `0050e5a8`（命令位置の公開資料なし） · `0050e5e8`（命令位置の公開資料なし）

~~~diff
- 0050e528 ["INT_ADD", "register:40f0:8", ["const:50e528:8", "const:4:8"]]
- 0050e528 ["CALL", null, ["callee:00c58a20:8"]]
+ 0050e568 ["INT_ADD", "register:40f0:8", ["const:50e568:8", "const:4:8"]]
+ 0050e568 ["CALL", null, ["callee:00c58a20:8"]]
- 0050e528 bytes 3e281d94
+ 0050e568 bytes 2e291d94
- 0050e568 ["COPY", "register:0:8", ["register:4048:8"]]
- 0050e568 ["INT_ADD", "register:40f0:8", ["const:50e568:8", "const:4:8"]]
- 0050e568 ["CALLIND", null, ["register:0:8"]]
+ 0050e5a8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050e5a8 ["INT_ADD", "register:40f0:8", ["const:50e5a8:8", "const:4:8"]]
+ 0050e5a8 ["CALLIND", null, ["register:0:8"]]
- 0050e568 bytes 20013fd6
+ 0050e5a8 bytes 20013fd6
- 0050e5a8 ["INT_ADD", "register:40f0:8", ["const:50e5a8:8", "const:4:8"]]
- 0050e5a8 ["CALL", null, ["callee:00c57ef0:8"]]
+ 0050e5e8 ["INT_ADD", "register:40f0:8", ["const:50e5e8:8", "const:4:8"]]
+ 0050e5e8 ["CALL", null, ["callee:00c57ef0:8"]]
- 0050e5a8 bytes 52251d94
+ 0050e5e8 bytes 42261d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2c8a3b723a9a70a237a9c5ac10ec89e"></a>

### [`0050ed6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050e/0050ed6c.md) → [`0050edac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050e/0050edac.md) _ZNK5Botan11X509_Object15check_signatureEPKNS_10Public_KeyE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c598a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c598a0.md) · 呼出先 8件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md)
- 新版 呼出元 1件 [`00c59ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59ca0.md) · 呼出先 8件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c57f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f60.md)

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
    "old": {
      "definition_site": "0050ee00",
      "incomplete_value": false,
      "site": "0050ee0c",
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
            "const:e39:8"
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
    "old": {
      "definition_site": "0050ee2c",
      "incomplete_value": false,
      "site": "0050ee34",
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
            "const:25:8"
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
    "old": {
      "definition_site": "0050ee7c",
      "incomplete_value": true,
      "site": "0050ee88",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
      "0050ee40",
      "PARAM",
      [
        "storage",
        "002bfe39",
        null,
        "string"
      ]
    ],
    [
      "0050ee6c",
      "PARAM",
      [
        "storage",
        "0029f025",
        null,
        "string"
      ]
    ],
    [
      "0050eeb8",
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
      "0050ee40",
      "PARAM",
      [
        "storage",
        "002bfe79",
        null,
        "string"
      ]
    ],
    [
      "0050ee6c",
      "PARAM",
      [
        "storage",
        "0029f0f2",
        null,
        "string"
      ]
    ],
    [
      "0050eeb8",
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

- 旧版 [`0050ee0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050e/0050ed6c.md#insn-0050ee0c) · [`0050ee34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050e/0050ed6c.md#insn-0050ee34) · [`0050ee88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050e/0050ed6c.md#insn-0050ee88)
- 新版 `0050ee4c`（命令位置の公開資料なし） · `0050ee74`（命令位置の公開資料なし） · `0050eec8`（命令位置の公開資料なし）

~~~diff
- 0050ee0c ["INT_ADD", "register:40f0:8", ["const:50ee0c:8", "const:4:8"]]
- 0050ee0c ["CALL", null, ["callee:00c57f60:8"]]
+ 0050ee4c ["INT_ADD", "register:40f0:8", ["const:50ee4c:8", "const:4:8"]]
+ 0050ee4c ["CALL", null, ["callee:00c57f60:8"]]
- 0050ee0c bytes 55231d94
+ 0050ee4c bytes 45241d94
- 0050ee34 ["INT_ADD", "register:40f0:8", ["const:50ee34:8", "const:4:8"]]
- 0050ee34 ["CALL", null, ["callee:00c57f70:8"]]
+ 0050ee74 ["INT_ADD", "register:40f0:8", ["const:50ee74:8", "const:4:8"]]
+ 0050ee74 ["CALL", null, ["callee:00c57f70:8"]]
- 0050ee34 bytes 4f231d94
+ 0050ee74 bytes 3f241d94
- 0050ee88 ["INT_ADD", "register:40f0:8", ["const:50ee88:8", "const:4:8"]]
- 0050ee88 ["CALL", null, ["callee:00c57f10:8"]]
+ 0050eec8 ["INT_ADD", "register:40f0:8", ["const:50eec8:8", "const:4:8"]]
+ 0050eec8 ["CALL", null, ["callee:00c57f10:8"]]
- 0050ee88 bytes 22231d94
+ 0050eec8 bytes 12241d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4aad887a0a304546db483e5ebf2f7cda"></a>

### [`0050ef4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050e/0050ef4c.md) → [`0050ef8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050e/0050ef8c.md) _ZNK5Botan14PKCS10_Request18subject_public_keyEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59890.md) · 呼出先 6件 [`00536cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/00536cc4.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c592d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c592d0.md) [`00c598c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c598c0.md)
- 新版 呼出元 1件 [`00c59c90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59c90.md) · 呼出先 6件 [`00536d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536d04.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c596d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c596d0.md) [`00c59cc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59cc0.md)

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
    "old": {
      "definition_site": "0050ef84",
      "incomplete_value": true,
      "site": "0050ef84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "0050efcc",
      "incomplete_value": true,
      "site": "0050efcc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0050efb4",
      "READ",
      [
        "storage",
        "00c9a9e0",
        null,
        "pointer"
      ]
    ],
    [
      "0050efc4",
      "DATA",
      [
        "storage",
        "00c66f88",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "0050effc",
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
      "0050efb4",
      "READ",
      [
        "storage",
        "00c9ade0",
        null,
        "pointer"
      ]
    ],
    [
      "0050efc4",
      "DATA",
      [
        "storage",
        "00c67388",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "0050effc",
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

- 旧版 [`0050efcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050e/0050ef4c.md#insn-0050efcc) · [`0050ef6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050e/0050ef4c.md#insn-0050ef6c) · [`0050ef74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050e/0050ef4c.md#insn-0050ef74)
- 新版 `0050f00c`（命令位置の公開資料なし） · `0050efac`（命令位置の公開資料なし） · `0050efb4`（命令位置の公開資料なし）

~~~diff
- 0050efcc ["COPY", "register:0:8", ["register:4048:8"]]
- 0050efcc ["INT_ADD", "register:40f0:8", ["const:50efcc:8", "const:4:8"]]
- 0050efcc ["CALLIND", null, ["register:0:8"]]
+ 0050f00c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050f00c ["INT_ADD", "register:40f0:8", ["const:50f00c:8", "const:4:8"]]
+ 0050f00c ["CALLIND", null, ["register:0:8"]]
- 0050efcc bytes 20013fd6
+ 0050f00c bytes 20013fd6
- 0050ef6c ["INT_ADD", "register:40f0:8", ["const:50ef6c:8", "const:4:8"]]
- 0050ef6c ["CALL", null, ["callee:00c59cc0:8"]]
+ 0050efac ["INT_ADD", "register:40f0:8", ["const:50efac:8", "const:4:8"]]
+ 0050efac ["CALL", null, ["callee:00c59cc0:8"]]
- 0050ef6c bytes 552a1d94
+ 0050efac bytes 452b1d94
- 0050ef74 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9e0:8"]]
- 0050ef74 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050efb4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:de0:8"]]
+ 0050efb4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050ef74 bytes 08f144f9
+ 0050efb4 bytes 08f146f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b56818f6149f7cf32a5a48c90838d13"></a>

### [`0050f068`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f068.md) → [`0050f0a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f0a8.md) _ZNK5Botan14PKCS10_Request4dataEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c598c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c598c0.md) · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`00c59cc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59cc0.md) · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
    "old": {
      "definition_site": "0050f0c8",
      "incomplete_value": false,
      "site": "0050f0d0",
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
            "const:11d:8"
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
    "old": {
      "definition_site": "0050f104",
      "incomplete_value": true,
      "site": "0050f110",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0050f140",
      "incomplete_value": false,
      "site": "0050f150",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "0050f100",
      "incomplete_value": false,
      "site": "0050f110",
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
      "0050f108",
      "PARAM",
      [
        "storage",
        "002a111d",
        null,
        "string"
      ]
    ],
    [
      "0050f140",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "0050f144",
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
      "0050f108",
      "PARAM",
      [
        "storage",
        "002a11ea",
        null,
        "string"
      ]
    ],
    [
      "0050f140",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "0050f144",
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

- 旧版 [`0050f0d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f068.md#insn-0050f0d0) · [`0050f110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f068.md#insn-0050f110) · [`0050f0bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f068.md#insn-0050f0bc)
- 新版 `0050f110`（命令位置の公開資料なし） · `0050f150`（命令位置の公開資料なし） · `0050f0fc`（命令位置の公開資料なし）

~~~diff
- 0050f0d0 ["INT_ADD", "register:40f0:8", ["const:50f0d0:8", "const:4:8"]]
- 0050f0d0 ["CALL", null, ["callee:0043ddd8:8"]]
+ 0050f110 ["INT_ADD", "register:40f0:8", ["const:50f110:8", "const:4:8"]]
+ 0050f110 ["CALL", null, ["callee:0043ddd8:8"]]
- 0050f0d0 bytes 32bbfc97
+ 0050f110 bytes 32bbfc97
- 0050f110 ["INT_ADD", "register:40f0:8", ["const:50f110:8", "const:4:8"]]
- 0050f110 ["CALL", null, ["callee:00c57f10:8"]]
+ 0050f150 ["INT_ADD", "register:40f0:8", ["const:50f150:8", "const:4:8"]]
+ 0050f150 ["CALL", null, ["callee:00c57f10:8"]]
- 0050f110 bytes 80221d94
+ 0050f150 bytes 70231d94
- 0050f0bc ["INT_ADD", "register:40f0:8", ["const:50f0bc:8", "const:4:8"]]
- 0050f0bc ["CALL", null, ["callee:00c57ef0:8"]]
+ 0050f0fc ["INT_ADD", "register:40f0:8", ["const:50f0fc:8", "const:4:8"]]
+ 0050f0fc ["CALL", null, ["callee:00c57ef0:8"]]
- 0050f0bc bytes 8d221d94
+ 0050f0fc bytes 7d231d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2dd5796a00ee182b320f0de0f31b6f0b"></a>

### [`0050f200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f200.md) → [`0050f240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f240.md) _ZNK5Botan14PKCS10_Request11constraintsEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c598d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c598d0.md) · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58280.md) [`00c596c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c596c0.md) [`00c598c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c598c0.md)
- 新版 呼出元 1件 [`00c59cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59cd0.md) · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58680.md) [`00c59ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59ac0.md) [`00c59cc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59cc0.md)

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
    "old": {
      "definition_site": "0050f244",
      "incomplete_value": true,
      "site": "0050f244",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a8d:8"
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
    "old": {
      "definition_site": "0050f238",
      "incomplete_value": true,
      "site": "0050f248",
      "value": [
        "LOAD",
        "8",
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
    "old": {
      "definition_site": "0050f2b0",
      "incomplete_value": true,
      "site": "0050f2b0",
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
      "0050f270",
      "READ",
      [
        "storage",
        "002a9a8d",
        null,
        "string"
      ]
    ],
    [
      "0050f278",
      "READ",
      [
        "storage",
        "002a9a94",
        null,
        "string"
      ]
    ],
    [
      "0050f2e0",
      "READ",
      [
        "storage",
        "00c9ad78",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050f270",
      "READ",
      [
        "storage",
        "002a9b5a",
        null,
        "string"
      ]
    ],
    [
      "0050f278",
      "READ",
      [
        "storage",
        "002a9b61",
        null,
        "string"
      ]
    ],
    [
      "0050f2e0",
      "READ",
      [
        "storage",
        "00c9b178",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050f270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f200.md#insn-0050f270) · [`0050f284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f200.md#insn-0050f284) · [`0050f220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f200.md#insn-0050f220)
- 新版 `0050f2b0`（命令位置の公開資料なし） · `0050f2c4`（命令位置の公開資料なし） · `0050f260`（命令位置の公開資料なし）

~~~diff
- 0050f270 ["COPY", "register:0:8", ["register:4040:8"]]
- 0050f270 ["INT_ADD", "register:40f0:8", ["const:50f270:8", "const:4:8"]]
- 0050f270 ["CALLIND", null, ["register:0:8"]]
+ 0050f2b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0050f2b0 ["INT_ADD", "register:40f0:8", ["const:50f2b0:8", "const:4:8"]]
+ 0050f2b0 ["CALLIND", null, ["register:0:8"]]
- 0050f270 bytes 00013fd6
+ 0050f2b0 bytes 00013fd6
- 0050f284 ["INT_ADD", "register:40f0:8", ["const:50f284:8", "const:4:8"]]
- 0050f284 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0050f2c4 ["INT_ADD", "register:40f0:8", ["const:50f2c4:8", "const:4:8"]]
+ 0050f2c4 ["CALL", null, ["callee:00c57eb0:8"]]
- 0050f284 bytes 0b221d94
+ 0050f2c4 bytes fb221d94
- 0050f220 ["INT_ADD", "register:40f0:8", ["const:50f220:8", "const:4:8"]]
- 0050f220 ["CALL", null, ["callee:00c59cc0:8"]]
+ 0050f260 ["INT_ADD", "register:40f0:8", ["const:50f260:8", "const:4:8"]]
+ 0050f260 ["CALL", null, ["callee:00c59cc0:8"]]
- 0050f220 bytes a8291d94
+ 0050f260 bytes 982a1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8b8a4abd56ef563bfe74b6c12831ac8"></a>

### [`0050f3ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f3ac.md) → [`0050f3ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f3ec.md) _ZNK5Botan14PKCS10_Request14ex_constraintsEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c598f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c598f0.md) · 呼出先 12件 [`00531b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/00531b44.md) [`0053ee30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053e/0053ee30.md) [`0053efc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053e/0053efc4.md) [`00540694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540694.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md)
- 新版 呼出元 1件 [`00c59cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59cf0.md) · 呼出先 12件 [`00531b84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00531/00531b84.md) [`0053ee70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053e/0053ee70.md) [`0053f004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053f004.md) [`005406d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005406d4.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md)

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
    "old": {
      "definition_site": "0050f3f4",
      "incomplete_value": true,
      "site": "0050f404",
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
                "const:1b9:8"
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
    "old": {
      "definition_site": "0050f408",
      "incomplete_value": true,
      "site": "0050f408",
      "value": [
        "LOAD",
        "8",
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
    "old": {
      "definition_site": "0050f3fc",
      "incomplete_value": true,
      "site": "0050f40c",
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
                "const:410:8"
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
      "0050f434",
      "READ",
      [
        "storage",
        "002ba1b9",
        null,
        "string"
      ]
    ],
    [
      "0050f438",
      "READ",
      [
        "storage",
        "002ba1c8",
        null,
        "string"
      ]
    ],
    [
      "0050f43c",
      "READ",
      [
        "storage",
        "002c2410",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0050f434",
      "READ",
      [
        "storage",
        "002ba1f9",
        null,
        "string"
      ]
    ],
    [
      "0050f438",
      "READ",
      [
        "storage",
        "002ba208",
        null,
        "string"
      ]
    ],
    [
      "0050f43c",
      "READ",
      [
        "storage",
        "002c2450",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050f438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f3ac.md#insn-0050f438) · [`0050f44c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f3ac.md#insn-0050f44c) · [`0050f3d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f3ac.md#insn-0050f3d8)
- 新版 `0050f478`（命令位置の公開資料なし） · `0050f48c`（命令位置の公開資料なし） · `0050f418`（命令位置の公開資料なし）

~~~diff
- 0050f438 ["COPY", "register:0:8", ["register:4040:8"]]
- 0050f438 ["INT_ADD", "register:40f0:8", ["const:50f438:8", "const:4:8"]]
- 0050f438 ["CALLIND", null, ["register:0:8"]]
+ 0050f478 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0050f478 ["INT_ADD", "register:40f0:8", ["const:50f478:8", "const:4:8"]]
+ 0050f478 ["CALLIND", null, ["register:0:8"]]
- 0050f438 bytes 00013fd6
+ 0050f478 bytes 00013fd6
- 0050f44c ["INT_ADD", "register:40f0:8", ["const:50f44c:8", "const:4:8"]]
- 0050f44c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0050f48c ["INT_ADD", "register:40f0:8", ["const:50f48c:8", "const:4:8"]]
+ 0050f48c ["CALL", null, ["callee:00c57eb0:8"]]
- 0050f44c bytes 99211d94
+ 0050f48c bytes 89221d94
- 0050f3d8 ["INT_ADD", "register:40f0:8", ["const:50f3d8:8", "const:4:8"]]
- 0050f3d8 ["CALL", null, ["callee:00c59cc0:8"]]
+ 0050f418 ["INT_ADD", "register:40f0:8", ["const:50f418:8", "const:4:8"]]
+ 0050f418 ["CALL", null, ["callee:00c59cc0:8"]]
- 0050f3d8 bytes 3a291d94
+ 0050f418 bytes 2a2a1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-183e6bbce32ab8f3bf06fdd7482fd90a"></a>

### [`0050f5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f5d4.md) → [`0050f614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f614.md) _ZNK5Botan14PKCS10_Request5is_CAEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c59900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59900.md) · 呼出先 7件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58280.md) [`00c596c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c596c0.md)
- 新版 呼出元 1件 [`00c59d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59d00.md) · 呼出先 7件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58680.md) [`00c59ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59ac0.md)

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
    "old": {
      "definition_site": "0050f610",
      "incomplete_value": true,
      "site": "0050f620",
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
                "const:2c0000:8"
              ],
              [
                "leaf",
                "const:fe7:8"
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
    "old": {
      "definition_site": "0050f624",
      "incomplete_value": true,
      "site": "0050f624",
      "value": [
        "LOAD",
        "8",
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
    "old": {
      "definition_site": "0050f618",
      "incomplete_value": true,
      "site": "0050f628",
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
                "const:410:8"
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
      "0050f650",
      "READ",
      [
        "storage",
        "002c0fe7",
        null,
        "string"
      ]
    ],
    [
      "0050f654",
      "READ",
      [
        "storage",
        "002c0ff6",
        null,
        "string"
      ]
    ],
    [
      "0050f658",
      "READ",
      [
        "storage",
        "002c2410",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0050f650",
      "READ",
      [
        "storage",
        "002c1027",
        null,
        "string"
      ]
    ],
    [
      "0050f654",
      "READ",
      [
        "storage",
        "002c1036",
        null,
        "string"
      ]
    ],
    [
      "0050f658",
      "READ",
      [
        "storage",
        "002c2450",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050f654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f5d4.md#insn-0050f654) · [`0050f668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f5d4.md#insn-0050f668) · [`0050f5f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f5d4.md#insn-0050f5f4)
- 新版 `0050f694`（命令位置の公開資料なし） · `0050f6a8`（命令位置の公開資料なし） · `0050f634`（命令位置の公開資料なし）

~~~diff
- 0050f654 ["COPY", "register:0:8", ["register:4040:8"]]
- 0050f654 ["INT_ADD", "register:40f0:8", ["const:50f654:8", "const:4:8"]]
- 0050f654 ["CALLIND", null, ["register:0:8"]]
+ 0050f694 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0050f694 ["INT_ADD", "register:40f0:8", ["const:50f694:8", "const:4:8"]]
+ 0050f694 ["CALLIND", null, ["register:0:8"]]
- 0050f654 bytes 00013fd6
+ 0050f694 bytes 00013fd6
- 0050f668 ["INT_ADD", "register:40f0:8", ["const:50f668:8", "const:4:8"]]
- 0050f668 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0050f6a8 ["INT_ADD", "register:40f0:8", ["const:50f6a8:8", "const:4:8"]]
+ 0050f6a8 ["CALL", null, ["callee:00c57eb0:8"]]
- 0050f668 bytes 12211d94
+ 0050f6a8 bytes 02221d94
- 0050f5f4 ["INT_ADD", "register:40f0:8", ["const:50f5f4:8", "const:4:8"]]
- 0050f5f4 ["CALL", null, ["callee:00c59cc0:8"]]
+ 0050f634 ["INT_ADD", "register:40f0:8", ["const:50f634:8", "const:4:8"]]
+ 0050f634 ["CALL", null, ["callee:00c59cc0:8"]]
- 0050f5f4 bytes b3281d94
+ 0050f634 bytes a3291d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a860e706fc88010233e3e69d978bb01"></a>

### [`0050f760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f760.md) → [`0050f7a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f7a0.md) _ZNK5Botan14PKCS10_Request10path_limitEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c59910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59910.md) · 呼出先 9件 [`00530fa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/00530fa8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58280.md)
- 新版 呼出元 1件 [`00c59d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59d10.md) · 呼出先 9件 [`00530fe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00530/00530fe8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58680.md)

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
    "old": {
      "definition_site": "0050f79c",
      "incomplete_value": true,
      "site": "0050f7ac",
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
                "const:2c0000:8"
              ],
              [
                "leaf",
                "const:fe7:8"
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
    "old": {
      "definition_site": "0050f7b0",
      "incomplete_value": true,
      "site": "0050f7b0",
      "value": [
        "LOAD",
        "8",
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
    "old": {
      "definition_site": "0050f7a4",
      "incomplete_value": true,
      "site": "0050f7b4",
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
                "const:410:8"
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
      "0050f7dc",
      "READ",
      [
        "storage",
        "002c0fe7",
        null,
        "string"
      ]
    ],
    [
      "0050f7e0",
      "READ",
      [
        "storage",
        "002c0ff6",
        null,
        "string"
      ]
    ],
    [
      "0050f7e4",
      "READ",
      [
        "storage",
        "002c2410",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0050f7dc",
      "READ",
      [
        "storage",
        "002c1027",
        null,
        "string"
      ]
    ],
    [
      "0050f7e0",
      "READ",
      [
        "storage",
        "002c1036",
        null,
        "string"
      ]
    ],
    [
      "0050f7e4",
      "READ",
      [
        "storage",
        "002c2450",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050f7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f760.md#insn-0050f7e0) · [`0050f7f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f760.md#insn-0050f7f4) · [`0050f780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f760.md#insn-0050f780)
- 新版 `0050f820`（命令位置の公開資料なし） · `0050f834`（命令位置の公開資料なし） · `0050f7c0`（命令位置の公開資料なし）

~~~diff
- 0050f7e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0050f7e0 ["INT_ADD", "register:40f0:8", ["const:50f7e0:8", "const:4:8"]]
- 0050f7e0 ["CALLIND", null, ["register:0:8"]]
+ 0050f820 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0050f820 ["INT_ADD", "register:40f0:8", ["const:50f820:8", "const:4:8"]]
+ 0050f820 ["CALLIND", null, ["register:0:8"]]
- 0050f7e0 bytes 00013fd6
+ 0050f820 bytes 00013fd6
- 0050f7f4 ["INT_ADD", "register:40f0:8", ["const:50f7f4:8", "const:4:8"]]
- 0050f7f4 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0050f834 ["INT_ADD", "register:40f0:8", ["const:50f834:8", "const:4:8"]]
+ 0050f834 ["CALL", null, ["callee:00c57eb0:8"]]
- 0050f7f4 bytes af201d94
+ 0050f834 bytes 9f211d94
- 0050f780 ["INT_ADD", "register:40f0:8", ["const:50f780:8", "const:4:8"]]
- 0050f780 ["CALL", null, ["callee:00c59cc0:8"]]
+ 0050f7c0 ["INT_ADD", "register:40f0:8", ["const:50f7c0:8", "const:4:8"]]
+ 0050f7c0 ["CALL", null, ["callee:00c59cc0:8"]]
- 0050f780 bytes 50281d94
+ 0050f7c0 bytes 40291d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a52ae32498008e1aae51933a221f3fd"></a>

### [`0050f908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f908.md) → [`0050f948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050f948.md) _ZNK5Botan14Cert_Extension17Basic_Constraints14get_path_limitEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59920.md) · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 1件 [`00c59d20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59d20.md) · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

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
    "old": {
      "definition_site": "0050f96c",
      "incomplete_value": false,
      "site": "0050f974",
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
            "const:ba0:8"
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
    "old": {
      "definition_site": "0050f9a8",
      "incomplete_value": true,
      "site": "0050f9b4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0050f9e4",
      "incomplete_value": false,
      "site": "0050f9f4",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "0050f9a4",
      "incomplete_value": false,
      "site": "0050f9b4",
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
      "0050f9ac",
      "PARAM",
      [
        "storage",
        "002b2ba0",
        null,
        "string"
      ]
    ],
    [
      "0050f9e4",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "0050f9e8",
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
      "0050f9ac",
      "PARAM",
      [
        "storage",
        "002b2be0",
        null,
        "string"
      ]
    ],
    [
      "0050f9e4",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "0050f9e8",
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

- 旧版 [`0050f974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f908.md#insn-0050f974) · [`0050f9b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f908.md#insn-0050f9b4) · [`0050f960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050f908.md#insn-0050f960)
- 新版 `0050f9b4`（命令位置の公開資料なし） · `0050f9f4`（命令位置の公開資料なし） · `0050f9a0`（命令位置の公開資料なし）

~~~diff
- 0050f974 ["INT_ADD", "register:40f0:8", ["const:50f974:8", "const:4:8"]]
- 0050f974 ["CALL", null, ["callee:0043ddd8:8"]]
+ 0050f9b4 ["INT_ADD", "register:40f0:8", ["const:50f9b4:8", "const:4:8"]]
+ 0050f9b4 ["CALL", null, ["callee:0043ddd8:8"]]
- 0050f974 bytes 09b9fc97
+ 0050f9b4 bytes 09b9fc97
- 0050f9b4 ["INT_ADD", "register:40f0:8", ["const:50f9b4:8", "const:4:8"]]
- 0050f9b4 ["CALL", null, ["callee:00c57f10:8"]]
+ 0050f9f4 ["INT_ADD", "register:40f0:8", ["const:50f9f4:8", "const:4:8"]]
+ 0050f9f4 ["CALL", null, ["callee:00c57f10:8"]]
- 0050f9b4 bytes 57201d94
+ 0050f9f4 bytes 47211d94
- 0050f960 ["INT_ADD", "register:40f0:8", ["const:50f960:8", "const:4:8"]]
- 0050f960 ["CALL", null, ["callee:00c57ef0:8"]]
+ 0050f9a0 ["INT_ADD", "register:40f0:8", ["const:50f9a0:8", "const:4:8"]]
+ 0050f9a0 ["CALL", null, ["callee:00c57ef0:8"]]
- 0050f960 bytes 64201d94
+ 0050f9a0 bytes 54211d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a15ca6601c633c048bc2be1208b2ac6"></a>

### [`0050fa08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050fa08.md) → [`0050fa48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050fa48.md) _ZN5Botan7X509_CAC2ERKNS_16X509_CertificateERKNS_11Private_KeyERKNSt6__ndk112basic_stringIcNS7_11char_traitsIcEENS7_9allocatorIcEEEERNS_21Ra

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 19件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0050fee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050fee8.md) [`00510020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00510/00510020.md)
- 新版 呼出元 0件  · 呼出先 19件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0050ff28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050ff28.md) [`00510060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00510/00510060.md)

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
    "old": {
      "definition_site": "0050fa50",
      "incomplete_value": true,
      "site": "0050fa50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "0050fa8c",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "0050fba8",
      "incomplete_value": false,
      "site": "0050fbb4",
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
            "const:c4c:8"
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
      "0050fa74",
      "READ",
      [
        "storage",
        "00c9a938",
        null,
        "pointer"
      ]
    ],
    [
      "0050fa90",
      "DATA",
      [
        "storage",
        "00c65da8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0050fac8",
      "READ",
      [
        "storage",
        "00c9ace0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050fa74",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "0050fa90",
      "DATA",
      [
        "storage",
        "00c661a8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0050fac8",
      "READ",
      [
        "storage",
        "00c9b0e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050fbb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050fa08.md#insn-0050fbb4) · [`0050fd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050fa08.md#insn-0050fd58) · [`0050fd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050fa08.md#insn-0050fd94)
- 新版 `0050fbf4`（命令位置の公開資料なし） · `0050fd98`（命令位置の公開資料なし） · `0050fdd4`（命令位置の公開資料なし）

~~~diff
- 0050fbb4 ["INT_ADD", "register:40f0:8", ["const:50fbb4:8", "const:4:8"]]
- 0050fbb4 ["CALL", null, ["callee:0050ff28:8"]]
+ 0050fbf4 ["INT_ADD", "register:40f0:8", ["const:50fbf4:8", "const:4:8"]]
+ 0050fbf4 ["CALL", null, ["callee:0050ff28:8"]]
- 0050fbb4 bytes cd000094
+ 0050fbf4 bytes cd000094
- 0050fd58 ["INT_ADD", "register:40f0:8", ["const:50fd58:8", "const:4:8"]]
- 0050fd58 ["CALL", null, ["callee:0043ddd8:8"]]
+ 0050fd98 ["INT_ADD", "register:40f0:8", ["const:50fd98:8", "const:4:8"]]
+ 0050fd98 ["CALL", null, ["callee:0043ddd8:8"]]
- 0050fd58 bytes 10b8fc97
+ 0050fd98 bytes 10b8fc97
- 0050fd94 ["INT_ADD", "register:40f0:8", ["const:50fd94:8", "const:4:8"]]
- 0050fd94 ["CALL", null, ["callee:00c57f10:8"]]
+ 0050fdd4 ["INT_ADD", "register:40f0:8", ["const:50fdd4:8", "const:4:8"]]
+ 0050fdd4 ["CALL", null, ["callee:00c57f10:8"]]
- 0050fd94 bytes 5f1f1d94
+ 0050fdd4 bytes 4f201d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f7629f0894fa0118653ee4c066b4bce"></a>

### [`00510020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00510/00510020.md) → [`00510060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00510/00510060.md) FUN_00510060

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`0050fa08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050f/0050fa08.md) [`005109bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00510/005109bc.md) [`0051276c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/0051276c.md) [`0052d4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052d4d0.md) [`0052e2f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052e/0052e2f4.md) · 呼出先 16件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`0046d568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d568.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 5件 [`0050fa48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050f/0050fa48.md) [`005109fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00510/005109fc.md) [`005127ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/005127ac.md) [`0052d510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052d510.md) [`0052e334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052e/0052e334.md) · 呼出先 16件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`0046d5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d5a8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
    "old": {
      "definition_site": "00510188",
      "incomplete_value": false,
      "site": "00510194",
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
            "const:389:8"
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
    "old": {
      "definition_site": "005101c8",
      "incomplete_value": true,
      "site": "005101d4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00510204",
      "incomplete_value": false,
      "site": "00510214",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "005101c4",
      "incomplete_value": false,
      "site": "005101d4",
      "value": [
        "leaf",
        "const:535828:8"
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
      "005101c8",
      "PARAM",
      [
        "storage",
        "002ba389",
        null,
        "string"
      ]
    ],
    [
      "00510204",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "00510208",
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
      "005101c8",
      "PARAM",
      [
        "storage",
        "002ba3c9",
        null,
        "string"
      ]
    ],
    [
      "00510204",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "00510208",
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

- 旧版 [`00510194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00510/00510020.md#insn-00510194) · [`005101d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00510/00510020.md#insn-005101d4) · [`00510214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00510/00510020.md#insn-00510214)
- 新版 `005101d4`（命令位置の公開資料なし） · `00510214`（命令位置の公開資料なし） · `00510254`（命令位置の公開資料なし）

~~~diff
- 00510194 ["INT_ADD", "register:40f0:8", ["const:510194:8", "const:4:8"]]
- 00510194 ["CALL", null, ["callee:00c580b0:8"]]
+ 005101d4 ["INT_ADD", "register:40f0:8", ["const:5101d4:8", "const:4:8"]]
+ 005101d4 ["CALL", null, ["callee:00c580b0:8"]]
- 00510194 bytes c71e1d94
+ 005101d4 bytes b71f1d94
- 005101d4 ["INT_ADD", "register:40f0:8", ["const:5101d4:8", "const:4:8"]]
- 005101d4 ["CALL", null, ["callee:00c57f10:8"]]
+ 00510214 ["INT_ADD", "register:40f0:8", ["const:510214:8", "const:4:8"]]
+ 00510214 ["CALL", null, ["callee:00c57f10:8"]]
- 005101d4 bytes 4f1e1d94
+ 00510214 bytes 3f1f1d94
- 00510214 ["COPY", "tmp:0:8", ["const:62d:8"]]
- 00510214 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00510214 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00510214 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00510254 ["COPY", "tmp:0:8", ["const:66d:8"]]
+ 00510254 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00510254 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00510254 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00510214 bytes 00b41891
+ 00510254 bytes 00b41991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec2420bf671253b070cccd2fe2fbcbe0"></a>

### [`005109bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00510/005109bc.md) → [`005109fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00510/005109fc.md) _ZN5Botan7X509_CAC1ERKNS_16X509_CertificateERKNS_11Private_KeyERKNSt6__ndk13mapINS7_12basic_stringIcNS7_11char_traitsIcEENS7_9allocatorIcEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 14件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00510020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00510/00510020.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`0053afc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053afc0.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00510060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00510/00510060.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`0053b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053b000.md)

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
    "old": {
      "definition_site": "00510a08",
      "incomplete_value": true,
      "site": "00510a08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00510a44",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00510b18",
      "incomplete_value": false,
      "site": "00510b20",
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
            "const:fbd:8"
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
      "00510a28",
      "READ",
      [
        "storage",
        "00c9a938",
        null,
        "pointer"
      ]
    ],
    [
      "00510a48",
      "DATA",
      [
        "storage",
        "00c65da8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00510a80",
      "READ",
      [
        "storage",
        "00c9ace0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00510a28",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "00510a48",
      "DATA",
      [
        "storage",
        "00c661a8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00510a80",
      "READ",
      [
        "storage",
        "00c9b0e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00510b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00510/005109bc.md#insn-00510b20) · [`00510b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00510/005109bc.md#insn-00510b5c) · [`005109e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00510/005109bc.md#insn-005109e8)
- 新版 `00510b60`（命令位置の公開資料なし） · `00510b9c`（命令位置の公開資料なし） · `00510a28`（命令位置の公開資料なし）

~~~diff
- 00510b20 ["INT_ADD", "register:40f0:8", ["const:510b20:8", "const:4:8"]]
- 00510b20 ["CALL", null, ["callee:0043ddd8:8"]]
+ 00510b60 ["INT_ADD", "register:40f0:8", ["const:510b60:8", "const:4:8"]]
+ 00510b60 ["CALL", null, ["callee:0043ddd8:8"]]
- 00510b20 bytes 9eb4fc97
+ 00510b60 bytes 9eb4fc97
- 00510b5c ["INT_ADD", "register:40f0:8", ["const:510b5c:8", "const:4:8"]]
- 00510b5c ["CALL", null, ["callee:00c57f10:8"]]
+ 00510b9c ["INT_ADD", "register:40f0:8", ["const:510b9c:8", "const:4:8"]]
+ 00510b9c ["CALL", null, ["callee:00c57f10:8"]]
- 00510b5c bytes ed1b1d94
+ 00510b9c bytes dd1c1d94
- 005109e8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:938:8"]]
- 005109e8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00510a28 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d38:8"]]
+ 00510a28 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 005109e8 bytes 299d44f9
+ 00510a28 bytes 299d46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-763af0e3921e60bc0011d4fb7d11ae4e"></a>

### [`00510d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00510/00510d18.md) → [`00510d58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00510/00510d58.md) _ZNK5Botan7X509_CA12sign_requestERKNS_14PKCS10_RequestERNS_21RandomNumberGeneratorERKNS_9X509_TimeES8_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 25件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`0050b31c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050b/0050b31c.md) [`005111e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/005111e4.md) [`005115f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/005115f8.md) [`0053b3e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053b3e4.md)
- 新版 呼出元 0件  · 呼出先 25件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`0050b35c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050b/0050b35c.md) [`00511224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00511/00511224.md) [`00511638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00511/00511638.md) [`0053b424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053b424.md)

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
    "old": {
      "definition_site": "00510e04",
      "incomplete_value": true,
      "site": "00510e08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00510e38",
      "incomplete_value": true,
      "site": "00510e3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00510e78",
      "incomplete_value": true,
      "site": "00510e84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00510e38",
      "READ",
      [
        "storage",
        "00c9ad88",
        null,
        "pointer"
      ]
    ],
    [
      "00510e48",
      "DATA",
      [
        "storage",
        "00c67550",
        null,
        "undefined1[96]"
      ]
    ],
    [
      "00510e70",
      "READ",
      [
        "storage",
        "00c9ad78",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00510e38",
      "READ",
      [
        "storage",
        "00c9b188",
        null,
        "pointer"
      ]
    ],
    [
      "00510e48",
      "DATA",
      [
        "storage",
        "00c67950",
        null,
        "undefined1[96]"
      ]
    ],
    [
      "00510e70",
      "READ",
      [
        "storage",
        "00c9b178",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00510e48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00510/00510d18.md#insn-00510e48) · [`00510f38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00510/00510d18.md#insn-00510f38) · [`00510fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00510/00510d18.md#insn-00510fb8)
- 新版 `00510e88`（命令位置の公開資料なし） · `00510f78`（命令位置の公開資料なし） · `00510ff8`（命令位置の公開資料なし）

~~~diff
- 00510e48 ["INT_ADD", "register:40f0:8", ["const:510e48:8", "const:4:8"]]
- 00510e48 ["CALL", null, ["callee:00c59d30:8"]]
+ 00510e88 ["INT_ADD", "register:40f0:8", ["const:510e88:8", "const:4:8"]]
+ 00510e88 ["CALL", null, ["callee:00c59d30:8"]]
- 00510e48 bytes ba221d94
+ 00510e88 bytes aa231d94
- 00510f38 ["INT_ADD", "register:40f0:8", ["const:510f38:8", "const:4:8"]]
- 00510f38 ["CALL", null, ["callee:00c59d30:8"]]
+ 00510f78 ["INT_ADD", "register:40f0:8", ["const:510f78:8", "const:4:8"]]
+ 00510f78 ["CALL", null, ["callee:00c59d30:8"]]
- 00510f38 bytes 7e221d94
+ 00510f78 bytes 6e231d94
- 00510fb8 ["INT_ADD", "register:40f0:8", ["const:510fb8:8", "const:4:8"]]
- 00510fb8 ["CALL", null, ["callee:0053ee70:8"]]
+ 00510ff8 ["INT_ADD", "register:40f0:8", ["const:510ff8:8", "const:4:8"]]
+ 00510ff8 ["CALL", null, ["callee:0053ee70:8"]]
- 00510fb8 bytes 9eb70094
+ 00510ff8 bytes 9eb70094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9ce67d7d367260d2882a356df989b4f"></a>

### [`005111e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/005111e4.md) → [`00511224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00511/00511224.md) FUN_00511224

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00510d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00510/00510d18.md) [`00526990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00526/00526990.md) [`0052d4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052d4d0.md) [`0052e2f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052e/0052e2f4.md) · 呼出先 7件 [`0053c3cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053c3cc.md) [`0053ee30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053e/0053ee30.md) [`0053efc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053e/0053efc4.md) [`00540694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540694.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md)
- 新版 呼出元 4件 [`00510d58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00510/00510d58.md) [`005269d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00526/005269d0.md) [`0052d510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052d/0052d510.md) [`0052e334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052e/0052e334.md) · 呼出先 7件 [`0053c40c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053c/0053c40c.md) [`0053ee70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053e/0053ee70.md) [`0053f004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053f/0053f004.md) [`005406d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005406d4.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md)

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
    "old": {
      "definition_site": "00511228",
      "incomplete_value": true,
      "site": "0051123c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00511258",
      "READ",
      [
        "storage",
        "00c9ad10",
        null,
        "pointer"
      ]
    ],
    [
      "0051127c",
      "DATA",
      [
        "storage",
        "00c684c0",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00511258",
      "READ",
      [
        "storage",
        "00c9b110",
        null,
        "pointer"
      ]
    ],
    [
      "0051127c",
      "DATA",
      [
        "storage",
        "00c688c0",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051127c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/005111e4.md#insn-0051127c) · [`00511208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/005111e4.md#insn-00511208) · [`00511218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/005111e4.md#insn-00511218)
- 新版 `005112bc`（命令位置の公開資料なし） · `00511248`（命令位置の公開資料なし） · `00511258`（命令位置の公開資料なし）

~~~diff
- 0051127c ["INT_ADD", "register:40f0:8", ["const:51127c:8", "const:4:8"]]
- 0051127c ["CALL", null, ["callee:0053ee70:8"]]
+ 005112bc ["INT_ADD", "register:40f0:8", ["const:5112bc:8", "const:4:8"]]
+ 005112bc ["CALL", null, ["callee:0053ee70:8"]]
- 0051127c bytes edb60094
+ 005112bc bytes edb60094
- 00511208 ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 00511248 ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 00511208 bytes 493c00b0
+ 00511248 bytes 493c00d0
- 00511218 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d10:8"]]
- 00511218 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00511258 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:110:8"]]
+ 00511258 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00511218 bytes 298946f9
+ 00511258 bytes 298940f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8fa98917575e8aff990feec434276f35"></a>

### [`0051138c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/0051138c.md) → [`005113cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00511/005113cc.md) _ZN5Botan10Extensions7replaceEPNS_21Certificate_ExtensionEb

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59930.md) · 呼出先 13件 [`00516b84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516b84.md) [`00535b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`0053d6e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053d6e8.md) [`0054b904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b904.md) [`0054bbbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054bbbc.md)
- 新版 呼出元 1件 [`00c59d30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59d30.md) · 呼出先 13件 [`00516bc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516bc4.md) [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`0053d728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053d/0053d728.md) [`0054b944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054b944.md) [`0054bbfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054b/0054bbfc.md)

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
    "old": {
      "definition_site": "00511420",
      "incomplete_value": true,
      "site": "00511420",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00511464",
      "incomplete_value": true,
      "site": "00511468",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00511450",
      "READ",
      [
        "storage",
        "00c9ad20",
        null,
        "pointer"
      ]
    ],
    [
      "00511460",
      "DATA",
      [
        "storage",
        "00c6a038",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "00511498",
      "READ",
      [
        "storage",
        "00c9a940",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00511450",
      "READ",
      [
        "storage",
        "00c9b120",
        null,
        "pointer"
      ]
    ],
    [
      "00511460",
      "DATA",
      [
        "storage",
        "00c6a438",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "00511498",
      "READ",
      [
        "storage",
        "00c9ad40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005113cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/0051138c.md#insn-005113cc) · [`005113d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/0051138c.md#insn-005113d8) · [`005113e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/0051138c.md#insn-005113e8)
- 新版 `0051140c`（命令位置の公開資料なし） · `00511418`（命令位置の公開資料なし） · `00511428`（命令位置の公開資料なし）

~~~diff
- 005113cc ["COPY", "register:0:8", ["register:4048:8"]]
- 005113cc ["INT_ADD", "register:40f0:8", ["const:5113cc:8", "const:4:8"]]
- 005113cc ["CALLIND", null, ["register:0:8"]]
+ 0051140c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051140c ["INT_ADD", "register:40f0:8", ["const:51140c:8", "const:4:8"]]
+ 0051140c ["CALLIND", null, ["register:0:8"]]
- 005113cc bytes 20013fd6
+ 0051140c bytes 20013fd6
- 005113d8 ["INT_ADD", "register:40f0:8", ["const:5113d8:8", "const:4:8"]]
- 005113d8 ["CALL", null, ["callee:0054bf14:8"]]
+ 00511418 ["INT_ADD", "register:40f0:8", ["const:511418:8", "const:4:8"]]
+ 00511418 ["CALL", null, ["callee:0054bf14:8"]]
- 005113d8 bytes bfea0094
+ 00511418 bytes bfea0094
- 005113e8 ["INT_ADD", "register:40f0:8", ["const:5113e8:8", "const:4:8"]]
- 005113e8 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00511428 ["INT_ADD", "register:40f0:8", ["const:511428:8", "const:4:8"]]
+ 00511428 ["CALL", null, ["callee:00c57eb0:8"]]
- 005113e8 bytes b2191d94
+ 00511428 bytes a21a1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae9e53962b1b57b3bb2d215cbb446cd2"></a>

### [`00511670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/00511670.md) → [`005116b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00511/005116b0.md) _ZN5Botan7X509_CA9make_certEPNS_9PK_SignerERNS_21RandomNumberGeneratorERKNS_19AlgorithmIdentifierERKNSt6__ndk16vectorIhNS8_9allocatorIhEEEER

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59950.md) · 呼出先 16件 [`00535b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b40.md) [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`00c59d50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59d50.md) · 呼出先 16件 [`00535b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b80.md) [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

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
    "old": {
      "definition_site": "00511744",
      "incomplete_value": true,
      "site": "00511744",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "0051190c",
      "incomplete_value": true,
      "site": "0051190c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 29,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
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
    "old": {
      "definition_site": "00511978",
      "incomplete_value": true,
      "site": "00511978",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00511774",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "0051193c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "005119a8",
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
      "00511774",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "0051193c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "005119a8",
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

- 旧版 [`00511744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/00511670.md#insn-00511744) · [`005118cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/00511670.md#insn-005118cc) · [`0051190c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/00511670.md#insn-0051190c)
- 新版 `00511784`（命令位置の公開資料なし） · `0051190c`（命令位置の公開資料なし） · `0051194c`（命令位置の公開資料なし）

~~~diff
- 00511744 ["COPY", "register:0:8", ["register:4048:8"]]
- 00511744 ["INT_ADD", "register:40f0:8", ["const:511744:8", "const:4:8"]]
- 00511744 ["CALLIND", null, ["register:0:8"]]
+ 00511784 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00511784 ["INT_ADD", "register:40f0:8", ["const:511784:8", "const:4:8"]]
+ 00511784 ["CALLIND", null, ["register:0:8"]]
- 00511744 bytes 20013fd6
+ 00511784 bytes 20013fd6
- 005118cc ["INT_ADD", "register:40f0:8", ["const:5118cc:8", "const:4:8"]]
- 005118cc ["CALL", null, ["callee:00c59d60:8"]]
+ 0051190c ["INT_ADD", "register:40f0:8", ["const:51190c:8", "const:4:8"]]
+ 0051190c ["CALL", null, ["callee:00c59d60:8"]]
- 005118cc bytes 25201d94
+ 0051190c bytes 15211d94
- 0051190c ["COPY", "register:0:8", ["register:4048:8"]]
- 0051190c ["INT_ADD", "register:40f0:8", ["const:51190c:8", "const:4:8"]]
- 0051190c ["CALLIND", null, ["register:0:8"]]
+ 0051194c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051194c ["INT_ADD", "register:40f0:8", ["const:51194c:8", "const:4:8"]]
+ 0051194c ["CALLIND", null, ["register:0:8"]]
- 0051190c bytes 20013fd6
+ 0051194c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5dc5443f79a222e852dd643f543a4017"></a>

### [`0051209c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/0051209c.md) → [`005120dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/005120dc.md) _ZNK5Botan7X509_CA8make_crlERKNSt6__ndk16vectorINS_9CRL_EntryENS1_9allocatorIS3_EEEEjRNS_21RandomNumberGeneratorENS1_6chrono10time_pointINSB

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59970.md) · 呼出先 21件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00517250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00517/00517250.md) [`00535b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b40.md) [`0053b3e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053b3e4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00c59d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59d70.md) · 呼出先 21件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00517290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00517/00517290.md) [`00535b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b80.md) [`0053b424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053b424.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
    "old": {
      "definition_site": "005120f0",
      "incomplete_value": true,
      "site": "005120f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00512140",
      "incomplete_value": true,
      "site": "0051214c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "005121b0",
      "incomplete_value": true,
      "site": "005121b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00512118",
      "READ",
      [
        "storage",
        "00c9ad10",
        null,
        "pointer"
      ]
    ],
    [
      "00512130",
      "DATA",
      [
        "storage",
        "00c684c0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00512170",
      "READ",
      [
        "storage",
        "00c9ad90",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00512118",
      "READ",
      [
        "storage",
        "00c9b110",
        null,
        "pointer"
      ]
    ],
    [
      "00512130",
      "DATA",
      [
        "storage",
        "00c688c0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00512170",
      "READ",
      [
        "storage",
        "00c9b190",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00512130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/0051209c.md#insn-00512130) · [`00512174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/0051209c.md#insn-00512174) · [`00512228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/0051209c.md#insn-00512228)
- 新版 `00512170`（命令位置の公開資料なし） · `005121b4`（命令位置の公開資料なし） · `00512268`（命令位置の公開資料なし）

~~~diff
- 00512130 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d90:8"]]
- 00512130 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00512170 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:190:8"]]
+ 00512170 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00512130 bytes 08c946f9
+ 00512170 bytes 08c940f9
- 00512174 ["INT_ADD", "register:40f0:8", ["const:512174:8", "const:4:8"]]
- 00512174 ["CALL", null, ["callee:00c58000:8"]]
+ 005121b4 ["INT_ADD", "register:40f0:8", ["const:5121b4:8", "const:4:8"]]
+ 005121b4 ["CALL", null, ["callee:00c58000:8"]]
- 00512174 bytes a3161d94
+ 005121b4 bytes 93171d94
- 00512228 ["COPY", "register:0:8", ["register:4048:8"]]
- 00512228 ["INT_ADD", "register:40f0:8", ["const:512228:8", "const:4:8"]]
- 00512228 ["CALLIND", null, ["register:0:8"]]
+ 00512268 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00512268 ["INT_ADD", "register:40f0:8", ["const:512268:8", "const:4:8"]]
+ 00512268 ["CALLIND", null, ["register:0:8"]]
- 00512228 bytes 20013fd6
+ 00512268 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc3fe84597a9e0e9da120c76c835a7f4"></a>

### [`005128d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/005128d0.md) → [`00512910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/00512910.md) _ZN5Botan8X509_CRLC1ERNS_10DataSourceE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md) [`00c59880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59880.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md) [`00c59c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59c80.md)

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
    "old": {
      "definition_site": "00512910",
      "incomplete_value": true,
      "site": "00512910",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00512910",
      "incomplete_value": true,
      "site": "00512910",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00512950",
      "incomplete_value": true,
      "site": "00512958",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00512930",
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      "00512938",
      "READ",
      [
        "storage",
        "00c9a938",
        null,
        "pointer"
      ]
    ],
    [
      "00512950",
      "DATA",
      [
        "storage",
        "00c69620",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "00512930",
      "READ",
      [
        "storage",
        "00c9b158",
        null,
        "pointer"
      ]
    ],
    [
      "00512938",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "00512950",
      "DATA",
      [
        "storage",
        "00c69a20",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005128e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/005128d0.md#insn-005128e8) · [`005128f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/005128d0.md#insn-005128f0) · [`005128f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/005128d0.md#insn-005128f8)
- 新版 `00512928`（命令位置の公開資料なし） · `00512930`（命令位置の公開資料なし） · `00512938`（命令位置の公開資料なし）

~~~diff
- 005128e8 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00512928 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 005128e8 bytes 483c0090
+ 00512928 bytes 483c00b0
- 005128f0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d58:8"]]
- 005128f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00512930 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:158:8"]]
+ 00512930 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005128f0 bytes 08ad46f9
+ 00512930 bytes 08ad40f9
- 005128f8 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:938:8"]]
- 005128f8 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 00512938 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:d38:8"]]
+ 00512938 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 005128f8 bytes 4a9d44f9
+ 00512938 bytes 4a9d46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8690c99b80056616fe6cee71c6549f09"></a>

### [`00512a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/00512a24.md) → [`00512a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/00512a64.md) _ZN5Botan8X509_CRLC1ERKNSt6__ndk16vectorIhNS1_9allocatorIhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59990.md) · 呼出先 7件 [`00540388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540388.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)
- 新版 呼出元 1件 [`00c59d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59d90.md) · 呼出先 7件 [`005403c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005403c8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md)

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
    "old": {
      "definition_site": "00512a64",
      "incomplete_value": true,
      "site": "00512a64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00512a64",
      "incomplete_value": true,
      "site": "00512a64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00512aac",
      "incomplete_value": true,
      "site": "00512ab8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00512a84",
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      "00512a8c",
      "READ",
      [
        "storage",
        "00c9a938",
        null,
        "pointer"
      ]
    ],
    [
      "00512aa4",
      "DATA",
      [
        "storage",
        "00c69620",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "00512a84",
      "READ",
      [
        "storage",
        "00c9b158",
        null,
        "pointer"
      ]
    ],
    [
      "00512a8c",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "00512aa4",
      "DATA",
      [
        "storage",
        "00c69a20",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00512b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/00512a24.md#insn-00512b10) · [`00512a3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/00512a24.md#insn-00512a3c) · [`00512a44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/00512a24.md#insn-00512a44)
- 新版 `00512b50`（命令位置の公開資料なし） · `00512a7c`（命令位置の公開資料なし） · `00512a84`（命令位置の公開資料なし）

~~~diff
- 00512b10 ["COPY", "register:0:8", ["register:4048:8"]]
- 00512b10 ["INT_ADD", "register:40f0:8", ["const:512b10:8", "const:4:8"]]
- 00512b10 ["CALLIND", null, ["register:0:8"]]
+ 00512b50 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00512b50 ["INT_ADD", "register:40f0:8", ["const:512b50:8", "const:4:8"]]
+ 00512b50 ["CALLIND", null, ["register:0:8"]]
- 00512b10 bytes 20013fd6
+ 00512b50 bytes 20013fd6
- 00512a3c ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00512a7c ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00512a3c bytes 483c0090
+ 00512a7c bytes 483c00b0
- 00512a44 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d58:8"]]
- 00512a44 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00512a84 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:158:8"]]
+ 00512a84 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00512a44 bytes 08ad46f9
+ 00512a84 bytes 08ad40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6963145d172b21f9e872ae50243bb1a"></a>

### [`00512b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/00512b9c.md) → [`00512bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/00512bdc.md) _ZN5Botan8X509_CRLC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md) [`00c59260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59260.md) [`00c59270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59270.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md) [`00c59660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59660.md) [`00c59670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59670.md)

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
    "old": {
      "definition_site": "00512bdc",
      "incomplete_value": true,
      "site": "00512bdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00512bdc",
      "incomplete_value": true,
      "site": "00512bdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00512c1c",
      "incomplete_value": true,
      "site": "00512c24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00512bfc",
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      "00512c04",
      "READ",
      [
        "storage",
        "00c9a938",
        null,
        "pointer"
      ]
    ],
    [
      "00512c1c",
      "DATA",
      [
        "storage",
        "00c69620",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "00512bfc",
      "READ",
      [
        "storage",
        "00c9b158",
        null,
        "pointer"
      ]
    ],
    [
      "00512c04",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "00512c1c",
      "DATA",
      [
        "storage",
        "00c69a20",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00512bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/00512b9c.md#insn-00512bb4) · [`00512bbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/00512b9c.md#insn-00512bbc) · [`00512bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/00512b9c.md#insn-00512bc4)
- 新版 `00512bf4`（命令位置の公開資料なし） · `00512bfc`（命令位置の公開資料なし） · `00512c04`（命令位置の公開資料なし）

~~~diff
- 00512bb4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00512bf4 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00512bb4 bytes 483c0090
+ 00512bf4 bytes 483c00b0
- 00512bbc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d58:8"]]
- 00512bbc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00512bfc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:158:8"]]
+ 00512bfc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00512bbc bytes 08ad46f9
+ 00512bfc bytes 08ad40f9
- 00512bc4 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:938:8"]]
- 00512bc4 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 00512c04 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:d38:8"]]
+ 00512c04 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 00512bc4 bytes 4a9d44f9
+ 00512c04 bytes 4a9d46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3073520eec84b3dafb1a61f32f3f990"></a>

### [`00512cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/00512cc8.md) → [`00512d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00512/00512d08.md) _ZN5Botan8X509_CRLC1ERKNS_7X509_DNERKNS_9X509_TimeES6_RKNSt6__ndk16vectorINS_9CRL_EntryENS7_9allocatorIS9_EEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0053bd38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053bd38.md) [`00548e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548e28.md) [`0054ab24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054ab24.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0053bd78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053bd78.md) [`00548e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00548/00548e68.md) [`0054ab64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0054a/0054ab64.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
    "old": {
      "definition_site": "00512d3c",
      "incomplete_value": true,
      "site": "00512d3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00512d3c",
      "incomplete_value": true,
      "site": "00512d3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "00512d78",
      "incomplete_value": true,
      "site": "00512d80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00512d64",
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      "00512d68",
      "READ",
      [
        "storage",
        "00c9a938",
        null,
        "pointer"
      ]
    ],
    [
      "00512d7c",
      "DATA",
      [
        "storage",
        "00c69620",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "00512d64",
      "READ",
      [
        "storage",
        "00c9b158",
        null,
        "pointer"
      ]
    ],
    [
      "00512d68",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "00512d7c",
      "DATA",
      [
        "storage",
        "00c69a20",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00512d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/00512cc8.md#insn-00512d10) · [`00512d24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/00512cc8.md#insn-00512d24) · [`00512d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/00512cc8.md#insn-00512d28)
- 新版 `00512d50`（命令位置の公開資料なし） · `00512d64`（命令位置の公開資料なし） · `00512d68`（命令位置の公開資料なし）

~~~diff
- 00512d10 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00512d50 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00512d10 bytes 483c0090
+ 00512d50 bytes 483c00b0
- 00512d24 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d58:8"]]
- 00512d24 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00512d64 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:158:8"]]
+ 00512d64 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00512d24 bytes 08ad46f9
+ 00512d64 bytes 08ad40f9
- 00512d28 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:938:8"]]
- 00512d28 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00512d68 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d38:8"]]
+ 00512d68 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00512d28 bytes 299d44f9
+ 00512d68 bytes 299d46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4915b7326b42f0a73697a587fa516e6"></a>

### [`00513270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00513/00513270.md) → [`005132b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00513/005132b0.md) _ZN5Botan8X509_CRL12force_decodeEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 42件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00451870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451870.md) [`00459490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md) [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`004a573c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a573c.md)
- 新版 呼出元 0件  · 呼出先 42件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004518b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004518b0.md) [`004594d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`004a577c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a577c.md)

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
    "old": {
      "definition_site": "005132d0",
      "incomplete_value": true,
      "site": "005132d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "005132f0",
      "incomplete_value": true,
      "site": "005132f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "005132f8",
      "incomplete_value": true,
      "site": "005132f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005132f4",
      "READ",
      [
        "storage",
        "00c9acd0",
        null,
        "pointer"
      ]
    ],
    [
      "00513310",
      "DATA",
      [
        "storage",
        "00c675f8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0051331c",
      "READ",
      [
        "storage",
        "00c9a9b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005132f4",
      "READ",
      [
        "storage",
        "00c9b0d0",
        null,
        "pointer"
      ]
    ],
    [
      "00513310",
      "DATA",
      [
        "storage",
        "00c679f8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0051331c",
      "READ",
      [
        "storage",
        "00c9adb0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051354c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00513/00513270.md#insn-0051354c) · [`005135a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00513/00513270.md#insn-005135a0) · [`005135dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00513/00513270.md#insn-005135dc)
- 新版 `0051358c`（命令位置の公開資料なし） · `005135e0`（命令位置の公開資料なし） · `0051361c`（命令位置の公開資料なし）

~~~diff
- 0051354c ["COPY", "register:0:8", ["register:4048:8"]]
- 0051354c ["INT_ADD", "register:40f0:8", ["const:51354c:8", "const:4:8"]]
- 0051354c ["CALLIND", null, ["register:0:8"]]
+ 0051358c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051358c ["INT_ADD", "register:40f0:8", ["const:51358c:8", "const:4:8"]]
+ 0051358c ["CALLIND", null, ["register:0:8"]]
- 0051354c bytes 20013fd6
+ 0051358c bytes 20013fd6
- 005135a0 ["COPY", "register:0:8", ["register:4048:8"]]
- 005135a0 ["INT_ADD", "register:40f0:8", ["const:5135a0:8", "const:4:8"]]
- 005135a0 ["CALLIND", null, ["register:0:8"]]
+ 005135e0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005135e0 ["INT_ADD", "register:40f0:8", ["const:5135e0:8", "const:4:8"]]
+ 005135e0 ["CALLIND", null, ["register:0:8"]]
- 005135a0 bytes 20013fd6
+ 005135e0 bytes 20013fd6
- 005135dc ["COPY", "register:0:8", ["register:4040:8"]]
- 005135dc ["INT_ADD", "register:40f0:8", ["const:5135dc:8", "const:4:8"]]
- 005135dc ["CALLIND", null, ["register:0:8"]]
+ 0051361c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0051361c ["INT_ADD", "register:40f0:8", ["const:51361c:8", "const:4:8"]]
+ 0051361c ["CALLIND", null, ["register:0:8"]]
- 005135dc bytes 00013fd6
+ 0051361c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a8b2cd29497aac4600d9c4588fb5fde"></a>

### [`00513e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00513/00513e10.md) → [`00513e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00513/00513e50.md) _ZNK5Botan8X509_CRL4dataEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59650.md) · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 1件 [`00c59a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59a50.md) · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

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
    "old": {
      "definition_site": "00513e70",
      "incomplete_value": false,
      "site": "00513e78",
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
            "const:dd3:8"
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
    "old": {
      "definition_site": "00513eac",
      "incomplete_value": true,
      "site": "00513eb8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00513ee8",
      "incomplete_value": false,
      "site": "00513ef8",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "00513ea8",
      "incomplete_value": false,
      "site": "00513eb8",
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
      "00513eb0",
      "PARAM",
      [
        "storage",
        "002bedd3",
        null,
        "string"
      ]
    ],
    [
      "00513ee8",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "00513eec",
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
      "00513eb0",
      "PARAM",
      [
        "storage",
        "002bee13",
        null,
        "string"
      ]
    ],
    [
      "00513ee8",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "00513eec",
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

- 旧版 [`00513e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00513/00513e10.md#insn-00513e78) · [`00513eb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00513/00513e10.md#insn-00513eb8) · [`00513e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00513/00513e10.md#insn-00513e64)
- 新版 `00513eb8`（命令位置の公開資料なし） · `00513ef8`（命令位置の公開資料なし） · `00513ea4`（命令位置の公開資料なし）

~~~diff
- 00513e78 ["INT_ADD", "register:40f0:8", ["const:513e78:8", "const:4:8"]]
- 00513e78 ["CALL", null, ["callee:0043ddd8:8"]]
+ 00513eb8 ["INT_ADD", "register:40f0:8", ["const:513eb8:8", "const:4:8"]]
+ 00513eb8 ["CALL", null, ["callee:0043ddd8:8"]]
- 00513e78 bytes c8a7fc97
+ 00513eb8 bytes c8a7fc97
- 00513eb8 ["INT_ADD", "register:40f0:8", ["const:513eb8:8", "const:4:8"]]
- 00513eb8 ["CALL", null, ["callee:00c57f10:8"]]
+ 00513ef8 ["INT_ADD", "register:40f0:8", ["const:513ef8:8", "const:4:8"]]
+ 00513ef8 ["CALL", null, ["callee:00c57f10:8"]]
- 00513eb8 bytes 160f1d94
+ 00513ef8 bytes 06101d94
- 00513e64 ["INT_ADD", "register:40f0:8", ["const:513e64:8", "const:4:8"]]
- 00513e64 ["CALL", null, ["callee:00c57ef0:8"]]
+ 00513ea4 ["INT_ADD", "register:40f0:8", ["const:513ea4:8", "const:4:8"]]
+ 00513ea4 ["CALL", null, ["callee:00c57ef0:8"]]
- 00513e64 bytes 230f1d94
+ 00513ea4 bytes 13101d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5adc9e3955d47907e7838668a4571cc"></a>

### [`00513f8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00513/00513f8c.md) → [`00513fcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00513/00513fcc.md) _ZN5Botan7X509_DNC2ERKNSt6__ndk18multimapINS_3OIDENS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS1_4lessIS3_EENS7_INS1_4pair

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59700.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59b00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59b00.md)

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
    "old": {
      "definition_site": "00513fd4",
      "incomplete_value": true,
      "site": "00513fdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00514008",
      "READ",
      [
        "storage",
        "00c9acd0",
        null,
        "pointer"
      ]
    ],
    [
      "0051401c",
      "DATA",
      [
        "storage",
        "00c675f8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00514008",
      "READ",
      [
        "storage",
        "00c9b0d0",
        null,
        "pointer"
      ]
    ],
    [
      "0051401c",
      "DATA",
      [
        "storage",
        "00c679f8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00513fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00513/00513f8c.md#insn-00513fb0) · [`00513fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00513/00513f8c.md#insn-00513fc8) · [`00514004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00513/00513f8c.md#insn-00514004)
- 新版 `00513ff0`（命令位置の公開資料なし） · `00514008`（命令位置の公開資料なし） · `00514044`（命令位置の公開資料なし）

~~~diff
- 00513fb0 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00513ff0 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00513fb0 bytes 283c00f0
+ 00513ff0 bytes 483c0090
- 00513fc8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cd0:8"]]
- 00513fc8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00514008 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d0:8"]]
+ 00514008 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00513fc8 bytes 086946f9
+ 00514008 bytes 086940f9
- 00514004 ["INT_ADD", "register:40f0:8", ["const:514004:8", "const:4:8"]]
- 00514004 ["CALL", null, ["callee:00c59b00:8"]]
+ 00514044 ["INT_ADD", "register:40f0:8", ["const:514044:8", "const:4:8"]]
+ 00514044 ["CALL", null, ["callee:00c59b00:8"]]
- 00514004 bytes bf151d94
+ 00514044 bytes af161d94
~~~


<a id="compare-6c05cda8198ff2b244ea8c3bcd61635c"></a>

### [`0051422c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/0051422c.md) → [`0051426c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00514/0051426c.md) _ZN5Botan7X509_DNC1ERKNSt6__ndk18multimapINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES8_NS1_4lessIS8_EENS6_INS1_4pairIKS8_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58280.md) [`00c59700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59700.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58680.md) [`00c59b00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59b00.md)

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
    "old": {
      "definition_site": "00514288",
      "incomplete_value": true,
      "site": "00514290",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "005142bc",
      "READ",
      [
        "storage",
        "00c9acd0",
        null,
        "pointer"
      ]
    ],
    [
      "005142d0",
      "DATA",
      [
        "storage",
        "00c675f8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "005142bc",
      "READ",
      [
        "storage",
        "00c9b0d0",
        null,
        "pointer"
      ]
    ],
    [
      "005142d0",
      "DATA",
      [
        "storage",
        "00c679f8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00514264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/0051422c.md#insn-00514264) · [`0051427c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/0051422c.md#insn-0051427c) · [`005142b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/0051422c.md#insn-005142b4)
- 新版 `005142a4`（命令位置の公開資料なし） · `005142bc`（命令位置の公開資料なし） · `005142f4`（命令位置の公開資料なし）

~~~diff
- 00514264 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 005142a4 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00514264 bytes 283c00d0
+ 005142a4 bytes 283c00f0
- 0051427c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cd0:8"]]
- 0051427c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005142bc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d0:8"]]
+ 005142bc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0051427c bytes 086946f9
+ 005142bc bytes 086940f9
- 005142b4 ["INT_ADD", "register:40f0:8", ["const:5142b4:8", "const:4:8"]]
- 005142b4 ["CALL", null, ["callee:00c58680:8"]]
+ 005142f4 ["INT_ADD", "register:40f0:8", ["const:5142f4:8", "const:4:8"]]
+ 005142f4 ["CALL", null, ["callee:00c58680:8"]]
- 005142b4 bytes f30f1d94
+ 005142f4 bytes e3101d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc9858f1465dd20da377329de906c436"></a>

### [`005145cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/005145cc.md) → [`0051460c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00514/0051460c.md) _ZN5Botan7X509_DN16deref_info_fieldERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59770.md) · 呼出先 3件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00441e54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441e54.md)
- 新版 呼出元 1件 [`00c59b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59b70.md) · 呼出先 3件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00441e94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441e94.md)

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
    "old": {
      "definition_site": "00514750",
      "incomplete_value": true,
      "site": "00514750",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2ea:8"
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
    "old": {
      "definition_site": "005147ac",
      "incomplete_value": true,
      "site": "005147ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4a2:8"
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
    "old": {
      "definition_site": "005147a0",
      "incomplete_value": true,
      "site": "005147b0",
      "value": [
        "LOAD",
        "8",
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
      "00514760",
      "PARAM",
      [
        "storage",
        "002b613c",
        null,
        null
      ]
    ],
    [
      "0051477c",
      "READ",
      [
        "storage",
        "002bb2ea",
        null,
        "string"
      ]
    ],
    [
      "005147a0",
      "PARAM",
      [
        "storage",
        "002c1153",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00514760",
      "PARAM",
      [
        "storage",
        "002b617c",
        null,
        null
      ]
    ],
    [
      "0051477c",
      "READ",
      [
        "storage",
        "002bb32a",
        null,
        "string"
      ]
    ],
    [
      "005147a0",
      "PARAM",
      [
        "storage",
        "002c1193",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00514728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/005145cc.md#insn-00514728) · [`00514768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/005145cc.md#insn-00514768) · [`0051477c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/005145cc.md#insn-0051477c)
- 新版 `00514768`（命令位置の公開資料なし） · `005147a8`（命令位置の公開資料なし） · `005147bc`（命令位置の公開資料なし）

~~~diff
- 00514728 ["INT_ADD", "register:40f0:8", ["const:514728:8", "const:4:8"]]
- 00514728 ["CALL", null, ["callee:00441e94:8"]]
+ 00514768 ["INT_ADD", "register:40f0:8", ["const:514768:8", "const:4:8"]]
+ 00514768 ["CALL", null, ["callee:00441e94:8"]]
- 00514728 bytes cbb5fc97
+ 00514768 bytes cbb5fc97
- 00514768 ["INT_ADD", "register:40f0:8", ["const:514768:8", "const:4:8"]]
- 00514768 ["CALL", null, ["callee:00441e94:8"]]
+ 005147a8 ["INT_ADD", "register:40f0:8", ["const:5147a8:8", "const:4:8"]]
+ 005147a8 ["CALL", null, ["callee:00441e94:8"]]
- 00514768 bytes bbb5fc97
+ 005147a8 bytes bbb5fc97
- 0051477c ["INT_ADD", "register:40f0:8", ["const:51477c:8", "const:4:8"]]
- 0051477c ["CALL", null, ["callee:00441e94:8"]]
+ 005147bc ["INT_ADD", "register:40f0:8", ["const:5147bc:8", "const:4:8"]]
+ 005147bc ["CALL", null, ["callee:00441e94:8"]]
- 0051477c bytes b6b5fc97
+ 005147bc bytes b6b5fc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c86f4b8d1fd114f832b81295fadfa627"></a>

### [`00514d64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/00514d64.md) → [`00514da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00514/00514da4.md) _ZNK5Botan7X509_DN11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`004ffa6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ff/004ffa6c.md) [`0052e2f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052e/0052e2f4.md) · 呼出先 11件 [`005150c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/005150c0.md) [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00549628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549628.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`004ffaac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ff/004ffaac.md) [`0052e334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0052e/0052e334.md) · 呼出先 11件 [`00515100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/00515100.md) [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00549668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00549/00549668.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
    "old": {
      "definition_site": "00514df4",
      "incomplete_value": true,
      "site": "00514df4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2ea:8"
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
    "old": {
      "definition_site": "00514e3c",
      "incomplete_value": true,
      "site": "00514e3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4b2:8"
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
    "old": {
      "definition_site": "00514e84",
      "incomplete_value": true,
      "site": "00514e84",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f26:8"
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
      "00514e20",
      "READ",
      [
        "storage",
        "002bb2ea",
        null,
        "string"
      ]
    ],
    [
      "00514e6c",
      "READ",
      [
        "storage",
        "002a64b2",
        null,
        "string"
      ]
    ],
    [
      "00514eb4",
      "READ",
      [
        "storage",
        "002b5f26",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00514e20",
      "READ",
      [
        "storage",
        "002bb32a",
        null,
        "string"
      ]
    ],
    [
      "00514e6c",
      "READ",
      [
        "storage",
        "002a658e",
        null,
        "string"
      ]
    ],
    [
      "00514eb4",
      "READ",
      [
        "storage",
        "002b5f66",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00514ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/00514d64.md#insn-00514ee0) · [`00514d94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/00514d64.md#insn-00514d94) · [`00514da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/00514d64.md#insn-00514da4)
- 新版 `00514f20`（命令位置の公開資料なし） · `00514dd4`（命令位置の公開資料なし） · `00514de4`（命令位置の公開資料なし）

~~~diff
- 00514ee0 ["INT_ADD", "register:40f0:8", ["const:514ee0:8", "const:4:8"]]
- 00514ee0 ["CALL", null, ["callee:00515100:8"]]
+ 00514f20 ["INT_ADD", "register:40f0:8", ["const:514f20:8", "const:4:8"]]
+ 00514f20 ["CALL", null, ["callee:00515100:8"]]
- 00514ee0 bytes 78000094
+ 00514f20 bytes 78000094
- 00514d94 ["INT_ADD", "register:40f0:8", ["const:514d94:8", "const:4:8"]]
- 00514d94 ["CALL", null, ["callee:00c59a20:8"]]
+ 00514dd4 ["INT_ADD", "register:40f0:8", ["const:514dd4:8", "const:4:8"]]
+ 00514dd4 ["CALL", null, ["callee:00c59a20:8"]]
- 00514d94 bytes 23121d94
+ 00514dd4 bytes 13131d94
- 00514da4 ["INT_ADD", "register:40f0:8", ["const:514da4:8", "const:4:8"]]
- 00514da4 ["CALL", null, ["callee:00c586b0:8"]]
+ 00514de4 ["INT_ADD", "register:40f0:8", ["const:514de4:8", "const:4:8"]]
+ 00514de4 ["CALL", null, ["callee:00c586b0:8"]]
- 00514da4 bytes 430d1d94
+ 00514de4 bytes 330e1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3514a4cf7005b6a0eaa2f71b84586f4b"></a>

### [`00515684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515684.md) → [`005156c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/005156c4.md) _ZN5Botan10Extensions15create_extn_objERKNS_3OIDEbRKNSt6__ndk16vectorIhNS4_9allocatorIhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c599e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599e0.md) · 呼出先 27件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`00503bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503bb4.md) [`00516620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516620.md) [`005166c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/005166c8.md) [`00516770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516770.md)
- 新版 呼出元 1件 [`00c59de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59de0.md) · 呼出先 27件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`00503bf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00503/00503bf4.md) [`00516660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516660.md) [`00516708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516708.md) [`005167b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/005167b0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
      "definition_site": "005156e8",
      "incomplete_value": true,
      "site": "005156e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ccb:8"
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
    "old": {
      "definition_site": "005157b8",
      "incomplete_value": true,
      "site": "005157b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:79d:8"
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
    "old": {
      "definition_site": "005158d8",
      "incomplete_value": true,
      "site": "005158d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2e0:8"
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
      "00515718",
      "READ",
      [
        "storage",
        "002b4ccb",
        null,
        "string"
      ]
    ],
    [
      "005157c0",
      "READ",
      [
        "storage",
        "00c9adb0",
        null,
        "pointer"
      ]
    ],
    [
      "005157cc",
      "DATA",
      [
        "storage",
        "00c67628",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "00515718",
      "READ",
      [
        "storage",
        "002b4d0b",
        null,
        "string"
      ]
    ],
    [
      "005157c0",
      "READ",
      [
        "storage",
        "00c9b1b0",
        null,
        "pointer"
      ]
    ],
    [
      "005157cc",
      "DATA",
      [
        "storage",
        "00c67a28",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00515778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515684.md#insn-00515778) · [`005156c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515684.md#insn-005156c8) · [`005156d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515684.md#insn-005156d0)
- 新版 `005157b8`（命令位置の公開資料なし） · `00515708`（命令位置の公開資料なし） · `00515710`（命令位置の公開資料なし）

~~~diff
- 00515778 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 005157b8 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00515778 bytes 283c00b0
+ 005157b8 bytes 283c00d0
- 005156c8 ["INT_ADD", "register:40f0:8", ["const:5156c8:8", "const:4:8"]]
- 005156c8 ["CALL", null, ["callee:00c58800:8"]]
+ 00515708 ["INT_ADD", "register:40f0:8", ["const:515708:8", "const:4:8"]]
+ 00515708 ["CALL", null, ["callee:00c58800:8"]]
- 005156c8 bytes 4e0b1d94
+ 00515708 bytes 3e0c1d94
- 005156d0 ["COPY", "tmp:0:8", ["const:ccb:8"]]
- 005156d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005156d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005156d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00515710 ["COPY", "tmp:0:8", ["const:d0b:8"]]
+ 00515710 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00515710 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00515710 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005156d0 bytes 292d3391
+ 00515710 bytes 292d3491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5d84bce95dc20ef785b417850b03ac1"></a>

### [`00516620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516620.md) → [`00516660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00516/00516660.md) FUN_00516660

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00515684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515684.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58290.md)
- 新版 呼出元 1件 [`005156c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00515/005156c4.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md)

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
    "old": {
      "definition_site": "00516658",
      "incomplete_value": true,
      "site": "00516658",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:36:8"
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
      "00516688",
      "READ",
      [
        "storage",
        "002a4036",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00516688",
      "READ",
      [
        "storage",
        "002a4103",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051663c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516620.md#insn-0051663c) · [`00516664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516620.md#insn-00516664) · [`00516674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516620.md#insn-00516674)
- 新版 `0051667c`（命令位置の公開資料なし） · `005166a4`（命令位置の公開資料なし） · `005166b4`（命令位置の公開資料なし）

~~~diff
- 0051663c ["COPY", "tmp:0:8", ["const:36:8"]]
- 0051663c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0051663c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0051663c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0051667c ["COPY", "tmp:0:8", ["const:103:8"]]
+ 0051667c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0051667c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0051667c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0051663c bytes 29d90091
+ 0051667c bytes 290d0491
- 00516664 ["INT_ADD", "register:40f0:8", ["const:516664:8", "const:4:8"]]
- 00516664 ["CALL", null, ["callee:00c58690:8"]]
+ 005166a4 ["INT_ADD", "register:40f0:8", ["const:5166a4:8", "const:4:8"]]
+ 005166a4 ["CALL", null, ["callee:00c58690:8"]]
- 00516664 bytes 0b071d94
+ 005166a4 bytes fb071d94
- 00516674 ["INT_ADD", "register:40f0:8", ["const:516674:8", "const:4:8"]]
- 00516674 ["CALL", null, ["callee:00c57eb0:8"]]
+ 005166b4 ["INT_ADD", "register:40f0:8", ["const:5166b4:8", "const:4:8"]]
+ 005166b4 ["CALL", null, ["callee:00c57eb0:8"]]
- 00516674 bytes 0f051d94
+ 005166b4 bytes ff051d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

