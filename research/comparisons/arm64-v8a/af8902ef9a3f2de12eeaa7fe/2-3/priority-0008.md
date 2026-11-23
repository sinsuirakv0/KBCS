# v16.0.0 → v16.0.1 · 最優先の変更候補 (8)

[一覧の目次](README.md)

<a id="compare-78dfe7304538e0d3960070c1b9128a8b"></a>

### [`004b7acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b7acc.md) → [`004b7b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b7b0c.md) _ZN5Botan7Charset10char2digitEc

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c586b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c586b0.md) · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`00c58ab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58ab0.md) · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
      "definition_site": "004b7b74",
      "incomplete_value": false,
      "site": "004b7b7c",
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
            "const:407:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b7b34",
      "incomplete_value": false,
      "site": "004b7b3c",
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
            "const:3c7:8"
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
      "definition_site": "004b7bb0",
      "incomplete_value": true,
      "site": "004b7bbc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
      "definition_site": "004b7b70",
      "incomplete_value": true,
      "site": "004b7b7c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
      "definition_site": "004b7bac",
      "incomplete_value": false,
      "site": "004b7bbc",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004b7b6c",
      "incomplete_value": false,
      "site": "004b7b7c",
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
      "004b7b74",
      "PARAM",
      [
        "storage",
        "002bb3c7",
        null,
        "string"
      ]
    ],
    [
      "004b7bac",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004b7bb0",
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
      "004b7b74",
      "PARAM",
      [
        "storage",
        "002bb407",
        null,
        "string"
      ]
    ],
    [
      "004b7bac",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004b7bb0",
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

- 旧版 [`004b7b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b7acc.md#insn-004b7b3c) · [`004b7b7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b7acc.md#insn-004b7b7c) · [`004b7b28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b7acc.md#insn-004b7b28)
- 新版 `004b7b7c`（命令位置の公開資料なし） · `004b7bbc`（命令位置の公開資料なし） · `004b7b68`（命令位置の公開資料なし）

~~~diff
- 004b7b3c ["INT_ADD", "register:40f0:8", ["const:4b7b3c:8", "const:4:8"]]
- 004b7b3c ["CALL", null, ["callee:0043ddd8:8"]]
+ 004b7b7c ["INT_ADD", "register:40f0:8", ["const:4b7b7c:8", "const:4:8"]]
+ 004b7b7c ["CALL", null, ["callee:0043ddd8:8"]]
- 004b7b3c bytes 9718fe97
+ 004b7b7c bytes 9718fe97
- 004b7b7c ["INT_ADD", "register:40f0:8", ["const:4b7b7c:8", "const:4:8"]]
- 004b7b7c ["CALL", null, ["callee:00c57f10:8"]]
+ 004b7bbc ["INT_ADD", "register:40f0:8", ["const:4b7bbc:8", "const:4:8"]]
+ 004b7bbc ["CALL", null, ["callee:00c57f10:8"]]
- 004b7b7c bytes e57f1e94
+ 004b7bbc bytes d5801e94
- 004b7b28 ["INT_ADD", "register:40f0:8", ["const:4b7b28:8", "const:4:8"]]
- 004b7b28 ["CALL", null, ["callee:00c57ef0:8"]]
+ 004b7b68 ["INT_ADD", "register:40f0:8", ["const:4b7b68:8", "const:4:8"]]
+ 004b7b68 ["CALL", null, ["callee:00c57ef0:8"]]
- 004b7b28 bytes f27f1e94
+ 004b7b68 bytes e2801e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db27f7f249f2c7cf0d80dc55b09d4191"></a>

