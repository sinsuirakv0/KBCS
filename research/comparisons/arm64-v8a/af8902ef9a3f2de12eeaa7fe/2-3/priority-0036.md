# v16.0.0 → v16.0.1 · 最優先の変更候補 (36)

[一覧の目次](README.md)

<a id="compare-62c832a33c510219cf1996a1e379c414"></a>

### [`0075b984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075b/0075b984.md) → [`0075b9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075b/0075b9c4.md) FUN_0075b9c4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0075d71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075d/0075d71c.md) · 呼出先 32件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`00604d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00604/00604d50.md) [`0071be98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071be98.md) [`0071c420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071c/0071c420.md)
- 新版 呼出元 1件 [`0075d75c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075d/0075d75c.md) · 呼出先 32件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`00604d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00604/00604d90.md) [`0071bed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071b/0071bed8.md) [`0071c460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071c/0071c460.md)

変更の種類 call, call_target, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 97.43% / 新版 97.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件, `store_destination` 2件, `store_value` 13件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0075badc",
      "incomplete_value": false,
      "site": "0075bae4",
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
            "const:af4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075ba9c",
      "incomplete_value": false,
      "site": "0075baa4",
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
            "const:ab4:8"
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0075bb04",
      "incomplete_value": false,
      "site": "0075bb10",
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
            "const:eed:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075bac4",
      "incomplete_value": false,
      "site": "0075bad0",
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
            "const:ead:8"
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
      "definition_site": "0075bb34",
      "incomplete_value": false,
      "site": "0075bb3c",
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
            "const:e48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075baf4",
      "incomplete_value": false,
      "site": "0075bafc",
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
            "const:e08:8"
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
      "0075ba1c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071d094"
      ]
    ],
    [
      "0075ba44",
      "DATA",
      [
        "storage",
        "003965b0",
        null,
        "qword"
      ]
    ],
    [
      "0075ba48",
      "DATA",
      [
        "storage",
        "0039b194",
        "fde_0039b194",
        "dword"
      ]
    ]
  ],
  "added": [
    [
      "0075ba1c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071d0d4"
      ]
    ],
    [
      "0075ba44",
      "DATA",
      [
        "storage",
        "003965b0",
        null,
        "byte[23]"
      ]
    ],
    [
      "0075ba48",
      "DATA",
      [
        "storage",
        "0039b194",
        null,
        "qword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075b9dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075b/0075b984.md#insn-0075b9dc) · [`0075ba0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075b/0075b984.md#insn-0075ba0c) · [`0075ba8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075b/0075b984.md#insn-0075ba8c)
- 新版 `0075ba1c`（命令位置の公開資料なし） · `0075ba4c`（命令位置の公開資料なし） · `0075bacc`（命令位置の公開資料なし）

~~~diff
- 0075b9dc ["INT_ADD", "register:40f0:8", ["const:75b9dc:8", "const:4:8"]]
- 0075b9dc ["CALL", null, ["ram:71d094:8"]]
+ 0075ba1c ["INT_ADD", "register:40f0:8", ["const:75ba1c:8", "const:4:8"]]
+ 0075ba1c ["CALL", null, ["ram:71d0d4:8"]]
- 0075b9dc bytes ae05ff97
+ 0075ba1c bytes ae05ff97
- 0075ba0c ["INT_ADD", "register:40f0:8", ["const:75ba0c:8", "const:4:8"]]
- 0075ba0c ["CALL", null, ["ram:71be98:8"]]
+ 0075ba4c ["INT_ADD", "register:40f0:8", ["const:75ba4c:8", "const:4:8"]]
+ 0075ba4c ["CALL", null, ["ram:71bed8:8"]]
- 0075ba0c bytes 2301ff97
+ 0075ba4c bytes 2301ff97
- 0075ba8c ["INT_ADD", "register:40f0:8", ["const:75ba8c:8", "const:4:8"]]
- 0075ba8c ["CALL", null, ["ram:71c420:8"]]
+ 0075bacc ["INT_ADD", "register:40f0:8", ["const:75bacc:8", "const:4:8"]]
+ 0075bacc ["CALL", null, ["ram:71c460:8"]]
- 0075ba8c bytes 6502ff97
+ 0075bacc bytes 6502ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e387a645cb32b0333679c26076bce51"></a>

### [`0075d71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075d/0075d71c.md) → [`0075d75c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075d/0075d75c.md) FUN_0075d75c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`0060e084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0060e/0060e084.md) [`006bbc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bb/006bbc58.md) [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) [`007efc68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ef/007efc68.md) · 呼出先 42件 [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`0053b73c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053b73c.md) [`0059761c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/0059761c.md) [`005976a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005976a8.md) [`00597738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597738.md)
- 新版 呼出元 4件 [`0060e0c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0060e/0060e0c4.md) [`006bbc98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006bb/006bbc98.md) [`0075eb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075eb80.md) [`007efca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007efca8.md) · 呼出先 42件 [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`0053b77c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0053b/0053b77c.md) [`0059765c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059765c.md) [`005976e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/005976e8.md) [`00597778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597778.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.50% / 新版 98.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0075d930",
      "incomplete_value": false,
      "site": "0075d930",
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
            "const:a67:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075d8f0",
      "incomplete_value": false,
      "site": "0075d8f0",
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
            "const:a27:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0075d994",
      "incomplete_value": false,
      "site": "0075d994",
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
            "const:443:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075d954",
      "incomplete_value": false,
      "site": "0075d954",
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
            "const:376:8"
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0075dadc",
      "incomplete_value": false,
      "site": "0075dadc",
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
            "const:a67:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075da9c",
      "incomplete_value": false,
      "site": "0075da9c",
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
            "const:a27:8"
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
      "0075d7b4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65bf4"
      ]
    ],
    [
      "0075d930",
      "DATA",
      [
        "storage",
        "002ada27",
        null,
        null
      ]
    ],
    [
      "0075d994",
      "DATA",
      [
        "storage",
        "002a1376",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0075d7b4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65dec"
      ]
    ],
    [
      "0075d930",
      "DATA",
      [
        "storage",
        "002ada67",
        null,
        null
      ]
    ],
    [
      "0075d994",
      "DATA",
      [
        "storage",
        "002a1443",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075d774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075d/0075d71c.md#insn-0075d774) · [`0075d7b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075d/0075d71c.md#insn-0075d7b4) · [`0075d8b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075d/0075d71c.md#insn-0075d8b0)
- 新版 `0075d7b4`（命令位置の公開資料なし） · `0075d7f4`（命令位置の公開資料なし） · `0075d8f0`（命令位置の公開資料なし）

~~~diff
- 0075d774 ["INT_ADD", "register:40f0:8", ["const:75d774:8", "const:4:8"]]
- 0075d774 ["CALL", null, ["ram:a65bf4:8"]]
+ 0075d7b4 ["INT_ADD", "register:40f0:8", ["const:75d7b4:8", "const:4:8"]]
+ 0075d7b4 ["CALL", null, ["ram:a65dec:8"]]
- 0075d774 bytes 20210c94
+ 0075d7b4 bytes 8e210c94
- 0075d7b4 ["INT_ADD", "register:40f0:8", ["const:75d7b4:8", "const:4:8"]]
- 0075d7b4 ["CALL", null, ["callee:00597778:8"]]
+ 0075d7f4 ["INT_ADD", "register:40f0:8", ["const:75d7f4:8", "const:4:8"]]
+ 0075d7f4 ["CALL", null, ["callee:00597778:8"]]
- 0075d7b4 bytes e1e7f897
+ 0075d7f4 bytes e1e7f897
- 0075d8b0 ["INT_ADD", "register:40f0:8", ["const:75d8b0:8", "const:4:8"]]
- 0075d8b0 ["CALL", null, ["callee:00a35b98:8"]]
+ 0075d8f0 ["INT_ADD", "register:40f0:8", ["const:75d8f0:8", "const:4:8"]]
+ 0075d8f0 ["CALL", null, ["callee:00a35b98:8"]]
- 0075d8b0 bytes 3c600b94
+ 0075d8f0 bytes aa600b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-879e1a06c3d0d841d8a517b5df1426cb"></a>

### [`0075e548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075e548.md) → [`0075e588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075e588.md) FUN_0075e588

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0075d71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075d/0075d71c.md) [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 14件 [`0044ea60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044ea60.md) [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`0059761c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/0059761c.md)
- 新版 呼出元 2件 [`0075d75c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075d/0075d75c.md) [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) · 呼出先 14件 [`0044eaa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044eaa0.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`0059765c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059765c.md)

変更の種類 call, call_target, constant, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 86.01% / 新版 86.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 3件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0075e5d4",
      "incomplete_value": true,
      "site": "0075e5dc",
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
                "const:a50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075e594",
      "incomplete_value": true,
      "site": "0075e59c",
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
                "const:a10:8"
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
      "definition_site": "0075e5d0",
      "incomplete_value": true,
      "site": "0075e5e0",
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
                "const:80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075e590",
      "incomplete_value": true,
      "site": "0075e5a0",
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
                "const:80:8"
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
      "definition_site": "0075e5d0",
      "incomplete_value": true,
      "site": "0075e5e0",
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
      "definition_site": "0075e590",
      "incomplete_value": true,
      "site": "0075e5a0",
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
      "0075e5d0",
      "READ",
      [
        "storage",
        "002b3fbb",
        null,
        "string"
      ]
    ],
    [
      "0075e5d0",
      "READ",
      [
        "storage",
        "002b3fcb",
        null,
        "string"
      ]
    ],
    [
      "0075e5d4",
      "READ",
      [
        "storage",
        "002c2a10",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0075e5d0",
      "READ",
      [
        "storage",
        "002b3ffb",
        null,
        "string"
      ]
    ],
    [
      "0075e5d0",
      "READ",
      [
        "storage",
        "002b400b",
        null,
        "string"
      ]
    ],
    [
      "0075e5d4",
      "READ",
      [
        "storage",
        "002c2a50",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075e5ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075e548.md#insn-0075e5ac) · [`0075e5b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075e548.md#insn-0075e5b4) · [`0075e5bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075e548.md#insn-0075e5bc)

~~~diff
- 0075e5ac ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:9d:8"]]
- 0075e5ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 0075e5ac bytes 00d0893c
- 0075e5b4 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:40:8"]]
- 0075e5b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5020:16"]]
- 0075e5b4 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 0075e5b4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5000:16"]]
- 0075e5b4 bytes 010002ad
- 0075e5bc ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:60:8"]]
- 0075e5bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 0075e5bc ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 0075e5bc ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5040:16"]]
- 0075e5bc bytes 000803ad
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-080343ee0a4e7fddc6686e22f5502182"></a>

### [`0075ea04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075ea04.md) → [`0075ea44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075ea44.md) FUN_0075ea44

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 6件 [`00728ca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00728/00728ca8.md) [`00728dac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00728/00728dac.md) [`00728fac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00728/00728fac.md) [`007290c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00729/007290c8.md) [`00800338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/00800338.md)
- 新版 呼出元 1件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) · 呼出先 6件 [`00728ce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00728/00728ce8.md) [`00728dec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00728/00728dec.md) [`00728fec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00728/00728fec.md) [`00729108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00729/00729108.md) [`00800378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/00800378.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.20% / 新版 96.20%

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
      "site": "0075ea8c",
      "value": [
        "leaf",
        "ram:728ce8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0075ea4c",
      "value": [
        "leaf",
        "ram:728ca8:8"
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
      "site": "0075eaa0",
      "value": [
        "leaf",
        "ram:728dec:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0075ea60",
      "value": [
        "leaf",
        "ram:728dac:8"
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
      "site": "0075eac0",
      "value": [
        "leaf",
        "ram:728ce8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0075ea80",
      "value": [
        "leaf",
        "ram:728ca8:8"
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
      "0075ea84",
      "DATA",
      [
        "storage",
        "0034733c",
        null,
        "qword"
      ]
    ],
    [
      "0075ea8c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00728ca8"
      ]
    ],
    [
      "0075eaa0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00728dac"
      ]
    ]
  ],
  "added": [
    [
      "0075ea84",
      "DATA",
      [
        "storage",
        "0034733c",
        null,
        "byte[27]"
      ]
    ],
    [
      "0075ea8c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00728ce8"
      ]
    ],
    [
      "0075eaa0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00728dec"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075ea4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075ea04.md#insn-0075ea4c) · [`0075ea60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075ea04.md#insn-0075ea60) · [`0075ea80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075ea04.md#insn-0075ea80)
- 新版 `0075ea8c`（命令位置の公開資料なし） · `0075eaa0`（命令位置の公開資料なし） · `0075eac0`（命令位置の公開資料なし）

~~~diff
- 0075ea4c ["INT_ADD", "register:40f0:8", ["const:75ea4c:8", "const:4:8"]]
- 0075ea4c ["CALL", null, ["ram:728ca8:8"]]
+ 0075ea8c ["INT_ADD", "register:40f0:8", ["const:75ea8c:8", "const:4:8"]]
+ 0075ea8c ["CALL", null, ["ram:728ce8:8"]]
- 0075ea4c bytes 9728ff97
+ 0075ea8c bytes 9728ff97
- 0075ea60 ["INT_ADD", "register:40f0:8", ["const:75ea60:8", "const:4:8"]]
- 0075ea60 ["CALL", null, ["ram:728dac:8"]]
+ 0075eaa0 ["INT_ADD", "register:40f0:8", ["const:75eaa0:8", "const:4:8"]]
+ 0075eaa0 ["CALL", null, ["ram:728dec:8"]]
- 0075ea60 bytes d328ff97
+ 0075eaa0 bytes d328ff97
- 0075ea80 ["INT_ADD", "register:40f0:8", ["const:75ea80:8", "const:4:8"]]
- 0075ea80 ["CALL", null, ["ram:728ca8:8"]]
+ 0075eac0 ["INT_ADD", "register:40f0:8", ["const:75eac0:8", "const:4:8"]]
+ 0075eac0 ["CALL", null, ["ram:728ce8:8"]]
- 0075ea80 bytes 8a28ff97
+ 0075eac0 bytes 8a28ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d784c27288b84fded913351a94b73d33"></a>

### [`007640b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/007640b0.md) → [`007640f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/007640f0.md) FUN_007640f0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) [`007938c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00793/007938c8.md) · 呼出先 9件 [`0047e89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e89c.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`0072ace0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072a/0072ace0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md)
- 新版 呼出元 2件 [`0075eb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075eb80.md) [`00793908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00793/00793908.md) · 呼出先 9件 [`0047e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`0072ad20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072a/0072ad20.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 89.09% / 新版 89.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_destination` 7件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00764320",
      "incomplete_value": false,
      "site": "00764320",
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
      "definition_site": "007642e0",
      "incomplete_value": false,
      "site": "007642e0",
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
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00764324",
      "incomplete_value": false,
      "site": "00764324",
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
      "definition_site": "007642e4",
      "incomplete_value": false,
      "site": "007642e4",
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
    "ordinal": 21,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00764320",
      "incomplete_value": false,
      "site": "00764324",
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
      "definition_site": "007642e0",
      "incomplete_value": false,
      "site": "007642e4",
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
      "007641e4",
      "READ",
      [
        "storage",
        "00c9a8a0",
        null,
        "pointer"
      ]
    ],
    [
      "00764238",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ],
    [
      "0076424c",
      "PARAM",
      [
        "storage",
        "00ca4b00",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "007641e4",
      "READ",
      [
        "storage",
        "00c9aca0",
        null,
        "pointer"
      ]
    ],
    [
      "00764238",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      "0076424c",
      "PARAM",
      [
        "storage",
        "00ca4f00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007641f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/007640b0.md#insn-007641f4) · [`00764234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/007640b0.md#insn-00764234) · [`007642a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/007640b0.md#insn-007642a4)
- 新版 `00764234`（命令位置の公開資料なし） · `00764274`（命令位置の公開資料なし） · `007642e4`（命令位置の公開資料なし）

~~~diff
- 007641f4 ["COPY", "tmp:0:8", ["const:b38:8"]]
- 007641f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007641f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007641f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00764234 ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 00764234 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00764234 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00764234 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007641f4 bytes 08e12c91
+ 00764234 bytes 08e13c91
- 00764234 ["INT_ADD", "register:40f0:8", ["const:764234:8", "const:4:8"]]
- 00764234 ["CALL", null, ["callee:0047e8dc:8"]]
+ 00764274 ["INT_ADD", "register:40f0:8", ["const:764274:8", "const:4:8"]]
+ 00764274 ["CALL", null, ["callee:0047e8dc:8"]]
- 00764234 bytes 9a69f497
+ 00764274 bytes 9a69f497
- 007642a4 ["INT_ADD", "register:40f0:8", ["const:7642a4:8", "const:4:8"]]
- 007642a4 ["CALL", null, ["callee:00c57e80:8"]]
+ 007642e4 ["INT_ADD", "register:40f0:8", ["const:7642e4:8", "const:4:8"]]
+ 007642e4 ["CALL", null, ["callee:00c57e80:8"]]
- 007642a4 bytes f7cd1394
+ 007642e4 bytes e7ce1394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3aea379ed71dbc977b16fac9f5b0bf29"></a>

### [`00764394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764394.md) → [`007643d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/007643d4.md) FUN_007643d4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)
- 新版 呼出元 1件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.06% / 新版 97.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00764448",
      "incomplete_value": false,
      "site": "0076444c",
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
      "definition_site": "00764408",
      "incomplete_value": false,
      "site": "0076440c",
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
      "00764448",
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
      "00764448",
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

- 旧版 [`0076440c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764394.md#insn-0076440c) · [`00764408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764394.md#insn-00764408)
- 新版 `0076444c`（命令位置の公開資料なし） · `00764448`（命令位置の公開資料なし）

~~~diff
- 0076440c ["INT_ADD", "register:40f0:8", ["const:76440c:8", "const:4:8"]]
- 0076440c ["CALL", null, ["callee:00442930:8"]]
+ 0076444c ["INT_ADD", "register:40f0:8", ["const:76444c:8", "const:4:8"]]
+ 0076444c ["CALL", null, ["callee:00442930:8"]]
- 0076440c bytes 3979f397
+ 0076444c bytes 3979f397
- 00764408 ["COPY", "tmp:0:8", ["const:f0:8"]]
- 00764408 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00764408 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00764408 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00764448 ["COPY", "tmp:0:8", ["const:1bd:8"]]
+ 00764448 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00764448 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00764448 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00764408 bytes 00c00391
+ 00764448 bytes 00f40691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-078a90c4fc18c3ae69c020e9cbba2fec"></a>

### [`0076441c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/0076441c.md) → [`0076445c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/0076445c.md) FUN_0076445c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)
- 新版 呼出元 1件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.06% / 新版 97.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007644d0",
      "incomplete_value": false,
      "site": "007644d4",
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
      "definition_site": "00764490",
      "incomplete_value": false,
      "site": "00764494",
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
      "007644d0",
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
      "007644d0",
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

- 旧版 [`00764494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/0076441c.md#insn-00764494) · [`00764490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/0076441c.md#insn-00764490)
- 新版 `007644d4`（命令位置の公開資料なし） · `007644d0`（命令位置の公開資料なし）

~~~diff
- 00764494 ["INT_ADD", "register:40f0:8", ["const:764494:8", "const:4:8"]]
- 00764494 ["CALL", null, ["callee:00442930:8"]]
+ 007644d4 ["INT_ADD", "register:40f0:8", ["const:7644d4:8", "const:4:8"]]
+ 007644d4 ["CALL", null, ["callee:00442930:8"]]
- 00764494 bytes 1779f397
+ 007644d4 bytes 1779f397
- 00764490 ["COPY", "tmp:0:8", ["const:f0:8"]]
- 00764490 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00764490 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00764490 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007644d0 ["COPY", "tmp:0:8", ["const:1bd:8"]]
+ 007644d0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007644d0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007644d0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00764490 bytes 00c00391
+ 007644d0 bytes 00f40691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb29126b8be7f4e86ff6032bfdb58402"></a>

### [`007644a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/007644a4.md) → [`007644e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/007644e4.md) FUN_007644e4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) [`00a8a220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a8a/00a8a220.md) · 呼出先 23件 [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`00800338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/00800338.md) [`009a9164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a9/009a9164.md) [`009a95cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a9/009a95cc.md) [`009aac20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009aa/009aac20.md)
- 新版 呼出元 2件 [`0075eb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075eb80.md) [`00a8a418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a8a/00a8a418.md) · 呼出先 23件 [`0048ce84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce84.md) [`00800378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/00800378.md) [`009a9300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a9/009a9300.md) [`009a9768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a9/009a9768.md) [`009aadbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009aa/009aadbc.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.34% / 新版 99.34%

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
      "site": "00764704",
      "value": [
        "leaf",
        "ram:9a9768:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007646c4",
      "value": [
        "leaf",
        "ram:9a95cc:8"
      ]
    },
    "ordinal": 27,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00764704",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "009a95cc"
      ]
    ]
  ],
  "added": [
    [
      "00764704",
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

- 旧版 [`007646c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/007644a4.md#insn-007646c4) · [`007644d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/007644a4.md#insn-007644d8) · [`007644e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/007644a4.md#insn-007644e0)
- 新版 `00764704`（命令位置の公開資料なし） · `00764518`（命令位置の公開資料なし） · `00764520`（命令位置の公開資料なし）

~~~diff
- 007646c4 ["INT_ADD", "register:40f0:8", ["const:7646c4:8", "const:4:8"]]
- 007646c4 ["CALL", null, ["ram:9a95cc:8"]]
+ 00764704 ["INT_ADD", "register:40f0:8", ["const:764704:8", "const:4:8"]]
+ 00764704 ["CALL", null, ["ram:9a9768:8"]]
- 007646c4 bytes c2130994
+ 00764704 bytes 19140994
- 007644d8 ["INT_ADD", "register:40f0:8", ["const:7644d8:8", "const:4:8"]]
- 007644d8 ["CALL", null, ["callee:0048ce84:8"]]
+ 00764518 ["INT_ADD", "register:40f0:8", ["const:764518:8", "const:4:8"]]
+ 00764518 ["CALL", null, ["callee:0048ce84:8"]]
- 007644d8 bytes 5ba2f497
+ 00764518 bytes 5ba2f497
- 007644e0 ["INT_ADD", "register:40f0:8", ["const:7644e0:8", "const:4:8"]]
- 007644e0 ["CALL", null, ["callee:00a35b98:8"]]
+ 00764520 ["INT_ADD", "register:40f0:8", ["const:764520:8", "const:4:8"]]
+ 00764520 ["CALL", null, ["callee:00a35b98:8"]]
- 007644e0 bytes 30450b94
+ 00764520 bytes 9e450b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-722e614f6fde7be1794d376b1dc7b994"></a>

### [`00764730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764730.md) → [`00764770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764770.md) FUN_00764770

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 5件 [`00735fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00735/00735fdc.md) [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) [`0088c830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c830.md) [`0089b248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089b/0089b248.md) [`008d9a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9a68.md) · 呼出先 16件 [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`00652d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00652/00652d20.md) [`0073369c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00733/0073369c.md)
- 新版 呼出元 5件 [`0073601c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00736/0073601c.md) [`0075eb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075eb80.md) [`0088c870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c870.md) [`0089b28c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089b/0089b28c.md) [`008d9c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d9c04.md) · 呼出先 16件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`00652d60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00652/00652d60.md) [`007336dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00733/007336dc.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.41% / 新版 93.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00764890",
      "incomplete_value": true,
      "site": "007648b4",
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
                "const:a71:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00764850",
      "incomplete_value": true,
      "site": "00764874",
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
                "const:995:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "007647fc",
      "incomplete_value": true,
      "site": "007647fc",
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
      "definition_site": "007647bc",
      "incomplete_value": true,
      "site": "007647bc",
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
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00764804",
      "incomplete_value": false,
      "site": "00764814",
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
    "old": {
      "definition_site": "007647c4",
      "incomplete_value": false,
      "site": "007647d4",
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
            "const:a58:8"
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
      "007647f8",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "00764804",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0076480c",
      "PARAM",
      [
        "storage",
        "00c77608",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007647f8",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "00764804",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0076480c",
      "PARAM",
      [
        "storage",
        "00c77a08",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007647d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764730.md#insn-007647d4) · [`007649b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764730.md#insn-007649b0) · [`007649f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764730.md#insn-007649f0)
- 新版 `00764814`（命令位置の公開資料なし） · `007649f0`（命令位置の公開資料なし） · `00764a30`（命令位置の公開資料なし）

~~~diff
- 007647d4 ["INT_ADD", "register:40f0:8", ["const:7647d4:8", "const:4:8"]]
- 007647d4 ["CALL", null, ["callee:00c58610:8"]]
+ 00764814 ["INT_ADD", "register:40f0:8", ["const:764814:8", "const:4:8"]]
+ 00764814 ["CALL", null, ["callee:00c58610:8"]]
- 007647d4 bytes 8fce1394
+ 00764814 bytes 7fcf1394
- 007649b0 ["INT_ADD", "register:40f0:8", ["const:7649b0:8", "const:4:8"]]
- 007649b0 ["CALL", null, ["callee:00c57e50:8"]]
+ 007649f0 ["INT_ADD", "register:40f0:8", ["const:7649f0:8", "const:4:8"]]
+ 007649f0 ["CALL", null, ["callee:00c57e50:8"]]
- 007649b0 bytes 28cc1394
+ 007649f0 bytes 18cd1394
- 007649f0 ["INT_ADD", "register:40f0:8", ["const:7649f0:8", "const:4:8"]]
- 007649f0 ["CALL", null, ["callee:00c57e30:8"]]
+ 00764a30 ["INT_ADD", "register:40f0:8", ["const:764a30:8", "const:4:8"]]
+ 00764a30 ["CALL", null, ["callee:00c57e30:8"]]
- 007649f0 bytes 10cc1394
+ 00764a30 bytes 00cd1394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb86c17867706a9d99b5603611b8c41a"></a>

### [`00764a8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764a8c.md) → [`00764acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764acc.md) FUN_00764acc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) · 呼出先 10件 [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0046ca44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046ca44.md) [`007858c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/007858c0.md) [`007858c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/007858c4.md) [`00785974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/00785974.md)
- 新版 呼出元 1件 [`0075eb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075eb80.md) · 呼出先 10件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046ca84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046ca84.md) [`00785900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00785/00785900.md) [`00785904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00785/00785904.md) [`007859b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00785/007859b4.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.65% / 新版 92.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00764b28",
      "incomplete_value": false,
      "site": "00764b28",
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
      "definition_site": "00764ae8",
      "incomplete_value": false,
      "site": "00764ae8",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00764b74",
      "incomplete_value": false,
      "site": "00764b74",
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
      "definition_site": "00764b34",
      "incomplete_value": false,
      "site": "00764b34",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00764af8",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00764ab8",
      "value": [
        "leaf",
        "ram:46c984:8"
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
      "00764af8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "00764b28",
      "DATA",
      [
        "storage",
        "00c78fa0",
        null,
        "undefined *"
      ]
    ],
    [
      "00764b60",
      "READ",
      [
        "storage",
        "00c78fc0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00764af8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "00764b28",
      "DATA",
      [
        "storage",
        "00c793a0",
        null,
        "undefined *"
      ]
    ],
    [
      "00764b60",
      "READ",
      [
        "storage",
        "00c793c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00764ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764a8c.md#insn-00764ab8) · [`00764af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764a8c.md#insn-00764af8) · [`00764ac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764a8c.md#insn-00764ac4)
- 新版 `00764af8`（命令位置の公開資料なし） · `00764b38`（命令位置の公開資料なし） · `00764b04`（命令位置の公開資料なし）

~~~diff
- 00764ab8 ["INT_ADD", "register:40f0:8", ["const:764ab8:8", "const:4:8"]]
- 00764ab8 ["CALL", null, ["ram:46c984:8"]]
+ 00764af8 ["INT_ADD", "register:40f0:8", ["const:764af8:8", "const:4:8"]]
+ 00764af8 ["CALL", null, ["ram:46c9c4:8"]]
- 00764ab8 bytes b31ff497
+ 00764af8 bytes b31ff497
- 00764af8 ["INT_ADD", "register:40f0:8", ["const:764af8:8", "const:4:8"]]
- 00764af8 ["CALL", null, ["callee:00788060:8"]]
+ 00764b38 ["INT_ADD", "register:40f0:8", ["const:764b38:8", "const:4:8"]]
+ 00764b38 ["CALL", null, ["callee:00788060:8"]]
- 00764af8 bytes 4a8d0094
+ 00764b38 bytes 4a8d0094
- 00764ac4 ["INT_ADD", "register:40f0:8", ["const:764ac4:8", "const:4:8"]]
- 00764ac4 ["CALL", null, ["callee:0046ca84:8"]]
+ 00764b04 ["INT_ADD", "register:40f0:8", ["const:764b04:8", "const:4:8"]]
+ 00764b04 ["CALL", null, ["callee:0046ca84:8"]]
- 00764ac4 bytes e01ff497
+ 00764b04 bytes e01ff497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64bc34884e47747dcf44d108817b9c14"></a>

### [`00764bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764bec.md) → [`00764c2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764c2c.md) FUN_00764c2c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 7件 [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) [`0076621c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00766/0076621c.md) [`00767108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00767/00767108.md) [`00767d64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00767/00767d64.md) [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 2件 [`00b2f3c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f3c8.md) [`00b2f458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f458.md)
- 新版 呼出元 7件 [`0075eb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075eb80.md) [`0076625c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00766/0076625c.md) [`00767148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00767/00767148.md) [`00767da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00767/00767da4.md) [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) · 呼出先 2件 [`00b2f7f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2f/00b2f7f0.md) [`00b2f880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2f/00b2f880.md)

変更の種類 constant, operands_and_dependencies, return_value_candidate, store_destination

命令の説明率　旧版 99.42% / 新版 99.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `return_value_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00764c78",
      "incomplete_value": true,
      "site": "00764c78",
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
            "const:e9c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00764c38",
      "incomplete_value": true,
      "site": "00764c38",
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
            "const:a9c:8"
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
      "definition_site": "00764eb0",
      "incomplete_value": false,
      "site": "00764eb0",
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
            "const:e20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00764e70",
      "incomplete_value": false,
      "site": "00764e70",
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
            "const:a20:8"
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00764ed8",
      "incomplete_value": true,
      "site": "00764edc",
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
      "definition_site": "00764e98",
      "incomplete_value": true,
      "site": "00764e9c",
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
      "00764c30",
      "READ",
      [
        "storage",
        "00ca3a9c",
        null,
        "undefined1"
      ]
    ],
    [
      "00764c78",
      "WRITE",
      [
        "storage",
        "00ca3a9c",
        null,
        "undefined1"
      ]
    ],
    [
      "00764eb0",
      "WRITE",
      [
        "storage",
        "00ca7a20",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00764c30",
      "READ",
      [
        "storage",
        "00ca3e9c",
        null,
        "undefined1"
      ]
    ],
    [
      "00764c78",
      "WRITE",
      [
        "storage",
        "00ca3e9c",
        null,
        "undefined1"
      ]
    ],
    [
      "00764eb0",
      "WRITE",
      [
        "storage",
        "00ca7e20",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00764c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764bec.md#insn-00764c38) · [`00764e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764bec.md#insn-00764e70) · [`00764bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764bec.md#insn-00764bf0)
- 新版 `00764c78`（命令位置の公開資料なし） · `00764eb0`（命令位置の公開資料なし） · `00764c30`（命令位置の公開資料なし）

~~~diff
- 00764c38 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00764c38 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00764c38 ["INT_ADD", "tmp:2:8", ["register:4040:8", "const:a9c:8"]]
- 00764c38 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00764c78 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00764c78 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00764c78 ["INT_ADD", "tmp:2:8", ["register:4040:8", "const:e9c:8"]]
+ 00764c78 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00764c38 bytes 1f712a39
+ 00764c78 bytes 1f713a39
- 00764e70 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a20:8"]]
- 00764e70 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:4"]]
+ 00764eb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e20:8"]]
+ 00764eb0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:4"]]
- 00764e70 bytes 00210ab9
+ 00764eb0 bytes 00210eb9
- 00764bf0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a9c:8"]]
- 00764bf0 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00764bf0 ["INT_ZEXT", "register:4048:8", ["tmp:1:1"]]
+ 00764c30 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e9c:8"]]
+ 00764c30 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00764c30 ["INT_ZEXT", "register:4048:8", ["tmp:1:1"]]
- 00764bf0 bytes 09716a39
+ 00764c30 bytes 09717a39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31b956c7810692eb3f35cc2f4db494af"></a>

### [`007650e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00765/007650e8.md) → [`00765128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00765/00765128.md) FUN_00765128

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0076621c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00766/0076621c.md) [`00767108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00767/00767108.md) · 呼出先 21件 [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`0045175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/0045175c.md) [`00451998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451998.md) [`0055e988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e988.md)
- 新版 呼出元 2件 [`0076625c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00766/0076625c.md) [`00767148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00767/00767148.md) · 呼出先 21件 [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`0045179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md) [`004519d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004519d8.md) [`0055e9c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e9c8.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_destination` 1件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0076516c",
      "incomplete_value": true,
      "site": "00765180",
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
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:deb:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0076512c",
      "incomplete_value": true,
      "site": "00765140",
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
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:dab:8"
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
      "definition_site": "0076516c",
      "incomplete_value": true,
      "site": "00765184",
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
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:deb:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0076512c",
      "incomplete_value": true,
      "site": "00765144",
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
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:dab:8"
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
      "definition_site": "0076524c",
      "incomplete_value": true,
      "site": "00765250",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "0076520c",
      "incomplete_value": true,
      "site": "00765210",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "0076516c",
      "READ",
      [
        "storage",
        "002afdab",
        null,
        "string"
      ]
    ],
    [
      "00765238",
      "READ",
      [
        "storage",
        "00c9a888",
        null,
        "pointer"
      ]
    ],
    [
      "0076523c",
      "READ",
      [
        "storage",
        "00c9a7b8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0076516c",
      "READ",
      [
        "storage",
        "002afdeb",
        null,
        "string"
      ]
    ],
    [
      "00765238",
      "READ",
      [
        "storage",
        "00c9ac88",
        null,
        "pointer"
      ]
    ],
    [
      "0076523c",
      "READ",
      [
        "storage",
        "00c9abb8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00765180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00765/007650e8.md#insn-00765180) · [`00765254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00765/007650e8.md#insn-00765254) · [`0076529c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00765/007650e8.md#insn-0076529c)
- 新版 `007651c0`（命令位置の公開資料なし） · `00765294`（命令位置の公開資料なし） · `007652dc`（命令位置の公開資料なし）

~~~diff
- 00765180 ["INT_ADD", "register:40f0:8", ["const:765180:8", "const:4:8"]]
- 00765180 ["CALL", null, ["callee:00c57eb0:8"]]
+ 007651c0 ["INT_ADD", "register:40f0:8", ["const:7651c0:8", "const:4:8"]]
+ 007651c0 ["CALL", null, ["callee:00c57eb0:8"]]
- 00765180 bytes 4cca1394
+ 007651c0 bytes 3ccb1394
- 00765254 ["INT_ADD", "register:40f0:8", ["const:765254:8", "const:4:8"]]
- 00765254 ["CALL", null, ["callee:00c581f0:8"]]
+ 00765294 ["INT_ADD", "register:40f0:8", ["const:765294:8", "const:4:8"]]
+ 00765294 ["CALL", null, ["callee:00c581f0:8"]]
- 00765254 bytes e7ca1394
+ 00765294 bytes d7cb1394
- 0076529c ["INT_ADD", "register:40f0:8", ["const:76529c:8", "const:4:8"]]
- 0076529c ["CALL", null, ["callee:00c581b0:8"]]
+ 007652dc ["INT_ADD", "register:40f0:8", ["const:7652dc:8", "const:4:8"]]
+ 007652dc ["CALL", null, ["callee:00c581b0:8"]]
- 0076529c bytes c5ca1394
+ 007652dc bytes b5cb1394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0c9e32e3d9bf995121ba3ea5c22e28c"></a>

### [`007656e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00765/007656e8.md) → [`00765728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00765/00765728.md) FUN_00765728

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00765ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00765/00765ddc.md) · 呼出先 22件 [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00451998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451998.md) [`0055e988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e988.md) [`00560418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560418.md)
- 新版 呼出元 1件 [`00765e1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00765/00765e1c.md) · 呼出先 22件 [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`004519d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004519d8.md) [`0055e9c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0055e/0055e9c8.md) [`00560458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/00560458.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 94.92% / 新版 94.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_destination` 1件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00765784",
      "incomplete_value": true,
      "site": "00765784",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2aa000:8"
              ],
              [
                "leaf",
                "const:e9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00765744",
      "incomplete_value": true,
      "site": "00765744",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2aa000:8"
              ],
              [
                "leaf",
                "const:1c:8"
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
      "definition_site": "007657ec",
      "incomplete_value": true,
      "site": "00765800",
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
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:deb:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007657ac",
      "incomplete_value": true,
      "site": "007657c0",
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
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:dab:8"
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
      "definition_site": "007657ec",
      "incomplete_value": true,
      "site": "00765804",
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
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:deb:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007657ac",
      "incomplete_value": true,
      "site": "007657c4",
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
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:dab:8"
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
      "00765774",
      "READ",
      [
        "storage",
        "002aa01c",
        null,
        "string"
      ]
    ],
    [
      "007657ec",
      "READ",
      [
        "storage",
        "002afdab",
        null,
        "string"
      ]
    ],
    [
      "007658b4",
      "READ",
      [
        "storage",
        "00c9a888",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00765774",
      "READ",
      [
        "storage",
        "002aa0e9",
        null,
        "string"
      ]
    ],
    [
      "007657ec",
      "READ",
      [
        "storage",
        "002afdeb",
        null,
        "string"
      ]
    ],
    [
      "007658b4",
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

- 旧版 [`00765784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00765/007656e8.md#insn-00765784) · [`00765800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00765/007656e8.md#insn-00765800) · [`007658cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00765/007656e8.md#insn-007658cc)
- 新版 `007657c4`（命令位置の公開資料なし） · `00765840`（命令位置の公開資料なし） · `0076590c`（命令位置の公開資料なし）

~~~diff
- 00765784 ["INT_ADD", "register:40f0:8", ["const:765784:8", "const:4:8"]]
- 00765784 ["CALL", null, ["callee:00c57eb0:8"]]
+ 007657c4 ["INT_ADD", "register:40f0:8", ["const:7657c4:8", "const:4:8"]]
+ 007657c4 ["CALL", null, ["callee:00c57eb0:8"]]
- 00765784 bytes cbc81394
+ 007657c4 bytes bbc91394
- 00765800 ["INT_ADD", "register:40f0:8", ["const:765800:8", "const:4:8"]]
- 00765800 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00765840 ["INT_ADD", "register:40f0:8", ["const:765840:8", "const:4:8"]]
+ 00765840 ["CALL", null, ["callee:00c57eb0:8"]]
- 00765800 bytes acc81394
+ 00765840 bytes 9cc91394
- 007658cc ["INT_ADD", "register:40f0:8", ["const:7658cc:8", "const:4:8"]]
- 007658cc ["CALL", null, ["callee:00c581f0:8"]]
+ 0076590c ["INT_ADD", "register:40f0:8", ["const:76590c:8", "const:4:8"]]
+ 0076590c ["CALL", null, ["callee:00c581f0:8"]]
- 007658cc bytes 49c91394
+ 0076590c bytes 39ca1394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5268c690a04de1a766f02021a9e3ee7e"></a>

### [`00765ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00765/00765ddc.md) → [`00765e1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00765/00765e1c.md) FUN_00765e1c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0076621c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00766/0076621c.md) [`00767108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00767/00767108.md) [`00767c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00767/00767c74.md) · 呼出先 10件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00459a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459a90.md) [`00596fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596fdc.md) [`0059715c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/0059715c.md) [`007656e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00765/007656e8.md)
- 新版 呼出元 3件 [`0076625c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00766/0076625c.md) [`00767148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00767/00767148.md) [`00767cb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00767/00767cb4.md) · 呼出先 10件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00459ad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459ad0.md) [`0059701c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059701c.md) [`0059719c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059719c.md) [`00765728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00765/00765728.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.71% / 新版 87.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00765ec8",
      "incomplete_value": true,
      "site": "00765ec8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00765e88",
      "incomplete_value": true,
      "site": "00765e88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3e3:8"
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
      "definition_site": "00765ecc",
      "incomplete_value": true,
      "site": "00765ecc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00765e8c",
      "incomplete_value": true,
      "site": "00765e8c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00765f48",
      "incomplete_value": false,
      "site": "00765f50",
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
    "old": {
      "definition_site": "00765f08",
      "incomplete_value": false,
      "site": "00765f10",
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
            "const:690:8"
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
      "00765e6c",
      "READ",
      [
        "storage",
        "002afdab",
        null,
        "string"
      ]
    ],
    [
      "00765eb8",
      "READ",
      [
        "storage",
        "002a33e3",
        null,
        "string"
      ]
    ],
    [
      "00765ebc",
      "READ",
      [
        "storage",
        "002a33e8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00765e6c",
      "READ",
      [
        "storage",
        "002afdeb",
        null,
        "string"
      ]
    ],
    [
      "00765eb8",
      "READ",
      [
        "storage",
        "002a34b0",
        null,
        "string"
      ]
    ],
    [
      "00765ebc",
      "READ",
      [
        "storage",
        "002a34b5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00765e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00765/00765ddc.md#insn-00765e4c) · [`00765f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00765/00765ddc.md#insn-00765f50) · [`00765f6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00765/00765ddc.md#insn-00765f6c)
- 新版 `00765e8c`（命令位置の公開資料なし） · `00765f90`（命令位置の公開資料なし） · `00765fac`（命令位置の公開資料なし）

~~~diff
- 00765e4c ["INT_ADD", "register:40f0:8", ["const:765e4c:8", "const:4:8"]]
- 00765e4c ["CALL", null, ["callee:0044108c:8"]]
+ 00765e8c ["INT_ADD", "register:40f0:8", ["const:765e8c:8", "const:4:8"]]
+ 00765e8c ["CALL", null, ["callee:0044108c:8"]]
- 00765e4c bytes 806cf397
+ 00765e8c bytes 806cf397
- 00765f50 ["INT_ADD", "register:40f0:8", ["const:765f50:8", "const:4:8"]]
- 00765f50 ["CALL", null, ["callee:00c53d00:8"]]
+ 00765f90 ["INT_ADD", "register:40f0:8", ["const:765f90:8", "const:4:8"]]
+ 00765f90 ["CALL", null, ["callee:00c53d00:8"]]
- 00765f50 bytes 64b61394
+ 00765f90 bytes 5cb71394
- 00765f6c ["INT_ADD", "register:40f0:8", ["const:765f6c:8", "const:4:8"]]
- 00765f6c ["CALL", null, ["callee:00c57e80:8"]]
+ 00765fac ["INT_ADD", "register:40f0:8", ["const:765fac:8", "const:4:8"]]
+ 00765fac ["CALL", null, ["callee:00c57e80:8"]]
- 00765f6c bytes c5c61394
+ 00765fac bytes b5c71394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-613ec21496bf09a7b98ed90242790db2"></a>

### [`0076621c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00766/0076621c.md) → [`0076625c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00766/0076625c.md) FUN_0076625c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00769220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769220.md) · 呼出先 27件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00451998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451998.md) [`004593b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/004593b0.md)
- 新版 呼出元 1件 [`00769260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769260.md) · 呼出先 27件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043dba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dba4.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`004519d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004519d8.md) [`004593f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004593f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.94% / 新版 95.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00766338",
      "incomplete_value": true,
      "site": "00766340",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007662f8",
      "incomplete_value": true,
      "site": "00766300",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00766408",
      "incomplete_value": true,
      "site": "00766420",
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
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:deb:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007663c8",
      "incomplete_value": true,
      "site": "007663e0",
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
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:dab:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00766408",
      "incomplete_value": true,
      "site": "00766424",
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
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:deb:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007663c8",
      "incomplete_value": true,
      "site": "007663e4",
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
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:dab:8"
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
      "007662dc",
      "DATA",
      [
        "storage",
        "003c7784",
        null,
        "byte[15]"
      ]
    ],
    [
      "0076632c",
      "READ",
      [
        "storage",
        "00c9a820",
        null,
        "pointer"
      ]
    ],
    [
      "00766340",
      "DATA",
      [
        "storage",
        "00c6d208",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007662dc",
      "DATA",
      [
        "storage",
        "003c7784",
        null,
        "qword"
      ]
    ],
    [
      "0076632c",
      "READ",
      [
        "storage",
        "00c9ac20",
        null,
        "pointer"
      ]
    ],
    [
      "00766340",
      "DATA",
      [
        "storage",
        "00c6d608",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00766424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00766/0076621c.md#insn-00766424) · [`0076648c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00766/0076621c.md#insn-0076648c) · [`00766264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00766/0076621c.md#insn-00766264)
- 新版 `00766464`（命令位置の公開資料なし） · `007664cc`（命令位置の公開資料なし） · `007662a4`（命令位置の公開資料なし）

~~~diff
- 00766424 ["INT_ADD", "register:40f0:8", ["const:766424:8", "const:4:8"]]
- 00766424 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00766464 ["INT_ADD", "register:40f0:8", ["const:766464:8", "const:4:8"]]
+ 00766464 ["CALL", null, ["callee:00c57eb0:8"]]
- 00766424 bytes a3c51394
+ 00766464 bytes 93c61394
- 0076648c ["INT_ADD", "register:40f0:8", ["const:76648c:8", "const:4:8"]]
- 0076648c ["CALL", null, ["callee:00c57e90:8"]]
+ 007664cc ["INT_ADD", "register:40f0:8", ["const:7664cc:8", "const:4:8"]]
+ 007664cc ["CALL", null, ["callee:00c57e90:8"]]
- 0076648c bytes 81c51394
+ 007664cc bytes 71c61394
- 00766264 ["INT_ADD", "register:40f0:8", ["const:766264:8", "const:4:8"]]
- 00766264 ["CALL", null, ["callee:00550c28:8"]]
+ 007662a4 ["INT_ADD", "register:40f0:8", ["const:7662a4:8", "const:4:8"]]
+ 007662a4 ["CALL", null, ["callee:00550c28:8"]]
- 00766264 bytes 61aaf797
+ 007662a4 bytes 61aaf797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f19f29208d48da0902619b99ad4727d"></a>

### [`00767108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00767/00767108.md) → [`00767148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00767/00767148.md) FUN_00767148

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00697250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/00697250.md) · 呼出先 28件 [`0043db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043db64.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`0045175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/0045175c.md) [`00451998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451998.md) [`004597ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/004597ec.md)
- 新版 呼出元 1件 [`00697290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/00697290.md) · 呼出先 28件 [`0043dba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dba4.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`0045179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/0045179c.md) [`004519d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004519d8.md) [`0045982c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/0045982c.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 93.23% / 新版 93.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00767220",
      "incomplete_value": true,
      "site": "00767228",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007671e0",
      "incomplete_value": true,
      "site": "007671e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "007672f0",
      "incomplete_value": true,
      "site": "00767300",
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
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:deb:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007672b0",
      "incomplete_value": true,
      "site": "007672c0",
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
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:dab:8"
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
      "definition_site": "007672f0",
      "incomplete_value": true,
      "site": "00767304",
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
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:deb:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007672b0",
      "incomplete_value": true,
      "site": "007672c4",
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
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:dab:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 37,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007671c8",
      "DATA",
      [
        "storage",
        "003c7784",
        null,
        "byte[15]"
      ]
    ],
    [
      "00767214",
      "READ",
      [
        "storage",
        "00c9a820",
        null,
        "pointer"
      ]
    ],
    [
      "00767228",
      "DATA",
      [
        "storage",
        "00c6d208",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "007671c8",
      "DATA",
      [
        "storage",
        "003c7784",
        null,
        "qword"
      ]
    ],
    [
      "00767214",
      "READ",
      [
        "storage",
        "00c9ac20",
        null,
        "pointer"
      ]
    ],
    [
      "00767228",
      "DATA",
      [
        "storage",
        "00c6d608",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00767604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00767/00767108.md#insn-00767604) · [`00767640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00767/00767108.md#insn-00767640) · [`00767740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00767/00767108.md#insn-00767740)
- 新版 `00767644`（命令位置の公開資料なし） · `00767680`（命令位置の公開資料なし） · `00767780`（命令位置の公開資料なし）

~~~diff
- 00767604 ["COPY", "register:0:8", ["register:4040:8"]]
- 00767604 ["INT_ADD", "register:40f0:8", ["const:767604:8", "const:4:8"]]
- 00767604 ["CALLIND", null, ["register:0:8"]]
+ 00767644 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00767644 ["INT_ADD", "register:40f0:8", ["const:767644:8", "const:4:8"]]
+ 00767644 ["CALLIND", null, ["register:0:8"]]
- 00767604 bytes 00013fd6
+ 00767644 bytes 00013fd6
- 00767640 ["INT_ADD", "register:40f0:8", ["const:767640:8", "const:4:8"]]
- 00767640 ["CALL", null, ["callee:0045179c:8"]]
+ 00767680 ["INT_ADD", "register:40f0:8", ["const:767680:8", "const:4:8"]]
+ 00767680 ["CALL", null, ["callee:0045179c:8"]]
- 00767640 bytes 47a8f397
+ 00767680 bytes 47a8f397
- 00767740 ["COPY", "register:4048:8", ["const:2b3000:8"]]
+ 00767780 ["COPY", "register:4048:8", ["const:2b4000:8"]]
- 00767740 bytes 69daff90
+ 00767780 bytes 69daffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c94d8b3dfa2fb9f39a6044a5b8847470"></a>

### [`00767d64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00767/00767d64.md) → [`00767da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00767/00767da4.md) FUN_00767da4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) [`00886f04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886f04.md) · 呼出先 8件 [`004597ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/004597ec.md) [`005970d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005970d0.md) [`00764bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764bec.md) [`00767c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00767/00767c74.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) [`00886f44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886f44.md) · 呼出先 8件 [`0045982c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/0045982c.md) [`00597110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597110.md) [`00764c2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764c2c.md) [`00767cb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00767/00767cb4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

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
      "definition_site": "00767e40",
      "incomplete_value": true,
      "site": "00767e48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00767e00",
      "incomplete_value": true,
      "site": "00767e08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00767dec",
      "DATA",
      [
        "storage",
        "003c7784",
        null,
        "byte[15]"
      ]
    ],
    [
      "00767e34",
      "READ",
      [
        "storage",
        "00c9a820",
        null,
        "pointer"
      ]
    ],
    [
      "00767e48",
      "DATA",
      [
        "storage",
        "00c6d208",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00767dec",
      "DATA",
      [
        "storage",
        "003c7784",
        null,
        "qword"
      ]
    ],
    [
      "00767e34",
      "READ",
      [
        "storage",
        "00c9ac20",
        null,
        "pointer"
      ]
    ],
    [
      "00767e48",
      "DATA",
      [
        "storage",
        "00c6d608",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00767d9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00767/00767d64.md#insn-00767d9c) · [`00767da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00767/00767d64.md#insn-00767da0) · [`00767db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00767/00767d64.md#insn-00767db0)
- 新版 `00767ddc`（命令位置の公開資料なし） · `00767de0`（命令位置の公開資料なし） · `00767df0`（命令位置の公開資料なし）

~~~diff
- 00767d9c ["INT_ADD", "register:40f0:8", ["const:767d9c:8", "const:4:8"]]
- 00767d9c ["CALL", null, ["callee:00767cb4:8"]]
+ 00767ddc ["INT_ADD", "register:40f0:8", ["const:767ddc:8", "const:4:8"]]
+ 00767ddc ["CALL", null, ["callee:00767cb4:8"]]
- 00767d9c bytes b6ffff97
+ 00767ddc bytes b6ffff97
- 00767da0 ["INT_ADD", "register:40f0:8", ["const:767da0:8", "const:4:8"]]
- 00767da0 ["CALL", null, ["callee:008514f8:8"]]
+ 00767de0 ["INT_ADD", "register:40f0:8", ["const:767de0:8", "const:4:8"]]
+ 00767de0 ["CALL", null, ["callee:008514f8:8"]]
- 00767da0 bytes c6a50394
+ 00767de0 bytes c6a50394
- 00767db0 ["INT_ADD", "register:40f0:8", ["const:767db0:8", "const:4:8"]]
- 00767db0 ["CALL", null, ["callee:008514f8:8"]]
+ 00767df0 ["INT_ADD", "register:40f0:8", ["const:767df0:8", "const:4:8"]]
+ 00767df0 ["CALL", null, ["callee:008514f8:8"]]
- 00767db0 bytes c2a50394
+ 00767df0 bytes c2a50394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95ee0d16cccb625e7f7035906600a5a0"></a>

### [`00768174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/00768174.md) → [`007681b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00768/007681b4.md) FUN_007681b4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00884b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884b34.md) [`00a06c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06c00.md) · 呼出先 9件 [`00597e7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e7c.md) [`00878278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/00878278.md) [`00b3c4b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3c/00b3c4b4.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 2件 [`00884b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00884/00884b74.md) [`00a06d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06d9c.md) · 呼出先 9件 [`00597ebc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ebc.md) [`008782b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00878/008782b8.md) [`00b3c8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3c/00b3c8dc.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.95% / 新版 94.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0076823c",
      "incomplete_value": true,
      "site": "0076823c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f7d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007681fc",
      "incomplete_value": true,
      "site": "007681fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f3d:8"
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
      "definition_site": "00768230",
      "incomplete_value": true,
      "site": "00768240",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "007681f0",
      "incomplete_value": true,
      "site": "00768200",
      "value": [
        "LOAD",
        "8",
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
      "007681f0",
      "DATA",
      [
        "storage",
        "003c76b8",
        null,
        "uleb128"
      ]
    ],
    [
      "0076822c",
      "READ",
      [
        "storage",
        "002b0f3d",
        null,
        "string"
      ]
    ],
    [
      "00768230",
      "READ",
      [
        "storage",
        "002b0f44",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007681f0",
      "DATA",
      [
        "storage",
        "003c76b8",
        null,
        "dword"
      ]
    ],
    [
      "0076822c",
      "READ",
      [
        "storage",
        "002b0f7d",
        null,
        "string"
      ]
    ],
    [
      "00768230",
      "READ",
      [
        "storage",
        "002b0f84",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007681ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/00768174.md#insn-007681ac) · [`007681cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/00768174.md#insn-007681cc) · [`007681dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/00768174.md#insn-007681dc)
- 新版 `007681ec`（命令位置の公開資料なし） · `0076820c`（命令位置の公開資料なし） · `0076821c`（命令位置の公開資料なし）

~~~diff
- 007681ac ["INT_ADD", "register:40f0:8", ["const:7681ac:8", "const:4:8"]]
- 007681ac ["CALL", null, ["callee:00c580e0:8"]]
+ 007681ec ["INT_ADD", "register:40f0:8", ["const:7681ec:8", "const:4:8"]]
+ 007681ec ["CALL", null, ["callee:00c580e0:8"]]
- 007681ac bytes cdbe1394
+ 007681ec bytes bdbf1394
- 007681cc ["INT_ADD", "register:40f0:8", ["const:7681cc:8", "const:4:8"]]
- 007681cc ["CALL", null, ["callee:00597ebc:8"]]
+ 0076820c ["INT_ADD", "register:40f0:8", ["const:76820c:8", "const:4:8"]]
+ 0076820c ["CALL", null, ["callee:00597ebc:8"]]
- 007681cc bytes 2cbff897
+ 0076820c bytes 2cbff897
- 007681dc ["INT_ADD", "register:40f0:8", ["const:7681dc:8", "const:4:8"]]
- 007681dc ["CALL", null, ["callee:00c57eb0:8"]]
+ 0076821c ["INT_ADD", "register:40f0:8", ["const:76821c:8", "const:4:8"]]
+ 0076821c ["CALL", null, ["callee:00c57eb0:8"]]
- 007681dc bytes 35be1394
+ 0076821c bytes 25bf1394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1fb6f9ce85662bd4086257bf3330cd2e"></a>

### [`007683d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/007683d4.md) → [`00768414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00768/00768414.md) FUN_00768414

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009cc994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009cc/009cc994.md) · 呼出先 8件 [`00597e7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e7c.md) [`00b3c69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3c/00b3c69c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`009ccb30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009cc/009ccb30.md) · 呼出先 8件 [`00597ebc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ebc.md) [`00b3cac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3c/00b3cac4.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00768494",
      "incomplete_value": true,
      "site": "007684a4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00768454",
      "incomplete_value": true,
      "site": "00768464",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007684a8",
      "incomplete_value": true,
      "site": "007684a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f7d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00768468",
      "incomplete_value": true,
      "site": "00768468",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f3d:8"
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
      "00768460",
      "DATA",
      [
        "storage",
        "003c76e8",
        null,
        "dword"
      ]
    ],
    [
      "00768494",
      "READ",
      [
        "storage",
        "002b0f44",
        null,
        "string"
      ]
    ],
    [
      "00768498",
      "READ",
      [
        "storage",
        "002b0f3d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00768460",
      "DATA",
      [
        "storage",
        "003c76e8",
        "fde_003c76e8",
        "dword"
      ]
    ],
    [
      "00768494",
      "READ",
      [
        "storage",
        "002b0f84",
        null,
        "string"
      ]
    ],
    [
      "00768498",
      "READ",
      [
        "storage",
        "002b0f7d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00768408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/007683d4.md#insn-00768408) · [`00768414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/007683d4.md#insn-00768414) · [`00768434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/007683d4.md#insn-00768434)
- 新版 `00768448`（命令位置の公開資料なし） · `00768454`（命令位置の公開資料なし） · `00768474`（命令位置の公開資料なし）

~~~diff
- 00768408 ["INT_ADD", "register:40f0:8", ["const:768408:8", "const:4:8"]]
- 00768408 ["CALL", null, ["callee:00c580e0:8"]]
+ 00768448 ["INT_ADD", "register:40f0:8", ["const:768448:8", "const:4:8"]]
+ 00768448 ["CALL", null, ["callee:00c580e0:8"]]
- 00768408 bytes 36be1394
+ 00768448 bytes 26bf1394
- 00768414 ["INT_ADD", "register:40f0:8", ["const:768414:8", "const:4:8"]]
- 00768414 ["CALL", null, ["callee:00b3cac4:8"]]
+ 00768454 ["INT_ADD", "register:40f0:8", ["const:768454:8", "const:4:8"]]
+ 00768454 ["CALL", null, ["callee:00b3cac4:8"]]
- 00768414 bytes a2500f94
+ 00768454 bytes 9c510f94
- 00768434 ["INT_ADD", "register:40f0:8", ["const:768434:8", "const:4:8"]]
- 00768434 ["CALL", null, ["callee:00597ebc:8"]]
+ 00768474 ["INT_ADD", "register:40f0:8", ["const:768474:8", "const:4:8"]]
+ 00768474 ["CALL", null, ["callee:00597ebc:8"]]
- 00768434 bytes 92bef897
+ 00768474 bytes 92bef897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4dd09983f9af03ccf10f1f1f2d8b7c24"></a>

### [`00769220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769220.md) → [`00769260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769260.md) FUN_00769260

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`007697b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/007697b4.md) [`00769bc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769bc8.md) [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`0088c830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c830.md) [`0088f45c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088f45c.md) · 呼出先 11件 [`0054071c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/0054071c.md) [`00597e7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e7c.md) [`0076621c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00766/0076621c.md) [`00767c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00767/00767c74.md) [`00767f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00767/00767f54.md)
- 新版 呼出元 6件 [`007697f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/007697f4.md) [`00769c08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769c08.md) [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) [`0088c870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c870.md) [`0088f49c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088f49c.md) · 呼出先 11件 [`0054075c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/0054075c.md) [`00597ebc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ebc.md) [`0076625c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00766/0076625c.md) [`00767cb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00767/00767cb4.md) [`00767f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00767/00767f94.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.33% / 新版 98.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00769570",
      "incomplete_value": false,
      "site": "00769578",
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
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00769530",
      "incomplete_value": false,
      "site": "00769538",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:f50:8"
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
      "site": "007692c8",
      "value": [
        "leaf",
        "ram:767f94:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00769288",
      "value": [
        "leaf",
        "ram:767f54:8"
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
      "site": "007694d4",
      "value": [
        "leaf",
        "ram:a14d8c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00769494",
      "value": [
        "leaf",
        "ram:a14bf0:8"
      ]
    },
    "ordinal": 13,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007692b4",
      "DATA",
      [
        "storage",
        "003c76b8",
        null,
        "uleb128"
      ]
    ],
    [
      "007692c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00767f54"
      ]
    ],
    [
      "007692cc",
      "DATA",
      [
        "storage",
        "003c76e8",
        null,
        "dword"
      ]
    ]
  ],
  "added": [
    [
      "007692b4",
      "DATA",
      [
        "storage",
        "003c76b8",
        null,
        "dword"
      ]
    ],
    [
      "007692c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00767f94"
      ]
    ],
    [
      "007692cc",
      "DATA",
      [
        "storage",
        "003c76e8",
        "fde_003c76e8",
        "dword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00769288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769220.md#insn-00769288) · [`00769494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769220.md#insn-00769494) · [`007692d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769220.md#insn-007692d8)
- 新版 `007692c8`（命令位置の公開資料なし） · `007694d4`（命令位置の公開資料なし） · `00769318`（命令位置の公開資料なし）

~~~diff
- 00769288 ["INT_ADD", "register:40f0:8", ["const:769288:8", "const:4:8"]]
- 00769288 ["CALL", null, ["ram:767f54:8"]]
+ 007692c8 ["INT_ADD", "register:40f0:8", ["const:7692c8:8", "const:4:8"]]
+ 007692c8 ["CALL", null, ["ram:767f94:8"]]
- 00769288 bytes 33fbff97
+ 007692c8 bytes 33fbff97
- 00769494 ["INT_ADD", "register:40f0:8", ["const:769494:8", "const:4:8"]]
- 00769494 ["CALL", null, ["ram:a14bf0:8"]]
+ 007694d4 ["INT_ADD", "register:40f0:8", ["const:7694d4:8", "const:4:8"]]
+ 007694d4 ["CALL", null, ["ram:a14d8c:8"]]
- 00769494 bytes d7ad0a94
+ 007694d4 bytes 2eae0a94
- 007692d8 ["INT_ADD", "register:40f0:8", ["const:7692d8:8", "const:4:8"]]
- 007692d8 ["CALL", null, ["callee:0054075c:8"]]
+ 00769318 ["INT_ADD", "register:40f0:8", ["const:769318:8", "const:4:8"]]
+ 00769318 ["CALL", null, ["callee:0054075c:8"]]
- 007692d8 bytes 115df797
+ 00769318 bytes 115df797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-236507c091fad87bb569ba07504518ac"></a>

### [`007697b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/007697b4.md) → [`007697f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/007697f4.md) FUN_007697f4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00882090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882090.md) [`00922c2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00922/00922c2c.md) · 呼出先 9件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00767c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00767/00767c74.md) [`00767f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00767/00767f54.md) [`00769220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769220.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 2件 [`008820d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00882/008820d0.md) [`00922dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00922/00922dc8.md) · 呼出先 9件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00767cb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00767/00767cb4.md) [`00767f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00767/00767f94.md) [`00769260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769260.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.14% / 新版 92.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007698f4",
      "incomplete_value": true,
      "site": "00769904",
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
                "const:bcd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007698b4",
      "incomplete_value": true,
      "site": "007698c4",
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
                "const:b8d:8"
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
      "definition_site": "007698f8",
      "incomplete_value": true,
      "site": "00769908",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "007698b8",
      "incomplete_value": true,
      "site": "007698c8",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007698fc",
      "incomplete_value": true,
      "site": "0076990c",
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
      "definition_site": "007698bc",
      "incomplete_value": true,
      "site": "007698cc",
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
      "0076983c",
      "DATA",
      [
        "storage",
        "003c76b8",
        null,
        "uleb128"
      ]
    ],
    [
      "0076984c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00767f54"
      ]
    ],
    [
      "00769850",
      "DATA",
      [
        "storage",
        "003c76e8",
        null,
        "dword"
      ]
    ]
  ],
  "added": [
    [
      "0076983c",
      "DATA",
      [
        "storage",
        "003c76b8",
        null,
        "dword"
      ]
    ],
    [
      "0076984c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00767f94"
      ]
    ],
    [
      "00769850",
      "DATA",
      [
        "storage",
        "003c76e8",
        "fde_003c76e8",
        "dword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0076980c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/007697b4.md#insn-0076980c) · [`00769838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/007697b4.md#insn-00769838) · [`00769844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/007697b4.md#insn-00769844)
- 新版 `0076984c`（命令位置の公開資料なし） · `00769878`（命令位置の公開資料なし） · `00769884`（命令位置の公開資料なし）

~~~diff
- 0076980c ["INT_ADD", "register:40f0:8", ["const:76980c:8", "const:4:8"]]
- 0076980c ["CALL", null, ["ram:767f54:8"]]
+ 0076984c ["INT_ADD", "register:40f0:8", ["const:76984c:8", "const:4:8"]]
+ 0076984c ["CALL", null, ["ram:767f94:8"]]
- 0076980c bytes d2f9ff97
+ 0076984c bytes d2f9ff97
- 00769838 ["INT_ADD", "register:40f0:8", ["const:769838:8", "const:4:8"]]
- 00769838 ["CALL", null, ["callee:00767cb4:8"]]
+ 00769878 ["INT_ADD", "register:40f0:8", ["const:769878:8", "const:4:8"]]
+ 00769878 ["CALL", null, ["callee:00767cb4:8"]]
- 00769838 bytes 0ff9ff97
+ 00769878 bytes 0ff9ff97
- 00769844 ["COPY", "tmp:0:8", ["const:3e3:8"]]
- 00769844 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
- 00769844 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
- 00769844 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
+ 00769884 ["COPY", "tmp:0:8", ["const:4b0:8"]]
+ 00769884 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
+ 00769884 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
+ 00769884 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
- 00769844 bytes d68e0f91
+ 00769884 bytes d6c21291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8c5b70571c72d9e8acf42f1c0d33f85"></a>

### [`007728a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00772/007728a0.md) → [`007728e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00772/007728e0.md) FUN_007728e0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`00914c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00914/00914c94.md) · 呼出先 22件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0043e7e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043e7e8.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00492dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492dc8.md)
- 新版 呼出元 2件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) [`00914e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00914/00914e30.md) · 呼出先 22件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0043e828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e828.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00492e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492e08.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.75% / 新版 92.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 17件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007729b0",
      "incomplete_value": true,
      "site": "007729c4",
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
                "const:2c4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00772970",
      "incomplete_value": true,
      "site": "00772984",
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
                "const:284:8"
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
      "definition_site": "007729b4",
      "incomplete_value": true,
      "site": "007729c8",
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
                "const:9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00772974",
      "incomplete_value": true,
      "site": "00772988",
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
                "const:9:8"
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
      "definition_site": "007729b8",
      "incomplete_value": true,
      "site": "007729cc",
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
                "const:790:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00772978",
      "incomplete_value": true,
      "site": "0077298c",
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
                "const:750:8"
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
      "007729b0",
      "READ",
      [
        "storage",
        "002c0284",
        null,
        "string"
      ]
    ],
    [
      "007729b4",
      "READ",
      [
        "storage",
        "002c028d",
        null,
        "string"
      ]
    ],
    [
      "007729b8",
      "READ",
      [
        "storage",
        "002c2750",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "007729b0",
      "READ",
      [
        "storage",
        "002c02c4",
        null,
        "string"
      ]
    ],
    [
      "007729b4",
      "READ",
      [
        "storage",
        "002c02cd",
        null,
        "string"
      ]
    ],
    [
      "007729b8",
      "READ",
      [
        "storage",
        "002c2790",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0077294c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00772/007728a0.md#insn-0077294c) · [`00772cd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00772/007728a0.md#insn-00772cd4) · [`00772d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00772/007728a0.md#insn-00772d08)
- 新版 `0077298c`（命令位置の公開資料なし） · `00772d14`（命令位置の公開資料なし） · `00772d48`（命令位置の公開資料なし）

~~~diff
- 0077294c ["INT_ADD", "register:40f0:8", ["const:77294c:8", "const:4:8"]]
- 0077294c ["CALL", null, ["callee:00c57eb0:8"]]
+ 0077298c ["INT_ADD", "register:40f0:8", ["const:77298c:8", "const:4:8"]]
+ 0077298c ["CALL", null, ["callee:00c57eb0:8"]]
- 0077294c bytes 59941394
+ 0077298c bytes 49951394
- 00772cd4 ["INT_ADD", "register:40f0:8", ["const:772cd4:8", "const:4:8"]]
- 00772cd4 ["CALL", null, ["callee:006647c0:8"]]
+ 00772d14 ["INT_ADD", "register:40f0:8", ["const:772d14:8", "const:4:8"]]
+ 00772d14 ["CALL", null, ["callee:006647c0:8"]]
- 00772cd4 bytes abc6fb97
+ 00772d14 bytes abc6fb97
- 00772d08 ["INT_ADD", "register:40f0:8", ["const:772d08:8", "const:4:8"]]
- 00772d08 ["CALL", null, ["ram:664860:8"]]
+ 00772d48 ["INT_ADD", "register:40f0:8", ["const:772d48:8", "const:4:8"]]
+ 00772d48 ["CALL", null, ["ram:6648a0:8"]]
- 00772d08 bytes d6c6fb97
+ 00772d48 bytes d6c6fb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9131bc2dbcd83fc3cae099c40497d426"></a>

### [`00773718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773718.md) → [`00773758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/00773758.md) FUN_00773758

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)
- 新版 呼出元 2件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00773798",
      "incomplete_value": false,
      "site": "0077379c",
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
      "definition_site": "00773758",
      "incomplete_value": false,
      "site": "0077375c",
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
      "00773798",
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
      "00773798",
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

- 旧版 [`0077375c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773718.md#insn-0077375c) · [`00773758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773718.md#insn-00773758)
- 新版 `0077379c`（命令位置の公開資料なし） · `00773798`（命令位置の公開資料なし）

~~~diff
- 0077375c ["INT_ADD", "register:40f0:8", ["const:77375c:8", "const:4:8"]]
- 0077375c ["CALL", null, ["callee:00442930:8"]]
+ 0077379c ["INT_ADD", "register:40f0:8", ["const:77379c:8", "const:4:8"]]
+ 0077379c ["CALL", null, ["callee:00442930:8"]]
- 0077375c bytes 653cf397
+ 0077379c bytes 653cf397
- 00773758 ["COPY", "tmp:0:8", ["const:f0:8"]]
- 00773758 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00773758 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00773758 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00773798 ["COPY", "tmp:0:8", ["const:1bd:8"]]
+ 00773798 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00773798 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00773798 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00773758 bytes 00c00391
+ 00773798 bytes 00f40691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1db304df8108d0b06cbf4499cf0bc26"></a>

### [`0077a3d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077a/0077a3d8.md) → [`0077a418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077a/0077a418.md) FUN_0077a418

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00773854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773854.md) · 呼出先 10件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md) [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md) [`0046a8a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046a8a8.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md)
- 新版 呼出元 1件 [`00773894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/00773894.md) · 呼出先 10件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md) [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md) [`0046a8e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046a8e8.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.51% / 新版 95.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `call_target` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0077a450",
      "incomplete_value": true,
      "site": "0077a450",
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
      "definition_site": "0077a410",
      "incomplete_value": true,
      "site": "0077a410",
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
      "definition_site": "0077a458",
      "incomplete_value": false,
      "site": "0077a46c",
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
    "old": {
      "definition_site": "0077a418",
      "incomplete_value": false,
      "site": "0077a42c",
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
            "const:a58:8"
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
      "definition_site": "0077a460",
      "incomplete_value": false,
      "site": "0077a46c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:a08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0077a420",
      "incomplete_value": false,
      "site": "0077a42c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:608:8"
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
      "0077a44c",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "0077a458",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0077a460",
      "PARAM",
      [
        "storage",
        "00c77608",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0077a44c",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "0077a458",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0077a460",
      "PARAM",
      [
        "storage",
        "00c77a08",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0077a420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077a/0077a3d8.md#insn-0077a420) · [`0077a42c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077a/0077a3d8.md#insn-0077a42c) · [`0077a460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077a/0077a3d8.md#insn-0077a460)
- 新版 `0077a460`（命令位置の公開資料なし） · `0077a46c`（命令位置の公開資料なし） · `0077a4a0`（命令位置の公開資料なし）

~~~diff
- 0077a420 ["COPY", "tmp:0:8", ["const:608:8"]]
- 0077a420 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0077a420 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0077a420 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0077a460 ["COPY", "tmp:0:8", ["const:a08:8"]]
+ 0077a460 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0077a460 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0077a460 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0077a420 bytes 42201891
+ 0077a460 bytes 42202891
- 0077a42c ["INT_ADD", "register:40f0:8", ["const:77a42c:8", "const:4:8"]]
- 0077a42c ["CALL", null, ["callee:00c58610:8"]]
+ 0077a46c ["INT_ADD", "register:40f0:8", ["const:77a46c:8", "const:4:8"]]
+ 0077a46c ["CALL", null, ["callee:00c58610:8"]]
- 0077a42c bytes 79771394
+ 0077a46c bytes 69781394
- 0077a460 ["INT_ADD", "register:40f0:8", ["const:77a460:8", "const:4:8"]]
- 0077a460 ["CALL", null, ["ram:46c984:8"]]
+ 0077a4a0 ["INT_ADD", "register:40f0:8", ["const:77a4a0:8", "const:4:8"]]
+ 0077a4a0 ["CALL", null, ["ram:46c9c4:8"]]
- 0077a460 bytes 49c9f397
+ 0077a4a0 bytes 49c9f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ac49f96f24473a97375acb5375b9ab5"></a>

### [`0077ac18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077a/0077ac18.md) → [`0077ac58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077a/0077ac58.md) FUN_0077ac58

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00996ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00996/00996ea0.md) · 呼出先 3件 [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0077b2cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077b/0077b2cc.md)
- 新版 呼出元 1件 [`0099703c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00997/0099703c.md) · 呼出先 3件 [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0077b30c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077b/0077b30c.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.11% / 新版 98.11%

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
      "site": "0077ace4",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0077aca4",
      "value": [
        "leaf",
        "ram:46c984:8"
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
      "0077ace4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ]
  ],
  "added": [
    [
      "0077ace4",
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

- 旧版 [`0077aca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077a/0077ac18.md#insn-0077aca4) · [`0077ac5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077a/0077ac18.md#insn-0077ac5c)
- 新版 `0077ace4`（命令位置の公開資料なし） · `0077ac9c`（命令位置の公開資料なし）

~~~diff
- 0077aca4 ["INT_ADD", "register:40f0:8", ["const:77aca4:8", "const:4:8"]]
- 0077aca4 ["CALL", null, ["ram:46c984:8"]]
+ 0077ace4 ["INT_ADD", "register:40f0:8", ["const:77ace4:8", "const:4:8"]]
+ 0077ace4 ["CALL", null, ["ram:46c9c4:8"]]
- 0077aca4 bytes 38c7f397
+ 0077ace4 bytes 38c7f397
- 0077ac5c ["INT_ADD", "register:40f0:8", ["const:77ac5c:8", "const:4:8"]]
- 0077ac5c ["CALL", null, ["callee:0077b30c:8"]]
+ 0077ac9c ["INT_ADD", "register:40f0:8", ["const:77ac9c:8", "const:4:8"]]
+ 0077ac9c ["CALL", null, ["callee:0077b30c:8"]]
- 0077ac5c bytes 9c010094
+ 0077ac9c bytes 9c010094
~~~


<a id="compare-da543e773e4ef9a7b6a325597f47c95e"></a>

### [`0077af28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077a/0077af28.md) → [`0077af68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077a/0077af68.md) FUN_0077af68

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00b28b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b28/00b28b2c.md) · 呼出先 15件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`004878dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487b40.md)
- 新版 呼出元 1件 [`00b28f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b28/00b28f54.md) · 呼出先 15件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0048791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048791c.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487b80.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 88.69% / 新版 88.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 7件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0077afac",
      "incomplete_value": false,
      "site": "0077afb0",
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
      "definition_site": "0077af6c",
      "incomplete_value": false,
      "site": "0077af70",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0077afcc",
      "incomplete_value": true,
      "site": "0077afdc",
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
                "const:db2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0077af8c",
      "incomplete_value": true,
      "site": "0077af9c",
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
                "const:d72:8"
              ]
            ]
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
      "definition_site": "0077afe0",
      "incomplete_value": true,
      "site": "0077afe0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0077afa0",
      "incomplete_value": true,
      "site": "0077afa0",
      "value": [
        "LOAD",
        "8",
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
      "0077afb0",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "0077afcc",
      "READ",
      [
        "storage",
        "002bdd72",
        null,
        "string"
      ]
    ],
    [
      "0077afd0",
      "READ",
      [
        "storage",
        "002bdd81",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0077afb0",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "0077afcc",
      "READ",
      [
        "storage",
        "002bddb2",
        null,
        "string"
      ]
    ],
    [
      "0077afd0",
      "READ",
      [
        "storage",
        "002bddc1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0077af60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077a/0077af28.md#insn-0077af60) · [`0077afdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077a/0077af28.md#insn-0077afdc) · [`0077b130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077a/0077af28.md#insn-0077b130)
- 新版 `0077afa0`（命令位置の公開資料なし） · `0077b01c`（命令位置の公開資料なし） · `0077b170`（命令位置の公開資料なし）

~~~diff
- 0077af60 ["INT_ADD", "register:40f0:8", ["const:77af60:8", "const:4:8"]]
- 0077af60 ["CALL", null, ["callee:00487e20:8"]]
+ 0077afa0 ["INT_ADD", "register:40f0:8", ["const:77afa0:8", "const:4:8"]]
+ 0077afa0 ["CALL", null, ["callee:00487e20:8"]]
- 0077af60 bytes a033f497
+ 0077afa0 bytes a033f497
- 0077afdc ["INT_ADD", "register:40f0:8", ["const:77afdc:8", "const:4:8"]]
- 0077afdc ["CALL", null, ["callee:0048791c:8"]]
+ 0077b01c ["INT_ADD", "register:40f0:8", ["const:77b01c:8", "const:4:8"]]
+ 0077b01c ["CALL", null, ["callee:0048791c:8"]]
- 0077afdc bytes 4032f497
+ 0077b01c bytes 4032f497
- 0077b130 ["INT_ADD", "register:40f0:8", ["const:77b130:8", "const:4:8"]]
- 0077b130 ["CALL", null, ["callee:00c57fb0:8"]]
+ 0077b170 ["INT_ADD", "register:40f0:8", ["const:77b170:8", "const:4:8"]]
+ 0077b170 ["CALL", null, ["callee:00c57fb0:8"]]
- 0077b130 bytes a0721394
+ 0077b170 bytes 90731394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a72657ace529c540eb341b0052a2a45"></a>

### [`0077b2cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077b/0077b2cc.md) → [`0077b30c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077b/0077b30c.md) FUN_0077b30c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`006b53c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b5/006b53c4.md) [`00773854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773854.md) [`0077ac18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077a/0077ac18.md) · 呼出先 11件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0072c194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072c/0072c194.md) [`0072c29c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072c/0072c29c.md)
- 新版 呼出元 3件 [`006b5404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b5/006b5404.md) [`00773894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/00773894.md) [`0077ac58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077a/0077ac58.md) · 呼出先 11件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0072c1d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072c/0072c1d4.md) [`0072c2dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072c/0072c2dc.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.91% / 新版 98.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

アドレスに依存する影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0077b570",
      "incomplete_value": true,
      "site": "0077b584",
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
                "const:b00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0077b530",
      "incomplete_value": true,
      "site": "0077b544",
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
                "const:ac0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 55,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0077b6cc",
      "incomplete_value": true,
      "site": "0077b6d8",
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
                "const:2f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0077b68c",
      "incomplete_value": true,
      "site": "0077b698",
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
                "const:2b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 77,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0077b83c",
      "incomplete_value": true,
      "site": "0077b850",
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
                "const:80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0077b7fc",
      "incomplete_value": true,
      "site": "0077b810",
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
                "const:40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 104,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0077b358",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "0077b390",
      "READ",
      [
        "storage",
        "00c9b0a8",
        null,
        "pointer"
      ]
    ],
    [
      "0077b3a0",
      "DATA",
      [
        "storage",
        "00ca4084",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0077b358",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "0077b390",
      "READ",
      [
        "storage",
        "00c9b4a8",
        null,
        "pointer"
      ]
    ],
    [
      "0077b3a0",
      "DATA",
      [
        "storage",
        "00ca4484",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0077b318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077b/0077b2cc.md#insn-0077b318) · [`0077b504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077b/0077b2cc.md#insn-0077b504) · [`0077b658`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077b/0077b2cc.md#insn-0077b658)
- 新版 `0077b358`（命令位置の公開資料なし） · `0077b544`（命令位置の公開資料なし） · `0077b698`（命令位置の公開資料なし）

~~~diff
- 0077b318 ["INT_ADD", "register:40f0:8", ["const:77b318:8", "const:4:8"]]
- 0077b318 ["CALL", null, ["ram:46c984:8"]]
+ 0077b358 ["INT_ADD", "register:40f0:8", ["const:77b358:8", "const:4:8"]]
+ 0077b358 ["CALL", null, ["ram:46c9c4:8"]]
- 0077b318 bytes 9bc5f397
+ 0077b358 bytes 9bc5f397
- 0077b504 ["INT_ADD", "register:40f0:8", ["const:77b504:8", "const:4:8"]]
- 0077b504 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0077b544 ["INT_ADD", "register:40f0:8", ["const:77b544:8", "const:4:8"]]
+ 0077b544 ["CALL", null, ["callee:00c57eb0:8"]]
- 0077b504 bytes 6b711394
+ 0077b544 bytes 5b721394
- 0077b658 ["INT_ADD", "register:40f0:8", ["const:77b658:8", "const:4:8"]]
- 0077b658 ["CALL", null, ["callee:00c57eb0:8"]]
+ 0077b698 ["INT_ADD", "register:40f0:8", ["const:77b698:8", "const:4:8"]]
+ 0077b698 ["CALL", null, ["callee:00c57eb0:8"]]
- 0077b658 bytes 16711394
+ 0077b698 bytes 06721394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa6eb3faf84d912076ea0d8a56a534c1"></a>

### [`0077bb80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077b/0077bb80.md) → [`0077bbc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077b/0077bbc0.md) FUN_0077bbc0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0077bff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077b/0077bff4.md) · 呼出先 6件 [`0067e5a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e5a8.md) [`006822e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/006822e4.md) [`007584b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00758/007584b8.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`0077c034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077c/0077c034.md) · 呼出先 6件 [`0067e5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067e/0067e5e8.md) [`00682324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00682/00682324.md) [`007584f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00758/007584f8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.89% / 新版 97.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0077bbdc",
      "incomplete_value": false,
      "site": "0077bbe0",
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
            "const:310:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0077bb9c",
      "incomplete_value": false,
      "site": "0077bba0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:f10:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0077bfb0",
      "incomplete_value": false,
      "site": "0077bfb4",
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
            "const:330:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0077bf70",
      "incomplete_value": false,
      "site": "0077bf74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:f30:8"
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
      "definition_site": "0077bfec",
      "incomplete_value": false,
      "site": "0077bff0",
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
      "definition_site": "0077bfac",
      "incomplete_value": false,
      "site": "0077bfb0",
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
      "0077bbe0",
      "DATA",
      [
        "storage",
        "00c77f10",
        null,
        "pointer"
      ]
    ],
    [
      "0077bfb4",
      "DATA",
      [
        "storage",
        "00c77f30",
        null,
        "pointer"
      ]
    ],
    [
      "0077bff0",
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
      "0077bbe0",
      "DATA",
      [
        "storage",
        "00c78310",
        null,
        "pointer"
      ]
    ],
    [
      "0077bfb4",
      "DATA",
      [
        "storage",
        "00c78330",
        null,
        "pointer"
      ]
    ],
    [
      "0077bff0",
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

- 旧版 [`0077bf70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077b/0077bb80.md#insn-0077bf70) · [`0077bb98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077b/0077bb80.md#insn-0077bb98) · [`0077bb9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077b/0077bb80.md#insn-0077bb9c)
- 新版 `0077bfb0`（命令位置の公開資料なし） · `0077bbd8`（命令位置の公開資料なし） · `0077bbdc`（命令位置の公開資料なし）

~~~diff
- 0077bf70 ["COPY", "tmp:0:8", ["const:f30:8"]]
- 0077bf70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0077bf70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0077bf70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0077bfb0 ["COPY", "tmp:0:8", ["const:330:8"]]
+ 0077bfb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0077bfb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0077bfb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0077bf70 bytes 08c13c91
+ 0077bfb0 bytes 08c10c91
- 0077bb98 ["COPY", "register:4040:8", ["const:c77000:8"]]
+ 0077bbd8 ["COPY", "register:4040:8", ["const:c78000:8"]]
- 0077bb98 bytes e8270090
+ 0077bbd8 bytes e82700b0
- 0077bb9c ["COPY", "tmp:0:8", ["const:f10:8"]]
- 0077bb9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0077bb9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0077bb9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0077bbdc ["COPY", "tmp:0:8", ["const:310:8"]]
+ 0077bbdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0077bbdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0077bbdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0077bb9c bytes 08413c91
+ 0077bbdc bytes 08410c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0bedcc8d906e43688f4da76e18fd3f1d"></a>

### [`0077c018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c018.md) → [`0077c058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077c/0077c058.md) FUN_0077c058

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`006822e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/006822e4.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00682324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00682/00682324.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0077c070",
      "incomplete_value": false,
      "site": "0077c074",
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
            "const:330:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0077c030",
      "incomplete_value": false,
      "site": "0077c034",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:f30:8"
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
      "definition_site": "0077c0ac",
      "incomplete_value": false,
      "site": "0077c0b0",
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
      "definition_site": "0077c06c",
      "incomplete_value": false,
      "site": "0077c070",
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
      "0077c074",
      "DATA",
      [
        "storage",
        "00c77f30",
        null,
        "pointer"
      ]
    ],
    [
      "0077c0b0",
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
      "0077c074",
      "DATA",
      [
        "storage",
        "00c78330",
        null,
        "pointer"
      ]
    ],
    [
      "0077c0b0",
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

- 旧版 [`0077c030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c018.md#insn-0077c030) · [`0077c02c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c018.md#insn-0077c02c) · [`0077c044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c018.md#insn-0077c044)
- 新版 `0077c070`（命令位置の公開資料なし） · `0077c06c`（命令位置の公開資料なし） · `0077c084`（命令位置の公開資料なし）

~~~diff
- 0077c030 ["COPY", "tmp:0:8", ["const:f30:8"]]
- 0077c030 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0077c030 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0077c030 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0077c070 ["COPY", "tmp:0:8", ["const:330:8"]]
+ 0077c070 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0077c070 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0077c070 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0077c030 bytes 08c13c91
+ 0077c070 bytes 08c10c91
- 0077c02c ["COPY", "register:4040:8", ["const:c77000:8"]]
+ 0077c06c ["COPY", "register:4040:8", ["const:c78000:8"]]
- 0077c02c bytes c82700f0
+ 0077c06c bytes e8270090
- 0077c044 ["INT_ADD", "register:40f0:8", ["const:77c044:8", "const:4:8"]]
- 0077c044 ["CALL", null, ["callee:00c53d00:8"]]
+ 0077c084 ["INT_ADD", "register:40f0:8", ["const:77c084:8", "const:4:8"]]
+ 0077c084 ["CALL", null, ["callee:00c53d00:8"]]
- 0077c044 bytes 275e1394
+ 0077c084 bytes 1f5f1394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d8a324876f0025439db880fece01699"></a>

### [`0077c0b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c0b0.md) → [`0077c0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077c/0077c0f0.md) FUN_0077c0f0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`006822e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/006822e4.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00682324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00682/00682324.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0077c108",
      "incomplete_value": true,
      "site": "0077c10c",
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
            "const:330:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0077c0c8",
      "incomplete_value": true,
      "site": "0077c0cc",
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
            "const:f30:8"
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
      "definition_site": "0077c144",
      "incomplete_value": false,
      "site": "0077c148",
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
      "definition_site": "0077c104",
      "incomplete_value": false,
      "site": "0077c108",
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
      "0077c10c",
      "DATA",
      [
        "storage",
        "00c77f30",
        null,
        "pointer"
      ]
    ],
    [
      "0077c148",
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
      "0077c10c",
      "DATA",
      [
        "storage",
        "00c78330",
        null,
        "pointer"
      ]
    ],
    [
      "0077c148",
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

- 旧版 [`0077c0c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c0b0.md#insn-0077c0c8) · [`0077c0c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c0b0.md#insn-0077c0c4) · [`0077c0dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c0b0.md#insn-0077c0dc)
- 新版 `0077c108`（命令位置の公開資料なし） · `0077c104`（命令位置の公開資料なし） · `0077c11c`（命令位置の公開資料なし）

~~~diff
- 0077c0c8 ["COPY", "tmp:0:8", ["const:f30:8"]]
- 0077c0c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0077c0c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0077c0c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0077c108 ["COPY", "tmp:0:8", ["const:330:8"]]
+ 0077c108 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0077c108 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0077c108 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0077c0c8 bytes 08c13c91
+ 0077c108 bytes 08c10c91
- 0077c0c4 ["COPY", "register:4040:8", ["const:c77000:8"]]
+ 0077c104 ["COPY", "register:4040:8", ["const:c78000:8"]]
- 0077c0c4 bytes c82700f0
+ 0077c104 bytes e8270090
- 0077c0dc ["INT_ADD", "register:40f0:8", ["const:77c0dc:8", "const:4:8"]]
- 0077c0dc ["CALL", null, ["callee:00c53d00:8"]]
+ 0077c11c ["INT_ADD", "register:40f0:8", ["const:77c11c:8", "const:4:8"]]
+ 0077c11c ["CALL", null, ["callee:00c53d00:8"]]
- 0077c0dc bytes 015e1394
+ 0077c11c bytes f95e1394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-642a2035ed9a4d716ef18e29af23bd74"></a>

### [`0077c7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c7a0.md) → [`0077c7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077c/0077c7e0.md) FUN_0077c7e0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md)

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
      "definition_site": "0077c7e4",
      "incomplete_value": false,
      "site": "0077c7e8",
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
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0077c7a4",
      "incomplete_value": false,
      "site": "0077c7a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:f50:8"
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
      "0077c7e8",
      "DATA",
      [
        "storage",
        "00c77f50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0077c7e8",
      "DATA",
      [
        "storage",
        "00c78350",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0077c7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c7a0.md#insn-0077c7a0) · [`0077c7a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c7a0.md#insn-0077c7a4)
- 新版 `0077c7e0`（命令位置の公開資料なし） · `0077c7e4`（命令位置の公開資料なし）

~~~diff
- 0077c7a0 ["COPY", "register:4040:8", ["const:c77000:8"]]
+ 0077c7e0 ["COPY", "register:4040:8", ["const:c78000:8"]]
- 0077c7a0 bytes c82700f0
+ 0077c7e0 bytes e8270090
- 0077c7a4 ["COPY", "tmp:0:8", ["const:f50:8"]]
- 0077c7a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0077c7a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0077c7a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0077c7e4 ["COPY", "tmp:0:8", ["const:350:8"]]
+ 0077c7e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0077c7e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0077c7e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0077c7a4 bytes 08413d91
+ 0077c7e4 bytes 08410d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45cd30926a1a69179f62e0c152eecc39"></a>

### [`0077c7b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c7b0.md) → [`0077c7f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077c/0077c7f0.md) FUN_0077c7f0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0077c800",
      "incomplete_value": false,
      "site": "0077c808",
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
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0077c7c0",
      "incomplete_value": false,
      "site": "0077c7c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:f50:8"
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
      "0077c808",
      "DATA",
      [
        "storage",
        "00c77f50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0077c808",
      "DATA",
      [
        "storage",
        "00c78350",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0077c7bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c7b0.md#insn-0077c7bc) · [`0077c7c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c7b0.md#insn-0077c7c0) · [`0077c7cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c7b0.md#insn-0077c7cc)
- 新版 `0077c7fc`（命令位置の公開資料なし） · `0077c800`（命令位置の公開資料なし） · `0077c80c`（命令位置の公開資料なし）

~~~diff
- 0077c7bc ["COPY", "register:4040:8", ["const:c77000:8"]]
+ 0077c7fc ["COPY", "register:4040:8", ["const:c78000:8"]]
- 0077c7bc bytes c82700f0
+ 0077c7fc bytes e8270090
- 0077c7c0 ["COPY", "tmp:0:8", ["const:f50:8"]]
- 0077c7c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0077c7c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0077c7c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0077c800 ["COPY", "tmp:0:8", ["const:350:8"]]
+ 0077c800 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0077c800 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0077c800 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0077c7c0 bytes 08413d91
+ 0077c800 bytes 08410d91
- 0077c7cc ["INT_ADD", "register:40f0:8", ["const:77c7cc:8", "const:4:8"]]
- 0077c7cc ["CALL", null, ["callee:00c57ea0:8"]]
+ 0077c80c ["INT_ADD", "register:40f0:8", ["const:77c80c:8", "const:4:8"]]
+ 0077c80c ["CALL", null, ["callee:00c57ea0:8"]]
- 0077c7cc bytes b56c1394
+ 0077c80c bytes a56d1394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8bc198c55c513e20c37b2822bede3721"></a>

### [`0077c80c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c80c.md) → [`0077c84c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077c/0077c84c.md) FUN_0077c84c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 8件 [`0077365c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/0077365c.md) [`007837b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/007837b4.md) [`00783894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/00783894.md) [`00a2f434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2f/00a2f434.md) [`00a2fc90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2f/00a2fc90.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 8件 [`0077369c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/0077369c.md) [`007837f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00783/007837f4.md) [`007838d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00783/007838d4.md) [`00a2f62c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2f/00a2f62c.md) [`00a2fe88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2f/00a2fe88.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "0077c858",
      "incomplete_value": false,
      "site": "0077c85c",
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
      "definition_site": "0077c818",
      "incomplete_value": false,
      "site": "0077c81c",
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
      "0077c858",
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
      "0077c858",
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

- 旧版 [`0077c81c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c80c.md#insn-0077c81c) · [`0077c818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c80c.md#insn-0077c818)
- 新版 `0077c85c`（命令位置の公開資料なし） · `0077c858`（命令位置の公開資料なし）

~~~diff
- 0077c81c ["INT_ADD", "register:40f0:8", ["const:77c81c:8", "const:4:8"]]
- 0077c81c ["CALL", null, ["callee:0043b778:8"]]
+ 0077c85c ["INT_ADD", "register:40f0:8", ["const:77c85c:8", "const:4:8"]]
+ 0077c85c ["CALL", null, ["callee:0043b778:8"]]
- 0077c81c bytes c7fbf297
+ 0077c85c bytes c7fbf297
- 0077c818 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 0077c818 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0077c818 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0077c818 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0077c858 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 0077c858 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0077c858 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0077c858 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0077c818 bytes 00303c91
+ 0077c858 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61de3783988e69a01148dad9864413b7"></a>

### [`0077ca54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077ca54.md) → [`0077ca94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077c/0077ca94.md) FUN_0077ca94

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0077c8d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c8d0.md) [`0077ca54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077ca54.md) · 呼出先 21件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 2件 [`0077c910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077c/0077c910.md) [`0077ca94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077c/0077ca94.md) · 呼出先 21件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.88% / 新版 98.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0077cc30",
      "incomplete_value": false,
      "site": "0077cc38",
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
    "old": {
      "definition_site": "0077cbf0",
      "incomplete_value": false,
      "site": "0077cbf8",
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
            "const:f13:8"
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
      "definition_site": "0077cce8",
      "incomplete_value": false,
      "site": "0077ccf0",
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
    "old": {
      "definition_site": "0077cca8",
      "incomplete_value": false,
      "site": "0077ccb0",
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
            "const:da7:8"
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
      "definition_site": "0077cd04",
      "incomplete_value": false,
      "site": "0077cd10",
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
    "old": {
      "definition_site": "0077ccc4",
      "incomplete_value": false,
      "site": "0077ccd0",
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
            "const:ea9:8"
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
      "0077cc30",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "0077cce8",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ],
    [
      "0077cd04",
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0077cc30",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "0077cce8",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ],
    [
      "0077cd04",
      "PARAM",
      [
        "storage",
        "002c0ee9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0077cbf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077ca54.md#insn-0077cbf8) · [`0077ccb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077ca54.md#insn-0077ccb0) · [`0077ccd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077ca54.md#insn-0077ccd0)
- 新版 `0077cc38`（命令位置の公開資料なし） · `0077ccf0`（命令位置の公開資料なし） · `0077cd10`（命令位置の公開資料なし）

~~~diff
- 0077cbf8 ["INT_ADD", "register:40f0:8", ["const:77cbf8:8", "const:4:8"]]
- 0077cbf8 ["CALL", null, ["callee:00441e94:8"]]
+ 0077cc38 ["INT_ADD", "register:40f0:8", ["const:77cc38:8", "const:4:8"]]
+ 0077cc38 ["CALL", null, ["callee:00441e94:8"]]
- 0077cbf8 bytes 9714f397
+ 0077cc38 bytes 9714f397
- 0077ccb0 ["INT_ADD", "register:40f0:8", ["const:77ccb0:8", "const:4:8"]]
- 0077ccb0 ["CALL", null, ["callee:00441e94:8"]]
+ 0077ccf0 ["INT_ADD", "register:40f0:8", ["const:77ccf0:8", "const:4:8"]]
+ 0077ccf0 ["CALL", null, ["callee:00441e94:8"]]
- 0077ccb0 bytes 6914f397
+ 0077ccf0 bytes 6914f397
- 0077ccd0 ["INT_ADD", "register:40f0:8", ["const:77ccd0:8", "const:4:8"]]
- 0077ccd0 ["CALL", null, ["callee:004427f4:8"]]
+ 0077cd10 ["INT_ADD", "register:40f0:8", ["const:77cd10:8", "const:4:8"]]
+ 0077cd10 ["CALL", null, ["callee:004427f4:8"]]
- 0077ccd0 bytes b916f397
+ 0077cd10 bytes b916f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28572050daac5a164c8d04dafddab6d5"></a>

### [`0077d53c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077d/0077d53c.md) → [`0077d57c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077d/0077d57c.md) FUN_0077d57c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0077ca54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077ca54.md) [`0077d53c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077d/0077d53c.md) · 呼出先 23件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 2件 [`0077ca94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077c/0077ca94.md) [`0077d57c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077d/0077d57c.md) · 呼出先 23件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.90% / 新版 98.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0077d6f4",
      "incomplete_value": false,
      "site": "0077d6fc",
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
    "old": {
      "definition_site": "0077d6b4",
      "incomplete_value": false,
      "site": "0077d6bc",
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
            "const:f13:8"
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
      "definition_site": "0077d7b0",
      "incomplete_value": false,
      "site": "0077d7b8",
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
    "old": {
      "definition_site": "0077d770",
      "incomplete_value": false,
      "site": "0077d778",
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
            "const:da7:8"
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
      "definition_site": "0077d7c8",
      "incomplete_value": false,
      "site": "0077d7d4",
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
    "old": {
      "definition_site": "0077d788",
      "incomplete_value": false,
      "site": "0077d794",
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
            "const:ea9:8"
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
      "0077d6f4",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "0077d7b0",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ],
    [
      "0077d7c8",
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0077d6f4",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "0077d7b0",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ],
    [
      "0077d7c8",
      "PARAM",
      [
        "storage",
        "002c0ee9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0077d6bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077d/0077d53c.md#insn-0077d6bc) · [`0077d778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077d/0077d53c.md#insn-0077d778) · [`0077d794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077d/0077d53c.md#insn-0077d794)
- 新版 `0077d6fc`（命令位置の公開資料なし） · `0077d7b8`（命令位置の公開資料なし） · `0077d7d4`（命令位置の公開資料なし）

~~~diff
- 0077d6bc ["INT_ADD", "register:40f0:8", ["const:77d6bc:8", "const:4:8"]]
- 0077d6bc ["CALL", null, ["callee:00441e94:8"]]
+ 0077d6fc ["INT_ADD", "register:40f0:8", ["const:77d6fc:8", "const:4:8"]]
+ 0077d6fc ["CALL", null, ["callee:00441e94:8"]]
- 0077d6bc bytes e611f397
+ 0077d6fc bytes e611f397
- 0077d778 ["INT_ADD", "register:40f0:8", ["const:77d778:8", "const:4:8"]]
- 0077d778 ["CALL", null, ["callee:00441e94:8"]]
+ 0077d7b8 ["INT_ADD", "register:40f0:8", ["const:77d7b8:8", "const:4:8"]]
+ 0077d7b8 ["CALL", null, ["callee:00441e94:8"]]
- 0077d778 bytes b711f397
+ 0077d7b8 bytes b711f397
- 0077d794 ["INT_ADD", "register:40f0:8", ["const:77d794:8", "const:4:8"]]
- 0077d794 ["CALL", null, ["callee:004427f4:8"]]
+ 0077d7d4 ["INT_ADD", "register:40f0:8", ["const:77d7d4:8", "const:4:8"]]
+ 0077d7d4 ["CALL", null, ["callee:004427f4:8"]]
- 0077d794 bytes 0814f397
+ 0077d7d4 bytes 0814f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2864a37d0a69c4ccb2d8eca6295922d9"></a>

### [`0077e0a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077e/0077e0a4.md) → [`0077e0e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077e/0077e0e4.md) FUN_0077e0e4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0077d53c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077d/0077d53c.md) [`0077e0a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077e/0077e0a4.md) · 呼出先 22件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 2件 [`0077d57c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077d/0077d57c.md) [`0077e0e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077e/0077e0e4.md) · 呼出先 22件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.74% / 新版 98.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0077e254",
      "incomplete_value": false,
      "site": "0077e25c",
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
    "old": {
      "definition_site": "0077e214",
      "incomplete_value": false,
      "site": "0077e21c",
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
            "const:f13:8"
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
      "definition_site": "0077e278",
      "incomplete_value": false,
      "site": "0077e284",
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
    "old": {
      "definition_site": "0077e238",
      "incomplete_value": false,
      "site": "0077e244",
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
            "const:ea9:8"
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
      "definition_site": "0077e454",
      "incomplete_value": false,
      "site": "0077e460",
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
      "definition_site": "0077e414",
      "incomplete_value": false,
      "site": "0077e420",
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
      "0077e254",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "0077e278",
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ],
    [
      "0077e3ac",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0077e254",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "0077e278",
      "PARAM",
      [
        "storage",
        "002c0ee9",
        null,
        "string"
      ]
    ],
    [
      "0077e3ac",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0077e21c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077e/0077e0a4.md#insn-0077e21c) · [`0077e244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077e/0077e0a4.md#insn-0077e244) · [`0077e420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077e/0077e0a4.md#insn-0077e420)
- 新版 `0077e25c`（命令位置の公開資料なし） · `0077e284`（命令位置の公開資料なし） · `0077e460`（命令位置の公開資料なし）

~~~diff
- 0077e21c ["INT_ADD", "register:40f0:8", ["const:77e21c:8", "const:4:8"]]
- 0077e21c ["CALL", null, ["callee:00441e94:8"]]
+ 0077e25c ["INT_ADD", "register:40f0:8", ["const:77e25c:8", "const:4:8"]]
+ 0077e25c ["CALL", null, ["callee:00441e94:8"]]
- 0077e21c bytes 0e0ff397
+ 0077e25c bytes 0e0ff397
- 0077e244 ["INT_ADD", "register:40f0:8", ["const:77e244:8", "const:4:8"]]
- 0077e244 ["CALL", null, ["callee:004427f4:8"]]
+ 0077e284 ["INT_ADD", "register:40f0:8", ["const:77e284:8", "const:4:8"]]
+ 0077e284 ["CALL", null, ["callee:004427f4:8"]]
- 0077e244 bytes 5c11f397
+ 0077e284 bytes 5c11f397
- 0077e420 ["INT_ADD", "register:40f0:8", ["const:77e420:8", "const:4:8"]]
- 0077e420 ["CALL", null, ["callee:00441cec:8"]]
+ 0077e460 ["INT_ADD", "register:40f0:8", ["const:77e460:8", "const:4:8"]]
+ 0077e460 ["CALL", null, ["callee:00441cec:8"]]
- 0077e420 bytes 230ef397
+ 0077e460 bytes 230ef397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b13d3e690434bed130b9caa34a25fb58"></a>

### [`0077ea50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077e/0077ea50.md) → [`0077ea90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077e/0077ea90.md) FUN_0077ea90

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0077e0a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077e/0077e0a4.md) [`0077ea50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077e/0077ea50.md) · 呼出先 22件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 2件 [`0077e0e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077e/0077e0e4.md) [`0077ea90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077e/0077ea90.md) · 呼出先 22件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.71% / 新版 98.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0077ebf8",
      "incomplete_value": false,
      "site": "0077ec00",
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
    "old": {
      "definition_site": "0077ebb8",
      "incomplete_value": false,
      "site": "0077ebc0",
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
            "const:f13:8"
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
      "definition_site": "0077ec1c",
      "incomplete_value": false,
      "site": "0077ec28",
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
    "old": {
      "definition_site": "0077ebdc",
      "incomplete_value": false,
      "site": "0077ebe8",
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
            "const:ea9:8"
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
      "definition_site": "0077ed50",
      "incomplete_value": false,
      "site": "0077ed58",
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
    "old": {
      "definition_site": "0077ed10",
      "incomplete_value": false,
      "site": "0077ed18",
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
            "const:da7:8"
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
      "0077ebf8",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "0077ec1c",
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ],
    [
      "0077ed50",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0077ebf8",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "0077ec1c",
      "PARAM",
      [
        "storage",
        "002c0ee9",
        null,
        "string"
      ]
    ],
    [
      "0077ed50",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0077ebc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077e/0077ea50.md#insn-0077ebc0) · [`0077ebe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077e/0077ea50.md#insn-0077ebe8) · [`0077ed18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077e/0077ea50.md#insn-0077ed18)
- 新版 `0077ec00`（命令位置の公開資料なし） · `0077ec28`（命令位置の公開資料なし） · `0077ed58`（命令位置の公開資料なし）

~~~diff
- 0077ebc0 ["INT_ADD", "register:40f0:8", ["const:77ebc0:8", "const:4:8"]]
- 0077ebc0 ["CALL", null, ["callee:00441e94:8"]]
+ 0077ec00 ["INT_ADD", "register:40f0:8", ["const:77ec00:8", "const:4:8"]]
+ 0077ec00 ["CALL", null, ["callee:00441e94:8"]]
- 0077ebc0 bytes a50cf397
+ 0077ec00 bytes a50cf397
- 0077ebe8 ["INT_ADD", "register:40f0:8", ["const:77ebe8:8", "const:4:8"]]
- 0077ebe8 ["CALL", null, ["callee:004427f4:8"]]
+ 0077ec28 ["INT_ADD", "register:40f0:8", ["const:77ec28:8", "const:4:8"]]
+ 0077ec28 ["CALL", null, ["callee:004427f4:8"]]
- 0077ebe8 bytes f30ef397
+ 0077ec28 bytes f30ef397
- 0077ed18 ["INT_ADD", "register:40f0:8", ["const:77ed18:8", "const:4:8"]]
- 0077ed18 ["CALL", null, ["callee:00441e94:8"]]
+ 0077ed58 ["INT_ADD", "register:40f0:8", ["const:77ed58:8", "const:4:8"]]
+ 0077ed58 ["CALL", null, ["callee:00441e94:8"]]
- 0077ed18 bytes 4f0cf397
+ 0077ed58 bytes 4f0cf397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ca23d2bb3fbe2c3e1fdc50de5f825e4"></a>

### [`0077f3d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077f/0077f3d4.md) → [`0077f414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077f/0077f414.md) FUN_0077f414

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0077ea50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077e/0077ea50.md) [`0077f3d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077f/0077f3d4.md) · 呼出先 22件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 2件 [`0077ea90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077e/0077ea90.md) [`0077f414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077f/0077f414.md) · 呼出先 22件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.70% / 新版 98.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0077f578",
      "incomplete_value": false,
      "site": "0077f580",
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
    "old": {
      "definition_site": "0077f538",
      "incomplete_value": false,
      "site": "0077f540",
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
            "const:f13:8"
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
      "definition_site": "0077f59c",
      "incomplete_value": false,
      "site": "0077f5a8",
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
    "old": {
      "definition_site": "0077f55c",
      "incomplete_value": false,
      "site": "0077f568",
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
            "const:ea9:8"
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
      "definition_site": "0077f6d0",
      "incomplete_value": false,
      "site": "0077f6d8",
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
    "old": {
      "definition_site": "0077f690",
      "incomplete_value": false,
      "site": "0077f698",
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
            "const:da7:8"
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
      "0077f578",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "0077f59c",
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ],
    [
      "0077f6d0",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0077f578",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "0077f59c",
      "PARAM",
      [
        "storage",
        "002c0ee9",
        null,
        "string"
      ]
    ],
    [
      "0077f6d0",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0077f540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077f/0077f3d4.md#insn-0077f540) · [`0077f568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077f/0077f3d4.md#insn-0077f568) · [`0077f698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077f/0077f3d4.md#insn-0077f698)
- 新版 `0077f580`（命令位置の公開資料なし） · `0077f5a8`（命令位置の公開資料なし） · `0077f6d8`（命令位置の公開資料なし）

~~~diff
- 0077f540 ["INT_ADD", "register:40f0:8", ["const:77f540:8", "const:4:8"]]
- 0077f540 ["CALL", null, ["callee:00441e94:8"]]
+ 0077f580 ["INT_ADD", "register:40f0:8", ["const:77f580:8", "const:4:8"]]
+ 0077f580 ["CALL", null, ["callee:00441e94:8"]]
- 0077f540 bytes 450af397
+ 0077f580 bytes 450af397
- 0077f568 ["INT_ADD", "register:40f0:8", ["const:77f568:8", "const:4:8"]]
- 0077f568 ["CALL", null, ["callee:004427f4:8"]]
+ 0077f5a8 ["INT_ADD", "register:40f0:8", ["const:77f5a8:8", "const:4:8"]]
+ 0077f5a8 ["CALL", null, ["callee:004427f4:8"]]
- 0077f568 bytes 930cf397
+ 0077f5a8 bytes 930cf397
- 0077f698 ["INT_ADD", "register:40f0:8", ["const:77f698:8", "const:4:8"]]
- 0077f698 ["CALL", null, ["callee:00441e94:8"]]
+ 0077f6d8 ["INT_ADD", "register:40f0:8", ["const:77f6d8:8", "const:4:8"]]
+ 0077f6d8 ["CALL", null, ["callee:00441e94:8"]]
- 0077f698 bytes ef09f397
+ 0077f6d8 bytes ef09f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-870700abe0d52a41f5873f461a00539f"></a>

### [`0077fd40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077f/0077fd40.md) → [`0077fd80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077f/0077fd80.md) FUN_0077fd80

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0077f3d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077f/0077f3d4.md) [`0077fd40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077f/0077fd40.md) · 呼出先 22件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 2件 [`0077f414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077f/0077f414.md) [`0077fd80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077f/0077fd80.md) · 呼出先 22件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.70% / 新版 98.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0077fee4",
      "incomplete_value": false,
      "site": "0077feec",
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
    "old": {
      "definition_site": "0077fea4",
      "incomplete_value": false,
      "site": "0077feac",
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
            "const:f13:8"
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
      "definition_site": "0077ff08",
      "incomplete_value": false,
      "site": "0077ff14",
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
    "old": {
      "definition_site": "0077fec8",
      "incomplete_value": false,
      "site": "0077fed4",
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
            "const:ea9:8"
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
      "definition_site": "0078003c",
      "incomplete_value": false,
      "site": "00780044",
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
    "old": {
      "definition_site": "0077fffc",
      "incomplete_value": false,
      "site": "00780004",
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
            "const:da7:8"
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
      "0077fee4",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "0077ff08",
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ],
    [
      "0078003c",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0077fee4",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "0077ff08",
      "PARAM",
      [
        "storage",
        "002c0ee9",
        null,
        "string"
      ]
    ],
    [
      "0078003c",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0077feac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077f/0077fd40.md#insn-0077feac) · [`0077fed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077f/0077fd40.md#insn-0077fed4) · [`00780004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077f/0077fd40.md#insn-00780004)
- 新版 `0077feec`（命令位置の公開資料なし） · `0077ff14`（命令位置の公開資料なし） · `00780044`（命令位置の公開資料なし）

~~~diff
- 0077feac ["INT_ADD", "register:40f0:8", ["const:77feac:8", "const:4:8"]]
- 0077feac ["CALL", null, ["callee:00441e94:8"]]
+ 0077feec ["INT_ADD", "register:40f0:8", ["const:77feec:8", "const:4:8"]]
+ 0077feec ["CALL", null, ["callee:00441e94:8"]]
- 0077feac bytes ea07f397
+ 0077feec bytes ea07f397
- 0077fed4 ["INT_ADD", "register:40f0:8", ["const:77fed4:8", "const:4:8"]]
- 0077fed4 ["CALL", null, ["callee:004427f4:8"]]
+ 0077ff14 ["INT_ADD", "register:40f0:8", ["const:77ff14:8", "const:4:8"]]
+ 0077ff14 ["CALL", null, ["callee:004427f4:8"]]
- 0077fed4 bytes 380af397
+ 0077ff14 bytes 380af397
- 00780004 ["INT_ADD", "register:40f0:8", ["const:780004:8", "const:4:8"]]
- 00780004 ["CALL", null, ["callee:00441e94:8"]]
+ 00780044 ["INT_ADD", "register:40f0:8", ["const:780044:8", "const:4:8"]]
+ 00780044 ["CALL", null, ["callee:00441e94:8"]]
- 00780004 bytes 9407f397
+ 00780044 bytes 9407f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c94ab84c207ca877b6239c8496bea98"></a>

### [`007806ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00780/007806ac.md) → [`007806ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00780/007806ec.md) FUN_007806ec

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0077fd40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077f/0077fd40.md) [`007806ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00780/007806ac.md) · 呼出先 22件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 2件 [`0077fd80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077f/0077fd80.md) [`007806ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00780/007806ec.md) · 呼出先 22件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.69% / 新版 98.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0078084c",
      "incomplete_value": false,
      "site": "00780854",
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
    "old": {
      "definition_site": "0078080c",
      "incomplete_value": false,
      "site": "00780814",
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
            "const:f13:8"
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
      "definition_site": "00780870",
      "incomplete_value": false,
      "site": "0078087c",
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
    "old": {
      "definition_site": "00780830",
      "incomplete_value": false,
      "site": "0078083c",
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
            "const:ea9:8"
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
      "definition_site": "007809a4",
      "incomplete_value": false,
      "site": "007809ac",
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
    "old": {
      "definition_site": "00780964",
      "incomplete_value": false,
      "site": "0078096c",
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
            "const:da7:8"
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
      "0078084c",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "00780870",
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ],
    [
      "007809a4",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0078084c",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "00780870",
      "PARAM",
      [
        "storage",
        "002c0ee9",
        null,
        "string"
      ]
    ],
    [
      "007809a4",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00780814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00780/007806ac.md#insn-00780814) · [`0078083c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00780/007806ac.md#insn-0078083c) · [`0078096c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00780/007806ac.md#insn-0078096c)
- 新版 `00780854`（命令位置の公開資料なし） · `0078087c`（命令位置の公開資料なし） · `007809ac`（命令位置の公開資料なし）

~~~diff
- 00780814 ["INT_ADD", "register:40f0:8", ["const:780814:8", "const:4:8"]]
- 00780814 ["CALL", null, ["callee:00441e94:8"]]
+ 00780854 ["INT_ADD", "register:40f0:8", ["const:780854:8", "const:4:8"]]
+ 00780854 ["CALL", null, ["callee:00441e94:8"]]
- 00780814 bytes 9005f397
+ 00780854 bytes 9005f397
- 0078083c ["INT_ADD", "register:40f0:8", ["const:78083c:8", "const:4:8"]]
- 0078083c ["CALL", null, ["callee:004427f4:8"]]
+ 0078087c ["INT_ADD", "register:40f0:8", ["const:78087c:8", "const:4:8"]]
+ 0078087c ["CALL", null, ["callee:004427f4:8"]]
- 0078083c bytes de07f397
+ 0078087c bytes de07f397
- 0078096c ["INT_ADD", "register:40f0:8", ["const:78096c:8", "const:4:8"]]
- 0078096c ["CALL", null, ["callee:00441e94:8"]]
+ 007809ac ["INT_ADD", "register:40f0:8", ["const:7809ac:8", "const:4:8"]]
+ 007809ac ["CALL", null, ["callee:00441e94:8"]]
- 0078096c bytes 3a05f397
+ 007809ac bytes 3a05f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fcc9791cac33de31aa7d3f94b7cffef"></a>

### [`00781004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781004.md) → [`00781044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00781/00781044.md) FUN_00781044

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`007806ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00780/007806ac.md) [`00781004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781004.md) [`00a5e2cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a5e/00a5e2cc.md) · 呼出先 22件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)
- 新版 呼出元 3件 [`007806ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00780/007806ec.md) [`00781044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00781/00781044.md) [`00a5e4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a5e/00a5e4c4.md) · 呼出先 22件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f70.md) [`00441cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441cec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.70% / 新版 98.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007811a4",
      "incomplete_value": false,
      "site": "007811ac",
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
    "old": {
      "definition_site": "00781164",
      "incomplete_value": false,
      "site": "0078116c",
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
            "const:f13:8"
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
      "definition_site": "007811c8",
      "incomplete_value": false,
      "site": "007811d4",
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
    "old": {
      "definition_site": "00781188",
      "incomplete_value": false,
      "site": "00781194",
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
            "const:ea9:8"
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
      "definition_site": "007812fc",
      "incomplete_value": false,
      "site": "00781304",
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
    "old": {
      "definition_site": "007812bc",
      "incomplete_value": false,
      "site": "007812c4",
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
            "const:da7:8"
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
      "007811a4",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "007811c8",
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ],
    [
      "007812fc",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "007811a4",
      "PARAM",
      [
        "storage",
        "002b7f53",
        null,
        null
      ]
    ],
    [
      "007811c8",
      "PARAM",
      [
        "storage",
        "002c0ee9",
        null,
        "string"
      ]
    ],
    [
      "007812fc",
      "PARAM",
      [
        "storage",
        "002b5de7",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078116c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781004.md#insn-0078116c) · [`00781194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781004.md#insn-00781194) · [`007812c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781004.md#insn-007812c4)
- 新版 `007811ac`（命令位置の公開資料なし） · `007811d4`（命令位置の公開資料なし） · `00781304`（命令位置の公開資料なし）

~~~diff
- 0078116c ["INT_ADD", "register:40f0:8", ["const:78116c:8", "const:4:8"]]
- 0078116c ["CALL", null, ["callee:00441e94:8"]]
+ 007811ac ["INT_ADD", "register:40f0:8", ["const:7811ac:8", "const:4:8"]]
+ 007811ac ["CALL", null, ["callee:00441e94:8"]]
- 0078116c bytes 3a03f397
+ 007811ac bytes 3a03f397
- 00781194 ["INT_ADD", "register:40f0:8", ["const:781194:8", "const:4:8"]]
- 00781194 ["CALL", null, ["callee:004427f4:8"]]
+ 007811d4 ["INT_ADD", "register:40f0:8", ["const:7811d4:8", "const:4:8"]]
+ 007811d4 ["CALL", null, ["callee:004427f4:8"]]
- 00781194 bytes 8805f397
+ 007811d4 bytes 8805f397
- 007812c4 ["INT_ADD", "register:40f0:8", ["const:7812c4:8", "const:4:8"]]
- 007812c4 ["CALL", null, ["callee:00441e94:8"]]
+ 00781304 ["INT_ADD", "register:40f0:8", ["const:781304:8", "const:4:8"]]
+ 00781304 ["CALL", null, ["callee:00441e94:8"]]
- 007812c4 bytes e402f397
+ 00781304 bytes e402f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f590ca01e4a3d3869c07088ef565cb5d"></a>

### [`00781978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781978.md) → [`007819b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00781/007819b8.md) FUN_007819b8

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
      "definition_site": "007819dc",
      "incomplete_value": false,
      "site": "007819dc",
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
            "const:3a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078199c",
      "incomplete_value": false,
      "site": "0078199c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
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
      "007819dc",
      "DATA",
      [
        "storage",
        "00c77fa0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007819dc",
      "DATA",
      [
        "storage",
        "00c783a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078198c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781978.md#insn-0078198c) · [`00781994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781978.md#insn-00781994) · [`00781998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781978.md#insn-00781998)
- 新版 `007819cc`（命令位置の公開資料なし） · `007819d4`（命令位置の公開資料なし） · `007819d8`（命令位置の公開資料なし）

~~~diff
- 0078198c ["INT_ADD", "register:40f0:8", ["const:78198c:8", "const:4:8"]]
- 0078198c ["CALL", null, ["callee:00c57e90:8"]]
+ 007819cc ["INT_ADD", "register:40f0:8", ["const:7819cc:8", "const:4:8"]]
+ 007819cc ["CALL", null, ["callee:00c57e90:8"]]
- 0078198c bytes 41581394
+ 007819cc bytes 31591394
- 00781994 ["COPY", "register:4040:8", ["const:c77000:8"]]
+ 007819d4 ["COPY", "register:4040:8", ["const:c78000:8"]]
- 00781994 bytes a82700d0
+ 007819d4 bytes a82700f0
- 00781998 ["COPY", "tmp:0:8", ["const:fa0:8"]]
- 00781998 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00781998 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00781998 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007819d8 ["COPY", "tmp:0:8", ["const:3a0:8"]]
+ 007819d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007819d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007819d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00781998 bytes 08813e91
+ 007819d8 bytes 08810e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f9631cdec8d03e0646398f3e77c4dbd"></a>

### [`007819c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/007819c8.md) → [`00781a08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00781/00781a08.md) FUN_00781a08

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md)

変更の種類 call, call_target, constant, operands_and_dependencies

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
      "definition_site": null,
      "incomplete_value": true,
      "site": "00781a28",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007819e8",
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
      "site": "00781a34",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007819f4",
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
      "00781a28",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00781a34",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00781a28",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00781a34",
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

- 旧版 [`007819e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/007819c8.md#insn-007819e8) · [`007819f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/007819c8.md#insn-007819f4)
- 新版 `00781a28`（命令位置の公開資料なし） · `00781a34`（命令位置の公開資料なし）

~~~diff
- 007819e8 ["INT_ADD", "register:40f0:8", ["const:7819e8:8", "const:4:8"]]
- 007819e8 ["CALL", null, ["ram:47acb4:8"]]
+ 00781a28 ["INT_ADD", "register:40f0:8", ["const:781a28:8", "const:4:8"]]
+ 00781a28 ["CALL", null, ["ram:47acf4:8"]]
- 007819e8 bytes b3e4f397
+ 00781a28 bytes b3e4f397
- 007819f4 ["INT_ADD", "register:40f0:8", ["const:7819f4:8", "const:4:8"]]
- 007819f4 ["CALL", null, ["ram:47acb4:8"]]
+ 00781a34 ["INT_ADD", "register:40f0:8", ["const:781a34:8", "const:4:8"]]
+ 00781a34 ["CALL", null, ["ram:47acf4:8"]]
- 007819f4 bytes b0e4f397
+ 00781a34 bytes b0e4f397
~~~


<a id="compare-756da7eba358d94cba6fbb217bdd2664"></a>

### [`00781a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781a60.md) → [`00781aa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00781/00781aa0.md) FUN_00781aa0

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
      "definition_site": "00781ac4",
      "incomplete_value": false,
      "site": "00781ac4",
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
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00781a84",
      "incomplete_value": false,
      "site": "00781a84",
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
      "00781ac4",
      "DATA",
      [
        "storage",
        "00c78020",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00781ac4",
      "DATA",
      [
        "storage",
        "00c78420",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00781a74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781a60.md#insn-00781a74) · [`00781a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781a60.md#insn-00781a80)
- 新版 `00781ab4`（命令位置の公開資料なし） · `00781ac0`（命令位置の公開資料なし）

~~~diff
- 00781a74 ["INT_ADD", "register:40f0:8", ["const:781a74:8", "const:4:8"]]
- 00781a74 ["CALL", null, ["callee:00c57e90:8"]]
+ 00781ab4 ["INT_ADD", "register:40f0:8", ["const:781ab4:8", "const:4:8"]]
+ 00781ab4 ["CALL", null, ["callee:00c57e90:8"]]
- 00781a74 bytes 07581394
+ 00781ab4 bytes f7581394
- 00781a80 ["COPY", "tmp:0:8", ["const:20:8"]]
- 00781a80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00781a80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00781a80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00781ac0 ["COPY", "tmp:0:8", ["const:420:8"]]
+ 00781ac0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00781ac0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00781ac0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00781a80 bytes 08810091
+ 00781ac0 bytes 08811091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-079c76d90a1bd119881f584d9c53f187"></a>

### [`00781b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781b40.md) → [`00781b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00781/00781b80.md) FUN_00781b80

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
      "definition_site": "00781ba4",
      "incomplete_value": false,
      "site": "00781ba4",
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
            "const:4a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00781b64",
      "incomplete_value": false,
      "site": "00781b64",
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
            "const:a0:8"
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
      "00781ba4",
      "DATA",
      [
        "storage",
        "00c780a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00781ba4",
      "DATA",
      [
        "storage",
        "00c784a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00781b54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781b40.md#insn-00781b54) · [`00781b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781b40.md#insn-00781b60)
- 新版 `00781b94`（命令位置の公開資料なし） · `00781ba0`（命令位置の公開資料なし）

~~~diff
- 00781b54 ["INT_ADD", "register:40f0:8", ["const:781b54:8", "const:4:8"]]
- 00781b54 ["CALL", null, ["callee:00c57e90:8"]]
+ 00781b94 ["INT_ADD", "register:40f0:8", ["const:781b94:8", "const:4:8"]]
+ 00781b94 ["CALL", null, ["callee:00c57e90:8"]]
- 00781b54 bytes cf571394
+ 00781b94 bytes bf581394
- 00781b60 ["COPY", "tmp:0:8", ["const:a0:8"]]
- 00781b60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00781b60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00781b60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00781ba0 ["COPY", "tmp:0:8", ["const:4a0:8"]]
+ 00781ba0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00781ba0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00781ba0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00781b60 bytes 08810291
+ 00781ba0 bytes 08811291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a940922fa0e6f52e879d56b9a34551a8"></a>

### [`00781b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781b90.md) → [`00781bd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00781/00781bd0.md) FUN_00781bd0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b6e0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e0c.md) [`008b6e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e60.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b6e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6e50.md) [`008b6ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6ea4.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00781c84",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00781c44",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00781cac",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00781c6c",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00781d0c",
      "incomplete_value": false,
      "site": "00781d10",
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
            "const:d74:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00781ccc",
      "incomplete_value": false,
      "site": "00781cd0",
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
            "const:d34:8"
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
      "00781c84",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00781cac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00781d0c",
      "PARAM",
      [
        "storage",
        "002b3d34",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00781c84",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00781cac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00781d0c",
      "PARAM",
      [
        "storage",
        "002b3d74",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00781c2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781b90.md#insn-00781c2c) · [`00781c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781b90.md#insn-00781c44) · [`00781c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781b90.md#insn-00781c6c)
- 新版 `00781c6c`（命令位置の公開資料なし） · `00781c84`（命令位置の公開資料なし） · `00781cac`（命令位置の公開資料なし）

~~~diff
- 00781c2c ["INT_ADD", "register:40f0:8", ["const:781c2c:8", "const:4:8"]]
- 00781c2c ["CALL", null, ["callee:008b6e50:8"]]
+ 00781c6c ["INT_ADD", "register:40f0:8", ["const:781c6c:8", "const:4:8"]]
+ 00781c6c ["CALL", null, ["callee:008b6e50:8"]]
- 00781c2c bytes 78d40494
+ 00781c6c bytes 79d40494
- 00781c44 ["INT_ADD", "register:40f0:8", ["const:781c44:8", "const:4:8"]]
- 00781c44 ["CALL", null, ["ram:47acb4:8"]]
+ 00781c84 ["INT_ADD", "register:40f0:8", ["const:781c84:8", "const:4:8"]]
+ 00781c84 ["CALL", null, ["ram:47acf4:8"]]
- 00781c44 bytes 1ce4f397
+ 00781c84 bytes 1ce4f397
- 00781c6c ["INT_ADD", "register:40f0:8", ["const:781c6c:8", "const:4:8"]]
- 00781c6c ["CALL", null, ["ram:47acb4:8"]]
+ 00781cac ["INT_ADD", "register:40f0:8", ["const:781cac:8", "const:4:8"]]
+ 00781cac ["CALL", null, ["ram:47acf4:8"]]
- 00781c6c bytes 12e4f397
+ 00781cac bytes 12e4f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2d5363d44fd3318faa5fd775747cd2b"></a>

### [`00781d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781d00.md) → [`00781d40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00781/00781d40.md) FUN_00781d40

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
      "definition_site": "00781d64",
      "incomplete_value": false,
      "site": "00781d64",
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
            "const:520:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00781d24",
      "incomplete_value": false,
      "site": "00781d24",
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
            "const:120:8"
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
      "00781d64",
      "DATA",
      [
        "storage",
        "00c78120",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00781d64",
      "DATA",
      [
        "storage",
        "00c78520",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00781d14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781d00.md#insn-00781d14) · [`00781d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781d00.md#insn-00781d20)
- 新版 `00781d54`（命令位置の公開資料なし） · `00781d60`（命令位置の公開資料なし）

~~~diff
- 00781d14 ["INT_ADD", "register:40f0:8", ["const:781d14:8", "const:4:8"]]
- 00781d14 ["CALL", null, ["callee:00c57e90:8"]]
+ 00781d54 ["INT_ADD", "register:40f0:8", ["const:781d54:8", "const:4:8"]]
+ 00781d54 ["CALL", null, ["callee:00c57e90:8"]]
- 00781d14 bytes 5f571394
+ 00781d54 bytes 4f581394
- 00781d20 ["COPY", "tmp:0:8", ["const:120:8"]]
- 00781d20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00781d20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00781d20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00781d60 ["COPY", "tmp:0:8", ["const:520:8"]]
+ 00781d60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00781d60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00781d60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00781d20 bytes 08810491
+ 00781d60 bytes 08811491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5a11b77d3ceb439945750bf94284004"></a>

### [`00781e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781e08.md) → [`00781e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00781/00781e48.md) FUN_00781e48

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
      "definition_site": "00781e6c",
      "incomplete_value": false,
      "site": "00781e6c",
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
            "const:5a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00781e2c",
      "incomplete_value": false,
      "site": "00781e2c",
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
            "const:1a0:8"
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
      "00781e6c",
      "DATA",
      [
        "storage",
        "00c781a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00781e6c",
      "DATA",
      [
        "storage",
        "00c785a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00781e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781e08.md#insn-00781e1c) · [`00781e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781e08.md#insn-00781e28)
- 新版 `00781e5c`（命令位置の公開資料なし） · `00781e68`（命令位置の公開資料なし）

~~~diff
- 00781e1c ["INT_ADD", "register:40f0:8", ["const:781e1c:8", "const:4:8"]]
- 00781e1c ["CALL", null, ["callee:00c57e90:8"]]
+ 00781e5c ["INT_ADD", "register:40f0:8", ["const:781e5c:8", "const:4:8"]]
+ 00781e5c ["CALL", null, ["callee:00c57e90:8"]]
- 00781e1c bytes 1d571394
+ 00781e5c bytes 0d581394
- 00781e28 ["COPY", "tmp:0:8", ["const:1a0:8"]]
- 00781e28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00781e28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00781e28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00781e68 ["COPY", "tmp:0:8", ["const:5a0:8"]]
+ 00781e68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00781e68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00781e68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00781e28 bytes 08810691
+ 00781e68 bytes 08811691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44b369d18131e65e280d328da055f23d"></a>

### [`00781e58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781e58.md) → [`00781e98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00781/00781e98.md) FUN_00781e98

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 16件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md)
- 新版 呼出元 0件  · 呼出先 16件 [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.57% / 新版 91.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件, `store_value` 6件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00781ff8",
      "incomplete_value": true,
      "site": "00782000",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:320:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00781fb8",
      "incomplete_value": true,
      "site": "00781fc0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2e0:8"
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
      "definition_site": "00782030",
      "incomplete_value": true,
      "site": "00782030",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ad000:8"
              ],
              [
                "leaf",
                "const:a7a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00781ff0",
      "incomplete_value": true,
      "site": "00781ff0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ad000:8"
              ],
              [
                "leaf",
                "const:a3a:8"
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
      "definition_site": "00782038",
      "incomplete_value": true,
      "site": "00782038",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00781ff8",
      "incomplete_value": true,
      "site": "00781ff8",
      "value": [
        "LOAD",
        "8",
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
      "00781edc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00781ef8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00781f84",
      "DATA",
      [
        "storage",
        "0039e389",
        null,
        "byte[35]"
      ]
    ]
  ],
  "added": [
    [
      "00781edc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00781ef8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00781f84",
      "DATA",
      [
        "storage",
        "0039e389",
        null,
        "byte[47]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00781e9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781e58.md#insn-00781e9c) · [`00781eb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781e58.md#insn-00781eb8) · [`00781fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00781/00781e58.md#insn-00781fb0)
- 新版 `00781edc`（命令位置の公開資料なし） · `00781ef8`（命令位置の公開資料なし） · `00781ff0`（命令位置の公開資料なし）

~~~diff
- 00781e9c ["INT_ADD", "register:40f0:8", ["const:781e9c:8", "const:4:8"]]
- 00781e9c ["CALL", null, ["ram:47acb4:8"]]
+ 00781edc ["INT_ADD", "register:40f0:8", ["const:781edc:8", "const:4:8"]]
+ 00781edc ["CALL", null, ["ram:47acf4:8"]]
- 00781e9c bytes 86e3f397
+ 00781edc bytes 86e3f397
- 00781eb8 ["INT_ADD", "register:40f0:8", ["const:781eb8:8", "const:4:8"]]
- 00781eb8 ["CALL", null, ["ram:47acb4:8"]]
+ 00781ef8 ["INT_ADD", "register:40f0:8", ["const:781ef8:8", "const:4:8"]]
+ 00781ef8 ["CALL", null, ["ram:47acf4:8"]]
- 00781eb8 bytes 7fe3f397
+ 00781ef8 bytes 7fe3f397
- 00781fb0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00781fb0 ["INT_ADD", "register:40f0:8", ["const:781fb0:8", "const:4:8"]]
- 00781fb0 ["CALLIND", null, ["register:0:8"]]
+ 00781ff0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00781ff0 ["INT_ADD", "register:40f0:8", ["const:781ff0:8", "const:4:8"]]
+ 00781ff0 ["CALLIND", null, ["register:0:8"]]
- 00781fb0 bytes 00013fd6
+ 00781ff0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42dd84753f38c654fe9841e3bbd67efe"></a>

### [`00782370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782370.md) → [`007823b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00782/007823b0.md) FUN_007823b0

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
      "definition_site": "007823c4",
      "incomplete_value": false,
      "site": "007823c8",
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
            "const:610:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00782384",
      "incomplete_value": false,
      "site": "00782388",
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
            "const:210:8"
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
      "007823c8",
      "DATA",
      [
        "storage",
        "00c78210",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007823c8",
      "DATA",
      [
        "storage",
        "00c78610",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078237c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782370.md#insn-0078237c) · [`00782384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782370.md#insn-00782384)
- 新版 `007823bc`（命令位置の公開資料なし） · `007823c4`（命令位置の公開資料なし）

~~~diff
- 0078237c ["INT_ADD", "register:40f0:8", ["const:78237c:8", "const:4:8"]]
- 0078237c ["CALL", null, ["callee:00c57e90:8"]]
+ 007823bc ["INT_ADD", "register:40f0:8", ["const:7823bc:8", "const:4:8"]]
+ 007823bc ["CALL", null, ["callee:00c57e90:8"]]
- 0078237c bytes c5551394
+ 007823bc bytes b5561394
- 00782384 ["COPY", "tmp:0:8", ["const:210:8"]]
- 00782384 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00782384 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00782384 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007823c4 ["COPY", "tmp:0:8", ["const:610:8"]]
+ 007823c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007823c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007823c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00782384 bytes 08410891
+ 007823c4 bytes 08411891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d40e978a02f6844082ab305f1105211"></a>

### [`00782394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782394.md) → [`007823d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00782/007823d4.md) FUN_007823d4

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
      "definition_site": "007823d8",
      "incomplete_value": false,
      "site": "007823dc",
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
            "const:610:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00782398",
      "incomplete_value": false,
      "site": "0078239c",
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
            "const:210:8"
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
      "007823dc",
      "DATA",
      [
        "storage",
        "00c78210",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007823dc",
      "DATA",
      [
        "storage",
        "00c78610",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00782398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782394.md#insn-00782398)
- 新版 `007823d8`（命令位置の公開資料なし）

~~~diff
- 00782398 ["COPY", "tmp:0:8", ["const:210:8"]]
- 00782398 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00782398 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00782398 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007823d8 ["COPY", "tmp:0:8", ["const:610:8"]]
+ 007823d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007823d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007823d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00782398 bytes 08410891
+ 007823d8 bytes 08411891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d835aef738d0c30875a5cfeff0d08389"></a>

### [`007823ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/007823ac.md) → [`007823ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00782/007823ec.md) FUN_007823ec

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043e7e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043e7e8.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043e828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e828.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.71% / 新版 94.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00782494",
      "incomplete_value": true,
      "site": "007824a4",
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
                "const:2bc000:8"
              ],
              [
                "leaf",
                "const:a2b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00782454",
      "incomplete_value": true,
      "site": "00782464",
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
                "const:2bc000:8"
              ],
              [
                "leaf",
                "const:9eb:8"
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
      "definition_site": "007824a8",
      "incomplete_value": true,
      "site": "007824a8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00782468",
      "incomplete_value": true,
      "site": "00782468",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00782570",
      "incomplete_value": false,
      "site": "00782570",
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
            "const:680:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00782530",
      "incomplete_value": false,
      "site": "00782530",
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
            "const:280:8"
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
      "00782428",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00782494",
      "READ",
      [
        "storage",
        "002bc9eb",
        null,
        "string"
      ]
    ],
    [
      "0078249c",
      "READ",
      [
        "storage",
        "002bc9f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00782428",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00782494",
      "READ",
      [
        "storage",
        "002bca2b",
        null,
        "string"
      ]
    ],
    [
      "0078249c",
      "READ",
      [
        "storage",
        "002bca39",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007823e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/007823ac.md#insn-007823e8) · [`007825c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/007823ac.md#insn-007825c8) · [`007823f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/007823ac.md#insn-007823f4)
- 新版 `00782428`（命令位置の公開資料なし） · `00782608`（命令位置の公開資料なし） · `00782434`（命令位置の公開資料なし）

~~~diff
- 007823e8 ["INT_ADD", "register:40f0:8", ["const:7823e8:8", "const:4:8"]]
- 007823e8 ["CALL", null, ["ram:47acb4:8"]]
+ 00782428 ["INT_ADD", "register:40f0:8", ["const:782428:8", "const:4:8"]]
+ 00782428 ["CALL", null, ["ram:47acf4:8"]]
- 007823e8 bytes 33e2f397
+ 00782428 bytes 33e2f397
- 007825c8 ["INT_ADD", "register:40f0:8", ["const:7825c8:8", "const:4:8"]]
- 007825c8 ["CALL", null, ["ram:47acb4:8"]]
+ 00782608 ["INT_ADD", "register:40f0:8", ["const:782608:8", "const:4:8"]]
+ 00782608 ["CALL", null, ["ram:47acf4:8"]]
- 007825c8 bytes bbe1f397
+ 00782608 bytes bbe1f397
- 007823f4 ["INT_ADD", "register:40f0:8", ["const:7823f4:8", "const:4:8"]]
- 007823f4 ["CALL", null, ["callee:0047cdd4:8"]]
+ 00782434 ["INT_ADD", "register:40f0:8", ["const:782434:8", "const:4:8"]]
+ 00782434 ["CALL", null, ["callee:0047cdd4:8"]]
- 007823f4 bytes 68eaf397
+ 00782434 bytes 68eaf397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a987f2f969a9b0829c52031235011629"></a>

### [`007827a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/007827a0.md) → [`007827e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00782/007827e0.md) FUN_007827e0

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
      "definition_site": "007827f4",
      "incomplete_value": false,
      "site": "007827f8",
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
            "const:680:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007827b4",
      "incomplete_value": false,
      "site": "007827b8",
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
            "const:280:8"
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
      "007827f8",
      "DATA",
      [
        "storage",
        "00c78280",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007827f8",
      "DATA",
      [
        "storage",
        "00c78680",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007827ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/007827a0.md#insn-007827ac) · [`007827b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/007827a0.md#insn-007827b4)
- 新版 `007827ec`（命令位置の公開資料なし） · `007827f4`（命令位置の公開資料なし）

~~~diff
- 007827ac ["INT_ADD", "register:40f0:8", ["const:7827ac:8", "const:4:8"]]
- 007827ac ["CALL", null, ["callee:00c57e90:8"]]
+ 007827ec ["INT_ADD", "register:40f0:8", ["const:7827ec:8", "const:4:8"]]
+ 007827ec ["CALL", null, ["callee:00c57e90:8"]]
- 007827ac bytes b9541394
+ 007827ec bytes a9551394
- 007827b4 ["COPY", "tmp:0:8", ["const:280:8"]]
- 007827b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007827b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007827b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007827f4 ["COPY", "tmp:0:8", ["const:680:8"]]
+ 007827f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007827f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007827f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007827b4 bytes 08010a91
+ 007827f4 bytes 08011a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44d34ab5cb70bef201e1e98050735ff5"></a>

### [`007827c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/007827c4.md) → [`00782804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00782/00782804.md) FUN_00782804

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
      "definition_site": "00782808",
      "incomplete_value": false,
      "site": "0078280c",
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
            "const:680:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007827c8",
      "incomplete_value": false,
      "site": "007827cc",
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
            "const:280:8"
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
      "0078280c",
      "DATA",
      [
        "storage",
        "00c78280",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0078280c",
      "DATA",
      [
        "storage",
        "00c78680",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007827c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/007827c4.md#insn-007827c8)
- 新版 `00782808`（命令位置の公開資料なし）

~~~diff
- 007827c8 ["COPY", "tmp:0:8", ["const:280:8"]]
- 007827c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007827c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007827c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00782808 ["COPY", "tmp:0:8", ["const:680:8"]]
+ 00782808 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00782808 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00782808 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007827c8 bytes 08010a91
+ 00782808 bytes 08011a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17e874a032735e797c86903ba1c37284"></a>

### [`007827dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/007827dc.md) → [`0078281c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00782/0078281c.md) FUN_0078281c

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 14件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`0071c420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071c/0071c420.md) [`007591f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00759/007591f4.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`0071c460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071c/0071c460.md) [`00759234`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00759/00759234.md)

変更の種類 call, call_target, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 85.44% / 新版 85.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007828c8",
      "incomplete_value": true,
      "site": "007828d8",
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
                "const:2ec:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00782888",
      "incomplete_value": true,
      "site": "00782898",
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
                "const:2ac:8"
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
      "definition_site": "007828cc",
      "incomplete_value": true,
      "site": "007828dc",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078288c",
      "incomplete_value": true,
      "site": "0078289c",
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
                "const:e:8"
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
      "definition_site": "007828d0",
      "incomplete_value": true,
      "site": "007828e0",
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
                "const:430:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00782890",
      "incomplete_value": true,
      "site": "007828a0",
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
                "const:3f0:8"
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
      "00782868",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071c420"
      ]
    ],
    [
      "00782870",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007591f4"
      ]
    ],
    [
      "00782874",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00782868",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071c460"
      ]
    ],
    [
      "00782870",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00759234"
      ]
    ],
    [
      "00782874",
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

- 旧版 [`00782828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/007827dc.md#insn-00782828) · [`00782830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/007827dc.md#insn-00782830) · [`00782834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/007827dc.md#insn-00782834)
- 新版 `00782868`（命令位置の公開資料なし） · `00782870`（命令位置の公開資料なし） · `00782874`（命令位置の公開資料なし）

~~~diff
- 00782828 ["INT_ADD", "register:40f0:8", ["const:782828:8", "const:4:8"]]
- 00782828 ["CALL", null, ["ram:71c420:8"]]
+ 00782868 ["INT_ADD", "register:40f0:8", ["const:782868:8", "const:4:8"]]
+ 00782868 ["CALL", null, ["ram:71c460:8"]]
- 00782828 bytes fe66fe97
+ 00782868 bytes fe66fe97
- 00782830 ["INT_ADD", "register:40f0:8", ["const:782830:8", "const:4:8"]]
- 00782830 ["CALL", null, ["ram:7591f4:8"]]
+ 00782870 ["INT_ADD", "register:40f0:8", ["const:782870:8", "const:4:8"]]
+ 00782870 ["CALL", null, ["ram:759234:8"]]
- 00782830 bytes 715aff97
+ 00782870 bytes 715aff97
- 00782834 ["INT_ADD", "register:40f0:8", ["const:782834:8", "const:4:8"]]
- 00782834 ["CALL", null, ["ram:47acb4:8"]]
+ 00782874 ["INT_ADD", "register:40f0:8", ["const:782874:8", "const:4:8"]]
+ 00782874 ["CALL", null, ["ram:47acf4:8"]]
- 00782834 bytes 20e1f397
+ 00782874 bytes 20e1f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-681bfa0f7111fdde020f76d8f5bcefc0"></a>

### [`00782a34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782a34.md) → [`00782a74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00782/00782a74.md) FUN_00782a74

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
      "definition_site": "00782a88",
      "incomplete_value": false,
      "site": "00782a8c",
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
            "const:6f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00782a48",
      "incomplete_value": false,
      "site": "00782a4c",
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
            "const:2f0:8"
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
      "00782a8c",
      "DATA",
      [
        "storage",
        "00c782f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00782a8c",
      "DATA",
      [
        "storage",
        "00c786f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00782a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782a34.md#insn-00782a40) · [`00782a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782a34.md#insn-00782a48)
- 新版 `00782a80`（命令位置の公開資料なし） · `00782a88`（命令位置の公開資料なし）

~~~diff
- 00782a40 ["INT_ADD", "register:40f0:8", ["const:782a40:8", "const:4:8"]]
- 00782a40 ["CALL", null, ["callee:00c57e90:8"]]
+ 00782a80 ["INT_ADD", "register:40f0:8", ["const:782a80:8", "const:4:8"]]
+ 00782a80 ["CALL", null, ["callee:00c57e90:8"]]
- 00782a40 bytes 14541394
+ 00782a80 bytes 04551394
- 00782a48 ["COPY", "tmp:0:8", ["const:2f0:8"]]
- 00782a48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00782a48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00782a48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00782a88 ["COPY", "tmp:0:8", ["const:6f0:8"]]
+ 00782a88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00782a88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00782a88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00782a48 bytes 08c10b91
+ 00782a88 bytes 08c11b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-567d5ac15413a54fff18e6ef74fd9109"></a>

### [`00782a58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782a58.md) → [`00782a98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00782/00782a98.md) FUN_00782a98

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
      "definition_site": "00782a9c",
      "incomplete_value": false,
      "site": "00782aa0",
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
            "const:6f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00782a5c",
      "incomplete_value": false,
      "site": "00782a60",
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
            "const:2f0:8"
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
      "00782aa0",
      "DATA",
      [
        "storage",
        "00c782f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00782aa0",
      "DATA",
      [
        "storage",
        "00c786f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00782a5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782a58.md#insn-00782a5c)
- 新版 `00782a9c`（命令位置の公開資料なし）

~~~diff
- 00782a5c ["COPY", "tmp:0:8", ["const:2f0:8"]]
- 00782a5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00782a5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00782a5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00782a9c ["COPY", "tmp:0:8", ["const:6f0:8"]]
+ 00782a9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00782a9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00782a9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00782a5c bytes 08c10b91
+ 00782a9c bytes 08c11b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2593c8b2268dd44dce4fe4e266cac0a"></a>

### [`00782a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782a70.md) → [`00782ab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00782/00782ab0.md) FUN_00782ab0

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
      "site": "00782ad4",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00782a94",
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
      "00782ad4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00782ad4",
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

- 旧版 [`00782a94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782a70.md#insn-00782a94) · [`00782aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782a70.md#insn-00782aa0)
- 新版 `00782ad4`（命令位置の公開資料なし） · `00782ae0`（命令位置の公開資料なし）

~~~diff
- 00782a94 ["INT_ADD", "register:40f0:8", ["const:782a94:8", "const:4:8"]]
- 00782a94 ["CALL", null, ["ram:47acb4:8"]]
+ 00782ad4 ["INT_ADD", "register:40f0:8", ["const:782ad4:8", "const:4:8"]]
+ 00782ad4 ["CALL", null, ["ram:47acf4:8"]]
- 00782a94 bytes 88e0f397
+ 00782ad4 bytes 88e0f397
- 00782aa0 ["INT_ADD", "register:40f0:8", ["const:782aa0:8", "const:4:8"]]
- 00782aa0 ["CALL", null, ["callee:0047cdd4:8"]]
+ 00782ae0 ["INT_ADD", "register:40f0:8", ["const:782ae0:8", "const:4:8"]]
+ 00782ae0 ["CALL", null, ["callee:0047cdd4:8"]]
- 00782aa0 bytes bde8f397
+ 00782ae0 bytes bde8f397
~~~


<a id="compare-a884dccdb65f798fc2cec2a89ef91211"></a>

### [`00782b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782b30.md) → [`00782b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00782/00782b70.md) FUN_00782b70

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`0075eb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075e/0075eb80.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "00782b7c",
      "incomplete_value": false,
      "site": "00782b80",
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
      "definition_site": "00782b3c",
      "incomplete_value": false,
      "site": "00782b40",
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
      "00782b7c",
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
      "00782b7c",
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

- 旧版 [`00782b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782b30.md#insn-00782b40) · [`00782b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782b30.md#insn-00782b3c)
- 新版 `00782b80`（命令位置の公開資料なし） · `00782b7c`（命令位置の公開資料なし）

~~~diff
- 00782b40 ["INT_ADD", "register:40f0:8", ["const:782b40:8", "const:4:8"]]
- 00782b40 ["CALL", null, ["callee:0043b778:8"]]
+ 00782b80 ["INT_ADD", "register:40f0:8", ["const:782b80:8", "const:4:8"]]
+ 00782b80 ["CALL", null, ["callee:0043b778:8"]]
- 00782b40 bytes fee2f297
+ 00782b80 bytes fee2f297
- 00782b3c ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00782b3c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00782b3c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00782b3c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00782b7c ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00782b7c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00782b7c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00782b7c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00782b3c bytes 00303c91
+ 00782b7c bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4f9beb8a52480d8b316b74d2e2fcfb9"></a>

### [`00782b48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782b48.md) → [`00782b88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00782/00782b88.md) FUN_00782b88

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
      "definition_site": "00782bac",
      "incomplete_value": false,
      "site": "00782bac",
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
            "const:7a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00782b6c",
      "incomplete_value": false,
      "site": "00782b6c",
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
            "const:3a0:8"
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
      "00782bac",
      "DATA",
      [
        "storage",
        "00c783a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00782bac",
      "DATA",
      [
        "storage",
        "00c787a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00782b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782b48.md#insn-00782b5c) · [`00782b68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782b48.md#insn-00782b68)
- 新版 `00782b9c`（命令位置の公開資料なし） · `00782ba8`（命令位置の公開資料なし）

~~~diff
- 00782b5c ["INT_ADD", "register:40f0:8", ["const:782b5c:8", "const:4:8"]]
- 00782b5c ["CALL", null, ["callee:00c57e90:8"]]
+ 00782b9c ["INT_ADD", "register:40f0:8", ["const:782b9c:8", "const:4:8"]]
+ 00782b9c ["CALL", null, ["callee:00c57e90:8"]]
- 00782b5c bytes cd531394
+ 00782b9c bytes bd541394
- 00782b68 ["COPY", "tmp:0:8", ["const:3a0:8"]]
- 00782b68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00782b68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00782b68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00782ba8 ["COPY", "tmp:0:8", ["const:7a0:8"]]
+ 00782ba8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00782ba8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00782ba8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00782b68 bytes 08810e91
+ 00782ba8 bytes 08811e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7332bf3a6ba219e57f2582758465b44d"></a>

### [`00782b98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782b98.md) → [`00782bd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00782/00782bd8.md) FUN_00782bd8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.55% / 新版 96.55%

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
      "site": "00782c00",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00782bc0",
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
      "00782c00",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00782c00",
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

- 旧版 [`00782bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782b98.md#insn-00782bc0) · [`00782bcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782b98.md#insn-00782bcc)
- 新版 `00782c00`（命令位置の公開資料なし） · `00782c0c`（命令位置の公開資料なし）

~~~diff
- 00782bc0 ["INT_ADD", "register:40f0:8", ["const:782bc0:8", "const:4:8"]]
- 00782bc0 ["CALL", null, ["ram:47acb4:8"]]
+ 00782c00 ["INT_ADD", "register:40f0:8", ["const:782c00:8", "const:4:8"]]
+ 00782c00 ["CALL", null, ["ram:47acf4:8"]]
- 00782bc0 bytes 3de0f397
+ 00782c00 bytes 3de0f397
- 00782bcc ["INT_ADD", "register:40f0:8", ["const:782bcc:8", "const:4:8"]]
- 00782bcc ["CALL", null, ["callee:0047cdd4:8"]]
+ 00782c0c ["INT_ADD", "register:40f0:8", ["const:782c0c:8", "const:4:8"]]
+ 00782c0c ["CALL", null, ["callee:0047cdd4:8"]]
- 00782bcc bytes 72e8f397
+ 00782c0c bytes 72e8f397
~~~


<a id="compare-8ca5953a896b83d21c8144e847999bdf"></a>

### [`00782c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782c38.md) → [`00782c78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00782/00782c78.md) FUN_00782c78

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
      "definition_site": "00782c8c",
      "incomplete_value": false,
      "site": "00782c90",
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
            "const:820:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00782c4c",
      "incomplete_value": false,
      "site": "00782c50",
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
            "const:420:8"
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
      "00782c90",
      "DATA",
      [
        "storage",
        "00c78420",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00782c90",
      "DATA",
      [
        "storage",
        "00c78820",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00782c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782c38.md#insn-00782c44) · [`00782c4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782c38.md#insn-00782c4c)
- 新版 `00782c84`（命令位置の公開資料なし） · `00782c8c`（命令位置の公開資料なし）

~~~diff
- 00782c44 ["INT_ADD", "register:40f0:8", ["const:782c44:8", "const:4:8"]]
- 00782c44 ["CALL", null, ["callee:00c57e90:8"]]
+ 00782c84 ["INT_ADD", "register:40f0:8", ["const:782c84:8", "const:4:8"]]
+ 00782c84 ["CALL", null, ["callee:00c57e90:8"]]
- 00782c44 bytes 93531394
+ 00782c84 bytes 83541394
- 00782c4c ["COPY", "tmp:0:8", ["const:420:8"]]
- 00782c4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00782c4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00782c4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00782c8c ["COPY", "tmp:0:8", ["const:820:8"]]
+ 00782c8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00782c8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00782c8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00782c4c bytes 08811091
+ 00782c8c bytes 08812091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a59f84f79eb81ace8171543d99eb0248"></a>

### [`00782c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782c74.md) → [`00782cb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00782/00782cb4.md) FUN_00782cb4

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
      "site": "00782cd8",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00782c98",
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
      "00782cd8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00782cd8",
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

- 旧版 [`00782c98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782c74.md#insn-00782c98) · [`00782ca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782c74.md#insn-00782ca4)
- 新版 `00782cd8`（命令位置の公開資料なし） · `00782ce4`（命令位置の公開資料なし）

~~~diff
- 00782c98 ["INT_ADD", "register:40f0:8", ["const:782c98:8", "const:4:8"]]
- 00782c98 ["CALL", null, ["ram:47acb4:8"]]
+ 00782cd8 ["INT_ADD", "register:40f0:8", ["const:782cd8:8", "const:4:8"]]
+ 00782cd8 ["CALL", null, ["ram:47acf4:8"]]
- 00782c98 bytes 07e0f397
+ 00782cd8 bytes 07e0f397
- 00782ca4 ["INT_ADD", "register:40f0:8", ["const:782ca4:8", "const:4:8"]]
- 00782ca4 ["CALL", null, ["callee:0047cdd4:8"]]
+ 00782ce4 ["INT_ADD", "register:40f0:8", ["const:782ce4:8", "const:4:8"]]
+ 00782ce4 ["CALL", null, ["callee:0047cdd4:8"]]
- 00782ca4 bytes 3ce8f397
+ 00782ce4 bytes 3ce8f397
~~~


<a id="compare-31a3c1d73cd365556672e8f130cb8991"></a>

### [`00782ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782ce8.md) → [`00782d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00782/00782d28.md) FUN_00782d28

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
      "definition_site": "00782d3c",
      "incomplete_value": false,
      "site": "00782d40",
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
            "const:8a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00782cfc",
      "incomplete_value": false,
      "site": "00782d00",
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
            "const:4a0:8"
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
      "00782d40",
      "DATA",
      [
        "storage",
        "00c784a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00782d40",
      "DATA",
      [
        "storage",
        "00c788a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00782cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782ce8.md#insn-00782cf4) · [`00782cfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782ce8.md#insn-00782cfc)
- 新版 `00782d34`（命令位置の公開資料なし） · `00782d3c`（命令位置の公開資料なし）

~~~diff
- 00782cf4 ["INT_ADD", "register:40f0:8", ["const:782cf4:8", "const:4:8"]]
- 00782cf4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00782d34 ["INT_ADD", "register:40f0:8", ["const:782d34:8", "const:4:8"]]
+ 00782d34 ["CALL", null, ["callee:00c57e90:8"]]
- 00782cf4 bytes 67531394
+ 00782d34 bytes 57541394
- 00782cfc ["COPY", "tmp:0:8", ["const:4a0:8"]]
- 00782cfc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00782cfc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00782cfc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00782d3c ["COPY", "tmp:0:8", ["const:8a0:8"]]
+ 00782d3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00782d3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00782d3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00782cfc bytes 08811291
+ 00782d3c bytes 08812291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa85d4a17f4241061db0db5034688656"></a>

### [`00782d24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782d24.md) → [`00782d64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00782/00782d64.md) FUN_00782d64

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
      "site": "00782d88",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00782d48",
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
      "00782d88",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00782d88",
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

- 旧版 [`00782d48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782d24.md#insn-00782d48) · [`00782d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782d24.md#insn-00782d54)
- 新版 `00782d88`（命令位置の公開資料なし） · `00782d94`（命令位置の公開資料なし）

~~~diff
- 00782d48 ["INT_ADD", "register:40f0:8", ["const:782d48:8", "const:4:8"]]
- 00782d48 ["CALL", null, ["ram:47acb4:8"]]
+ 00782d88 ["INT_ADD", "register:40f0:8", ["const:782d88:8", "const:4:8"]]
+ 00782d88 ["CALL", null, ["ram:47acf4:8"]]
- 00782d48 bytes dbdff397
+ 00782d88 bytes dbdff397
- 00782d54 ["INT_ADD", "register:40f0:8", ["const:782d54:8", "const:4:8"]]
- 00782d54 ["CALL", null, ["callee:0047cdd4:8"]]
+ 00782d94 ["INT_ADD", "register:40f0:8", ["const:782d94:8", "const:4:8"]]
+ 00782d94 ["CALL", null, ["callee:0047cdd4:8"]]
- 00782d54 bytes 10e8f397
+ 00782d94 bytes 10e8f397
~~~


<a id="compare-0c5722907de565173e6f73864f90e6b3"></a>

### [`00782d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782d98.md) → [`00782dd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00782/00782dd8.md) FUN_00782dd8

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
      "definition_site": "00782dec",
      "incomplete_value": false,
      "site": "00782df0",
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
            "const:920:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00782dac",
      "incomplete_value": false,
      "site": "00782db0",
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
            "const:520:8"
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
      "00782df0",
      "DATA",
      [
        "storage",
        "00c78520",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00782df0",
      "DATA",
      [
        "storage",
        "00c78920",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00782da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782d98.md#insn-00782da4) · [`00782dac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782d98.md#insn-00782dac)
- 新版 `00782de4`（命令位置の公開資料なし） · `00782dec`（命令位置の公開資料なし）

~~~diff
- 00782da4 ["INT_ADD", "register:40f0:8", ["const:782da4:8", "const:4:8"]]
- 00782da4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00782de4 ["INT_ADD", "register:40f0:8", ["const:782de4:8", "const:4:8"]]
+ 00782de4 ["CALL", null, ["callee:00c57e90:8"]]
- 00782da4 bytes 3b531394
+ 00782de4 bytes 2b541394
- 00782dac ["COPY", "tmp:0:8", ["const:520:8"]]
- 00782dac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00782dac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00782dac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00782dec ["COPY", "tmp:0:8", ["const:920:8"]]
+ 00782dec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00782dec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00782dec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00782dac bytes 08811491
+ 00782dec bytes 08812491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-870fcff994137ea2d3d7f9ed3791830e"></a>

### [`00782dd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782dd4.md) → [`00782e14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00782/00782e14.md) FUN_00782e14

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 92.86% / 新版 92.86%

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
      "site": "00782e38",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00782df8",
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
      "site": "00782e60",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00782e20",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "00782e38",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00782e60",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00782e38",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00782e60",
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

- 旧版 [`00782df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782dd4.md#insn-00782df8) · [`00782e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782dd4.md#insn-00782e20) · [`00782e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782dd4.md#insn-00782e04)
- 新版 `00782e38`（命令位置の公開資料なし） · `00782e60`（命令位置の公開資料なし） · `00782e44`（命令位置の公開資料なし）

~~~diff
- 00782df8 ["INT_ADD", "register:40f0:8", ["const:782df8:8", "const:4:8"]]
- 00782df8 ["CALL", null, ["ram:47acb4:8"]]
+ 00782e38 ["INT_ADD", "register:40f0:8", ["const:782e38:8", "const:4:8"]]
+ 00782e38 ["CALL", null, ["ram:47acf4:8"]]
- 00782df8 bytes afdff397
+ 00782e38 bytes afdff397
- 00782e20 ["INT_ADD", "register:40f0:8", ["const:782e20:8", "const:4:8"]]
- 00782e20 ["CALL", null, ["ram:47acb4:8"]]
+ 00782e60 ["INT_ADD", "register:40f0:8", ["const:782e60:8", "const:4:8"]]
+ 00782e60 ["CALL", null, ["ram:47acf4:8"]]
- 00782e20 bytes a5dff397
+ 00782e60 bytes a5dff397
- 00782e04 ["INT_ADD", "register:40f0:8", ["const:782e04:8", "const:4:8"]]
- 00782e04 ["CALL", null, ["callee:0047cdd4:8"]]
+ 00782e44 ["INT_ADD", "register:40f0:8", ["const:782e44:8", "const:4:8"]]
+ 00782e44 ["CALL", null, ["callee:0047cdd4:8"]]
- 00782e04 bytes e4e7f397
+ 00782e44 bytes e4e7f397
~~~


<a id="compare-36c485b9b6e0011d3506b340e9b2addf"></a>

### [`00782e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782e70.md) → [`00782eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00782/00782eb0.md) FUN_00782eb0

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
      "definition_site": "00782ec4",
      "incomplete_value": false,
      "site": "00782ec8",
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
            "const:9a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00782e84",
      "incomplete_value": false,
      "site": "00782e88",
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
            "const:5a0:8"
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
      "00782ec8",
      "DATA",
      [
        "storage",
        "00c785a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00782ec8",
      "DATA",
      [
        "storage",
        "00c789a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00782e7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782e70.md#insn-00782e7c) · [`00782e84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782e70.md#insn-00782e84)
- 新版 `00782ebc`（命令位置の公開資料なし） · `00782ec4`（命令位置の公開資料なし）

~~~diff
- 00782e7c ["INT_ADD", "register:40f0:8", ["const:782e7c:8", "const:4:8"]]
- 00782e7c ["CALL", null, ["callee:00c57e90:8"]]
+ 00782ebc ["INT_ADD", "register:40f0:8", ["const:782ebc:8", "const:4:8"]]
+ 00782ebc ["CALL", null, ["callee:00c57e90:8"]]
- 00782e7c bytes 05531394
+ 00782ebc bytes f5531394
- 00782e84 ["COPY", "tmp:0:8", ["const:5a0:8"]]
- 00782e84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00782e84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00782e84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00782ec4 ["COPY", "tmp:0:8", ["const:9a0:8"]]
+ 00782ec4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00782ec4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00782ec4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00782e84 bytes 08811691
+ 00782ec4 bytes 08812691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12f5abaf7c01a60e78d5461f400e09d4"></a>

### [`00782eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782eac.md) → [`00782eec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00782/00782eec.md) FUN_00782eec

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
      "site": "00782f10",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00782ed0",
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
      "00782f10",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00782f10",
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

- 旧版 [`00782ed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782eac.md#insn-00782ed0) · [`00782edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782eac.md#insn-00782edc)
- 新版 `00782f10`（命令位置の公開資料なし） · `00782f1c`（命令位置の公開資料なし）

~~~diff
- 00782ed0 ["INT_ADD", "register:40f0:8", ["const:782ed0:8", "const:4:8"]]
- 00782ed0 ["CALL", null, ["ram:47acb4:8"]]
+ 00782f10 ["INT_ADD", "register:40f0:8", ["const:782f10:8", "const:4:8"]]
+ 00782f10 ["CALL", null, ["ram:47acf4:8"]]
- 00782ed0 bytes 79dff397
+ 00782f10 bytes 79dff397
- 00782edc ["INT_ADD", "register:40f0:8", ["const:782edc:8", "const:4:8"]]
- 00782edc ["CALL", null, ["callee:0047cdd4:8"]]
+ 00782f1c ["INT_ADD", "register:40f0:8", ["const:782f1c:8", "const:4:8"]]
+ 00782f1c ["CALL", null, ["callee:0047cdd4:8"]]
- 00782edc bytes aee7f397
+ 00782f1c bytes aee7f397
~~~


<a id="compare-0ab5dd2952703c382d583c4638be899f"></a>

### [`00782f20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782f20.md) → [`00782f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00782/00782f60.md) FUN_00782f60

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
      "definition_site": "00782f74",
      "incomplete_value": false,
      "site": "00782f78",
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
            "const:a20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00782f34",
      "incomplete_value": false,
      "site": "00782f38",
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
            "const:620:8"
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
      "00782f78",
      "DATA",
      [
        "storage",
        "00c78620",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00782f78",
      "DATA",
      [
        "storage",
        "00c78a20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00782f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782f20.md#insn-00782f2c) · [`00782f34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782f20.md#insn-00782f34)
- 新版 `00782f6c`（命令位置の公開資料なし） · `00782f74`（命令位置の公開資料なし）

~~~diff
- 00782f2c ["INT_ADD", "register:40f0:8", ["const:782f2c:8", "const:4:8"]]
- 00782f2c ["CALL", null, ["callee:00c57e90:8"]]
+ 00782f6c ["INT_ADD", "register:40f0:8", ["const:782f6c:8", "const:4:8"]]
+ 00782f6c ["CALL", null, ["callee:00c57e90:8"]]
- 00782f2c bytes d9521394
+ 00782f6c bytes c9531394
- 00782f34 ["COPY", "tmp:0:8", ["const:620:8"]]
- 00782f34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00782f34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00782f34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00782f74 ["COPY", "tmp:0:8", ["const:a20:8"]]
+ 00782f74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00782f74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00782f74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00782f34 bytes 08811891
+ 00782f74 bytes 08812891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2d30514fd4e8b9a64262d282ca48256"></a>

### [`00782f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782f5c.md) → [`00782f9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00782/00782f9c.md) FUN_00782f9c

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.75% / 新版 93.75%

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
      "site": "00782fb8",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00782f78",
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
      "00782fb8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00782fb8",
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

- 旧版 [`00782f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782f5c.md#insn-00782f78) · [`00782f84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782f5c.md#insn-00782f84)
- 新版 `00782fb8`（命令位置の公開資料なし） · `00782fc4`（命令位置の公開資料なし）

~~~diff
- 00782f78 ["INT_ADD", "register:40f0:8", ["const:782f78:8", "const:4:8"]]
- 00782f78 ["CALL", null, ["ram:47acb4:8"]]
+ 00782fb8 ["INT_ADD", "register:40f0:8", ["const:782fb8:8", "const:4:8"]]
+ 00782fb8 ["CALL", null, ["ram:47acf4:8"]]
- 00782f78 bytes 4fdff397
+ 00782fb8 bytes 4fdff397
- 00782f84 ["INT_ADD", "register:40f0:8", ["const:782f84:8", "const:4:8"]]
- 00782f84 ["CALL", null, ["callee:0047cdd4:8"]]
+ 00782fc4 ["INT_ADD", "register:40f0:8", ["const:782fc4:8", "const:4:8"]]
+ 00782fc4 ["CALL", null, ["callee:0047cdd4:8"]]
- 00782f84 bytes 84e7f397
+ 00782fc4 bytes 84e7f397
~~~


<a id="compare-9d0c25ebe030fb8d8c64e8be0b1a22dd"></a>

### [`00782fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782fc8.md) → [`00783008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00783/00783008.md) FUN_00783008

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
      "definition_site": "0078301c",
      "incomplete_value": false,
      "site": "00783020",
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
            "const:aa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00782fdc",
      "incomplete_value": false,
      "site": "00782fe0",
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
            "const:6a0:8"
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
      "00783020",
      "DATA",
      [
        "storage",
        "00c786a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00783020",
      "DATA",
      [
        "storage",
        "00c78aa0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00782fd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782fc8.md#insn-00782fd4) · [`00782fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00782/00782fc8.md#insn-00782fdc)
- 新版 `00783014`（命令位置の公開資料なし） · `0078301c`（命令位置の公開資料なし）

~~~diff
- 00782fd4 ["INT_ADD", "register:40f0:8", ["const:782fd4:8", "const:4:8"]]
- 00782fd4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00783014 ["INT_ADD", "register:40f0:8", ["const:783014:8", "const:4:8"]]
+ 00783014 ["CALL", null, ["callee:00c57e90:8"]]
- 00782fd4 bytes af521394
+ 00783014 bytes 9f531394
- 00782fdc ["COPY", "tmp:0:8", ["const:6a0:8"]]
- 00782fdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00782fdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00782fdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0078301c ["COPY", "tmp:0:8", ["const:aa0:8"]]
+ 0078301c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0078301c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0078301c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00782fdc bytes 08811a91
+ 0078301c bytes 08812a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9601cf2d673548a77a333ba13cc421ca"></a>

### [`00783098`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/00783098.md) → [`007830d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00783/007830d8.md) FUN_007830d8

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
      "definition_site": "007830ec",
      "incomplete_value": false,
      "site": "007830f0",
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
            "const:b20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007830ac",
      "incomplete_value": false,
      "site": "007830b0",
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
            "const:720:8"
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
      "007830f0",
      "DATA",
      [
        "storage",
        "00c78720",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007830f0",
      "DATA",
      [
        "storage",
        "00c78b20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007830a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/00783098.md#insn-007830a4) · [`007830ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/00783098.md#insn-007830ac)
- 新版 `007830e4`（命令位置の公開資料なし） · `007830ec`（命令位置の公開資料なし）

~~~diff
- 007830a4 ["INT_ADD", "register:40f0:8", ["const:7830a4:8", "const:4:8"]]
- 007830a4 ["CALL", null, ["callee:00c57e90:8"]]
+ 007830e4 ["INT_ADD", "register:40f0:8", ["const:7830e4:8", "const:4:8"]]
+ 007830e4 ["CALL", null, ["callee:00c57e90:8"]]
- 007830a4 bytes 7b521394
+ 007830e4 bytes 6b531394
- 007830ac ["COPY", "tmp:0:8", ["const:720:8"]]
- 007830ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007830ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007830ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007830ec ["COPY", "tmp:0:8", ["const:b20:8"]]
+ 007830ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007830ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007830ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007830ac bytes 08811c91
+ 007830ec bytes 08812c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78b87cfb40f0bf6f67cc6b29530bbcb0"></a>

### [`007830d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/007830d4.md) → [`00783114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00783/00783114.md) FUN_00783114

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
      "site": "00783138",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007830f8",
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
      "00783138",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00783138",
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

- 旧版 [`007830f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/007830d4.md#insn-007830f8) · [`00783104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/007830d4.md#insn-00783104)
- 新版 `00783138`（命令位置の公開資料なし） · `00783144`（命令位置の公開資料なし）

~~~diff
- 007830f8 ["INT_ADD", "register:40f0:8", ["const:7830f8:8", "const:4:8"]]
- 007830f8 ["CALL", null, ["ram:47acb4:8"]]
+ 00783138 ["INT_ADD", "register:40f0:8", ["const:783138:8", "const:4:8"]]
+ 00783138 ["CALL", null, ["ram:47acf4:8"]]
- 007830f8 bytes efdef397
+ 00783138 bytes efdef397
- 00783104 ["INT_ADD", "register:40f0:8", ["const:783104:8", "const:4:8"]]
- 00783104 ["CALL", null, ["callee:0047cdd4:8"]]
+ 00783144 ["INT_ADD", "register:40f0:8", ["const:783144:8", "const:4:8"]]
+ 00783144 ["CALL", null, ["callee:0047cdd4:8"]]
- 00783104 bytes 24e7f397
+ 00783144 bytes 24e7f397
~~~


<a id="compare-9408861bc8f2ab8554138ba115b9d6f5"></a>

### [`00783148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/00783148.md) → [`00783188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00783/00783188.md) FUN_00783188

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
      "definition_site": "0078319c",
      "incomplete_value": false,
      "site": "007831a0",
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
            "const:ba0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078315c",
      "incomplete_value": false,
      "site": "00783160",
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
            "const:7a0:8"
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
      "007831a0",
      "DATA",
      [
        "storage",
        "00c787a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007831a0",
      "DATA",
      [
        "storage",
        "00c78ba0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00783154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/00783148.md#insn-00783154) · [`0078315c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/00783148.md#insn-0078315c)
- 新版 `00783194`（命令位置の公開資料なし） · `0078319c`（命令位置の公開資料なし）

~~~diff
- 00783154 ["INT_ADD", "register:40f0:8", ["const:783154:8", "const:4:8"]]
- 00783154 ["CALL", null, ["callee:00c57e90:8"]]
+ 00783194 ["INT_ADD", "register:40f0:8", ["const:783194:8", "const:4:8"]]
+ 00783194 ["CALL", null, ["callee:00c57e90:8"]]
- 00783154 bytes 4f521394
+ 00783194 bytes 3f531394
- 0078315c ["COPY", "tmp:0:8", ["const:7a0:8"]]
- 0078315c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0078315c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0078315c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0078319c ["COPY", "tmp:0:8", ["const:ba0:8"]]
+ 0078319c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0078319c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0078319c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0078315c bytes 08811e91
+ 0078319c bytes 08812e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b6baa1e251b6cc31a6c01e7b0cc8108"></a>

### [`00783184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/00783184.md) → [`007831c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00783/007831c4.md) FUN_007831c4

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
      "site": "007831e8",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007831a8",
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
      "007831e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "007831e8",
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

- 旧版 [`007831a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/00783184.md#insn-007831a8) · [`007831b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/00783184.md#insn-007831b4)
- 新版 `007831e8`（命令位置の公開資料なし） · `007831f4`（命令位置の公開資料なし）

~~~diff
- 007831a8 ["INT_ADD", "register:40f0:8", ["const:7831a8:8", "const:4:8"]]
- 007831a8 ["CALL", null, ["ram:47acb4:8"]]
+ 007831e8 ["INT_ADD", "register:40f0:8", ["const:7831e8:8", "const:4:8"]]
+ 007831e8 ["CALL", null, ["ram:47acf4:8"]]
- 007831a8 bytes c3def397
+ 007831e8 bytes c3def397
- 007831b4 ["INT_ADD", "register:40f0:8", ["const:7831b4:8", "const:4:8"]]
- 007831b4 ["CALL", null, ["callee:0047cdd4:8"]]
+ 007831f4 ["INT_ADD", "register:40f0:8", ["const:7831f4:8", "const:4:8"]]
+ 007831f4 ["CALL", null, ["callee:0047cdd4:8"]]
- 007831b4 bytes f8e6f397
+ 007831f4 bytes f8e6f397
~~~


<a id="compare-fb13ef63d85838da972f7d2285c58861"></a>

### [`007831f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/007831f8.md) → [`00783238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00783/00783238.md) FUN_00783238

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
      "definition_site": "0078324c",
      "incomplete_value": false,
      "site": "00783250",
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
            "const:c20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078320c",
      "incomplete_value": false,
      "site": "00783210",
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
            "const:820:8"
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
      "00783250",
      "DATA",
      [
        "storage",
        "00c78820",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00783250",
      "DATA",
      [
        "storage",
        "00c78c20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00783204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/007831f8.md#insn-00783204) · [`0078320c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/007831f8.md#insn-0078320c)
- 新版 `00783244`（命令位置の公開資料なし） · `0078324c`（命令位置の公開資料なし）

~~~diff
- 00783204 ["INT_ADD", "register:40f0:8", ["const:783204:8", "const:4:8"]]
- 00783204 ["CALL", null, ["callee:00c57e90:8"]]
+ 00783244 ["INT_ADD", "register:40f0:8", ["const:783244:8", "const:4:8"]]
+ 00783244 ["CALL", null, ["callee:00c57e90:8"]]
- 00783204 bytes 23521394
+ 00783244 bytes 13531394
- 0078320c ["COPY", "tmp:0:8", ["const:820:8"]]
- 0078320c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0078320c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0078320c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0078324c ["COPY", "tmp:0:8", ["const:c20:8"]]
+ 0078324c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0078324c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0078324c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0078320c bytes 08812091
+ 0078324c bytes 08813091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e76815562a84b567753b00ecb56f2711"></a>

### [`00783234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/00783234.md) → [`00783274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00783/00783274.md) FUN_00783274

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0044bed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044bed4.md) [`0044bfec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044b/0044bfec.md) [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048e7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e7a0.md) [`0048eeb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048eeb0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0044bf14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044b/0044bf14.md) [`0044c02c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044c/0044c02c.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048e7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e7e0.md) [`0048eef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048eef0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.55% / 新版 94.55%

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
      "site": "007832c4",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00783284",
      "value": [
        "leaf",
        "ram:48ccb8:8"
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
      "007832c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "007832d4",
      "READ",
      [
        "storage",
        "002bb223",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007832c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "007832d4",
      "READ",
      [
        "storage",
        "002bb263",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00783284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/00783234.md#insn-00783284) · [`00783264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/00783234.md#insn-00783264) · [`00783270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/00783234.md#insn-00783270)
- 新版 `007832c4`（命令位置の公開資料なし） · `007832a4`（命令位置の公開資料なし） · `007832b0`（命令位置の公開資料なし）

~~~diff
- 00783284 ["INT_ADD", "register:40f0:8", ["const:783284:8", "const:4:8"]]
- 00783284 ["CALL", null, ["ram:48ccb8:8"]]
+ 007832c4 ["INT_ADD", "register:40f0:8", ["const:7832c4:8", "const:4:8"]]
+ 007832c4 ["CALL", null, ["ram:48ccf8:8"]]
- 00783284 bytes 8d26f497
+ 007832c4 bytes 8d26f497
- 00783264 ["INT_ADD", "register:40f0:8", ["const:783264:8", "const:4:8"]]
- 00783264 ["CALL", null, ["callee:0044c02c:8"]]
+ 007832a4 ["INT_ADD", "register:40f0:8", ["const:7832a4:8", "const:4:8"]]
+ 007832a4 ["CALL", null, ["callee:0044c02c:8"]]
- 00783264 bytes 6223f397
+ 007832a4 bytes 6223f397
- 00783270 ["INT_ADD", "register:40f0:8", ["const:783270:8", "const:4:8"]]
- 00783270 ["CALL", null, ["callee:0044bf14:8"]]
+ 007832b0 ["INT_ADD", "register:40f0:8", ["const:7832b0:8", "const:4:8"]]
+ 007832b0 ["CALL", null, ["callee:0044bf14:8"]]
- 00783270 bytes 1923f397
+ 007832b0 bytes 1923f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4fa97a64644ae69369281c87b1a6f604"></a>

### [`00783388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/00783388.md) → [`007833c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00783/007833c8.md) FUN_007833c8

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
      "definition_site": "007833dc",
      "incomplete_value": false,
      "site": "007833e0",
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
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078339c",
      "incomplete_value": false,
      "site": "007833a0",
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
            "const:8a0:8"
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
      "007833e0",
      "DATA",
      [
        "storage",
        "00c788a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007833e0",
      "DATA",
      [
        "storage",
        "00c78ca0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00783394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/00783388.md#insn-00783394) · [`0078339c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/00783388.md#insn-0078339c)
- 新版 `007833d4`（命令位置の公開資料なし） · `007833dc`（命令位置の公開資料なし）

~~~diff
- 00783394 ["INT_ADD", "register:40f0:8", ["const:783394:8", "const:4:8"]]
- 00783394 ["CALL", null, ["callee:00c57e90:8"]]
+ 007833d4 ["INT_ADD", "register:40f0:8", ["const:7833d4:8", "const:4:8"]]
+ 007833d4 ["CALL", null, ["callee:00c57e90:8"]]
- 00783394 bytes bf511394
+ 007833d4 bytes af521394
- 0078339c ["COPY", "tmp:0:8", ["const:8a0:8"]]
- 0078339c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0078339c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0078339c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007833dc ["COPY", "tmp:0:8", ["const:ca0:8"]]
+ 007833dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007833dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007833dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0078339c bytes 08812291
+ 007833dc bytes 08813291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66dd842ec54ddc7238e443a4b516ef19"></a>

### [`00783434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/00783434.md) → [`00783474`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00783/00783474.md) FUN_00783474

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
      "definition_site": "00783488",
      "incomplete_value": false,
      "site": "0078348c",
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
            "const:d20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00783448",
      "incomplete_value": false,
      "site": "0078344c",
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
            "const:920:8"
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
      "0078348c",
      "DATA",
      [
        "storage",
        "00c78920",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0078348c",
      "DATA",
      [
        "storage",
        "00c78d20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00783440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/00783434.md#insn-00783440) · [`00783448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/00783434.md#insn-00783448)
- 新版 `00783480`（命令位置の公開資料なし） · `00783488`（命令位置の公開資料なし）

~~~diff
- 00783440 ["INT_ADD", "register:40f0:8", ["const:783440:8", "const:4:8"]]
- 00783440 ["CALL", null, ["callee:00c57e90:8"]]
+ 00783480 ["INT_ADD", "register:40f0:8", ["const:783480:8", "const:4:8"]]
+ 00783480 ["CALL", null, ["callee:00c57e90:8"]]
- 00783440 bytes 94511394
+ 00783480 bytes 84521394
- 00783448 ["COPY", "tmp:0:8", ["const:920:8"]]
- 00783448 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00783448 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00783448 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00783488 ["COPY", "tmp:0:8", ["const:d20:8"]]
+ 00783488 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00783488 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00783488 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00783448 bytes 08812491
+ 00783488 bytes 08813491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c99e95ed59d2e9a1328481630e5f672"></a>

### [`00783470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/00783470.md) → [`007834b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00783/007834b0.md) FUN_007834b0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0044edfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044e/0044edfc.md) [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048e7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e7a0.md) [`0048eeb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048eeb0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0044ee3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044e/0044ee3c.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048e7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048e7e0.md) [`0048eef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048e/0048eef0.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.94% / 新版 91.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00783508",
      "incomplete_value": true,
      "site": "00783508",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:263:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007834c8",
      "incomplete_value": true,
      "site": "007834c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:223:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "007834dc",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0078349c",
      "value": [
        "leaf",
        "ram:48ccb8:8"
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
      "site": "0078357c",
      "value": [
        "leaf",
        "ram:48ccf8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0078353c",
      "value": [
        "leaf",
        "ram:48ccb8:8"
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
      "007834dc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "007834f8",
      "READ",
      [
        "storage",
        "002bb223",
        null,
        "string"
      ]
    ],
    [
      "00783564",
      "DATA",
      [
        "storage",
        "0039b1bc",
        "fde_0039b1bc",
        "dword"
      ]
    ]
  ],
  "added": [
    [
      "007834dc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "007834f8",
      "READ",
      [
        "storage",
        "002bb263",
        null,
        "string"
      ]
    ],
    [
      "00783564",
      "DATA",
      [
        "storage",
        "0039b1bc",
        null,
        "uleb128"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078349c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/00783470.md#insn-0078349c) · [`0078353c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/00783470.md#insn-0078353c) · [`007834a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/00783470.md#insn-007834a8)
- 新版 `007834dc`（命令位置の公開資料なし） · `0078357c`（命令位置の公開資料なし） · `007834e8`（命令位置の公開資料なし）

~~~diff
- 0078349c ["INT_ADD", "register:40f0:8", ["const:78349c:8", "const:4:8"]]
- 0078349c ["CALL", null, ["ram:48ccb8:8"]]
+ 007834dc ["INT_ADD", "register:40f0:8", ["const:7834dc:8", "const:4:8"]]
+ 007834dc ["CALL", null, ["ram:48ccf8:8"]]
- 0078349c bytes 0726f497
+ 007834dc bytes 0726f497
- 0078353c ["INT_ADD", "register:40f0:8", ["const:78353c:8", "const:4:8"]]
- 0078353c ["CALL", null, ["ram:48ccb8:8"]]
+ 0078357c ["INT_ADD", "register:40f0:8", ["const:78357c:8", "const:4:8"]]
+ 0078357c ["CALL", null, ["ram:48ccf8:8"]]
- 0078353c bytes df25f497
+ 0078357c bytes df25f497
- 007834a8 ["INT_ADD", "register:40f0:8", ["const:7834a8:8", "const:4:8"]]
- 007834a8 ["CALL", null, ["callee:0044ee3c:8"]]
+ 007834e8 ["INT_ADD", "register:40f0:8", ["const:7834e8:8", "const:4:8"]]
+ 007834e8 ["CALL", null, ["callee:0044ee3c:8"]]
- 007834a8 bytes 552ef397
+ 007834e8 bytes 552ef397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2308ca47680da314ceec530f3d8d29e"></a>

### [`007835d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/007835d0.md) → [`00783610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00783/00783610.md) FUN_00783610

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
      "definition_site": "00783624",
      "incomplete_value": false,
      "site": "00783628",
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
    "old": {
      "definition_site": "007835e4",
      "incomplete_value": false,
      "site": "007835e8",
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
            "const:9a0:8"
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
      "00783628",
      "DATA",
      [
        "storage",
        "00c789a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00783628",
      "DATA",
      [
        "storage",
        "00c78da0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007835dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/007835d0.md#insn-007835dc) · [`007835e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/007835d0.md#insn-007835e4)
- 新版 `0078361c`（命令位置の公開資料なし） · `00783624`（命令位置の公開資料なし）

~~~diff
- 007835dc ["INT_ADD", "register:40f0:8", ["const:7835dc:8", "const:4:8"]]
- 007835dc ["CALL", null, ["callee:00c57e90:8"]]
+ 0078361c ["INT_ADD", "register:40f0:8", ["const:78361c:8", "const:4:8"]]
+ 0078361c ["CALL", null, ["callee:00c57e90:8"]]
- 007835dc bytes 2d511394
+ 0078361c bytes 1d521394
- 007835e4 ["COPY", "tmp:0:8", ["const:9a0:8"]]
- 007835e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007835e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007835e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00783624 ["COPY", "tmp:0:8", ["const:da0:8"]]
+ 00783624 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00783624 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00783624 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007835e4 bytes 08812691
+ 00783624 bytes 08813691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77164872b26a5793364b6a96d3fd1702"></a>

### [`0078360c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/0078360c.md) → [`0078364c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00783/0078364c.md) FUN_0078364c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md) [`00a1a508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a508.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00a1a6a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a1a/00a1a6a4.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.55% / 新版 96.55%

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
      "site": "00783670",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00783630",
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
      "00783670",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00783670",
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

- 旧版 [`00783630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/0078360c.md#insn-00783630) · [`00783670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/0078360c.md#insn-00783670) · [`0078363c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/0078360c.md#insn-0078363c)
- 新版 `00783670`（命令位置の公開資料なし） · `007836b0`（命令位置の公開資料なし） · `0078367c`（命令位置の公開資料なし）

~~~diff
- 00783630 ["INT_ADD", "register:40f0:8", ["const:783630:8", "const:4:8"]]
- 00783630 ["CALL", null, ["ram:47acb4:8"]]
+ 00783670 ["INT_ADD", "register:40f0:8", ["const:783670:8", "const:4:8"]]
+ 00783670 ["CALL", null, ["ram:47acf4:8"]]
- 00783630 bytes a1ddf397
+ 00783670 bytes a1ddf397
- 00783670 ["INT_ADD", "register:40f0:8", ["const:783670:8", "const:4:8"]]
- 00783670 ["CALL", null, ["callee:008514f8:8"]]
+ 007836b0 ["INT_ADD", "register:40f0:8", ["const:7836b0:8", "const:4:8"]]
+ 007836b0 ["CALL", null, ["callee:008514f8:8"]]
- 00783670 bytes 92370394
+ 007836b0 bytes 92370394
- 0078363c ["INT_ADD", "register:40f0:8", ["const:78363c:8", "const:4:8"]]
- 0078363c ["CALL", null, ["callee:0047cdd4:8"]]
+ 0078367c ["INT_ADD", "register:40f0:8", ["const:78367c:8", "const:4:8"]]
+ 0078367c ["CALL", null, ["callee:0047cdd4:8"]]
- 0078363c bytes d6e5f397
+ 0078367c bytes d6e5f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22040148fc0d8cd8d921712f343ecebf"></a>

### [`007836ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/007836ac.md) → [`007836ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00783/007836ec.md) FUN_007836ec

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
      "definition_site": "00783700",
      "incomplete_value": false,
      "site": "00783704",
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
    "old": {
      "definition_site": "007836c0",
      "incomplete_value": false,
      "site": "007836c4",
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
            "const:a20:8"
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
      "00783704",
      "DATA",
      [
        "storage",
        "00c78a20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00783704",
      "DATA",
      [
        "storage",
        "00c78e20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007836b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/007836ac.md#insn-007836b8) · [`007836c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/007836ac.md#insn-007836c0)
- 新版 `007836f8`（命令位置の公開資料なし） · `00783700`（命令位置の公開資料なし）

~~~diff
- 007836b8 ["INT_ADD", "register:40f0:8", ["const:7836b8:8", "const:4:8"]]
- 007836b8 ["CALL", null, ["callee:00c57e90:8"]]
+ 007836f8 ["INT_ADD", "register:40f0:8", ["const:7836f8:8", "const:4:8"]]
+ 007836f8 ["CALL", null, ["callee:00c57e90:8"]]
- 007836b8 bytes f6501394
+ 007836f8 bytes e6511394
- 007836c0 ["COPY", "tmp:0:8", ["const:a20:8"]]
- 007836c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007836c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007836c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00783700 ["COPY", "tmp:0:8", ["const:e20:8"]]
+ 00783700 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00783700 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00783700 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007836c0 bytes 08812891
+ 00783700 bytes 08813891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce60707a47b5528f0533a35ece6760d4"></a>

### [`007836e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/007836e8.md) → [`00783728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00783/00783728.md) FUN_00783728

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.75% / 新版 93.75%

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
      "site": "00783744",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00783704",
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
      "00783744",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00783744",
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

- 旧版 [`00783704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/007836e8.md#insn-00783704) · [`00783710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/007836e8.md#insn-00783710)
- 新版 `00783744`（命令位置の公開資料なし） · `00783750`（命令位置の公開資料なし）

~~~diff
- 00783704 ["INT_ADD", "register:40f0:8", ["const:783704:8", "const:4:8"]]
- 00783704 ["CALL", null, ["ram:47acb4:8"]]
+ 00783744 ["INT_ADD", "register:40f0:8", ["const:783744:8", "const:4:8"]]
+ 00783744 ["CALL", null, ["ram:47acf4:8"]]
- 00783704 bytes 6cddf397
+ 00783744 bytes 6cddf397
- 00783710 ["INT_ADD", "register:40f0:8", ["const:783710:8", "const:4:8"]]
- 00783710 ["CALL", null, ["callee:0047cdd4:8"]]
+ 00783750 ["INT_ADD", "register:40f0:8", ["const:783750:8", "const:4:8"]]
+ 00783750 ["CALL", null, ["callee:0047cdd4:8"]]
- 00783710 bytes a1e5f397
+ 00783750 bytes a1e5f397
~~~


<a id="compare-834a7be8df8d98ed26da5548f460155a"></a>

### [`00783750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/00783750.md) → [`00783790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00783/00783790.md) FUN_00783790

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "0078379c",
      "incomplete_value": false,
      "site": "007837a0",
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
    "old": {
      "definition_site": "0078375c",
      "incomplete_value": false,
      "site": "00783760",
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
            "const:aa0:8"
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
      "007837a0",
      "DATA",
      [
        "storage",
        "00c78aa0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007837a0",
      "DATA",
      [
        "storage",
        "00c78ea0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078375c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/00783750.md#insn-0078375c)
- 新版 `0078379c`（命令位置の公開資料なし）

~~~diff
- 0078375c ["COPY", "tmp:0:8", ["const:aa0:8"]]
- 0078375c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0078375c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0078375c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0078379c ["COPY", "tmp:0:8", ["const:ea0:8"]]
+ 0078379c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0078379c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0078379c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0078375c bytes 29812a91
+ 0078379c bytes 29813a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10cfc064dceb62b53017018dde18e8b6"></a>

### [`00783774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/00783774.md) → [`007837b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00783/007837b4.md) FUN_007837b4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

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
      "definition_site": "007837bc",
      "incomplete_value": false,
      "site": "007837c0",
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
    "old": {
      "definition_site": "0078377c",
      "incomplete_value": false,
      "site": "00783780",
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
            "const:aa0:8"
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
      "007837c0",
      "DATA",
      [
        "storage",
        "00c78aa0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007837c0",
      "DATA",
      [
        "storage",
        "00c78ea0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078377c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/00783774.md#insn-0078377c) · [`007837a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/00783774.md#insn-007837a0)
- 新版 `007837bc`（命令位置の公開資料なし） · `007837e0`（命令位置の公開資料なし）

~~~diff
- 0078377c ["COPY", "tmp:0:8", ["const:aa0:8"]]
- 0078377c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0078377c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0078377c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007837bc ["COPY", "tmp:0:8", ["const:ea0:8"]]
+ 007837bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007837bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007837bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0078377c bytes 29812a91
+ 007837bc bytes 29813a91
- 007837a0 ["INT_ADD", "register:40f0:8", ["const:7837a0:8", "const:4:8"]]
- 007837a0 ["CALL", null, ["callee:00c57eb0:8"]]
+ 007837e0 ["INT_ADD", "register:40f0:8", ["const:7837e0:8", "const:4:8"]]
+ 007837e0 ["CALL", null, ["callee:00c57eb0:8"]]
- 007837a0 bytes c4501394
+ 007837e0 bytes b4511394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ccaa26704bf785d026cf4cd8cc31712e"></a>

### [`007837b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/007837b4.md) → [`007837f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00783/007837f4.md) FUN_007837f4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0077c80c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c80c.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0077c84c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077c/0077c84c.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

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
      "definition_site": "00783814",
      "incomplete_value": false,
      "site": "0078381c",
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
    "old": {
      "definition_site": "007837d4",
      "incomplete_value": false,
      "site": "007837dc",
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
            "const:aa0:8"
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
      "0078381c",
      "DATA",
      [
        "storage",
        "00c78aa0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0078381c",
      "DATA",
      [
        "storage",
        "00c78ea0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007837cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/007837b4.md#insn-007837cc) · [`007837d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/007837b4.md#insn-007837d4) · [`00783830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/007837b4.md#insn-00783830)
- 新版 `0078380c`（命令位置の公開資料なし） · `00783814`（命令位置の公開資料なし） · `00783870`（命令位置の公開資料なし）

~~~diff
- 007837cc ["INT_ADD", "register:40f0:8", ["const:7837cc:8", "const:4:8"]]
- 007837cc ["CALL", null, ["callee:00c57e90:8"]]
+ 0078380c ["INT_ADD", "register:40f0:8", ["const:78380c:8", "const:4:8"]]
+ 0078380c ["CALL", null, ["callee:00c57e90:8"]]
- 007837cc bytes b1501394
+ 0078380c bytes a1511394
- 007837d4 ["COPY", "tmp:0:8", ["const:aa0:8"]]
- 007837d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007837d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007837d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00783814 ["COPY", "tmp:0:8", ["const:ea0:8"]]
+ 00783814 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00783814 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00783814 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007837d4 bytes 08812a91
+ 00783814 bytes 08813a91
- 00783830 ["INT_ADD", "register:40f0:8", ["const:783830:8", "const:4:8"]]
- 00783830 ["CALL", null, ["callee:00c57e90:8"]]
+ 00783870 ["INT_ADD", "register:40f0:8", ["const:783870:8", "const:4:8"]]
+ 00783870 ["CALL", null, ["callee:00c57e90:8"]]
- 00783830 bytes 98501394
+ 00783870 bytes 88511394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a555203788ef8117db988f0cef666d2f"></a>

### [`00783894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/00783894.md) → [`007838d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00783/007838d4.md) FUN_007838d4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0077c80c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0077c/0077c80c.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0077c84c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0077c/0077c84c.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

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
      "definition_site": "007838f8",
      "incomplete_value": false,
      "site": "00783904",
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
    "old": {
      "definition_site": "007838b8",
      "incomplete_value": false,
      "site": "007838c4",
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
            "const:aa0:8"
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
      "00783904",
      "DATA",
      [
        "storage",
        "00c78aa0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00783904",
      "DATA",
      [
        "storage",
        "00c78ea0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00783904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/00783894.md#insn-00783904) · [`007838b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/00783894.md#insn-007838b8) · [`0078391c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/00783894.md#insn-0078391c)
- 新版 `00783944`（命令位置の公開資料なし） · `007838f8`（命令位置の公開資料なし） · `0078395c`（命令位置の公開資料なし）

~~~diff
- 00783904 ["INT_ADD", "register:40f0:8", ["const:783904:8", "const:4:8"]]
- 00783904 ["CALL", null, ["callee:00c57e90:8"]]
+ 00783944 ["INT_ADD", "register:40f0:8", ["const:783944:8", "const:4:8"]]
+ 00783944 ["CALL", null, ["callee:00c57e90:8"]]
- 00783904 bytes 63501394
+ 00783944 bytes 53511394
- 007838b8 ["COPY", "tmp:0:8", ["const:aa0:8"]]
- 007838b8 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
- 007838b8 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
- 007838b8 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
+ 007838f8 ["COPY", "tmp:0:8", ["const:ea0:8"]]
+ 007838f8 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
+ 007838f8 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
+ 007838f8 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
- 007838b8 bytes 6b812a91
+ 007838f8 bytes 6b813a91
- 0078391c ["INT_ADD", "register:40f0:8", ["const:78391c:8", "const:4:8"]]
- 0078391c ["CALL", null, ["callee:00c58000:8"]]
+ 0078395c ["INT_ADD", "register:40f0:8", ["const:78395c:8", "const:4:8"]]
+ 0078395c ["CALL", null, ["callee:00c58000:8"]]
- 0078391c bytes b9501394
+ 0078395c bytes a9511394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d353879b4cc5aef63e56dd656f8e9a05"></a>

### [`007839a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/007839a8.md) → [`007839e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00783/007839e8.md) FUN_007839e8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 24件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md)
- 新版 呼出元 0件  · 呼出先 24件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.19% / 新版 97.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 2件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00783db4",
      "incomplete_value": false,
      "site": "00783db4",
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
            "const:df7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00783d74",
      "incomplete_value": false,
      "site": "00783d74",
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
            "const:d2a:8"
          ]
        ]
      ]
    },
    "ordinal": 57,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00783dd0",
      "incomplete_value": false,
      "site": "00783ddc",
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
            "const:54c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00783d90",
      "incomplete_value": false,
      "site": "00783d9c",
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
            "const:50c:8"
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
      "definition_site": "00783e08",
      "incomplete_value": true,
      "site": "00783e1c",
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
                "register:4040:8"
              ],
              [
                "leaf",
                "const:c09:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00783dc8",
      "incomplete_value": true,
      "site": "00783ddc",
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
                "register:4040:8"
              ],
              [
                "leaf",
                "const:bc9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 64,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00783d54",
      "PARAM",
      [
        "storage",
        "002bb771",
        null,
        "string"
      ]
    ],
    [
      "00783d94",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071c420"
      ]
    ],
    [
      "00783db4",
      "DATA",
      [
        "storage",
        "002a8d2a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00783d54",
      "PARAM",
      [
        "storage",
        "002bb7b1",
        null,
        "string"
      ]
    ],
    [
      "00783d94",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071c460"
      ]
    ],
    [
      "00783db4",
      "DATA",
      [
        "storage",
        "002a8df7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00783d14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/007839a8.md#insn-00783d14) · [`00783d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/007839a8.md#insn-00783d18) · [`00783d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00783/007839a8.md#insn-00783d54)
- 新版 `00783d54`（命令位置の公開資料なし） · `00783d58`（命令位置の公開資料なし） · `00783d94`（命令位置の公開資料なし）

~~~diff
- 00783d14 ["COPY", "tmp:0:8", ["const:771:8"]]
- 00783d14 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00783d14 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00783d14 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00783d54 ["COPY", "tmp:0:8", ["const:7b1:8"]]
+ 00783d54 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00783d54 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00783d54 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00783d14 bytes 42c41d91
+ 00783d54 bytes 42c41e91
- 00783d18 ["INT_ADD", "register:40f0:8", ["const:783d18:8", "const:4:8"]]
- 00783d18 ["CALL", null, ["callee:00c57f60:8"]]
+ 00783d58 ["INT_ADD", "register:40f0:8", ["const:783d58:8", "const:4:8"]]
+ 00783d58 ["CALL", null, ["callee:00c57f60:8"]]
- 00783d18 bytes 924f1394
+ 00783d58 bytes 82501394
- 00783d54 ["INT_ADD", "register:40f0:8", ["const:783d54:8", "const:4:8"]]
- 00783d54 ["CALL", null, ["ram:71c420:8"]]
+ 00783d94 ["INT_ADD", "register:40f0:8", ["const:783d94:8", "const:4:8"]]
+ 00783d94 ["CALL", null, ["ram:71c460:8"]]
- 00783d54 bytes b361fe97
+ 00783d94 bytes b361fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2672663c8b404637e6435c3cd4a7fa3c"></a>

### [`007842cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00784/007842cc.md) → [`0078430c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00784/0078430c.md) FUN_0078430c

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
      "definition_site": "00784330",
      "incomplete_value": false,
      "site": "00784330",
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
    "old": {
      "definition_site": "007842f0",
      "incomplete_value": false,
      "site": "007842f0",
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
            "const:b20:8"
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
      "00784330",
      "DATA",
      [
        "storage",
        "00c78b20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00784330",
      "DATA",
      [
        "storage",
        "00c78f20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007842e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00784/007842cc.md#insn-007842e0) · [`007842ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00784/007842cc.md#insn-007842ec)
- 新版 `00784320`（命令位置の公開資料なし） · `0078432c`（命令位置の公開資料なし）

~~~diff
- 007842e0 ["INT_ADD", "register:40f0:8", ["const:7842e0:8", "const:4:8"]]
- 007842e0 ["CALL", null, ["callee:00c57e90:8"]]
+ 00784320 ["INT_ADD", "register:40f0:8", ["const:784320:8", "const:4:8"]]
+ 00784320 ["CALL", null, ["callee:00c57e90:8"]]
- 007842e0 bytes ec4d1394
+ 00784320 bytes dc4e1394
- 007842ec ["COPY", "tmp:0:8", ["const:b20:8"]]
- 007842ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007842ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007842ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0078432c ["COPY", "tmp:0:8", ["const:f20:8"]]
+ 0078432c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0078432c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0078432c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007842ec bytes 08812c91
+ 0078432c bytes 08813c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19a859bade22a4b13f294b7acb2ed61a"></a>

### [`0078431c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00784/0078431c.md) → [`0078435c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00784/0078435c.md) FUN_0078435c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.00% / 新版 96.00%

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
      "site": "007843a0",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00784360",
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
      "007843a0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "007843a0",
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

- 旧版 [`00784360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00784/0078431c.md#insn-00784360) · [`0078436c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00784/0078431c.md#insn-0078436c)
- 新版 `007843a0`（命令位置の公開資料なし） · `007843ac`（命令位置の公開資料なし）

~~~diff
- 00784360 ["INT_ADD", "register:40f0:8", ["const:784360:8", "const:4:8"]]
- 00784360 ["CALL", null, ["ram:47acb4:8"]]
+ 007843a0 ["INT_ADD", "register:40f0:8", ["const:7843a0:8", "const:4:8"]]
+ 007843a0 ["CALL", null, ["ram:47acf4:8"]]
- 00784360 bytes 55daf397
+ 007843a0 bytes 55daf397
- 0078436c ["INT_ADD", "register:40f0:8", ["const:78436c:8", "const:4:8"]]
- 0078436c ["CALL", null, ["callee:0047cdd4:8"]]
+ 007843ac ["INT_ADD", "register:40f0:8", ["const:7843ac:8", "const:4:8"]]
+ 007843ac ["CALL", null, ["callee:0047cdd4:8"]]
- 0078436c bytes 8ae2f397
+ 007843ac bytes 8ae2f397
~~~


<a id="compare-9a30ec3084736349c5edfafdf46cad56"></a>

### [`007843ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00784/007843ac.md) → [`007843ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00784/007843ec.md) FUN_007843ec

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
      "definition_site": "00784410",
      "incomplete_value": false,
      "site": "00784414",
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
    "old": {
      "definition_site": "007843d0",
      "incomplete_value": false,
      "site": "007843d4",
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
      "00784414",
      "DATA",
      [
        "storage",
        "00c78ba0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00784414",
      "DATA",
      [
        "storage",
        "00c78fa0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007843c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00784/007843ac.md#insn-007843c0) · [`007843d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00784/007843ac.md#insn-007843d0)
- 新版 `00784400`（命令位置の公開資料なし） · `00784410`（命令位置の公開資料なし）

~~~diff
- 007843c0 ["INT_ADD", "register:40f0:8", ["const:7843c0:8", "const:4:8"]]
- 007843c0 ["CALL", null, ["callee:00c57e90:8"]]
+ 00784400 ["INT_ADD", "register:40f0:8", ["const:784400:8", "const:4:8"]]
+ 00784400 ["CALL", null, ["callee:00c57e90:8"]]
- 007843c0 bytes b44d1394
+ 00784400 bytes a44e1394
- 007843d0 ["COPY", "tmp:0:8", ["const:ba0:8"]]
- 007843d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007843d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007843d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00784410 ["COPY", "tmp:0:8", ["const:fa0:8"]]
+ 00784410 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00784410 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00784410 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007843d0 bytes 08812e91
+ 00784410 bytes 08813e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5feb457a94eb72acdb7664d254949989"></a>

### [`00784414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00784/00784414.md) → [`00784454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00784/00784454.md) FUN_00784454

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 24件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md)
- 新版 呼出元 0件  · 呼出先 24件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0046d490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d490.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.36% / 新版 95.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件, `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0078457c",
      "incomplete_value": false,
      "site": "0078457c",
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
            "const:90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078453c",
      "incomplete_value": false,
      "site": "0078453c",
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
            "const:c90:8"
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
      "definition_site": "0078463c",
      "incomplete_value": true,
      "site": "0078463c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:73d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007845fc",
      "incomplete_value": true,
      "site": "007845fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6fd:8"
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
      "definition_site": "00784838",
      "incomplete_value": true,
      "site": "00784838",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:34a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007847f8",
      "incomplete_value": true,
      "site": "007847f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:27d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 52,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "007844ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "007844bc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071be98"
      ]
    ],
    [
      "00784530",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071be98"
      ]
    ]
  ],
  "added": [
    [
      "007844ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "007844bc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bed8"
      ]
    ],
    [
      "00784530",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bed8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078446c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00784/00784414.md#insn-0078446c) · [`0078447c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00784/00784414.md#insn-0078447c) · [`007844f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00784/00784414.md#insn-007844f0)
- 新版 `007844ac`（命令位置の公開資料なし） · `007844bc`（命令位置の公開資料なし） · `00784530`（命令位置の公開資料なし）

~~~diff
- 0078446c ["INT_ADD", "register:40f0:8", ["const:78446c:8", "const:4:8"]]
- 0078446c ["CALL", null, ["ram:47acb4:8"]]
+ 007844ac ["INT_ADD", "register:40f0:8", ["const:7844ac:8", "const:4:8"]]
+ 007844ac ["CALL", null, ["ram:47acf4:8"]]
- 0078446c bytes 12daf397
+ 007844ac bytes 12daf397
- 0078447c ["INT_ADD", "register:40f0:8", ["const:78447c:8", "const:4:8"]]
- 0078447c ["CALL", null, ["ram:71be98:8"]]
+ 007844bc ["INT_ADD", "register:40f0:8", ["const:7844bc:8", "const:4:8"]]
+ 007844bc ["CALL", null, ["ram:71bed8:8"]]
- 0078447c bytes 875efe97
+ 007844bc bytes 875efe97
- 007844f0 ["INT_ADD", "register:40f0:8", ["const:7844f0:8", "const:4:8"]]
- 007844f0 ["CALL", null, ["ram:71be98:8"]]
+ 00784530 ["INT_ADD", "register:40f0:8", ["const:784530:8", "const:4:8"]]
+ 00784530 ["CALL", null, ["ram:71bed8:8"]]
- 007844f0 bytes 6a5efe97
+ 00784530 bytes 6a5efe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c42166b5f721fe2265a2472a03fe1488"></a>

### [`00784c18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00784/00784c18.md) → [`00784c58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00784/00784c58.md) FUN_00784c58

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
      "definition_site": "00784c7c",
      "incomplete_value": false,
      "site": "00784c80",
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
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00784c3c",
      "incomplete_value": false,
      "site": "00784c40",
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
            "const:c10:8"
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
      "00784c80",
      "DATA",
      [
        "storage",
        "00c78c10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00784c80",
      "DATA",
      [
        "storage",
        "00c79010",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00784c2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00784/00784c18.md#insn-00784c2c) · [`00784c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00784/00784c18.md#insn-00784c38) · [`00784c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00784/00784c18.md#insn-00784c3c)
- 新版 `00784c6c`（命令位置の公開資料なし） · `00784c78`（命令位置の公開資料なし） · `00784c7c`（命令位置の公開資料なし）

~~~diff
- 00784c2c ["INT_ADD", "register:40f0:8", ["const:784c2c:8", "const:4:8"]]
- 00784c2c ["CALL", null, ["callee:00c57e90:8"]]
+ 00784c6c ["INT_ADD", "register:40f0:8", ["const:784c6c:8", "const:4:8"]]
+ 00784c6c ["CALL", null, ["callee:00c57e90:8"]]
- 00784c2c bytes 994b1394
+ 00784c6c bytes 894c1394
- 00784c38 ["COPY", "register:4040:8", ["const:c78000:8"]]
+ 00784c78 ["COPY", "register:4040:8", ["const:c79000:8"]]
- 00784c38 bytes a8270090
+ 00784c78 bytes a82700b0
- 00784c3c ["COPY", "tmp:0:8", ["const:c10:8"]]
- 00784c3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00784c3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00784c3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00784c7c ["COPY", "tmp:0:8", ["const:10:8"]]
+ 00784c7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00784c7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00784c7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00784c3c bytes 08413091
+ 00784c7c bytes 08410091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b30bc9db2822993d9656c0c98cdbaf14"></a>

### [`00784c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00784/00784c58.md) → [`00784c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00784/00784c98.md) FUN_00784c98

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
      "definition_site": "00784c9c",
      "incomplete_value": false,
      "site": "00784ca0",
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
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00784c5c",
      "incomplete_value": false,
      "site": "00784c60",
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
            "const:c10:8"
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
      "00784ca0",
      "DATA",
      [
        "storage",
        "00c78c10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00784ca0",
      "DATA",
      [
        "storage",
        "00c79010",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00784c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00784/00784c58.md#insn-00784c58) · [`00784c5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00784/00784c58.md#insn-00784c5c)
- 新版 `00784c98`（命令位置の公開資料なし） · `00784c9c`（命令位置の公開資料なし）

~~~diff
- 00784c58 ["COPY", "register:4040:8", ["const:c78000:8"]]
+ 00784c98 ["COPY", "register:4040:8", ["const:c79000:8"]]
- 00784c58 bytes a8270090
+ 00784c98 bytes a82700b0
- 00784c5c ["COPY", "tmp:0:8", ["const:c10:8"]]
- 00784c5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00784c5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00784c5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00784c9c ["COPY", "tmp:0:8", ["const:10:8"]]
+ 00784c9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00784c9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00784c9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00784c5c bytes 08413091
+ 00784c9c bytes 08410091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77e627fd5eeb34b0e74a021fa2967e04"></a>

### [`007850ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/007850ec.md) → [`0078512c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00785/0078512c.md) FUN_0078512c

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
      "definition_site": "00785150",
      "incomplete_value": false,
      "site": "00785150",
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
            "const:90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00785110",
      "incomplete_value": false,
      "site": "00785110",
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
            "const:c90:8"
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
      "00785150",
      "DATA",
      [
        "storage",
        "00c78c90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00785150",
      "DATA",
      [
        "storage",
        "00c79090",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00785100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/007850ec.md#insn-00785100) · [`00785108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/007850ec.md#insn-00785108) · [`0078510c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/007850ec.md#insn-0078510c)
- 新版 `00785140`（命令位置の公開資料なし） · `00785148`（命令位置の公開資料なし） · `0078514c`（命令位置の公開資料なし）

~~~diff
- 00785100 ["INT_ADD", "register:40f0:8", ["const:785100:8", "const:4:8"]]
- 00785100 ["CALL", null, ["callee:00c57e90:8"]]
+ 00785140 ["INT_ADD", "register:40f0:8", ["const:785140:8", "const:4:8"]]
+ 00785140 ["CALL", null, ["callee:00c57e90:8"]]
- 00785100 bytes 644a1394
+ 00785140 bytes 544b1394
- 00785108 ["COPY", "register:4040:8", ["const:c78000:8"]]
+ 00785148 ["COPY", "register:4040:8", ["const:c79000:8"]]
- 00785108 bytes 882700f0
+ 00785148 bytes a8270090
- 0078510c ["COPY", "tmp:0:8", ["const:c90:8"]]
- 0078510c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0078510c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0078510c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0078514c ["COPY", "tmp:0:8", ["const:90:8"]]
+ 0078514c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0078514c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0078514c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0078510c bytes 08413291
+ 0078514c bytes 08410291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb088deacfa5af9352bffd8fffff96d0"></a>

### [`00785120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/00785120.md) → [`00785160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00785/00785160.md) FUN_00785160

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
      "definition_site": "0078516c",
      "incomplete_value": false,
      "site": "0078516c",
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
            "const:90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078512c",
      "incomplete_value": false,
      "site": "0078512c",
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
            "const:c90:8"
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
      "0078516c",
      "DATA",
      [
        "storage",
        "00c78c90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0078516c",
      "DATA",
      [
        "storage",
        "00c79090",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00785124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/00785120.md#insn-00785124) · [`00785128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/00785120.md#insn-00785128)
- 新版 `00785164`（命令位置の公開資料なし） · `00785168`（命令位置の公開資料なし）

~~~diff
- 00785124 ["COPY", "register:4048:8", ["const:c78000:8"]]
+ 00785164 ["COPY", "register:4048:8", ["const:c79000:8"]]
- 00785124 bytes 892700f0
+ 00785164 bytes a9270090
- 00785128 ["COPY", "tmp:0:8", ["const:c90:8"]]
- 00785128 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00785128 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00785128 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00785168 ["COPY", "tmp:0:8", ["const:90:8"]]
+ 00785168 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00785168 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00785168 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00785128 bytes 29413291
+ 00785168 bytes 29410291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07e5a7af26c48551b4ebc40de95d1647"></a>

### [`0078520c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/0078520c.md) → [`0078524c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00785/0078524c.md) FUN_0078524c

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
      "definition_site": "00785260",
      "incomplete_value": false,
      "site": "00785264",
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
            "const:120:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00785220",
      "incomplete_value": false,
      "site": "00785224",
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
            "const:d20:8"
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
      "00785264",
      "DATA",
      [
        "storage",
        "00c78d20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00785264",
      "DATA",
      [
        "storage",
        "00c79120",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00785218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/0078520c.md#insn-00785218) · [`0078521c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/0078520c.md#insn-0078521c) · [`00785220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/0078520c.md#insn-00785220)
- 新版 `00785258`（命令位置の公開資料なし） · `0078525c`（命令位置の公開資料なし） · `00785260`（命令位置の公開資料なし）

~~~diff
- 00785218 ["INT_ADD", "register:40f0:8", ["const:785218:8", "const:4:8"]]
- 00785218 ["CALL", null, ["callee:00c57e90:8"]]
+ 00785258 ["INT_ADD", "register:40f0:8", ["const:785258:8", "const:4:8"]]
+ 00785258 ["CALL", null, ["callee:00c57e90:8"]]
- 00785218 bytes 1e4a1394
+ 00785258 bytes 0e4b1394
- 0078521c ["COPY", "register:4040:8", ["const:c78000:8"]]
+ 0078525c ["COPY", "register:4040:8", ["const:c79000:8"]]
- 0078521c bytes 882700f0
+ 0078525c bytes a8270090
- 00785220 ["COPY", "tmp:0:8", ["const:d20:8"]]
- 00785220 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00785220 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00785220 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00785260 ["COPY", "tmp:0:8", ["const:120:8"]]
+ 00785260 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00785260 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00785260 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00785220 bytes 08813491
+ 00785260 bytes 08810491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99a5bfe3aea73f8a11124c8dafe4a300"></a>

### [`00785248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/00785248.md) → [`00785288`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00785/00785288.md) FUN_00785288

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`0046aecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046aecc.md) [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md) [`0071be98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071be98.md) [`008b924c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b924c.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`0046af0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046af0c.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md) [`0071bed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071b/0071bed8.md) [`008b9290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9290.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.46% / 新版 97.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "007852d0",
      "incomplete_value": true,
      "site": "007852d0",
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
      "definition_site": "00785290",
      "incomplete_value": true,
      "site": "00785290",
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007852d8",
      "incomplete_value": false,
      "site": "007852e8",
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
    "old": {
      "definition_site": "00785298",
      "incomplete_value": false,
      "site": "007852a8",
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
            "const:a58:8"
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
      "definition_site": "007852e0",
      "incomplete_value": false,
      "site": "007852e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:a08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007852a0",
      "incomplete_value": false,
      "site": "007852a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c77000:8"
          ],
          [
            "leaf",
            "const:608:8"
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
      "007852cc",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "007852d8",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007852e0",
      "PARAM",
      [
        "storage",
        "00c77608",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "007852cc",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "007852d8",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007852e0",
      "PARAM",
      [
        "storage",
        "00c77a08",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007852a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/00785248.md#insn-007852a8) · [`007853b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/00785248.md#insn-007853b4) · [`00785280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00785/00785248.md#insn-00785280)
- 新版 `007852e8`（命令位置の公開資料なし） · `007853f4`（命令位置の公開資料なし） · `007852c0`（命令位置の公開資料なし）

~~~diff
- 007852a8 ["INT_ADD", "register:40f0:8", ["const:7852a8:8", "const:4:8"]]
- 007852a8 ["CALL", null, ["callee:00c58610:8"]]
+ 007852e8 ["INT_ADD", "register:40f0:8", ["const:7852e8:8", "const:4:8"]]
+ 007852e8 ["CALL", null, ["callee:00c58610:8"]]
- 007852a8 bytes da4b1394
+ 007852e8 bytes ca4c1394
- 007853b4 ["INT_ADD", "register:40f0:8", ["const:7853b4:8", "const:4:8"]]
- 007853b4 ["CALL", null, ["ram:71be98:8"]]
+ 007853f4 ["INT_ADD", "register:40f0:8", ["const:7853f4:8", "const:4:8"]]
+ 007853f4 ["CALL", null, ["ram:71bed8:8"]]
- 007853b4 bytes b95afe97
+ 007853f4 bytes b95afe97
- 00785280 ["INT_ADD", "register:40f0:8", ["const:785280:8", "const:4:8"]]
- 00785280 ["CALL", null, ["callee:008b9290:8"]]
+ 007852c0 ["INT_ADD", "register:40f0:8", ["const:7852c0:8", "const:4:8"]]
+ 007852c0 ["CALL", null, ["callee:008b9290:8"]]
- 00785280 bytes f3cf0494
+ 007852c0 bytes f4cf0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

