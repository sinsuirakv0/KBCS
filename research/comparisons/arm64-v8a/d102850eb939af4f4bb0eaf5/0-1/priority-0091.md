# v16.0.1 → v16.0.2 · 最優先の変更候補 (91)

[一覧の目次](README.md)

<a id="compare-8d247a31cc1308b399312b9fe7df9a0b"></a>

### [`00c4eb18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4eb18.md) → [`00c4ebb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ebb4.md) FUN_00c4ebb4

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 3件 [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 3件 [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4ec20",
      "incomplete_value": false,
      "site": "00c4ec20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:710:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4eb84",
      "incomplete_value": false,
      "site": "00c4eb84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:640:8"
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
      "00c4ec20",
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4ec20",
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4eb4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4eb18.md#insn-00c4eb4c) · [`00c4eb74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4eb18.md#insn-00c4eb74) · [`00c4eb7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4eb18.md#insn-00c4eb7c)
- 新版 [`00c4ebe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ebb4.md#insn-00c4ebe8) · [`00c4ec10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ebb4.md#insn-00c4ec10) · [`00c4ec18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ebb4.md#insn-00c4ec18)

~~~diff
- 00c4eb4c ["INT_ADD", "register:40f0:8", ["const:c4eb4c:8", "const:4:8"]]
- 00c4eb4c ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c4ebe8 ["INT_ADD", "register:40f0:8", ["const:c4ebe8:8", "const:4:8"]]
+ 00c4ebe8 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c4eb4c bytes 352d0094
+ 00c4ebe8 bytes 422d0094
- 00c4eb74 ["INT_ADD", "register:40f0:8", ["const:c4eb74:8", "const:4:8"]]
- 00c4eb74 ["CALL", null, ["callee:00c580b0:8"]]
+ 00c4ec10 ["INT_ADD", "register:40f0:8", ["const:c4ec10:8", "const:4:8"]]
+ 00c4ec10 ["CALL", null, ["callee:00c580b0:8"]]
- 00c4eb74 bytes 1b250094
+ 00c4ec10 bytes 28250094
- 00c4eb7c ["COPY", "tmp:0:8", ["const:640:8"]]
- 00c4eb7c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c4eb7c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c4eb7c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c4ec18 ["COPY", "tmp:0:8", ["const:710:8"]]
+ 00c4ec18 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c4ec18 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c4ec18 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c4eb7c bytes 29011991
+ 00c4ec18 bytes 29411c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef1e89dd90826f3ee5d51cc63bd2075c"></a>

### [`00c4ebc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ebc4.md) → [`00c4ec60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ec60.md) FUN_00c4ec60

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4ecc8",
      "incomplete_value": false,
      "site": "00c4ecc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4ec2c",
      "incomplete_value": false,
      "site": "00c4ec2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:af0:8"
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
      "00c4ecc8",
      "DATA",
      [
        "storage",
        "00c99af0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4ecc8",
      "DATA",
      [
        "storage",
        "00c99bc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4ebfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ebc4.md#insn-00c4ebfc) · [`00c4ec20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ebc4.md#insn-00c4ec20) · [`00c4ec6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ebc4.md#insn-00c4ec6c)
- 新版 [`00c4ec98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ec60.md#insn-00c4ec98) · [`00c4ecbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ec60.md#insn-00c4ecbc) · [`00c4ed08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ec60.md#insn-00c4ed08)

~~~diff
- 00c4ebfc ["INT_ADD", "register:40f0:8", ["const:c4ebfc:8", "const:4:8"]]
- 00c4ebfc ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c4ec98 ["INT_ADD", "register:40f0:8", ["const:c4ec98:8", "const:4:8"]]
+ 00c4ec98 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c4ebfc bytes 092d0094
+ 00c4ec98 bytes 162d0094
- 00c4ec20 ["COPY", "tmp:0:8", ["const:af0:8"]]
- 00c4ec20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c4ec20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c4ec20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c4ecbc ["COPY", "tmp:0:8", ["const:bc0:8"]]
+ 00c4ecbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4ecbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4ecbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c4ec20 bytes 08c12b91
+ 00c4ecbc bytes 08012f91
- 00c4ec6c ["INT_ADD", "register:40f0:8", ["const:c4ec6c:8", "const:4:8"]]
- 00c4ec6c ["CALL", null, ["callee:00c580f0:8"]]
+ 00c4ed08 ["INT_ADD", "register:40f0:8", ["const:c4ed08:8", "const:4:8"]]
+ 00c4ed08 ["CALL", null, ["callee:00c580f0:8"]]
- 00c4ec6c bytes ed240094
+ 00c4ed08 bytes fa240094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4b8babe74779ef706c8577b902b76c0"></a>

### [`00c4ec70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ec70.md) → [`00c4ed0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ed0c.md) FUN_00c4ed0c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4ed70",
      "incomplete_value": false,
      "site": "00c4ed70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:c30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4ecd4",
      "incomplete_value": false,
      "site": "00c4ecd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:b60:8"
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
      "00c4ed70",
      "DATA",
      [
        "storage",
        "00c99b60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4ed70",
      "DATA",
      [
        "storage",
        "00c99c30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4eca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ec70.md#insn-00c4eca4) · [`00c4ecc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ec70.md#insn-00c4ecc8) · [`00c4ed0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ec70.md#insn-00c4ed0c)
- 新版 [`00c4ed40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ed0c.md#insn-00c4ed40) · [`00c4ed64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ed0c.md#insn-00c4ed64) · [`00c4eda8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ed0c.md#insn-00c4eda8)

~~~diff
- 00c4eca4 ["INT_ADD", "register:40f0:8", ["const:c4eca4:8", "const:4:8"]]
- 00c4eca4 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c4ed40 ["INT_ADD", "register:40f0:8", ["const:c4ed40:8", "const:4:8"]]
+ 00c4ed40 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c4eca4 bytes df2c0094
+ 00c4ed40 bytes ec2c0094
- 00c4ecc8 ["COPY", "tmp:0:8", ["const:b60:8"]]
- 00c4ecc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c4ecc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c4ecc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c4ed64 ["COPY", "tmp:0:8", ["const:c30:8"]]
+ 00c4ed64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4ed64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4ed64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c4ecc8 bytes 08812d91
+ 00c4ed64 bytes 08c13091
- 00c4ed0c ["INT_ADD", "register:40f0:8", ["const:c4ed0c:8", "const:4:8"]]
- 00c4ed0c ["CALL", null, ["callee:00c580f0:8"]]
+ 00c4eda8 ["INT_ADD", "register:40f0:8", ["const:c4eda8:8", "const:4:8"]]
+ 00c4eda8 ["CALL", null, ["callee:00c580f0:8"]]
- 00c4ed0c bytes c5240094
+ 00c4eda8 bytes d2240094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afb0a798488afdc7e71e777f2c4570d5"></a>

### [`00c4ed10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ed10.md) → [`00c4edac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4edac.md) FUN_00c4edac

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4ee14",
      "incomplete_value": false,
      "site": "00c4ee14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4ed78",
      "incomplete_value": false,
      "site": "00c4ed78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:bd0:8"
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
      "00c4ee14",
      "DATA",
      [
        "storage",
        "00c99bd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4ee14",
      "DATA",
      [
        "storage",
        "00c99ca0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4ed48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ed10.md#insn-00c4ed48) · [`00c4ed6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ed10.md#insn-00c4ed6c) · [`00c4edb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ed10.md#insn-00c4edb8)
- 新版 [`00c4ede4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4edac.md#insn-00c4ede4) · [`00c4ee08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4edac.md#insn-00c4ee08) · [`00c4ee54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4edac.md#insn-00c4ee54)

~~~diff
- 00c4ed48 ["INT_ADD", "register:40f0:8", ["const:c4ed48:8", "const:4:8"]]
- 00c4ed48 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c4ede4 ["INT_ADD", "register:40f0:8", ["const:c4ede4:8", "const:4:8"]]
+ 00c4ede4 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c4ed48 bytes b62c0094
+ 00c4ede4 bytes c32c0094
- 00c4ed6c ["COPY", "tmp:0:8", ["const:bd0:8"]]
- 00c4ed6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c4ed6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c4ed6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c4ee08 ["COPY", "tmp:0:8", ["const:ca0:8"]]
+ 00c4ee08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4ee08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4ee08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c4ed6c bytes 08412f91
+ 00c4ee08 bytes 08813291
- 00c4edb8 ["INT_ADD", "register:40f0:8", ["const:c4edb8:8", "const:4:8"]]
- 00c4edb8 ["CALL", null, ["callee:00c580f0:8"]]
+ 00c4ee54 ["INT_ADD", "register:40f0:8", ["const:c4ee54:8", "const:4:8"]]
+ 00c4ee54 ["CALL", null, ["callee:00c580f0:8"]]
- 00c4edb8 bytes 9a240094
+ 00c4ee54 bytes a7240094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-593535b9d2b6996e1b563349f13817af"></a>

### [`00c4edbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4edbc.md) → [`00c4ee58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ee58.md) FUN_00c4ee58

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4eec0",
      "incomplete_value": false,
      "site": "00c4eec0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:d10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4ee24",
      "incomplete_value": false,
      "site": "00c4ee24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:c40:8"
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
      "00c4eec0",
      "DATA",
      [
        "storage",
        "00c99c40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4eec0",
      "DATA",
      [
        "storage",
        "00c99d10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4edf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4edbc.md#insn-00c4edf4) · [`00c4ee18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4edbc.md#insn-00c4ee18) · [`00c4ee64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4edbc.md#insn-00c4ee64)
- 新版 [`00c4ee90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ee58.md#insn-00c4ee90) · [`00c4eeb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ee58.md#insn-00c4eeb4) · [`00c4ef00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ee58.md#insn-00c4ef00)

~~~diff
- 00c4edf4 ["INT_ADD", "register:40f0:8", ["const:c4edf4:8", "const:4:8"]]
- 00c4edf4 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c4ee90 ["INT_ADD", "register:40f0:8", ["const:c4ee90:8", "const:4:8"]]
+ 00c4ee90 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c4edf4 bytes 8b2c0094
+ 00c4ee90 bytes 982c0094
- 00c4ee18 ["COPY", "tmp:0:8", ["const:c40:8"]]
- 00c4ee18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c4ee18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c4ee18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c4eeb4 ["COPY", "tmp:0:8", ["const:d10:8"]]
+ 00c4eeb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4eeb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4eeb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c4ee18 bytes 08013191
+ 00c4eeb4 bytes 08413491
- 00c4ee64 ["INT_ADD", "register:40f0:8", ["const:c4ee64:8", "const:4:8"]]
- 00c4ee64 ["CALL", null, ["callee:00c580f0:8"]]
+ 00c4ef00 ["INT_ADD", "register:40f0:8", ["const:c4ef00:8", "const:4:8"]]
+ 00c4ef00 ["CALL", null, ["callee:00c580f0:8"]]
- 00c4ee64 bytes 6f240094
+ 00c4ef00 bytes 7c240094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5e7f7d3d72763266989923119324f6b"></a>

### [`00c4ee68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ee68.md) → [`00c4ef04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ef04.md) FUN_00c4ef04

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 6件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3fd7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) [`00c50830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50830.md) [`00c508d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c508d0.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md)
- 新版 呼出元 1件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 6件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3fe18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c508cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c508cc.md) [`00c5096c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c5096c.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.57% / 新版 96.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4f000",
      "incomplete_value": false,
      "site": "00c4f000",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:710:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4ef64",
      "incomplete_value": false,
      "site": "00c4ef64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:640:8"
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
      "definition_site": "00c4f0dc",
      "incomplete_value": false,
      "site": "00c4f0dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4f040",
      "incomplete_value": false,
      "site": "00c4f040",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:d20:8"
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
      "definition_site": "00c4f178",
      "incomplete_value": false,
      "site": "00c4f178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4f0dc",
      "incomplete_value": false,
      "site": "00c4f0dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:d20:8"
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
      "00c4f000",
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4f0dc",
      "DATA",
      [
        "storage",
        "00c99d20",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4f178",
      "DATA",
      [
        "storage",
        "00c99d20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4f000",
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4f0dc",
      "DATA",
      [
        "storage",
        "00c99df0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4f178",
      "DATA",
      [
        "storage",
        "00c99df0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4ef2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ee68.md#insn-00c4ef2c) · [`00c4ef60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ee68.md#insn-00c4ef60) · [`00c4efd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ee68.md#insn-00c4efd0)
- 新版 [`00c4efc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ef04.md#insn-00c4efc8) · [`00c4effc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ef04.md#insn-00c4effc) · [`00c4f06c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ef04.md#insn-00c4f06c)

~~~diff
- 00c4ef2c ["INT_ADD", "register:40f0:8", ["const:c4ef2c:8", "const:4:8"]]
- 00c4ef2c ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c4efc8 ["INT_ADD", "register:40f0:8", ["const:c4efc8:8", "const:4:8"]]
+ 00c4efc8 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c4ef2c bytes 3d2c0094
+ 00c4efc8 bytes 4a2c0094
- 00c4ef60 ["COPY", "tmp:0:8", ["const:640:8"]]
- 00c4ef60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c4ef60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c4ef60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c4effc ["COPY", "tmp:0:8", ["const:710:8"]]
+ 00c4effc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4effc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4effc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c4ef60 bytes 08011991
+ 00c4effc bytes 08411c91
- 00c4efd0 ["INT_ADD", "register:40f0:8", ["const:c4efd0:8", "const:4:8"]]
- 00c4efd0 ["CALL", null, ["callee:00c508cc:8"]]
+ 00c4f06c ["INT_ADD", "register:40f0:8", ["const:c4f06c:8", "const:4:8"]]
+ 00c4f06c ["CALL", null, ["callee:00c508cc:8"]]
- 00c4efd0 bytes 18060094
+ 00c4f06c bytes 18060094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2eff3ac2a6c4eee12c3c60756b93b66c"></a>

### [`00c4f124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f124.md) → [`00c4f1c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f1c0.md) FUN_00c4f1c0

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 3件 [`00c3c20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 3件 [`00c3c2a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.05% / 新版 94.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4f2cc",
      "incomplete_value": false,
      "site": "00c4f2cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:f40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4f230",
      "incomplete_value": false,
      "site": "00c4f230",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:e70:8"
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
      "00c4f2cc",
      "DATA",
      [
        "storage",
        "00c99e70",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4f2ec",
      "DATA",
      [
        "storage",
        "002b364c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c4f2cc",
      "DATA",
      [
        "storage",
        "00c99f40",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4f2ec",
      "DATA",
      [
        "storage",
        "002b367d",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4f19c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f124.md#insn-00c4f19c) · [`00c4f1ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f124.md#insn-00c4f1ac) · [`00c4f1bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f124.md#insn-00c4f1bc)
- 新版 [`00c4f238`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f1c0.md#insn-00c4f238) · [`00c4f248`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f1c0.md#insn-00c4f248) · [`00c4f258`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f1c0.md#insn-00c4f258)

~~~diff
- 00c4f19c ["COPY", "tmp:0:8", ["const:64c:8"]]
- 00c4f19c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00c4f19c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00c4f19c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00c4f238 ["COPY", "tmp:0:8", ["const:67d:8"]]
+ 00c4f238 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00c4f238 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00c4f238 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00c4f19c bytes 73321991
+ 00c4f238 bytes 73f61991
- 00c4f1ac ["COPY", "tmp:0:8", ["const:c1e:8"]]
- 00c4f1ac ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00c4f1ac ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00c4f1ac ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00c4f248 ["COPY", "tmp:0:8", ["const:c5e:8"]]
+ 00c4f248 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00c4f248 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00c4f248 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00c4f1ac bytes 737a3091
+ 00c4f248 bytes 737a3191
- 00c4f1bc ["COPY", "tmp:0:8", ["const:847:8"]]
- 00c4f1bc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00c4f1bc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00c4f1bc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00c4f258 ["COPY", "tmp:0:8", ["const:7eb:8"]]
+ 00c4f258 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00c4f258 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00c4f258 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00c4f1bc bytes 731e2191
+ 00c4f258 bytes 73ae1f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf18a36e4144eff45ad5848979618fc4"></a>

### [`00c4f274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f274.md) → [`00c4f310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f310.md) FUN_00c4f310

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4f378",
      "incomplete_value": false,
      "site": "00c4f378",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:fb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4f2dc",
      "incomplete_value": false,
      "site": "00c4f2dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
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
      "00c4f378",
      "DATA",
      [
        "storage",
        "00c99ee0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4f378",
      "DATA",
      [
        "storage",
        "00c99fb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4f2a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f274.md#insn-00c4f2a8) · [`00c4f2d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f274.md#insn-00c4f2d4) · [`00c4f31c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f274.md#insn-00c4f31c)
- 新版 [`00c4f344`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f310.md#insn-00c4f344) · [`00c4f370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f310.md#insn-00c4f370) · [`00c4f3b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f310.md#insn-00c4f3b8)

~~~diff
- 00c4f2a8 ["INT_ADD", "register:40f0:8", ["const:c4f2a8:8", "const:4:8"]]
- 00c4f2a8 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c4f344 ["INT_ADD", "register:40f0:8", ["const:c4f344:8", "const:4:8"]]
+ 00c4f344 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c4f2a8 bytes 5e2b0094
+ 00c4f344 bytes 6b2b0094
- 00c4f2d4 ["COPY", "tmp:0:8", ["const:ee0:8"]]
- 00c4f2d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c4f2d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c4f2d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c4f370 ["COPY", "tmp:0:8", ["const:fb0:8"]]
+ 00c4f370 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4f370 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4f370 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c4f2d4 bytes 08813b91
+ 00c4f370 bytes 08c13e91
- 00c4f31c ["INT_ADD", "register:40f0:8", ["const:c4f31c:8", "const:4:8"]]
- 00c4f31c ["CALL", null, ["callee:00c580f0:8"]]
+ 00c4f3b8 ["INT_ADD", "register:40f0:8", ["const:c4f3b8:8", "const:4:8"]]
+ 00c4f3b8 ["CALL", null, ["callee:00c580f0:8"]]
- 00c4f31c bytes 41230094
+ 00c4f3b8 bytes 4e230094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-515576d3bead6950cc6d0fd1b0bcdf02"></a>

### [`00c4f320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f320.md) → [`00c4f3bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f3bc.md) FUN_00c4f3bc

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.74% / 新版 95.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4f430",
      "incomplete_value": false,
      "site": "00c4f430",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4f394",
      "incomplete_value": false,
      "site": "00c4f394",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:f50:8"
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
      "00c4f430",
      "DATA",
      [
        "storage",
        "00c99f50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4f430",
      "DATA",
      [
        "storage",
        "00c9a020",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4f358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f320.md#insn-00c4f358) · [`00c4f380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f320.md#insn-00c4f380) · [`00c4f384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f320.md#insn-00c4f384)
- 新版 [`00c4f3f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f3bc.md#insn-00c4f3f4) · [`00c4f41c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f3bc.md#insn-00c4f41c) · [`00c4f420`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f3bc.md#insn-00c4f420)

~~~diff
- 00c4f358 ["INT_ADD", "register:40f0:8", ["const:c4f358:8", "const:4:8"]]
- 00c4f358 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c4f3f4 ["INT_ADD", "register:40f0:8", ["const:c4f3f4:8", "const:4:8"]]
+ 00c4f3f4 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c4f358 bytes 322b0094
+ 00c4f3f4 bytes 3f2b0094
- 00c4f380 ["COPY", "register:4050:8", ["const:c99000:8"]]
+ 00c4f41c ["COPY", "register:4050:8", ["const:c9a000:8"]]
- 00c4f380 bytes 4a0200d0
+ 00c4f41c bytes 4a0200f0
- 00c4f384 ["COPY", "tmp:0:8", ["const:f50:8"]]
- 00c4f384 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00c4f384 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00c4f384 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00c4f420 ["COPY", "tmp:0:8", ["const:20:8"]]
+ 00c4f420 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00c4f420 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00c4f420 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00c4f384 bytes 4a413d91
+ 00c4f420 bytes 4a810091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb484457befa7ec62798478993ca49ee"></a>

### [`00c4f3dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f3dc.md) → [`00c4f478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f478.md) FUN_00c4f478

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4f4dc",
      "incomplete_value": false,
      "site": "00c4f4dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:d10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4f440",
      "incomplete_value": false,
      "site": "00c4f440",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:c40:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4f4fc",
      "incomplete_value": false,
      "site": "00c4f4fc",
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
            "const:50f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4f460",
      "incomplete_value": false,
      "site": "00c4f460",
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
            "const:56b:8"
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
      "00c4f4dc",
      "DATA",
      [
        "storage",
        "00c99c40",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4f4fc",
      "DATA",
      [
        "storage",
        "002a756b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4f4dc",
      "DATA",
      [
        "storage",
        "00c99d10",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4f4fc",
      "DATA",
      [
        "storage",
        "002a750f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4f410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f3dc.md#insn-00c4f410) · [`00c4f434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f3dc.md#insn-00c4f434) · [`00c4f458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f3dc.md#insn-00c4f458)
- 新版 [`00c4f4ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f478.md#insn-00c4f4ac) · [`00c4f4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f478.md#insn-00c4f4d0) · [`00c4f4f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f478.md#insn-00c4f4f4)

~~~diff
- 00c4f410 ["INT_ADD", "register:40f0:8", ["const:c4f410:8", "const:4:8"]]
- 00c4f410 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c4f4ac ["INT_ADD", "register:40f0:8", ["const:c4f4ac:8", "const:4:8"]]
+ 00c4f4ac ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c4f410 bytes 042b0094
+ 00c4f4ac bytes 112b0094
- 00c4f434 ["COPY", "tmp:0:8", ["const:c40:8"]]
- 00c4f434 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c4f434 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c4f434 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c4f4d0 ["COPY", "tmp:0:8", ["const:d10:8"]]
+ 00c4f4d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4f4d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4f4d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c4f434 bytes 08013191
+ 00c4f4d0 bytes 08413491
- 00c4f458 ["COPY", "tmp:0:8", ["const:56b:8"]]
- 00c4f458 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c4f458 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c4f458 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c4f4f4 ["COPY", "tmp:0:8", ["const:50f:8"]]
+ 00c4f4f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c4f4f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c4f4f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c4f458 bytes 29ad1591
+ 00c4f4f4 bytes 293d1491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcfb9fd3fefefea619f310529bd61a26"></a>

### [`00c4f48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f48c.md) → [`00c4f528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f528.md) FUN_00c4f528

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4f58c",
      "incomplete_value": false,
      "site": "00c4f58c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:d10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4f4f0",
      "incomplete_value": false,
      "site": "00c4f4f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:c40:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4f5ac",
      "incomplete_value": false,
      "site": "00c4f5ac",
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
            "const:eb9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4f510",
      "incomplete_value": false,
      "site": "00c4f510",
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
            "const:f06:8"
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
      "00c4f58c",
      "DATA",
      [
        "storage",
        "00c99c40",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4f5ac",
      "DATA",
      [
        "storage",
        "002a0f06",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4f58c",
      "DATA",
      [
        "storage",
        "00c99d10",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4f5ac",
      "DATA",
      [
        "storage",
        "002a0eb9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4f4c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f48c.md#insn-00c4f4c0) · [`00c4f4e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f48c.md#insn-00c4f4e4) · [`00c4f508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f48c.md#insn-00c4f508)
- 新版 [`00c4f55c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f528.md#insn-00c4f55c) · [`00c4f580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f528.md#insn-00c4f580) · [`00c4f5a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f528.md#insn-00c4f5a4)

~~~diff
- 00c4f4c0 ["INT_ADD", "register:40f0:8", ["const:c4f4c0:8", "const:4:8"]]
- 00c4f4c0 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c4f55c ["INT_ADD", "register:40f0:8", ["const:c4f55c:8", "const:4:8"]]
+ 00c4f55c ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c4f4c0 bytes d82a0094
+ 00c4f55c bytes e52a0094
- 00c4f4e4 ["COPY", "tmp:0:8", ["const:c40:8"]]
- 00c4f4e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c4f4e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c4f4e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c4f580 ["COPY", "tmp:0:8", ["const:d10:8"]]
+ 00c4f580 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4f580 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4f580 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c4f4e4 bytes 08013191
+ 00c4f580 bytes 08413491
- 00c4f508 ["COPY", "tmp:0:8", ["const:f06:8"]]
- 00c4f508 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c4f508 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c4f508 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c4f5a4 ["COPY", "tmp:0:8", ["const:eb9:8"]]
+ 00c4f5a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c4f5a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c4f5a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c4f508 bytes 29193c91
+ 00c4f5a4 bytes 29e53a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df03319e4fa707d864276ad5dbdd7988"></a>

### [`00c4f9a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f9a0.md) → [`00c4fa3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4fa3c.md) FUN_00c4fa3c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c45144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45144.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c451e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c451e0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.38% / 新版 97.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4fbcc",
      "incomplete_value": true,
      "site": "00c4fbd8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:659:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4fb30",
      "incomplete_value": true,
      "site": "00c4fb3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6ad:8"
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
      "definition_site": "00c4fc34",
      "incomplete_value": true,
      "site": "00c4fc40",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:aaf:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4fb98",
      "incomplete_value": true,
      "site": "00c4fba4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b03:8"
              ]
            ]
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
      "00c4fbcc",
      "READ",
      [
        "storage",
        "002bd6ad",
        null,
        "string"
      ]
    ],
    [
      "00c4fc34",
      "READ",
      [
        "storage",
        "002beb03",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4fbcc",
      "READ",
      [
        "storage",
        "002bd659",
        null,
        "string"
      ]
    ],
    [
      "00c4fc34",
      "READ",
      [
        "storage",
        "002beaaf",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c4f9ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f9a0.md#insn-00c4f9ec) · [`00c4fa14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f9a0.md#insn-00c4fa14) · [`00c4fa4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f9a0.md#insn-00c4fa4c)
- 新版 [`00c4fa88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4fa3c.md#insn-00c4fa88) · [`00c4fab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4fa3c.md#insn-00c4fab0) · [`00c4fae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4fa3c.md#insn-00c4fae8)

~~~diff
- 00c4f9ec ["INT_ADD", "register:40f0:8", ["const:c4f9ec:8", "const:4:8"]]
- 00c4f9ec ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4fa88 ["INT_ADD", "register:40f0:8", ["const:c4fa88:8", "const:4:8"]]
+ 00c4fa88 ["CALL", null, ["callee:00c5a170:8"]]
- 00c4f9ec bytes ad290094
+ 00c4fa88 bytes ba290094
- 00c4fa14 ["INT_ADD", "register:40f0:8", ["const:c4fa14:8", "const:4:8"]]
- 00c4fa14 ["CALL", null, ["callee:00c451e0:8"]]
+ 00c4fab0 ["INT_ADD", "register:40f0:8", ["const:c4fab0:8", "const:4:8"]]
+ 00c4fab0 ["CALL", null, ["callee:00c451e0:8"]]
- 00c4fa14 bytes ccd5ff97
+ 00c4fab0 bytes ccd5ff97
- 00c4fa4c ["INT_ADD", "register:40f0:8", ["const:c4fa4c:8", "const:4:8"]]
- 00c4fa4c ["CALL", null, ["callee:00c5a170:8"]]
+ 00c4fae8 ["INT_ADD", "register:40f0:8", ["const:c4fae8:8", "const:4:8"]]
+ 00c4fae8 ["CALL", null, ["callee:00c5a170:8"]]
- 00c4fa4c bytes 95290094
+ 00c4fae8 bytes a2290094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cfc36bf523ef456c588f05852e218cca"></a>

### [`00c500b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c500b4.md) → [`00c50150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50150.md) FUN_00c50150

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c50228",
      "incomplete_value": true,
      "site": "00c50234",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:659:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c5018c",
      "incomplete_value": true,
      "site": "00c50198",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6ad:8"
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
      "definition_site": "00c50290",
      "incomplete_value": true,
      "site": "00c5029c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:aaf:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c501f4",
      "incomplete_value": true,
      "site": "00c50200",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b03:8"
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
      "00c50228",
      "READ",
      [
        "storage",
        "002bd6ad",
        null,
        "string"
      ]
    ],
    [
      "00c50290",
      "READ",
      [
        "storage",
        "002beb03",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c50228",
      "READ",
      [
        "storage",
        "002bd659",
        null,
        "string"
      ]
    ],
    [
      "00c50290",
      "READ",
      [
        "storage",
        "002beaaf",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c500d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c500b4.md#insn-00c500d8) · [`00c5010c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c500b4.md#insn-00c5010c) · [`00c50170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c500b4.md#insn-00c50170)
- 新版 [`00c50174`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50150.md#insn-00c50174) · [`00c501a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50150.md#insn-00c501a8) · [`00c5020c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50150.md#insn-00c5020c)

~~~diff
- 00c500d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c500d8 ["INT_ADD", "register:40f0:8", ["const:c500d8:8", "const:4:8"]]
- 00c500d8 ["CALLIND", null, ["register:0:8"]]
+ 00c50174 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c50174 ["INT_ADD", "register:40f0:8", ["const:c50174:8", "const:4:8"]]
+ 00c50174 ["CALLIND", null, ["register:0:8"]]
- 00c500d8 bytes 00013fd6
+ 00c50174 bytes 00013fd6
- 00c5010c ["INT_ADD", "register:40f0:8", ["const:c5010c:8", "const:4:8"]]
- 00c5010c ["CALL", null, ["callee:00c5a170:8"]]
+ 00c501a8 ["INT_ADD", "register:40f0:8", ["const:c501a8:8", "const:4:8"]]
+ 00c501a8 ["CALL", null, ["callee:00c5a170:8"]]
- 00c5010c bytes e5270094
+ 00c501a8 bytes f2270094
- 00c50170 ["INT_ADD", "register:40f0:8", ["const:c50170:8", "const:4:8"]]
- 00c50170 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c5020c ["INT_ADD", "register:40f0:8", ["const:c5020c:8", "const:4:8"]]
+ 00c5020c ["CALL", null, ["callee:00c5a170:8"]]
- 00c50170 bytes cc270094
+ 00c5020c bytes d9270094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6edb62532c268d559178de9628587591"></a>

### [`00c5049c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c5049c.md) → [`00c50538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50538.md) FUN_00c50538

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.37% / 新版 98.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c505a0",
      "incomplete_value": true,
      "site": "00c505ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:518:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c50504",
      "incomplete_value": true,
      "site": "00c50510",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:574:8"
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
      "00c505a0",
      "READ",
      [
        "storage",
        "002a7574",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c505a0",
      "READ",
      [
        "storage",
        "002a7518",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c504e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c5049c.md#insn-00c504e8) · [`00c504fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c5049c.md#insn-00c504fc) · [`00c50548`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c5049c.md#insn-00c50548)
- 新版 [`00c50584`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50538.md#insn-00c50584) · [`00c50598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50538.md#insn-00c50598) · [`00c505e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50538.md#insn-00c505e4)

~~~diff
- 00c504e8 ["INT_ADD", "register:40f0:8", ["const:c504e8:8", "const:4:8"]]
- 00c504e8 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c50584 ["INT_ADD", "register:40f0:8", ["const:c50584:8", "const:4:8"]]
+ 00c50584 ["CALL", null, ["callee:00c5a170:8"]]
- 00c504e8 bytes ee260094
+ 00c50584 bytes fb260094
- 00c504fc ["COPY", "tmp:0:8", ["const:574:8"]]
- 00c504fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c504fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c504fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c50598 ["COPY", "tmp:0:8", ["const:518:8"]]
+ 00c50598 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c50598 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c50598 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c504fc bytes 29d11591
+ 00c50598 bytes 29611491
- 00c50548 ["INT_ADD", "register:40f0:8", ["const:c50548:8", "const:4:8"]]
- 00c50548 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c505e4 ["INT_ADD", "register:40f0:8", ["const:c505e4:8", "const:4:8"]]
+ 00c505e4 ["CALL", null, ["callee:00c5a170:8"]]
- 00c50548 bytes d6260094
+ 00c505e4 bytes e3260094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05571abb0d539e6daead83191c89f400"></a>

### [`00c50830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50830.md) → [`00c508cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c508cc.md) FUN_00c508cc

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c4ee68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ee68.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c4ef04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ef04.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c50930",
      "incomplete_value": false,
      "site": "00c50930",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:d80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c50894",
      "incomplete_value": false,
      "site": "00c50894",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:cb0:8"
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
      "00c50930",
      "DATA",
      [
        "storage",
        "00c99cb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c50930",
      "DATA",
      [
        "storage",
        "00c99d80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c50864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50830.md#insn-00c50864) · [`00c50888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50830.md#insn-00c50888) · [`00c508cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50830.md#insn-00c508cc)
- 新版 [`00c50900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c508cc.md#insn-00c50900) · [`00c50924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c508cc.md#insn-00c50924) · [`00c50968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c508cc.md#insn-00c50968)

~~~diff
- 00c50864 ["INT_ADD", "register:40f0:8", ["const:c50864:8", "const:4:8"]]
- 00c50864 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c50900 ["INT_ADD", "register:40f0:8", ["const:c50900:8", "const:4:8"]]
+ 00c50900 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c50864 bytes ef250094
+ 00c50900 bytes fc250094
- 00c50888 ["COPY", "tmp:0:8", ["const:cb0:8"]]
- 00c50888 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c50888 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c50888 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c50924 ["COPY", "tmp:0:8", ["const:d80:8"]]
+ 00c50924 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c50924 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c50924 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c50888 bytes 08c13291
+ 00c50924 bytes 08013691
- 00c508cc ["INT_ADD", "register:40f0:8", ["const:c508cc:8", "const:4:8"]]
- 00c508cc ["CALL", null, ["callee:00c580f0:8"]]
+ 00c50968 ["INT_ADD", "register:40f0:8", ["const:c50968:8", "const:4:8"]]
+ 00c50968 ["CALL", null, ["callee:00c580f0:8"]]
- 00c508cc bytes d51d0094
+ 00c50968 bytes e21d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a80dc53eaf35f8d72424e52754ab41f4"></a>

### [`00c508d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c508d0.md) → [`00c5096c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c5096c.md) FUN_00c5096c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c4ee68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ee68.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c4ef04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ef04.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c509d4",
      "incomplete_value": false,
      "site": "00c509d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c50938",
      "incomplete_value": false,
      "site": "00c50938",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:d20:8"
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
      "00c509d4",
      "DATA",
      [
        "storage",
        "00c99d20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c509d4",
      "DATA",
      [
        "storage",
        "00c99df0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c50908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c508d0.md#insn-00c50908) · [`00c5092c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c508d0.md#insn-00c5092c) · [`00c50974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c508d0.md#insn-00c50974)
- 新版 [`00c509a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c5096c.md#insn-00c509a4) · [`00c509c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c5096c.md#insn-00c509c8) · [`00c50a10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c5096c.md#insn-00c50a10)

~~~diff
- 00c50908 ["INT_ADD", "register:40f0:8", ["const:c50908:8", "const:4:8"]]
- 00c50908 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c509a4 ["INT_ADD", "register:40f0:8", ["const:c509a4:8", "const:4:8"]]
+ 00c509a4 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c50908 bytes c6250094
+ 00c509a4 bytes d3250094
- 00c5092c ["COPY", "tmp:0:8", ["const:d20:8"]]
- 00c5092c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c5092c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c5092c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c509c8 ["COPY", "tmp:0:8", ["const:df0:8"]]
+ 00c509c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c509c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c509c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c5092c bytes 08813491
+ 00c509c8 bytes 08c13791
- 00c50974 ["INT_ADD", "register:40f0:8", ["const:c50974:8", "const:4:8"]]
- 00c50974 ["CALL", null, ["callee:00c580f0:8"]]
+ 00c50a10 ["INT_ADD", "register:40f0:8", ["const:c50a10:8", "const:4:8"]]
+ 00c50a10 ["CALL", null, ["callee:00c580f0:8"]]
- 00c50974 bytes ab1d0094
+ 00c50a10 bytes b81d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10fec85c4eb7790c17e2ed7daef617be"></a>

### [`00c50978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50978.md) → [`00c50a14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50a14.md) FUN_00c50a14

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.06% / 新版 93.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c50a78",
      "incomplete_value": true,
      "site": "00c50a84",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b14:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c509dc",
      "incomplete_value": true,
      "site": "00c509e8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bf000:8"
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c50a88",
      "incomplete_value": true,
      "site": "00c50a88",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00c509ec",
      "incomplete_value": true,
      "site": "00c509ec",
      "value": [
        "LOAD",
        "8",
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
      "00c50a78",
      "READ",
      [
        "storage",
        "002bfb68",
        null,
        "string"
      ]
    ],
    [
      "00c50a7c",
      "READ",
      [
        "storage",
        "002bfb6d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c50a78",
      "READ",
      [
        "storage",
        "002bfb14",
        null,
        "string"
      ]
    ],
    [
      "00c50a7c",
      "READ",
      [
        "storage",
        "002bfb19",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c509bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50978.md#insn-00c509bc) · [`00c509d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50978.md#insn-00c509d4) · [`00c50a0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50978.md#insn-00c50a0c)
- 新版 [`00c50a58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50a14.md#insn-00c50a58) · [`00c50a70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50a14.md#insn-00c50a70) · [`00c50aa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50a14.md#insn-00c50aa8)

~~~diff
- 00c509bc ["INT_ADD", "register:40f0:8", ["const:c509bc:8", "const:4:8"]]
- 00c509bc ["CALL", null, ["callee:00c5a170:8"]]
+ 00c50a58 ["INT_ADD", "register:40f0:8", ["const:c50a58:8", "const:4:8"]]
+ 00c50a58 ["CALL", null, ["callee:00c5a170:8"]]
- 00c509bc bytes b9250094
+ 00c50a58 bytes c6250094
- 00c509d4 ["COPY", "tmp:0:8", ["const:b68:8"]]
- 00c509d4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00c509d4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00c509d4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00c50a70 ["COPY", "tmp:0:8", ["const:b14:8"]]
+ 00c50a70 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00c50a70 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00c50a70 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00c509d4 bytes 4aa12d91
+ 00c50a70 bytes 4a512c91
- 00c50a0c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c50a0c ["INT_ADD", "register:40f0:8", ["const:c50a0c:8", "const:4:8"]]
- 00c50a0c ["CALLIND", null, ["register:0:8"]]
+ 00c50aa8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c50aa8 ["INT_ADD", "register:40f0:8", ["const:c50aa8:8", "const:4:8"]]
+ 00c50aa8 ["CALLIND", null, ["register:0:8"]]
- 00c50a0c bytes 00013fd6
+ 00c50aa8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4723284da2cfaf5bc4e13d9fa01e43e2"></a>

### [`00c50bfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50bfc.md) → [`00c50c98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50c98.md) FUN_00c50c98

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.12% / 新版 95.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c50d00",
      "incomplete_value": false,
      "site": "00c50d00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:e60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c50c64",
      "incomplete_value": false,
      "site": "00c50c64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:d90:8"
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
      "00c50d00",
      "DATA",
      [
        "storage",
        "00c99d90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c50d00",
      "DATA",
      [
        "storage",
        "00c99e60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c50c34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50bfc.md#insn-00c50c34) · [`00c50c58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50bfc.md#insn-00c50c58) · [`00c50c9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50bfc.md#insn-00c50c9c)
- 新版 [`00c50cd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50c98.md#insn-00c50cd0) · [`00c50cf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50c98.md#insn-00c50cf4) · [`00c50d38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50c98.md#insn-00c50d38)

~~~diff
- 00c50c34 ["INT_ADD", "register:40f0:8", ["const:c50c34:8", "const:4:8"]]
- 00c50c34 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c50cd0 ["INT_ADD", "register:40f0:8", ["const:c50cd0:8", "const:4:8"]]
+ 00c50cd0 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c50c34 bytes fb240094
+ 00c50cd0 bytes 08250094
- 00c50c58 ["COPY", "tmp:0:8", ["const:d90:8"]]
- 00c50c58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c50c58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c50c58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c50cf4 ["COPY", "tmp:0:8", ["const:e60:8"]]
+ 00c50cf4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c50cf4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c50cf4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c50c58 bytes 08413691
+ 00c50cf4 bytes 08813991
- 00c50c9c ["INT_ADD", "register:40f0:8", ["const:c50c9c:8", "const:4:8"]]
- 00c50c9c ["CALL", null, ["callee:00c580f0:8"]]
+ 00c50d38 ["INT_ADD", "register:40f0:8", ["const:c50d38:8", "const:4:8"]]
+ 00c50d38 ["CALL", null, ["callee:00c580f0:8"]]
- 00c50c9c bytes e11c0094
+ 00c50d38 bytes ee1c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c952237d2b83152bfe80fff6b307aa56"></a>

### [`00c50ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50ccc.md) → [`00c50d68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50d68.md) FUN_00c50d68

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c3800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c380a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.14% / 新版 97.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c50ee4",
      "incomplete_value": false,
      "site": "00c50efc",
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
            "const:e95:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c50e48",
      "incomplete_value": false,
      "site": "00c50e60",
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
            "const:ee2:8"
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
      "definition_site": "00c50eec",
      "incomplete_value": false,
      "site": "00c50efc",
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
            "const:52e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c50e50",
      "incomplete_value": false,
      "site": "00c50e60",
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
            "const:58a:8"
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
      "definition_site": "00c50ef4",
      "incomplete_value": false,
      "site": "00c50efc",
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
      "definition_site": "00c50e58",
      "incomplete_value": false,
      "site": "00c50e60",
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
    "ordinal": 5,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c50ee4",
      "PARAM",
      [
        "storage",
        "002a0ee2",
        null,
        "string"
      ]
    ],
    [
      "00c50eec",
      "PARAM",
      [
        "storage",
        "002ac58a",
        null,
        "string"
      ]
    ],
    [
      "00c50ef4",
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
      "00c50ee4",
      "PARAM",
      [
        "storage",
        "002a0e95",
        null,
        "string"
      ]
    ],
    [
      "00c50eec",
      "PARAM",
      [
        "storage",
        "002ac52e",
        null,
        "string"
      ]
    ],
    [
      "00c50ef4",
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

- 旧版 [`00c50e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50ccc.md#insn-00c50e60) · [`00c50d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50ccc.md#insn-00c50d28) · [`00c50d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50ccc.md#insn-00c50d70)
- 新版 [`00c50efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50d68.md#insn-00c50efc) · [`00c50dc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50d68.md#insn-00c50dc4) · [`00c50e0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50d68.md#insn-00c50e0c)

~~~diff
- 00c50e60 ["INT_ADD", "register:40f0:8", ["const:c50e60:8", "const:4:8"]]
- 00c50e60 ["CALL", null, ["callee:00c380a8:8"]]
+ 00c50efc ["INT_ADD", "register:40f0:8", ["const:c50efc:8", "const:4:8"]]
+ 00c50efc ["CALL", null, ["callee:00c380a8:8"]]
- 00c50e60 bytes 6b9cff97
+ 00c50efc bytes 6b9cff97
- 00c50d28 ["INT_ADD", "register:40f0:8", ["const:c50d28:8", "const:4:8"]]
- 00c50d28 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c50dc4 ["INT_ADD", "register:40f0:8", ["const:c50dc4:8", "const:4:8"]]
+ 00c50dc4 ["CALL", null, ["callee:00c5a170:8"]]
- 00c50d28 bytes de240094
+ 00c50dc4 bytes eb240094
- 00c50d70 ["INT_ADD", "register:40f0:8", ["const:c50d70:8", "const:4:8"]]
- 00c50d70 ["CALL", null, ["callee:00c5a170:8"]]
+ 00c50e0c ["INT_ADD", "register:40f0:8", ["const:c50e0c:8", "const:4:8"]]
+ 00c50e0c ["CALL", null, ["callee:00c5a170:8"]]
- 00c50d70 bytes cc240094
+ 00c50e0c bytes d9240094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cbdb729f17d18e1ed03f43ec83ecc6e0"></a>

### [`00c50e78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50e78.md) → [`00c50f14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50f14.md) FUN_00c50f14

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3accc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3ad68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.56% / 新版 95.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c50f80",
      "incomplete_value": false,
      "site": "00c50f80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c50ee4",
      "incomplete_value": false,
      "site": "00c50ee4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:e00:8"
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
      "00c50f80",
      "DATA",
      [
        "storage",
        "00c99e00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c50f80",
      "DATA",
      [
        "storage",
        "00c99ed0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c50eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50e78.md#insn-00c50eb0) · [`00c50edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50e78.md#insn-00c50edc) · [`00c50f28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50e78.md#insn-00c50f28)
- 新版 [`00c50f4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50f14.md#insn-00c50f4c) · [`00c50f78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50f14.md#insn-00c50f78) · [`00c50fc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c50f14.md#insn-00c50fc4)

~~~diff
- 00c50eb0 ["INT_ADD", "register:40f0:8", ["const:c50eb0:8", "const:4:8"]]
- 00c50eb0 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c50f4c ["INT_ADD", "register:40f0:8", ["const:c50f4c:8", "const:4:8"]]
+ 00c50f4c ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c50eb0 bytes 5c240094
+ 00c50f4c bytes 69240094
- 00c50edc ["COPY", "tmp:0:8", ["const:e00:8"]]
- 00c50edc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c50edc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c50edc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c50f78 ["COPY", "tmp:0:8", ["const:ed0:8"]]
+ 00c50f78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c50f78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c50f78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c50edc bytes 08013891
+ 00c50f78 bytes 08413b91
- 00c50f28 ["INT_ADD", "register:40f0:8", ["const:c50f28:8", "const:4:8"]]
- 00c50f28 ["CALL", null, ["callee:00c580f0:8"]]
+ 00c50fc4 ["INT_ADD", "register:40f0:8", ["const:c50fc4:8", "const:4:8"]]
+ 00c50fc4 ["CALL", null, ["callee:00c580f0:8"]]
- 00c50f28 bytes 3e1c0094
+ 00c50fc4 bytes 4b1c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71aa99b9ddb094faad142690dde46dca"></a>

### [`00c51b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51b74.md) → [`00c51c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51c10.md) FUN_00c51c10

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c5183c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c5183c.md) [`00c51a4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51a4c.md) · 呼出先 6件 [`00c3800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md)
- 新版 呼出元 2件 [`00c518d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c518d8.md) [`00c51ae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51ae8.md) · 呼出先 6件 [`00c380a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md)

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
      "definition_site": "00c51d78",
      "incomplete_value": false,
      "site": "00c51d90",
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
            "const:e95:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c51cdc",
      "incomplete_value": false,
      "site": "00c51cf4",
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
            "const:ee2:8"
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
      "definition_site": "00c51d80",
      "incomplete_value": false,
      "site": "00c51d90",
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
            "const:8c7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c51ce4",
      "incomplete_value": false,
      "site": "00c51cf4",
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
            "const:896:8"
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
      "definition_site": "00c51d88",
      "incomplete_value": false,
      "site": "00c51d90",
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
            "const:955:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c51cec",
      "incomplete_value": false,
      "site": "00c51cf4",
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
            "const:9b1:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c51d78",
      "PARAM",
      [
        "storage",
        "002a0ee2",
        null,
        "string"
      ]
    ],
    [
      "00c51d80",
      "PARAM",
      [
        "storage",
        "002b2896",
        null,
        "string"
      ]
    ],
    [
      "00c51d88",
      "PARAM",
      [
        "storage",
        "002a89b1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c51d78",
      "PARAM",
      [
        "storage",
        "002a0e95",
        null,
        "string"
      ]
    ],
    [
      "00c51d80",
      "PARAM",
      [
        "storage",
        "002b28c7",
        null,
        "string"
      ]
    ],
    [
      "00c51d88",
      "PARAM",
      [
        "storage",
        "002a8955",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c51cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51b74.md#insn-00c51cf4) · [`00c51bcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51b74.md#insn-00c51bcc) · [`00c51c0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51b74.md#insn-00c51c0c)
- 新版 [`00c51d90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51c10.md#insn-00c51d90) · [`00c51c68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51c10.md#insn-00c51c68) · [`00c51ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51c10.md#insn-00c51ca8)

~~~diff
- 00c51cf4 ["INT_ADD", "register:40f0:8", ["const:c51cf4:8", "const:4:8"]]
- 00c51cf4 ["CALL", null, ["callee:00c380a8:8"]]
+ 00c51d90 ["INT_ADD", "register:40f0:8", ["const:c51d90:8", "const:4:8"]]
+ 00c51d90 ["CALL", null, ["callee:00c380a8:8"]]
- 00c51cf4 bytes c698ff97
+ 00c51d90 bytes c698ff97
- 00c51bcc ["COPY", "register:0:8", ["register:4040:8"]]
- 00c51bcc ["INT_ADD", "register:40f0:8", ["const:c51bcc:8", "const:4:8"]]
- 00c51bcc ["CALLIND", null, ["register:0:8"]]
+ 00c51c68 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c51c68 ["INT_ADD", "register:40f0:8", ["const:c51c68:8", "const:4:8"]]
+ 00c51c68 ["CALLIND", null, ["register:0:8"]]
- 00c51bcc bytes 00013fd6
+ 00c51c68 bytes 00013fd6
- 00c51c0c ["INT_ADD", "register:40f0:8", ["const:c51c0c:8", "const:4:8"]]
- 00c51c0c ["CALL", null, ["callee:00c5a170:8"]]
+ 00c51ca8 ["INT_ADD", "register:40f0:8", ["const:c51ca8:8", "const:4:8"]]
+ 00c51ca8 ["CALL", null, ["callee:00c5a170:8"]]
- 00c51c0c bytes 25210094
+ 00c51ca8 bytes 32210094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83d0af2cc1f0367919973d87e73cd2b7"></a>

### [`00c51f64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51f64.md) → [`00c52000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52000.md) __cxa_free_exception

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c57f20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f20.md) · 呼出先 1件 [`00c52818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52818.md)
- 新版 呼出元 1件 [`00c57ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57ff0.md) · 呼出先 1件 [`00c528b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c528b4.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 87.50% / 新版 87.50%

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
      "site": "00c52010",
      "value": [
        "leaf",
        "ram:c528b4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c51f74",
      "value": [
        "leaf",
        "ram:c52818:8"
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
      "00c52010",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c52818"
      ]
    ]
  ],
  "added": [
    [
      "00c52010",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c528b4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c51f74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51f64.md#insn-00c51f74)
- 新版 [`00c52010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52000.md#insn-00c52010)

~~~diff
- 00c51f74 ["INT_ADD", "register:40f0:8", ["const:c51f74:8", "const:4:8"]]
- 00c51f74 ["CALL", null, ["ram:c52818:8"]]
+ 00c52010 ["INT_ADD", "register:40f0:8", ["const:c52010:8", "const:4:8"]]
+ 00c52010 ["CALL", null, ["ram:c528b4:8"]]
- 00c51f74 bytes 29020094
+ 00c52010 bytes 29020094
~~~


<a id="compare-7ae771ab2f4f2b6c8b4c2cfdd1d4231c"></a>

### [`00c51ff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51ff8.md) → [`00c52094`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52094.md) FUN_00c52094

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c51f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51f88.md) · 呼出先 4件 [`00440c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440c3c.md) [`00c378e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c378e0.md) [`00c52818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52818.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)
- 新版 呼出元 1件 [`00c52024`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52024.md) · 呼出先 4件 [`00440c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440c7c.md) [`00c3797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c3797c.md) [`00c528b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c528b4.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)

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
      "site": "00c520d8",
      "value": [
        "leaf",
        "ram:c528b4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c5203c",
      "value": [
        "leaf",
        "ram:c52818:8"
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
      "00c520d8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c52818"
      ]
    ]
  ],
  "added": [
    [
      "00c520d8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c528b4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c5203c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51ff8.md#insn-00c5203c) · [`00c5201c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51ff8.md#insn-00c5201c) · [`00c52034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51ff8.md#insn-00c52034)
- 新版 [`00c520d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52094.md#insn-00c520d8) · [`00c520b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52094.md#insn-00c520b8) · [`00c520d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52094.md#insn-00c520d0)

~~~diff
- 00c5203c ["INT_ADD", "register:40f0:8", ["const:c5203c:8", "const:4:8"]]
- 00c5203c ["CALL", null, ["ram:c52818:8"]]
+ 00c520d8 ["INT_ADD", "register:40f0:8", ["const:c520d8:8", "const:4:8"]]
+ 00c520d8 ["CALL", null, ["ram:c528b4:8"]]
- 00c5203c bytes f7010094
+ 00c520d8 bytes f7010094
- 00c5201c ["INT_ADD", "register:40f0:8", ["const:c5201c:8", "const:4:8"]]
- 00c5201c ["CALL", null, ["callee:00c53da0:8"]]
+ 00c520b8 ["INT_ADD", "register:40f0:8", ["const:c520b8:8", "const:4:8"]]
+ 00c520b8 ["CALL", null, ["callee:00c53da0:8"]]
- 00c5201c bytes 39070094
+ 00c520b8 bytes 3a070094
- 00c52034 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c52034 ["INT_ADD", "register:40f0:8", ["const:c52034:8", "const:4:8"]]
- 00c52034 ["CALLIND", null, ["register:0:8"]]
+ 00c520d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c520d0 ["INT_ADD", "register:40f0:8", ["const:c520d0:8", "const:4:8"]]
+ 00c520d0 ["CALLIND", null, ["register:0:8"]]
- 00c52034 bytes 00013fd6
+ 00c520d0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b35cb533ab57c88daada1ff41fc024b"></a>

### [`00c52130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52130.md) → [`00c521cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c521cc.md) __cxa_end_catch

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c582d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582d0.md) · 呼出先 4件 [`00c52818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52818.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5413c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c5413c.md) [`00c5eda0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eda0.md)
- 新版 呼出元 1件 [`00c583a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583a0.md) · 呼出先 4件 [`00c528b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c528b4.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c541dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c541dc.md) [`00c5ee70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ee70.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.49% / 新版 96.49%

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
      "site": "00c5223c",
      "value": [
        "leaf",
        "ram:c528b4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c521a0",
      "value": [
        "leaf",
        "ram:c52818:8"
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
      "site": "00c5226c",
      "value": [
        "leaf",
        "ram:c528b4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c521d0",
      "value": [
        "leaf",
        "ram:c52818:8"
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
      "00c5223c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c52818"
      ]
    ],
    [
      "00c5226c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c52818"
      ]
    ]
  ],
  "added": [
    [
      "00c5223c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c528b4"
      ]
    ],
    [
      "00c5226c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c528b4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c521a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52130.md#insn-00c521a0) · [`00c521d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52130.md#insn-00c521d0) · [`00c52140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52130.md#insn-00c52140)
- 新版 [`00c5223c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c521cc.md#insn-00c5223c) · [`00c5226c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c521cc.md#insn-00c5226c) · [`00c521dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c521cc.md#insn-00c521dc)

~~~diff
- 00c521a0 ["INT_ADD", "register:40f0:8", ["const:c521a0:8", "const:4:8"]]
- 00c521a0 ["CALL", null, ["ram:c52818:8"]]
+ 00c5223c ["INT_ADD", "register:40f0:8", ["const:c5223c:8", "const:4:8"]]
+ 00c5223c ["CALL", null, ["ram:c528b4:8"]]
- 00c521a0 bytes 9e010094
+ 00c5223c bytes 9e010094
- 00c521d0 ["INT_ADD", "register:40f0:8", ["const:c521d0:8", "const:4:8"]]
- 00c521d0 ["CALL", null, ["ram:c52818:8"]]
+ 00c5226c ["INT_ADD", "register:40f0:8", ["const:c5226c:8", "const:4:8"]]
+ 00c5226c ["CALL", null, ["ram:c528b4:8"]]
- 00c521d0 bytes 92010094
+ 00c5226c bytes 92010094
- 00c52140 ["INT_ADD", "register:40f0:8", ["const:c52140:8", "const:4:8"]]
- 00c52140 ["CALL", null, ["callee:00c5ee70:8"]]
+ 00c521dc ["INT_ADD", "register:40f0:8", ["const:c521dc:8", "const:4:8"]]
+ 00c521dc ["CALL", null, ["callee:00c5ee70:8"]]
- 00c52140 bytes 18330094
+ 00c521dc bytes 25330094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44e8a26e7b13cdace25889ad776ddb65"></a>

### [`00c5221c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c5221c.md) → [`00c522b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c522b8.md) __cxa_decrement_exception_refcount

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5df10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5df10.md) · 呼出先 2件 [`00c52818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52818.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)
- 新版 呼出元 1件 [`00c5dfe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dfe0.md) · 呼出先 2件 [`00c528b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c528b4.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

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
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c522f8",
      "value": [
        "leaf",
        "ram:c528b4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c5225c",
      "value": [
        "leaf",
        "ram:c52818:8"
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
      "00c522f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c52818"
      ]
    ]
  ],
  "added": [
    [
      "00c522f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c528b4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c5225c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c5221c.md#insn-00c5225c) · [`00c5223c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c5221c.md#insn-00c5223c) · [`00c52254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c5221c.md#insn-00c52254)
- 新版 [`00c522f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c522b8.md#insn-00c522f8) · [`00c522d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c522b8.md#insn-00c522d8) · [`00c522f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c522b8.md#insn-00c522f0)

~~~diff
- 00c5225c ["INT_ADD", "register:40f0:8", ["const:c5225c:8", "const:4:8"]]
- 00c5225c ["CALL", null, ["ram:c52818:8"]]
+ 00c522f8 ["INT_ADD", "register:40f0:8", ["const:c522f8:8", "const:4:8"]]
+ 00c522f8 ["CALL", null, ["ram:c528b4:8"]]
- 00c5225c bytes 6f010094
+ 00c522f8 bytes 6f010094
- 00c5223c ["INT_ADD", "register:40f0:8", ["const:c5223c:8", "const:4:8"]]
- 00c5223c ["CALL", null, ["callee:00c53da0:8"]]
+ 00c522d8 ["INT_ADD", "register:40f0:8", ["const:c522d8:8", "const:4:8"]]
+ 00c522d8 ["CALL", null, ["callee:00c53da0:8"]]
- 00c5223c bytes b1060094
+ 00c522d8 bytes b2060094
- 00c52254 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c52254 ["INT_ADD", "register:40f0:8", ["const:c52254:8", "const:4:8"]]
- 00c52254 ["CALLIND", null, ["register:0:8"]]
+ 00c522f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c522f0 ["INT_ADD", "register:40f0:8", ["const:c522f0:8", "const:4:8"]]
+ 00c522f0 ["CALLIND", null, ["register:0:8"]]
- 00c52254 bytes 00013fd6
+ 00c522f0 bytes 00013fd6
~~~


<a id="compare-d6e21dd3fa38686d9045b539fccf7923"></a>

### [`00c52578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52578.md) → [`00c52614`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52614.md) FUN_00c52614

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c52458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52458.md) · 呼出先 4件 [`00440c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440c3c.md) [`00c378e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c378e0.md) [`00c52818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52818.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)
- 新版 呼出元 1件 [`00c524f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c524f4.md) · 呼出先 4件 [`00440c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440c7c.md) [`00c3797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c3797c.md) [`00c528b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c528b4.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)

変更の種類 call, call_target, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 92.86% / 新版 92.86%

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
      "site": "00c52660",
      "value": [
        "leaf",
        "ram:c528b4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c525c4",
      "value": [
        "leaf",
        "ram:c52818:8"
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
      "00c52660",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c52818"
      ]
    ],
    [
      "00c52674",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c52818"
      ]
    ]
  ],
  "added": [
    [
      "00c52660",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c528b4"
      ]
    ],
    [
      "00c52674",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c528b4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c525c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52578.md#insn-00c525c4) · [`00c525a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52578.md#insn-00c525a4) · [`00c525bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52578.md#insn-00c525bc)
- 新版 [`00c52660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52614.md#insn-00c52660) · [`00c52640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52614.md#insn-00c52640) · [`00c52658`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52614.md#insn-00c52658)

~~~diff
- 00c525c4 ["INT_ADD", "register:40f0:8", ["const:c525c4:8", "const:4:8"]]
- 00c525c4 ["CALL", null, ["ram:c52818:8"]]
+ 00c52660 ["INT_ADD", "register:40f0:8", ["const:c52660:8", "const:4:8"]]
+ 00c52660 ["CALL", null, ["ram:c528b4:8"]]
- 00c525c4 bytes 95000094
+ 00c52660 bytes 95000094
- 00c525a4 ["INT_ADD", "register:40f0:8", ["const:c525a4:8", "const:4:8"]]
- 00c525a4 ["CALL", null, ["callee:00c53da0:8"]]
+ 00c52640 ["INT_ADD", "register:40f0:8", ["const:c52640:8", "const:4:8"]]
+ 00c52640 ["CALL", null, ["callee:00c53da0:8"]]
- 00c525a4 bytes d7050094
+ 00c52640 bytes d8050094
- 00c525bc ["COPY", "register:0:8", ["register:4040:8"]]
- 00c525bc ["INT_ADD", "register:40f0:8", ["const:c525bc:8", "const:4:8"]]
- 00c525bc ["CALLIND", null, ["register:0:8"]]
+ 00c52658 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c52658 ["INT_ADD", "register:40f0:8", ["const:c52658:8", "const:4:8"]]
+ 00c52658 ["CALLIND", null, ["register:0:8"]]
- 00c525bc bytes 00013fd6
+ 00c52658 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a5279fc8df79772a6042830c12b8686"></a>

### [`00c52690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52690.md) → [`00c5272c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c5272c.md) FUN_00c5272c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c52644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52644.md) · 呼出先 3件 [`00c3800c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md) [`00c5b6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6a0.md) [`00c5b6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6b0.md)
- 新版 呼出元 1件 [`00c526e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c526e0.md) · 呼出先 3件 [`00c380a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md) [`00c5b770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b770.md) [`00c5b780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b780.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 82.02% / 新版 82.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 8件, `store_destination` 3件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c5277c",
      "incomplete_value": true,
      "site": "00c5277c",
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
            "const:b90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c526e0",
      "incomplete_value": true,
      "site": "00c526e0",
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
            "const:a90:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c52774",
      "incomplete_value": false,
      "site": "00c5277c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:bac:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c526d8",
      "incomplete_value": false,
      "site": "00c526e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:aac:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c52780",
      "incomplete_value": false,
      "site": "00c52780",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:bac:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c526e4",
      "incomplete_value": false,
      "site": "00c526e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:aac:8"
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
      "00c52744",
      "PARAM",
      [
        "storage",
        "01128a68",
        null,
        null
      ]
    ],
    [
      "00c52750",
      "READ",
      [
        "storage",
        "01128a90",
        null,
        "undefined8"
      ]
    ],
    [
      "00c5277c",
      "WRITE",
      [
        "storage",
        "01128a90",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c52744",
      "PARAM",
      [
        "storage",
        "01128b68",
        null,
        null
      ]
    ],
    [
      "00c52750",
      "READ",
      [
        "storage",
        "01128b90",
        null,
        "undefined8"
      ]
    ],
    [
      "00c5277c",
      "WRITE",
      [
        "storage",
        "01128b90",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c526ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52690.md#insn-00c526ac) · [`00c526e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52690.md#insn-00c526e0) · [`00c526f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52690.md#insn-00c526f4)
- 新版 [`00c52748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c5272c.md#insn-00c52748) · [`00c5277c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c5272c.md#insn-00c5277c) · [`00c52790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c5272c.md#insn-00c52790)

~~~diff
- 00c526ac ["INT_ADD", "register:40f0:8", ["const:c526ac:8", "const:4:8"]]
- 00c526ac ["CALL", null, ["callee:00c5b770:8"]]
+ 00c52748 ["INT_ADD", "register:40f0:8", ["const:c52748:8", "const:4:8"]]
+ 00c52748 ["CALL", null, ["callee:00c5b770:8"]]
- 00c526ac bytes fd230094
+ 00c52748 bytes 0a240094
- 00c526e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a90:8"]]
- 00c526e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4070:8"]]
+ 00c5277c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b90:8"]]
+ 00c5277c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4070:8"]]
- 00c526e0 bytes 0e4905f9
+ 00c5277c bytes 0ec905f9
- 00c526f4 ["COPY", "tmp:0:8", ["const:aa0:8"]]
- 00c526f4 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
- 00c526f4 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
- 00c526f4 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
+ 00c52790 ["COPY", "tmp:0:8", ["const:ba0:8"]]
+ 00c52790 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
+ 00c52790 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
+ 00c52790 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
- 00c526f4 bytes 6b812a91
+ 00c52790 bytes 6b812e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3aff1fa856faeb1a9c4b3ebd585921ee"></a>

### [`00c52948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52948.md) → [`00c529e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c529e4.md) __gxx_personality_v0

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00c378e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c378e0.md) [`00c51e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51e48.md) [`00c53100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53100.md) [`00c532a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c532a8.md) [`00c540d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c540d4.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00c3797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c3797c.md) [`00c51ee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51ee4.md) [`00c5319c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c5319c.md) [`00c53344`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53344.md) [`00c54174`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54174.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.89% / 新版 98.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c52d38",
      "incomplete_value": true,
      "site": "00c52d38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "INT_MULT",
            "8",
            [
              "LOAD",
              [
                "live",
                "register:40d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c52c9c",
      "incomplete_value": true,
      "site": "00c52c9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "INT_MULT",
            "8",
            [
              "LOAD",
              [
                "live",
                "register:40d0:8"
              ]
            ]
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
      "00c52d28",
      "DATA",
      [
        "storage",
        "00313da8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c52d28",
      "DATA",
      [
        "storage",
        "00313de8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c529c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52948.md#insn-00c529c8) · [`00c529d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52948.md#insn-00c529d8) · [`00c529e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52948.md#insn-00c529e4)
- 新版 [`00c52a64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c529e4.md#insn-00c52a64) · [`00c52a74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c529e4.md#insn-00c52a74) · [`00c52a80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c529e4.md#insn-00c52a80)

~~~diff
- 00c529c8 ["INT_ADD", "register:40f0:8", ["const:c529c8:8", "const:4:8"]]
- 00c529c8 ["CALL", null, ["callee:00c541f8:8"]]
+ 00c52a64 ["INT_ADD", "register:40f0:8", ["const:c52a64:8", "const:4:8"]]
+ 00c52a64 ["CALL", null, ["callee:00c541f8:8"]]
- 00c529c8 bytes e4050094
+ 00c52a64 bytes e5050094
- 00c529d8 ["INT_ADD", "register:40f0:8", ["const:c529d8:8", "const:4:8"]]
- 00c529d8 ["CALL", null, ["callee:00c541f8:8"]]
+ 00c52a74 ["INT_ADD", "register:40f0:8", ["const:c52a74:8", "const:4:8"]]
+ 00c52a74 ["CALL", null, ["callee:00c541f8:8"]]
- 00c529d8 bytes e0050094
+ 00c52a74 bytes e1050094
- 00c529e4 ["INT_ADD", "register:40f0:8", ["const:c529e4:8", "const:4:8"]]
- 00c529e4 ["CALL", null, ["callee:00c54230:8"]]
+ 00c52a80 ["INT_ADD", "register:40f0:8", ["const:c52a80:8", "const:4:8"]]
+ 00c52a80 ["CALL", null, ["callee:00c54230:8"]]
- 00c529e4 bytes eb050094
+ 00c52a80 bytes ec050094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc914c83f925aa19b30b06dbc9c700f6"></a>

### [`00c52ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52ee4.md) → [`00c52f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52f80.md) __cxa_call_unexpected

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 18件 [`00c37894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37894.md) [`00c378e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c378e0.md) [`00c37ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ba4.md) [`00c51e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51e48.md) [`00c51e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c51/00c51e54.md)
- 新版 呼出元 0件  · 呼出先 18件 [`00c37930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37930.md) [`00c3797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c3797c.md) [`00c37c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c40.md) [`00c51ee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51ee4.md) [`00c51ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51ef0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.69% / 新版 97.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c530d4",
      "incomplete_value": true,
      "site": "00c530d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c53038",
      "incomplete_value": true,
      "site": "00c5303c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00c530e8",
      "incomplete_value": true,
      "site": "00c530fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c5304c",
      "incomplete_value": true,
      "site": "00c53060",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c53134",
      "incomplete_value": true,
      "site": "00c5313c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c53098",
      "incomplete_value": true,
      "site": "00c530a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e60:8"
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
      "00c530d0",
      "READ",
      [
        "storage",
        "00c9be58",
        null,
        "pointer"
      ]
    ],
    [
      "00c530d8",
      "DATA",
      [
        "storage",
        "00c96668",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "00c530e8",
      "READ",
      [
        "storage",
        "00c9be60",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c530d0",
      "READ",
      [
        "storage",
        "00c9bf28",
        null,
        "pointer"
      ]
    ],
    [
      "00c530d8",
      "DATA",
      [
        "storage",
        "00c96738",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "00c530e8",
      "READ",
      [
        "storage",
        "00c9bf30",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c53060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52ee4.md#insn-00c53060) · [`00c530a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52ee4.md#insn-00c530a0) · [`00c52f0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c52/00c52ee4.md#insn-00c52f0c)
- 新版 [`00c530fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52f80.md#insn-00c530fc) · [`00c5313c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52f80.md#insn-00c5313c) · [`00c52fa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c52/00c52f80.md#insn-00c52fa8)

~~~diff
- 00c53060 ["INT_ADD", "register:40f0:8", ["const:c53060:8", "const:4:8"]]
- 00c53060 ["CALL", null, ["callee:00c53344:8"]]
+ 00c530fc ["INT_ADD", "register:40f0:8", ["const:c530fc:8", "const:4:8"]]
+ 00c530fc ["CALL", null, ["callee:00c53344:8"]]
- 00c53060 bytes 92000094
+ 00c530fc bytes 92000094
- 00c530a0 ["INT_ADD", "register:40f0:8", ["const:c530a0:8", "const:4:8"]]
- 00c530a0 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00c5313c ["INT_ADD", "register:40f0:8", ["const:c5313c:8", "const:4:8"]]
+ 00c5313c ["CALL", null, ["callee:00c57fe0:8"]]
- 00c530a0 bytes 9c130094
+ 00c5313c bytes a9130094
- 00c52f0c ["INT_ADD", "register:40f0:8", ["const:c52f0c:8", "const:4:8"]]
- 00c52f0c ["CALL", null, ["callee:00c580e0:8"]]
+ 00c52fa8 ["INT_ADD", "register:40f0:8", ["const:c52fa8:8", "const:4:8"]]
+ 00c52fa8 ["CALL", null, ["callee:00c580e0:8"]]
- 00c52f0c bytes 41140094
+ 00c52fa8 bytes 4e140094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7445098e5526695e53c1b89350ed9df"></a>

### [`00c53504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53504.md) → [`00c535a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c535a0.md) __emutls_get_address

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5a2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a2f0.md) · 呼出先 11件 [`00c5372c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c5372c.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md) [`00c58140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58140.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c5a3c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a3c0.md) · 呼出先 11件 [`00c537c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c537c8.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md) [`00c58210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58210.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 95.93% / 新版 95.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 1件

アドレスに依存する影響 `call_argument_candidate` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c5365c",
      "incomplete_value": false,
      "site": "00c5365c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:db0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c535c0",
      "incomplete_value": false,
      "site": "00c535c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:cb0:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c53654",
      "incomplete_value": true,
      "site": "00c5365c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c535b8",
      "incomplete_value": true,
      "site": "00c535c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:1:8"
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
      "definition_site": "00c53654",
      "incomplete_value": true,
      "site": "00c53660",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c535b8",
      "incomplete_value": true,
      "site": "00c535c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:1:8"
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
      "00c535c8",
      "READ",
      [
        "storage",
        "01128ca4",
        null,
        "undefined4"
      ]
    ],
    [
      "00c53630",
      "PARAM",
      [
        "storage",
        "00c5372c",
        null,
        null
      ]
    ],
    [
      "00c53634",
      "PARAM",
      [
        "storage",
        "01128ca8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c535c8",
      "READ",
      [
        "storage",
        "01128da4",
        null,
        "undefined4"
      ]
    ],
    [
      "00c53630",
      "PARAM",
      [
        "storage",
        "00c537c8",
        null,
        null
      ]
    ],
    [
      "00c53634",
      "PARAM",
      [
        "storage",
        "01128da8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c53530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53504.md#insn-00c53530) · [`00c5358c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53504.md#insn-00c5358c) · [`00c5359c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53504.md#insn-00c5359c)
- 新版 [`00c535cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c535a0.md#insn-00c535cc) · [`00c53628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c535a0.md#insn-00c53628) · [`00c53638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c535a0.md#insn-00c53638)

~~~diff
- 00c53530 ["INT_ADD", "register:40f0:8", ["const:c53530:8", "const:4:8"]]
- 00c53530 ["CALL", null, ["callee:00c5e2c0:8"]]
+ 00c535cc ["INT_ADD", "register:40f0:8", ["const:c535cc:8", "const:4:8"]]
+ 00c535cc ["CALL", null, ["callee:00c5e2c0:8"]]
- 00c53530 bytes 302b0094
+ 00c535cc bytes 3d2b0094
- 00c5358c ["COPY", "tmp:0:8", ["const:ca8:8"]]
- 00c5358c ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 00c5358c ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 00c5358c ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 00c53628 ["COPY", "tmp:0:8", ["const:da8:8"]]
+ 00c53628 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 00c53628 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 00c53628 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 00c5358c bytes 94a23291
+ 00c53628 bytes 94a23691
- 00c5359c ["INT_ADD", "register:40f0:8", ["const:c5359c:8", "const:4:8"]]
- 00c5359c ["CALL", null, ["callee:00c5b790:8"]]
+ 00c53638 ["INT_ADD", "register:40f0:8", ["const:c53638:8", "const:4:8"]]
+ 00c53638 ["CALL", null, ["callee:00c5b790:8"]]
- 00c5359c bytes 49200094
+ 00c53638 bytes 56200094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db9343ab50415019a7274972d1094733"></a>

### [`00c536f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c536f0.md) → [`00c5378c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c5378c.md) FUN_00c5378c

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0043ae28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae28.md) · 呼出先 1件 [`00c5ef10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ef10.md)
- 新版 呼出元 1件 [`0043ae68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043ae68.md) · 呼出先 1件 [`00c5efe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5efe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c537b0",
      "incomplete_value": true,
      "site": "00c537b4",
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
      "definition_site": "00c53714",
      "incomplete_value": true,
      "site": "00c53718",
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
      "00c53794",
      "READ",
      [
        "storage",
        "01128ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c537b0",
      "READ",
      [
        "storage",
        "01128ca4",
        null,
        "undefined4"
      ]
    ],
    [
      "00c537b8",
      "WRITE",
      [
        "storage",
        "01128ca0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c53794",
      "READ",
      [
        "storage",
        "01128da0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c537b0",
      "READ",
      [
        "storage",
        "01128da4",
        null,
        "undefined4"
      ]
    ],
    [
      "00c537b8",
      "WRITE",
      [
        "storage",
        "01128da0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c53718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c536f0.md#insn-00c53718) · [`00c536f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c536f0.md#insn-00c536f8) · [`00c53710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c536f0.md#insn-00c53710)
- 新版 [`00c537b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c5378c.md#insn-00c537b4) · [`00c53794`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c5378c.md#insn-00c53794) · [`00c537ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c5378c.md#insn-00c537ac)

~~~diff
- 00c53718 ["INT_ADD", "register:40f0:8", ["const:c53718:8", "const:4:8"]]
- 00c53718 ["CALL", null, ["callee:00c5efe0:8"]]
+ 00c537b4 ["INT_ADD", "register:40f0:8", ["const:c537b4:8", "const:4:8"]]
+ 00c537b4 ["CALL", null, ["callee:00c5efe0:8"]]
- 00c53718 bytes fe2d0094
+ 00c537b4 bytes 0b2e0094
- 00c536f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ca0:8"]]
- 00c536f8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00c536f8 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00c53794 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:da0:8"]]
+ 00c53794 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00c53794 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00c536f8 bytes 08817239
+ 00c53794 bytes 08817639
- 00c53710 ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 00c53710 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00c53710 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00c53710 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00c537ac ["COPY", "tmp:0:8", ["const:da0:8"]]
+ 00c537ac ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00c537ac ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00c537ac ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00c53710 bytes 73823291
+ 00c537ac bytes 73823691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec21dc9e11a9e8088b76b8964bca6225"></a>

### [`00c5372c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c5372c.md) → [`00c537c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c537c8.md) FUN_00c537c8

採用 · 移動量 `+0x9c` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c53504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53504.md) · 呼出先 3件 [`00c53768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53768.md) [`00c5a300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a300.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 1件 [`00c535a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c535a0.md) · 呼出先 3件 [`00c53804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53804.md) [`00c5a3d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a3d0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c537f0",
      "incomplete_value": false,
      "site": "00c537f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:da0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c53754",
      "incomplete_value": false,
      "site": "00c53754",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
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
      "definition_site": "00c537d4",
      "incomplete_value": false,
      "site": "00c537e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:da4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c53738",
      "incomplete_value": false,
      "site": "00c53744",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:ca4:8"
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
      "definition_site": "00c537dc",
      "incomplete_value": false,
      "site": "00c537e0",
      "value": [
        "leaf",
        "const:c53804:8"
      ]
    },
    "old": {
      "definition_site": "00c53740",
      "incomplete_value": false,
      "site": "00c53744",
      "value": [
        "leaf",
        "const:c53768:8"
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
      "00c537d4",
      "PARAM",
      [
        "storage",
        "01128ca4",
        null,
        "undefined4"
      ]
    ],
    [
      "00c537dc",
      "PARAM",
      [
        "storage",
        "00c53768",
        null,
        null
      ]
    ],
    [
      "00c537f0",
      "WRITE",
      [
        "storage",
        "01128ca0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c537d4",
      "PARAM",
      [
        "storage",
        "01128da4",
        null,
        "undefined4"
      ]
    ],
    [
      "00c537dc",
      "PARAM",
      [
        "storage",
        "00c53804",
        null,
        null
      ]
    ],
    [
      "00c537f0",
      "WRITE",
      [
        "storage",
        "01128da0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c53744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c5372c.md#insn-00c53744) · [`00c53754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c5372c.md#insn-00c53754) · [`00c53738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c5372c.md#insn-00c53738)
- 新版 [`00c537e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c537c8.md#insn-00c537e0) · [`00c537f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c537c8.md#insn-00c537f0) · [`00c537d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c537c8.md#insn-00c537d4)

~~~diff
- 00c53744 ["INT_ADD", "register:40f0:8", ["const:c53744:8", "const:4:8"]]
- 00c53744 ["CALL", null, ["callee:00c5a3d0:8"]]
+ 00c537e0 ["INT_ADD", "register:40f0:8", ["const:c537e0:8", "const:4:8"]]
+ 00c537e0 ["CALL", null, ["callee:00c5a3d0:8"]]
- 00c53744 bytes ef1a0094
+ 00c537e0 bytes fc1a0094
- 00c53754 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00c53754 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:ca0:8"]]
- 00c53754 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00c537f0 ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 00c537f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:da0:8"]]
+ 00c537f0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00c53754 bytes 09813239
+ 00c537f0 bytes 09813639
- 00c53738 ["COPY", "tmp:0:8", ["const:ca4:8"]]
- 00c53738 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c53738 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c53738 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c537d4 ["COPY", "tmp:0:8", ["const:da4:8"]]
+ 00c537d4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c537d4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c537d4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c53738 bytes 00903291
+ 00c537d4 bytes 00903691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74587ba621f2965c463e5b90de890e6c"></a>

### [`00c53824`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53824.md) → [`00c538c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c538c4.md) _INIT_0

採用 · 移動量 `+0xa0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c5d130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d130.md) [`00c5ef20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ef20.md) [`00c5ef30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ef30.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5d200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d200.md) [`00c5eff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eff0.md) [`00c5f000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5f/00c5f000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 86.84% / 新版 86.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c538e4",
      "incomplete_value": false,
      "site": "00c538e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:de0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c53844",
      "incomplete_value": false,
      "site": "00c53844",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:ce0:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c53930",
      "incomplete_value": false,
      "site": "00c53930",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:de0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c53890",
      "incomplete_value": false,
      "site": "00c53890",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:ce0:8"
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
      "definition_site": "00c5394c",
      "incomplete_value": false,
      "site": "00c5394c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:de0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c538ac",
      "incomplete_value": false,
      "site": "00c538ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:ce0:8"
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
      "00c538e4",
      "WRITE",
      [
        "storage",
        "01128ce0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c538f8",
      "PARAM",
      [
        "storage",
        "002a63d1",
        null,
        "string"
      ]
    ],
    [
      "00c53910",
      "PARAM",
      [
        "storage",
        "002a99e5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c538e4",
      "WRITE",
      [
        "storage",
        "01128de0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c538f8",
      "PARAM",
      [
        "storage",
        "002a6375",
        null,
        "string"
      ]
    ],
    [
      "00c53910",
      "PARAM",
      [
        "storage",
        "002a9a14",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c53844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53824.md#insn-00c53844) · [`00c53860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53824.md#insn-00c53860) · [`00c5387c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53824.md#insn-00c5387c)
- 新版 [`00c538e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c538c4.md#insn-00c538e4) · [`00c53900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c538c4.md#insn-00c53900) · [`00c5391c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c538c4.md#insn-00c5391c)

~~~diff
- 00c53844 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00c53844 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00c53844 ["INT_ADD", "tmp:2:8", ["register:4048:8", "const:ce0:8"]]
- 00c53844 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00c538e4 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00c538e4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00c538e4 ["INT_ADD", "tmp:2:8", ["register:4048:8", "const:de0:8"]]
+ 00c538e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00c53844 bytes 3f813339
+ 00c538e4 bytes 3f813739
- 00c53860 ["INT_ADD", "register:40f0:8", ["const:c53860:8", "const:4:8"]]
- 00c53860 ["CALL", null, ["callee:00c5f000:8"]]
+ 00c53900 ["INT_ADD", "register:40f0:8", ["const:c53900:8", "const:4:8"]]
+ 00c53900 ["CALL", null, ["callee:00c5f000:8"]]
- 00c53860 bytes b42d0094
+ 00c53900 bytes c02d0094
- 00c5387c ["INT_ADD", "register:40f0:8", ["const:c5387c:8", "const:4:8"]]
- 00c5387c ["CALL", null, ["callee:00c5d200:8"]]
+ 00c5391c ["INT_ADD", "register:40f0:8", ["const:c5391c:8", "const:4:8"]]
+ 00c5391c ["CALL", null, ["callee:00c5d200:8"]]
- 00c5387c bytes 2d260094
+ 00c5391c bytes 39260094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9bd310d39a5c2c3120c318ba6ae07802"></a>

### [`00c53b68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53b68.md) → [`00c53c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53c08.md) _INIT_1

採用 · 移動量 `+0xa0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c538bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c538bc.md) [`00c5d130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d130.md) [`00c5ef20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ef20.md) [`00c5ef30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ef30.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c5395c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c5395c.md) [`00c5d200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d200.md) [`00c5eff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eff0.md) [`00c5f000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5f/00c5f000.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c53c14",
      "incomplete_value": true,
      "site": "00c53c14",
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
      "definition_site": "00c53b74",
      "incomplete_value": true,
      "site": "00c53b74",
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
      "definition_site": "00c53c2c",
      "incomplete_value": false,
      "site": "00c53c34",
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
            "const:375:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c53b8c",
      "incomplete_value": false,
      "site": "00c53b94",
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
            "const:3d1:8"
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
      "definition_site": "00c53c44",
      "incomplete_value": false,
      "site": "00c53c50",
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
            "const:a14:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c53ba4",
      "incomplete_value": false,
      "site": "00c53bb0",
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
            "const:9e5:8"
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
      "00c53c10",
      "READ",
      [
        "storage",
        "01128ce8",
        null,
        "undefined8"
      ]
    ],
    [
      "00c53c2c",
      "PARAM",
      [
        "storage",
        "002a63d1",
        null,
        "string"
      ]
    ],
    [
      "00c53c44",
      "PARAM",
      [
        "storage",
        "002a99e5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c53c10",
      "READ",
      [
        "storage",
        "01128de8",
        null,
        "undefined8"
      ]
    ],
    [
      "00c53c2c",
      "PARAM",
      [
        "storage",
        "002a6375",
        null,
        "string"
      ]
    ],
    [
      "00c53c44",
      "PARAM",
      [
        "storage",
        "002a9a14",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c53b94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53b68.md#insn-00c53b94) · [`00c53bb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53b68.md#insn-00c53bb0) · [`00c53be0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53b68.md#insn-00c53be0)
- 新版 [`00c53c34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53c08.md#insn-00c53c34) · [`00c53c50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53c08.md#insn-00c53c50) · [`00c53c80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53c08.md#insn-00c53c80)

~~~diff
- 00c53b94 ["INT_ADD", "register:40f0:8", ["const:c53b94:8", "const:4:8"]]
- 00c53b94 ["CALL", null, ["callee:00c5f000:8"]]
+ 00c53c34 ["INT_ADD", "register:40f0:8", ["const:c53c34:8", "const:4:8"]]
+ 00c53c34 ["CALL", null, ["callee:00c5f000:8"]]
- 00c53b94 bytes e72c0094
+ 00c53c34 bytes f32c0094
- 00c53bb0 ["INT_ADD", "register:40f0:8", ["const:c53bb0:8", "const:4:8"]]
- 00c53bb0 ["CALL", null, ["callee:00c5d200:8"]]
+ 00c53c50 ["INT_ADD", "register:40f0:8", ["const:c53c50:8", "const:4:8"]]
+ 00c53c50 ["CALL", null, ["callee:00c5d200:8"]]
- 00c53bb0 bytes 60250094
+ 00c53c50 bytes 6c250094
- 00c53be0 ["INT_ADD", "register:40f0:8", ["const:c53be0:8", "const:4:8"]]
- 00c53be0 ["CALL", null, ["ram:c538bc:8"]]
+ 00c53c80 ["INT_ADD", "register:40f0:8", ["const:c53c80:8", "const:4:8"]]
+ 00c53c80 ["CALL", null, ["ram:c5395c:8"]]
- 00c53be0 bytes 37ffff97
+ 00c53c80 bytes 37ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7dab7d98eb8a77293a07695f7e92a052"></a>

### [`00c53e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53e28.md) → [`00c53ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ec8.md) FUN_00c53ec8

採用 · 移動量 `+0xa0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c53d30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d30.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) · 呼出先 9件 [`00c541a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c541a0.md) [`00c54248`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54248.md) [`00c543c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c543c4.md) [`00c543d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c543d8.md) [`00c54418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54418.md)
- 新版 呼出元 2件 [`00c53dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53dd0.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) · 呼出先 9件 [`00c54240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54240.md) [`00c542e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c542e8.md) [`00c54464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54464.md) [`00c54478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54478.md) [`00c544b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c544b8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.51% / 新版 93.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c53fa0",
      "incomplete_value": true,
      "site": "00c53fa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c53f00",
      "incomplete_value": true,
      "site": "00c53f04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:130:8"
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
      "definition_site": "00c53f88",
      "incomplete_value": false,
      "site": "00c53fa4",
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
            "const:ec4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c53ee8",
      "incomplete_value": false,
      "site": "00c53f04",
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
            "const:f11:8"
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
      "definition_site": "00c53f94",
      "incomplete_value": false,
      "site": "00c53fa4",
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
            "const:522:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c53ef4",
      "incomplete_value": false,
      "site": "00c53f04",
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
            "const:57e:8"
          ]
        ]
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
      "00c53f88",
      "PARAM",
      [
        "storage",
        "002a0f11",
        null,
        "string"
      ]
    ],
    [
      "00c53f8c",
      "READ",
      [
        "storage",
        "00c9bb78",
        null,
        "pointer"
      ]
    ],
    [
      "00c53f94",
      "PARAM",
      [
        "storage",
        "002ad57e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c53f88",
      "PARAM",
      [
        "storage",
        "002a0ec4",
        null,
        "string"
      ]
    ],
    [
      "00c53f8c",
      "READ",
      [
        "storage",
        "00c9bc48",
        null,
        "pointer"
      ]
    ],
    [
      "00c53f94",
      "PARAM",
      [
        "storage",
        "002ad522",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c53f04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53e28.md#insn-00c53f04) · [`00c53e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53e28.md#insn-00c53e50) · [`00c53e58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53e28.md#insn-00c53e58)
- 新版 [`00c53fa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ec8.md#insn-00c53fa4) · [`00c53ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ec8.md#insn-00c53ef0) · [`00c53ef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ec8.md#insn-00c53ef8)

~~~diff
- 00c53f04 ["INT_ADD", "register:40f0:8", ["const:c53f04:8", "const:4:8"]]
- 00c53f04 ["CALL", null, ["callee:00c5f010:8"]]
+ 00c53fa4 ["INT_ADD", "register:40f0:8", ["const:c53fa4:8", "const:4:8"]]
+ 00c53fa4 ["CALL", null, ["callee:00c5f010:8"]]
- 00c53f04 bytes 0f2c0094
+ 00c53fa4 bytes 1b2c0094
- 00c53e50 ["INT_ADD", "register:40f0:8", ["const:c53e50:8", "const:4:8"]]
- 00c53e50 ["CALL", null, ["callee:00c54240:8"]]
+ 00c53ef0 ["INT_ADD", "register:40f0:8", ["const:c53ef0:8", "const:4:8"]]
+ 00c53ef0 ["CALL", null, ["callee:00c54240:8"]]
- 00c53e50 bytes d4000094
+ 00c53ef0 bytes d4000094
- 00c53e58 ["INT_ADD", "register:40f0:8", ["const:c53e58:8", "const:4:8"]]
- 00c53e58 ["CALL", null, ["callee:00c54464:8"]]
+ 00c53ef8 ["INT_ADD", "register:40f0:8", ["const:c53ef8:8", "const:4:8"]]
+ 00c53ef8 ["CALL", null, ["callee:00c54464:8"]]
- 00c53e58 bytes 5b010094
+ 00c53ef8 bytes 5b010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef8e665d820c9a22d6065fa63f78634c"></a>

### [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) → [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) FUN_00c53ffc

採用 · 移動量 `+0xa0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 256件 [`004614b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/004614b0.md) [`00461818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00461/00461818.md) [`00467ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467ffc.md) [`00473540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00473/00473540.md) [`00478148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00478/00478148.md) · 呼出先 7件 [`00c53e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53e28.md) [`00c53fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53fe0.md) [`00c57c48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57c48.md) [`00c5a1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1b0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 256件 [`004614f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/004614f0.md) [`00461858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00461/00461858.md) [`0046803c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/0046803c.md) [`00473580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/00473580.md) [`00478188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00478/00478188.md) · 呼出先 7件 [`00c53ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ec8.md) [`00c54080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54080.md) [`00c57ce8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57ce8.md) [`00c5a280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a280.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 84.85% / 新版 84.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c5406c",
      "incomplete_value": true,
      "site": "00c54070",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c53fcc",
      "incomplete_value": true,
      "site": "00c53fd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:130:8"
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
      "definition_site": "00c54054",
      "incomplete_value": false,
      "site": "00c54070",
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
            "const:ec4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c53fb4",
      "incomplete_value": false,
      "site": "00c53fd0",
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
            "const:f11:8"
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
      "definition_site": "00c54060",
      "incomplete_value": false,
      "site": "00c54070",
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
            "const:669:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c53fc0",
      "incomplete_value": false,
      "site": "00c53fd0",
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
            "const:6bd:8"
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
      "00c54054",
      "PARAM",
      [
        "storage",
        "002a0f11",
        null,
        "string"
      ]
    ],
    [
      "00c54058",
      "READ",
      [
        "storage",
        "00c9bb78",
        null,
        "pointer"
      ]
    ],
    [
      "00c54060",
      "PARAM",
      [
        "storage",
        "002bd6bd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c54054",
      "PARAM",
      [
        "storage",
        "002a0ec4",
        null,
        "string"
      ]
    ],
    [
      "00c54058",
      "READ",
      [
        "storage",
        "00c9bc48",
        null,
        "pointer"
      ]
    ],
    [
      "00c54060",
      "PARAM",
      [
        "storage",
        "002bd669",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c53fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md#insn-00c53fd0) · [`00c53f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md#insn-00c53f78) · [`00c53f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md#insn-00c53f90)
- 新版 [`00c54070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md#insn-00c54070) · [`00c54018`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md#insn-00c54018) · [`00c54030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md#insn-00c54030)

~~~diff
- 00c53fd0 ["INT_ADD", "register:40f0:8", ["const:c53fd0:8", "const:4:8"]]
- 00c53fd0 ["CALL", null, ["callee:00c5f010:8"]]
+ 00c54070 ["INT_ADD", "register:40f0:8", ["const:c54070:8", "const:4:8"]]
+ 00c54070 ["CALL", null, ["callee:00c5f010:8"]]
- 00c53fd0 bytes dc2b0094
+ 00c54070 bytes e82b0094
- 00c53f78 ["INT_ADD", "register:40f0:8", ["const:c53f78:8", "const:4:8"]]
- 00c53f78 ["CALL", null, ["callee:00c57ce8:8"]]
+ 00c54018 ["INT_ADD", "register:40f0:8", ["const:c54018:8", "const:4:8"]]
+ 00c54018 ["CALL", null, ["callee:00c57ce8:8"]]
- 00c53f78 bytes 340f0094
+ 00c54018 bytes 340f0094
- 00c53f90 ["INT_ADD", "register:40f0:8", ["const:c53f90:8", "const:4:8"]]
- 00c53f90 ["CALL", null, ["callee:00c53ec8:8"]]
+ 00c54030 ["INT_ADD", "register:40f0:8", ["const:c54030:8", "const:4:8"]]
+ 00c54030 ["CALL", null, ["callee:00c53ec8:8"]]
- 00c53f90 bytes a6ffff97
+ 00c54030 bytes a6ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f839208a655229e67d4fb04c8c9aaaaf"></a>

### [`00c541a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c541a0.md) → [`00c54240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54240.md) FUN_00c54240

採用 · 移動量 `+0xa0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`00c53d30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d30.md) [`00c53e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53e28.md) [`00c53fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53fe0.md) · 呼出先 2件 [`00c54c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54c68.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 3件 [`00c53dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53dd0.md) [`00c53ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ec8.md) [`00c54080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54080.md) · 呼出先 2件 [`00c54d08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54d08.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c5426c",
      "incomplete_value": false,
      "site": "00c5426c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c541cc",
      "incomplete_value": false,
      "site": "00c541cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:fc0:8"
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
      "definition_site": "00c5426c",
      "incomplete_value": false,
      "site": "00c5426c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c541cc",
      "incomplete_value": false,
      "site": "00c541cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:cf0:8"
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
      "00c5426c",
      "DATA",
      [
        "storage",
        "00c99fc0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c5426c",
      "DATA",
      [
        "storage",
        "01128cf0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c5426c",
      "DATA",
      [
        "storage",
        "00c9a090",
        null,
        "undefined *"
      ]
    ],
    [
      "00c5426c",
      "DATA",
      [
        "storage",
        "01128df0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c541b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c541a0.md#insn-00c541b0) · [`00c541b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c541a0.md#insn-00c541b4) · [`00c541b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c541a0.md#insn-00c541b8)
- 新版 [`00c54250`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54240.md#insn-00c54250) · [`00c54254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54240.md#insn-00c54254)

~~~diff
- 00c541b0 ["COPY", "register:4040:8", ["const:c99000:8"]]
+ 00c54250 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00c541b0 bytes 280200b0
+ 00c54250 bytes 280200d0
- 00c541b4 ["COPY", "tmp:0:8", ["const:fc0:8"]]
- 00c541b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c541b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c541b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c54254 ["COPY", "tmp:0:8", ["const:90:8"]]
+ 00c54254 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c54254 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c54254 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c541b4 bytes 08013f91
+ 00c54254 bytes 08410291
- 00c541b8 ["COPY", "register:4048:8", ["const:1128000:8"]]
- 00c541b8 bytes a9260090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-876cb883d105cfd9d9c8bb99324530d7"></a>

### [`00c545d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c545d0.md) → [`00c54670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54670.md) FUN_00c54670

採用 · 移動量 `+0xa0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00c54440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54440.md) [`00c5775c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c5775c.md) · 呼出先 6件 [`00c56320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c56320.md) [`00c566ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c566ac.md) [`00c5a1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1b0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md) [`00c5ef40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ef40.md)
- 新版 呼出元 2件 [`00c544e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c544e0.md) [`00c577fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c577fc.md) · 呼出先 6件 [`00c563c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c563c0.md) [`00c5674c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c5674c.md) [`00c5a280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a280.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md) [`00c5f010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5f/00c5f010.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.07% / 新版 96.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c54924",
      "incomplete_value": true,
      "site": "00c54928",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c54884",
      "incomplete_value": true,
      "site": "00c54888",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:130:8"
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
      "definition_site": "00c5490c",
      "incomplete_value": false,
      "site": "00c54928",
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
            "const:ec4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c5486c",
      "incomplete_value": false,
      "site": "00c54888",
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
            "const:f11:8"
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
      "definition_site": "00c54918",
      "incomplete_value": false,
      "site": "00c54928",
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
            "const:890:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c54878",
      "incomplete_value": false,
      "site": "00c54888",
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
            "const:85f:8"
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
      "00c546d4",
      "DATA",
      [
        "storage",
        "002bd710",
        null,
        "string"
      ]
    ],
    [
      "00c547b0",
      "DATA",
      [
        "storage",
        "002a3eef",
        null,
        "string"
      ]
    ],
    [
      "00c5490c",
      "PARAM",
      [
        "storage",
        "002a0f11",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c546d4",
      "DATA",
      [
        "storage",
        "002bd6bc",
        null,
        "string"
      ]
    ],
    [
      "00c547b0",
      "DATA",
      [
        "storage",
        "002a3ea2",
        null,
        "string"
      ]
    ],
    [
      "00c5490c",
      "PARAM",
      [
        "storage",
        "002a0ec4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c54888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c545d0.md#insn-00c54888) · [`00c54634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c545d0.md#insn-00c54634) · [`00c54680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c545d0.md#insn-00c54680)
- 新版 [`00c54928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54670.md#insn-00c54928) · [`00c546d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54670.md#insn-00c546d4) · [`00c54720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54670.md#insn-00c54720)

~~~diff
- 00c54888 ["INT_ADD", "register:40f0:8", ["const:c54888:8", "const:4:8"]]
- 00c54888 ["CALL", null, ["callee:00c5f010:8"]]
+ 00c54928 ["INT_ADD", "register:40f0:8", ["const:c54928:8", "const:4:8"]]
+ 00c54928 ["CALL", null, ["callee:00c5f010:8"]]
- 00c54888 bytes ae290094
+ 00c54928 bytes ba290094
- 00c54634 ["COPY", "tmp:0:8", ["const:710:8"]]
- 00c54634 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c54634 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c54634 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c546d4 ["COPY", "tmp:0:8", ["const:6bc:8"]]
+ 00c546d4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c546d4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c546d4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c54634 bytes 00401c91
+ 00c546d4 bytes 00f01a91
- 00c54680 ["INT_ADD", "register:40f0:8", ["const:c54680:8", "const:4:8"]]
- 00c54680 ["CALL", null, ["callee:00c5674c:8"]]
+ 00c54720 ["INT_ADD", "register:40f0:8", ["const:c54720:8", "const:4:8"]]
+ 00c54720 ["CALL", null, ["callee:00c5674c:8"]]
- 00c54680 bytes 0b080094
+ 00c54720 bytes 0b080094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4361fc907cdafb54c5a31b654721359d"></a>

### [`00c548ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c548ec.md) → [`00c5498c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c5498c.md) FUN_00c5498c

採用 · 移動量 `+0xa0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c5a1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1b0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md) [`00c5ef40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ef40.md) [`0112a8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a8f0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c5a280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a280.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md) [`00c5f010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5f/00c5f010.md) [`0112a8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a8f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 91.38% / 新版 91.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c54a60",
      "incomplete_value": true,
      "site": "00c54a64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c549c0",
      "incomplete_value": true,
      "site": "00c549c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:130:8"
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
      "definition_site": "00c54a48",
      "incomplete_value": false,
      "site": "00c54a64",
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
            "const:ec4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c549a8",
      "incomplete_value": false,
      "site": "00c549c4",
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
            "const:f11:8"
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
      "definition_site": "00c54a54",
      "incomplete_value": false,
      "site": "00c54a64",
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
            "const:72e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c549b4",
      "incomplete_value": false,
      "site": "00c549c4",
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
            "const:78a:8"
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
      "00c54a48",
      "PARAM",
      [
        "storage",
        "002a0f11",
        null,
        "string"
      ]
    ],
    [
      "00c54a4c",
      "READ",
      [
        "storage",
        "00c9bb78",
        null,
        "pointer"
      ]
    ],
    [
      "00c54a54",
      "PARAM",
      [
        "storage",
        "002af78a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c54a48",
      "PARAM",
      [
        "storage",
        "002a0ec4",
        null,
        "string"
      ]
    ],
    [
      "00c54a4c",
      "READ",
      [
        "storage",
        "00c9bc48",
        null,
        "pointer"
      ]
    ],
    [
      "00c54a54",
      "PARAM",
      [
        "storage",
        "002af72e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c549c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c548ec.md#insn-00c549c4) · [`00c549a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c548ec.md#insn-00c549a8) · [`00c549ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c548ec.md#insn-00c549ac)
- 新版 [`00c54a64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c5498c.md#insn-00c54a64) · [`00c54a48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c5498c.md#insn-00c54a48) · [`00c54a4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c5498c.md#insn-00c54a4c)

~~~diff
- 00c549c4 ["INT_ADD", "register:40f0:8", ["const:c549c4:8", "const:4:8"]]
- 00c549c4 ["CALL", null, ["callee:00c5f010:8"]]
+ 00c54a64 ["INT_ADD", "register:40f0:8", ["const:c54a64:8", "const:4:8"]]
+ 00c54a64 ["CALL", null, ["callee:00c5f010:8"]]
- 00c549c4 bytes 5f290094
+ 00c54a64 bytes 6b290094
- 00c549a8 ["COPY", "tmp:0:8", ["const:f11:8"]]
- 00c549a8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00c549a8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00c549a8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00c54a48 ["COPY", "tmp:0:8", ["const:ec4:8"]]
+ 00c54a48 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00c54a48 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00c54a48 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00c549a8 bytes 21443c91
+ 00c54a48 bytes 21103b91
- 00c549ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b78:8"]]
- 00c549ac ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c54a4c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c48:8"]]
+ 00c54a4c ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
- 00c549ac bytes 73be45f9
+ 00c54a4c bytes 732646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09279f55ec704683b23514de60547055"></a>

### [`00c549d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c549d4.md) → [`00c54a74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54a74.md) FUN_00c54a74

採用 · 移動量 `+0xa0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c5a1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1b0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md) [`00c5ef40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ef40.md) [`0112a8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a8f0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c5a280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a280.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md) [`00c5f010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5f/00c5f010.md) [`0112a8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a8f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 91.38% / 新版 91.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c54b48",
      "incomplete_value": true,
      "site": "00c54b4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c54aa8",
      "incomplete_value": true,
      "site": "00c54aac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:130:8"
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
      "definition_site": "00c54b30",
      "incomplete_value": false,
      "site": "00c54b4c",
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
            "const:ec4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c54a90",
      "incomplete_value": false,
      "site": "00c54aac",
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
            "const:f11:8"
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
      "definition_site": "00c54b3c",
      "incomplete_value": false,
      "site": "00c54b4c",
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
            "const:e17:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c54a9c",
      "incomplete_value": false,
      "site": "00c54aac",
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
            "const:dd7:8"
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
      "00c54b30",
      "PARAM",
      [
        "storage",
        "002a0f11",
        null,
        "string"
      ]
    ],
    [
      "00c54b34",
      "READ",
      [
        "storage",
        "00c9bb78",
        null,
        "pointer"
      ]
    ],
    [
      "00c54b3c",
      "PARAM",
      [
        "storage",
        "002b5dd7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c54b30",
      "PARAM",
      [
        "storage",
        "002a0ec4",
        null,
        "string"
      ]
    ],
    [
      "00c54b34",
      "READ",
      [
        "storage",
        "00c9bc48",
        null,
        "pointer"
      ]
    ],
    [
      "00c54b3c",
      "PARAM",
      [
        "storage",
        "002b5e17",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c54aac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c549d4.md#insn-00c54aac) · [`00c54a90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c549d4.md#insn-00c54a90) · [`00c54a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c549d4.md#insn-00c54a94)
- 新版 [`00c54b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54a74.md#insn-00c54b4c) · [`00c54b30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54a74.md#insn-00c54b30) · [`00c54b34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54a74.md#insn-00c54b34)

~~~diff
- 00c54aac ["INT_ADD", "register:40f0:8", ["const:c54aac:8", "const:4:8"]]
- 00c54aac ["CALL", null, ["callee:00c5f010:8"]]
+ 00c54b4c ["INT_ADD", "register:40f0:8", ["const:c54b4c:8", "const:4:8"]]
+ 00c54b4c ["CALL", null, ["callee:00c5f010:8"]]
- 00c54aac bytes 25290094
+ 00c54b4c bytes 31290094
- 00c54a90 ["COPY", "tmp:0:8", ["const:f11:8"]]
- 00c54a90 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00c54a90 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00c54a90 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00c54b30 ["COPY", "tmp:0:8", ["const:ec4:8"]]
+ 00c54b30 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00c54b30 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00c54b30 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00c54a90 bytes 21443c91
+ 00c54b30 bytes 21103b91
- 00c54a94 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b78:8"]]
- 00c54a94 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c54b34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c48:8"]]
+ 00c54b34 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
- 00c54a94 bytes 73be45f9
+ 00c54b34 bytes 732646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4184f77d6602f698cb27893d23e64dfc"></a>

### [`00c54c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54c68.md) → [`00c54d08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54d08.md) FUN_00c54d08

採用 · 移動量 `+0xa0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c541a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c541a0.md) · 呼出先 10件 [`00c54440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54440.md) [`00c55464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c55/00c55464.md) [`00c57238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57238.md) [`00c5750c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c5750c.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)
- 新版 呼出元 1件 [`00c54240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54240.md) · 呼出先 10件 [`00c544e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c544e0.md) [`00c55504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c55/00c55504.md) [`00c572d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c572d8.md) [`00c575ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c575ac.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.50% / 新版 96.50%

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
      "definition_site": "00c54d58",
      "incomplete_value": false,
      "site": "00c54d68",
      "value": [
        "leaf",
        "const:c575ac:8"
      ]
    },
    "old": {
      "definition_site": "00c54cb8",
      "incomplete_value": false,
      "site": "00c54cc8",
      "value": [
        "leaf",
        "const:c5750c:8"
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c54d94",
      "incomplete_value": false,
      "site": "00c54d98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:df4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c54cf4",
      "incomplete_value": false,
      "site": "00c54cf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:cf4:8"
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
      "definition_site": "00c54ddc",
      "incomplete_value": false,
      "site": "00c54de0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:df4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c54d3c",
      "incomplete_value": false,
      "site": "00c54d40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:cf4:8"
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
      "00c54d58",
      "PARAM",
      [
        "storage",
        "00c5750c",
        null,
        null
      ]
    ],
    [
      "00c54d94",
      "PARAM",
      [
        "storage",
        "01128cf4",
        null,
        null
      ]
    ],
    [
      "00c54da4",
      "READ",
      [
        "storage",
        "00ca48a8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c54d58",
      "PARAM",
      [
        "storage",
        "00c575ac",
        null,
        null
      ]
    ],
    [
      "00c54d94",
      "PARAM",
      [
        "storage",
        "01128df4",
        null,
        null
      ]
    ],
    [
      "00c54da4",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c54cc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54c68.md#insn-00c54cc8) · [`00c54cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54c68.md#insn-00c54cf8) · [`00c54d3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54c68.md#insn-00c54d3c)
- 新版 [`00c54d68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54d08.md#insn-00c54d68) · [`00c54d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54d08.md#insn-00c54d98) · [`00c54ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54d08.md#insn-00c54ddc)

~~~diff
- 00c54cc8 ["INT_ADD", "register:40f0:8", ["const:c54cc8:8", "const:4:8"]]
- 00c54cc8 ["CALL", null, ["callee:00c5f040:8"]]
+ 00c54d68 ["INT_ADD", "register:40f0:8", ["const:c54d68:8", "const:4:8"]]
+ 00c54d68 ["CALL", null, ["callee:00c5f040:8"]]
- 00c54cc8 bytes aa280094
+ 00c54d68 bytes b6280094
- 00c54cf8 ["INT_ADD", "register:40f0:8", ["const:c54cf8:8", "const:4:8"]]
- 00c54cf8 ["CALL", null, ["callee:00c5f050:8"]]
+ 00c54d98 ["INT_ADD", "register:40f0:8", ["const:c54d98:8", "const:4:8"]]
+ 00c54d98 ["CALL", null, ["callee:00c5f050:8"]]
- 00c54cf8 bytes a2280094
+ 00c54d98 bytes ae280094
- 00c54d3c ["COPY", "tmp:0:8", ["const:cf4:8"]]
- 00c54d3c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c54d3c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c54d3c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c54ddc ["COPY", "tmp:0:8", ["const:df4:8"]]
+ 00c54ddc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c54ddc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c54ddc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c54d3c bytes 00d03391
+ 00c54ddc bytes 00d03791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ace84f2e248afe4c70358c1a4bfea074"></a>

### [`00c54fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54fd0.md) → [`00c55070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c55/00c55070.md) FUN_00c55070

採用 · 移動量 `+0xa0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c54af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54af0.md) · 呼出先 11件 [`00c54440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54440.md) [`00c55464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c55/00c55464.md) [`00c55fdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c55/00c55fdc.md) [`00c56110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c56110.md) [`00c56874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c56874.md)
- 新版 呼出元 1件 [`00c54b90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54b90.md) · 呼出先 11件 [`00c544e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c544e0.md) [`00c55504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c55/00c55504.md) [`00c5607c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c5607c.md) [`00c561b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c561b0.md) [`00c56914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c56914.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.88% / 新版 94.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c55488",
      "incomplete_value": true,
      "site": "00c5548c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c553e8",
      "incomplete_value": true,
      "site": "00c553ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:130:8"
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
      "definition_site": "00c55470",
      "incomplete_value": false,
      "site": "00c5548c",
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
            "const:ec4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c553d0",
      "incomplete_value": false,
      "site": "00c553ec",
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
            "const:f11:8"
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
      "definition_site": "00c5547c",
      "incomplete_value": false,
      "site": "00c5548c",
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
            "const:d5b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c553dc",
      "incomplete_value": false,
      "site": "00c553ec",
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
            "const:da8:8"
          ]
        ]
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
      "00c55470",
      "PARAM",
      [
        "storage",
        "002a0f11",
        null,
        "string"
      ]
    ],
    [
      "00c55474",
      "READ",
      [
        "storage",
        "00c9bb78",
        null,
        "pointer"
      ]
    ],
    [
      "00c5547c",
      "PARAM",
      [
        "storage",
        "002a1da8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c55470",
      "PARAM",
      [
        "storage",
        "002a0ec4",
        null,
        "string"
      ]
    ],
    [
      "00c55474",
      "READ",
      [
        "storage",
        "00c9bc48",
        null,
        "pointer"
      ]
    ],
    [
      "00c5547c",
      "PARAM",
      [
        "storage",
        "002a1d5b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c553b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54fd0.md#insn-00c553b4) · [`00c553ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54fd0.md#insn-00c553ec) · [`00c55420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54fd0.md#insn-00c55420)
- 新版 [`00c55454`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c55/00c55070.md#insn-00c55454) · [`00c5548c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c55/00c55070.md#insn-00c5548c) · [`00c554c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c55/00c55070.md#insn-00c554c0)

~~~diff
- 00c553b4 ["INT_ADD", "register:40f0:8", ["const:c553b4:8", "const:4:8"]]
- 00c553b4 ["CALL", null, ["callee:00c580d0:8"]]
+ 00c55454 ["INT_ADD", "register:40f0:8", ["const:c55454:8", "const:4:8"]]
+ 00c55454 ["CALL", null, ["callee:00c580d0:8"]]
- 00c553b4 bytes 130b0094
+ 00c55454 bytes 1f0b0094
- 00c553ec ["INT_ADD", "register:40f0:8", ["const:c553ec:8", "const:4:8"]]
- 00c553ec ["CALL", null, ["callee:00c5f010:8"]]
+ 00c5548c ["INT_ADD", "register:40f0:8", ["const:c5548c:8", "const:4:8"]]
+ 00c5548c ["CALL", null, ["callee:00c5f010:8"]]
- 00c553ec bytes d5260094
+ 00c5548c bytes e1260094
- 00c55420 ["INT_ADD", "register:40f0:8", ["const:c55420:8", "const:4:8"]]
- 00c55420 ["CALL", null, ["callee:00c5f010:8"]]
+ 00c554c0 ["INT_ADD", "register:40f0:8", ["const:c554c0:8", "const:4:8"]]
+ 00c554c0 ["CALL", null, ["callee:00c5f010:8"]]
- 00c55420 bytes c8260094
+ 00c554c0 bytes d4260094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73b2be96dedf0de2a8050fcd84766c5d"></a>

### [`00c55464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c55/00c55464.md) → [`00c55504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c55/00c55504.md) FUN_00c55504

採用 · 移動量 `+0xa0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00c54c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54c68.md) [`00c54fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54fd0.md) [`00c57238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57238.md) · 呼出先 8件 [`00c56320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c56320.md) [`00c566ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c566ac.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1b0.md) [`00c5a220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a220.md)
- 新版 呼出元 3件 [`00c54d08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54d08.md) [`00c55070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c55/00c55070.md) [`00c572d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c572d8.md) · 呼出先 8件 [`00c563c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c563c0.md) [`00c5674c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c5674c.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a280.md) [`00c5a2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a2f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.10% / 新版 92.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 18件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c55ee4",
      "incomplete_value": true,
      "site": "00c55ee8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c55e44",
      "incomplete_value": true,
      "site": "00c55e48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:130:8"
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
      "definition_site": "00c55ed8",
      "incomplete_value": false,
      "site": "00c55ee8",
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
            "const:e3c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c55e38",
      "incomplete_value": false,
      "site": "00c55e48",
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
            "const:e89:8"
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
      "definition_site": "00c55f7c",
      "incomplete_value": true,
      "site": "00c55f80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c55edc",
      "incomplete_value": true,
      "site": "00c55ee0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:130:8"
          ]
        ]
      ]
    },
    "ordinal": 28,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c555dc",
      "DATA",
      [
        "storage",
        "00313e10",
        "switchD_00c55544::switchdataD_00313e10",
        "ushort"
      ]
    ],
    [
      "00c55e00",
      "PARAM",
      [
        "storage",
        "002bc359",
        null,
        "string"
      ]
    ],
    [
      "00c55e10",
      "PARAM",
      [
        "storage",
        "002b7ec7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c555dc",
      "DATA",
      [
        "storage",
        "00313e50",
        "switchD_00c555e4::switchdataD_00313e50",
        "ushort"
      ]
    ],
    [
      "00c55e00",
      "PARAM",
      [
        "storage",
        "002bc305",
        null,
        "string"
      ]
    ],
    [
      "00c55e10",
      "PARAM",
      [
        "storage",
        "002b7f07",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c55da8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c55/00c55464.md#insn-00c55da8) · [`00c55e48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c55/00c55464.md#insn-00c55e48) · [`00c55e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c55/00c55464.md#insn-00c55e90)
- 新版 [`00c55e48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c55/00c55504.md#insn-00c55e48) · [`00c55ee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c55/00c55504.md#insn-00c55ee8) · [`00c55f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c55/00c55504.md#insn-00c55f30)

~~~diff
- 00c55da8 ["COPY", "tmp:0:8", ["const:fe0:8"]]
- 00c55da8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c55da8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c55da8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c55e48 ["COPY", "tmp:0:8", ["const:20:8"]]
+ 00c55e48 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c55e48 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c55e48 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c55da8 bytes 00803f91
+ 00c55e48 bytes 00800091
- 00c55e48 ["INT_ADD", "register:40f0:8", ["const:c55e48:8", "const:4:8"]]
- 00c55e48 ["CALL", null, ["callee:00c5f010:8"]]
+ 00c55ee8 ["INT_ADD", "register:40f0:8", ["const:c55ee8:8", "const:4:8"]]
+ 00c55ee8 ["CALL", null, ["callee:00c5f010:8"]]
- 00c55e48 bytes 3e240094
+ 00c55ee8 bytes 4a240094
- 00c55e90 ["COPY", "tmp:0:8", ["const:912:8"]]
- 00c55e90 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00c55e90 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00c55e90 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c55f30 ["COPY", "tmp:0:8", ["const:8b6:8"]]
+ 00c55f30 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c55f30 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c55f30 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00c55e90 bytes 00482491
+ 00c55f30 bytes 00d82291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0879e6ebd67f680fe17ca05d0f3dba1d"></a>

### [`00c55fdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c55/00c55fdc.md) → [`00c5607c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c5607c.md) FUN_00c5607c

採用 · 移動量 `+0xa0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c54fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54fd0.md) · 呼出先 5件 [`00c56874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c56874.md) [`00c5a1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1b0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md) [`00c5ef40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ef40.md) [`0112a8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a8f0.md)
- 新版 呼出元 1件 [`00c55070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c55/00c55070.md) · 呼出先 5件 [`00c56914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c56914.md) [`00c5a280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a280.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md) [`00c5f010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5f/00c5f010.md) [`0112a8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a8f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.51% / 新版 93.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c5619c",
      "incomplete_value": true,
      "site": "00c561a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c560fc",
      "incomplete_value": true,
      "site": "00c56100",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:130:8"
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
      "definition_site": "00c56184",
      "incomplete_value": false,
      "site": "00c561a0",
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
            "const:ec4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c560e4",
      "incomplete_value": false,
      "site": "00c56100",
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
            "const:f11:8"
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
      "definition_site": "00c56190",
      "incomplete_value": false,
      "site": "00c561a0",
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
            "const:72e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c560f0",
      "incomplete_value": false,
      "site": "00c56100",
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
            "const:78a:8"
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
      "00c56184",
      "PARAM",
      [
        "storage",
        "002a0f11",
        null,
        "string"
      ]
    ],
    [
      "00c56188",
      "READ",
      [
        "storage",
        "00c9bb78",
        null,
        "pointer"
      ]
    ],
    [
      "00c56190",
      "PARAM",
      [
        "storage",
        "002af78a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c56184",
      "PARAM",
      [
        "storage",
        "002a0ec4",
        null,
        "string"
      ]
    ],
    [
      "00c56188",
      "READ",
      [
        "storage",
        "00c9bc48",
        null,
        "pointer"
      ]
    ],
    [
      "00c56190",
      "PARAM",
      [
        "storage",
        "002af72e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c56100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c55/00c55fdc.md#insn-00c56100) · [`00c560e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c55/00c55fdc.md#insn-00c560e4) · [`00c560e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c55/00c55fdc.md#insn-00c560e8)
- 新版 [`00c561a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c5607c.md#insn-00c561a0) · [`00c56184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c5607c.md#insn-00c56184) · [`00c56188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c5607c.md#insn-00c56188)

~~~diff
- 00c56100 ["INT_ADD", "register:40f0:8", ["const:c56100:8", "const:4:8"]]
- 00c56100 ["CALL", null, ["callee:00c5f010:8"]]
+ 00c561a0 ["INT_ADD", "register:40f0:8", ["const:c561a0:8", "const:4:8"]]
+ 00c561a0 ["CALL", null, ["callee:00c5f010:8"]]
- 00c56100 bytes 90230094
+ 00c561a0 bytes 9c230094
- 00c560e4 ["COPY", "tmp:0:8", ["const:f11:8"]]
- 00c560e4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00c560e4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00c560e4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00c56184 ["COPY", "tmp:0:8", ["const:ec4:8"]]
+ 00c56184 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00c56184 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00c56184 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00c560e4 bytes 21443c91
+ 00c56184 bytes 21103b91
- 00c560e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b78:8"]]
- 00c560e8 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c56188 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c48:8"]]
+ 00c56188 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
- 00c560e8 bytes 73be45f9
+ 00c56188 bytes 732646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f4ec365f74081fcce1e6d45b16c9e7d"></a>

### [`00c56110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c56110.md) → [`00c561b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c561b0.md) FUN_00c561b0

採用 · 移動量 `+0xa0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c54fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54fd0.md) · 呼出先 5件 [`00c56874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c56874.md) [`00c5a1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1b0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md) [`00c5ef40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ef40.md) [`0112a8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a8f0.md)
- 新版 呼出元 1件 [`00c55070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c55/00c55070.md) · 呼出先 5件 [`00c56914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c56914.md) [`00c5a280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a280.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md) [`00c5f010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5f/00c5f010.md) [`0112a8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a8f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.42% / 新版 92.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c56378",
      "incomplete_value": true,
      "site": "00c5637c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c562d8",
      "incomplete_value": true,
      "site": "00c562dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:130:8"
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
      "definition_site": "00c56360",
      "incomplete_value": false,
      "site": "00c5637c",
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
            "const:ec4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c562c0",
      "incomplete_value": false,
      "site": "00c562dc",
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
            "const:f11:8"
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
      "definition_site": "00c5636c",
      "incomplete_value": false,
      "site": "00c5637c",
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
            "const:5eb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c562cc",
      "incomplete_value": false,
      "site": "00c562dc",
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
            "const:647:8"
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
      "00c56360",
      "PARAM",
      [
        "storage",
        "002a0f11",
        null,
        "string"
      ]
    ],
    [
      "00c56364",
      "READ",
      [
        "storage",
        "00c9bb78",
        null,
        "pointer"
      ]
    ],
    [
      "00c5636c",
      "PARAM",
      [
        "storage",
        "002ae647",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c56360",
      "PARAM",
      [
        "storage",
        "002a0ec4",
        null,
        "string"
      ]
    ],
    [
      "00c56364",
      "READ",
      [
        "storage",
        "00c9bc48",
        null,
        "pointer"
      ]
    ],
    [
      "00c5636c",
      "PARAM",
      [
        "storage",
        "002ae5eb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c562dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c56110.md#insn-00c562dc) · [`00c56310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c56110.md#insn-00c56310) · [`00c561a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c56110.md#insn-00c561a0)
- 新版 [`00c5637c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c561b0.md#insn-00c5637c) · [`00c563b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c561b0.md#insn-00c563b0) · [`00c56240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c561b0.md#insn-00c56240)

~~~diff
- 00c562dc ["INT_ADD", "register:40f0:8", ["const:c562dc:8", "const:4:8"]]
- 00c562dc ["CALL", null, ["callee:00c5f010:8"]]
+ 00c5637c ["INT_ADD", "register:40f0:8", ["const:c5637c:8", "const:4:8"]]
+ 00c5637c ["CALL", null, ["callee:00c5f010:8"]]
- 00c562dc bytes 19230094
+ 00c5637c bytes 25230094
- 00c56310 ["INT_ADD", "register:40f0:8", ["const:c56310:8", "const:4:8"]]
- 00c56310 ["CALL", null, ["callee:00c5f010:8"]]
+ 00c563b0 ["INT_ADD", "register:40f0:8", ["const:c563b0:8", "const:4:8"]]
+ 00c563b0 ["CALL", null, ["callee:00c5f010:8"]]
- 00c56310 bytes 0c230094
+ 00c563b0 bytes 18230094
- 00c561a0 ["INT_ADD", "register:40f0:8", ["const:c561a0:8", "const:4:8"]]
- 00c561a0 ["CALL", null, ["callee:00c56914:8"]]
+ 00c56240 ["INT_ADD", "register:40f0:8", ["const:c56240:8", "const:4:8"]]
+ 00c56240 ["CALL", null, ["callee:00c56914:8"]]
- 00c561a0 bytes b5010094
+ 00c56240 bytes b5010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81b179d6508e7478685b1ee4f41003ae"></a>

### [`00c56320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c56320.md) → [`00c563c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c563c0.md) FUN_00c563c0

採用 · 移動量 `+0xa0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`00c54440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54440.md) [`00c545d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c545d0.md) [`00c55464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c55/00c55464.md) [`00c5763c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c5763c.md) [`00c5775c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c5775c.md) · 呼出先 5件 [`00c566ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c566ac.md) [`00c5a1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1b0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md) [`00c5ef40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ef40.md) [`0112a8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a8f0.md)
- 新版 呼出元 6件 [`00c544e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c544e0.md) [`00c54670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54670.md) [`00c55504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c55/00c55504.md) [`00c576dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c576dc.md) [`00c577fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c577fc.md) · 呼出先 5件 [`00c5674c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c5674c.md) [`00c5a280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a280.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md) [`00c5f010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5f/00c5f010.md) [`0112a8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a8f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 84.58% / 新版 84.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 28件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c565e8",
      "incomplete_value": true,
      "site": "00c565ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c56548",
      "incomplete_value": true,
      "site": "00c5654c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:130:8"
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
      "definition_site": "00c565d0",
      "incomplete_value": false,
      "site": "00c565ec",
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
            "const:ec4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c56530",
      "incomplete_value": false,
      "site": "00c5654c",
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
            "const:f11:8"
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
      "definition_site": "00c565dc",
      "incomplete_value": false,
      "site": "00c565ec",
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
            "const:890:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c5653c",
      "incomplete_value": false,
      "site": "00c5654c",
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
            "const:85f:8"
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
      "00c565d0",
      "PARAM",
      [
        "storage",
        "002a0f11",
        null,
        "string"
      ]
    ],
    [
      "00c565d4",
      "READ",
      [
        "storage",
        "00c9bb78",
        null,
        "pointer"
      ]
    ],
    [
      "00c565dc",
      "PARAM",
      [
        "storage",
        "002b385f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c565d0",
      "PARAM",
      [
        "storage",
        "002a0ec4",
        null,
        "string"
      ]
    ],
    [
      "00c565d4",
      "READ",
      [
        "storage",
        "00c9bc48",
        null,
        "pointer"
      ]
    ],
    [
      "00c565dc",
      "PARAM",
      [
        "storage",
        "002b3890",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c5654c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c56320.md#insn-00c5654c) · [`00c56590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c56320.md#insn-00c56590) · [`00c565cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c56320.md#insn-00c565cc)
- 新版 [`00c565ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c563c0.md#insn-00c565ec) · [`00c56630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c563c0.md#insn-00c56630) · [`00c5666c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c563c0.md#insn-00c5666c)

~~~diff
- 00c5654c ["INT_ADD", "register:40f0:8", ["const:c5654c:8", "const:4:8"]]
- 00c5654c ["CALL", null, ["callee:00c5f010:8"]]
+ 00c565ec ["INT_ADD", "register:40f0:8", ["const:c565ec:8", "const:4:8"]]
+ 00c565ec ["CALL", null, ["callee:00c5f010:8"]]
- 00c5654c bytes 7d220094
+ 00c565ec bytes 89220094
- 00c56590 ["INT_ADD", "register:40f0:8", ["const:c56590:8", "const:4:8"]]
- 00c56590 ["CALL", null, ["callee:00c5f010:8"]]
+ 00c56630 ["INT_ADD", "register:40f0:8", ["const:c56630:8", "const:4:8"]]
+ 00c56630 ["CALL", null, ["callee:00c5f010:8"]]
- 00c56590 bytes 6c220094
+ 00c56630 bytes 78220094
- 00c565cc ["INT_ADD", "register:40f0:8", ["const:c565cc:8", "const:4:8"]]
- 00c565cc ["CALL", null, ["callee:00c5f010:8"]]
+ 00c5666c ["INT_ADD", "register:40f0:8", ["const:c5666c:8", "const:4:8"]]
+ 00c5666c ["CALL", null, ["callee:00c5f010:8"]]
- 00c565cc bytes 5d220094
+ 00c5666c bytes 69220094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f8f118574411fae16de4e9d236b25bf"></a>

### [`00c566ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c566ac.md) → [`00c5674c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c5674c.md) FUN_00c5674c

採用 · 移動量 `+0xa0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`00c54440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54440.md) [`00c545d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c545d0.md) [`00c55464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c55/00c55464.md) [`00c56320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c56320.md) [`00c56874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c56874.md) · 呼出先 4件 [`00c5a1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1b0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md) [`00c5ef40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ef40.md) [`0112a8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a8f0.md)
- 新版 呼出元 6件 [`00c544e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c544e0.md) [`00c54670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54670.md) [`00c55504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c55/00c55504.md) [`00c563c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c563c0.md) [`00c56914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c56914.md) · 呼出先 4件 [`00c5a280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a280.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md) [`00c5f010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5f/00c5f010.md) [`0112a8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a8f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 91.23% / 新版 91.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c568cc",
      "incomplete_value": true,
      "site": "00c568d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c5682c",
      "incomplete_value": true,
      "site": "00c56830",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:130:8"
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
      "definition_site": "00c568b4",
      "incomplete_value": false,
      "site": "00c568d0",
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
            "const:ec4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c56814",
      "incomplete_value": false,
      "site": "00c56830",
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
            "const:f11:8"
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
      "definition_site": "00c568c0",
      "incomplete_value": false,
      "site": "00c568d0",
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
            "const:37d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c56820",
      "incomplete_value": false,
      "site": "00c56830",
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
            "const:3d9:8"
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
      "00c568b4",
      "PARAM",
      [
        "storage",
        "002a0f11",
        null,
        "string"
      ]
    ],
    [
      "00c568b8",
      "READ",
      [
        "storage",
        "00c9bb78",
        null,
        "pointer"
      ]
    ],
    [
      "00c568c0",
      "PARAM",
      [
        "storage",
        "002a63d9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c568b4",
      "PARAM",
      [
        "storage",
        "002a0ec4",
        null,
        "string"
      ]
    ],
    [
      "00c568b8",
      "READ",
      [
        "storage",
        "00c9bc48",
        null,
        "pointer"
      ]
    ],
    [
      "00c568c0",
      "PARAM",
      [
        "storage",
        "002a637d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c56830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c566ac.md#insn-00c56830) · [`00c56864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c566ac.md#insn-00c56864) · [`00c56814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c566ac.md#insn-00c56814)
- 新版 [`00c568d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c5674c.md#insn-00c568d0) · [`00c56904`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c5674c.md#insn-00c56904) · [`00c568b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c5674c.md#insn-00c568b4)

~~~diff
- 00c56830 ["INT_ADD", "register:40f0:8", ["const:c56830:8", "const:4:8"]]
- 00c56830 ["CALL", null, ["callee:00c5f010:8"]]
+ 00c568d0 ["INT_ADD", "register:40f0:8", ["const:c568d0:8", "const:4:8"]]
+ 00c568d0 ["CALL", null, ["callee:00c5f010:8"]]
- 00c56830 bytes c4210094
+ 00c568d0 bytes d0210094
- 00c56864 ["INT_ADD", "register:40f0:8", ["const:c56864:8", "const:4:8"]]
- 00c56864 ["CALL", null, ["callee:00c5f010:8"]]
+ 00c56904 ["INT_ADD", "register:40f0:8", ["const:c56904:8", "const:4:8"]]
+ 00c56904 ["CALL", null, ["callee:00c5f010:8"]]
- 00c56864 bytes b7210094
+ 00c56904 bytes c3210094
- 00c56814 ["COPY", "tmp:0:8", ["const:f11:8"]]
- 00c56814 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00c56814 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00c56814 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00c568b4 ["COPY", "tmp:0:8", ["const:ec4:8"]]
+ 00c568b4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00c568b4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00c568b4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00c56814 bytes 21443c91
+ 00c568b4 bytes 21103b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47ce0e5b190f92c49ff19d5c91d6d32b"></a>

### [`00c56874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c56874.md) → [`00c56914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c56914.md) FUN_00c56914

採用 · 移動量 `+0xa0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00c54fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54fd0.md) [`00c55fdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c55/00c55fdc.md) [`00c56110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c56110.md) · 呼出先 5件 [`00c566ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c566ac.md) [`00c5a1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1b0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md) [`00c5ef40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ef40.md) [`0112a8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a8f0.md)
- 新版 呼出元 3件 [`00c55070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c55/00c55070.md) [`00c5607c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c5607c.md) [`00c561b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c561b0.md) · 呼出先 5件 [`00c5674c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c5674c.md) [`00c5a280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a280.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md) [`00c5f010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5f/00c5f010.md) [`0112a8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a8f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 91.84% / 新版 91.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 40件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c570e4",
      "incomplete_value": true,
      "site": "00c570e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c57044",
      "incomplete_value": true,
      "site": "00c57048",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:130:8"
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
      "definition_site": "00c570cc",
      "incomplete_value": false,
      "site": "00c570e8",
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
            "const:ec4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c5702c",
      "incomplete_value": false,
      "site": "00c57048",
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
            "const:f11:8"
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
      "definition_site": "00c570d8",
      "incomplete_value": false,
      "site": "00c570e8",
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
            "const:890:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c57038",
      "incomplete_value": false,
      "site": "00c57048",
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
            "const:85f:8"
          ]
        ]
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
      "00c569c0",
      "DATA",
      [
        "storage",
        "00313e70",
        "switchD_00c56928::switchdataD_00313e70",
        "ushort"
      ]
    ],
    [
      "00c570cc",
      "PARAM",
      [
        "storage",
        "002a0f11",
        null,
        "string"
      ]
    ],
    [
      "00c570d0",
      "READ",
      [
        "storage",
        "00c9bb78",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c569c0",
      "DATA",
      [
        "storage",
        "00313eb0",
        "switchD_00c569c8::switchdataD_00313eb0",
        "ushort"
      ]
    ],
    [
      "00c570cc",
      "PARAM",
      [
        "storage",
        "002a0ec4",
        null,
        "string"
      ]
    ],
    [
      "00c570d0",
      "READ",
      [
        "storage",
        "00c9bc48",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c57048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c56874.md#insn-00c57048) · [`00c5707c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c56874.md#insn-00c5707c) · [`00c570b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c56874.md#insn-00c570b0)
- 新版 [`00c570e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c56914.md#insn-00c570e8) · [`00c5711c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c56914.md#insn-00c5711c) · [`00c57150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c56914.md#insn-00c57150)

~~~diff
- 00c57048 ["INT_ADD", "register:40f0:8", ["const:c57048:8", "const:4:8"]]
- 00c57048 ["CALL", null, ["callee:00c5f010:8"]]
+ 00c570e8 ["INT_ADD", "register:40f0:8", ["const:c570e8:8", "const:4:8"]]
+ 00c570e8 ["CALL", null, ["callee:00c5f010:8"]]
- 00c57048 bytes be1f0094
+ 00c570e8 bytes ca1f0094
- 00c5707c ["INT_ADD", "register:40f0:8", ["const:c5707c:8", "const:4:8"]]
- 00c5707c ["CALL", null, ["callee:00c5f010:8"]]
+ 00c5711c ["INT_ADD", "register:40f0:8", ["const:c5711c:8", "const:4:8"]]
+ 00c5711c ["CALL", null, ["callee:00c5f010:8"]]
- 00c5707c bytes b11f0094
+ 00c5711c bytes bd1f0094
- 00c570b0 ["INT_ADD", "register:40f0:8", ["const:c570b0:8", "const:4:8"]]
- 00c570b0 ["CALL", null, ["callee:00c5f010:8"]]
+ 00c57150 ["INT_ADD", "register:40f0:8", ["const:c57150:8", "const:4:8"]]
+ 00c57150 ["CALL", null, ["callee:00c5f010:8"]]
- 00c570b0 bytes a41f0094
+ 00c57150 bytes b01f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6bbfcf653ec649ebc11a900b50664d19"></a>

### [`00c57238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57238.md) → [`00c572d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c572d8.md) FUN_00c572d8

採用 · 移動量 `+0xa0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c54c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c54/00c54c68.md) · 呼出先 10件 [`00c55464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c55/00c55464.md) [`00c5775c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c5775c.md) [`00c57924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57924.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)
- 新版 呼出元 1件 [`00c54d08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c54/00c54d08.md) · 呼出先 10件 [`00c55504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c55/00c55504.md) [`00c577fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c577fc.md) [`00c579c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c579c4.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 89.50% / 新版 89.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 3件, `call_argument_candidate` 5件, `store_destination` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c57550",
      "incomplete_value": true,
      "site": "00c57550",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d8:8"
          ],
          [
            "leaf",
            "const:978:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c574b0",
      "incomplete_value": true,
      "site": "00c574b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d8:8"
          ],
          [
            "leaf",
            "const:8a8:8"
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c57554",
      "incomplete_value": true,
      "site": "00c57554",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:988:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c574b4",
      "incomplete_value": true,
      "site": "00c574b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:8b8:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c57574",
      "incomplete_value": true,
      "site": "00c57574",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c8:8"
          ],
          [
            "leaf",
            "const:980:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c574d4",
      "incomplete_value": true,
      "site": "00c574d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c8:8"
          ],
          [
            "leaf",
            "const:8b0:8"
          ]
        ]
      ]
    },
    "ordinal": 28,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c5735c",
      "PARAM",
      [
        "storage",
        "01128cf4",
        null,
        null
      ]
    ],
    [
      "00c5736c",
      "READ",
      [
        "storage",
        "00ca48a8",
        null,
        "pointer"
      ]
    ],
    [
      "00c57370",
      "READ",
      [
        "storage",
        "00ca48b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c5735c",
      "PARAM",
      [
        "storage",
        "01128df4",
        null,
        null
      ]
    ],
    [
      "00c5736c",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "pointer"
      ]
    ],
    [
      "00c57370",
      "READ",
      [
        "storage",
        "00ca4980",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c572ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57238.md#insn-00c572ac) · [`00c572c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57238.md#insn-00c572c0) · [`00c5734c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57238.md#insn-00c5734c)
- 新版 [`00c5734c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c572d8.md#insn-00c5734c) · [`00c57360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c572d8.md#insn-00c57360) · [`00c573ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c572d8.md#insn-00c573ec)

~~~diff
- 00c572ac ["INT_ADD", "register:40f0:8", ["const:c572ac:8", "const:4:8"]]
- 00c572ac ["CALL", null, ["callee:00c579c4:8"]]
+ 00c5734c ["INT_ADD", "register:40f0:8", ["const:c5734c:8", "const:4:8"]]
+ 00c5734c ["CALL", null, ["callee:00c579c4:8"]]
- 00c572ac bytes 9e010094
+ 00c5734c bytes 9e010094
- 00c572c0 ["INT_ADD", "register:40f0:8", ["const:c572c0:8", "const:4:8"]]
- 00c572c0 ["CALL", null, ["callee:00c5f050:8"]]
+ 00c57360 ["INT_ADD", "register:40f0:8", ["const:c57360:8", "const:4:8"]]
+ 00c57360 ["CALL", null, ["callee:00c5f050:8"]]
- 00c572c0 bytes 301f0094
+ 00c57360 bytes 3c1f0094
- 00c5734c ["INT_ADD", "register:40f0:8", ["const:c5734c:8", "const:4:8"]]
- 00c5734c ["CALL", null, ["callee:00c5f030:8"]]
+ 00c573ec ["INT_ADD", "register:40f0:8", ["const:c573ec:8", "const:4:8"]]
+ 00c573ec ["CALL", null, ["callee:00c5f030:8"]]
- 00c5734c bytes 051f0094
+ 00c573ec bytes 111f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99bfc66fe50b55ce719fe0ca3b305afd"></a>

### [`00c5763c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c5763c.md) → [`00c576dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c576dc.md) FUN_00c576dc

採用 · 移動量 `+0xa0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00c5750c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c5750c.md) [`00c57924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57924.md) · 呼出先 4件 [`00c56320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c56/00c56320.md) [`00c5a1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1b0.md) [`00c5ef40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ef40.md) [`0112a8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a8f0.md)
- 新版 呼出元 2件 [`00c575ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c575ac.md) [`00c579c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c579c4.md) · 呼出先 4件 [`00c563c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c56/00c563c0.md) [`00c5a280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a280.md) [`00c5f010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5f/00c5f010.md) [`0112a8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a8f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c57724",
      "incomplete_value": true,
      "site": "00c57728",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c57684",
      "incomplete_value": true,
      "site": "00c57688",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:130:8"
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
      "definition_site": "00c57718",
      "incomplete_value": false,
      "site": "00c57728",
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
            "const:b62:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c57678",
      "incomplete_value": false,
      "site": "00c57688",
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
            "const:b31:8"
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
      "definition_site": "00c577a8",
      "incomplete_value": true,
      "site": "00c577ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c57708",
      "incomplete_value": true,
      "site": "00c5770c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:130:8"
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
      "00c57718",
      "PARAM",
      [
        "storage",
        "002b4b31",
        null,
        "string"
      ]
    ],
    [
      "00c5771c",
      "READ",
      [
        "storage",
        "00c9bb78",
        null,
        "pointer"
      ]
    ],
    [
      "00c57798",
      "PARAM",
      [
        "storage",
        "002a8a15",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c57718",
      "PARAM",
      [
        "storage",
        "002b4b62",
        null,
        "string"
      ]
    ],
    [
      "00c5771c",
      "READ",
      [
        "storage",
        "00c9bc48",
        null,
        "pointer"
      ]
    ],
    [
      "00c57798",
      "PARAM",
      [
        "storage",
        "002a89b9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c57688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c5763c.md#insn-00c57688) · [`00c5770c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c5763c.md#insn-00c5770c) · [`00c57678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c5763c.md#insn-00c57678)
- 新版 [`00c57728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c576dc.md#insn-00c57728) · [`00c577ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c576dc.md#insn-00c577ac) · [`00c57718`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c576dc.md#insn-00c57718)

~~~diff
- 00c57688 ["INT_ADD", "register:40f0:8", ["const:c57688:8", "const:4:8"]]
- 00c57688 ["CALL", null, ["callee:00c5f010:8"]]
+ 00c57728 ["INT_ADD", "register:40f0:8", ["const:c57728:8", "const:4:8"]]
+ 00c57728 ["CALL", null, ["callee:00c5f010:8"]]
- 00c57688 bytes 2e1e0094
+ 00c57728 bytes 3a1e0094
- 00c5770c ["INT_ADD", "register:40f0:8", ["const:c5770c:8", "const:4:8"]]
- 00c5770c ["CALL", null, ["callee:00c5f010:8"]]
+ 00c577ac ["INT_ADD", "register:40f0:8", ["const:c577ac:8", "const:4:8"]]
+ 00c577ac ["CALL", null, ["callee:00c5f010:8"]]
- 00c5770c bytes 0d1e0094
+ 00c577ac bytes 191e0094
- 00c57678 ["COPY", "tmp:0:8", ["const:b31:8"]]
- 00c57678 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00c57678 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00c57678 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00c57718 ["COPY", "tmp:0:8", ["const:b62:8"]]
+ 00c57718 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00c57718 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00c57718 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00c57678 bytes 21c42c91
+ 00c57718 bytes 21882d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-858d71f3acd4ac21a29a0b3d117e037d"></a>

### [`00c57a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57a8c.md) → [`00c57b2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57b2c.md) FUN_00c57b2c

採用 · 移動量 `+0xa0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c57924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57924.md) · 呼出先 4件 [`00c5a1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a1b0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md) [`00c5ef40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ef40.md) [`0112a8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a8f0.md)
- 新版 呼出元 1件 [`00c579c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c579c4.md) · 呼出先 4件 [`00c5a280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a280.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md) [`00c5f010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5f/00c5f010.md) [`0112a8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a8f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 84.13% / 新版 84.13%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c57bd4",
      "incomplete_value": true,
      "site": "00c57bd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c57b34",
      "incomplete_value": true,
      "site": "00c57b38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:130:8"
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
      "definition_site": "00c57bbc",
      "incomplete_value": false,
      "site": "00c57bd8",
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
            "const:ec4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c57b1c",
      "incomplete_value": false,
      "site": "00c57b38",
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
            "const:f11:8"
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
      "definition_site": "00c57bc8",
      "incomplete_value": false,
      "site": "00c57bd8",
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
            "const:a64:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c57b28",
      "incomplete_value": false,
      "site": "00c57b38",
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
            "const:a35:8"
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
      "00c57bbc",
      "PARAM",
      [
        "storage",
        "002a0f11",
        null,
        "string"
      ]
    ],
    [
      "00c57bc0",
      "READ",
      [
        "storage",
        "00c9bb78",
        null,
        "pointer"
      ]
    ],
    [
      "00c57bc8",
      "PARAM",
      [
        "storage",
        "002a9a35",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c57bbc",
      "PARAM",
      [
        "storage",
        "002a0ec4",
        null,
        "string"
      ]
    ],
    [
      "00c57bc0",
      "READ",
      [
        "storage",
        "00c9bc48",
        null,
        "pointer"
      ]
    ],
    [
      "00c57bc8",
      "PARAM",
      [
        "storage",
        "002a9a64",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c57b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57a8c.md#insn-00c57b38) · [`00c57b78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57a8c.md#insn-00c57b78) · [`00c57b1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57a8c.md#insn-00c57b1c)
- 新版 [`00c57bd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57b2c.md#insn-00c57bd8) · [`00c57c18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57b2c.md#insn-00c57c18) · [`00c57bbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57b2c.md#insn-00c57bbc)

~~~diff
- 00c57b38 ["INT_ADD", "register:40f0:8", ["const:c57b38:8", "const:4:8"]]
- 00c57b38 ["CALL", null, ["callee:00c5f010:8"]]
+ 00c57bd8 ["INT_ADD", "register:40f0:8", ["const:c57bd8:8", "const:4:8"]]
+ 00c57bd8 ["CALL", null, ["callee:00c5f010:8"]]
- 00c57b38 bytes 021d0094
+ 00c57bd8 bytes 0e1d0094
- 00c57b78 ["INT_ADD", "register:40f0:8", ["const:c57b78:8", "const:4:8"]]
- 00c57b78 ["CALL", null, ["callee:00c5f010:8"]]
+ 00c57c18 ["INT_ADD", "register:40f0:8", ["const:c57c18:8", "const:4:8"]]
+ 00c57c18 ["CALL", null, ["callee:00c5f010:8"]]
- 00c57b78 bytes f21c0094
+ 00c57c18 bytes fe1c0094
- 00c57b1c ["COPY", "tmp:0:8", ["const:f11:8"]]
- 00c57b1c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00c57b1c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00c57b1c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00c57bbc ["COPY", "tmp:0:8", ["const:ec4:8"]]
+ 00c57bbc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00c57bbc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00c57bbc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00c57b1c bytes 21443c91
+ 00c57bbc bytes 21103b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-292c09d60250463201c71b37bf9b105b"></a>

### [`00c57cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57cf4.md) → [`00c57dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57dbc.md) _Znwm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) · 呼出先 6件 [`00c37ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ba4.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c58a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58a40.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) · 呼出先 6件 [`00c37c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c40.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c58b10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58b10.md) [`00c5a0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c57e1c",
      "incomplete_value": true,
      "site": "00c57e24",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
      "definition_site": "00c57d54",
      "incomplete_value": true,
      "site": "00c57d5c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c57e20",
      "incomplete_value": true,
      "site": "00c57e24",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
      "definition_site": "00c57d58",
      "incomplete_value": true,
      "site": "00c57d5c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
      "00c57e1c",
      "READ",
      [
        "storage",
        "00c9ade8",
        null,
        "pointer"
      ]
    ],
    [
      "00c57e1c",
      "PARAM",
      [
        "storage",
        "00c96698",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00c57e20",
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
      "00c57e1c",
      "READ",
      [
        "storage",
        "00c9aeb8",
        null,
        "pointer"
      ]
    ],
    [
      "00c57e1c",
      "PARAM",
      [
        "storage",
        "00c96768",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00c57e20",
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

- 旧版 [`00c57d5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57cf4.md#insn-00c57d5c) · [`00c57d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57cf4.md#insn-00c57d10) · [`00c57d18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57cf4.md#insn-00c57d18)
- 新版 [`00c57e24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57dbc.md#insn-00c57e24) · [`00c57dd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57dbc.md#insn-00c57dd8) · [`00c57de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57dbc.md#insn-00c57de0)

~~~diff
- 00c57d5c ["INT_ADD", "register:40f0:8", ["const:c57d5c:8", "const:4:8"]]
- 00c57d5c ["CALL", null, ["callee:00c57fe0:8"]]
+ 00c57e24 ["INT_ADD", "register:40f0:8", ["const:c57e24:8", "const:4:8"]]
+ 00c57e24 ["CALL", null, ["callee:00c57fe0:8"]]
- 00c57d5c bytes 6d000094
+ 00c57e24 bytes 6f000094
- 00c57d10 ["INT_ADD", "register:40f0:8", ["const:c57d10:8", "const:4:8"]]
- 00c57d10 ["CALL", null, ["callee:00c5a0f0:8"]]
+ 00c57dd8 ["INT_ADD", "register:40f0:8", ["const:c57dd8:8", "const:4:8"]]
+ 00c57dd8 ["CALL", null, ["callee:00c5a0f0:8"]]
- 00c57d10 bytes c4080094
+ 00c57dd8 bytes c6080094
- 00c57d18 ["INT_ADD", "register:40f0:8", ["const:c57d18:8", "const:4:8"]]
- 00c57d18 ["CALL", null, ["callee:00c5eeb0:8"]]
+ 00c57de0 ["INT_ADD", "register:40f0:8", ["const:c57de0:8", "const:4:8"]]
+ 00c57de0 ["CALL", null, ["callee:00c5eeb0:8"]]
- 00c57d18 bytes 321c0094
+ 00c57de0 bytes 341c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc8941771edd29be5d05799ccdf4e4c8"></a>

### [`00c57d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57d68.md) → [`00c57e30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57e30.md) _ZnwmSt11align_val_t

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5eec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5eec0.md) · 呼出先 6件 [`00c37ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ba4.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c58a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58a40.md) [`00c5ede0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5ede0.md)
- 新版 呼出元 1件 [`00c5ef90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5ef90.md) · 呼出先 6件 [`00c37c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c40.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c58b10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58b10.md) [`00c5eeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eeb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c57eb4",
      "incomplete_value": true,
      "site": "00c57ebc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
      "definition_site": "00c57dec",
      "incomplete_value": true,
      "site": "00c57df4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c57eb8",
      "incomplete_value": true,
      "site": "00c57ebc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
      "definition_site": "00c57df0",
      "incomplete_value": true,
      "site": "00c57df4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
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
      "00c57eb4",
      "READ",
      [
        "storage",
        "00c9ade8",
        null,
        "pointer"
      ]
    ],
    [
      "00c57eb4",
      "PARAM",
      [
        "storage",
        "00c96698",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00c57eb8",
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
      "00c57eb4",
      "READ",
      [
        "storage",
        "00c9aeb8",
        null,
        "pointer"
      ]
    ],
    [
      "00c57eb4",
      "PARAM",
      [
        "storage",
        "00c96768",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00c57eb8",
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

- 旧版 [`00c57df4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57d68.md#insn-00c57df4) · [`00c57da0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57d68.md#insn-00c57da0) · [`00c57dac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57d68.md#insn-00c57dac)
- 新版 [`00c57ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57e30.md#insn-00c57ebc) · [`00c57e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57e30.md#insn-00c57e68) · [`00c57e74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57e30.md#insn-00c57e74)

~~~diff
- 00c57df4 ["INT_ADD", "register:40f0:8", ["const:c57df4:8", "const:4:8"]]
- 00c57df4 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00c57ebc ["INT_ADD", "register:40f0:8", ["const:c57ebc:8", "const:4:8"]]
+ 00c57ebc ["CALL", null, ["callee:00c57fe0:8"]]
- 00c57df4 bytes 47000094
+ 00c57ebc bytes 49000094
- 00c57da0 ["INT_ADD", "register:40f0:8", ["const:c57da0:8", "const:4:8"]]
- 00c57da0 ["CALL", null, ["callee:00c5efa0:8"]]
+ 00c57e68 ["INT_ADD", "register:40f0:8", ["const:c57e68:8", "const:4:8"]]
+ 00c57e68 ["CALL", null, ["callee:00c5efa0:8"]]
- 00c57da0 bytes 4c1c0094
+ 00c57e68 bytes 4e1c0094
- 00c57dac ["INT_ADD", "register:40f0:8", ["const:c57dac:8", "const:4:8"]]
- 00c57dac ["CALL", null, ["callee:00c5eeb0:8"]]
+ 00c57e74 ["INT_ADD", "register:40f0:8", ["const:c57e74:8", "const:4:8"]]
+ 00c57e74 ["CALL", null, ["callee:00c5eeb0:8"]]
- 00c57dac bytes 0d1c0094
+ 00c57e74 bytes 0f1c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

