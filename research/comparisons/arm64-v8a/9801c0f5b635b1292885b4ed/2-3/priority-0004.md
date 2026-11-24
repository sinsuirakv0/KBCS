# v16.0.1 → v16.0.2 · 最優先の変更候補 (4)

[一覧の目次](README.md)

<a id="compare-be075abc384f205f2bc2fd817c650a7a"></a>

### [`00463124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463124.md) → [`00463164`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00463/00463164.md) FUN_00463164

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00463190",
      "incomplete_value": false,
      "site": "00463190",
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
            "const:5e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00463150",
      "incomplete_value": false,
      "site": "00463150",
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
            "const:518:8"
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
      "00463190",
      "DATA",
      [
        "storage",
        "00c64518",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00463190",
      "DATA",
      [
        "storage",
        "00c645e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00463138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463124.md#insn-00463138) · [`00463148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463124.md#insn-00463148) · [`0046316c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463124.md#insn-0046316c)
- 新版 `00463178`（命令位置の公開資料なし） · `00463188`（命令位置の公開資料なし） · `004631ac`（命令位置の公開資料なし）

~~~diff
- 00463138 ["INT_ADD", "register:40f0:8", ["const:463138:8", "const:4:8"]]
- 00463138 ["CALL", null, ["callee:00c57f60:8"]]
+ 00463178 ["INT_ADD", "register:40f0:8", ["const:463178:8", "const:4:8"]]
+ 00463178 ["CALL", null, ["callee:00c57f60:8"]]
- 00463138 bytes 56d31f94
+ 00463178 bytes 7ad31f94
- 00463148 ["COPY", "tmp:0:8", ["const:518:8"]]
- 00463148 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00463148 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00463148 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00463188 ["COPY", "tmp:0:8", ["const:5e8:8"]]
+ 00463188 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00463188 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00463188 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00463148 bytes 08611491
+ 00463188 bytes 08a11791
- 0046316c ["COPY", "register:0:8", ["register:4040:8"]]
- 0046316c ["INT_ADD", "register:40f0:8", ["const:46316c:8", "const:4:8"]]
- 0046316c ["CALLIND", null, ["register:0:8"]]
+ 004631ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 004631ac ["INT_ADD", "register:40f0:8", ["const:4631ac:8", "const:4:8"]]
+ 004631ac ["CALLIND", null, ["register:0:8"]]
- 0046316c bytes 00013fd6
+ 004631ac bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ae6ef42aa82d4dd961de3544ab6217f"></a>

### [`004631ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/004631ac.md) → [`004631ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00463/004631ec.md) FUN_004631ec

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00463208",
      "incomplete_value": false,
      "site": "00463208",
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
            "const:5e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004631c8",
      "incomplete_value": false,
      "site": "004631c8",
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
            "const:518:8"
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
      "00463208",
      "DATA",
      [
        "storage",
        "00c64518",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00463208",
      "DATA",
      [
        "storage",
        "00c645e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004631c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/004631ac.md#insn-004631c4) · [`004631e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/004631ac.md#insn-004631e8)
- 新版 `00463204`（命令位置の公開資料なし） · `00463228`（命令位置の公開資料なし）

~~~diff
- 004631c4 ["COPY", "tmp:0:8", ["const:518:8"]]
- 004631c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004631c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004631c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00463204 ["COPY", "tmp:0:8", ["const:5e8:8"]]
+ 00463204 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00463204 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00463204 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004631c4 bytes 29611491
+ 00463204 bytes 29a11791
- 004631e8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004631e8 ["INT_ADD", "register:40f0:8", ["const:4631e8:8", "const:4:8"]]
- 004631e8 ["CALLIND", null, ["register:0:8"]]
+ 00463228 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00463228 ["INT_ADD", "register:40f0:8", ["const:463228:8", "const:4:8"]]
+ 00463228 ["CALLIND", null, ["register:0:8"]]
- 004631e8 bytes 20013fd6
+ 00463228 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a1ff801ee598d0c4e1d5cce25bf4908"></a>

### [`004632a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/004632a8.md) → [`004632e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00463/004632e8.md) FUN_004632e8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.79% / 新版 97.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0046338c",
      "incomplete_value": true,
      "site": "0046338c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a0000:8"
              ],
              [
                "leaf",
                "const:f4e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046334c",
      "incomplete_value": true,
      "site": "0046334c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a0000:8"
              ],
              [
                "leaf",
                "const:f9b:8"
              ]
            ]
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
      "0046337c",
      "READ",
      [
        "storage",
        "002a0f9b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0046337c",
      "READ",
      [
        "storage",
        "002a0f4e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046338c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/004632a8.md#insn-0046338c) · [`004632fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/004632a8.md#insn-004632fc) · [`00463328`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/004632a8.md#insn-00463328)
- 新版 `004633cc`（命令位置の公開資料なし） · `0046333c`（命令位置の公開資料なし） · `00463368`（命令位置の公開資料なし）

~~~diff
- 0046338c ["INT_ADD", "register:40f0:8", ["const:46338c:8", "const:4:8"]]
- 0046338c ["CALL", null, ["callee:00c57f80:8"]]
+ 004633cc ["INT_ADD", "register:40f0:8", ["const:4633cc:8", "const:4:8"]]
+ 004633cc ["CALL", null, ["callee:00c57f80:8"]]
- 0046338c bytes c9d21f94
+ 004633cc bytes edd21f94
- 004632fc ["INT_ADD", "register:40f0:8", ["const:4632fc:8", "const:4:8"]]
- 004632fc ["CALL", null, ["callee:004410cc:8"]]
+ 0046333c ["INT_ADD", "register:40f0:8", ["const:46333c:8", "const:4:8"]]
+ 0046333c ["CALL", null, ["callee:004410cc:8"]]
- 004632fc bytes 6477ff97
+ 0046333c bytes 6477ff97
- 00463328 ["INT_ADD", "register:40f0:8", ["const:463328:8", "const:4:8"]]
- 00463328 ["CALL", null, ["callee:00c57f80:8"]]
+ 00463368 ["INT_ADD", "register:40f0:8", ["const:463368:8", "const:4:8"]]
+ 00463368 ["CALL", null, ["callee:00c57f80:8"]]
- 00463328 bytes e2d21f94
+ 00463368 bytes 06d31f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f76d490d4237d7ea0881ef46f65f03e7"></a>

### [`0046356c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/0046356c.md) → [`004635ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00463/004635ac.md) FUN_004635ac

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004635b8",
      "incomplete_value": false,
      "site": "004635c4",
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
            "const:668:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00463578",
      "incomplete_value": false,
      "site": "00463584",
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
            "const:598:8"
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
      "004635c4",
      "DATA",
      [
        "storage",
        "00c64598",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004635c4",
      "DATA",
      [
        "storage",
        "00c64668",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00463578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/0046356c.md#insn-00463578)
- 新版 `004635b8`（命令位置の公開資料なし）

~~~diff
- 00463578 ["COPY", "tmp:0:8", ["const:598:8"]]
- 00463578 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00463578 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00463578 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 004635b8 ["COPY", "tmp:0:8", ["const:668:8"]]
+ 004635b8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 004635b8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 004635b8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00463578 bytes 4a611691
+ 004635b8 bytes 4aa11991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3087ae608fe37d241da0dc6d2b5fdeb6"></a>

### [`004635b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/004635b0.md) → [`004635f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00463/004635f0.md) FUN_004635f0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00463608",
      "incomplete_value": false,
      "site": "00463614",
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
            "const:668:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004635c8",
      "incomplete_value": false,
      "site": "004635d4",
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
            "const:598:8"
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
      "00463614",
      "DATA",
      [
        "storage",
        "00c64598",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00463614",
      "DATA",
      [
        "storage",
        "00c64668",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004635c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/004635b0.md#insn-004635c8) · [`004635f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/004635b0.md#insn-004635f8)
- 新版 `00463608`（命令位置の公開資料なし） · `00463638`（命令位置の公開資料なし）

~~~diff
- 004635c8 ["COPY", "tmp:0:8", ["const:598:8"]]
- 004635c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004635c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004635c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00463608 ["COPY", "tmp:0:8", ["const:668:8"]]
+ 00463608 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00463608 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00463608 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004635c8 bytes 08611691
+ 00463608 bytes 08a11991
- 004635f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004635f8 ["INT_ADD", "register:40f0:8", ["const:4635f8:8", "const:4:8"]]
- 004635f8 ["CALLIND", null, ["register:0:8"]]
+ 00463638 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00463638 ["INT_ADD", "register:40f0:8", ["const:463638:8", "const:4:8"]]
+ 00463638 ["CALLIND", null, ["register:0:8"]]
- 004635f8 bytes 00013fd6
+ 00463638 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e946843f5ae593691d9663c560cb104"></a>

### [`0046360c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/0046360c.md) → [`0046364c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00463/0046364c.md) FUN_0046364c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00463678",
      "incomplete_value": false,
      "site": "00463678",
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
            "const:668:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00463638",
      "incomplete_value": false,
      "site": "00463638",
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
            "const:598:8"
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
      "00463678",
      "DATA",
      [
        "storage",
        "00c64598",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00463678",
      "DATA",
      [
        "storage",
        "00c64668",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00463620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/0046360c.md#insn-00463620) · [`00463630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/0046360c.md#insn-00463630) · [`00463654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/0046360c.md#insn-00463654)
- 新版 `00463660`（命令位置の公開資料なし） · `00463670`（命令位置の公開資料なし） · `00463694`（命令位置の公開資料なし）

~~~diff
- 00463620 ["INT_ADD", "register:40f0:8", ["const:463620:8", "const:4:8"]]
- 00463620 ["CALL", null, ["callee:00c57f60:8"]]
+ 00463660 ["INT_ADD", "register:40f0:8", ["const:463660:8", "const:4:8"]]
+ 00463660 ["CALL", null, ["callee:00c57f60:8"]]
- 00463620 bytes 1cd21f94
+ 00463660 bytes 40d21f94
- 00463630 ["COPY", "tmp:0:8", ["const:598:8"]]
- 00463630 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00463630 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00463630 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00463670 ["COPY", "tmp:0:8", ["const:668:8"]]
+ 00463670 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00463670 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00463670 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00463630 bytes 08611691
+ 00463670 bytes 08a11991
- 00463654 ["COPY", "register:0:8", ["register:4040:8"]]
- 00463654 ["INT_ADD", "register:40f0:8", ["const:463654:8", "const:4:8"]]
- 00463654 ["CALLIND", null, ["register:0:8"]]
+ 00463694 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00463694 ["INT_ADD", "register:40f0:8", ["const:463694:8", "const:4:8"]]
+ 00463694 ["CALLIND", null, ["register:0:8"]]
- 00463654 bytes 00013fd6
+ 00463694 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-219fb3931137a9e27b7298d5d1ebc0f1"></a>

### [`00463694`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463694.md) → [`004636d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00463/004636d4.md) FUN_004636d4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004636f0",
      "incomplete_value": false,
      "site": "004636f0",
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
            "const:668:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004636b0",
      "incomplete_value": false,
      "site": "004636b0",
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
            "const:598:8"
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
      "004636f0",
      "DATA",
      [
        "storage",
        "00c64598",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004636f0",
      "DATA",
      [
        "storage",
        "00c64668",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004636ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463694.md#insn-004636ac) · [`004636d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463694.md#insn-004636d0)
- 新版 `004636ec`（命令位置の公開資料なし） · `00463710`（命令位置の公開資料なし）

~~~diff
- 004636ac ["COPY", "tmp:0:8", ["const:598:8"]]
- 004636ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004636ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004636ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004636ec ["COPY", "tmp:0:8", ["const:668:8"]]
+ 004636ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004636ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004636ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004636ac bytes 29611691
+ 004636ec bytes 29a11991
- 004636d0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004636d0 ["INT_ADD", "register:40f0:8", ["const:4636d0:8", "const:4:8"]]
- 004636d0 ["CALLIND", null, ["register:0:8"]]
+ 00463710 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00463710 ["INT_ADD", "register:40f0:8", ["const:463710:8", "const:4:8"]]
+ 00463710 ["CALLIND", null, ["register:0:8"]]
- 004636d0 bytes 20013fd6
+ 00463710 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f421ee09efa253a1026a6dad44bef4ee"></a>

### [`00463884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463884.md) → [`004638c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00463/004638c4.md) FUN_004638c4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004638d0",
      "incomplete_value": false,
      "site": "004638dc",
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
            "const:6e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00463890",
      "incomplete_value": false,
      "site": "0046389c",
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
            "const:618:8"
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
      "004638dc",
      "DATA",
      [
        "storage",
        "00c64618",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004638dc",
      "DATA",
      [
        "storage",
        "00c646e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00463890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463884.md#insn-00463890)
- 新版 `004638d0`（命令位置の公開資料なし）

~~~diff
- 00463890 ["COPY", "tmp:0:8", ["const:618:8"]]
- 00463890 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00463890 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00463890 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 004638d0 ["COPY", "tmp:0:8", ["const:6e8:8"]]
+ 004638d0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 004638d0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 004638d0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00463890 bytes 4a611891
+ 004638d0 bytes 4aa11b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd96e9f280ace80df7f82ce9b162f7a4"></a>

### [`004638c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/004638c8.md) → [`00463908`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00463/00463908.md) FUN_00463908

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00463920",
      "incomplete_value": false,
      "site": "0046392c",
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
            "const:6e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004638e0",
      "incomplete_value": false,
      "site": "004638ec",
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
            "const:618:8"
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
      "0046392c",
      "DATA",
      [
        "storage",
        "00c64618",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0046392c",
      "DATA",
      [
        "storage",
        "00c646e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004638e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/004638c8.md#insn-004638e0) · [`00463910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/004638c8.md#insn-00463910)
- 新版 `00463920`（命令位置の公開資料なし） · `00463950`（命令位置の公開資料なし）

~~~diff
- 004638e0 ["COPY", "tmp:0:8", ["const:618:8"]]
- 004638e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004638e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004638e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00463920 ["COPY", "tmp:0:8", ["const:6e8:8"]]
+ 00463920 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00463920 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00463920 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004638e0 bytes 08611891
+ 00463920 bytes 08a11b91
- 00463910 ["COPY", "register:0:8", ["register:4040:8"]]
- 00463910 ["INT_ADD", "register:40f0:8", ["const:463910:8", "const:4:8"]]
- 00463910 ["CALLIND", null, ["register:0:8"]]
+ 00463950 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00463950 ["INT_ADD", "register:40f0:8", ["const:463950:8", "const:4:8"]]
+ 00463950 ["CALLIND", null, ["register:0:8"]]
- 00463910 bytes 00013fd6
+ 00463950 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c902b038305181cf3028bed49e06925b"></a>

### [`00463924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463924.md) → [`00463964`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00463/00463964.md) FUN_00463964

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00463990",
      "incomplete_value": false,
      "site": "00463990",
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
            "const:6e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00463950",
      "incomplete_value": false,
      "site": "00463950",
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
            "const:618:8"
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
      "00463990",
      "DATA",
      [
        "storage",
        "00c64618",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00463990",
      "DATA",
      [
        "storage",
        "00c646e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00463938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463924.md#insn-00463938) · [`00463948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463924.md#insn-00463948) · [`0046396c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463924.md#insn-0046396c)
- 新版 `00463978`（命令位置の公開資料なし） · `00463988`（命令位置の公開資料なし） · `004639ac`（命令位置の公開資料なし）

~~~diff
- 00463938 ["INT_ADD", "register:40f0:8", ["const:463938:8", "const:4:8"]]
- 00463938 ["CALL", null, ["callee:00c57f60:8"]]
+ 00463978 ["INT_ADD", "register:40f0:8", ["const:463978:8", "const:4:8"]]
+ 00463978 ["CALL", null, ["callee:00c57f60:8"]]
- 00463938 bytes 56d11f94
+ 00463978 bytes 7ad11f94
- 00463948 ["COPY", "tmp:0:8", ["const:618:8"]]
- 00463948 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00463948 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00463948 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00463988 ["COPY", "tmp:0:8", ["const:6e8:8"]]
+ 00463988 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00463988 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00463988 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00463948 bytes 08611891
+ 00463988 bytes 08a11b91
- 0046396c ["COPY", "register:0:8", ["register:4040:8"]]
- 0046396c ["INT_ADD", "register:40f0:8", ["const:46396c:8", "const:4:8"]]
- 0046396c ["CALLIND", null, ["register:0:8"]]
+ 004639ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 004639ac ["INT_ADD", "register:40f0:8", ["const:4639ac:8", "const:4:8"]]
+ 004639ac ["CALLIND", null, ["register:0:8"]]
- 0046396c bytes 00013fd6
+ 004639ac bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-983335c74099949686524c2e64ace1a5"></a>

### [`004639ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/004639ac.md) → [`004639ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00463/004639ec.md) FUN_004639ec

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00463a08",
      "incomplete_value": false,
      "site": "00463a08",
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
            "const:6e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004639c8",
      "incomplete_value": false,
      "site": "004639c8",
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
            "const:618:8"
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
      "00463a08",
      "DATA",
      [
        "storage",
        "00c64618",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00463a08",
      "DATA",
      [
        "storage",
        "00c646e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004639c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/004639ac.md#insn-004639c4) · [`004639e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/004639ac.md#insn-004639e8)
- 新版 `00463a04`（命令位置の公開資料なし） · `00463a28`（命令位置の公開資料なし）

~~~diff
- 004639c4 ["COPY", "tmp:0:8", ["const:618:8"]]
- 004639c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004639c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004639c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00463a04 ["COPY", "tmp:0:8", ["const:6e8:8"]]
+ 00463a04 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00463a04 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00463a04 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004639c4 bytes 29611891
+ 00463a04 bytes 29a11b91
- 004639e8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004639e8 ["INT_ADD", "register:40f0:8", ["const:4639e8:8", "const:4:8"]]
- 004639e8 ["CALLIND", null, ["register:0:8"]]
+ 00463a28 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00463a28 ["INT_ADD", "register:40f0:8", ["const:463a28:8", "const:4:8"]]
+ 00463a28 ["CALLIND", null, ["register:0:8"]]
- 004639e8 bytes 20013fd6
+ 00463a28 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47122f521bd97b39264f36de476973db"></a>

### [`00463b44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463b44.md) → [`00463b84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00463/00463b84.md) FUN_00463b84

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00463b90",
      "incomplete_value": false,
      "site": "00463b9c",
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
            "const:768:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00463b50",
      "incomplete_value": false,
      "site": "00463b5c",
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
            "const:698:8"
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
      "00463b9c",
      "DATA",
      [
        "storage",
        "00c64698",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00463b9c",
      "DATA",
      [
        "storage",
        "00c64768",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00463b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463b44.md#insn-00463b50)
- 新版 `00463b90`（命令位置の公開資料なし）

~~~diff
- 00463b50 ["COPY", "tmp:0:8", ["const:698:8"]]
- 00463b50 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00463b50 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00463b50 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00463b90 ["COPY", "tmp:0:8", ["const:768:8"]]
+ 00463b90 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00463b90 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00463b90 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00463b50 bytes 4a611a91
+ 00463b90 bytes 4aa11d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b19674e821d323012c404e1a6975690"></a>

### [`00463b88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463b88.md) → [`00463bc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00463/00463bc8.md) FUN_00463bc8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00463be0",
      "incomplete_value": false,
      "site": "00463bec",
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
            "const:768:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00463ba0",
      "incomplete_value": false,
      "site": "00463bac",
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
            "const:698:8"
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
      "00463bec",
      "DATA",
      [
        "storage",
        "00c64698",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00463bec",
      "DATA",
      [
        "storage",
        "00c64768",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00463ba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463b88.md#insn-00463ba0) · [`00463bd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463b88.md#insn-00463bd0)
- 新版 `00463be0`（命令位置の公開資料なし） · `00463c10`（命令位置の公開資料なし）

~~~diff
- 00463ba0 ["COPY", "tmp:0:8", ["const:698:8"]]
- 00463ba0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00463ba0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00463ba0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00463be0 ["COPY", "tmp:0:8", ["const:768:8"]]
+ 00463be0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00463be0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00463be0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00463ba0 bytes 08611a91
+ 00463be0 bytes 08a11d91
- 00463bd0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00463bd0 ["INT_ADD", "register:40f0:8", ["const:463bd0:8", "const:4:8"]]
- 00463bd0 ["CALLIND", null, ["register:0:8"]]
+ 00463c10 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00463c10 ["INT_ADD", "register:40f0:8", ["const:463c10:8", "const:4:8"]]
+ 00463c10 ["CALLIND", null, ["register:0:8"]]
- 00463bd0 bytes 00013fd6
+ 00463c10 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03c2953d697f94bea928cde82574ec90"></a>

### [`00463be4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463be4.md) → [`00463c24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00463/00463c24.md) FUN_00463c24

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00463c50",
      "incomplete_value": false,
      "site": "00463c50",
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
            "const:768:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00463c10",
      "incomplete_value": false,
      "site": "00463c10",
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
            "const:698:8"
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
      "00463c50",
      "DATA",
      [
        "storage",
        "00c64698",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00463c50",
      "DATA",
      [
        "storage",
        "00c64768",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00463bf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463be4.md#insn-00463bf8) · [`00463c08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463be4.md#insn-00463c08) · [`00463c2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463be4.md#insn-00463c2c)
- 新版 `00463c38`（命令位置の公開資料なし） · `00463c48`（命令位置の公開資料なし） · `00463c6c`（命令位置の公開資料なし）

~~~diff
- 00463bf8 ["INT_ADD", "register:40f0:8", ["const:463bf8:8", "const:4:8"]]
- 00463bf8 ["CALL", null, ["callee:00c57f60:8"]]
+ 00463c38 ["INT_ADD", "register:40f0:8", ["const:463c38:8", "const:4:8"]]
+ 00463c38 ["CALL", null, ["callee:00c57f60:8"]]
- 00463bf8 bytes a6d01f94
+ 00463c38 bytes cad01f94
- 00463c08 ["COPY", "tmp:0:8", ["const:698:8"]]
- 00463c08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00463c08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00463c08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00463c48 ["COPY", "tmp:0:8", ["const:768:8"]]
+ 00463c48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00463c48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00463c48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00463c08 bytes 08611a91
+ 00463c48 bytes 08a11d91
- 00463c2c ["COPY", "register:0:8", ["register:4040:8"]]
- 00463c2c ["INT_ADD", "register:40f0:8", ["const:463c2c:8", "const:4:8"]]
- 00463c2c ["CALLIND", null, ["register:0:8"]]
+ 00463c6c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00463c6c ["INT_ADD", "register:40f0:8", ["const:463c6c:8", "const:4:8"]]
+ 00463c6c ["CALLIND", null, ["register:0:8"]]
- 00463c2c bytes 00013fd6
+ 00463c6c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bcd8f26c24e6d6dbd03ba9cbb26e55b1"></a>

### [`00463c6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463c6c.md) → [`00463cac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00463/00463cac.md) FUN_00463cac

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00463cc8",
      "incomplete_value": false,
      "site": "00463cc8",
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
            "const:768:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00463c88",
      "incomplete_value": false,
      "site": "00463c88",
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
            "const:698:8"
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
      "00463cc8",
      "DATA",
      [
        "storage",
        "00c64698",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00463cc8",
      "DATA",
      [
        "storage",
        "00c64768",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00463c84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463c6c.md#insn-00463c84) · [`00463ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463c6c.md#insn-00463ca8)
- 新版 `00463cc4`（命令位置の公開資料なし） · `00463ce8`（命令位置の公開資料なし）

~~~diff
- 00463c84 ["COPY", "tmp:0:8", ["const:698:8"]]
- 00463c84 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00463c84 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00463c84 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00463cc4 ["COPY", "tmp:0:8", ["const:768:8"]]
+ 00463cc4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00463cc4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00463cc4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00463c84 bytes 29611a91
+ 00463cc4 bytes 29a11d91
- 00463ca8 ["COPY", "register:0:8", ["register:4048:8"]]
- 00463ca8 ["INT_ADD", "register:40f0:8", ["const:463ca8:8", "const:4:8"]]
- 00463ca8 ["CALLIND", null, ["register:0:8"]]
+ 00463ce8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00463ce8 ["INT_ADD", "register:40f0:8", ["const:463ce8:8", "const:4:8"]]
+ 00463ce8 ["CALLIND", null, ["register:0:8"]]
- 00463ca8 bytes 20013fd6
+ 00463ce8 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b345d8c877a80ff181dcf99e7f8a24e"></a>

### [`00463e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463e04.md) → [`00463e44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00463/00463e44.md) FUN_00463e44

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00463e50",
      "incomplete_value": false,
      "site": "00463e5c",
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
            "const:7e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00463e10",
      "incomplete_value": false,
      "site": "00463e1c",
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
            "const:718:8"
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
      "00463e5c",
      "DATA",
      [
        "storage",
        "00c64718",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00463e5c",
      "DATA",
      [
        "storage",
        "00c647e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00463e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463e04.md#insn-00463e10)
- 新版 `00463e50`（命令位置の公開資料なし）

~~~diff
- 00463e10 ["COPY", "tmp:0:8", ["const:718:8"]]
- 00463e10 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00463e10 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00463e10 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00463e50 ["COPY", "tmp:0:8", ["const:7e8:8"]]
+ 00463e50 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00463e50 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00463e50 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00463e10 bytes 4a611c91
+ 00463e50 bytes 4aa11f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4670cf3d87849e65184ac9864179ee4"></a>

### [`00463e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463e48.md) → [`00463e88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00463/00463e88.md) FUN_00463e88

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00463ea0",
      "incomplete_value": false,
      "site": "00463eac",
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
            "const:7e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00463e60",
      "incomplete_value": false,
      "site": "00463e6c",
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
            "const:718:8"
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
      "00463eac",
      "DATA",
      [
        "storage",
        "00c64718",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00463eac",
      "DATA",
      [
        "storage",
        "00c647e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00463e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463e48.md#insn-00463e60) · [`00463e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463e48.md#insn-00463e90)
- 新版 `00463ea0`（命令位置の公開資料なし） · `00463ed0`（命令位置の公開資料なし）

~~~diff
- 00463e60 ["COPY", "tmp:0:8", ["const:718:8"]]
- 00463e60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00463e60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00463e60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00463ea0 ["COPY", "tmp:0:8", ["const:7e8:8"]]
+ 00463ea0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00463ea0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00463ea0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00463e60 bytes 08611c91
+ 00463ea0 bytes 08a11f91
- 00463e90 ["COPY", "register:0:8", ["register:4040:8"]]
- 00463e90 ["INT_ADD", "register:40f0:8", ["const:463e90:8", "const:4:8"]]
- 00463e90 ["CALLIND", null, ["register:0:8"]]
+ 00463ed0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00463ed0 ["INT_ADD", "register:40f0:8", ["const:463ed0:8", "const:4:8"]]
+ 00463ed0 ["CALLIND", null, ["register:0:8"]]
- 00463e90 bytes 00013fd6
+ 00463ed0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d275bddf13295515b23d9cec4239f79b"></a>

### [`00463ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463ea4.md) → [`00463ee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00463/00463ee4.md) FUN_00463ee4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00463f10",
      "incomplete_value": false,
      "site": "00463f10",
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
            "const:7e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00463ed0",
      "incomplete_value": false,
      "site": "00463ed0",
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
            "const:718:8"
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
      "00463f10",
      "DATA",
      [
        "storage",
        "00c64718",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00463f10",
      "DATA",
      [
        "storage",
        "00c647e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00463eb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463ea4.md#insn-00463eb8) · [`00463ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463ea4.md#insn-00463ec8) · [`00463eec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463ea4.md#insn-00463eec)
- 新版 `00463ef8`（命令位置の公開資料なし） · `00463f08`（命令位置の公開資料なし） · `00463f2c`（命令位置の公開資料なし）

~~~diff
- 00463eb8 ["INT_ADD", "register:40f0:8", ["const:463eb8:8", "const:4:8"]]
- 00463eb8 ["CALL", null, ["callee:00c57f60:8"]]
+ 00463ef8 ["INT_ADD", "register:40f0:8", ["const:463ef8:8", "const:4:8"]]
+ 00463ef8 ["CALL", null, ["callee:00c57f60:8"]]
- 00463eb8 bytes f6cf1f94
+ 00463ef8 bytes 1ad01f94
- 00463ec8 ["COPY", "tmp:0:8", ["const:718:8"]]
- 00463ec8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00463ec8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00463ec8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00463f08 ["COPY", "tmp:0:8", ["const:7e8:8"]]
+ 00463f08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00463f08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00463f08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00463ec8 bytes 08611c91
+ 00463f08 bytes 08a11f91
- 00463eec ["COPY", "register:0:8", ["register:4040:8"]]
- 00463eec ["INT_ADD", "register:40f0:8", ["const:463eec:8", "const:4:8"]]
- 00463eec ["CALLIND", null, ["register:0:8"]]
+ 00463f2c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00463f2c ["INT_ADD", "register:40f0:8", ["const:463f2c:8", "const:4:8"]]
+ 00463f2c ["CALLIND", null, ["register:0:8"]]
- 00463eec bytes 00013fd6
+ 00463f2c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e40727c837ee36d85dae50b058b370e6"></a>

### [`00463f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463f2c.md) → [`00463f6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00463/00463f6c.md) FUN_00463f6c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00463f88",
      "incomplete_value": false,
      "site": "00463f88",
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
            "const:7e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00463f48",
      "incomplete_value": false,
      "site": "00463f48",
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
            "const:718:8"
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
      "00463f88",
      "DATA",
      [
        "storage",
        "00c64718",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00463f88",
      "DATA",
      [
        "storage",
        "00c647e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00463f44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463f2c.md#insn-00463f44) · [`00463f68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463f2c.md#insn-00463f68)
- 新版 `00463f84`（命令位置の公開資料なし） · `00463fa8`（命令位置の公開資料なし）

~~~diff
- 00463f44 ["COPY", "tmp:0:8", ["const:718:8"]]
- 00463f44 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00463f44 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00463f44 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00463f84 ["COPY", "tmp:0:8", ["const:7e8:8"]]
+ 00463f84 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00463f84 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00463f84 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00463f44 bytes 29611c91
+ 00463f84 bytes 29a11f91
- 00463f68 ["COPY", "register:0:8", ["register:4048:8"]]
- 00463f68 ["INT_ADD", "register:40f0:8", ["const:463f68:8", "const:4:8"]]
- 00463f68 ["CALLIND", null, ["register:0:8"]]
+ 00463fa8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00463fa8 ["INT_ADD", "register:40f0:8", ["const:463fa8:8", "const:4:8"]]
+ 00463fa8 ["CALLIND", null, ["register:0:8"]]
- 00463f68 bytes 20013fd6
+ 00463fa8 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da1bc5fc36c2932c49be334e9010718e"></a>

### [`00464028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464028.md) → [`00464068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00464/00464068.md) FUN_00464068

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00461a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461a80.md) [`0046479c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/0046479c.md) [`00464878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464878.md)
- 新版 呼出元 0件  · 呼出先 7件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00461ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/00461ac0.md) [`004647dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00464/004647dc.md) [`004648b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00464/004648b8.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.54% / 新版 95.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00464340",
      "incomplete_value": true,
      "site": "00464340",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a8000:8"
              ],
              [
                "leaf",
                "const:a58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00464300",
      "incomplete_value": true,
      "site": "00464300",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a8000:8"
              ],
              [
                "leaf",
                "const:ab4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 60,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00464334",
      "incomplete_value": true,
      "site": "00464344",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004642f4",
      "incomplete_value": true,
      "site": "00464304",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 61,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004643cc",
      "incomplete_value": true,
      "site": "004643d8",
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
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:603:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046438c",
      "incomplete_value": true,
      "site": "00464398",
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
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:65f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 70,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004641a8",
      "DATA",
      [
        "storage",
        "0079656b",
        null,
        null
      ]
    ],
    [
      "00464330",
      "READ",
      [
        "storage",
        "002a8ab4",
        null,
        "string"
      ]
    ],
    [
      "00464334",
      "READ",
      [
        "storage",
        "002a8abb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00464330",
      "READ",
      [
        "storage",
        "002a8a58",
        null,
        "string"
      ]
    ],
    [
      "00464334",
      "READ",
      [
        "storage",
        "002a8a5f",
        null,
        "string"
      ]
    ],
    [
      "004643cc",
      "READ",
      [
        "storage",
        "002a7603",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00464358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464028.md#insn-00464358) · [`00464090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464028.md#insn-00464090) · [`004640bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464028.md#insn-004640bc)
- 新版 `00464398`（命令位置の公開資料なし） · `004640d0`（命令位置の公開資料なし） · `004640fc`（命令位置の公開資料なし）

~~~diff
- 00464358 ["INT_ADD", "register:40f0:8", ["const:464358:8", "const:4:8"]]
- 00464358 ["CALL", null, ["callee:00c57f80:8"]]
+ 00464398 ["INT_ADD", "register:40f0:8", ["const:464398:8", "const:4:8"]]
+ 00464398 ["CALL", null, ["callee:00c57f80:8"]]
- 00464358 bytes d6ce1f94
+ 00464398 bytes face1f94
- 00464090 ["INT_ADD", "register:40f0:8", ["const:464090:8", "const:4:8"]]
- 00464090 ["CALL", null, ["callee:004410cc:8"]]
+ 004640d0 ["INT_ADD", "register:40f0:8", ["const:4640d0:8", "const:4:8"]]
+ 004640d0 ["CALL", null, ["callee:004410cc:8"]]
- 00464090 bytes ff73ff97
+ 004640d0 bytes ff73ff97
- 004640bc ["INT_ADD", "register:40f0:8", ["const:4640bc:8", "const:4:8"]]
- 004640bc ["CALL", null, ["callee:00c57f80:8"]]
+ 004640fc ["INT_ADD", "register:40f0:8", ["const:4640fc:8", "const:4:8"]]
+ 004640fc ["CALL", null, ["callee:00c57f80:8"]]
- 004640bc bytes 7dcf1f94
+ 004640fc bytes a1cf1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27a2a99d6d4d7fa28006ab0e7354c481"></a>

### [`00464b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464b08.md) → [`00464b48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00464/00464b48.md) FUN_00464b48

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00464b54",
      "incomplete_value": false,
      "site": "00464b60",
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
            "const:868:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00464b14",
      "incomplete_value": false,
      "site": "00464b20",
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
            "const:798:8"
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
      "00464b60",
      "DATA",
      [
        "storage",
        "00c64798",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00464b60",
      "DATA",
      [
        "storage",
        "00c64868",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00464b14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464b08.md#insn-00464b14)
- 新版 `00464b54`（命令位置の公開資料なし）

~~~diff
- 00464b14 ["COPY", "tmp:0:8", ["const:798:8"]]
- 00464b14 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00464b14 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00464b14 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00464b54 ["COPY", "tmp:0:8", ["const:868:8"]]
+ 00464b54 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00464b54 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00464b54 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00464b14 bytes 4a611e91
+ 00464b54 bytes 4aa12191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b95516d8b9495e356917e30219990cbd"></a>

### [`00464b4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464b4c.md) → [`00464b8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00464/00464b8c.md) FUN_00464b8c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00464ba4",
      "incomplete_value": false,
      "site": "00464bb0",
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
            "const:868:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00464b64",
      "incomplete_value": false,
      "site": "00464b70",
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
            "const:798:8"
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
      "00464bb0",
      "DATA",
      [
        "storage",
        "00c64798",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00464bb0",
      "DATA",
      [
        "storage",
        "00c64868",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00464b64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464b4c.md#insn-00464b64) · [`00464b94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464b4c.md#insn-00464b94)
- 新版 `00464ba4`（命令位置の公開資料なし） · `00464bd4`（命令位置の公開資料なし）

~~~diff
- 00464b64 ["COPY", "tmp:0:8", ["const:798:8"]]
- 00464b64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00464b64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00464b64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00464ba4 ["COPY", "tmp:0:8", ["const:868:8"]]
+ 00464ba4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00464ba4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00464ba4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00464b64 bytes 08611e91
+ 00464ba4 bytes 08a12191
- 00464b94 ["COPY", "register:0:8", ["register:4040:8"]]
- 00464b94 ["INT_ADD", "register:40f0:8", ["const:464b94:8", "const:4:8"]]
- 00464b94 ["CALLIND", null, ["register:0:8"]]
+ 00464bd4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00464bd4 ["INT_ADD", "register:40f0:8", ["const:464bd4:8", "const:4:8"]]
+ 00464bd4 ["CALLIND", null, ["register:0:8"]]
- 00464b94 bytes 00013fd6
+ 00464bd4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11fac43384ff7f53f70e24e8044d45a5"></a>

### [`00464ba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464ba8.md) → [`00464be8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00464/00464be8.md) FUN_00464be8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00464c14",
      "incomplete_value": false,
      "site": "00464c14",
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
            "const:868:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00464bd4",
      "incomplete_value": false,
      "site": "00464bd4",
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
            "const:798:8"
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
      "00464c14",
      "DATA",
      [
        "storage",
        "00c64798",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00464c14",
      "DATA",
      [
        "storage",
        "00c64868",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00464bbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464ba8.md#insn-00464bbc) · [`00464bcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464ba8.md#insn-00464bcc) · [`00464bf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464ba8.md#insn-00464bf0)
- 新版 `00464bfc`（命令位置の公開資料なし） · `00464c0c`（命令位置の公開資料なし） · `00464c30`（命令位置の公開資料なし）

~~~diff
- 00464bbc ["INT_ADD", "register:40f0:8", ["const:464bbc:8", "const:4:8"]]
- 00464bbc ["CALL", null, ["callee:00c57f60:8"]]
+ 00464bfc ["INT_ADD", "register:40f0:8", ["const:464bfc:8", "const:4:8"]]
+ 00464bfc ["CALL", null, ["callee:00c57f60:8"]]
- 00464bbc bytes b5cc1f94
+ 00464bfc bytes d9cc1f94
- 00464bcc ["COPY", "tmp:0:8", ["const:798:8"]]
- 00464bcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00464bcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00464bcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00464c0c ["COPY", "tmp:0:8", ["const:868:8"]]
+ 00464c0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00464c0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00464c0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00464bcc bytes 08611e91
+ 00464c0c bytes 08a12191
- 00464bf0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00464bf0 ["INT_ADD", "register:40f0:8", ["const:464bf0:8", "const:4:8"]]
- 00464bf0 ["CALLIND", null, ["register:0:8"]]
+ 00464c30 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00464c30 ["INT_ADD", "register:40f0:8", ["const:464c30:8", "const:4:8"]]
+ 00464c30 ["CALLIND", null, ["register:0:8"]]
- 00464bf0 bytes 00013fd6
+ 00464c30 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7437d80f3830d393f2dfcdc3bfb98795"></a>

### [`00464c30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464c30.md) → [`00464c70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00464/00464c70.md) FUN_00464c70

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00464c8c",
      "incomplete_value": false,
      "site": "00464c8c",
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
            "const:868:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00464c4c",
      "incomplete_value": false,
      "site": "00464c4c",
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
            "const:798:8"
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
      "00464c8c",
      "DATA",
      [
        "storage",
        "00c64798",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00464c8c",
      "DATA",
      [
        "storage",
        "00c64868",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00464c48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464c30.md#insn-00464c48) · [`00464c6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464c30.md#insn-00464c6c)
- 新版 `00464c88`（命令位置の公開資料なし） · `00464cac`（命令位置の公開資料なし）

~~~diff
- 00464c48 ["COPY", "tmp:0:8", ["const:798:8"]]
- 00464c48 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00464c48 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00464c48 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00464c88 ["COPY", "tmp:0:8", ["const:868:8"]]
+ 00464c88 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00464c88 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00464c88 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00464c48 bytes 29611e91
+ 00464c88 bytes 29a12191
- 00464c6c ["COPY", "register:0:8", ["register:4048:8"]]
- 00464c6c ["INT_ADD", "register:40f0:8", ["const:464c6c:8", "const:4:8"]]
- 00464c6c ["CALLIND", null, ["register:0:8"]]
+ 00464cac ["COPY", "register:0:8", ["register:4048:8"]]
+ 00464cac ["INT_ADD", "register:40f0:8", ["const:464cac:8", "const:4:8"]]
+ 00464cac ["CALLIND", null, ["register:0:8"]]
- 00464c6c bytes 20013fd6
+ 00464cac bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b61f4d07befddb17989406787aa07ae2"></a>

### [`00464e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464e10.md) → [`00464e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00464/00464e50.md) FUN_00464e50

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00464e5c",
      "incomplete_value": false,
      "site": "00464e68",
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
            "const:8e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00464e1c",
      "incomplete_value": false,
      "site": "00464e28",
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
            "const:818:8"
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
      "00464e68",
      "DATA",
      [
        "storage",
        "00c64818",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00464e68",
      "DATA",
      [
        "storage",
        "00c648e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00464e1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464e10.md#insn-00464e1c)
- 新版 `00464e5c`（命令位置の公開資料なし）

~~~diff
- 00464e1c ["COPY", "tmp:0:8", ["const:818:8"]]
- 00464e1c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00464e1c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00464e1c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00464e5c ["COPY", "tmp:0:8", ["const:8e8:8"]]
+ 00464e5c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00464e5c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00464e5c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00464e1c bytes 4a612091
+ 00464e5c bytes 4aa12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a228c9af0051bd579f630f53c7309f2c"></a>

### [`00464e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464e54.md) → [`00464e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00464/00464e94.md) FUN_00464e94

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00464eac",
      "incomplete_value": false,
      "site": "00464eb8",
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
            "const:8e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00464e6c",
      "incomplete_value": false,
      "site": "00464e78",
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
            "const:818:8"
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
      "00464eb8",
      "DATA",
      [
        "storage",
        "00c64818",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00464eb8",
      "DATA",
      [
        "storage",
        "00c648e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00464e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464e54.md#insn-00464e6c) · [`00464e9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464e54.md#insn-00464e9c)
- 新版 `00464eac`（命令位置の公開資料なし） · `00464edc`（命令位置の公開資料なし）

~~~diff
- 00464e6c ["COPY", "tmp:0:8", ["const:818:8"]]
- 00464e6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00464e6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00464e6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00464eac ["COPY", "tmp:0:8", ["const:8e8:8"]]
+ 00464eac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00464eac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00464eac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00464e6c bytes 08612091
+ 00464eac bytes 08a12391
- 00464e9c ["COPY", "register:0:8", ["register:4040:8"]]
- 00464e9c ["INT_ADD", "register:40f0:8", ["const:464e9c:8", "const:4:8"]]
- 00464e9c ["CALLIND", null, ["register:0:8"]]
+ 00464edc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00464edc ["INT_ADD", "register:40f0:8", ["const:464edc:8", "const:4:8"]]
+ 00464edc ["CALLIND", null, ["register:0:8"]]
- 00464e9c bytes 00013fd6
+ 00464edc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-356d3e4db8a9c7e945b18fc412f71e4f"></a>

### [`00464eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464eb0.md) → [`00464ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00464/00464ef0.md) FUN_00464ef0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00464f1c",
      "incomplete_value": false,
      "site": "00464f1c",
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
            "const:8e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00464edc",
      "incomplete_value": false,
      "site": "00464edc",
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
            "const:818:8"
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
      "00464f1c",
      "DATA",
      [
        "storage",
        "00c64818",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00464f1c",
      "DATA",
      [
        "storage",
        "00c648e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00464ec4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464eb0.md#insn-00464ec4) · [`00464ed4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464eb0.md#insn-00464ed4) · [`00464ef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464eb0.md#insn-00464ef8)
- 新版 `00464f04`（命令位置の公開資料なし） · `00464f14`（命令位置の公開資料なし） · `00464f38`（命令位置の公開資料なし）

~~~diff
- 00464ec4 ["INT_ADD", "register:40f0:8", ["const:464ec4:8", "const:4:8"]]
- 00464ec4 ["CALL", null, ["callee:00c57f60:8"]]
+ 00464f04 ["INT_ADD", "register:40f0:8", ["const:464f04:8", "const:4:8"]]
+ 00464f04 ["CALL", null, ["callee:00c57f60:8"]]
- 00464ec4 bytes f3cb1f94
+ 00464f04 bytes 17cc1f94
- 00464ed4 ["COPY", "tmp:0:8", ["const:818:8"]]
- 00464ed4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00464ed4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00464ed4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00464f14 ["COPY", "tmp:0:8", ["const:8e8:8"]]
+ 00464f14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00464f14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00464f14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00464ed4 bytes 08612091
+ 00464f14 bytes 08a12391
- 00464ef8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00464ef8 ["INT_ADD", "register:40f0:8", ["const:464ef8:8", "const:4:8"]]
- 00464ef8 ["CALLIND", null, ["register:0:8"]]
+ 00464f38 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00464f38 ["INT_ADD", "register:40f0:8", ["const:464f38:8", "const:4:8"]]
+ 00464f38 ["CALLIND", null, ["register:0:8"]]
- 00464ef8 bytes 00013fd6
+ 00464f38 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3723b97c3aa2a6ca104c6c8fd92d70a4"></a>

### [`00464f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464f38.md) → [`00464f78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00464/00464f78.md) FUN_00464f78

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00464f94",
      "incomplete_value": false,
      "site": "00464f94",
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
            "const:8e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00464f54",
      "incomplete_value": false,
      "site": "00464f54",
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
            "const:818:8"
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
      "00464f94",
      "DATA",
      [
        "storage",
        "00c64818",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00464f94",
      "DATA",
      [
        "storage",
        "00c648e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00464f50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464f38.md#insn-00464f50) · [`00464f74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00464/00464f38.md#insn-00464f74)
- 新版 `00464f90`（命令位置の公開資料なし） · `00464fb4`（命令位置の公開資料なし）

~~~diff
- 00464f50 ["COPY", "tmp:0:8", ["const:818:8"]]
- 00464f50 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00464f50 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00464f50 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00464f90 ["COPY", "tmp:0:8", ["const:8e8:8"]]
+ 00464f90 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00464f90 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00464f90 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00464f50 bytes 29612091
+ 00464f90 bytes 29a12391
- 00464f74 ["COPY", "register:0:8", ["register:4048:8"]]
- 00464f74 ["INT_ADD", "register:40f0:8", ["const:464f74:8", "const:4:8"]]
- 00464f74 ["CALLIND", null, ["register:0:8"]]
+ 00464fb4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00464fb4 ["INT_ADD", "register:40f0:8", ["const:464fb4:8", "const:4:8"]]
+ 00464fb4 ["CALLIND", null, ["register:0:8"]]
- 00464f74 bytes 20013fd6
+ 00464fb4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84517811ff645c6c7c06773f94b566df"></a>

### [`00465110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465110.md) → [`00465150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00465/00465150.md) FUN_00465150

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
      "definition_site": "00465164",
      "incomplete_value": false,
      "site": "00465168",
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
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00465124",
      "incomplete_value": false,
      "site": "00465128",
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
            "const:898:8"
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
      "00465168",
      "DATA",
      [
        "storage",
        "00c64898",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00465168",
      "DATA",
      [
        "storage",
        "00c64968",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046511c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465110.md#insn-0046511c) · [`00465124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465110.md#insn-00465124)
- 新版 `0046515c`（命令位置の公開資料なし） · `00465164`（命令位置の公開資料なし）

~~~diff
- 0046511c ["INT_ADD", "register:40f0:8", ["const:46511c:8", "const:4:8"]]
- 0046511c ["CALL", null, ["callee:00c57f60:8"]]
+ 0046515c ["INT_ADD", "register:40f0:8", ["const:46515c:8", "const:4:8"]]
+ 0046515c ["CALL", null, ["callee:00c57f60:8"]]
- 0046511c bytes 5dcb1f94
+ 0046515c bytes 81cb1f94
- 00465124 ["COPY", "tmp:0:8", ["const:898:8"]]
- 00465124 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00465124 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00465124 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00465164 ["COPY", "tmp:0:8", ["const:968:8"]]
+ 00465164 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00465164 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00465164 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00465124 bytes 08612291
+ 00465164 bytes 08a12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e96794b653fa17681c406f99428831d5"></a>

### [`00465134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465134.md) → [`00465174`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00465/00465174.md) FUN_00465174

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
      "definition_site": "00465178",
      "incomplete_value": false,
      "site": "0046517c",
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
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00465138",
      "incomplete_value": false,
      "site": "0046513c",
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
            "const:898:8"
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
      "0046517c",
      "DATA",
      [
        "storage",
        "00c64898",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0046517c",
      "DATA",
      [
        "storage",
        "00c64968",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00465138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465134.md#insn-00465138)
- 新版 `00465178`（命令位置の公開資料なし）

~~~diff
- 00465138 ["COPY", "tmp:0:8", ["const:898:8"]]
- 00465138 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00465138 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00465138 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00465178 ["COPY", "tmp:0:8", ["const:968:8"]]
+ 00465178 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00465178 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00465178 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00465138 bytes 08612291
+ 00465178 bytes 08a12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb859a3df9a0b51db1dc294bbfe6cad2"></a>

### [`0046514c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/0046514c.md) → [`0046518c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00465/0046518c.md) FUN_0046518c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004651c0",
      "incomplete_value": false,
      "site": "004651c4",
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
            "const:ba0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00465180",
      "incomplete_value": false,
      "site": "00465184",
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
            "const:aa0:8"
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
      "definition_site": "004651d0",
      "incomplete_value": false,
      "site": "004651d4",
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
            "const:ba0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00465190",
      "incomplete_value": false,
      "site": "00465194",
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
            "const:aa0:8"
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
      "0046519c",
      "READ",
      [
        "storage",
        "00ca4aa0",
        null,
        "undefined1"
      ]
    ],
    [
      "004651a8",
      "READ",
      [
        "storage",
        "00ca4a98",
        null,
        "undefined8"
      ]
    ],
    [
      "004651c0",
      "PARAM",
      [
        "storage",
        "00ca4aa0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0046519c",
      "READ",
      [
        "storage",
        "00ca4ba0",
        null,
        "undefined1"
      ]
    ],
    [
      "004651a8",
      "READ",
      [
        "storage",
        "00ca4b98",
        null,
        "undefined8"
      ]
    ],
    [
      "004651c0",
      "PARAM",
      [
        "storage",
        "00ca4ba0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00465184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/0046514c.md#insn-00465184) · [`00465194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/0046514c.md#insn-00465194) · [`00465158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/0046514c.md#insn-00465158)
- 新版 `004651c4`（命令位置の公開資料なし） · `004651d4`（命令位置の公開資料なし） · `00465198`（命令位置の公開資料なし）

~~~diff
- 00465184 ["INT_ADD", "register:40f0:8", ["const:465184:8", "const:4:8"]]
- 00465184 ["CALL", null, ["callee:00c57f20:8"]]
+ 004651c4 ["INT_ADD", "register:40f0:8", ["const:4651c4:8", "const:4:8"]]
+ 004651c4 ["CALL", null, ["callee:00c57f20:8"]]
- 00465184 bytes 33cb1f94
+ 004651c4 bytes 57cb1f94
- 00465194 ["INT_ADD", "register:40f0:8", ["const:465194:8", "const:4:8"]]
- 00465194 ["CALL", null, ["callee:00c57f40:8"]]
+ 004651d4 ["INT_ADD", "register:40f0:8", ["const:4651d4:8", "const:4:8"]]
+ 004651d4 ["CALL", null, ["callee:00c57f40:8"]]
- 00465194 bytes 37cb1f94
+ 004651d4 bytes 5bcb1f94
- 00465158 ["COPY", "tmp:0:8", ["const:aa0:8"]]
- 00465158 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00465158 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00465158 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00465198 ["COPY", "tmp:0:8", ["const:ba0:8"]]
+ 00465198 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00465198 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00465198 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00465158 bytes 08812a91
+ 00465198 bytes 08812e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f1830f53eace7432560c9ed9fd5a326"></a>

### [`004651c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/004651c8.md) → [`00465208`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00465/00465208.md) FUN_00465208

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
      "definition_site": "0046521c",
      "incomplete_value": false,
      "site": "00465220",
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
            "const:9e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004651dc",
      "incomplete_value": false,
      "site": "004651e0",
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
            "const:918:8"
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
      "00465220",
      "DATA",
      [
        "storage",
        "00c64918",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00465220",
      "DATA",
      [
        "storage",
        "00c649e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004651d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/004651c8.md#insn-004651d4) · [`004651dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/004651c8.md#insn-004651dc)
- 新版 `00465214`（命令位置の公開資料なし） · `0046521c`（命令位置の公開資料なし）

~~~diff
- 004651d4 ["INT_ADD", "register:40f0:8", ["const:4651d4:8", "const:4:8"]]
- 004651d4 ["CALL", null, ["callee:00c57f60:8"]]
+ 00465214 ["INT_ADD", "register:40f0:8", ["const:465214:8", "const:4:8"]]
+ 00465214 ["CALL", null, ["callee:00c57f60:8"]]
- 004651d4 bytes 2fcb1f94
+ 00465214 bytes 53cb1f94
- 004651dc ["COPY", "tmp:0:8", ["const:918:8"]]
- 004651dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004651dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004651dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0046521c ["COPY", "tmp:0:8", ["const:9e8:8"]]
+ 0046521c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0046521c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0046521c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004651dc bytes 08612491
+ 0046521c bytes 08a12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-baa0ddcac35f288458226fc07d014410"></a>

### [`004651ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/004651ec.md) → [`0046522c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00465/0046522c.md) FUN_0046522c

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
      "definition_site": "00465230",
      "incomplete_value": false,
      "site": "00465234",
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
            "const:9e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004651f0",
      "incomplete_value": false,
      "site": "004651f4",
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
            "const:918:8"
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
      "00465234",
      "DATA",
      [
        "storage",
        "00c64918",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00465234",
      "DATA",
      [
        "storage",
        "00c649e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004651f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/004651ec.md#insn-004651f0)
- 新版 `00465230`（命令位置の公開資料なし）

~~~diff
- 004651f0 ["COPY", "tmp:0:8", ["const:918:8"]]
- 004651f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004651f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004651f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00465230 ["COPY", "tmp:0:8", ["const:9e8:8"]]
+ 00465230 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00465230 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00465230 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004651f0 bytes 08612491
+ 00465230 bytes 08a12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-face7bb05288a58ea75c4ada3ead24a8"></a>

### [`00465204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465204.md) → [`00465244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00465/00465244.md) FUN_00465244

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00465284",
      "incomplete_value": false,
      "site": "0046528c",
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
            "const:ba0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00465244",
      "incomplete_value": false,
      "site": "0046524c",
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
            "const:aa0:8"
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
      "definition_site": "0046529c",
      "incomplete_value": false,
      "site": "004652a0",
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
            "const:ba0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046525c",
      "incomplete_value": false,
      "site": "00465260",
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
            "const:aa0:8"
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
      "0046525c",
      "READ",
      [
        "storage",
        "00ca4aa0",
        null,
        "undefined1"
      ]
    ],
    [
      "00465268",
      "READ",
      [
        "storage",
        "00ca4a98",
        null,
        "undefined8"
      ]
    ],
    [
      "00465284",
      "PARAM",
      [
        "storage",
        "00ca4aa0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0046525c",
      "READ",
      [
        "storage",
        "00ca4ba0",
        null,
        "undefined1"
      ]
    ],
    [
      "00465268",
      "READ",
      [
        "storage",
        "00ca4b98",
        null,
        "undefined8"
      ]
    ],
    [
      "00465284",
      "PARAM",
      [
        "storage",
        "00ca4ba0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046524c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465204.md#insn-0046524c) · [`00465260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465204.md#insn-00465260) · [`00465214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465204.md#insn-00465214)
- 新版 `0046528c`（命令位置の公開資料なし） · `004652a0`（命令位置の公開資料なし） · `00465254`（命令位置の公開資料なし）

~~~diff
- 0046524c ["INT_ADD", "register:40f0:8", ["const:46524c:8", "const:4:8"]]
- 0046524c ["CALL", null, ["callee:00c57f20:8"]]
+ 0046528c ["INT_ADD", "register:40f0:8", ["const:46528c:8", "const:4:8"]]
+ 0046528c ["CALL", null, ["callee:00c57f20:8"]]
- 0046524c bytes 01cb1f94
+ 0046528c bytes 25cb1f94
- 00465260 ["INT_ADD", "register:40f0:8", ["const:465260:8", "const:4:8"]]
- 00465260 ["CALL", null, ["callee:00c57f40:8"]]
+ 004652a0 ["INT_ADD", "register:40f0:8", ["const:4652a0:8", "const:4:8"]]
+ 004652a0 ["CALL", null, ["callee:00c57f40:8"]]
- 00465260 bytes 04cb1f94
+ 004652a0 bytes 28cb1f94
- 00465214 ["COPY", "tmp:0:8", ["const:aa0:8"]]
- 00465214 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00465214 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00465214 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00465254 ["COPY", "tmp:0:8", ["const:ba0:8"]]
+ 00465254 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00465254 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00465254 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00465214 bytes 08812a91
+ 00465254 bytes 08812e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07cf4dccc7c4410de82e6843275faa64"></a>

### [`00465298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465298.md) → [`004652d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00465/004652d8.md) FUN_004652d8

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
      "definition_site": "004652ec",
      "incomplete_value": false,
      "site": "004652f0",
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
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004652ac",
      "incomplete_value": false,
      "site": "004652b0",
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
            "const:998:8"
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
      "004652f0",
      "DATA",
      [
        "storage",
        "00c64998",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004652f0",
      "DATA",
      [
        "storage",
        "00c64a68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004652a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465298.md#insn-004652a4) · [`004652ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465298.md#insn-004652ac)
- 新版 `004652e4`（命令位置の公開資料なし） · `004652ec`（命令位置の公開資料なし）

~~~diff
- 004652a4 ["INT_ADD", "register:40f0:8", ["const:4652a4:8", "const:4:8"]]
- 004652a4 ["CALL", null, ["callee:00c57f60:8"]]
+ 004652e4 ["INT_ADD", "register:40f0:8", ["const:4652e4:8", "const:4:8"]]
+ 004652e4 ["CALL", null, ["callee:00c57f60:8"]]
- 004652a4 bytes fbca1f94
+ 004652e4 bytes 1fcb1f94
- 004652ac ["COPY", "tmp:0:8", ["const:998:8"]]
- 004652ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004652ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004652ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004652ec ["COPY", "tmp:0:8", ["const:a68:8"]]
+ 004652ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004652ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004652ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004652ac bytes 08612691
+ 004652ec bytes 08a12991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14ef4b6e1e964f0dbf2829a92a75162d"></a>

### [`004652bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/004652bc.md) → [`004652fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00465/004652fc.md) FUN_004652fc

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
      "definition_site": "00465300",
      "incomplete_value": false,
      "site": "00465304",
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
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004652c0",
      "incomplete_value": false,
      "site": "004652c4",
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
            "const:998:8"
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
      "00465304",
      "DATA",
      [
        "storage",
        "00c64998",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00465304",
      "DATA",
      [
        "storage",
        "00c64a68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004652c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/004652bc.md#insn-004652c0)
- 新版 `00465300`（命令位置の公開資料なし）

~~~diff
- 004652c0 ["COPY", "tmp:0:8", ["const:998:8"]]
- 004652c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004652c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004652c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00465300 ["COPY", "tmp:0:8", ["const:a68:8"]]
+ 00465300 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00465300 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00465300 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004652c0 bytes 08612691
+ 00465300 bytes 08a12991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30c559710db56fd3fadedfe36bb3a9d4"></a>

### [`004652d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/004652d4.md) → [`00465314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00465/00465314.md) FUN_00465314

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.73% / 新版 89.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `call_target` 1件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 2件, `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004653b8",
      "incomplete_value": true,
      "site": "004653b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:398:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00465378",
      "incomplete_value": true,
      "site": "00465378",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3ec:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "004654a4",
      "incomplete_value": true,
      "site": "004654a4",
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
              "LOAD"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00465464",
      "incomplete_value": true,
      "site": "00465464",
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
              "LOAD"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0046548c",
      "incomplete_value": true,
      "site": "004654a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046544c",
      "incomplete_value": true,
      "site": "00465464",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a98:8"
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
      "004653a4",
      "READ",
      [
        "storage",
        "002bc3ec",
        null,
        "string"
      ]
    ],
    [
      "00465480",
      "READ",
      [
        "storage",
        "00ca4aa0",
        null,
        "undefined1"
      ]
    ],
    [
      "0046548c",
      "READ",
      [
        "storage",
        "00ca4a98",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004653a4",
      "READ",
      [
        "storage",
        "002bc398",
        null,
        "string"
      ]
    ],
    [
      "00465480",
      "READ",
      [
        "storage",
        "00ca4ba0",
        null,
        "undefined1"
      ]
    ],
    [
      "0046548c",
      "READ",
      [
        "storage",
        "00ca4b98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004653b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/004652d4.md#insn-004653b8) · [`00465464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/004652d4.md#insn-00465464) · [`00465490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/004652d4.md#insn-00465490)
- 新版 `004653f8`（命令位置の公開資料なし） · `004654a4`（命令位置の公開資料なし） · `004654d0`（命令位置の公開資料なし）

~~~diff
- 004653b8 ["INT_ADD", "register:40f0:8", ["const:4653b8:8", "const:4:8"]]
- 004653b8 ["CALL", null, ["callee:00c57f80:8"]]
+ 004653f8 ["INT_ADD", "register:40f0:8", ["const:4653f8:8", "const:4:8"]]
+ 004653f8 ["CALL", null, ["callee:00c57f80:8"]]
- 004653b8 bytes beca1f94
+ 004653f8 bytes e2ca1f94
- 00465464 ["COPY", "register:0:8", ["register:4040:8"]]
- 00465464 ["INT_ADD", "register:40f0:8", ["const:465464:8", "const:4:8"]]
- 00465464 ["CALLIND", null, ["register:0:8"]]
+ 004654a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004654a4 ["INT_ADD", "register:40f0:8", ["const:4654a4:8", "const:4:8"]]
+ 004654a4 ["CALLIND", null, ["register:0:8"]]
- 00465464 bytes 00013fd6
+ 004654a4 bytes 00013fd6
- 00465490 ["COPY", "register:0:8", ["register:4040:8"]]
- 00465490 ["INT_ADD", "register:40f0:8", ["const:465490:8", "const:4:8"]]
- 00465490 ["CALLIND", null, ["register:0:8"]]
+ 004654d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004654d0 ["INT_ADD", "register:40f0:8", ["const:4654d0:8", "const:4:8"]]
+ 004654d0 ["CALLIND", null, ["register:0:8"]]
- 00465490 bytes 00013fd6
+ 004654d0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a83052d4542ffc1733fb41664eae232c"></a>

### [`00465658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465658.md) → [`00465698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00465/00465698.md) FUN_00465698

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
      "definition_site": "004656ac",
      "incomplete_value": false,
      "site": "004656b0",
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
            "const:ae8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046566c",
      "incomplete_value": false,
      "site": "00465670",
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
            "const:a18:8"
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
      "004656b0",
      "DATA",
      [
        "storage",
        "00c64a18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004656b0",
      "DATA",
      [
        "storage",
        "00c64ae8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00465664`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465658.md#insn-00465664) · [`0046566c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465658.md#insn-0046566c)
- 新版 `004656a4`（命令位置の公開資料なし） · `004656ac`（命令位置の公開資料なし）

~~~diff
- 00465664 ["INT_ADD", "register:40f0:8", ["const:465664:8", "const:4:8"]]
- 00465664 ["CALL", null, ["callee:00c57f60:8"]]
+ 004656a4 ["INT_ADD", "register:40f0:8", ["const:4656a4:8", "const:4:8"]]
+ 004656a4 ["CALL", null, ["callee:00c57f60:8"]]
- 00465664 bytes 0bca1f94
+ 004656a4 bytes 2fca1f94
- 0046566c ["COPY", "tmp:0:8", ["const:a18:8"]]
- 0046566c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0046566c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0046566c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004656ac ["COPY", "tmp:0:8", ["const:ae8:8"]]
+ 004656ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004656ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004656ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0046566c bytes 08612891
+ 004656ac bytes 08a12b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a84d6f28f4beb327af7372c5917ea526"></a>

### [`0046567c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/0046567c.md) → [`004656bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00465/004656bc.md) FUN_004656bc

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
      "definition_site": "004656c0",
      "incomplete_value": false,
      "site": "004656c4",
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
            "const:ae8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00465680",
      "incomplete_value": false,
      "site": "00465684",
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
            "const:a18:8"
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
      "004656c4",
      "DATA",
      [
        "storage",
        "00c64a18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004656c4",
      "DATA",
      [
        "storage",
        "00c64ae8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00465680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/0046567c.md#insn-00465680)
- 新版 `004656c0`（命令位置の公開資料なし）

~~~diff
- 00465680 ["COPY", "tmp:0:8", ["const:a18:8"]]
- 00465680 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00465680 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00465680 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004656c0 ["COPY", "tmp:0:8", ["const:ae8:8"]]
+ 004656c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004656c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004656c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00465680 bytes 08612891
+ 004656c0 bytes 08a12b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f17d1c7c87206741b0cf7863efd37262"></a>

### [`00465694`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465694.md) → [`004656d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00465/004656d4.md) FUN_004656d4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00465714",
      "incomplete_value": false,
      "site": "0046571c",
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
            "const:ba0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004656d4",
      "incomplete_value": false,
      "site": "004656dc",
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
            "const:aa0:8"
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
      "definition_site": "0046572c",
      "incomplete_value": false,
      "site": "00465730",
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
            "const:ba0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004656ec",
      "incomplete_value": false,
      "site": "004656f0",
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
            "const:aa0:8"
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
      "004656ec",
      "READ",
      [
        "storage",
        "00ca4aa0",
        null,
        "undefined1"
      ]
    ],
    [
      "004656f8",
      "READ",
      [
        "storage",
        "00ca4a98",
        null,
        "undefined8"
      ]
    ],
    [
      "00465714",
      "PARAM",
      [
        "storage",
        "00ca4aa0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "004656ec",
      "READ",
      [
        "storage",
        "00ca4ba0",
        null,
        "undefined1"
      ]
    ],
    [
      "004656f8",
      "READ",
      [
        "storage",
        "00ca4b98",
        null,
        "undefined8"
      ]
    ],
    [
      "00465714",
      "PARAM",
      [
        "storage",
        "00ca4ba0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004656dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465694.md#insn-004656dc) · [`004656f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465694.md#insn-004656f0) · [`004656a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465694.md#insn-004656a4)
- 新版 `0046571c`（命令位置の公開資料なし） · `00465730`（命令位置の公開資料なし） · `004656e4`（命令位置の公開資料なし）

~~~diff
- 004656dc ["INT_ADD", "register:40f0:8", ["const:4656dc:8", "const:4:8"]]
- 004656dc ["CALL", null, ["callee:00c57f20:8"]]
+ 0046571c ["INT_ADD", "register:40f0:8", ["const:46571c:8", "const:4:8"]]
+ 0046571c ["CALL", null, ["callee:00c57f20:8"]]
- 004656dc bytes ddc91f94
+ 0046571c bytes 01ca1f94
- 004656f0 ["INT_ADD", "register:40f0:8", ["const:4656f0:8", "const:4:8"]]
- 004656f0 ["CALL", null, ["callee:00c57f40:8"]]
+ 00465730 ["INT_ADD", "register:40f0:8", ["const:465730:8", "const:4:8"]]
+ 00465730 ["CALL", null, ["callee:00c57f40:8"]]
- 004656f0 bytes e0c91f94
+ 00465730 bytes 04ca1f94
- 004656a4 ["COPY", "tmp:0:8", ["const:aa0:8"]]
- 004656a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004656a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004656a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004656e4 ["COPY", "tmp:0:8", ["const:ba0:8"]]
+ 004656e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004656e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004656e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004656a4 bytes 08812a91
+ 004656e4 bytes 08812e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-901ebf2594ab46bc6e6b4c62b016ebae"></a>

### [`00465724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465724.md) → [`00465764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00465/00465764.md) FUN_00465764

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "0046577c",
      "incomplete_value": false,
      "site": "00465780",
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
            "const:b68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046573c",
      "incomplete_value": false,
      "site": "00465740",
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
      "00465780",
      "DATA",
      [
        "storage",
        "00c64a98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00465780",
      "DATA",
      [
        "storage",
        "00c64b68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046573c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465724.md#insn-0046573c) · [`00465768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465724.md#insn-00465768) · [`00465778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465724.md#insn-00465778)
- 新版 `0046577c`（命令位置の公開資料なし） · `004657a8`（命令位置の公開資料なし） · `004657b8`（命令位置の公開資料なし）

~~~diff
- 0046573c ["COPY", "tmp:0:8", ["const:a98:8"]]
- 0046573c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0046573c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0046573c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0046577c ["COPY", "tmp:0:8", ["const:b68:8"]]
+ 0046577c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0046577c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0046577c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0046573c bytes 29612a91
+ 0046577c bytes 29a12d91
- 00465768 ["INT_ADD", "register:40f0:8", ["const:465768:8", "const:4:8"]]
- 00465768 ["CALL", null, ["callee:00c57f80:8"]]
+ 004657a8 ["INT_ADD", "register:40f0:8", ["const:4657a8:8", "const:4:8"]]
+ 004657a8 ["CALL", null, ["callee:00c57f80:8"]]
- 00465768 bytes d2c91f94
+ 004657a8 bytes f6c91f94
- 00465778 ["INT_ADD", "register:40f0:8", ["const:465778:8", "const:4:8"]]
- 00465778 ["CALL", null, ["callee:00c57f80:8"]]
+ 004657b8 ["INT_ADD", "register:40f0:8", ["const:4657b8:8", "const:4:8"]]
+ 004657b8 ["CALL", null, ["callee:00c57f80:8"]]
- 00465778 bytes cec91f94
+ 004657b8 bytes f2c91f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b633b5d98a9ef99def057163bd68c422"></a>

### [`00465794`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465794.md) → [`004657d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00465/004657d4.md) FUN_004657d4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "004657ec",
      "incomplete_value": false,
      "site": "004657f0",
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
            "const:b68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004657ac",
      "incomplete_value": false,
      "site": "004657b0",
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
      "004657f0",
      "DATA",
      [
        "storage",
        "00c64a98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004657f0",
      "DATA",
      [
        "storage",
        "00c64b68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004657ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465794.md#insn-004657ac) · [`004657cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465794.md#insn-004657cc) · [`004657e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465794.md#insn-004657e4)
- 新版 `004657ec`（命令位置の公開資料なし） · `0046580c`（命令位置の公開資料なし） · `00465824`（命令位置の公開資料なし）

~~~diff
- 004657ac ["COPY", "tmp:0:8", ["const:a98:8"]]
- 004657ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004657ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004657ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004657ec ["COPY", "tmp:0:8", ["const:b68:8"]]
+ 004657ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004657ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004657ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004657ac bytes 29612a91
+ 004657ec bytes 29a12d91
- 004657cc ["INT_ADD", "register:40f0:8", ["const:4657cc:8", "const:4:8"]]
- 004657cc ["CALL", null, ["callee:00c57f80:8"]]
+ 0046580c ["INT_ADD", "register:40f0:8", ["const:46580c:8", "const:4:8"]]
+ 0046580c ["CALL", null, ["callee:00c57f80:8"]]
- 004657cc bytes b9c91f94
+ 0046580c bytes ddc91f94
- 004657e4 ["INT_ADD", "register:40f0:8", ["const:4657e4:8", "const:4:8"]]
- 004657e4 ["CALL", null, ["callee:00c57f80:8"]]
+ 00465824 ["INT_ADD", "register:40f0:8", ["const:465824:8", "const:4:8"]]
+ 00465824 ["CALL", null, ["callee:00c57f80:8"]]
- 004657e4 bytes b3c91f94
+ 00465824 bytes d7c91f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8979fd4c10e8c2c26c3f5f76a72a3a87"></a>

### [`00465804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465804.md) → [`00465844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00465/00465844.md) FUN_00465844

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`004668cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/004668cc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046690c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00466/0046690c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00465868",
      "incomplete_value": false,
      "site": "00465868",
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
            "const:b68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00465828",
      "incomplete_value": false,
      "site": "00465828",
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
            "const:a98:8"
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
      "00465868",
      "DATA",
      [
        "storage",
        "00c64a98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00465868",
      "DATA",
      [
        "storage",
        "00c64b68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00465818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465804.md#insn-00465818) · [`00465824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465804.md#insn-00465824) · [`00465830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465804.md#insn-00465830)
- 新版 `00465858`（命令位置の公開資料なし） · `00465864`（命令位置の公開資料なし） · `00465870`（命令位置の公開資料なし）

~~~diff
- 00465818 ["INT_ADD", "register:40f0:8", ["const:465818:8", "const:4:8"]]
- 00465818 ["CALL", null, ["callee:00c57f60:8"]]
+ 00465858 ["INT_ADD", "register:40f0:8", ["const:465858:8", "const:4:8"]]
+ 00465858 ["CALL", null, ["callee:00c57f60:8"]]
- 00465818 bytes 9ec91f94
+ 00465858 bytes c2c91f94
- 00465824 ["COPY", "tmp:0:8", ["const:a98:8"]]
- 00465824 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00465824 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00465824 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00465864 ["COPY", "tmp:0:8", ["const:b68:8"]]
+ 00465864 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00465864 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00465864 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00465824 bytes 08612a91
+ 00465864 bytes 08a12d91
- 00465830 ["INT_ADD", "register:40f0:8", ["const:465830:8", "const:4:8"]]
- 00465830 ["CALL", null, ["callee:0046690c:8"]]
+ 00465870 ["INT_ADD", "register:40f0:8", ["const:465870:8", "const:4:8"]]
+ 00465870 ["CALL", null, ["callee:0046690c:8"]]
- 00465830 bytes 27040094
+ 00465870 bytes 27040094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70862e52fbdba3da471c39a3a2f485ad"></a>

### [`00465858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465858.md) → [`00465898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00465/00465898.md) FUN_00465898

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`004668cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/004668cc.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0046690c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00466/0046690c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004658a4",
      "incomplete_value": false,
      "site": "004658a4",
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
            "const:b68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00465864",
      "incomplete_value": false,
      "site": "00465864",
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
      "004658a4",
      "DATA",
      [
        "storage",
        "00c64a98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004658a4",
      "DATA",
      [
        "storage",
        "00c64b68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00465860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/00465858.md#insn-00465860)
- 新版 `004658a0`（命令位置の公開資料なし）

~~~diff
- 00465860 ["COPY", "tmp:0:8", ["const:a98:8"]]
- 00465860 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00465860 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00465860 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004658a0 ["COPY", "tmp:0:8", ["const:b68:8"]]
+ 004658a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004658a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004658a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00465860 bytes 29612a91
+ 004658a0 bytes 29a12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18974090ea517b6d191885f69aec6daa"></a>

### [`0046593c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/0046593c.md) → [`0046597c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00465/0046597c.md) FUN_0046597c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 22件 [`0043db54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043db54.md) [`0044fcbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044fcbc.md) [`00450180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/00450180.md) [`00450750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/00450750.md) [`0055e874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e874.md)
- 新版 呼出元 0件  · 呼出先 22件 [`0043db94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043db94.md) [`0044fcfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044fcfc.md) [`004501c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/004501c0.md) [`00450790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/00450790.md) [`0055e8b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055e/0055e8b4.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.09% / 新版 92.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 20件, `call_target` 3件, `store_value` 9件

アドレスに依存する影響 `call_argument_candidate` 2件, `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004659fc",
      "incomplete_value": true,
      "site": "004659fc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b3000:8"
              ],
              [
                "leaf",
                "const:93f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004659bc",
      "incomplete_value": true,
      "site": "004659bc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b3000:8"
              ],
              [
                "leaf",
                "const:90e:8"
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
      "definition_site": "00465bd0",
      "incomplete_value": true,
      "site": "00465bd0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:937:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00465b90",
      "incomplete_value": true,
      "site": "00465b90",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:993:8"
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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00465dd0",
      "incomplete_value": true,
      "site": "00465de0",
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
                "const:2b2000:8"
              ],
              [
                "leaf",
                "const:991:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00465d90",
      "incomplete_value": true,
      "site": "00465da0",
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
                "const:2b2000:8"
              ],
              [
                "leaf",
                "const:960:8"
              ]
            ]
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
      "004659e0",
      "READ",
      [
        "storage",
        "002b390e",
        null,
        "string"
      ]
    ],
    [
      "00465a9c",
      "READ",
      [
        "storage",
        "00ca4aa0",
        null,
        "undefined1"
      ]
    ],
    [
      "00465aa8",
      "READ",
      [
        "storage",
        "00ca4a98",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004659e0",
      "READ",
      [
        "storage",
        "002b393f",
        null,
        "string"
      ]
    ],
    [
      "00465a9c",
      "READ",
      [
        "storage",
        "00ca4ba0",
        null,
        "undefined1"
      ]
    ],
    [
      "00465aa8",
      "READ",
      [
        "storage",
        "00ca4b98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00465c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/0046593c.md#insn-00465c98) · [`00465d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/0046593c.md#insn-00465d04) · [`00465d40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00465/0046593c.md#insn-00465d40)
- 新版 `00465cd8`（命令位置の公開資料なし） · `00465d44`（命令位置の公開資料なし） · `00465d80`（命令位置の公開資料なし）

~~~diff
- 00465c98 ["COPY", "register:0:8", ["register:4040:8"]]
- 00465c98 ["INT_ADD", "register:40f0:8", ["const:465c98:8", "const:4:8"]]
- 00465c98 ["CALLIND", null, ["register:0:8"]]
+ 00465cd8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00465cd8 ["INT_ADD", "register:40f0:8", ["const:465cd8:8", "const:4:8"]]
+ 00465cd8 ["CALLIND", null, ["register:0:8"]]
- 00465c98 bytes 00013fd6
+ 00465cd8 bytes 00013fd6
- 00465d04 ["COPY", "register:0:8", ["register:4040:8"]]
- 00465d04 ["INT_ADD", "register:40f0:8", ["const:465d04:8", "const:4:8"]]
- 00465d04 ["CALLIND", null, ["register:0:8"]]
+ 00465d44 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00465d44 ["INT_ADD", "register:40f0:8", ["const:465d44:8", "const:4:8"]]
+ 00465d44 ["CALLIND", null, ["register:0:8"]]
- 00465d04 bytes 00013fd6
+ 00465d44 bytes 00013fd6
- 00465d40 ["COPY", "register:0:8", ["register:4040:8"]]
- 00465d40 ["INT_ADD", "register:40f0:8", ["const:465d40:8", "const:4:8"]]
- 00465d40 ["CALLIND", null, ["register:0:8"]]
+ 00465d80 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00465d80 ["INT_ADD", "register:40f0:8", ["const:465d80:8", "const:4:8"]]
+ 00465d80 ["CALLIND", null, ["register:0:8"]]
- 00465d40 bytes 00013fd6
+ 00465d80 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ace48f7a5b6545aafe9b6e9b2b9651e6"></a>

### [`004669c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/004669c0.md) → [`00466a00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00466/00466a00.md) FUN_00466a00

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
      "definition_site": "00466a14",
      "incomplete_value": false,
      "site": "00466a18",
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
            "const:be8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004669d4",
      "incomplete_value": false,
      "site": "004669d8",
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
            "const:b18:8"
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
      "00466a18",
      "DATA",
      [
        "storage",
        "00c64b18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00466a18",
      "DATA",
      [
        "storage",
        "00c64be8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004669cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/004669c0.md#insn-004669cc) · [`004669d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/004669c0.md#insn-004669d4)
- 新版 `00466a0c`（命令位置の公開資料なし） · `00466a14`（命令位置の公開資料なし）

~~~diff
- 004669cc ["INT_ADD", "register:40f0:8", ["const:4669cc:8", "const:4:8"]]
- 004669cc ["CALL", null, ["callee:00c57f60:8"]]
+ 00466a0c ["INT_ADD", "register:40f0:8", ["const:466a0c:8", "const:4:8"]]
+ 00466a0c ["CALL", null, ["callee:00c57f60:8"]]
- 004669cc bytes 31c51f94
+ 00466a0c bytes 55c51f94
- 004669d4 ["COPY", "tmp:0:8", ["const:b18:8"]]
- 004669d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004669d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004669d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00466a14 ["COPY", "tmp:0:8", ["const:be8:8"]]
+ 00466a14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00466a14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00466a14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004669d4 bytes 08612c91
+ 00466a14 bytes 08a12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0cf2c6c18d931e48cbb5661094f2ccb4"></a>

### [`004669e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/004669e4.md) → [`00466a24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00466/00466a24.md) FUN_00466a24

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
      "definition_site": "00466a28",
      "incomplete_value": false,
      "site": "00466a2c",
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
            "const:be8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004669e8",
      "incomplete_value": false,
      "site": "004669ec",
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
            "const:b18:8"
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
      "00466a2c",
      "DATA",
      [
        "storage",
        "00c64b18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00466a2c",
      "DATA",
      [
        "storage",
        "00c64be8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004669e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/004669e4.md#insn-004669e8)
- 新版 `00466a28`（命令位置の公開資料なし）

~~~diff
- 004669e8 ["COPY", "tmp:0:8", ["const:b18:8"]]
- 004669e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004669e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004669e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00466a28 ["COPY", "tmp:0:8", ["const:be8:8"]]
+ 00466a28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00466a28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00466a28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004669e8 bytes 08612c91
+ 00466a28 bytes 08a12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8084539949d18b6f503c1afd97169129"></a>

### [`004669fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/004669fc.md) → [`00466a3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00466/00466a3c.md) FUN_00466a3c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 80.95% / 新版 80.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00466a74",
      "incomplete_value": false,
      "site": "00466a78",
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
            "const:ba0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00466a34",
      "incomplete_value": false,
      "site": "00466a38",
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
            "const:aa0:8"
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
      "definition_site": "00466a84",
      "incomplete_value": false,
      "site": "00466a88",
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
            "const:ba0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00466a44",
      "incomplete_value": false,
      "site": "00466a48",
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
            "const:aa0:8"
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
      "00466a4c",
      "READ",
      [
        "storage",
        "00ca4aa0",
        null,
        "undefined1"
      ]
    ],
    [
      "00466a58",
      "READ",
      [
        "storage",
        "00ca4a98",
        null,
        "undefined8"
      ]
    ],
    [
      "00466a74",
      "PARAM",
      [
        "storage",
        "00ca4aa0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00466a4c",
      "READ",
      [
        "storage",
        "00ca4ba0",
        null,
        "undefined1"
      ]
    ],
    [
      "00466a58",
      "READ",
      [
        "storage",
        "00ca4b98",
        null,
        "undefined8"
      ]
    ],
    [
      "00466a74",
      "PARAM",
      [
        "storage",
        "00ca4ba0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00466a08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/004669fc.md#insn-00466a08) · [`00466a38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/004669fc.md#insn-00466a38) · [`00466a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/004669fc.md#insn-00466a48)
- 新版 `00466a48`（命令位置の公開資料なし） · `00466a78`（命令位置の公開資料なし） · `00466a88`（命令位置の公開資料なし）

~~~diff
- 00466a08 ["COPY", "tmp:0:8", ["const:aa0:8"]]
- 00466a08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00466a08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00466a08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00466a48 ["COPY", "tmp:0:8", ["const:ba0:8"]]
+ 00466a48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00466a48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00466a48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00466a08 bytes 08812a91
+ 00466a48 bytes 08812e91
- 00466a38 ["INT_ADD", "register:40f0:8", ["const:466a38:8", "const:4:8"]]
- 00466a38 ["CALL", null, ["callee:00c57f20:8"]]
+ 00466a78 ["INT_ADD", "register:40f0:8", ["const:466a78:8", "const:4:8"]]
+ 00466a78 ["CALL", null, ["callee:00c57f20:8"]]
- 00466a38 bytes 06c51f94
+ 00466a78 bytes 2ac51f94
- 00466a48 ["INT_ADD", "register:40f0:8", ["const:466a48:8", "const:4:8"]]
- 00466a48 ["CALL", null, ["callee:00c57f40:8"]]
+ 00466a88 ["INT_ADD", "register:40f0:8", ["const:466a88:8", "const:4:8"]]
+ 00466a88 ["CALL", null, ["callee:00c57f40:8"]]
- 00466a48 bytes 0ac51f94
+ 00466a88 bytes 2ec51f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e918cc34097e8fb71374c8bdf0628b5"></a>

### [`00466a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466a80.md) → [`00466ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00466/00466ac0.md) FUN_00466ac0

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
      "definition_site": "00466ad4",
      "incomplete_value": false,
      "site": "00466ad8",
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
            "const:c68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00466a94",
      "incomplete_value": false,
      "site": "00466a98",
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
            "const:b98:8"
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
      "00466ad8",
      "DATA",
      [
        "storage",
        "00c64b98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00466ad8",
      "DATA",
      [
        "storage",
        "00c64c68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00466a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466a80.md#insn-00466a8c) · [`00466a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466a80.md#insn-00466a94)
- 新版 `00466acc`（命令位置の公開資料なし） · `00466ad4`（命令位置の公開資料なし）

~~~diff
- 00466a8c ["INT_ADD", "register:40f0:8", ["const:466a8c:8", "const:4:8"]]
- 00466a8c ["CALL", null, ["callee:00c57f60:8"]]
+ 00466acc ["INT_ADD", "register:40f0:8", ["const:466acc:8", "const:4:8"]]
+ 00466acc ["CALL", null, ["callee:00c57f60:8"]]
- 00466a8c bytes 01c51f94
+ 00466acc bytes 25c51f94
- 00466a94 ["COPY", "tmp:0:8", ["const:b98:8"]]
- 00466a94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00466a94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00466a94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00466ad4 ["COPY", "tmp:0:8", ["const:c68:8"]]
+ 00466ad4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00466ad4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00466ad4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00466a94 bytes 08612e91
+ 00466ad4 bytes 08a13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6b6318ae77dd0ff54546586bfe3c649"></a>

### [`00466aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466aa4.md) → [`00466ae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00466/00466ae4.md) FUN_00466ae4

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
      "definition_site": "00466ae8",
      "incomplete_value": false,
      "site": "00466aec",
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
            "const:c68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00466aa8",
      "incomplete_value": false,
      "site": "00466aac",
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
            "const:b98:8"
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
      "00466aec",
      "DATA",
      [
        "storage",
        "00c64b98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00466aec",
      "DATA",
      [
        "storage",
        "00c64c68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00466aa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466aa4.md#insn-00466aa8)
- 新版 `00466ae8`（命令位置の公開資料なし）

~~~diff
- 00466aa8 ["COPY", "tmp:0:8", ["const:b98:8"]]
- 00466aa8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00466aa8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00466aa8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00466ae8 ["COPY", "tmp:0:8", ["const:c68:8"]]
+ 00466ae8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00466ae8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00466ae8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00466aa8 bytes 08612e91
+ 00466ae8 bytes 08a13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55868b5740a35625b7fb459e2f8dd283"></a>

### [`00466abc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466abc.md) → [`00466afc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00466/00466afc.md) FUN_00466afc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 80.95% / 新版 80.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00466b34",
      "incomplete_value": false,
      "site": "00466b38",
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
            "const:ba0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00466af4",
      "incomplete_value": false,
      "site": "00466af8",
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
            "const:aa0:8"
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
      "definition_site": "00466b44",
      "incomplete_value": false,
      "site": "00466b48",
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
            "const:ba0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00466b04",
      "incomplete_value": false,
      "site": "00466b08",
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
            "const:aa0:8"
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
      "00466b0c",
      "READ",
      [
        "storage",
        "00ca4aa0",
        null,
        "undefined1"
      ]
    ],
    [
      "00466b18",
      "READ",
      [
        "storage",
        "00ca4a98",
        null,
        "undefined8"
      ]
    ],
    [
      "00466b34",
      "PARAM",
      [
        "storage",
        "00ca4aa0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00466b0c",
      "READ",
      [
        "storage",
        "00ca4ba0",
        null,
        "undefined1"
      ]
    ],
    [
      "00466b18",
      "READ",
      [
        "storage",
        "00ca4b98",
        null,
        "undefined8"
      ]
    ],
    [
      "00466b34",
      "PARAM",
      [
        "storage",
        "00ca4ba0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00466ac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466abc.md#insn-00466ac8) · [`00466af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466abc.md#insn-00466af8) · [`00466b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466abc.md#insn-00466b08)
- 新版 `00466b08`（命令位置の公開資料なし） · `00466b38`（命令位置の公開資料なし） · `00466b48`（命令位置の公開資料なし）

~~~diff
- 00466ac8 ["COPY", "tmp:0:8", ["const:aa0:8"]]
- 00466ac8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00466ac8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00466ac8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00466b08 ["COPY", "tmp:0:8", ["const:ba0:8"]]
+ 00466b08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00466b08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00466b08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00466ac8 bytes 08812a91
+ 00466b08 bytes 08812e91
- 00466af8 ["INT_ADD", "register:40f0:8", ["const:466af8:8", "const:4:8"]]
- 00466af8 ["CALL", null, ["callee:00c57f20:8"]]
+ 00466b38 ["INT_ADD", "register:40f0:8", ["const:466b38:8", "const:4:8"]]
+ 00466b38 ["CALL", null, ["callee:00c57f20:8"]]
- 00466af8 bytes d6c41f94
+ 00466b38 bytes fac41f94
- 00466b08 ["INT_ADD", "register:40f0:8", ["const:466b08:8", "const:4:8"]]
- 00466b08 ["CALL", null, ["callee:00c57f40:8"]]
+ 00466b48 ["INT_ADD", "register:40f0:8", ["const:466b48:8", "const:4:8"]]
+ 00466b48 ["CALL", null, ["callee:00c57f40:8"]]
- 00466b08 bytes dac41f94
+ 00466b48 bytes fec41f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-323bc20f8d9cb4d80a871523c3c336c9"></a>

### [`00466b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466b38.md) → [`00466b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00466/00466b78.md) FUN_00466b78

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00466b84",
      "incomplete_value": false,
      "site": "00466b90",
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
            "const:ce8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00466b44",
      "incomplete_value": false,
      "site": "00466b50",
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
            "const:c18:8"
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
      "00466b90",
      "DATA",
      [
        "storage",
        "00c64c18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00466b90",
      "DATA",
      [
        "storage",
        "00c64ce8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00466b44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466b38.md#insn-00466b44)
- 新版 `00466b84`（命令位置の公開資料なし）

~~~diff
- 00466b44 ["COPY", "tmp:0:8", ["const:c18:8"]]
- 00466b44 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00466b44 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00466b44 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00466b84 ["COPY", "tmp:0:8", ["const:ce8:8"]]
+ 00466b84 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00466b84 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00466b84 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00466b44 bytes 4a613091
+ 00466b84 bytes 4aa13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e33b9f7a09b316ae41de62b53703e77"></a>

### [`00466b7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466b7c.md) → [`00466bbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00466/00466bbc.md) FUN_00466bbc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00466bd4",
      "incomplete_value": false,
      "site": "00466be0",
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
            "const:ce8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00466b94",
      "incomplete_value": false,
      "site": "00466ba0",
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
            "const:c18:8"
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
      "00466be0",
      "DATA",
      [
        "storage",
        "00c64c18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00466be0",
      "DATA",
      [
        "storage",
        "00c64ce8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00466b94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466b7c.md#insn-00466b94) · [`00466bc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466b7c.md#insn-00466bc4)
- 新版 `00466bd4`（命令位置の公開資料なし） · `00466c04`（命令位置の公開資料なし）

~~~diff
- 00466b94 ["COPY", "tmp:0:8", ["const:c18:8"]]
- 00466b94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00466b94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00466b94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00466bd4 ["COPY", "tmp:0:8", ["const:ce8:8"]]
+ 00466bd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00466bd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00466bd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00466b94 bytes 08613091
+ 00466bd4 bytes 08a13391
- 00466bc4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00466bc4 ["INT_ADD", "register:40f0:8", ["const:466bc4:8", "const:4:8"]]
- 00466bc4 ["CALLIND", null, ["register:0:8"]]
+ 00466c04 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00466c04 ["INT_ADD", "register:40f0:8", ["const:466c04:8", "const:4:8"]]
+ 00466c04 ["CALLIND", null, ["register:0:8"]]
- 00466bc4 bytes 00013fd6
+ 00466c04 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f44d75532c8118c8042995d3dd26060"></a>

### [`00466bd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466bd8.md) → [`00466c18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00466/00466c18.md) FUN_00466c18

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00466c44",
      "incomplete_value": false,
      "site": "00466c44",
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
            "const:ce8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00466c04",
      "incomplete_value": false,
      "site": "00466c04",
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
            "const:c18:8"
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
      "00466c44",
      "DATA",
      [
        "storage",
        "00c64c18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00466c44",
      "DATA",
      [
        "storage",
        "00c64ce8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00466bec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466bd8.md#insn-00466bec) · [`00466bfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466bd8.md#insn-00466bfc) · [`00466c20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466bd8.md#insn-00466c20)
- 新版 `00466c2c`（命令位置の公開資料なし） · `00466c3c`（命令位置の公開資料なし） · `00466c60`（命令位置の公開資料なし）

~~~diff
- 00466bec ["INT_ADD", "register:40f0:8", ["const:466bec:8", "const:4:8"]]
- 00466bec ["CALL", null, ["callee:00c57f60:8"]]
+ 00466c2c ["INT_ADD", "register:40f0:8", ["const:466c2c:8", "const:4:8"]]
+ 00466c2c ["CALL", null, ["callee:00c57f60:8"]]
- 00466bec bytes a9c41f94
+ 00466c2c bytes cdc41f94
- 00466bfc ["COPY", "tmp:0:8", ["const:c18:8"]]
- 00466bfc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00466bfc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00466bfc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00466c3c ["COPY", "tmp:0:8", ["const:ce8:8"]]
+ 00466c3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00466c3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00466c3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00466bfc bytes 08613091
+ 00466c3c bytes 08a13391
- 00466c20 ["COPY", "register:0:8", ["register:4040:8"]]
- 00466c20 ["INT_ADD", "register:40f0:8", ["const:466c20:8", "const:4:8"]]
- 00466c20 ["CALLIND", null, ["register:0:8"]]
+ 00466c60 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00466c60 ["INT_ADD", "register:40f0:8", ["const:466c60:8", "const:4:8"]]
+ 00466c60 ["CALLIND", null, ["register:0:8"]]
- 00466c20 bytes 00013fd6
+ 00466c60 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9cd85728d3d01b1bb12aa72aeb81dcf3"></a>

### [`00466c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466c60.md) → [`00466ca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00466/00466ca0.md) FUN_00466ca0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00466cbc",
      "incomplete_value": false,
      "site": "00466cbc",
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
            "const:ce8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00466c7c",
      "incomplete_value": false,
      "site": "00466c7c",
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
            "const:c18:8"
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
      "00466cbc",
      "DATA",
      [
        "storage",
        "00c64c18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00466cbc",
      "DATA",
      [
        "storage",
        "00c64ce8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00466c78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466c60.md#insn-00466c78) · [`00466c9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466c60.md#insn-00466c9c)
- 新版 `00466cb8`（命令位置の公開資料なし） · `00466cdc`（命令位置の公開資料なし）

~~~diff
- 00466c78 ["COPY", "tmp:0:8", ["const:c18:8"]]
- 00466c78 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00466c78 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00466c78 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00466cb8 ["COPY", "tmp:0:8", ["const:ce8:8"]]
+ 00466cb8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00466cb8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00466cb8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00466c78 bytes 29613091
+ 00466cb8 bytes 29a13391
- 00466c9c ["COPY", "register:0:8", ["register:4048:8"]]
- 00466c9c ["INT_ADD", "register:40f0:8", ["const:466c9c:8", "const:4:8"]]
- 00466c9c ["CALLIND", null, ["register:0:8"]]
+ 00466cdc ["COPY", "register:0:8", ["register:4048:8"]]
+ 00466cdc ["INT_ADD", "register:40f0:8", ["const:466cdc:8", "const:4:8"]]
+ 00466cdc ["CALLIND", null, ["register:0:8"]]
- 00466c9c bytes 20013fd6
+ 00466cdc bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77d763049f81feb6eeb148b453a3d142"></a>

### [`00466f0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466f0c.md) → [`00466f4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00466/00466f4c.md) FUN_00466f4c

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
      "definition_site": "00466f60",
      "incomplete_value": false,
      "site": "00466f64",
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
            "const:d68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00466f20",
      "incomplete_value": false,
      "site": "00466f24",
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
            "const:c98:8"
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
      "00466f64",
      "DATA",
      [
        "storage",
        "00c64c98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00466f64",
      "DATA",
      [
        "storage",
        "00c64d68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00466f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466f0c.md#insn-00466f18) · [`00466f20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466f0c.md#insn-00466f20)
- 新版 `00466f58`（命令位置の公開資料なし） · `00466f60`（命令位置の公開資料なし）

~~~diff
- 00466f18 ["INT_ADD", "register:40f0:8", ["const:466f18:8", "const:4:8"]]
- 00466f18 ["CALL", null, ["callee:00c57f60:8"]]
+ 00466f58 ["INT_ADD", "register:40f0:8", ["const:466f58:8", "const:4:8"]]
+ 00466f58 ["CALL", null, ["callee:00c57f60:8"]]
- 00466f18 bytes dec31f94
+ 00466f58 bytes 02c41f94
- 00466f20 ["COPY", "tmp:0:8", ["const:c98:8"]]
- 00466f20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00466f20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00466f20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00466f60 ["COPY", "tmp:0:8", ["const:d68:8"]]
+ 00466f60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00466f60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00466f60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00466f20 bytes 08613291
+ 00466f60 bytes 08a13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-113a703fbeef72d949c33430af6b5822"></a>

### [`00466f30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466f30.md) → [`00466f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00466/00466f70.md) FUN_00466f70

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
      "definition_site": "00466f74",
      "incomplete_value": false,
      "site": "00466f78",
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
            "const:d68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00466f34",
      "incomplete_value": false,
      "site": "00466f38",
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
            "const:c98:8"
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
      "00466f78",
      "DATA",
      [
        "storage",
        "00c64c98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00466f78",
      "DATA",
      [
        "storage",
        "00c64d68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00466f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466f30.md#insn-00466f34)
- 新版 `00466f74`（命令位置の公開資料なし）

~~~diff
- 00466f34 ["COPY", "tmp:0:8", ["const:c98:8"]]
- 00466f34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00466f34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00466f34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00466f74 ["COPY", "tmp:0:8", ["const:d68:8"]]
+ 00466f74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00466f74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00466f74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00466f34 bytes 08613291
+ 00466f74 bytes 08a13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59ad2dd0bfe0b869724928b10c1ac2da"></a>

### [`00466f48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466f48.md) → [`00466f88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00466/00466f88.md) FUN_00466f88

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`004594d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) [`00596d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596d10.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md)
- 新版 呼出元 0件  · 呼出先 9件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00459510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459510.md) [`00596d50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596d50.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.63% / 新版 89.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 4件, `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0046703c",
      "incomplete_value": true,
      "site": "0046703c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6cf:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00466ffc",
      "incomplete_value": true,
      "site": "00466ffc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:723:8"
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
      "definition_site": "00466fe8",
      "incomplete_value": true,
      "site": "00466fec",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9a000:8"
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
    "old": {
      "definition_site": "00466fa8",
      "incomplete_value": true,
      "site": "00466fac",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9a000:8"
              ],
              [
                "leaf",
                "const:c70:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "004670a4",
      "incomplete_value": true,
      "site": "004670a4",
      "value": [
        "LOAD",
        "8",
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
                "const:80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00467064",
      "incomplete_value": true,
      "site": "00467064",
      "value": [
        "LOAD",
        "8",
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
                "const:80:8"
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
      "00466fe8",
      "READ",
      [
        "storage",
        "00c9ac70",
        null,
        "pointer"
      ]
    ],
    [
      "00466fe8",
      "PARAM",
      [
        "storage",
        "01127500",
        "_ZNSt6__ndk14coutE",
        "undefined8"
      ]
    ],
    [
      "0046702c",
      "READ",
      [
        "storage",
        "002bd723",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00466fe8",
      "READ",
      [
        "storage",
        "00c9ad40",
        null,
        "pointer"
      ]
    ],
    [
      "00466fe8",
      "PARAM",
      [
        "storage",
        "01127600",
        "_ZNSt6__ndk14coutE",
        "undefined8"
      ]
    ],
    [
      "0046702c",
      "READ",
      [
        "storage",
        "002bd6cf",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00466fac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466f48.md#insn-00466fac) · [`00466fbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466f48.md#insn-00466fbc) · [`00467024`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00466/00466f48.md#insn-00467024)
- 新版 `00466fec`（命令位置の公開資料なし） · `00466ffc`（命令位置の公開資料なし） · `00467064`（命令位置の公開資料なし）

~~~diff
- 00466fac ["INT_ADD", "register:40f0:8", ["const:466fac:8", "const:4:8"]]
- 00466fac ["CALL", null, ["callee:00459510:8"]]
+ 00466fec ["INT_ADD", "register:40f0:8", ["const:466fec:8", "const:4:8"]]
+ 00466fec ["CALL", null, ["callee:00459510:8"]]
- 00466fac bytes 49c9ff97
+ 00466fec bytes 49c9ff97
- 00466fbc ["INT_ADD", "register:40f0:8", ["const:466fbc:8", "const:4:8"]]
- 00466fbc ["CALL", null, ["callee:00c57f80:8"]]
+ 00466ffc ["INT_ADD", "register:40f0:8", ["const:466ffc:8", "const:4:8"]]
+ 00466ffc ["CALL", null, ["callee:00c57f80:8"]]
- 00466fbc bytes bdc31f94
+ 00466ffc bytes e1c31f94
- 00467024 ["COPY", "register:0:8", ["register:4040:8"]]
- 00467024 ["INT_ADD", "register:40f0:8", ["const:467024:8", "const:4:8"]]
- 00467024 ["CALLIND", null, ["register:0:8"]]
+ 00467064 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00467064 ["INT_ADD", "register:40f0:8", ["const:467064:8", "const:4:8"]]
+ 00467064 ["CALLIND", null, ["register:0:8"]]
- 00467024 bytes 00013fd6
+ 00467064 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-266957873f88db7d23d2866b0caa30ae"></a>

### [`00467258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467258.md) → [`00467298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467298.md) _INIT_11

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
      "definition_site": "004672d4",
      "incomplete_value": true,
      "site": "004672f0",
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
      "definition_site": "00467294",
      "incomplete_value": true,
      "site": "004672b0",
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
      "definition_site": "004672f8",
      "incomplete_value": true,
      "site": "00467314",
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
      "definition_site": "004672b8",
      "incomplete_value": true,
      "site": "004672d4",
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
      "definition_site": "00467318",
      "incomplete_value": true,
      "site": "00467334",
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
      "definition_site": "004672d8",
      "incomplete_value": true,
      "site": "004672f4",
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
      "004672d4",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "004672f8",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00467318",
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
      "004672d4",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "004672f8",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "00467318",
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

- 旧版 [`004672d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467258.md#insn-004672d0) · [`004672f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467258.md#insn-004672f0) · [`004673b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467258.md#insn-004673b8)
- 新版 `00467310`（命令位置の公開資料なし） · `00467330`（命令位置の公開資料なし） · `004673f8`（命令位置の公開資料なし）

~~~diff
- 004672d0 ["COPY", "tmp:0:8", ["const:dc2:8"]]
- 004672d0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004672d0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004672d0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00467310 ["COPY", "tmp:0:8", ["const:d6e:8"]]
+ 00467310 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00467310 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00467310 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004672d0 bytes 4a093791
+ 00467310 bytes 4ab93591
- 004672f0 ["COPY", "tmp:0:8", ["const:f62:8"]]
- 004672f0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004672f0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004672f0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00467330 ["COPY", "tmp:0:8", ["const:f15:8"]]
+ 00467330 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00467330 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00467330 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004672f0 bytes 4a893d91
+ 00467330 bytes 4a553c91
- 004673b8 ["INT_ADD", "register:40f0:8", ["const:4673b8:8", "const:4:8"]]
- 004673b8 ["CALL", null, ["callee:0043b838:8"]]
+ 004673f8 ["INT_ADD", "register:40f0:8", ["const:4673f8:8", "const:4:8"]]
+ 004673f8 ["CALL", null, ["callee:0043b838:8"]]
- 004673b8 bytes 1051ff97
+ 004673f8 bytes 1051ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ee02203da6a0bcddb65d9c4b4e7f28c"></a>

### [`00467650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467650.md) → [`00467690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467690.md) FUN_00467690

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0046de24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046de24.md) [`005fc3a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fc/005fc3a0.md) · 呼出先 0件 
- 新版 呼出元 2件 [`0046de64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046de64.md) [`005fc3e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005fc/005fc3e0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 72.73% / 新版 72.73%

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
      "definition_site": "0046769c",
      "incomplete_value": true,
      "site": "004676a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046765c",
      "incomplete_value": true,
      "site": "00467668",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004676a4",
      "incomplete_value": true,
      "site": "004676ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:de0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00467664",
      "incomplete_value": true,
      "site": "0046766c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da0:8"
              ]
            ]
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
      "0046769c",
      "READ",
      [
        "storage",
        "002c3d98",
        null,
        "undefined8"
      ]
    ],
    [
      "004676a4",
      "READ",
      [
        "storage",
        "002c3da0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0046769c",
      "READ",
      [
        "storage",
        "002c3dd8",
        null,
        "undefined8"
      ]
    ],
    [
      "004676a4",
      "READ",
      [
        "storage",
        "002c3de0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046765c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467650.md#insn-0046765c) · [`00467660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467650.md#insn-00467660) · [`00467664`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467650.md#insn-00467664)
- 新版 `0046769c`（命令位置の公開資料なし） · `004676a4`（命令位置の公開資料なし）

~~~diff
- 0046765c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d98:8"]]
- 0046765c ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
- 0046765c ["COPY", "register:5008:8", ["const:0:8"]]
- 0046765c ["COPY", "register:5010:8", ["const:0:8"]]
+ 0046769c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd8:8"]]
+ 0046769c ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0046769c ["COPY", "register:5008:8", ["const:0:8"]]
+ 0046769c ["COPY", "register:5010:8", ["const:0:8"]]
- 0046765c bytes 00cd46fd
+ 0046769c bytes 00ed46fd
- 00467660 ["COPY", "register:4040:8", ["const:2c3000:8"]]
- 00467660 bytes e8f2ff90
- 00467664 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:da0:8"]]
- 00467664 ["LOAD", "register:5040:8", ["const:1b1:8", "tmp:0:8"]]
- 00467664 ["COPY", "register:5048:8", ["const:0:8"]]
- 00467664 ["COPY", "register:5050:8", ["const:0:8"]]
+ 004676a4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:de0:8"]]
+ 004676a4 ["LOAD", "register:5040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004676a4 ["COPY", "register:5048:8", ["const:0:8"]]
+ 004676a4 ["COPY", "register:5050:8", ["const:0:8"]]
- 00467664 bytes 02d146fd
+ 004676a4 bytes 02f146fd
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db1fd6539df6ab381b68147a45ec478e"></a>

### [`0046767c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/0046767c.md) → [`004676bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004676bc.md) FUN_004676bc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00a47104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47104.md) [`00a47634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47634.md) · 呼出先 0件 
- 新版 呼出元 2件 [`00a47158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a47/00a47158.md) [`00a47688`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a47/00a47688.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 55.56% / 新版 55.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004676c8",
      "incomplete_value": true,
      "site": "004676d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00467688",
      "incomplete_value": true,
      "site": "00467694",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d98:8"
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
      "definition_site": "004676cc",
      "incomplete_value": true,
      "site": "004676d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:de0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046768c",
      "incomplete_value": true,
      "site": "00467698",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da0:8"
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
      "004676c8",
      "READ",
      [
        "storage",
        "002c3d98",
        null,
        "undefined8"
      ]
    ],
    [
      "004676cc",
      "READ",
      [
        "storage",
        "002c3da0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004676c8",
      "READ",
      [
        "storage",
        "002c3dd8",
        null,
        "undefined8"
      ]
    ],
    [
      "004676cc",
      "READ",
      [
        "storage",
        "002c3de0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00467688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/0046767c.md#insn-00467688) · [`0046768c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/0046767c.md#insn-0046768c)
- 新版 `004676c8`（命令位置の公開資料なし） · `004676cc`（命令位置の公開資料なし）

~~~diff
- 00467688 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d98:8"]]
- 00467688 ["LOAD", "register:5040:8", ["const:1b1:8", "tmp:0:8"]]
- 00467688 ["COPY", "register:5048:8", ["const:0:8"]]
- 00467688 ["COPY", "register:5050:8", ["const:0:8"]]
+ 004676c8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd8:8"]]
+ 004676c8 ["LOAD", "register:5040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004676c8 ["COPY", "register:5048:8", ["const:0:8"]]
+ 004676c8 ["COPY", "register:5050:8", ["const:0:8"]]
- 00467688 bytes 02cd46fd
+ 004676c8 bytes 02ed46fd
- 0046768c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:da0:8"]]
- 0046768c ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
- 0046768c ["COPY", "register:5008:8", ["const:0:8"]]
- 0046768c ["COPY", "register:5010:8", ["const:0:8"]]
+ 004676cc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:de0:8"]]
+ 004676cc ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
+ 004676cc ["COPY", "register:5008:8", ["const:0:8"]]
+ 004676cc ["COPY", "register:5010:8", ["const:0:8"]]
- 0046768c bytes 20d146fd
+ 004676cc bytes 20f146fd
~~~


<a id="compare-6b913bd598643fc7e028aa93af008306"></a>

### [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) → [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) FUN_004678a0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 154件 [`005c4958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c4/005c4958.md) [`005c7d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c7/005c7d00.md) [`005e0424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e0424.md) [`005e4074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e4/005e4074.md) [`005ed274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ed/005ed274.md) · 呼出先 5件 [`004678f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/004678f0.md) [`0046791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/0046791c.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)
- 新版 呼出元 154件 [`005c4998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c4/005c4998.md) [`005c7d40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c7/005c7d40.md) [`005e0464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e0/005e0464.md) [`005e40b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e4/005e40b4.md) [`005ed2b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ed/005ed2b4.md) · 呼出先 5件 [`00467930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467930.md) [`0046795c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/0046795c.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 63.33% / 新版 63.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `call_target` 1件, `return_value_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004678d4",
      "incomplete_value": false,
      "site": "004678d8",
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
            "const:d10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00467894",
      "incomplete_value": false,
      "site": "00467898",
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
            "const:c10:8"
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
      "definition_site": null,
      "incomplete_value": true,
      "site": "004678e8",
      "value": [
        "leaf",
        "ram:467930:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004678a8",
      "value": [
        "leaf",
        "ram:4678f0:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004678e4",
      "incomplete_value": false,
      "site": "004678e8",
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
            "const:ca8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004678a4",
      "incomplete_value": false,
      "site": "004678a8",
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
            "const:ba8:8"
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
      "004678b4",
      "READ",
      [
        "storage",
        "00ca4c10",
        null,
        "undefined1"
      ]
    ],
    [
      "004678c0",
      "DATA",
      [
        "storage",
        "00ca4ba8",
        null,
        null
      ]
    ],
    [
      "004678d4",
      "PARAM",
      [
        "storage",
        "00ca4c10",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "004678b4",
      "READ",
      [
        "storage",
        "00ca4d10",
        null,
        "undefined1"
      ]
    ],
    [
      "004678c0",
      "DATA",
      [
        "storage",
        "00ca4ca8",
        null,
        null
      ]
    ],
    [
      "004678d4",
      "PARAM",
      [
        "storage",
        "00ca4d10",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00467898`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md#insn-00467898) · [`004678a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md#insn-004678a8) · [`004678c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md#insn-004678c4)
- 新版 `004678d8`（命令位置の公開資料なし） · `004678e8`（命令位置の公開資料なし） · `00467904`（命令位置の公開資料なし）

~~~diff
- 00467898 ["INT_ADD", "register:40f0:8", ["const:467898:8", "const:4:8"]]
- 00467898 ["CALL", null, ["callee:00c57f20:8"]]
+ 004678d8 ["INT_ADD", "register:40f0:8", ["const:4678d8:8", "const:4:8"]]
+ 004678d8 ["CALL", null, ["callee:00c57f20:8"]]
- 00467898 bytes 6ec11f94
+ 004678d8 bytes 92c11f94
- 004678a8 ["INT_ADD", "register:40f0:8", ["const:4678a8:8", "const:4:8"]]
- 004678a8 ["CALL", null, ["ram:4678f0:8"]]
+ 004678e8 ["INT_ADD", "register:40f0:8", ["const:4678e8:8", "const:4:8"]]
+ 004678e8 ["CALL", null, ["ram:467930:8"]]
- 004678a8 bytes 12000094
+ 004678e8 bytes 12000094
- 004678c4 ["INT_ADD", "register:40f0:8", ["const:4678c4:8", "const:4:8"]]
- 004678c4 ["CALL", null, ["callee:00c57f00:8"]]
+ 00467904 ["INT_ADD", "register:40f0:8", ["const:467904:8", "const:4:8"]]
+ 00467904 ["CALL", null, ["callee:00c57f00:8"]]
- 004678c4 bytes 5bc11f94
+ 00467904 bytes 7fc11f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7af12ff55b7233da1481cdbf3f139ca"></a>

### [`0046796c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/0046796c.md) → [`004679ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004679ac.md) FUN_004679ac

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b2c200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2c200.md) · 呼出先 11件 [`00467dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467dbc.md) [`0046ca54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046ca54.md) [`0046cb0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046cb0c.md) [`0055a624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a624.md) [`0055a6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a6a4.md)
- 新版 呼出元 1件 [`00b2c29c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2c/00b2c29c.md) · 呼出先 11件 [`00467dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467dfc.md) [`0046ca94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca94.md) [`0046cb4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046cb4c.md) [`0055a664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055a/0055a664.md) [`0055a6e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055a/0055a6e4.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.96% / 新版 92.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00467a64",
      "incomplete_value": true,
      "site": "00467a6c",
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
                "const:950:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00467a24",
      "incomplete_value": true,
      "site": "00467a2c",
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
                "const:910:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00467a00",
      "incomplete_value": false,
      "site": "00467a04",
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
            "const:d70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004679c0",
      "incomplete_value": false,
      "site": "004679c4",
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
            "const:c70:8"
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
      "definition_site": "00467a24",
      "incomplete_value": false,
      "site": "00467a28",
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
            "const:d70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004679e4",
      "incomplete_value": false,
      "site": "004679e8",
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
            "const:c70:8"
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
      "00467a00",
      "PARAM",
      [
        "storage",
        "00ca4c70",
        null,
        "undefined8"
      ]
    ],
    [
      "00467a24",
      "PARAM",
      [
        "storage",
        "00ca4c70",
        null,
        "undefined8"
      ]
    ],
    [
      "00467a48",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0055a6a4"
      ]
    ]
  ],
  "added": [
    [
      "00467a00",
      "PARAM",
      [
        "storage",
        "00ca4d70",
        null,
        "undefined8"
      ]
    ],
    [
      "00467a24",
      "PARAM",
      [
        "storage",
        "00ca4d70",
        null,
        "undefined8"
      ]
    ],
    [
      "00467a48",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0055a6e4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004679c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/0046796c.md#insn-004679c4) · [`004679e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/0046796c.md#insn-004679e8) · [`00467a04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/0046796c.md#insn-00467a04)
- 新版 `00467a04`（命令位置の公開資料なし） · `00467a28`（命令位置の公開資料なし） · `00467a44`（命令位置の公開資料なし）

~~~diff
- 004679c4 ["INT_ADD", "register:40f0:8", ["const:4679c4:8", "const:4:8"]]
- 004679c4 ["CALL", null, ["callee:0046ca94:8"]]
+ 00467a04 ["INT_ADD", "register:40f0:8", ["const:467a04:8", "const:4:8"]]
+ 00467a04 ["CALL", null, ["callee:0046ca94:8"]]
- 004679c4 bytes 24140094
+ 00467a04 bytes 24140094
- 004679e8 ["INT_ADD", "register:40f0:8", ["const:4679e8:8", "const:4:8"]]
- 004679e8 ["CALL", null, ["callee:0046cb4c:8"]]
+ 00467a28 ["INT_ADD", "register:40f0:8", ["const:467a28:8", "const:4:8"]]
+ 00467a28 ["CALL", null, ["callee:0046cb4c:8"]]
- 004679e8 bytes 49140094
+ 00467a28 bytes 49140094
- 00467a04 ["INT_ADD", "register:40f0:8", ["const:467a04:8", "const:4:8"]]
- 00467a04 ["CALL", null, ["callee:00467dfc:8"]]
+ 00467a44 ["INT_ADD", "register:40f0:8", ["const:467a44:8", "const:4:8"]]
+ 00467a44 ["CALL", null, ["callee:00467dfc:8"]]
- 00467a04 bytes ee000094
+ 00467a44 bytes ee000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4489ad991cf6598452cee89a6b6500a5"></a>

### [`00467a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467a88.md) → [`00467ac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467ac8.md) FUN_00467ac8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 11件 [`005f46ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f4/005f46ac.md) [`005f4d6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f4/005f4d6c.md) [`0065cccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065c/0065cccc.md) [`0065d630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065d/0065d630.md) [`00707ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707ee0.md) · 呼出先 4件 [`0046ca54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046ca54.md) [`0046cb0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046cb0c.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`0085ad58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085a/0085ad58.md)
- 新版 呼出元 11件 [`005f46ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005f4/005f46ec.md) [`005f4dac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005f4/005f4dac.md) [`0065cd0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0065c/0065cd0c.md) [`0065d670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0065d/0065d670.md) [`00707f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00707/00707f38.md) · 呼出先 4件 [`0046ca94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca94.md) [`0046cb4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046cb4c.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`0085adb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085a/0085adb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00467ae4",
      "incomplete_value": true,
      "site": "00467aec",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
      "definition_site": "00467aa4",
      "incomplete_value": true,
      "site": "00467aac",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00467b04",
      "incomplete_value": false,
      "site": "00467b08",
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
            "const:d70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00467ac4",
      "incomplete_value": false,
      "site": "00467ac8",
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
            "const:c70:8"
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
      "00467ae4",
      "READ",
      [
        "storage",
        "00c9ab68",
        null,
        "pointer"
      ]
    ],
    [
      "00467ae4",
      "PARAM",
      [
        "storage",
        "00ca4c70",
        null,
        "undefined8"
      ]
    ],
    [
      "00467b04",
      "PARAM",
      [
        "storage",
        "00ca4c70",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00467ae4",
      "READ",
      [
        "storage",
        "00c9ac38",
        null,
        "pointer"
      ]
    ],
    [
      "00467ae4",
      "PARAM",
      [
        "storage",
        "00ca4d70",
        null,
        "undefined8"
      ]
    ],
    [
      "00467b04",
      "PARAM",
      [
        "storage",
        "00ca4d70",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00467aac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467a88.md#insn-00467aac) · [`00467ac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467a88.md#insn-00467ac8) · [`00467aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467a88.md#insn-00467aa4)
- 新版 `00467aec`（命令位置の公開資料なし） · `00467b08`（命令位置の公開資料なし） · `00467ae4`（命令位置の公開資料なし）

~~~diff
- 00467aac ["INT_ADD", "register:40f0:8", ["const:467aac:8", "const:4:8"]]
- 00467aac ["CALL", null, ["callee:0046ca94:8"]]
+ 00467aec ["INT_ADD", "register:40f0:8", ["const:467aec:8", "const:4:8"]]
+ 00467aec ["CALL", null, ["callee:0046ca94:8"]]
- 00467aac bytes ea130094
+ 00467aec bytes ea130094
- 00467ac8 ["INT_ADD", "register:40f0:8", ["const:467ac8:8", "const:4:8"]]
- 00467ac8 ["CALL", null, ["callee:0046cb4c:8"]]
+ 00467b08 ["INT_ADD", "register:40f0:8", ["const:467b08:8", "const:4:8"]]
+ 00467b08 ["CALL", null, ["callee:0046cb4c:8"]]
- 00467ac8 bytes 11140094
+ 00467b08 bytes 11140094
- 00467aa4 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:b68:8"]]
- 00467aa4 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00467ae4 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:c38:8"]]
+ 00467ae4 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00467aa4 bytes 00b445f9
+ 00467ae4 bytes 001c46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c46078707fd7f6fc27a1cb4e50dc9b6"></a>

### [`00467afc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467afc.md) → [`00467b3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467b3c.md) FUN_00467b3c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`006bf88c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006bf/006bf88c.md) [`00707ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707ee0.md) [`00789de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00789/00789de0.md) [`00859b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859b58.md) · 呼出先 3件 [`00467dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467dbc.md) [`0055a6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a6a4.md) [`0055a6a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a6a8.md)
- 新版 呼出元 4件 [`006bf8e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bf/006bf8e4.md) [`00707f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00707/00707f38.md) [`00789e38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00789/00789e38.md) [`00859bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00859/00859bb0.md) · 呼出先 3件 [`00467dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467dfc.md) [`0055a6e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055a/0055a6e4.md) [`0055a6e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055a/0055a6e8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 91.67% / 新版 91.67%

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
      "site": "00467b54",
      "value": [
        "leaf",
        "ram:55a6e4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00467b14",
      "value": [
        "leaf",
        "ram:55a6a4:8"
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
      "00467b54",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0055a6a4"
      ]
    ]
  ],
  "added": [
    [
      "00467b54",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0055a6e4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00467b14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467afc.md#insn-00467b14) · [`00467b10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467afc.md#insn-00467b10)
- 新版 `00467b54`（命令位置の公開資料なし） · `00467b50`（命令位置の公開資料なし）

~~~diff
- 00467b14 ["INT_ADD", "register:40f0:8", ["const:467b14:8", "const:4:8"]]
- 00467b14 ["CALL", null, ["ram:55a6a4:8"]]
+ 00467b54 ["INT_ADD", "register:40f0:8", ["const:467b54:8", "const:4:8"]]
+ 00467b54 ["CALL", null, ["ram:55a6e4:8"]]
- 00467b14 bytes e4ca0394
+ 00467b54 bytes e4ca0394
- 00467b10 ["INT_ADD", "register:40f0:8", ["const:467b10:8", "const:4:8"]]
- 00467b10 ["CALL", null, ["callee:00467dfc:8"]]
+ 00467b50 ["INT_ADD", "register:40f0:8", ["const:467b50:8", "const:4:8"]]
+ 00467b50 ["CALL", null, ["callee:00467dfc:8"]]
- 00467b10 bytes ab000094
+ 00467b50 bytes ab000094
~~~


<a id="compare-77e1fe0ac0d982e40b3ef7e1bf3a1059"></a>

### [`00467eac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467eac.md) → [`00467eec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467eec.md) FUN_00467eec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`005ed274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ed/005ed274.md) [`00707ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707ee0.md) [`00789de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00789/00789de0.md) · 呼出先 5件 [`00467dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467dbc.md) [`0055a6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a6a4.md) [`0055a6a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a6a8.md) [`0055a6ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a6ac.md) [`0055a6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055a/0055a6b0.md)
- 新版 呼出元 3件 [`005ed2b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ed/005ed2b4.md) [`00707f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00707/00707f38.md) [`00789e38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00789/00789e38.md) · 呼出先 5件 [`00467dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467dfc.md) [`0055a6e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055a/0055a6e4.md) [`0055a6e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055a/0055a6e8.md) [`0055a6ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055a/0055a6ec.md) [`0055a6f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055a/0055a6f0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.43% / 新版 96.43%

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
      "site": "00467f0c",
      "value": [
        "leaf",
        "ram:55a6e4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00467ecc",
      "value": [
        "leaf",
        "ram:55a6a4:8"
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
      "00467f0c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0055a6a4"
      ]
    ]
  ],
  "added": [
    [
      "00467f0c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0055a6e4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00467ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467eac.md#insn-00467ecc) · [`00467ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467eac.md#insn-00467ec8) · [`00467ed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467eac.md#insn-00467ed8)
- 新版 `00467f0c`（命令位置の公開資料なし） · `00467f08`（命令位置の公開資料なし） · `00467f18`（命令位置の公開資料なし）

~~~diff
- 00467ecc ["INT_ADD", "register:40f0:8", ["const:467ecc:8", "const:4:8"]]
- 00467ecc ["CALL", null, ["ram:55a6a4:8"]]
+ 00467f0c ["INT_ADD", "register:40f0:8", ["const:467f0c:8", "const:4:8"]]
+ 00467f0c ["CALL", null, ["ram:55a6e4:8"]]
- 00467ecc bytes f6c90394
+ 00467f0c bytes f6c90394
- 00467ec8 ["INT_ADD", "register:40f0:8", ["const:467ec8:8", "const:4:8"]]
- 00467ec8 ["CALL", null, ["callee:00467dfc:8"]]
+ 00467f08 ["INT_ADD", "register:40f0:8", ["const:467f08:8", "const:4:8"]]
+ 00467f08 ["CALL", null, ["callee:00467dfc:8"]]
- 00467ec8 bytes bdffff97
+ 00467f08 bytes bdffff97
- 00467ed8 ["INT_ADD", "register:40f0:8", ["const:467ed8:8", "const:4:8"]]
- 00467ed8 ["CALL", null, ["callee:0055a6e8:8"]]
+ 00467f18 ["INT_ADD", "register:40f0:8", ["const:467f18:8", "const:4:8"]]
+ 00467f18 ["CALL", null, ["callee:0055a6e8:8"]]
- 00467ed8 bytes f4c90394
+ 00467f18 bytes f4c90394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-331cf7aaf2de186c635c1b8ec09027b3"></a>

### [`004681c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/004681c0.md) → [`00468200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468200.md) FUN_00468200

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 5件 [`005ed274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ed/005ed274.md) [`005ef5ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ef/005ef5ac.md) [`006b61c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b6/006b61c4.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) [`009259d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00925/009259d0.md) · 呼出先 12件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00467dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467dbc.md) [`004684e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/004684e8.md) [`00468500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468500.md) [`0046c44c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c44c.md)
- 新版 呼出元 5件 [`005ed2b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ed/005ed2b4.md) [`005ef5ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ef/005ef5ec.md) [`006b621c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b6/006b621c.md) [`007df140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007df/007df140.md) [`00925a24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00925/00925a24.md) · 呼出先 12件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00467dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467dfc.md) [`00468528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468528.md) [`00468540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468540.md) [`0046c48c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046c48c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 89.60% / 新版 89.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_destination` 4件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "004682bc",
      "incomplete_value": true,
      "site": "004682bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4050:8"
          ],
          [
            "leaf",
            "const:d20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046827c",
      "incomplete_value": true,
      "site": "0046827c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4050:8"
          ],
          [
            "leaf",
            "const:c20:8"
          ]
        ]
      ]
    },
    "ordinal": 28,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "004683b4",
      "incomplete_value": false,
      "site": "004683b4",
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
            "const:d18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00468374",
      "incomplete_value": false,
      "site": "00468374",
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
            "const:c18:8"
          ]
        ]
      ]
    },
    "ordinal": 35,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "004683b4",
      "incomplete_value": false,
      "site": "004683b4",
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
                "const:d18:8"
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
      "definition_site": "00468374",
      "incomplete_value": false,
      "site": "00468374",
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
                "const:c18:8"
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
    "ordinal": 36,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0046823c",
      "READ",
      [
        "storage",
        "00ca4c30",
        null,
        "undefined1"
      ]
    ],
    [
      "00468258",
      "READ",
      [
        "storage",
        "00ca4c18",
        null,
        "undefined8"
      ]
    ],
    [
      "00468260",
      "WRITE",
      [
        "storage",
        "00ca4c20",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0046823c",
      "READ",
      [
        "storage",
        "00ca4d30",
        null,
        "undefined1"
      ]
    ],
    [
      "00468258",
      "READ",
      [
        "storage",
        "00ca4d18",
        null,
        "undefined8"
      ]
    ],
    [
      "00468260",
      "WRITE",
      [
        "storage",
        "00ca4d20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046827c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/004681c0.md#insn-0046827c) · [`004683b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/004681c0.md#insn-004683b4) · [`004683d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/004681c0.md#insn-004683d4)
- 新版 `004682bc`（命令位置の公開資料なし） · `004683f4`（命令位置の公開資料なし） · `00468414`（命令位置の公開資料なし）

~~~diff
- 0046827c ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:c20:8"]]
- 0046827c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40e0:8"]]
+ 004682bc ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:d20:8"]]
+ 004682bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40e0:8"]]
- 0046827c bytes 5c1106f9
+ 004682bc bytes 5c9106f9
- 004683b4 ["COPY", "tmp:0:8", ["const:c38:8"]]
- 004683b4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 004683b4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 004683b4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 004683f4 ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 004683f4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 004683f4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 004683f4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 004683b4 bytes 73e23091
+ 004683f4 bytes 73e23491
- 004683d4 ["INT_ADD", "register:40f0:8", ["const:4683d4:8", "const:4:8"]]
- 004683d4 ["CALL", null, ["callee:00468540:8"]]
+ 00468414 ["INT_ADD", "register:40f0:8", ["const:468414:8", "const:4:8"]]
+ 00468414 ["CALL", null, ["callee:00468540:8"]]
- 004683d4 bytes 4b000094
+ 00468414 bytes 4b000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-434a9060e9a48e6c53e1159e86f1a124"></a>

### [`0046c44c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c44c.md) → [`0046c48c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046c48c.md) FUN_0046c48c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 10件 [`004681c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/004681c0.md) [`00468500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468500.md) [`00555478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555478.md) [`00555e0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00555/00555e0c.md) [`00559c10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00559/00559c10.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 10件 [`00468200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468200.md) [`00468540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468540.md) [`005554b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/005554b8.md) [`00555e4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00555/00555e4c.md) [`00559c50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00559/00559c50.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "0046c498",
      "incomplete_value": false,
      "site": "0046c49c",
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
      "definition_site": "0046c458",
      "incomplete_value": false,
      "site": "0046c45c",
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
      "0046c498",
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
      "0046c498",
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

- 旧版 [`0046c45c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c44c.md#insn-0046c45c) · [`0046c458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c44c.md#insn-0046c458)
- 新版 `0046c49c`（命令位置の公開資料なし） · `0046c498`（命令位置の公開資料なし）

~~~diff
- 0046c45c ["INT_ADD", "register:40f0:8", ["const:46c45c:8", "const:4:8"]]
- 0046c45c ["CALL", null, ["callee:0043b7b8:8"]]
+ 0046c49c ["INT_ADD", "register:40f0:8", ["const:46c49c:8", "const:4:8"]]
+ 0046c49c ["CALL", null, ["callee:0043b7b8:8"]]
- 0046c45c bytes c73cff97
+ 0046c49c bytes c73cff97
- 0046c458 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 0046c458 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0046c458 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0046c458 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0046c498 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 0046c498 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0046c498 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0046c498 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0046c458 bytes 00303d91
+ 0046c498 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2be6c95bfd3c5f834c50e9fdcf7b4b5f"></a>

### [`0046c460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c460.md) → [`0046c4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046c4a0.md) FUN_0046c4a0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 7件 [`00467ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467ffc.md) [`00559964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00559/00559964.md) [`005de680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005de/005de680.md) [`00812ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00812/00812ecc.md) [`00813e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00813/00813e50.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 7件 [`0046803c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/0046803c.md) [`005599a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00559/005599a4.md) [`005de6c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005de/005de6c0.md) [`00812f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00812/00812f24.md) [`00813ea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00813/00813ea8.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "0046c4ac",
      "incomplete_value": false,
      "site": "0046c4b0",
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
      "definition_site": "0046c46c",
      "incomplete_value": false,
      "site": "0046c470",
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
      "0046c4ac",
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
      "0046c4ac",
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

- 旧版 [`0046c470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c460.md#insn-0046c470) · [`0046c46c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c460.md#insn-0046c46c)
- 新版 `0046c4b0`（命令位置の公開資料なし） · `0046c4ac`（命令位置の公開資料なし）

~~~diff
- 0046c470 ["INT_ADD", "register:40f0:8", ["const:46c470:8", "const:4:8"]]
- 0046c470 ["CALL", null, ["callee:0043b7b8:8"]]
+ 0046c4b0 ["INT_ADD", "register:40f0:8", ["const:46c4b0:8", "const:4:8"]]
+ 0046c4b0 ["CALL", null, ["callee:0043b7b8:8"]]
- 0046c470 bytes c23cff97
+ 0046c4b0 bytes c23cff97
- 0046c46c ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 0046c46c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0046c46c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0046c46c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0046c4ac ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 0046c4ac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0046c4ac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0046c4ac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0046c46c bytes 00303d91
+ 0046c4ac bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0115004855e8117b6d5566c91d379b3c"></a>

### [`0046c614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c614.md) → [`0046c654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046c654.md) FUN_0046c654

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0046c474`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c474.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 1件 [`0046c4b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046c4b4.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "0046c660",
      "incomplete_value": false,
      "site": "0046c664",
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
      "definition_site": "0046c620",
      "incomplete_value": false,
      "site": "0046c624",
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
      "0046c660",
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
      "0046c660",
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

- 旧版 [`0046c624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c614.md#insn-0046c624) · [`0046c620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c614.md#insn-0046c620)
- 新版 `0046c664`（命令位置の公開資料なし） · `0046c660`（命令位置の公開資料なし）

~~~diff
- 0046c624 ["INT_ADD", "register:40f0:8", ["const:46c624:8", "const:4:8"]]
- 0046c624 ["CALL", null, ["callee:0043b7b8:8"]]
+ 0046c664 ["INT_ADD", "register:40f0:8", ["const:46c664:8", "const:4:8"]]
+ 0046c664 ["CALL", null, ["callee:0043b7b8:8"]]
- 0046c624 bytes 553cff97
+ 0046c664 bytes 553cff97
- 0046c620 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 0046c620 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0046c620 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0046c620 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0046c660 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 0046c660 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0046c660 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0046c660 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0046c620 bytes 00303d91
+ 0046c660 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f2ba95be51d515e6d7565efe92676dc"></a>

### [`0046c628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c628.md) → [`0046c668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046c668.md) _INIT_12

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
      "definition_site": "0046c6a4",
      "incomplete_value": true,
      "site": "0046c6c0",
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
      "definition_site": "0046c664",
      "incomplete_value": true,
      "site": "0046c680",
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
      "definition_site": "0046c6c8",
      "incomplete_value": true,
      "site": "0046c6e4",
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
      "definition_site": "0046c688",
      "incomplete_value": true,
      "site": "0046c6a4",
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
      "definition_site": "0046c6e8",
      "incomplete_value": true,
      "site": "0046c704",
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
      "definition_site": "0046c6a8",
      "incomplete_value": true,
      "site": "0046c6c4",
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
      "0046c6a4",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "0046c6c8",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "0046c6e8",
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
      "0046c6a4",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "0046c6c8",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "0046c6e8",
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

- 旧版 [`0046c6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c628.md#insn-0046c6a0) · [`0046c6c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c628.md#insn-0046c6c0) · [`0046c788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c628.md#insn-0046c788)
- 新版 `0046c6e0`（命令位置の公開資料なし） · `0046c700`（命令位置の公開資料なし） · `0046c7c8`（命令位置の公開資料なし）

~~~diff
- 0046c6a0 ["COPY", "tmp:0:8", ["const:dc2:8"]]
- 0046c6a0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0046c6a0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0046c6a0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0046c6e0 ["COPY", "tmp:0:8", ["const:d6e:8"]]
+ 0046c6e0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0046c6e0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0046c6e0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0046c6a0 bytes 4a093791
+ 0046c6e0 bytes 4ab93591
- 0046c6c0 ["COPY", "tmp:0:8", ["const:f62:8"]]
- 0046c6c0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0046c6c0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0046c6c0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0046c700 ["COPY", "tmp:0:8", ["const:f15:8"]]
+ 0046c700 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0046c700 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0046c700 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0046c6c0 bytes 4a893d91
+ 0046c700 bytes 4a553c91
- 0046c788 ["INT_ADD", "register:40f0:8", ["const:46c788:8", "const:4:8"]]
- 0046c788 ["CALL", null, ["callee:0043b838:8"]]
+ 0046c7c8 ["INT_ADD", "register:40f0:8", ["const:46c7c8:8", "const:4:8"]]
+ 0046c7c8 ["CALL", null, ["callee:0043b838:8"]]
- 0046c788 bytes 1c3cff97
+ 0046c7c8 bytes 1c3cff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d20c44211d457f331e5460f9c196711f"></a>

### [`0046caa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046caa4.md) → [`0046cae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046cae4.md) FUN_0046cae4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00b2bbcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2bbcc.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00b2bc68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2b/00b2bc68.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0046caec",
      "incomplete_value": false,
      "site": "0046caec",
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
            "const:db4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046caac",
      "incomplete_value": false,
      "site": "0046caac",
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
            "const:cb4:8"
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
      "0046caec",
      "WRITE",
      [
        "storage",
        "00ca4cb4",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0046caec",
      "WRITE",
      [
        "storage",
        "00ca4db4",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046caac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046caa4.md#insn-0046caac)
- 新版 `0046caec`（命令位置の公開資料なし）

~~~diff
- 0046caac ["COPY", "tmp:0:4", ["register:4048:4"]]
- 0046caac ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:cb4:8"]]
- 0046caac ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 0046caec ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 0046caec ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:db4:8"]]
+ 0046caec ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 0046caac bytes 09d13239
+ 0046caec bytes 09d13639
~~~


<a id="compare-2f57f1b4d164e34b72c25564e8211a9e"></a>

### [`0046cb0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046cb0c.md) → [`0046cb4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046cb4c.md) FUN_0046cb4c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 26件 [`0046796c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/0046796c.md) [`00467a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467a88.md) [`00490b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00490/00490b34.md) [`00492120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492120.md) [`0049256c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/0049256c.md) · 呼出先 0件 
- 新版 呼出元 26件 [`004679ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004679ac.md) [`00467ac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467ac8.md) [`00490b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00490/00490b74.md) [`00492160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492160.md) [`004925ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/004925ac.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "0046cb8c",
      "incomplete_value": true,
      "site": "0046cb90",
      "value": [
        "TRUNC",
        "4",
        [
          [
            "FLOAT_DIV",
            "4",
            [
              "FLOAT_MULT",
              "INT2FLOAT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046cb4c",
      "incomplete_value": true,
      "site": "0046cb50",
      "value": [
        "TRUNC",
        "4",
        [
          [
            "FLOAT_DIV",
            "4",
            [
              "FLOAT_MULT",
              "INT2FLOAT"
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
      "0046cb70",
      "READ",
      [
        "storage",
        "00ca4ca4",
        null,
        "undefined4"
      ]
    ],
    [
      "0046cb74",
      "READ",
      [
        "storage",
        "00ca4c78",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0046cb70",
      "READ",
      [
        "storage",
        "00ca4da4",
        null,
        "undefined4"
      ]
    ],
    [
      "0046cb74",
      "READ",
      [
        "storage",
        "00ca4d78",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046cb28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046cb0c.md#insn-0046cb28)
- 新版 `0046cb68`（命令位置の公開資料なし）

~~~diff
- 0046cb28 ["COPY", "tmp:0:8", ["const:c78:8"]]
- 0046cb28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0046cb28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0046cb28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0046cb68 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 0046cb68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0046cb68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0046cb68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0046cb28 bytes 08e13191
+ 0046cb68 bytes 08e13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc238ab21ebf8889f2586387ea3480df"></a>

### [`0046cc1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046cc1c.md) → [`0046cc5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046cc5c.md) FUN_0046cc5c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`005f6c54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f6/005f6c54.md) [`005f7130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f7/005f7130.md) [`00707ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707ee0.md) [`00a47f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a47/00a47f00.md) [`00a4f2f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f2f8.md) · 呼出先 0件 
- 新版 呼出元 5件 [`005f6c94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005f6/005f6c94.md) [`005f7170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005f7/005f7170.md) [`00707f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00707/00707f38.md) [`00a47f54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a47/00a47f54.md) [`00a4f368`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f368.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 59.09% / 新版 59.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "0046cca4",
      "incomplete_value": true,
      "site": "0046cca8",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "INT_SUB",
            "4",
            [
              [
                "live",
                "register:4048:4"
              ],
              "TRUNC"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046cc64",
      "incomplete_value": true,
      "site": "0046cc68",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "INT_SUB",
            "4",
            [
              [
                "live",
                "register:4048:4"
              ],
              "TRUNC"
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
      "0046cc80",
      "READ",
      [
        "storage",
        "00ca4ca8",
        null,
        "undefined4"
      ]
    ],
    [
      "0046cc84",
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
      "0046cc80",
      "READ",
      [
        "storage",
        "00ca4da8",
        null,
        "undefined4"
      ]
    ],
    [
      "0046cc84",
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

- 旧版 [`0046cc38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046cc1c.md#insn-0046cc38)
- 新版 `0046cc78`（命令位置の公開資料なし）

~~~diff
- 0046cc38 ["COPY", "tmp:0:8", ["const:c7c:8"]]
- 0046cc38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0046cc38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0046cc38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0046cc78 ["COPY", "tmp:0:8", ["const:d7c:8"]]
+ 0046cc78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0046cc78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0046cc78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0046cc38 bytes 08f13191
+ 0046cc78 bytes 08f13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f5a9a6c0b86a45e815f77af03757202"></a>

### [`0046ccf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046ccf4.md) → [`0046cd34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046cd34.md) _INIT_13

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 80.54% / 新版 80.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 8件, `store_value` 8件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0046cd70",
      "incomplete_value": true,
      "site": "0046cd8c",
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
      "definition_site": "0046cd30",
      "incomplete_value": true,
      "site": "0046cd4c",
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
      "definition_site": "0046cd94",
      "incomplete_value": true,
      "site": "0046cdb0",
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
      "definition_site": "0046cd54",
      "incomplete_value": true,
      "site": "0046cd70",
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
      "definition_site": "0046cdb4",
      "incomplete_value": true,
      "site": "0046cdd0",
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
      "definition_site": "0046cd74",
      "incomplete_value": true,
      "site": "0046cd90",
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
      "0046cd70",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "0046cd94",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "0046cdb4",
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
      "0046cd70",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "0046cd94",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "0046cdb4",
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

- 旧版 [`0046cd6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046ccf4.md#insn-0046cd6c) · [`0046cd8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046ccf4.md#insn-0046cd8c) · [`0046ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046ccf4.md#insn-0046ce54)
- 新版 `0046cdac`（命令位置の公開資料なし） · `0046cdcc`（命令位置の公開資料なし） · `0046ce94`（命令位置の公開資料なし）

~~~diff
- 0046cd6c ["COPY", "tmp:0:8", ["const:dc2:8"]]
- 0046cd6c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0046cd6c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0046cd6c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0046cdac ["COPY", "tmp:0:8", ["const:d6e:8"]]
+ 0046cdac ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0046cdac ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0046cdac ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0046cd6c bytes 4a093791
+ 0046cdac bytes 4ab93591
- 0046cd8c ["COPY", "tmp:0:8", ["const:f62:8"]]
- 0046cd8c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0046cd8c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0046cd8c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0046cdcc ["COPY", "tmp:0:8", ["const:f15:8"]]
+ 0046cdcc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0046cdcc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0046cdcc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0046cd8c bytes 4a893d91
+ 0046cdcc bytes 4a553c91
- 0046ce54 ["INT_ADD", "register:40f0:8", ["const:46ce54:8", "const:4:8"]]
- 0046ce54 ["CALL", null, ["callee:0043b838:8"]]
+ 0046ce94 ["INT_ADD", "register:40f0:8", ["const:46ce94:8", "const:4:8"]]
+ 0046ce94 ["CALL", null, ["callee:0043b838:8"]]
- 0046ce54 bytes 693aff97
+ 0046ce94 bytes 693aff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b06a31826d7e47a440ddde3eeb217c26"></a>

### [`0046d0a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d0a4.md) → [`0046d0e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d0e4.md) FUN_0046d0e4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00b1f428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1f/00b1f428.md) · 呼出先 4件 [`0046d118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d118.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)
- 新版 呼出元 2件 [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00b1f4c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b1f/00b1f4c4.md) · 呼出先 4件 [`0046d158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d158.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate, store_destination, store_value

命令の説明率　旧版 62.07% / 新版 62.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `return_value_candidate` 1件, `store_destination` 3件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0046d138",
      "incomplete_value": false,
      "site": "0046d138",
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
                "const:db8:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046d0f8",
      "incomplete_value": false,
      "site": "0046d0f8",
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
                "const:cb8:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0046d13c",
      "incomplete_value": false,
      "site": "0046d13c",
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
                "const:db8:8"
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
      "definition_site": "0046d0fc",
      "incomplete_value": false,
      "site": "0046d0fc",
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
                "const:cb8:8"
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0046d140",
      "incomplete_value": false,
      "site": "0046d140",
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
            "const:db8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046d100",
      "incomplete_value": false,
      "site": "0046d100",
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
            "const:cb8:8"
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
      "0046d0f4",
      "READ",
      [
        "storage",
        "00ca4cd0",
        null,
        "undefined1"
      ]
    ],
    [
      "0046d100",
      "DATA",
      [
        "storage",
        "00ca4cb8",
        null,
        "undefined8"
      ]
    ],
    [
      "0046d110",
      "PARAM",
      [
        "storage",
        "00ca4cd0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0046d0f4",
      "READ",
      [
        "storage",
        "00ca4dd0",
        null,
        "undefined1"
      ]
    ],
    [
      "0046d100",
      "DATA",
      [
        "storage",
        "00ca4db8",
        null,
        "undefined8"
      ]
    ],
    [
      "0046d110",
      "PARAM",
      [
        "storage",
        "00ca4dd0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046d0c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d0a4.md#insn-0046d0c0) · [`0046d0d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d0a4.md#insn-0046d0d0) · [`0046d0d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d0a4.md#insn-0046d0d4)
- 新版 `0046d100`（命令位置の公開資料なし） · `0046d110`（命令位置の公開資料なし） · `0046d114`（命令位置の公開資料なし）

~~~diff
- 0046d0c0 ["COPY", "tmp:0:8", ["const:cb8:8"]]
- 0046d0c0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0046d0c0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0046d0c0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0046d100 ["COPY", "tmp:0:8", ["const:db8:8"]]
+ 0046d100 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0046d100 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0046d100 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0046d0c0 bytes 00e03291
+ 0046d100 bytes 00e03691
- 0046d0d0 ["COPY", "tmp:0:8", ["const:cd0:8"]]
- 0046d0d0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0046d0d0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0046d0d0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0046d110 ["COPY", "tmp:0:8", ["const:dd0:8"]]
+ 0046d110 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0046d110 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0046d110 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0046d0d0 bytes 00403391
+ 0046d110 bytes 00403791
- 0046d0d4 ["INT_ADD", "register:40f0:8", ["const:46d0d4:8", "const:4:8"]]
- 0046d0d4 ["CALL", null, ["callee:00c57f20:8"]]
+ 0046d114 ["INT_ADD", "register:40f0:8", ["const:46d114:8", "const:4:8"]]
+ 0046d114 ["CALL", null, ["callee:00c57f20:8"]]
- 0046d0d4 bytes 5fab1f94
+ 0046d114 bytes 83ab1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0915d68bce7045461c57473a031758b4"></a>

### [`0046d120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d120.md) → [`0046d160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d160.md) FUN_0046d160

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00b1f428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1f/00b1f428.md) · 呼出先 15件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0046d5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d5a8.md) [`0048792c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048792c.md) [`00487a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487a64.md)
- 新版 呼出元 1件 [`00b1f4c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b1f/00b1f4c4.md) · 呼出先 15件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0046d5e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d5e8.md) [`0048796c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048796c.md) [`00487aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487aa4.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 89.10% / 新版 89.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 6件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0046d1ac",
      "incomplete_value": false,
      "site": "0046d1b8",
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
      "definition_site": "0046d16c",
      "incomplete_value": false,
      "site": "0046d178",
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0046d1d0",
      "incomplete_value": true,
      "site": "0046d1d0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a5000:8"
              ],
              [
                "leaf",
                "const:323:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046d190",
      "incomplete_value": true,
      "site": "0046d190",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a5000:8"
              ],
              [
                "leaf",
                "const:37f:8"
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
      "definition_site": "0046d1c8",
      "incomplete_value": true,
      "site": "0046d1d4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0046d188",
      "incomplete_value": true,
      "site": "0046d194",
      "value": [
        "LOAD",
        "8",
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
      "0046d1b8",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "0046d1c0",
      "READ",
      [
        "storage",
        "002a537f",
        null,
        "string"
      ]
    ],
    [
      "0046d1c8",
      "READ",
      [
        "storage",
        "002a5386",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0046d1b8",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "0046d1c0",
      "READ",
      [
        "storage",
        "002a5323",
        null,
        "string"
      ]
    ],
    [
      "0046d1c8",
      "READ",
      [
        "storage",
        "002a532a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046d150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d120.md#insn-0046d150) · [`0046d1d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d120.md#insn-0046d1d4) · [`0046d2b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d120.md#insn-0046d2b4)
- 新版 `0046d190`（命令位置の公開資料なし） · `0046d214`（命令位置の公開資料なし） · `0046d2f4`（命令位置の公開資料なし）

~~~diff
- 0046d150 ["INT_ADD", "register:40f0:8", ["const:46d150:8", "const:4:8"]]
- 0046d150 ["CALL", null, ["callee:0046d4d0:8"]]
+ 0046d190 ["INT_ADD", "register:40f0:8", ["const:46d190:8", "const:4:8"]]
+ 0046d190 ["CALL", null, ["callee:0046d4d0:8"]]
- 0046d150 bytes d0000094
+ 0046d190 bytes d0000094
- 0046d1d4 ["INT_ADD", "register:40f0:8", ["const:46d1d4:8", "const:4:8"]]
- 0046d1d4 ["CALL", null, ["callee:00488598:8"]]
+ 0046d214 ["INT_ADD", "register:40f0:8", ["const:46d214:8", "const:4:8"]]
+ 0046d214 ["CALL", null, ["callee:00488598:8"]]
- 0046d1d4 bytes e16c0094
+ 0046d214 bytes e16c0094
- 0046d2b4 ["INT_ADD", "register:40f0:8", ["const:46d2b4:8", "const:4:8"]]
- 0046d2b4 ["CALL", null, ["callee:00c57f80:8"]]
+ 0046d2f4 ["INT_ADD", "register:40f0:8", ["const:46d2f4:8", "const:4:8"]]
+ 0046d2f4 ["CALL", null, ["callee:00c57f80:8"]]
- 0046d2b4 bytes ffaa1f94
+ 0046d2f4 bytes 23ab1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c2ac85572a050485ce3a8ab281083a4"></a>

### [`0046d4f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d4f0.md) → [`0046d530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d530.md) FUN_0046d530

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fa0.md) [`00c57fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fc0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58070.md) [`00c58080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58080.md) [`00c58090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58090.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 73.91% / 新版 73.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0046d560",
      "incomplete_value": true,
      "site": "0046d568",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046d520",
      "incomplete_value": true,
      "site": "0046d528",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0046d56c",
      "incomplete_value": true,
      "site": "0046d56c",
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
      "definition_site": "0046d52c",
      "incomplete_value": true,
      "site": "0046d52c",
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
      "definition_site": "0046d57c",
      "incomplete_value": true,
      "site": "0046d57c",
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
      "definition_site": "0046d53c",
      "incomplete_value": true,
      "site": "0046d53c",
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
      "0046d54c",
      "READ",
      [
        "storage",
        "00c9abb0",
        null,
        "pointer"
      ]
    ],
    [
      "0046d550",
      "READ",
      [
        "storage",
        "00c9abb8",
        null,
        "pointer"
      ]
    ],
    [
      "0046d55c",
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
      "0046d54c",
      "READ",
      [
        "storage",
        "00c9ac80",
        null,
        "pointer"
      ]
    ],
    [
      "0046d550",
      "READ",
      [
        "storage",
        "00c9ac88",
        null,
        "pointer"
      ]
    ],
    [
      "0046d55c",
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

- 旧版 [`0046d568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d4f0.md#insn-0046d568) · [`0046d50c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d4f0.md#insn-0046d50c) · [`0046d510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d4f0.md#insn-0046d510)
- 新版 `0046d5a8`（命令位置の公開資料なし） · `0046d54c`（命令位置の公開資料なし） · `0046d550`（命令位置の公開資料なし）

~~~diff
- 0046d568 ["INT_ADD", "register:40f0:8", ["const:46d568:8", "const:4:8"]]
- 0046d568 ["CALL", null, ["callee:00c58080:8"]]
+ 0046d5a8 ["INT_ADD", "register:40f0:8", ["const:46d5a8:8", "const:4:8"]]
+ 0046d5a8 ["CALL", null, ["callee:00c58080:8"]]
- 0046d568 bytes 92aa1f94
+ 0046d5a8 bytes b6aa1f94
- 0046d50c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bb0:8"]]
- 0046d50c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0046d54c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c80:8"]]
+ 0046d54c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0046d50c bytes 08d945f9
+ 0046d54c bytes 084146f9
- 0046d510 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:bb8:8"]]
- 0046d510 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
+ 0046d550 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:c88:8"]]
+ 0046d550 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
- 0046d510 bytes d6de45f9
+ 0046d550 bytes d64646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f31fe411f27605d926e927c9cad19890"></a>

### [`0046db00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046db00.md) → [`0046db40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046db40.md) FUN_0046db40

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 15件 [`0046d7c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7c0.md) [`0055fc7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055fc7c.md) [`0055fcd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055f/0055fcd4.md) [`005e8198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e8/005e8198.md) [`00865af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00865/00865af4.md) · 呼出先 2件 [`0046dc30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046dc30.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 15件 [`0046d800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d800.md) [`0055fcbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055fcbc.md) [`0055fd14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0055f/0055fd14.md) [`005e81d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e8/005e81d8.md) [`00865b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00865/00865b4c.md) · 呼出先 2件 [`0046dc70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046dc70.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0046dc18",
      "incomplete_value": true,
      "site": "0046dc30",
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
                "const:730:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046dbd8",
      "incomplete_value": true,
      "site": "0046dbf0",
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
                "const:6f0:8"
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
      "definition_site": "0046dc34",
      "incomplete_value": true,
      "site": "0046dc40",
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
                "const:ba0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046dbf4",
      "incomplete_value": true,
      "site": "0046dc00",
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
                "const:b60:8"
              ]
            ]
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
      "0046dc18",
      "READ",
      [
        "storage",
        "002c26f0",
        null,
        null
      ]
    ],
    [
      "0046dc34",
      "READ",
      [
        "storage",
        "002c2b60",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0046dc18",
      "READ",
      [
        "storage",
        "002c2730",
        null,
        null
      ]
    ],
    [
      "0046dc34",
      "READ",
      [
        "storage",
        "002c2ba0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046dbb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046db00.md#insn-0046dbb4) · [`0046dbd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046db00.md#insn-0046dbd8) · [`0046dbf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046db00.md#insn-0046dbf4)
- 新版 `0046dbf4`（命令位置の公開資料なし） · `0046dc18`（命令位置の公開資料なし） · `0046dc34`（命令位置の公開資料なし）

~~~diff
- 0046dbb4 ["INT_ADD", "register:40f0:8", ["const:46dbb4:8", "const:4:8"]]
- 0046dbb4 ["CALL", null, ["callee:0046dc70:8"]]
+ 0046dbf4 ["INT_ADD", "register:40f0:8", ["const:46dbf4:8", "const:4:8"]]
+ 0046dbf4 ["CALL", null, ["callee:0046dc70:8"]]
- 0046dbb4 bytes 1f000094
+ 0046dbf4 bytes 1f000094
- 0046dbd8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:6f0:8"]]
- 0046dbd8 ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
- 0046dbd8 ["COPY", "register:5030:8", ["const:0:8"]]
- 0046dbd8 ["COPY", "register:5038:8", ["const:0:8"]]
+ 0046dc18 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:730:8"]]
+ 0046dc18 ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
+ 0046dc18 ["COPY", "register:5030:8", ["const:0:8"]]
+ 0046dc18 ["COPY", "register:5038:8", ["const:0:8"]]
- 0046dbd8 bytes 21bdc13d
+ 0046dc18 bytes 21cdc13d
- 0046dbf4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b60:8"]]
- 0046dbf4 ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
- 0046dbf4 ["COPY", "register:5030:8", ["const:0:8"]]
- 0046dbf4 ["COPY", "register:5038:8", ["const:0:8"]]
+ 0046dc34 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ba0:8"]]
+ 0046dc34 ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
+ 0046dc34 ["COPY", "register:5030:8", ["const:0:8"]]
+ 0046dc34 ["COPY", "register:5038:8", ["const:0:8"]]
- 0046dbf4 bytes 01d9c23d
+ 0046dc34 bytes 01e9c23d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6579fef5914daa5be32dc385be0e8a5"></a>

### [`0046e7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e7c4.md) → [`0046e804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e804.md) FUN_0046e804

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 25件 [`005df6d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005df/005df6d0.md) [`005e4f74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e4/005e4f74.md) [`00682464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00682/00682464.md) [`0078c21c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078c/0078c21c.md) [`007bbe1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bb/007bbe1c.md) · 呼出先 1件 [`00c58190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58190.md)
- 新版 呼出元 25件 [`005df710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005df/005df710.md) [`005e4fb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e4/005e4fb4.md) [`006824a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00682/006824a4.md) [`0078c274`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078c/0078c274.md) [`007bbe74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bb/007bbe74.md) · 呼出先 1件 [`00c58260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58260.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0046e830",
      "incomplete_value": false,
      "site": "0046e838",
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
      "definition_site": "0046e7f0",
      "incomplete_value": false,
      "site": "0046e7f8",
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
      "0046e830",
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
      "0046e830",
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

- 旧版 [`0046e7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e7c4.md#insn-0046e7f8) · [`0046e7f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e7c4.md#insn-0046e7f0)
- 新版 `0046e838`（命令位置の公開資料なし） · `0046e830`（命令位置の公開資料なし）

~~~diff
- 0046e7f8 ["INT_ADD", "register:40f0:8", ["const:46e7f8:8", "const:4:8"]]
- 0046e7f8 ["CALL", null, ["callee:00c58260:8"]]
+ 0046e838 ["INT_ADD", "register:40f0:8", ["const:46e838:8", "const:4:8"]]
+ 0046e838 ["CALL", null, ["callee:00c58260:8"]]
- 0046e7f8 bytes 66a61f94
+ 0046e838 bytes 8aa61f94
- 0046e7f0 ["COPY", "tmp:0:8", ["const:3ea:8"]]
- 0046e7f0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0046e7f0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0046e7f0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0046e830 ["COPY", "tmp:0:8", ["const:38e:8"]]
+ 0046e830 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0046e830 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0046e830 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0046e7f0 bytes 21a80f91
+ 0046e830 bytes 21380e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2728a0d92202248d547d0ff3e45d0f5"></a>

### [`0046e8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e8a4.md) → [`0046e8e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e8e4.md) FUN_0046e8e4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 38件 [`005df778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005df/005df778.md) [`005e50b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e5/005e50b8.md) [`00682218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00682/00682218.md) [`0078ddcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078d/0078ddcc.md) [`0078de54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078d/0078de54.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58190.md)
- 新版 呼出元 38件 [`005df7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005df/005df7b8.md) [`005e50f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e5/005e50f8.md) [`00682258`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00682/00682258.md) [`0078de24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078d/0078de24.md) [`0078deac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078d/0078deac.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58260.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.00% / 新版 98.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0046e92c",
      "incomplete_value": false,
      "site": "0046e934",
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
      "definition_site": "0046e8ec",
      "incomplete_value": false,
      "site": "0046e8f4",
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
      "0046e92c",
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
      "0046e92c",
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

- 旧版 [`0046e8f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e8a4.md#insn-0046e8f4) · [`0046e8d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e8a4.md#insn-0046e8d8) · [`0046e8ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e8a4.md#insn-0046e8ec)
- 新版 `0046e934`（命令位置の公開資料なし） · `0046e918`（命令位置の公開資料なし） · `0046e92c`（命令位置の公開資料なし）

~~~diff
- 0046e8f4 ["INT_ADD", "register:40f0:8", ["const:46e8f4:8", "const:4:8"]]
- 0046e8f4 ["CALL", null, ["callee:00c58260:8"]]
+ 0046e934 ["INT_ADD", "register:40f0:8", ["const:46e934:8", "const:4:8"]]
+ 0046e934 ["CALL", null, ["callee:00c58260:8"]]
- 0046e8f4 bytes 27a61f94
+ 0046e934 bytes 4ba61f94
- 0046e8d8 ["INT_ADD", "register:40f0:8", ["const:46e8d8:8", "const:4:8"]]
- 0046e8d8 ["CALL", null, ["callee:00c57f80:8"]]
+ 0046e918 ["INT_ADD", "register:40f0:8", ["const:46e918:8", "const:4:8"]]
+ 0046e918 ["CALL", null, ["callee:00c57f80:8"]]
- 0046e8d8 bytes 76a51f94
+ 0046e918 bytes 9aa51f94
- 0046e8ec ["COPY", "tmp:0:8", ["const:3ea:8"]]
- 0046e8ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0046e8ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0046e8ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0046e92c ["COPY", "tmp:0:8", ["const:38e:8"]]
+ 0046e92c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0046e92c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0046e92c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0046e8ec bytes 21a80f91
+ 0046e92c bytes 21380e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0548a39af433b2798b28405c862fd206"></a>

### [`0046e970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e970.md) → [`0046e9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e9b0.md) FUN_0046e9b0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 36件 [`005e1bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e1bb8.md) [`005e3114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e3/005e3114.md) [`005e94f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e9/005e94f4.md) [`006312f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00631/006312f4.md) [`0063a7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063a/0063a7a4.md) · 呼出先 15件 [`00470164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470164.md) [`00470368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470368.md) [`0048791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048791c.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md)
- 新版 呼出元 36件 [`005e1bf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e1/005e1bf8.md) [`005e3154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e3/005e3154.md) [`005e9534`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e9/005e9534.md) [`00631334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00631/00631334.md) [`0063a7e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063a/0063a7e4.md) · 呼出先 15件 [`004701a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/004701a4.md) [`004703a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/004703a8.md) [`0048795c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048795c.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`00487e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 95.20% / 新版 95.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0046e9f4",
      "incomplete_value": false,
      "site": "0046e9f8",
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
      "definition_site": "0046e9b4",
      "incomplete_value": false,
      "site": "0046e9b8",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0046ecec",
      "incomplete_value": true,
      "site": "0046ecf0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046ecac",
      "incomplete_value": true,
      "site": "0046ecb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0046ece8",
      "incomplete_value": true,
      "site": "0046ecf4",
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
      "definition_site": "0046eca8",
      "incomplete_value": true,
      "site": "0046ecb4",
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
      "0046e9f8",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "0046ea10",
      "PARAM",
      [
        "storage",
        "002a63ea",
        null,
        "undefined1"
      ]
    ],
    [
      "0046ecdc",
      "READ",
      [
        "storage",
        "00c9abb0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0046e9f8",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "0046ea10",
      "PARAM",
      [
        "storage",
        "002a638e",
        null,
        "undefined1"
      ]
    ],
    [
      "0046ecdc",
      "READ",
      [
        "storage",
        "00c9ac80",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046e9d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e970.md#insn-0046e9d8) · [`0046e9f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e970.md#insn-0046e9f8) · [`0046ea18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e970.md#insn-0046ea18)
- 新版 `0046ea18`（命令位置の公開資料なし） · `0046ea38`（命令位置の公開資料なし） · `0046ea58`（命令位置の公開資料なし）

~~~diff
- 0046e9d8 ["INT_ADD", "register:40f0:8", ["const:46e9d8:8", "const:4:8"]]
- 0046e9d8 ["CALL", null, ["callee:00c58260:8"]]
+ 0046ea18 ["INT_ADD", "register:40f0:8", ["const:46ea18:8", "const:4:8"]]
+ 0046ea18 ["CALL", null, ["callee:00c58260:8"]]
- 0046e9d8 bytes eea51f94
+ 0046ea18 bytes 12a61f94
- 0046e9f8 ["INT_ADD", "register:40f0:8", ["const:46e9f8:8", "const:4:8"]]
- 0046e9f8 ["CALL", null, ["callee:00b11188:8"]]
+ 0046ea38 ["INT_ADD", "register:40f0:8", ["const:46ea38:8", "const:4:8"]]
+ 0046ea38 ["CALL", null, ["callee:00b11188:8"]]
- 0046e9f8 bytes bd891a94
+ 0046ea38 bytes d4891a94
- 0046ea18 ["INT_ADD", "register:40f0:8", ["const:46ea18:8", "const:4:8"]]
- 0046ea18 ["CALL", null, ["callee:0048795c:8"]]
+ 0046ea58 ["INT_ADD", "register:40f0:8", ["const:46ea58:8", "const:4:8"]]
+ 0046ea58 ["CALL", null, ["callee:0048795c:8"]]
- 0046ea18 bytes c1630094
+ 0046ea58 bytes c1630094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90dbc94e1dc23a557e4c6bcd26986471"></a>

### [`0046eef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046eef8.md) → [`0046ef38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046ef38.md) FUN_0046ef38

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 26件 [`005f0e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f0/005f0e54.md) [`0067e3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067e/0067e3b0.md) [`0070e004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070e004.md) [`0078c21c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078c/0078c21c.md) [`007b0a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b0a18.md) · 呼出先 1件 [`00c58190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58190.md)
- 新版 呼出元 26件 [`005f0e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005f0/005f0e94.md) [`0067e3f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0067e/0067e3f0.md) [`0070e05c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e05c.md) [`0078c274`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078c/0078c274.md) [`007b0a70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007b0/007b0a70.md) · 呼出先 1件 [`00c58260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58260.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0046ef78",
      "incomplete_value": false,
      "site": "0046ef80",
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
      "definition_site": "0046ef38",
      "incomplete_value": false,
      "site": "0046ef40",
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
      "0046ef78",
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
      "0046ef78",
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

- 旧版 [`0046ef40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046eef8.md#insn-0046ef40) · [`0046ef38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046eef8.md#insn-0046ef38)
- 新版 `0046ef80`（命令位置の公開資料なし） · `0046ef78`（命令位置の公開資料なし）

~~~diff
- 0046ef40 ["INT_ADD", "register:40f0:8", ["const:46ef40:8", "const:4:8"]]
- 0046ef40 ["CALL", null, ["callee:00c58260:8"]]
+ 0046ef80 ["INT_ADD", "register:40f0:8", ["const:46ef80:8", "const:4:8"]]
+ 0046ef80 ["CALL", null, ["callee:00c58260:8"]]
- 0046ef40 bytes 94a41f94
+ 0046ef80 bytes b8a41f94
- 0046ef38 ["COPY", "tmp:0:8", ["const:3ea:8"]]
- 0046ef38 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0046ef38 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0046ef38 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0046ef78 ["COPY", "tmp:0:8", ["const:38e:8"]]
+ 0046ef78 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0046ef78 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0046ef78 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0046ef38 bytes 21a80f91
+ 0046ef78 bytes 21380e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4016f36bf5125129bbb99537ea7d903"></a>

### [`0046efdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046efdc.md) → [`0046f01c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046f/0046f01c.md) FUN_0046f01c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 31件 [`005f0efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f0/005f0efc.md) [`0067e50c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067e/0067e50c.md) [`00681ff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00681/00681ff8.md) [`0070e148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070e148.md) [`0078ddcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078d/0078ddcc.md) · 呼出先 4件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58190`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58190.md)
- 新版 呼出元 31件 [`005f0f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005f0/005f0f3c.md) [`0067e54c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0067e/0067e54c.md) [`00682038`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00682/00682038.md) [`0070e1a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070e1a0.md) [`0078de24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078d/0078de24.md) · 呼出先 4件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58260.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.11% / 新版 98.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0046f050",
      "incomplete_value": false,
      "site": "0046f058",
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
      "definition_site": "0046f010",
      "incomplete_value": false,
      "site": "0046f018",
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
      "0046f050",
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
      "0046f050",
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

- 旧版 [`0046f018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046efdc.md#insn-0046f018) · [`0046f058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046efdc.md#insn-0046f058) · [`0046f010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046efdc.md#insn-0046f010)
- 新版 `0046f058`（命令位置の公開資料なし） · `0046f098`（命令位置の公開資料なし） · `0046f050`（命令位置の公開資料なし）

~~~diff
- 0046f018 ["INT_ADD", "register:40f0:8", ["const:46f018:8", "const:4:8"]]
- 0046f018 ["CALL", null, ["callee:00c58260:8"]]
+ 0046f058 ["INT_ADD", "register:40f0:8", ["const:46f058:8", "const:4:8"]]
+ 0046f058 ["CALL", null, ["callee:00c58260:8"]]
- 0046f018 bytes 5ea41f94
+ 0046f058 bytes 82a41f94
- 0046f058 ["INT_ADD", "register:40f0:8", ["const:46f058:8", "const:4:8"]]
- 0046f058 ["CALL", null, ["callee:00c57f80:8"]]
+ 0046f098 ["INT_ADD", "register:40f0:8", ["const:46f098:8", "const:4:8"]]
+ 0046f098 ["CALL", null, ["callee:00c57f80:8"]]
- 0046f058 bytes 96a31f94
+ 0046f098 bytes baa31f94
- 0046f010 ["COPY", "tmp:0:8", ["const:3ea:8"]]
- 0046f010 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0046f010 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0046f010 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0046f050 ["COPY", "tmp:0:8", ["const:38e:8"]]
+ 0046f050 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0046f050 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0046f050 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0046f010 bytes 21a80f91
+ 0046f050 bytes 21380e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1488b51fa0187a57ed4ae7a52bbf0778"></a>

### [`0046f0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f0b4.md) → [`0046f0f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046f/0046f0f4.md) FUN_0046f0f4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 36件 [`005e1bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e1bb8.md) [`005e3114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e3/005e3114.md) [`005e94f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e9/005e94f4.md) [`006312f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00631/006312f4.md) [`0063a7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063a/0063a7a4.md) · 呼出先 16件 [`004704a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/004704a8.md) [`00470714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470714.md) [`00470854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470854.md) [`0048791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048791c.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md)
- 新版 呼出元 36件 [`005e1bf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e1/005e1bf8.md) [`005e3154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e3/005e3154.md) [`005e9534`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e9/005e9534.md) [`00631334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00631/00631334.md) [`0063a7e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0063a/0063a7e4.md) · 呼出先 16件 [`004704e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/004704e8.md) [`00470754`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470754.md) [`00470894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470894.md) [`0048795c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048795c.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 96.60% / 新版 96.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `store_value` 4件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0046f134",
      "incomplete_value": false,
      "site": "0046f13c",
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
      "definition_site": "0046f0f4",
      "incomplete_value": false,
      "site": "0046f0fc",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0046f4b4",
      "incomplete_value": true,
      "site": "0046f4c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:438:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046f474",
      "incomplete_value": true,
      "site": "0046f480",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 43,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0046f5cc",
      "incomplete_value": true,
      "site": "0046f5d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046f58c",
      "incomplete_value": true,
      "site": "0046f590",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 53,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0046f13c",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "0046f170",
      "PARAM",
      [
        "storage",
        "002a63ea",
        null,
        "undefined1"
      ]
    ],
    [
      "0046f4b4",
      "READ",
      [
        "storage",
        "002c43f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0046f13c",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "0046f170",
      "PARAM",
      [
        "storage",
        "002a638e",
        null,
        "undefined1"
      ]
    ],
    [
      "0046f4b4",
      "READ",
      [
        "storage",
        "002c4438",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046f138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f0b4.md#insn-0046f138) · [`0046f440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f0b4.md#insn-0046f440) · [`0046f5d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f0b4.md#insn-0046f5d4)
- 新版 `0046f178`（命令位置の公開資料なし） · `0046f480`（命令位置の公開資料なし） · `0046f614`（命令位置の公開資料なし）

~~~diff
- 0046f138 ["INT_ADD", "register:40f0:8", ["const:46f138:8", "const:4:8"]]
- 0046f138 ["CALL", null, ["callee:00c58260:8"]]
+ 0046f178 ["INT_ADD", "register:40f0:8", ["const:46f178:8", "const:4:8"]]
+ 0046f178 ["CALL", null, ["callee:00c58260:8"]]
- 0046f138 bytes 16a41f94
+ 0046f178 bytes 3aa41f94
- 0046f440 ["INT_ADD", "register:40f0:8", ["const:46f440:8", "const:4:8"]]
- 0046f440 ["CALL", null, ["callee:0048797c:8"]]
+ 0046f480 ["INT_ADD", "register:40f0:8", ["const:46f480:8", "const:4:8"]]
+ 0046f480 ["CALL", null, ["callee:0048797c:8"]]
- 0046f440 bytes 3f610094
+ 0046f480 bytes 3f610094
- 0046f5d4 ["INT_ADD", "register:40f0:8", ["const:46f5d4:8", "const:4:8"]]
- 0046f5d4 ["CALL", null, ["callee:00c58080:8"]]
+ 0046f614 ["INT_ADD", "register:40f0:8", ["const:46f614:8", "const:4:8"]]
+ 0046f614 ["CALL", null, ["callee:00c58080:8"]]
- 0046f5d4 bytes 77a21f94
+ 0046f614 bytes 9ba21f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-744bb143fb431201247cd11f7d763332"></a>

### [`00470354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470354.md) → [`00470394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470394.md) FUN_00470394

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`00470164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470164.md) [`007bbe1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bb/007bbe1c.md) [`007f1ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1ab8.md) [`008ff8cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ff/008ff8cc.md) [`00a3f34c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3f/00a3f34c.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 5件 [`004701a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/004701a4.md) [`007bbe74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007bb/007bbe74.md) [`007f1b10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f1/007f1b10.md) [`008ff920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ff/008ff920.md) [`00a3f3a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a3f/00a3f3a0.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "004703a0",
      "incomplete_value": false,
      "site": "004703a4",
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
      "definition_site": "00470360",
      "incomplete_value": false,
      "site": "00470364",
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
      "004703a0",
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
      "004703a0",
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

- 旧版 [`00470364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470354.md#insn-00470364) · [`00470360`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470354.md#insn-00470360)
- 新版 `004703a4`（命令位置の公開資料なし） · `004703a0`（命令位置の公開資料なし）

~~~diff
- 00470364 ["INT_ADD", "register:40f0:8", ["const:470364:8", "const:4:8"]]
- 00470364 ["CALL", null, ["callee:0043b7b8:8"]]
+ 004703a4 ["INT_ADD", "register:40f0:8", ["const:4703a4:8", "const:4:8"]]
+ 004703a4 ["CALL", null, ["callee:0043b7b8:8"]]
- 00470364 bytes 052dff97
+ 004703a4 bytes 052dff97
- 00470360 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00470360 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00470360 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00470360 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004703a0 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 004703a0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004703a0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004703a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00470360 bytes 00303d91
+ 004703a0 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7398a524e0bbbab8d3841fcf4089b9b"></a>

### [`00470494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470494.md) → [`004704d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/004704d4.md) FUN_004704d4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00470368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470368.md) [`007f1cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f1/007f1cb0.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 2件 [`004703a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/004703a8.md) [`007f1d08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007f1/007f1d08.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "004704e0",
      "incomplete_value": false,
      "site": "004704e4",
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
      "definition_site": "004704a0",
      "incomplete_value": false,
      "site": "004704a4",
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
      "004704e0",
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
      "004704e0",
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

- 旧版 [`004704a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470494.md#insn-004704a4) · [`004704a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470494.md#insn-004704a0)
- 新版 `004704e4`（命令位置の公開資料なし） · `004704e0`（命令位置の公開資料なし）

~~~diff
- 004704a4 ["INT_ADD", "register:40f0:8", ["const:4704a4:8", "const:4:8"]]
- 004704a4 ["CALL", null, ["callee:0043b7b8:8"]]
+ 004704e4 ["INT_ADD", "register:40f0:8", ["const:4704e4:8", "const:4:8"]]
+ 004704e4 ["CALL", null, ["callee:0043b7b8:8"]]
- 004704a4 bytes b52cff97
+ 004704e4 bytes b52cff97
- 004704a0 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 004704a0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004704a0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004704a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004704e0 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 004704e0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004704e0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004704e0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004704a0 bytes 00303d91
+ 004704e0 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27d4d7908823da1cfba504ea11dadbb2"></a>

### [`004704a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/004704a8.md) → [`004704e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/004704e8.md) FUN_004704e8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0046f0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f0b4.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`004675e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/004675e8.md) [`00470700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470700.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0046f0f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046f/0046f0f4.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00467628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467628.md) [`00470740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470740.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.55% / 新版 98.55%

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
      "site": "004705e4",
      "value": [
        "leaf",
        "ram:467628:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004705a4",
      "value": [
        "leaf",
        "ram:4675e8:8"
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
      "site": "0047066c",
      "value": [
        "leaf",
        "ram:467628:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0047062c",
      "value": [
        "leaf",
        "ram:4675e8:8"
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
      "004705e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "004675e8"
      ]
    ],
    [
      "0047066c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "004675e8"
      ]
    ]
  ],
  "added": [
    [
      "004705e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00467628"
      ]
    ],
    [
      "0047066c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00467628"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004705a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/004704a8.md#insn-004705a4) · [`0047062c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/004704a8.md#insn-0047062c) · [`00470560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/004704a8.md#insn-00470560)
- 新版 `004705e4`（命令位置の公開資料なし） · `0047066c`（命令位置の公開資料なし） · `004705a0`（命令位置の公開資料なし）

~~~diff
- 004705a4 ["INT_ADD", "register:40f0:8", ["const:4705a4:8", "const:4:8"]]
- 004705a4 ["CALL", null, ["ram:4675e8:8"]]
+ 004705e4 ["INT_ADD", "register:40f0:8", ["const:4705e4:8", "const:4:8"]]
+ 004705e4 ["CALL", null, ["ram:467628:8"]]
- 004705a4 bytes 11dcff97
+ 004705e4 bytes 11dcff97
- 0047062c ["INT_ADD", "register:40f0:8", ["const:47062c:8", "const:4:8"]]
- 0047062c ["CALL", null, ["ram:4675e8:8"]]
+ 0047066c ["INT_ADD", "register:40f0:8", ["const:47066c:8", "const:4:8"]]
+ 0047066c ["CALL", null, ["ram:467628:8"]]
- 0047062c bytes efdbff97
+ 0047066c bytes efdbff97
- 00470560 ["INT_ADD", "register:40f0:8", ["const:470560:8", "const:4:8"]]
- 00470560 ["CALL", null, ["callee:00c57f60:8"]]
+ 004705a0 ["INT_ADD", "register:40f0:8", ["const:4705a0:8", "const:4:8"]]
+ 004705a0 ["CALL", null, ["callee:00c57f60:8"]]
- 00470560 bytes 4c9e1f94
+ 004705a0 bytes 709e1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30a7daccb78be66c80593d2c73cc86a8"></a>

### [`00470700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470700.md) → [`00470740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470740.md) FUN_00470740

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004704a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/004704a8.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 1件 [`004704e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/004704e8.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "0047074c",
      "incomplete_value": false,
      "site": "00470750",
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
      "definition_site": "0047070c",
      "incomplete_value": false,
      "site": "00470710",
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
      "0047074c",
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
      "0047074c",
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

- 旧版 [`00470710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470700.md#insn-00470710) · [`0047070c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470700.md#insn-0047070c)
- 新版 `00470750`（命令位置の公開資料なし） · `0047074c`（命令位置の公開資料なし）

~~~diff
- 00470710 ["INT_ADD", "register:40f0:8", ["const:470710:8", "const:4:8"]]
- 00470710 ["CALL", null, ["callee:0043b7b8:8"]]
+ 00470750 ["INT_ADD", "register:40f0:8", ["const:470750:8", "const:4:8"]]
+ 00470750 ["CALL", null, ["callee:0043b7b8:8"]]
- 00470710 bytes 1a2cff97
+ 00470750 bytes 1a2cff97
- 0047070c ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 0047070c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0047070c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0047070c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0047074c ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 0047074c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0047074c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0047074c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0047070c bytes 00303d91
+ 0047074c bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-123ae1d6603cb44c2e2faf3d4cabd7fe"></a>

### [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) → [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) FUN_00470880

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 262件 [`0046f75c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f75c.md) [`00470714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470714.md) [`00470994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470994.md) [`0047af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047af10.md) [`0049e4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049e/0049e4c4.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 262件 [`0046f79c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046f/0046f79c.md) [`00470754`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470754.md) [`004709d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/004709d4.md) [`0047af50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047af50.md) [`0049e504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049e504.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "0047088c",
      "incomplete_value": false,
      "site": "00470890",
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
      "definition_site": "0047084c",
      "incomplete_value": false,
      "site": "00470850",
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
      "0047088c",
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
      "0047088c",
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

- 旧版 [`00470850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md#insn-00470850) · [`0047084c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md#insn-0047084c)
- 新版 `00470890`（命令位置の公開資料なし） · `0047088c`（命令位置の公開資料なし）

~~~diff
- 00470850 ["INT_ADD", "register:40f0:8", ["const:470850:8", "const:4:8"]]
- 00470850 ["CALL", null, ["callee:0043b7b8:8"]]
+ 00470890 ["INT_ADD", "register:40f0:8", ["const:470890:8", "const:4:8"]]
+ 00470890 ["CALL", null, ["callee:0043b7b8:8"]]
- 00470850 bytes ca2bff97
+ 00470890 bytes ca2bff97
- 0047084c ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 0047084c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0047084c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0047084c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0047088c ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 0047088c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0047088c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0047088c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0047084c bytes 00303d91
+ 0047088c bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-560e6d6d142d8bb31ae03ab6bd6f737d"></a>

### [`00470980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470980.md) → [`004709c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/004709c0.md) FUN_004709c0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00470854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470854.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 1件 [`00470894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470894.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "004709cc",
      "incomplete_value": false,
      "site": "004709d0",
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
      "definition_site": "0047098c",
      "incomplete_value": false,
      "site": "00470990",
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
      "004709cc",
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
      "004709cc",
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

- 旧版 [`00470990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470980.md#insn-00470990) · [`0047098c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470980.md#insn-0047098c)
- 新版 `004709d0`（命令位置の公開資料なし） · `004709cc`（命令位置の公開資料なし）

~~~diff
- 00470990 ["INT_ADD", "register:40f0:8", ["const:470990:8", "const:4:8"]]
- 00470990 ["CALL", null, ["callee:0043b7b8:8"]]
+ 004709d0 ["INT_ADD", "register:40f0:8", ["const:4709d0:8", "const:4:8"]]
+ 004709d0 ["CALL", null, ["callee:0043b7b8:8"]]
- 00470990 bytes 7a2bff97
+ 004709d0 bytes 7a2bff97
- 0047098c ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 0047098c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0047098c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0047098c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004709cc ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 004709cc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004709cc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004709cc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0047098c bytes 00303d91
+ 004709cc bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5e48842b9853a9e4b3b06ae37458f21"></a>

### [`00470ac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470ac4.md) → [`00470b04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470b04.md) _INIT_14

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
      "definition_site": "00470b40",
      "incomplete_value": true,
      "site": "00470b5c",
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
      "definition_site": "00470b00",
      "incomplete_value": true,
      "site": "00470b1c",
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
      "definition_site": "00470b64",
      "incomplete_value": true,
      "site": "00470b80",
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
      "definition_site": "00470b24",
      "incomplete_value": true,
      "site": "00470b40",
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
      "definition_site": "00470b84",
      "incomplete_value": true,
      "site": "00470ba0",
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
      "definition_site": "00470b44",
      "incomplete_value": true,
      "site": "00470b60",
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
      "00470b40",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00470b64",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00470b84",
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
      "00470b40",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "00470b64",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "00470b84",
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

- 旧版 [`00470b3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470ac4.md#insn-00470b3c) · [`00470b5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470ac4.md#insn-00470b5c) · [`00470c24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470ac4.md#insn-00470c24)
- 新版 `00470b7c`（命令位置の公開資料なし） · `00470b9c`（命令位置の公開資料なし） · `00470c64`（命令位置の公開資料なし）

~~~diff
- 00470b3c ["COPY", "tmp:0:8", ["const:dc2:8"]]
- 00470b3c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00470b3c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00470b3c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00470b7c ["COPY", "tmp:0:8", ["const:d6e:8"]]
+ 00470b7c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00470b7c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00470b7c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00470b3c bytes 4a093791
+ 00470b7c bytes 4ab93591
- 00470b5c ["COPY", "tmp:0:8", ["const:f62:8"]]
- 00470b5c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00470b5c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00470b5c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00470b9c ["COPY", "tmp:0:8", ["const:f15:8"]]
+ 00470b9c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00470b9c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00470b9c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00470b5c bytes 4a893d91
+ 00470b9c bytes 4a553c91
- 00470c24 ["INT_ADD", "register:40f0:8", ["const:470c24:8", "const:4:8"]]
- 00470c24 ["CALL", null, ["callee:0043b838:8"]]
+ 00470c64 ["INT_ADD", "register:40f0:8", ["const:470c64:8", "const:4:8"]]
+ 00470c64 ["CALL", null, ["callee:0043b838:8"]]
- 00470c24 bytes f52aff97
+ 00470c64 bytes f52aff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d6662d1497eafc3b20ce610d8b87714"></a>

### [`00470f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470f34.md) → [`00470f74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470f74.md) FUN_00470f74

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00851a0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851a0c.md) [`00876f04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00876/00876f04.md) [`00b11c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b11/00b11c80.md) · 呼出先 32件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043dba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dba4.md) [`00471d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471d1c.md) [`00471fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471fb4.md) [`004720b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/004720b8.md)
- 新版 呼出元 3件 [`00851a64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851a64.md) [`00876f5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00876/00876f5c.md) [`00b11d1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b11/00b11d1c.md) · 呼出先 32件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043dbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043dbe4.md) [`00471d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00471/00471d5c.md) [`00471ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00471/00471ff4.md) [`004720f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00472/004720f8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 97.28% / 新版 97.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 1件, `store_value` 3件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0047137c",
      "incomplete_value": true,
      "site": "00471380",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047133c",
      "incomplete_value": true,
      "site": "00471340",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 32,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00471378",
      "incomplete_value": true,
      "site": "00471384",
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
      "definition_site": "00471338",
      "incomplete_value": true,
      "site": "00471344",
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
    "ordinal": 33,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00471390",
      "incomplete_value": true,
      "site": "00471390",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
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
      "definition_site": "00471350",
      "incomplete_value": true,
      "site": "00471350",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
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
    "ordinal": 34,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004712bc",
      "PARAM",
      [
        "storage",
        "002c86f5",
        null,
        null
      ]
    ],
    [
      "0047136c",
      "READ",
      [
        "storage",
        "00c9abb0",
        null,
        "pointer"
      ]
    ],
    [
      "00471370",
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
      "004712bc",
      "PARAM",
      [
        "storage",
        "002c8735",
        null,
        null
      ]
    ],
    [
      "0047136c",
      "READ",
      [
        "storage",
        "00c9ac80",
        null,
        "pointer"
      ]
    ],
    [
      "00471370",
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

- 旧版 [`00471280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470f34.md#insn-00471280) · [`00471384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470f34.md#insn-00471384) · [`00471400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470f34.md#insn-00471400)
- 新版 `004712c0`（命令位置の公開資料なし） · `004713c4`（命令位置の公開資料なし） · `00471440`（命令位置の公開資料なし）

~~~diff
- 00471280 ["INT_ADD", "register:40f0:8", ["const:471280:8", "const:4:8"]]
- 00471280 ["CALL", null, ["callee:00471d5c:8"]]
+ 004712c0 ["INT_ADD", "register:40f0:8", ["const:4712c0:8", "const:4:8"]]
+ 004712c0 ["CALL", null, ["callee:00471d5c:8"]]
- 00471280 bytes a7020094
+ 004712c0 bytes a7020094
- 00471384 ["INT_ADD", "register:40f0:8", ["const:471384:8", "const:4:8"]]
- 00471384 ["CALL", null, ["callee:00c58080:8"]]
+ 004713c4 ["INT_ADD", "register:40f0:8", ["const:4713c4:8", "const:4:8"]]
+ 004713c4 ["CALL", null, ["callee:00c58080:8"]]
- 00471384 bytes 0b9b1f94
+ 004713c4 bytes 2f9b1f94
- 00471400 ["INT_ADD", "register:40f0:8", ["const:471400:8", "const:4:8"]]
- 00471400 ["CALL", null, ["callee:00550be4:8"]]
+ 00471440 ["INT_ADD", "register:40f0:8", ["const:471440:8", "const:4:8"]]
+ 00471440 ["CALL", null, ["callee:00550be4:8"]]
- 00471400 bytes e97d0394
+ 00471440 bytes e97d0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-213d40f998e9dc0bcdfd7f76b3a825b1"></a>

### [`00471930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471930.md) → [`00471970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00471/00471970.md) FUN_00471970

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`004847c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00484/004847c0.md) [`00488790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488790.md) [`0048969c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/0048969c.md) [`00b110ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b11/00b110ec.md) · 呼出先 14件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043dba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dba4.md) [`00471fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471fb4.md) [`004720b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/004720b8.md) [`00472364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472364.md)
- 新版 呼出元 4件 [`00484800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00484/00484800.md) [`004887d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/004887d0.md) [`004896dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/004896dc.md) [`00b11188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b11/00b11188.md) · 呼出先 14件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043dbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043dbe4.md) [`00471ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00471/00471ff4.md) [`004720f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00472/004720f8.md) [`004723a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00472/004723a4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.32% / 新版 99.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00471abc",
      "incomplete_value": false,
      "site": "00471ad0",
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
      "definition_site": "00471a7c",
      "incomplete_value": false,
      "site": "00471a90",
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
      "00471abc",
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
      "00471abc",
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

- 旧版 [`00471a90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471930.md#insn-00471a90) · [`00471ad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471930.md#insn-00471ad0) · [`00471968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471930.md#insn-00471968)
- 新版 `00471ad0`（命令位置の公開資料なし） · `00471b10`（命令位置の公開資料なし） · `004719a8`（命令位置の公開資料なし）

~~~diff
- 00471a90 ["INT_ADD", "register:40f0:8", ["const:471a90:8", "const:4:8"]]
- 00471a90 ["CALL", null, ["callee:004720f8:8"]]
+ 00471ad0 ["INT_ADD", "register:40f0:8", ["const:471ad0:8", "const:4:8"]]
+ 00471ad0 ["CALL", null, ["callee:004720f8:8"]]
- 00471a90 bytes 8a010094
+ 00471ad0 bytes 8a010094
- 00471ad0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00471ad0 ["INT_ADD", "register:40f0:8", ["const:471ad0:8", "const:4:8"]]
- 00471ad0 ["CALLIND", null, ["register:0:8"]]
+ 00471b10 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00471b10 ["INT_ADD", "register:40f0:8", ["const:471b10:8", "const:4:8"]]
+ 00471b10 ["CALLIND", null, ["register:0:8"]]
- 00471ad0 bytes 00013fd6
+ 00471b10 bytes 00013fd6
- 00471968 ["INT_ADD", "register:40f0:8", ["const:471968:8", "const:4:8"]]
- 00471968 ["CALL", null, ["callee:00c581b0:8"]]
+ 004719a8 ["INT_ADD", "register:40f0:8", ["const:4719a8:8", "const:4:8"]]
+ 004719a8 ["CALL", null, ["callee:00c581b0:8"]]
- 00471968 bytes de991f94
+ 004719a8 bytes 029a1f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6959b2a11ef1229b3e5fe5f7186a8bc7"></a>

### [`00472670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472670.md) → [`004726b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00472/004726b0.md) _INIT_15

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
      "definition_site": "004726ec",
      "incomplete_value": true,
      "site": "00472708",
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
      "definition_site": "004726ac",
      "incomplete_value": true,
      "site": "004726c8",
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
      "definition_site": "00472710",
      "incomplete_value": true,
      "site": "0047272c",
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
      "definition_site": "004726d0",
      "incomplete_value": true,
      "site": "004726ec",
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
      "definition_site": "00472730",
      "incomplete_value": true,
      "site": "0047274c",
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
      "definition_site": "004726f0",
      "incomplete_value": true,
      "site": "0047270c",
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
      "004726ec",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00472710",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00472730",
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
      "004726ec",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "00472710",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "00472730",
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

- 旧版 [`004726e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472670.md#insn-004726e8) · [`00472708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472670.md#insn-00472708) · [`004727d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472670.md#insn-004727d0)
- 新版 `00472728`（命令位置の公開資料なし） · `00472748`（命令位置の公開資料なし） · `00472810`（命令位置の公開資料なし）

~~~diff
- 004726e8 ["COPY", "tmp:0:8", ["const:dc2:8"]]
- 004726e8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004726e8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004726e8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00472728 ["COPY", "tmp:0:8", ["const:d6e:8"]]
+ 00472728 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00472728 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00472728 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004726e8 bytes 4a093791
+ 00472728 bytes 4ab93591
- 00472708 ["COPY", "tmp:0:8", ["const:f62:8"]]
- 00472708 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00472708 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00472708 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00472748 ["COPY", "tmp:0:8", ["const:f15:8"]]
+ 00472748 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00472748 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00472748 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00472708 bytes 4a893d91
+ 00472748 bytes 4a553c91
- 004727d0 ["INT_ADD", "register:40f0:8", ["const:4727d0:8", "const:4:8"]]
- 004727d0 ["CALL", null, ["callee:0043b838:8"]]
+ 00472810 ["INT_ADD", "register:40f0:8", ["const:472810:8", "const:4:8"]]
+ 00472810 ["CALL", null, ["callee:0043b838:8"]]
- 004727d0 bytes 0a24ff97
+ 00472810 bytes 0a24ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3dbe87ff8352617e78d41750689c954"></a>

### [`00472da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472da4.md) → [`00472de4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00472/00472de4.md) FUN_00472de4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 9件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) [`00851504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851504.md) [`00853308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00853/00853308.md) [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) [`0088c120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c120.md) · 呼出先 5件 [`00472e34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472e34.md) [`00473028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473028.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)
- 新版 呼出元 9件 [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) [`0085155c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/0085155c.md) [`00853360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00853/00853360.md) [`00856e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00856/00856e84.md) [`0088c178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c178.md) · 呼出先 5件 [`00472e74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00472/00472e74.md) [`00473068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/00473068.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `return_value_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00472e18",
      "incomplete_value": false,
      "site": "00472e1c",
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
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00472dd8",
      "incomplete_value": false,
      "site": "00472ddc",
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
            "const:de8:8"
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
      "definition_site": "00472e28",
      "incomplete_value": false,
      "site": "00472e2c",
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
            "const:ea0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00472de8",
      "incomplete_value": false,
      "site": "00472dec",
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
            "const:da0:8"
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
      "definition_site": "00472e34",
      "incomplete_value": false,
      "site": "00472e48",
      "value": [
        "leaf",
        "const:473068:8"
      ]
    },
    "old": {
      "definition_site": "00472df4",
      "incomplete_value": false,
      "site": "00472e08",
      "value": [
        "leaf",
        "const:473028:8"
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
      "00472df8",
      "READ",
      [
        "storage",
        "00ca4de8",
        null,
        "undefined1"
      ]
    ],
    [
      "00472e04",
      "DATA",
      [
        "storage",
        "00ca4da0",
        null,
        null
      ]
    ],
    [
      "00472e18",
      "PARAM",
      [
        "storage",
        "00ca4de8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00472df8",
      "READ",
      [
        "storage",
        "00ca4ee8",
        null,
        "undefined1"
      ]
    ],
    [
      "00472e04",
      "DATA",
      [
        "storage",
        "00ca4ea0",
        null,
        null
      ]
    ],
    [
      "00472e18",
      "PARAM",
      [
        "storage",
        "00ca4ee8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00472ddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472da4.md#insn-00472ddc) · [`00472dec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472da4.md#insn-00472dec) · [`00472e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472da4.md#insn-00472e08)
- 新版 `00472e1c`（命令位置の公開資料なし） · `00472e2c`（命令位置の公開資料なし） · `00472e48`（命令位置の公開資料なし）

~~~diff
- 00472ddc ["INT_ADD", "register:40f0:8", ["const:472ddc:8", "const:4:8"]]
- 00472ddc ["CALL", null, ["callee:00c57f20:8"]]
+ 00472e1c ["INT_ADD", "register:40f0:8", ["const:472e1c:8", "const:4:8"]]
+ 00472e1c ["CALL", null, ["callee:00c57f20:8"]]
- 00472ddc bytes 1d941f94
+ 00472e1c bytes 41941f94
- 00472dec ["INT_ADD", "register:40f0:8", ["const:472dec:8", "const:4:8"]]
- 00472dec ["CALL", null, ["callee:00472e74:8"]]
+ 00472e2c ["INT_ADD", "register:40f0:8", ["const:472e2c:8", "const:4:8"]]
+ 00472e2c ["CALL", null, ["callee:00472e74:8"]]
- 00472dec bytes 12000094
+ 00472e2c bytes 12000094
- 00472e08 ["INT_ADD", "register:40f0:8", ["const:472e08:8", "const:4:8"]]
- 00472e08 ["CALL", null, ["callee:00c57f00:8"]]
+ 00472e48 ["INT_ADD", "register:40f0:8", ["const:472e48:8", "const:4:8"]]
+ 00472e48 ["CALL", null, ["callee:00c57f00:8"]]
- 00472e08 bytes 0a941f94
+ 00472e48 bytes 2e941f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d105fa470faafac25d5620310105a68"></a>

### [`00472e34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472e34.md) → [`00472e74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00472/00472e74.md) FUN_00472e74

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 3件 [`00472da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472da4.md) [`004766c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/004766c8.md) [`004779cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00477/004779cc.md) · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 3件 [`00472de4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00472/00472de4.md) [`00476708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00476/00476708.md) [`00477a0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00477/00477a0c.md) · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.45% / 新版 92.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00472eb8",
      "incomplete_value": false,
      "site": "00472ebc",
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
      "definition_site": "00472e78",
      "incomplete_value": false,
      "site": "00472e7c",
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00472f00",
      "incomplete_value": false,
      "site": "00472f04",
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
      "definition_site": "00472ec0",
      "incomplete_value": false,
      "site": "00472ec4",
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
      "00472ebc",
      "DATA",
      [
        "storage",
        "00c64db0",
        null,
        "undefined *"
      ]
    ],
    [
      "00472f04",
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
      "00472ebc",
      "DATA",
      [
        "storage",
        "00c64e80",
        null,
        "undefined *"
      ]
    ],
    [
      "00472f04",
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

- 旧版 [`00472e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472e34.md#insn-00472e6c) · [`00472e78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472e34.md#insn-00472e78) · [`00472eb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472e34.md#insn-00472eb4)
- 新版 `00472eac`（命令位置の公開資料なし） · `00472eb8`（命令位置の公開資料なし） · `00472ef4`（命令位置の公開資料なし）

~~~diff
- 00472e6c ["INT_ADD", "register:40f0:8", ["const:472e6c:8", "const:4:8"]]
- 00472e6c ["CALL", null, ["callee:00c57f60:8"]]
+ 00472eac ["INT_ADD", "register:40f0:8", ["const:472eac:8", "const:4:8"]]
+ 00472eac ["CALL", null, ["callee:00c57f60:8"]]
- 00472e6c bytes 09941f94
+ 00472eac bytes 2d941f94
- 00472e78 ["COPY", "tmp:0:8", ["const:db0:8"]]
- 00472e78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00472e78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00472e78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00472eb8 ["COPY", "tmp:0:8", ["const:e80:8"]]
+ 00472eb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00472eb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00472eb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00472e78 bytes 08c13691
+ 00472eb8 bytes 08013a91
- 00472eb4 ["INT_ADD", "register:40f0:8", ["const:472eb4:8", "const:4:8"]]
- 00472eb4 ["CALL", null, ["callee:00c57f60:8"]]
+ 00472ef4 ["INT_ADD", "register:40f0:8", ["const:472ef4:8", "const:4:8"]]
+ 00472ef4 ["CALL", null, ["callee:00c57f60:8"]]
- 00472eb4 bytes f7931f94
+ 00472ef4 bytes 1b941f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f74aba75e1763744d55f117dc8e5e5fb"></a>

### [`00473028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473028.md) → [`00473068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/00473068.md) FUN_00473068

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00472da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00472/00472da4.md) [`004766c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00476/004766c8.md) [`004779cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00477/004779cc.md) · 呼出先 9件 [`00474ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00474/00474ec8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md)
- 新版 呼出元 3件 [`00472de4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00472/00472de4.md) [`00476708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00476/00476708.md) [`00477a0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00477/00477a0c.md) · 呼出先 9件 [`00474f08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00474/00474f08.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c581b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581b0.md) [`00c581c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.82% / 新版 98.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0047308c",
      "incomplete_value": false,
      "site": "00473090",
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
            "const:25:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047304c",
      "incomplete_value": false,
      "site": "00473050",
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
            "const:fe5:8"
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
      "0047308c",
      "PARAM",
      [
        "storage",
        "002b7fe5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0047308c",
      "PARAM",
      [
        "storage",
        "002b8025",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00473050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473028.md#insn-00473050) · [`00473048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473028.md#insn-00473048) · [`0047304c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473028.md#insn-0047304c)
- 新版 `00473090`（命令位置の公開資料なし） · `00473088`（命令位置の公開資料なし） · `0047308c`（命令位置の公開資料なし）

~~~diff
- 00473050 ["INT_ADD", "register:40f0:8", ["const:473050:8", "const:4:8"]]
- 00473050 ["CALL", null, ["callee:00c58540:8"]]
+ 00473090 ["INT_ADD", "register:40f0:8", ["const:473090:8", "const:4:8"]]
+ 00473090 ["CALL", null, ["callee:00c58540:8"]]
- 00473050 bytes 08951f94
+ 00473090 bytes 2c951f94
- 00473048 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 00473088 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 00473048 bytes 20f2ff90
+ 00473088 bytes 20f2ffb0
- 0047304c ["COPY", "tmp:0:8", ["const:fe5:8"]]
- 0047304c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0047304c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0047304c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0047308c ["COPY", "tmp:0:8", ["const:25:8"]]
+ 0047308c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0047308c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0047308c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0047304c bytes 00943f91
+ 0047308c bytes 00940091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72822e4ef53144340ef0c815a07473f3"></a>

### [`00473194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473194.md) → [`004731d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/004731d4.md) FUN_004731d4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00851504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/00851504.md) · 呼出先 4件 [`00475878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475878.md) [`0047587c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/0047587c.md) [`005509ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/005509ac.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`0085155c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/0085155c.md) · 呼出先 4件 [`004758b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00475/004758b8.md) [`004758bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00475/004758bc.md) [`005509ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/005509ec.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

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
      "definition_site": "00473200",
      "incomplete_value": false,
      "site": "00473200",
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
      "definition_site": "004731c0",
      "incomplete_value": false,
      "site": "004731c0",
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
      "00473200",
      "DATA",
      [
        "storage",
        "00c64e50",
        null,
        "undefined *"
      ]
    ],
    [
      "00473234",
      "READ",
      [
        "storage",
        "00c64e70",
        null,
        "pointer"
      ]
    ],
    [
      "00473234",
      "READ",
      [
        "storage",
        "00c64e78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00473200",
      "DATA",
      [
        "storage",
        "00c64f20",
        null,
        "undefined *"
      ]
    ],
    [
      "00473234",
      "READ",
      [
        "storage",
        "00c64f40",
        null,
        "pointer"
      ]
    ],
    [
      "00473234",
      "READ",
      [
        "storage",
        "00c64f48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004731b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473194.md#insn-004731b8) · [`004731cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473194.md#insn-004731cc) · [`004731f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473194.md#insn-004731f8)
- 新版 `004731f8`（命令位置の公開資料なし） · `0047320c`（命令位置の公開資料なし） · `00473238`（命令位置の公開資料なし）

~~~diff
- 004731b8 ["COPY", "tmp:0:8", ["const:e50:8"]]
- 004731b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004731b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004731b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004731f8 ["COPY", "tmp:0:8", ["const:f20:8"]]
+ 004731f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004731f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004731f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004731b8 bytes 08413991
+ 004731f8 bytes 08813c91
- 004731cc ["INT_ADD", "register:40f0:8", ["const:4731cc:8", "const:4:8"]]
- 004731cc ["CALL", null, ["callee:005509ec:8"]]
+ 0047320c ["INT_ADD", "register:40f0:8", ["const:47320c:8", "const:4:8"]]
+ 0047320c ["CALL", null, ["callee:005509ec:8"]]
- 004731cc bytes f8750394
+ 0047320c bytes f8750394
- 004731f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004731f8 ["INT_ADD", "register:40f0:8", ["const:4731f8:8", "const:4:8"]]
- 004731f8 ["CALLIND", null, ["register:0:8"]]
+ 00473238 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00473238 ["INT_ADD", "register:40f0:8", ["const:473238:8", "const:4:8"]]
+ 00473238 ["CALLIND", null, ["register:0:8"]]
- 004731f8 bytes 00013fd6
+ 00473238 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac3a11f06fb763eeb685d3a70cc12efa"></a>

### [`00473270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473270.md) → [`004732b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/004732b0.md) FUN_004732b0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) [`00853308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00853/00853308.md) [`00922dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00922/00922dc8.md) [`00a8a418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a8a/00a8a418.md) · 呼出先 10件 [`00475da0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00475/00475da0.md) [`007683c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00768/007683c8.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 4件 [`00769ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/00769ddc.md) [`00853360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00853/00853360.md) [`00922e1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00922/00922e1c.md) [`00a8a488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a8a/00a8a488.md) · 呼出先 10件 [`00475de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00475/00475de0.md) [`00768420`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00768/00768420.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.36% / 新版 96.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004732d8",
      "value": [
        "leaf",
        "ram:768420:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00473298",
      "value": [
        "leaf",
        "ram:7683c8:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00473314",
      "incomplete_value": false,
      "site": "00473320",
      "value": [
        "leaf",
        "const:475de0:8"
      ]
    },
    "old": {
      "definition_site": "004732d4",
      "incomplete_value": false,
      "site": "004732e0",
      "value": [
        "leaf",
        "const:475da0:8"
      ]
    },
    "ordinal": 5,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0047337c",
      "incomplete_value": false,
      "site": "00473380",
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
      "definition_site": "0047333c",
      "incomplete_value": false,
      "site": "00473340",
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
      "004732d8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007683c8"
      ]
    ],
    [
      "00473314",
      "PARAM",
      [
        "storage",
        "00475da0",
        null,
        null
      ]
    ],
    [
      "0047337c",
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
      "004732d8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768420"
      ]
    ],
    [
      "00473314",
      "PARAM",
      [
        "storage",
        "00475de0",
        null,
        null
      ]
    ],
    [
      "0047337c",
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

- 旧版 [`00473298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473270.md#insn-00473298) · [`004732e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473270.md#insn-004732e0) · [`00473300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473270.md#insn-00473300)
- 新版 `004732d8`（命令位置の公開資料なし） · `00473320`（命令位置の公開資料なし） · `00473340`（命令位置の公開資料なし）

~~~diff
- 00473298 ["INT_ADD", "register:40f0:8", ["const:473298:8", "const:4:8"]]
- 00473298 ["CALL", null, ["ram:7683c8:8"]]
+ 004732d8 ["INT_ADD", "register:40f0:8", ["const:4732d8:8", "const:4:8"]]
+ 004732d8 ["CALL", null, ["ram:768420:8"]]
- 00473298 bytes 4cd40b94
+ 004732d8 bytes 52d40b94
- 004732e0 ["INT_ADD", "register:40f0:8", ["const:4732e0:8", "const:4:8"]]
- 004732e0 ["CALL", null, ["callee:00c581e0:8"]]
+ 00473320 ["INT_ADD", "register:40f0:8", ["const:473320:8", "const:4:8"]]
+ 00473320 ["CALL", null, ["callee:00c581e0:8"]]
- 004732e0 bytes 8c931f94
+ 00473320 bytes b0931f94
- 00473300 ["INT_ADD", "register:40f0:8", ["const:473300:8", "const:4:8"]]
- 00473300 ["CALL", null, ["callee:00c58250:8"]]
+ 00473340 ["INT_ADD", "register:40f0:8", ["const:473340:8", "const:4:8"]]
+ 00473340 ["CALL", null, ["callee:00c58250:8"]]
- 00473300 bytes a0931f94
+ 00473340 bytes c4931f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

