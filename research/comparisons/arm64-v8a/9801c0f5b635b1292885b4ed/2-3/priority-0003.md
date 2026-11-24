# v16.0.1 → v16.0.2 · 最優先の変更候補 (3)

[一覧の目次](README.md)

<a id="compare-058c49c653b494eb289435059f9f9164"></a>

### [`0045aa8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045aa8c.md) → [`0045aacc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045aacc.md) FUN_0045aacc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00451dcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/00451dcc.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00451e0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/00451e0c.md)

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
      "definition_site": "0045aad4",
      "incomplete_value": false,
      "site": "0045aad4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:a50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045aa94",
      "incomplete_value": false,
      "site": "0045aa94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:980:8"
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
      "0045aad4",
      "DATA",
      [
        "storage",
        "00c63980",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045aad4",
      "DATA",
      [
        "storage",
        "00c63a50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045aa8c.md#insn-0045aa90)
- 新版 `0045aad0`（命令位置の公開資料なし）

~~~diff
- 0045aa90 ["COPY", "tmp:0:8", ["const:980:8"]]
- 0045aa90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045aa90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045aa90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045aad0 ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 0045aad0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045aad0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045aad0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045aa90 bytes 08012691
+ 0045aad0 bytes 08412991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21cc047f980578c4965db31e86d06b65"></a>

### [`0045aa9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045aa9c.md) → [`0045aadc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045aadc.md) FUN_0045aadc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00451dcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/00451dcc.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00451e0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/00451e0c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "0045aaf4",
      "incomplete_value": false,
      "site": "0045aaf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:a50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045aab4",
      "incomplete_value": false,
      "site": "0045aab4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:980:8"
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
      "0045aaf4",
      "DATA",
      [
        "storage",
        "00c63980",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045aaf4",
      "DATA",
      [
        "storage",
        "00c63a50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045aaac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045aa9c.md#insn-0045aaac) · [`0045aab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045aa9c.md#insn-0045aab8)
- 新版 `0045aaec`（命令位置の公開資料なし） · `0045aaf8`（命令位置の公開資料なし）

~~~diff
- 0045aaac ["COPY", "tmp:0:8", ["const:980:8"]]
- 0045aaac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045aaac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045aaac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045aaec ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 0045aaec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045aaec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045aaec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045aaac bytes 08012691
+ 0045aaec bytes 08412991
- 0045aab8 ["INT_ADD", "register:40f0:8", ["const:45aab8:8", "const:4:8"]]
- 0045aab8 ["CALL", null, ["callee:00451e0c:8"]]
+ 0045aaf8 ["INT_ADD", "register:40f0:8", ["const:45aaf8:8", "const:4:8"]]
+ 0045aaf8 ["CALL", null, ["callee:00451e0c:8"]]
- 0045aab8 bytes c5dcff97
+ 0045aaf8 bytes c5dcff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc55355006c114d396747550befac2c8"></a>

### [`0045aacc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045aacc.md) → [`0045ab0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045ab0c.md) FUN_0045ab0c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0045b2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b2f0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0045b330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045b330.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "0045ab30",
      "incomplete_value": false,
      "site": "0045ab30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:a50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045aaf0",
      "incomplete_value": false,
      "site": "0045aaf0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:980:8"
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
      "0045ab30",
      "DATA",
      [
        "storage",
        "00c63980",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045ab30",
      "DATA",
      [
        "storage",
        "00c63a50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045aae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045aacc.md#insn-0045aae0) · [`0045aaec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045aacc.md#insn-0045aaec) · [`0045aaf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045aacc.md#insn-0045aaf8)
- 新版 `0045ab20`（命令位置の公開資料なし） · `0045ab2c`（命令位置の公開資料なし） · `0045ab38`（命令位置の公開資料なし）

~~~diff
- 0045aae0 ["INT_ADD", "register:40f0:8", ["const:45aae0:8", "const:4:8"]]
- 0045aae0 ["CALL", null, ["callee:00c57f60:8"]]
+ 0045ab20 ["INT_ADD", "register:40f0:8", ["const:45ab20:8", "const:4:8"]]
+ 0045ab20 ["CALL", null, ["callee:00c57f60:8"]]
- 0045aae0 bytes ecf41f94
+ 0045ab20 bytes 10f51f94
- 0045aaec ["COPY", "tmp:0:8", ["const:980:8"]]
- 0045aaec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045aaec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045aaec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045ab2c ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 0045ab2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045ab2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045ab2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045aaec bytes 08012691
+ 0045ab2c bytes 08412991
- 0045aaf8 ["INT_ADD", "register:40f0:8", ["const:45aaf8:8", "const:4:8"]]
- 0045aaf8 ["CALL", null, ["callee:0045b330:8"]]
+ 0045ab38 ["INT_ADD", "register:40f0:8", ["const:45ab38:8", "const:4:8"]]
+ 0045ab38 ["CALL", null, ["callee:0045b330:8"]]
- 0045aaf8 bytes fe010094
+ 0045ab38 bytes fe010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b39af075ccaba991dd01c5aaa2f32734"></a>

### [`0045ab20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045ab20.md) → [`0045ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045ab60.md) FUN_0045ab60

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`0045b2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b2f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0045b330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045b330.md)

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
      "definition_site": "0045ab6c",
      "incomplete_value": false,
      "site": "0045ab6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:a50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045ab2c",
      "incomplete_value": false,
      "site": "0045ab2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:980:8"
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
      "0045ab6c",
      "DATA",
      [
        "storage",
        "00c63980",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045ab6c",
      "DATA",
      [
        "storage",
        "00c63a50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045ab28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045ab20.md#insn-0045ab28)
- 新版 `0045ab68`（命令位置の公開資料なし）

~~~diff
- 0045ab28 ["COPY", "tmp:0:8", ["const:980:8"]]
- 0045ab28 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0045ab28 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0045ab28 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045ab68 ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 0045ab68 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045ab68 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045ab68 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0045ab28 bytes 29012691
+ 0045ab68 bytes 29412991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61b5bc7ca9e5d67b5af43493afd6aff7"></a>

### [`0045ab6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045ab6c.md) → [`0045abac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045abac.md) FUN_0045abac

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 18件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00450750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/00450750.md) [`00452c54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00452/00452c54.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0045b8ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b8ac.md)
- 新版 呼出元 0件  · 呼出先 18件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00450790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/00450790.md) [`00452c94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00452/00452c94.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`0045b8ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045b8ec.md)

変更の種類 call, call_argument_candidate, call_count, call_target, constant, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 97.19% / 新版 97.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件, `store_value` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0045ae94",
      "incomplete_value": false,
      "site": "0045ae94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:ac0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045ae54",
      "incomplete_value": false,
      "site": "0045ae54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
          ]
        ]
      ]
    },
    "ordinal": 30,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "0045acf4"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0045ad3c",
      "value": [
        "leaf",
        "ram:7643dc:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0045acfc",
      "value": [
        "leaf",
        "ram:764384:8"
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
      "0045ad2c",
      "READ",
      [
        "storage",
        "00ca4aa0",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:0045acf4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00851550"
      ]
    ],
    [
      "0045ad3c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764384"
      ]
    ]
  ],
  "added": [
    [
      "0045ad2c",
      "READ",
      [
        "storage",
        "00ca4ba0",
        null,
        "undefined1"
      ]
    ],
    [
      "0045ad34",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00851550"
      ]
    ],
    [
      "0045ad3c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007643dc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045ab6c.md#insn-0045acf4) · [`0045acfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045ab6c.md#insn-0045acfc)
- 新版 `0045ad3c`（命令位置の公開資料なし） · `0045ad34`（命令位置の公開資料なし）

~~~diff
- 0045acf4 ["INT_ADD", "register:40f0:8", ["const:45acf4:8", "const:4:8"]]
- 0045acf4 ["CALL", null, ["callee:00851550:8"]]
- 0045acf4 bytes 01da0f94
- 0045acfc ["INT_ADD", "register:40f0:8", ["const:45acfc:8", "const:4:8"]]
- 0045acfc ["CALL", null, ["ram:764384:8"]]
+ 0045ad3c ["INT_ADD", "register:40f0:8", ["const:45ad3c:8", "const:4:8"]]
+ 0045ad3c ["CALL", null, ["ram:7643dc:8"]]
- 0045acfc bytes a2250c94
+ 0045ad3c bytes a8250c94
+ 0045ad34 ["INT_ADD", "register:40f0:8", ["const:45ad34:8", "const:4:8"]]
+ 0045ad34 ["CALL", null, ["callee:00851550:8"]]
+ 0045ad34 bytes 07da0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ee0939ef753d237458e5e83b95a48a8"></a>

### [`0045b660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b660.md) → [`0045b6a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045b6a0.md) FUN_0045b6a0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.61% / 新版 96.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0045b6b8",
      "incomplete_value": false,
      "site": "0045b6c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:ac0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045b678",
      "incomplete_value": false,
      "site": "0045b684",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
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
      "0045b6c4",
      "DATA",
      [
        "storage",
        "00c639f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045b6c4",
      "DATA",
      [
        "storage",
        "00c63ac0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045b678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b660.md#insn-0045b678) · [`0045b6a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b660.md#insn-0045b6a8) · [`0045b6d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b660.md#insn-0045b6d8)
- 新版 `0045b6b8`（命令位置の公開資料なし） · `0045b6e8`（命令位置の公開資料なし） · `0045b718`（命令位置の公開資料なし）

~~~diff
- 0045b678 ["COPY", "tmp:0:8", ["const:9f0:8"]]
- 0045b678 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045b678 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045b678 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045b6b8 ["COPY", "tmp:0:8", ["const:ac0:8"]]
+ 0045b6b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045b6b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045b6b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045b678 bytes 08c12791
+ 0045b6b8 bytes 08012b91
- 0045b6a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045b6a8 ["INT_ADD", "register:40f0:8", ["const:45b6a8:8", "const:4:8"]]
- 0045b6a8 ["CALLIND", null, ["register:0:8"]]
+ 0045b6e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045b6e8 ["INT_ADD", "register:40f0:8", ["const:45b6e8:8", "const:4:8"]]
+ 0045b6e8 ["CALLIND", null, ["register:0:8"]]
- 0045b6a8 bytes 00013fd6
+ 0045b6e8 bytes 00013fd6
- 0045b6d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045b6d8 ["INT_ADD", "register:40f0:8", ["const:45b6d8:8", "const:4:8"]]
- 0045b6d8 ["CALLIND", null, ["register:0:8"]]
+ 0045b718 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045b718 ["INT_ADD", "register:40f0:8", ["const:45b718:8", "const:4:8"]]
+ 0045b718 ["CALLIND", null, ["register:0:8"]]
- 0045b6d8 bytes 00013fd6
+ 0045b718 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f80baf5754e9837e9bb6a57ae4470ac"></a>

### [`0045b74c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b74c.md) → [`0045b78c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045b78c.md) FUN_0045b78c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "0045b7a4",
      "incomplete_value": false,
      "site": "0045b7b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:ac0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045b764",
      "incomplete_value": false,
      "site": "0045b770",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
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
      "0045b7b0",
      "DATA",
      [
        "storage",
        "00c639f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045b7b0",
      "DATA",
      [
        "storage",
        "00c63ac0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b74c.md#insn-0045b764) · [`0045b794`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b74c.md#insn-0045b794) · [`0045b7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b74c.md#insn-0045b7c4)
- 新版 `0045b7a4`（命令位置の公開資料なし） · `0045b7d4`（命令位置の公開資料なし） · `0045b804`（命令位置の公開資料なし）

~~~diff
- 0045b764 ["COPY", "tmp:0:8", ["const:9f0:8"]]
- 0045b764 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045b764 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045b764 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045b7a4 ["COPY", "tmp:0:8", ["const:ac0:8"]]
+ 0045b7a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045b7a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045b7a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045b764 bytes 08c12791
+ 0045b7a4 bytes 08012b91
- 0045b794 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045b794 ["INT_ADD", "register:40f0:8", ["const:45b794:8", "const:4:8"]]
- 0045b794 ["CALLIND", null, ["register:0:8"]]
+ 0045b7d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045b7d4 ["INT_ADD", "register:40f0:8", ["const:45b7d4:8", "const:4:8"]]
+ 0045b7d4 ["CALLIND", null, ["register:0:8"]]
- 0045b794 bytes 00013fd6
+ 0045b7d4 bytes 00013fd6
- 0045b7c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045b7c4 ["INT_ADD", "register:40f0:8", ["const:45b7c4:8", "const:4:8"]]
- 0045b7c4 ["CALLIND", null, ["register:0:8"]]
+ 0045b804 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045b804 ["INT_ADD", "register:40f0:8", ["const:45b804:8", "const:4:8"]]
+ 0045b804 ["CALLIND", null, ["register:0:8"]]
- 0045b7c4 bytes 00013fd6
+ 0045b804 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b55b07603a7a31cacb4fab7ac742e361"></a>

### [`0045b834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b834.md) → [`0045b874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045b874.md) FUN_0045b874

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0045bafc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bafc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0045bb3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045bb3c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "0045b898",
      "incomplete_value": false,
      "site": "0045b898",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:ac0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045b858",
      "incomplete_value": false,
      "site": "0045b858",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
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
      "0045b898",
      "DATA",
      [
        "storage",
        "00c639f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045b898",
      "DATA",
      [
        "storage",
        "00c63ac0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045b848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b834.md#insn-0045b848) · [`0045b854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b834.md#insn-0045b854) · [`0045b860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b834.md#insn-0045b860)
- 新版 `0045b888`（命令位置の公開資料なし） · `0045b894`（命令位置の公開資料なし） · `0045b8a0`（命令位置の公開資料なし）

~~~diff
- 0045b848 ["INT_ADD", "register:40f0:8", ["const:45b848:8", "const:4:8"]]
- 0045b848 ["CALL", null, ["callee:00c57f60:8"]]
+ 0045b888 ["INT_ADD", "register:40f0:8", ["const:45b888:8", "const:4:8"]]
+ 0045b888 ["CALL", null, ["callee:00c57f60:8"]]
- 0045b848 bytes 92f11f94
+ 0045b888 bytes b6f11f94
- 0045b854 ["COPY", "tmp:0:8", ["const:9f0:8"]]
- 0045b854 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045b854 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045b854 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045b894 ["COPY", "tmp:0:8", ["const:ac0:8"]]
+ 0045b894 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045b894 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045b894 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045b854 bytes 08c12791
+ 0045b894 bytes 08012b91
- 0045b860 ["INT_ADD", "register:40f0:8", ["const:45b860:8", "const:4:8"]]
- 0045b860 ["CALL", null, ["callee:0045bb3c:8"]]
+ 0045b8a0 ["INT_ADD", "register:40f0:8", ["const:45b8a0:8", "const:4:8"]]
+ 0045b8a0 ["CALL", null, ["callee:0045bb3c:8"]]
- 0045b860 bytes a7000094
+ 0045b8a0 bytes a7000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76669b6645826382374b1f2e26dc51fe"></a>

### [`0045b888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b888.md) → [`0045b8c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045b8c8.md) FUN_0045b8c8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`0045bafc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bafc.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0045bb3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045bb3c.md)

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
      "definition_site": "0045b8d4",
      "incomplete_value": false,
      "site": "0045b8d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:ac0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045b894",
      "incomplete_value": false,
      "site": "0045b894",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
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
      "0045b8d4",
      "DATA",
      [
        "storage",
        "00c639f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045b8d4",
      "DATA",
      [
        "storage",
        "00c63ac0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045b890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b888.md#insn-0045b890)
- 新版 `0045b8d0`（命令位置の公開資料なし）

~~~diff
- 0045b890 ["COPY", "tmp:0:8", ["const:9f0:8"]]
- 0045b890 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0045b890 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0045b890 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045b8d0 ["COPY", "tmp:0:8", ["const:ac0:8"]]
+ 0045b8d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045b8d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045b8d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0045b890 bytes 29c12791
+ 0045b8d0 bytes 29012b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f546501441927591108ea8b97970bfcb"></a>

### [`0045b8d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b8d4.md) → [`0045b914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045b914.md) FUN_0045b914

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`004509b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00450/004509b0.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00764384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764384.md) [`00768e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00768/00768e90.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`004509f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00450/004509f0.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`007643dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/007643dc.md) [`00768ee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00768/00768ee8.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.17% / 新版 94.17%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0045b950",
      "value": [
        "leaf",
        "ram:768ee8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0045b910",
      "value": [
        "leaf",
        "ram:768e90:8"
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
      "site": "0045b9c8",
      "value": [
        "leaf",
        "ram:7643dc:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0045b988",
      "value": [
        "leaf",
        "ram:764384:8"
      ]
    },
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0045ba7c",
      "incomplete_value": false,
      "site": "0045ba80",
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
      "definition_site": "0045ba3c",
      "incomplete_value": false,
      "site": "0045ba40",
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
      "0045b950",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768e90"
      ]
    ],
    [
      "0045b95c",
      "READ",
      [
        "storage",
        "00ca4aa0",
        null,
        "undefined1"
      ]
    ],
    [
      "0045b9c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764384"
      ]
    ]
  ],
  "added": [
    [
      "0045b950",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768ee8"
      ]
    ],
    [
      "0045b95c",
      "READ",
      [
        "storage",
        "00ca4ba0",
        null,
        "undefined1"
      ]
    ],
    [
      "0045b9c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007643dc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045b910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b8d4.md#insn-0045b910) · [`0045b988`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b8d4.md#insn-0045b988) · [`0045ba00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045b8d4.md#insn-0045ba00)
- 新版 `0045b950`（命令位置の公開資料なし） · `0045b9c8`（命令位置の公開資料なし） · `0045ba40`（命令位置の公開資料なし）

~~~diff
- 0045b910 ["INT_ADD", "register:40f0:8", ["const:45b910:8", "const:4:8"]]
- 0045b910 ["CALL", null, ["ram:768e90:8"]]
+ 0045b950 ["INT_ADD", "register:40f0:8", ["const:45b950:8", "const:4:8"]]
+ 0045b950 ["CALL", null, ["ram:768ee8:8"]]
- 0045b910 bytes 60350c94
+ 0045b950 bytes 66350c94
- 0045b988 ["INT_ADD", "register:40f0:8", ["const:45b988:8", "const:4:8"]]
- 0045b988 ["CALL", null, ["ram:764384:8"]]
+ 0045b9c8 ["INT_ADD", "register:40f0:8", ["const:45b9c8:8", "const:4:8"]]
+ 0045b9c8 ["CALL", null, ["ram:7643dc:8"]]
- 0045b988 bytes 7f220c94
+ 0045b9c8 bytes 85220c94
- 0045ba00 ["INT_ADD", "register:40f0:8", ["const:45ba00:8", "const:4:8"]]
- 0045ba00 ["CALL", null, ["callee:00c57f80:8"]]
+ 0045ba40 ["INT_ADD", "register:40f0:8", ["const:45ba40:8", "const:4:8"]]
+ 0045ba40 ["CALL", null, ["callee:00c57f80:8"]]
- 0045ba00 bytes 2cf11f94
+ 0045ba40 bytes 50f11f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02af968827ce98f8137636ed32087890"></a>

### [`0045bd8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bd8c.md) → [`0045bdcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045bdcc.md) FUN_0045bdcc

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
      "definition_site": "0045bdd0",
      "incomplete_value": false,
      "site": "0045bdd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:b60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045bd90",
      "incomplete_value": false,
      "site": "0045bd94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:a90:8"
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
      "0045bdd4",
      "DATA",
      [
        "storage",
        "00c63a90",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0045bdd4",
      "DATA",
      [
        "storage",
        "00c63b60",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045bd90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bd8c.md#insn-0045bd90)
- 新版 `0045bdd0`（命令位置の公開資料なし）

~~~diff
- 0045bd90 ["COPY", "tmp:0:8", ["const:a90:8"]]
- 0045bd90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045bd90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045bd90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045bdd0 ["COPY", "tmp:0:8", ["const:b60:8"]]
+ 0045bdd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045bdd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045bdd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045bd90 bytes 08412a91
+ 0045bdd0 bytes 08812d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee04a34dcad9a237a978ed6507eff947"></a>

### [`0045bd9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bd9c.md) → [`0045bddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045bddc.md) FUN_0045bddc

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
      "definition_site": "0045bdec",
      "incomplete_value": false,
      "site": "0045bdf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:b60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045bdac",
      "incomplete_value": false,
      "site": "0045bdb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:a90:8"
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
      "0045bdf4",
      "DATA",
      [
        "storage",
        "00c63a90",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0045bdf4",
      "DATA",
      [
        "storage",
        "00c63b60",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045bdac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bd9c.md#insn-0045bdac) · [`0045bdb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bd9c.md#insn-0045bdb8)
- 新版 `0045bdec`（命令位置の公開資料なし） · `0045bdf8`（命令位置の公開資料なし）

~~~diff
- 0045bdac ["COPY", "tmp:0:8", ["const:a90:8"]]
- 0045bdac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045bdac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045bdac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045bdec ["COPY", "tmp:0:8", ["const:b60:8"]]
+ 0045bdec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045bdec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045bdec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045bdac bytes 08412a91
+ 0045bdec bytes 08812d91
- 0045bdb8 ["INT_ADD", "register:40f0:8", ["const:45bdb8:8", "const:4:8"]]
- 0045bdb8 ["CALL", null, ["callee:00c57f70:8"]]
+ 0045bdf8 ["INT_ADD", "register:40f0:8", ["const:45bdf8:8", "const:4:8"]]
+ 0045bdf8 ["CALL", null, ["callee:00c57f70:8"]]
- 0045bdb8 bytes 3af01f94
+ 0045bdf8 bytes 5ef01f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a72179d4d2d472a79fb4000d4fa739b"></a>

### [`0045bddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bddc.md) → [`0045be1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045be1c.md) FUN_0045be1c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`0045be2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045be2c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0045be6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045be6c.md)

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
      "definition_site": "0045be2c",
      "incomplete_value": false,
      "site": "0045be30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:bb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045bdec",
      "incomplete_value": false,
      "site": "0045bdf0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
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
      "0045be30",
      "DATA",
      [
        "storage",
        "00c63ae0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0045be30",
      "DATA",
      [
        "storage",
        "00c63bb0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045bdec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bddc.md#insn-0045bdec)
- 新版 `0045be2c`（命令位置の公開資料なし）

~~~diff
- 0045bdec ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 0045bdec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0045bdec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0045bdec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045be2c ["COPY", "tmp:0:8", ["const:bb0:8"]]
+ 0045be2c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045be2c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045be2c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0045bdec bytes 29812b91
+ 0045be2c bytes 29c12e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fca32a71af5a2b2a31bea9baa044f9d"></a>

### [`0045bdf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bdf8.md) → [`0045be38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045be38.md) FUN_0045be38

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 7件 [`005959dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/005959dc.md) [`00595d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595d1c.md) [`00767148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00767/00767148.md) [`00798ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00798/00798ea0.md) [`007abc24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ab/007abc24.md) · 呼出先 2件 [`0045be2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045be2c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 7件 [`00595a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595a1c.md) [`00595d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595d5c.md) [`007671a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00767/007671a0.md) [`00798ef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00798/00798ef8.md) [`007abc7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ab/007abc7c.md) · 呼出先 2件 [`0045be6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045be6c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "0045be54",
      "incomplete_value": false,
      "site": "0045be54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:bb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045be14",
      "incomplete_value": false,
      "site": "0045be14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
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
      "0045be54",
      "DATA",
      [
        "storage",
        "00c63ae0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0045be54",
      "DATA",
      [
        "storage",
        "00c63bb0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045be0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bdf8.md#insn-0045be0c) · [`0045be18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bdf8.md#insn-0045be18)
- 新版 `0045be4c`（命令位置の公開資料なし） · `0045be58`（命令位置の公開資料なし）

~~~diff
- 0045be0c ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 0045be0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045be0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045be0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045be4c ["COPY", "tmp:0:8", ["const:bb0:8"]]
+ 0045be4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045be4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045be4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045be0c bytes 08812b91
+ 0045be4c bytes 08c12e91
- 0045be18 ["INT_ADD", "register:40f0:8", ["const:45be18:8", "const:4:8"]]
- 0045be18 ["CALL", null, ["callee:0045be6c:8"]]
+ 0045be58 ["INT_ADD", "register:40f0:8", ["const:45be58:8", "const:4:8"]]
+ 0045be58 ["CALL", null, ["callee:0045be6c:8"]]
- 0045be18 bytes 05000094
+ 0045be58 bytes 05000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6c6e7c9d22ce2a7d9a72ba66072ea02"></a>

### [`0045be94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045be94.md) → [`0045bed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045bed4.md) FUN_0045bed4

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
      "definition_site": "0045bee0",
      "incomplete_value": false,
      "site": "0045beec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:c10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045bea0",
      "incomplete_value": false,
      "site": "0045beac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:b40:8"
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
      "0045beec",
      "DATA",
      [
        "storage",
        "00c63b40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045beec",
      "DATA",
      [
        "storage",
        "00c63c10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045bea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045be94.md#insn-0045bea0)
- 新版 `0045bee0`（命令位置の公開資料なし）

~~~diff
- 0045bea0 ["COPY", "tmp:0:8", ["const:b40:8"]]
- 0045bea0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0045bea0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0045bea0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0045bee0 ["COPY", "tmp:0:8", ["const:c10:8"]]
+ 0045bee0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0045bee0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0045bee0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0045bea0 bytes 4a012d91
+ 0045bee0 bytes 4a413091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-488e5893ebd95b84721b65791ff11dd9"></a>

### [`0045bed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bed8.md) → [`0045bf18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045bf18.md) FUN_0045bf18

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
      "definition_site": "0045bf30",
      "incomplete_value": false,
      "site": "0045bf3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:c10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045bef0",
      "incomplete_value": false,
      "site": "0045befc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:b40:8"
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
      "0045bf3c",
      "DATA",
      [
        "storage",
        "00c63b40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045bf3c",
      "DATA",
      [
        "storage",
        "00c63c10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045bef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bed8.md#insn-0045bef0) · [`0045bf20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bed8.md#insn-0045bf20)
- 新版 `0045bf30`（命令位置の公開資料なし） · `0045bf60`（命令位置の公開資料なし）

~~~diff
- 0045bef0 ["COPY", "tmp:0:8", ["const:b40:8"]]
- 0045bef0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045bef0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045bef0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045bf30 ["COPY", "tmp:0:8", ["const:c10:8"]]
+ 0045bf30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045bf30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045bf30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045bef0 bytes 08012d91
+ 0045bf30 bytes 08413091
- 0045bf20 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045bf20 ["INT_ADD", "register:40f0:8", ["const:45bf20:8", "const:4:8"]]
- 0045bf20 ["CALLIND", null, ["register:0:8"]]
+ 0045bf60 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045bf60 ["INT_ADD", "register:40f0:8", ["const:45bf60:8", "const:4:8"]]
+ 0045bf60 ["CALLIND", null, ["register:0:8"]]
- 0045bf20 bytes 00013fd6
+ 0045bf60 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf3726e09678c8d3df267df5353a4e2c"></a>

### [`0045bf34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bf34.md) → [`0045bf74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045bf74.md) FUN_0045bf74

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
      "definition_site": "0045bfa0",
      "incomplete_value": false,
      "site": "0045bfa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:c10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045bf60",
      "incomplete_value": false,
      "site": "0045bf60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:b40:8"
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
      "0045bfa0",
      "DATA",
      [
        "storage",
        "00c63b40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045bfa0",
      "DATA",
      [
        "storage",
        "00c63c10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045bf48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bf34.md#insn-0045bf48) · [`0045bf58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bf34.md#insn-0045bf58) · [`0045bf7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bf34.md#insn-0045bf7c)
- 新版 `0045bf88`（命令位置の公開資料なし） · `0045bf98`（命令位置の公開資料なし） · `0045bfbc`（命令位置の公開資料なし）

~~~diff
- 0045bf48 ["INT_ADD", "register:40f0:8", ["const:45bf48:8", "const:4:8"]]
- 0045bf48 ["CALL", null, ["callee:00c57f60:8"]]
+ 0045bf88 ["INT_ADD", "register:40f0:8", ["const:45bf88:8", "const:4:8"]]
+ 0045bf88 ["CALL", null, ["callee:00c57f60:8"]]
- 0045bf48 bytes d2ef1f94
+ 0045bf88 bytes f6ef1f94
- 0045bf58 ["COPY", "tmp:0:8", ["const:b40:8"]]
- 0045bf58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045bf58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045bf58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045bf98 ["COPY", "tmp:0:8", ["const:c10:8"]]
+ 0045bf98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045bf98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045bf98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045bf58 bytes 08012d91
+ 0045bf98 bytes 08413091
- 0045bf7c ["COPY", "register:0:8", ["register:4040:8"]]
- 0045bf7c ["INT_ADD", "register:40f0:8", ["const:45bf7c:8", "const:4:8"]]
- 0045bf7c ["CALLIND", null, ["register:0:8"]]
+ 0045bfbc ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045bfbc ["INT_ADD", "register:40f0:8", ["const:45bfbc:8", "const:4:8"]]
+ 0045bfbc ["CALLIND", null, ["register:0:8"]]
- 0045bf7c bytes 00013fd6
+ 0045bfbc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a6143f21a8543bcf14c4a1c32b9f1f7"></a>

### [`0045bfbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bfbc.md) → [`0045bffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045b/0045bffc.md) FUN_0045bffc

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
      "definition_site": "0045c018",
      "incomplete_value": false,
      "site": "0045c018",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:c10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045bfd8",
      "incomplete_value": false,
      "site": "0045bfd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:b40:8"
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
      "0045c018",
      "DATA",
      [
        "storage",
        "00c63b40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045c018",
      "DATA",
      [
        "storage",
        "00c63c10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045bfd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bfbc.md#insn-0045bfd4) · [`0045bff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045b/0045bfbc.md#insn-0045bff8)
- 新版 `0045c014`（命令位置の公開資料なし） · `0045c038`（命令位置の公開資料なし）

~~~diff
- 0045bfd4 ["COPY", "tmp:0:8", ["const:b40:8"]]
- 0045bfd4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0045bfd4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0045bfd4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045c014 ["COPY", "tmp:0:8", ["const:c10:8"]]
+ 0045c014 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045c014 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045c014 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0045bfd4 bytes 29012d91
+ 0045c014 bytes 29413091
- 0045bff8 ["COPY", "register:0:8", ["register:4048:8"]]
- 0045bff8 ["INT_ADD", "register:40f0:8", ["const:45bff8:8", "const:4:8"]]
- 0045bff8 ["CALLIND", null, ["register:0:8"]]
+ 0045c038 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0045c038 ["INT_ADD", "register:40f0:8", ["const:45c038:8", "const:4:8"]]
+ 0045c038 ["CALLIND", null, ["register:0:8"]]
- 0045bff8 bytes 20013fd6
+ 0045c038 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d59bde5c7adbb7129e63276d8a01204c"></a>

### [`0045c0b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045c0b8.md) → [`0045c0f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045c0f8.md) FUN_0045c0f8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.26% / 新版 97.26%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0045c140",
      "incomplete_value": true,
      "site": "0045c140",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1e5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045c100",
      "incomplete_value": true,
      "site": "0045c100",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1a5:8"
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
      "definition_site": "0045c2c4",
      "incomplete_value": true,
      "site": "0045c2d8",
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
                "const:dce:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045c284",
      "incomplete_value": true,
      "site": "0045c298",
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
                "const:e1b:8"
              ]
            ]
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
      "definition_site": "0045c3a4",
      "incomplete_value": true,
      "site": "0045c3a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ee0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045c364",
      "incomplete_value": true,
      "site": "0045c364",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f2d:8"
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
      "0045c11c",
      "READ",
      [
        "storage",
        "002b71a5",
        null,
        "string"
      ]
    ],
    [
      "0045c2c4",
      "READ",
      [
        "storage",
        "002a1e1b",
        null,
        "string"
      ]
    ],
    [
      "0045c390",
      "READ",
      [
        "storage",
        "0029ff2d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0045c11c",
      "READ",
      [
        "storage",
        "002b71e5",
        null,
        "string"
      ]
    ],
    [
      "0045c2c4",
      "READ",
      [
        "storage",
        "002a1dce",
        null,
        "string"
      ]
    ],
    [
      "0045c390",
      "READ",
      [
        "storage",
        "0029fee0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045c140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045c0b8.md#insn-0045c140) · [`0045c0d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045c0b8.md#insn-0045c0d4) · [`0045c110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045c0b8.md#insn-0045c110)
- 新版 `0045c180`（命令位置の公開資料なし） · `0045c114`（命令位置の公開資料なし） · `0045c150`（命令位置の公開資料なし）

~~~diff
- 0045c140 ["INT_ADD", "register:40f0:8", ["const:45c140:8", "const:4:8"]]
- 0045c140 ["CALL", null, ["callee:00c57f80:8"]]
+ 0045c180 ["INT_ADD", "register:40f0:8", ["const:45c180:8", "const:4:8"]]
+ 0045c180 ["CALL", null, ["callee:00c57f80:8"]]
- 0045c140 bytes 5cef1f94
+ 0045c180 bytes 80ef1f94
- 0045c0d4 ["COPY", "tmp:0:8", ["const:1a5:8"]]
- 0045c0d4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0045c0d4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0045c0d4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0045c114 ["COPY", "tmp:0:8", ["const:1e5:8"]]
+ 0045c114 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0045c114 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0045c114 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0045c0d4 bytes 4a950691
+ 0045c114 bytes 4a950791
- 0045c110 ["INT_ADD", "register:40f0:8", ["const:45c110:8", "const:4:8"]]
- 0045c110 ["CALL", null, ["callee:004410cc:8"]]
+ 0045c150 ["INT_ADD", "register:40f0:8", ["const:45c150:8", "const:4:8"]]
+ 0045c150 ["CALL", null, ["callee:004410cc:8"]]
- 0045c110 bytes df93ff97
+ 0045c150 bytes df93ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0475f83249b0262c57ff9f29a5afe4cc"></a>

### [`0045c6e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045c6e4.md) → [`0045c724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045c724.md) FUN_0045c724

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
      "definition_site": "0045c730",
      "incomplete_value": false,
      "site": "0045c73c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045c6f0",
      "incomplete_value": false,
      "site": "0045c6fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:bd0:8"
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
      "0045c73c",
      "DATA",
      [
        "storage",
        "00c63bd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045c73c",
      "DATA",
      [
        "storage",
        "00c63ca0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045c6f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045c6e4.md#insn-0045c6f0)
- 新版 `0045c730`（命令位置の公開資料なし）

~~~diff
- 0045c6f0 ["COPY", "tmp:0:8", ["const:bd0:8"]]
- 0045c6f0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0045c6f0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0045c6f0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0045c730 ["COPY", "tmp:0:8", ["const:ca0:8"]]
+ 0045c730 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0045c730 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0045c730 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0045c6f0 bytes 4a412f91
+ 0045c730 bytes 4a813291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c85b6351d4450c5250e645c4a5260467"></a>

### [`0045c728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045c728.md) → [`0045c768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045c768.md) FUN_0045c768

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
      "definition_site": "0045c780",
      "incomplete_value": false,
      "site": "0045c78c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045c740",
      "incomplete_value": false,
      "site": "0045c74c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:bd0:8"
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
      "0045c78c",
      "DATA",
      [
        "storage",
        "00c63bd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045c78c",
      "DATA",
      [
        "storage",
        "00c63ca0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045c740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045c728.md#insn-0045c740) · [`0045c770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045c728.md#insn-0045c770)
- 新版 `0045c780`（命令位置の公開資料なし） · `0045c7b0`（命令位置の公開資料なし）

~~~diff
- 0045c740 ["COPY", "tmp:0:8", ["const:bd0:8"]]
- 0045c740 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045c740 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045c740 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045c780 ["COPY", "tmp:0:8", ["const:ca0:8"]]
+ 0045c780 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045c780 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045c780 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045c740 bytes 08412f91
+ 0045c780 bytes 08813291
- 0045c770 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045c770 ["INT_ADD", "register:40f0:8", ["const:45c770:8", "const:4:8"]]
- 0045c770 ["CALLIND", null, ["register:0:8"]]
+ 0045c7b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045c7b0 ["INT_ADD", "register:40f0:8", ["const:45c7b0:8", "const:4:8"]]
+ 0045c7b0 ["CALLIND", null, ["register:0:8"]]
- 0045c770 bytes 00013fd6
+ 0045c7b0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c848e34c6aac8c0901380e902e4b9eaf"></a>

### [`0045c784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045c784.md) → [`0045c7c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045c7c4.md) FUN_0045c7c4

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
      "definition_site": "0045c7f0",
      "incomplete_value": false,
      "site": "0045c7f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045c7b0",
      "incomplete_value": false,
      "site": "0045c7b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:bd0:8"
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
      "0045c7f0",
      "DATA",
      [
        "storage",
        "00c63bd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045c7f0",
      "DATA",
      [
        "storage",
        "00c63ca0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045c798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045c784.md#insn-0045c798) · [`0045c7a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045c784.md#insn-0045c7a8) · [`0045c7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045c784.md#insn-0045c7cc)
- 新版 `0045c7d8`（命令位置の公開資料なし） · `0045c7e8`（命令位置の公開資料なし） · `0045c80c`（命令位置の公開資料なし）

~~~diff
- 0045c798 ["INT_ADD", "register:40f0:8", ["const:45c798:8", "const:4:8"]]
- 0045c798 ["CALL", null, ["callee:00c57f60:8"]]
+ 0045c7d8 ["INT_ADD", "register:40f0:8", ["const:45c7d8:8", "const:4:8"]]
+ 0045c7d8 ["CALL", null, ["callee:00c57f60:8"]]
- 0045c798 bytes beed1f94
+ 0045c7d8 bytes e2ed1f94
- 0045c7a8 ["COPY", "tmp:0:8", ["const:bd0:8"]]
- 0045c7a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045c7a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045c7a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045c7e8 ["COPY", "tmp:0:8", ["const:ca0:8"]]
+ 0045c7e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045c7e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045c7e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045c7a8 bytes 08412f91
+ 0045c7e8 bytes 08813291
- 0045c7cc ["COPY", "register:0:8", ["register:4040:8"]]
- 0045c7cc ["INT_ADD", "register:40f0:8", ["const:45c7cc:8", "const:4:8"]]
- 0045c7cc ["CALLIND", null, ["register:0:8"]]
+ 0045c80c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045c80c ["INT_ADD", "register:40f0:8", ["const:45c80c:8", "const:4:8"]]
+ 0045c80c ["CALLIND", null, ["register:0:8"]]
- 0045c7cc bytes 00013fd6
+ 0045c80c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f45cd82f6b07f18fc7fe0c1952e1510"></a>

### [`0045c80c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045c80c.md) → [`0045c84c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045c84c.md) FUN_0045c84c

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
      "definition_site": "0045c868",
      "incomplete_value": false,
      "site": "0045c868",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045c828",
      "incomplete_value": false,
      "site": "0045c828",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:bd0:8"
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
      "0045c868",
      "DATA",
      [
        "storage",
        "00c63bd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045c868",
      "DATA",
      [
        "storage",
        "00c63ca0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045c824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045c80c.md#insn-0045c824) · [`0045c848`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045c80c.md#insn-0045c848)
- 新版 `0045c864`（命令位置の公開資料なし） · `0045c888`（命令位置の公開資料なし）

~~~diff
- 0045c824 ["COPY", "tmp:0:8", ["const:bd0:8"]]
- 0045c824 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0045c824 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0045c824 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045c864 ["COPY", "tmp:0:8", ["const:ca0:8"]]
+ 0045c864 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045c864 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045c864 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0045c824 bytes 29412f91
+ 0045c864 bytes 29813291
- 0045c848 ["COPY", "register:0:8", ["register:4048:8"]]
- 0045c848 ["INT_ADD", "register:40f0:8", ["const:45c848:8", "const:4:8"]]
- 0045c848 ["CALLIND", null, ["register:0:8"]]
+ 0045c888 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0045c888 ["INT_ADD", "register:40f0:8", ["const:45c888:8", "const:4:8"]]
+ 0045c888 ["CALLIND", null, ["register:0:8"]]
- 0045c848 bytes 20013fd6
+ 0045c888 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d8cd7f9a519ee8321de7cad870f01eb"></a>

### [`0045cd8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045cd8c.md) → [`0045cdcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045cdcc.md) FUN_0045cdcc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0045ca98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045ca98.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 1件 [`0045cad8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045cad8.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "0045cdd8",
      "incomplete_value": false,
      "site": "0045cddc",
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
      "definition_site": "0045cd98",
      "incomplete_value": false,
      "site": "0045cd9c",
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
      "0045cdd8",
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
      "0045cdd8",
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

- 旧版 [`0045cd9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045cd8c.md#insn-0045cd9c) · [`0045cd98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045cd8c.md#insn-0045cd98)
- 新版 `0045cddc`（命令位置の公開資料なし） · `0045cdd8`（命令位置の公開資料なし）

~~~diff
- 0045cd9c ["INT_ADD", "register:40f0:8", ["const:45cd9c:8", "const:4:8"]]
- 0045cd9c ["CALL", null, ["callee:0043b7b8:8"]]
+ 0045cddc ["INT_ADD", "register:40f0:8", ["const:45cddc:8", "const:4:8"]]
+ 0045cddc ["CALL", null, ["callee:0043b7b8:8"]]
- 0045cd9c bytes 777aff97
+ 0045cddc bytes 777aff97
- 0045cd98 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 0045cd98 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0045cd98 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0045cd98 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0045cdd8 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 0045cdd8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0045cdd8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0045cdd8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0045cd98 bytes 00303d91
+ 0045cdd8 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b6cf3d23c27f7c3e82f6b3effc3f767"></a>

### [`0045cda0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045cda0.md) → [`0045cde0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045cde0.md) FUN_0045cde0

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
      "definition_site": "0045cdec",
      "incomplete_value": false,
      "site": "0045cdf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:d30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045cdac",
      "incomplete_value": false,
      "site": "0045cdb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:c60:8"
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
      "0045cdf8",
      "DATA",
      [
        "storage",
        "00c63c60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045cdf8",
      "DATA",
      [
        "storage",
        "00c63d30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045cdac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045cda0.md#insn-0045cdac)
- 新版 `0045cdec`（命令位置の公開資料なし）

~~~diff
- 0045cdac ["COPY", "tmp:0:8", ["const:c60:8"]]
- 0045cdac ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0045cdac ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0045cdac ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0045cdec ["COPY", "tmp:0:8", ["const:d30:8"]]
+ 0045cdec ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0045cdec ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0045cdec ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0045cdac bytes 4a813191
+ 0045cdec bytes 4ac13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0b4e4f67b63cf6ee706a05bb3f76931"></a>

### [`0045cde4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045cde4.md) → [`0045ce24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045ce24.md) FUN_0045ce24

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
      "definition_site": "0045ce3c",
      "incomplete_value": false,
      "site": "0045ce48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:d30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045cdfc",
      "incomplete_value": false,
      "site": "0045ce08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:c60:8"
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
      "0045ce48",
      "DATA",
      [
        "storage",
        "00c63c60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045ce48",
      "DATA",
      [
        "storage",
        "00c63d30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045cdfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045cde4.md#insn-0045cdfc) · [`0045ce2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045cde4.md#insn-0045ce2c)
- 新版 `0045ce3c`（命令位置の公開資料なし） · `0045ce6c`（命令位置の公開資料なし）

~~~diff
- 0045cdfc ["COPY", "tmp:0:8", ["const:c60:8"]]
- 0045cdfc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045cdfc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045cdfc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045ce3c ["COPY", "tmp:0:8", ["const:d30:8"]]
+ 0045ce3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045ce3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045ce3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045cdfc bytes 08813191
+ 0045ce3c bytes 08c13491
- 0045ce2c ["COPY", "register:0:8", ["register:4040:8"]]
- 0045ce2c ["INT_ADD", "register:40f0:8", ["const:45ce2c:8", "const:4:8"]]
- 0045ce2c ["CALLIND", null, ["register:0:8"]]
+ 0045ce6c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045ce6c ["INT_ADD", "register:40f0:8", ["const:45ce6c:8", "const:4:8"]]
+ 0045ce6c ["CALLIND", null, ["register:0:8"]]
- 0045ce2c bytes 00013fd6
+ 0045ce6c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8b762402212f7ecfe11d343acc3771a"></a>

### [`0045ce40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045ce40.md) → [`0045ce80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045ce80.md) FUN_0045ce80

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
      "definition_site": "0045ceac",
      "incomplete_value": false,
      "site": "0045ceac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:d30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045ce6c",
      "incomplete_value": false,
      "site": "0045ce6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:c60:8"
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
      "0045ceac",
      "DATA",
      [
        "storage",
        "00c63c60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045ceac",
      "DATA",
      [
        "storage",
        "00c63d30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045ce40.md#insn-0045ce54) · [`0045ce64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045ce40.md#insn-0045ce64) · [`0045ce88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045ce40.md#insn-0045ce88)
- 新版 `0045ce94`（命令位置の公開資料なし） · `0045cea4`（命令位置の公開資料なし） · `0045cec8`（命令位置の公開資料なし）

~~~diff
- 0045ce54 ["INT_ADD", "register:40f0:8", ["const:45ce54:8", "const:4:8"]]
- 0045ce54 ["CALL", null, ["callee:00c57f60:8"]]
+ 0045ce94 ["INT_ADD", "register:40f0:8", ["const:45ce94:8", "const:4:8"]]
+ 0045ce94 ["CALL", null, ["callee:00c57f60:8"]]
- 0045ce54 bytes 0fec1f94
+ 0045ce94 bytes 33ec1f94
- 0045ce64 ["COPY", "tmp:0:8", ["const:c60:8"]]
- 0045ce64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045ce64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045ce64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045cea4 ["COPY", "tmp:0:8", ["const:d30:8"]]
+ 0045cea4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045cea4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045cea4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045ce64 bytes 08813191
+ 0045cea4 bytes 08c13491
- 0045ce88 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045ce88 ["INT_ADD", "register:40f0:8", ["const:45ce88:8", "const:4:8"]]
- 0045ce88 ["CALLIND", null, ["register:0:8"]]
+ 0045cec8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045cec8 ["INT_ADD", "register:40f0:8", ["const:45cec8:8", "const:4:8"]]
+ 0045cec8 ["CALLIND", null, ["register:0:8"]]
- 0045ce88 bytes 00013fd6
+ 0045cec8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1efacef30e511b1970acefcac34b4150"></a>

### [`0045cec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045cec8.md) → [`0045cf08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045c/0045cf08.md) FUN_0045cf08

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
      "definition_site": "0045cf24",
      "incomplete_value": false,
      "site": "0045cf24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:d30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045cee4",
      "incomplete_value": false,
      "site": "0045cee4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:c60:8"
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
      "0045cf24",
      "DATA",
      [
        "storage",
        "00c63c60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045cf24",
      "DATA",
      [
        "storage",
        "00c63d30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045cee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045cec8.md#insn-0045cee0) · [`0045cf04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045c/0045cec8.md#insn-0045cf04)
- 新版 `0045cf20`（命令位置の公開資料なし） · `0045cf44`（命令位置の公開資料なし）

~~~diff
- 0045cee0 ["COPY", "tmp:0:8", ["const:c60:8"]]
- 0045cee0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0045cee0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0045cee0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045cf20 ["COPY", "tmp:0:8", ["const:d30:8"]]
+ 0045cf20 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045cf20 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045cf20 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0045cee0 bytes 29813191
+ 0045cf20 bytes 29c13491
- 0045cf04 ["COPY", "register:0:8", ["register:4048:8"]]
- 0045cf04 ["INT_ADD", "register:40f0:8", ["const:45cf04:8", "const:4:8"]]
- 0045cf04 ["CALLIND", null, ["register:0:8"]]
+ 0045cf44 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0045cf44 ["INT_ADD", "register:40f0:8", ["const:45cf44:8", "const:4:8"]]
+ 0045cf44 ["CALLIND", null, ["register:0:8"]]
- 0045cf04 bytes 20013fd6
+ 0045cf44 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-117cec073af775be0ced54b15de9082a"></a>

### [`0045d790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045d790.md) → [`0045d7d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045d7d0.md) FUN_0045d7d0

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
      "definition_site": "0045d7dc",
      "incomplete_value": false,
      "site": "0045d7e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:db0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045d79c",
      "incomplete_value": false,
      "site": "0045d7a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:ce0:8"
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
      "0045d7e8",
      "DATA",
      [
        "storage",
        "00c63ce0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045d7e8",
      "DATA",
      [
        "storage",
        "00c63db0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045d79c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045d790.md#insn-0045d79c)
- 新版 `0045d7dc`（命令位置の公開資料なし）

~~~diff
- 0045d79c ["COPY", "tmp:0:8", ["const:ce0:8"]]
- 0045d79c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0045d79c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0045d79c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0045d7dc ["COPY", "tmp:0:8", ["const:db0:8"]]
+ 0045d7dc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0045d7dc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0045d7dc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0045d79c bytes 4a813391
+ 0045d7dc bytes 4ac13691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7f36eead56caca044ce2f0de69fce44"></a>

### [`0045d7d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045d7d4.md) → [`0045d814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045d814.md) FUN_0045d814

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
      "definition_site": "0045d82c",
      "incomplete_value": false,
      "site": "0045d838",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:db0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045d7ec",
      "incomplete_value": false,
      "site": "0045d7f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:ce0:8"
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
      "0045d838",
      "DATA",
      [
        "storage",
        "00c63ce0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045d838",
      "DATA",
      [
        "storage",
        "00c63db0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045d7ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045d7d4.md#insn-0045d7ec) · [`0045d81c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045d7d4.md#insn-0045d81c)
- 新版 `0045d82c`（命令位置の公開資料なし） · `0045d85c`（命令位置の公開資料なし）

~~~diff
- 0045d7ec ["COPY", "tmp:0:8", ["const:ce0:8"]]
- 0045d7ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045d7ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045d7ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045d82c ["COPY", "tmp:0:8", ["const:db0:8"]]
+ 0045d82c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045d82c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045d82c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045d7ec bytes 08813391
+ 0045d82c bytes 08c13691
- 0045d81c ["COPY", "register:0:8", ["register:4040:8"]]
- 0045d81c ["INT_ADD", "register:40f0:8", ["const:45d81c:8", "const:4:8"]]
- 0045d81c ["CALLIND", null, ["register:0:8"]]
+ 0045d85c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045d85c ["INT_ADD", "register:40f0:8", ["const:45d85c:8", "const:4:8"]]
+ 0045d85c ["CALLIND", null, ["register:0:8"]]
- 0045d81c bytes 00013fd6
+ 0045d85c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-644f6c3a01cdc6fd9d4bc38737368ad9"></a>

### [`0045d830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045d830.md) → [`0045d870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045d870.md) FUN_0045d870

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
      "definition_site": "0045d89c",
      "incomplete_value": false,
      "site": "0045d89c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:db0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045d85c",
      "incomplete_value": false,
      "site": "0045d85c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:ce0:8"
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
      "0045d89c",
      "DATA",
      [
        "storage",
        "00c63ce0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045d89c",
      "DATA",
      [
        "storage",
        "00c63db0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045d844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045d830.md#insn-0045d844) · [`0045d854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045d830.md#insn-0045d854) · [`0045d878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045d830.md#insn-0045d878)
- 新版 `0045d884`（命令位置の公開資料なし） · `0045d894`（命令位置の公開資料なし） · `0045d8b8`（命令位置の公開資料なし）

~~~diff
- 0045d844 ["INT_ADD", "register:40f0:8", ["const:45d844:8", "const:4:8"]]
- 0045d844 ["CALL", null, ["callee:00c57f60:8"]]
+ 0045d884 ["INT_ADD", "register:40f0:8", ["const:45d884:8", "const:4:8"]]
+ 0045d884 ["CALL", null, ["callee:00c57f60:8"]]
- 0045d844 bytes 93e91f94
+ 0045d884 bytes b7e91f94
- 0045d854 ["COPY", "tmp:0:8", ["const:ce0:8"]]
- 0045d854 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045d854 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045d854 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045d894 ["COPY", "tmp:0:8", ["const:db0:8"]]
+ 0045d894 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045d894 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045d894 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045d854 bytes 08813391
+ 0045d894 bytes 08c13691
- 0045d878 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045d878 ["INT_ADD", "register:40f0:8", ["const:45d878:8", "const:4:8"]]
- 0045d878 ["CALLIND", null, ["register:0:8"]]
+ 0045d8b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045d8b8 ["INT_ADD", "register:40f0:8", ["const:45d8b8:8", "const:4:8"]]
+ 0045d8b8 ["CALLIND", null, ["register:0:8"]]
- 0045d878 bytes 00013fd6
+ 0045d8b8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cf003e204658c4e4b849c4316f4f7c8"></a>

### [`0045d8b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045d8b8.md) → [`0045d8f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045d8f8.md) FUN_0045d8f8

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
      "definition_site": "0045d914",
      "incomplete_value": false,
      "site": "0045d914",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:db0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045d8d4",
      "incomplete_value": false,
      "site": "0045d8d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:ce0:8"
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
      "0045d914",
      "DATA",
      [
        "storage",
        "00c63ce0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045d914",
      "DATA",
      [
        "storage",
        "00c63db0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045d8d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045d8b8.md#insn-0045d8d0) · [`0045d8f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045d8b8.md#insn-0045d8f4)
- 新版 `0045d910`（命令位置の公開資料なし） · `0045d934`（命令位置の公開資料なし）

~~~diff
- 0045d8d0 ["COPY", "tmp:0:8", ["const:ce0:8"]]
- 0045d8d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0045d8d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0045d8d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045d910 ["COPY", "tmp:0:8", ["const:db0:8"]]
+ 0045d910 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045d910 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045d910 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0045d8d0 bytes 29813391
+ 0045d910 bytes 29c13691
- 0045d8f4 ["COPY", "register:0:8", ["register:4048:8"]]
- 0045d8f4 ["INT_ADD", "register:40f0:8", ["const:45d8f4:8", "const:4:8"]]
- 0045d8f4 ["CALLIND", null, ["register:0:8"]]
+ 0045d934 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0045d934 ["INT_ADD", "register:40f0:8", ["const:45d934:8", "const:4:8"]]
+ 0045d934 ["CALLIND", null, ["register:0:8"]]
- 0045d8f4 bytes 20013fd6
+ 0045d934 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-788a245d0a75717540ccfa979d1022e1"></a>

### [`0045d9b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045d9b4.md) → [`0045d9f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045d9f4.md) FUN_0045d9f4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00a1a6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a6a4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00a1a6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a1a/00a1a6f8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0045db08",
      "incomplete_value": false,
      "site": "0045db08",
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
    "old": {
      "definition_site": "0045dac8",
      "incomplete_value": false,
      "site": "0045dac8",
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
            "const:b18:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0045db0c",
      "incomplete_value": false,
      "site": "0045db0c",
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
            "const:c30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045dacc",
      "incomplete_value": false,
      "site": "0045dacc",
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
            "const:b30:8"
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
      "definition_site": "0045da50",
      "incomplete_value": true,
      "site": "0045da50",
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
      "definition_site": "0045da10",
      "incomplete_value": true,
      "site": "0045da10",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0045da48",
      "READ",
      [
        "storage",
        "00ca4b10",
        null,
        "undefined8"
      ]
    ],
    [
      "0045da48",
      "READ",
      [
        "storage",
        "00ca4b18",
        null,
        "undefined8"
      ]
    ],
    [
      "0045dab4",
      "READ",
      [
        "storage",
        "00ca4b10",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0045da48",
      "READ",
      [
        "storage",
        "00ca4c10",
        null,
        "undefined8"
      ]
    ],
    [
      "0045da48",
      "READ",
      [
        "storage",
        "00ca4c18",
        null,
        "undefined8"
      ]
    ],
    [
      "0045dab4",
      "READ",
      [
        "storage",
        "00ca4c10",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045dac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045d9b4.md#insn-0045dac8) · [`0045dacc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045d9b4.md#insn-0045dacc) · [`0045db08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045d9b4.md#insn-0045db08)
- 新版 `0045db08`（命令位置の公開資料なし） · `0045db0c`（命令位置の公開資料なし） · `0045db48`（命令位置の公開資料なし）

~~~diff
- 0045dac8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b18:8"]]
- 0045dac8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 0045db08 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c18:8"]]
+ 0045db08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 0045dac8 bytes 138d05f9
+ 0045db08 bytes 130d06f9
- 0045dacc ["COPY", "tmp:0:4", ["const:0:4"]]
- 0045dacc ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 0045dacc ["INT_ADD", "tmp:2:8", ["register:4048:8", "const:b30:8"]]
- 0045dacc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 0045db0c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 0045db0c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 0045db0c ["INT_ADD", "tmp:2:8", ["register:4048:8", "const:c30:8"]]
+ 0045db0c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 0045dacc bytes 3fc12c39
+ 0045db0c bytes 3fc13039
- 0045db08 ["INT_ADD", "register:40f0:8", ["const:45db08:8", "const:4:8"]]
- 0045db08 ["CALL", null, ["callee:00459db4:8"]]
+ 0045db48 ["INT_ADD", "register:40f0:8", ["const:45db48:8", "const:4:8"]]
+ 0045db48 ["CALL", null, ["callee:00459db4:8"]]
- 0045db08 bytes 9bf0ff97
+ 0045db48 bytes 9bf0ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5fe96ad94c61405a6770fe4eacc06236"></a>

### [`0045de6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045de6c.md) → [`0045deac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045deac.md) FUN_0045deac

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0045db78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045db78.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 1件 [`0045dbb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045dbb8.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "0045deb8",
      "incomplete_value": false,
      "site": "0045debc",
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
      "definition_site": "0045de78",
      "incomplete_value": false,
      "site": "0045de7c",
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
      "0045deb8",
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
      "0045deb8",
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

- 旧版 [`0045de7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045de6c.md#insn-0045de7c) · [`0045de78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045de6c.md#insn-0045de78)
- 新版 `0045debc`（命令位置の公開資料なし） · `0045deb8`（命令位置の公開資料なし）

~~~diff
- 0045de7c ["INT_ADD", "register:40f0:8", ["const:45de7c:8", "const:4:8"]]
- 0045de7c ["CALL", null, ["callee:0043b7b8:8"]]
+ 0045debc ["INT_ADD", "register:40f0:8", ["const:45debc:8", "const:4:8"]]
+ 0045debc ["CALL", null, ["callee:0043b7b8:8"]]
- 0045de7c bytes 3f76ff97
+ 0045debc bytes 3f76ff97
- 0045de78 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 0045de78 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0045de78 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0045de78 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0045deb8 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 0045deb8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0045deb8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0045deb8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0045de78 bytes 00303d91
+ 0045deb8 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab18113071589bb8b5396b4747bd80fc"></a>

### [`0045de84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045de84.md) → [`0045dec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045dec4.md) FUN_0045dec4

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
      "definition_site": "0045dee8",
      "incomplete_value": false,
      "site": "0045dee8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:e40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045dea8",
      "incomplete_value": false,
      "site": "0045dea8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:d70:8"
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
      "0045dee8",
      "DATA",
      [
        "storage",
        "00c63d70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045dee8",
      "DATA",
      [
        "storage",
        "00c63e40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045de98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045de84.md#insn-0045de98) · [`0045dea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045de84.md#insn-0045dea4)
- 新版 `0045ded8`（命令位置の公開資料なし） · `0045dee4`（命令位置の公開資料なし）

~~~diff
- 0045de98 ["INT_ADD", "register:40f0:8", ["const:45de98:8", "const:4:8"]]
- 0045de98 ["CALL", null, ["callee:00c57f60:8"]]
+ 0045ded8 ["INT_ADD", "register:40f0:8", ["const:45ded8:8", "const:4:8"]]
+ 0045ded8 ["CALL", null, ["callee:00c57f60:8"]]
- 0045de98 bytes fee71f94
+ 0045ded8 bytes 22e81f94
- 0045dea4 ["COPY", "tmp:0:8", ["const:d70:8"]]
- 0045dea4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045dea4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045dea4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045dee4 ["COPY", "tmp:0:8", ["const:e40:8"]]
+ 0045dee4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045dee4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045dee4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045dea4 bytes 08c13591
+ 0045dee4 bytes 08013991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db8a05341c6d2832d8b523bcaa37d24c"></a>

### [`0045deb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045deb8.md) → [`0045def8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045def8.md) FUN_0045def8

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
      "definition_site": "0045df04",
      "incomplete_value": false,
      "site": "0045df04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:e40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045dec4",
      "incomplete_value": false,
      "site": "0045dec4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:d70:8"
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
      "0045df04",
      "DATA",
      [
        "storage",
        "00c63d70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045df04",
      "DATA",
      [
        "storage",
        "00c63e40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045dec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045deb8.md#insn-0045dec0)
- 新版 `0045df00`（命令位置の公開資料なし）

~~~diff
- 0045dec0 ["COPY", "tmp:0:8", ["const:d70:8"]]
- 0045dec0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0045dec0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0045dec0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045df00 ["COPY", "tmp:0:8", ["const:e40:8"]]
+ 0045df00 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045df00 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045df00 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0045dec0 bytes 29c13591
+ 0045df00 bytes 29013991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91cc7d9cc565385ae81900dfee5d0663"></a>

### [`0045ded4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045ded4.md) → [`0045df14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045d/0045df14.md) FUN_0045df14

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c581b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581b0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 93.91% / 新版 93.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 2件, `store_destination` 3件, `store_value` 1件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0045df68",
      "incomplete_value": true,
      "site": "0045df68",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1e5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045df28",
      "incomplete_value": true,
      "site": "0045df28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1a5:8"
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
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0045e2f4",
      "incomplete_value": false,
      "site": "0045e2f4",
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
    "old": {
      "definition_site": "0045e2b4",
      "incomplete_value": false,
      "site": "0045e2b4",
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
            "const:b70:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0045e2f8",
      "incomplete_value": false,
      "site": "0045e2f8",
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
            "const:c88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045e2b8",
      "incomplete_value": false,
      "site": "0045e2b8",
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
            "const:b88:8"
          ]
        ]
      ]
    },
    "ordinal": 30,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0045df34",
      "PARAM",
      [
        "storage",
        "00ca4b34",
        null,
        null
      ]
    ],
    [
      "0045df54",
      "READ",
      [
        "storage",
        "002b71a5",
        null,
        "string"
      ]
    ],
    [
      "0045e07c",
      "READ",
      [
        "storage",
        "00ca4b68",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0045df34",
      "PARAM",
      [
        "storage",
        "00ca4c34",
        null,
        null
      ]
    ],
    [
      "0045df54",
      "READ",
      [
        "storage",
        "002b71e5",
        null,
        "string"
      ]
    ],
    [
      "0045e07c",
      "READ",
      [
        "storage",
        "00ca4c68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045df04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045ded4.md#insn-0045df04) · [`0045df68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045ded4.md#insn-0045df68) · [`0045e2b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045d/0045ded4.md#insn-0045e2b4)
- 新版 `0045df44`（命令位置の公開資料なし） · `0045dfa8`（命令位置の公開資料なし） · `0045e2f4`（命令位置の公開資料なし）

~~~diff
- 0045df04 ["INT_ADD", "register:40f0:8", ["const:45df04:8", "const:4:8"]]
- 0045df04 ["CALL", null, ["callee:00c581b0:8"]]
+ 0045df44 ["INT_ADD", "register:40f0:8", ["const:45df44:8", "const:4:8"]]
+ 0045df44 ["CALL", null, ["callee:00c581b0:8"]]
- 0045df04 bytes 77e81f94
+ 0045df44 bytes 9be81f94
- 0045df68 ["INT_ADD", "register:40f0:8", ["const:45df68:8", "const:4:8"]]
- 0045df68 ["CALL", null, ["callee:00c57f80:8"]]
+ 0045dfa8 ["INT_ADD", "register:40f0:8", ["const:45dfa8:8", "const:4:8"]]
+ 0045dfa8 ["CALL", null, ["callee:00c57f80:8"]]
- 0045df68 bytes d2e71f94
+ 0045dfa8 bytes f6e71f94
- 0045e2b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b70:8"]]
- 0045e2b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 0045e2f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c70:8"]]
+ 0045e2f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 0045e2b4 bytes 13b905f9
+ 0045e2f4 bytes 133906f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8f703481c17e8b37183968e9c97c006"></a>

### [`0045e470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045e470.md) → [`0045e4b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045e4b0.md) FUN_0045e4b0

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
      "definition_site": "0045e4d4",
      "incomplete_value": false,
      "site": "0045e4d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:ec0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045e494",
      "incomplete_value": false,
      "site": "0045e494",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:df0:8"
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
      "0045e4d4",
      "DATA",
      [
        "storage",
        "00c63df0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045e4d4",
      "DATA",
      [
        "storage",
        "00c63ec0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045e484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045e470.md#insn-0045e484) · [`0045e490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045e470.md#insn-0045e490)
- 新版 `0045e4c4`（命令位置の公開資料なし） · `0045e4d0`（命令位置の公開資料なし）

~~~diff
- 0045e484 ["INT_ADD", "register:40f0:8", ["const:45e484:8", "const:4:8"]]
- 0045e484 ["CALL", null, ["callee:00c57f60:8"]]
+ 0045e4c4 ["INT_ADD", "register:40f0:8", ["const:45e4c4:8", "const:4:8"]]
+ 0045e4c4 ["CALL", null, ["callee:00c57f60:8"]]
- 0045e484 bytes 83e61f94
+ 0045e4c4 bytes a7e61f94
- 0045e490 ["COPY", "tmp:0:8", ["const:df0:8"]]
- 0045e490 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045e490 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045e490 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045e4d0 ["COPY", "tmp:0:8", ["const:ec0:8"]]
+ 0045e4d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045e4d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045e4d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045e490 bytes 08c13791
+ 0045e4d0 bytes 08013b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97ecb94adb44954d07489af69dee0b41"></a>

### [`0045e4a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045e4a4.md) → [`0045e4e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045e4e4.md) FUN_0045e4e4

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
      "definition_site": "0045e4f0",
      "incomplete_value": false,
      "site": "0045e4f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:ec0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045e4b0",
      "incomplete_value": false,
      "site": "0045e4b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:df0:8"
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
      "0045e4f0",
      "DATA",
      [
        "storage",
        "00c63df0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045e4f0",
      "DATA",
      [
        "storage",
        "00c63ec0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045e4ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045e4a4.md#insn-0045e4ac)
- 新版 `0045e4ec`（命令位置の公開資料なし）

~~~diff
- 0045e4ac ["COPY", "tmp:0:8", ["const:df0:8"]]
- 0045e4ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0045e4ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0045e4ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045e4ec ["COPY", "tmp:0:8", ["const:ec0:8"]]
+ 0045e4ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045e4ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045e4ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0045e4ac bytes 29c13791
+ 0045e4ec bytes 29013b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74931dac5d6c57c808862d829493e93a"></a>

### [`0045e4c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045e4c0.md) → [`0045e500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045e500.md) FUN_0045e500

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00768a28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00768/00768a28.md) [`007690c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/007690c4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00768a80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00768/00768a80.md) [`0076911c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/0076911c.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0045e608",
      "incomplete_value": false,
      "site": "0045e608",
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
    "old": {
      "definition_site": "0045e5c8",
      "incomplete_value": false,
      "site": "0045e5c8",
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
            "const:b70:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0045e60c",
      "incomplete_value": false,
      "site": "0045e60c",
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
            "const:c88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045e5cc",
      "incomplete_value": false,
      "site": "0045e5cc",
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
            "const:b88:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0045e568",
      "incomplete_value": true,
      "site": "0045e568",
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
      "definition_site": "0045e528",
      "incomplete_value": true,
      "site": "0045e528",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0045e560",
      "READ",
      [
        "storage",
        "00ca4b68",
        null,
        "undefined8"
      ]
    ],
    [
      "0045e560",
      "READ",
      [
        "storage",
        "00ca4b70",
        null,
        "undefined8"
      ]
    ],
    [
      "0045e5b4",
      "READ",
      [
        "storage",
        "00ca4b68",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0045e560",
      "READ",
      [
        "storage",
        "00ca4c68",
        null,
        "undefined8"
      ]
    ],
    [
      "0045e560",
      "READ",
      [
        "storage",
        "00ca4c70",
        null,
        "undefined8"
      ]
    ],
    [
      "0045e5b4",
      "READ",
      [
        "storage",
        "00ca4c68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045e5c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045e4c0.md#insn-0045e5c8) · [`0045e5cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045e4c0.md#insn-0045e5cc) · [`0045e608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045e4c0.md#insn-0045e608)
- 新版 `0045e608`（命令位置の公開資料なし） · `0045e60c`（命令位置の公開資料なし） · `0045e648`（命令位置の公開資料なし）

~~~diff
- 0045e5c8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b70:8"]]
- 0045e5c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 0045e608 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c70:8"]]
+ 0045e608 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 0045e5c8 bytes 13b905f9
+ 0045e608 bytes 133906f9
- 0045e5cc ["COPY", "tmp:0:4", ["const:0:4"]]
- 0045e5cc ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 0045e5cc ["INT_ADD", "tmp:2:8", ["register:4048:8", "const:b88:8"]]
- 0045e5cc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 0045e60c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 0045e60c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 0045e60c ["INT_ADD", "tmp:2:8", ["register:4048:8", "const:c88:8"]]
+ 0045e60c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 0045e5cc bytes 3f212e39
+ 0045e60c bytes 3f213239
- 0045e608 ["INT_ADD", "register:40f0:8", ["const:45e608:8", "const:4:8"]]
- 0045e608 ["CALL", null, ["callee:00459db4:8"]]
+ 0045e648 ["INT_ADD", "register:40f0:8", ["const:45e648:8", "const:4:8"]]
+ 0045e648 ["CALL", null, ["callee:00459db4:8"]]
- 0045e608 bytes dbedff97
+ 0045e648 bytes dbedff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b4fe2d56f6b5da30f6fbeaac47c7782"></a>

### [`0045e668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045e668.md) → [`0045e6a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045e6a8.md) FUN_0045e6a8

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0045f368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f368.md) · 呼出先 6件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`0045ebe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045ebe4.md) [`00597ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ecc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`0045f3a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f3a8.md) · 呼出先 6件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`0045ec24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045ec24.md) [`00597f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f0c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.64% / 新版 88.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 17件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0045e754",
      "incomplete_value": true,
      "site": "0045e764",
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
                "const:2b5000:8"
              ],
              [
                "leaf",
                "const:ed9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045e714",
      "incomplete_value": true,
      "site": "0045e724",
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
                "const:2b5000:8"
              ],
              [
                "leaf",
                "const:e99:8"
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
      "definition_site": "0045e7cc",
      "incomplete_value": true,
      "site": "0045e7cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f59:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045e78c",
      "incomplete_value": true,
      "site": "0045e78c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fa6:8"
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
      "definition_site": "0045e868",
      "incomplete_value": true,
      "site": "0045e880",
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
                "const:6a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045e828",
      "incomplete_value": true,
      "site": "0045e840",
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
                "const:660:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0045e754",
      "READ",
      [
        "storage",
        "002b5e99",
        null,
        "string"
      ]
    ],
    [
      "0045e7b8",
      "READ",
      [
        "storage",
        "002a0fa6",
        null,
        "string"
      ]
    ],
    [
      "0045e868",
      "READ",
      [
        "storage",
        "002c2660",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0045e754",
      "READ",
      [
        "storage",
        "002b5ed9",
        null,
        "string"
      ]
    ],
    [
      "0045e7b8",
      "READ",
      [
        "storage",
        "002a0f59",
        null,
        "string"
      ]
    ],
    [
      "0045e868",
      "READ",
      [
        "storage",
        "002c26a0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045e74c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045e668.md#insn-0045e74c) · [`0045e884`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045e668.md#insn-0045e884) · [`0045e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045e668.md#insn-0045e8dc)
- 新版 `0045e78c`（命令位置の公開資料なし） · `0045e8c4`（命令位置の公開資料なし）

~~~diff
- 0045e74c ["COPY", "register:0:8", ["register:4040:8"]]
- 0045e74c ["INT_ADD", "register:40f0:8", ["const:45e74c:8", "const:4:8"]]
- 0045e74c ["CALLIND", null, ["register:0:8"]]
+ 0045e78c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045e78c ["INT_ADD", "register:40f0:8", ["const:45e78c:8", "const:4:8"]]
+ 0045e78c ["CALLIND", null, ["register:0:8"]]
- 0045e74c bytes 00013fd6
+ 0045e78c bytes 00013fd6
- 0045e884 ["COPY", "tmp:0:8", ["const:651:8"]]
- 0045e884 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045e884 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045e884 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045e8c4 ["COPY", "tmp:0:8", ["const:5f5:8"]]
+ 0045e8c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045e8c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045e8c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045e884 bytes 08451991
+ 0045e8c4 bytes 08d51791
- 0045e8dc ["COPY", "register:4048:8", ["const:2c2000:8"]]
- 0045e8dc bytes 29f3ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d82bbedd2ca48f4737c7645a76dfede8"></a>

### [`0045ebe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045ebe4.md) → [`0045ec24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045ec24.md) FUN_0045ec24

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0045e668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045e668.md) · 呼出先 5件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00597ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ecc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`0045e6a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045e6a8.md) · 呼出先 5件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00597f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f0c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.03% / 新版 82.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0045ec70",
      "incomplete_value": true,
      "site": "0045ec70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a6e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045ec30",
      "incomplete_value": true,
      "site": "0045ec30",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:aca:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "0045ec74",
      "incomplete_value": true,
      "site": "0045ec74",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0045ec34",
      "incomplete_value": true,
      "site": "0045ec34",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0045ecdc",
      "incomplete_value": true,
      "site": "0045ecdc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eeb:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045ec9c",
      "incomplete_value": true,
      "site": "0045ec9c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eab:8"
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
      "0045ec60",
      "READ",
      [
        "storage",
        "002a8aca",
        null,
        "string"
      ]
    ],
    [
      "0045ec64",
      "READ",
      [
        "storage",
        "002a8ad0",
        null,
        "string"
      ]
    ],
    [
      "0045ecc8",
      "READ",
      [
        "storage",
        "002b5eab",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0045ec60",
      "READ",
      [
        "storage",
        "002a8a6e",
        null,
        "string"
      ]
    ],
    [
      "0045ec64",
      "READ",
      [
        "storage",
        "002a8a74",
        null,
        "string"
      ]
    ],
    [
      "0045ecc8",
      "READ",
      [
        "storage",
        "002b5eeb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045ecdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045ebe4.md#insn-0045ecdc) · [`0045ec18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045ebe4.md#insn-0045ec18) · [`0045ec1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045ebe4.md#insn-0045ec1c)
- 新版 `0045ed1c`（命令位置の公開資料なし） · `0045ec58`（命令位置の公開資料なし）

~~~diff
- 0045ecdc ["INT_ADD", "register:40f0:8", ["const:45ecdc:8", "const:4:8"]]
- 0045ecdc ["CALL", null, ["callee:00c57f80:8"]]
+ 0045ed1c ["INT_ADD", "register:40f0:8", ["const:45ed1c:8", "const:4:8"]]
+ 0045ed1c ["CALL", null, ["callee:00c57f80:8"]]
- 0045ecdc bytes 75e41f94
+ 0045ed1c bytes 99e41f94
- 0045ec18 ["COPY", "tmp:0:8", ["const:aca:8"]]
- 0045ec18 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0045ec18 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0045ec18 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045ec58 ["COPY", "tmp:0:8", ["const:a6e:8"]]
+ 0045ec58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045ec58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045ec58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0045ec18 bytes 29292b91
+ 0045ec58 bytes 29b92991
- 0045ec1c ["COPY", "register:40b0:8", ["register:4000:8"]]
- 0045ec1c bytes f60300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4f4db55f01086226e1a91471ab92df9"></a>

### [`0045ee1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045ee1c.md) → [`0045ee5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045ee5c.md) FUN_0045ee5c

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
      "definition_site": "0045ee60",
      "incomplete_value": false,
      "site": "0045ee64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:f40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045ee20",
      "incomplete_value": false,
      "site": "0045ee24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:e70:8"
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
      "0045ee64",
      "DATA",
      [
        "storage",
        "00c63e70",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0045ee64",
      "DATA",
      [
        "storage",
        "00c63f40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045ee20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045ee1c.md#insn-0045ee20)
- 新版 `0045ee60`（命令位置の公開資料なし）

~~~diff
- 0045ee20 ["COPY", "tmp:0:8", ["const:e70:8"]]
- 0045ee20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045ee20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045ee20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045ee60 ["COPY", "tmp:0:8", ["const:f40:8"]]
+ 0045ee60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045ee60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045ee60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045ee20 bytes 08c13991
+ 0045ee60 bytes 08013d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb34329a6480dec23a0afd2fcab79d38"></a>

### [`0045ee2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045ee2c.md) → [`0045ee6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045ee6c.md) FUN_0045ee6c

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
      "definition_site": "0045ee7c",
      "incomplete_value": false,
      "site": "0045ee84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:f40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045ee3c",
      "incomplete_value": false,
      "site": "0045ee44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:e70:8"
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
      "0045ee84",
      "DATA",
      [
        "storage",
        "00c63e70",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0045ee84",
      "DATA",
      [
        "storage",
        "00c63f40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045ee3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045ee2c.md#insn-0045ee3c) · [`0045ee48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045ee2c.md#insn-0045ee48)
- 新版 `0045ee7c`（命令位置の公開資料なし） · `0045ee88`（命令位置の公開資料なし）

~~~diff
- 0045ee3c ["COPY", "tmp:0:8", ["const:e70:8"]]
- 0045ee3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045ee3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045ee3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045ee7c ["COPY", "tmp:0:8", ["const:f40:8"]]
+ 0045ee7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045ee7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045ee7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045ee3c bytes 08c13991
+ 0045ee7c bytes 08013d91
- 0045ee48 ["INT_ADD", "register:40f0:8", ["const:45ee48:8", "const:4:8"]]
- 0045ee48 ["CALL", null, ["callee:00c57f70:8"]]
+ 0045ee88 ["INT_ADD", "register:40f0:8", ["const:45ee88:8", "const:4:8"]]
+ 0045ee88 ["CALL", null, ["callee:00c57f70:8"]]
- 0045ee48 bytes 16e41f94
+ 0045ee88 bytes 3ae41f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87018ba77068a197443632831b9fae48"></a>

### [`0045ee68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045ee68.md) → [`0045eea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045eea8.md) FUN_0045eea8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e60.md) [`00c580d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580d0.md) [`00c582f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582f0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f30.md) [`00c581a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581a0.md) [`00c583c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583c0.md) [`00c583d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.21% / 新版 84.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0045eecc",
      "incomplete_value": true,
      "site": "0045eecc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045ee8c",
      "incomplete_value": true,
      "site": "0045ee8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "0045eec0",
      "READ",
      [
        "storage",
        "00c9ac50",
        null,
        "pointer"
      ]
    ],
    [
      "0045eecc",
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
      "0045eec0",
      "READ",
      [
        "storage",
        "00c9ad20",
        null,
        "pointer"
      ]
    ],
    [
      "0045eecc",
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

- 旧版 [`0045ee80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045ee68.md#insn-0045ee80) · [`0045ee90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045ee68.md#insn-0045ee90) · [`0045ee98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045ee68.md#insn-0045ee98)
- 新版 `0045eec0`（命令位置の公開資料なし） · `0045eed0`（命令位置の公開資料なし） · `0045eed8`（命令位置の公開資料なし）

~~~diff
- 0045ee80 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c50:8"]]
- 0045ee80 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0045eec0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d20:8"]]
+ 0045eec0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0045ee80 bytes 082946f9
+ 0045eec0 bytes 089146f9
- 0045ee90 ["INT_ADD", "register:40f0:8", ["const:45ee90:8", "const:4:8"]]
- 0045ee90 ["CALL", null, ["callee:00c581a0:8"]]
+ 0045eed0 ["INT_ADD", "register:40f0:8", ["const:45eed0:8", "const:4:8"]]
+ 0045eed0 ["CALL", null, ["callee:00c581a0:8"]]
- 0045ee90 bytes 90e41f94
+ 0045eed0 bytes b4e41f94
- 0045ee98 ["INT_ADD", "register:40f0:8", ["const:45ee98:8", "const:4:8"]]
- 0045ee98 ["CALL", null, ["callee:00c57f30:8"]]
+ 0045eed8 ["INT_ADD", "register:40f0:8", ["const:45eed8:8", "const:4:8"]]
+ 0045eed8 ["CALL", null, ["callee:00c57f30:8"]]
- 0045ee98 bytes f2e31f94
+ 0045eed8 bytes 16e41f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-441e30c6bfae526859b05ec3b606df91"></a>

### [`0045eeb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045eeb4.md) → [`0045eef4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045eef4.md) FUN_0045eef4

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
      "definition_site": "0045ef18",
      "incomplete_value": true,
      "site": "0045ef18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045eed8",
      "incomplete_value": true,
      "site": "0045eed8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "0045ef0c",
      "READ",
      [
        "storage",
        "00c9ac50",
        null,
        "pointer"
      ]
    ],
    [
      "0045ef18",
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
      "0045ef0c",
      "READ",
      [
        "storage",
        "00c9ad20",
        null,
        "pointer"
      ]
    ],
    [
      "0045ef18",
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

- 旧版 [`0045eecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045eeb4.md#insn-0045eecc) · [`0045eedc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045eeb4.md#insn-0045eedc) · [`0045eee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045eeb4.md#insn-0045eee4)
- 新版 `0045ef0c`（命令位置の公開資料なし） · `0045ef1c`（命令位置の公開資料なし） · `0045ef24`（命令位置の公開資料なし）

~~~diff
- 0045eecc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c50:8"]]
- 0045eecc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0045ef0c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d20:8"]]
+ 0045ef0c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0045eecc bytes 082946f9
+ 0045ef0c bytes 089146f9
- 0045eedc ["INT_ADD", "register:40f0:8", ["const:45eedc:8", "const:4:8"]]
- 0045eedc ["CALL", null, ["callee:00c581a0:8"]]
+ 0045ef1c ["INT_ADD", "register:40f0:8", ["const:45ef1c:8", "const:4:8"]]
+ 0045ef1c ["CALL", null, ["callee:00c581a0:8"]]
- 0045eedc bytes 7de41f94
+ 0045ef1c bytes a1e41f94
- 0045eee4 ["INT_ADD", "register:40f0:8", ["const:45eee4:8", "const:4:8"]]
- 0045eee4 ["CALL", null, ["callee:00c57f30:8"]]
+ 0045ef24 ["INT_ADD", "register:40f0:8", ["const:45ef24:8", "const:4:8"]]
+ 0045ef24 ["CALL", null, ["callee:00c57f30:8"]]
- 0045eee4 bytes dfe31f94
+ 0045ef24 bytes 03e41f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d6d3460176a46b0fbc8a570b31464c2"></a>

### [`0045ef14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045ef14.md) → [`0045ef54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045ef54.md) FUN_0045ef54

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0045ee5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045ee5c.md) · 呼出先 12件 [`0045a6c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6c8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c582f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582f0.md)
- 新版 呼出元 1件 [`0045ee9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045ee9c.md) · 呼出先 12件 [`0045a708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045a/0045a708.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c583c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.52% / 新版 94.52%

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
      "definition_site": "0045eff8",
      "incomplete_value": true,
      "site": "0045effc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045efb8",
      "incomplete_value": true,
      "site": "0045efbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0045efd4",
      "incomplete_value": true,
      "site": "0045efdc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9a000:8"
              ],
              [
                "leaf",
                "const:d28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045ef94",
      "incomplete_value": true,
      "site": "0045ef9c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c9a000:8"
              ],
              [
                "leaf",
                "const:c58:8"
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
      "definition_site": "0045efd0",
      "incomplete_value": false,
      "site": "0045efdc",
      "value": [
        "leaf",
        "const:45a708:8"
      ]
    },
    "old": {
      "definition_site": "0045ef90",
      "incomplete_value": false,
      "site": "0045ef9c",
      "value": [
        "leaf",
        "const:45a6c8:8"
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
      "0045efd0",
      "PARAM",
      [
        "storage",
        "0045a6c8",
        null,
        null
      ]
    ],
    [
      "0045efd4",
      "READ",
      [
        "storage",
        "00c9ac58",
        null,
        "pointer"
      ]
    ],
    [
      "0045efd4",
      "PARAM",
      [
        "storage",
        "00c92cb0",
        "_ZTINSt6__ndk112future_errorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0045efd0",
      "PARAM",
      [
        "storage",
        "0045a708",
        null,
        null
      ]
    ],
    [
      "0045efd4",
      "READ",
      [
        "storage",
        "00c9ad28",
        null,
        "pointer"
      ]
    ],
    [
      "0045efd4",
      "PARAM",
      [
        "storage",
        "00c92d80",
        "_ZTINSt6__ndk112future_errorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045ef7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045ef14.md#insn-0045ef7c) · [`0045ef9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045ef14.md#insn-0045ef9c) · [`0045ef54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045ef14.md#insn-0045ef54)
- 新版 `0045efbc`（命令位置の公開資料なし） · `0045efdc`（命令位置の公開資料なし） · `0045ef94`（命令位置の公開資料なし）

~~~diff
- 0045ef7c ["INT_ADD", "register:40f0:8", ["const:45ef7c:8", "const:4:8"]]
- 0045ef7c ["CALL", null, ["callee:00c583f0:8"]]
+ 0045efbc ["INT_ADD", "register:40f0:8", ["const:45efbc:8", "const:4:8"]]
+ 0045efbc ["CALL", null, ["callee:00c583f0:8"]]
- 0045ef7c bytes e9e41f94
+ 0045efbc bytes 0de51f94
- 0045ef9c ["INT_ADD", "register:40f0:8", ["const:45ef9c:8", "const:4:8"]]
- 0045ef9c ["CALL", null, ["callee:00c58400:8"]]
+ 0045efdc ["INT_ADD", "register:40f0:8", ["const:45efdc:8", "const:4:8"]]
+ 0045efdc ["CALL", null, ["callee:00c58400:8"]]
- 0045ef9c bytes e5e41f94
+ 0045efdc bytes 09e51f94
- 0045ef54 ["INT_ADD", "register:40f0:8", ["const:45ef54:8", "const:4:8"]]
- 0045ef54 ["CALL", null, ["callee:00c583c0:8"]]
+ 0045ef94 ["INT_ADD", "register:40f0:8", ["const:45ef94:8", "const:4:8"]]
+ 0045ef94 ["CALL", null, ["callee:00c583c0:8"]]
- 0045ef54 bytes e7e41f94
+ 0045ef94 bytes 0be51f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07d4449b1edb179093e8332824ef10ad"></a>

### [`0045f138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f138.md) → [`0045f178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f178.md) FUN_0045f178

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
      "definition_site": "0045f184",
      "incomplete_value": false,
      "site": "0045f190",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:fe8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045f144",
      "incomplete_value": false,
      "site": "0045f150",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:f18:8"
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
      "0045f190",
      "DATA",
      [
        "storage",
        "00c63f18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045f190",
      "DATA",
      [
        "storage",
        "00c63fe8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045f144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f138.md#insn-0045f144)
- 新版 `0045f184`（命令位置の公開資料なし）

~~~diff
- 0045f144 ["COPY", "tmp:0:8", ["const:f18:8"]]
- 0045f144 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0045f144 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0045f144 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0045f184 ["COPY", "tmp:0:8", ["const:fe8:8"]]
+ 0045f184 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0045f184 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0045f184 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0045f144 bytes 4a613c91
+ 0045f184 bytes 4aa13f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e24890f73dc2ae5ce64358aa7c63d302"></a>

### [`0045f17c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f17c.md) → [`0045f1bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f1bc.md) FUN_0045f1bc

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
      "definition_site": "0045f1d4",
      "incomplete_value": false,
      "site": "0045f1e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:fe8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045f194",
      "incomplete_value": false,
      "site": "0045f1a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:f18:8"
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
      "0045f1e0",
      "DATA",
      [
        "storage",
        "00c63f18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045f1e0",
      "DATA",
      [
        "storage",
        "00c63fe8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045f194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f17c.md#insn-0045f194) · [`0045f1c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f17c.md#insn-0045f1c4)
- 新版 `0045f1d4`（命令位置の公開資料なし） · `0045f204`（命令位置の公開資料なし）

~~~diff
- 0045f194 ["COPY", "tmp:0:8", ["const:f18:8"]]
- 0045f194 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045f194 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045f194 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045f1d4 ["COPY", "tmp:0:8", ["const:fe8:8"]]
+ 0045f1d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f1d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f1d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045f194 bytes 08613c91
+ 0045f1d4 bytes 08a13f91
- 0045f1c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045f1c4 ["INT_ADD", "register:40f0:8", ["const:45f1c4:8", "const:4:8"]]
- 0045f1c4 ["CALLIND", null, ["register:0:8"]]
+ 0045f204 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045f204 ["INT_ADD", "register:40f0:8", ["const:45f204:8", "const:4:8"]]
+ 0045f204 ["CALLIND", null, ["register:0:8"]]
- 0045f1c4 bytes 00013fd6
+ 0045f204 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71462e285c746fe74fab9bace2e33670"></a>

### [`0045f1d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f1d8.md) → [`0045f218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f218.md) FUN_0045f218

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.55% / 新版 93.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0045f244",
      "incomplete_value": false,
      "site": "0045f244",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:fe8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045f204",
      "incomplete_value": false,
      "site": "0045f204",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:f18:8"
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
      "0045f244",
      "DATA",
      [
        "storage",
        "00c63f18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045f244",
      "DATA",
      [
        "storage",
        "00c63fe8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045f1ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f1d8.md#insn-0045f1ec) · [`0045f1fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f1d8.md#insn-0045f1fc) · [`0045f220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f1d8.md#insn-0045f220)
- 新版 `0045f22c`（命令位置の公開資料なし） · `0045f23c`（命令位置の公開資料なし） · `0045f260`（命令位置の公開資料なし）

~~~diff
- 0045f1ec ["INT_ADD", "register:40f0:8", ["const:45f1ec:8", "const:4:8"]]
- 0045f1ec ["CALL", null, ["callee:00c57f60:8"]]
+ 0045f22c ["INT_ADD", "register:40f0:8", ["const:45f22c:8", "const:4:8"]]
+ 0045f22c ["CALL", null, ["callee:00c57f60:8"]]
- 0045f1ec bytes 29e31f94
+ 0045f22c bytes 4de31f94
- 0045f1fc ["COPY", "tmp:0:8", ["const:f18:8"]]
- 0045f1fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045f1fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045f1fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045f23c ["COPY", "tmp:0:8", ["const:fe8:8"]]
+ 0045f23c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f23c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f23c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045f1fc bytes 08613c91
+ 0045f23c bytes 08a13f91
- 0045f220 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045f220 ["INT_ADD", "register:40f0:8", ["const:45f220:8", "const:4:8"]]
- 0045f220 ["CALLIND", null, ["register:0:8"]]
+ 0045f260 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045f260 ["INT_ADD", "register:40f0:8", ["const:45f260:8", "const:4:8"]]
+ 0045f260 ["CALLIND", null, ["register:0:8"]]
- 0045f220 bytes 00013fd6
+ 0045f260 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebd15b9d9765bf1f76f80a968269708c"></a>

### [`0045f268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f268.md) → [`0045f2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f2a8.md) FUN_0045f2a8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "0045f2c8",
      "incomplete_value": false,
      "site": "0045f2c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:fe8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045f288",
      "incomplete_value": false,
      "site": "0045f288",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:f18:8"
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
      "0045f2c8",
      "DATA",
      [
        "storage",
        "00c63f18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045f2c8",
      "DATA",
      [
        "storage",
        "00c63fe8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045f2c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f268.md#insn-0045f2c8) · [`0045f284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f268.md#insn-0045f284) · [`0045f2a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f268.md#insn-0045f2a4)
- 新版 `0045f308`（命令位置の公開資料なし） · `0045f2c4`（命令位置の公開資料なし） · `0045f2e4`（命令位置の公開資料なし）

~~~diff
- 0045f2c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045f2c8 ["INT_ADD", "register:40f0:8", ["const:45f2c8:8", "const:4:8"]]
- 0045f2c8 ["CALLIND", null, ["register:0:8"]]
+ 0045f308 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045f308 ["INT_ADD", "register:40f0:8", ["const:45f308:8", "const:4:8"]]
+ 0045f308 ["CALLIND", null, ["register:0:8"]]
- 0045f2c8 bytes 00013fd6
+ 0045f308 bytes 00013fd6
- 0045f284 ["COPY", "tmp:0:8", ["const:f18:8"]]
- 0045f284 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045f284 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045f284 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045f2c4 ["COPY", "tmp:0:8", ["const:fe8:8"]]
+ 0045f2c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f2c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f2c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045f284 bytes 08613c91
+ 0045f2c4 bytes 08a13f91
- 0045f2a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045f2a4 ["INT_ADD", "register:40f0:8", ["const:45f2a4:8", "const:4:8"]]
- 0045f2a4 ["CALLIND", null, ["register:0:8"]]
+ 0045f2e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045f2e4 ["INT_ADD", "register:40f0:8", ["const:45f2e4:8", "const:4:8"]]
+ 0045f2e4 ["CALLIND", null, ["register:0:8"]]
- 0045f2a4 bytes 00013fd6
+ 0045f2e4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80990882a9c9ce53f268ba8f914f76ba"></a>

### [`0045f368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f368.md) → [`0045f3a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f3a8.md) FUN_0045f3a8

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0045e668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045e/0045e668.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`0045e6a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045e/0045e6a8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.00% / 新版 98.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0045f454",
      "incomplete_value": true,
      "site": "0045f454",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:de3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045f414",
      "incomplete_value": true,
      "site": "0045f414",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e30:8"
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
      "0045f440",
      "READ",
      [
        "storage",
        "002a1e30",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0045f440",
      "READ",
      [
        "storage",
        "002a1de3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045f454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f368.md#insn-0045f454) · [`0045f3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f368.md#insn-0045f3c0) · [`0045f3ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f368.md#insn-0045f3ec)
- 新版 `0045f494`（命令位置の公開資料なし） · `0045f400`（命令位置の公開資料なし） · `0045f42c`（命令位置の公開資料なし）

~~~diff
- 0045f454 ["INT_ADD", "register:40f0:8", ["const:45f454:8", "const:4:8"]]
- 0045f454 ["CALL", null, ["callee:00c57f80:8"]]
+ 0045f494 ["INT_ADD", "register:40f0:8", ["const:45f494:8", "const:4:8"]]
+ 0045f494 ["CALL", null, ["callee:00c57f80:8"]]
- 0045f454 bytes 97e21f94
+ 0045f494 bytes bbe21f94
- 0045f3c0 ["INT_ADD", "register:40f0:8", ["const:45f3c0:8", "const:4:8"]]
- 0045f3c0 ["CALL", null, ["callee:004410cc:8"]]
+ 0045f400 ["INT_ADD", "register:40f0:8", ["const:45f400:8", "const:4:8"]]
+ 0045f400 ["CALL", null, ["callee:004410cc:8"]]
- 0045f3c0 bytes 3387ff97
+ 0045f400 bytes 3387ff97
- 0045f3ec ["INT_ADD", "register:40f0:8", ["const:45f3ec:8", "const:4:8"]]
- 0045f3ec ["CALL", null, ["callee:00c57f80:8"]]
+ 0045f42c ["INT_ADD", "register:40f0:8", ["const:45f42c:8", "const:4:8"]]
+ 0045f42c ["CALL", null, ["callee:00c57f80:8"]]
- 0045f3ec bytes b1e21f94
+ 0045f42c bytes d5e21f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2008afe167c0fb272fb3d4a79dcae8aa"></a>

### [`0045f62c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f62c.md) → [`0045f66c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f66c.md) FUN_0045f66c

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
      "definition_site": "0045f678",
      "incomplete_value": false,
      "site": "0045f684",
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
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045f638",
      "incomplete_value": false,
      "site": "0045f644",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:f98:8"
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
      "0045f684",
      "DATA",
      [
        "storage",
        "00c63f98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045f684",
      "DATA",
      [
        "storage",
        "00c64068",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045f634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f62c.md#insn-0045f634) · [`0045f638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f62c.md#insn-0045f638)
- 新版 `0045f674`（命令位置の公開資料なし） · `0045f678`（命令位置の公開資料なし）

~~~diff
- 0045f634 ["COPY", "register:4050:8", ["const:c63000:8"]]
+ 0045f674 ["COPY", "register:4050:8", ["const:c64000:8"]]
- 0045f634 bytes 2a400090
+ 0045f674 bytes 2a4000b0
- 0045f638 ["COPY", "tmp:0:8", ["const:f98:8"]]
- 0045f638 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0045f638 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0045f638 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0045f678 ["COPY", "tmp:0:8", ["const:68:8"]]
+ 0045f678 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0045f678 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0045f678 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0045f638 bytes 4a613e91
+ 0045f678 bytes 4aa10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7eed076c4be5ed076e04b862a1169130"></a>

### [`0045f670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f670.md) → [`0045f6b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f6b0.md) FUN_0045f6b0

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
      "definition_site": "0045f6c8",
      "incomplete_value": false,
      "site": "0045f6d4",
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
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045f688",
      "incomplete_value": false,
      "site": "0045f694",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:f98:8"
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
      "0045f6d4",
      "DATA",
      [
        "storage",
        "00c63f98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045f6d4",
      "DATA",
      [
        "storage",
        "00c64068",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045f684`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f670.md#insn-0045f684) · [`0045f688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f670.md#insn-0045f688) · [`0045f6b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f670.md#insn-0045f6b8)
- 新版 `0045f6c4`（命令位置の公開資料なし） · `0045f6c8`（命令位置の公開資料なし） · `0045f6f8`（命令位置の公開資料なし）

~~~diff
- 0045f684 ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 0045f6c4 ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0045f684 bytes 28400090
+ 0045f6c4 bytes 284000b0
- 0045f688 ["COPY", "tmp:0:8", ["const:f98:8"]]
- 0045f688 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045f688 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045f688 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045f6c8 ["COPY", "tmp:0:8", ["const:68:8"]]
+ 0045f6c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f6c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f6c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045f688 bytes 08613e91
+ 0045f6c8 bytes 08a10191
- 0045f6b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045f6b8 ["INT_ADD", "register:40f0:8", ["const:45f6b8:8", "const:4:8"]]
- 0045f6b8 ["CALLIND", null, ["register:0:8"]]
+ 0045f6f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045f6f8 ["INT_ADD", "register:40f0:8", ["const:45f6f8:8", "const:4:8"]]
+ 0045f6f8 ["CALLIND", null, ["register:0:8"]]
- 0045f6b8 bytes 00013fd6
+ 0045f6f8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d70b284f295fdf4faa5c7f5357fa4cd"></a>

### [`0045f6cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f6cc.md) → [`0045f70c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f70c.md) FUN_0045f70c

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
      "definition_site": "0045f738",
      "incomplete_value": false,
      "site": "0045f738",
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
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045f6f8",
      "incomplete_value": false,
      "site": "0045f6f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:f98:8"
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
      "0045f738",
      "DATA",
      [
        "storage",
        "00c63f98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045f738",
      "DATA",
      [
        "storage",
        "00c64068",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045f6e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f6cc.md#insn-0045f6e0) · [`0045f6ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f6cc.md#insn-0045f6ec) · [`0045f6f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f6cc.md#insn-0045f6f0)
- 新版 `0045f720`（命令位置の公開資料なし） · `0045f72c`（命令位置の公開資料なし） · `0045f730`（命令位置の公開資料なし）

~~~diff
- 0045f6e0 ["INT_ADD", "register:40f0:8", ["const:45f6e0:8", "const:4:8"]]
- 0045f6e0 ["CALL", null, ["callee:00c57f60:8"]]
+ 0045f720 ["INT_ADD", "register:40f0:8", ["const:45f720:8", "const:4:8"]]
+ 0045f720 ["CALL", null, ["callee:00c57f60:8"]]
- 0045f6e0 bytes ece11f94
+ 0045f720 bytes 10e21f94
- 0045f6ec ["COPY", "register:4040:8", ["const:c63000:8"]]
+ 0045f72c ["COPY", "register:4040:8", ["const:c64000:8"]]
- 0045f6ec bytes 28400090
+ 0045f72c bytes 284000b0
- 0045f6f0 ["COPY", "tmp:0:8", ["const:f98:8"]]
- 0045f6f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045f6f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045f6f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045f730 ["COPY", "tmp:0:8", ["const:68:8"]]
+ 0045f730 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f730 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f730 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045f6f0 bytes 08613e91
+ 0045f730 bytes 08a10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e21318a1d1abadbb7529e2752d2ec43"></a>

### [`0045f754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f754.md) → [`0045f794`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f794.md) FUN_0045f794

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
      "definition_site": "0045f7b0",
      "incomplete_value": false,
      "site": "0045f7b0",
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
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045f770",
      "incomplete_value": false,
      "site": "0045f770",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c63000:8"
          ],
          [
            "leaf",
            "const:f98:8"
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
      "0045f7b0",
      "DATA",
      [
        "storage",
        "00c63f98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045f7b0",
      "DATA",
      [
        "storage",
        "00c64068",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045f768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f754.md#insn-0045f768) · [`0045f76c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f754.md#insn-0045f76c) · [`0045f790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f754.md#insn-0045f790)
- 新版 `0045f7a8`（命令位置の公開資料なし） · `0045f7ac`（命令位置の公開資料なし） · `0045f7d0`（命令位置の公開資料なし）

~~~diff
- 0045f768 ["COPY", "register:4048:8", ["const:c63000:8"]]
+ 0045f7a8 ["COPY", "register:4048:8", ["const:c64000:8"]]
- 0045f768 bytes 29400090
+ 0045f7a8 bytes 294000b0
- 0045f76c ["COPY", "tmp:0:8", ["const:f98:8"]]
- 0045f76c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0045f76c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0045f76c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045f7ac ["COPY", "tmp:0:8", ["const:68:8"]]
+ 0045f7ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045f7ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045f7ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0045f76c bytes 29613e91
+ 0045f7ac bytes 29a10191
- 0045f790 ["COPY", "register:0:8", ["register:4048:8"]]
- 0045f790 ["INT_ADD", "register:40f0:8", ["const:45f790:8", "const:4:8"]]
- 0045f790 ["CALLIND", null, ["register:0:8"]]
+ 0045f7d0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0045f7d0 ["INT_ADD", "register:40f0:8", ["const:45f7d0:8", "const:4:8"]]
+ 0045f7d0 ["CALLIND", null, ["register:0:8"]]
- 0045f790 bytes 20013fd6
+ 0045f7d0 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f347e32492612c8332332139c407f6ef"></a>

### [`0045f900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f900.md) → [`0045f940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f940.md) FUN_0045f940

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
      "definition_site": "0045f954",
      "incomplete_value": false,
      "site": "0045f958",
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
            "const:e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045f914",
      "incomplete_value": false,
      "site": "0045f918",
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
            "const:18:8"
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
      "0045f958",
      "DATA",
      [
        "storage",
        "00c64018",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045f958",
      "DATA",
      [
        "storage",
        "00c640e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045f914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f900.md#insn-0045f914) · [`0045f928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f900.md#insn-0045f928) · [`0045f948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f900.md#insn-0045f948)
- 新版 `0045f954`（命令位置の公開資料なし） · `0045f968`（命令位置の公開資料なし） · `0045f988`（命令位置の公開資料なし）

~~~diff
- 0045f914 ["COPY", "tmp:0:8", ["const:18:8"]]
- 0045f914 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045f914 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045f914 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045f954 ["COPY", "tmp:0:8", ["const:e8:8"]]
+ 0045f954 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f954 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f954 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045f914 bytes 08610091
+ 0045f954 bytes 08a10391
- 0045f928 ["INT_ADD", "register:40f0:8", ["const:45f928:8", "const:4:8"]]
- 0045f928 ["CALL", null, ["callee:00c53da0:8"]]
+ 0045f968 ["INT_ADD", "register:40f0:8", ["const:45f968:8", "const:4:8"]]
+ 0045f968 ["CALL", null, ["callee:00c53da0:8"]]
- 0045f928 bytes f6d01f94
+ 0045f968 bytes 0ed11f94
- 0045f948 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045f948 ["INT_ADD", "register:40f0:8", ["const:45f948:8", "const:4:8"]]
- 0045f948 ["CALLIND", null, ["register:0:8"]]
+ 0045f988 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045f988 ["INT_ADD", "register:40f0:8", ["const:45f988:8", "const:4:8"]]
+ 0045f988 ["CALLIND", null, ["register:0:8"]]
- 0045f948 bytes 00013fd6
+ 0045f988 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d240fe1390cdcd68bb2638ae4c7feb56"></a>

### [`0045f95c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f95c.md) → [`0045f99c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f99c.md) FUN_0045f99c

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
      "definition_site": "0045f9b4",
      "incomplete_value": false,
      "site": "0045f9b8",
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
            "const:e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045f974",
      "incomplete_value": false,
      "site": "0045f978",
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
            "const:18:8"
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
      "0045f9b8",
      "DATA",
      [
        "storage",
        "00c64018",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045f9b8",
      "DATA",
      [
        "storage",
        "00c640e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045f974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f95c.md#insn-0045f974) · [`0045f988`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f95c.md#insn-0045f988) · [`0045f99c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f95c.md#insn-0045f99c)
- 新版 `0045f9b4`（命令位置の公開資料なし） · `0045f9c8`（命令位置の公開資料なし） · `0045f9dc`（命令位置の公開資料なし）

~~~diff
- 0045f974 ["COPY", "tmp:0:8", ["const:18:8"]]
- 0045f974 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045f974 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045f974 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045f9b4 ["COPY", "tmp:0:8", ["const:e8:8"]]
+ 0045f9b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f9b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045f9b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045f974 bytes 08610091
+ 0045f9b4 bytes 08a10391
- 0045f988 ["INT_ADD", "register:40f0:8", ["const:45f988:8", "const:4:8"]]
- 0045f988 ["CALL", null, ["callee:00c53da0:8"]]
+ 0045f9c8 ["INT_ADD", "register:40f0:8", ["const:45f9c8:8", "const:4:8"]]
+ 0045f9c8 ["CALL", null, ["callee:00c53da0:8"]]
- 0045f988 bytes ded01f94
+ 0045f9c8 bytes f6d01f94
- 0045f99c ["COPY", "register:0:8", ["register:4040:8"]]
- 0045f99c ["INT_ADD", "register:40f0:8", ["const:45f99c:8", "const:4:8"]]
- 0045f99c ["CALLIND", null, ["register:0:8"]]
+ 0045f9dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045f9dc ["INT_ADD", "register:40f0:8", ["const:45f9dc:8", "const:4:8"]]
+ 0045f9dc ["CALLIND", null, ["register:0:8"]]
- 0045f99c bytes 00013fd6
+ 0045f9dc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a841387507d70dec2543b32a40061926"></a>

### [`0045f9b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f9b8.md) → [`0045f9f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045f9f8.md) FUN_0045f9f8

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
      "definition_site": "0045fa1c",
      "incomplete_value": false,
      "site": "0045fa1c",
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
            "const:e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045f9dc",
      "incomplete_value": false,
      "site": "0045f9dc",
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
            "const:18:8"
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
      "0045fa1c",
      "DATA",
      [
        "storage",
        "00c64018",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045fa1c",
      "DATA",
      [
        "storage",
        "00c640e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045f9cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f9b8.md#insn-0045f9cc) · [`0045f9d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f9b8.md#insn-0045f9d8) · [`0045f9f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045f9b8.md#insn-0045f9f4)
- 新版 `0045fa0c`（命令位置の公開資料なし） · `0045fa18`（命令位置の公開資料なし） · `0045fa34`（命令位置の公開資料なし）

~~~diff
- 0045f9cc ["INT_ADD", "register:40f0:8", ["const:45f9cc:8", "const:4:8"]]
- 0045f9cc ["CALL", null, ["callee:00c57f60:8"]]
+ 0045fa0c ["INT_ADD", "register:40f0:8", ["const:45fa0c:8", "const:4:8"]]
+ 0045fa0c ["CALL", null, ["callee:00c57f60:8"]]
- 0045f9cc bytes 31e11f94
+ 0045fa0c bytes 55e11f94
- 0045f9d8 ["COPY", "tmp:0:8", ["const:18:8"]]
- 0045f9d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0045f9d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0045f9d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045fa18 ["COPY", "tmp:0:8", ["const:e8:8"]]
+ 0045fa18 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045fa18 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045fa18 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0045f9d8 bytes 29610091
+ 0045fa18 bytes 29a10391
- 0045f9f4 ["INT_ADD", "register:40f0:8", ["const:45f9f4:8", "const:4:8"]]
- 0045f9f4 ["CALL", null, ["callee:00c53d70:8"]]
+ 0045fa34 ["INT_ADD", "register:40f0:8", ["const:45fa34:8", "const:4:8"]]
+ 0045fa34 ["CALL", null, ["callee:00c53d70:8"]]
- 0045f9f4 bytes b7d01f94
+ 0045fa34 bytes cfd01f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a8800fd1b8b4b46b8f50653ae8d3168"></a>

### [`0045fa08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fa08.md) → [`0045fa48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045fa48.md) FUN_0045fa48

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
      "definition_site": "0045fa54",
      "incomplete_value": false,
      "site": "0045fa54",
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
            "const:e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045fa14",
      "incomplete_value": false,
      "site": "0045fa14",
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
            "const:18:8"
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
      "0045fa54",
      "DATA",
      [
        "storage",
        "00c64018",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045fa54",
      "DATA",
      [
        "storage",
        "00c640e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045fa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fa08.md#insn-0045fa10) · [`0045fa30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fa08.md#insn-0045fa30)
- 新版 `0045fa50`（命令位置の公開資料なし） · `0045fa70`（命令位置の公開資料なし）

~~~diff
- 0045fa10 ["COPY", "tmp:0:8", ["const:18:8"]]
- 0045fa10 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0045fa10 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0045fa10 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045fa50 ["COPY", "tmp:0:8", ["const:e8:8"]]
+ 0045fa50 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045fa50 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045fa50 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0045fa10 bytes 29610091
+ 0045fa50 bytes 29a10391
- 0045fa30 ["INT_ADD", "register:40f0:8", ["const:45fa30:8", "const:4:8"]]
- 0045fa30 ["CALL", null, ["callee:00c53d70:8"]]
+ 0045fa70 ["INT_ADD", "register:40f0:8", ["const:45fa70:8", "const:4:8"]]
+ 0045fa70 ["CALL", null, ["callee:00c53d70:8"]]
- 0045fa30 bytes a8d01f94
+ 0045fa70 bytes c0d01f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ddc7bb70e06754f32588722b58f2dda5"></a>

### [`0045fb9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fb9c.md) → [`0045fbdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045fbdc.md) FUN_0045fbdc

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
      "definition_site": "0045fbe8",
      "incomplete_value": false,
      "site": "0045fbf4",
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
            "const:168:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045fba8",
      "incomplete_value": false,
      "site": "0045fbb4",
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
            "const:98:8"
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
      "0045fbf4",
      "DATA",
      [
        "storage",
        "00c64098",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045fbf4",
      "DATA",
      [
        "storage",
        "00c64168",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045fba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fb9c.md#insn-0045fba8)
- 新版 `0045fbe8`（命令位置の公開資料なし）

~~~diff
- 0045fba8 ["COPY", "tmp:0:8", ["const:98:8"]]
- 0045fba8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0045fba8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0045fba8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0045fbe8 ["COPY", "tmp:0:8", ["const:168:8"]]
+ 0045fbe8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0045fbe8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0045fbe8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0045fba8 bytes 4a610291
+ 0045fbe8 bytes 4aa10591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6400a7f890becc0052a0b48d158b99bc"></a>

### [`0045fbe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fbe0.md) → [`0045fc20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045fc20.md) FUN_0045fc20

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
      "definition_site": "0045fc38",
      "incomplete_value": false,
      "site": "0045fc44",
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
            "const:168:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045fbf8",
      "incomplete_value": false,
      "site": "0045fc04",
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
            "const:98:8"
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
      "0045fc44",
      "DATA",
      [
        "storage",
        "00c64098",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045fc44",
      "DATA",
      [
        "storage",
        "00c64168",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045fbf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fbe0.md#insn-0045fbf8) · [`0045fc28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fbe0.md#insn-0045fc28)
- 新版 `0045fc38`（命令位置の公開資料なし） · `0045fc68`（命令位置の公開資料なし）

~~~diff
- 0045fbf8 ["COPY", "tmp:0:8", ["const:98:8"]]
- 0045fbf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045fbf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045fbf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045fc38 ["COPY", "tmp:0:8", ["const:168:8"]]
+ 0045fc38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045fc38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045fc38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045fbf8 bytes 08610291
+ 0045fc38 bytes 08a10591
- 0045fc28 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045fc28 ["INT_ADD", "register:40f0:8", ["const:45fc28:8", "const:4:8"]]
- 0045fc28 ["CALLIND", null, ["register:0:8"]]
+ 0045fc68 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045fc68 ["INT_ADD", "register:40f0:8", ["const:45fc68:8", "const:4:8"]]
+ 0045fc68 ["CALLIND", null, ["register:0:8"]]
- 0045fc28 bytes 00013fd6
+ 0045fc68 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf1373dccfbfa11810a1e593c4589f00"></a>

### [`0045fc3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fc3c.md) → [`0045fc7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045fc7c.md) FUN_0045fc7c

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
      "definition_site": "0045fca8",
      "incomplete_value": false,
      "site": "0045fca8",
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
            "const:168:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045fc68",
      "incomplete_value": false,
      "site": "0045fc68",
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
            "const:98:8"
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
      "0045fca8",
      "DATA",
      [
        "storage",
        "00c64098",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045fca8",
      "DATA",
      [
        "storage",
        "00c64168",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045fc50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fc3c.md#insn-0045fc50) · [`0045fc60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fc3c.md#insn-0045fc60) · [`0045fc84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fc3c.md#insn-0045fc84)
- 新版 `0045fc90`（命令位置の公開資料なし） · `0045fca0`（命令位置の公開資料なし） · `0045fcc4`（命令位置の公開資料なし）

~~~diff
- 0045fc50 ["INT_ADD", "register:40f0:8", ["const:45fc50:8", "const:4:8"]]
- 0045fc50 ["CALL", null, ["callee:00c57f60:8"]]
+ 0045fc90 ["INT_ADD", "register:40f0:8", ["const:45fc90:8", "const:4:8"]]
+ 0045fc90 ["CALL", null, ["callee:00c57f60:8"]]
- 0045fc50 bytes 90e01f94
+ 0045fc90 bytes b4e01f94
- 0045fc60 ["COPY", "tmp:0:8", ["const:98:8"]]
- 0045fc60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045fc60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045fc60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045fca0 ["COPY", "tmp:0:8", ["const:168:8"]]
+ 0045fca0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045fca0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045fca0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045fc60 bytes 08610291
+ 0045fca0 bytes 08a10591
- 0045fc84 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045fc84 ["INT_ADD", "register:40f0:8", ["const:45fc84:8", "const:4:8"]]
- 0045fc84 ["CALLIND", null, ["register:0:8"]]
+ 0045fcc4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045fcc4 ["INT_ADD", "register:40f0:8", ["const:45fcc4:8", "const:4:8"]]
+ 0045fcc4 ["CALLIND", null, ["register:0:8"]]
- 0045fc84 bytes 00013fd6
+ 0045fcc4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc48668b75356a97b1fae1d699fa2b62"></a>

### [`0045fcc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fcc4.md) → [`0045fd04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045fd04.md) FUN_0045fd04

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
      "definition_site": "0045fd20",
      "incomplete_value": false,
      "site": "0045fd20",
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
            "const:168:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045fce0",
      "incomplete_value": false,
      "site": "0045fce0",
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
            "const:98:8"
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
      "0045fd20",
      "DATA",
      [
        "storage",
        "00c64098",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045fd20",
      "DATA",
      [
        "storage",
        "00c64168",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045fcdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fcc4.md#insn-0045fcdc) · [`0045fd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fcc4.md#insn-0045fd00)
- 新版 `0045fd1c`（命令位置の公開資料なし） · `0045fd40`（命令位置の公開資料なし）

~~~diff
- 0045fcdc ["COPY", "tmp:0:8", ["const:98:8"]]
- 0045fcdc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0045fcdc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0045fcdc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045fd1c ["COPY", "tmp:0:8", ["const:168:8"]]
+ 0045fd1c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045fd1c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045fd1c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0045fcdc bytes 29610291
+ 0045fd1c bytes 29a10591
- 0045fd00 ["COPY", "register:0:8", ["register:4048:8"]]
- 0045fd00 ["INT_ADD", "register:40f0:8", ["const:45fd00:8", "const:4:8"]]
- 0045fd00 ["CALLIND", null, ["register:0:8"]]
+ 0045fd40 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0045fd40 ["INT_ADD", "register:40f0:8", ["const:45fd40:8", "const:4:8"]]
+ 0045fd40 ["CALLIND", null, ["register:0:8"]]
- 0045fd00 bytes 20013fd6
+ 0045fd40 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a5bad052e123d9c23a19dd324c261b1"></a>

### [`0045fe08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fe08.md) → [`0045fe48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045fe48.md) FUN_0045fe48

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
      "definition_site": "0045fe54",
      "incomplete_value": false,
      "site": "0045fe60",
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
            "const:1e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045fe14",
      "incomplete_value": false,
      "site": "0045fe20",
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
            "const:118:8"
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
      "0045fe60",
      "DATA",
      [
        "storage",
        "00c64118",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045fe60",
      "DATA",
      [
        "storage",
        "00c641e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045fe14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fe08.md#insn-0045fe14)
- 新版 `0045fe54`（命令位置の公開資料なし）

~~~diff
- 0045fe14 ["COPY", "tmp:0:8", ["const:118:8"]]
- 0045fe14 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0045fe14 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0045fe14 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0045fe54 ["COPY", "tmp:0:8", ["const:1e8:8"]]
+ 0045fe54 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0045fe54 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0045fe54 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0045fe14 bytes 4a610491
+ 0045fe54 bytes 4aa10791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b4aefbc47070bc073dbbd979bd7ff4f"></a>

### [`0045fe4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fe4c.md) → [`0045fe8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045fe8c.md) FUN_0045fe8c

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
      "definition_site": "0045fea4",
      "incomplete_value": false,
      "site": "0045feb0",
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
            "const:1e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045fe64",
      "incomplete_value": false,
      "site": "0045fe70",
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
            "const:118:8"
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
      "0045feb0",
      "DATA",
      [
        "storage",
        "00c64118",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045feb0",
      "DATA",
      [
        "storage",
        "00c641e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045fe64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fe4c.md#insn-0045fe64) · [`0045fe94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fe4c.md#insn-0045fe94)
- 新版 `0045fea4`（命令位置の公開資料なし） · `0045fed4`（命令位置の公開資料なし）

~~~diff
- 0045fe64 ["COPY", "tmp:0:8", ["const:118:8"]]
- 0045fe64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045fe64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045fe64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045fea4 ["COPY", "tmp:0:8", ["const:1e8:8"]]
+ 0045fea4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045fea4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045fea4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045fe64 bytes 08610491
+ 0045fea4 bytes 08a10791
- 0045fe94 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045fe94 ["INT_ADD", "register:40f0:8", ["const:45fe94:8", "const:4:8"]]
- 0045fe94 ["CALLIND", null, ["register:0:8"]]
+ 0045fed4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045fed4 ["INT_ADD", "register:40f0:8", ["const:45fed4:8", "const:4:8"]]
+ 0045fed4 ["CALLIND", null, ["register:0:8"]]
- 0045fe94 bytes 00013fd6
+ 0045fed4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f7d433682da45c651292e2d17cf4d7e"></a>

### [`0045fea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fea8.md) → [`0045fee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045fee8.md) FUN_0045fee8

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
      "definition_site": "0045ff14",
      "incomplete_value": false,
      "site": "0045ff14",
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
            "const:1e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045fed4",
      "incomplete_value": false,
      "site": "0045fed4",
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
            "const:118:8"
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
      "0045ff14",
      "DATA",
      [
        "storage",
        "00c64118",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045ff14",
      "DATA",
      [
        "storage",
        "00c641e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045febc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fea8.md#insn-0045febc) · [`0045fecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fea8.md#insn-0045fecc) · [`0045fef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045fea8.md#insn-0045fef0)
- 新版 `0045fefc`（命令位置の公開資料なし） · `0045ff0c`（命令位置の公開資料なし） · `0045ff30`（命令位置の公開資料なし）

~~~diff
- 0045febc ["INT_ADD", "register:40f0:8", ["const:45febc:8", "const:4:8"]]
- 0045febc ["CALL", null, ["callee:00c57f60:8"]]
+ 0045fefc ["INT_ADD", "register:40f0:8", ["const:45fefc:8", "const:4:8"]]
+ 0045fefc ["CALL", null, ["callee:00c57f60:8"]]
- 0045febc bytes f5df1f94
+ 0045fefc bytes 19e01f94
- 0045fecc ["COPY", "tmp:0:8", ["const:118:8"]]
- 0045fecc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0045fecc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0045fecc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0045ff0c ["COPY", "tmp:0:8", ["const:1e8:8"]]
+ 0045ff0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0045ff0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0045ff0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0045fecc bytes 08610491
+ 0045ff0c bytes 08a10791
- 0045fef0 ["COPY", "register:0:8", ["register:4040:8"]]
- 0045fef0 ["INT_ADD", "register:40f0:8", ["const:45fef0:8", "const:4:8"]]
- 0045fef0 ["CALLIND", null, ["register:0:8"]]
+ 0045ff30 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0045ff30 ["INT_ADD", "register:40f0:8", ["const:45ff30:8", "const:4:8"]]
+ 0045ff30 ["CALLIND", null, ["register:0:8"]]
- 0045fef0 bytes 00013fd6
+ 0045ff30 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a17570742ab08a7c5b4f1372e205129a"></a>

### [`0045ff30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045ff30.md) → [`0045ff70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0045f/0045ff70.md) FUN_0045ff70

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
      "definition_site": "0045ff8c",
      "incomplete_value": false,
      "site": "0045ff8c",
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
            "const:1e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0045ff4c",
      "incomplete_value": false,
      "site": "0045ff4c",
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
            "const:118:8"
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
      "0045ff8c",
      "DATA",
      [
        "storage",
        "00c64118",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0045ff8c",
      "DATA",
      [
        "storage",
        "00c641e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0045ff48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045ff30.md#insn-0045ff48) · [`0045ff6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045f/0045ff30.md#insn-0045ff6c)
- 新版 `0045ff88`（命令位置の公開資料なし） · `0045ffac`（命令位置の公開資料なし）

~~~diff
- 0045ff48 ["COPY", "tmp:0:8", ["const:118:8"]]
- 0045ff48 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0045ff48 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0045ff48 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0045ff88 ["COPY", "tmp:0:8", ["const:1e8:8"]]
+ 0045ff88 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0045ff88 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0045ff88 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0045ff48 bytes 29610491
+ 0045ff88 bytes 29a10791
- 0045ff6c ["COPY", "register:0:8", ["register:4048:8"]]
- 0045ff6c ["INT_ADD", "register:40f0:8", ["const:45ff6c:8", "const:4:8"]]
- 0045ff6c ["CALLIND", null, ["register:0:8"]]
+ 0045ffac ["COPY", "register:0:8", ["register:4048:8"]]
+ 0045ffac ["INT_ADD", "register:40f0:8", ["const:45ffac:8", "const:4:8"]]
+ 0045ffac ["CALLIND", null, ["register:0:8"]]
- 0045ff6c bytes 20013fd6
+ 0045ffac bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7059fbabd80ff9a9f0ccee77fcaf356"></a>

### [`004600d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/004600d0.md) → [`00460110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/00460110.md) FUN_00460110

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
      "definition_site": "00460124",
      "incomplete_value": false,
      "site": "00460128",
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
            "const:268:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004600e4",
      "incomplete_value": false,
      "site": "004600e8",
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
            "const:198:8"
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
      "00460128",
      "DATA",
      [
        "storage",
        "00c64198",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00460128",
      "DATA",
      [
        "storage",
        "00c64268",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004600dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/004600d0.md#insn-004600dc) · [`004600e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/004600d0.md#insn-004600e4)
- 新版 `0046011c`（命令位置の公開資料なし） · `00460124`（命令位置の公開資料なし）

~~~diff
- 004600dc ["INT_ADD", "register:40f0:8", ["const:4600dc:8", "const:4:8"]]
- 004600dc ["CALL", null, ["callee:00c57f60:8"]]
+ 0046011c ["INT_ADD", "register:40f0:8", ["const:46011c:8", "const:4:8"]]
+ 0046011c ["CALL", null, ["callee:00c57f60:8"]]
- 004600dc bytes 6ddf1f94
+ 0046011c bytes 91df1f94
- 004600e4 ["COPY", "tmp:0:8", ["const:198:8"]]
- 004600e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004600e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004600e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00460124 ["COPY", "tmp:0:8", ["const:268:8"]]
+ 00460124 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00460124 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00460124 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004600e4 bytes 08610691
+ 00460124 bytes 08a10991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a693fba46b5f439d71bd34a6bac28ec"></a>

### [`004600f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/004600f4.md) → [`00460134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/00460134.md) FUN_00460134

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
      "definition_site": "00460138",
      "incomplete_value": false,
      "site": "0046013c",
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
            "const:268:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004600f8",
      "incomplete_value": false,
      "site": "004600fc",
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
            "const:198:8"
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
      "0046013c",
      "DATA",
      [
        "storage",
        "00c64198",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0046013c",
      "DATA",
      [
        "storage",
        "00c64268",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004600f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/004600f4.md#insn-004600f8)
- 新版 `00460138`（命令位置の公開資料なし）

~~~diff
- 004600f8 ["COPY", "tmp:0:8", ["const:198:8"]]
- 004600f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004600f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004600f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00460138 ["COPY", "tmp:0:8", ["const:268:8"]]
+ 00460138 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00460138 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00460138 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004600f8 bytes 08610691
+ 00460138 bytes 08a10991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ccaffad61d8206c318df08c757608076"></a>

### [`0046010c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/0046010c.md) → [`0046014c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/0046014c.md) FUN_0046014c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00596d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00596/00596d10.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md)
- 新版 呼出元 0件  · 呼出先 9件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00596d50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00596/00596d50.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.77% / 新版 91.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 3件, `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00460278",
      "incomplete_value": true,
      "site": "00460278",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ecf:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00460238",
      "incomplete_value": true,
      "site": "00460238",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e8f:8"
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
      "definition_site": "00460314",
      "incomplete_value": true,
      "site": "00460314",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004602d4",
      "incomplete_value": true,
      "site": "004602d4",
      "value": [
        "LOAD",
        "8",
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
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00460304",
      "incomplete_value": true,
      "site": "00460314",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004602c4",
      "incomplete_value": true,
      "site": "004602d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00460268",
      "READ",
      [
        "storage",
        "002b5e8f",
        null,
        "string"
      ]
    ],
    [
      "004602b0",
      "READ",
      [
        "storage",
        "00ca4aa0",
        null,
        "undefined1"
      ]
    ],
    [
      "004602bc",
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
      "00460268",
      "READ",
      [
        "storage",
        "002b5ecf",
        null,
        "string"
      ]
    ],
    [
      "004602b0",
      "READ",
      [
        "storage",
        "00ca4ba0",
        null,
        "undefined1"
      ]
    ],
    [
      "004602bc",
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

- 旧版 [`004602d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/0046010c.md#insn-004602d4) · [`00460350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/0046010c.md#insn-00460350) · [`004603fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/0046010c.md#insn-004603fc)
- 新版 `00460314`（命令位置の公開資料なし） · `00460390`（命令位置の公開資料なし） · `0046043c`（命令位置の公開資料なし）

~~~diff
- 004602d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 004602d4 ["INT_ADD", "register:40f0:8", ["const:4602d4:8", "const:4:8"]]
- 004602d4 ["CALLIND", null, ["register:0:8"]]
+ 00460314 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00460314 ["INT_ADD", "register:40f0:8", ["const:460314:8", "const:4:8"]]
+ 00460314 ["CALLIND", null, ["register:0:8"]]
- 004602d4 bytes 00013fd6
+ 00460314 bytes 00013fd6
- 00460350 ["COPY", "register:0:8", ["register:4040:8"]]
- 00460350 ["INT_ADD", "register:40f0:8", ["const:460350:8", "const:4:8"]]
- 00460350 ["CALLIND", null, ["register:0:8"]]
+ 00460390 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00460390 ["INT_ADD", "register:40f0:8", ["const:460390:8", "const:4:8"]]
+ 00460390 ["CALLIND", null, ["register:0:8"]]
- 00460350 bytes 00013fd6
+ 00460390 bytes 00013fd6
- 004603fc ["COPY", "register:0:8", ["register:4040:8"]]
- 004603fc ["INT_ADD", "register:40f0:8", ["const:4603fc:8", "const:4:8"]]
- 004603fc ["CALLIND", null, ["register:0:8"]]
+ 0046043c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0046043c ["INT_ADD", "register:40f0:8", ["const:46043c:8", "const:4:8"]]
+ 0046043c ["CALLIND", null, ["register:0:8"]]
- 004603fc bytes 00013fd6
+ 0046043c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-336fffcbab2fe0cd04af1f08bf789e29"></a>

### [`0046056c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/0046056c.md) → [`004605ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/004605ac.md) FUN_004605ac

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
      "definition_site": "004605b8",
      "incomplete_value": false,
      "site": "004605c4",
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
            "const:2e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00460578",
      "incomplete_value": false,
      "site": "00460584",
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
            "const:218:8"
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
      "004605c4",
      "DATA",
      [
        "storage",
        "00c64218",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004605c4",
      "DATA",
      [
        "storage",
        "00c642e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00460578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/0046056c.md#insn-00460578)
- 新版 `004605b8`（命令位置の公開資料なし）

~~~diff
- 00460578 ["COPY", "tmp:0:8", ["const:218:8"]]
- 00460578 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00460578 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00460578 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 004605b8 ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 004605b8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 004605b8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 004605b8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00460578 bytes 4a610891
+ 004605b8 bytes 4aa10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2b9f4b3a43edefd14fb659956b434b6"></a>

### [`004605b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/004605b0.md) → [`004605f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/004605f0.md) FUN_004605f0

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
      "definition_site": "00460608",
      "incomplete_value": false,
      "site": "00460614",
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
            "const:2e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004605c8",
      "incomplete_value": false,
      "site": "004605d4",
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
            "const:218:8"
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
      "00460614",
      "DATA",
      [
        "storage",
        "00c64218",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00460614",
      "DATA",
      [
        "storage",
        "00c642e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004605c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/004605b0.md#insn-004605c8) · [`004605f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/004605b0.md#insn-004605f8)
- 新版 `00460608`（命令位置の公開資料なし） · `00460638`（命令位置の公開資料なし）

~~~diff
- 004605c8 ["COPY", "tmp:0:8", ["const:218:8"]]
- 004605c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004605c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004605c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00460608 ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 00460608 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00460608 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00460608 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004605c8 bytes 08610891
+ 00460608 bytes 08a10b91
- 004605f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004605f8 ["INT_ADD", "register:40f0:8", ["const:4605f8:8", "const:4:8"]]
- 004605f8 ["CALLIND", null, ["register:0:8"]]
+ 00460638 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00460638 ["INT_ADD", "register:40f0:8", ["const:460638:8", "const:4:8"]]
+ 00460638 ["CALLIND", null, ["register:0:8"]]
- 004605f8 bytes 00013fd6
+ 00460638 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ef30e5141fbd518aea88ffa0cb7107c"></a>

### [`0046060c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/0046060c.md) → [`0046064c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/0046064c.md) FUN_0046064c

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
      "definition_site": "00460678",
      "incomplete_value": false,
      "site": "00460678",
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
            "const:2e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00460638",
      "incomplete_value": false,
      "site": "00460638",
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
            "const:218:8"
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
      "00460678",
      "DATA",
      [
        "storage",
        "00c64218",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00460678",
      "DATA",
      [
        "storage",
        "00c642e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00460620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/0046060c.md#insn-00460620) · [`00460630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/0046060c.md#insn-00460630) · [`00460654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/0046060c.md#insn-00460654)
- 新版 `00460660`（命令位置の公開資料なし） · `00460670`（命令位置の公開資料なし） · `00460694`（命令位置の公開資料なし）

~~~diff
- 00460620 ["INT_ADD", "register:40f0:8", ["const:460620:8", "const:4:8"]]
- 00460620 ["CALL", null, ["callee:00c57f60:8"]]
+ 00460660 ["INT_ADD", "register:40f0:8", ["const:460660:8", "const:4:8"]]
+ 00460660 ["CALL", null, ["callee:00c57f60:8"]]
- 00460620 bytes 1cde1f94
+ 00460660 bytes 40de1f94
- 00460630 ["COPY", "tmp:0:8", ["const:218:8"]]
- 00460630 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00460630 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00460630 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00460670 ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 00460670 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00460670 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00460670 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00460630 bytes 08610891
+ 00460670 bytes 08a10b91
- 00460654 ["COPY", "register:0:8", ["register:4040:8"]]
- 00460654 ["INT_ADD", "register:40f0:8", ["const:460654:8", "const:4:8"]]
- 00460654 ["CALLIND", null, ["register:0:8"]]
+ 00460694 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00460694 ["INT_ADD", "register:40f0:8", ["const:460694:8", "const:4:8"]]
+ 00460694 ["CALLIND", null, ["register:0:8"]]
- 00460654 bytes 00013fd6
+ 00460694 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a2347b08c58a7caad5bc9683c95a493"></a>

### [`00460694`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/00460694.md) → [`004606d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/004606d4.md) FUN_004606d4

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
      "definition_site": "004606f0",
      "incomplete_value": false,
      "site": "004606f0",
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
            "const:2e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004606b0",
      "incomplete_value": false,
      "site": "004606b0",
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
            "const:218:8"
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
      "004606f0",
      "DATA",
      [
        "storage",
        "00c64218",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004606f0",
      "DATA",
      [
        "storage",
        "00c642e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004606ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/00460694.md#insn-004606ac) · [`004606d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/00460694.md#insn-004606d0)
- 新版 `004606ec`（命令位置の公開資料なし） · `00460710`（命令位置の公開資料なし）

~~~diff
- 004606ac ["COPY", "tmp:0:8", ["const:218:8"]]
- 004606ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004606ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004606ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004606ec ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 004606ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004606ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004606ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004606ac bytes 29610891
+ 004606ec bytes 29a10b91
- 004606d0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004606d0 ["INT_ADD", "register:40f0:8", ["const:4606d0:8", "const:4:8"]]
- 004606d0 ["CALLIND", null, ["register:0:8"]]
+ 00460710 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00460710 ["INT_ADD", "register:40f0:8", ["const:460710:8", "const:4:8"]]
+ 00460710 ["CALLIND", null, ["register:0:8"]]
- 004606d0 bytes 20013fd6
+ 00460710 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90d9402ada302b731e08a956633fcfd5"></a>

### [`00460790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/00460790.md) → [`004607d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00460/004607d0.md) FUN_004607d0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`004614b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/004614b0.md) [`004616d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/004616d0.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`004614f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/004614f0.md) [`00461710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/00461710.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.41% / 新版 97.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00460958",
      "incomplete_value": true,
      "site": "00460964",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9a2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00460918",
      "incomplete_value": true,
      "site": "00460924",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:971:8"
              ]
            ]
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
      "definition_site": "00460ac4",
      "incomplete_value": true,
      "site": "00460ad4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00460a84",
      "incomplete_value": true,
      "site": "00460a94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1b8:8"
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
      "definition_site": "00460ad8",
      "incomplete_value": true,
      "site": "00460ad8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00460a98",
      "incomplete_value": true,
      "site": "00460a98",
      "value": [
        "LOAD",
        "8",
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
      "00460958",
      "READ",
      [
        "storage",
        "002b2971",
        null,
        "string"
      ]
    ],
    [
      "00460ac4",
      "READ",
      [
        "storage",
        "002b71b8",
        null,
        "string"
      ]
    ],
    [
      "00460acc",
      "READ",
      [
        "storage",
        "002b71bd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00460958",
      "READ",
      [
        "storage",
        "002b29a2",
        null,
        "string"
      ]
    ],
    [
      "00460ac4",
      "READ",
      [
        "storage",
        "002b71f8",
        null,
        "string"
      ]
    ],
    [
      "00460acc",
      "READ",
      [
        "storage",
        "002b71fd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00460bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/00460790.md#insn-00460bdc) · [`00460d30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/00460790.md#insn-00460d30) · [`004607f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00460/00460790.md#insn-004607f8)
- 新版 `00460c1c`（命令位置の公開資料なし） · `00460d70`（命令位置の公開資料なし） · `00460838`（命令位置の公開資料なし）

~~~diff
- 00460bdc ["INT_ADD", "register:40f0:8", ["const:460bdc:8", "const:4:8"]]
- 00460bdc ["CALL", null, ["callee:00c57f80:8"]]
+ 00460c1c ["INT_ADD", "register:40f0:8", ["const:460c1c:8", "const:4:8"]]
+ 00460c1c ["CALL", null, ["callee:00c57f80:8"]]
- 00460bdc bytes b5dc1f94
+ 00460c1c bytes d9dc1f94
- 00460d30 ["INT_ADD", "register:40f0:8", ["const:460d30:8", "const:4:8"]]
- 00460d30 ["CALL", null, ["callee:00c57f80:8"]]
+ 00460d70 ["INT_ADD", "register:40f0:8", ["const:460d70:8", "const:4:8"]]
+ 00460d70 ["CALL", null, ["callee:00c57f80:8"]]
- 00460d30 bytes 60dc1f94
+ 00460d70 bytes 84dc1f94
- 004607f8 ["INT_ADD", "register:40f0:8", ["const:4607f8:8", "const:4:8"]]
- 004607f8 ["CALL", null, ["callee:004410cc:8"]]
+ 00460838 ["INT_ADD", "register:40f0:8", ["const:460838:8", "const:4:8"]]
+ 00460838 ["CALL", null, ["callee:004410cc:8"]]
- 004607f8 bytes 2582ff97
+ 00460838 bytes 2582ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c8419c93d4edfa39f3dc83ec81dd48b"></a>

### [`00461660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461660.md) → [`004616a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/004616a0.md) FUN_004616a0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`004614b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/004614b0.md) [`00461dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461dc8.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 2件 [`004614f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/004614f0.md) [`00461e08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/00461e08.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "004616ac",
      "incomplete_value": false,
      "site": "004616b0",
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
      "definition_site": "0046166c",
      "incomplete_value": false,
      "site": "00461670",
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
      "004616ac",
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
      "004616ac",
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

- 旧版 [`00461670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461660.md#insn-00461670) · [`0046166c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461660.md#insn-0046166c)
- 新版 `004616b0`（命令位置の公開資料なし） · `004616ac`（命令位置の公開資料なし）

~~~diff
- 00461670 ["INT_ADD", "register:40f0:8", ["const:461670:8", "const:4:8"]]
- 00461670 ["CALL", null, ["callee:0043b7b8:8"]]
+ 004616b0 ["INT_ADD", "register:40f0:8", ["const:4616b0:8", "const:4:8"]]
+ 004616b0 ["CALL", null, ["callee:0043b7b8:8"]]
- 00461670 bytes 4268ff97
+ 004616b0 bytes 4268ff97
- 0046166c ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 0046166c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0046166c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0046166c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004616ac ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 004616ac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004616ac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004616ac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0046166c bytes 00303d91
+ 004616ac bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ab968ce4f63c32ac64a437297e9f6c4"></a>

### [`00461a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461a18.md) → [`00461a58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/00461a58.md) FUN_00461a58

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00461818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461818.md) [`00461b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461b38.md) [`009bf214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009bf/009bf214.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 3件 [`00461858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/00461858.md) [`00461b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/00461b78.md) [`009bf268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009bf/009bf268.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "00461a64",
      "incomplete_value": false,
      "site": "00461a68",
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
      "definition_site": "00461a24",
      "incomplete_value": false,
      "site": "00461a28",
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
      "00461a64",
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
      "00461a64",
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

- 旧版 [`00461a28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461a18.md#insn-00461a28) · [`00461a24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461a18.md#insn-00461a24)
- 新版 `00461a68`（命令位置の公開資料なし） · `00461a64`（命令位置の公開資料なし）

~~~diff
- 00461a28 ["INT_ADD", "register:40f0:8", ["const:461a28:8", "const:4:8"]]
- 00461a28 ["CALL", null, ["callee:0043b7b8:8"]]
+ 00461a68 ["INT_ADD", "register:40f0:8", ["const:461a68:8", "const:4:8"]]
+ 00461a68 ["CALL", null, ["callee:0043b7b8:8"]]
- 00461a28 bytes 5467ff97
+ 00461a68 bytes 5467ff97
- 00461a24 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00461a24 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00461a24 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00461a24 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00461a64 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00461a64 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00461a64 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00461a64 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00461a24 bytes 00303d91
+ 00461a64 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86a199200bef46a1652b8d457723e1c6"></a>

### [`00462030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462030.md) → [`00462070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462070.md) FUN_00462070

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
      "definition_site": "0046207c",
      "incomplete_value": false,
      "site": "00462088",
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
            "const:368:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046203c",
      "incomplete_value": false,
      "site": "00462048",
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
            "const:298:8"
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
      "00462088",
      "DATA",
      [
        "storage",
        "00c64298",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00462088",
      "DATA",
      [
        "storage",
        "00c64368",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046203c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462030.md#insn-0046203c)
- 新版 `0046207c`（命令位置の公開資料なし）

~~~diff
- 0046203c ["COPY", "tmp:0:8", ["const:298:8"]]
- 0046203c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0046203c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0046203c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0046207c ["COPY", "tmp:0:8", ["const:368:8"]]
+ 0046207c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0046207c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0046207c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0046203c bytes 4a610a91
+ 0046207c bytes 4aa10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-257fa5ff8b56501a45a6892e40689ab4"></a>

### [`00462074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462074.md) → [`004620b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/004620b4.md) FUN_004620b4

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
      "definition_site": "004620cc",
      "incomplete_value": false,
      "site": "004620d8",
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
            "const:368:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046208c",
      "incomplete_value": false,
      "site": "00462098",
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
            "const:298:8"
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
      "004620d8",
      "DATA",
      [
        "storage",
        "00c64298",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004620d8",
      "DATA",
      [
        "storage",
        "00c64368",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046208c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462074.md#insn-0046208c) · [`004620bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462074.md#insn-004620bc)
- 新版 `004620cc`（命令位置の公開資料なし） · `004620fc`（命令位置の公開資料なし）

~~~diff
- 0046208c ["COPY", "tmp:0:8", ["const:298:8"]]
- 0046208c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0046208c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0046208c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004620cc ["COPY", "tmp:0:8", ["const:368:8"]]
+ 004620cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004620cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004620cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0046208c bytes 08610a91
+ 004620cc bytes 08a10d91
- 004620bc ["COPY", "register:0:8", ["register:4040:8"]]
- 004620bc ["INT_ADD", "register:40f0:8", ["const:4620bc:8", "const:4:8"]]
- 004620bc ["CALLIND", null, ["register:0:8"]]
+ 004620fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 004620fc ["INT_ADD", "register:40f0:8", ["const:4620fc:8", "const:4:8"]]
+ 004620fc ["CALLIND", null, ["register:0:8"]]
- 004620bc bytes 00013fd6
+ 004620fc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7703d79389a9ff9f3575c19ec1614c6f"></a>

### [`004620d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004620d0.md) → [`00462110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462110.md) FUN_00462110

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
      "definition_site": "0046213c",
      "incomplete_value": false,
      "site": "0046213c",
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
            "const:368:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004620fc",
      "incomplete_value": false,
      "site": "004620fc",
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
            "const:298:8"
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
      "0046213c",
      "DATA",
      [
        "storage",
        "00c64298",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0046213c",
      "DATA",
      [
        "storage",
        "00c64368",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004620e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004620d0.md#insn-004620e4) · [`004620f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004620d0.md#insn-004620f4) · [`00462118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004620d0.md#insn-00462118)
- 新版 `00462124`（命令位置の公開資料なし） · `00462134`（命令位置の公開資料なし） · `00462158`（命令位置の公開資料なし）

~~~diff
- 004620e4 ["INT_ADD", "register:40f0:8", ["const:4620e4:8", "const:4:8"]]
- 004620e4 ["CALL", null, ["callee:00c57f60:8"]]
+ 00462124 ["INT_ADD", "register:40f0:8", ["const:462124:8", "const:4:8"]]
+ 00462124 ["CALL", null, ["callee:00c57f60:8"]]
- 004620e4 bytes 6bd71f94
+ 00462124 bytes 8fd71f94
- 004620f4 ["COPY", "tmp:0:8", ["const:298:8"]]
- 004620f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004620f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004620f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00462134 ["COPY", "tmp:0:8", ["const:368:8"]]
+ 00462134 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00462134 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00462134 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004620f4 bytes 08610a91
+ 00462134 bytes 08a10d91
- 00462118 ["COPY", "register:0:8", ["register:4040:8"]]
- 00462118 ["INT_ADD", "register:40f0:8", ["const:462118:8", "const:4:8"]]
- 00462118 ["CALLIND", null, ["register:0:8"]]
+ 00462158 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00462158 ["INT_ADD", "register:40f0:8", ["const:462158:8", "const:4:8"]]
+ 00462158 ["CALLIND", null, ["register:0:8"]]
- 00462118 bytes 00013fd6
+ 00462158 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77e4c8fdf066c2b4846108705b2ce917"></a>

### [`00462158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462158.md) → [`00462198`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462198.md) FUN_00462198

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
      "definition_site": "004621b4",
      "incomplete_value": false,
      "site": "004621b4",
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
            "const:368:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00462174",
      "incomplete_value": false,
      "site": "00462174",
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
            "const:298:8"
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
      "004621b4",
      "DATA",
      [
        "storage",
        "00c64298",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004621b4",
      "DATA",
      [
        "storage",
        "00c64368",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00462170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462158.md#insn-00462170) · [`00462194`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462158.md#insn-00462194)
- 新版 `004621b0`（命令位置の公開資料なし） · `004621d4`（命令位置の公開資料なし）

~~~diff
- 00462170 ["COPY", "tmp:0:8", ["const:298:8"]]
- 00462170 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00462170 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00462170 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004621b0 ["COPY", "tmp:0:8", ["const:368:8"]]
+ 004621b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004621b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004621b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00462170 bytes 29610a91
+ 004621b0 bytes 29a10d91
- 00462194 ["COPY", "register:0:8", ["register:4048:8"]]
- 00462194 ["INT_ADD", "register:40f0:8", ["const:462194:8", "const:4:8"]]
- 00462194 ["CALLIND", null, ["register:0:8"]]
+ 004621d4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004621d4 ["INT_ADD", "register:40f0:8", ["const:4621d4:8", "const:4:8"]]
+ 004621d4 ["CALLIND", null, ["register:0:8"]]
- 00462194 bytes 20013fd6
+ 004621d4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1705d5bd165e42e06e29f65bbea2b42e"></a>

### [`004623c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004623c0.md) → [`00462400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462400.md) FUN_00462400

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
      "definition_site": "0046240c",
      "incomplete_value": false,
      "site": "00462418",
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
            "const:3e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004623cc",
      "incomplete_value": false,
      "site": "004623d8",
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
            "const:318:8"
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
      "00462418",
      "DATA",
      [
        "storage",
        "00c64318",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00462418",
      "DATA",
      [
        "storage",
        "00c643e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004623cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004623c0.md#insn-004623cc)
- 新版 `0046240c`（命令位置の公開資料なし）

~~~diff
- 004623cc ["COPY", "tmp:0:8", ["const:318:8"]]
- 004623cc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004623cc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004623cc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0046240c ["COPY", "tmp:0:8", ["const:3e8:8"]]
+ 0046240c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0046240c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0046240c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004623cc bytes 4a610c91
+ 0046240c bytes 4aa10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48e8171e0a1981e14f6d06d209a293c1"></a>

### [`00462404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462404.md) → [`00462444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462444.md) FUN_00462444

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
      "definition_site": "0046245c",
      "incomplete_value": false,
      "site": "00462468",
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
            "const:3e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046241c",
      "incomplete_value": false,
      "site": "00462428",
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
            "const:318:8"
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
      "00462468",
      "DATA",
      [
        "storage",
        "00c64318",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00462468",
      "DATA",
      [
        "storage",
        "00c643e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046241c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462404.md#insn-0046241c) · [`0046244c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462404.md#insn-0046244c)
- 新版 `0046245c`（命令位置の公開資料なし） · `0046248c`（命令位置の公開資料なし）

~~~diff
- 0046241c ["COPY", "tmp:0:8", ["const:318:8"]]
- 0046241c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0046241c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0046241c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0046245c ["COPY", "tmp:0:8", ["const:3e8:8"]]
+ 0046245c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0046245c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0046245c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0046241c bytes 08610c91
+ 0046245c bytes 08a10f91
- 0046244c ["COPY", "register:0:8", ["register:4040:8"]]
- 0046244c ["INT_ADD", "register:40f0:8", ["const:46244c:8", "const:4:8"]]
- 0046244c ["CALLIND", null, ["register:0:8"]]
+ 0046248c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0046248c ["INT_ADD", "register:40f0:8", ["const:46248c:8", "const:4:8"]]
+ 0046248c ["CALLIND", null, ["register:0:8"]]
- 0046244c bytes 00013fd6
+ 0046248c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe575f65fbf24da520ed0cd0954edb9a"></a>

### [`00462460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462460.md) → [`004624a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/004624a0.md) FUN_004624a0

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
      "definition_site": "004624cc",
      "incomplete_value": false,
      "site": "004624cc",
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
            "const:3e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046248c",
      "incomplete_value": false,
      "site": "0046248c",
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
            "const:318:8"
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
      "004624cc",
      "DATA",
      [
        "storage",
        "00c64318",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004624cc",
      "DATA",
      [
        "storage",
        "00c643e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00462474`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462460.md#insn-00462474) · [`00462484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462460.md#insn-00462484) · [`004624a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462460.md#insn-004624a8)
- 新版 `004624b4`（命令位置の公開資料なし） · `004624c4`（命令位置の公開資料なし） · `004624e8`（命令位置の公開資料なし）

~~~diff
- 00462474 ["INT_ADD", "register:40f0:8", ["const:462474:8", "const:4:8"]]
- 00462474 ["CALL", null, ["callee:00c57f60:8"]]
+ 004624b4 ["INT_ADD", "register:40f0:8", ["const:4624b4:8", "const:4:8"]]
+ 004624b4 ["CALL", null, ["callee:00c57f60:8"]]
- 00462474 bytes 87d61f94
+ 004624b4 bytes abd61f94
- 00462484 ["COPY", "tmp:0:8", ["const:318:8"]]
- 00462484 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00462484 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00462484 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004624c4 ["COPY", "tmp:0:8", ["const:3e8:8"]]
+ 004624c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004624c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004624c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00462484 bytes 08610c91
+ 004624c4 bytes 08a10f91
- 004624a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004624a8 ["INT_ADD", "register:40f0:8", ["const:4624a8:8", "const:4:8"]]
- 004624a8 ["CALLIND", null, ["register:0:8"]]
+ 004624e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004624e8 ["INT_ADD", "register:40f0:8", ["const:4624e8:8", "const:4:8"]]
+ 004624e8 ["CALLIND", null, ["register:0:8"]]
- 004624a8 bytes 00013fd6
+ 004624e8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1371660a332ea3af37176e790b7c65d"></a>

### [`004624e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004624e8.md) → [`00462528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462528.md) FUN_00462528

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
      "definition_site": "00462544",
      "incomplete_value": false,
      "site": "00462544",
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
            "const:3e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00462504",
      "incomplete_value": false,
      "site": "00462504",
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
            "const:318:8"
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
      "00462544",
      "DATA",
      [
        "storage",
        "00c64318",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00462544",
      "DATA",
      [
        "storage",
        "00c643e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00462500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004624e8.md#insn-00462500) · [`00462524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004624e8.md#insn-00462524)
- 新版 `00462540`（命令位置の公開資料なし） · `00462564`（命令位置の公開資料なし）

~~~diff
- 00462500 ["COPY", "tmp:0:8", ["const:318:8"]]
- 00462500 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00462500 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00462500 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00462540 ["COPY", "tmp:0:8", ["const:3e8:8"]]
+ 00462540 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00462540 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00462540 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00462500 bytes 29610c91
+ 00462540 bytes 29a10f91
- 00462524 ["COPY", "register:0:8", ["register:4048:8"]]
- 00462524 ["INT_ADD", "register:40f0:8", ["const:462524:8", "const:4:8"]]
- 00462524 ["CALLIND", null, ["register:0:8"]]
+ 00462564 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00462564 ["INT_ADD", "register:40f0:8", ["const:462564:8", "const:4:8"]]
+ 00462564 ["CALLIND", null, ["register:0:8"]]
- 00462524 bytes 20013fd6
+ 00462564 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e374f39b88235fe0c2c4c52530781f73"></a>

### [`00462680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462680.md) → [`004626c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/004626c0.md) FUN_004626c0

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
      "definition_site": "004626cc",
      "incomplete_value": false,
      "site": "004626d8",
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
            "const:468:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046268c",
      "incomplete_value": false,
      "site": "00462698",
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
            "const:398:8"
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
      "004626d8",
      "DATA",
      [
        "storage",
        "00c64398",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004626d8",
      "DATA",
      [
        "storage",
        "00c64468",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046268c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462680.md#insn-0046268c)
- 新版 `004626cc`（命令位置の公開資料なし）

~~~diff
- 0046268c ["COPY", "tmp:0:8", ["const:398:8"]]
- 0046268c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0046268c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0046268c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 004626cc ["COPY", "tmp:0:8", ["const:468:8"]]
+ 004626cc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 004626cc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 004626cc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0046268c bytes 4a610e91
+ 004626cc bytes 4aa11191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-546f6e192fb1ca1eb203b71cf7c73720"></a>

### [`004626c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004626c4.md) → [`00462704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462704.md) FUN_00462704

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
      "definition_site": "0046271c",
      "incomplete_value": false,
      "site": "00462728",
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
            "const:468:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004626dc",
      "incomplete_value": false,
      "site": "004626e8",
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
            "const:398:8"
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
      "00462728",
      "DATA",
      [
        "storage",
        "00c64398",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00462728",
      "DATA",
      [
        "storage",
        "00c64468",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004626dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004626c4.md#insn-004626dc) · [`0046270c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004626c4.md#insn-0046270c)
- 新版 `0046271c`（命令位置の公開資料なし） · `0046274c`（命令位置の公開資料なし）

~~~diff
- 004626dc ["COPY", "tmp:0:8", ["const:398:8"]]
- 004626dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004626dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004626dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0046271c ["COPY", "tmp:0:8", ["const:468:8"]]
+ 0046271c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0046271c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0046271c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004626dc bytes 08610e91
+ 0046271c bytes 08a11191
- 0046270c ["COPY", "register:0:8", ["register:4040:8"]]
- 0046270c ["INT_ADD", "register:40f0:8", ["const:46270c:8", "const:4:8"]]
- 0046270c ["CALLIND", null, ["register:0:8"]]
+ 0046274c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0046274c ["INT_ADD", "register:40f0:8", ["const:46274c:8", "const:4:8"]]
+ 0046274c ["CALLIND", null, ["register:0:8"]]
- 0046270c bytes 00013fd6
+ 0046274c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de948be7457f59a0af87050759c10db2"></a>

### [`00462720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462720.md) → [`00462760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462760.md) FUN_00462760

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
      "definition_site": "0046278c",
      "incomplete_value": false,
      "site": "0046278c",
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
            "const:468:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046274c",
      "incomplete_value": false,
      "site": "0046274c",
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
            "const:398:8"
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
      "0046278c",
      "DATA",
      [
        "storage",
        "00c64398",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0046278c",
      "DATA",
      [
        "storage",
        "00c64468",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00462734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462720.md#insn-00462734) · [`00462744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462720.md#insn-00462744) · [`00462768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462720.md#insn-00462768)
- 新版 `00462774`（命令位置の公開資料なし） · `00462784`（命令位置の公開資料なし） · `004627a8`（命令位置の公開資料なし）

~~~diff
- 00462734 ["INT_ADD", "register:40f0:8", ["const:462734:8", "const:4:8"]]
- 00462734 ["CALL", null, ["callee:00c57f60:8"]]
+ 00462774 ["INT_ADD", "register:40f0:8", ["const:462774:8", "const:4:8"]]
+ 00462774 ["CALL", null, ["callee:00c57f60:8"]]
- 00462734 bytes d7d51f94
+ 00462774 bytes fbd51f94
- 00462744 ["COPY", "tmp:0:8", ["const:398:8"]]
- 00462744 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00462744 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00462744 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00462784 ["COPY", "tmp:0:8", ["const:468:8"]]
+ 00462784 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00462784 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00462784 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00462744 bytes 08610e91
+ 00462784 bytes 08a11191
- 00462768 ["COPY", "register:0:8", ["register:4040:8"]]
- 00462768 ["INT_ADD", "register:40f0:8", ["const:462768:8", "const:4:8"]]
- 00462768 ["CALLIND", null, ["register:0:8"]]
+ 004627a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004627a8 ["INT_ADD", "register:40f0:8", ["const:4627a8:8", "const:4:8"]]
+ 004627a8 ["CALLIND", null, ["register:0:8"]]
- 00462768 bytes 00013fd6
+ 004627a8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6956438476f10e79620b9b00ebb044bb"></a>

### [`004627a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004627a8.md) → [`004627e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/004627e8.md) FUN_004627e8

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
      "definition_site": "00462804",
      "incomplete_value": false,
      "site": "00462804",
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
            "const:468:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004627c4",
      "incomplete_value": false,
      "site": "004627c4",
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
            "const:398:8"
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
      "00462804",
      "DATA",
      [
        "storage",
        "00c64398",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00462804",
      "DATA",
      [
        "storage",
        "00c64468",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004627c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004627a8.md#insn-004627c0) · [`004627e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004627a8.md#insn-004627e4)
- 新版 `00462800`（命令位置の公開資料なし） · `00462824`（命令位置の公開資料なし）

~~~diff
- 004627c0 ["COPY", "tmp:0:8", ["const:398:8"]]
- 004627c0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004627c0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004627c0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00462800 ["COPY", "tmp:0:8", ["const:468:8"]]
+ 00462800 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00462800 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00462800 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004627c0 bytes 29610e91
+ 00462800 bytes 29a11191
- 004627e4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004627e4 ["INT_ADD", "register:40f0:8", ["const:4627e4:8", "const:4:8"]]
- 004627e4 ["CALLIND", null, ["register:0:8"]]
+ 00462824 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00462824 ["INT_ADD", "register:40f0:8", ["const:462824:8", "const:4:8"]]
+ 00462824 ["CALLIND", null, ["register:0:8"]]
- 004627e4 bytes 20013fd6
+ 00462824 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c381f85c80636369b1d88720f3e7a2b5"></a>

### [`00462940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462940.md) → [`00462980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462980.md) FUN_00462980

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
      "definition_site": "0046298c",
      "incomplete_value": false,
      "site": "00462998",
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
            "const:4e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046294c",
      "incomplete_value": false,
      "site": "00462958",
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
            "const:418:8"
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
      "00462998",
      "DATA",
      [
        "storage",
        "00c64418",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00462998",
      "DATA",
      [
        "storage",
        "00c644e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046294c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462940.md#insn-0046294c)
- 新版 `0046298c`（命令位置の公開資料なし）

~~~diff
- 0046294c ["COPY", "tmp:0:8", ["const:418:8"]]
- 0046294c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0046294c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0046294c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0046298c ["COPY", "tmp:0:8", ["const:4e8:8"]]
+ 0046298c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0046298c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0046298c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0046294c bytes 4a611091
+ 0046298c bytes 4aa11391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94e8fd4bcfb2ff215634f9efe33f6ee7"></a>

### [`00462984`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462984.md) → [`004629c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/004629c4.md) FUN_004629c4

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
      "definition_site": "004629dc",
      "incomplete_value": false,
      "site": "004629e8",
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
            "const:4e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046299c",
      "incomplete_value": false,
      "site": "004629a8",
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
            "const:418:8"
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
      "004629e8",
      "DATA",
      [
        "storage",
        "00c64418",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004629e8",
      "DATA",
      [
        "storage",
        "00c644e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046299c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462984.md#insn-0046299c) · [`004629cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462984.md#insn-004629cc)
- 新版 `004629dc`（命令位置の公開資料なし） · `00462a0c`（命令位置の公開資料なし）

~~~diff
- 0046299c ["COPY", "tmp:0:8", ["const:418:8"]]
- 0046299c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0046299c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0046299c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004629dc ["COPY", "tmp:0:8", ["const:4e8:8"]]
+ 004629dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004629dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004629dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0046299c bytes 08611091
+ 004629dc bytes 08a11391
- 004629cc ["COPY", "register:0:8", ["register:4040:8"]]
- 004629cc ["INT_ADD", "register:40f0:8", ["const:4629cc:8", "const:4:8"]]
- 004629cc ["CALLIND", null, ["register:0:8"]]
+ 00462a0c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00462a0c ["INT_ADD", "register:40f0:8", ["const:462a0c:8", "const:4:8"]]
+ 00462a0c ["CALLIND", null, ["register:0:8"]]
- 004629cc bytes 00013fd6
+ 00462a0c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b17d30399d56b4e4ce989ee543d5fa05"></a>

### [`004629e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004629e0.md) → [`00462a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462a20.md) FUN_00462a20

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
      "definition_site": "00462a4c",
      "incomplete_value": false,
      "site": "00462a4c",
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
            "const:4e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00462a0c",
      "incomplete_value": false,
      "site": "00462a0c",
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
            "const:418:8"
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
      "00462a4c",
      "DATA",
      [
        "storage",
        "00c64418",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00462a4c",
      "DATA",
      [
        "storage",
        "00c644e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004629f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004629e0.md#insn-004629f4) · [`00462a04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004629e0.md#insn-00462a04) · [`00462a28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/004629e0.md#insn-00462a28)
- 新版 `00462a34`（命令位置の公開資料なし） · `00462a44`（命令位置の公開資料なし） · `00462a68`（命令位置の公開資料なし）

~~~diff
- 004629f4 ["INT_ADD", "register:40f0:8", ["const:4629f4:8", "const:4:8"]]
- 004629f4 ["CALL", null, ["callee:00c57f60:8"]]
+ 00462a34 ["INT_ADD", "register:40f0:8", ["const:462a34:8", "const:4:8"]]
+ 00462a34 ["CALL", null, ["callee:00c57f60:8"]]
- 004629f4 bytes 27d51f94
+ 00462a34 bytes 4bd51f94
- 00462a04 ["COPY", "tmp:0:8", ["const:418:8"]]
- 00462a04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00462a04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00462a04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00462a44 ["COPY", "tmp:0:8", ["const:4e8:8"]]
+ 00462a44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00462a44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00462a44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00462a04 bytes 08611091
+ 00462a44 bytes 08a11391
- 00462a28 ["COPY", "register:0:8", ["register:4040:8"]]
- 00462a28 ["INT_ADD", "register:40f0:8", ["const:462a28:8", "const:4:8"]]
- 00462a28 ["CALLIND", null, ["register:0:8"]]
+ 00462a68 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00462a68 ["INT_ADD", "register:40f0:8", ["const:462a68:8", "const:4:8"]]
+ 00462a68 ["CALLIND", null, ["register:0:8"]]
- 00462a28 bytes 00013fd6
+ 00462a68 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7bcbf1bdc25990f3388088587b681aa3"></a>

### [`00462a68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462a68.md) → [`00462aa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462aa8.md) FUN_00462aa8

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
      "definition_site": "00462ac4",
      "incomplete_value": false,
      "site": "00462ac4",
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
            "const:4e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00462a84",
      "incomplete_value": false,
      "site": "00462a84",
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
            "const:418:8"
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
      "00462ac4",
      "DATA",
      [
        "storage",
        "00c64418",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00462ac4",
      "DATA",
      [
        "storage",
        "00c644e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00462a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462a68.md#insn-00462a80) · [`00462aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462a68.md#insn-00462aa4)
- 新版 `00462ac0`（命令位置の公開資料なし） · `00462ae4`（命令位置の公開資料なし）

~~~diff
- 00462a80 ["COPY", "tmp:0:8", ["const:418:8"]]
- 00462a80 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00462a80 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00462a80 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00462ac0 ["COPY", "tmp:0:8", ["const:4e8:8"]]
+ 00462ac0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00462ac0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00462ac0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00462a80 bytes 29611091
+ 00462ac0 bytes 29a11391
- 00462aa4 ["COPY", "register:0:8", ["register:4048:8"]]
- 00462aa4 ["INT_ADD", "register:40f0:8", ["const:462aa4:8", "const:4:8"]]
- 00462aa4 ["CALLIND", null, ["register:0:8"]]
+ 00462ae4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00462ae4 ["INT_ADD", "register:40f0:8", ["const:462ae4:8", "const:4:8"]]
+ 00462ae4 ["CALLIND", null, ["register:0:8"]]
- 00462aa4 bytes 20013fd6
+ 00462ae4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3c4fbbee0f589409581bc7787307c5b"></a>

### [`00462dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462dbc.md) → [`00462dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462dfc.md) FUN_00462dfc

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
      "definition_site": "00462e08",
      "incomplete_value": false,
      "site": "00462e14",
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
            "const:568:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00462dc8",
      "incomplete_value": false,
      "site": "00462dd4",
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
            "const:498:8"
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
      "00462e14",
      "DATA",
      [
        "storage",
        "00c64498",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00462e14",
      "DATA",
      [
        "storage",
        "00c64568",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00462dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462dbc.md#insn-00462dc8)
- 新版 `00462e08`（命令位置の公開資料なし）

~~~diff
- 00462dc8 ["COPY", "tmp:0:8", ["const:498:8"]]
- 00462dc8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00462dc8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00462dc8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00462e08 ["COPY", "tmp:0:8", ["const:568:8"]]
+ 00462e08 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00462e08 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00462e08 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00462dc8 bytes 4a611291
+ 00462e08 bytes 4aa11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96d5ba7b9e91c7e7b78f1f8e2852d12e"></a>

### [`00462e00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462e00.md) → [`00462e40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462e40.md) FUN_00462e40

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
      "definition_site": "00462e58",
      "incomplete_value": false,
      "site": "00462e64",
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
            "const:568:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00462e18",
      "incomplete_value": false,
      "site": "00462e24",
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
            "const:498:8"
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
      "00462e64",
      "DATA",
      [
        "storage",
        "00c64498",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00462e64",
      "DATA",
      [
        "storage",
        "00c64568",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00462e18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462e00.md#insn-00462e18) · [`00462e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462e00.md#insn-00462e48)
- 新版 `00462e58`（命令位置の公開資料なし） · `00462e88`（命令位置の公開資料なし）

~~~diff
- 00462e18 ["COPY", "tmp:0:8", ["const:498:8"]]
- 00462e18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00462e18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00462e18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00462e58 ["COPY", "tmp:0:8", ["const:568:8"]]
+ 00462e58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00462e58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00462e58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00462e18 bytes 08611291
+ 00462e58 bytes 08a11591
- 00462e48 ["COPY", "register:0:8", ["register:4040:8"]]
- 00462e48 ["INT_ADD", "register:40f0:8", ["const:462e48:8", "const:4:8"]]
- 00462e48 ["CALLIND", null, ["register:0:8"]]
+ 00462e88 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00462e88 ["INT_ADD", "register:40f0:8", ["const:462e88:8", "const:4:8"]]
+ 00462e88 ["CALLIND", null, ["register:0:8"]]
- 00462e48 bytes 00013fd6
+ 00462e88 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3167915e3e50a5b2e6b01baedca0edb5"></a>

### [`00462e5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462e5c.md) → [`00462e9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462e9c.md) FUN_00462e9c

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
      "definition_site": "00462ec8",
      "incomplete_value": false,
      "site": "00462ec8",
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
            "const:568:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00462e88",
      "incomplete_value": false,
      "site": "00462e88",
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
            "const:498:8"
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
      "00462ec8",
      "DATA",
      [
        "storage",
        "00c64498",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00462ec8",
      "DATA",
      [
        "storage",
        "00c64568",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00462e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462e5c.md#insn-00462e70) · [`00462e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462e5c.md#insn-00462e80) · [`00462ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462e5c.md#insn-00462ea4)
- 新版 `00462eb0`（命令位置の公開資料なし） · `00462ec0`（命令位置の公開資料なし） · `00462ee4`（命令位置の公開資料なし）

~~~diff
- 00462e70 ["INT_ADD", "register:40f0:8", ["const:462e70:8", "const:4:8"]]
- 00462e70 ["CALL", null, ["callee:00c57f60:8"]]
+ 00462eb0 ["INT_ADD", "register:40f0:8", ["const:462eb0:8", "const:4:8"]]
+ 00462eb0 ["CALL", null, ["callee:00c57f60:8"]]
- 00462e70 bytes 08d41f94
+ 00462eb0 bytes 2cd41f94
- 00462e80 ["COPY", "tmp:0:8", ["const:498:8"]]
- 00462e80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00462e80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00462e80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00462ec0 ["COPY", "tmp:0:8", ["const:568:8"]]
+ 00462ec0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00462ec0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00462ec0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00462e80 bytes 08611291
+ 00462ec0 bytes 08a11591
- 00462ea4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00462ea4 ["INT_ADD", "register:40f0:8", ["const:462ea4:8", "const:4:8"]]
- 00462ea4 ["CALLIND", null, ["register:0:8"]]
+ 00462ee4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00462ee4 ["INT_ADD", "register:40f0:8", ["const:462ee4:8", "const:4:8"]]
+ 00462ee4 ["CALLIND", null, ["register:0:8"]]
- 00462ea4 bytes 00013fd6
+ 00462ee4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da1c1332c1dc2e0d0def76816a0e1b99"></a>

### [`00462ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462ee4.md) → [`00462f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00462/00462f24.md) FUN_00462f24

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
      "definition_site": "00462f40",
      "incomplete_value": false,
      "site": "00462f40",
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
            "const:568:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00462f00",
      "incomplete_value": false,
      "site": "00462f00",
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
            "const:498:8"
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
      "00462f40",
      "DATA",
      [
        "storage",
        "00c64498",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00462f40",
      "DATA",
      [
        "storage",
        "00c64568",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00462efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462ee4.md#insn-00462efc) · [`00462f20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00462/00462ee4.md#insn-00462f20)
- 新版 `00462f3c`（命令位置の公開資料なし） · `00462f60`（命令位置の公開資料なし）

~~~diff
- 00462efc ["COPY", "tmp:0:8", ["const:498:8"]]
- 00462efc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00462efc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00462efc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00462f3c ["COPY", "tmp:0:8", ["const:568:8"]]
+ 00462f3c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00462f3c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00462f3c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00462efc bytes 29611291
+ 00462f3c bytes 29a11591
- 00462f20 ["COPY", "register:0:8", ["register:4048:8"]]
- 00462f20 ["INT_ADD", "register:40f0:8", ["const:462f20:8", "const:4:8"]]
- 00462f20 ["CALLIND", null, ["register:0:8"]]
+ 00462f60 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00462f60 ["INT_ADD", "register:40f0:8", ["const:462f60:8", "const:4:8"]]
+ 00462f60 ["CALLIND", null, ["register:0:8"]]
- 00462f20 bytes 20013fd6
+ 00462f60 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-468e3aa639beb5fce71f44375063d2c1"></a>

### [`00463084`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463084.md) → [`004630c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00463/004630c4.md) FUN_004630c4

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
      "definition_site": "004630d0",
      "incomplete_value": false,
      "site": "004630dc",
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
      "definition_site": "00463090",
      "incomplete_value": false,
      "site": "0046309c",
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
      "004630dc",
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
      "004630dc",
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

- 旧版 [`00463090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/00463084.md#insn-00463090)
- 新版 `004630d0`（命令位置の公開資料なし）

~~~diff
- 00463090 ["COPY", "tmp:0:8", ["const:518:8"]]
- 00463090 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00463090 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00463090 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 004630d0 ["COPY", "tmp:0:8", ["const:5e8:8"]]
+ 004630d0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 004630d0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 004630d0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00463090 bytes 4a611491
+ 004630d0 bytes 4aa11791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62b50581fde7100d8598ebe85e692e15"></a>

### [`004630c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/004630c8.md) → [`00463108`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00463/00463108.md) FUN_00463108

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
      "definition_site": "00463120",
      "incomplete_value": false,
      "site": "0046312c",
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
      "definition_site": "004630e0",
      "incomplete_value": false,
      "site": "004630ec",
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
      "0046312c",
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
      "0046312c",
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

- 旧版 [`004630e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/004630c8.md#insn-004630e0) · [`00463110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00463/004630c8.md#insn-00463110)
- 新版 `00463120`（命令位置の公開資料なし） · `00463150`（命令位置の公開資料なし）

~~~diff
- 004630e0 ["COPY", "tmp:0:8", ["const:518:8"]]
- 004630e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004630e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004630e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00463120 ["COPY", "tmp:0:8", ["const:5e8:8"]]
+ 00463120 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00463120 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00463120 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004630e0 bytes 08611491
+ 00463120 bytes 08a11791
- 00463110 ["COPY", "register:0:8", ["register:4040:8"]]
- 00463110 ["INT_ADD", "register:40f0:8", ["const:463110:8", "const:4:8"]]
- 00463110 ["CALLIND", null, ["register:0:8"]]
+ 00463150 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00463150 ["INT_ADD", "register:40f0:8", ["const:463150:8", "const:4:8"]]
+ 00463150 ["CALLIND", null, ["register:0:8"]]
- 00463110 bytes 00013fd6
+ 00463150 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

