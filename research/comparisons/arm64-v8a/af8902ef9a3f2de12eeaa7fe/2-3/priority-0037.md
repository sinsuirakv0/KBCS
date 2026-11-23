# v16.0.0 → v16.0.1 · 最優先の変更候補 (37)

[一覧の目次](README.md)

<a id="compare-d143414cfd9f02d01e68364764707dfb"></a>

### [`0078544c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/0078544c.md) → [`0078548c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00785/0078548c.md) FUN_0078548c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "007854a0",
      "incomplete_value": false,
      "site": "007854a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:1a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00785460",
      "incomplete_value": false,
      "site": "00785464",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:da0:8"
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
      "007854a4",
      "DATA",
      [
        "storage",
        "00c78da0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007854a4",
      "DATA",
      [
        "storage",
        "00c791a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00785458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/0078544c.md#insn-00785458) · [`0078545c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/0078544c.md#insn-0078545c) · [`00785460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/0078544c.md#insn-00785460)
- 新版 `00785498`（命令位置の公開資料なし） · `0078549c`（命令位置の公開資料なし） · `007854a0`（命令位置の公開資料なし）

~~~diff
- 00785458 ["INT_ADD", "register:40f0:8", ["const:785458:8", "const:4:8"]]
- 00785458 ["CALL", null, ["callee:00c57e90:8"]]
+ 00785498 ["INT_ADD", "register:40f0:8", ["const:785498:8", "const:4:8"]]
+ 00785498 ["CALL", null, ["callee:00c57e90:8"]]
- 00785458 bytes 8e491394
+ 00785498 bytes 7e4a1394
- 0078545c ["COPY", "register:4040:8", ["const:c78000:8"]]
+ 0078549c ["COPY", "register:4040:8", ["const:c79000:8"]]
- 0078545c bytes 882700f0
+ 0078549c bytes a8270090
- 00785460 ["COPY", "tmp:0:8", ["const:da0:8"]]
- 00785460 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00785460 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00785460 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007854a0 ["COPY", "tmp:0:8", ["const:1a0:8"]]
+ 007854a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007854a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007854a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00785460 bytes 08813691
+ 007854a0 bytes 08810691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3933ff8aad3b44242fa79236a9986760"></a>

### [`00785488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/00785488.md) → [`007854c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00785/007854c8.md) FUN_007854c8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

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
      "site": "007854ec",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007854ac",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "007854ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "007854ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007854ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/00785488.md#insn-007854ac) · [`007854b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/00785488.md#insn-007854b8)
- 新版 `007854ec`（命令位置の公開資料なし） · `007854f8`（命令位置の公開資料なし）

~~~diff
- 007854ac ["INT_ADD", "register:40f0:8", ["const:7854ac:8", "const:4:8"]]
- 007854ac ["CALL", null, ["ram:47acb4:8"]]
+ 007854ec ["INT_ADD", "register:40f0:8", ["const:7854ec:8", "const:4:8"]]
+ 007854ec ["CALL", null, ["ram:47acf4:8"]]
- 007854ac bytes 02d6f397
+ 007854ec bytes 02d6f397
- 007854b8 ["INT_ADD", "register:40f0:8", ["const:7854b8:8", "const:4:8"]]
- 007854b8 ["CALL", null, ["callee:0047cdd4:8"]]
+ 007854f8 ["INT_ADD", "register:40f0:8", ["const:7854f8:8", "const:4:8"]]
+ 007854f8 ["CALL", null, ["callee:0047cdd4:8"]]
- 007854b8 bytes 37def397
+ 007854f8 bytes 37def397
~~~


<a id="compare-426c723b52492469fc07955ec373459d"></a>

### [`007854fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/007854fc.md) → [`0078553c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00785/0078553c.md) FUN_0078553c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00785550",
      "incomplete_value": false,
      "site": "00785554",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:220:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00785510",
      "incomplete_value": false,
      "site": "00785514",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:e20:8"
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
      "00785554",
      "DATA",
      [
        "storage",
        "00c78e20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00785554",
      "DATA",
      [
        "storage",
        "00c79220",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00785508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/007854fc.md#insn-00785508) · [`0078550c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/007854fc.md#insn-0078550c) · [`00785510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/007854fc.md#insn-00785510)
- 新版 `00785548`（命令位置の公開資料なし） · `0078554c`（命令位置の公開資料なし） · `00785550`（命令位置の公開資料なし）

~~~diff
- 00785508 ["INT_ADD", "register:40f0:8", ["const:785508:8", "const:4:8"]]
- 00785508 ["CALL", null, ["callee:00c57e90:8"]]
+ 00785548 ["INT_ADD", "register:40f0:8", ["const:785548:8", "const:4:8"]]
+ 00785548 ["CALL", null, ["callee:00c57e90:8"]]
- 00785508 bytes 62491394
+ 00785548 bytes 524a1394
- 0078550c ["COPY", "register:4040:8", ["const:c78000:8"]]
+ 0078554c ["COPY", "register:4040:8", ["const:c79000:8"]]
- 0078550c bytes 882700f0
+ 0078554c bytes a8270090
- 00785510 ["COPY", "tmp:0:8", ["const:e20:8"]]
- 00785510 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00785510 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00785510 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00785550 ["COPY", "tmp:0:8", ["const:220:8"]]
+ 00785550 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00785550 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00785550 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00785510 bytes 08813891
+ 00785550 bytes 08810891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9804dafb833c00a62ee636307f1ac3f"></a>

### [`00785538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/00785538.md) → [`00785578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00785/00785578.md) FUN_00785578

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`007287a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00728/007287a8.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`007287e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00728/007287e8.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.41% / 新版 98.41%

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
      "site": "00785654",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00785614",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "00785654",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00785654",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007855d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/00785538.md#insn-007855d4) · [`00785614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/00785538.md#insn-00785614) · [`0078556c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/00785538.md#insn-0078556c)
- 新版 `00785614`（命令位置の公開資料なし） · `00785654`（命令位置の公開資料なし） · `007855ac`（命令位置の公開資料なし）

~~~diff
- 007855d4 ["INT_ADD", "register:40f0:8", ["const:7855d4:8", "const:4:8"]]
- 007855d4 ["CALL", null, ["callee:008514f8:8"]]
+ 00785614 ["INT_ADD", "register:40f0:8", ["const:785614:8", "const:4:8"]]
+ 00785614 ["CALL", null, ["callee:008514f8:8"]]
- 007855d4 bytes b92f0394
+ 00785614 bytes b92f0394
- 00785614 ["INT_ADD", "register:40f0:8", ["const:785614:8", "const:4:8"]]
- 00785614 ["CALL", null, ["ram:47acb4:8"]]
+ 00785654 ["INT_ADD", "register:40f0:8", ["const:785654:8", "const:4:8"]]
+ 00785654 ["CALL", null, ["ram:47acf4:8"]]
- 00785614 bytes a8d5f397
+ 00785654 bytes a8d5f397
- 0078556c ["INT_ADD", "register:40f0:8", ["const:78556c:8", "const:4:8"]]
- 0078556c ["CALL", null, ["callee:008514f8:8"]]
+ 007855ac ["INT_ADD", "register:40f0:8", ["const:7855ac:8", "const:4:8"]]
+ 007855ac ["CALL", null, ["callee:008514f8:8"]]
- 0078556c bytes d32f0394
+ 007855ac bytes d32f0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74412e51daf1cdaae0508e8ee29d56d0"></a>

### [`00785660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/00785660.md) → [`007856a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00785/007856a0.md) FUN_007856a0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "007856b4",
      "incomplete_value": false,
      "site": "007856b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:2a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00785674",
      "incomplete_value": false,
      "site": "00785678",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:ea0:8"
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
      "007856b8",
      "DATA",
      [
        "storage",
        "00c78ea0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007856b8",
      "DATA",
      [
        "storage",
        "00c792a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078566c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/00785660.md#insn-0078566c) · [`00785670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/00785660.md#insn-00785670) · [`00785674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/00785660.md#insn-00785674)
- 新版 `007856ac`（命令位置の公開資料なし） · `007856b0`（命令位置の公開資料なし） · `007856b4`（命令位置の公開資料なし）

~~~diff
- 0078566c ["INT_ADD", "register:40f0:8", ["const:78566c:8", "const:4:8"]]
- 0078566c ["CALL", null, ["callee:00c57e90:8"]]
+ 007856ac ["INT_ADD", "register:40f0:8", ["const:7856ac:8", "const:4:8"]]
+ 007856ac ["CALL", null, ["callee:00c57e90:8"]]
- 0078566c bytes 09491394
+ 007856ac bytes f9491394
- 00785670 ["COPY", "register:4040:8", ["const:c78000:8"]]
+ 007856b0 ["COPY", "register:4040:8", ["const:c79000:8"]]
- 00785670 bytes 882700f0
+ 007856b0 bytes a8270090
- 00785674 ["COPY", "tmp:0:8", ["const:ea0:8"]]
- 00785674 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00785674 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00785674 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007856b4 ["COPY", "tmp:0:8", ["const:2a0:8"]]
+ 007856b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007856b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007856b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00785674 bytes 08813a91
+ 007856b4 bytes 08810a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7aa69789e69e2490314de5c9bad22e25"></a>

### [`0078569c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/0078569c.md) → [`007856dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00785/007856dc.md) FUN_007856dc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

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
      "site": "00785700",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007856c0",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "00785700",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00785700",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007856c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/0078569c.md#insn-007856c0) · [`007856cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/0078569c.md#insn-007856cc)
- 新版 `00785700`（命令位置の公開資料なし） · `0078570c`（命令位置の公開資料なし）

~~~diff
- 007856c0 ["INT_ADD", "register:40f0:8", ["const:7856c0:8", "const:4:8"]]
- 007856c0 ["CALL", null, ["ram:47acb4:8"]]
+ 00785700 ["INT_ADD", "register:40f0:8", ["const:785700:8", "const:4:8"]]
+ 00785700 ["CALL", null, ["ram:47acf4:8"]]
- 007856c0 bytes 7dd5f397
+ 00785700 bytes 7dd5f397
- 007856cc ["INT_ADD", "register:40f0:8", ["const:7856cc:8", "const:4:8"]]
- 007856cc ["CALL", null, ["callee:0047cdd4:8"]]
+ 0078570c ["INT_ADD", "register:40f0:8", ["const:78570c:8", "const:4:8"]]
+ 0078570c ["CALL", null, ["callee:0047cdd4:8"]]
- 007856cc bytes b2ddf397
+ 0078570c bytes b2ddf397
~~~


<a id="compare-7fba736f4fc62d96429d667d90e54f72"></a>

### [`0078570c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/0078570c.md) → [`0078574c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00785/0078574c.md) FUN_0078574c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0077a3d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077a/0077a3d8.md) [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)
- 新版 呼出元 2件 [`0077a418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077a/0077a418.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)

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
      "definition_site": "00785758",
      "incomplete_value": false,
      "site": "0078575c",
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
    "old": {
      "definition_site": "00785718",
      "incomplete_value": false,
      "site": "0078571c",
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
            "const:f0c:8"
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
      "00785758",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00785758",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078571c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/0078570c.md#insn-0078571c) · [`00785718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/0078570c.md#insn-00785718)
- 新版 `0078575c`（命令位置の公開資料なし） · `00785758`（命令位置の公開資料なし）

~~~diff
- 0078571c ["INT_ADD", "register:40f0:8", ["const:78571c:8", "const:4:8"]]
- 0078571c ["CALL", null, ["callee:00442930:8"]]
+ 0078575c ["INT_ADD", "register:40f0:8", ["const:78575c:8", "const:4:8"]]
+ 0078575c ["CALL", null, ["callee:00442930:8"]]
- 0078571c bytes 75f4f297
+ 0078575c bytes 75f4f297
- 00785718 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00785718 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00785718 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00785718 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00785758 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00785758 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00785758 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00785758 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00785718 bytes 00303c91
+ 00785758 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6cf5bfbae100d85e29c6b281662432f1"></a>

### [`00785724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/00785724.md) → [`00785764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00785/00785764.md) FUN_00785764

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00785784",
      "incomplete_value": false,
      "site": "00785788",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:320:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00785744",
      "incomplete_value": false,
      "site": "00785748",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:f20:8"
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
      "00785788",
      "DATA",
      [
        "storage",
        "00c78f20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00785788",
      "DATA",
      [
        "storage",
        "00c79320",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00785738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/00785724.md#insn-00785738) · [`00785740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/00785724.md#insn-00785740) · [`00785744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/00785724.md#insn-00785744)
- 新版 `00785778`（命令位置の公開資料なし） · `00785780`（命令位置の公開資料なし） · `00785784`（命令位置の公開資料なし）

~~~diff
- 00785738 ["INT_ADD", "register:40f0:8", ["const:785738:8", "const:4:8"]]
- 00785738 ["CALL", null, ["callee:00c57e90:8"]]
+ 00785778 ["INT_ADD", "register:40f0:8", ["const:785778:8", "const:4:8"]]
+ 00785778 ["CALL", null, ["callee:00c57e90:8"]]
- 00785738 bytes d6481394
+ 00785778 bytes c6491394
- 00785740 ["COPY", "register:4040:8", ["const:c78000:8"]]
+ 00785780 ["COPY", "register:4040:8", ["const:c79000:8"]]
- 00785740 bytes 882700f0
+ 00785780 bytes a8270090
- 00785744 ["COPY", "tmp:0:8", ["const:f20:8"]]
- 00785744 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00785744 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00785744 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00785784 ["COPY", "tmp:0:8", ["const:320:8"]]
+ 00785784 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00785784 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00785784 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00785744 bytes 08813c91
+ 00785784 bytes 08810c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d77ab7298cb5163a1cee33380c0ba475"></a>

### [`0078575c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/0078575c.md) → [`0078579c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00785/0078579c.md) FUN_0078579c

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
      "definition_site": "007857a0",
      "incomplete_value": false,
      "site": "007857a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:320:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00785760",
      "incomplete_value": false,
      "site": "00785764",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:f20:8"
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
      "007857a4",
      "DATA",
      [
        "storage",
        "00c78f20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007857a4",
      "DATA",
      [
        "storage",
        "00c79320",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078575c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/0078575c.md#insn-0078575c) · [`00785760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/0078575c.md#insn-00785760)
- 新版 `0078579c`（命令位置の公開資料なし） · `007857a0`（命令位置の公開資料なし）

~~~diff
- 0078575c ["COPY", "register:4040:8", ["const:c78000:8"]]
+ 0078579c ["COPY", "register:4040:8", ["const:c79000:8"]]
- 0078575c bytes 882700f0
+ 0078579c bytes a8270090
- 00785760 ["COPY", "tmp:0:8", ["const:f20:8"]]
- 00785760 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00785760 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00785760 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007857a0 ["COPY", "tmp:0:8", ["const:320:8"]]
+ 007857a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007857a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007857a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00785760 bytes 08813c91
+ 007857a0 bytes 08810c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91c13624a6937424780368aa75813344"></a>

### [`0078577c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/0078577c.md) → [`007857bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00785/007857bc.md) FUN_007857bc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.08% / 新版 98.08%

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
      "site": "007857e0",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007857a0",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "007857e0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "007857e0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007857a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/0078577c.md#insn-007857a0) · [`007857ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/0078577c.md#insn-007857ac) · [`007857d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/0078577c.md#insn-007857d8)
- 新版 `007857e0`（命令位置の公開資料なし） · `007857ec`（命令位置の公開資料なし） · `00785818`（命令位置の公開資料なし）

~~~diff
- 007857a0 ["INT_ADD", "register:40f0:8", ["const:7857a0:8", "const:4:8"]]
- 007857a0 ["CALL", null, ["ram:47acb4:8"]]
+ 007857e0 ["INT_ADD", "register:40f0:8", ["const:7857e0:8", "const:4:8"]]
+ 007857e0 ["CALL", null, ["ram:47acf4:8"]]
- 007857a0 bytes 45d5f397
+ 007857e0 bytes 45d5f397
- 007857ac ["INT_ADD", "register:40f0:8", ["const:7857ac:8", "const:4:8"]]
- 007857ac ["CALL", null, ["callee:0047cdd4:8"]]
+ 007857ec ["INT_ADD", "register:40f0:8", ["const:7857ec:8", "const:4:8"]]
+ 007857ec ["CALL", null, ["callee:0047cdd4:8"]]
- 007857ac bytes 7addf397
+ 007857ec bytes 7addf397
- 007857d8 ["INT_ADD", "register:40f0:8", ["const:7857d8:8", "const:4:8"]]
- 007857d8 ["CALL", null, ["callee:008514f8:8"]]
+ 00785818 ["INT_ADD", "register:40f0:8", ["const:785818:8", "const:4:8"]]
+ 00785818 ["CALL", null, ["callee:008514f8:8"]]
- 007857d8 bytes 382f0394
+ 00785818 bytes 382f0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5372cca815b9e619110e2c302de608d3"></a>

### [`00785878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/00785878.md) → [`007858b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00785/007858b8.md) FUN_007858b8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "007858dc",
      "incomplete_value": false,
      "site": "007858dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:3a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078589c",
      "incomplete_value": false,
      "site": "0078589c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:fa0:8"
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
      "007858dc",
      "DATA",
      [
        "storage",
        "00c78fa0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007858dc",
      "DATA",
      [
        "storage",
        "00c793a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078588c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/00785878.md#insn-0078588c) · [`00785894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/00785878.md#insn-00785894) · [`00785898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/00785878.md#insn-00785898)
- 新版 `007858cc`（命令位置の公開資料なし） · `007858d4`（命令位置の公開資料なし） · `007858d8`（命令位置の公開資料なし）

~~~diff
- 0078588c ["INT_ADD", "register:40f0:8", ["const:78588c:8", "const:4:8"]]
- 0078588c ["CALL", null, ["callee:00c57e90:8"]]
+ 007858cc ["INT_ADD", "register:40f0:8", ["const:7858cc:8", "const:4:8"]]
+ 007858cc ["CALL", null, ["callee:00c57e90:8"]]
- 0078588c bytes 81481394
+ 007858cc bytes 71491394
- 00785894 ["COPY", "register:4040:8", ["const:c78000:8"]]
+ 007858d4 ["COPY", "register:4040:8", ["const:c79000:8"]]
- 00785894 bytes 882700f0
+ 007858d4 bytes a8270090
- 00785898 ["COPY", "tmp:0:8", ["const:fa0:8"]]
- 00785898 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00785898 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00785898 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007858d8 ["COPY", "tmp:0:8", ["const:3a0:8"]]
+ 007858d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007858d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007858d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00785898 bytes 08813e91
+ 007858d8 bytes 08810e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba869374c682daa54821c7fa28f03301"></a>

### [`007858ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/007858ac.md) → [`007858ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00785/007858ec.md) FUN_007858ec

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
      "definition_site": "007858f8",
      "incomplete_value": false,
      "site": "007858f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:3a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007858b8",
      "incomplete_value": false,
      "site": "007858b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c78000:8"
          ],
          [
            "leaf",
            "const:fa0:8"
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
      "007858f8",
      "DATA",
      [
        "storage",
        "00c78fa0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007858f8",
      "DATA",
      [
        "storage",
        "00c793a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007858b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/007858ac.md#insn-007858b0) · [`007858b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/007858ac.md#insn-007858b4)
- 新版 `007858f0`（命令位置の公開資料なし） · `007858f4`（命令位置の公開資料なし）

~~~diff
- 007858b0 ["COPY", "register:4048:8", ["const:c78000:8"]]
+ 007858f0 ["COPY", "register:4048:8", ["const:c79000:8"]]
- 007858b0 bytes 892700f0
+ 007858f0 bytes a9270090
- 007858b4 ["COPY", "tmp:0:8", ["const:fa0:8"]]
- 007858b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007858b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007858b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007858f4 ["COPY", "tmp:0:8", ["const:3a0:8"]]
+ 007858f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007858f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007858f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007858b4 bytes 29813e91
+ 007858f4 bytes 29810e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04df2666c1eff9d986f3a286df35f275"></a>

### [`0078592c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/0078592c.md) → [`0078596c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00785/0078596c.md) FUN_0078596c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00785990",
      "incomplete_value": false,
      "site": "00785990",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00785950",
      "incomplete_value": false,
      "site": "00785950",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:20:8"
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
      "00785990",
      "DATA",
      [
        "storage",
        "00c79020",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00785990",
      "DATA",
      [
        "storage",
        "00c79420",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00785940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/0078592c.md#insn-00785940) · [`0078594c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/0078592c.md#insn-0078594c)
- 新版 `00785980`（命令位置の公開資料なし） · `0078598c`（命令位置の公開資料なし）

~~~diff
- 00785940 ["INT_ADD", "register:40f0:8", ["const:785940:8", "const:4:8"]]
- 00785940 ["CALL", null, ["callee:00c57e90:8"]]
+ 00785980 ["INT_ADD", "register:40f0:8", ["const:785980:8", "const:4:8"]]
+ 00785980 ["CALL", null, ["callee:00c57e90:8"]]
- 00785940 bytes 54481394
+ 00785980 bytes 44491394
- 0078594c ["COPY", "tmp:0:8", ["const:20:8"]]
- 0078594c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0078594c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0078594c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0078598c ["COPY", "tmp:0:8", ["const:420:8"]]
+ 0078598c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0078598c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0078598c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0078594c bytes 08810091
+ 0078598c bytes 08811091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71e48bbb54d291e430804d4a03a87e99"></a>

### [`00785960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/00785960.md) → [`007859a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00785/007859a0.md) FUN_007859a0

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
      "definition_site": "007859ac",
      "incomplete_value": false,
      "site": "007859ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078596c",
      "incomplete_value": false,
      "site": "0078596c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:20:8"
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
      "007859ac",
      "DATA",
      [
        "storage",
        "00c79020",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007859ac",
      "DATA",
      [
        "storage",
        "00c79420",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00785968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/00785960.md#insn-00785968)
- 新版 `007859a8`（命令位置の公開資料なし）

~~~diff
- 00785968 ["COPY", "tmp:0:8", ["const:20:8"]]
- 00785968 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00785968 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00785968 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007859a8 ["COPY", "tmp:0:8", ["const:420:8"]]
+ 007859a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007859a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007859a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00785968 bytes 29810091
+ 007859a8 bytes 29811091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb02162328283d343338a77618323ac9"></a>

### [`0078597c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/0078597c.md) → [`007859bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00785/007859bc.md) FUN_007859bc

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 11件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00800338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/00800338.md) [`008025f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/008025f0.md) [`00806188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00806/00806188.md) [`00806264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00806/00806264.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00800378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/00800378.md) [`00802630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802630.md) [`008061c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00806/008061c8.md) [`008062a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00806/008062a4.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.21% / 新版 95.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007859f8",
      "incomplete_value": false,
      "site": "00785a04",
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
      "definition_site": "007859b8",
      "incomplete_value": false,
      "site": "007859c4",
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
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00785a9c",
      "value": [
        "leaf",
        "ram:807104:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00785a5c",
      "value": [
        "leaf",
        "ram:8070c4:8"
      ]
    },
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00785aac",
      "value": [
        "leaf",
        "ram:8061c8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00785a6c",
      "value": [
        "leaf",
        "ram:806188:8"
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
      "007859f8",
      "PARAM",
      [
        "storage",
        "002a630e",
        null,
        "undefined1"
      ]
    ],
    [
      "00785a9c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "008070c4"
      ]
    ],
    [
      "00785aac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00806188"
      ]
    ]
  ],
  "added": [
    [
      "007859f8",
      "PARAM",
      [
        "storage",
        "002a63ea",
        null,
        "undefined1"
      ]
    ],
    [
      "00785a9c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00807104"
      ]
    ],
    [
      "00785aac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "008061c8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007859c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/0078597c.md#insn-007859c4) · [`00785a5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/0078597c.md#insn-00785a5c) · [`00785a6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/0078597c.md#insn-00785a6c)
- 新版 `00785a04`（命令位置の公開資料なし） · `00785a9c`（命令位置の公開資料なし） · `00785aac`（命令位置の公開資料なし）

~~~diff
- 007859c4 ["INT_ADD", "register:40f0:8", ["const:7859c4:8", "const:4:8"]]
- 007859c4 ["CALL", null, ["callee:00c58190:8"]]
+ 00785a04 ["INT_ADD", "register:40f0:8", ["const:785a04:8", "const:4:8"]]
+ 00785a04 ["CALL", null, ["callee:00c58190:8"]]
- 007859c4 bytes f3481394
+ 00785a04 bytes e3491394
- 00785a5c ["INT_ADD", "register:40f0:8", ["const:785a5c:8", "const:4:8"]]
- 00785a5c ["CALL", null, ["ram:8070c4:8"]]
+ 00785a9c ["INT_ADD", "register:40f0:8", ["const:785a9c:8", "const:4:8"]]
+ 00785a9c ["CALL", null, ["ram:807104:8"]]
- 00785a5c bytes 9a050294
+ 00785a9c bytes 9a050294
- 00785a6c ["INT_ADD", "register:40f0:8", ["const:785a6c:8", "const:4:8"]]
- 00785a6c ["CALL", null, ["ram:806188:8"]]
+ 00785aac ["INT_ADD", "register:40f0:8", ["const:785aac:8", "const:4:8"]]
+ 00785aac ["CALL", null, ["ram:8061c8:8"]]
- 00785a6c bytes c7010294
+ 00785aac bytes c7010294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c54e7ca7799aead24fac520b91169432"></a>

### [`00785c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/00785c40.md) → [`00785c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00785/00785c80.md) _INIT_134

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.14% / 新版 88.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00785ce0",
      "incomplete_value": true,
      "site": "00785cfc",
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
    "old": {
      "definition_site": "00785ca0",
      "incomplete_value": true,
      "site": "00785cbc",
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
                "const:ef9:8"
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
      "definition_site": "00785d00",
      "incomplete_value": true,
      "site": "00785d1c",
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
    "old": {
      "definition_site": "00785cc0",
      "incomplete_value": true,
      "site": "00785cdc",
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
                "const:d82:8"
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
      "definition_site": "00785d5c",
      "incomplete_value": true,
      "site": "00785d78",
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
                "const:2a0000:8"
              ],
              [
                "leaf",
                "const:f5d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00785d1c",
      "incomplete_value": true,
      "site": "00785d38",
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
                "const:2a0000:8"
              ],
              [
                "leaf",
                "const:e90:8"
              ]
            ]
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
      "00785cbc",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00785ce0",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "00785d00",
      "READ",
      [
        "storage",
        "002b8d82",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00785cbc",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00785ce0",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00785d00",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00785e74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/00785c40.md#insn-00785e74) · [`00785c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/00785c40.md#insn-00785c6c) · [`00785c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/00785c40.md#insn-00785c74)
- 新版 `00785eb4`（命令位置の公開資料なし） · `00785cac`（命令位置の公開資料なし）

~~~diff
- 00785e74 ["INT_ADD", "register:40f0:8", ["const:785e74:8", "const:4:8"]]
- 00785e74 ["CALL", null, ["callee:00c57e30:8"]]
+ 00785eb4 ["INT_ADD", "register:40f0:8", ["const:785eb4:8", "const:4:8"]]
+ 00785eb4 ["CALL", null, ["callee:00c57e30:8"]]
- 00785e74 bytes ef461394
+ 00785eb4 bytes df471394
- 00785c6c ["COPY", "tmp:0:8", ["const:a08:8"]]
- 00785c6c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00785c6c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00785c6c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00785cac ["COPY", "tmp:0:8", ["const:e08:8"]]
+ 00785cac ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00785cac ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00785cac ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00785c6c bytes 73222891
+ 00785cac bytes 73223891
- 00785c74 ["COPY", "register:4048:8", ["const:2b7000:8"]]
- 00785c74 bytes 89d9ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-279a987b0a7a1d4754e4db294b5278c6"></a>

### [`00785fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/00785fd0.md) → [`00786010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00786/00786010.md) FUN_00786010

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00764a8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764a8c.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00764acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764acc.md) · 呼出先 0件 

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
      "definition_site": "0078601c",
      "incomplete_value": true,
      "site": "00786034",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00785fdc",
      "incomplete_value": true,
      "site": "00785ff4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a0:8"
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
      "0078601c",
      "READ",
      [
        "storage",
        "002c40a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0078601c",
      "READ",
      [
        "storage",
        "002c40e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00785fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/00785fd0.md#insn-00785fdc)
- 新版 `0078601c`（命令位置の公開資料なし）

~~~diff
- 00785fdc ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:a0:8"]]
- 00785fdc ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
- 00785fdc ["COPY", "register:5008:8", ["const:0:8"]]
- 00785fdc ["COPY", "register:5010:8", ["const:0:8"]]
+ 0078601c ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:e0:8"]]
+ 0078601c ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0078601c ["COPY", "register:5008:8", ["const:0:8"]]
+ 0078601c ["COPY", "register:5010:8", ["const:0:8"]]
- 00785fdc bytes 405140fd
+ 0078601c bytes 407140fd
~~~


<a id="compare-b25e8149080cdecb4625167399dca3fd"></a>

### [`0078610c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00786/0078610c.md) → [`0078614c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00786/0078614c.md) FUN_0078614c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 16件 [`00785ffc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/00785ffc.md) [`007863ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00786/007863ac.md) [`007867cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00786/007867cc.md) [`00786b68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00786/00786b68.md) [`00786c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00786/00786c94.md)
- 新版 呼出元 1件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) · 呼出先 16件 [`0078603c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00786/0078603c.md) [`007863ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00786/007863ec.md) [`0078680c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00786/0078680c.md) [`00786ba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00786/00786ba8.md) [`00786cd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00786/00786cd4.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.40% / 新版 99.40%

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
      "site": "00786398",
      "value": [
        "leaf",
        "ram:a65dec:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00786358",
      "value": [
        "leaf",
        "ram:a65bf4:8"
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
      "00786398",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65bf4"
      ]
    ]
  ],
  "added": [
    [
      "00786398",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65dec"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00786358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00786/0078610c.md#insn-00786358) · [`00786170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00786/0078610c.md#insn-00786170) · [`00786180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00786/0078610c.md#insn-00786180)
- 新版 `00786398`（命令位置の公開資料なし） · `007861b0`（命令位置の公開資料なし） · `007861c0`（命令位置の公開資料なし）

~~~diff
- 00786358 ["INT_ADD", "register:40f0:8", ["const:786358:8", "const:4:8"]]
- 00786358 ["CALL", null, ["ram:a65bf4:8"]]
+ 00786398 ["INT_ADD", "register:40f0:8", ["const:786398:8", "const:4:8"]]
+ 00786398 ["CALL", null, ["ram:a65dec:8"]]
- 00786358 bytes 277e0b94
+ 00786398 bytes 957e0b94
- 00786170 ["INT_ADD", "register:40f0:8", ["const:786170:8", "const:4:8"]]
- 00786170 ["CALL", null, ["callee:00801c44:8"]]
+ 007861b0 ["INT_ADD", "register:40f0:8", ["const:7861b0:8", "const:4:8"]]
+ 007861b0 ["CALL", null, ["callee:00801c44:8"]]
- 00786170 bytes a5ee0194
+ 007861b0 bytes a5ee0194
- 00786180 ["INT_ADD", "register:40f0:8", ["const:786180:8", "const:4:8"]]
- 00786180 ["CALL", null, ["callee:00801c90:8"]]
+ 007861c0 ["INT_ADD", "register:40f0:8", ["const:7861c0:8", "const:4:8"]]
+ 007861c0 ["CALL", null, ["callee:00801c90:8"]]
- 00786180 bytes b4ee0194
+ 007861c0 bytes b4ee0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-690f41413fdb2f382677bed59b5f09f9"></a>

### [`007863ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00786/007863ac.md) → [`007863ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00786/007863ec.md) FUN_007863ec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0078610c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00786/0078610c.md) · 呼出先 14件 [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md) [`005d8b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8b88.md) [`00788204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/00788204.md) [`00788208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/00788208.md) [`008b6eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6eec.md)
- 新版 呼出元 1件 [`0078614c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00786/0078614c.md) · 呼出先 14件 [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md) [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md) [`00788244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00788/00788244.md) [`00788248`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00788/00788248.md) [`008b6f30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.25% / 新版 98.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0078665c",
      "incomplete_value": false,
      "site": "0078665c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:4b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078661c",
      "incomplete_value": false,
      "site": "0078661c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:b0:8"
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
      "007864f0",
      "READ",
      [
        "storage",
        "00c9af68",
        null,
        "pointer"
      ]
    ],
    [
      "00786504",
      "DATA",
      [
        "storage",
        "00c8b358",
        null,
        "undefined *"
      ]
    ],
    [
      "0078651c",
      "READ",
      [
        "storage",
        "00c9af70",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007864f0",
      "READ",
      [
        "storage",
        "00c9b368",
        null,
        "pointer"
      ]
    ],
    [
      "00786504",
      "DATA",
      [
        "storage",
        "00c8b758",
        null,
        "undefined *"
      ]
    ],
    [
      "0078651c",
      "READ",
      [
        "storage",
        "00c9b370",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007863f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00786/007863ac.md#insn-007863f0) · [`00786408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00786/007863ac.md#insn-00786408) · [`00786444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00786/007863ac.md#insn-00786444)
- 新版 `00786430`（命令位置の公開資料なし） · `00786448`（命令位置の公開資料なし） · `00786484`（命令位置の公開資料なし）

~~~diff
- 007863f0 ["INT_ADD", "register:40f0:8", ["const:7863f0:8", "const:4:8"]]
- 007863f0 ["CALL", null, ["callee:00489f4c:8"]]
+ 00786430 ["INT_ADD", "register:40f0:8", ["const:786430:8", "const:4:8"]]
+ 00786430 ["CALL", null, ["callee:00489f4c:8"]]
- 007863f0 bytes c70ef497
+ 00786430 bytes c70ef497
- 00786408 ["INT_ADD", "register:40f0:8", ["const:786408:8", "const:4:8"]]
- 00786408 ["CALL", null, ["callee:00489f4c:8"]]
+ 00786448 ["INT_ADD", "register:40f0:8", ["const:786448:8", "const:4:8"]]
+ 00786448 ["CALL", null, ["callee:00489f4c:8"]]
- 00786408 bytes c10ef497
+ 00786448 bytes c10ef497
- 00786444 ["INT_ADD", "register:40f0:8", ["const:786444:8", "const:4:8"]]
- 00786444 ["CALL", null, ["callee:00a468fc:8"]]
+ 00786484 ["INT_ADD", "register:40f0:8", ["const:786484:8", "const:4:8"]]
+ 00786484 ["CALL", null, ["callee:00a468fc:8"]]
- 00786444 bytes b0000b94
+ 00786484 bytes 1e010b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dafeca2a66a6c7ca678f84bdfd9949f9"></a>

### [`007867cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00786/007867cc.md) → [`0078680c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00786/0078680c.md) FUN_0078680c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0078610c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00786/0078610c.md) · 呼出先 13件 [`005d8b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8b88.md) [`00788374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/00788374.md) [`008b6fa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6fa8.md) [`00a4658c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a4658c.md) [`00a466d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a466d0.md)
- 新版 呼出元 1件 [`0078614c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00786/0078614c.md) · 呼出先 13件 [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md) [`007883b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00788/007883b4.md) [`008b6fec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6fec.md) [`00a46784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46784.md) [`00a468c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a468c8.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.90% / 新版 95.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00786940",
      "incomplete_value": true,
      "site": "00786944",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00786900",
      "incomplete_value": true,
      "site": "00786904",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00786a98",
      "incomplete_value": true,
      "site": "00786a9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00786a58",
      "incomplete_value": true,
      "site": "00786a5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00786900",
      "READ",
      [
        "storage",
        "00c9af68",
        null,
        "pointer"
      ]
    ],
    [
      "00786918",
      "DATA",
      [
        "storage",
        "00c8b358",
        null,
        "undefined *"
      ]
    ],
    [
      "0078693c",
      "READ",
      [
        "storage",
        "00c9af70",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00786900",
      "READ",
      [
        "storage",
        "00c9b368",
        null,
        "pointer"
      ]
    ],
    [
      "00786918",
      "DATA",
      [
        "storage",
        "00c8b758",
        null,
        "undefined *"
      ]
    ],
    [
      "0078693c",
      "READ",
      [
        "storage",
        "00c9b370",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078682c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00786/007867cc.md#insn-0078682c) · [`00786840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00786/007867cc.md#insn-00786840) · [`00786850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00786/007867cc.md#insn-00786850)
- 新版 `0078686c`（命令位置の公開資料なし） · `00786880`（命令位置の公開資料なし） · `00786890`（命令位置の公開資料なし）

~~~diff
- 0078682c ["INT_ADD", "register:40f0:8", ["const:78682c:8", "const:4:8"]]
- 0078682c ["CALL", null, ["callee:00a468fc:8"]]
+ 0078686c ["INT_ADD", "register:40f0:8", ["const:78686c:8", "const:4:8"]]
+ 0078686c ["CALL", null, ["callee:00a468fc:8"]]
- 0078682c bytes b6ff0a94
+ 0078686c bytes 24000b94
- 00786840 ["INT_ADD", "register:40f0:8", ["const:786840:8", "const:4:8"]]
- 00786840 ["CALL", null, ["callee:00a46c2c:8"]]
+ 00786880 ["INT_ADD", "register:40f0:8", ["const:786880:8", "const:4:8"]]
+ 00786880 ["CALL", null, ["callee:00a46c2c:8"]]
- 00786840 bytes 7d000b94
+ 00786880 bytes eb000b94
- 00786850 ["COPY", "register:0:8", ["register:4040:8"]]
- 00786850 ["INT_ADD", "register:40f0:8", ["const:786850:8", "const:4:8"]]
- 00786850 ["CALLIND", null, ["register:0:8"]]
+ 00786890 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00786890 ["INT_ADD", "register:40f0:8", ["const:786890:8", "const:4:8"]]
+ 00786890 ["CALLIND", null, ["register:0:8"]]
- 00786850 bytes 00013fd6
+ 00786890 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8dd9d9da51f775d4bf7fdabed4d0e440"></a>

### [`00786c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00786/00786c94.md) → [`00786cd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00786/00786cd4.md) FUN_00786cd4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0078610c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00786/0078610c.md) · 呼出先 16件 [`005d8b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8b88.md) [`007884ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/007884ec.md) [`007884f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/007884f0.md) [`008b6e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e80.md) [`008b6fa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6fa8.md)
- 新版 呼出元 1件 [`0078614c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00786/0078614c.md) · 呼出先 16件 [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md) [`0078852c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00788/0078852c.md) [`00788530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00788/00788530.md) [`008b6ec4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6ec4.md) [`008b6fec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6fec.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.61% / 新版 98.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007871c0",
      "incomplete_value": false,
      "site": "007871c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:5b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00787180",
      "incomplete_value": false,
      "site": "00787180",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:1b0:8"
          ]
        ]
      ]
    },
    "ordinal": 54,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00786ddc",
      "READ",
      [
        "storage",
        "00c9af68",
        null,
        "pointer"
      ]
    ],
    [
      "00786df0",
      "DATA",
      [
        "storage",
        "00c8b358",
        null,
        "undefined *"
      ]
    ],
    [
      "00786e08",
      "READ",
      [
        "storage",
        "00c9af70",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00786ddc",
      "READ",
      [
        "storage",
        "00c9b368",
        null,
        "pointer"
      ]
    ],
    [
      "00786df0",
      "DATA",
      [
        "storage",
        "00c8b758",
        null,
        "undefined *"
      ]
    ],
    [
      "00786e08",
      "READ",
      [
        "storage",
        "00c9b370",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00786cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00786/00786c94.md#insn-00786cf4) · [`00786d14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00786/00786c94.md#insn-00786d14) · [`00786d2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00786/00786c94.md#insn-00786d2c)
- 新版 `00786d34`（命令位置の公開資料なし） · `00786d54`（命令位置の公開資料なし） · `00786d6c`（命令位置の公開資料なし）

~~~diff
- 00786cf4 ["INT_ADD", "register:40f0:8", ["const:786cf4:8", "const:4:8"]]
- 00786cf4 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00786d34 ["INT_ADD", "register:40f0:8", ["const:786d34:8", "const:4:8"]]
+ 00786d34 ["CALL", null, ["callee:00c53cd0:8"]]
- 00786cf4 bytes ef321394
+ 00786d34 bytes e7331394
- 00786d14 ["INT_ADD", "register:40f0:8", ["const:786d14:8", "const:4:8"]]
- 00786d14 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00786d54 ["INT_ADD", "register:40f0:8", ["const:786d54:8", "const:4:8"]]
+ 00786d54 ["CALL", null, ["callee:00c53cd0:8"]]
- 00786d14 bytes e7321394
+ 00786d54 bytes df331394
- 00786d2c ["INT_ADD", "register:40f0:8", ["const:786d2c:8", "const:4:8"]]
- 00786d2c ["CALL", null, ["callee:00a468fc:8"]]
+ 00786d6c ["INT_ADD", "register:40f0:8", ["const:786d6c:8", "const:4:8"]]
+ 00786d6c ["CALL", null, ["callee:00a468fc:8"]]
- 00786d2c bytes 76fe0a94
+ 00786d6c bytes e4fe0a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49a970ea8d30b135fcf06635eaa55795"></a>

### [`007874d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/007874d8.md) → [`00787518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00787/00787518.md) FUN_00787518

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0078610c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00786/0078610c.md) [`007877bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/007877bc.md) · 呼出先 11件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00800338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/00800338.md) [`008025f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/008025f0.md) [`00806188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00806/00806188.md) [`00806264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00806/00806264.md)
- 新版 呼出元 2件 [`0078614c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00786/0078614c.md) [`007877fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00787/007877fc.md) · 呼出先 11件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00800378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/00800378.md) [`00802630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802630.md) [`008061c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00806/008061c8.md) [`008062a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00806/008062a4.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.76% / 新版 97.76%

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
      "site": "00787594",
      "value": [
        "leaf",
        "ram:807104:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00787554",
      "value": [
        "leaf",
        "ram:8070c4:8"
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
      "site": "007875a4",
      "value": [
        "leaf",
        "ram:8061c8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00787564",
      "value": [
        "leaf",
        "ram:806188:8"
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0078766c",
      "value": [
        "leaf",
        "ram:8062a4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0078762c",
      "value": [
        "leaf",
        "ram:806264:8"
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
      "00787594",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "008070c4"
      ]
    ],
    [
      "007875a4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00806188"
      ]
    ],
    [
      "0078766c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00806264"
      ]
    ]
  ],
  "added": [
    [
      "00787594",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00807104"
      ]
    ],
    [
      "007875a4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "008061c8"
      ]
    ],
    [
      "0078766c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "008062a4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00787554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/007874d8.md#insn-00787554) · [`00787564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/007874d8.md#insn-00787564) · [`0078762c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/007874d8.md#insn-0078762c)
- 新版 `00787594`（命令位置の公開資料なし） · `007875a4`（命令位置の公開資料なし） · `0078766c`（命令位置の公開資料なし）

~~~diff
- 00787554 ["INT_ADD", "register:40f0:8", ["const:787554:8", "const:4:8"]]
- 00787554 ["CALL", null, ["ram:8070c4:8"]]
+ 00787594 ["INT_ADD", "register:40f0:8", ["const:787594:8", "const:4:8"]]
+ 00787594 ["CALL", null, ["ram:807104:8"]]
- 00787554 bytes dcfe0194
+ 00787594 bytes dcfe0194
- 00787564 ["INT_ADD", "register:40f0:8", ["const:787564:8", "const:4:8"]]
- 00787564 ["CALL", null, ["ram:806188:8"]]
+ 007875a4 ["INT_ADD", "register:40f0:8", ["const:7875a4:8", "const:4:8"]]
+ 007875a4 ["CALL", null, ["ram:8061c8:8"]]
- 00787564 bytes 09fb0194
+ 007875a4 bytes 09fb0194
- 0078762c ["INT_ADD", "register:40f0:8", ["const:78762c:8", "const:4:8"]]
- 0078762c ["CALL", null, ["ram:806264:8"]]
+ 0078766c ["INT_ADD", "register:40f0:8", ["const:78766c:8", "const:4:8"]]
+ 0078766c ["CALL", null, ["ram:8062a4:8"]]
- 0078762c bytes 0efb0194
+ 0078766c bytes 0efb0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-312c36f56e66e9d1d83594b9115972fd"></a>

### [`007877bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/007877bc.md) → [`007877fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00787/007877fc.md) FUN_007877fc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00788378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/00788378.md) · 呼出先 10件 [`00785ffc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/00785ffc.md) [`00786b68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00786/00786b68.md) [`00787440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/00787440.md) [`007874d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/007874d8.md) [`00800338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/00800338.md)
- 新版 呼出元 1件 [`007883b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00788/007883b8.md) · 呼出先 10件 [`0078603c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00786/0078603c.md) [`00786ba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00786/00786ba8.md) [`00787480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00787/00787480.md) [`00787518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00787/00787518.md) [`00800378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/00800378.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.19% / 新版 99.19%

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
      "site": "007878d4",
      "value": [
        "leaf",
        "ram:a65dec:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00787894",
      "value": [
        "leaf",
        "ram:a65bf4:8"
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
      "007878d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65bf4"
      ]
    ]
  ],
  "added": [
    [
      "007878d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65dec"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00787894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/007877bc.md#insn-00787894) · [`0078783c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/007877bc.md#insn-0078783c) · [`00787844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/007877bc.md#insn-00787844)
- 新版 `007878d4`（命令位置の公開資料なし） · `0078787c`（命令位置の公開資料なし） · `00787884`（命令位置の公開資料なし）

~~~diff
- 00787894 ["INT_ADD", "register:40f0:8", ["const:787894:8", "const:4:8"]]
- 00787894 ["CALL", null, ["ram:a65bf4:8"]]
+ 007878d4 ["INT_ADD", "register:40f0:8", ["const:7878d4:8", "const:4:8"]]
+ 007878d4 ["CALL", null, ["ram:a65dec:8"]]
- 00787894 bytes d8780b94
+ 007878d4 bytes 46790b94
- 0078783c ["INT_ADD", "register:40f0:8", ["const:78783c:8", "const:4:8"]]
- 0078783c ["CALL", null, ["callee:00787480:8"]]
+ 0078787c ["INT_ADD", "register:40f0:8", ["const:78787c:8", "const:4:8"]]
+ 0078787c ["CALL", null, ["callee:00787480:8"]]
- 0078783c bytes 01ffff97
+ 0078787c bytes 01ffff97
- 00787844 ["INT_ADD", "register:40f0:8", ["const:787844:8", "const:4:8"]]
- 00787844 ["CALL", null, ["callee:00800378:8"]]
+ 00787884 ["INT_ADD", "register:40f0:8", ["const:787884:8", "const:4:8"]]
+ 00787884 ["CALL", null, ["callee:00800378:8"]]
- 00787844 bytes bde20194
+ 00787884 bytes bde20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6a13f367cda7e82103da7394648c92e"></a>

### [`00787bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/00787bc0.md) → [`00787c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00787/00787c00.md) FUN_00787c00

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00773854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773854.md) · 呼出先 8件 [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md) [`00467f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467f14.md) [`00468b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468b9c.md) [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md)
- 新版 呼出元 1件 [`00773894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/00773894.md) · 呼出先 8件 [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md) [`00467f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f54.md) [`00468bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468bdc.md) [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.33% / 新版 96.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00787c80",
      "incomplete_value": true,
      "site": "00787c88",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
      "definition_site": "00787c40",
      "incomplete_value": true,
      "site": "00787c48",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00787ca4",
      "incomplete_value": true,
      "site": "00787ca8",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
      "definition_site": "00787c64",
      "incomplete_value": true,
      "site": "00787c68",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00787cc4",
      "incomplete_value": true,
      "site": "00787cc8",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
      "definition_site": "00787c84",
      "incomplete_value": true,
      "site": "00787c88",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00787c80",
      "READ",
      [
        "storage",
        "00ca3b0c",
        null,
        "undefined4"
      ]
    ],
    [
      "00787ca4",
      "READ",
      [
        "storage",
        "00ca3b10",
        null,
        "undefined4"
      ]
    ],
    [
      "00787cc4",
      "READ",
      [
        "storage",
        "00ca3b14",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00787c80",
      "READ",
      [
        "storage",
        "00ca3f0c",
        null,
        "undefined4"
      ]
    ],
    [
      "00787ca4",
      "READ",
      [
        "storage",
        "00ca3f10",
        null,
        "undefined4"
      ]
    ],
    [
      "00787cc4",
      "READ",
      [
        "storage",
        "00ca3f14",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00787c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/00787bc0.md#insn-00787c08) · [`00787c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/00787bc0.md#insn-00787c48) · [`00787c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/00787bc0.md#insn-00787c68)
- 新版 `00787c48`（命令位置の公開資料なし） · `00787c88`（命令位置の公開資料なし） · `00787ca8`（命令位置の公開資料なし）

~~~diff
- 00787c08 ["INT_ADD", "register:40f0:8", ["const:787c08:8", "const:4:8"]]
- 00787c08 ["CALL", null, ["callee:00467b2c:8"]]
+ 00787c48 ["INT_ADD", "register:40f0:8", ["const:787c48:8", "const:4:8"]]
+ 00787c48 ["CALL", null, ["callee:00467b2c:8"]]
- 00787c08 bytes b97ff397
+ 00787c48 bytes b97ff397
- 00787c48 ["INT_ADD", "register:40f0:8", ["const:787c48:8", "const:4:8"]]
- 00787c48 ["CALL", null, ["callee:008b79c8:8"]]
+ 00787c88 ["INT_ADD", "register:40f0:8", ["const:787c88:8", "const:4:8"]]
+ 00787c88 ["CALL", null, ["callee:008b79c8:8"]]
- 00787c48 bytes 4fbf0494
+ 00787c88 bytes 50bf0494
- 00787c68 ["INT_ADD", "register:40f0:8", ["const:787c68:8", "const:4:8"]]
- 00787c68 ["CALL", null, ["callee:008b79c8:8"]]
+ 00787ca8 ["INT_ADD", "register:40f0:8", ["const:787ca8:8", "const:4:8"]]
+ 00787ca8 ["CALL", null, ["callee:008b79c8:8"]]
- 00787c68 bytes 47bf0494
+ 00787ca8 bytes 48bf0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1101b2f94ce2cde3abd7b3f3afd2697f"></a>

### [`00787d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/00787d74.md) → [`00787db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00787/00787db4.md) FUN_00787db4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00787bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/00787bc0.md) · 呼出先 6件 [`00468c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468c20.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md) [`0046a8a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046a8a8.md) [`00729a64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00729/00729a64.md)
- 新版 呼出元 1件 [`00787c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00787/00787c00.md) · 呼出先 6件 [`00468c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468c60.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md) [`0046a8e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a8e8.md) [`00729aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00729/00729aa4.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.81% / 新版 98.81%

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
      "site": "00787df4",
      "value": [
        "leaf",
        "ram:729aa4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00787db4",
      "value": [
        "leaf",
        "ram:729a64:8"
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
      "00787df4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00729a64"
      ]
    ]
  ],
  "added": [
    [
      "00787df4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00729aa4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00787db4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/00787d74.md#insn-00787db4) · [`00787dd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/00787d74.md#insn-00787dd4) · [`00787e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/00787d74.md#insn-00787e10)
- 新版 `00787df4`（命令位置の公開資料なし） · `00787e14`（命令位置の公開資料なし） · `00787e50`（命令位置の公開資料なし）

~~~diff
- 00787db4 ["INT_ADD", "register:40f0:8", ["const:787db4:8", "const:4:8"]]
- 00787db4 ["CALL", null, ["ram:729a64:8"]]
+ 00787df4 ["INT_ADD", "register:40f0:8", ["const:787df4:8", "const:4:8"]]
+ 00787df4 ["CALL", null, ["ram:729aa4:8"]]
- 00787db4 bytes 2c87fe97
+ 00787df4 bytes 2c87fe97
- 00787dd4 ["INT_ADD", "register:40f0:8", ["const:787dd4:8", "const:4:8"]]
- 00787dd4 ["CALL", null, ["callee:0046a8e8:8"]]
+ 00787e14 ["INT_ADD", "register:40f0:8", ["const:787e14:8", "const:4:8"]]
+ 00787e14 ["CALL", null, ["callee:0046a8e8:8"]]
- 00787dd4 bytes b58af397
+ 00787e14 bytes b58af397
- 00787e10 ["INT_ADD", "register:40f0:8", ["const:787e10:8", "const:4:8"]]
- 00787e10 ["CALL", null, ["callee:00469c04:8"]]
+ 00787e50 ["INT_ADD", "register:40f0:8", ["const:787e50:8", "const:4:8"]]
+ 00787e50 ["CALL", null, ["callee:00469c04:8"]]
- 00787e10 bytes 6d87f397
+ 00787e50 bytes 6d87f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aec25de4986bbde99363599d2d4a1b9f"></a>

### [`007881bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/007881bc.md) → [`007881fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00788/007881fc.md) FUN_007881fc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00788220",
      "incomplete_value": false,
      "site": "00788220",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:4b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007881e0",
      "incomplete_value": false,
      "site": "007881e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:b0:8"
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
      "00788220",
      "DATA",
      [
        "storage",
        "00c790b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00788220",
      "DATA",
      [
        "storage",
        "00c794b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007881d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/007881bc.md#insn-007881d0) · [`007881dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/007881bc.md#insn-007881dc)
- 新版 `00788210`（命令位置の公開資料なし） · `0078821c`（命令位置の公開資料なし）

~~~diff
- 007881d0 ["INT_ADD", "register:40f0:8", ["const:7881d0:8", "const:4:8"]]
- 007881d0 ["CALL", null, ["callee:00c57e90:8"]]
+ 00788210 ["INT_ADD", "register:40f0:8", ["const:788210:8", "const:4:8"]]
+ 00788210 ["CALL", null, ["callee:00c57e90:8"]]
- 007881d0 bytes 303e1394
+ 00788210 bytes 203f1394
- 007881dc ["COPY", "tmp:0:8", ["const:b0:8"]]
- 007881dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007881dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007881dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0078821c ["COPY", "tmp:0:8", ["const:4b0:8"]]
+ 0078821c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0078821c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0078821c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007881dc bytes 08c10291
+ 0078821c bytes 08c11291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f2bc2b29f76d521fb62429ec3f63fae"></a>

### [`007881f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/007881f0.md) → [`00788230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00788/00788230.md) FUN_00788230

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
      "definition_site": "0078823c",
      "incomplete_value": false,
      "site": "0078823c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:4b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007881fc",
      "incomplete_value": false,
      "site": "007881fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:b0:8"
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
      "0078823c",
      "DATA",
      [
        "storage",
        "00c790b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0078823c",
      "DATA",
      [
        "storage",
        "00c794b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007881f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/007881f0.md#insn-007881f8)
- 新版 `00788238`（命令位置の公開資料なし）

~~~diff
- 007881f8 ["COPY", "tmp:0:8", ["const:b0:8"]]
- 007881f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007881f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007881f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00788238 ["COPY", "tmp:0:8", ["const:4b0:8"]]
+ 00788238 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00788238 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00788238 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007881f8 bytes 29c10291
+ 00788238 bytes 29c11291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18e5dfc7cc8b7c041934deca9ce76533"></a>

### [`0078820c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/0078820c.md) → [`0078824c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00788/0078824c.md) FUN_0078824c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b6e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e60.md) [`00a466e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a466e0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b6ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6ea4.md) [`00a468d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a468d8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.30% / 新版 96.30%

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
      "site": "007882d4",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00788294",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007882e0",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007882a0",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "007882d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "007882e0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "007882d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007882e0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00788260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/0078820c.md#insn-00788260) · [`00788294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/0078820c.md#insn-00788294) · [`007882a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/0078820c.md#insn-007882a0)
- 新版 `007882a0`（命令位置の公開資料なし） · `007882d4`（命令位置の公開資料なし） · `007882e0`（命令位置の公開資料なし）

~~~diff
- 00788260 ["INT_ADD", "register:40f0:8", ["const:788260:8", "const:4:8"]]
- 00788260 ["CALL", null, ["callee:00a46bb8:8"]]
+ 007882a0 ["INT_ADD", "register:40f0:8", ["const:7882a0:8", "const:4:8"]]
+ 007882a0 ["CALL", null, ["callee:00a46bb8:8"]]
- 00788260 bytes d8f90a94
+ 007882a0 bytes 46fa0a94
- 00788294 ["INT_ADD", "register:40f0:8", ["const:788294:8", "const:4:8"]]
- 00788294 ["CALL", null, ["ram:47acb4:8"]]
+ 007882d4 ["INT_ADD", "register:40f0:8", ["const:7882d4:8", "const:4:8"]]
+ 007882d4 ["CALL", null, ["ram:47acf4:8"]]
- 00788294 bytes 88caf397
+ 007882d4 bytes 88caf397
- 007882a0 ["INT_ADD", "register:40f0:8", ["const:7882a0:8", "const:4:8"]]
- 007882a0 ["CALL", null, ["ram:47acb4:8"]]
+ 007882e0 ["INT_ADD", "register:40f0:8", ["const:7882e0:8", "const:4:8"]]
+ 007882e0 ["CALL", null, ["ram:47acf4:8"]]
- 007882a0 bytes 85caf397
+ 007882e0 bytes 85caf397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1aec90cf64da849ad339d0084d33de2b"></a>

### [`00788310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/00788310.md) → [`00788350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00788/00788350.md) FUN_00788350

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00788374",
      "incomplete_value": false,
      "site": "00788378",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:530:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00788334",
      "incomplete_value": false,
      "site": "00788338",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:130:8"
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
      "00788378",
      "DATA",
      [
        "storage",
        "00c79130",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00788378",
      "DATA",
      [
        "storage",
        "00c79530",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00788324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/00788310.md#insn-00788324) · [`00788334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/00788310.md#insn-00788334)
- 新版 `00788364`（命令位置の公開資料なし） · `00788374`（命令位置の公開資料なし）

~~~diff
- 00788324 ["INT_ADD", "register:40f0:8", ["const:788324:8", "const:4:8"]]
- 00788324 ["CALL", null, ["callee:00c57e90:8"]]
+ 00788364 ["INT_ADD", "register:40f0:8", ["const:788364:8", "const:4:8"]]
+ 00788364 ["CALL", null, ["callee:00c57e90:8"]]
- 00788324 bytes db3d1394
+ 00788364 bytes cb3e1394
- 00788334 ["COPY", "tmp:0:8", ["const:130:8"]]
- 00788334 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00788334 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00788334 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00788374 ["COPY", "tmp:0:8", ["const:530:8"]]
+ 00788374 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00788374 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00788374 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00788334 bytes 08c10491
+ 00788374 bytes 08c11491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21659ef403818a4070033ce7fba82590"></a>

### [`00788350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/00788350.md) → [`00788390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00788/00788390.md) FUN_00788390

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
      "definition_site": "00788394",
      "incomplete_value": false,
      "site": "00788398",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:530:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00788354",
      "incomplete_value": false,
      "site": "00788358",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:130:8"
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
      "00788398",
      "DATA",
      [
        "storage",
        "00c79130",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00788398",
      "DATA",
      [
        "storage",
        "00c79530",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00788354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/00788350.md#insn-00788354)
- 新版 `00788394`（命令位置の公開資料なし）

~~~diff
- 00788354 ["COPY", "tmp:0:8", ["const:130:8"]]
- 00788354 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00788354 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00788354 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00788394 ["COPY", "tmp:0:8", ["const:530:8"]]
+ 00788394 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00788394 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00788394 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00788354 bytes 08c10491
+ 00788394 bytes 08c11491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fce88b57f6cd7fabe0350b6ec0db293f"></a>

### [`00788378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/00788378.md) → [`007883b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00788/007883b8.md) FUN_007883b8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`007877bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/007877bc.md) [`008b6e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e60.md) [`00a466e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a466e0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`007877fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00787/007877fc.md) [`008b6ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6ea4.md) [`00a468d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a468d8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.55% / 新版 96.55%

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
      "site": "00788448",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00788408",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00788454",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00788414",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "00788448",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00788454",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00788448",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00788454",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00788408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/00788378.md#insn-00788408) · [`00788414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/00788378.md#insn-00788414) · [`00788398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/00788378.md#insn-00788398)
- 新版 `00788448`（命令位置の公開資料なし） · `00788454`（命令位置の公開資料なし） · `007883d8`（命令位置の公開資料なし）

~~~diff
- 00788408 ["INT_ADD", "register:40f0:8", ["const:788408:8", "const:4:8"]]
- 00788408 ["CALL", null, ["ram:47acb4:8"]]
+ 00788448 ["INT_ADD", "register:40f0:8", ["const:788448:8", "const:4:8"]]
+ 00788448 ["CALL", null, ["ram:47acf4:8"]]
- 00788408 bytes 2bcaf397
+ 00788448 bytes 2bcaf397
- 00788414 ["INT_ADD", "register:40f0:8", ["const:788414:8", "const:4:8"]]
- 00788414 ["CALL", null, ["ram:47acb4:8"]]
+ 00788454 ["INT_ADD", "register:40f0:8", ["const:788454:8", "const:4:8"]]
+ 00788454 ["CALL", null, ["ram:47acf4:8"]]
- 00788414 bytes 28caf397
+ 00788454 bytes 28caf397
- 00788398 ["INT_ADD", "register:40f0:8", ["const:788398:8", "const:4:8"]]
- 00788398 ["CALL", null, ["callee:008b6ea4:8"]]
+ 007883d8 ["INT_ADD", "register:40f0:8", ["const:7883d8:8", "const:4:8"]]
+ 007883d8 ["CALL", null, ["callee:008b6ea4:8"]]
- 00788398 bytes b2ba0494
+ 007883d8 bytes b3ba0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d99f3cf66c0fc01e9a51591f5c77168e"></a>

### [`0078848c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/0078848c.md) → [`007884cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00788/007884cc.md) FUN_007884cc

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "007884f0",
      "incomplete_value": false,
      "site": "007884f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:5b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007884b0",
      "incomplete_value": false,
      "site": "007884b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:1b0:8"
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
      "007884f4",
      "DATA",
      [
        "storage",
        "00c791b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007884f4",
      "DATA",
      [
        "storage",
        "00c795b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007884a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/0078848c.md#insn-007884a0) · [`007884b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/0078848c.md#insn-007884b0)
- 新版 `007884e0`（命令位置の公開資料なし） · `007884f0`（命令位置の公開資料なし）

~~~diff
- 007884a0 ["INT_ADD", "register:40f0:8", ["const:7884a0:8", "const:4:8"]]
- 007884a0 ["CALL", null, ["callee:00c57e90:8"]]
+ 007884e0 ["INT_ADD", "register:40f0:8", ["const:7884e0:8", "const:4:8"]]
+ 007884e0 ["CALL", null, ["callee:00c57e90:8"]]
- 007884a0 bytes 7c3d1394
+ 007884e0 bytes 6c3e1394
- 007884b0 ["COPY", "tmp:0:8", ["const:1b0:8"]]
- 007884b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007884b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007884b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007884f0 ["COPY", "tmp:0:8", ["const:5b0:8"]]
+ 007884f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007884f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007884f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007884b0 bytes 08c10691
+ 007884f0 bytes 08c11691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d08c71ac7ac27d21e8f5182cd5f59e4"></a>

### [`007884cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/007884cc.md) → [`0078850c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00788/0078850c.md) FUN_0078850c

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
      "definition_site": "00788510",
      "incomplete_value": false,
      "site": "00788514",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:5b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007884d0",
      "incomplete_value": false,
      "site": "007884d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:1b0:8"
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
      "00788514",
      "DATA",
      [
        "storage",
        "00c791b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00788514",
      "DATA",
      [
        "storage",
        "00c795b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007884d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/007884cc.md#insn-007884d0)
- 新版 `00788510`（命令位置の公開資料なし）

~~~diff
- 007884d0 ["COPY", "tmp:0:8", ["const:1b0:8"]]
- 007884d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007884d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007884d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00788510 ["COPY", "tmp:0:8", ["const:5b0:8"]]
+ 00788510 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00788510 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00788510 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007884d0 bytes 08c10691
+ 00788510 bytes 08c11691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2410d834d7eaf9607d24635a03add01d"></a>

### [`007884f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/007884f4.md) → [`00788534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00788/00788534.md) FUN_00788534

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`007879a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00787/007879a8.md) [`008b6e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e60.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`007879e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00787/007879e8.md) [`008b6ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6ea4.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.67% / 新版 98.67%

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
      "site": "007886ac",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0078866c",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "ordinal": 14,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007886c8",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00788688",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "007886ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "007886c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "007886ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007886c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00788648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/007884f4.md#insn-00788648) · [`0078866c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/007884f4.md#insn-0078866c) · [`00788688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/007884f4.md#insn-00788688)
- 新版 `00788688`（命令位置の公開資料なし） · `007886ac`（命令位置の公開資料なし） · `007886c8`（命令位置の公開資料なし）

~~~diff
- 00788648 ["INT_ADD", "register:40f0:8", ["const:788648:8", "const:4:8"]]
- 00788648 ["CALL", null, ["callee:00a468d8:8"]]
+ 00788688 ["INT_ADD", "register:40f0:8", ["const:788688:8", "const:4:8"]]
+ 00788688 ["CALL", null, ["callee:00a468d8:8"]]
- 00788648 bytes 26f80a94
+ 00788688 bytes 94f80a94
- 0078866c ["INT_ADD", "register:40f0:8", ["const:78866c:8", "const:4:8"]]
- 0078866c ["CALL", null, ["ram:47acb4:8"]]
+ 007886ac ["INT_ADD", "register:40f0:8", ["const:7886ac:8", "const:4:8"]]
+ 007886ac ["CALL", null, ["ram:47acf4:8"]]
- 0078866c bytes 92c9f397
+ 007886ac bytes 92c9f397
- 00788688 ["INT_ADD", "register:40f0:8", ["const:788688:8", "const:4:8"]]
- 00788688 ["CALL", null, ["ram:47acb4:8"]]
+ 007886c8 ["INT_ADD", "register:40f0:8", ["const:7886c8:8", "const:4:8"]]
+ 007886c8 ["CALL", null, ["ram:47acf4:8"]]
- 00788688 bytes 8bc9f397
+ 007886c8 bytes 8bc9f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7427a2458d0731fd4455c38ac62c49ee"></a>

### [`007888dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/007888dc.md) → [`0078891c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00788/0078891c.md) _INIT_135

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.01% / 新版 87.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0078899c",
      "incomplete_value": true,
      "site": "007889b8",
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
    "old": {
      "definition_site": "0078895c",
      "incomplete_value": true,
      "site": "00788978",
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
                "const:d82:8"
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
      "definition_site": "007889bc",
      "incomplete_value": true,
      "site": "007889d4",
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
                "const:f62:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078897c",
      "incomplete_value": true,
      "site": "00788994",
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
                "const:e95:8"
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
      "definition_site": "007889d8",
      "incomplete_value": true,
      "site": "007889f4",
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
                "const:2ac000:8"
              ],
              [
                "leaf",
                "const:5d2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00788998",
      "incomplete_value": true,
      "site": "007889b4",
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
                "const:2ac000:8"
              ],
              [
                "leaf",
                "const:592:8"
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
      "00788958",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "0078897c",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "0078899c",
      "READ",
      [
        "storage",
        "002b8d82",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00788958",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "0078897c",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "0078899c",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00788954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/007888dc.md#insn-00788954) · [`00788974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/007888dc.md#insn-00788974) · [`00788b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/007888dc.md#insn-00788b10)
- 新版 `00788994`（命令位置の公開資料なし） · `007889b4`（命令位置の公開資料なし） · `00788b50`（命令位置の公開資料なし）

~~~diff
- 00788954 ["COPY", "tmp:0:8", ["const:d82:8"]]
- 00788954 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00788954 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00788954 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00788994 ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 00788994 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00788994 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00788994 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00788954 bytes 4a093691
+ 00788994 bytes 4a093791
- 00788974 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 00788974 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00788974 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00788974 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 007889b4 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 007889b4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 007889b4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 007889b4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00788974 bytes 4a553a91
+ 007889b4 bytes 4a893d91
- 00788b10 ["INT_ADD", "register:40f0:8", ["const:788b10:8", "const:4:8"]]
- 00788b10 ["CALL", null, ["callee:00c57e30:8"]]
+ 00788b50 ["INT_ADD", "register:40f0:8", ["const:788b50:8", "const:4:8"]]
+ 00788b50 ["CALL", null, ["callee:00c57e30:8"]]
- 00788b10 bytes c83b1394
+ 00788b50 bytes b83c1394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8cb350518787293dabe4a4165a666afc"></a>

### [`00788c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/00788c6c.md) → [`00788cac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00788/00788cac.md) FUN_00788cac

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 44件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`005d8b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8b88.md) [`00606448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606448.md)
- 新版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 44件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md) [`00606488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/00606488.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 97.05% / 新版 97.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 2件, `call_target` 3件, `store_destination` 3件, `store_value` 6件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00788cf8",
      "incomplete_value": false,
      "site": "00788cf8",
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
            "const:968:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00788cb8",
      "incomplete_value": false,
      "site": "00788cb8",
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
            "const:568:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00788cf0",
      "incomplete_value": true,
      "site": "00788cf8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00788cb0",
      "incomplete_value": true,
      "site": "00788cb8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:578:8"
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
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00788cfc",
      "incomplete_value": false,
      "site": "00788cfc",
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
            "const:978:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00788cbc",
      "incomplete_value": false,
      "site": "00788cbc",
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
            "const:578:8"
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
      "00788cf0",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "00788cf4",
      "READ",
      [
        "storage",
        "00ca4568",
        null,
        "undefined8"
      ]
    ],
    [
      "00788cf8",
      "WRITE",
      [
        "storage",
        "00ca4568",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00788cf0",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "00788cf4",
      "READ",
      [
        "storage",
        "00ca4968",
        null,
        "undefined8"
      ]
    ],
    [
      "00788cf8",
      "WRITE",
      [
        "storage",
        "00ca4968",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00788cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/00788c6c.md#insn-00788cb8) · [`00788cbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/00788c6c.md#insn-00788cbc) · [`00788cd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/00788c6c.md#insn-00788cd4)
- 新版 `00788cf8`（命令位置の公開資料なし） · `00788cfc`（命令位置の公開資料なし） · `00788d14`（命令位置の公開資料なし）

~~~diff
- 00788cb8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:568:8"]]
- 00788cb8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00788cf8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:968:8"]]
+ 00788cf8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00788cb8 bytes 09b502f9
+ 00788cf8 bytes 09b504f9
- 00788cbc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:578:8"]]
- 00788cbc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 00788cfc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:978:8"]]
+ 00788cfc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00788cbc bytes aabe02f9
+ 00788cfc bytes aabe04f9
- 00788cd4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:578:8"]]
- 00788cd4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
+ 00788d14 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:978:8"]]
+ 00788d14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00788cd4 bytes b4be02f9
+ 00788d14 bytes b4be04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9af4a889a3f12548f6ec777b0e8a1801"></a>

### [`00789c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00789/00789c10.md) → [`00789c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00789/00789c50.md) FUN_00789c50

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 13件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0049f3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3b0.md) [`006766ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/006766ec.md) [`008b6ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6ecc.md)
- 新版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 13件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0049f3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f3f0.md) [`0067672c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/0067672c.md) [`008b6f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f10.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.00% / 新版 99.00%

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
      "site": "00789da0",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00789d60",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "00789c94",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "qword"
      ]
    ],
    [
      "00789cec",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "qword"
      ]
    ],
    [
      "00789da0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00789c94",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "dword"
      ]
    ],
    [
      "00789cec",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "dword"
      ]
    ],
    [
      "00789da0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00789d60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00789/00789c10.md#insn-00789d60) · [`00789c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00789/00789c10.md#insn-00789c50) · [`00789c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00789/00789c10.md#insn-00789c70)
- 新版 `00789da0`（命令位置の公開資料なし） · `00789c90`（命令位置の公開資料なし） · `00789cb0`（命令位置の公開資料なし）

~~~diff
- 00789d60 ["INT_ADD", "register:40f0:8", ["const:789d60:8", "const:4:8"]]
- 00789d60 ["CALL", null, ["ram:47acb4:8"]]
+ 00789da0 ["INT_ADD", "register:40f0:8", ["const:789da0:8", "const:4:8"]]
+ 00789da0 ["CALL", null, ["ram:47acf4:8"]]
- 00789d60 bytes d5c3f397
+ 00789da0 bytes d5c3f397
- 00789c50 ["INT_ADD", "register:40f0:8", ["const:789c50:8", "const:4:8"]]
- 00789c50 ["CALL", null, ["callee:00ac8ddc:8"]]
+ 00789c90 ["INT_ADD", "register:40f0:8", ["const:789c90:8", "const:4:8"]]
+ 00789c90 ["CALL", null, ["callee:00ac8ddc:8"]]
- 00789c50 bytes e4fb0c94
+ 00789c90 bytes 53fc0c94
- 00789c70 ["INT_ADD", "register:40f0:8", ["const:789c70:8", "const:4:8"]]
- 00789c70 ["CALL", null, ["callee:008b78d8:8"]]
+ 00789cb0 ["INT_ADD", "register:40f0:8", ["const:789cb0:8", "const:4:8"]]
+ 00789cb0 ["CALL", null, ["callee:008b78d8:8"]]
- 00789c70 bytes 09b70494
+ 00789cb0 bytes 0ab70494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5dc4910836d5f903e28cf1b555ea0ef6"></a>

### [`00789da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00789/00789da0.md) → [`00789de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00789/00789de0.md) FUN_00789de0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00859b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00859/00859b18.md) · 呼出先 64件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467abc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467abc.md) [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md)
- 新版 呼出元 1件 [`00859b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859b58.md) · 呼出先 64件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467afc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467afc.md) [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 98.67% / 新版 98.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 10件, `store_value` 2件

アドレスに依存する影響 `branch_value` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0078a5f0",
      "incomplete_value": true,
      "site": "0078a5fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:328:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078a5b0",
      "incomplete_value": true,
      "site": "0078a5bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 63,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0078a5f8",
      "incomplete_value": true,
      "site": "0078a604",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ce8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078a5b8",
      "incomplete_value": true,
      "site": "0078a5c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ca8:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "0078a600",
      "incomplete_value": true,
      "site": "0078a604",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078a5c0",
      "incomplete_value": true,
      "site": "0078a5c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:380:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 65,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00789e24",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "00789e38",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00789e40",
      "PARAM",
      [
        "storage",
        "00c79220",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00789e24",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "00789e38",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00789e40",
      "PARAM",
      [
        "storage",
        "00c79620",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00789e0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00789/00789da0.md#insn-00789e0c) · [`00789e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00789/00789da0.md#insn-00789e20) · [`0078a0dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00789/00789da0.md#insn-0078a0dc)
- 新版 `00789e4c`（命令位置の公開資料なし） · `00789e60`（命令位置の公開資料なし） · `0078a11c`（命令位置の公開資料なし）

~~~diff
- 00789e0c ["INT_ADD", "register:40f0:8", ["const:789e0c:8", "const:4:8"]]
- 00789e0c ["CALL", null, ["callee:00c58610:8"]]
+ 00789e4c ["INT_ADD", "register:40f0:8", ["const:789e4c:8", "const:4:8"]]
+ 00789e4c ["CALL", null, ["callee:00c58610:8"]]
- 00789e0c bytes 01391394
+ 00789e4c bytes f1391394
- 00789e20 ["INT_ADD", "register:40f0:8", ["const:789e20:8", "const:4:8"]]
- 00789e20 ["CALL", null, ["ram:46c984:8"]]
+ 00789e60 ["INT_ADD", "register:40f0:8", ["const:789e60:8", "const:4:8"]]
+ 00789e60 ["CALL", null, ["ram:46c9c4:8"]]
- 00789e20 bytes d98af397
+ 00789e60 bytes d98af397
- 0078a0dc ["INT_ADD", "register:40f0:8", ["const:78a0dc:8", "const:4:8"]]
- 0078a0dc ["CALL", null, ["ram:46c984:8"]]
+ 0078a11c ["INT_ADD", "register:40f0:8", ["const:78a11c:8", "const:4:8"]]
+ 0078a11c ["CALL", null, ["ram:46c9c4:8"]]
- 0078a0dc bytes 2a8af397
+ 0078a11c bytes 2a8af397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc59ff07e1854cc27ed8035c23c826f7"></a>

### [`0078bd18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078b/0078bd18.md) → [`0078bd58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078b/0078bd58.md) FUN_0078bd58

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0078def8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078d/0078def8.md) · 呼出先 12件 [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00493650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493650.md) [`0049f3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3b0.md) [`0078e8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e8d4.md)
- 新版 呼出元 1件 [`0078df38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078d/0078df38.md) · 呼出先 12件 [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00493690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493690.md) [`0049f3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f3f0.md) [`0078e914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078e/0078e914.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.17% / 新版 94.17%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0078be14",
      "incomplete_value": false,
      "site": "0078be14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:9e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078bdd4",
      "incomplete_value": false,
      "site": "0078bdd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:5e8:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0078be60",
      "incomplete_value": false,
      "site": "0078be60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:ae8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078be20",
      "incomplete_value": false,
      "site": "0078be20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:6e8:8"
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
      "definition_site": null,
      "incomplete_value": true,
      "site": "0078bda4",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0078bd64",
      "value": [
        "leaf",
        "ram:48ccb8:8"
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
      "0078bd80",
      "DATA",
      [
        "storage",
        "0039b1d8",
        "fde_0039b1d8",
        "dword"
      ]
    ],
    [
      "0078bd90",
      "DATA",
      [
        "storage",
        "0039b1d8",
        "fde_0039b1d8",
        "dword"
      ]
    ],
    [
      "0078bda4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ]
  ],
  "added": [
    [
      "0078bd80",
      "DATA",
      [
        "storage",
        "0039b1d8",
        null,
        "dword"
      ]
    ],
    [
      "0078bd90",
      "DATA",
      [
        "storage",
        "0039b1d8",
        null,
        "dword"
      ]
    ],
    [
      "0078bda4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078bd64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078b/0078bd18.md#insn-0078bd64) · [`0078bda4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078b/0078bd18.md#insn-0078bda4) · [`0078bd70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078b/0078bd18.md#insn-0078bd70)
- 新版 `0078bda4`（命令位置の公開資料なし） · `0078bde4`（命令位置の公開資料なし） · `0078bdb0`（命令位置の公開資料なし）

~~~diff
- 0078bd64 ["INT_ADD", "register:40f0:8", ["const:78bd64:8", "const:4:8"]]
- 0078bd64 ["CALL", null, ["ram:48ccb8:8"]]
+ 0078bda4 ["INT_ADD", "register:40f0:8", ["const:78bda4:8", "const:4:8"]]
+ 0078bda4 ["CALL", null, ["ram:48ccf8:8"]]
- 0078bd64 bytes d503f497
+ 0078bda4 bytes d503f497
- 0078bda4 ["INT_ADD", "register:40f0:8", ["const:78bda4:8", "const:4:8"]]
- 0078bda4 ["CALL", null, ["callee:00493690:8"]]
+ 0078bde4 ["INT_ADD", "register:40f0:8", ["const:78bde4:8", "const:4:8"]]
+ 0078bde4 ["CALL", null, ["callee:00493690:8"]]
- 0078bda4 bytes 2b1ef497
+ 0078bde4 bytes 2b1ef497
- 0078bd70 ["COPY", "tmp:0:8", ["const:2ba:8"]]
- 0078bd70 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0078bd70 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0078bd70 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0078bdb0 ["COPY", "tmp:0:8", ["const:2fa:8"]]
+ 0078bdb0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0078bdb0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0078bdb0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0078bd70 bytes 29e90a91
+ 0078bdb0 bytes 29e90b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a59a89659cf787234949d11f2939373b"></a>

### [`0078bf84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078b/0078bf84.md) → [`0078bfc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078b/0078bfc4.md) FUN_0078bfc4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0078def8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078d/0078def8.md) · 呼出先 11件 [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00493650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493650.md) [`0049f3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3b0.md) [`007459e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00745/007459e4.md)
- 新版 呼出元 1件 [`0078df38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078d/0078df38.md) · 呼出先 11件 [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00493690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493690.md) [`0049f3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f3f0.md) [`00745a24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00745/00745a24.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.22% / 新版 93.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0078c038",
      "incomplete_value": true,
      "site": "0078c038",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2fa:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078bff8",
      "incomplete_value": true,
      "site": "0078bff8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2ba:8"
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
      "definition_site": "0078c080",
      "incomplete_value": false,
      "site": "0078c080",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078c040",
      "incomplete_value": false,
      "site": "0078c040",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:668:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0078c0b8",
      "incomplete_value": false,
      "site": "0078c0b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:ae8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078c078",
      "incomplete_value": false,
      "site": "0078c078",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:6e8:8"
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
      "0078bfec",
      "DATA",
      [
        "storage",
        "0039b1d8",
        "fde_0039b1d8",
        "dword"
      ]
    ],
    [
      "0078c008",
      "DATA",
      [
        "storage",
        "0039b1d8",
        "fde_0039b1d8",
        "dword"
      ]
    ],
    [
      "0078c010",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ]
  ],
  "added": [
    [
      "0078bfec",
      "DATA",
      [
        "storage",
        "0039b1d8",
        null,
        "dword"
      ]
    ],
    [
      "0078c008",
      "DATA",
      [
        "storage",
        "0039b1d8",
        null,
        "dword"
      ]
    ],
    [
      "0078c010",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078bfd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078b/0078bf84.md#insn-0078bfd0) · [`0078c010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078b/0078bf84.md#insn-0078c010) · [`0078c038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078b/0078bf84.md#insn-0078c038)
- 新版 `0078c010`（命令位置の公開資料なし） · `0078c050`（命令位置の公開資料なし） · `0078c078`（命令位置の公開資料なし）

~~~diff
- 0078bfd0 ["INT_ADD", "register:40f0:8", ["const:78bfd0:8", "const:4:8"]]
- 0078bfd0 ["CALL", null, ["ram:48ccb8:8"]]
+ 0078c010 ["INT_ADD", "register:40f0:8", ["const:78c010:8", "const:4:8"]]
+ 0078c010 ["CALL", null, ["ram:48ccf8:8"]]
- 0078bfd0 bytes 3a03f497
+ 0078c010 bytes 3a03f497
- 0078c010 ["INT_ADD", "register:40f0:8", ["const:78c010:8", "const:4:8"]]
- 0078c010 ["CALL", null, ["callee:00493690:8"]]
+ 0078c050 ["INT_ADD", "register:40f0:8", ["const:78c050:8", "const:4:8"]]
+ 0078c050 ["CALL", null, ["callee:00493690:8"]]
- 0078c010 bytes 901df497
+ 0078c050 bytes 901df497
- 0078c038 ["COPY", "tmp:0:8", ["const:668:8"]]
- 0078c038 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0078c038 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0078c038 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0078c078 ["COPY", "tmp:0:8", ["const:a68:8"]]
+ 0078c078 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0078c078 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0078c078 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0078c038 bytes 08a11991
+ 0078c078 bytes 08a12991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-301e222f1a1c1f441c16f22073bbe1ce"></a>

### [`0078c1dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078c/0078c1dc.md) → [`0078c21c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078c/0078c21c.md) FUN_0078c21c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00788c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/00788c6c.md) · 呼出先 25件 [`0046e784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e784.md) [`0046e930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e930.md) [`0046eeb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046eeb8.md) [`0046f074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f074.md) [`0046f62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f62c.md)
- 新版 呼出元 1件 [`00788cac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00788/00788cac.md) · 呼出先 25件 [`0046e7c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e7c4.md) [`0046e970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e970.md) [`0046eef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046eef8.md) [`0046f0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f0b4.md) [`0046f66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f66c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 41件, `store_destination` 14件, `store_value` 49件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0078c25c",
      "incomplete_value": false,
      "site": "0078c260",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:648:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078c21c",
      "incomplete_value": false,
      "site": "0078c220",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:248:8"
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
      "definition_site": "0078c2cc",
      "incomplete_value": true,
      "site": "0078c2cc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b6000:8"
              ],
              [
                "leaf",
                "const:38e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078c28c",
      "incomplete_value": true,
      "site": "0078c28c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b6000:8"
              ],
              [
                "leaf",
                "const:34e:8"
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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0078c2e4",
      "incomplete_value": true,
      "site": "0078c2e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f16:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078c2a4",
      "incomplete_value": true,
      "site": "0078c2a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ed6:8"
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
      "0078c260",
      "DATA",
      [
        "storage",
        "00c79248",
        null,
        "pointer"
      ]
    ],
    [
      "0078c29c",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ],
    [
      "0078c2bc",
      "READ",
      [
        "storage",
        "002b634e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0078c260",
      "DATA",
      [
        "storage",
        "00c79648",
        null,
        "pointer"
      ]
    ],
    [
      "0078c29c",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      "0078c2bc",
      "READ",
      [
        "storage",
        "002b638e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078c2e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078c/0078c1dc.md#insn-0078c2e8) · [`0078c980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078c/0078c1dc.md#insn-0078c980) · [`0078c9b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078c/0078c1dc.md#insn-0078c9b0)
- 新版 `0078c328`（命令位置の公開資料なし） · `0078c9c0`（命令位置の公開資料なし） · `0078c9f0`（命令位置の公開資料なし）

~~~diff
- 0078c2e8 ["INT_ADD", "register:40f0:8", ["const:78c2e8:8", "const:4:8"]]
- 0078c2e8 ["CALL", null, ["callee:00c53d00:8"]]
+ 0078c328 ["INT_ADD", "register:40f0:8", ["const:78c328:8", "const:4:8"]]
+ 0078c328 ["CALL", null, ["callee:00c53d00:8"]]
- 0078c2e8 bytes 7e1d1394
+ 0078c328 bytes 761e1394
- 0078c980 ["INT_ADD", "register:40f0:8", ["const:78c980:8", "const:4:8"]]
- 0078c980 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0078c9c0 ["INT_ADD", "register:40f0:8", ["const:78c9c0:8", "const:4:8"]]
+ 0078c9c0 ["CALL", null, ["callee:00c57eb0:8"]]
- 0078c980 bytes 4c2c1394
+ 0078c9c0 bytes 3c2d1394
- 0078c9b0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:640:8"]]
- 0078c9b0 ["LOAD", "register:5040:16", ["const:1b1:8", "tmp:0:8"]]
- 0078c9b0 ["COPY", "register:5050:8", ["const:0:8"]]
- 0078c9b0 ["COPY", "register:5058:8", ["const:0:8"]]
+ 0078c9f0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:680:8"]]
+ 0078c9f0 ["LOAD", "register:5040:16", ["const:1b1:8", "tmp:0:8"]]
+ 0078c9f0 ["COPY", "register:5050:8", ["const:0:8"]]
+ 0078c9f0 ["COPY", "register:5058:8", ["const:0:8"]]
- 0078c9b0 bytes 2291c13d
+ 0078c9f0 bytes 22a1c13d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8922945bbd7b366983a73a694fb6c582"></a>

### [`0078dd8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078d/0078dd8c.md) → [`0078ddcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078d/0078ddcc.md) FUN_0078ddcc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0046e864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e864.md) [`0046ef9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ef9c.md) [`006822e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/006822e4.md) [`0078db1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078d/0078db1c.md) [`0078dc6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078d/0078dc6c.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0046e8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e8a4.md) [`0046efdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046efdc.md) [`00682324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00682/00682324.md) [`0078db5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078d/0078db5c.md) [`0078dcac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078d/0078dcac.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0078dddc",
      "incomplete_value": false,
      "site": "0078dde4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:648:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078dd9c",
      "incomplete_value": false,
      "site": "0078dda4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:248:8"
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
      "definition_site": "0078de10",
      "incomplete_value": false,
      "site": "0078de14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:810:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078ddd0",
      "incomplete_value": false,
      "site": "0078ddd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:410:8"
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
      "0078dde4",
      "DATA",
      [
        "storage",
        "00c79248",
        null,
        "pointer"
      ]
    ],
    [
      "0078de14",
      "DATA",
      [
        "storage",
        "00c74410",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0078dde4",
      "DATA",
      [
        "storage",
        "00c79648",
        null,
        "pointer"
      ]
    ],
    [
      "0078de14",
      "DATA",
      [
        "storage",
        "00c74810",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078dde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078d/0078dd8c.md#insn-0078dde4) · [`0078dd9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078d/0078dd8c.md#insn-0078dd9c) · [`0078ddac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078d/0078dd8c.md#insn-0078ddac)
- 新版 `0078de24`（命令位置の公開資料なし） · `0078dddc`（命令位置の公開資料なし） · `0078ddec`（命令位置の公開資料なし）

~~~diff
- 0078dde4 ["INT_ADD", "register:40f0:8", ["const:78dde4:8", "const:4:8"]]
- 0078dde4 ["CALL", null, ["callee:00c53d00:8"]]
+ 0078de24 ["INT_ADD", "register:40f0:8", ["const:78de24:8", "const:4:8"]]
+ 0078de24 ["CALL", null, ["callee:00c53d00:8"]]
- 0078dde4 bytes bf161394
+ 0078de24 bytes b7171394
- 0078dd9c ["COPY", "tmp:0:8", ["const:248:8"]]
- 0078dd9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0078dd9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0078dd9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0078dddc ["COPY", "tmp:0:8", ["const:648:8"]]
+ 0078dddc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0078dddc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0078dddc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0078dd9c bytes 08210991
+ 0078dddc bytes 08211991
- 0078ddac ["INT_ADD", "register:40f0:8", ["const:78ddac:8", "const:4:8"]]
- 0078ddac ["CALL", null, ["callee:0046e8a4:8"]]
+ 0078ddec ["INT_ADD", "register:40f0:8", ["const:78ddec:8", "const:4:8"]]
+ 0078ddec ["CALL", null, ["callee:0046e8a4:8"]]
- 0078ddac bytes ae82f397
+ 0078ddec bytes ae82f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebf94a3c368b47f0e6ecd60abab924e4"></a>

### [`0078de14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078d/0078de14.md) → [`0078de54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078d/0078de54.md) FUN_0078de54

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`0046e864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e864.md) [`0046ef9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ef9c.md) [`006822e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/006822e4.md) [`0078db1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078d/0078db1c.md) [`0078dc6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078d/0078dc6c.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0046e8a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e8a4.md) [`0046efdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046efdc.md) [`00682324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00682/00682324.md) [`0078db5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078d/0078db5c.md) [`0078dcac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078d/0078dcac.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0078de64",
      "incomplete_value": false,
      "site": "0078de6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:648:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078de24",
      "incomplete_value": false,
      "site": "0078de2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:248:8"
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
      "definition_site": "0078de98",
      "incomplete_value": false,
      "site": "0078de9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:810:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078de58",
      "incomplete_value": false,
      "site": "0078de5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c74000:8"
          ],
          [
            "leaf",
            "const:410:8"
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
      "0078de6c",
      "DATA",
      [
        "storage",
        "00c79248",
        null,
        "pointer"
      ]
    ],
    [
      "0078de9c",
      "DATA",
      [
        "storage",
        "00c74410",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0078de6c",
      "DATA",
      [
        "storage",
        "00c79648",
        null,
        "pointer"
      ]
    ],
    [
      "0078de9c",
      "DATA",
      [
        "storage",
        "00c74810",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078de6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078d/0078de14.md#insn-0078de6c) · [`0078de24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078d/0078de14.md#insn-0078de24) · [`0078de34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078d/0078de14.md#insn-0078de34)
- 新版 `0078deac`（命令位置の公開資料なし） · `0078de64`（命令位置の公開資料なし） · `0078de74`（命令位置の公開資料なし）

~~~diff
- 0078de6c ["INT_ADD", "register:40f0:8", ["const:78de6c:8", "const:4:8"]]
- 0078de6c ["CALL", null, ["callee:00c53d00:8"]]
+ 0078deac ["INT_ADD", "register:40f0:8", ["const:78deac:8", "const:4:8"]]
+ 0078deac ["CALL", null, ["callee:00c53d00:8"]]
- 0078de6c bytes 9d161394
+ 0078deac bytes 95171394
- 0078de24 ["COPY", "tmp:0:8", ["const:248:8"]]
- 0078de24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0078de24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0078de24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0078de64 ["COPY", "tmp:0:8", ["const:648:8"]]
+ 0078de64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0078de64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0078de64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0078de24 bytes 08210991
+ 0078de64 bytes 08211991
- 0078de34 ["INT_ADD", "register:40f0:8", ["const:78de34:8", "const:4:8"]]
- 0078de34 ["CALL", null, ["callee:0046e8a4:8"]]
+ 0078de74 ["INT_ADD", "register:40f0:8", ["const:78de74:8", "const:4:8"]]
+ 0078de74 ["CALL", null, ["callee:0046e8a4:8"]]
- 0078de34 bytes 8c82f397
+ 0078de74 bytes 8c82f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b4fdb05e24122c5850a4fd3824a3f2b"></a>

### [`0078dea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078d/0078dea8.md) → [`0078dee8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078d/0078dee8.md) FUN_0078dee8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "0078df0c",
      "incomplete_value": false,
      "site": "0078df0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:668:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078decc",
      "incomplete_value": false,
      "site": "0078decc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:268:8"
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
      "0078df0c",
      "DATA",
      [
        "storage",
        "00c79268",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0078df0c",
      "DATA",
      [
        "storage",
        "00c79668",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078debc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078d/0078dea8.md#insn-0078debc) · [`0078dec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078d/0078dea8.md#insn-0078dec8)
- 新版 `0078defc`（命令位置の公開資料なし） · `0078df08`（命令位置の公開資料なし）

~~~diff
- 0078debc ["INT_ADD", "register:40f0:8", ["const:78debc:8", "const:4:8"]]
- 0078debc ["CALL", null, ["callee:00c57e90:8"]]
+ 0078defc ["INT_ADD", "register:40f0:8", ["const:78defc:8", "const:4:8"]]
+ 0078defc ["CALL", null, ["callee:00c57e90:8"]]
- 0078debc bytes f5261394
+ 0078defc bytes e5271394
- 0078dec8 ["COPY", "tmp:0:8", ["const:268:8"]]
- 0078dec8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0078dec8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0078dec8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0078df08 ["COPY", "tmp:0:8", ["const:668:8"]]
+ 0078df08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0078df08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0078df08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0078dec8 bytes 08a10991
+ 0078df08 bytes 08a11991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-365e19a4949ff1e5e4f09ed569187530"></a>

### [`0078dedc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078d/0078dedc.md) → [`0078df1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078d/0078df1c.md) FUN_0078df1c

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
      "definition_site": "0078df28",
      "incomplete_value": false,
      "site": "0078df28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:668:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078dee8",
      "incomplete_value": false,
      "site": "0078dee8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:268:8"
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
      "0078df28",
      "DATA",
      [
        "storage",
        "00c79268",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0078df28",
      "DATA",
      [
        "storage",
        "00c79668",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078dee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078d/0078dedc.md#insn-0078dee4)
- 新版 `0078df24`（命令位置の公開資料なし）

~~~diff
- 0078dee4 ["COPY", "tmp:0:8", ["const:268:8"]]
- 0078dee4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0078dee4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0078dee4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0078df24 ["COPY", "tmp:0:8", ["const:668:8"]]
+ 0078df24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0078df24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0078df24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0078dee4 bytes 29a10991
+ 0078df24 bytes 29a11991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95ead0fcf5fc53444a166fba440d038b"></a>

### [`0078def8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078d/0078def8.md) → [`0078df38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078d/0078df38.md) FUN_0078df38

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 15件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0049f3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3b0.md) [`00606448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606448.md) [`007441c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00744/007441c8.md)
- 新版 呼出元 0件  · 呼出先 15件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0049f3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f3f0.md) [`00606488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/00606488.md) [`00744208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00744/00744208.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.12% / 新版 98.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0078e04c",
      "incomplete_value": false,
      "site": "0078e04c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:ae8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078e00c",
      "incomplete_value": false,
      "site": "0078e00c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:6e8:8"
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
      "definition_site": null,
      "incomplete_value": true,
      "site": "0078df70",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0078df30",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "0078df70",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "0078e04c",
      "DATA",
      [
        "storage",
        "00c796e8",
        null,
        "undefined *"
      ]
    ],
    [
      "0078e128",
      "READ",
      [
        "storage",
        "00c79708",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0078df70",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "0078e04c",
      "DATA",
      [
        "storage",
        "00c79ae8",
        null,
        "undefined *"
      ]
    ],
    [
      "0078e128",
      "READ",
      [
        "storage",
        "00c79b08",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078df30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078d/0078def8.md#insn-0078df30) · [`0078e04c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078d/0078def8.md#insn-0078e04c) · [`0078df78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078d/0078def8.md#insn-0078df78)
- 新版 `0078df70`（命令位置の公開資料なし） · `0078e08c`（命令位置の公開資料なし） · `0078dfb8`（命令位置の公開資料なし）

~~~diff
- 0078df30 ["INT_ADD", "register:40f0:8", ["const:78df30:8", "const:4:8"]]
- 0078df30 ["CALL", null, ["ram:47acb4:8"]]
+ 0078df70 ["INT_ADD", "register:40f0:8", ["const:78df70:8", "const:4:8"]]
+ 0078df70 ["CALL", null, ["ram:47acf4:8"]]
- 0078df30 bytes 61b3f397
+ 0078df70 bytes 61b3f397
- 0078e04c ["INT_ADD", "register:40f0:8", ["const:78e04c:8", "const:4:8"]]
- 0078e04c ["CALL", null, ["callee:00744208:8"]]
+ 0078e08c ["INT_ADD", "register:40f0:8", ["const:78e08c:8", "const:4:8"]]
+ 0078e08c ["CALL", null, ["callee:00744208:8"]]
- 0078e04c bytes 5fd8fe97
+ 0078e08c bytes 5fd8fe97
- 0078df78 ["INT_ADD", "register:40f0:8", ["const:78df78:8", "const:4:8"]]
- 0078df78 ["CALL", null, ["callee:00ac8ddc:8"]]
+ 0078dfb8 ["INT_ADD", "register:40f0:8", ["const:78dfb8:8", "const:4:8"]]
+ 0078dfb8 ["CALL", null, ["callee:00ac8ddc:8"]]
- 0078df78 bytes 1aeb0c94
+ 0078dfb8 bytes 89eb0c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e4992de34ed0a4e9a7cb6038572c842"></a>

### [`0078e1f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e1f0.md) → [`0078e230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078e/0078e230.md) FUN_0078e230

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "0078e254",
      "incomplete_value": false,
      "site": "0078e254",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:6e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078e214",
      "incomplete_value": false,
      "site": "0078e214",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:2e8:8"
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
      "0078e254",
      "DATA",
      [
        "storage",
        "00c792e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0078e254",
      "DATA",
      [
        "storage",
        "00c796e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078e204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e1f0.md#insn-0078e204) · [`0078e210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e1f0.md#insn-0078e210)
- 新版 `0078e244`（命令位置の公開資料なし） · `0078e250`（命令位置の公開資料なし）

~~~diff
- 0078e204 ["INT_ADD", "register:40f0:8", ["const:78e204:8", "const:4:8"]]
- 0078e204 ["CALL", null, ["callee:00c57e90:8"]]
+ 0078e244 ["INT_ADD", "register:40f0:8", ["const:78e244:8", "const:4:8"]]
+ 0078e244 ["CALL", null, ["callee:00c57e90:8"]]
- 0078e204 bytes 23261394
+ 0078e244 bytes 13271394
- 0078e210 ["COPY", "tmp:0:8", ["const:2e8:8"]]
- 0078e210 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0078e210 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0078e210 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0078e250 ["COPY", "tmp:0:8", ["const:6e8:8"]]
+ 0078e250 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0078e250 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0078e250 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0078e210 bytes 08a10b91
+ 0078e250 bytes 08a11b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcea9900cd6d8e9c5597eed8f631a3e0"></a>

### [`0078e240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e240.md) → [`0078e280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078e/0078e280.md) FUN_0078e280

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`007441c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00744/007441c8.md) [`007441fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00744/007441fc.md) [`0080018c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/0080018c.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`00744208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00744/00744208.md) [`0074423c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00744/0074423c.md) [`008001cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/008001cc.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.14% / 新版 97.14%

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
      "site": "0078e2b0",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0078e270",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "site": "0078e2bc",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0078e27c",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "site": "0078e3c8",
      "value": [
        "leaf",
        "ram:806af4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0078e388",
      "value": [
        "leaf",
        "ram:806ab4:8"
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
      "0078e2b0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "0078e2bc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "0078e3ac",
      "DATA",
      [
        "storage",
        "0038f284",
        null,
        "byte[15]"
      ]
    ]
  ],
  "added": [
    [
      "0078e2b0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "0078e2bc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "0078e3ac",
      "DATA",
      [
        "storage",
        "0038f284",
        "fde_0038f284",
        "dword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078e270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e240.md#insn-0078e270) · [`0078e27c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e240.md#insn-0078e27c) · [`0078e388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e240.md#insn-0078e388)
- 新版 `0078e2b0`（命令位置の公開資料なし） · `0078e2bc`（命令位置の公開資料なし） · `0078e3c8`（命令位置の公開資料なし）

~~~diff
- 0078e270 ["INT_ADD", "register:40f0:8", ["const:78e270:8", "const:4:8"]]
- 0078e270 ["CALL", null, ["ram:47acb4:8"]]
+ 0078e2b0 ["INT_ADD", "register:40f0:8", ["const:78e2b0:8", "const:4:8"]]
+ 0078e2b0 ["CALL", null, ["ram:47acf4:8"]]
- 0078e270 bytes 91b2f397
+ 0078e2b0 bytes 91b2f397
- 0078e27c ["INT_ADD", "register:40f0:8", ["const:78e27c:8", "const:4:8"]]
- 0078e27c ["CALL", null, ["ram:47acb4:8"]]
+ 0078e2bc ["INT_ADD", "register:40f0:8", ["const:78e2bc:8", "const:4:8"]]
+ 0078e2bc ["CALL", null, ["ram:47acf4:8"]]
- 0078e27c bytes 8eb2f397
+ 0078e2bc bytes 8eb2f397
- 0078e388 ["INT_ADD", "register:40f0:8", ["const:78e388:8", "const:4:8"]]
- 0078e388 ["CALL", null, ["ram:806ab4:8"]]
+ 0078e3c8 ["INT_ADD", "register:40f0:8", ["const:78e3c8:8", "const:4:8"]]
+ 0078e3c8 ["CALL", null, ["ram:806af4:8"]]
- 0078e388 bytes cbe10194
+ 0078e3c8 bytes cbe10194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f301d42b41c5134b3e19779889005f7"></a>

### [`0078e410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e410.md) → [`0078e450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078e/0078e450.md) FUN_0078e450

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "0078e474",
      "incomplete_value": false,
      "site": "0078e474",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:768:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078e434",
      "incomplete_value": false,
      "site": "0078e434",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:368:8"
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
      "0078e474",
      "DATA",
      [
        "storage",
        "00c79368",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0078e474",
      "DATA",
      [
        "storage",
        "00c79768",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078e424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e410.md#insn-0078e424) · [`0078e430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e410.md#insn-0078e430)
- 新版 `0078e464`（命令位置の公開資料なし） · `0078e470`（命令位置の公開資料なし）

~~~diff
- 0078e424 ["INT_ADD", "register:40f0:8", ["const:78e424:8", "const:4:8"]]
- 0078e424 ["CALL", null, ["callee:00c57e90:8"]]
+ 0078e464 ["INT_ADD", "register:40f0:8", ["const:78e464:8", "const:4:8"]]
+ 0078e464 ["CALL", null, ["callee:00c57e90:8"]]
- 0078e424 bytes 9b251394
+ 0078e464 bytes 8b261394
- 0078e430 ["COPY", "tmp:0:8", ["const:368:8"]]
- 0078e430 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0078e430 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0078e430 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0078e470 ["COPY", "tmp:0:8", ["const:768:8"]]
+ 0078e470 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0078e470 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0078e470 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0078e430 bytes 08a10d91
+ 0078e470 bytes 08a11d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d151d60dcceb64725632680421e1984"></a>

### [`0078e444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e444.md) → [`0078e484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078e/0078e484.md) FUN_0078e484

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
      "definition_site": "0078e490",
      "incomplete_value": false,
      "site": "0078e490",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:768:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078e450",
      "incomplete_value": false,
      "site": "0078e450",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:368:8"
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
      "0078e490",
      "DATA",
      [
        "storage",
        "00c79368",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0078e490",
      "DATA",
      [
        "storage",
        "00c79768",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078e44c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e444.md#insn-0078e44c)
- 新版 `0078e48c`（命令位置の公開資料なし）

~~~diff
- 0078e44c ["COPY", "tmp:0:8", ["const:368:8"]]
- 0078e44c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0078e44c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0078e44c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0078e48c ["COPY", "tmp:0:8", ["const:768:8"]]
+ 0078e48c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0078e48c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0078e48c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0078e44c bytes 29a10d91
+ 0078e48c bytes 29a11d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d86cece2a9a57d5aa0f78913aa0f79d"></a>

### [`0078e4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e4d0.md) → [`0078e510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078e/0078e510.md) FUN_0078e510

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "0078e530",
      "incomplete_value": false,
      "site": "0078e534",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:7e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078e4f0",
      "incomplete_value": false,
      "site": "0078e4f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
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
      "0078e534",
      "DATA",
      [
        "storage",
        "00c793e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0078e534",
      "DATA",
      [
        "storage",
        "00c797e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078e4e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e4d0.md#insn-0078e4e4) · [`0078e4f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e4d0.md#insn-0078e4f0)
- 新版 `0078e524`（命令位置の公開資料なし） · `0078e530`（命令位置の公開資料なし）

~~~diff
- 0078e4e4 ["INT_ADD", "register:40f0:8", ["const:78e4e4:8", "const:4:8"]]
- 0078e4e4 ["CALL", null, ["callee:00c57e90:8"]]
+ 0078e524 ["INT_ADD", "register:40f0:8", ["const:78e524:8", "const:4:8"]]
+ 0078e524 ["CALL", null, ["callee:00c57e90:8"]]
- 0078e4e4 bytes 6b251394
+ 0078e524 bytes 5b261394
- 0078e4f0 ["COPY", "tmp:0:8", ["const:3e8:8"]]
- 0078e4f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0078e4f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0078e4f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0078e530 ["COPY", "tmp:0:8", ["const:7e8:8"]]
+ 0078e530 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0078e530 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0078e530 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0078e4f0 bytes 08a10f91
+ 0078e530 bytes 08a11f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a721b47c97b34c8869009bcd5b10a3f"></a>

### [`0078e508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e508.md) → [`0078e548`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078e/0078e548.md) FUN_0078e548

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
      "definition_site": "0078e54c",
      "incomplete_value": false,
      "site": "0078e550",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:7e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078e50c",
      "incomplete_value": false,
      "site": "0078e510",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
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
      "0078e550",
      "DATA",
      [
        "storage",
        "00c793e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0078e550",
      "DATA",
      [
        "storage",
        "00c797e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078e50c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e508.md#insn-0078e50c)
- 新版 `0078e54c`（命令位置の公開資料なし）

~~~diff
- 0078e50c ["COPY", "tmp:0:8", ["const:3e8:8"]]
- 0078e50c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0078e50c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0078e50c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0078e54c ["COPY", "tmp:0:8", ["const:7e8:8"]]
+ 0078e54c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0078e54c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0078e54c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0078e50c bytes 08a10f91
+ 0078e54c bytes 08a11f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1a7b21f6493bf78cff8620e0c933cf0"></a>

### [`0078e558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e558.md) → [`0078e598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078e/0078e598.md) FUN_0078e598

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "0078e5bc",
      "incomplete_value": false,
      "site": "0078e5bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:868:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078e57c",
      "incomplete_value": false,
      "site": "0078e57c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:468:8"
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
      "0078e5bc",
      "DATA",
      [
        "storage",
        "00c79468",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0078e5bc",
      "DATA",
      [
        "storage",
        "00c79868",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078e56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e558.md#insn-0078e56c) · [`0078e578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e558.md#insn-0078e578)
- 新版 `0078e5ac`（命令位置の公開資料なし） · `0078e5b8`（命令位置の公開資料なし）

~~~diff
- 0078e56c ["INT_ADD", "register:40f0:8", ["const:78e56c:8", "const:4:8"]]
- 0078e56c ["CALL", null, ["callee:00c57e90:8"]]
+ 0078e5ac ["INT_ADD", "register:40f0:8", ["const:78e5ac:8", "const:4:8"]]
+ 0078e5ac ["CALL", null, ["callee:00c57e90:8"]]
- 0078e56c bytes 49251394
+ 0078e5ac bytes 39261394
- 0078e578 ["COPY", "tmp:0:8", ["const:468:8"]]
- 0078e578 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0078e578 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0078e578 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0078e5b8 ["COPY", "tmp:0:8", ["const:868:8"]]
+ 0078e5b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0078e5b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0078e5b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0078e578 bytes 08a11191
+ 0078e5b8 bytes 08a12191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb82fae2f2827b2d22566c7db6b2bfc5"></a>

### [`0078e58c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e58c.md) → [`0078e5cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078e/0078e5cc.md) FUN_0078e5cc

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
      "definition_site": "0078e5d8",
      "incomplete_value": false,
      "site": "0078e5d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:868:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078e598",
      "incomplete_value": false,
      "site": "0078e598",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:468:8"
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
      "0078e5d8",
      "DATA",
      [
        "storage",
        "00c79468",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0078e5d8",
      "DATA",
      [
        "storage",
        "00c79868",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078e594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e58c.md#insn-0078e594)
- 新版 `0078e5d4`（命令位置の公開資料なし）

~~~diff
- 0078e594 ["COPY", "tmp:0:8", ["const:468:8"]]
- 0078e594 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0078e594 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0078e594 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0078e5d4 ["COPY", "tmp:0:8", ["const:868:8"]]
+ 0078e5d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0078e5d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0078e5d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0078e594 bytes 29a11191
+ 0078e5d4 bytes 29a12191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56065cfbd5a2a2cd4b49dc2fde60aa77"></a>

### [`0078e614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e614.md) → [`0078e654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078e/0078e654.md) FUN_0078e654

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "0078e678",
      "incomplete_value": false,
      "site": "0078e678",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:8e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078e638",
      "incomplete_value": false,
      "site": "0078e638",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:4e8:8"
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
      "0078e678",
      "DATA",
      [
        "storage",
        "00c794e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0078e678",
      "DATA",
      [
        "storage",
        "00c798e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078e628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e614.md#insn-0078e628) · [`0078e634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e614.md#insn-0078e634)
- 新版 `0078e668`（命令位置の公開資料なし） · `0078e674`（命令位置の公開資料なし）

~~~diff
- 0078e628 ["INT_ADD", "register:40f0:8", ["const:78e628:8", "const:4:8"]]
- 0078e628 ["CALL", null, ["callee:00c57e90:8"]]
+ 0078e668 ["INT_ADD", "register:40f0:8", ["const:78e668:8", "const:4:8"]]
+ 0078e668 ["CALL", null, ["callee:00c57e90:8"]]
- 0078e628 bytes 1a251394
+ 0078e668 bytes 0a261394
- 0078e634 ["COPY", "tmp:0:8", ["const:4e8:8"]]
- 0078e634 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0078e634 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0078e634 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0078e674 ["COPY", "tmp:0:8", ["const:8e8:8"]]
+ 0078e674 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0078e674 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0078e674 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0078e634 bytes 08a11391
+ 0078e674 bytes 08a12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-234b632c0e08a0f3ff3653f9326ce930"></a>

### [`0078e664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e664.md) → [`0078e6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078e/0078e6a4.md) FUN_0078e6a4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`0078e7ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e7ec.md) [`0078e7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e7f0.md) [`008b6ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6ed4.md) [`008b7984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7984.md) [`00aca9d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00aca9d8.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0078e82c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078e/0078e82c.md) [`0078e830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078e/0078e830.md) [`008b6f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f18.md) [`008b79c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b79c8.md) [`00acabd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aca/00acabd4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0078e6d8",
      "incomplete_value": false,
      "site": "0078e6d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:958:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078e698",
      "incomplete_value": false,
      "site": "0078e698",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:558:8"
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
      "0078e6d8",
      "DATA",
      [
        "storage",
        "00c79558",
        null,
        "undefined *"
      ]
    ],
    [
      "0078e710",
      "READ",
      [
        "storage",
        "00c79578",
        null,
        "pointer"
      ]
    ],
    [
      "0078e710",
      "READ",
      [
        "storage",
        "00c79580",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0078e6d8",
      "DATA",
      [
        "storage",
        "00c79958",
        null,
        "undefined *"
      ]
    ],
    [
      "0078e710",
      "READ",
      [
        "storage",
        "00c79978",
        null,
        "pointer"
      ]
    ],
    [
      "0078e710",
      "READ",
      [
        "storage",
        "00c79980",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078e68c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e664.md#insn-0078e68c) · [`0078e6a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e664.md#insn-0078e6a8) · [`0078e6d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e664.md#insn-0078e6d4)
- 新版 `0078e6cc`（命令位置の公開資料なし） · `0078e6e8`（命令位置の公開資料なし） · `0078e714`（命令位置の公開資料なし）

~~~diff
- 0078e68c ["COPY", "tmp:0:8", ["const:558:8"]]
- 0078e68c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0078e68c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0078e68c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0078e6cc ["COPY", "tmp:0:8", ["const:958:8"]]
+ 0078e6cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0078e6cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0078e6cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0078e68c bytes 08611591
+ 0078e6cc bytes 08612591
- 0078e6a8 ["INT_ADD", "register:40f0:8", ["const:78e6a8:8", "const:4:8"]]
- 0078e6a8 ["CALL", null, ["callee:00acabd4:8"]]
+ 0078e6e8 ["INT_ADD", "register:40f0:8", ["const:78e6e8:8", "const:4:8"]]
+ 0078e6e8 ["CALL", null, ["callee:00acabd4:8"]]
- 0078e6a8 bytes ccf00c94
+ 0078e6e8 bytes 3bf10c94
- 0078e6d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0078e6d4 ["INT_ADD", "register:40f0:8", ["const:78e6d4:8", "const:4:8"]]
- 0078e6d4 ["CALLIND", null, ["register:0:8"]]
+ 0078e714 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0078e714 ["INT_ADD", "register:40f0:8", ["const:78e714:8", "const:4:8"]]
+ 0078e714 ["CALLIND", null, ["register:0:8"]]
- 0078e6d4 bytes 00013fd6
+ 0078e714 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6721cf97ce2c74289e7320d6b3a7f81"></a>

### [`0078e7a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e7a4.md) → [`0078e7e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078e/0078e7e4.md) FUN_0078e7e4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "0078e808",
      "incomplete_value": false,
      "site": "0078e808",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:958:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078e7c8",
      "incomplete_value": false,
      "site": "0078e7c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:558:8"
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
      "0078e808",
      "DATA",
      [
        "storage",
        "00c79558",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0078e808",
      "DATA",
      [
        "storage",
        "00c79958",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078e7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e7a4.md#insn-0078e7b8) · [`0078e7c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e7a4.md#insn-0078e7c4)
- 新版 `0078e7f8`（命令位置の公開資料なし） · `0078e804`（命令位置の公開資料なし）

~~~diff
- 0078e7b8 ["INT_ADD", "register:40f0:8", ["const:78e7b8:8", "const:4:8"]]
- 0078e7b8 ["CALL", null, ["callee:00c57e90:8"]]
+ 0078e7f8 ["INT_ADD", "register:40f0:8", ["const:78e7f8:8", "const:4:8"]]
+ 0078e7f8 ["CALL", null, ["callee:00c57e90:8"]]
- 0078e7b8 bytes b6241394
+ 0078e7f8 bytes a6251394
- 0078e7c4 ["COPY", "tmp:0:8", ["const:558:8"]]
- 0078e7c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0078e7c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0078e7c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0078e804 ["COPY", "tmp:0:8", ["const:958:8"]]
+ 0078e804 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0078e804 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0078e804 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0078e7c4 bytes 08611591
+ 0078e804 bytes 08612591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd7290a65878c33de39bf515b7b6db89"></a>

### [`0078e7d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e7d8.md) → [`0078e818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078e/0078e818.md) FUN_0078e818

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
      "definition_site": "0078e824",
      "incomplete_value": false,
      "site": "0078e824",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:958:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078e7e4",
      "incomplete_value": false,
      "site": "0078e7e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
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
      "0078e824",
      "DATA",
      [
        "storage",
        "00c79558",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0078e824",
      "DATA",
      [
        "storage",
        "00c79958",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078e7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e7d8.md#insn-0078e7e0)
- 新版 `0078e820`（命令位置の公開資料なし）

~~~diff
- 0078e7e0 ["COPY", "tmp:0:8", ["const:558:8"]]
- 0078e7e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0078e7e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0078e7e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0078e820 ["COPY", "tmp:0:8", ["const:958:8"]]
+ 0078e820 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0078e820 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0078e820 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0078e7e0 bytes 29611591
+ 0078e820 bytes 29612591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f1ca4bb0a99b9b29ffbb5223ea0b194"></a>

### [`0078e86c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e86c.md) → [`0078e8ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078e/0078e8ac.md) FUN_0078e8ac

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00789da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00789/00789da0.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)
- 新版 呼出元 1件 [`00789de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00789/00789de0.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)

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
      "definition_site": "0078e8b8",
      "incomplete_value": false,
      "site": "0078e8bc",
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
    "old": {
      "definition_site": "0078e878",
      "incomplete_value": false,
      "site": "0078e87c",
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
            "const:f0c:8"
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
      "0078e8b8",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0078e8b8",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078e87c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e86c.md#insn-0078e87c) · [`0078e878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e86c.md#insn-0078e878)
- 新版 `0078e8bc`（命令位置の公開資料なし） · `0078e8b8`（命令位置の公開資料なし）

~~~diff
- 0078e87c ["INT_ADD", "register:40f0:8", ["const:78e87c:8", "const:4:8"]]
- 0078e87c ["CALL", null, ["callee:00442930:8"]]
+ 0078e8bc ["INT_ADD", "register:40f0:8", ["const:78e8bc:8", "const:4:8"]]
+ 0078e8bc ["CALL", null, ["callee:00442930:8"]]
- 0078e87c bytes 1dd0f297
+ 0078e8bc bytes 1dd0f297
- 0078e878 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0078e878 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0078e878 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0078e878 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0078e8b8 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 0078e8b8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0078e8b8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0078e8b8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0078e878 bytes 00303c91
+ 0078e8b8 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d30f4a106c4abad14d2ddf4345d110c1"></a>

### [`0078e884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e884.md) → [`0078e8c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078e/0078e8c4.md) FUN_0078e8c4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "0078e8e4",
      "incomplete_value": false,
      "site": "0078e8e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:9e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078e8a4",
      "incomplete_value": false,
      "site": "0078e8a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:5e8:8"
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
      "0078e8e8",
      "DATA",
      [
        "storage",
        "00c795e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0078e8e8",
      "DATA",
      [
        "storage",
        "00c799e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078e898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e884.md#insn-0078e898) · [`0078e8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e884.md#insn-0078e8a4)
- 新版 `0078e8d8`（命令位置の公開資料なし） · `0078e8e4`（命令位置の公開資料なし）

~~~diff
- 0078e898 ["INT_ADD", "register:40f0:8", ["const:78e898:8", "const:4:8"]]
- 0078e898 ["CALL", null, ["callee:00c57e90:8"]]
+ 0078e8d8 ["INT_ADD", "register:40f0:8", ["const:78e8d8:8", "const:4:8"]]
+ 0078e8d8 ["CALL", null, ["callee:00c57e90:8"]]
- 0078e898 bytes 7e241394
+ 0078e8d8 bytes 6e251394
- 0078e8a4 ["COPY", "tmp:0:8", ["const:5e8:8"]]
- 0078e8a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0078e8a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0078e8a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0078e8e4 ["COPY", "tmp:0:8", ["const:9e8:8"]]
+ 0078e8e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0078e8e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0078e8e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0078e8a4 bytes 08a11791
+ 0078e8e4 bytes 08a12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02f9438f8a7d5aee54b42b8bc6684757"></a>

### [`0078e8bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e8bc.md) → [`0078e8fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078e/0078e8fc.md) FUN_0078e8fc

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
      "definition_site": "0078e900",
      "incomplete_value": false,
      "site": "0078e904",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:9e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078e8c0",
      "incomplete_value": false,
      "site": "0078e8c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:5e8:8"
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
      "0078e904",
      "DATA",
      [
        "storage",
        "00c795e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0078e904",
      "DATA",
      [
        "storage",
        "00c799e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078e8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e8bc.md#insn-0078e8c0)
- 新版 `0078e900`（命令位置の公開資料なし）

~~~diff
- 0078e8c0 ["COPY", "tmp:0:8", ["const:5e8:8"]]
- 0078e8c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0078e8c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0078e8c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0078e900 ["COPY", "tmp:0:8", ["const:9e8:8"]]
+ 0078e900 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0078e900 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0078e900 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0078e8c0 bytes 08a11791
+ 0078e900 bytes 08a12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fba622c802d1c8b58ad6490ca483e50a"></a>

### [`0078e8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e8dc.md) → [`0078e91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078e/0078e91c.md) FUN_0078e91c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048e7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e7a0.md) [`0049f3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3b0.md) [`0078ecf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078ecf4.md) [`0078ecf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078ecf8.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048e7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e7e0.md) [`0049f3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f3f0.md) [`0078ed34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078e/0078ed34.md) [`0078ed38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078e/0078ed38.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0078e97c",
      "incomplete_value": false,
      "site": "0078e97c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:ae8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078e93c",
      "incomplete_value": false,
      "site": "0078e93c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:6e8:8"
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
      "definition_site": null,
      "incomplete_value": true,
      "site": "0078e95c",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0078e91c",
      "value": [
        "leaf",
        "ram:48ccb8:8"
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
      "0078e95c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "0078e968",
      "DATA",
      [
        "storage",
        "0039b1d8",
        "fde_0039b1d8",
        "dword"
      ]
    ],
    [
      "0078e97c",
      "DATA",
      [
        "storage",
        "00c796e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0078e95c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "0078e968",
      "DATA",
      [
        "storage",
        "0039b1d8",
        null,
        "dword"
      ]
    ],
    [
      "0078e97c",
      "DATA",
      [
        "storage",
        "00c79ae8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078e91c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e8dc.md#insn-0078e91c) · [`0078e920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e8dc.md#insn-0078e920) · [`0078e934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e8dc.md#insn-0078e934)
- 新版 `0078e95c`（命令位置の公開資料なし） · `0078e960`（命令位置の公開資料なし） · `0078e974`（命令位置の公開資料なし）

~~~diff
- 0078e91c ["INT_ADD", "register:40f0:8", ["const:78e91c:8", "const:4:8"]]
- 0078e91c ["CALL", null, ["ram:48ccb8:8"]]
+ 0078e95c ["INT_ADD", "register:40f0:8", ["const:78e95c:8", "const:4:8"]]
+ 0078e95c ["CALL", null, ["ram:48ccf8:8"]]
- 0078e91c bytes e7f8f397
+ 0078e95c bytes e7f8f397
- 0078e920 ["INT_ADD", "register:40f0:8", ["const:78e920:8", "const:4:8"]]
- 0078e920 ["CALL", null, ["callee:0048e7e0:8"]]
+ 0078e960 ["INT_ADD", "register:40f0:8", ["const:78e960:8", "const:4:8"]]
+ 0078e960 ["CALL", null, ["callee:0048e7e0:8"]]
- 0078e920 bytes a0fff397
+ 0078e960 bytes a0fff397
- 0078e934 ["COPY", "tmp:0:8", ["const:6e8:8"]]
- 0078e934 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0078e934 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0078e934 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0078e974 ["COPY", "tmp:0:8", ["const:ae8:8"]]
+ 0078e974 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0078e974 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0078e974 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0078e934 bytes 08a11b91
+ 0078e974 bytes 08a12b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc6b08b28bd1c90d3dbb0a138bc65fd5"></a>

### [`0078ea98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078ea98.md) → [`0078ead8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078e/0078ead8.md) FUN_0078ead8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "0078eaf8",
      "incomplete_value": false,
      "site": "0078eafc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078eab8",
      "incomplete_value": false,
      "site": "0078eabc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:668:8"
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
      "0078eafc",
      "DATA",
      [
        "storage",
        "00c79668",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0078eafc",
      "DATA",
      [
        "storage",
        "00c79a68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078eaac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078ea98.md#insn-0078eaac) · [`0078eab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078ea98.md#insn-0078eab8)
- 新版 `0078eaec`（命令位置の公開資料なし） · `0078eaf8`（命令位置の公開資料なし）

~~~diff
- 0078eaac ["INT_ADD", "register:40f0:8", ["const:78eaac:8", "const:4:8"]]
- 0078eaac ["CALL", null, ["callee:00c57e90:8"]]
+ 0078eaec ["INT_ADD", "register:40f0:8", ["const:78eaec:8", "const:4:8"]]
+ 0078eaec ["CALL", null, ["callee:00c57e90:8"]]
- 0078eaac bytes f9231394
+ 0078eaec bytes e9241394
- 0078eab8 ["COPY", "tmp:0:8", ["const:668:8"]]
- 0078eab8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0078eab8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0078eab8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0078eaf8 ["COPY", "tmp:0:8", ["const:a68:8"]]
+ 0078eaf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0078eaf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0078eaf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0078eab8 bytes 08a11991
+ 0078eaf8 bytes 08a12991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a902b154f783aa8cee0817afac60875"></a>

### [`0078eaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078eaf0.md) → [`0078eb30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078e/0078eb30.md) FUN_0078eb30

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048e7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e7a0.md) [`0049f3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3b0.md) [`0078ecf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078ecf4.md) [`0078ecf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078ecf8.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048e7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e7e0.md) [`0049f3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f3f0.md) [`0078ed34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078e/0078ed34.md) [`0078ed38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078e/0078ed38.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0078eb90",
      "incomplete_value": true,
      "site": "0078eb90",
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
            "const:ae8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078eb50",
      "incomplete_value": true,
      "site": "0078eb50",
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
            "const:6e8:8"
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
      "definition_site": null,
      "incomplete_value": true,
      "site": "0078eb70",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0078eb30",
      "value": [
        "leaf",
        "ram:48ccb8:8"
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
      "0078eb70",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "0078eb7c",
      "DATA",
      [
        "storage",
        "0039b1d8",
        "fde_0039b1d8",
        "dword"
      ]
    ],
    [
      "0078eb90",
      "DATA",
      [
        "storage",
        "00c796e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0078eb70",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "0078eb7c",
      "DATA",
      [
        "storage",
        "0039b1d8",
        null,
        "dword"
      ]
    ],
    [
      "0078eb90",
      "DATA",
      [
        "storage",
        "00c79ae8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078eb30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078eaf0.md#insn-0078eb30) · [`0078eb34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078eaf0.md#insn-0078eb34) · [`0078eb48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078eaf0.md#insn-0078eb48)
- 新版 `0078eb70`（命令位置の公開資料なし） · `0078eb74`（命令位置の公開資料なし） · `0078eb88`（命令位置の公開資料なし）

~~~diff
- 0078eb30 ["INT_ADD", "register:40f0:8", ["const:78eb30:8", "const:4:8"]]
- 0078eb30 ["CALL", null, ["ram:48ccb8:8"]]
+ 0078eb70 ["INT_ADD", "register:40f0:8", ["const:78eb70:8", "const:4:8"]]
+ 0078eb70 ["CALL", null, ["ram:48ccf8:8"]]
- 0078eb30 bytes 62f8f397
+ 0078eb70 bytes 62f8f397
- 0078eb34 ["INT_ADD", "register:40f0:8", ["const:78eb34:8", "const:4:8"]]
- 0078eb34 ["CALL", null, ["callee:0048e7e0:8"]]
+ 0078eb74 ["INT_ADD", "register:40f0:8", ["const:78eb74:8", "const:4:8"]]
+ 0078eb74 ["CALL", null, ["callee:0048e7e0:8"]]
- 0078eb34 bytes 1bfff397
+ 0078eb74 bytes 1bfff397
- 0078eb48 ["COPY", "tmp:0:8", ["const:6e8:8"]]
- 0078eb48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0078eb48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0078eb48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0078eb88 ["COPY", "tmp:0:8", ["const:ae8:8"]]
+ 0078eb88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0078eb88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0078eb88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0078eb48 bytes 08a11b91
+ 0078eb88 bytes 08a12b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b24c0eb304c15b99cc4d133bb23b060"></a>

### [`0078ecac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078ecac.md) → [`0078ecec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078e/0078ecec.md) FUN_0078ecec

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "0078ed10",
      "incomplete_value": false,
      "site": "0078ed10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:ae8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078ecd0",
      "incomplete_value": false,
      "site": "0078ecd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:6e8:8"
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
      "0078ed10",
      "DATA",
      [
        "storage",
        "00c796e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0078ed10",
      "DATA",
      [
        "storage",
        "00c79ae8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078ecc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078ecac.md#insn-0078ecc0) · [`0078eccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078ecac.md#insn-0078eccc)
- 新版 `0078ed00`（命令位置の公開資料なし） · `0078ed0c`（命令位置の公開資料なし）

~~~diff
- 0078ecc0 ["INT_ADD", "register:40f0:8", ["const:78ecc0:8", "const:4:8"]]
- 0078ecc0 ["CALL", null, ["callee:00c57e90:8"]]
+ 0078ed00 ["INT_ADD", "register:40f0:8", ["const:78ed00:8", "const:4:8"]]
+ 0078ed00 ["CALL", null, ["callee:00c57e90:8"]]
- 0078ecc0 bytes 74231394
+ 0078ed00 bytes 64241394
- 0078eccc ["COPY", "tmp:0:8", ["const:6e8:8"]]
- 0078eccc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0078eccc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0078eccc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0078ed0c ["COPY", "tmp:0:8", ["const:ae8:8"]]
+ 0078ed0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0078ed0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0078ed0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0078eccc bytes 08a11b91
+ 0078ed0c bytes 08a12b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-230f623d363efa57b75136f1a68b70d2"></a>

### [`0078ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078ed74.md) → [`0078edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078e/0078edb4.md) _INIT_136

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.01% / 新版 87.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0078edf0",
      "incomplete_value": true,
      "site": "0078ee0c",
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
    "old": {
      "definition_site": "0078edb0",
      "incomplete_value": true,
      "site": "0078edcc",
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
                "const:ee6:8"
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
      "definition_site": "0078ee14",
      "incomplete_value": true,
      "site": "0078ee30",
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
    "old": {
      "definition_site": "0078edd4",
      "incomplete_value": true,
      "site": "0078edf0",
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
                "const:ef9:8"
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
      "definition_site": "0078ee34",
      "incomplete_value": true,
      "site": "0078ee50",
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
    "old": {
      "definition_site": "0078edf4",
      "incomplete_value": true,
      "site": "0078ee10",
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
                "const:d82:8"
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
      "0078edf0",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "0078ee14",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "0078ee34",
      "READ",
      [
        "storage",
        "002b8d82",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0078edf0",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "0078ee14",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "0078ee34",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078ee0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078ed74.md#insn-0078ee0c) · [`0078efa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078ed74.md#insn-0078efa8) · [`0078eda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078ed74.md#insn-0078eda0)
- 新版 `0078ee4c`（命令位置の公開資料なし） · `0078efe8`（命令位置の公開資料なし） · `0078ede0`（命令位置の公開資料なし）

~~~diff
- 0078ee0c ["COPY", "tmp:0:8", ["const:e95:8"]]
- 0078ee0c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0078ee0c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0078ee0c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0078ee4c ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 0078ee4c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0078ee4c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0078ee4c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0078ee0c bytes 4a553a91
+ 0078ee4c bytes 4a893d91
- 0078efa8 ["INT_ADD", "register:40f0:8", ["const:78efa8:8", "const:4:8"]]
- 0078efa8 ["CALL", null, ["callee:00c57e30:8"]]
+ 0078efe8 ["INT_ADD", "register:40f0:8", ["const:78efe8:8", "const:4:8"]]
+ 0078efe8 ["CALL", null, ["callee:00c57e30:8"]]
- 0078efa8 bytes a2221394
+ 0078efe8 bytes 92231394
- 0078eda0 ["COPY", "tmp:0:8", ["const:a40:8"]]
- 0078eda0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0078eda0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0078eda0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0078ede0 ["COPY", "tmp:0:8", ["const:e40:8"]]
+ 0078ede0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0078ede0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0078ede0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0078eda0 bytes 73022991
+ 0078ede0 bytes 73023991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2de83c53b3aaef6ba214ed06d544aa64"></a>

### [`0078fe94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078f/0078fe94.md) → [`0078fed4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078f/0078fed4.md) FUN_0078fed4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) · 呼出先 15件 [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`007901c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00790/007901c4.md) [`00794838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00794/00794838.md)
- 新版 呼出元 1件 [`0075eb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075eb80.md) · 呼出先 15件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`00790204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00790/00790204.md) [`00794878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/00794878.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 84.66% / 新版 84.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `call_target` 2件, `store_destination` 7件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0078ff64",
      "incomplete_value": false,
      "site": "0078ff64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:b68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078ff24",
      "incomplete_value": false,
      "site": "0078ff24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:768:8"
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
      "definition_site": "00790020",
      "incomplete_value": false,
      "site": "00790020",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:be8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078ffe0",
      "incomplete_value": false,
      "site": "0078ffe0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:7e8:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00790130",
      "incomplete_value": false,
      "site": "00790130",
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
    "old": {
      "definition_site": "007900f0",
      "incomplete_value": false,
      "site": "007900f0",
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
                "const:b00:8"
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
    "ordinal": 20,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0078ff08",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ],
    [
      "0078ff14",
      "PARAM",
      [
        "storage",
        "00ca4b00",
        null,
        "undefined8"
      ]
    ],
    [
      "0078ff1c",
      "PARAM",
      [
        "storage",
        "00ca7a70",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0078ff08",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      "0078ff14",
      "PARAM",
      [
        "storage",
        "00ca4f00",
        null,
        "undefined8"
      ]
    ],
    [
      "0078ff1c",
      "PARAM",
      [
        "storage",
        "00ca7e70",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078fee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078f/0078fe94.md#insn-0078fee4) · [`0078fef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078f/0078fe94.md#insn-0078fef0) · [`0078fef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078f/0078fe94.md#insn-0078fef8)
- 新版 `0078ff24`（命令位置の公開資料なし） · `0078ff30`（命令位置の公開資料なし） · `0078ff38`（命令位置の公開資料なし）

~~~diff
- 0078fee4 ["COPY", "tmp:0:8", ["const:a88:8"]]
- 0078fee4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0078fee4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0078fee4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0078ff24 ["COPY", "tmp:0:8", ["const:e88:8"]]
+ 0078ff24 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0078ff24 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0078ff24 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0078fee4 bytes 42202a91
+ 0078ff24 bytes 42203a91
- 0078fef0 ["INT_ADD", "register:40f0:8", ["const:78fef0:8", "const:4:8"]]
- 0078fef0 ["CALL", null, ["callee:0047e60c:8"]]
+ 0078ff30 ["INT_ADD", "register:40f0:8", ["const:78ff30:8", "const:4:8"]]
+ 0078ff30 ["CALL", null, ["callee:0047e60c:8"]]
- 0078fef0 bytes b7b9f397
+ 0078ff30 bytes b7b9f397
- 0078fef8 ["INT_ADD", "register:40f0:8", ["const:78fef8:8", "const:4:8"]]
- 0078fef8 ["CALL", null, ["ram:46c984:8"]]
+ 0078ff38 ["INT_ADD", "register:40f0:8", ["const:78ff38:8", "const:4:8"]]
+ 0078ff38 ["CALL", null, ["ram:46c9c4:8"]]
- 0078fef8 bytes a372f397
+ 0078ff38 bytes a372f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-710bf30b8590ae56860fbe3c192e86c6"></a>

### [`007901c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00790/007901c4.md) → [`00790204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00790/00790204.md) FUN_00790204

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0078fe94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078f/0078fe94.md) · 呼出先 12件 [`005d8b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8b88.md) [`0079513c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00795/0079513c.md) [`008b6ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6ecc.md) [`008b6fa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6fa8.md) [`00a4658c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a4658c.md)
- 新版 呼出元 1件 [`0078fed4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078f/0078fed4.md) · 呼出先 12件 [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md) [`0079517c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/0079517c.md) [`008b6f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f10.md) [`008b6fec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6fec.md) [`00a46784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46784.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.64% / 新版 94.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00790314",
      "incomplete_value": true,
      "site": "00790318",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007902d4",
      "incomplete_value": true,
      "site": "007902d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00790358",
      "incomplete_value": true,
      "site": "00790358",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00790318",
      "incomplete_value": true,
      "site": "00790318",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007903f0",
      "incomplete_value": false,
      "site": "007903f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:c68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007903b0",
      "incomplete_value": false,
      "site": "007903b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:868:8"
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
      "007902d8",
      "READ",
      [
        "storage",
        "00c9af68",
        null,
        "pointer"
      ]
    ],
    [
      "007902ec",
      "DATA",
      [
        "storage",
        "00c8b358",
        null,
        "undefined *"
      ]
    ],
    [
      "00790310",
      "READ",
      [
        "storage",
        "00c9af70",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007902d8",
      "READ",
      [
        "storage",
        "00c9b368",
        null,
        "pointer"
      ]
    ],
    [
      "007902ec",
      "DATA",
      [
        "storage",
        "00c8b758",
        null,
        "undefined *"
      ]
    ],
    [
      "00790310",
      "READ",
      [
        "storage",
        "00c9b370",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00790298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00790/007901c4.md#insn-00790298) · [`00790244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00790/007901c4.md#insn-00790244) · [`00790258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00790/007901c4.md#insn-00790258)
- 新版 `007902d8`（命令位置の公開資料なし） · `00790284`（命令位置の公開資料なし） · `00790298`（命令位置の公開資料なし）

~~~diff
- 00790298 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:f68:8"]]
- 00790298 ["LOAD", "register:40d8:8", ["const:1b1:8", "tmp:0:8"]]
+ 007902d8 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:368:8"]]
+ 007902d8 ["LOAD", "register:40d8:8", ["const:1b1:8", "tmp:0:8"]]
- 00790298 bytes 7bb747f9
+ 007902d8 bytes 7bb741f9
- 00790244 ["INT_ADD", "register:40f0:8", ["const:790244:8", "const:4:8"]]
- 00790244 ["CALL", null, ["callee:00a4754c:8"]]
+ 00790284 ["INT_ADD", "register:40f0:8", ["const:790284:8", "const:4:8"]]
+ 00790284 ["CALL", null, ["callee:00a4754c:8"]]
- 00790244 bytes 44dc0a94
+ 00790284 bytes b2dc0a94
- 00790258 ["COPY", "register:0:8", ["register:4040:8"]]
- 00790258 ["INT_ADD", "register:40f0:8", ["const:790258:8", "const:4:8"]]
- 00790258 ["CALLIND", null, ["register:0:8"]]
+ 00790298 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00790298 ["INT_ADD", "register:40f0:8", ["const:790298:8", "const:4:8"]]
+ 00790298 ["CALLIND", null, ["register:0:8"]]
- 00790258 bytes 00013fd6
+ 00790298 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-995a4c953cbc54034b14364949fed943"></a>

### [`00792988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00792/00792988.md) → [`007929c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00792/007929c8.md) FUN_007929c8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) · 呼出先 8件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`005c1bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1bb0.md) [`00794be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00794/00794be8.md) [`009a95cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a9/009a95cc.md) [`009ad7e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ad/009ad7e4.md)
- 新版 呼出元 1件 [`0075eb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075eb80.md) · 呼出先 8件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`005c1bf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c1bf0.md) [`00794c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/00794c28.md) [`009a9768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a9/009a9768.md) [`009ad980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ad/009ad980.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.43% / 新版 99.43%

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
      "site": "00792ad4",
      "value": [
        "leaf",
        "ram:9a9768:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00792a94",
      "value": [
        "leaf",
        "ram:9a95cc:8"
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
      "00792ad4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "009a95cc"
      ]
    ]
  ],
  "added": [
    [
      "00792ad4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "009a9768"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00792a94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00792/00792988.md#insn-00792a94) · [`007929e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00792/00792988.md#insn-007929e8) · [`007929f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00792/00792988.md#insn-007929f4)
- 新版 `00792ad4`（命令位置の公開資料なし） · `00792a28`（命令位置の公開資料なし） · `00792a34`（命令位置の公開資料なし）

~~~diff
- 00792a94 ["INT_ADD", "register:40f0:8", ["const:792a94:8", "const:4:8"]]
- 00792a94 ["CALL", null, ["ram:9a95cc:8"]]
+ 00792ad4 ["INT_ADD", "register:40f0:8", ["const:792ad4:8", "const:4:8"]]
+ 00792ad4 ["CALL", null, ["ram:9a9768:8"]]
- 00792a94 bytes ce5a0894
+ 00792ad4 bytes 255b0894
- 007929e8 ["INT_ADD", "register:40f0:8", ["const:7929e8:8", "const:4:8"]]
- 007929e8 ["CALL", null, ["callee:00794c28:8"]]
+ 00792a28 ["INT_ADD", "register:40f0:8", ["const:792a28:8", "const:4:8"]]
+ 00792a28 ["CALL", null, ["callee:00794c28:8"]]
- 007929e8 bytes 80080094
+ 00792a28 bytes 80080094
- 007929f4 ["INT_ADD", "register:40f0:8", ["const:7929f4:8", "const:4:8"]]
- 007929f4 ["CALL", null, ["callee:005c1bf0:8"]]
+ 00792a34 ["INT_ADD", "register:40f0:8", ["const:792a34:8", "const:4:8"]]
+ 00792a34 ["CALL", null, ["callee:005c1bf0:8"]]
- 007929f4 bytes 6fbcf897
+ 00792a34 bytes 6fbcf897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd0d9abbcb9235404c2b3b078ef52c46"></a>

### [`00792e74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00792/00792e74.md) → [`00792eb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00792/00792eb4.md) FUN_00792eb4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00773854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773854.md) · 呼出先 14件 [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`004687c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/004687c4.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0063670c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/0063670c.md) [`00794eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00794/00794eb4.md)
- 新版 呼出元 1件 [`00773894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/00773894.md) · 呼出先 14件 [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00468804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468804.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0063674c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00636/0063674c.md) [`00794ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/00794ef4.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.23% / 新版 99.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00793140",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00793100",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 8,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007931f0",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007931b0",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 11,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007932a0",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00793260",
      "value": [
        "leaf",
        "ram:46c984:8"
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
      "00793140",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "007931f0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "007932a0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ]
  ],
  "added": [
    [
      "00793140",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "007931f0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "007932a0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00793100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00792/00792e74.md#insn-00793100) · [`007931b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00792/00792e74.md#insn-007931b0) · [`00793260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00792/00792e74.md#insn-00793260)
- 新版 `00793140`（命令位置の公開資料なし） · `007931f0`（命令位置の公開資料なし） · `007932a0`（命令位置の公開資料なし）

~~~diff
- 00793100 ["INT_ADD", "register:40f0:8", ["const:793100:8", "const:4:8"]]
- 00793100 ["CALL", null, ["ram:46c984:8"]]
+ 00793140 ["INT_ADD", "register:40f0:8", ["const:793140:8", "const:4:8"]]
+ 00793140 ["CALL", null, ["ram:46c9c4:8"]]
- 00793100 bytes 2166f397
+ 00793140 bytes 2166f397
- 007931b0 ["INT_ADD", "register:40f0:8", ["const:7931b0:8", "const:4:8"]]
- 007931b0 ["CALL", null, ["ram:46c984:8"]]
+ 007931f0 ["INT_ADD", "register:40f0:8", ["const:7931f0:8", "const:4:8"]]
+ 007931f0 ["CALL", null, ["ram:46c9c4:8"]]
- 007931b0 bytes f565f397
+ 007931f0 bytes f565f397
- 00793260 ["INT_ADD", "register:40f0:8", ["const:793260:8", "const:4:8"]]
- 00793260 ["CALL", null, ["ram:46c984:8"]]
+ 007932a0 ["INT_ADD", "register:40f0:8", ["const:7932a0:8", "const:4:8"]]
+ 007932a0 ["CALL", null, ["ram:46c9c4:8"]]
- 00793260 bytes c965f397
+ 007932a0 bytes c965f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03bccd4968e14490c1ac2d39f9adf8da"></a>

### [`007938c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00793/007938c8.md) → [`00793908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00793/00793908.md) FUN_00793908

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`007937d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00793/007937d0.md) [`00794840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00794/00794840.md) [`007948c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00794/007948c8.md) · 呼出先 18件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`00615e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00615/00615e8c.md) [`00652480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00652/00652480.md)
- 新版 呼出元 3件 [`00793810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00793/00793810.md) [`00794880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/00794880.md) [`00794908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/00794908.md) · 呼出先 18件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`00615ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00615/00615ecc.md) [`006524c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00652/006524c0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.80% / 新版 99.80%

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
      "site": "00793d50",
      "value": [
        "leaf",
        "ram:9a9768:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00793d10",
      "value": [
        "leaf",
        "ram:9a95cc:8"
      ]
    },
    "ordinal": 21,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00793d50",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "009a95cc"
      ]
    ]
  ],
  "added": [
    [
      "00793d50",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "009a9768"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00793d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00793/007938c8.md#insn-00793d10) · [`00793920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00793/007938c8.md#insn-00793920) · [`007939c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00793/007938c8.md#insn-007939c8)
- 新版 `00793d50`（命令位置の公開資料なし） · `00793960`（命令位置の公開資料なし） · `00793a08`（命令位置の公開資料なし）

~~~diff
- 00793d10 ["INT_ADD", "register:40f0:8", ["const:793d10:8", "const:4:8"]]
- 00793d10 ["CALL", null, ["ram:9a95cc:8"]]
+ 00793d50 ["INT_ADD", "register:40f0:8", ["const:793d50:8", "const:4:8"]]
+ 00793d50 ["CALL", null, ["ram:9a9768:8"]]
- 00793d10 bytes 2f560894
+ 00793d50 bytes 86560894
- 00793920 ["INT_ADD", "register:40f0:8", ["const:793920:8", "const:4:8"]]
- 00793920 ["CALL", null, ["callee:008514f8:8"]]
+ 00793960 ["INT_ADD", "register:40f0:8", ["const:793960:8", "const:4:8"]]
+ 00793960 ["CALL", null, ["callee:008514f8:8"]]
- 00793920 bytes e6f60294
+ 00793960 bytes e6f60294
- 007939c8 ["INT_ADD", "register:40f0:8", ["const:7939c8:8", "const:4:8"]]
- 007939c8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00793a08 ["INT_ADD", "register:40f0:8", ["const:793a08:8", "const:4:8"]]
+ 00793a08 ["CALL", null, ["callee:00c57e90:8"]]
- 007939c8 bytes 32101394
+ 00793a08 bytes 22111394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c267273ee18b497c57b0dc831bb31be9"></a>

### [`00794194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00794/00794194.md) → [`007941d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/007941d4.md) FUN_007941d4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`007911e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00791/007911e4.md) [`007918d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00791/007918d0.md) [`00791e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00791/00791e20.md) [`00792444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00792/00792444.md) · 呼出先 16件 [`0047e89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e89c.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`00493958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493958.md) [`0054071c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/0054071c.md) [`0063670c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/0063670c.md)
- 新版 呼出元 4件 [`00791224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00791/00791224.md) [`00791910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00791/00791910.md) [`00791e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00791/00791e60.md) [`00792484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00792/00792484.md) · 呼出先 16件 [`0047e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`00493998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493998.md) [`0054075c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/0054075c.md) [`0063674c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00636/0063674c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 94.00% / 新版 94.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_destination` 7件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00794650",
      "incomplete_value": false,
      "site": "00794650",
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
    "old": {
      "definition_site": "00794610",
      "incomplete_value": false,
      "site": "00794610",
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
                "const:b00:8"
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
    "ordinal": 54,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00794654",
      "incomplete_value": false,
      "site": "00794654",
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
    "old": {
      "definition_site": "00794614",
      "incomplete_value": false,
      "site": "00794614",
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
            "const:b00:8"
          ]
        ]
      ]
    },
    "ordinal": 55,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00794650",
      "incomplete_value": false,
      "site": "00794654",
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
    "old": {
      "definition_site": "00794610",
      "incomplete_value": false,
      "site": "00794614",
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
                "const:b00:8"
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
    "ordinal": 55,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00794214",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ],
    [
      "0079437c",
      "READ",
      [
        "storage",
        "00c9a8a0",
        null,
        "pointer"
      ]
    ],
    [
      "0079437c",
      "PARAM",
      [
        "storage",
        "00ca4bd8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00794214",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      "0079437c",
      "READ",
      [
        "storage",
        "00c9aca0",
        null,
        "pointer"
      ]
    ],
    [
      "0079437c",
      "PARAM",
      [
        "storage",
        "00ca4fd8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00794358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00794/00794194.md#insn-00794358) · [`007945e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00794/00794194.md#insn-007945e0) · [`007945e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00794/00794194.md#insn-007945e8)
- 新版 `00794398`（命令位置の公開資料なし） · `00794620`（命令位置の公開資料なし） · `00794628`（命令位置の公開資料なし）

~~~diff
- 00794358 ["INT_ADD", "register:40f0:8", ["const:794358:8", "const:4:8"]]
- 00794358 ["CALL", null, ["callee:0047e8dc:8"]]
+ 00794398 ["INT_ADD", "register:40f0:8", ["const:794398:8", "const:4:8"]]
+ 00794398 ["CALL", null, ["callee:0047e8dc:8"]]
- 00794358 bytes 51a9f397
+ 00794398 bytes 51a9f397
- 007945e0 ["COPY", "tmp:0:8", ["const:b38:8"]]
- 007945e0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007945e0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007945e0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00794620 ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 00794620 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00794620 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00794620 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007945e0 bytes 00e02c91
+ 00794620 bytes 00e03c91
- 007945e8 ["INT_ADD", "register:40f0:8", ["const:7945e8:8", "const:4:8"]]
- 007945e8 ["CALL", null, ["callee:00c57e50:8"]]
+ 00794628 ["INT_ADD", "register:40f0:8", ["const:794628:8", "const:4:8"]]
+ 00794628 ["CALL", null, ["callee:00c57e50:8"]]
- 007945e8 bytes 1a0d1394
+ 00794628 bytes 0a0e1394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3d057dcd6c8a7a1618890dc7c8c2c60"></a>

### [`007947f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00794/007947f0.md) → [`00794830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/00794830.md) FUN_00794830

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00794854",
      "incomplete_value": false,
      "site": "00794854",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:b68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00794814",
      "incomplete_value": false,
      "site": "00794814",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:768:8"
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
      "00794854",
      "DATA",
      [
        "storage",
        "00c79768",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00794854",
      "DATA",
      [
        "storage",
        "00c79b68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00794804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00794/007947f0.md#insn-00794804) · [`00794810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00794/007947f0.md#insn-00794810)
- 新版 `00794844`（命令位置の公開資料なし） · `00794850`（命令位置の公開資料なし）

~~~diff
- 00794804 ["INT_ADD", "register:40f0:8", ["const:794804:8", "const:4:8"]]
- 00794804 ["CALL", null, ["callee:00c57e90:8"]]
+ 00794844 ["INT_ADD", "register:40f0:8", ["const:794844:8", "const:4:8"]]
+ 00794844 ["CALL", null, ["callee:00c57e90:8"]]
- 00794804 bytes a30c1394
+ 00794844 bytes 930d1394
- 00794810 ["COPY", "tmp:0:8", ["const:768:8"]]
- 00794810 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00794810 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00794810 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00794850 ["COPY", "tmp:0:8", ["const:b68:8"]]
+ 00794850 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00794850 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00794850 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00794810 bytes 08a11d91
+ 00794850 bytes 08a12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c979392becba7faefadddfa3f3d4ae84"></a>

### [`00794824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00794/00794824.md) → [`00794864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/00794864.md) FUN_00794864

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
      "definition_site": "00794870",
      "incomplete_value": false,
      "site": "00794870",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:b68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00794830",
      "incomplete_value": false,
      "site": "00794830",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:768:8"
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
      "00794870",
      "DATA",
      [
        "storage",
        "00c79768",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00794870",
      "DATA",
      [
        "storage",
        "00c79b68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079482c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00794/00794824.md#insn-0079482c)
- 新版 `0079486c`（命令位置の公開資料なし）

~~~diff
- 0079482c ["COPY", "tmp:0:8", ["const:768:8"]]
- 0079482c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0079482c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0079482c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0079486c ["COPY", "tmp:0:8", ["const:b68:8"]]
+ 0079486c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0079486c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0079486c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0079482c bytes 29a11d91
+ 0079486c bytes 29a12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6228354c546a20e32cf226d2e503a148"></a>

### [`00794878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00794/00794878.md) → [`007948b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/007948b8.md) FUN_007948b8

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "007948dc",
      "incomplete_value": false,
      "site": "007948dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:be8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079489c",
      "incomplete_value": false,
      "site": "0079489c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:7e8:8"
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
      "007948dc",
      "DATA",
      [
        "storage",
        "00c797e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007948dc",
      "DATA",
      [
        "storage",
        "00c79be8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079488c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00794/00794878.md#insn-0079488c) · [`00794898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00794/00794878.md#insn-00794898)
- 新版 `007948cc`（命令位置の公開資料なし） · `007948d8`（命令位置の公開資料なし）

~~~diff
- 0079488c ["INT_ADD", "register:40f0:8", ["const:79488c:8", "const:4:8"]]
- 0079488c ["CALL", null, ["callee:00c57e90:8"]]
+ 007948cc ["INT_ADD", "register:40f0:8", ["const:7948cc:8", "const:4:8"]]
+ 007948cc ["CALL", null, ["callee:00c57e90:8"]]
- 0079488c bytes 810c1394
+ 007948cc bytes 710d1394
- 00794898 ["COPY", "tmp:0:8", ["const:7e8:8"]]
- 00794898 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00794898 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00794898 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007948d8 ["COPY", "tmp:0:8", ["const:be8:8"]]
+ 007948d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007948d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007948d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00794898 bytes 08a11f91
+ 007948d8 bytes 08a12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a234758621501404104f4e37fced0bdd"></a>

### [`007948ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00794/007948ac.md) → [`007948ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/007948ec.md) FUN_007948ec

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
      "definition_site": "007948f8",
      "incomplete_value": false,
      "site": "007948f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:be8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007948b8",
      "incomplete_value": false,
      "site": "007948b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:7e8:8"
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
      "007948f8",
      "DATA",
      [
        "storage",
        "00c797e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007948f8",
      "DATA",
      [
        "storage",
        "00c79be8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007948b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00794/007948ac.md#insn-007948b4)
- 新版 `007948f4`（命令位置の公開資料なし）

~~~diff
- 007948b4 ["COPY", "tmp:0:8", ["const:7e8:8"]]
- 007948b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007948b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007948b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007948f4 ["COPY", "tmp:0:8", ["const:be8:8"]]
+ 007948f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007948f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007948f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007948b4 bytes 29a11f91
+ 007948f4 bytes 29a12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0318d9a8557546916da7f29d91ab6718"></a>

### [`00794b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00794/00794b2c.md) → [`00794b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/00794b6c.md) FUN_00794b6c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`007948fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00794/007948fc.md) [`0080d820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0080d/0080d820.md) [`00b2a7a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a7a4.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 3件 [`0079493c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/0079493c.md) [`0080d860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0080d/0080d860.md) [`00b2abcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2abcc.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "00794b78",
      "incomplete_value": false,
      "site": "00794b7c",
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
    "old": {
      "definition_site": "00794b38",
      "incomplete_value": false,
      "site": "00794b3c",
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
            "const:f0c:8"
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
      "00794b78",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00794b78",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00794b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00794/00794b2c.md#insn-00794b3c) · [`00794b38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00794/00794b2c.md#insn-00794b38)
- 新版 `00794b7c`（命令位置の公開資料なし） · `00794b78`（命令位置の公開資料なし）

~~~diff
- 00794b3c ["INT_ADD", "register:40f0:8", ["const:794b3c:8", "const:4:8"]]
- 00794b3c ["CALL", null, ["callee:0043b778:8"]]
+ 00794b7c ["INT_ADD", "register:40f0:8", ["const:794b7c:8", "const:4:8"]]
+ 00794b7c ["CALL", null, ["callee:0043b778:8"]]
- 00794b3c bytes ff9af297
+ 00794b7c bytes ff9af297
- 00794b38 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00794b38 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00794b38 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00794b38 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00794b78 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00794b78 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00794b78 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00794b78 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00794b38 bytes 00303c91
+ 00794b78 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b0925664d4763e14980ddc03b00797f"></a>

### [`00794f68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00794/00794f68.md) → [`00794fa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/00794fa8.md) FUN_00794fa8

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
      "definition_site": "00794fb4",
      "incomplete_value": false,
      "site": "00794fc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:c68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00794f74",
      "incomplete_value": false,
      "site": "00794f80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:868:8"
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
      "00794fc0",
      "DATA",
      [
        "storage",
        "00c79868",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00794fc0",
      "DATA",
      [
        "storage",
        "00c79c68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00794f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00794/00794f68.md#insn-00794f74)
- 新版 `00794fb4`（命令位置の公開資料なし）

~~~diff
- 00794f74 ["COPY", "tmp:0:8", ["const:868:8"]]
- 00794f74 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00794f74 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00794f74 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00794fb4 ["COPY", "tmp:0:8", ["const:c68:8"]]
+ 00794fb4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00794fb4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00794fb4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00794f74 bytes 4aa12191
+ 00794fb4 bytes 4aa13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d65b3d99e8f34f0f79b97d7d12c6764"></a>

### [`00794fac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00794/00794fac.md) → [`00794fec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00794/00794fec.md) FUN_00794fec

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "00795004",
      "incomplete_value": false,
      "site": "00795010",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:c68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00794fc4",
      "incomplete_value": false,
      "site": "00794fd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:868:8"
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
      "00795010",
      "DATA",
      [
        "storage",
        "00c79868",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00795010",
      "DATA",
      [
        "storage",
        "00c79c68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00794fc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00794/00794fac.md#insn-00794fc4) · [`00794ff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00794/00794fac.md#insn-00794ff4)
- 新版 `00795004`（命令位置の公開資料なし） · `00795034`（命令位置の公開資料なし）

~~~diff
- 00794fc4 ["COPY", "tmp:0:8", ["const:868:8"]]
- 00794fc4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00794fc4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00794fc4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00795004 ["COPY", "tmp:0:8", ["const:c68:8"]]
+ 00795004 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00795004 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00795004 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00794fc4 bytes 08a12191
+ 00795004 bytes 08a13191
- 00794ff4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00794ff4 ["INT_ADD", "register:40f0:8", ["const:794ff4:8", "const:4:8"]]
- 00794ff4 ["CALLIND", null, ["register:0:8"]]
+ 00795034 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00795034 ["INT_ADD", "register:40f0:8", ["const:795034:8", "const:4:8"]]
+ 00795034 ["CALLIND", null, ["register:0:8"]]
- 00794ff4 bytes 00013fd6
+ 00795034 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06c259dde32685d0c79b2b03cd46185d"></a>

### [`00795008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00795/00795008.md) → [`00795048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795048.md) FUN_00795048

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00795074",
      "incomplete_value": false,
      "site": "00795074",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:c68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00795034",
      "incomplete_value": false,
      "site": "00795034",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:868:8"
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
      "00795074",
      "DATA",
      [
        "storage",
        "00c79868",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00795074",
      "DATA",
      [
        "storage",
        "00c79c68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079501c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00795/00795008.md#insn-0079501c) · [`0079502c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00795/00795008.md#insn-0079502c) · [`00795050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00795/00795008.md#insn-00795050)
- 新版 `0079505c`（命令位置の公開資料なし） · `0079506c`（命令位置の公開資料なし） · `00795090`（命令位置の公開資料なし）

~~~diff
- 0079501c ["INT_ADD", "register:40f0:8", ["const:79501c:8", "const:4:8"]]
- 0079501c ["CALL", null, ["callee:00c57e90:8"]]
+ 0079505c ["INT_ADD", "register:40f0:8", ["const:79505c:8", "const:4:8"]]
+ 0079505c ["CALL", null, ["callee:00c57e90:8"]]
- 0079501c bytes 9d0a1394
+ 0079505c bytes 8d0b1394
- 0079502c ["COPY", "tmp:0:8", ["const:868:8"]]
- 0079502c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079502c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079502c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079506c ["COPY", "tmp:0:8", ["const:c68:8"]]
+ 0079506c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079506c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079506c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079502c bytes 08a12191
+ 0079506c bytes 08a13191
- 00795050 ["COPY", "register:0:8", ["register:4040:8"]]
- 00795050 ["INT_ADD", "register:40f0:8", ["const:795050:8", "const:4:8"]]
- 00795050 ["CALLIND", null, ["register:0:8"]]
+ 00795090 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00795090 ["INT_ADD", "register:40f0:8", ["const:795090:8", "const:4:8"]]
+ 00795090 ["CALLIND", null, ["register:0:8"]]
- 00795050 bytes 00013fd6
+ 00795090 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b1ed398149eba6bf4b1f8b0b7c72c5c"></a>

### [`00795090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00795/00795090.md) → [`007950d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/007950d0.md) FUN_007950d0

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
      "definition_site": "007950ec",
      "incomplete_value": false,
      "site": "007950ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:c68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007950ac",
      "incomplete_value": false,
      "site": "007950ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:868:8"
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
      "007950ec",
      "DATA",
      [
        "storage",
        "00c79868",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007950ec",
      "DATA",
      [
        "storage",
        "00c79c68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007950a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00795/00795090.md#insn-007950a8) · [`007950cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00795/00795090.md#insn-007950cc)
- 新版 `007950e8`（命令位置の公開資料なし） · `0079510c`（命令位置の公開資料なし）

~~~diff
- 007950a8 ["COPY", "tmp:0:8", ["const:868:8"]]
- 007950a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007950a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007950a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007950e8 ["COPY", "tmp:0:8", ["const:c68:8"]]
+ 007950e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007950e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007950e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007950a8 bytes 29a12191
+ 007950e8 bytes 29a13191
- 007950cc ["COPY", "register:0:8", ["register:4048:8"]]
- 007950cc ["INT_ADD", "register:40f0:8", ["const:7950cc:8", "const:4:8"]]
- 007950cc ["CALLIND", null, ["register:0:8"]]
+ 0079510c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0079510c ["INT_ADD", "register:40f0:8", ["const:79510c:8", "const:4:8"]]
+ 0079510c ["CALLIND", null, ["register:0:8"]]
- 007950cc bytes 20013fd6
+ 0079510c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c5e76c5f0946146b865b380d91b1781"></a>

### [`0079518c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00795/0079518c.md) → [`007951cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/007951cc.md) FUN_007951cc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 92.00% / 新版 92.00%

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
      "site": "007951ec",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007951ac",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "site": "007951f8",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007951b8",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "007951ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "007951f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "007951ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007951f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007951ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00795/0079518c.md#insn-007951ac) · [`007951b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00795/0079518c.md#insn-007951b8) · [`007951ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00795/0079518c.md#insn-007951ec)
- 新版 `007951ec`（命令位置の公開資料なし） · `007951f8`（命令位置の公開資料なし） · `0079522c`（命令位置の公開資料なし）

~~~diff
- 007951ac ["INT_ADD", "register:40f0:8", ["const:7951ac:8", "const:4:8"]]
- 007951ac ["CALL", null, ["ram:47acb4:8"]]
+ 007951ec ["INT_ADD", "register:40f0:8", ["const:7951ec:8", "const:4:8"]]
+ 007951ec ["CALL", null, ["ram:47acf4:8"]]
- 007951ac bytes c296f397
+ 007951ec bytes c296f397
- 007951b8 ["INT_ADD", "register:40f0:8", ["const:7951b8:8", "const:4:8"]]
- 007951b8 ["CALL", null, ["ram:47acb4:8"]]
+ 007951f8 ["INT_ADD", "register:40f0:8", ["const:7951f8:8", "const:4:8"]]
+ 007951f8 ["CALL", null, ["ram:47acf4:8"]]
- 007951b8 bytes bf96f397
+ 007951f8 bytes bf96f397
- 007951ec ["INT_ADD", "register:40f0:8", ["const:7951ec:8", "const:4:8"]]
- 007951ec ["CALL", null, ["callee:00459d74:8"]]
+ 0079522c ["INT_ADD", "register:40f0:8", ["const:79522c:8", "const:4:8"]]
+ 0079522c ["CALL", null, ["callee:00459d74:8"]]
- 007951ec bytes d212f397
+ 0079522c bytes d212f397
~~~


<a id="compare-ab08275dea4c1c75a954e33633d094c1"></a>

### [`00795634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00795/00795634.md) → [`00795674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795674.md) FUN_00795674

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00795218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00795/00795218.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`00795258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795258.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "00795680",
      "incomplete_value": false,
      "site": "00795684",
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
    "old": {
      "definition_site": "00795640",
      "incomplete_value": false,
      "site": "00795644",
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
            "const:f0c:8"
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
      "00795680",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00795680",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00795644`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00795/00795634.md#insn-00795644) · [`00795640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00795/00795634.md#insn-00795640)
- 新版 `00795684`（命令位置の公開資料なし） · `00795680`（命令位置の公開資料なし）

~~~diff
- 00795644 ["INT_ADD", "register:40f0:8", ["const:795644:8", "const:4:8"]]
- 00795644 ["CALL", null, ["callee:0043b778:8"]]
+ 00795684 ["INT_ADD", "register:40f0:8", ["const:795684:8", "const:4:8"]]
+ 00795684 ["CALL", null, ["callee:0043b778:8"]]
- 00795644 bytes 3d98f297
+ 00795684 bytes 3d98f297
- 00795640 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00795640 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00795640 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00795640 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00795680 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00795680 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00795680 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00795680 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00795640 bytes 00303c91
+ 00795680 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9525ea56d425dcadf9aaa391abc1b5ee"></a>

### [`00795a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00795/00795a54.md) → [`00795a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795a94.md) _INIT_138

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.57% / 新版 87.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00795b14",
      "incomplete_value": true,
      "site": "00795b30",
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
    "old": {
      "definition_site": "00795ad4",
      "incomplete_value": true,
      "site": "00795af0",
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
                "const:d82:8"
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
      "definition_site": "00795b34",
      "incomplete_value": true,
      "site": "00795b4c",
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
                "const:f62:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00795af4",
      "incomplete_value": true,
      "site": "00795b0c",
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
                "const:e95:8"
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
      "definition_site": "00795b50",
      "incomplete_value": true,
      "site": "00795b6c",
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
                "const:2ac000:8"
              ],
              [
                "leaf",
                "const:5d2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00795b10",
      "incomplete_value": true,
      "site": "00795b2c",
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
                "const:2ac000:8"
              ],
              [
                "leaf",
                "const:592:8"
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
      "00795ad0",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00795af4",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "00795b14",
      "READ",
      [
        "storage",
        "002b8d82",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00795ad0",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00795af4",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00795b14",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00795acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00795/00795a54.md#insn-00795acc) · [`00795aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00795/00795a54.md#insn-00795aec) · [`00795c88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00795/00795a54.md#insn-00795c88)
- 新版 `00795b0c`（命令位置の公開資料なし） · `00795b2c`（命令位置の公開資料なし） · `00795cc8`（命令位置の公開資料なし）

~~~diff
- 00795acc ["COPY", "tmp:0:8", ["const:d82:8"]]
- 00795acc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00795acc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00795acc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00795b0c ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 00795b0c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00795b0c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00795b0c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00795acc bytes 4a093691
+ 00795b0c bytes 4a093791
- 00795aec ["COPY", "tmp:0:8", ["const:e95:8"]]
- 00795aec ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00795aec ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00795aec ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00795b2c ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 00795b2c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00795b2c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00795b2c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00795aec bytes 4a553a91
+ 00795b2c bytes 4a893d91
- 00795c88 ["INT_ADD", "register:40f0:8", ["const:795c88:8", "const:4:8"]]
- 00795c88 ["CALL", null, ["callee:00c57e30:8"]]
+ 00795cc8 ["INT_ADD", "register:40f0:8", ["const:795cc8:8", "const:4:8"]]
+ 00795cc8 ["CALL", null, ["callee:00c57e30:8"]]
- 00795c88 bytes 6a071394
+ 00795cc8 bytes 5a081394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4125bbd4ebc6acfdd407088cfa127d59"></a>

### [`00795de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00795/00795de4.md) → [`00795e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795e24.md) FUN_00795e24

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 22件 [`0059a6c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a6c8.md) [`0059add8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059add8.md) [`005ad7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad7a0.md) [`005ae8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae8a4.md) [`005b1de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1de4.md) · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 22件 [`0059a708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059a708.md) [`0059ae18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059a/0059ae18.md) [`005ad7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ad/005ad7e0.md) [`005ae8e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ae/005ae8e4.md) [`005b1e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1e24.md) · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00795e4c",
      "incomplete_value": true,
      "site": "00795e4c",
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
            "const:ed0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00795e0c",
      "incomplete_value": true,
      "site": "00795e0c",
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
            "const:ad0:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00795e38",
      "incomplete_value": true,
      "site": "00795e38",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00795df8",
      "incomplete_value": true,
      "site": "00795df8",
      "value": [
        "INT_NOTEQUAL",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00795df8"
      ],
      [
        "FALL_THROUGH",
        "00795e38"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00795e38",
      "incomplete_value": true,
      "site": "00795e44",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00795df8",
      "incomplete_value": true,
      "site": "00795e04",
      "value": [
        "INT_NOTEQUAL",
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
      "00795e34",
      "READ",
      [
        "storage",
        "00ca7ad0",
        null,
        "undefined8"
      ]
    ],
    [
      "00795e4c",
      "WRITE",
      [
        "storage",
        "00ca7ad0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00795e34",
      "READ",
      [
        "storage",
        "00ca7ed0",
        null,
        "undefined8"
      ]
    ],
    [
      "00795e4c",
      "WRITE",
      [
        "storage",
        "00ca7ed0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00795e0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00795/00795de4.md#insn-00795e0c) · [`00795df4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00795/00795de4.md#insn-00795df4) · [`00795e00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00795/00795de4.md#insn-00795e00)
- 新版 `00795e4c`（命令位置の公開資料なし） · `00795e34`（命令位置の公開資料なし） · `00795e40`（命令位置の公開資料なし）

~~~diff
- 00795e0c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ad0:8"]]
- 00795e0c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00795e4c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ed0:8"]]
+ 00795e4c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00795e0c bytes 606a05f9
+ 00795e4c bytes 606a07f9
- 00795df4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ad0:8"]]
- 00795df4 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00795e34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ed0:8"]]
+ 00795e34 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00795df4 bytes 606a45f9
+ 00795e34 bytes 606a47f9
- 00795e00 ["INT_ADD", "register:40f0:8", ["const:795e00:8", "const:4:8"]]
- 00795e00 ["CALL", null, ["callee:00c57e90:8"]]
+ 00795e40 ["INT_ADD", "register:40f0:8", ["const:795e40:8", "const:4:8"]]
+ 00795e40 ["CALL", null, ["callee:00c57e90:8"]]
- 00795e00 bytes 24071394
+ 00795e40 bytes 14081394
~~~


<a id="compare-44df40fe44d4979db6e1f1c66df94af1"></a>

### [`00796220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00796/00796220.md) → [`00796260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00796/00796260.md) FUN_00796260

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007960c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00796/007960c4.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`00796104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00796/00796104.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "0079626c",
      "incomplete_value": false,
      "site": "00796270",
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
    "old": {
      "definition_site": "0079622c",
      "incomplete_value": false,
      "site": "00796230",
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
            "const:f0c:8"
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
      "0079626c",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0079626c",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00796230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00796/00796220.md#insn-00796230) · [`0079622c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00796/00796220.md#insn-0079622c)
- 新版 `00796270`（命令位置の公開資料なし） · `0079626c`（命令位置の公開資料なし）

~~~diff
- 00796230 ["INT_ADD", "register:40f0:8", ["const:796230:8", "const:4:8"]]
- 00796230 ["CALL", null, ["callee:0043b778:8"]]
+ 00796270 ["INT_ADD", "register:40f0:8", ["const:796270:8", "const:4:8"]]
+ 00796270 ["CALL", null, ["callee:0043b778:8"]]
- 00796230 bytes 4295f297
+ 00796270 bytes 4295f297
- 0079622c ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0079622c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0079622c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0079622c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0079626c ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 0079626c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0079626c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0079626c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0079622c bytes 00303c91
+ 0079626c bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6056b030f52af5ca25943ef3575973e8"></a>

### [`00796234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00796/00796234.md) → [`00796274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00796/00796274.md) _INIT_139

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 82.49% / 新版 82.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 3件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007962b0",
      "incomplete_value": true,
      "site": "007962cc",
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
    "old": {
      "definition_site": "00796270",
      "incomplete_value": true,
      "site": "0079628c",
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
                "const:ee6:8"
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
      "definition_site": "007962d4",
      "incomplete_value": true,
      "site": "007962f0",
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
    "old": {
      "definition_site": "00796294",
      "incomplete_value": true,
      "site": "007962b0",
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
                "const:ef9:8"
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
      "definition_site": "007962f4",
      "incomplete_value": true,
      "site": "00796310",
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
    "old": {
      "definition_site": "007962b4",
      "incomplete_value": true,
      "site": "007962d0",
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
                "const:d82:8"
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
      "007962b0",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "007962d4",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "007962f4",
      "READ",
      [
        "storage",
        "002b8d82",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007962b0",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "007962d4",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "007962f4",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007962ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00796/00796234.md#insn-007962ac) · [`007962cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00796/00796234.md#insn-007962cc) · [`00796394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00796/00796234.md#insn-00796394)
- 新版 `007962ec`（命令位置の公開資料なし） · `0079630c`（命令位置の公開資料なし） · `007963d4`（命令位置の公開資料なし）

~~~diff
- 007962ac ["COPY", "tmp:0:8", ["const:d82:8"]]
- 007962ac ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007962ac ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007962ac ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 007962ec ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 007962ec ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 007962ec ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 007962ec ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007962ac bytes 4a093691
+ 007962ec bytes 4a093791
- 007962cc ["COPY", "tmp:0:8", ["const:e95:8"]]
- 007962cc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007962cc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007962cc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0079630c ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 0079630c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0079630c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0079630c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007962cc bytes 4a553a91
+ 0079630c bytes 4a893d91
- 00796394 ["INT_ADD", "register:40f0:8", ["const:796394:8", "const:4:8"]]
- 00796394 ["CALL", null, ["callee:0043b7f8:8"]]
+ 007963d4 ["INT_ADD", "register:40f0:8", ["const:7963d4:8", "const:4:8"]]
+ 007963d4 ["CALL", null, ["callee:0043b7f8:8"]]
- 00796394 bytes 0995f297
+ 007963d4 bytes 0995f297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8946da79f2f7bd74c440379ca797cf6"></a>

### [`007965f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00796/007965f4.md) → [`00796634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00796/00796634.md) FUN_00796634

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`007965c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00796/007965c4.md) · 呼出先 11件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`00764344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764344.md) [`00796f8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00796/00796f8c.md)
- 新版 呼出元 1件 [`00796604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00796/00796604.md) · 呼出先 11件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`00764384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764384.md) [`00796fcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00796/00796fcc.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.50% / 新版 98.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007967dc",
      "incomplete_value": false,
      "site": "007967e0",
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
      "definition_site": "0079679c",
      "incomplete_value": false,
      "site": "007967a0",
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00796818",
      "value": [
        "leaf",
        "ram:764384:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007967d8",
      "value": [
        "leaf",
        "ram:764344:8"
      ]
    },
    "ordinal": 8,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0079682c",
      "incomplete_value": false,
      "site": "00796840",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca7000:8"
          ],
          [
            "leaf",
            "const:f08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007967ec",
      "incomplete_value": false,
      "site": "00796800",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca7000:8"
          ],
          [
            "leaf",
            "const:b08:8"
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
      "007967dc",
      "PARAM",
      [
        "storage",
        "002a00f0",
        null,
        "string"
      ]
    ],
    [
      "00796818",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764344"
      ]
    ],
    [
      "0079682c",
      "PARAM",
      [
        "storage",
        "00ca7b08",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "007967dc",
      "PARAM",
      [
        "storage",
        "002a01bd",
        null,
        "string"
      ]
    ],
    [
      "00796818",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764384"
      ]
    ],
    [
      "0079682c",
      "PARAM",
      [
        "storage",
        "00ca7f08",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00796760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00796/007965f4.md#insn-00796760) · [`007967a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00796/007965f4.md#insn-007967a0) · [`007967d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00796/007965f4.md#insn-007967d8)
- 新版 `007967a0`（命令位置の公開資料なし） · `007967e0`（命令位置の公開資料なし） · `00796818`（命令位置の公開資料なし）

~~~diff
- 00796760 ["INT_ADD", "register:40f0:8", ["const:796760:8", "const:4:8"]]
- 00796760 ["CALL", null, ["callee:00c58050:8"]]
+ 007967a0 ["INT_ADD", "register:40f0:8", ["const:7967a0:8", "const:4:8"]]
+ 007967a0 ["CALL", null, ["callee:00c58050:8"]]
- 00796760 bytes 3c051394
+ 007967a0 bytes 2c061394
- 007967a0 ["INT_ADD", "register:40f0:8", ["const:7967a0:8", "const:4:8"]]
- 007967a0 ["CALL", null, ["callee:00442930:8"]]
+ 007967e0 ["INT_ADD", "register:40f0:8", ["const:7967e0:8", "const:4:8"]]
+ 007967e0 ["CALL", null, ["callee:00442930:8"]]
- 007967a0 bytes 54b0f297
+ 007967e0 bytes 54b0f297
- 007967d8 ["INT_ADD", "register:40f0:8", ["const:7967d8:8", "const:4:8"]]
- 007967d8 ["CALL", null, ["ram:764344:8"]]
+ 00796818 ["INT_ADD", "register:40f0:8", ["const:796818:8", "const:4:8"]]
+ 00796818 ["CALL", null, ["ram:764384:8"]]
- 007967d8 bytes db36ff97
+ 00796818 bytes db36ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72ec33a4341bd13b3fd6c670b6816bd7"></a>

### [`00796ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00796/00796ab8.md) → [`00796af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00796/00796af8.md) FUN_00796af8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`007965c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00796/007965c4.md) · 呼出先 7件 [`00784240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00784/00784240.md) [`008783b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/008783b0.md) [`0087925c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/0087925c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md)
- 新版 呼出元 1件 [`00796604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00796/00796604.md) · 呼出先 7件 [`00784280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00784/00784280.md) [`008783f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/008783f0.md) [`0087929c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00879/0087929c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.79% / 新版 88.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 10件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00796b34",
      "incomplete_value": false,
      "site": "00796b3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:398:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00796af4",
      "incomplete_value": false,
      "site": "00796afc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:358:8"
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
      "definition_site": "00796b5c",
      "incomplete_value": false,
      "site": "00796b64",
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
            "const:67:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00796b1c",
      "incomplete_value": false,
      "site": "00796b24",
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
            "const:27:8"
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
      "definition_site": "00796bb8",
      "incomplete_value": false,
      "site": "00796bc0",
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
            "const:4cc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00796b78",
      "incomplete_value": false,
      "site": "00796b80",
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
            "const:3ff:8"
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
      "00796b3c",
      "DATA",
      [
        "storage",
        "002b9358",
        null,
        "string"
      ]
    ],
    [
      "00796b64",
      "DATA",
      [
        "storage",
        "002b4027",
        null,
        "string"
      ]
    ],
    [
      "00796ba8",
      "PARAM",
      [
        "storage",
        "00ca7b08",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00796b3c",
      "DATA",
      [
        "storage",
        "002b9398",
        null,
        "string"
      ]
    ],
    [
      "00796b64",
      "DATA",
      [
        "storage",
        "002b4067",
        null,
        "string"
      ]
    ],
    [
      "00796ba8",
      "PARAM",
      [
        "storage",
        "00ca7f08",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00796b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00796/00796ab8.md#insn-00796b3c) · [`00796b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00796/00796ab8.md#insn-00796b70) · [`00796c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00796/00796ab8.md#insn-00796c1c)
- 新版 `00796b7c`（命令位置の公開資料なし） · `00796bb0`（命令位置の公開資料なし） · `00796c5c`（命令位置の公開資料なし）

~~~diff
- 00796b3c ["INT_ADD", "register:40f0:8", ["const:796b3c:8", "const:4:8"]]
- 00796b3c ["CALL", null, ["callee:00c5a830:8"]]
+ 00796b7c ["INT_ADD", "register:40f0:8", ["const:796b7c:8", "const:4:8"]]
+ 00796b7c ["CALL", null, ["callee:00c5a830:8"]]
- 00796b3c bytes 3d0e1394
+ 00796b7c bytes 2d0f1394
- 00796b70 ["INT_ADD", "register:40f0:8", ["const:796b70:8", "const:4:8"]]
- 00796b70 ["CALL", null, ["callee:00784280:8"]]
+ 00796bb0 ["INT_ADD", "register:40f0:8", ["const:796bb0:8", "const:4:8"]]
+ 00796bb0 ["CALL", null, ["callee:00784280:8"]]
- 00796b70 bytes b4b5ff97
+ 00796bb0 bytes b4b5ff97
- 00796c1c ["INT_ADD", "register:40f0:8", ["const:796c1c:8", "const:4:8"]]
- 00796c1c ["CALL", null, ["callee:00c5a830:8"]]
+ 00796c5c ["INT_ADD", "register:40f0:8", ["const:796c5c:8", "const:4:8"]]
+ 00796c5c ["CALL", null, ["callee:00c5a830:8"]]
- 00796c1c bytes 050e1394
+ 00796c5c bytes f50e1394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af46a3eea5023cafd58707c8c4ba4fe8"></a>

### [`00796f8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00796/00796f8c.md) → [`00796fcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00796/00796fcc.md) FUN_00796fcc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007965f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00796/007965f4.md) · 呼出先 14件 [`004878ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878ec.md) [`00487a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487a24.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md) [`00488618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488618.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md)
- 新版 呼出元 1件 [`00796634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00796/00796634.md) · 呼出先 14件 [`0048792c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048792c.md) [`00487a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487a64.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md) [`00488658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488658.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 90.08% / 新版 90.08%

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
      "definition_site": "00797000",
      "incomplete_value": false,
      "site": "00797008",
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
    "old": {
      "definition_site": "00796fc0",
      "incomplete_value": false,
      "site": "00796fc8",
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
            "const:938:8"
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
      "definition_site": "00797138",
      "incomplete_value": true,
      "site": "0079713c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007970f8",
      "incomplete_value": true,
      "site": "007970fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00797134",
      "incomplete_value": true,
      "site": "00797140",
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
      "definition_site": "007970f4",
      "incomplete_value": true,
      "site": "00797100",
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
      "00797008",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "00797030",
      "PARAM",
      [
        "storage",
        "00ca7af0",
        null,
        null
      ]
    ],
    [
      "007970cc",
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
      "00797008",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "00797030",
      "PARAM",
      [
        "storage",
        "00ca7ef0",
        null,
        null
      ]
    ],
    [
      "007970cc",
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

- 旧版 [`007970bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00796/00796f8c.md#insn-007970bc) · [`00797140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00796/00796f8c.md#insn-00797140) · [`00796fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00796/00796f8c.md#insn-00796fb8)
- 新版 `007970fc`（命令位置の公開資料なし） · `00797180`（命令位置の公開資料なし） · `00796ff8`（命令位置の公開資料なし）

~~~diff
- 007970bc ["INT_ADD", "register:40f0:8", ["const:7970bc:8", "const:4:8"]]
- 007970bc ["CALL", null, ["callee:00c57eb0:8"]]
+ 007970fc ["INT_ADD", "register:40f0:8", ["const:7970fc:8", "const:4:8"]]
+ 007970fc ["CALL", null, ["callee:00c57eb0:8"]]
- 007970bc bytes 7d021394
+ 007970fc bytes 6d031394
- 00797140 ["INT_ADD", "register:40f0:8", ["const:797140:8", "const:4:8"]]
- 00797140 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00797180 ["INT_ADD", "register:40f0:8", ["const:797180:8", "const:4:8"]]
+ 00797180 ["CALL", null, ["callee:00c57fb0:8"]]
- 00797140 bytes 9c021394
+ 00797180 bytes 8c031394
- 00796fb8 ["INT_ADD", "register:40f0:8", ["const:796fb8:8", "const:4:8"]]
- 00796fb8 ["CALL", null, ["callee:00487e20:8"]]
+ 00796ff8 ["INT_ADD", "register:40f0:8", ["const:796ff8:8", "const:4:8"]]
+ 00796ff8 ["CALL", null, ["callee:00487e20:8"]]
- 00796fb8 bytes 8ac3f397
+ 00796ff8 bytes 8ac3f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd594c90ae28afb4ff9b144970b1e43c"></a>

### [`00797254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00797/00797254.md) → [`00797294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00797/00797294.md) _INIT_140

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00bc43c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc43c8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00bc47f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc47f0.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 81.25% / 新版 81.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_destination` 4件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00797334",
      "incomplete_value": true,
      "site": "0079734c",
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
                "live",
                "register:4050:8"
              ],
              [
                "leaf",
                "const:f62:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007972f4",
      "incomplete_value": true,
      "site": "0079730c",
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
                "live",
                "register:4050:8"
              ],
              [
                "leaf",
                "const:e95:8"
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
      "definition_site": "00797350",
      "incomplete_value": true,
      "site": "0079736c",
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
                "const:2ac000:8"
              ],
              [
                "leaf",
                "const:5d2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00797310",
      "incomplete_value": true,
      "site": "0079732c",
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
                "const:2ac000:8"
              ],
              [
                "leaf",
                "const:592:8"
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
      "definition_site": "00797390",
      "incomplete_value": true,
      "site": "007973d4",
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
                "live",
                "register:4048:8"
              ],
              [
                "leaf",
                "const:f09:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00797350",
      "incomplete_value": true,
      "site": "00797394",
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
                "live",
                "register:4048:8"
              ],
              [
                "leaf",
                "const:e3c:8"
              ]
            ]
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
      "007972d0",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "007972f4",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "00797314",
      "READ",
      [
        "storage",
        "002b8d82",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007972d0",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "007972f4",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00797314",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007972cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00797/00797254.md#insn-007972cc) · [`007972ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00797/00797254.md#insn-007972ec) · [`00797474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00797/00797254.md#insn-00797474)
- 新版 `0079730c`（命令位置の公開資料なし） · `0079732c`（命令位置の公開資料なし） · `007974b4`（命令位置の公開資料なし）

~~~diff
- 007972cc ["COPY", "tmp:0:8", ["const:d82:8"]]
- 007972cc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007972cc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007972cc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0079730c ["COPY", "tmp:0:8", ["const:dc2:8"]]
+ 0079730c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0079730c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0079730c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007972cc bytes 4a093691
+ 0079730c bytes 4a093791
- 007972ec ["COPY", "tmp:0:8", ["const:e95:8"]]
- 007972ec ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007972ec ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007972ec ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0079732c ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 0079732c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0079732c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0079732c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007972ec bytes 4a553a91
+ 0079732c bytes 4a893d91
- 00797474 ["COPY", "tmp:0:8", ["const:b90:8"]]
- 00797474 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00797474 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00797474 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 007974b4 ["COPY", "tmp:0:8", ["const:f90:8"]]
+ 007974b4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 007974b4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 007974b4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00797474 bytes 73422e91
+ 007974b4 bytes 73423e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6e4242903bfc83c0898f0dd5bfaeea6"></a>

### [`00797660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00797/00797660.md) → [`007976a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00797/007976a0.md) _INIT_141

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.57% / 新版 87.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007976dc",
      "incomplete_value": true,
      "site": "007976f8",
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
    "old": {
      "definition_site": "0079769c",
      "incomplete_value": true,
      "site": "007976b8",
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
                "const:ee6:8"
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
      "definition_site": "0079775c",
      "incomplete_value": true,
      "site": "00797778",
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
                "const:2ac000:8"
              ],
              [
                "leaf",
                "const:5d2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079771c",
      "incomplete_value": true,
      "site": "00797738",
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
                "const:2ac000:8"
              ],
              [
                "leaf",
                "const:592:8"
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
      "definition_site": "0079777c",
      "incomplete_value": true,
      "site": "00797798",
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
                "const:2a0000:8"
              ],
              [
                "leaf",
                "const:f5d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079773c",
      "incomplete_value": true,
      "site": "00797758",
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
                "const:2a0000:8"
              ],
              [
                "leaf",
                "const:e90:8"
              ]
            ]
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
      "007976dc",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00797700",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "00797720",
      "READ",
      [
        "storage",
        "002b8d82",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007976dc",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00797700",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00797720",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007976f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00797/00797660.md#insn-007976f8) · [`00797894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00797/00797660.md#insn-00797894) · [`0079768c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00797/00797660.md#insn-0079768c)
- 新版 `00797738`（命令位置の公開資料なし） · `007978d4`（命令位置の公開資料なし） · `007976cc`（命令位置の公開資料なし）

~~~diff
- 007976f8 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 007976f8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 007976f8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 007976f8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00797738 ["COPY", "tmp:0:8", ["const:f62:8"]]
+ 00797738 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00797738 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00797738 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 007976f8 bytes 4a553a91
+ 00797738 bytes 4a893d91
- 00797894 ["INT_ADD", "register:40f0:8", ["const:797894:8", "const:4:8"]]
- 00797894 ["CALL", null, ["callee:00c57e30:8"]]
+ 007978d4 ["INT_ADD", "register:40f0:8", ["const:7978d4:8", "const:4:8"]]
+ 007978d4 ["CALL", null, ["callee:00c57e30:8"]]
- 00797894 bytes 67001394
+ 007978d4 bytes 57011394
- 0079768c ["COPY", "tmp:0:8", ["const:b20:8"]]
- 0079768c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0079768c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0079768c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 007976cc ["COPY", "tmp:0:8", ["const:f20:8"]]
+ 007976cc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 007976cc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 007976cc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0079768c bytes 73822c91
+ 007976cc bytes 73823c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d93841a103c8024b63f3b47601a8e296"></a>

### [`00798020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00798/00798020.md) → [`00798060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00798/00798060.md) FUN_00798060

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00a8e3bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a8e/00a8e3bc.md) · 呼出先 10件 [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`0079d3b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d3b8.md) [`0079d3bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d3bc.md) [`007a070c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a0/007a070c.md) [`007a0744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a0/007a0744.md)
- 新版 呼出元 1件 [`00a8e5b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a8e/00a8e5b4.md) · 呼出先 10件 [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`0079d3f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d3f8.md) [`0079d3fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d3fc.md) [`007a074c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a074c.md) [`007a0784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0784.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007980c4",
      "incomplete_value": true,
      "site": "007980d8",
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
      "definition_site": "00798084",
      "incomplete_value": true,
      "site": "00798098",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007980d0",
      "incomplete_value": true,
      "site": "007980e0",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:c1e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00798090",
      "incomplete_value": true,
      "site": "007980a0",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:bde:8"
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
      "definition_site": "007980d0",
      "incomplete_value": true,
      "site": "007980e0",
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
      "definition_site": "00798090",
      "incomplete_value": true,
      "site": "007980a0",
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
      "007980c4",
      "READ",
      [
        "storage",
        "002c3260",
        null,
        null
      ]
    ],
    [
      "007980d0",
      "READ",
      [
        "storage",
        "002aebde",
        null,
        "string"
      ]
    ],
    [
      "007980d0",
      "READ",
      [
        "storage",
        "002aebee",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007980c4",
      "READ",
      [
        "storage",
        "002c32a0",
        null,
        null
      ]
    ],
    [
      "007980d0",
      "READ",
      [
        "storage",
        "002aec1e",
        null,
        "string"
      ]
    ],
    [
      "007980d0",
      "READ",
      [
        "storage",
        "002aec2e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079808c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00798/00798020.md#insn-0079808c) · [`0079804c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00798/00798020.md#insn-0079804c) · [`0079805c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00798/00798020.md#insn-0079805c)
- 新版 `007980cc`（命令位置の公開資料なし） · `0079808c`（命令位置の公開資料なし） · `0079809c`（命令位置の公開資料なし）

~~~diff
- 0079808c ["COPY", "tmp:0:8", ["const:bde:8"]]
- 0079808c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079808c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079808c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007980cc ["COPY", "tmp:0:8", ["const:c1e:8"]]
+ 007980cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007980cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007980cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079808c bytes 08792f91
+ 007980cc bytes 08793091
- 0079804c ["INT_ADD", "register:40f0:8", ["const:79804c:8", "const:4:8"]]
- 0079804c ["CALL", null, ["callee:007a074c:8"]]
+ 0079808c ["INT_ADD", "register:40f0:8", ["const:79808c:8", "const:4:8"]]
+ 0079808c ["CALL", null, ["callee:007a074c:8"]]
- 0079804c bytes b0210094
+ 0079808c bytes b0210094
- 0079805c ["INT_ADD", "register:40f0:8", ["const:79805c:8", "const:4:8"]]
- 0079805c ["CALL", null, ["callee:007a0784:8"]]
+ 0079809c ["INT_ADD", "register:40f0:8", ["const:79809c:8", "const:4:8"]]
+ 0079809c ["CALL", null, ["callee:007a0784:8"]]
- 0079805c bytes ba210094
+ 0079809c bytes ba210094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be6d7169933244130480c675b62be7e7"></a>

### [`007981d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00798/007981d4.md) → [`00798214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00798/00798214.md) FUN_00798214

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00897848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00897/00897848.md) · 呼出先 10件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00540d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540d3c.md) [`007a070c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a0/007a070c.md) [`007a0744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a0/007a0744.md)
- 新版 呼出元 1件 [`0089788c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00897/0089788c.md) · 呼出先 10件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00540d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540d7c.md) [`007a074c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a074c.md) [`007a0784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0784.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.62% / 新版 95.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00798288",
      "incomplete_value": true,
      "site": "00798298",
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
                "const:6d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00798248",
      "incomplete_value": true,
      "site": "00798258",
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
                "const:2d:8"
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
      "definition_site": "0079829c",
      "incomplete_value": true,
      "site": "0079829c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0079825c",
      "incomplete_value": true,
      "site": "0079825c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00798290",
      "incomplete_value": true,
      "site": "007982a0",
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
      "definition_site": "00798250",
      "incomplete_value": true,
      "site": "00798260",
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
      "00798288",
      "READ",
      [
        "storage",
        "002b402d",
        null,
        "string"
      ]
    ],
    [
      "0079828c",
      "READ",
      [
        "storage",
        "002b403c",
        null,
        "string"
      ]
    ],
    [
      "00798290",
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
      "00798288",
      "READ",
      [
        "storage",
        "002b406d",
        null,
        "string"
      ]
    ],
    [
      "0079828c",
      "READ",
      [
        "storage",
        "002b407c",
        null,
        "string"
      ]
    ],
    [
      "00798290",
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

- 旧版 [`00798220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00798/007981d4.md#insn-00798220) · [`00798398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00798/007981d4.md#insn-00798398) · [`0079864c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00798/007981d4.md#insn-0079864c)
- 新版 `00798260`（命令位置の公開資料なし） · `007983d8`（命令位置の公開資料なし） · `0079868c`（命令位置の公開資料なし）

~~~diff
- 00798220 ["INT_ADD", "register:40f0:8", ["const:798220:8", "const:4:8"]]
- 00798220 ["CALL", null, ["callee:007a074c:8"]]
+ 00798260 ["INT_ADD", "register:40f0:8", ["const:798260:8", "const:4:8"]]
+ 00798260 ["CALL", null, ["callee:007a074c:8"]]
- 00798220 bytes 3b210094
+ 00798260 bytes 3b210094
- 00798398 ["INT_ADD", "register:40f0:8", ["const:798398:8", "const:4:8"]]
- 00798398 ["CALL", null, ["callee:00540d7c:8"]]
+ 007983d8 ["INT_ADD", "register:40f0:8", ["const:7983d8:8", "const:4:8"]]
+ 007983d8 ["CALL", null, ["callee:00540d7c:8"]]
- 00798398 bytes 69a2f697
+ 007983d8 bytes 69a2f697
- 0079864c ["INT_ADD", "register:40f0:8", ["const:79864c:8", "const:4:8"]]
- 0079864c ["CALL", null, ["callee:00540d7c:8"]]
+ 0079868c ["INT_ADD", "register:40f0:8", ["const:79868c:8", "const:4:8"]]
+ 0079868c ["CALL", null, ["callee:00540d7c:8"]]
- 0079864c bytes bca1f697
+ 0079868c bytes bca1f697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1447c675fc77569949a3153702f31952"></a>

### [`00798e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00798/00798e60.md) → [`00798ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00798/00798ea0.md) FUN_00798ea0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00897848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00897/00897848.md) · 呼出先 31件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0045175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/0045175c.md) [`00451998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451998.md) [`004593b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/004593b0.md) [`004597ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/004597ec.md)
- 新版 呼出元 1件 [`0089788c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00897/0089788c.md) · 呼出先 31件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0045179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md) [`004519d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004519d8.md) [`004593f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004593f0.md) [`0045982c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/0045982c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.80% / 新版 91.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 19件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00798ee4",
      "incomplete_value": false,
      "site": "00798ef0",
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
    "old": {
      "definition_site": "00798ea4",
      "incomplete_value": false,
      "site": "00798eb0",
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
            "const:6e0:8"
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
      "definition_site": "00798f20",
      "incomplete_value": true,
      "site": "00798f2c",
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
                "const:e00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00798ee0",
      "incomplete_value": true,
      "site": "00798eec",
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
                "const:dc0:8"
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
      "definition_site": "00798f1c",
      "incomplete_value": true,
      "site": "00798f30",
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
                "const:2a6000:8"
              ],
              [
                "leaf",
                "const:ab0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00798edc",
      "incomplete_value": true,
      "site": "00798ef0",
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
                "const:2a6000:8"
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
      "00798ef0",
      "DATA",
      [
        "storage",
        "00c636e0",
        null,
        "pointer"
      ]
    ],
    [
      "00798f1c",
      "READ",
      [
        "storage",
        "002a69d4",
        null,
        "string"
      ]
    ],
    [
      "00798f1c",
      "READ",
      [
        "storage",
        "002a69e4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00798ef0",
      "DATA",
      [
        "storage",
        "00c63ae0",
        null,
        "pointer"
      ]
    ],
    [
      "00798f1c",
      "READ",
      [
        "storage",
        "002a6ab0",
        null,
        "string"
      ]
    ],
    [
      "00798f1c",
      "READ",
      [
        "storage",
        "002a6ac0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00799100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00798/00798e60.md#insn-00799100) · [`00799390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00798/00798e60.md#insn-00799390)
- 新版 `00798eec`（命令位置の公開資料なし） · `00799140`（命令位置の公開資料なし） · `007993d0`（命令位置の公開資料なし）

~~~diff
+ 00798eec ["COPY", "register:4040:8", ["register:4000:8"]]
+ 00798eec bytes e80300aa
- 00799100 ["INT_ADD", "register:40f0:8", ["const:799100:8", "const:4:8"]]
- 00799100 ["CALL", null, ["callee:00c57e90:8"]]
+ 00799140 ["INT_ADD", "register:40f0:8", ["const:799140:8", "const:4:8"]]
+ 00799140 ["CALL", null, ["callee:00c57e90:8"]]
- 00799100 bytes 64fa1294
+ 00799140 bytes 54fb1294
- 00799390 ["INT_ADD", "register:40f0:8", ["const:799390:8", "const:4:8"]]
- 00799390 ["CALL", null, ["callee:00597a74:8"]]
+ 007993d0 ["INT_ADD", "register:40f0:8", ["const:7993d0:8", "const:4:8"]]
+ 007993d0 ["CALL", null, ["callee:00597a74:8"]]
- 00799390 bytes a9f9f797
+ 007993d0 bytes a9f9f797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d1e10fbb624e33ffeb95beb66bf56cd"></a>

### [`00799c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00799/00799c54.md) → [`00799c94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00799/00799c94.md) FUN_00799c94

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0079b984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079b/0079b984.md) · 呼出先 15件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00540d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540d3c.md) [`005a4260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4260.md)
- 新版 呼出元 1件 [`0079b9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079b/0079b9c4.md) · 呼出先 15件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00540d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540d7c.md) [`005a42a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005a4/005a42a0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.19% / 新版 98.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00799e70",
      "value": [
        "leaf",
        "ram:71bed8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00799e30",
      "value": [
        "leaf",
        "ram:71be98:8"
      ]
    },
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00799fb4",
      "value": [
        "leaf",
        "ram:71bed8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00799f74",
      "value": [
        "leaf",
        "ram:71be98:8"
      ]
    },
    "ordinal": 8,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0079a4e8",
      "incomplete_value": false,
      "site": "0079a4ec",
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
      "definition_site": "0079a4a8",
      "incomplete_value": false,
      "site": "0079a4ac",
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
    "ordinal": 32,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00799e70",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071be98"
      ]
    ],
    [
      "00799fb4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071be98"
      ]
    ],
    [
      "0079a4c8",
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
      "00799e70",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bed8"
      ]
    ],
    [
      "00799fb4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bed8"
      ]
    ],
    [
      "0079a4c8",
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

- 旧版 [`00799e30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00799/00799c54.md#insn-00799e30) · [`00799f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00799/00799c54.md#insn-00799f74) · [`0079a48c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00799/00799c54.md#insn-0079a48c)
- 新版 `00799e70`（命令位置の公開資料なし） · `00799fb4`（命令位置の公開資料なし） · `0079a4cc`（命令位置の公開資料なし）

~~~diff
- 00799e30 ["INT_ADD", "register:40f0:8", ["const:799e30:8", "const:4:8"]]
- 00799e30 ["CALL", null, ["ram:71be98:8"]]
+ 00799e70 ["INT_ADD", "register:40f0:8", ["const:799e70:8", "const:4:8"]]
+ 00799e70 ["CALL", null, ["ram:71bed8:8"]]
- 00799e30 bytes 1a08fe97
+ 00799e70 bytes 1a08fe97
- 00799f74 ["INT_ADD", "register:40f0:8", ["const:799f74:8", "const:4:8"]]
- 00799f74 ["CALL", null, ["ram:71be98:8"]]
+ 00799fb4 ["INT_ADD", "register:40f0:8", ["const:799fb4:8", "const:4:8"]]
+ 00799fb4 ["CALL", null, ["ram:71bed8:8"]]
- 00799f74 bytes c907fe97
+ 00799fb4 bytes c907fe97
- 0079a48c ["INT_ADD", "register:40f0:8", ["const:79a48c:8", "const:4:8"]]
- 0079a48c ["CALL", null, ["callee:00442930:8"]]
+ 0079a4cc ["INT_ADD", "register:40f0:8", ["const:79a4cc:8", "const:4:8"]]
+ 0079a4cc ["CALL", null, ["callee:00442930:8"]]
- 0079a48c bytes 19a1f297
+ 0079a4cc bytes 19a1f297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03d32529605e3f8c2d0b4a0d7257bac8"></a>

### [`0079a800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079a/0079a800.md) → [`0079a840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079a/0079a840.md) FUN_0079a840

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`0088c0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c0e0.md) [`00a8a220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a8a/00a8a220.md) · 呼出先 6件 [`0079a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079a/0079a950.md) [`0079d81c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d81c.md) [`0079d820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d820.md) [`0079d8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d8a4.md) [`0079d8a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d8a8.md)
- 新版 呼出元 2件 [`0088c120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c120.md) [`00a8d008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a8d/00a8d008.md) · 呼出先 6件 [`0079a990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079a/0079a990.md) [`0079d85c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d85c.md) [`0079d860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d860.md) [`0079d8e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d8e4.md) [`0079d8e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d8e8.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.34% / 新版 94.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0079a868",
      "incomplete_value": false,
      "site": "0079a868",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:d68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079a828",
      "incomplete_value": false,
      "site": "0079a828",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:968:8"
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
      "0079a868",
      "DATA",
      [
        "storage",
        "00c79968",
        null,
        "undefined *"
      ]
    ],
    [
      "0079a880",
      "DATA",
      [
        "storage",
        "00c799e8",
        null,
        "undefined *"
      ]
    ],
    [
      "0079a8b8",
      "READ",
      [
        "storage",
        "00c79a08",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0079a868",
      "DATA",
      [
        "storage",
        "00c79d68",
        null,
        "undefined *"
      ]
    ],
    [
      "0079a880",
      "DATA",
      [
        "storage",
        "00c79de8",
        null,
        "undefined *"
      ]
    ],
    [
      "0079a8b8",
      "READ",
      [
        "storage",
        "00c79e08",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079a824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079a/0079a800.md#insn-0079a824) · [`0079a838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079a/0079a800.md#insn-0079a838) · [`0079a850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079a/0079a800.md#insn-0079a850)
- 新版 `0079a864`（命令位置の公開資料なし） · `0079a878`（命令位置の公開資料なし） · `0079a890`（命令位置の公開資料なし）

~~~diff
- 0079a824 ["COPY", "tmp:0:8", ["const:968:8"]]
- 0079a824 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079a824 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079a824 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079a864 ["COPY", "tmp:0:8", ["const:d68:8"]]
+ 0079a864 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079a864 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079a864 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079a824 bytes 08a12591
+ 0079a864 bytes 08a13591
- 0079a838 ["COPY", "tmp:0:8", ["const:9e8:8"]]
- 0079a838 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079a838 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079a838 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079a878 ["COPY", "tmp:0:8", ["const:de8:8"]]
+ 0079a878 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079a878 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079a878 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079a838 bytes 08a12791
+ 0079a878 bytes 08a13791
- 0079a850 ["INT_ADD", "register:40f0:8", ["const:79a850:8", "const:4:8"]]
- 0079a850 ["CALL", null, ["callee:0079a990:8"]]
+ 0079a890 ["INT_ADD", "register:40f0:8", ["const:79a890:8", "const:4:8"]]
+ 0079a890 ["CALL", null, ["callee:0079a990:8"]]
- 0079a850 bytes 40000094
+ 0079a890 bytes 40000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f0eb7e6f34aecfaba984e1b8b73e57c"></a>

### [`0079a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079a/0079a950.md) → [`0079a990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079a/0079a990.md) FUN_0079a990

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0079a800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079a/0079a800.md) · 呼出先 14件 [`00598af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598af4.md) [`00598cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598cb4.md) [`0059b8c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059b/0059b8c8.md) [`00795de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00795/00795de4.md) [`00795e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00795/00795e1c.md)
- 新版 呼出元 1件 [`0079a840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079a/0079a840.md) · 呼出先 14件 [`00598b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598b34.md) [`00598cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00598/00598cf4.md) [`0059b908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0059b/0059b908.md) [`00795e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795e24.md) [`00795e5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00795/00795e5c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.45% / 新版 97.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0079aa1c",
      "incomplete_value": false,
      "site": "0079aa20",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:a10:8"
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
      "definition_site": "0079a9dc",
      "incomplete_value": false,
      "site": "0079a9e0",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:610:8"
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
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0079ac70",
      "incomplete_value": false,
      "site": "0079ac70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:288:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079ac30",
      "incomplete_value": false,
      "site": "0079ac30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:e88:8"
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
      "0079a9f0",
      "DATA",
      [
        "storage",
        "00c6e2b8",
        null,
        "undefined *"
      ]
    ],
    [
      "0079aa20",
      "DATA",
      [
        "storage",
        "00c6d620",
        null,
        "undefined *"
      ]
    ],
    [
      "0079aaf0",
      "DATA",
      [
        "storage",
        "00c79e08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079a9f0",
      "DATA",
      [
        "storage",
        "00c6e6b8",
        null,
        "undefined *"
      ]
    ],
    [
      "0079aa20",
      "DATA",
      [
        "storage",
        "00c6da20",
        null,
        "undefined *"
      ]
    ],
    [
      "0079aaf0",
      "DATA",
      [
        "storage",
        "00c7a208",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079a984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079a/0079a950.md#insn-0079a984) · [`0079a99c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079a/0079a950.md#insn-0079a99c) · [`0079a9a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079a/0079a950.md#insn-0079a9a4)
- 新版 `0079a9c4`（命令位置の公開資料なし） · `0079a9dc`（命令位置の公開資料なし） · `0079a9e4`（命令位置の公開資料なし）

~~~diff
- 0079a984 ["INT_ADD", "register:40f0:8", ["const:79a984:8", "const:4:8"]]
- 0079a984 ["CALL", null, ["callee:00c57e90:8"]]
+ 0079a9c4 ["INT_ADD", "register:40f0:8", ["const:79a9c4:8", "const:4:8"]]
+ 0079a9c4 ["CALL", null, ["callee:00c57e90:8"]]
- 0079a984 bytes 43f41294
+ 0079a9c4 bytes 33f51294
- 0079a99c ["INT_ADD", "register:40f0:8", ["const:79a99c:8", "const:4:8"]]
- 0079a99c ["CALL", null, ["callee:0059b908:8"]]
+ 0079a9dc ["INT_ADD", "register:40f0:8", ["const:79a9dc:8", "const:4:8"]]
+ 0079a9dc ["CALL", null, ["callee:0059b908:8"]]
- 0079a99c bytes cb03f897
+ 0079a9dc bytes cb03f897
- 0079a9a4 ["COPY", "tmp:0:8", ["const:2a8:8"]]
- 0079a9a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079a9a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079a9a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079a9e4 ["COPY", "tmp:0:8", ["const:6a8:8"]]
+ 0079a9e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079a9e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079a9e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079a9a4 bytes 08a10a91
+ 0079a9e4 bytes 08a11a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f6781053d5d84d6ed32186d3693fe5f"></a>

### [`0079b0d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079b/0079b0d0.md) → [`0079b110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079b/0079b110.md) FUN_0079b110

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0079af48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079a/0079af48.md) · 呼出先 9件 [`0044f8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f8a0.md) [`00452c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00452/00452c14.md) [`00764344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764344.md) [`00768564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/00768564.md) [`0079d99c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d99c.md)
- 新版 呼出元 1件 [`0079af88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079a/0079af88.md) · 呼出先 9件 [`0044f8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f8e0.md) [`00452c54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00452/00452c54.md) [`00764384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764384.md) [`007685a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00768/007685a4.md) [`0079d9dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d9dc.md)

変更の種類 call, call_count, call_target, constant, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 90.38% / 新版 90.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0079b154",
      "incomplete_value": false,
      "site": "0079b154",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:e68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079b114",
      "incomplete_value": false,
      "site": "0079b114",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0079b138",
      "value": [
        "leaf",
        "ram:764384:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0079b0f8",
      "value": [
        "leaf",
        "ram:764344:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "0079b0fc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0079b138",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764344"
      ]
    ],
    [
      "unmatched:0079b0fc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514f8"
      ]
    ],
    [
      "0079b144",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768564"
      ]
    ]
  ],
  "added": [
    [
      "0079b138",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764384"
      ]
    ],
    [
      "0079b13c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514f8"
      ]
    ],
    [
      "0079b144",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007685a4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079b0f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079b/0079b0d0.md#insn-0079b0f8) · [`0079b0fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079b/0079b0d0.md#insn-0079b0fc) · [`0079b104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079b/0079b0d0.md#insn-0079b104)
- 新版 `0079b138`（命令位置の公開資料なし） · `0079b144`（命令位置の公開資料なし）

~~~diff
- 0079b0f8 ["INT_ADD", "register:40f0:8", ["const:79b0f8:8", "const:4:8"]]
- 0079b0f8 ["CALL", null, ["ram:764344:8"]]
+ 0079b138 ["INT_ADD", "register:40f0:8", ["const:79b138:8", "const:4:8"]]
+ 0079b138 ["CALL", null, ["ram:764384:8"]]
- 0079b0f8 bytes 9324ff97
+ 0079b138 bytes 9324ff97
- 0079b0fc ["INT_ADD", "register:40f0:8", ["const:79b0fc:8", "const:4:8"]]
- 0079b0fc ["CALL", null, ["callee:008514f8:8"]]
- 0079b0fc bytes efd80294
- 0079b104 ["INT_ADD", "register:40f0:8", ["const:79b104:8", "const:4:8"]]
- 0079b104 ["CALL", null, ["ram:768564:8"]]
+ 0079b144 ["INT_ADD", "register:40f0:8", ["const:79b144:8", "const:4:8"]]
+ 0079b144 ["CALL", null, ["ram:7685a4:8"]]
- 0079b104 bytes 1835ff97
+ 0079b144 bytes 1835ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90dee3e49aa6411fd5dd15c39f1e35a0"></a>

### [`0079b240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079b/0079b240.md) → [`0079b280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079b/0079b280.md) FUN_0079b280

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0079d9a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079d9a4.md) · 呼出先 6件 [`0079b38c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079b/0079b38c.md) [`0079dacc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079dacc.md) [`0079dad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079dad0.md) [`0079db50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079db50.md) [`0079db54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079d/0079db54.md)
- 新版 呼出元 1件 [`0079d9e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079d9e4.md) · 呼出先 6件 [`0079b3cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079b/0079b3cc.md) [`0079db0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079db0c.md) [`0079db10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079db10.md) [`0079db90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079db90.md) [`0079db94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0079d/0079db94.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0079b2a8",
      "incomplete_value": false,
      "site": "0079b2a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079b268",
      "incomplete_value": false,
      "site": "0079b268",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:ae8:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0079b2bc",
      "incomplete_value": false,
      "site": "0079b2bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:f78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079b27c",
      "incomplete_value": false,
      "site": "0079b27c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:b78:8"
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
      "0079b2a8",
      "DATA",
      [
        "storage",
        "00c79ae8",
        null,
        "undefined *"
      ]
    ],
    [
      "0079b2bc",
      "DATA",
      [
        "storage",
        "00c79b78",
        null,
        "undefined *"
      ]
    ],
    [
      "0079b2f4",
      "READ",
      [
        "storage",
        "00c79b98",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0079b2a8",
      "DATA",
      [
        "storage",
        "00c79ee8",
        null,
        "undefined *"
      ]
    ],
    [
      "0079b2bc",
      "DATA",
      [
        "storage",
        "00c79f78",
        null,
        "undefined *"
      ]
    ],
    [
      "0079b2f4",
      "READ",
      [
        "storage",
        "00c79f98",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079b264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079b/0079b240.md#insn-0079b264) · [`0079b278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079b/0079b240.md#insn-0079b278) · [`0079b28c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079b/0079b240.md#insn-0079b28c)
- 新版 `0079b2a4`（命令位置の公開資料なし） · `0079b2b8`（命令位置の公開資料なし） · `0079b2cc`（命令位置の公開資料なし）

~~~diff
- 0079b264 ["COPY", "tmp:0:8", ["const:ae8:8"]]
- 0079b264 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079b264 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079b264 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079b2a4 ["COPY", "tmp:0:8", ["const:ee8:8"]]
+ 0079b2a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079b2a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079b2a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079b264 bytes 08a12b91
+ 0079b2a4 bytes 08a13b91
- 0079b278 ["COPY", "tmp:0:8", ["const:b78:8"]]
- 0079b278 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079b278 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079b278 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079b2b8 ["COPY", "tmp:0:8", ["const:f78:8"]]
+ 0079b2b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079b2b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079b2b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079b278 bytes 08e12d91
+ 0079b2b8 bytes 08e13d91
- 0079b28c ["INT_ADD", "register:40f0:8", ["const:79b28c:8", "const:4:8"]]
- 0079b28c ["CALL", null, ["callee:0079b3cc:8"]]
+ 0079b2cc ["INT_ADD", "register:40f0:8", ["const:79b2cc:8", "const:4:8"]]
+ 0079b2cc ["CALL", null, ["callee:0079b3cc:8"]]
- 0079b28c bytes 40000094
+ 0079b2cc bytes 40000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