### [`004b7bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b7bd0.md) → [`004b7c10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b7c10.md) _ZN5Botan6BigIntmLERKS0_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c586c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c586c0.md) · 呼出先 10件 [`004b8810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8810.md) [`004b90a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b90a0.md) [`004b91a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b91a0.md) [`004d6e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d6/004d6e28.md) [`005408e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005408e0.md)
- 新版 呼出元 1件 [`00c58ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58ac0.md) · 呼出先 10件 [`004b8850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8850.md) [`004b90e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b9/004b90e0.md) [`004b91e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b9/004b91e0.md) [`004d6e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d6/004d6e68.md) [`00540920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540920.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.21% / 新版 98.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b7f28",
      "incomplete_value": true,
      "site": "004b7f28",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004b7ee8",
      "incomplete_value": true,
      "site": "004b7ee8",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 10,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b7f54",
      "incomplete_value": true,
      "site": "004b7f54",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004b7f14",
      "incomplete_value": true,
      "site": "004b7f14",
      "value": [
        "LOAD",
        "8",
        [
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
      "004b7f18",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004b7f44",
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
      "004b7f18",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004b7f44",
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

- 旧版 [`004b7ee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b7bd0.md#insn-004b7ee8) · [`004b7f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b7bd0.md#insn-004b7f14) · [`004b7d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b7bd0.md#insn-004b7d04)
- 新版 `004b7f28`（命令位置の公開資料なし） · `004b7f54`（命令位置の公開資料なし） · `004b7d44`（命令位置の公開資料なし）

~~~diff
- 004b7ee8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b7ee8 ["INT_ADD", "register:40f0:8", ["const:4b7ee8:8", "const:4:8"]]
- 004b7ee8 ["CALLIND", null, ["register:0:8"]]
+ 004b7f28 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b7f28 ["INT_ADD", "register:40f0:8", ["const:4b7f28:8", "const:4:8"]]
+ 004b7f28 ["CALLIND", null, ["register:0:8"]]
- 004b7ee8 bytes 20013fd6
+ 004b7f28 bytes 20013fd6
- 004b7f14 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b7f14 ["INT_ADD", "register:40f0:8", ["const:4b7f14:8", "const:4:8"]]
- 004b7f14 ["CALLIND", null, ["register:0:8"]]
+ 004b7f54 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b7f54 ["INT_ADD", "register:40f0:8", ["const:4b7f54:8", "const:4:8"]]
+ 004b7f54 ["CALLIND", null, ["register:0:8"]]
- 004b7f14 bytes 20013fd6
+ 004b7f54 bytes 20013fd6
- 004b7d04 ["INT_ADD", "register:40f0:8", ["const:4b7d04:8", "const:4:8"]]
- 004b7d04 ["CALL", null, ["callee:00540920:8"]]
+ 004b7d44 ["INT_ADD", "register:40f0:8", ["const:4b7d44:8", "const:4:8"]]
+ 004b7d44 ["CALL", null, ["callee:00540920:8"]]
- 004b7d04 bytes f7220294
+ 004b7d44 bytes f7220294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5195f0a8bc003c4b1f9090e8b1e16510"></a>

### [`004b7f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b7f88.md) → [`004b7fc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b7fc8.md) _ZN5Botan6BigIntpLERKS0_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c586d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c586d0.md) · 呼出先 10件 [`004b8774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8774.md) [`004b8810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8810.md) [`004b890c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b890c.md) [`004b8b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8b2c.md) [`004d6b84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d6/004d6b84.md)
- 新版 呼出元 1件 [`00c58ad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58ad0.md) · 呼出先 10件 [`004b87b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b87b4.md) [`004b8850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8850.md) [`004b894c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b894c.md) [`004b8b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8b6c.md) [`004d6bc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d6/004d6bc4.md)

変更の種類 call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.03% / 新版 98.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b81e8",
      "incomplete_value": true,
      "site": "004b81e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004b81a8",
      "incomplete_value": true,
      "site": "004b81a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004b81dc",
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
      "004b81dc",
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

- 旧版 [`004b81a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b7f88.md#insn-004b81a8) · [`004b8044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b7f88.md#insn-004b8044) · [`004b8080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b7f88.md#insn-004b8080)
- 新版 `004b81e8`（命令位置の公開資料なし） · `004b8084`（命令位置の公開資料なし） · `004b80c0`（命令位置の公開資料なし）

~~~diff
- 004b81a8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b81a8 ["INT_ADD", "register:40f0:8", ["const:4b81a8:8", "const:4:8"]]
- 004b81a8 ["CALLIND", null, ["register:0:8"]]
+ 004b81e8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b81e8 ["INT_ADD", "register:40f0:8", ["const:4b81e8:8", "const:4:8"]]
+ 004b81e8 ["CALLIND", null, ["register:0:8"]]
- 004b81a8 bytes 20013fd6
+ 004b81e8 bytes 20013fd6
- 004b8044 ["INT_ADD", "register:40f0:8", ["const:4b8044:8", "const:4:8"]]
- 004b8044 ["CALL", null, ["callee:00540920:8"]]
+ 004b8084 ["INT_ADD", "register:40f0:8", ["const:4b8084:8", "const:4:8"]]
+ 004b8084 ["CALL", null, ["callee:00540920:8"]]
- 004b8044 bytes 27220294
+ 004b8084 bytes 27220294
- 004b8080 ["INT_ADD", "register:40f0:8", ["const:4b8080:8", "const:4:8"]]
- 004b8080 ["CALL", null, ["callee:004d6bc4:8"]]
+ 004b80c0 ["INT_ADD", "register:40f0:8", ["const:4b80c0:8", "const:4:8"]]
+ 004b80c0 ["CALL", null, ["callee:004d6bc4:8"]]
- 004b8080 bytes c17a0094
+ 004b80c0 bytes c17a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-137f1aec00deec3990c230e189b10336"></a>

### [`004b8210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8210.md) → [`004b8250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8250.md) _ZN5BotanlsERNSt6__ndk113basic_ostreamIcNS0_11char_traitsIcEEEERKNS_6BigIntE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 14件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

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
    "old": {
      "definition_site": "004b82a8",
      "incomplete_value": true,
      "site": "004b82a8",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "004b82f8",
      "incomplete_value": true,
      "site": "004b82f8",
      "value": [
        "LOAD",
        "8",
        [
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
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "004b830c",
      "incomplete_value": false,
      "site": "004b8318",
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
            "const:f1f:8"
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
      "004b82d8",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004b8328",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004b834c",
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
      "004b82d8",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004b8328",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004b834c",
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

- 旧版 [`004b82a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8210.md#insn-004b82a8) · [`004b82e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8210.md#insn-004b82e8) · [`004b82f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8210.md#insn-004b82f8)
- 新版 `004b82e8`（命令位置の公開資料なし） · `004b8328`（命令位置の公開資料なし） · `004b8338`（命令位置の公開資料なし）

~~~diff
- 004b82a8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b82a8 ["INT_ADD", "register:40f0:8", ["const:4b82a8:8", "const:4:8"]]
- 004b82a8 ["CALLIND", null, ["register:0:8"]]
+ 004b82e8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b82e8 ["INT_ADD", "register:40f0:8", ["const:4b82e8:8", "const:4:8"]]
+ 004b82e8 ["CALLIND", null, ["register:0:8"]]
- 004b82a8 bytes 20013fd6
+ 004b82e8 bytes 20013fd6
- 004b82e8 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:338:8"]]
- 004b82e8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004b8328 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:738:8"]]
+ 004b8328 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004b82e8 bytes 299f41f9
+ 004b8328 bytes 299f43f9
- 004b82f8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b82f8 ["INT_ADD", "register:40f0:8", ["const:4b82f8:8", "const:4:8"]]
- 004b82f8 ["CALLIND", null, ["register:0:8"]]
+ 004b8338 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b8338 ["INT_ADD", "register:40f0:8", ["const:4b8338:8", "const:4:8"]]
+ 004b8338 ["CALLIND", null, ["register:0:8"]]
- 004b82f8 bytes 20013fd6
+ 004b8338 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71e5d67cca701994c31545c2fff37264"></a>

### [`004b8500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8500.md) → [`004b8540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8540.md) _ZN5BotanrsERNSt6__ndk113basic_istreamIcNS0_11char_traitsIcEEEERNS_6BigIntE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`005434e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/005434e8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00543528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543528.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

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
    "old": {
      "definition_site": "004b8550",
      "incomplete_value": true,
      "site": "004b8554",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9a000:8"
              ],
              [
                "leaf",
                "const:830:8"
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
    "old": {
      "definition_site": "004b8610",
      "incomplete_value": true,
      "site": "004b8610",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "004b8668",
      "incomplete_value": false,
      "site": "004b8670",
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
            "const:4cb:8"
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
      "004b8590",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "004b8590",
      "PARAM",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "004b8640",
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
      "004b8590",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      "004b8590",
      "PARAM",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "004b8640",
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

- 旧版 [`004b8554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8500.md#insn-004b8554) · [`004b8610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8500.md#insn-004b8610) · [`004b8670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8500.md#insn-004b8670)
- 新版 `004b8594`（命令位置の公開資料なし） · `004b8650`（命令位置の公開資料なし） · `004b86b0`（命令位置の公開資料なし）

~~~diff
- 004b8554 ["INT_ADD", "register:40f0:8", ["const:4b8554:8", "const:4:8"]]
- 004b8554 ["CALL", null, ["callee:00c58280:8"]]
+ 004b8594 ["INT_ADD", "register:40f0:8", ["const:4b8594:8", "const:4:8"]]
+ 004b8594 ["CALL", null, ["callee:00c58280:8"]]
- 004b8554 bytes 4b7e1e94
+ 004b8594 bytes 3b7f1e94
- 004b8610 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b8610 ["INT_ADD", "register:40f0:8", ["const:4b8610:8", "const:4:8"]]
- 004b8610 ["CALLIND", null, ["register:0:8"]]
+ 004b8650 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b8650 ["INT_ADD", "register:40f0:8", ["const:4b8650:8", "const:4:8"]]
+ 004b8650 ["CALLIND", null, ["register:0:8"]]
- 004b8610 bytes 20013fd6
+ 004b8650 bytes 20013fd6
- 004b8670 ["INT_ADD", "register:40f0:8", ["const:4b8670:8", "const:4:8"]]
- 004b8670 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004b86b0 ["INT_ADD", "register:40f0:8", ["const:4b86b0:8", "const:4:8"]]
+ 004b86b0 ["CALL", null, ["callee:0043ddd8:8"]]
- 004b8670 bytes ca15fe97
+ 004b86b0 bytes ca15fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-218992216b118c024ae47fd21e191a98"></a>

### [`004b8810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8810.md) → [`004b8850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8850.md) FUN_004b8850

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 8件 [`004a1314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a1/004a1314.md) [`004b7bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b7bd0.md) [`004b7f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b7f88.md) [`004ba1b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ba/004ba1b4.md) [`004db524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004db524.md) · 呼出先 7件 [`005362f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/005362f4.md) [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 8件 [`004a1354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1354.md) [`004b7c10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b7c10.md) [`004b7fc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b7fc8.md) [`004ba1f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ba/004ba1f4.md) [`004db564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004db/004db564.md) · 呼出先 7件 [`00536334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536334.md) [`00c37ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ba4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
    "old": {
      "definition_site": "004b88d8",
      "incomplete_value": true,
      "site": "004b88e0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
    "old": {
      "definition_site": "004b88dc",
      "incomplete_value": true,
      "site": "004b88e0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
      "004b8918",
      "READ",
      [
        "storage",
        "00c9a9e8",
        null,
        "pointer"
      ]
    ],
    [
      "004b8918",
      "PARAM",
      [
        "storage",
        "00c96298",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "004b891c",
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
      "004b8918",
      "READ",
      [
        "storage",
        "00c9ade8",
        null,
        "pointer"
      ]
    ],
    [
      "004b8918",
      "PARAM",
      [
        "storage",
        "00c96698",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "004b891c",
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

- 旧版 [`004b88e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8810.md#insn-004b88e0) · [`004b885c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8810.md#insn-004b885c) · [`004b88a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8810.md#insn-004b88a8)
- 新版 `004b8920`（命令位置の公開資料なし） · `004b889c`（命令位置の公開資料なし） · `004b88e8`（命令位置の公開資料なし）

~~~diff
- 004b88e0 ["INT_ADD", "register:40f0:8", ["const:4b88e0:8", "const:4:8"]]
- 004b88e0 ["CALL", null, ["callee:00c57f10:8"]]
+ 004b8920 ["INT_ADD", "register:40f0:8", ["const:4b8920:8", "const:4:8"]]
+ 004b8920 ["CALL", null, ["callee:00c57f10:8"]]
- 004b88e0 bytes 8c7c1e94
+ 004b8920 bytes 7c7d1e94
- 004b885c ["INT_ADD", "register:40f0:8", ["const:4b885c:8", "const:4:8"]]
- 004b885c ["CALL", null, ["callee:00c58a30:8"]]
+ 004b889c ["INT_ADD", "register:40f0:8", ["const:4b889c:8", "const:4:8"]]
+ 004b889c ["CALL", null, ["callee:00c58a30:8"]]
- 004b885c bytes 757f1e94
+ 004b889c bytes 65801e94
- 004b88a8 ["INT_ADD", "register:40f0:8", ["const:4b88a8:8", "const:4:8"]]
- 004b88a8 ["CALL", null, ["callee:00536334:8"]]
+ 004b88e8 ["INT_ADD", "register:40f0:8", ["const:4b88e8:8", "const:4:8"]]
+ 004b88e8 ["CALL", null, ["callee:00536334:8"]]
- 004b88a8 bytes 93f60194
+ 004b88e8 bytes 93f60194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fddb046386a1eb9ebea9359b64b687cd"></a>

### [`004b890c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b890c.md) → [`004b894c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b894c.md) FUN_004b894c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`004b7f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b7f88.md) [`004b9d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b9d78.md) [`004b9f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b9f00.md) [`004d7350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7350.md) [`004d78c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d78c8.md) · 呼出先 1件 [`00c58250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58250.md)
- 新版 呼出元 5件 [`004b7fc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b7fc8.md) [`004b9db8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b9/004b9db8.md) [`004b9f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b9/004b9f40.md) [`004d7390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d7/004d7390.md) [`004d7908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d7/004d7908.md) · 呼出先 1件 [`00c58650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58650.md)

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
    "old": {
      "definition_site": "004b8ab4",
      "incomplete_value": false,
      "site": "004b8ad4",
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
    "old": {
      "definition_site": "004b8abc",
      "incomplete_value": false,
      "site": "004b8ad4",
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
    "old": {
      "definition_site": "004b8ac4",
      "incomplete_value": false,
      "site": "004b8ad4",
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
            "const:d58:8"
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
      "004b8af4",
      "PARAM",
      [
        "storage",
        "002a6504",
        null,
        "string"
      ]
    ],
    [
      "004b8afc",
      "PARAM",
      [
        "storage",
        "002b606d",
        null,
        "string"
      ]
    ],
    [
      "004b8b04",
      "PARAM",
      [
        "storage",
        "002b4d58",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004b8af4",
      "PARAM",
      [
        "storage",
        "002a65e0",
        null,
        "string"
      ]
    ],
    [
      "004b8afc",
      "PARAM",
      [
        "storage",
        "002b60ad",
        null,
        "string"
      ]
    ],
    [
      "004b8b04",
      "PARAM",
      [
        "storage",
        "002b4d98",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b8ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b890c.md#insn-004b8ad4) · [`004b8ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b890c.md#insn-004b8ab4) · [`004b8abc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b890c.md#insn-004b8abc)
- 新版 `004b8b14`（命令位置の公開資料なし） · `004b8af4`（命令位置の公開資料なし） · `004b8afc`（命令位置の公開資料なし）

~~~diff
- 004b8ad4 ["INT_ADD", "register:40f0:8", ["const:4b8ad4:8", "const:4:8"]]
- 004b8ad4 ["CALL", null, ["callee:00c58650:8"]]
+ 004b8b14 ["INT_ADD", "register:40f0:8", ["const:4b8b14:8", "const:4:8"]]
+ 004b8b14 ["CALL", null, ["callee:00c58650:8"]]
- 004b8ad4 bytes df7d1e94
+ 004b8b14 bytes cf7e1e94
- 004b8ab4 ["COPY", "tmp:0:8", ["const:504:8"]]
- 004b8ab4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004b8ab4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004b8ab4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004b8af4 ["COPY", "tmp:0:8", ["const:5e0:8"]]
+ 004b8af4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004b8af4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004b8af4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004b8ab4 bytes 00101491
+ 004b8af4 bytes 00801791
- 004b8abc ["COPY", "tmp:0:8", ["const:6d:8"]]
- 004b8abc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004b8abc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004b8abc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004b8afc ["COPY", "tmp:0:8", ["const:ad:8"]]
+ 004b8afc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004b8afc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004b8afc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004b8abc bytes 21b40191
+ 004b8afc bytes 21b40291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-401cd1562d0cbdb0ec5dfff63045220f"></a>

### [`004b8b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8b2c.md) → [`004b8b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8b6c.md) FUN_004b8b6c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`004b7f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b7f88.md) [`004b8cd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8cd4.md) [`004d7350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7350.md) [`004d78c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d78c8.md) · 呼出先 1件 [`00c58250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58250.md)
- 新版 呼出元 4件 [`004b7fc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b7fc8.md) [`004b8d14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8d14.md) [`004d7390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d7/004d7390.md) [`004d7908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d7/004d7908.md) · 呼出先 1件 [`00c58650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58650.md)

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
    "old": {
      "definition_site": "004b8cb0",
      "incomplete_value": false,
      "site": "004b8cd0",
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
    "old": {
      "definition_site": "004b8cb8",
      "incomplete_value": false,
      "site": "004b8cd0",
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
    "old": {
      "definition_site": "004b8cc0",
      "incomplete_value": false,
      "site": "004b8cd0",
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
            "const:951:8"
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
      "004b8cf0",
      "PARAM",
      [
        "storage",
        "002a6504",
        null,
        "string"
      ]
    ],
    [
      "004b8cf8",
      "PARAM",
      [
        "storage",
        "002b606d",
        null,
        "string"
      ]
    ],
    [
      "004b8d00",
      "PARAM",
      [
        "storage",
        "002af951",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004b8cf0",
      "PARAM",
      [
        "storage",
        "002a65e0",
        null,
        "string"
      ]
    ],
    [
      "004b8cf8",
      "PARAM",
      [
        "storage",
        "002b60ad",
        null,
        "string"
      ]
    ],
    [
      "004b8d00",
      "PARAM",
      [
        "storage",
        "002af991",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b8cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8b2c.md#insn-004b8cd0) · [`004b8cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8b2c.md#insn-004b8cb0) · [`004b8cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8b2c.md#insn-004b8cb8)
- 新版 `004b8d10`（命令位置の公開資料なし） · `004b8cf0`（命令位置の公開資料なし） · `004b8cf8`（命令位置の公開資料なし）

~~~diff
- 004b8cd0 ["INT_ADD", "register:40f0:8", ["const:4b8cd0:8", "const:4:8"]]
- 004b8cd0 ["CALL", null, ["callee:00c58650:8"]]
+ 004b8d10 ["INT_ADD", "register:40f0:8", ["const:4b8d10:8", "const:4:8"]]
+ 004b8d10 ["CALL", null, ["callee:00c58650:8"]]
- 004b8cd0 bytes 607d1e94
+ 004b8d10 bytes 507e1e94
- 004b8cb0 ["COPY", "tmp:0:8", ["const:504:8"]]
- 004b8cb0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004b8cb0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004b8cb0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004b8cf0 ["COPY", "tmp:0:8", ["const:5e0:8"]]
+ 004b8cf0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004b8cf0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004b8cf0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004b8cb0 bytes 00101491
+ 004b8cf0 bytes 00801791
- 004b8cb8 ["COPY", "tmp:0:8", ["const:6d:8"]]
- 004b8cb8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004b8cb8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004b8cb8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004b8cf8 ["COPY", "tmp:0:8", ["const:ad:8"]]
+ 004b8cf8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004b8cf8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004b8cf8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004b8cb8 bytes 21b40191
+ 004b8cf8 bytes 21b40291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49ed408bbac291f418f5bedc9c32d233"></a>

### [`004b8cd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8cd4.md) → [`004b8d14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8d14.md) _ZN5Botan6BigIntmIERKS0_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58840.md) · 呼出先 6件 [`004b8774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8774.md) [`004b8b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8b2c.md) [`004b8f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8f14.md) [`004d6b84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d6/004d6b84.md) [`005408e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005408e0.md)
- 新版 呼出元 1件 [`00c58c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58c40.md) · 呼出先 6件 [`004b87b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b87b4.md) [`004b8b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8b6c.md) [`004b8f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8f54.md) [`004d6bc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d6/004d6bc4.md) [`00540920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540920.md)

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
      "site": "004b8e44",
      "value": [
        "leaf",
        "ram:4b8f54:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004b8e04",
      "value": [
        "leaf",
        "ram:4b8f14:8"
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
      "004b8e44",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "004b8f14"
      ]
    ]
  ],
  "added": [
    [
      "004b8e44",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "004b8f54"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b8e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8cd4.md#insn-004b8e04) · [`004b8d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8cd4.md#insn-004b8d54) · [`004b8d94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8cd4.md#insn-004b8d94)
- 新版 `004b8e44`（命令位置の公開資料なし） · `004b8d94`（命令位置の公開資料なし） · `004b8dd4`（命令位置の公開資料なし）

~~~diff
- 004b8e04 ["INT_ADD", "register:40f0:8", ["const:4b8e04:8", "const:4:8"]]
- 004b8e04 ["CALL", null, ["ram:4b8f14:8"]]
+ 004b8e44 ["INT_ADD", "register:40f0:8", ["const:4b8e44:8", "const:4:8"]]
+ 004b8e44 ["CALL", null, ["ram:4b8f54:8"]]
- 004b8e04 bytes 44000094
+ 004b8e44 bytes 44000094
- 004b8d54 ["INT_ADD", "register:40f0:8", ["const:4b8d54:8", "const:4:8"]]
- 004b8d54 ["CALL", null, ["callee:004b87b4:8"]]
+ 004b8d94 ["INT_ADD", "register:40f0:8", ["const:4b8d94:8", "const:4:8"]]
+ 004b8d94 ["CALL", null, ["callee:004b87b4:8"]]
- 004b8d54 bytes 88feff97
+ 004b8d94 bytes 88feff97
- 004b8d94 ["INT_ADD", "register:40f0:8", ["const:4b8d94:8", "const:4:8"]]
- 004b8d94 ["CALL", null, ["callee:00540920:8"]]
+ 004b8dd4 ["INT_ADD", "register:40f0:8", ["const:4b8dd4:8", "const:4:8"]]
+ 004b8dd4 ["CALL", null, ["callee:00540920:8"]]
- 004b8d94 bytes d31e0294
+ 004b8dd4 bytes d31e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49a742fc204a63f29cfc4f4b5607bb43"></a>

### [`004b963c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b963c.md) → [`004b967c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b9/004b967c.md) _ZN5BotanrmERKNS_6BigIntES2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c588a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c588a0.md) · 呼出先 11件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`00c58ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58ca0.md) · 呼出先 11件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
    "old": {
      "definition_site": "004b96f0",
      "incomplete_value": true,
      "site": "004b96f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "004b9714",
      "incomplete_value": true,
      "site": "004b9718",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
      "definition_site": "004b9750",
      "incomplete_value": false,
      "site": "004b9758",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004b9710",
      "incomplete_value": false,
      "site": "004b9718",
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
      "004b971c",
      "READ",
      [
        "storage",
        "00c9aa00",
        null,
        "pointer"
      ]
    ],
    [
      "004b9734",
      "DATA",
      [
        "storage",
        "00c69860",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004b9750",
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
      "004b971c",
      "READ",
      [
        "storage",
        "00c9ae00",
        null,
        "pointer"
      ]
    ],
    [
      "004b9734",
      "DATA",
      [
        "storage",
        "00c69c60",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004b9750",
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

- 旧版 [`004b9718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b963c.md#insn-004b9718) · [`004b97a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b963c.md#insn-004b97a0) · [`004b9814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b963c.md#insn-004b9814)
- 新版 `004b9758`（命令位置の公開資料なし） · `004b97e0`（命令位置の公開資料なし） · `004b9854`（命令位置の公開資料なし）

~~~diff
- 004b9718 ["INT_ADD", "register:40f0:8", ["const:4b9718:8", "const:4:8"]]
- 004b9718 ["CALL", null, ["callee:00c57f10:8"]]
+ 004b9758 ["INT_ADD", "register:40f0:8", ["const:4b9758:8", "const:4:8"]]
+ 004b9758 ["CALL", null, ["callee:00c57f10:8"]]
- 004b9718 bytes fe781e94
+ 004b9758 bytes ee791e94
- 004b97a0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b97a0 ["INT_ADD", "register:40f0:8", ["const:4b97a0:8", "const:4:8"]]
- 004b97a0 ["CALLIND", null, ["register:0:8"]]
+ 004b97e0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b97e0 ["INT_ADD", "register:40f0:8", ["const:4b97e0:8", "const:4:8"]]
+ 004b97e0 ["CALLIND", null, ["register:0:8"]]
- 004b97a0 bytes 20013fd6
+ 004b97e0 bytes 20013fd6
- 004b9814 ["INT_ADD", "register:40f0:8", ["const:4b9814:8", "const:4:8"]]
- 004b9814 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004b9854 ["INT_ADD", "register:40f0:8", ["const:4b9854:8", "const:4:8"]]
+ 004b9854 ["CALL", null, ["callee:0043ddd8:8"]]
- 004b9814 bytes 6111fe97
+ 004b9854 bytes 6111fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18297fb86f9074dccf46c1fe2a840b95"></a>

### [`004b98bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b98bc.md) → [`004b98fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b9/004b98fc.md) _ZN5Botan6BigIntrMEj

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`004bbb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bbb2c.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`005408e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005408e0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`004bbb6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bbb6c.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00540920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540920.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
    "old": {
      "definition_site": "004b9ab8",
      "incomplete_value": true,
      "site": "004b9abc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "004b9ac0",
      "incomplete_value": true,
      "site": "004b9ac4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b9aec",
      "incomplete_value": false,
      "site": "004b9b04",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004b9aac",
      "incomplete_value": false,
      "site": "004b9ac4",
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
      "004b9ad8",
      "READ",
      [
        "storage",
        "00c9aa00",
        null,
        "pointer"
      ]
    ],
    [
      "004b9aec",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004b9afc",
      "DATA",
      [
        "storage",
        "00c69860",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004b9ad8",
      "READ",
      [
        "storage",
        "00c9ae00",
        null,
        "pointer"
      ]
    ],
    [
      "004b9aec",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004b9afc",
      "DATA",
      [
        "storage",
        "00c69c60",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b9ac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b98bc.md#insn-004b9ac4) · [`004b9910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b98bc.md#insn-004b9910) · [`004b9964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b98bc.md#insn-004b9964)
- 新版 `004b9b04`（命令位置の公開資料なし） · `004b9950`（命令位置の公開資料なし） · `004b99a4`（命令位置の公開資料なし）

~~~diff
- 004b9ac4 ["INT_ADD", "register:40f0:8", ["const:4b9ac4:8", "const:4:8"]]
- 004b9ac4 ["CALL", null, ["callee:00c57f10:8"]]
+ 004b9b04 ["INT_ADD", "register:40f0:8", ["const:4b9b04:8", "const:4:8"]]
+ 004b9b04 ["CALL", null, ["callee:00c57f10:8"]]
- 004b9ac4 bytes 13781e94
+ 004b9b04 bytes 03791e94
- 004b9910 ["INT_ADD", "register:40f0:8", ["const:4b9910:8", "const:4:8"]]
- 004b9910 ["CALL", null, ["callee:00c58090:8"]]
+ 004b9950 ["INT_ADD", "register:40f0:8", ["const:4b9950:8", "const:4:8"]]
+ 004b9950 ["CALL", null, ["callee:00c58090:8"]]
- 004b9910 bytes e0781e94
+ 004b9950 bytes d0791e94
- 004b9964 ["INT_ADD", "register:40f0:8", ["const:4b9964:8", "const:4:8"]]
- 004b9964 ["CALL", null, ["callee:004bbb6c:8"]]
+ 004b99a4 ["INT_ADD", "register:40f0:8", ["const:4b99a4:8", "const:4:8"]]
+ 004b99a4 ["CALL", null, ["callee:004bbb6c:8"]]
- 004b9964 bytes 72080094
+ 004b99a4 bytes 72080094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-441f847880a065d06db0034e3b1a4a9e"></a>

### [`004ba458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ba/004ba458.md) → [`004ba498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ba/004ba498.md) _ZN5BotanrmERKNS_6BigIntEj

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c588d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c588d0.md) · 呼出先 4件 [`004bbb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bbb2c.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`00c58cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58cd0.md) · 呼出先 4件 [`004bbb6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bbb6c.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
    "old": {
      "definition_site": "004ba5ac",
      "incomplete_value": true,
      "site": "004ba5b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "004ba5b4",
      "incomplete_value": true,
      "site": "004ba5b8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ba5e0",
      "incomplete_value": false,
      "site": "004ba5f8",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004ba5a0",
      "incomplete_value": false,
      "site": "004ba5b8",
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
      "004ba5cc",
      "READ",
      [
        "storage",
        "00c9aa00",
        null,
        "pointer"
      ]
    ],
    [
      "004ba5e0",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004ba5f0",
      "DATA",
      [
        "storage",
        "00c69860",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004ba5cc",
      "READ",
      [
        "storage",
        "00c9ae00",
        null,
        "pointer"
      ]
    ],
    [
      "004ba5e0",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004ba5f0",
      "DATA",
      [
        "storage",
        "00c69c60",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ba5b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ba/004ba458.md#insn-004ba5b8) · [`004ba4f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ba/004ba458.md#insn-004ba4f4) · [`004ba554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ba/004ba458.md#insn-004ba554)
- 新版 `004ba5f8`（命令位置の公開資料なし） · `004ba534`（命令位置の公開資料なし） · `004ba594`（命令位置の公開資料なし）

~~~diff
- 004ba5b8 ["INT_ADD", "register:40f0:8", ["const:4ba5b8:8", "const:4:8"]]
- 004ba5b8 ["CALL", null, ["callee:00c57f10:8"]]
+ 004ba5f8 ["INT_ADD", "register:40f0:8", ["const:4ba5f8:8", "const:4:8"]]
+ 004ba5f8 ["CALL", null, ["callee:00c57f10:8"]]
- 004ba5b8 bytes 56751e94
+ 004ba5f8 bytes 46761e94
- 004ba4f4 ["INT_ADD", "register:40f0:8", ["const:4ba4f4:8", "const:4:8"]]
- 004ba4f4 ["CALL", null, ["callee:004bbb6c:8"]]
+ 004ba534 ["INT_ADD", "register:40f0:8", ["const:4ba534:8", "const:4:8"]]
+ 004ba534 ["CALL", null, ["callee:004bbb6c:8"]]
- 004ba4f4 bytes 8e050094
+ 004ba534 bytes 8e050094
- 004ba554 ["INT_ADD", "register:40f0:8", ["const:4ba554:8", "const:4:8"]]
- 004ba554 ["CALL", null, ["callee:00c57ef0:8"]]
+ 004ba594 ["INT_ADD", "register:40f0:8", ["const:4ba594:8", "const:4:8"]]
+ 004ba594 ["CALL", null, ["callee:00c57ef0:8"]]
- 004ba554 bytes 67751e94
+ 004ba594 bytes 57761e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f145299f1799a24b7d532a44945afacc"></a>

### [`004bb0ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bb0ec.md) → [`004bb12c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bb12c.md) _ZNK5Botan6BigInt13get_substringEmm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58910.md) · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`00c58d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58d10.md) · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
    "old": {
      "definition_site": "004bb2b8",
      "incomplete_value": false,
      "site": "004bb2c0",
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
            "const:ec4:8"
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
    "old": {
      "definition_site": "004bb2f4",
      "incomplete_value": true,
      "site": "004bb300",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
      "definition_site": "004bb330",
      "incomplete_value": false,
      "site": "004bb340",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004bb2f0",
      "incomplete_value": false,
      "site": "004bb300",
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
      "004bb2f8",
      "PARAM",
      [
        "storage",
        "0029eec4",
        null,
        "string"
      ]
    ],
    [
      "004bb330",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004bb334",
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
      "004bb2f8",
      "PARAM",
      [
        "storage",
        "0029ef91",
        null,
        "string"
      ]
    ],
    [
      "004bb330",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004bb334",
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

- 旧版 [`004bb2c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bb0ec.md#insn-004bb2c0) · [`004bb300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bb0ec.md#insn-004bb300) · [`004bb2ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bb0ec.md#insn-004bb2ac)
- 新版 `004bb300`（命令位置の公開資料なし） · `004bb340`（命令位置の公開資料なし） · `004bb2ec`（命令位置の公開資料なし）

~~~diff
- 004bb2c0 ["INT_ADD", "register:40f0:8", ["const:4bb2c0:8", "const:4:8"]]
- 004bb2c0 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004bb300 ["INT_ADD", "register:40f0:8", ["const:4bb300:8", "const:4:8"]]
+ 004bb300 ["CALL", null, ["callee:0043ddd8:8"]]
- 004bb2c0 bytes b60afe97
+ 004bb300 bytes b60afe97
- 004bb300 ["INT_ADD", "register:40f0:8", ["const:4bb300:8", "const:4:8"]]
- 004bb300 ["CALL", null, ["callee:00c57f10:8"]]
+ 004bb340 ["INT_ADD", "register:40f0:8", ["const:4bb340:8", "const:4:8"]]
+ 004bb340 ["CALL", null, ["callee:00c57f10:8"]]
- 004bb300 bytes 04721e94
+ 004bb340 bytes f4721e94
- 004bb2ac ["INT_ADD", "register:40f0:8", ["const:4bb2ac:8", "const:4:8"]]
- 004bb2ac ["CALL", null, ["callee:00c57ef0:8"]]
+ 004bb2ec ["INT_ADD", "register:40f0:8", ["const:4bb2ec:8", "const:4:8"]]
+ 004bb2ec ["CALL", null, ["callee:00c57ef0:8"]]
- 004bb2ac bytes 11721e94
+ 004bb2ec bytes 01731e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ab4fda0a67786142d225fde8cb5c18d"></a>

### [`004bb354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bb354.md) → [`004bb394`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bb394.md) _ZNK5Botan6BigInt9to_u32bitEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
    "old": {
      "definition_site": "004bb43c",
      "incomplete_value": false,
      "site": "004bb444",
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
            "const:85d:8"
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
    "old": {
      "definition_site": "004bb478",
      "incomplete_value": true,
      "site": "004bb484",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bb4b4",
      "incomplete_value": false,
      "site": "004bb4c4",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004bb474",
      "incomplete_value": false,
      "site": "004bb484",
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
      "004bb47c",
      "PARAM",
      [
        "storage",
        "002bd85d",
        null,
        "string"
      ]
    ],
    [
      "004bb4b4",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004bb4b8",
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
      "004bb47c",
      "PARAM",
      [
        "storage",
        "002bd89d",
        null,
        "string"
      ]
    ],
    [
      "004bb4b4",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004bb4b8",
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

- 旧版 [`004bb444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bb354.md#insn-004bb444) · [`004bb484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bb354.md#insn-004bb484) · [`004bb4a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bb354.md#insn-004bb4a8)
- 新版 `004bb484`（命令位置の公開資料なし） · `004bb4c4`（命令位置の公開資料なし） · `004bb4e8`（命令位置の公開資料なし）

~~~diff
- 004bb444 ["INT_ADD", "register:40f0:8", ["const:4bb444:8", "const:4:8"]]
- 004bb444 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004bb484 ["INT_ADD", "register:40f0:8", ["const:4bb484:8", "const:4:8"]]
+ 004bb484 ["CALL", null, ["callee:0043ddd8:8"]]
- 004bb444 bytes 550afe97
+ 004bb484 bytes 550afe97
- 004bb484 ["INT_ADD", "register:40f0:8", ["const:4bb484:8", "const:4:8"]]
- 004bb484 ["CALL", null, ["callee:00c57f10:8"]]
+ 004bb4c4 ["INT_ADD", "register:40f0:8", ["const:4bb4c4:8", "const:4:8"]]
+ 004bb4c4 ["CALL", null, ["callee:00c57f10:8"]]
- 004bb484 bytes a3711e94
+ 004bb4c4 bytes 93721e94
- 004bb4a8 ["INT_ADD", "register:40f0:8", ["const:4bb4a8:8", "const:4:8"]]
- 004bb4a8 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004bb4e8 ["INT_ADD", "register:40f0:8", ["const:4bb4e8:8", "const:4:8"]]
+ 004bb4e8 ["CALL", null, ["callee:0043ddd8:8"]]
- 004bb4a8 bytes 3c0afe97
+ 004bb4e8 bytes 3c0afe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62924804fbf60ec262803e52e2746357"></a>

### [`004bb6f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bb6f0.md) → [`004bb730`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bb730.md) _ZN5Botan6BigInt17const_time_lookupERNSt6__ndk16vectorIjNS_16secure_allocatorIjEEEERKNS2_IS0_NS1_9allocatorIS0_EEEEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58920.md) · 呼出先 2件 [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md) [`00c58250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58250.md)
- 新版 呼出元 1件 [`00c58d20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58d20.md) · 呼出先 2件 [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md) [`00c58650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58650.md)

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
    "old": {
      "definition_site": "004bb860",
      "incomplete_value": false,
      "site": "004bb880",
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
            "const:14b:8"
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
    "old": {
      "definition_site": "004bb868",
      "incomplete_value": false,
      "site": "004bb880",
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
            "const:ef2:8"
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
    "old": {
      "definition_site": "004bb870",
      "incomplete_value": false,
      "site": "004bb880",
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
            "const:4f7:8"
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
      "004bb8a0",
      "PARAM",
      [
        "storage",
        "002b814b",
        null,
        "string"
      ]
    ],
    [
      "004bb8a8",
      "PARAM",
      [
        "storage",
        "0029eef2",
        null,
        "string"
      ]
    ],
    [
      "004bb8b0",
      "PARAM",
      [
        "storage",
        "002bc4f7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bb8a0",
      "PARAM",
      [
        "storage",
        "002b818b",
        null,
        "string"
      ]
    ],
    [
      "004bb8a8",
      "PARAM",
      [
        "storage",
        "0029efbf",
        null,
        "string"
      ]
    ],
    [
      "004bb8b0",
      "PARAM",
      [
        "storage",
        "002bc537",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bb880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bb6f0.md#insn-004bb880) · [`004bb728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bb6f0.md#insn-004bb728) · [`004bb860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bb6f0.md#insn-004bb860)
- 新版 `004bb8c0`（命令位置の公開資料なし） · `004bb768`（命令位置の公開資料なし） · `004bb8a0`（命令位置の公開資料なし）

~~~diff
- 004bb880 ["INT_ADD", "register:40f0:8", ["const:4bb880:8", "const:4:8"]]
- 004bb880 ["CALL", null, ["callee:00c58650:8"]]
+ 004bb8c0 ["INT_ADD", "register:40f0:8", ["const:4bb8c0:8", "const:4:8"]]
+ 004bb8c0 ["CALL", null, ["callee:00c58650:8"]]
- 004bb880 bytes 74721e94
+ 004bb8c0 bytes 64731e94
- 004bb728 ["INT_ADD", "register:40f0:8", ["const:4bb728:8", "const:4:8"]]
- 004bb728 ["CALL", null, ["callee:00c58090:8"]]
+ 004bb768 ["INT_ADD", "register:40f0:8", ["const:4bb768:8", "const:4:8"]]
+ 004bb768 ["CALL", null, ["callee:00c58090:8"]]
- 004bb728 bytes 5a711e94
+ 004bb768 bytes 4a721e94
- 004bb860 ["COPY", "tmp:0:8", ["const:14b:8"]]
- 004bb860 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004bb860 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004bb860 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004bb8a0 ["COPY", "tmp:0:8", ["const:18b:8"]]
+ 004bb8a0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004bb8a0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004bb8a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004bb860 bytes 002c0591
+ 004bb8a0 bytes 002c0691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-660af40114633d2c4df301f5e817fe3f"></a>

### [`004bb884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bb884.md) → [`004bb8c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bb8c4.md) FUN_004bb8c4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004b66e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b6/004b66e8.md) · 呼出先 7件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c58520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58520.md) [`00c58740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58740.md) [`00c58840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58840.md)
- 新版 呼出元 1件 [`004b6728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b6/004b6728.md) · 呼出先 7件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c58920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58920.md) [`00c58b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58b40.md) [`00c58c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58c40.md)

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
    "old": {
      "definition_site": "004bba14",
      "incomplete_value": true,
      "site": "004bba14",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "004bbaa4",
      "incomplete_value": true,
      "site": "004bbaa4",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "004bbad4",
      "incomplete_value": true,
      "site": "004bbad4",
      "value": [
        "LOAD",
        "8",
        [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004bba44",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004bbad4",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004bbb04",
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
      "004bba44",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004bbad4",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004bbb04",
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

- 旧版 [`004bba14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bb884.md#insn-004bba14) · [`004bba94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bb884.md#insn-004bba94) · [`004bbaa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bb884.md#insn-004bbaa4)
- 新版 `004bba54`（命令位置の公開資料なし） · `004bbad4`（命令位置の公開資料なし） · `004bbae4`（命令位置の公開資料なし）

~~~diff
- 004bba14 ["COPY", "register:0:8", ["register:4048:8"]]
- 004bba14 ["INT_ADD", "register:40f0:8", ["const:4bba14:8", "const:4:8"]]
- 004bba14 ["CALLIND", null, ["register:0:8"]]
+ 004bba54 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004bba54 ["INT_ADD", "register:40f0:8", ["const:4bba54:8", "const:4:8"]]
+ 004bba54 ["CALLIND", null, ["register:0:8"]]
- 004bba14 bytes 20013fd6
+ 004bba54 bytes 20013fd6
- 004bba94 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:338:8"]]
- 004bba94 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004bbad4 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:738:8"]]
+ 004bbad4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004bba94 bytes 099f41f9
+ 004bbad4 bytes 099f43f9
- 004bbaa4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004bbaa4 ["INT_ADD", "register:40f0:8", ["const:4bbaa4:8", "const:4:8"]]
- 004bbaa4 ["CALLIND", null, ["register:0:8"]]
+ 004bbae4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004bbae4 ["INT_ADD", "register:40f0:8", ["const:4bbae4:8", "const:4:8"]]
+ 004bbae4 ["CALLIND", null, ["register:0:8"]]
- 004bbaa4 bytes 20013fd6
+ 004bbae4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4a85455aebd2fdee386e0d9f0c4aca6"></a>

### [`004bbb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bbb2c.md) → [`004bbb6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bbb6c.md) FUN_004bbb6c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`004b66e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b6/004b66e8.md) [`004b98bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b98bc.md) [`004ba458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ba/004ba458.md) [`004ddec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004dd/004ddec8.md) · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 4件 [`004b6728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b6/004b6728.md) [`004b98fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b9/004b98fc.md) [`004ba498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ba/004ba498.md) [`004ddf08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004dd/004ddf08.md) · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
    "old": {
      "definition_site": "004bbb98",
      "incomplete_value": false,
      "site": "004bbba0",
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
            "const:d64:8"
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
    "old": {
      "definition_site": "004bbbd4",
      "incomplete_value": true,
      "site": "004bbbe0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
      "definition_site": "004bbc10",
      "incomplete_value": false,
      "site": "004bbc20",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004bbbd0",
      "incomplete_value": false,
      "site": "004bbbe0",
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
      "004bbbd8",
      "PARAM",
      [
        "storage",
        "002b4d64",
        null,
        "string"
      ]
    ],
    [
      "004bbc10",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004bbc14",
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
      "004bbbd8",
      "PARAM",
      [
        "storage",
        "002b4da4",
        null,
        "string"
      ]
    ],
    [
      "004bbc10",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004bbc14",
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

- 旧版 [`004bbba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bbb2c.md#insn-004bbba0) · [`004bbbe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bbb2c.md#insn-004bbbe0) · [`004bbb8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bbb2c.md#insn-004bbb8c)
- 新版 `004bbbe0`（命令位置の公開資料なし） · `004bbc20`（命令位置の公開資料なし） · `004bbbcc`（命令位置の公開資料なし）

~~~diff
- 004bbba0 ["INT_ADD", "register:40f0:8", ["const:4bbba0:8", "const:4:8"]]
- 004bbba0 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004bbbe0 ["INT_ADD", "register:40f0:8", ["const:4bbbe0:8", "const:4:8"]]
+ 004bbbe0 ["CALL", null, ["callee:0043ddd8:8"]]
- 004bbba0 bytes 7e08fe97
+ 004bbbe0 bytes 7e08fe97
- 004bbbe0 ["INT_ADD", "register:40f0:8", ["const:4bbbe0:8", "const:4:8"]]
- 004bbbe0 ["CALL", null, ["callee:00c57f10:8"]]
+ 004bbc20 ["INT_ADD", "register:40f0:8", ["const:4bbc20:8", "const:4:8"]]
+ 004bbc20 ["CALL", null, ["callee:00c57f10:8"]]
- 004bbbe0 bytes cc6f1e94
+ 004bbc20 bytes bc701e94
- 004bbb8c ["INT_ADD", "register:40f0:8", ["const:4bbb8c:8", "const:4:8"]]
- 004bbb8c ["CALL", null, ["callee:00c57ef0:8"]]
+ 004bbbcc ["INT_ADD", "register:40f0:8", ["const:4bbbcc:8", "const:4:8"]]
+ 004bbbcc ["CALL", null, ["callee:00c57ef0:8"]]
- 004bbb8c bytes d96f1e94
+ 004bbbcc bytes c9701e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9a65430feaae6a4278c1708b4590683"></a>

### [`004bbfc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bbfc0.md) → [`004bc000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bc000.md) _ZN5Botan11BlockCipher15create_or_throwERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

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
    "old": {
      "definition_site": "004bc038",
      "incomplete_value": false,
      "site": "004bc040",
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
            "const:40:8"
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
    "old": {
      "definition_site": "004bc078",
      "incomplete_value": true,
      "site": "004bc084",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
      "definition_site": "004bc0b4",
      "incomplete_value": false,
      "site": "004bc0c4",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004bc074",
      "incomplete_value": false,
      "site": "004bc084",
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
      "004bc078",
      "PARAM",
      [
        "storage",
        "002a4040",
        null,
        "string"
      ]
    ],
    [
      "004bc0b4",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004bc0b8",
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
      "004bc078",
      "PARAM",
      [
        "storage",
        "002a410d",
        null,
        "string"
      ]
    ],
    [
      "004bc0b4",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004bc0b8",
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

- 旧版 [`004bc040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bbfc0.md#insn-004bc040) · [`004bc084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bbfc0.md#insn-004bc084) · [`004bbff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bbfc0.md#insn-004bbff4)
- 新版 `004bc080`（命令位置の公開資料なし） · `004bc0c4`（命令位置の公開資料なし） · `004bc034`（命令位置の公開資料なし）

~~~diff
- 004bc040 ["INT_ADD", "register:40f0:8", ["const:4bc040:8", "const:4:8"]]
- 004bc040 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004bc080 ["INT_ADD", "register:40f0:8", ["const:4bc080:8", "const:4:8"]]
+ 004bc080 ["CALL", null, ["callee:0043ddd8:8"]]
- 004bc040 bytes 5607fe97
+ 004bc080 bytes 5607fe97
- 004bc084 ["INT_ADD", "register:40f0:8", ["const:4bc084:8", "const:4:8"]]
- 004bc084 ["CALL", null, ["callee:00c57f10:8"]]
+ 004bc0c4 ["INT_ADD", "register:40f0:8", ["const:4bc0c4:8", "const:4:8"]]
+ 004bc0c4 ["CALL", null, ["callee:00c57f10:8"]]
- 004bc084 bytes a36e1e94
+ 004bc0c4 bytes 936f1e94
- 004bbff4 ["INT_ADD", "register:40f0:8", ["const:4bbff4:8", "const:4:8"]]
- 004bbff4 ["CALL", null, ["callee:00c58d30:8"]]
+ 004bc034 ["INT_ADD", "register:40f0:8", ["const:4bc034:8", "const:4:8"]]
+ 004bc034 ["CALL", null, ["callee:00c58d30:8"]]
- 004bbff4 bytes 4f721e94
+ 004bc034 bytes 3f731e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d66a24de5c11e760b614eb3ea7ac105"></a>

### [`004bc378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc378.md) → [`004bc3b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bc3b8.md) _ZN5Botan8CBC_ModeC2EPNS_11BlockCipherEPNS_28BlockCipherModePaddingMethodE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58960.md) · 呼出先 9件 [`004a680c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a680c.md) [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 1件 [`00c58d60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58d60.md) · 呼出先 9件 [`004a684c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a684c.md) [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

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
    "old": {
      "definition_site": "004bc3b0",
      "incomplete_value": true,
      "site": "004bc3b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "old": {
      "definition_site": "004bc454",
      "incomplete_value": false,
      "site": "004bc460",
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
    "ordinal": 6,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "004bc480",
      "incomplete_value": false,
      "site": "004bc488",
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
      "004bc3e0",
      "READ",
      [
        "storage",
        "00c9aa30",
        null,
        "pointer"
      ]
    ],
    [
      "004bc3f0",
      "DATA",
      [
        "storage",
        "00c66020",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "004bc494",
      "PARAM",
      [
        "storage",
        "002bb347",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bc3e0",
      "READ",
      [
        "storage",
        "00c9ae30",
        null,
        "pointer"
      ]
    ],
    [
      "004bc3f0",
      "DATA",
      [
        "storage",
        "00c66420",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "004bc494",
      "PARAM",
      [
        "storage",
        "002bb387",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bc460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc378.md#insn-004bc460) · [`004bc488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc378.md#insn-004bc488) · [`004bc4d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc378.md#insn-004bc4d4)
- 新版 `004bc4a0`（命令位置の公開資料なし） · `004bc4c8`（命令位置の公開資料なし） · `004bc514`（命令位置の公開資料なし）

~~~diff
- 004bc460 ["INT_ADD", "register:40f0:8", ["const:4bc460:8", "const:4:8"]]
- 004bc460 ["CALL", null, ["callee:00c57f60:8"]]
+ 004bc4a0 ["INT_ADD", "register:40f0:8", ["const:4bc4a0:8", "const:4:8"]]
+ 004bc4a0 ["CALL", null, ["callee:00c57f60:8"]]
- 004bc460 bytes c06d1e94
+ 004bc4a0 bytes b06e1e94
- 004bc488 ["INT_ADD", "register:40f0:8", ["const:4bc488:8", "const:4:8"]]
- 004bc488 ["CALL", null, ["callee:00c57f70:8"]]
+ 004bc4c8 ["INT_ADD", "register:40f0:8", ["const:4bc4c8:8", "const:4:8"]]
+ 004bc4c8 ["CALL", null, ["callee:00c57f70:8"]]
- 004bc488 bytes ba6d1e94
+ 004bc4c8 bytes aa6e1e94
- 004bc4d4 ["INT_ADD", "register:40f0:8", ["const:4bc4d4:8", "const:4:8"]]
- 004bc4d4 ["CALL", null, ["callee:00c57f70:8"]]
+ 004bc514 ["INT_ADD", "register:40f0:8", ["const:4bc514:8", "const:4:8"]]
+ 004bc514 ["CALL", null, ["callee:00c57f70:8"]]
- 004bc4d4 bytes a76d1e94
+ 004bc514 bytes 976e1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c6634837c3cdfb9f6ca0d11c528287d"></a>

### [`004bc6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc6f8.md) → [`004bc738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bc738.md) _ZNK5Botan8CBC_Mode4nameEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58970.md) · 呼出先 5件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c58250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58250.md)
- 新版 呼出元 1件 [`00c58d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58d70.md) · 呼出先 5件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md) [`00c58650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58650.md)

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
    "old": {
      "definition_site": "004bc740",
      "incomplete_value": false,
      "site": "004bc748",
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
            "const:4d:8"
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
    "old": {
      "definition_site": "004bc7ec",
      "incomplete_value": false,
      "site": "004bc7f4",
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
            "const:f5d:8"
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
    "old": {
      "definition_site": "004bc880",
      "incomplete_value": false,
      "site": "004bc8a0",
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
            "const:862:8"
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
      "004bc780",
      "PARAM",
      [
        "storage",
        "002a404d",
        null,
        "string"
      ]
    ],
    [
      "004bc82c",
      "PARAM",
      [
        "storage",
        "0029ff5d",
        null,
        "string"
      ]
    ],
    [
      "004bc8c0",
      "PARAM",
      [
        "storage",
        "002ac862",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bc780",
      "PARAM",
      [
        "storage",
        "002a411a",
        null,
        "string"
      ]
    ],
    [
      "004bc82c",
      "PARAM",
      [
        "storage",
        "002a002a",
        null,
        "string"
      ]
    ],
    [
      "004bc8c0",
      "PARAM",
      [
        "storage",
        "002ac8a2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bc748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc6f8.md#insn-004bc748) · [`004bc7f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc6f8.md#insn-004bc7f4) · [`004bc834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc6f8.md#insn-004bc834)
- 新版 `004bc788`（命令位置の公開資料なし） · `004bc834`（命令位置の公開資料なし） · `004bc874`（命令位置の公開資料なし）

~~~diff
- 004bc748 ["INT_ADD", "register:40f0:8", ["const:4bc748:8", "const:4:8"]]
- 004bc748 ["CALL", null, ["callee:00c57f70:8"]]
+ 004bc788 ["INT_ADD", "register:40f0:8", ["const:4bc788:8", "const:4:8"]]
+ 004bc788 ["CALL", null, ["callee:00c57f70:8"]]
- 004bc748 bytes 0a6d1e94
+ 004bc788 bytes fa6d1e94
- 004bc7f4 ["INT_ADD", "register:40f0:8", ["const:4bc7f4:8", "const:4:8"]]
- 004bc7f4 ["CALL", null, ["callee:00c57f70:8"]]
+ 004bc834 ["INT_ADD", "register:40f0:8", ["const:4bc834:8", "const:4:8"]]
+ 004bc834 ["CALL", null, ["callee:00c57f70:8"]]
- 004bc7f4 bytes df6c1e94
+ 004bc834 bytes cf6d1e94
- 004bc834 ["INT_ADD", "register:40f0:8", ["const:4bc834:8", "const:4:8"]]
- 004bc834 ["CALL", null, ["callee:00c57eb0:8"]]
+ 004bc874 ["INT_ADD", "register:40f0:8", ["const:4bc874:8", "const:4:8"]]
+ 004bc874 ["CALL", null, ["callee:00c57eb0:8"]]
- 004bc834 bytes 9f6c1e94
+ 004bc874 bytes 8f6d1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cf758fb0a49e0deed55b07d5b185997"></a>

### [`004bc9c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc9c0.md) → [`004bca00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bca00.md) FUN_004bca00

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 10件 [`004bc9b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc9b8.md) [`004bf404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bf404.md) [`004c4028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c4028.md) [`004c4468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c4468.md) [`004c4ccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c4ccc.md) · 呼出先 5件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c58980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58980.md)
- 新版 呼出元 10件 [`004bc9f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bc9f8.md) [`004bf444`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bf444.md) [`004c4068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c4068.md) [`004c44a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c44a8.md) [`004c4d0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c4d0c.md) · 呼出先 5件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c58d80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58d80.md)

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
    "old": {
      "definition_site": "004bcab8",
      "incomplete_value": true,
      "site": "004bcac4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9a000:8"
              ],
              [
                "leaf",
                "const:a38:8"
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
      "definition_site": "004bcaf4",
      "incomplete_value": false,
      "site": "004bcb04",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004bcab4",
      "incomplete_value": false,
      "site": "004bcac4",
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
      "004bcaf4",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004bcaf8",
      "READ",
      [
        "storage",
        "00c9aa38",
        null,
        "pointer"
      ]
    ],
    [
      "004bcaf8",
      "PARAM",
      [
        "storage",
        "00c66a28",
        "_ZTIN5Botan18Invalid_Key_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004bcaf4",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004bcaf8",
      "READ",
      [
        "storage",
        "00c9ae38",
        null,
        "pointer"
      ]
    ],
    [
      "004bcaf8",
      "PARAM",
      [
        "storage",
        "00c66e28",
        "_ZTIN5Botan18Invalid_Key_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bca84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc9c0.md#insn-004bca84) · [`004bcac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc9c0.md#insn-004bcac4) · [`004bc9f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc9c0.md#insn-004bc9f8)
- 新版 `004bcac4`（命令位置の公開資料なし） · `004bcb04`（命令位置の公開資料なし） · `004bca38`（命令位置の公開資料なし）

~~~diff
- 004bca84 ["COPY", "register:0:8", ["register:4050:8"]]
- 004bca84 ["INT_ADD", "register:40f0:8", ["const:4bca84:8", "const:4:8"]]
- 004bca84 ["CALLIND", null, ["register:0:8"]]
+ 004bcac4 ["COPY", "register:0:8", ["register:4050:8"]]
+ 004bcac4 ["INT_ADD", "register:40f0:8", ["const:4bcac4:8", "const:4:8"]]
+ 004bcac4 ["CALLIND", null, ["register:0:8"]]
- 004bca84 bytes 40013fd6
+ 004bcac4 bytes 40013fd6
- 004bcac4 ["INT_ADD", "register:40f0:8", ["const:4bcac4:8", "const:4:8"]]
- 004bcac4 ["CALL", null, ["callee:00c57f10:8"]]
+ 004bcb04 ["INT_ADD", "register:40f0:8", ["const:4bcb04:8", "const:4:8"]]
+ 004bcb04 ["CALL", null, ["callee:00c57f10:8"]]
- 004bcac4 bytes 136c1e94
+ 004bcb04 bytes 036d1e94
- 004bc9f8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004bc9f8 ["INT_ADD", "register:40f0:8", ["const:4bc9f8:8", "const:4:8"]]
- 004bc9f8 ["CALLIND", null, ["register:0:8"]]
+ 004bca38 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004bca38 ["INT_ADD", "register:40f0:8", ["const:4bca38:8", "const:4:8"]]
+ 004bca38 ["CALLIND", null, ["register:0:8"]]
- 004bc9f8 bytes 20013fd6
+ 004bca38 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1abb670fcecd933377858a30fc89a42"></a>

### [`004bcb14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bcb14.md) → [`004bcb54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bcb54.md) _ZN5Botan8CBC_Mode9start_msgEPKhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00543380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543380.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`005433c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/005433c0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
    "old": {
      "definition_site": "004bcc04",
      "incomplete_value": true,
      "site": "004bcc10",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bcc40",
      "incomplete_value": false,
      "site": "004bcc50",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004bcc00",
      "incomplete_value": false,
      "site": "004bcc10",
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
      "004bcc40",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004bcc44",
      "READ",
      [
        "storage",
        "00c9aa40",
        null,
        "pointer"
      ]
    ],
    [
      "004bcc44",
      "PARAM",
      [
        "storage",
        "00c660b0",
        "_ZTIN5Botan17Invalid_IV_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004bcc40",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004bcc44",
      "READ",
      [
        "storage",
        "00c9ae40",
        null,
        "pointer"
      ]
    ],
    [
      "004bcc44",
      "PARAM",
      [
        "storage",
        "00c664b0",
        "_ZTIN5Botan17Invalid_IV_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bcbd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bcb14.md#insn-004bcbd0) · [`004bcc10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bcb14.md#insn-004bcc10) · [`004bcb4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bcb14.md#insn-004bcb4c)
- 新版 `004bcc10`（命令位置の公開資料なし） · `004bcc50`（命令位置の公開資料なし） · `004bcb8c`（命令位置の公開資料なし）

~~~diff
- 004bcbd0 ["COPY", "register:0:8", ["register:4050:8"]]
- 004bcbd0 ["INT_ADD", "register:40f0:8", ["const:4bcbd0:8", "const:4:8"]]
- 004bcbd0 ["CALLIND", null, ["register:0:8"]]
+ 004bcc10 ["COPY", "register:0:8", ["register:4050:8"]]
+ 004bcc10 ["INT_ADD", "register:40f0:8", ["const:4bcc10:8", "const:4:8"]]
+ 004bcc10 ["CALLIND", null, ["register:0:8"]]
- 004bcbd0 bytes 40013fd6
+ 004bcc10 bytes 40013fd6
- 004bcc10 ["INT_ADD", "register:40f0:8", ["const:4bcc10:8", "const:4:8"]]
- 004bcc10 ["CALL", null, ["callee:00c57f10:8"]]
+ 004bcc50 ["INT_ADD", "register:40f0:8", ["const:4bcc50:8", "const:4:8"]]
+ 004bcc50 ["CALL", null, ["callee:00c57f10:8"]]
- 004bcc10 bytes c06b1e94
+ 004bcc50 bytes b06c1e94
- 004bcb4c ["COPY", "register:0:8", ["register:4040:8"]]
- 004bcb4c ["INT_ADD", "register:40f0:8", ["const:4bcb4c:8", "const:4:8"]]
- 004bcb4c ["CALLIND", null, ["register:0:8"]]
+ 004bcb8c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bcb8c ["INT_ADD", "register:40f0:8", ["const:4bcb8c:8", "const:4:8"]]
+ 004bcb8c ["CALLIND", null, ["register:0:8"]]
- 004bcb4c bytes 00013fd6
+ 004bcb8c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bea005bd8c37c7060ab6339ce2e0f6f7"></a>

### [`004bcc68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bcc68.md) → [`004bcca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bcca8.md) _ZNK5Botan14CBC_Encryption13output_lengthEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58250.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58650.md)

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
    "old": {
      "definition_site": "004bcca8",
      "incomplete_value": false,
      "site": "004bccc8",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "004bccb0",
      "incomplete_value": false,
      "site": "004bccc8",
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
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "004bccb8",
      "incomplete_value": false,
      "site": "004bccc8",
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
      "004bcce8",
      "PARAM",
      [
        "storage",
        "002a1ff2",
        null,
        "string"
      ]
    ],
    [
      "004bccf0",
      "PARAM",
      [
        "storage",
        "002ab57d",
        null,
        "string"
      ]
    ],
    [
      "004bccf8",
      "PARAM",
      [
        "storage",
        "002b8265",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bcce8",
      "PARAM",
      [
        "storage",
        "002a20bf",
        null,
        "string"
      ]
    ],
    [
      "004bccf0",
      "PARAM",
      [
        "storage",
        "002ab5bd",
        null,
        "string"
      ]
    ],
    [
      "004bccf8",
      "PARAM",
      [
        "storage",
        "002b82a5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bccc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bcc68.md#insn-004bccc8) · [`004bcca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bcc68.md#insn-004bcca4) · [`004bcca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bcc68.md#insn-004bcca8)
- 新版 `004bcd08`（命令位置の公開資料なし） · `004bcce4`（命令位置の公開資料なし） · `004bcce8`（命令位置の公開資料なし）

~~~diff
- 004bccc8 ["INT_ADD", "register:40f0:8", ["const:4bccc8:8", "const:4:8"]]
- 004bccc8 ["CALL", null, ["callee:00c58650:8"]]
+ 004bcd08 ["INT_ADD", "register:40f0:8", ["const:4bcd08:8", "const:4:8"]]
+ 004bcd08 ["CALL", null, ["callee:00c58650:8"]]
- 004bccc8 bytes 626d1e94
+ 004bcd08 bytes 526e1e94
- 004bcca4 ["COPY", "register:4000:8", ["const:2a1000:8"]]
+ 004bcce4 ["COPY", "register:4000:8", ["const:2a2000:8"]]
- 004bcca4 bytes 20efffb0
+ 004bcce4 bytes 20efffd0
- 004bcca8 ["COPY", "tmp:0:8", ["const:ff2:8"]]
- 004bcca8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004bcca8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004bcca8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004bcce8 ["COPY", "tmp:0:8", ["const:bf:8"]]
+ 004bcce8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004bcce8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004bcce8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004bcca8 bytes 00c83f91
+ 004bcce8 bytes 00fc0291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87d99852b4fdee8f76fd8092777b7ebe"></a>

### [`004bcccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bcccc.md) → [`004bcd0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bcd0c.md) _ZN5Botan14CBC_Encryption7processEPhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00543818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543818.md) [`00c58250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58250.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00543858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543858.md) [`00c58650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58650.md)

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
    "old": {
      "definition_site": "004bcf14",
      "incomplete_value": false,
      "site": "004bcf34",
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "004bcf1c",
      "incomplete_value": false,
      "site": "004bcf34",
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
            "const:f66:8"
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
    "old": {
      "definition_site": "004bcf24",
      "incomplete_value": false,
      "site": "004bcf34",
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
      "004bcf54",
      "PARAM",
      [
        "storage",
        "002a8b53",
        null,
        "string"
      ]
    ],
    [
      "004bcf5c",
      "PARAM",
      [
        "storage",
        "0029ff66",
        null,
        "string"
      ]
    ],
    [
      "004bcf64",
      "PARAM",
      [
        "storage",
        "002a4053",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bcf54",
      "PARAM",
      [
        "storage",
        "002a8c20",
        null,
        "string"
      ]
    ],
    [
      "004bcf5c",
      "PARAM",
      [
        "storage",
        "002a0033",
        null,
        "string"
      ]
    ],
    [
      "004bcf64",
      "PARAM",
      [
        "storage",
        "002a4120",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bcf34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bcccc.md#insn-004bcf34) · [`004bcdac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bcccc.md#insn-004bcdac) · [`004bcdc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bcccc.md#insn-004bcdc8)
- 新版 `004bcf74`（命令位置の公開資料なし） · `004bcdec`（命令位置の公開資料なし） · `004bce08`（命令位置の公開資料なし）

~~~diff
- 004bcf34 ["INT_ADD", "register:40f0:8", ["const:4bcf34:8", "const:4:8"]]
- 004bcf34 ["CALL", null, ["callee:00c58650:8"]]
+ 004bcf74 ["INT_ADD", "register:40f0:8", ["const:4bcf74:8", "const:4:8"]]
+ 004bcf74 ["CALL", null, ["callee:00c58650:8"]]
- 004bcf34 bytes c76c1e94
+ 004bcf74 bytes b76d1e94
- 004bcdac ["COPY", "register:0:8", ["register:4040:8"]]
- 004bcdac ["INT_ADD", "register:40f0:8", ["const:4bcdac:8", "const:4:8"]]
- 004bcdac ["CALLIND", null, ["register:0:8"]]
+ 004bcdec ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bcdec ["INT_ADD", "register:40f0:8", ["const:4bcdec:8", "const:4:8"]]
+ 004bcdec ["CALLIND", null, ["register:0:8"]]
- 004bcdac bytes 00013fd6
+ 004bcdec bytes 00013fd6
- 004bcdc8 ["INT_ADD", "register:40f0:8", ["const:4bcdc8:8", "const:4:8"]]
- 004bcdc8 ["CALL", null, ["callee:00543858:8"]]
+ 004bce08 ["INT_ADD", "register:40f0:8", ["const:4bce08:8", "const:4:8"]]
+ 004bce08 ["CALL", null, ["callee:00543858:8"]]
- 004bcdc8 bytes 941a0294
+ 004bce08 bytes 941a0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a01309761ee8f5b1b14469693063dbc"></a>

### [`004bcf38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bcf38.md) → [`004bcf78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bcf78.md) _ZN5Botan14CBC_Encryption6finishERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
    "old": {
      "definition_site": "004bd05c",
      "incomplete_value": false,
      "site": "004bd07c",
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
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "004bd064",
      "incomplete_value": false,
      "site": "004bd07c",
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "004bd06c",
      "incomplete_value": false,
      "site": "004bd07c",
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
      "004bd09c",
      "PARAM",
      [
        "storage",
        "002ad725",
        null,
        "string"
      ]
    ],
    [
      "004bd0a4",
      "PARAM",
      [
        "storage",
        "002b4cdd",
        null,
        "string"
      ]
    ],
    [
      "004bd0ac",
      "PARAM",
      [
        "storage",
        "002ba20d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bd09c",
      "PARAM",
      [
        "storage",
        "002ad765",
        null,
        "string"
      ]
    ],
    [
      "004bd0a4",
      "PARAM",
      [
        "storage",
        "002b4d1d",
        null,
        "string"
      ]
    ],
    [
      "004bd0ac",
      "PARAM",
      [
        "storage",
        "002ba24d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bd074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bcf38.md#insn-004bd074) · [`004bd07c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bcf38.md#insn-004bd07c) · [`004bd0b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bcf38.md#insn-004bd0b4)
- 新版 `004bd0b4`（命令位置の公開資料なし） · `004bd0bc`（命令位置の公開資料なし） · `004bd0f4`（命令位置の公開資料なし）

~~~diff
- 004bd074 ["COPY", "tmp:0:8", ["const:267:8"]]
- 004bd074 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 004bd074 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 004bd074 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 004bd0b4 ["COPY", "tmp:0:8", ["const:dcb:8"]]
+ 004bd0b4 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 004bd0b4 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 004bd0b4 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 004bd074 bytes 639c0991
+ 004bd0b4 bytes 632c3791
- 004bd07c ["INT_ADD", "register:40f0:8", ["const:4bd07c:8", "const:4:8"]]
- 004bd07c ["CALL", null, ["callee:00c58650:8"]]
+ 004bd0bc ["INT_ADD", "register:40f0:8", ["const:4bd0bc:8", "const:4:8"]]
+ 004bd0bc ["CALL", null, ["callee:00c58650:8"]]
- 004bd07c bytes 756c1e94
+ 004bd0bc bytes 656d1e94
- 004bd0b4 ["INT_ADD", "register:40f0:8", ["const:4bd0b4:8", "const:4:8"]]
- 004bd0b4 ["CALL", null, ["callee:00c58650:8"]]
+ 004bd0f4 ["INT_ADD", "register:40f0:8", ["const:4bd0f4:8", "const:4:8"]]
+ 004bd0f4 ["CALL", null, ["callee:00c58650:8"]]
- 004bd0b4 bytes 676c1e94
+ 004bd0f4 bytes 576d1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6e71100cf1065ee0241762528ef3cf7"></a>

### [`004bd218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bd/004bd218.md) → [`004bd258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bd/004bd258.md) _ZN5Botan14CTS_Encryption6finishERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 13件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00540264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540264.md) [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`005402a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005402a4.md) [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

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
    "old": {
      "definition_site": "004bd4d0",
      "incomplete_value": true,
      "site": "004bd4d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 10,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "004bd590",
      "incomplete_value": false,
      "site": "004bd5b0",
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
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "004bd598",
      "incomplete_value": false,
      "site": "004bd5b0",
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
      "004bd500",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004bd5d0",
      "PARAM",
      [
        "storage",
        "002ad725",
        null,
        "string"
      ]
    ],
    [
      "004bd5d8",
      "PARAM",
      [
        "storage",
        "002b4cdd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bd500",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004bd5d0",
      "PARAM",
      [
        "storage",
        "002ad765",
        null,
        "string"
      ]
    ],
    [
      "004bd5d8",
      "PARAM",
      [
        "storage",
        "002b4d1d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bd4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bd/004bd218.md#insn-004bd4d0) · [`004bd598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bd/004bd218.md#insn-004bd598) · [`004bd5b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bd/004bd218.md#insn-004bd5b0)
- 新版 `004bd510`（命令位置の公開資料なし） · `004bd5d8`（命令位置の公開資料なし） · `004bd5f0`（命令位置の公開資料なし）

~~~diff
- 004bd4d0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004bd4d0 ["INT_ADD", "register:40f0:8", ["const:4bd4d0:8", "const:4:8"]]
- 004bd4d0 ["CALLIND", null, ["register:0:8"]]
+ 004bd510 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004bd510 ["INT_ADD", "register:40f0:8", ["const:4bd510:8", "const:4:8"]]
+ 004bd510 ["CALLIND", null, ["register:0:8"]]
- 004bd4d0 bytes 20013fd6
+ 004bd510 bytes 20013fd6
- 004bd598 ["COPY", "tmp:0:8", ["const:cdd:8"]]
- 004bd598 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004bd598 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004bd598 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004bd5d8 ["COPY", "tmp:0:8", ["const:d1d:8"]]
+ 004bd5d8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004bd5d8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004bd5d8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004bd598 bytes 21743391
+ 004bd5d8 bytes 21743491
- 004bd5b0 ["INT_ADD", "register:40f0:8", ["const:4bd5b0:8", "const:4:8"]]
- 004bd5b0 ["CALL", null, ["callee:00c58650:8"]]
+ 004bd5f0 ["INT_ADD", "register:40f0:8", ["const:4bd5f0:8", "const:4:8"]]
+ 004bd5f0 ["CALL", null, ["callee:00c58650:8"]]
- 004bd5b0 bytes 286b1e94
+ 004bd5f0 bytes 186c1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c74f72b19fa8996592d825027e242679"></a>

### [`004bd73c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bd/004bd73c.md) → [`004bd77c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bd/004bd77c.md) _ZN5Botan14CBC_Decryption7processEPhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c58250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58250.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58650.md)

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
    "old": {
      "definition_site": "004bd96c",
      "incomplete_value": false,
      "site": "004bd98c",
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "004bd974",
      "incomplete_value": false,
      "site": "004bd98c",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "004bd97c",
      "incomplete_value": false,
      "site": "004bd98c",
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
      "004bd9ac",
      "PARAM",
      [
        "storage",
        "002a8b53",
        null,
        "string"
      ]
    ],
    [
      "004bd9b4",
      "PARAM",
      [
        "storage",
        "002b0ae7",
        null,
        "string"
      ]
    ],
    [
      "004bd9bc",
      "PARAM",
      [
        "storage",
        "002a4053",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bd9ac",
      "PARAM",
      [
        "storage",
        "002a8c20",
        null,
        "string"
      ]
    ],
    [
      "004bd9b4",
      "PARAM",
      [
        "storage",
        "002b0b27",
        null,
        "string"
      ]
    ],
    [
      "004bd9bc",
      "PARAM",
      [
        "storage",
        "002a4120",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bd98c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bd/004bd73c.md#insn-004bd98c) · [`004bd7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bd/004bd73c.md#insn-004bd7d4) · [`004bd8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bd/004bd73c.md#insn-004bd8dc)
- 新版 `004bd9cc`（命令位置の公開資料なし） · `004bd814`（命令位置の公開資料なし） · `004bd91c`（命令位置の公開資料なし）

~~~diff
- 004bd98c ["INT_ADD", "register:40f0:8", ["const:4bd98c:8", "const:4:8"]]
- 004bd98c ["CALL", null, ["callee:00c58650:8"]]
+ 004bd9cc ["INT_ADD", "register:40f0:8", ["const:4bd9cc:8", "const:4:8"]]
+ 004bd9cc ["CALL", null, ["callee:00c58650:8"]]
- 004bd98c bytes 316a1e94
+ 004bd9cc bytes 216b1e94
- 004bd7d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 004bd7d4 ["INT_ADD", "register:40f0:8", ["const:4bd7d4:8", "const:4:8"]]
- 004bd7d4 ["CALLIND", null, ["register:0:8"]]
+ 004bd814 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bd814 ["INT_ADD", "register:40f0:8", ["const:4bd814:8", "const:4:8"]]
+ 004bd814 ["CALLIND", null, ["register:0:8"]]
- 004bd7d4 bytes 00013fd6
+ 004bd814 bytes 00013fd6
- 004bd8dc ["INT_ADD", "register:40f0:8", ["const:4bd8dc:8", "const:4:8"]]
- 004bd8dc ["CALL", null, ["callee:00c57f40:8"]]
+ 004bd91c ["INT_ADD", "register:40f0:8", ["const:4bd91c:8", "const:4:8"]]
+ 004bd91c ["CALL", null, ["callee:00c57f40:8"]]
- 004bd8dc bytes 99681e94
+ 004bd91c bytes 89691e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24a8cd55d47cf4a4134dfa9ddccc1bc8"></a>

### [`004bd990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bd/004bd990.md) → [`004bd9d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bd/004bd9d0.md) _ZN5Botan14CBC_Decryption6finishERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

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
    "old": {
      "definition_site": "004bdb60",
      "incomplete_value": false,
      "site": "004bdb68",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "004bdbb0",
      "incomplete_value": true,
      "site": "004bdbbc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bdbec",
      "incomplete_value": false,
      "site": "004bdbfc",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004bdbac",
      "incomplete_value": false,
      "site": "004bdbbc",
      "value": [
        "leaf",
        "const:535828:8"
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
      "004bdba0",
      "PARAM",
      [
        "storage",
        "002c1013",
        null,
        "string"
      ]
    ],
    [
      "004bdbec",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004bdbf0",
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
      "004bdba0",
      "PARAM",
      [
        "storage",
        "002c1053",
        null,
        "string"
      ]
    ],
    [
      "004bdbec",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004bdbf0",
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

- 旧版 [`004bdb68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bd/004bd990.md#insn-004bdb68) · [`004bdbbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bd/004bd990.md#insn-004bdbbc) · [`004bdbf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bd/004bd990.md#insn-004bdbf0)
- 新版 `004bdba8`（命令位置の公開資料なし） · `004bdbfc`（命令位置の公開資料なし） · `004bdc30`（命令位置の公開資料なし）

~~~diff
- 004bdb68 ["INT_ADD", "register:40f0:8", ["const:4bdb68:8", "const:4:8"]]
- 004bdb68 ["CALL", null, ["callee:00c57f70:8"]]
+ 004bdba8 ["INT_ADD", "register:40f0:8", ["const:4bdba8:8", "const:4:8"]]
+ 004bdba8 ["CALL", null, ["callee:00c57f70:8"]]
- 004bdb68 bytes 02681e94
+ 004bdba8 bytes f2681e94
- 004bdbbc ["INT_ADD", "register:40f0:8", ["const:4bdbbc:8", "const:4:8"]]
- 004bdbbc ["CALL", null, ["callee:00c57f10:8"]]
+ 004bdbfc ["INT_ADD", "register:40f0:8", ["const:4bdbfc:8", "const:4:8"]]
+ 004bdbfc ["CALL", null, ["callee:00c57f10:8"]]
- 004bdbbc bytes d5671e94
+ 004bdbfc bytes c5681e94
- 004bdbf0 ["COPY", "tmp:0:8", ["const:b9a:8"]]
- 004bdbf0 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 004bdbf0 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 004bdbf0 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 004bdc30 ["COPY", "tmp:0:8", ["const:c67:8"]]
+ 004bdc30 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 004bdc30 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 004bdc30 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 004bdbf0 bytes 63682e91
+ 004bdc30 bytes 639c3191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9c7f63373e219c0306d53855eb7ef55"></a>

### [`004bdd9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bd/004bdd9c.md) → [`004bdddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bd/004bdddc.md) _ZN5Botan14CTS_Decryption6finishERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 13件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00540264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540264.md) [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`005402a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005402a4.md) [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

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
    "old": {
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
    "ordinal": 9,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
    "ordinal": 11,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
      "004be150",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004be22c",
      "PARAM",
      [
        "storage",
        "002ad725",
        null,
        "string"
      ]
    ],
    [
      "004be234",
      "PARAM",
      [
        "storage",
        "002b4cdd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004be150",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004be22c",
      "PARAM",
      [
        "storage",
        "002ad765",
        null,
        "string"
      ]
    ],
    [
      "004be234",
      "PARAM",
      [
        "storage",
        "002b4d1d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004be120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bd/004bdd9c.md#insn-004be120) · [`004be1f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bd/004bdd9c.md#insn-004be1f4) · [`004be20c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bd/004bdd9c.md#insn-004be20c)
- 新版 `004be160`（命令位置の公開資料なし） · `004be234`（命令位置の公開資料なし） · `004be24c`（命令位置の公開資料なし）

~~~diff
- 004be120 ["COPY", "register:0:8", ["register:4048:8"]]
- 004be120 ["INT_ADD", "register:40f0:8", ["const:4be120:8", "const:4:8"]]
- 004be120 ["CALLIND", null, ["register:0:8"]]
+ 004be160 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004be160 ["INT_ADD", "register:40f0:8", ["const:4be160:8", "const:4:8"]]
+ 004be160 ["CALLIND", null, ["register:0:8"]]
- 004be120 bytes 20013fd6
+ 004be160 bytes 20013fd6
- 004be1f4 ["COPY", "tmp:0:8", ["const:cdd:8"]]
- 004be1f4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004be1f4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004be1f4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004be234 ["COPY", "tmp:0:8", ["const:d1d:8"]]
+ 004be234 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004be234 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004be234 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004be1f4 bytes 21743391
+ 004be234 bytes 21743491
- 004be20c ["INT_ADD", "register:40f0:8", ["const:4be20c:8", "const:4:8"]]
- 004be20c ["CALL", null, ["callee:00c58650:8"]]
+ 004be24c ["INT_ADD", "register:40f0:8", ["const:4be24c:8", "const:4:8"]]
+ 004be24c ["CALL", null, ["callee:00c58650:8"]]
- 004be20c bytes 11681e94
+ 004be24c bytes 01691e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3952f4bc0b7723234a720fadb9aea74"></a>

### [`004be3e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004be/004be3e4.md) → [`004be424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004be/004be424.md) _ZN5Botan5CPUID9to_stringEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c589a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c589a0.md) · 呼出先 8件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00440f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f1c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00c58da0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58da0.md) · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00440f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

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
    "old": {
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
    "ordinal": 54,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
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
    "ordinal": 59,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
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
    "old": {
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
      "004be454",
      "READ",
      [
        "storage",
        "00c9a918",
        null,
        "pointer"
      ]
    ],
    [
      "004be45c",
      "READ",
      [
        "storage",
        "00ca4e38",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ],
    [
      "004be574",
      "READ",
      [
        "storage",
        "00ca4e38",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004be454",
      "READ",
      [
        "storage",
        "00c9ad18",
        null,
        "pointer"
      ]
    ],
    [
      "004be45c",
      "READ",
      [
        "storage",
        "00ca5238",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ],
    [
      "004be574",
      "READ",
      [
        "storage",
        "00ca5238",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004be814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004be/004be3e4.md#insn-004be814) · [`004be414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004be/004be3e4.md#insn-004be414) · [`004be448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004be/004be3e4.md#insn-004be448)
- 新版 `004be854`（命令位置の公開資料なし） · `004be454`（命令位置の公開資料なし） · `004be488`（命令位置の公開資料なし）

~~~diff
- 004be814 ["INT_ADD", "register:40f0:8", ["const:4be814:8", "const:4:8"]]
- 004be814 ["CALL", null, ["callee:00c57e90:8"]]
+ 004be854 ["INT_ADD", "register:40f0:8", ["const:4be854:8", "const:4:8"]]
+ 004be854 ["CALL", null, ["callee:00c57e90:8"]]
- 004be814 bytes 9f641e94
+ 004be854 bytes 8f651e94
- 004be414 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:918:8"]]
- 004be414 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 004be454 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:d18:8"]]
+ 004be454 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 004be414 bytes 188f44f9
+ 004be454 bytes 188f46f9
- 004be448 ["INT_ADD", "register:40f0:8", ["const:4be448:8", "const:4:8"]]
- 004be448 ["CALL", null, ["callee:00c57e90:8"]]
+ 004be488 ["INT_ADD", "register:40f0:8", ["const:4be488:8", "const:4:8"]]
+ 004be488 ["CALL", null, ["callee:00c57e90:8"]]
- 004be448 bytes 92651e94
+ 004be488 bytes 82661e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10b0f3e1f05bfd7b3be66c7966fec204"></a>

### [`004beb5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004be/004beb5c.md) → [`004beb9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004be/004beb9c.md) _ZN5Botan5CPUID5printERNSt6__ndk113basic_ostreamIcNS1_11char_traitsIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00459490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c589a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c589a0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004594d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58da0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58da0.md)

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
    "old": {
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
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
      "004bebb8",
      "PARAM",
      [
        "storage",
        "002a64ec",
        null,
        "string"
      ]
    ],
    [
      "004bec00",
      "PARAM",
      [
        "storage",
        "002b4ba0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004bebb8",
      "PARAM",
      [
        "storage",
        "002a65c8",
        null,
        "string"
      ]
    ],
    [
      "004bec00",
      "PARAM",
      [
        "storage",
        "002b4be0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004beb88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004be/004beb5c.md#insn-004beb88) · [`004bebc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004be/004beb5c.md#insn-004bebc8) · [`004beb78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004be/004beb5c.md#insn-004beb78)
- 新版 `004bebc8`（命令位置の公開資料なし） · `004bec08`（命令位置の公開資料なし） · `004bebb8`（命令位置の公開資料なし）

~~~diff
- 004beb88 ["INT_ADD", "register:40f0:8", ["const:4beb88:8", "const:4:8"]]
- 004beb88 ["CALL", null, ["callee:004594d0:8"]]
+ 004bebc8 ["INT_ADD", "register:40f0:8", ["const:4bebc8:8", "const:4:8"]]
+ 004bebc8 ["CALL", null, ["callee:004594d0:8"]]
- 004beb88 bytes 426afe97
+ 004bebc8 bytes 426afe97
- 004bebc8 ["INT_ADD", "register:40f0:8", ["const:4bebc8:8", "const:4:8"]]
- 004bebc8 ["CALL", null, ["callee:004594d0:8"]]
+ 004bec08 ["INT_ADD", "register:40f0:8", ["const:4bec08:8", "const:4:8"]]
+ 004bec08 ["CALL", null, ["callee:004594d0:8"]]
- 004bebc8 bytes 326afe97
+ 004bec08 bytes 326afe97
- 004beb78 ["COPY", "tmp:0:8", ["const:4ec:8"]]
- 004beb78 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004beb78 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004beb78 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004bebb8 ["COPY", "tmp:0:8", ["const:5c8:8"]]
+ 004bebb8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004bebb8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004bebb8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004beb78 bytes 21b01391
+ 004bebb8 bytes 21201791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7c091e0208a3c212cee7a0ca04e0116"></a>

### [`004bec30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004be/004bec30.md) → [`004bec70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004be/004bec70.md) _ZN5Botan5CPUID10initializeEv

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
    "old": {
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
      "004bec78",
      "READ",
      [
        "storage",
        "00c9a918",
        null,
        "pointer"
      ]
    ],
    [
      "004bec7c",
      "WRITE",
      [
        "storage",
        "00ca4e38",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004bec78",
      "READ",
      [
        "storage",
        "00c9ad18",
        null,
        "pointer"
      ]
    ],
    [
      "004bec7c",
      "WRITE",
      [
        "storage",
        "00ca5238",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bec38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004be/004bec30.md#insn-004bec38)
- 新版 `004bec78`（命令位置の公開資料なし）

~~~diff
- 004bec38 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:918:8"]]
- 004bec38 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004bec78 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d18:8"]]
+ 004bec78 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004bec38 bytes 088d44f9
+ 004bec78 bytes 088d46f9
~~~


<a id="compare-bb2201c8d8722ab5f0661058c8d97b27"></a>

### [`004beeec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004be/004beeec.md) → [`004bef2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004be/004bef2c.md) _ZN5Botan8ECB_ModeC2EPNS_11BlockCipherEPNS_28BlockCipherModePaddingMethodE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c589b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c589b0.md) · 呼出先 8件 [`004a680c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a680c.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`00c58db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58db0.md) · 呼出先 8件 [`004a684c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a684c.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
    "old": {
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
    "ordinal": 4,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
      "004bef54",
      "READ",
      [
        "storage",
        "00c9aa48",
        null,
        "pointer"
      ]
    ],
    [
      "004bef68",
      "DATA",
      [
        "storage",
        "00c660d8",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "004befe8",
      "PARAM",
      [
        "storage",
        "002bb347",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bef54",
      "READ",
      [
        "storage",
        "00c9ae48",
        null,
        "pointer"
      ]
    ],
    [
      "004bef68",
      "DATA",
      [
        "storage",
        "00c664d8",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "004befe8",
      "PARAM",
      [
        "storage",
        "002bb387",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004befb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004be/004beeec.md#insn-004befb4) · [`004befdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004be/004beeec.md#insn-004befdc) · [`004bf028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004be/004beeec.md#insn-004bf028)
- 新版 `004beff4`（命令位置の公開資料なし） · `004bf01c`（命令位置の公開資料なし） · `004bf068`（命令位置の公開資料なし）

~~~diff
- 004befb4 ["INT_ADD", "register:40f0:8", ["const:4befb4:8", "const:4:8"]]
- 004befb4 ["CALL", null, ["callee:00c57f60:8"]]
+ 004beff4 ["INT_ADD", "register:40f0:8", ["const:4beff4:8", "const:4:8"]]
+ 004beff4 ["CALL", null, ["callee:00c57f60:8"]]
- 004befb4 bytes eb621e94
+ 004beff4 bytes db631e94
- 004befdc ["INT_ADD", "register:40f0:8", ["const:4befdc:8", "const:4:8"]]
- 004befdc ["CALL", null, ["callee:00c57f70:8"]]
+ 004bf01c ["INT_ADD", "register:40f0:8", ["const:4bf01c:8", "const:4:8"]]
+ 004bf01c ["CALL", null, ["callee:00c57f70:8"]]
- 004befdc bytes e5621e94
+ 004bf01c bytes d5631e94
- 004bf028 ["INT_ADD", "register:40f0:8", ["const:4bf028:8", "const:4:8"]]
- 004bf028 ["CALL", null, ["callee:00c57f70:8"]]
+ 004bf068 ["INT_ADD", "register:40f0:8", ["const:4bf068:8", "const:4:8"]]
+ 004bf068 ["CALL", null, ["callee:00c57f70:8"]]
- 004bf028 bytes d2621e94
+ 004bf068 bytes c2631e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15813837b9b77529fb2b745333b96d8e"></a>

### [`004bf1f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bf1f8.md) → [`004bf238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bf238.md) _ZNK5Botan8ECB_Mode4nameEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c589c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c589c0.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)
- 新版 呼出元 1件 [`00c58dc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58dc0.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md)

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
    "old": {
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
      "004bf278",
      "PARAM",
      [
        "storage",
        "002a64fa",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bf278",
      "PARAM",
      [
        "storage",
        "002a65d6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bf240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bf1f8.md#insn-004bf240) · [`004bf230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bf1f8.md#insn-004bf230) · [`004bf238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bf1f8.md#insn-004bf238)
- 新版 `004bf280`（命令位置の公開資料なし） · `004bf270`（命令位置の公開資料なし） · `004bf278`（命令位置の公開資料なし）

~~~diff
- 004bf240 ["INT_ADD", "register:40f0:8", ["const:4bf240:8", "const:4:8"]]
- 004bf240 ["CALL", null, ["callee:00c57f70:8"]]
+ 004bf280 ["INT_ADD", "register:40f0:8", ["const:4bf280:8", "const:4:8"]]
+ 004bf280 ["CALL", null, ["callee:00c57f70:8"]]
- 004bf240 bytes 4c621e94
+ 004bf280 bytes 3c631e94
- 004bf230 ["COPY", "register:0:8", ["register:4048:8"]]
- 004bf230 ["INT_ADD", "register:40f0:8", ["const:4bf230:8", "const:4:8"]]
- 004bf230 ["CALLIND", null, ["register:0:8"]]
+ 004bf270 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004bf270 ["INT_ADD", "register:40f0:8", ["const:4bf270:8", "const:4:8"]]
+ 004bf270 ["CALLIND", null, ["register:0:8"]]
- 004bf230 bytes 20013fd6
+ 004bf270 bytes 20013fd6
- 004bf238 ["COPY", "tmp:0:8", ["const:4fa:8"]]
- 004bf238 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004bf238 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004bf238 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004bf278 ["COPY", "tmp:0:8", ["const:5d6:8"]]
+ 004bf278 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004bf278 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004bf278 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004bf238 bytes 21e81391
+ 004bf278 bytes 21581791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05831b936d1cbecd93c34392edd33ccf"></a>

### [`004bf40c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bf40c.md) → [`004bf44c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bf44c.md) _ZN5Botan8ECB_Mode9start_msgEPKhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c58990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58990.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c58d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58d90.md)

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
    "old": {
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bf4f0",
      "incomplete_value": false,
      "site": "004bf500",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004bf4b0",
      "incomplete_value": false,
      "site": "004bf4c0",
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
      "004bf4f0",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004bf4f4",
      "READ",
      [
        "storage",
        "00c9aa40",
        null,
        "pointer"
      ]
    ],
    [
      "004bf4f4",
      "PARAM",
      [
        "storage",
        "00c660b0",
        "_ZTIN5Botan17Invalid_IV_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004bf4f0",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004bf4f4",
      "READ",
      [
        "storage",
        "00c9ae40",
        null,
        "pointer"
      ]
    ],
    [
      "004bf4f4",
      "PARAM",
      [
        "storage",
        "00c664b0",
        "_ZTIN5Botan17Invalid_IV_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bf4c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bf40c.md#insn-004bf4c0) · [`004bf464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bf40c.md#insn-004bf464) · [`004bf47c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bf40c.md#insn-004bf47c)
- 新版 `004bf500`（命令位置の公開資料なし） · `004bf4a4`（命令位置の公開資料なし） · `004bf4bc`（命令位置の公開資料なし）

~~~diff
- 004bf4c0 ["INT_ADD", "register:40f0:8", ["const:4bf4c0:8", "const:4:8"]]
- 004bf4c0 ["CALL", null, ["callee:00c57f10:8"]]
+ 004bf500 ["INT_ADD", "register:40f0:8", ["const:4bf500:8", "const:4:8"]]
+ 004bf500 ["CALL", null, ["callee:00c57f10:8"]]
- 004bf4c0 bytes 94611e94
+ 004bf500 bytes 84621e94
- 004bf464 ["INT_ADD", "register:40f0:8", ["const:4bf464:8", "const:4:8"]]
- 004bf464 ["CALL", null, ["callee:00c57ef0:8"]]
+ 004bf4a4 ["INT_ADD", "register:40f0:8", ["const:4bf4a4:8", "const:4:8"]]
+ 004bf4a4 ["CALL", null, ["callee:00c57ef0:8"]]
- 004bf464 bytes a3611e94
+ 004bf4a4 bytes 93621e94
- 004bf47c ["COPY", "register:0:8", ["register:4048:8"]]
- 004bf47c ["INT_ADD", "register:40f0:8", ["const:4bf47c:8", "const:4:8"]]
- 004bf47c ["CALLIND", null, ["register:0:8"]]
+ 004bf4bc ["COPY", "register:0:8", ["register:4048:8"]]
+ 004bf4bc ["INT_ADD", "register:40f0:8", ["const:4bf4bc:8", "const:4:8"]]
+ 004bf4bc ["CALLIND", null, ["register:0:8"]]
- 004bf47c bytes 20013fd6
+ 004bf4bc bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c05c57b6b10f6a8d39341a5225c3298"></a>

### [`004bf51c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bf51c.md) → [`004bf55c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bf55c.md) _ZNK5Botan14ECB_Encryption13output_lengthEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58250.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58650.md)

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
    "old": {
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
      "004bf5ac",
      "PARAM",
      [
        "storage",
        "002a1ff2",
        null,
        "string"
      ]
    ],
    [
      "004bf5b4",
      "PARAM",
      [
        "storage",
        "002ab57d",
        null,
        "string"
      ]
    ],
    [
      "004bf5bc",
      "PARAM",
      [
        "storage",
        "002b8265",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bf5ac",
      "PARAM",
      [
        "storage",
        "002a20bf",
        null,
        "string"
      ]
    ],
    [
      "004bf5b4",
      "PARAM",
      [
        "storage",
        "002ab5bd",
        null,
        "string"
      ]
    ],
    [
      "004bf5bc",
      "PARAM",
      [
        "storage",
        "002b82a5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bf58c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bf51c.md#insn-004bf58c) · [`004bf538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bf51c.md#insn-004bf538) · [`004bf568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bf51c.md#insn-004bf568)
- 新版 `004bf5cc`（命令位置の公開資料なし） · `004bf578`（命令位置の公開資料なし） · `004bf5a8`（命令位置の公開資料なし）

~~~diff
- 004bf58c ["INT_ADD", "register:40f0:8", ["const:4bf58c:8", "const:4:8"]]
- 004bf58c ["CALL", null, ["callee:00c58650:8"]]
+ 004bf5cc ["INT_ADD", "register:40f0:8", ["const:4bf5cc:8", "const:4:8"]]
+ 004bf5cc ["CALL", null, ["callee:00c58650:8"]]
- 004bf58c bytes 31631e94
+ 004bf5cc bytes 21641e94
- 004bf538 ["COPY", "register:0:8", ["register:4040:8"]]
- 004bf538 ["INT_ADD", "register:40f0:8", ["const:4bf538:8", "const:4:8"]]
- 004bf538 ["CALLIND", null, ["register:0:8"]]
+ 004bf578 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bf578 ["INT_ADD", "register:40f0:8", ["const:4bf578:8", "const:4:8"]]
+ 004bf578 ["CALLIND", null, ["register:0:8"]]
- 004bf538 bytes 00013fd6
+ 004bf578 bytes 00013fd6
- 004bf568 ["COPY", "register:4000:8", ["const:2a1000:8"]]
+ 004bf5a8 ["COPY", "register:4000:8", ["const:2a2000:8"]]
- 004bf568 bytes 00efffd0
+ 004bf5a8 bytes 00effff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e50aa8aea069c987e605fdacc07518c"></a>

### [`004bf590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bf590.md) → [`004bf5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bf5d0.md) _ZN5Botan14ECB_Encryption7processEPhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58250.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58650.md)

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
    "old": {
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
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
      "004bf638",
      "PARAM",
      [
        "storage",
        "002a8b53",
        null,
        "string"
      ]
    ],
    [
      "004bf640",
      "PARAM",
      [
        "storage",
        "002a3028",
        null,
        "string"
      ]
    ],
    [
      "004bf648",
      "PARAM",
      [
        "storage",
        "002a4053",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bf638",
      "PARAM",
      [
        "storage",
        "002a8c20",
        null,
        "string"
      ]
    ],
    [
      "004bf640",
      "PARAM",
      [
        "storage",
        "002a30f5",
        null,
        "string"
      ]
    ],
    [
      "004bf648",
      "PARAM",
      [
        "storage",
        "002a4120",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bf618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bf590.md#insn-004bf618) · [`004bf5b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bf590.md#insn-004bf5b8) · [`004bf5dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bf590.md#insn-004bf5dc)
- 新版 `004bf658`（命令位置の公開資料なし） · `004bf5f8`（命令位置の公開資料なし） · `004bf61c`（命令位置の公開資料なし）

~~~diff
- 004bf618 ["INT_ADD", "register:40f0:8", ["const:4bf618:8", "const:4:8"]]
- 004bf618 ["CALL", null, ["callee:00c58650:8"]]
+ 004bf658 ["INT_ADD", "register:40f0:8", ["const:4bf658:8", "const:4:8"]]
+ 004bf658 ["CALL", null, ["callee:00c58650:8"]]
- 004bf618 bytes 0e631e94
+ 004bf658 bytes fe631e94
- 004bf5b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004bf5b8 ["INT_ADD", "register:40f0:8", ["const:4bf5b8:8", "const:4:8"]]
- 004bf5b8 ["CALLIND", null, ["register:0:8"]]
+ 004bf5f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bf5f8 ["INT_ADD", "register:40f0:8", ["const:4bf5f8:8", "const:4:8"]]
+ 004bf5f8 ["CALLIND", null, ["register:0:8"]]
- 004bf5b8 bytes 00013fd6
+ 004bf5f8 bytes 00013fd6
- 004bf5dc ["COPY", "register:0:8", ["register:4040:8"]]
- 004bf5dc ["INT_ADD", "register:40f0:8", ["const:4bf5dc:8", "const:4:8"]]
- 004bf5dc ["CALLIND", null, ["register:0:8"]]
+ 004bf61c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bf61c ["INT_ADD", "register:40f0:8", ["const:4bf61c:8", "const:4:8"]]
+ 004bf61c ["CALLIND", null, ["register:0:8"]]
- 004bf5dc bytes 00013fd6
+ 004bf61c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22941e62c338c3e92e383cd5259c4c2f"></a>

### [`004bf61c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bf61c.md) → [`004bf65c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bf65c.md) _ZN5Botan14ECB_Encryption6finishERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
    "old": {
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
      "004bf788",
      "PARAM",
      [
        "storage",
        "002ad725",
        null,
        "string"
      ]
    ],
    [
      "004bf790",
      "PARAM",
      [
        "storage",
        "002b4cdd",
        null,
        "string"
      ]
    ],
    [
      "004bf798",
      "PARAM",
      [
        "storage",
        "002ba20d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bf788",
      "PARAM",
      [
        "storage",
        "002ad765",
        null,
        "string"
      ]
    ],
    [
      "004bf790",
      "PARAM",
      [
        "storage",
        "002b4d1d",
        null,
        "string"
      ]
    ],
    [
      "004bf798",
      "PARAM",
      [
        "storage",
        "002ba24d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bf768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bf61c.md#insn-004bf768) · [`004bf794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bf61c.md#insn-004bf794) · [`004bf7e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bf61c.md#insn-004bf7e8)
- 新版 `004bf7a8`（命令位置の公開資料なし） · `004bf7d4`（命令位置の公開資料なし） · `004bf828`（命令位置の公開資料なし）

~~~diff
- 004bf768 ["INT_ADD", "register:40f0:8", ["const:4bf768:8", "const:4:8"]]
- 004bf768 ["CALL", null, ["callee:00c58650:8"]]
+ 004bf7a8 ["INT_ADD", "register:40f0:8", ["const:4bf7a8:8", "const:4:8"]]
+ 004bf7a8 ["CALL", null, ["callee:00c58650:8"]]
- 004bf768 bytes ba621e94
+ 004bf7a8 bytes aa631e94
- 004bf794 ["INT_ADD", "register:40f0:8", ["const:4bf794:8", "const:4:8"]]
- 004bf794 ["CALL", null, ["callee:00c57f60:8"]]
+ 004bf7d4 ["INT_ADD", "register:40f0:8", ["const:4bf7d4:8", "const:4:8"]]
+ 004bf7d4 ["CALL", null, ["callee:00c57f60:8"]]
- 004bf794 bytes f3601e94
+ 004bf7d4 bytes e3611e94
- 004bf7e8 ["INT_ADD", "register:40f0:8", ["const:4bf7e8:8", "const:4:8"]]
- 004bf7e8 ["CALL", null, ["callee:00c57f10:8"]]
+ 004bf828 ["INT_ADD", "register:40f0:8", ["const:4bf828:8", "const:4:8"]]
+ 004bf828 ["CALL", null, ["callee:00c57f10:8"]]
- 004bf7e8 bytes ca601e94
+ 004bf828 bytes ba611e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b996cc75d4261911be8516fcbf07e87"></a>

### [`004bf8b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bf8b0.md) → [`004bf8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bf8f0.md) _ZN5Botan14ECB_Decryption7processEPhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58250.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58650.md)

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
    "old": {
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
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
      "004bf958",
      "PARAM",
      [
        "storage",
        "002a8b53",
        null,
        "string"
      ]
    ],
    [
      "004bf960",
      "PARAM",
      [
        "storage",
        "002b0ae7",
        null,
        "string"
      ]
    ],
    [
      "004bf968",
      "PARAM",
      [
        "storage",
        "002a4053",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004bf958",
      "PARAM",
      [
        "storage",
        "002a8c20",
        null,
        "string"
      ]
    ],
    [
      "004bf960",
      "PARAM",
      [
        "storage",
        "002b0b27",
        null,
        "string"
      ]
    ],
    [
      "004bf968",
      "PARAM",
      [
        "storage",
        "002a4120",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004bf938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bf8b0.md#insn-004bf938) · [`004bf8d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bf8b0.md#insn-004bf8d8) · [`004bf8fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bf8b0.md#insn-004bf8fc)
- 新版 `004bf978`（命令位置の公開資料なし） · `004bf918`（命令位置の公開資料なし） · `004bf93c`（命令位置の公開資料なし）

~~~diff
- 004bf938 ["INT_ADD", "register:40f0:8", ["const:4bf938:8", "const:4:8"]]
- 004bf938 ["CALL", null, ["callee:00c58650:8"]]
+ 004bf978 ["INT_ADD", "register:40f0:8", ["const:4bf978:8", "const:4:8"]]
+ 004bf978 ["CALL", null, ["callee:00c58650:8"]]
- 004bf938 bytes 46621e94
+ 004bf978 bytes 36631e94
- 004bf8d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004bf8d8 ["INT_ADD", "register:40f0:8", ["const:4bf8d8:8", "const:4:8"]]
- 004bf8d8 ["CALLIND", null, ["register:0:8"]]
+ 004bf918 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bf918 ["INT_ADD", "register:40f0:8", ["const:4bf918:8", "const:4:8"]]
+ 004bf918 ["CALLIND", null, ["register:0:8"]]
- 004bf8d8 bytes 00013fd6
+ 004bf918 bytes 00013fd6
- 004bf8fc ["COPY", "register:0:8", ["register:4040:8"]]
- 004bf8fc ["INT_ADD", "register:40f0:8", ["const:4bf8fc:8", "const:4:8"]]
- 004bf8fc ["CALLIND", null, ["register:0:8"]]
+ 004bf93c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bf93c ["INT_ADD", "register:40f0:8", ["const:4bf93c:8", "const:4:8"]]
+ 004bf93c ["CALLIND", null, ["register:0:8"]]
- 004bf8fc bytes 00013fd6
+ 004bf93c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1439c79d0fad0ca31eb419a6fd25e82f"></a>

### [`004bf93c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bf93c.md) → [`004bf97c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bf97c.md) _ZN5Botan14ECB_Decryption6finishERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
    "old": {
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bfb38",
      "incomplete_value": false,
      "site": "004bfb48",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004bfaf8",
      "incomplete_value": false,
      "site": "004bfb08",
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
      "004bfaec",
      "PARAM",
      [
        "storage",
        "002c1013",
        null,
        "string"
      ]
    ],
    [
      "004bfb38",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004bfb3c",
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
      "004bfaec",
      "PARAM",
      [
        "storage",
        "002c1053",
        null,
        "string"
      ]
    ],
    [
      "004bfb38",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004bfb3c",
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

- 旧版 [`004bfab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bf93c.md#insn-004bfab4) · [`004bfb08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bf93c.md#insn-004bfb08) · [`004bfb38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bf93c.md#insn-004bfb38)
- 新版 `004bfaf4`（命令位置の公開資料なし） · `004bfb48`（命令位置の公開資料なし） · `004bfb78`（命令位置の公開資料なし）

~~~diff
- 004bfab4 ["INT_ADD", "register:40f0:8", ["const:4bfab4:8", "const:4:8"]]
- 004bfab4 ["CALL", null, ["callee:00c57f70:8"]]
+ 004bfaf4 ["INT_ADD", "register:40f0:8", ["const:4bfaf4:8", "const:4:8"]]
+ 004bfaf4 ["CALL", null, ["callee:00c57f70:8"]]
- 004bfab4 bytes 2f601e94
+ 004bfaf4 bytes 1f611e94
- 004bfb08 ["INT_ADD", "register:40f0:8", ["const:4bfb08:8", "const:4:8"]]
- 004bfb08 ["CALL", null, ["callee:00c57f10:8"]]
+ 004bfb48 ["INT_ADD", "register:40f0:8", ["const:4bfb48:8", "const:4:8"]]
+ 004bfb48 ["CALL", null, ["callee:00c57f10:8"]]
- 004bfb08 bytes 02601e94
+ 004bfb48 bytes f2601e94
- 004bfb38 ["COPY", "tmp:0:8", ["const:267:8"]]
- 004bfb38 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 004bfb38 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 004bfb38 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 004bfb78 ["COPY", "tmp:0:8", ["const:dcb:8"]]
+ 004bfb78 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 004bfb78 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 004bfb78 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 004bfb38 bytes 639c0991
+ 004bfb78 bytes 632c3791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92681fc3fbc745264fd23270c4288f56"></a>

### [`004bfcc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bfcc4.md) → [`004bfd04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bfd04.md) _ZN5Botan13EMSA_PKCS1v1511encoding_ofERKNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEmRNS_21RandomNumberGeneratorE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004bfdf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bfdf8.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004bfe38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bfe38.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

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
    "old": {
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bfdd8",
      "incomplete_value": false,
      "site": "004bfde8",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004bfd98",
      "incomplete_value": false,
      "site": "004bfda8",
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
      "004bfda4",
      "PARAM",
      [
        "storage",
        "002b4cec",
        null,
        "string"
      ]
    ],
    [
      "004bfdd8",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004bfddc",
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
      "004bfda4",
      "PARAM",
      [
        "storage",
        "002b4d2c",
        null,
        "string"
      ]
    ],
    [
      "004bfdd8",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004bfddc",
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

- 旧版 [`004bfd6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bfcc4.md#insn-004bfd6c) · [`004bfda8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bfcc4.md#insn-004bfda8) · [`004bfd0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bfcc4.md#insn-004bfd0c)
- 新版 `004bfdac`（命令位置の公開資料なし） · `004bfde8`（命令位置の公開資料なし） · `004bfd4c`（命令位置の公開資料なし）

~~~diff
- 004bfd6c ["INT_ADD", "register:40f0:8", ["const:4bfd6c:8", "const:4:8"]]
- 004bfd6c ["CALL", null, ["callee:0043ddd8:8"]]
+ 004bfdac ["INT_ADD", "register:40f0:8", ["const:4bfdac:8", "const:4:8"]]
+ 004bfdac ["CALL", null, ["callee:0043ddd8:8"]]
- 004bfd6c bytes 0bf8fd97
+ 004bfdac bytes 0bf8fd97
- 004bfda8 ["INT_ADD", "register:40f0:8", ["const:4bfda8:8", "const:4:8"]]
- 004bfda8 ["CALL", null, ["callee:00c57f10:8"]]
+ 004bfde8 ["INT_ADD", "register:40f0:8", ["const:4bfde8:8", "const:4:8"]]
+ 004bfde8 ["CALL", null, ["callee:00c57f10:8"]]
- 004bfda8 bytes 5a5f1e94
+ 004bfde8 bytes 4a601e94
- 004bfd0c ["COPY", "register:0:8", ["register:4040:8"]]
- 004bfd0c ["INT_ADD", "register:40f0:8", ["const:4bfd0c:8", "const:4:8"]]
- 004bfd0c ["CALLIND", null, ["register:0:8"]]
+ 004bfd4c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bfd4c ["INT_ADD", "register:40f0:8", ["const:4bfd4c:8", "const:4:8"]]
+ 004bfd4c ["CALLIND", null, ["register:0:8"]]
- 004bfd0c bytes 00013fd6
+ 004bfd4c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90ad6b0cd63fe7bdfa80617367053ae3"></a>

### [`004bfdf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bfdf8.md) → [`004bfe38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bfe38.md) FUN_004bfe38

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`004bfcc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bfcc4.md) [`004c0034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c0/004c0034.md) [`004c16cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c16cc.md) [`004c16e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c16e4.md) · 呼出先 10件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 4件 [`004bfd04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bfd04.md) [`004c0074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c0074.md) [`004c170c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c1/004c170c.md) [`004c1724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c1/004c1724.md) · 呼出先 10件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

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
    "old": {
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004bffcc",
      "incomplete_value": false,
      "site": "004bffdc",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004bff8c",
      "incomplete_value": false,
      "site": "004bff9c",
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
      "004bff98",
      "PARAM",
      [
        "storage",
        "002a8c51",
        null,
        "string"
      ]
    ],
    [
      "004bffcc",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004bffd0",
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
      "004bff98",
      "PARAM",
      [
        "storage",
        "002a8d1e",
        null,
        "string"
      ]
    ],
    [
      "004bffcc",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004bffd0",
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

- 旧版 [`004bff60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bfdf8.md#insn-004bff60) · [`004bff9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bfdf8.md#insn-004bff9c) · [`004bffd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bfdf8.md#insn-004bffd4)
- 新版 `004bffa0`（命令位置の公開資料なし） · `004bffdc`（命令位置の公開資料なし） · `004c0014`（命令位置の公開資料なし）

~~~diff
- 004bff60 ["INT_ADD", "register:40f0:8", ["const:4bff60:8", "const:4:8"]]
- 004bff60 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004bffa0 ["INT_ADD", "register:40f0:8", ["const:4bffa0:8", "const:4:8"]]
+ 004bffa0 ["CALL", null, ["callee:0043ddd8:8"]]
- 004bff60 bytes 8ef7fd97
+ 004bffa0 bytes 8ef7fd97
- 004bff9c ["INT_ADD", "register:40f0:8", ["const:4bff9c:8", "const:4:8"]]
- 004bff9c ["CALL", null, ["callee:00c57f10:8"]]
+ 004bffdc ["INT_ADD", "register:40f0:8", ["const:4bffdc:8", "const:4:8"]]
+ 004bffdc ["CALL", null, ["callee:00c57f10:8"]]
- 004bff9c bytes dd5e1e94
+ 004bffdc bytes cd5f1e94
- 004bffd4 ["INT_ADD", "register:40f0:8", ["const:4bffd4:8", "const:4:8"]]
- 004bffd4 ["CALL", null, ["callee:00c58650:8"]]
+ 004c0014 ["INT_ADD", "register:40f0:8", ["const:4c0014:8", "const:4:8"]]
+ 004c0014 ["CALL", null, ["callee:00c58650:8"]]
- 004bffd4 bytes 9f601e94
+ 004c0014 bytes 8f611e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85741ddd326190d42799928dcf020ef3"></a>

### [`004c0034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c0/004c0034.md) → [`004c0074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c0074.md) _ZN5Botan13EMSA_PKCS1v156verifyERKNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEES7_m

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`004bfdf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bfdf8.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004bfe38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bfe38.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)

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
    "old": {
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
      "004c0128",
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
      "004c0128",
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

- 旧版 [`004c00f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c0/004c0034.md#insn-004c00f8) · [`004c007c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c0/004c0034.md#insn-004c007c) · [`004c009c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c0/004c0034.md#insn-004c009c)
- 新版 `004c0138`（命令位置の公開資料なし） · `004c00bc`（命令位置の公開資料なし） · `004c00dc`（命令位置の公開資料なし）

~~~diff
- 004c00f8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c00f8 ["INT_ADD", "register:40f0:8", ["const:4c00f8:8", "const:4:8"]]
- 004c00f8 ["CALLIND", null, ["register:0:8"]]
+ 004c0138 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c0138 ["INT_ADD", "register:40f0:8", ["const:4c0138:8", "const:4:8"]]
+ 004c0138 ["CALLIND", null, ["register:0:8"]]
- 004c00f8 bytes 20013fd6
+ 004c0138 bytes 20013fd6
- 004c007c ["COPY", "register:0:8", ["register:4040:8"]]
- 004c007c ["INT_ADD", "register:40f0:8", ["const:4c007c:8", "const:4:8"]]
- 004c007c ["CALLIND", null, ["register:0:8"]]
+ 004c00bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c00bc ["INT_ADD", "register:40f0:8", ["const:4c00bc:8", "const:4:8"]]
+ 004c00bc ["CALLIND", null, ["register:0:8"]]
- 004c007c bytes 00013fd6
+ 004c00bc bytes 00013fd6
- 004c009c ["INT_ADD", "register:40f0:8", ["const:4c009c:8", "const:4:8"]]
- 004c009c ["CALL", null, ["callee:004bfe38:8"]]
+ 004c00dc ["INT_ADD", "register:40f0:8", ["const:4c00dc:8", "const:4:8"]]
+ 004c00dc ["CALL", null, ["callee:004bfe38:8"]]
- 004c009c bytes 57ffff97
+ 004c00dc bytes 57ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e174f677e1e99ee94277d9584f331721"></a>

### [`004c0148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c0/004c0148.md) → [`004c0188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c0188.md) _ZNK5Botan13EMSA_PKCS1v1515config_for_x509ERKNS_11Private_KeyERKNSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 15件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004c0774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c0/004c0774.md) [`004c0928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c0/004c0928.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 15件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004c07b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c07b4.md) [`004c0968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c0968.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
    "old": {
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
      "004c02b8",
      "READ",
      [
        "storage",
        "00c9a938",
        null,
        "pointer"
      ]
    ],
    [
      "004c02c4",
      "DATA",
      [
        "storage",
        "00c65da8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004c030c",
      "PARAM",
      [
        "storage",
        "002a5276",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004c02b8",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "004c02c4",
      "DATA",
      [
        "storage",
        "00c661a8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004c030c",
      "PARAM",
      [
        "storage",
        "002a5352",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c02c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c0/004c0148.md#insn-004c02c4) · [`004c02d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c0/004c0148.md#insn-004c02d4) · [`004c0490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c0/004c0148.md#insn-004c0490)
- 新版 `004c0304`（命令位置の公開資料なし） · `004c0314`（命令位置の公開資料なし） · `004c04d0`（命令位置の公開資料なし）

~~~diff
- 004c02c4 ["COPY", "register:0:8", ["register:4050:8"]]
- 004c02c4 ["INT_ADD", "register:40f0:8", ["const:4c02c4:8", "const:4:8"]]
- 004c02c4 ["CALLIND", null, ["register:0:8"]]
+ 004c0304 ["COPY", "register:0:8", ["register:4050:8"]]
+ 004c0304 ["INT_ADD", "register:40f0:8", ["const:4c0304:8", "const:4:8"]]
+ 004c0304 ["CALLIND", null, ["register:0:8"]]
- 004c02c4 bytes 40013fd6
+ 004c0304 bytes 40013fd6
- 004c02d4 ["INT_ADD", "register:40f0:8", ["const:4c02d4:8", "const:4:8"]]
- 004c02d4 ["CALL", null, ["callee:00c57f70:8"]]
+ 004c0314 ["INT_ADD", "register:40f0:8", ["const:4c0314:8", "const:4:8"]]
+ 004c0314 ["CALL", null, ["callee:00c57f70:8"]]
- 004c02d4 bytes 275e1e94
+ 004c0314 bytes 175f1e94
- 004c0490 ["INT_ADD", "register:40f0:8", ["const:4c0490:8", "const:4:8"]]
- 004c0490 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004c04d0 ["INT_ADD", "register:40f0:8", ["const:4c04d0:8", "const:4:8"]]
+ 004c04d0 ["CALL", null, ["callee:0043ddd8:8"]]
- 004c0490 bytes 42f6fd97
+ 004c04d0 bytes 42f6fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dde565b11900bb8332bcfc8ede1d3f81"></a>

### [`004c0928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c0/004c0928.md) → [`004c0968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c0968.md) FUN_004c0968

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004c0148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c0/004c0148.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 1件 [`004c0188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c0188.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f60.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

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
    "old": {
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
    "ordinal": 1,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
      "004c09a0",
      "PARAM",
      [
        "storage",
        "002bedcc",
        null,
        "string"
      ]
    ],
    [
      "004c09cc",
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
      "004c09a0",
      "PARAM",
      [
        "storage",
        "002bee0c",
        null,
        "string"
      ]
    ],
    [
      "004c09cc",
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

- 旧版 [`004c096c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c0/004c0928.md#insn-004c096c) · [`004c0994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c0/004c0928.md#insn-004c0994) · [`004c0958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c0/004c0928.md#insn-004c0958)
- 新版 `004c09ac`（命令位置の公開資料なし） · `004c09d4`（命令位置の公開資料なし） · `004c0998`（命令位置の公開資料なし）

~~~diff
- 004c096c ["INT_ADD", "register:40f0:8", ["const:4c096c:8", "const:4:8"]]
- 004c096c ["CALL", null, ["callee:00c57f60:8"]]
+ 004c09ac ["INT_ADD", "register:40f0:8", ["const:4c09ac:8", "const:4:8"]]
+ 004c09ac ["CALL", null, ["callee:00c57f60:8"]]
- 004c096c bytes 7d5c1e94
+ 004c09ac bytes 6d5d1e94
- 004c0994 ["INT_ADD", "register:40f0:8", ["const:4c0994:8", "const:4:8"]]
- 004c0994 ["CALL", null, ["callee:00c57f70:8"]]
+ 004c09d4 ["INT_ADD", "register:40f0:8", ["const:4c09d4:8", "const:4:8"]]
+ 004c09d4 ["CALL", null, ["callee:00c57f70:8"]]
- 004c0994 bytes 775c1e94
+ 004c09d4 bytes 675d1e94
- 004c0958 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c0958 ["INT_ADD", "register:40f0:8", ["const:4c0958:8", "const:4:8"]]
- 004c0958 ["CALLIND", null, ["register:0:8"]]
+ 004c0998 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c0998 ["INT_ADD", "register:40f0:8", ["const:4c0998:8", "const:4:8"]]
+ 004c0998 ["CALLIND", null, ["register:0:8"]]
- 004c0958 bytes 20013fd6
+ 004c0998 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55bc6e700bcef9455c51389914b254a4"></a>

### [`004c0a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c0/004c0a7c.md) → [`004c0abc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c0abc.md) _ZN5Botan13EMSA_PKCS1v15C2EPNS_12HashFunctionE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c59110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59110.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c589e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c589e0.md)
- 新版 呼出元 1件 [`00c59510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59510.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58de0.md)

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
    "old": {
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
      "004c0ae0",
      "READ",
      [
        "storage",
        "00c9aa50",
        null,
        "pointer"
      ]
    ],
    [
      "004c0af8",
      "DATA",
      [
        "storage",
        "00c66178",
        null,
        "undefined1[88]"
      ]
    ]
  ],
  "added": [
    [
      "004c0ae0",
      "READ",
      [
        "storage",
        "00c9ae50",
        null,
        "pointer"
      ]
    ],
    [
      "004c0af8",
      "DATA",
      [
        "storage",
        "00c66578",
        null,
        "undefined1[88]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c0aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c0/004c0a7c.md#insn-004c0aa0) · [`004c0aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c0/004c0a7c.md#insn-004c0aa4) · [`004c0ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c0/004c0a7c.md#insn-004c0ad0)
- 新版 `004c0ae0`（命令位置の公開資料なし） · `004c0b10`（命令位置の公開資料なし）

~~~diff
- 004c0aa0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a50:8"]]
- 004c0aa0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c0ae0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e50:8"]]
+ 004c0ae0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c0aa0 bytes 292945f9
+ 004c0ae0 bytes 292947f9
- 004c0aa4 ["COPY", "register:4098:8", ["register:4000:8"]]
- 004c0aa4 bytes f30300aa
- 004c0ad0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c0ad0 ["INT_ADD", "register:40f0:8", ["const:4c0ad0:8", "const:4:8"]]
- 004c0ad0 ["CALLIND", null, ["register:0:8"]]
+ 004c0b10 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c0b10 ["INT_ADD", "register:40f0:8", ["const:4c0b10:8", "const:4:8"]]
+ 004c0b10 ["CALLIND", null, ["register:0:8"]]
- 004c0ad0 bytes 20013fd6
+ 004c0b10 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-600890db57d4773941a6ff5f7e49a60d"></a>

### [`004c0ba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c0/004c0ba4.md) → [`004c0be4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c0be4.md) _ZN5Botan12pkcs_hash_idERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c589e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c589e0.md) · 呼出先 9件 [`00441e54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441e54.md) [`004cc14c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc14c.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`00c58de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58de0.md) · 呼出先 9件 [`00441e94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441e94.md) [`004cc18c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cc/004cc18c.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

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
    "old": {
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
      "004c0d3c",
      "READ",
      [
        "storage",
        "002cae86",
        null,
        null
      ]
    ],
    [
      "004c0dfc",
      "PARAM",
      [
        "storage",
        "002ae77e",
        null,
        "string"
      ]
    ],
    [
      "004c0e20",
      "PARAM",
      [
        "storage",
        "002caeb6",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004c0d3c",
      "READ",
      [
        "storage",
        "002caec6",
        null,
        null
      ]
    ],
    [
      "004c0dfc",
      "PARAM",
      [
        "storage",
        "002ae7be",
        null,
        "string"
      ]
    ],
    [
      "004c0e20",
      "PARAM",
      [
        "storage",
        "002caef6",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c0dc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c0/004c0ba4.md#insn-004c0dc4) · [`004c0df4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c0/004c0ba4.md#insn-004c0df4) · [`004c0e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c0/004c0ba4.md#insn-004c0e24)
- 新版 `004c0e04`（命令位置の公開資料なし） · `004c0e34`（命令位置の公開資料なし） · `004c0e64`（命令位置の公開資料なし）

~~~diff
- 004c0dc4 ["INT_ADD", "register:40f0:8", ["const:4c0dc4:8", "const:4:8"]]
- 004c0dc4 ["CALL", null, ["callee:00441e94:8"]]
+ 004c0e04 ["INT_ADD", "register:40f0:8", ["const:4c0e04:8", "const:4:8"]]
+ 004c0e04 ["CALL", null, ["callee:00441e94:8"]]
- 004c0dc4 bytes 2404fe97
+ 004c0e04 bytes 2404fe97
- 004c0df4 ["INT_ADD", "register:40f0:8", ["const:4c0df4:8", "const:4:8"]]
- 004c0df4 ["CALL", null, ["callee:00441e94:8"]]
+ 004c0e34 ["INT_ADD", "register:40f0:8", ["const:4c0e34:8", "const:4:8"]]
+ 004c0e34 ["CALL", null, ["callee:00441e94:8"]]
- 004c0df4 bytes 1804fe97
+ 004c0e34 bytes 1804fe97
- 004c0e24 ["INT_ADD", "register:40f0:8", ["const:4c0e24:8", "const:4:8"]]
- 004c0e24 ["CALL", null, ["callee:00441e94:8"]]
+ 004c0e64 ["INT_ADD", "register:40f0:8", ["const:4c0e64:8", "const:4:8"]]
+ 004c0e64 ["CALL", null, ["callee:00441e94:8"]]
- 004c0e24 bytes 0c04fe97
+ 004c0e64 bytes 0c04fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f796e2883ec50acd0e07eb16af78599"></a>

### [`004c10e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c10e4.md) → [`004c1124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c1/004c1124.md) _ZN5Botan17EMSA_PKCS1v15_RawC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59100.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c589e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c589e0.md) [`00c589f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c589f0.md)
- 新版 呼出元 1件 [`00c59500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59500.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58de0.md) [`00c58df0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58df0.md)

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
    "old": {
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
      "004c1148",
      "READ",
      [
        "storage",
        "00c9aa58",
        null,
        "pointer"
      ]
    ],
    [
      "004c1160",
      "DATA",
      [
        "storage",
        "00c661d0",
        null,
        "undefined1[88]"
      ]
    ]
  ],
  "added": [
    [
      "004c1148",
      "READ",
      [
        "storage",
        "00c9ae58",
        null,
        "pointer"
      ]
    ],
    [
      "004c1160",
      "DATA",
      [
        "storage",
        "00c665d0",
        null,
        "undefined1[88]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c1160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c10e4.md#insn-004c1160) · [`004c1108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c10e4.md#insn-004c1108) · [`004c1170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c10e4.md#insn-004c1170)
- 新版 `004c11a0`（命令位置の公開資料なし） · `004c1148`（命令位置の公開資料なし） · `004c11b0`（命令位置の公開資料なし）

~~~diff
- 004c1160 ["INT_ADD", "register:40f0:8", ["const:4c1160:8", "const:4:8"]]
- 004c1160 ["CALL", null, ["callee:00c58de0:8"]]
+ 004c11a0 ["INT_ADD", "register:40f0:8", ["const:4c11a0:8", "const:4:8"]]
+ 004c11a0 ["CALL", null, ["callee:00c58de0:8"]]
- 004c1160 bytes 205e1e94
+ 004c11a0 bytes 105f1e94
- 004c1108 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a58:8"]]
- 004c1108 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c1148 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e58:8"]]
+ 004c1148 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c1108 bytes 082d45f9
+ 004c1148 bytes 082d47f9
- 004c1170 ["INT_ADD", "register:40f0:8", ["const:4c1170:8", "const:4:8"]]
- 004c1170 ["CALL", null, ["callee:00c57eb0:8"]]
+ 004c11b0 ["INT_ADD", "register:40f0:8", ["const:4c11b0:8", "const:4:8"]]
+ 004c11b0 ["CALL", null, ["callee:00c57eb0:8"]]
- 004c1170 bytes 505a1e94
+ 004c11b0 bytes 405b1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-856c0fce4d9e3224aa34293ddd81f56f"></a>

### [`004c15a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c15a0.md) → [`004c15e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c1/004c15e0.md) _ZN5Botan17EMSA_PKCS1v15_Raw8raw_dataEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
    "old": {
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
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c16a0",
      "incomplete_value": false,
      "site": "004c16b0",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004c1660",
      "incomplete_value": false,
      "site": "004c1670",
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
      "004c1668",
      "PARAM",
      [
        "storage",
        "002b5f84",
        null,
        "string"
      ]
    ],
    [
      "004c16a0",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004c16a4",
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
      "004c1668",
      "PARAM",
      [
        "storage",
        "002b5fc4",
        null,
        "string"
      ]
    ],
    [
      "004c16a0",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004c16a4",
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

- 旧版 [`004c1630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c15a0.md#insn-004c1630) · [`004c1670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c15a0.md#insn-004c1670) · [`004c161c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c15a0.md#insn-004c161c)
- 新版 `004c1670`（命令位置の公開資料なし） · `004c16b0`（命令位置の公開資料なし） · `004c165c`（命令位置の公開資料なし）

~~~diff
- 004c1630 ["INT_ADD", "register:40f0:8", ["const:4c1630:8", "const:4:8"]]
- 004c1630 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004c1670 ["INT_ADD", "register:40f0:8", ["const:4c1670:8", "const:4:8"]]
+ 004c1670 ["CALL", null, ["callee:0043ddd8:8"]]
- 004c1630 bytes daf1fd97
+ 004c1670 bytes daf1fd97
- 004c1670 ["INT_ADD", "register:40f0:8", ["const:4c1670:8", "const:4:8"]]
- 004c1670 ["CALL", null, ["callee:00c57f10:8"]]
+ 004c16b0 ["INT_ADD", "register:40f0:8", ["const:4c16b0:8", "const:4:8"]]
+ 004c16b0 ["CALL", null, ["callee:00c57f10:8"]]
- 004c1670 bytes 28591e94
+ 004c16b0 bytes 185a1e94
- 004c161c ["INT_ADD", "register:40f0:8", ["const:4c161c:8", "const:4:8"]]
- 004c161c ["CALL", null, ["callee:00c57ef0:8"]]
+ 004c165c ["INT_ADD", "register:40f0:8", ["const:4c165c:8", "const:4:8"]]
+ 004c165c ["CALL", null, ["callee:00c57ef0:8"]]
- 004c161c bytes 35591e94
+ 004c165c bytes 255a1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afbc10e32705a8efd22b3d8328800f53"></a>

### [`004c17e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c17e0.md) → [`004c1820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c1/004c1820.md) _ZN5Botan4PSSRC2EPNS_12HashFunctionE

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
    "old": {
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
      "004c1838",
      "READ",
      [
        "storage",
        "00c9aa60",
        null,
        "pointer"
      ]
    ],
    [
      "004c1844",
      "DATA",
      [
        "storage",
        "00c66228",
        null,
        "undefined1[88]"
      ]
    ]
  ],
  "added": [
    [
      "004c1838",
      "READ",
      [
        "storage",
        "00c9ae60",
        null,
        "pointer"
      ]
    ],
    [
      "004c1844",
      "DATA",
      [
        "storage",
        "00c66628",
        null,
        "undefined1[88]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c17f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c17e0.md#insn-004c17f8) · [`004c1810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c17e0.md#insn-004c1810)
- 新版 `004c1838`（命令位置の公開資料なし） · `004c1850`（命令位置の公開資料なし）

~~~diff
- 004c17f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a60:8"]]
- 004c17f8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c1838 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e60:8"]]
+ 004c1838 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c17f8 bytes 083145f9
+ 004c1838 bytes 083147f9
- 004c1810 ["COPY", "register:0:8", ["register:4040:8"]]
- 004c1810 ["INT_ADD", "register:40f0:8", ["const:4c1810:8", "const:4:8"]]
- 004c1810 ["CALLIND", null, ["register:0:8"]]
+ 004c1850 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c1850 ["INT_ADD", "register:40f0:8", ["const:4c1850:8", "const:4:8"]]
+ 004c1850 ["CALLIND", null, ["register:0:8"]]
- 004c1810 bytes 00013fd6
+ 004c1850 bytes 00013fd6
~~~


<a id="compare-68ceeb8a1262d8b02efd87d75c68a98e"></a>

### [`004c19d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c19d0.md) → [`004c1a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c1/004c1a10.md) FUN_004c1a10

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`004c18d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c18d4.md) [`004c2e5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c2/004c2e5c.md) · 呼出先 11件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 2件 [`004c1914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c1/004c1914.md) [`004c2e9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c2/004c2e9c.md) · 呼出先 11件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

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
    "old": {
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
    "ordinal": 18,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
      "004c1cb0",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004c1d10",
      "PARAM",
      [
        "storage",
        "002bc662",
        null,
        "string"
      ]
    ],
    [
      "004c1d48",
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
      "004c1cb0",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004c1d10",
      "PARAM",
      [
        "storage",
        "002bc6a2",
        null,
        "string"
      ]
    ],
    [
      "004c1d48",
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

- 旧版 [`004c1c80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c19d0.md#insn-004c1c80) · [`004c1cd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c19d0.md#insn-004c1cd8) · [`004c1d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c19d0.md#insn-004c1d18)
- 新版 `004c1cc0`（命令位置の公開資料なし） · `004c1d18`（命令位置の公開資料なし） · `004c1d58`（命令位置の公開資料なし）

~~~diff
- 004c1c80 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c1c80 ["INT_ADD", "register:40f0:8", ["const:4c1c80:8", "const:4:8"]]
- 004c1c80 ["CALLIND", null, ["register:0:8"]]
+ 004c1cc0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c1cc0 ["INT_ADD", "register:40f0:8", ["const:4c1cc0:8", "const:4:8"]]
+ 004c1cc0 ["CALLIND", null, ["register:0:8"]]
- 004c1c80 bytes 20013fd6
+ 004c1cc0 bytes 20013fd6
- 004c1cd8 ["INT_ADD", "register:40f0:8", ["const:4c1cd8:8", "const:4:8"]]
- 004c1cd8 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004c1d18 ["INT_ADD", "register:40f0:8", ["const:4c1d18:8", "const:4:8"]]
+ 004c1d18 ["CALL", null, ["callee:0043ddd8:8"]]
- 004c1cd8 bytes 30f0fd97
+ 004c1d18 bytes 30f0fd97
- 004c1d18 ["INT_ADD", "register:40f0:8", ["const:4c1d18:8", "const:4:8"]]
- 004c1d18 ["CALL", null, ["callee:00c57f10:8"]]
+ 004c1d58 ["INT_ADD", "register:40f0:8", ["const:4c1d58:8", "const:4:8"]]
+ 004c1d58 ["CALL", null, ["callee:00c57f10:8"]]
- 004c1d18 bytes 7e571e94
+ 004c1d58 bytes 6e581e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07dadb4cd95a38c5ecb95d70bccf2057"></a>

### [`004c1e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c1e04.md) → [`004c1e44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c1/004c1e44.md) FUN_004c1e44

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`004c1dfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c1dfc.md) [`004c2f58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c2/004c2f58.md) · 呼出先 10件 [`004b13b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b1/004b13b4.md) [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`004bfc64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bfc64.md) [`00540264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540264.md) [`00543818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543818.md)
- 新版 呼出元 2件 [`004c1e3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c1/004c1e3c.md) [`004c2f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c2/004c2f98.md) · 呼出先 10件 [`004b13f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b1/004b13f4.md) [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md) [`004bfca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bf/004bfca4.md) [`005402a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005402a4.md) [`00543858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543858.md)

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
    "old": {
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
      "004c2220",
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
      "004c2220",
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

- 旧版 [`004c21f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c1e04.md#insn-004c21f0) · [`004c1e44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c1e04.md#insn-004c1e44) · [`004c1eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c1e04.md#insn-004c1eac)
- 新版 `004c2230`（命令位置の公開資料なし） · `004c1e84`（命令位置の公開資料なし） · `004c1eec`（命令位置の公開資料なし）

~~~diff
- 004c21f0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c21f0 ["INT_ADD", "register:40f0:8", ["const:4c21f0:8", "const:4:8"]]
- 004c21f0 ["CALLIND", null, ["register:0:8"]]
+ 004c2230 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c2230 ["INT_ADD", "register:40f0:8", ["const:4c2230:8", "const:4:8"]]
+ 004c2230 ["CALLIND", null, ["register:0:8"]]
- 004c21f0 bytes 20013fd6
+ 004c2230 bytes 20013fd6
- 004c1e44 ["COPY", "register:0:8", ["register:4040:8"]]
- 004c1e44 ["INT_ADD", "register:40f0:8", ["const:4c1e44:8", "const:4:8"]]
- 004c1e44 ["CALLIND", null, ["register:0:8"]]
+ 004c1e84 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c1e84 ["INT_ADD", "register:40f0:8", ["const:4c1e84:8", "const:4:8"]]
+ 004c1e84 ["CALLIND", null, ["register:0:8"]]
- 004c1e44 bytes 00013fd6
+ 004c1e84 bytes 00013fd6
- 004c1eac ["INT_ADD", "register:40f0:8", ["const:4c1eac:8", "const:4:8"]]
- 004c1eac ["CALL", null, ["callee:005402a4:8"]]
+ 004c1eec ["INT_ADD", "register:40f0:8", ["const:4c1eec:8", "const:4:8"]]
+ 004c1eec ["CALL", null, ["callee:005402a4:8"]]
- 004c1eac bytes eef80194
+ 004c1eec bytes eef80194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1b1ddaf0059b2a429bfe34f7b987699"></a>

### [`004c2250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c2/004c2250.md) → [`004c2290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c2/004c2290.md) _ZNK5Botan4PSSR4nameEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f60.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md)

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
    "old": {
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
    "ordinal": 1,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
      "004c22d0",
      "PARAM",
      [
        "storage",
        "002b8f21",
        null,
        "string"
      ]
    ],
    [
      "004c22fc",
      "PARAM",
      [
        "storage",
        "002ad75e",
        null,
        "string"
      ]
    ],
    [
      "004c236c",
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
      "004c22d0",
      "PARAM",
      [
        "storage",
        "002b8f61",
        null,
        "string"
      ]
    ],
    [
      "004c22fc",
      "PARAM",
      [
        "storage",
        "002ad79e",
        null,
        "string"
      ]
    ],
    [
      "004c236c",
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

- 旧版 [`004c229c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c2/004c2250.md#insn-004c229c) · [`004c22c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c2/004c2250.md#insn-004c22c4) · [`004c2334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c2/004c2250.md#insn-004c2334)
- 新版 `004c22dc`（命令位置の公開資料なし） · `004c2304`（命令位置の公開資料なし） · `004c2374`（命令位置の公開資料なし）

~~~diff
- 004c229c ["INT_ADD", "register:40f0:8", ["const:4c229c:8", "const:4:8"]]
- 004c229c ["CALL", null, ["callee:00c57f60:8"]]
+ 004c22dc ["INT_ADD", "register:40f0:8", ["const:4c22dc:8", "const:4:8"]]
+ 004c22dc ["CALL", null, ["callee:00c57f60:8"]]
- 004c229c bytes 31561e94
+ 004c22dc bytes 21571e94
- 004c22c4 ["INT_ADD", "register:40f0:8", ["const:4c22c4:8", "const:4:8"]]
- 004c22c4 ["CALL", null, ["callee:00c57f70:8"]]
+ 004c2304 ["INT_ADD", "register:40f0:8", ["const:4c2304:8", "const:4:8"]]
+ 004c2304 ["CALL", null, ["callee:00c57f70:8"]]
- 004c22c4 bytes 2b561e94
+ 004c2304 bytes 1b571e94
- 004c2334 ["INT_ADD", "register:40f0:8", ["const:4c2334:8", "const:4:8"]]
- 004c2334 ["CALL", null, ["callee:00c57f70:8"]]
+ 004c2374 ["INT_ADD", "register:40f0:8", ["const:4c2374:8", "const:4:8"]]
+ 004c2374 ["CALL", null, ["callee:00c57f70:8"]]
- 004c2334 bytes 0f561e94
+ 004c2374 bytes ff561e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c7530cfea849f0cbf839909dec07a87"></a>

### [`004c24bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c2/004c24bc.md) → [`004c24fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c2/004c24fc.md) _ZNK5Botan4PSSR15config_for_x509ERKNS_11Private_KeyERKNSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 22件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004a6d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a6d70.md) [`004c0774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c0/004c0774.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00535b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b40.md)
- 新版 呼出元 0件  · 呼出先 22件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004a6db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6db0.md) [`004c07b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c0/004c07b4.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00535b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b80.md)

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
    "old": {
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
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
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
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
    "old": {
      "definition_site": "004c27b4",
      "incomplete_value": true,
      "site": "004c27b4",
      "value": [
        "LOAD",
        "8",
        [
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
      "004c262c",
      "READ",
      [
        "storage",
        "00c9a938",
        null,
        "pointer"
      ]
    ],
    [
      "004c2638",
      "DATA",
      [
        "storage",
        "00c65da8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004c2660",
      "READ",
      [
        "storage",
        "002b19fe",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004c262c",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "004c2638",
      "DATA",
      [
        "storage",
        "00c661a8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004c2660",
      "READ",
      [
        "storage",
        "002b1a3e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c27b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c2/004c24bc.md#insn-004c27b4) · [`004c2814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c2/004c24bc.md#insn-004c2814) · [`004c290c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c2/004c24bc.md#insn-004c290c)
- 新版 `004c27f4`（命令位置の公開資料なし） · `004c2854`（命令位置の公開資料なし） · `004c294c`（命令位置の公開資料なし）

~~~diff
- 004c27b4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c27b4 ["INT_ADD", "register:40f0:8", ["const:4c27b4:8", "const:4:8"]]
- 004c27b4 ["CALLIND", null, ["register:0:8"]]
+ 004c27f4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c27f4 ["INT_ADD", "register:40f0:8", ["const:4c27f4:8", "const:4:8"]]
+ 004c27f4 ["CALLIND", null, ["register:0:8"]]
- 004c27b4 bytes 20013fd6
+ 004c27f4 bytes 20013fd6
- 004c2814 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c2814 ["INT_ADD", "register:40f0:8", ["const:4c2814:8", "const:4:8"]]
- 004c2814 ["CALLIND", null, ["register:0:8"]]
+ 004c2854 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c2854 ["INT_ADD", "register:40f0:8", ["const:4c2854:8", "const:4:8"]]
+ 004c2854 ["CALLIND", null, ["register:0:8"]]
- 004c2814 bytes 20013fd6
+ 004c2854 bytes 20013fd6
- 004c290c ["COPY", "register:0:8", ["register:4048:8"]]
- 004c290c ["INT_ADD", "register:40f0:8", ["const:4c290c:8", "const:4:8"]]
- 004c290c ["CALLIND", null, ["register:0:8"]]
+ 004c294c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c294c ["INT_ADD", "register:40f0:8", ["const:4c294c:8", "const:4:8"]]
+ 004c294c ["CALLIND", null, ["register:0:8"]]
- 004c290c bytes 20013fd6
+ 004c294c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aed0fbdb8b85bfda7d0655154152e093"></a>

### [`004c2c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c2/004c2c74.md) → [`004c2cb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c2/004c2cb4.md) _ZN5Botan8PSSR_RawC1EPNS_12HashFunctionE

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
    "old": {
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
      "004c2ccc",
      "READ",
      [
        "storage",
        "00c9aa68",
        null,
        "pointer"
      ]
    ],
    [
      "004c2cd8",
      "DATA",
      [
        "storage",
        "00c66280",
        null,
        "undefined1[88]"
      ]
    ]
  ],
  "added": [
    [
      "004c2ccc",
      "READ",
      [
        "storage",
        "00c9ae68",
        null,
        "pointer"
      ]
    ],
    [
      "004c2cd8",
      "DATA",
      [
        "storage",
        "00c66680",
        null,
        "undefined1[88]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c2c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c2/004c2c74.md#insn-004c2c8c) · [`004c2ca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c2/004c2c74.md#insn-004c2ca4)
- 新版 `004c2ccc`（命令位置の公開資料なし） · `004c2ce4`（命令位置の公開資料なし）

~~~diff
- 004c2c8c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a68:8"]]
- 004c2c8c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c2ccc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e68:8"]]
+ 004c2ccc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c2c8c bytes 083545f9
+ 004c2ccc bytes 083547f9
- 004c2ca4 ["COPY", "register:0:8", ["register:4040:8"]]
- 004c2ca4 ["INT_ADD", "register:40f0:8", ["const:4c2ca4:8", "const:4:8"]]
- 004c2ca4 ["CALLIND", null, ["register:0:8"]]
+ 004c2ce4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c2ce4 ["INT_ADD", "register:40f0:8", ["const:4c2ce4:8", "const:4:8"]]
+ 004c2ce4 ["CALLIND", null, ["register:0:8"]]
- 004c2ca4 bytes 00013fd6
+ 004c2ce4 bytes 00013fd6
~~~


<a id="compare-a5e3190c6897695613c94b23fbaf4e82"></a>

### [`004c2d14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c2/004c2d14.md) → [`004c2d54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c2/004c2d54.md) _ZN5Botan8PSSR_Raw8raw_dataEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
    "old": {
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c2e2c",
      "incomplete_value": false,
      "site": "004c2e3c",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004c2dec",
      "incomplete_value": false,
      "site": "004c2dfc",
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
      "004c2df8",
      "PARAM",
      [
        "storage",
        "002a3041",
        null,
        "string"
      ]
    ],
    [
      "004c2e2c",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004c2e30",
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
      "004c2df8",
      "PARAM",
      [
        "storage",
        "002a310e",
        null,
        "string"
      ]
    ],
    [
      "004c2e2c",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004c2e30",
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

- 旧版 [`004c2dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c2/004c2d14.md#insn-004c2dc0) · [`004c2dfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c2/004c2d14.md#insn-004c2dfc) · [`004c2d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c2/004c2d14.md#insn-004c2d68)
- 新版 `004c2e00`（命令位置の公開資料なし） · `004c2e3c`（命令位置の公開資料なし） · `004c2da8`（命令位置の公開資料なし）

~~~diff
- 004c2dc0 ["INT_ADD", "register:40f0:8", ["const:4c2dc0:8", "const:4:8"]]
- 004c2dc0 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004c2e00 ["INT_ADD", "register:40f0:8", ["const:4c2e00:8", "const:4:8"]]
+ 004c2e00 ["CALL", null, ["callee:0043ddd8:8"]]
- 004c2dc0 bytes f6ebfd97
+ 004c2e00 bytes f6ebfd97
- 004c2dfc ["INT_ADD", "register:40f0:8", ["const:4c2dfc:8", "const:4:8"]]
- 004c2dfc ["CALL", null, ["callee:00c57f10:8"]]
+ 004c2e3c ["INT_ADD", "register:40f0:8", ["const:4c2e3c:8", "const:4:8"]]
+ 004c2e3c ["CALL", null, ["callee:00c57f10:8"]]
- 004c2dfc bytes 45531e94
+ 004c2e3c bytes 35541e94
- 004c2d68 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c2d68 ["INT_ADD", "register:40f0:8", ["const:4c2d68:8", "const:4:8"]]
- 004c2d68 ["CALLIND", null, ["register:0:8"]]
+ 004c2da8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c2da8 ["INT_ADD", "register:40f0:8", ["const:4c2da8:8", "const:4:8"]]
+ 004c2da8 ["CALLIND", null, ["register:0:8"]]
- 004c2d68 bytes 20013fd6
+ 004c2da8 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7154d363d73fd4ab0d4ec593de05e94"></a>

### [`004c2f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c2/004c2f60.md) → [`004c2fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c2/004c2fa0.md) _ZNK5Botan8PSSR_Raw4nameEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f60.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md)

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
    "old": {
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
    "ordinal": 1,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
      "004c2fe0",
      "PARAM",
      [
        "storage",
        "002a0fa1",
        null,
        "string"
      ]
    ],
    [
      "004c300c",
      "PARAM",
      [
        "storage",
        "002ad75e",
        null,
        "string"
      ]
    ],
    [
      "004c307c",
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
      "004c2fe0",
      "PARAM",
      [
        "storage",
        "002a106e",
        null,
        "string"
      ]
    ],
    [
      "004c300c",
      "PARAM",
      [
        "storage",
        "002ad79e",
        null,
        "string"
      ]
    ],
    [
      "004c307c",
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

- 旧版 [`004c2fac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c2/004c2f60.md#insn-004c2fac) · [`004c2fd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c2/004c2f60.md#insn-004c2fd4) · [`004c3044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c2/004c2f60.md#insn-004c3044)
- 新版 `004c2fec`（命令位置の公開資料なし） · `004c3014`（命令位置の公開資料なし） · `004c3084`（命令位置の公開資料なし）

~~~diff
- 004c2fac ["INT_ADD", "register:40f0:8", ["const:4c2fac:8", "const:4:8"]]
- 004c2fac ["CALL", null, ["callee:00c57f60:8"]]
+ 004c2fec ["INT_ADD", "register:40f0:8", ["const:4c2fec:8", "const:4:8"]]
+ 004c2fec ["CALL", null, ["callee:00c57f60:8"]]
- 004c2fac bytes ed521e94
+ 004c2fec bytes dd531e94
- 004c2fd4 ["INT_ADD", "register:40f0:8", ["const:4c2fd4:8", "const:4:8"]]
- 004c2fd4 ["CALL", null, ["callee:00c57f70:8"]]
+ 004c3014 ["INT_ADD", "register:40f0:8", ["const:4c3014:8", "const:4:8"]]
+ 004c3014 ["CALL", null, ["callee:00c57f70:8"]]
- 004c2fd4 bytes e7521e94
+ 004c3014 bytes d7531e94
- 004c3044 ["INT_ADD", "register:40f0:8", ["const:4c3044:8", "const:4:8"]]
- 004c3044 ["CALL", null, ["callee:00c57f70:8"]]
+ 004c3084 ["INT_ADD", "register:40f0:8", ["const:4c3084:8", "const:4:8"]]
+ 004c3084 ["CALL", null, ["callee:00c57f70:8"]]
- 004c3044 bytes cb521e94
+ 004c3084 bytes bb531e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f0ca55765b0c5ea0f3cce3633b19b17"></a>

### [`004c31cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c3/004c31cc.md) → [`004c320c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c3/004c320c.md) _ZN5Botan14Entropy_Source6createERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
    "old": {
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
      "004c32d8",
      "DATA",
      [
        "storage",
        "00c69888",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004c32d8",
      "DATA",
      [
        "storage",
        "00c69c88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c3288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c3/004c31cc.md#insn-004c3288) · [`004c3290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c3/004c31cc.md#insn-004c3290)
- 新版 `004c32c8`（命令位置の公開資料なし） · `004c32d0`（命令位置の公開資料なし）

~~~diff
- 004c3288 ["INT_ADD", "register:40f0:8", ["const:4c3288:8", "const:4:8"]]
- 004c3288 ["CALL", null, ["callee:00c57e90:8"]]
+ 004c32c8 ["INT_ADD", "register:40f0:8", ["const:4c32c8:8", "const:4:8"]]
+ 004c32c8 ["CALL", null, ["callee:00c57e90:8"]]
- 004c3288 bytes 02521e94
+ 004c32c8 bytes f2521e94
- 004c3290 ["COPY", "tmp:0:8", ["const:888:8"]]
- 004c3290 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004c3290 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004c3290 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004c32d0 ["COPY", "tmp:0:8", ["const:c88:8"]]
+ 004c32d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004c32d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004c32d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004c3290 bytes 29212291
+ 004c32d0 bytes 29213291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fee8f2b30f78681087bbdc18c969fd52"></a>

### [`004c3afc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c3/004c3afc.md) → [`004c3b3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c3/004c3b3c.md) _ZN5Botan15Entropy_Sources14global_sourcesEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 10件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440ac0.md) [`00473500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473500.md) [`004c3e5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c3/004c3e5c.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440b00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440b00.md) [`00473540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473540.md) [`004c3e9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c3/004c3e9c.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md)

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
    "old": {
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
      "004c3b68",
      "READ",
      [
        "storage",
        "00ca4e60",
        null,
        "undefined1"
      ]
    ],
    [
      "004c3b84",
      "DATA",
      [
        "storage",
        "00ca4e48",
        null,
        null
      ]
    ],
    [
      "004c3ba4",
      "PARAM",
      [
        "storage",
        "00ca4e60",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "004c3b68",
      "READ",
      [
        "storage",
        "00ca5260",
        null,
        "undefined1"
      ]
    ],
    [
      "004c3b84",
      "DATA",
      [
        "storage",
        "00ca5248",
        null,
        null
      ]
    ],
    [
      "004c3ba4",
      "PARAM",
      [
        "storage",
        "00ca5260",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c3b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c3/004c3afc.md#insn-004c3b40) · [`004c3b68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c3/004c3afc.md#insn-004c3b68) · [`004c3b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c3/004c3afc.md#insn-004c3b80)
- 新版 `004c3b80`（命令位置の公開資料なし） · `004c3ba8`（命令位置の公開資料なし） · `004c3bc0`（命令位置の公開資料なし）

~~~diff
- 004c3b40 ["COPY", "register:4000:8", ["const:ca4000:8"]]
+ 004c3b80 ["COPY", "register:4000:8", ["const:ca5000:8"]]
- 004c3b40 bytes 003f00b0
+ 004c3b80 bytes 003f00d0
- 004c3b68 ["INT_ADD", "register:40f0:8", ["const:4c3b68:8", "const:4:8"]]
- 004c3b68 ["CALL", null, ["callee:00c57e50:8"]]
+ 004c3ba8 ["INT_ADD", "register:40f0:8", ["const:4c3ba8:8", "const:4:8"]]
+ 004c3ba8 ["CALL", null, ["callee:00c57e50:8"]]
- 004c3b68 bytes ba4f1e94
+ 004c3ba8 bytes aa501e94
- 004c3b80 ["INT_ADD", "register:40f0:8", ["const:4c3b80:8", "const:4:8"]]
- 004c3b80 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004c3bc0 ["INT_ADD", "register:40f0:8", ["const:4c3bc0:8", "const:4:8"]]
+ 004c3bc0 ["CALL", null, ["callee:0043ddd8:8"]]
- 004c3b80 bytes 86e8fd97
+ 004c3bc0 bytes 86e8fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20b161ea5af44a6c1e08d860207be353"></a>

### [`004c3ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c3/004c3ed8.md) → [`004c3f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c3/004c3f18.md) _ZN5Botan19StreamCipher_FilterC1EPNS_12StreamCipherE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00543c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543c1c.md) [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00543c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543c5c.md) [`00c37ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ba4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
    "old": {
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "004c3fc8",
      "incomplete_value": true,
      "site": "004c3fd0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004c3f38",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "004c3f54",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c3f7c",
      "READ",
      [
        "storage",
        "00c9aa78",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c3f38",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "004c3f54",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c3f7c",
      "READ",
      [
        "storage",
        "00c9ae78",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c3fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c3/004c3ed8.md#insn-004c3fd0) · [`004c3ef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c3/004c3ed8.md#insn-004c3ef8) · [`004c3f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c3/004c3ed8.md#insn-004c3f2c)
- 新版 `004c4010`（命令位置の公開資料なし） · `004c3f38`（命令位置の公開資料なし） · `004c3f6c`（命令位置の公開資料なし）

~~~diff
- 004c3fd0 ["INT_ADD", "register:40f0:8", ["const:4c3fd0:8", "const:4:8"]]
- 004c3fd0 ["CALL", null, ["callee:00c57f10:8"]]
+ 004c4010 ["INT_ADD", "register:40f0:8", ["const:4c4010:8", "const:4:8"]]
+ 004c4010 ["CALL", null, ["callee:00c57f10:8"]]
- 004c3fd0 bytes d04e1e94
+ 004c4010 bytes c04f1e94
- 004c3ef8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a70:8"]]
- 004c3ef8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c3f38 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 004c3f38 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c3ef8 bytes 083945f9
+ 004c3f38 bytes 083947f9
- 004c3f2c ["INT_ADD", "register:40f0:8", ["const:4c3f2c:8", "const:4:8"]]
- 004c3f2c ["CALL", null, ["callee:00543c5c:8"]]
+ 004c3f6c ["INT_ADD", "register:40f0:8", ["const:4c3f6c:8", "const:4:8"]]
+ 004c3f6c ["CALL", null, ["callee:00543c5c:8"]]
- 004c3f2c bytes 3cff0194
+ 004c3f6c bytes 3cff0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bcadf9c342e9a207d0748d7b0bfa4b4b"></a>

### [`004c4028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c4028.md) → [`004c4068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c4068.md) _ZN5Botan19StreamCipher_FilterC1EPNS_12StreamCipherERKNS_11OctetStringE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`004bc9c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc9c0.md) [`00543c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543c1c.md) [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`004bca00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bca00.md) [`00543c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543c5c.md) [`00c37ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ba4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

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
    "ordinal": 8,
    "slot": 2
  },
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "004c4138",
      "incomplete_value": true,
      "site": "004c4140",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
      "004c4090",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "004c40ac",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c40d4",
      "READ",
      [
        "storage",
        "00c9aa78",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c4090",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "004c40ac",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c40d4",
      "READ",
      [
        "storage",
        "00c9ae78",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c4140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c4028.md#insn-004c4140) · [`004c4050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c4028.md#insn-004c4050) · [`004c4084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c4028.md#insn-004c4084)
- 新版 `004c4180`（命令位置の公開資料なし） · `004c4090`（命令位置の公開資料なし） · `004c40c4`（命令位置の公開資料なし）

~~~diff
- 004c4140 ["INT_ADD", "register:40f0:8", ["const:4c4140:8", "const:4:8"]]
- 004c4140 ["CALL", null, ["callee:00c57f10:8"]]
+ 004c4180 ["INT_ADD", "register:40f0:8", ["const:4c4180:8", "const:4:8"]]
+ 004c4180 ["CALL", null, ["callee:00c57f10:8"]]
- 004c4140 bytes 744e1e94
+ 004c4180 bytes 644f1e94
- 004c4050 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a70:8"]]
- 004c4050 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c4090 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e70:8"]]
+ 004c4090 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c4050 bytes 293945f9
+ 004c4090 bytes 293947f9
- 004c4084 ["INT_ADD", "register:40f0:8", ["const:4c4084:8", "const:4:8"]]
- 004c4084 ["CALL", null, ["callee:00543c5c:8"]]
+ 004c40c4 ["INT_ADD", "register:40f0:8", ["const:4c40c4:8", "const:4:8"]]
+ 004c40c4 ["CALL", null, ["callee:00543c5c:8"]]
- 004c4084 bytes e6fe0194
+ 004c40c4 bytes e6fe0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a77a9918c590abe8c00a04e028c0b967"></a>

### [`004c41c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c41c0.md) → [`004c4200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c4200.md) _ZN5Botan19StreamCipher_FilterC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`00543c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543c1c.md) [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00543c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543c5c.md) [`00c37ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ba4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

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
    "ordinal": 7,
    "slot": 2
  },
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "004c42d4",
      "incomplete_value": true,
      "site": "004c42dc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
      "004c4220",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "004c423c",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c4264",
      "READ",
      [
        "storage",
        "00c9aa78",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c4220",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "004c423c",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c4264",
      "READ",
      [
        "storage",
        "00c9ae78",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c42dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c41c0.md#insn-004c42dc) · [`004c41e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c41c0.md#insn-004c41e0) · [`004c4214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c41c0.md#insn-004c4214)
- 新版 `004c431c`（命令位置の公開資料なし） · `004c4220`（命令位置の公開資料なし） · `004c4254`（命令位置の公開資料なし）

~~~diff
- 004c42dc ["INT_ADD", "register:40f0:8", ["const:4c42dc:8", "const:4:8"]]
- 004c42dc ["CALL", null, ["callee:00c57f10:8"]]
+ 004c431c ["INT_ADD", "register:40f0:8", ["const:4c431c:8", "const:4:8"]]
+ 004c431c ["CALL", null, ["callee:00c57f10:8"]]
- 004c42dc bytes 0d4e1e94
+ 004c431c bytes fd4e1e94
- 004c41e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a70:8"]]
- 004c41e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c4220 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 004c4220 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c41e0 bytes 083945f9
+ 004c4220 bytes 083947f9
- 004c4214 ["INT_ADD", "register:40f0:8", ["const:4c4214:8", "const:4:8"]]
- 004c4214 ["CALL", null, ["callee:00543c5c:8"]]
+ 004c4254 ["INT_ADD", "register:40f0:8", ["const:4c4254:8", "const:4:8"]]
+ 004c4254 ["CALL", null, ["callee:00543c5c:8"]]
- 004c4214 bytes 82fe0194
+ 004c4254 bytes 82fe0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f5f844708062ef7572edd0426b02a74"></a>

### [`004c4354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c4354.md) → [`004c4394`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c4394.md) _ZN5Botan12StreamCipher15create_or_throwERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58a50.md) · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`00c58e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58e50.md) · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
    "old": {
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c4448",
      "incomplete_value": false,
      "site": "004c4458",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004c4408",
      "incomplete_value": false,
      "site": "004c4418",
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
      "004c440c",
      "PARAM",
      [
        "storage",
        "002ba274",
        null,
        "string"
      ]
    ],
    [
      "004c4448",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004c444c",
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
      "004c440c",
      "PARAM",
      [
        "storage",
        "002ba2b4",
        null,
        "string"
      ]
    ],
    [
      "004c4448",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004c444c",
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

- 旧版 [`004c43d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c4354.md#insn-004c43d4) · [`004c4418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c4354.md#insn-004c4418) · [`004c4388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c4354.md#insn-004c4388)
- 新版 `004c4414`（命令位置の公開資料なし） · `004c4458`（命令位置の公開資料なし） · `004c43c8`（命令位置の公開資料なし）

~~~diff
- 004c43d4 ["INT_ADD", "register:40f0:8", ["const:4c43d4:8", "const:4:8"]]
- 004c43d4 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004c4414 ["INT_ADD", "register:40f0:8", ["const:4c4414:8", "const:4:8"]]
+ 004c4414 ["CALL", null, ["callee:0043ddd8:8"]]
- 004c43d4 bytes 71e6fd97
+ 004c4414 bytes 71e6fd97
- 004c4418 ["INT_ADD", "register:40f0:8", ["const:4c4418:8", "const:4:8"]]
- 004c4418 ["CALL", null, ["callee:00c57f10:8"]]
+ 004c4458 ["INT_ADD", "register:40f0:8", ["const:4c4458:8", "const:4:8"]]
+ 004c4458 ["CALL", null, ["callee:00c57f10:8"]]
- 004c4418 bytes be4d1e94
+ 004c4458 bytes ae4e1e94
- 004c4388 ["INT_ADD", "register:40f0:8", ["const:4c4388:8", "const:4:8"]]
- 004c4388 ["CALL", null, ["callee:00c58e60:8"]]
+ 004c43c8 ["INT_ADD", "register:40f0:8", ["const:4c43c8:8", "const:4:8"]]
+ 004c43c8 ["CALL", null, ["callee:00c58e60:8"]]
- 004c4388 bytes b6511e94
+ 004c43c8 bytes a6521e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-477eeb15212fa37ad97e47e344f6ac4d"></a>

### [`004c4468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c4468.md) → [`004c44a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c44a8.md) _ZN5Botan19StreamCipher_FilterC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERKNS_11OctetStringE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 10件 [`004bc9c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc9c0.md) [`00543c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543c1c.md) [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 10件 [`004bca00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bca00.md) [`00543c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543c5c.md) [`00c37ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ba4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

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
    "ordinal": 8,
    "slot": 2
  },
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "004c4598",
      "incomplete_value": true,
      "site": "004c45a0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004c44d0",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "004c44ec",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c4514",
      "READ",
      [
        "storage",
        "00c9aa78",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c44d0",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "004c44ec",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c4514",
      "READ",
      [
        "storage",
        "00c9ae78",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c45a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c4468.md#insn-004c45a0) · [`004c4490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c4468.md#insn-004c4490) · [`004c44c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c4468.md#insn-004c44c4)
- 新版 `004c45e0`（命令位置の公開資料なし） · `004c44d0`（命令位置の公開資料なし） · `004c4504`（命令位置の公開資料なし）

~~~diff
- 004c45a0 ["INT_ADD", "register:40f0:8", ["const:4c45a0:8", "const:4:8"]]
- 004c45a0 ["CALL", null, ["callee:00c57f10:8"]]
+ 004c45e0 ["INT_ADD", "register:40f0:8", ["const:4c45e0:8", "const:4:8"]]
+ 004c45e0 ["CALL", null, ["callee:00c57f10:8"]]
- 004c45a0 bytes 5c4d1e94
+ 004c45e0 bytes 4c4e1e94
- 004c4490 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a70:8"]]
- 004c4490 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c44d0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e70:8"]]
+ 004c44d0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c4490 bytes 293945f9
+ 004c44d0 bytes 293947f9
- 004c44c4 ["INT_ADD", "register:40f0:8", ["const:4c44c4:8", "const:4:8"]]
- 004c44c4 ["CALL", null, ["callee:00543c5c:8"]]
+ 004c4504 ["INT_ADD", "register:40f0:8", ["const:4c4504:8", "const:4:8"]]
+ 004c4504 ["CALL", null, ["callee:00543c5c:8"]]
- 004c44c4 bytes d6fd0194
+ 004c4504 bytes d6fd0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-490e414b32750668946a3a20761dd3fe"></a>

### [`004c46b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c46b4.md) → [`004c46f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c46f4.md) _ZN5Botan11Hash_FilterC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00543c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543c1c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58a70.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00543c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543c5c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58e70.md)

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
    "old": {
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
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
      "004c471c",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "004c4738",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c4758",
      "READ",
      [
        "storage",
        "00c9aa80",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c471c",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "004c4738",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c4758",
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

- 旧版 [`004c46dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c46b4.md#insn-004c46dc) · [`004c4710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c46b4.md#insn-004c4710) · [`004c4718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c46b4.md#insn-004c4718)
- 新版 `004c471c`（命令位置の公開資料なし） · `004c4750`（命令位置の公開資料なし） · `004c4758`（命令位置の公開資料なし）

~~~diff
- 004c46dc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a70:8"]]
- 004c46dc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c471c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e70:8"]]
+ 004c471c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c46dc bytes 293945f9
+ 004c471c bytes 293947f9
- 004c4710 ["INT_ADD", "register:40f0:8", ["const:4c4710:8", "const:4:8"]]
- 004c4710 ["CALL", null, ["callee:00543c5c:8"]]
+ 004c4750 ["INT_ADD", "register:40f0:8", ["const:4c4750:8", "const:4:8"]]
+ 004c4750 ["CALL", null, ["callee:00543c5c:8"]]
- 004c4710 bytes 43fd0194
+ 004c4750 bytes 43fd0194
- 004c4718 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a80:8"]]
- 004c4718 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c4758 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e80:8"]]
+ 004c4758 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c4718 bytes 084145f9
+ 004c4758 bytes 084147f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ede5f0952e801eb44ed4ac00d3083106"></a>

### [`004c47d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c47d8.md) → [`004c4818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c4818.md) _ZN5Botan6FilterC2Ev

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00543c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543c1c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00543c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543c5c.md)

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
    "old": {
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
      "004c4834",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "004c4840",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "004c4834",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "004c4840",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c47f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c47d8.md#insn-004c47f4) · [`004c47f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c47d8.md#insn-004c47f8) · [`004c4818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c47d8.md#insn-004c4818)
- 新版 `004c4834`（命令位置の公開資料なし） · `004c4858`（命令位置の公開資料なし）

~~~diff
- 004c47f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a70:8"]]
- 004c47f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c4834 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 004c4834 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c47f4 bytes 083945f9
+ 004c4834 bytes 083947f9
- 004c47f8 ["COPY", "register:40a0:8", ["register:4000:8"]]
- 004c47f8 bytes f40300aa
- 004c4818 ["INT_ADD", "register:40f0:8", ["const:4c4818:8", "const:4:8"]]
- 004c4818 ["CALL", null, ["callee:00543c5c:8"]]
+ 004c4858 ["INT_ADD", "register:40f0:8", ["const:4c4858:8", "const:4:8"]]
+ 004c4858 ["CALL", null, ["callee:00543c5c:8"]]
- 004c4818 bytes 01fd0194
+ 004c4858 bytes 01fd0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64ebe92c02ffdd7df491ef7c093441c3"></a>

### [`004c485c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c485c.md) → [`004c489c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c489c.md) _ZN5Botan12HashFunction15create_or_throwERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58a70.md) · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`00c58e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58e70.md) · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
    "old": {
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c4950",
      "incomplete_value": false,
      "site": "004c4960",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004c4910",
      "incomplete_value": false,
      "site": "004c4920",
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
      "004c4914",
      "PARAM",
      [
        "storage",
        "002a1ecf",
        null,
        null
      ]
    ],
    [
      "004c4950",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004c4954",
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
      "004c4914",
      "PARAM",
      [
        "storage",
        "002a1f9c",
        null,
        null
      ]
    ],
    [
      "004c4950",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004c4954",
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

- 旧版 [`004c48dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c485c.md#insn-004c48dc) · [`004c4920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c485c.md#insn-004c4920) · [`004c4890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c485c.md#insn-004c4890)
- 新版 `004c491c`（命令位置の公開資料なし） · `004c4960`（命令位置の公開資料なし） · `004c48d0`（命令位置の公開資料なし）

~~~diff
- 004c48dc ["INT_ADD", "register:40f0:8", ["const:4c48dc:8", "const:4:8"]]
- 004c48dc ["CALL", null, ["callee:0043ddd8:8"]]
+ 004c491c ["INT_ADD", "register:40f0:8", ["const:4c491c:8", "const:4:8"]]
+ 004c491c ["CALL", null, ["callee:0043ddd8:8"]]
- 004c48dc bytes 2fe5fd97
+ 004c491c bytes 2fe5fd97
- 004c4920 ["INT_ADD", "register:40f0:8", ["const:4c4920:8", "const:4:8"]]
- 004c4920 ["CALL", null, ["callee:00c57f10:8"]]
+ 004c4960 ["INT_ADD", "register:40f0:8", ["const:4c4960:8", "const:4:8"]]
+ 004c4960 ["CALL", null, ["callee:00c57f10:8"]]
- 004c4920 bytes 7c4c1e94
+ 004c4960 bytes 6c4d1e94
- 004c4890 ["INT_ADD", "register:40f0:8", ["const:4c4890:8", "const:4:8"]]
- 004c4890 ["CALL", null, ["callee:00c58df0:8"]]
+ 004c48d0 ["INT_ADD", "register:40f0:8", ["const:4c48d0:8", "const:4:8"]]
+ 004c48d0 ["CALL", null, ["callee:00c58df0:8"]]
- 004c4890 bytes 58501e94
+ 004c48d0 bytes 48511e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78600de799ac5bacf90b36d139b45d13"></a>

### [`004c4a94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c4a94.md) → [`004c4ad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c4ad4.md) _ZN5Botan10MAC_FilterC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00543c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543c1c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58a80.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00543c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543c5c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58e80.md)

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
    "old": {
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
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
      "004c4afc",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "004c4b18",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c4b38",
      "READ",
      [
        "storage",
        "00c9aa88",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c4afc",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "004c4b18",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c4b38",
      "READ",
      [
        "storage",
        "00c9ae88",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c4abc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c4a94.md#insn-004c4abc) · [`004c4af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c4a94.md#insn-004c4af0) · [`004c4af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c4a94.md#insn-004c4af8)
- 新版 `004c4afc`（命令位置の公開資料なし） · `004c4b30`（命令位置の公開資料なし） · `004c4b38`（命令位置の公開資料なし）

~~~diff
- 004c4abc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a70:8"]]
- 004c4abc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c4afc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e70:8"]]
+ 004c4afc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c4abc bytes 293945f9
+ 004c4afc bytes 293947f9
- 004c4af0 ["INT_ADD", "register:40f0:8", ["const:4c4af0:8", "const:4:8"]]
- 004c4af0 ["CALL", null, ["callee:00543c5c:8"]]
+ 004c4b30 ["INT_ADD", "register:40f0:8", ["const:4c4b30:8", "const:4:8"]]
+ 004c4b30 ["CALL", null, ["callee:00543c5c:8"]]
- 004c4af0 bytes 4bfc0194
+ 004c4b30 bytes 4bfc0194
- 004c4af8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a88:8"]]
- 004c4af8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c4b38 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e88:8"]]
+ 004c4b38 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c4af8 bytes 084545f9
+ 004c4b38 bytes 084547f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ce42a6db8a0f478ee0c7b134efe50cb"></a>

### [`004c4bb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c4bb8.md) → [`004c4bf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c4bf8.md) _ZN5Botan25MessageAuthenticationCode15create_or_throwERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58a80.md) · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`00c58e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58e80.md) · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
    "old": {
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c4cac",
      "incomplete_value": false,
      "site": "004c4cbc",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004c4c6c",
      "incomplete_value": false,
      "site": "004c4c7c",
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
      "004c4c70",
      "PARAM",
      [
        "storage",
        "002ac723",
        null,
        null
      ]
    ],
    [
      "004c4cac",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004c4cb0",
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
      "004c4c70",
      "PARAM",
      [
        "storage",
        "002ac763",
        null,
        null
      ]
    ],
    [
      "004c4cac",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004c4cb0",
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

- 旧版 [`004c4c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c4bb8.md#insn-004c4c38) · [`004c4c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c4bb8.md#insn-004c4c7c) · [`004c4bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c4bb8.md#insn-004c4bec)
- 新版 `004c4c78`（命令位置の公開資料なし） · `004c4cbc`（命令位置の公開資料なし） · `004c4c2c`（命令位置の公開資料なし）

~~~diff
- 004c4c38 ["INT_ADD", "register:40f0:8", ["const:4c4c38:8", "const:4:8"]]
- 004c4c38 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004c4c78 ["INT_ADD", "register:40f0:8", ["const:4c4c78:8", "const:4:8"]]
+ 004c4c78 ["CALL", null, ["callee:0043ddd8:8"]]
- 004c4c38 bytes 58e4fd97
+ 004c4c78 bytes 58e4fd97
- 004c4c7c ["INT_ADD", "register:40f0:8", ["const:4c4c7c:8", "const:4:8"]]
- 004c4c7c ["CALL", null, ["callee:00c57f10:8"]]
+ 004c4cbc ["INT_ADD", "register:40f0:8", ["const:4c4cbc:8", "const:4:8"]]
+ 004c4cbc ["CALL", null, ["callee:00c57f10:8"]]
- 004c4c7c bytes a54b1e94
+ 004c4cbc bytes 954c1e94
- 004c4bec ["INT_ADD", "register:40f0:8", ["const:4c4bec:8", "const:4:8"]]
- 004c4bec ["CALL", null, ["callee:00c58e90:8"]]
+ 004c4c2c ["INT_ADD", "register:40f0:8", ["const:4c4c2c:8", "const:4:8"]]
+ 004c4c2c ["CALL", null, ["callee:00c58e90:8"]]
- 004c4bec bytes a94f1e94
+ 004c4c2c bytes 99501e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d14ad7719ae0d9f7abde58291c3d27ae"></a>

### [`004c4ccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c4ccc.md) → [`004c4d0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c4d0c.md) _ZN5Botan10MAC_FilterC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERKNS_11OctetStringEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`004bc9c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc9c0.md) [`00543c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543c1c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58a80.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004bca00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bc/004bca00.md) [`00543c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543c5c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58e80.md)

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
    "old": {
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
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
      "004c4d34",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "004c4d54",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c4d74",
      "READ",
      [
        "storage",
        "00c9aa88",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c4d34",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "004c4d54",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c4d74",
      "READ",
      [
        "storage",
        "00c9ae88",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c4cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c4ccc.md#insn-004c4cf4) · [`004c4d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c4ccc.md#insn-004c4d10) · [`004c4d2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c4ccc.md#insn-004c4d2c)
- 新版 `004c4d34`（命令位置の公開資料なし） · `004c4d6c`（命令位置の公開資料なし）

~~~diff
- 004c4cf4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a70:8"]]
- 004c4cf4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c4d34 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e70:8"]]
+ 004c4d34 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c4cf4 bytes 293945f9
+ 004c4d34 bytes 293947f9
- 004c4d10 ["COPY", "register:40b8:8", ["register:4000:8"]]
- 004c4d10 bytes f70300aa
- 004c4d2c ["INT_ADD", "register:40f0:8", ["const:4c4d2c:8", "const:4:8"]]
- 004c4d2c ["CALL", null, ["callee:00543c5c:8"]]
+ 004c4d6c ["INT_ADD", "register:40f0:8", ["const:4c4d6c:8", "const:4:8"]]
+ 004c4d6c ["CALL", null, ["callee:00543c5c:8"]]
- 004c4d2c bytes bcfb0194
+ 004c4d6c bytes bcfb0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c40e447c5676ea0cc732ca22b1da7ca"></a>

### [`004c4f4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c4f4c.md) → [`004c4f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c4/004c4f8c.md) _ZN5Botan12Keyed_Filter6set_ivERKNS_11OctetStringE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c58990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58990.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c58d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58d90.md)

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
    "old": {
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c503c",
      "incomplete_value": false,
      "site": "004c504c",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004c4ffc",
      "incomplete_value": false,
      "site": "004c500c",
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
      "004c503c",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004c5040",
      "READ",
      [
        "storage",
        "00c9aa40",
        null,
        "pointer"
      ]
    ],
    [
      "004c5040",
      "PARAM",
      [
        "storage",
        "00c660b0",
        "_ZTIN5Botan17Invalid_IV_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004c503c",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004c5040",
      "READ",
      [
        "storage",
        "00c9ae40",
        null,
        "pointer"
      ]
    ],
    [
      "004c5040",
      "PARAM",
      [
        "storage",
        "00c664b0",
        "_ZTIN5Botan17Invalid_IV_LengthE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c500c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c4f4c.md#insn-004c500c) · [`004c4fac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c4f4c.md#insn-004c4fac) · [`004c4fc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c4f4c.md#insn-004c4fc4)
- 新版 `004c504c`（命令位置の公開資料なし） · `004c4fec`（命令位置の公開資料なし） · `004c5004`（命令位置の公開資料なし）

~~~diff
- 004c500c ["INT_ADD", "register:40f0:8", ["const:4c500c:8", "const:4:8"]]
- 004c500c ["CALL", null, ["callee:00c57f10:8"]]
+ 004c504c ["INT_ADD", "register:40f0:8", ["const:4c504c:8", "const:4:8"]]
+ 004c504c ["CALL", null, ["callee:00c57f10:8"]]
- 004c500c bytes c14a1e94
+ 004c504c bytes b14b1e94
- 004c4fac ["INT_ADD", "register:40f0:8", ["const:4c4fac:8", "const:4:8"]]
- 004c4fac ["CALL", null, ["callee:00c57ef0:8"]]
+ 004c4fec ["INT_ADD", "register:40f0:8", ["const:4c4fec:8", "const:4:8"]]
+ 004c4fec ["CALL", null, ["callee:00c57ef0:8"]]
- 004c4fac bytes d14a1e94
+ 004c4fec bytes c14b1e94
- 004c4fc4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c4fc4 ["INT_ADD", "register:40f0:8", ["const:4c4fc4:8", "const:4:8"]]
- 004c4fc4 ["CALLIND", null, ["register:0:8"]]
+ 004c5004 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c5004 ["INT_ADD", "register:40f0:8", ["const:4c5004:8", "const:4:8"]]
+ 004c5004 ["CALLIND", null, ["register:0:8"]]
- 004c4fc4 bytes 20013fd6
+ 004c5004 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-039c537055facd454bab133521fb979d"></a>

### [`004c5060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c5/004c5060.md) → [`004c50a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c50a0.md) _ZN5Botan5ChainC1EPNS_6FilterES2_S2_S2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00543c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543c1c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00543c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543c5c.md)

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
    "old": {
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
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
      "004c50c0",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "004c50dc",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c50fc",
      "READ",
      [
        "storage",
        "00c9aa90",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c50c0",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "004c50dc",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c50fc",
      "READ",
      [
        "storage",
        "00c9ae90",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c5080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c5/004c5060.md#insn-004c5080) · [`004c50b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c5/004c5060.md#insn-004c50b4) · [`004c50bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c5/004c5060.md#insn-004c50bc)
- 新版 `004c50c0`（命令位置の公開資料なし） · `004c50f4`（命令位置の公開資料なし） · `004c50fc`（命令位置の公開資料なし）

~~~diff
- 004c5080 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a70:8"]]
- 004c5080 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c50c0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 004c50c0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c5080 bytes 083945f9
+ 004c50c0 bytes 083947f9
- 004c50b4 ["INT_ADD", "register:40f0:8", ["const:4c50b4:8", "const:4:8"]]
- 004c50b4 ["CALL", null, ["callee:00543c5c:8"]]
+ 004c50f4 ["INT_ADD", "register:40f0:8", ["const:4c50f4:8", "const:4:8"]]
+ 004c50f4 ["CALL", null, ["callee:00543c5c:8"]]
- 004c50b4 bytes dafa0194
+ 004c50f4 bytes dafa0194
- 004c50bc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a90:8"]]
- 004c50bc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c50fc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e90:8"]]
+ 004c50fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c50bc bytes 084945f9
+ 004c50fc bytes 084947f9
~~~


<a id="compare-d212734cc536c7efc477f52a341dbdd9"></a>

### [`004c5228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c5/004c5228.md) → [`004c5268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c5268.md) _ZN5Botan5ChainC1EPPNS_6FilterEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00543c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543c1c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00543c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543c5c.md)

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
    "old": {
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
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
      "004c5284",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "004c5298",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c52b8",
      "READ",
      [
        "storage",
        "00c9aa90",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c5284",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "004c5298",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c52b8",
      "READ",
      [
        "storage",
        "00c9ae90",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c5244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c5/004c5228.md#insn-004c5244) · [`004c5270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c5/004c5228.md#insn-004c5270) · [`004c5278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c5/004c5228.md#insn-004c5278)
- 新版 `004c5284`（命令位置の公開資料なし） · `004c52b0`（命令位置の公開資料なし） · `004c52b8`（命令位置の公開資料なし）

~~~diff
- 004c5244 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a70:8"]]
- 004c5244 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c5284 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 004c5284 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c5244 bytes 083945f9
+ 004c5284 bytes 083947f9
- 004c5270 ["INT_ADD", "register:40f0:8", ["const:4c5270:8", "const:4:8"]]
- 004c5270 ["CALL", null, ["callee:00543c5c:8"]]
+ 004c52b0 ["INT_ADD", "register:40f0:8", ["const:4c52b0:8", "const:4:8"]]
+ 004c52b0 ["CALL", null, ["callee:00543c5c:8"]]
- 004c5270 bytes 6bfa0194
+ 004c52b0 bytes 6bfa0194
- 004c5278 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a90:8"]]
- 004c5278 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c52b8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e90:8"]]
+ 004c52b8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c5278 bytes 084945f9
+ 004c52b8 bytes 084947f9
~~~


<a id="compare-cc03f684343ceeb2bb07052393eea0d7"></a>

### [`004c5348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c5/004c5348.md) → [`004c5388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c5388.md) _ZN5Botan4ForkC1EPNS_6FilterES2_S2_S2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00543c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543c1c.md) [`00543d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543d5c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00543c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543c5c.md) [`00543d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543d9c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

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
    "old": {
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
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
      "004c53b4",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "004c53d8",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c53fc",
      "READ",
      [
        "storage",
        "00c9aa98",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c53b4",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "004c53d8",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c53fc",
      "READ",
      [
        "storage",
        "00c9ae98",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c5374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c5/004c5348.md#insn-004c5374) · [`004c5394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c5/004c5348.md#insn-004c5394) · [`004c53b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c5/004c5348.md#insn-004c53b0)
- 新版 `004c53b4`（命令位置の公開資料なし） · `004c53f0`（命令位置の公開資料なし）

~~~diff
- 004c5374 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a70:8"]]
- 004c5374 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c53b4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e70:8"]]
+ 004c53b4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c5374 bytes 293945f9
+ 004c53b4 bytes 293947f9
- 004c5394 ["COPY", "register:40c0:8", ["register:4000:8"]]
- 004c5394 bytes f80300aa
- 004c53b0 ["INT_ADD", "register:40f0:8", ["const:4c53b0:8", "const:4:8"]]
- 004c53b0 ["CALL", null, ["callee:00543c5c:8"]]
+ 004c53f0 ["INT_ADD", "register:40f0:8", ["const:4c53f0:8", "const:4:8"]]
+ 004c53f0 ["CALL", null, ["callee:00543c5c:8"]]
- 004c53b0 bytes 1bfa0194
+ 004c53f0 bytes 1bfa0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fb4be5aaf7c469e9a5d10e17291315a"></a>

### [`004c54a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c5/004c54a0.md) → [`004c54e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c54e0.md) _ZN5Botan4ForkC1EPPNS_6FilterEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00543c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543c1c.md) [`00543d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543d5c.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00543c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543c5c.md) [`00543d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543d9c.md)

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
    "old": {
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
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
      "004c54fc",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "004c5510",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c5530",
      "READ",
      [
        "storage",
        "00c9aa98",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c54fc",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "004c5510",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c5530",
      "READ",
      [
        "storage",
        "00c9ae98",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c54bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c5/004c54a0.md#insn-004c54bc) · [`004c54e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c5/004c54a0.md#insn-004c54e8) · [`004c54f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c5/004c54a0.md#insn-004c54f0)
- 新版 `004c54fc`（命令位置の公開資料なし） · `004c5528`（命令位置の公開資料なし） · `004c5530`（命令位置の公開資料なし）

~~~diff
- 004c54bc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a70:8"]]
- 004c54bc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c54fc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 004c54fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c54bc bytes 083945f9
+ 004c54fc bytes 083947f9
- 004c54e8 ["INT_ADD", "register:40f0:8", ["const:4c54e8:8", "const:4:8"]]
- 004c54e8 ["CALL", null, ["callee:00543c5c:8"]]
+ 004c5528 ["INT_ADD", "register:40f0:8", ["const:4c5528:8", "const:4:8"]]
+ 004c5528 ["CALL", null, ["callee:00543c5c:8"]]
- 004c54e8 bytes cdf90194
+ 004c5528 bytes cdf90194
- 004c54f0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a98:8"]]
- 004c54f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c5530 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e98:8"]]
+ 004c5530 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c54f0 bytes 084d45f9
+ 004c5530 bytes 084d47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae657732118018ddef96ece86832b1f9"></a>

### [`004c55a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c5/004c55a8.md) → [`004c55e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c55e8.md) _ZN5Botan15Buffered_FilterC2Emm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58aa0.md) · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 1件 [`00c58ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58ea0.md) · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

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
    "old": {
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
      "004c5610",
      "READ",
      [
        "storage",
        "00c9aaa0",
        null,
        "pointer"
      ]
    ],
    [
      "004c561c",
      "DATA",
      [
        "storage",
        "00c664a8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004c5688",
      "PARAM",
      [
        "storage",
        "002a409d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004c5610",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "004c561c",
      "DATA",
      [
        "storage",
        "00c668a8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004c5688",
      "PARAM",
      [
        "storage",
        "002a416a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c5650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c5/004c55a8.md#insn-004c5650) · [`004c568c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c5/004c55a8.md#insn-004c568c) · [`004c56ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c5/004c55a8.md#insn-004c56ac)
- 新版 `004c5690`（命令位置の公開資料なし） · `004c56cc`（命令位置の公開資料なし） · `004c56ec`（命令位置の公開資料なし）

~~~diff
- 004c5650 ["INT_ADD", "register:40f0:8", ["const:4c5650:8", "const:4:8"]]
- 004c5650 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004c5690 ["INT_ADD", "register:40f0:8", ["const:4c5690:8", "const:4:8"]]
+ 004c5690 ["CALL", null, ["callee:0043ddd8:8"]]
- 004c5650 bytes d2e1fd97
+ 004c5690 bytes d2e1fd97
- 004c568c ["INT_ADD", "register:40f0:8", ["const:4c568c:8", "const:4:8"]]
- 004c568c ["CALL", null, ["callee:00c57f10:8"]]
+ 004c56cc ["INT_ADD", "register:40f0:8", ["const:4c56cc:8", "const:4:8"]]
+ 004c56cc ["CALL", null, ["callee:00c57f10:8"]]
- 004c568c bytes 21491e94
+ 004c56cc bytes 114a1e94
- 004c56ac ["INT_ADD", "register:40f0:8", ["const:4c56ac:8", "const:4:8"]]
- 004c56ac ["CALL", null, ["callee:0043ddd8:8"]]
+ 004c56ec ["INT_ADD", "register:40f0:8", ["const:4c56ec:8", "const:4:8"]]
+ 004c56ec ["CALL", null, ["callee:0043ddd8:8"]]
- 004c56ac bytes bbe1fd97
+ 004c56ec bytes bbe1fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-423d7b7dd79208f3a9592de5dbe6f740"></a>

### [`004c5894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c5/004c5894.md) → [`004c58d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c58d4.md) _ZN5Botan15Buffered_Filter7end_msgEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58ac0.md) · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`00c58ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58ec0.md) · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
    "old": {
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c59d0",
      "incomplete_value": false,
      "site": "004c59e0",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004c5990",
      "incomplete_value": false,
      "site": "004c59a0",
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
      "004c599c",
      "PARAM",
      [
        "storage",
        "002a306f",
        null,
        "string"
      ]
    ],
    [
      "004c59d0",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004c59d4",
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
      "004c599c",
      "PARAM",
      [
        "storage",
        "002a313c",
        null,
        "string"
      ]
    ],
    [
      "004c59d0",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004c59d4",
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

- 旧版 [`004c5964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c5/004c5894.md#insn-004c5964) · [`004c59a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c5/004c5894.md#insn-004c59a0) · [`004c5900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c5/004c5894.md#insn-004c5900)
- 新版 `004c59a4`（命令位置の公開資料なし） · `004c59e0`（命令位置の公開資料なし） · `004c5940`（命令位置の公開資料なし）

~~~diff
- 004c5964 ["INT_ADD", "register:40f0:8", ["const:4c5964:8", "const:4:8"]]
- 004c5964 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004c59a4 ["INT_ADD", "register:40f0:8", ["const:4c59a4:8", "const:4:8"]]
+ 004c59a4 ["CALL", null, ["callee:0043ddd8:8"]]
- 004c5964 bytes 0de1fd97
+ 004c59a4 bytes 0de1fd97
- 004c59a0 ["INT_ADD", "register:40f0:8", ["const:4c59a0:8", "const:4:8"]]
- 004c59a0 ["CALL", null, ["callee:00c57f10:8"]]
+ 004c59e0 ["INT_ADD", "register:40f0:8", ["const:4c59e0:8", "const:4:8"]]
+ 004c59e0 ["CALL", null, ["callee:00c57f10:8"]]
- 004c59a0 bytes 5c481e94
+ 004c59e0 bytes 4c491e94
- 004c5900 ["COPY", "register:0:8", ["register:4040:8"]]
- 004c5900 ["INT_ADD", "register:40f0:8", ["const:4c5900:8", "const:4:8"]]
- 004c5900 ["CALLIND", null, ["register:0:8"]]
+ 004c5940 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c5940 ["INT_ADD", "register:40f0:8", ["const:4c5940:8", "const:4:8"]]
+ 004c5940 ["CALLIND", null, ["register:0:8"]]
- 004c5900 bytes 00013fd6
+ 004c5940 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4e9f3f5052d701dce1ac5aad2f59e68"></a>

### [`004c59f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c5/004c59f0.md) → [`004c5a30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c5a30.md) _ZN5Botan18Cipher_Mode_FilterC1EPNS_11Cipher_ModeE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c58b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58b90.md) · 呼出先 7件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`00543c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543c1c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)
- 新版 呼出元 1件 [`00c58f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58f90.md) · 呼出先 7件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md) [`00543c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543c5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)

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
    "old": {
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
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
      "004c5a4c",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "004c5a5c",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c5a7c",
      "READ",
      [
        "storage",
        "00c9aaa8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c5a4c",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "004c5a5c",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c5a7c",
      "READ",
      [
        "storage",
        "00c9aea8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c5a0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c5/004c59f0.md#insn-004c5a0c) · [`004c5a5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c5/004c59f0.md#insn-004c5a5c) · [`004c5b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c5/004c59f0.md#insn-004c5b2c)
- 新版 `004c5a4c`（命令位置の公開資料なし） · `004c5a9c`（命令位置の公開資料なし） · `004c5b6c`（命令位置の公開資料なし）

~~~diff
- 004c5a0c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a70:8"]]
- 004c5a0c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c5a4c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 004c5a4c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c5a0c bytes 083945f9
+ 004c5a4c bytes 083947f9
- 004c5a5c ["COPY", "register:0:8", ["register:4040:8"]]
- 004c5a5c ["INT_ADD", "register:40f0:8", ["const:4c5a5c:8", "const:4:8"]]
- 004c5a5c ["CALLIND", null, ["register:0:8"]]
+ 004c5a9c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c5a9c ["INT_ADD", "register:40f0:8", ["const:4c5a9c:8", "const:4:8"]]
+ 004c5a9c ["CALLIND", null, ["register:0:8"]]
- 004c5a5c bytes 00013fd6
+ 004c5a9c bytes 00013fd6
- 004c5b2c ["INT_ADD", "register:40f0:8", ["const:4c5b2c:8", "const:4:8"]]
- 004c5b2c ["CALL", null, ["callee:004b3508:8"]]
+ 004c5b6c ["INT_ADD", "register:40f0:8", ["const:4c5b6c:8", "const:4:8"]]
+ 004c5b6c ["CALL", null, ["callee:004b3508:8"]]
- 004c5b2c bytes 67b6ff97
+ 004c5b6c bytes 67b6ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b27c0802eac32d8333e972fad74e6e02"></a>

### [`004c5db8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c5/004c5db8.md) → [`004c5df8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c5/004c5df8.md) _ZN5Botan18Cipher_Mode_Filter9start_msgEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 0件  · 呼出先 7件 [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
    "old": {
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
    "ordinal": 4,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
      "004c5eb0",
      "PARAM",
      [
        "storage",
        "002b7290",
        null,
        "string"
      ]
    ],
    [
      "004c5edc",
      "PARAM",
      [
        "storage",
        "002ac6ec",
        null,
        "string"
      ]
    ],
    [
      "004c5f2c",
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
      "004c5eb0",
      "PARAM",
      [
        "storage",
        "002b72d0",
        null,
        "string"
      ]
    ],
    [
      "004c5edc",
      "PARAM",
      [
        "storage",
        "002ac72c",
        null,
        "string"
      ]
    ],
    [
      "004c5f2c",
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

- 旧版 [`004c5e7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c5/004c5db8.md#insn-004c5e7c) · [`004c5ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c5/004c5db8.md#insn-004c5ea4) · [`004c5efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c5/004c5db8.md#insn-004c5efc)
- 新版 `004c5ebc`（命令位置の公開資料なし） · `004c5ee4`（命令位置の公開資料なし） · `004c5f3c`（命令位置の公開資料なし）

~~~diff
- 004c5e7c ["INT_ADD", "register:40f0:8", ["const:4c5e7c:8", "const:4:8"]]
- 004c5e7c ["CALL", null, ["callee:00c57f60:8"]]
+ 004c5ebc ["INT_ADD", "register:40f0:8", ["const:4c5ebc:8", "const:4:8"]]
+ 004c5ebc ["CALL", null, ["callee:00c57f60:8"]]
- 004c5e7c bytes 39471e94
+ 004c5ebc bytes 29481e94
- 004c5ea4 ["INT_ADD", "register:40f0:8", ["const:4c5ea4:8", "const:4:8"]]
- 004c5ea4 ["CALL", null, ["callee:00c57f70:8"]]
+ 004c5ee4 ["INT_ADD", "register:40f0:8", ["const:4c5ee4:8", "const:4:8"]]
+ 004c5ee4 ["CALL", null, ["callee:00c57f70:8"]]
- 004c5ea4 bytes 33471e94
+ 004c5ee4 bytes 23481e94
- 004c5efc ["INT_ADD", "register:40f0:8", ["const:4c5efc:8", "const:4:8"]]
- 004c5efc ["CALL", null, ["callee:00c57f10:8"]]
+ 004c5f3c ["INT_ADD", "register:40f0:8", ["const:4c5f3c:8", "const:4:8"]]
+ 004c5f3c ["CALL", null, ["callee:00c57f10:8"]]
- 004c5efc bytes 05471e94
+ 004c5f3c bytes f5471e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9a6278d9046e79bbbde78b8cd53661e"></a>

### [`004c6174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c6174.md) → [`004c61b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c61b4.md) _ZN5Botan15DataSink_Stream5writeEPKhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md)

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
    "old": {
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
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c626c",
      "incomplete_value": false,
      "site": "004c627c",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004c622c",
      "incomplete_value": false,
      "site": "004c623c",
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
      "004c6230",
      "PARAM",
      [
        "storage",
        "002b7298",
        null,
        "string"
      ]
    ],
    [
      "004c626c",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004c6270",
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
      "004c6230",
      "PARAM",
      [
        "storage",
        "002b72d8",
        null,
        "string"
      ]
    ],
    [
      "004c626c",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004c6270",
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

- 旧版 [`004c61fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c6174.md#insn-004c61fc) · [`004c623c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c6174.md#insn-004c623c) · [`004c619c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c6174.md#insn-004c619c)
- 新版 `004c623c`（命令位置の公開資料なし） · `004c627c`（命令位置の公開資料なし） · `004c61dc`（命令位置の公開資料なし）

~~~diff
- 004c61fc ["INT_ADD", "register:40f0:8", ["const:4c61fc:8", "const:4:8"]]
- 004c61fc ["CALL", null, ["callee:00c580b0:8"]]
+ 004c623c ["INT_ADD", "register:40f0:8", ["const:4c623c:8", "const:4:8"]]
+ 004c623c ["CALL", null, ["callee:00c580b0:8"]]
- 004c61fc bytes ad461e94
+ 004c623c bytes 9d471e94
- 004c623c ["INT_ADD", "register:40f0:8", ["const:4c623c:8", "const:4:8"]]
- 004c623c ["CALL", null, ["callee:00c57f10:8"]]
+ 004c627c ["INT_ADD", "register:40f0:8", ["const:4c627c:8", "const:4:8"]]
+ 004c627c ["CALL", null, ["callee:00c57f10:8"]]
- 004c623c bytes 35461e94
+ 004c627c bytes 25471e94
- 004c619c ["INT_ADD", "register:40f0:8", ["const:4c619c:8", "const:4:8"]]
- 004c619c ["CALL", null, ["callee:00c58c70:8"]]
+ 004c61dc ["INT_ADD", "register:40f0:8", ["const:4c61dc:8", "const:4:8"]]
+ 004c61dc ["CALL", null, ["callee:00c58c70:8"]]
- 004c619c bytes b5491e94
+ 004c61dc bytes a54a1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-409267a19d82c8bf3b9bae3f85c790fb"></a>

### [`004c6298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c6298.md) → [`004c62d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c62d8.md) _ZN5Botan15DataSink_StreamC2ERNSt6__ndk113basic_ostreamIcNS1_11char_traitsIcEEEERKNS1_12basic_stringIcS4_NS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00543c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543c1c.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00543c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543c5c.md)

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
    "old": {
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
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
      "004c62f4",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "004c6308",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c6328",
      "READ",
      [
        "storage",
        "00c9aab8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c62f4",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "004c6308",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c6328",
      "READ",
      [
        "storage",
        "00c9aeb8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c62b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c6298.md#insn-004c62b4) · [`004c62e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c6298.md#insn-004c62e0) · [`004c62e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c6298.md#insn-004c62e8)
- 新版 `004c62f4`（命令位置の公開資料なし） · `004c6320`（命令位置の公開資料なし） · `004c6328`（命令位置の公開資料なし）

~~~diff
- 004c62b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a70:8"]]
- 004c62b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c62f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 004c62f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c62b4 bytes 083945f9
+ 004c62f4 bytes 083947f9
- 004c62e0 ["INT_ADD", "register:40f0:8", ["const:4c62e0:8", "const:4:8"]]
- 004c62e0 ["CALL", null, ["callee:00543c5c:8"]]
+ 004c6320 ["INT_ADD", "register:40f0:8", ["const:4c6320:8", "const:4:8"]]
+ 004c6320 ["CALL", null, ["callee:00543c5c:8"]]
- 004c62e0 bytes 4ff60194
+ 004c6320 bytes 4ff60194
- 004c62e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
- 004c62e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c6328 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:eb8:8"]]
+ 004c6328 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c62e8 bytes 085d45f9
+ 004c6328 bytes 085d47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12bd5f3ff78181ffd652a927105cbc44"></a>

### [`004c6374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c6374.md) → [`004c63b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c63b4.md) _ZN5Botan15DataSink_StreamC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEb

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 10件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`004c6594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c6594.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00543c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543c1c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`004c65d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c65d4.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00543c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543c5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
    "old": {
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
      "004c63dc",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "004c63f8",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c6418",
      "READ",
      [
        "storage",
        "00c9aab8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c63dc",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "004c63f8",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c6418",
      "READ",
      [
        "storage",
        "00c9aeb8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c6494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c6374.md#insn-004c6494) · [`004c64d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c6374.md#insn-004c64d0) · [`004c639c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c6374.md#insn-004c639c)
- 新版 `004c64d4`（命令位置の公開資料なし） · `004c6510`（命令位置の公開資料なし） · `004c63dc`（命令位置の公開資料なし）

~~~diff
- 004c6494 ["INT_ADD", "register:40f0:8", ["const:4c6494:8", "const:4:8"]]
- 004c6494 ["CALL", null, ["callee:00c580b0:8"]]
+ 004c64d4 ["INT_ADD", "register:40f0:8", ["const:4c64d4:8", "const:4:8"]]
+ 004c64d4 ["CALL", null, ["callee:00c580b0:8"]]
- 004c6494 bytes 07461e94
+ 004c64d4 bytes f7461e94
- 004c64d0 ["INT_ADD", "register:40f0:8", ["const:4c64d0:8", "const:4:8"]]
- 004c64d0 ["CALL", null, ["callee:00c57f10:8"]]
+ 004c6510 ["INT_ADD", "register:40f0:8", ["const:4c6510:8", "const:4:8"]]
+ 004c6510 ["CALL", null, ["callee:00c57f10:8"]]
- 004c64d0 bytes 90451e94
+ 004c6510 bytes 80461e94
- 004c639c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a70:8"]]
- 004c639c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c63dc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e70:8"]]
+ 004c63dc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c639c bytes 293945f9
+ 004c63dc bytes 293947f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fb183a1beb26781778d2e513ea9e56c"></a>

### [`004c6594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c6594.md) → [`004c65d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c65d4.md) FUN_004c65d4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004c6374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c6374.md) · 呼出先 4件 [`00c57de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57de0.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c58b00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58b00.md) [`00c58b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58b10.md)
- 新版 呼出元 1件 [`004c63b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c63b4.md) · 呼出先 4件 [`00c581e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581e0.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c58f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58f00.md) [`00c58f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58f10.md)

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
    "old": {
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
    "old": {
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
      "004c65f8",
      "READ",
      [
        "storage",
        "00c9aac0",
        null,
        "pointer"
      ]
    ],
    [
      "004c65fc",
      "READ",
      [
        "storage",
        "00c9aac8",
        null,
        "pointer"
      ]
    ],
    [
      "004c6610",
      "READ",
      [
        "storage",
        "00c92cd0",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "004c65f8",
      "READ",
      [
        "storage",
        "00c9aec0",
        null,
        "pointer"
      ]
    ],
    [
      "004c65fc",
      "READ",
      [
        "storage",
        "00c9aec8",
        null,
        "pointer"
      ]
    ],
    [
      "004c6610",
      "READ",
      [
        "storage",
        "00c930d0",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c661c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c6594.md#insn-004c661c) · [`004c65b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c6594.md#insn-004c65b8) · [`004c65bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c6594.md#insn-004c65bc)
- 新版 `004c665c`（命令位置の公開資料なし） · `004c65f8`（命令位置の公開資料なし） · `004c65fc`（命令位置の公開資料なし）

~~~diff
- 004c661c ["INT_ADD", "register:40f0:8", ["const:4c661c:8", "const:4:8"]]
- 004c661c ["CALL", null, ["callee:00c58f00:8"]]
+ 004c665c ["INT_ADD", "register:40f0:8", ["const:4c665c:8", "const:4:8"]]
+ 004c665c ["CALL", null, ["callee:00c58f00:8"]]
- 004c661c bytes 39491e94
+ 004c665c bytes 294a1e94
- 004c65b8 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:ac0:8"]]
- 004c65b8 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c65f8 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:ec0:8"]]
+ 004c65f8 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
- 004c65b8 bytes 396345f9
+ 004c65f8 bytes 396347f9
- 004c65bc ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:ac8:8"]]
- 004c65bc ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c65fc ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:ec8:8"]]
+ 004c65fc ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 004c65bc bytes 186745f9
+ 004c65fc bytes 186747f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cdcc6d59b81df17a05bfd6403874a9b5"></a>

### [`004c69c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c69c4.md) → [`004c6a04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c6a04.md) _ZN5Botan6Filter8set_portEm

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
    "old": {
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
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c6aa8",
      "incomplete_value": false,
      "site": "004c6ab8",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004c6a68",
      "incomplete_value": false,
      "site": "004c6a78",
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
      "004c6a70",
      "PARAM",
      [
        "storage",
        "002c103d",
        null,
        "string"
      ]
    ],
    [
      "004c6aa8",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004c6aac",
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
      "004c6a70",
      "PARAM",
      [
        "storage",
        "002c107d",
        null,
        "string"
      ]
    ],
    [
      "004c6aa8",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004c6aac",
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

- 旧版 [`004c6a38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c69c4.md#insn-004c6a38) · [`004c6a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c69c4.md#insn-004c6a78) · [`004c6a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c69c4.md#insn-004c6a24)
- 新版 `004c6a78`（命令位置の公開資料なし） · `004c6ab8`（命令位置の公開資料なし） · `004c6a64`（命令位置の公開資料なし）

~~~diff
- 004c6a38 ["INT_ADD", "register:40f0:8", ["const:4c6a38:8", "const:4:8"]]
- 004c6a38 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004c6a78 ["INT_ADD", "register:40f0:8", ["const:4c6a78:8", "const:4:8"]]
+ 004c6a78 ["CALL", null, ["callee:0043ddd8:8"]]
- 004c6a38 bytes d8dcfd97
+ 004c6a78 bytes d8dcfd97
- 004c6a78 ["INT_ADD", "register:40f0:8", ["const:4c6a78:8", "const:4:8"]]
- 004c6a78 ["CALL", null, ["callee:00c57f10:8"]]
+ 004c6ab8 ["INT_ADD", "register:40f0:8", ["const:4c6ab8:8", "const:4:8"]]
+ 004c6ab8 ["CALL", null, ["callee:00c57f10:8"]]
- 004c6a78 bytes 26441e94
+ 004c6ab8 bytes 16451e94
- 004c6a24 ["INT_ADD", "register:40f0:8", ["const:4c6a24:8", "const:4:8"]]
- 004c6a24 ["CALL", null, ["callee:00c57ef0:8"]]
+ 004c6a64 ["INT_ADD", "register:40f0:8", ["const:4c6a64:8", "const:4:8"]]
+ 004c6a64 ["CALL", null, ["callee:00c57ef0:8"]]
- 004c6a24 bytes 33441e94
+ 004c6a64 bytes 23451e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16a47ce6f6b377732bf9e5b0eac68c2a"></a>

### [`004c6b04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c6b04.md) → [`004c6b44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c6b44.md) _ZN5Botan10get_cipherERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEENS_10Cipher_DirE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58b70.md) · 呼出先 8件 [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`00c58f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58f70.md) · 呼出先 8件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
    "old": {
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c6be4",
      "incomplete_value": false,
      "site": "004c6bf0",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004c6ba4",
      "incomplete_value": false,
      "site": "004c6bb0",
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
      "004c6be4",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004c6be8",
      "READ",
      [
        "storage",
        "00c9aad0",
        null,
        "pointer"
      ]
    ],
    [
      "004c6be8",
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
      "004c6be4",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004c6be8",
      "READ",
      [
        "storage",
        "00c9aed0",
        null,
        "pointer"
      ]
    ],
    [
      "004c6be8",
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

- 旧版 [`004c6bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c6b04.md#insn-004c6bb0) · [`004c6b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c6b04.md#insn-004c6b30) · [`004c6b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c6b04.md#insn-004c6b40)
- 新版 `004c6bf0`（命令位置の公開資料なし） · `004c6b70`（命令位置の公開資料なし） · `004c6b80`（命令位置の公開資料なし）

~~~diff
- 004c6bb0 ["INT_ADD", "register:40f0:8", ["const:4c6bb0:8", "const:4:8"]]
- 004c6bb0 ["CALL", null, ["callee:00c57f10:8"]]
+ 004c6bf0 ["INT_ADD", "register:40f0:8", ["const:4c6bf0:8", "const:4:8"]]
+ 004c6bf0 ["CALL", null, ["callee:00c57f10:8"]]
- 004c6bb0 bytes d8431e94
+ 004c6bf0 bytes c8441e94
- 004c6b30 ["INT_ADD", "register:40f0:8", ["const:4c6b30:8", "const:4:8"]]
- 004c6b30 ["CALL", null, ["callee:00c58f80:8"]]
+ 004c6b70 ["INT_ADD", "register:40f0:8", ["const:4c6b70:8", "const:4:8"]]
+ 004c6b70 ["CALL", null, ["callee:00c58f80:8"]]
- 004c6b30 bytes 14481e94
+ 004c6b70 bytes 04491e94
- 004c6b40 ["INT_ADD", "register:40f0:8", ["const:4c6b40:8", "const:4:8"]]
- 004c6b40 ["CALL", null, ["callee:00c57e90:8"]]
+ 004c6b80 ["INT_ADD", "register:40f0:8", ["const:4c6b80:8", "const:4:8"]]
+ 004c6b80 ["CALL", null, ["callee:00c57e90:8"]]
- 004c6b40 bytes d4431e94
+ 004c6b80 bytes c4441e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac9221f743061b1ad6a57a07617a11d0"></a>

### [`004c6c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c6c08.md) → [`004c6c48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c6/004c6c48.md) _ZN5Botan15get_cipher_modeERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEENS_10Cipher_DirES8_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58b80.md) · 呼出先 27件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00459490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md) [`004d1ae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d1/004d1ae4.md) [`004d1b7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d1/004d1b7c.md) [`00547b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547b2c.md)
- 新版 呼出元 1件 [`00c58f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58f80.md) · 呼出先 27件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`004594d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) [`004d1b24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d1/004d1b24.md) [`004d1bbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d1/004d1bbc.md) [`00547b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00547/00547b6c.md)

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
    "old": {
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
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
    "old": {
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
      "004c6ca0",
      "READ",
      [
        "storage",
        "00c9aad8",
        null,
        "pointer"
      ]
    ],
    [
      "004c6ca8",
      "DATA",
      [
        "storage",
        "00c69960",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "004c6d10",
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
      "004c6ca0",
      "READ",
      [
        "storage",
        "00c9aed8",
        null,
        "pointer"
      ]
    ],
    [
      "004c6ca8",
      "DATA",
      [
        "storage",
        "00c69d60",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "004c6d10",
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

- 旧版 [`004c6d58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c6c08.md#insn-004c6d58) · [`004c6ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c6c08.md#insn-004c6ddc) · [`004c6e38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c6c08.md#insn-004c6e38)
- 新版 `004c6d98`（命令位置の公開資料なし） · `004c6e1c`（命令位置の公開資料なし） · `004c6e78`（命令位置の公開資料なし）

~~~diff
- 004c6d58 ["INT_ADD", "register:40f0:8", ["const:4c6d58:8", "const:4:8"]]
- 004c6d58 ["CALL", null, ["callee:0043bb20:8"]]
+ 004c6d98 ["INT_ADD", "register:40f0:8", ["const:4c6d98:8", "const:4:8"]]
+ 004c6d98 ["CALL", null, ["callee:0043bb20:8"]]
- 004c6d58 bytes 62d3fd97
+ 004c6d98 bytes 62d3fd97
- 004c6ddc ["INT_ADD", "register:40f0:8", ["const:4c6ddc:8", "const:4:8"]]
- 004c6ddc ["CALL", null, ["callee:00c581f0:8"]]
+ 004c6e1c ["INT_ADD", "register:40f0:8", ["const:4c6e1c:8", "const:4:8"]]
+ 004c6e1c ["CALL", null, ["callee:00c581f0:8"]]
- 004c6ddc bytes 05441e94
+ 004c6e1c bytes f5441e94
- 004c6e38 ["INT_ADD", "register:40f0:8", ["const:4c6e38:8", "const:4:8"]]
- 004c6e38 ["CALL", null, ["callee:004594d0:8"]]
+ 004c6e78 ["INT_ADD", "register:40f0:8", ["const:4c6e78:8", "const:4:8"]]
+ 004c6e78 ["CALL", null, ["callee:004594d0:8"]]
- 004c6e38 bytes 9649fe97
+ 004c6e78 bytes 9649fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b26a261e3cc67e182b89c3583ae6b23"></a>

### [`004c780c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c7/004c780c.md) → [`004c784c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c7/004c784c.md) _ZN5Botan11SecureQueue4readEPhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58bf0.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)
- 新版 呼出元 1件 [`00c58ff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58ff0.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)

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
    "old": {
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
      "004c7910",
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
      "004c7910",
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

- 旧版 [`004c78e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c7/004c780c.md#insn-004c78e0) · [`004c7890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c7/004c780c.md#insn-004c7890) · [`004c78d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c7/004c780c.md#insn-004c78d0)
- 新版 `004c7920`（命令位置の公開資料なし） · `004c78d0`（命令位置の公開資料なし） · `004c7910`（命令位置の公開資料なし）

~~~diff
- 004c78e0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c78e0 ["INT_ADD", "register:40f0:8", ["const:4c78e0:8", "const:4:8"]]
- 004c78e0 ["CALLIND", null, ["register:0:8"]]
+ 004c7920 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c7920 ["INT_ADD", "register:40f0:8", ["const:4c7920:8", "const:4:8"]]
+ 004c7920 ["CALLIND", null, ["register:0:8"]]
- 004c78e0 bytes 20013fd6
+ 004c7920 bytes 20013fd6
- 004c7890 ["INT_ADD", "register:40f0:8", ["const:4c7890:8", "const:4:8"]]
- 004c7890 ["CALL", null, ["callee:00c57f40:8"]]
+ 004c78d0 ["INT_ADD", "register:40f0:8", ["const:4c78d0:8", "const:4:8"]]
+ 004c78d0 ["CALL", null, ["callee:00c57f40:8"]]
- 004c7890 bytes ac401e94
+ 004c78d0 bytes 9c411e94
- 004c78d0 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:338:8"]]
- 004c78d0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c7910 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:738:8"]]
+ 004c7910 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004c78d0 bytes 499f41f9
+ 004c7910 bytes 499f43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c8cd8549e2a76c2166c740f4ddf57f4"></a>

### [`004c7a88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c7/004c7a88.md) → [`004c7ac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c7/004c7ac8.md) FUN_004c7ac8

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004c8bd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c8bd8.md) · 呼出先 3件 [`00543e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543e8c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58250.md)
- 新版 呼出元 1件 [`004c8c18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8c18.md) · 呼出先 3件 [`00543ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543ecc.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58650.md)

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
    "old": {
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
      "004c7ba0",
      "PARAM",
      [
        "storage",
        "002a9adb",
        null,
        "string"
      ]
    ],
    [
      "004c7ba8",
      "PARAM",
      [
        "storage",
        "002a9ae1",
        null,
        "string"
      ]
    ],
    [
      "004c7bb0",
      "PARAM",
      [
        "storage",
        "002a6500",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004c7ba0",
      "PARAM",
      [
        "storage",
        "002a9ba8",
        null,
        "string"
      ]
    ],
    [
      "004c7ba8",
      "PARAM",
      [
        "storage",
        "002a9bae",
        null,
        "string"
      ]
    ],
    [
      "004c7bb0",
      "PARAM",
      [
        "storage",
        "002a65dc",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c7b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c7/004c7a88.md#insn-004c7b78) · [`004c7b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c7/004c7a88.md#insn-004c7b80) · [`004c7bb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c7/004c7a88.md#insn-004c7bb8)
- 新版 `004c7bb8`（命令位置の公開資料なし） · `004c7bc0`（命令位置の公開資料なし） · `004c7bf8`（命令位置の公開資料なし）

~~~diff
- 004c7b78 ["COPY", "tmp:0:8", ["const:267:8"]]
- 004c7b78 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 004c7b78 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 004c7b78 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 004c7bb8 ["COPY", "tmp:0:8", ["const:dcb:8"]]
+ 004c7bb8 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 004c7bb8 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 004c7bb8 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 004c7b78 bytes 639c0991
+ 004c7bb8 bytes 632c3791
- 004c7b80 ["INT_ADD", "register:40f0:8", ["const:4c7b80:8", "const:4:8"]]
- 004c7b80 ["CALL", null, ["callee:00c58650:8"]]
+ 004c7bc0 ["INT_ADD", "register:40f0:8", ["const:4c7bc0:8", "const:4:8"]]
+ 004c7bc0 ["CALL", null, ["callee:00c58650:8"]]
- 004c7b80 bytes b4411e94
+ 004c7bc0 bytes a4421e94
- 004c7bb8 ["INT_ADD", "register:40f0:8", ["const:4c7bb8:8", "const:4:8"]]
- 004c7bb8 ["CALL", null, ["callee:00c58650:8"]]
+ 004c7bf8 ["INT_ADD", "register:40f0:8", ["const:4c7bf8:8", "const:4:8"]]
+ 004c7bf8 ["CALL", null, ["callee:00c58650:8"]]
- 004c7bb8 bytes a6411e94
+ 004c7bf8 bytes 96421e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9872ad7983f375ef7eb10144cc5edaee"></a>

### [`004c7d38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c7/004c7d38.md) → [`004c7d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c7/004c7d78.md) _ZN5Botan4PipeC1EPNS_6FilterES2_S2_S2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c58c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c59010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59010.md)

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
    "old": {
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
      "004c7d98",
      "READ",
      [
        "storage",
        "00c9ab00",
        null,
        "pointer"
      ]
    ],
    [
      "004c7db4",
      "DATA",
      [
        "storage",
        "00c66640",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "004c7d98",
      "READ",
      [
        "storage",
        "00c9af00",
        null,
        "pointer"
      ]
    ],
    [
      "004c7db4",
      "DATA",
      [
        "storage",
        "00c66a40",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c7d58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c7/004c7d38.md#insn-004c7d58) · [`004c7d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c7/004c7d38.md#insn-004c7d7c) · [`004c7da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c7/004c7d38.md#insn-004c7da4)
- 新版 `004c7d98`（命令位置の公開資料なし） · `004c7dbc`（命令位置の公開資料なし） · `004c7de4`（命令位置の公開資料なし）

~~~diff
- 004c7d58 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b00:8"]]
- 004c7d58 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c7d98 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f00:8"]]
+ 004c7d98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c7d58 bytes 088145f9
+ 004c7d98 bytes 088147f9
- 004c7d7c ["INT_ADD", "register:40f0:8", ["const:4c7d7c:8", "const:4:8"]]
- 004c7d7c ["CALL", null, ["callee:00c57e90:8"]]
+ 004c7dbc ["INT_ADD", "register:40f0:8", ["const:4c7dbc:8", "const:4:8"]]
+ 004c7dbc ["CALL", null, ["callee:00c57e90:8"]]
- 004c7d7c bytes 453f1e94
+ 004c7dbc bytes 35401e94
- 004c7da4 ["INT_ADD", "register:40f0:8", ["const:4c7da4:8", "const:4:8"]]
- 004c7da4 ["CALL", null, ["callee:00c59010:8"]]
+ 004c7de4 ["INT_ADD", "register:40f0:8", ["const:4c7de4:8", "const:4:8"]]
+ 004c7de4 ["CALL", null, ["callee:00c59010:8"]]
- 004c7da4 bytes 9b431e94
+ 004c7de4 bytes 8b441e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3eabd8bf4f27e8214a3f2010b1440e82"></a>

### [`004c7df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c7/004c7df8.md) → [`004c7e38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c7/004c7e38.md) _ZN5Botan4PipeC2ESt16initializer_listIPNS_6FilterEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c58c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c59010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59010.md)

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
    "old": {
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
      "004c7e54",
      "READ",
      [
        "storage",
        "00c9ab00",
        null,
        "pointer"
      ]
    ],
    [
      "004c7e68",
      "DATA",
      [
        "storage",
        "00c66640",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "004c7e54",
      "READ",
      [
        "storage",
        "00c9af00",
        null,
        "pointer"
      ]
    ],
    [
      "004c7e68",
      "DATA",
      [
        "storage",
        "00c66a40",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c7e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c7/004c7df8.md#insn-004c7e14) · [`004c7e30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c7/004c7df8.md#insn-004c7e30) · [`004c7e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c7/004c7df8.md#insn-004c7e60)
- 新版 `004c7e54`（命令位置の公開資料なし） · `004c7e70`（命令位置の公開資料なし） · `004c7ea0`（命令位置の公開資料なし）

~~~diff
- 004c7e14 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b00:8"]]
- 004c7e14 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c7e54 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f00:8"]]
+ 004c7e54 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c7e14 bytes 088145f9
+ 004c7e54 bytes 088147f9
- 004c7e30 ["INT_ADD", "register:40f0:8", ["const:4c7e30:8", "const:4:8"]]
- 004c7e30 ["CALL", null, ["callee:00c57e90:8"]]
+ 004c7e70 ["INT_ADD", "register:40f0:8", ["const:4c7e70:8", "const:4:8"]]
+ 004c7e70 ["CALL", null, ["callee:00c57e90:8"]]
- 004c7e30 bytes 183f1e94
+ 004c7e70 bytes 08401e94
- 004c7e60 ["INT_ADD", "register:40f0:8", ["const:4c7e60:8", "const:4:8"]]
- 004c7e60 ["CALL", null, ["callee:00c59010:8"]]
+ 004c7ea0 ["INT_ADD", "register:40f0:8", ["const:4c7ea0:8", "const:4:8"]]
+ 004c7ea0 ["CALL", null, ["callee:00c59010:8"]]
- 004c7e60 bytes 6c431e94
+ 004c7ea0 bytes 5c441e94
~~~


<a id="compare-8599844de773e074fbeb35446e46171c"></a>

### [`004c7e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c7/004c7e98.md) → [`004c7ed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c7/004c7ed8.md) _ZN5Botan4Pipe9do_appendEPNS_6FilterE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c10.md) · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 1件 [`00c59010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59010.md) · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

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
    "old": {
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
      "004c7f00",
      "READ",
      [
        "storage",
        "00c9ab08",
        null,
        "pointer"
      ]
    ],
    [
      "004c7fa4",
      "PARAM",
      [
        "storage",
        "002b2a60",
        null,
        "string"
      ]
    ],
    [
      "004c7fdc",
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
      "004c7f00",
      "READ",
      [
        "storage",
        "00c9af08",
        null,
        "pointer"
      ]
    ],
    [
      "004c7fa4",
      "PARAM",
      [
        "storage",
        "002b2aa0",
        null,
        "string"
      ]
    ],
    [
      "004c7fdc",
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

- 旧版 [`004c7f6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c7/004c7e98.md#insn-004c7f6c) · [`004c7fac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c7/004c7e98.md#insn-004c7fac) · [`004c7fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c7/004c7e98.md#insn-004c7fd0)
- 新版 `004c7fac`（命令位置の公開資料なし） · `004c7fec`（命令位置の公開資料なし） · `004c8010`（命令位置の公開資料なし）

~~~diff
- 004c7f6c ["INT_ADD", "register:40f0:8", ["const:4c7f6c:8", "const:4:8"]]
- 004c7f6c ["CALL", null, ["callee:0043ddd8:8"]]
+ 004c7fac ["INT_ADD", "register:40f0:8", ["const:4c7fac:8", "const:4:8"]]
+ 004c7fac ["CALL", null, ["callee:0043ddd8:8"]]
- 004c7f6c bytes 8bd7fd97
+ 004c7fac bytes 8bd7fd97
- 004c7fac ["INT_ADD", "register:40f0:8", ["const:4c7fac:8", "const:4:8"]]
- 004c7fac ["CALL", null, ["callee:00c57f10:8"]]
+ 004c7fec ["INT_ADD", "register:40f0:8", ["const:4c7fec:8", "const:4:8"]]
+ 004c7fec ["CALL", null, ["callee:00c57f10:8"]]
- 004c7fac bytes d93e1e94
+ 004c7fec bytes c93f1e94
- 004c7fd0 ["INT_ADD", "register:40f0:8", ["const:4c7fd0:8", "const:4:8"]]
- 004c7fd0 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004c8010 ["INT_ADD", "register:40f0:8", ["const:4c8010:8", "const:4:8"]]
+ 004c8010 ["CALL", null, ["callee:0043ddd8:8"]]
- 004c7fd0 bytes 72d7fd97
+ 004c8010 bytes 72d7fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1313380f06b3413f20e752614ec4b7d0"></a>

### [`004c8158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c8158.md) → [`004c8198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8198.md) _ZN5Botan4Pipe8destructEPNS_6FilterE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c20.md) · 呼出先 1件 [`00c58c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c20.md)
- 新版 呼出元 1件 [`00c59020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59020.md) · 呼出先 1件 [`00c59020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59020.md)

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
    "old": {
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
      "004c81b4",
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
      "004c81b4",
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

- 旧版 [`004c8174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c8158.md#insn-004c8174) · [`004c81a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c8158.md#insn-004c81a4)
- 新版 `004c81b4`（命令位置の公開資料なし） · `004c81e4`（命令位置の公開資料なし）

~~~diff
- 004c8174 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b08:8"]]
- 004c8174 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c81b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f08:8"]]
+ 004c81b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c8174 bytes 088545f9
+ 004c81b4 bytes 088547f9
- 004c81a4 ["INT_ADD", "register:40f0:8", ["const:4c81a4:8", "const:4:8"]]
- 004c81a4 ["CALL", null, ["callee:00c59020:8"]]
+ 004c81e4 ["INT_ADD", "register:40f0:8", ["const:4c81e4:8", "const:4:8"]]
+ 004c81e4 ["CALL", null, ["callee:00c59020:8"]]
- 004c81a4 bytes 9f421e94
+ 004c81e4 bytes 8f431e94
~~~


<a id="compare-17affefefdf1e90be42f365574f8372b"></a>

### [`004c8258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c8258.md) → [`004c8298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8298.md) _ZNK5Botan4Pipe9remainingEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c40.md) · 呼出先 5件 [`004c96cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c96cc.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`00c59040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59040.md) · 呼出先 5件 [`004c970c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c9/004c970c.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
    "old": {
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c83bc",
      "incomplete_value": false,
      "site": "004c83c8",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004c837c",
      "incomplete_value": false,
      "site": "004c8388",
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
      "004c82b8",
      "READ",
      [
        "storage",
        "002b4d20",
        null,
        "string"
      ]
    ],
    [
      "004c83bc",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004c83c0",
      "READ",
      [
        "storage",
        "00c9ab10",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004c82b8",
      "READ",
      [
        "storage",
        "002b4d60",
        null,
        "string"
      ]
    ],
    [
      "004c83bc",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004c83c0",
      "READ",
      [
        "storage",
        "00c9af10",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c8388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c8258.md#insn-004c8388) · [`004c8270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c8258.md#insn-004c8270) · [`004c834c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c8258.md#insn-004c834c)
- 新版 `004c83c8`（命令位置の公開資料なし） · `004c82b0`（命令位置の公開資料なし） · `004c838c`（命令位置の公開資料なし）

~~~diff
- 004c8388 ["INT_ADD", "register:40f0:8", ["const:4c8388:8", "const:4:8"]]
- 004c8388 ["CALL", null, ["callee:00c57f10:8"]]
+ 004c83c8 ["INT_ADD", "register:40f0:8", ["const:4c83c8:8", "const:4:8"]]
+ 004c83c8 ["CALL", null, ["callee:00c57f10:8"]]
- 004c8388 bytes e23d1e94
+ 004c83c8 bytes d23e1e94
- 004c8270 ["COPY", "tmp:0:8", ["const:d20:8"]]
- 004c8270 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004c8270 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004c8270 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 004c82b0 ["COPY", "tmp:0:8", ["const:d60:8"]]
+ 004c82b0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 004c82b0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 004c82b0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004c8270 bytes 4a813491
+ 004c82b0 bytes 4a813591
- 004c834c ["INT_ADD", "register:40f0:8", ["const:4c834c:8", "const:4:8"]]
- 004c834c ["CALL", null, ["callee:00c57ef0:8"]]
+ 004c838c ["INT_ADD", "register:40f0:8", ["const:4c838c:8", "const:4:8"]]
+ 004c838c ["CALL", null, ["callee:00c57ef0:8"]]
- 004c834c bytes e93d1e94
+ 004c838c bytes d93e1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a60935abd49e6d5009d27650e243079"></a>

### [`004c83d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c83d0.md) → [`004c8410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8410.md) _ZN5Botan4Pipe15set_default_msgEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

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
    "old": {
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
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c84b8",
      "incomplete_value": false,
      "site": "004c84c8",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004c8478",
      "incomplete_value": false,
      "site": "004c8488",
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
      "004c8480",
      "PARAM",
      [
        "storage",
        "002b1b92",
        null,
        "string"
      ]
    ],
    [
      "004c84b8",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004c84bc",
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
      "004c8480",
      "PARAM",
      [
        "storage",
        "002b1bd2",
        null,
        "string"
      ]
    ],
    [
      "004c84b8",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004c84bc",
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

- 旧版 [`004c8448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c83d0.md#insn-004c8448) · [`004c8488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c83d0.md#insn-004c8488) · [`004c8434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c83d0.md#insn-004c8434)
- 新版 `004c8488`（命令位置の公開資料なし） · `004c84c8`（命令位置の公開資料なし） · `004c8474`（命令位置の公開資料なし）

~~~diff
- 004c8448 ["INT_ADD", "register:40f0:8", ["const:4c8448:8", "const:4:8"]]
- 004c8448 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004c8488 ["INT_ADD", "register:40f0:8", ["const:4c8488:8", "const:4:8"]]
+ 004c8488 ["CALL", null, ["callee:0043ddd8:8"]]
- 004c8448 bytes 54d6fd97
+ 004c8488 bytes 54d6fd97
- 004c8488 ["INT_ADD", "register:40f0:8", ["const:4c8488:8", "const:4:8"]]
- 004c8488 ["CALL", null, ["callee:00c57f10:8"]]
+ 004c84c8 ["INT_ADD", "register:40f0:8", ["const:4c84c8:8", "const:4:8"]]
+ 004c84c8 ["CALL", null, ["callee:00c57f10:8"]]
- 004c8488 bytes a23d1e94
+ 004c84c8 bytes 923e1e94
- 004c8434 ["INT_ADD", "register:40f0:8", ["const:4c8434:8", "const:4:8"]]
- 004c8434 ["CALL", null, ["callee:00c57ef0:8"]]
+ 004c8474 ["INT_ADD", "register:40f0:8", ["const:4c8474:8", "const:4:8"]]
+ 004c8474 ["CALL", null, ["callee:00c57ef0:8"]]
- 004c8434 bytes af3d1e94
+ 004c8474 bytes 9f3e1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3347c9ee0c907df66088c14b5e3cea7"></a>

### [`004c8530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c8530.md) → [`004c8570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8570.md) _ZN5Botan4Pipe9start_msgEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c58c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c50.md) · 呼出先 10件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00543c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543c1c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00c59050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59050.md) · 呼出先 10件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00543c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543c5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
    "old": {
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
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
    "old": {
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
      "004c85bc",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "004c85c8",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c85f4",
      "DATA",
      [
        "storage",
        "00c66758",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004c85bc",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "004c85c8",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c85f4",
      "DATA",
      [
        "storage",
        "00c66b58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004c8618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c8530.md#insn-004c8618) · [`004c8654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c8530.md#insn-004c8654) · [`004c856c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c8530.md#insn-004c856c)
- 新版 `004c8658`（命令位置の公開資料なし） · `004c8694`（命令位置の公開資料なし） · `004c85ac`（命令位置の公開資料なし）

~~~diff
- 004c8618 ["INT_ADD", "register:40f0:8", ["const:4c8618:8", "const:4:8"]]
- 004c8618 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004c8658 ["INT_ADD", "register:40f0:8", ["const:4c8658:8", "const:4:8"]]
+ 004c8658 ["CALL", null, ["callee:0043ddd8:8"]]
- 004c8618 bytes e0d5fd97
+ 004c8658 bytes e0d5fd97
- 004c8654 ["INT_ADD", "register:40f0:8", ["const:4c8654:8", "const:4:8"]]
- 004c8654 ["CALL", null, ["callee:00c57f10:8"]]
+ 004c8694 ["INT_ADD", "register:40f0:8", ["const:4c8694:8", "const:4:8"]]
+ 004c8694 ["CALL", null, ["callee:00c57f10:8"]]
- 004c8654 bytes 2f3d1e94
+ 004c8694 bytes 1f3e1e94
- 004c856c ["INT_ADD", "register:40f0:8", ["const:4c856c:8", "const:4:8"]]
- 004c856c ["CALL", null, ["callee:00c57e90:8"]]
+ 004c85ac ["INT_ADD", "register:40f0:8", ["const:4c85ac:8", "const:4:8"]]
+ 004c85ac ["CALL", null, ["callee:00c57e90:8"]]
- 004c856c bytes 493d1e94
+ 004c85ac bytes 393e1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea402482e1f9d5c263aeb27651f7f0c4"></a>

### [`004c86d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c86d0.md) → [`004c8710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8710.md) _ZN5Botan4Pipe5writeEPKhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c60.md) · 呼出先 6件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 1件 [`00c59060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59060.md) · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

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
    "old": {
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
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c87b4",
      "incomplete_value": false,
      "site": "004c87c4",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004c8774",
      "incomplete_value": false,
      "site": "004c8784",
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
      "004c877c",
      "PARAM",
      [
        "storage",
        "002a0fab",
        null,
        "string"
      ]
    ],
    [
      "004c87b4",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004c87b8",
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
      "004c877c",
      "PARAM",
      [
        "storage",
        "002a1078",
        null,
        "string"
      ]
    ],
    [
      "004c87b4",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004c87b8",
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

- 旧版 [`004c8744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c86d0.md#insn-004c8744) · [`004c8784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c86d0.md#insn-004c8784) · [`004c8730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c86d0.md#insn-004c8730)
- 新版 `004c8784`（命令位置の公開資料なし） · `004c87c4`（命令位置の公開資料なし） · `004c8770`（命令位置の公開資料なし）

~~~diff
- 004c8744 ["INT_ADD", "register:40f0:8", ["const:4c8744:8", "const:4:8"]]
- 004c8744 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004c8784 ["INT_ADD", "register:40f0:8", ["const:4c8784:8", "const:4:8"]]
+ 004c8784 ["CALL", null, ["callee:0043ddd8:8"]]
- 004c8744 bytes 95d5fd97
+ 004c8784 bytes 95d5fd97
- 004c8784 ["INT_ADD", "register:40f0:8", ["const:4c8784:8", "const:4:8"]]
- 004c8784 ["CALL", null, ["callee:00c57f10:8"]]
+ 004c87c4 ["INT_ADD", "register:40f0:8", ["const:4c87c4:8", "const:4:8"]]
+ 004c87c4 ["CALL", null, ["callee:00c57f10:8"]]
- 004c8784 bytes e33c1e94
+ 004c87c4 bytes d33d1e94
- 004c8730 ["INT_ADD", "register:40f0:8", ["const:4c8730:8", "const:4:8"]]
- 004c8730 ["CALL", null, ["callee:00c57ef0:8"]]
+ 004c8770 ["INT_ADD", "register:40f0:8", ["const:4c8770:8", "const:4:8"]]
+ 004c8770 ["CALL", null, ["callee:00c57ef0:8"]]
- 004c8730 bytes f03c1e94
+ 004c8770 bytes e03d1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c6be51d0284e7581d3da6789b970494"></a>

### [`004c87d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c87d8.md) → [`004c8818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8818.md) _ZN5Botan4Pipe7end_msgEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c70.md) · 呼出先 12件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`004c7c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c7/004c7c20.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`00c59070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59070.md) · 呼出先 12件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`004c7c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c7/004c7c60.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
    "old": {
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
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
    "old": {
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
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
    "old": {
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
      "004c8878",
      "READ",
      [
        "storage",
        "00c9aa70",
        null,
        "pointer"
      ]
    ],
    [
      "004c8884",
      "DATA",
      [
        "storage",
        "00c665d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c88a8",
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
      "004c8878",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "004c8884",
      "DATA",
      [
        "storage",
        "00c669d8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004c88a8",
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

- 旧版 [`004c8838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c87d8.md#insn-004c8838) · [`004c8878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c87d8.md#insn-004c8878) · [`004c88d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c87d8.md#insn-004c88d4)
- 新版 `004c8878`（命令位置の公開資料なし） · `004c88b8`（命令位置の公開資料なし） · `004c8914`（命令位置の公開資料なし）

~~~diff
- 004c8838 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a70:8"]]
- 004c8838 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004c8878 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 004c8878 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004c8838 bytes 083945f9
+ 004c8878 bytes 083947f9
- 004c8878 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c8878 ["INT_ADD", "register:40f0:8", ["const:4c8878:8", "const:4:8"]]
- 004c8878 ["CALLIND", null, ["register:0:8"]]
+ 004c88b8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c88b8 ["INT_ADD", "register:40f0:8", ["const:4c88b8:8", "const:4:8"]]
+ 004c88b8 ["CALLIND", null, ["register:0:8"]]
- 004c8878 bytes 20013fd6
+ 004c88b8 bytes 20013fd6
- 004c88d4 ["INT_ADD", "register:40f0:8", ["const:4c88d4:8", "const:4:8"]]
- 004c88d4 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004c8914 ["INT_ADD", "register:40f0:8", ["const:4c8914:8", "const:4:8"]]
+ 004c8914 ["CALL", null, ["callee:0043ddd8:8"]]
- 004c88d4 bytes 31d5fd97
+ 004c8914 bytes 31d5fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e19d1ca4241cc534bcbf7bdfdc1bb3f5"></a>

### [`004c8a74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c8a74.md) → [`004c8ab4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8ab4.md) _ZN5Botan4Pipe5writeERNS_10DataSourceE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58ca0.md) · 呼出先 9件 [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md)
- 新版 呼出元 1件 [`00c590a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c590a0.md) · 呼出先 9件 [`00c37ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ba4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md)

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
    "old": {
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "004c8b90",
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
      "004c8b5c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "004c8bcc",
      "READ",
      [
        "storage",
        "00c9a9e8",
        null,
        "pointer"
      ]
    ],
    [
      "004c8bcc",
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
      "004c8b5c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004c8bcc",
      "READ",
      [
        "storage",
        "00c9ade8",
        null,
        "pointer"
      ]
    ],
    [
      "004c8bcc",
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

- 旧版 [`004c8b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c8a74.md#insn-004c8b30) · [`004c8b94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c8a74.md#insn-004c8b94) · [`004c8bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c8a74.md#insn-004c8bd4)
- 新版 `004c8b70`（命令位置の公開資料なし） · `004c8bd4`（命令位置の公開資料なし） · `004c8c14`（命令位置の公開資料なし）

~~~diff
- 004c8b30 ["COPY", "register:0:8", ["register:4048:8"]]
- 004c8b30 ["INT_ADD", "register:40f0:8", ["const:4c8b30:8", "const:4:8"]]
- 004c8b30 ["CALLIND", null, ["register:0:8"]]
+ 004c8b70 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c8b70 ["INT_ADD", "register:40f0:8", ["const:4c8b70:8", "const:4:8"]]
+ 004c8b70 ["CALLIND", null, ["register:0:8"]]
- 004c8b30 bytes 20013fd6
+ 004c8b70 bytes 20013fd6
- 004c8b94 ["INT_ADD", "register:40f0:8", ["const:4c8b94:8", "const:4:8"]]
- 004c8b94 ["CALL", null, ["callee:00c57f10:8"]]
+ 004c8bd4 ["INT_ADD", "register:40f0:8", ["const:4c8bd4:8", "const:4:8"]]
+ 004c8bd4 ["CALL", null, ["callee:00c57f10:8"]]
- 004c8b94 bytes df3b1e94
+ 004c8bd4 bytes cf3c1e94
- 004c8bd4 ["INT_ADD", "register:40f0:8", ["const:4c8bd4:8", "const:4:8"]]
- 004c8bd4 ["CALL", null, ["callee:00c57ee0:8"]]
+ 004c8c14 ["INT_ADD", "register:40f0:8", ["const:4c8c14:8", "const:4:8"]]
+ 004c8c14 ["CALL", null, ["callee:00c57ee0:8"]]
- 004c8bd4 bytes c33b1e94
+ 004c8c14 bytes b33c1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d61ae312567fd3fb4f1934964da993e7"></a>

### [`004c8d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c8d28.md) → [`004c8d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8d68.md) _ZN5Botan4Pipe13append_filterEPNS_6FilterE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

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
    "old": {
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
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004c8e08",
      "incomplete_value": false,
      "site": "004c8e18",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "old": {
      "definition_site": "004c8dc8",
      "incomplete_value": false,
      "site": "004c8dd8",
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
      "004c8dd0",
      "PARAM",
      [
        "storage",
        "002a53eb",
        null,
        "string"
      ]
    ],
    [
      "004c8e08",
      "PARAM",
      [
        "storage",
        "00535828",
        null,
        null
      ]
    ],
    [
      "004c8e0c",
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
      "004c8dd0",
      "PARAM",
      [
        "storage",
        "002a54c7",
        null,
        "string"
      ]
    ],
    [
      "004c8e08",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004c8e0c",
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

- 旧版 [`004c8d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c8d28.md#insn-004c8d98) · [`004c8dd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c8d28.md#insn-004c8dd8) · [`004c8d84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c8d28.md#insn-004c8d84)
- 新版 `004c8dd8`（命令位置の公開資料なし） · `004c8e18`（命令位置の公開資料なし） · `004c8dc4`（命令位置の公開資料なし）

~~~diff
- 004c8d98 ["INT_ADD", "register:40f0:8", ["const:4c8d98:8", "const:4:8"]]
- 004c8d98 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004c8dd8 ["INT_ADD", "register:40f0:8", ["const:4c8dd8:8", "const:4:8"]]
+ 004c8dd8 ["CALL", null, ["callee:0043ddd8:8"]]
- 004c8d98 bytes 00d4fd97
+ 004c8dd8 bytes 00d4fd97
- 004c8dd8 ["INT_ADD", "register:40f0:8", ["const:4c8dd8:8", "const:4:8"]]
- 004c8dd8 ["CALL", null, ["callee:00c57f10:8"]]
+ 004c8e18 ["INT_ADD", "register:40f0:8", ["const:4c8e18:8", "const:4:8"]]
+ 004c8e18 ["CALL", null, ["callee:00c57f10:8"]]
- 004c8dd8 bytes 4e3b1e94
+ 004c8e18 bytes 3e3c1e94
- 004c8d84 ["INT_ADD", "register:40f0:8", ["const:4c8d84:8", "const:4:8"]]
- 004c8d84 ["CALL", null, ["callee:00c57ef0:8"]]
+ 004c8dc4 ["INT_ADD", "register:40f0:8", ["const:4c8dc4:8", "const:4:8"]]
+ 004c8dc4 ["CALL", null, ["callee:00c57ef0:8"]]
- 004c8d84 bytes 5b3b1e94
+ 004c8dc4 bytes 4b3c1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72393e2a3819fc2d83ff0aefeb2d2b7a"></a>

### [`004c8e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c8e2c.md) → [`004c8e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004c8/004c8e6c.md) _ZN5Botan4Pipe7prependEPNS_6FilterE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004aec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec24.md) [`00535828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535828.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)

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
    "old": {
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
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
      "004c8e9c",
      "READ",
      [
        "storage",
        "00c9ab08",
        null,
        "pointer"
      ]
    ],
    [
      "004c8f38",
      "PARAM",
      [
        "storage",
        "002b6013",
        null,
        "string"
      ]
    ],
    [
      "004c8f70",
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
      "004c8e9c",
      "READ",
      [
        "storage",
        "00c9af08",
        null,
        "pointer"
      ]
    ],
    [
      "004c8f38",
      "PARAM",
      [
        "storage",
        "002b6053",
        null,
        "string"
      ]
    ],
    [
      "004c8f70",
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

- 旧版 [`004c8f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c8e2c.md#insn-004c8f00) · [`004c8f40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c8e2c.md#insn-004c8f40) · [`004c8f64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c8e2c.md#insn-004c8f64)
- 新版 `004c8f40`（命令位置の公開資料なし） · `004c8f80`（命令位置の公開資料なし） · `004c8fa4`（命令位置の公開資料なし）

~~~diff
- 004c8f00 ["INT_ADD", "register:40f0:8", ["const:4c8f00:8", "const:4:8"]]
- 004c8f00 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004c8f40 ["INT_ADD", "register:40f0:8", ["const:4c8f40:8", "const:4:8"]]
+ 004c8f40 ["CALL", null, ["callee:0043ddd8:8"]]
- 004c8f00 bytes a6d3fd97
+ 004c8f40 bytes a6d3fd97
- 004c8f40 ["INT_ADD", "register:40f0:8", ["const:4c8f40:8", "const:4:8"]]
- 004c8f40 ["CALL", null, ["callee:00c57f10:8"]]
+ 004c8f80 ["INT_ADD", "register:40f0:8", ["const:4c8f80:8", "const:4:8"]]
+ 004c8f80 ["CALL", null, ["callee:00c57f10:8"]]
- 004c8f40 bytes f43a1e94
+ 004c8f80 bytes e43b1e94
- 004c8f64 ["INT_ADD", "register:40f0:8", ["const:4c8f64:8", "const:4:8"]]
- 004c8f64 ["CALL", null, ["callee:0043ddd8:8"]]
+ 004c8fa4 ["INT_ADD", "register:40f0:8", ["const:4c8fa4:8", "const:4:8"]]
+ 004c8fa4 ["CALL", null, ["callee:0043ddd8:8"]]
- 004c8f64 bytes 8dd3fd97
+ 004c8fa4 bytes 8dd3fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

