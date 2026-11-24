# v16.0.1 → v16.0.2 · 命令位置の検査未完了 (1)

[一覧の目次](README.md)

<a id="compare-f955c14d823ad883f0b16ebe7f59d84e"></a>

### [`0046d7c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7c0.md) → [`0046d800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d800.md) FUN_0046d800

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 5件 [`0046d7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`009dc124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dc/009dc124.md) [`009dc130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dc/009dc130.md) [`009dc13c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dc/009dc13c.md) [`00a06d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06d9c.md) · 呼出先 7件 [`0046db00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046db00.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c583a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c583a0.md) [`00c583b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c583b0.md)
- 新版 呼出元 5件 [`0046d7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d7f0.md) [`009dc178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dc/009dc178.md) [`009dc184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dc/009dc184.md) [`009dc190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dc/009dc190.md) [`00a06df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a06df0.md) · 呼出先 7件 [`0046db40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046db40.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58470.md) [`00c58480`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58480.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.56% / 新版 95.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0046d858",
      "READ",
      [
        "storage",
        "002b8e1d",
        null,
        "string"
      ]
    ],
    [
      "0046d85c",
      "READ",
      [
        "storage",
        "002c4148",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0046d858",
      "READ",
      [
        "storage",
        "002b8dc9",
        null,
        "string"
      ]
    ],
    [
      "0046d85c",
      "READ",
      [
        "storage",
        "002c4188",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046d80c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7c0.md#insn-0046d80c) · [`0046d810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7c0.md#insn-0046d810) · [`0046d81c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7c0.md#insn-0046d81c)
- 新版 [`0046d84c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d800.md#insn-0046d84c) · [`0046d85c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d800.md#insn-0046d85c)

~~~diff
- 0046d80c ["COPY", "tmp:0:8", ["const:e1d:8"]]
- 0046d80c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0046d80c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0046d80c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0046d84c ["COPY", "tmp:0:8", ["const:dc9:8"]]
+ 0046d84c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0046d84c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0046d84c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0046d80c bytes 08753891
+ 0046d84c bytes 08253791
- 0046d810 ["COPY", "register:4048:8", ["const:2c4000:8"]]
- 0046d810 bytes a9f2fff0
- 0046d81c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:148:8"]]
- 0046d81c ["LOAD", "register:5100:8", ["const:1b1:8", "tmp:0:8"]]
- 0046d81c ["COPY", "register:5108:8", ["const:0:8"]]
- 0046d81c ["COPY", "register:5110:8", ["const:0:8"]]
+ 0046d85c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:188:8"]]
+ 0046d85c ["LOAD", "register:5100:8", ["const:1b1:8", "tmp:0:8"]]
+ 0046d85c ["COPY", "register:5108:8", ["const:0:8"]]
+ 0046d85c ["COPY", "register:5110:8", ["const:0:8"]]
- 0046d81c bytes 28a540fd
+ 0046d85c bytes 28c540fd
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c19d78dccec3b7146f4a4d6b246a2056"></a>

### [`0048d280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d280.md) → [`0048d2c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048d/0048d2c0.md) FUN_0048d2c0

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0085b138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b138.md) · 呼出先 0件 
- 新版 呼出元 1件 [`0085b190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085b190.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0048d2cc",
      "READ",
      [
        "storage",
        "00ca4c88",
        null,
        "undefined4"
      ]
    ],
    [
      "0048d2d4",
      "READ",
      [
        "storage",
        "00ca4c78",
        null,
        "undefined4"
      ]
    ],
    [
      "0048d2e0",
      "READ",
      [
        "storage",
        "00ca4c8c",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0048d2cc",
      "READ",
      [
        "storage",
        "00ca4d88",
        null,
        "undefined4"
      ]
    ],
    [
      "0048d2d4",
      "READ",
      [
        "storage",
        "00ca4d78",
        null,
        "undefined4"
      ]
    ],
    [
      "0048d2e0",
      "READ",
      [
        "storage",
        "00ca4d8c",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048d284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d280.md#insn-0048d284) · [`0048d290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d280.md#insn-0048d290)
- 新版 [`0048d2c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048d/0048d2c0.md#insn-0048d2c4) · [`0048d2d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048d/0048d2c0.md#insn-0048d2d0)

~~~diff
- 0048d284 ["COPY", "tmp:0:8", ["const:c70:8"]]
- 0048d284 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0048d284 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0048d284 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0048d2c4 ["COPY", "tmp:0:8", ["const:d70:8"]]
+ 0048d2c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0048d2c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0048d2c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0048d284 bytes 08c13191
+ 0048d2c4 bytes 08c13591
- 0048d290 ["INT_MULT", "tmp:0:4", ["register:4050:4", "register:4048:4"]]
- 0048d290 ["INT_ZEXT", "register:4048:8", ["tmp:0:4"]]
- 0048d290 bytes 497d091b
+ 0048d2d0 ["INT_MULT", "tmp:0:4", ["register:4050:4", "register:4048:4"]]
+ 0048d2d0 ["INT_ZEXT", "register:4048:8", ["tmp:0:4"]]
+ 0048d2d0 bytes 497d091b
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5771085f675ad1dbe6ab905e50766bda"></a>

### [`00493b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493b2c.md) → [`00493b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493b6c.md) FUN_00493b6c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0093b770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093b/0093b770.md) · 呼出先 3件 [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c585f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c585f0.md) [`00c58600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58600.md)
- 新版 呼出元 1件 [`0093b7c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0093b/0093b7c4.md) · 呼出先 3件 [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md) [`00c586c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586c0.md) [`00c586d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586d0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00493c08",
      "PARAM",
      [
        "storage",
        "002af85d",
        null,
        null
      ]
    ],
    [
      "00493c10",
      "PARAM",
      [
        "storage",
        "002a8adb",
        null,
        null
      ]
    ],
    [
      "00493c10",
      "PARAM",
      [
        "storage",
        "002af85a",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00493c08",
      "PARAM",
      [
        "storage",
        "002af801",
        null,
        null
      ]
    ],
    [
      "00493c10",
      "PARAM",
      [
        "storage",
        "002a8a7f",
        null,
        null
      ]
    ],
    [
      "00493c10",
      "PARAM",
      [
        "storage",
        "002af7fe",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00493b7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493b2c.md#insn-00493b7c) · [`00493ba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493b2c.md#insn-00493ba0) · [`00493ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493b2c.md#insn-00493ba4)
- 新版 [`00493bbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493b6c.md#insn-00493bbc) · [`00493be0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/00493b6c.md#insn-00493be0)

~~~diff
- 00493b7c ["INT_ADD", "register:40f0:8", ["const:493b7c:8", "const:4:8"]]
- 00493b7c ["CALL", null, ["callee:00c586c0:8"]]
+ 00493bbc ["INT_ADD", "register:40f0:8", ["const:493bbc:8", "const:4:8"]]
+ 00493bbc ["CALL", null, ["callee:00c586c0:8"]]
- 00493b7c bytes 9d121f94
+ 00493bbc bytes c1121f94
- 00493ba0 ["COPY", "tmp:0:8", ["const:85a:8"]]
- 00493ba0 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
- 00493ba0 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
- 00493ba0 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
+ 00493be0 ["COPY", "tmp:0:8", ["const:7fe:8"]]
+ 00493be0 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
+ 00493be0 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
+ 00493be0 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
- 00493ba0 bytes d66a2191
+ 00493be0 bytes d6fa1f91
- 00493ba4 ["COPY", "register:40b8:8", ["const:2be000:8"]]
- 00493ba4 bytes 57f1fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c56458532a6590fe0071be95a28c772"></a>

### [`004b5148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b5/004b5148.md) → [`004b5188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b5/004b5188.md) _ZN5Botan10hex_encodeEPKhmb

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c58ba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58ba0.md) · 呼出先 3件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)
- 新版 呼出元 1件 [`00c58c70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58c70.md) · 呼出先 3件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004b5264",
      "DATA",
      [
        "storage",
        "002c30d0",
        null,
        "string"
      ]
    ],
    [
      "004b5264",
      "DATA",
      [
        "storage",
        "002c21f0",
        null,
        null
      ]
    ],
    [
      "004b526c",
      "DATA",
      [
        "storage",
        "002c30d0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004b5264",
      "DATA",
      [
        "storage",
        "002c3110",
        null,
        "string"
      ]
    ],
    [
      "004b5264",
      "DATA",
      [
        "storage",
        "002c2230",
        null,
        null
      ]
    ],
    [
      "004b526c",
      "DATA",
      [
        "storage",
        "002c3110",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b51bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b5/004b5148.md#insn-004b51bc) · [`004b51dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b5/004b5148.md#insn-004b51dc) · [`004b51f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b5/004b5148.md#insn-004b51f4)
- 新版 [`004b51fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b5/004b5188.md#insn-004b51fc) · [`004b521c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b5/004b5188.md#insn-004b521c) · [`004b5234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b5/004b5188.md#insn-004b5234)

~~~diff
- 004b51bc ["INT_ADD", "register:40f0:8", ["const:4b51bc:8", "const:4:8"]]
- 004b51bc ["CALL", null, ["callee:00c57f60:8"]]
+ 004b51fc ["INT_ADD", "register:40f0:8", ["const:4b51fc:8", "const:4:8"]]
+ 004b51fc ["CALL", null, ["callee:00c57f60:8"]]
- 004b51bc bytes 358b1e94
+ 004b51fc bytes 598b1e94
- 004b51dc ["INT_ADD", "register:40f0:8", ["const:4b51dc:8", "const:4:8"]]
- 004b51dc ["CALL", null, ["callee:00c58160:8"]]
+ 004b521c ["INT_ADD", "register:40f0:8", ["const:4b521c:8", "const:4:8"]]
+ 004b521c ["CALL", null, ["callee:00c58160:8"]]
- 004b51dc bytes ad8b1e94
+ 004b521c bytes d18b1e94
- 004b51f4 ["COPY", "tmp:0:8", ["const:1f0:8"]]
- 004b51f4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004b51f4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004b51f4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 004b5234 ["COPY", "tmp:0:8", ["const:230:8"]]
+ 004b5234 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 004b5234 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 004b5234 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004b51f4 bytes 4ac10791
+ 004b5234 bytes 4ac10891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ee69498958ba7967c8c6fd1dadb7d13"></a>

### [`004b6690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b6/004b6690.md) → [`004b66d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b6/004b66d0.md) _ZN5Botan10hex_encodeEPcPKhmb

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 72.22% / 新版 72.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004b6700",
      "DATA",
      [
        "storage",
        "002c30d0",
        null,
        "string"
      ]
    ],
    [
      "004b6700",
      "DATA",
      [
        "storage",
        "002c21f0",
        null,
        null
      ]
    ],
    [
      "004b6708",
      "DATA",
      [
        "storage",
        "002c30d0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004b6700",
      "DATA",
      [
        "storage",
        "002c3110",
        null,
        "string"
      ]
    ],
    [
      "004b6700",
      "DATA",
      [
        "storage",
        "002c2230",
        null,
        null
      ]
    ],
    [
      "004b6708",
      "DATA",
      [
        "storage",
        "002c3110",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b6690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b6/004b6690.md#insn-004b6690) · [`004b6694`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b6/004b6690.md#insn-004b6694) · [`004b669c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b6/004b6690.md#insn-004b669c)
- 新版 [`004b66d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b6/004b66d0.md#insn-004b66d4)

~~~diff
- 004b6690 ["COPY", "register:4040:8", ["const:2c3000:8"]]
- 004b6690 bytes 68f0ffb0
- 004b6694 ["COPY", "tmp:0:8", ["const:d0:8"]]
- 004b6694 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004b6694 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004b6694 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004b66d4 ["COPY", "tmp:0:8", ["const:110:8"]]
+ 004b66d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004b66d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004b66d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004b6694 bytes 08410391
+ 004b66d4 bytes 08410491
- 004b669c ["COPY", "register:4048:8", ["const:2c2000:8"]]
- 004b669c bytes 69f0ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96d9944d6d42546a9b725e9105f72e1c"></a>

### [`004cfe64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cf/004cfe64.md) → [`004cfea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cf/004cfea4.md) _ZNK5Botan13PKCS7_Padding5unpadEPKhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.11% / 新版 95.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004cff0c",
      "READ",
      [
        "storage",
        "002c2380",
        null,
        null
      ]
    ],
    [
      "004cff10",
      "READ",
      [
        "storage",
        "002c2190",
        null,
        null
      ]
    ],
    [
      "004cff14",
      "READ",
      [
        "storage",
        "002c2b70",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004cff0c",
      "READ",
      [
        "storage",
        "002c23c0",
        null,
        null
      ]
    ],
    [
      "004cff10",
      "READ",
      [
        "storage",
        "002c21d0",
        null,
        null
      ]
    ],
    [
      "004cff14",
      "READ",
      [
        "storage",
        "002c2bb0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cfecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cf/004cfe64.md#insn-004cfecc) · [`004cfed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cf/004cfe64.md#insn-004cfed0) · [`004cfed4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cf/004cfe64.md#insn-004cfed4)
- 新版 [`004cff0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cf/004cfea4.md#insn-004cff0c) · [`004cff10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cf/004cfea4.md#insn-004cff10) · [`004cff14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004cf/004cfea4.md#insn-004cff14)

~~~diff
- 004cfecc ["INT_ADD", "tmp:0:8", ["register:4070:8", "const:380:8"]]
- 004cfecc ["LOAD", "register:50a0:16", ["const:1b1:8", "tmp:0:8"]]
- 004cfecc ["COPY", "register:50b0:8", ["const:0:8"]]
- 004cfecc ["COPY", "register:50b8:8", ["const:0:8"]]
+ 004cff0c ["INT_ADD", "tmp:0:8", ["register:4070:8", "const:3c0:8"]]
+ 004cff0c ["LOAD", "register:50a0:16", ["const:1b1:8", "tmp:0:8"]]
+ 004cff0c ["COPY", "register:50b0:8", ["const:0:8"]]
+ 004cff0c ["COPY", "register:50b8:8", ["const:0:8"]]
- 004cfecc bytes c5e1c03d
+ 004cff0c bytes c5f1c03d
- 004cfed0 ["INT_ADD", "tmp:0:8", ["register:4068:8", "const:190:8"]]
- 004cfed0 ["LOAD", "register:50c0:16", ["const:1b1:8", "tmp:0:8"]]
- 004cfed0 ["COPY", "register:50d0:8", ["const:0:8"]]
- 004cfed0 ["COPY", "register:50d8:8", ["const:0:8"]]
+ 004cff10 ["INT_ADD", "tmp:0:8", ["register:4068:8", "const:1d0:8"]]
+ 004cff10 ["LOAD", "register:50c0:16", ["const:1b1:8", "tmp:0:8"]]
+ 004cff10 ["COPY", "register:50d0:8", ["const:0:8"]]
+ 004cff10 ["COPY", "register:50d8:8", ["const:0:8"]]
- 004cfed0 bytes a665c03d
+ 004cff10 bytes a675c03d
- 004cfed4 ["INT_ADD", "tmp:0:8", ["register:4058:8", "const:b70:8"]]
- 004cfed4 ["LOAD", "register:50e0:16", ["const:1b1:8", "tmp:0:8"]]
- 004cfed4 ["COPY", "register:50f0:8", ["const:0:8"]]
- 004cfed4 ["COPY", "register:50f8:8", ["const:0:8"]]
+ 004cff14 ["INT_ADD", "tmp:0:8", ["register:4058:8", "const:bb0:8"]]
+ 004cff14 ["LOAD", "register:50e0:16", ["const:1b1:8", "tmp:0:8"]]
+ 004cff14 ["COPY", "register:50f0:8", ["const:0:8"]]
+ 004cff14 ["COPY", "register:50f8:8", ["const:0:8"]]
- 004cfed4 bytes 67ddc23d
+ 004cff14 bytes 67edc23d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87ef0df9e5d551e0fe18cdd2b75741a0"></a>

### [`004d0358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d0/004d0358.md) → [`004d0398`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d0/004d0398.md) _ZNK5Botan17ANSI_X923_Padding5unpadEPKhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 94.90% / 新版 94.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004d03fc",
      "READ",
      [
        "storage",
        "002c2380",
        null,
        null
      ]
    ],
    [
      "004d0400",
      "READ",
      [
        "storage",
        "002c2190",
        null,
        null
      ]
    ],
    [
      "004d0404",
      "READ",
      [
        "storage",
        "002c2b70",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004d03fc",
      "READ",
      [
        "storage",
        "002c23c0",
        null,
        null
      ]
    ],
    [
      "004d0400",
      "READ",
      [
        "storage",
        "002c21d0",
        null,
        null
      ]
    ],
    [
      "004d0404",
      "READ",
      [
        "storage",
        "002c2bb0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d03bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d0/004d0358.md#insn-004d03bc) · [`004d03c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d0/004d0358.md#insn-004d03c0) · [`004d03c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d0/004d0358.md#insn-004d03c4)
- 新版 [`004d03fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d0/004d0398.md#insn-004d03fc) · [`004d0400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d0/004d0398.md#insn-004d0400) · [`004d0404`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d0/004d0398.md#insn-004d0404)

~~~diff
- 004d03bc ["INT_ADD", "tmp:0:8", ["register:4068:8", "const:380:8"]]
- 004d03bc ["LOAD", "register:50a0:16", ["const:1b1:8", "tmp:0:8"]]
- 004d03bc ["COPY", "register:50b0:8", ["const:0:8"]]
- 004d03bc ["COPY", "register:50b8:8", ["const:0:8"]]
+ 004d03fc ["INT_ADD", "tmp:0:8", ["register:4068:8", "const:3c0:8"]]
+ 004d03fc ["LOAD", "register:50a0:16", ["const:1b1:8", "tmp:0:8"]]
+ 004d03fc ["COPY", "register:50b0:8", ["const:0:8"]]
+ 004d03fc ["COPY", "register:50b8:8", ["const:0:8"]]
- 004d03bc bytes a5e1c03d
+ 004d03fc bytes a5f1c03d
- 004d03c0 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:190:8"]]
- 004d03c0 ["LOAD", "register:50c0:16", ["const:1b1:8", "tmp:0:8"]]
- 004d03c0 ["COPY", "register:50d0:8", ["const:0:8"]]
- 004d03c0 ["COPY", "register:50d8:8", ["const:0:8"]]
+ 004d0400 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:1d0:8"]]
+ 004d0400 ["LOAD", "register:50c0:16", ["const:1b1:8", "tmp:0:8"]]
+ 004d0400 ["COPY", "register:50d0:8", ["const:0:8"]]
+ 004d0400 ["COPY", "register:50d8:8", ["const:0:8"]]
- 004d03c0 bytes 4665c03d
+ 004d0400 bytes 4675c03d
- 004d03c4 ["INT_ADD", "tmp:0:8", ["register:4058:8", "const:b70:8"]]
- 004d03c4 ["LOAD", "register:50e0:16", ["const:1b1:8", "tmp:0:8"]]
- 004d03c4 ["COPY", "register:50f0:8", ["const:0:8"]]
- 004d03c4 ["COPY", "register:50f8:8", ["const:0:8"]]
+ 004d0404 ["INT_ADD", "tmp:0:8", ["register:4058:8", "const:bb0:8"]]
+ 004d0404 ["LOAD", "register:50e0:16", ["const:1b1:8", "tmp:0:8"]]
+ 004d0404 ["COPY", "register:50f0:8", ["const:0:8"]]
+ 004d0404 ["COPY", "register:50f8:8", ["const:0:8"]]
- 004d03c4 bytes 67ddc23d
+ 004d0404 bytes 67edc23d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26e725b03179cf4f26563606b3cd9500"></a>

### [`004d0960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d0/004d0960.md) → [`004d09a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d0/004d09a0.md) _ZNK5Botan11ESP_Padding5unpadEPKhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004d0a08",
      "READ",
      [
        "storage",
        "002c2380",
        null,
        null
      ]
    ],
    [
      "004d0a0c",
      "READ",
      [
        "storage",
        "002c2190",
        null,
        null
      ]
    ],
    [
      "004d0a10",
      "READ",
      [
        "storage",
        "002c2b70",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004d0a08",
      "READ",
      [
        "storage",
        "002c23c0",
        null,
        null
      ]
    ],
    [
      "004d0a0c",
      "READ",
      [
        "storage",
        "002c21d0",
        null,
        null
      ]
    ],
    [
      "004d0a10",
      "READ",
      [
        "storage",
        "002c2bb0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d09c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d0/004d0960.md#insn-004d09c8) · [`004d09cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d0/004d0960.md#insn-004d09cc) · [`004d09d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d0/004d0960.md#insn-004d09d0)
- 新版 [`004d0a08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d0/004d09a0.md#insn-004d0a08) · [`004d0a0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d0/004d09a0.md#insn-004d0a0c) · [`004d0a10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d0/004d09a0.md#insn-004d0a10)

~~~diff
- 004d09c8 ["INT_ADD", "tmp:0:8", ["register:4068:8", "const:380:8"]]
- 004d09c8 ["LOAD", "register:50a0:16", ["const:1b1:8", "tmp:0:8"]]
- 004d09c8 ["COPY", "register:50b0:8", ["const:0:8"]]
- 004d09c8 ["COPY", "register:50b8:8", ["const:0:8"]]
+ 004d0a08 ["INT_ADD", "tmp:0:8", ["register:4068:8", "const:3c0:8"]]
+ 004d0a08 ["LOAD", "register:50a0:16", ["const:1b1:8", "tmp:0:8"]]
+ 004d0a08 ["COPY", "register:50b0:8", ["const:0:8"]]
+ 004d0a08 ["COPY", "register:50b8:8", ["const:0:8"]]
- 004d09c8 bytes a5e1c03d
+ 004d0a08 bytes a5f1c03d
- 004d09cc ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:190:8"]]
- 004d09cc ["LOAD", "register:50c0:16", ["const:1b1:8", "tmp:0:8"]]
- 004d09cc ["COPY", "register:50d0:8", ["const:0:8"]]
- 004d09cc ["COPY", "register:50d8:8", ["const:0:8"]]
+ 004d0a0c ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:1d0:8"]]
+ 004d0a0c ["LOAD", "register:50c0:16", ["const:1b1:8", "tmp:0:8"]]
+ 004d0a0c ["COPY", "register:50d0:8", ["const:0:8"]]
+ 004d0a0c ["COPY", "register:50d8:8", ["const:0:8"]]
- 004d09cc bytes 4665c03d
+ 004d0a0c bytes 4675c03d
- 004d09d0 ["INT_ADD", "tmp:0:8", ["register:4058:8", "const:b70:8"]]
- 004d09d0 ["LOAD", "register:50e0:16", ["const:1b1:8", "tmp:0:8"]]
- 004d09d0 ["COPY", "register:50f0:8", ["const:0:8"]]
- 004d09d0 ["COPY", "register:50f8:8", ["const:0:8"]]
+ 004d0a10 ["INT_ADD", "tmp:0:8", ["register:4058:8", "const:bb0:8"]]
+ 004d0a10 ["LOAD", "register:50e0:16", ["const:1b1:8", "tmp:0:8"]]
+ 004d0a10 ["COPY", "register:50f0:8", ["const:0:8"]]
+ 004d0a10 ["COPY", "register:50f8:8", ["const:0:8"]]
- 004d09d0 bytes 67ddc23d
+ 004d0a10 bytes 67edc23d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-892aeaa5605548c31be1414d3b51356c"></a>

### [`004feb30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fe/004feb30.md) → [`004feb70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fe/004feb70.md) _ZN5Botan14version_stringEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 46.15% / 新版 46.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "004feb64"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "004feb68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "004feb68"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004feb94",
      "READ",
      [
        "storage",
        "002bc60e",
        null,
        "string"
      ]
    ],
    [
      "004feb94",
      "READ",
      [
        "storage",
        "002bc61e",
        null,
        "string"
      ]
    ],
    [
      "004feb98",
      "READ",
      [
        "storage",
        "002c2ab0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004feb94",
      "READ",
      [
        "storage",
        "002bc5ba",
        null,
        "string"
      ]
    ],
    [
      "004feb94",
      "READ",
      [
        "storage",
        "002bc5ca",
        null,
        "string"
      ]
    ],
    [
      "004feb98",
      "READ",
      [
        "storage",
        "002c2af0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004feb44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fe/004feb30.md#insn-004feb44) · [`004feb64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fe/004feb30.md#insn-004feb64) · [`004feb68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fe/004feb30.md#insn-004feb68)
- 新版 [`004feb84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fe/004feb70.md#insn-004feb84)

~~~diff
- 004feb44 ["INT_ADD", "register:40f0:8", ["const:4feb44:8", "const:4:8"]]
- 004feb44 ["CALL", null, ["callee:00c57f60:8"]]
+ 004feb84 ["INT_ADD", "register:40f0:8", ["const:4feb84:8", "const:4:8"]]
+ 004feb84 ["CALL", null, ["callee:00c57f60:8"]]
- 004feb44 bytes d3641d94
+ 004feb84 bytes f7641d94
- 004feb64 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 004feb64 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5040:16"]]
- 004feb64 bytes 6202803d
- 004feb68 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:40:8"]]
- 004feb68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 004feb68 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 004feb68 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5020:16"]]
- 004feb68 bytes 000402ad
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c4726c6d4829f3b66b0726e5e9ca66d"></a>

### [`005766d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005766d4.md) → [`00576714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/00576714.md) FUN_00576714

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00550a00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550a00.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00550a40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00550/00550a40.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 11.11% / 新版 11.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0057671c",
      "READ",
      [
        "storage",
        "00c9ab70",
        null,
        "pointer"
      ]
    ],
    [
      "00576720",
      "READ",
      [
        "storage",
        "00c9ab78",
        null,
        "pointer"
      ]
    ],
    [
      "00576724",
      "READ",
      [
        "storage",
        "00ca645c",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0057671c",
      "READ",
      [
        "storage",
        "00c9ac40",
        null,
        "pointer"
      ]
    ],
    [
      "00576720",
      "READ",
      [
        "storage",
        "00c9ac48",
        null,
        "pointer"
      ]
    ],
    [
      "00576724",
      "READ",
      [
        "storage",
        "00ca655c",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005766d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005766d4.md#insn-005766d4) · [`005766d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005766d4.md#insn-005766d8) · [`005766dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005766d4.md#insn-005766dc)
- 新版 [`0057671c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/00576714.md#insn-0057671c)

~~~diff
- 005766d4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 005766d4 bytes 28390090
- 005766d8 ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 005766d8 bytes 29390090
- 005766dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b70:8"]]
- 005766dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0057671c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c40:8"]]
+ 0057671c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005766dc bytes 08b945f9
+ 0057671c bytes 082146f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8befb62da82823571600757bb48ef753"></a>

### [`00585060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/00585060.md) → [`005850a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/005850a0.md) FUN_005850a0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 7件 [`00585214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/00585214.md) [`00587c54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587c54.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00585254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/00585254.md) [`00587c94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00587/00587c94.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.94% / 新版 96.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00585100",
      "PARAM",
      [
        "storage",
        "00c6c9d0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00585104",
      "PARAM",
      [
        "storage",
        "00c6c9e0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00585100",
      "PARAM",
      [
        "storage",
        "00c6caa0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00585104",
      "PARAM",
      [
        "storage",
        "00c6cab0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00585098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/00585060.md#insn-00585098) · [`005850a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/00585060.md#insn-005850a0) · [`005850a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/00585060.md#insn-005850a4)
- 新版 [`005850d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/005850a0.md#insn-005850d8) · [`005850e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00585/005850a0.md#insn-005850e4)

~~~diff
- 00585098 ["COPY", "tmp:0:8", ["const:9d0:8"]]
- 00585098 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 00585098 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 00585098 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 005850d8 ["COPY", "tmp:0:8", ["const:aa0:8"]]
+ 005850d8 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 005850d8 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 005850d8 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 00585098 bytes 94422791
+ 005850d8 bytes 94822a91
- 005850a0 ["COPY", "register:40a8:8", ["const:c6c000:8"]]
- 005850a0 bytes 353700f0
- 005850a4 ["COPY", "tmp:0:8", ["const:9e0:8"]]
- 005850a4 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 005850a4 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 005850a4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 005850e4 ["COPY", "tmp:0:8", ["const:ab0:8"]]
+ 005850e4 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 005850e4 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 005850e4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 005850a4 bytes b5822791
+ 005850e4 bytes b5c22a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8bd03b29cb2bc611e9cbdb344f0f0669"></a>

### [`0058e560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058e560.md) → [`0058e5a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058e5a0.md) FUN_0058e5a0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589840.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00497874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00497/00497874.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md) [`00589880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589880.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.04% / 新版 96.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0058e61c",
      "READ",
      [
        "storage",
        "002a9def",
        null,
        "string"
      ]
    ],
    [
      "0058e61c",
      "READ",
      [
        "storage",
        "002a9dff",
        null,
        "string"
      ]
    ],
    [
      "0058e620",
      "READ",
      [
        "storage",
        "002c23a0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0058e61c",
      "READ",
      [
        "storage",
        "002a9d93",
        null,
        "string"
      ]
    ],
    [
      "0058e61c",
      "READ",
      [
        "storage",
        "002a9da3",
        null,
        "string"
      ]
    ],
    [
      "0058e620",
      "READ",
      [
        "storage",
        "002c23e0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058e594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058e560.md#insn-0058e594) · [`0058e59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058e560.md#insn-0058e59c) · [`0058e5cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058e560.md#insn-0058e5cc)
- 新版 [`0058e5d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058e5a0.md#insn-0058e5d4) · [`0058e5dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058e5a0.md#insn-0058e5dc) · [`0058e60c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0058e/0058e5a0.md#insn-0058e60c)

~~~diff
- 0058e594 ["INT_ADD", "register:40f0:8", ["const:58e594:8", "const:4:8"]]
- 0058e594 ["CALL", null, ["callee:00589880:8"]]
+ 0058e5d4 ["INT_ADD", "register:40f0:8", ["const:58e5d4:8", "const:4:8"]]
+ 0058e5d4 ["CALL", null, ["callee:00589880:8"]]
- 0058e594 bytes abecff97
+ 0058e5d4 bytes abecff97
- 0058e59c ["INT_ADD", "register:40f0:8", ["const:58e59c:8", "const:4:8"]]
- 0058e59c ["CALL", null, ["callee:00588eac:8"]]
+ 0058e5dc ["INT_ADD", "register:40f0:8", ["const:58e5dc:8", "const:4:8"]]
+ 0058e5dc ["CALL", null, ["callee:00588eac:8"]]
- 0058e59c bytes 34eaff97
+ 0058e5dc bytes 34eaff97
- 0058e5cc ["INT_ADD", "register:40f0:8", ["const:58e5cc:8", "const:4:8"]]
- 0058e5cc ["CALL", null, ["callee:00c57f60:8"]]
+ 0058e60c ["INT_ADD", "register:40f0:8", ["const:58e60c:8", "const:4:8"]]
+ 0058e60c ["CALL", null, ["callee:00c57f60:8"]]
- 0058e5cc bytes 31261b94
+ 0058e60c bytes 55261b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-114d8a1c74e5cea09e9aa0e2435e3544"></a>

### [`00595870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595870.md) → [`005958b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005958b0.md) FUN_005958b0

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0059568c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/0059568c.md) [`005959dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/005959dc.md) [`00595d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595d1c.md) · 呼出先 0件 
- 新版 呼出元 3件 [`005956cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005956cc.md) [`00595a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595a1c.md) [`00595d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/00595d5c.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.70% / 新版 96.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005958e0",
      "DATA",
      [
        "storage",
        "002d301d",
        "switchD_005958b0::switchdataD_002d301d",
        "byte"
      ]
    ]
  ],
  "added": [
    [
      "005958e0",
      "DATA",
      [
        "storage",
        "002d305d",
        "switchD_005958f0::switchdataD_002d305d",
        "byte"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00595898`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595870.md#insn-00595898) · [`0059589c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595870.md#insn-0059589c)
- 新版 [`005958d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005958b0.md#insn-005958d8) · [`005958dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00595/005958b0.md#insn-005958dc)

~~~diff
- 00595898 ["COPY", "tmp:0:8", ["const:1d:8"]]
- 00595898 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
- 00595898 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
- 00595898 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
+ 005958d8 ["COPY", "tmp:0:8", ["const:5d:8"]]
+ 005958d8 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
+ 005958d8 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
+ 005958d8 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
- 00595898 bytes 6b750091
+ 005958d8 bytes 6b750191
- 0059589c ["COPY", "register:4068:8", ["const:5958b4:8"]]
- 0059589c bytes cd000010
+ 005958dc ["COPY", "register:4068:8", ["const:5958f4:8"]]
+ 005958dc bytes cd000010
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-613ae09838c4de167a3aed1e0b6867df"></a>

### [`0064dbc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064d/0064dbc8.md) → [`0064dc08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064d/0064dc08.md) FUN_0064dc08

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006554f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00655/006554f0.md) · 呼出先 12件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00641174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00641/00641174.md) [`00641c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00641/00641c68.md) [`006b7130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b7/006b7130.md) [`0071bed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071b/0071bed8.md)
- 新版 呼出元 1件 [`00655530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00655/00655530.md) · 呼出先 12件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`006411b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00641/006411b4.md) [`00641ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00641/00641ca8.md) [`006b7188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b7/006b7188.md) [`0071bf30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071b/0071bf30.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0064dd04",
      "value": [
        "leaf",
        "ram:71bf30:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0064dcc4",
      "value": [
        "leaf",
        "ram:71bed8:8"
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
      "site": "0064dd14",
      "value": [
        "leaf",
        "ram:71d254:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0064dcd4",
      "value": [
        "leaf",
        "ram:71d1fc:8"
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
      "site": "0064dd1c",
      "value": [
        "leaf",
        "ram:71bf30:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0064dcdc",
      "value": [
        "leaf",
        "ram:71bed8:8"
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
      "0064dd04",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bed8"
      ]
    ],
    [
      "0064dd14",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071d1fc"
      ]
    ],
    [
      "0064dd1c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bed8"
      ]
    ]
  ],
  "added": [
    [
      "0064dd04",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bf30"
      ]
    ],
    [
      "0064dd14",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071d254"
      ]
    ],
    [
      "0064dd1c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bf30"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0064dcc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064d/0064dbc8.md#insn-0064dcc4) · [`0064dcd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064d/0064dbc8.md#insn-0064dcd4) · [`0064dcdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064d/0064dbc8.md#insn-0064dcdc)
- 新版 [`0064dd04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064d/0064dc08.md#insn-0064dd04) · [`0064dd14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064d/0064dc08.md#insn-0064dd14) · [`0064dd1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064d/0064dc08.md#insn-0064dd1c)

~~~diff
- 0064dcc4 ["INT_ADD", "register:40f0:8", ["const:64dcc4:8", "const:4:8"]]
- 0064dcc4 ["CALL", null, ["ram:71bed8:8"]]
+ 0064dd04 ["INT_ADD", "register:40f0:8", ["const:64dd04:8", "const:4:8"]]
+ 0064dd04 ["CALL", null, ["ram:71bf30:8"]]
- 0064dcc4 bytes 85380394
+ 0064dd04 bytes 8b380394
- 0064dcd4 ["INT_ADD", "register:40f0:8", ["const:64dcd4:8", "const:4:8"]]
- 0064dcd4 ["CALL", null, ["ram:71d1fc:8"]]
+ 0064dd14 ["INT_ADD", "register:40f0:8", ["const:64dd14:8", "const:4:8"]]
+ 0064dd14 ["CALL", null, ["ram:71d254:8"]]
- 0064dcd4 bytes 4a3d0394
+ 0064dd14 bytes 503d0394
- 0064dcdc ["INT_ADD", "register:40f0:8", ["const:64dcdc:8", "const:4:8"]]
- 0064dcdc ["CALL", null, ["ram:71bed8:8"]]
+ 0064dd1c ["INT_ADD", "register:40f0:8", ["const:64dd1c:8", "const:4:8"]]
+ 0064dd1c ["CALL", null, ["ram:71bf30:8"]]
- 0064dcdc bytes 7f380394
+ 0064dd1c bytes 85380394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-093149f3f3040bcd2c9b906d72445c13"></a>

### [`0064e19c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064e/0064e19c.md) → [`0064e1dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064e/0064e1dc.md) FUN_0064e1dc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0064a530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064a/0064a530.md) [`006535a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00653/006535a0.md) · 呼出先 8件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00641174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00641/00641174.md) [`00641c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00641/00641c68.md) [`0071bed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071b/0071bed8.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 2件 [`0064a570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064a/0064a570.md) [`006535e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00653/006535e0.md) · 呼出先 8件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`006411b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00641/006411b4.md) [`00641ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00641/00641ca8.md) [`0071bf30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071b/0071bf30.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.61% / 新版 96.61%

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
      "site": "0064e214",
      "value": [
        "leaf",
        "ram:71bf30:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0064e1d4",
      "value": [
        "leaf",
        "ram:71bed8:8"
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
      "site": "0064e2d4",
      "value": [
        "leaf",
        "ram:641ca8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0064e294",
      "value": [
        "leaf",
        "ram:641c68:8"
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
      "site": "0064e2e0",
      "value": [
        "leaf",
        "ram:71bf30:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0064e2a0",
      "value": [
        "leaf",
        "ram:71bed8:8"
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
      "0064e214",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bed8"
      ]
    ],
    [
      "0064e2d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00641c68"
      ]
    ],
    [
      "0064e2e0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bed8"
      ]
    ]
  ],
  "added": [
    [
      "0064e214",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bf30"
      ]
    ],
    [
      "0064e2d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00641ca8"
      ]
    ],
    [
      "0064e2e0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bf30"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0064e1d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064e/0064e19c.md#insn-0064e1d4) · [`0064e294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064e/0064e19c.md#insn-0064e294) · [`0064e2a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064e/0064e19c.md#insn-0064e2a0)
- 新版 [`0064e214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064e/0064e1dc.md#insn-0064e214) · [`0064e2d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064e/0064e1dc.md#insn-0064e2d4) · [`0064e2e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0064e/0064e1dc.md#insn-0064e2e0)

~~~diff
- 0064e1d4 ["INT_ADD", "register:40f0:8", ["const:64e1d4:8", "const:4:8"]]
- 0064e1d4 ["CALL", null, ["ram:71bed8:8"]]
+ 0064e214 ["INT_ADD", "register:40f0:8", ["const:64e214:8", "const:4:8"]]
+ 0064e214 ["CALL", null, ["ram:71bf30:8"]]
- 0064e1d4 bytes 41370394
+ 0064e214 bytes 47370394
- 0064e294 ["INT_ADD", "register:40f0:8", ["const:64e294:8", "const:4:8"]]
- 0064e294 ["CALL", null, ["ram:641c68:8"]]
+ 0064e2d4 ["INT_ADD", "register:40f0:8", ["const:64e2d4:8", "const:4:8"]]
+ 0064e2d4 ["CALL", null, ["ram:641ca8:8"]]
- 0064e294 bytes 75ceff97
+ 0064e2d4 bytes 75ceff97
- 0064e2a0 ["INT_ADD", "register:40f0:8", ["const:64e2a0:8", "const:4:8"]]
- 0064e2a0 ["CALL", null, ["ram:71bed8:8"]]
+ 0064e2e0 ["INT_ADD", "register:40f0:8", ["const:64e2e0:8", "const:4:8"]]
+ 0064e2e0 ["CALL", null, ["ram:71bf30:8"]]
- 0064e2a0 bytes 0e370394
+ 0064e2e0 bytes 14370394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d09b1c7cd188b74d2f861d3742bb6ef"></a>

### [`0068a19c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068a/0068a19c.md) → [`0068a1f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068a/0068a1f4.md) FUN_0068a1f4

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0068a2b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068a/0068a2b8.md) · 呼出先 1件 [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md)
- 新版 呼出元 1件 [`0068a310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068a/0068a310.md) · 呼出先 1件 [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.77% / 新版 95.77%

CFGの説明率　旧版 73.91% / 新版 73.91%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0068a260",
      "DATA",
      [
        "storage",
        "002c2200",
        null,
        null
      ]
    ],
    [
      "unmatched:0068a29c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "0068a2bc"
      ]
    ]
  ],
  "added": [
    [
      "0068a2b8",
      "DATA",
      [
        "storage",
        "002c2240",
        null,
        null
      ]
    ],
    [
      "0068a30c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "0068a2bc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0068a1d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068a/0068a19c.md#insn-0068a1d8) · [`0068a200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068a/0068a19c.md#insn-0068a200) · [`0068a210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068a/0068a19c.md#insn-0068a210)
- 新版 [`0068a230`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068a/0068a1f4.md#insn-0068a230) · [`0068a258`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068a/0068a1f4.md#insn-0068a258) · [`0068a268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068a/0068a1f4.md#insn-0068a268)

~~~diff
- 0068a1d8 ["INT_ADD", "register:40f0:8", ["const:68a1d8:8", "const:4:8"]]
- 0068a1d8 ["CALL", null, ["callee:0048797c:8"]]
+ 0068a230 ["INT_ADD", "register:40f0:8", ["const:68a230:8", "const:4:8"]]
+ 0068a230 ["CALL", null, ["callee:0048797c:8"]]
- 0068a1d8 bytes d9f5f797
+ 0068a230 bytes d3f5f797
- 0068a200 ["INT_ADD", "register:40f0:8", ["const:68a200:8", "const:4:8"]]
- 0068a200 ["CALL", null, ["callee:0048797c:8"]]
+ 0068a258 ["INT_ADD", "register:40f0:8", ["const:68a258:8", "const:4:8"]]
+ 0068a258 ["CALL", null, ["callee:0048797c:8"]]
- 0068a200 bytes cff5f797
+ 0068a258 bytes c9f5f797
- 0068a210 ["INT_ADD", "register:40f0:8", ["const:68a210:8", "const:4:8"]]
- 0068a210 ["CALL", null, ["callee:0048797c:8"]]
+ 0068a268 ["INT_ADD", "register:40f0:8", ["const:68a268:8", "const:4:8"]]
+ 0068a268 ["CALL", null, ["callee:0048797c:8"]]
- 0068a210 bytes cbf5f797
+ 0068a268 bytes c5f5f797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1625dd9ecad1368cdfdb44085910338f"></a>

### [`00692244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/00692244.md) → [`0069229c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/0069229c.md) FUN_0069229c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0069201c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/0069201c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00692074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00692/00692074.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 65.22% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006922b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006922bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00692310"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00692274",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00692388"
      ]
    ]
  ],
  "added": [
    [
      "006922cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00692388"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00692274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/00692244.md#insn-00692274) · [`006922b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/00692244.md#insn-006922b8) · [`006922bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00692/00692244.md#insn-006922bc)

~~~diff
- 00692274 ["CBRANCH", null, ["local:b15:8", "register:101:1"]]
- 00692274 bytes e0050054
- 006922b8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:40:8"]]
- 006922b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 006922b8 bytes 2a2100f9
- 006922bc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:30:8"]]
- 006922bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 006922bc bytes 200d803d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e00d592341d6e60b532b80810683edd"></a>

### [`00693338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/00693338.md) → [`00693390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/00693390.md) FUN_00693390

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0069335c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0069335c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006933b4"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0069335c",
      "DATA",
      [
        "storage",
        "00c74850",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00693360",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00693364",
      "DATA",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "006933b4",
      "DATA",
      [
        "storage",
        "00c74920",
        null,
        "undefined *"
      ]
    ],
    [
      "006933b8",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "006933bc",
      "DATA",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0069335c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/00693338.md#insn-0069335c) · [`00693368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/00693338.md#insn-00693368)
- 新版 [`006933b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/00693390.md#insn-006933b4)

~~~diff
- 0069335c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0069335c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 0069335c ["COPY", "tmp:2:8", ["register:4000:8"]]
- 0069335c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0069335c bytes 082400a9
- 00693368 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00693368 ["RETURN", null, ["register:0:8"]]
- 00693368 bytes c0035fd6
+ 006933b4 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 006933b4 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 006933b4 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 006933b4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 006933b4 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9acca97bf370c7dad33a92bf6909406"></a>

### [`00693408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/00693408.md) → [`00693460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/00693460.md) FUN_00693460

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0069342c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0069342c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00693484"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0069342c",
      "DATA",
      [
        "storage",
        "00c748d0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00693430",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00693434",
      "DATA",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00693484",
      "DATA",
      [
        "storage",
        "00c749a0",
        null,
        "undefined *"
      ]
    ],
    [
      "00693488",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0069348c",
      "DATA",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0069342c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/00693408.md#insn-0069342c) · [`00693438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/00693408.md#insn-00693438)
- 新版 [`00693484`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/00693460.md#insn-00693484)

~~~diff
- 0069342c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0069342c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 0069342c ["COPY", "tmp:2:8", ["register:4000:8"]]
- 0069342c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0069342c bytes 082400a9
- 00693438 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00693438 ["RETURN", null, ["register:0:8"]]
- 00693438 bytes c0035fd6
+ 00693484 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00693484 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00693484 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 00693484 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00693484 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c73b94591913b5e9c9023ecb057cb9ef"></a>

### [`00693790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/00693790.md) → [`006937e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/006937e8.md) FUN_006937e8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0069379c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0069379c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006937f4"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0069379c",
      "DATA",
      [
        "storage",
        "00c74940",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006937f4",
      "DATA",
      [
        "storage",
        "00c74a10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0069379c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/00693790.md#insn-0069379c) · [`006937a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/00693790.md#insn-006937a0)
- 新版 [`006937f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/006937e8.md#insn-006937f4)

~~~diff
- 0069379c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 0069379c ["COPY", "tmp:1:8", ["register:4040:8"]]
- 0069379c ["COPY", "tmp:2:8", ["register:4008:8"]]
- 0069379c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0069379c bytes 292000a9
- 006937a0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 006937a0 ["RETURN", null, ["register:0:8"]]
- 006937a0 bytes c0035fd6
+ 006937f4 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 006937f4 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 006937f4 ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 006937f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 006937f4 bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8cb1c6adec733897e012095568d4d9ce"></a>

### [`00693c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/00693c68.md) → [`00693cc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/00693cc0.md) FUN_00693cc0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00693c8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00693c8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00693ce4"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00693c8c",
      "DATA",
      [
        "storage",
        "00c74ad0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00693c90",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00693c94",
      "DATA",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00693ce4",
      "DATA",
      [
        "storage",
        "00c74ba0",
        null,
        "undefined *"
      ]
    ],
    [
      "00693ce8",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00693cec",
      "DATA",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00693c8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/00693c68.md#insn-00693c8c) · [`00693c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/00693c68.md#insn-00693c98)
- 新版 [`00693ce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/00693cc0.md#insn-00693ce4)

~~~diff
- 00693c8c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00693c8c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00693c8c ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00693c8c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00693c8c bytes 082400a9
- 00693c98 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00693c98 ["RETURN", null, ["register:0:8"]]
- 00693c98 bytes c0035fd6
+ 00693ce4 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00693ce4 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00693ce4 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 00693ce4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00693ce4 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3dd341d988c1f8edf9118584c9d9035"></a>

### [`00693c9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/00693c9c.md) → [`00693cf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/00693cf4.md) FUN_00693cf4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00693ca8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00693ca8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00693d00"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00693ca8",
      "DATA",
      [
        "storage",
        "00c74ad0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00693d00",
      "DATA",
      [
        "storage",
        "00c74ba0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00693ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/00693c9c.md#insn-00693ca8) · [`00693cac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/00693c9c.md#insn-00693cac)
- 新版 [`00693d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/00693cf4.md#insn-00693d00)

~~~diff
- 00693ca8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00693ca8 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00693ca8 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00693ca8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00693ca8 bytes 292000a9
- 00693cac ["COPY", "register:0:8", ["register:40f0:8"]]
- 00693cac ["RETURN", null, ["register:0:8"]]
- 00693cac bytes c0035fd6
+ 00693d00 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00693d00 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 00693d00 ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 00693d00 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00693d00 bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-226a388daba1d6d2caf3d468b1b1e292"></a>

### [`00693d38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/00693d38.md) → [`00693d90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/00693d90.md) FUN_00693d90

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00693d5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00693d5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00693db4"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00693d5c",
      "DATA",
      [
        "storage",
        "00c74b50",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00693d60",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00693d64",
      "DATA",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00693db4",
      "DATA",
      [
        "storage",
        "00c74c20",
        null,
        "undefined *"
      ]
    ],
    [
      "00693db8",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00693dbc",
      "DATA",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00693d5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/00693d38.md#insn-00693d5c) · [`00693d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/00693d38.md#insn-00693d68)
- 新版 [`00693db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/00693d90.md#insn-00693db4)

~~~diff
- 00693d5c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00693d5c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00693d5c ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00693d5c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00693d5c bytes 082400a9
- 00693d68 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00693d68 ["RETURN", null, ["register:0:8"]]
- 00693d68 bytes c0035fd6
+ 00693db4 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00693db4 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00693db4 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 00693db4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00693db4 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1b9527775d35a45d59a4a3292fc4513"></a>

### [`00693d6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/00693d6c.md) → [`00693dc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/00693dc4.md) FUN_00693dc4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00693d78"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00693d78"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00693dd0"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00693d78",
      "DATA",
      [
        "storage",
        "00c74b50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00693dd0",
      "DATA",
      [
        "storage",
        "00c74c20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00693d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/00693d6c.md#insn-00693d78) · [`00693d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/00693d6c.md#insn-00693d7c)
- 新版 [`00693dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00693/00693dc4.md#insn-00693dd0)

~~~diff
- 00693d78 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00693d78 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00693d78 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00693d78 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00693d78 bytes 292000a9
- 00693d7c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00693d7c ["RETURN", null, ["register:0:8"]]
- 00693d7c bytes c0035fd6
+ 00693dd0 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00693dd0 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 00693dd0 ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 00693dd0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00693dd0 bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c623459ab9cd9aa7292a0640d9cde91d"></a>

### [`00694290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694290.md) → [`006942e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/006942e8.md) FUN_006942e8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 38.46% / 新版 38.46%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00694290"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00694290"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00694294"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00694290",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00694294",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:006942b4",
      "DATA",
      [
        "storage",
        "00c74bc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006942e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "006942ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0069430c",
      "DATA",
      [
        "storage",
        "00c74c90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00694290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694290.md#insn-00694290) · [`00694294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694290.md#insn-00694294) · [`006942b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694290.md#insn-006942b4)

~~~diff
- 00694290 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00694290 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00694290 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00694290 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00694290 bytes fd7bbea9
- 00694294 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00694294 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00694294 bytes f30b00f9
- 006942b4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 006942b4 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 006942b4 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 006942b4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 006942b4 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb22656dccb89f392a5f2257bdebc07e"></a>

### [`006942c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/006942c4.md) → [`0069431c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/0069431c.md) FUN_0069431c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006942d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006942d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00694328"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006942d0",
      "DATA",
      [
        "storage",
        "00c74bc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00694328",
      "DATA",
      [
        "storage",
        "00c74c90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006942d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/006942c4.md#insn-006942d0) · [`006942d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/006942c4.md#insn-006942d4)
- 新版 [`00694328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/0069431c.md#insn-00694328)

~~~diff
- 006942d0 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 006942d0 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 006942d0 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 006942d0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 006942d0 bytes 292000a9
- 006942d4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 006942d4 ["RETURN", null, ["register:0:8"]]
- 006942d4 bytes c0035fd6
+ 00694328 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00694328 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 00694328 ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 00694328 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00694328 bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9cde5dea028be84a889003b4b80b88d2"></a>

### [`006942e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/006942e0.md) → [`00694338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694338.md) FUN_00694338

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 16.67% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006942f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00694348"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "006942fc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006942f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:006942fc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "00694348",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00694354",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006942f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/006942e0.md#insn-006942f0) · [`006942fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/006942e0.md#insn-006942fc)
- 新版 [`00694348`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694338.md#insn-00694348)

~~~diff
- 006942f0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 006942f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 006942f0 bytes f30b00f9
- 006942fc ["INT_ADD", "register:40f0:8", ["const:6942fc:8", "const:4:8"]]
- 006942fc ["CALL", null, ["ram:47acf4:8"]]
- 006942fc bytes 7e9af797
+ 00694348 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
+ 00694348 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 00694348 bytes f30b00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b809cf81c3aa78a8c11086336f9f097e"></a>

### [`0069434c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/0069434c.md) → [`006943a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/006943a4.md) FUN_006943a4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00694370"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00694370"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006943c8"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00694370",
      "DATA",
      [
        "storage",
        "00c74c50",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00694374",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00694378",
      "DATA",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "006943c8",
      "DATA",
      [
        "storage",
        "00c74d20",
        null,
        "undefined *"
      ]
    ],
    [
      "006943cc",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "006943d0",
      "DATA",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00694370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/0069434c.md#insn-00694370) · [`0069437c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/0069434c.md#insn-0069437c)
- 新版 [`006943c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/006943a4.md#insn-006943c8)

~~~diff
- 00694370 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00694370 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00694370 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00694370 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00694370 bytes 082400a9
- 0069437c ["COPY", "register:0:8", ["register:40f0:8"]]
- 0069437c ["RETURN", null, ["register:0:8"]]
- 0069437c bytes c0035fd6
+ 006943c8 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 006943c8 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 006943c8 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 006943c8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 006943c8 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ae840621f85d1e3d0288f06e1bd3d43"></a>

### [`00694380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694380.md) → [`006943d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/006943d8.md) FUN_006943d8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0069438c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0069438c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006943e4"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0069438c",
      "DATA",
      [
        "storage",
        "00c74c50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006943e4",
      "DATA",
      [
        "storage",
        "00c74d20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0069438c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694380.md#insn-0069438c) · [`00694390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694380.md#insn-00694390)
- 新版 [`006943e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/006943d8.md#insn-006943e4)

~~~diff
- 0069438c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 0069438c ["COPY", "tmp:1:8", ["register:4040:8"]]
- 0069438c ["COPY", "tmp:2:8", ["register:4008:8"]]
- 0069438c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0069438c bytes 292000a9
- 00694390 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00694390 ["RETURN", null, ["register:0:8"]]
- 00694390 bytes c0035fd6
+ 006943e4 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 006943e4 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 006943e4 ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 006943e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 006943e4 bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0e1c6c02d7c391f4a8370cd425c444a"></a>

### [`00694480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694480.md) → [`006944d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/006944d8.md) FUN_006944d8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 38.46% / 新版 38.46%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00694480"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00694480"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00694484"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00694480",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00694484",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:006944a4",
      "DATA",
      [
        "storage",
        "00c74cd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006944d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "006944dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "006944fc",
      "DATA",
      [
        "storage",
        "00c74da0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00694480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694480.md#insn-00694480) · [`00694484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694480.md#insn-00694484) · [`006944a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694480.md#insn-006944a4)

~~~diff
- 00694480 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00694480 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00694480 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00694480 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00694480 bytes fd7bbea9
- 00694484 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00694484 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00694484 bytes f30b00f9
- 006944a4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 006944a4 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 006944a4 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 006944a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 006944a4 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a868e049b74264897930ee0b1e66075"></a>

### [`00694a24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694a24.md) → [`00694a7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694a7c.md) FUN_00694a7c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00694a30"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00694a30"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00694a88"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00694a30",
      "DATA",
      [
        "storage",
        "00c74e50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00694a88",
      "DATA",
      [
        "storage",
        "00c74f20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00694a30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694a24.md#insn-00694a30) · [`00694a34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694a24.md#insn-00694a34)
- 新版 [`00694a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694a7c.md#insn-00694a88)

~~~diff
- 00694a30 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00694a30 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00694a30 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00694a30 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00694a30 bytes 292000a9
- 00694a34 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00694a34 ["RETURN", null, ["register:0:8"]]
- 00694a34 bytes c0035fd6
+ 00694a88 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00694a88 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 00694a88 ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 00694a88 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00694a88 bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8fdda277225f19c7cceccd0a6fecba1a"></a>

### [`00694aec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694aec.md) → [`00694b44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00694/00694b44.md) FUN_00694b44

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00694af4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00694b00"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00694b04"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00694af4",
      "DATA",
      [
        "storage",
        "00c74ed0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00694b4c",
      "DATA",
      [
        "storage",
        "00c74fa0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00694af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694aec.md#insn-00694af4) · [`00694b00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694aec.md#insn-00694b00) · [`00694b04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00694/00694aec.md#insn-00694b04)

~~~diff
- 00694af4 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00694af4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00694af4 bytes 280000f9
- 00694b00 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:18:8"]]
- 00694b00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00694b00 bytes 280c00f9
- 00694b04 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:8:8"]]
- 00694b04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00694b04 bytes 2080803c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7bcdf27f84041e2b4d3ef10f9ed01d22"></a>

### [`00696dcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/00696dcc.md) → [`00696e24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696e24.md) FUN_00696e24

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00696df0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00696df4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00696e48"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00696df0",
      "DATA",
      [
        "storage",
        "00c75280",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00696e48",
      "DATA",
      [
        "storage",
        "00c75350",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00696df0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/00696dcc.md#insn-00696df0) · [`00696df4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/00696dcc.md#insn-00696df4)
- 新版 [`00696e48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696e24.md#insn-00696e48)

~~~diff
- 00696df0 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00696df0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00696df0 bytes 080000f9
- 00696df4 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
- 00696df4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00696df4 bytes 0080803c
+ 00696e48 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00696e48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00696e48 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39f1889c8a1f286f2f27dae0205a60cb"></a>

### [`00697168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/00697168.md) → [`006971c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/006971c0.md) FUN_006971c0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`00696e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/00696e24.md) [`0071d1fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071d/0071d1fc.md) [`00720090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00720/00720090.md) [`0090dcfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0090d/0090dcfc.md) [`0094726c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00947/0094726c.md) · 呼出先 5件 [`00697290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/00697290.md) [`00b3be94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3be94.md) [`00b3bf20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3bf20.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 5件 [`00696e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00696/00696e7c.md) [`0071d254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071d/0071d254.md) [`007200e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00720/007200e8.md) [`0090dd50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0090d/0090dd50.md) [`009472c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00947/009472c0.md) · 呼出先 5件 [`006972e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/006972e8.md) [`00b3bf30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3bf30.md) [`00b3bfbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3bfbc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.61% / 新版 96.61%

CFGの説明率　旧版 66.67% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00697238"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00697290"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00697238",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006972e4"
      ]
    ]
  ],
  "added": [
    [
      "00697290",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006972e4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00697238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/00697168.md#insn-00697238) · [`0069719c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/00697168.md#insn-0069719c)
- 新版 [`00697290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/006971c0.md#insn-00697290) · [`006971f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/006971c0.md#insn-006971f4)

~~~diff
- 00697238 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00697238 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00697238 bytes a1020054
+ 00697290 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00697290 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
+ 00697290 bytes a1020054
- 0069719c ["INT_ADD", "register:40f0:8", ["const:69719c:8", "const:4:8"]]
- 0069719c ["CALL", null, ["callee:00b3bf30:8"]]
+ 006971f4 ["INT_ADD", "register:40f0:8", ["const:6971f4:8", "const:4:8"]]
+ 006971f4 ["CALL", null, ["callee:00b3bf30:8"]]
- 0069719c bytes 3e931294
+ 006971f4 bytes 4f931294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f938db3f144d88f0a7fff6434d54dc5"></a>

### [`00697290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/00697290.md) → [`006972e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/006972e8.md) FUN_006972e8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`00697168`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/00697168.md) [`0071e394`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071e/0071e394.md) [`0071e5c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071e/0071e5c0.md) [`0071e834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071e/0071e834.md) · 呼出先 6件 [`00767148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00767/00767148.md) [`00767cb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00767/00767cb4.md) [`007696b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/007696b4.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 4件 [`006971c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/006971c0.md) [`0071e3ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071e/0071e3ec.md) [`0071e618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071e/0071e618.md) [`0071e88c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071e/0071e88c.md) · 呼出先 6件 [`007671a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00767/007671a0.md) [`00767d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00767/00767d0c.md) [`0076970c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00769/0076970c.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 91.94% / 新版 91.94%

CFGの説明率　旧版 53.85% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006972c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00697318"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "006972c4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006972c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:006972c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007696b4"
      ]
    ]
  ],
  "added": [
    [
      "00697318",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "0069731c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0076970c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006972c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/00697290.md#insn-006972c0) · [`006972c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/00697290.md#insn-006972c4)
- 新版 [`00697318`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/006972e8.md#insn-00697318)

~~~diff
- 006972c0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 006972c0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 006972c0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 006972c0 bytes a8831ff8
- 006972c4 ["INT_ADD", "register:40f0:8", ["const:6972c4:8", "const:4:8"]]
- 006972c4 ["CALL", null, ["ram:7696b4:8"]]
- 006972c4 bytes fc480394
+ 00697318 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00697318 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
+ 00697318 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 00697318 bytes a8831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1fe93b65c3e98fcc826a12fd6481392f"></a>

### [`006973b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/006973b4.md) → [`0069740c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/0069740c.md) FUN_0069740c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006973d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00697430"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006973d8",
      "DATA",
      [
        "storage",
        "00c75300",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00697430",
      "DATA",
      [
        "storage",
        "00c753d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006973d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/006973b4.md#insn-006973d8) · [`006973c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/006973b4.md#insn-006973c8)
- 新版 [`00697430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/0069740c.md#insn-00697430) · [`00697420`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/0069740c.md#insn-00697420)

~~~diff
- 006973d8 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 006973d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 006973d8 bytes 080000f9
+ 00697430 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00697430 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00697430 bytes 080000f9
- 006973c8 ["INT_ADD", "register:40f0:8", ["const:6973c8:8", "const:4:8"]]
- 006973c8 ["CALL", null, ["callee:00c57f60:8"]]
+ 00697420 ["INT_ADD", "register:40f0:8", ["const:697420:8", "const:4:8"]]
+ 00697420 ["CALL", null, ["callee:00c57f60:8"]]
- 006973c8 bytes b2021794
+ 00697420 bytes d0021794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5c1869c720826308421d519e97ceea5"></a>

### [`006973ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/006973ec.md) → [`00697444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697444.md) FUN_00697444

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006973f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006973fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0069744c"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006973f4",
      "DATA",
      [
        "storage",
        "00c75300",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0069744c",
      "DATA",
      [
        "storage",
        "00c753d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006973f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/006973ec.md#insn-006973f4) · [`006973fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/006973ec.md#insn-006973fc) · [`00697400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/006973ec.md#insn-00697400)

~~~diff
- 006973f4 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 006973f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 006973f4 bytes 280000f9
- 006973fc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:8:8"]]
- 006973fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 006973fc bytes 2080803c
- 00697400 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00697400 ["RETURN", null, ["register:0:8"]]
- 00697400 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-319cf5fc2ec729b48038ada7a89ad1cf"></a>

### [`00697dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/00697dbc.md) → [`00697e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697e14.md) FUN_00697e14

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 44.44% / 新版 44.44%

CFGの説明率　旧版 25.00% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00697dcc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00697e24"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00697dcc",
      "DATA",
      [
        "storage",
        "00c75480",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00697e24",
      "DATA",
      [
        "storage",
        "00c75550",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00697dcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/00697dbc.md#insn-00697dcc) · [`00697dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/00697dbc.md#insn-00697dbc)
- 新版 [`00697e24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697e14.md#insn-00697e24)

~~~diff
- 00697dcc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00697dcc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00697dcc bytes 090100f9
+ 00697e24 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00697e24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00697e24 bytes 090100f9
- 00697dbc ["COPY", "register:4040:8", ["register:4000:8"]]
- 00697dbc bytes e80300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95a189e4a822929cfe95654690b6f783"></a>

### [`00697de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/00697de0.md) → [`00697e38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697e38.md) FUN_00697e38

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00697dec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00697e44"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00697dec",
      "DATA",
      [
        "storage",
        "00c75480",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00697e44",
      "DATA",
      [
        "storage",
        "00c75550",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00697dec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/00697de0.md#insn-00697dec) · [`00697de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/00697de0.md#insn-00697de0)
- 新版 [`00697e44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00697/00697e38.md#insn-00697e44)

~~~diff
- 00697dec ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00697dec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00697dec bytes 090000f9
+ 00697e44 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00697e44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00697e44 bytes 090000f9
- 00697de0 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:20:8"]]
- 00697de0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00697de0 bytes 081040f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26577b338b97c4c27d0ed71e7655f234"></a>

### [`0069884c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00698/0069884c.md) → [`006988a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/006988a4.md) FUN_006988a4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 57.14% / 新版 57.14%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00698870"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00698874"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006988c8"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00698870",
      "DATA",
      [
        "storage",
        "00c75580",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00698878",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0069887c",
      "DATA",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "006988c8",
      "DATA",
      [
        "storage",
        "00c75650",
        null,
        "undefined *"
      ]
    ],
    [
      "006988d0",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "006988d4",
      "DATA",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00698870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00698/0069884c.md#insn-00698870) · [`00698874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00698/0069884c.md#insn-00698874) · [`00698880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00698/0069884c.md#insn-00698880)

~~~diff
- 00698870 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00698870 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00698870 bytes 080000f9
- 00698874 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
- 00698874 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00698874 bytes 0080803c
- 00698880 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00698880 ["RETURN", null, ["register:0:8"]]
- 00698880 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b5ab1ad559b5311db70c155925e00e0"></a>

### [`006988a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00698/006988a4.md) → [`006988fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/006988fc.md) FUN_006988fc

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b6f48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f48.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b6fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6fa0.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.00% / 新版 70.00%

CFGの説明率　旧版 31.25% / 新版 35.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006988a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006988a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006988a8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006988a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:006988a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0069892c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:006988f4"
      ]
    ]
  ],
  "added": [
    [
      "006988fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00698900",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0069892c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0069894c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006988a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00698/006988a4.md#insn-006988a4) · [`006988a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00698/006988a4.md#insn-006988a8) · [`006988dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00698/006988a4.md#insn-006988dc)

~~~diff
- 006988a4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 006988a4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 006988a4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 006988a4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 006988a4 bytes fd7bbea9
- 006988a8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 006988a8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 006988a8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 006988a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 006988a8 bytes f44f01a9
- 006988dc ["INT_ADD", "register:40f0:8", ["const:6988dc:8", "const:4:8"]]
- 006988dc ["CALL", null, ["ram:47acf4:8"]]
- 006988dc bytes 0689f797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc97fb2dd425a4bdb55a1988924c11e2"></a>

### [`00698948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00698/00698948.md) → [`006989a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/006989a0.md) FUN_006989a0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 38.46% / 新版 38.46%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00698948"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00698948"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0069894c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00698948",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0069894c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0069896c",
      "DATA",
      [
        "storage",
        "00c75600",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006989a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "006989a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "006989c4",
      "DATA",
      [
        "storage",
        "00c756d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00698948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00698/00698948.md#insn-00698948) · [`0069894c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00698/00698948.md#insn-0069894c) · [`0069896c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00698/00698948.md#insn-0069896c)

~~~diff
- 00698948 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00698948 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00698948 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00698948 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00698948 bytes fd7bbea9
- 0069894c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0069894c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 0069894c bytes f30b00f9
- 0069896c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0069896c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 0069896c ["COPY", "tmp:2:8", ["register:4000:8"]]
- 0069896c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0069896c bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6051ad097a3fd35bb1231d99e8be1b4f"></a>

### [`0069897c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00698/0069897c.md) → [`006989d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/006989d4.md) FUN_006989d4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 20.00% / 新版 20.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00698988"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00698988"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006989e0"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00698988",
      "DATA",
      [
        "storage",
        "00c75600",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006989e0",
      "DATA",
      [
        "storage",
        "00c756d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00698988`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00698/0069897c.md#insn-00698988) · [`0069898c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00698/0069897c.md#insn-0069898c)
- 新版 [`006989e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/006989d4.md#insn-006989e0)

~~~diff
- 00698988 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00698988 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00698988 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00698988 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00698988 bytes 292000a9
- 0069898c ["COPY", "register:0:8", ["register:40f0:8"]]
- 0069898c ["RETURN", null, ["register:0:8"]]
- 0069898c bytes c0035fd6
+ 006989e0 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 006989e0 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 006989e0 ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 006989e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 006989e0 bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e31a9b6909c91075d8fd24d729981ead"></a>

### [`00698a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00698/00698a50.md) → [`00698aa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/00698aa8.md) FUN_00698aa8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00698a58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00698a64"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00698a68"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00698a58",
      "DATA",
      [
        "storage",
        "00c75680",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00698ab0",
      "DATA",
      [
        "storage",
        "00c75750",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00698a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00698/00698a50.md#insn-00698a58) · [`00698a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00698/00698a50.md#insn-00698a64) · [`00698a68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00698/00698a50.md#insn-00698a68)

~~~diff
- 00698a58 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00698a58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00698a58 bytes 280000f9
- 00698a64 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:18:8"]]
- 00698a64 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00698a64 bytes 280c00f9
- 00698a68 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:8:8"]]
- 00698a68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00698a68 bytes 2080803c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17cebc83a72588de7a3625eabe307db7"></a>

### [`00698d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00698/00698d7c.md) → [`00698dd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/00698dd4.md) FUN_00698dd4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00698da0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00698df8"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00698da0",
      "DATA",
      [
        "storage",
        "00c75700",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00698df8",
      "DATA",
      [
        "storage",
        "00c757d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00698da0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00698/00698d7c.md#insn-00698da0) · [`00698d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00698/00698d7c.md#insn-00698d90)
- 新版 [`00698df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/00698dd4.md#insn-00698df8) · [`00698de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/00698dd4.md#insn-00698de8)

~~~diff
- 00698da0 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00698da0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00698da0 bytes 080000f9
+ 00698df8 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00698df8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00698df8 bytes 080000f9
- 00698d90 ["INT_ADD", "register:40f0:8", ["const:698d90:8", "const:4:8"]]
- 00698d90 ["CALL", null, ["callee:00c57f60:8"]]
+ 00698de8 ["INT_ADD", "register:40f0:8", ["const:698de8:8", "const:4:8"]]
+ 00698de8 ["CALL", null, ["callee:00c57f60:8"]]
- 00698d90 bytes 40fc1694
+ 00698de8 bytes 5efc1694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a327fa9b15ef88bff8e4b10880e23e16"></a>

### [`00698db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00698/00698db4.md) → [`00698e0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/00698e0c.md) FUN_00698e0c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00698dbc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00698dc4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00698e14"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00698dbc",
      "DATA",
      [
        "storage",
        "00c75700",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00698e14",
      "DATA",
      [
        "storage",
        "00c757d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00698dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00698/00698db4.md#insn-00698dbc) · [`00698dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00698/00698db4.md#insn-00698dc4) · [`00698dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00698/00698db4.md#insn-00698dc8)

~~~diff
- 00698dbc ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00698dbc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00698dbc bytes 280000f9
- 00698dc4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:8:8"]]
- 00698dc4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00698dc4 bytes 2080803c
- 00698dc8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00698dc8 ["RETURN", null, ["register:0:8"]]
- 00698dc8 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8462aa91a3e571feffd6510e57e8ca0"></a>

### [`00698dd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00698/00698dd4.md) → [`00698e2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/00698e2c.md) FUN_00698e2c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`00688294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00688/00688294.md) [`0068974c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00689/0068974c.md) [`0068ed80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068e/0068ed80.md)
- 新版 呼出元 0件  · 呼出先 12件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`006882d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00688/006882d4.md) [`0068978c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00689/0068978c.md) [`0068edd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0068e/0068edd8.md)

変更の種類 call, call_argument_candidate, call_count, call_target, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 89.06% / 新版 89.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 3件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00698eb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00698f10"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00698e60",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00698e08",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "00698e60",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00698eec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bed8"
      ]
    ],
    [
      "unmatched:00698ea4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071d1fc"
      ]
    ]
  ],
  "added": [
    [
      "00698e60",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00698eec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bf30"
      ]
    ],
    [
      "00698efc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071d254"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00698e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00698/00698dd4.md#insn-00698e08) · [`00698e94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00698/00698dd4.md#insn-00698e94) · [`00698ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00698/00698dd4.md#insn-00698ea4)
- 新版 [`00698e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/00698e2c.md#insn-00698e60) · [`00698eec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00698/00698e2c.md#insn-00698eec)

~~~diff
- 00698e08 ["INT_ADD", "register:40f0:8", ["const:698e08:8", "const:4:8"]]
- 00698e08 ["CALL", null, ["ram:47acf4:8"]]
+ 00698e60 ["INT_ADD", "register:40f0:8", ["const:698e60:8", "const:4:8"]]
+ 00698e60 ["CALL", null, ["ram:47ad34:8"]]
- 00698e08 bytes bb87f797
+ 00698e60 bytes b587f797
- 00698e94 ["INT_ADD", "register:40f0:8", ["const:698e94:8", "const:4:8"]]
- 00698e94 ["CALL", null, ["ram:71bed8:8"]]
+ 00698eec ["INT_ADD", "register:40f0:8", ["const:698eec:8", "const:4:8"]]
+ 00698eec ["CALL", null, ["ram:71bf30:8"]]
- 00698e94 bytes 110c0294
+ 00698eec bytes 110c0294
- 00698ea4 ["INT_ADD", "register:40f0:8", ["const:698ea4:8", "const:4:8"]]
- 00698ea4 ["CALL", null, ["ram:71d1fc:8"]]
- 00698ea4 bytes d6100294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cdd705f4df76911aabde5a7a0d60cf5"></a>

### [`00698ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00698/00698ffc.md) → [`00699054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00699/00699054.md) FUN_00699054

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 38.46% / 新版 38.46%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00698ffc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00698ffc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00699000"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00698ffc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00699000",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00699020",
      "DATA",
      [
        "storage",
        "00c75800",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00699054",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00699058",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00699078",
      "DATA",
      [
        "storage",
        "00c758d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00698ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00698/00698ffc.md#insn-00698ffc) · [`00699000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00698/00698ffc.md#insn-00699000) · [`00699020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00698/00698ffc.md#insn-00699020)

~~~diff
- 00698ffc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00698ffc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00698ffc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00698ffc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00698ffc bytes fd7bbea9
- 00699000 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00699000 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00699000 bytes f30b00f9
- 00699020 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00699020 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00699020 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00699020 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00699020 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5721b0db5ec6af0160de827b9208a2d4"></a>

### [`0069904c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00699/0069904c.md) → [`006990a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00699/006990a4.md) FUN_006990a4

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 13件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`0085b2a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b2a4.md) [`0085b2ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b2ac.md) [`008b6a5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6a5c.md) [`008b6e58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6e58.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`0085b2fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085b2fc.md) [`0085b304`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085b304.md) [`008b6ab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6ab4.md) [`008b6eb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6eb0.md)

変更の種類 call, call_count, constant, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 96.33% / 新版 96.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00699158"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "006991b0"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00699158",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00a46944"
      ]
    ],
    [
      "unmatched:0069917c",
      "DATA",
      [
        "storage",
        "00333fb0",
        null,
        "fde_table_entry"
      ]
    ]
  ],
  "added": [
    [
      "006991b0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00a46944"
      ]
    ],
    [
      "006991d4",
      "DATA",
      [
        "storage",
        "00333fb0",
        null,
        "fde_table_entry"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00699158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00699/0069904c.md#insn-00699158) · [`006991b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00699/0069904c.md#insn-006991b0)
- 新版 [`00699208`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00699/006990a4.md#insn-00699208) · [`006991b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00699/006990a4.md#insn-006991b0)

~~~diff
- 00699158 ["INT_ADD", "register:40f0:8", ["const:699158:8", "const:4:8"]]
- 00699158 ["CALL", null, ["callee:00a46944:8"]]
- 00699158 bytes e6b50e94
- 006991b0 ["INT_ADD", "register:40f0:8", ["const:6991b0:8", "const:4:8"]]
- 006991b0 ["CALL", null, ["callee:008b6efc:8"]]
+ 00699208 ["INT_ADD", "register:40f0:8", ["const:699208:8", "const:4:8"]]
+ 00699208 ["CALL", null, ["callee:008b6efc:8"]]
- 006991b0 bytes 3d770894
+ 00699208 bytes 3d770894
+ 006991b0 ["INT_ADD", "register:40f0:8", ["const:6991b0:8", "const:4:8"]]
+ 006991b0 ["CALL", null, ["callee:00a46944:8"]]
+ 006991b0 bytes e5b50e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-866e6ceb38a28453fe8b3945aaa29e6e"></a>

### [`0069922c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00699/0069922c.md) → [`00699284`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00699/00699284.md) FUN_00699284

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00699250"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00699250"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006992a8"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00699250",
      "DATA",
      [
        "storage",
        "00c75880",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00699254",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00699258",
      "DATA",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "006992a8",
      "DATA",
      [
        "storage",
        "00c75950",
        null,
        "undefined *"
      ]
    ],
    [
      "006992ac",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "006992b0",
      "DATA",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00699250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00699/0069922c.md#insn-00699250) · [`0069925c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00699/0069922c.md#insn-0069925c)
- 新版 [`006992a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00699/00699284.md#insn-006992a8)

~~~diff
- 00699250 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00699250 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00699250 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00699250 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00699250 bytes 082400a9
- 0069925c ["COPY", "register:0:8", ["register:40f0:8"]]
- 0069925c ["RETURN", null, ["register:0:8"]]
- 0069925c bytes c0035fd6
+ 006992a8 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 006992a8 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 006992a8 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 006992a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 006992a8 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99e5106d178cda767ddab22c0540a3f2"></a>

### [`0069a404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069a/0069a404.md) → [`0069a45c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0069a/0069a45c.md) FUN_0069a45c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 44.44% / 新版 36.36%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0069a404"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0069a404"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0069a408"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0069a404",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0069a408",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0069a45c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0069a460",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0069a404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069a/0069a404.md#insn-0069a404) · [`0069a408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069a/0069a404.md#insn-0069a408)
- 新版 [`0069a45c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0069a/0069a45c.md#insn-0069a45c)

~~~diff
- 0069a404 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0069a404 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0069a404 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0069a404 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0069a404 bytes fd7bbea9
- 0069a408 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0069a408 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 0069a408 bytes f30b00f9
+ 0069a45c ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 0069a45c ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 0069a45c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 0069a45c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 0069a45c bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ce95a93143160bb171d977f74238c59"></a>

### [`0069e804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069e/0069e804.md) → [`0069e85c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0069e/0069e85c.md) FUN_0069e85c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009d0320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d0/009d0320.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`009d0374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d0/009d0374.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 85.29% / 新版 85.29%

CFGの説明率　旧版 46.67% / 新版 46.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0069e82c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0069e83c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0069e884"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0069e82c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0069e898"
      ]
    ],
    [
      "unmatched:0069e83c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0069e8bc"
      ]
    ],
    [
      "0069e8ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:0069e834"
      ]
    ]
  ],
  "added": [
    [
      "0069e884",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0069e898"
      ]
    ],
    [
      "0069e894",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0069e8bc"
      ]
    ],
    [
      "0069e8ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0069e88c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0069e82c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069e/0069e804.md#insn-0069e82c) · [`0069e83c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069e/0069e804.md#insn-0069e83c)
- 新版 [`0069e884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0069e/0069e85c.md#insn-0069e884)

~~~diff
- 0069e82c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0069e82c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 0069e82c bytes a1000054
- 0069e83c ["CBRANCH", null, ["local:b9:8", "register:101:1"]]
- 0069e83c bytes 40010054
+ 0069e884 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 0069e884 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 0069e884 bytes a1000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11233e5d52109a3c1e575ba8889a17f3"></a>

### [`0069e88c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069e/0069e88c.md) → [`0069e8e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0069e/0069e8e4.md) FUN_0069e8e4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) · 呼出先 1件 [`006a27cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a2/006a27cc.md)
- 新版 呼出元 1件 [`0089e8d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089e/0089e8d4.md) · 呼出先 1件 [`006a2824`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a2/006a2824.md)

変更の種類 call_argument_candidate, constant, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0069e908",
      "incomplete_value": true,
      "site": "0069e90c",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "old": {
      "definition_site": "0069e8b0",
      "incomplete_value": true,
      "site": "0069e8b4",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0069e8f0",
      "incomplete_value": true,
      "site": "0069e90c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4000:8"
              ],
              [
                "leaf",
                "const:28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`0069e8b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069e/0069e88c.md#insn-0069e8b4) · [`0069e894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069e/0069e88c.md#insn-0069e894)
- 新版 [`0069e90c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0069e/0069e8e4.md#insn-0069e90c) · [`0069e8ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0069e/0069e8e4.md#insn-0069e8ec)

~~~diff
- 0069e8b4 ["INT_ADD", "register:40f0:8", ["const:69e8b4:8", "const:4:8"]]
- 0069e8b4 ["CALL", null, ["callee:006a2824:8"]]
+ 0069e90c ["INT_ADD", "register:40f0:8", ["const:69e90c:8", "const:4:8"]]
+ 0069e90c ["CALL", null, ["callee:006a2824:8"]]
- 0069e8b4 bytes c60f0094
+ 0069e90c bytes c60f0094
- 0069e894 ["COPY", "register:40e8:8", ["register:8:8"]]
- 0069e894 bytes fd030091
+ 0069e8ec ["COPY", "register:40e8:8", ["register:8:8"]]
+ 0069e8ec bytes fd030091
~~~


<a id="compare-b19d62a64955ea662ff7c019a42e7782"></a>

### [`0069e910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069e/0069e910.md) → [`0069e968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0069e/0069e968.md) FUN_0069e968

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0089bc8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089b/0089bc8c.md) [`00a06d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06d9c.md) · 呼出先 10件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0063495c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00634/0063495c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`0089bce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089b/0089bce4.md) [`00a06df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a06df0.md) · 呼出先 10件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0063499c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00634/0063499c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 82.47% / 新版 82.47%

CFGの説明率　旧版 60.00% / 新版 61.76%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0069e990"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0069e9ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0069ea00"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0069e9ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0069eae0"
      ]
    ],
    [
      "unmatched:0069ea10",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0069ea84"
      ]
    ],
    [
      "unmatched:0069ea18",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0069eae8"
      ]
    ]
  ],
  "added": [
    [
      "0069ea44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0069eae0"
      ]
    ],
    [
      "0069ea68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0069ea84"
      ]
    ],
    [
      "0069ea70",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0069eae8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0069e990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069e/0069e910.md#insn-0069e990) · [`0069e9e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069e/0069e910.md#insn-0069e9e8)
- 新版 [`0069e9e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0069e/0069e968.md#insn-0069e9e8)

~~~diff
- 0069e990 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0069e990 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 0069e990 ["COPY", "tmp:2:8", ["register:4048:8"]]
- 0069e990 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 0069e990 bytes 29859f9a
- 0069e9e8 ["INT_RIGHT", "register:4050:8", ["register:4040:8", "const:3e:8"]]
- 0069e9e8 bytes 0afd7ed3
+ 0069e9e8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 0069e9e8 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 0069e9e8 ["COPY", "tmp:2:8", ["register:4048:8"]]
+ 0069e9e8 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
+ 0069e9e8 bytes 29859f9a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fc2969a0d7cea9e734d79e3e1c32b32"></a>

### [`0069ef14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069e/0069ef14.md) → [`0069ef6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0069e/0069ef6c.md) FUN_0069ef6c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 6件 [`0069ec1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069e/0069ec1c.md) [`006b7130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b7/006b7130.md) [`0085408c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00854/0085408c.md) [`008542f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00854/008542f8.md) [`0088a16c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088a/0088a16c.md) · 呼出先 6件 [`0069fd48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069f/0069fd48.md) [`0069fff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069f/0069fff0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md)
- 新版 呼出元 6件 [`0069ec74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0069e/0069ec74.md) [`006b7188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b7/006b7188.md) [`008540e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00854/008540e4.md) [`00854350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00854/00854350.md) [`0088a1c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088a/0088a1c4.md) · 呼出先 6件 [`0069fda0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0069f/0069fda0.md) [`006a0048`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a0/006a0048.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c581b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581b0.md) [`00c581c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581c0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 98.97% / 新版 98.97%

CFGの説明率　旧版 89.66% / 新版 92.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "0069ef80"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "0069efd8"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0069ef80",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "0069efd8",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0069ef80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069e/0069ef14.md#insn-0069ef80) · [`0069ef40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069e/0069ef14.md#insn-0069ef40)
- 新版 [`0069efd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0069e/0069ef6c.md#insn-0069efd8) · [`0069ef98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0069e/0069ef6c.md#insn-0069ef98)

~~~diff
- 0069ef80 ["COPY", "register:0:8", ["register:4040:8"]]
- 0069ef80 ["INT_ADD", "register:40f0:8", ["const:69ef80:8", "const:4:8"]]
- 0069ef80 ["CALLIND", null, ["register:0:8"]]
- 0069ef80 bytes 00013fd6
+ 0069efd8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0069efd8 ["INT_ADD", "register:40f0:8", ["const:69efd8:8", "const:4:8"]]
+ 0069efd8 ["CALLIND", null, ["register:0:8"]]
+ 0069efd8 bytes 00013fd6
- 0069ef40 ["INT_ADD", "register:40f0:8", ["const:69ef40:8", "const:4:8"]]
- 0069ef40 ["CALL", null, ["callee:00c581b0:8"]]
+ 0069ef98 ["INT_ADD", "register:40f0:8", ["const:69ef98:8", "const:4:8"]]
+ 0069ef98 ["CALL", null, ["callee:00c581b0:8"]]
- 0069ef40 bytes 68e41694
+ 0069ef98 bytes 86e41694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f606639900b47dd13861006499f14891"></a>

### [`0069ffdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069f/0069ffdc.md) → [`006a0034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a0/006a0034.md) FUN_006a0034

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0069fd48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069f/0069fd48.md) [`006a35d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a3/006a35d8.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 2件 [`0069fda0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0069f/0069fda0.md) [`006a3630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a3/006a3630.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0069ffdc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0069ffdc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006a0034"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0069ffdc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0069ffe8",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ],
    [
      "unmatched:0069ffec",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0043b7b8"
      ]
    ]
  ],
  "added": [
    [
      "006a0034",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "006a0040",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ],
    [
      "006a0044",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0043b7b8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0069ffdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069f/0069ffdc.md#insn-0069ffdc) · [`0069ffec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069f/0069ffdc.md#insn-0069ffec)
- 新版 [`006a0034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a0/006a0034.md#insn-006a0034)

~~~diff
- 0069ffdc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0069ffdc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0069ffdc ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 0069ffdc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0069ffdc bytes fd7bbfa9
- 0069ffec ["INT_ADD", "register:40f0:8", ["const:69ffec:8", "const:4:8"]]
- 0069ffec ["CALL", null, ["callee:0043b7b8:8"]]
- 0069ffec bytes e36df697
+ 006a0034 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 006a0034 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 006a0034 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 006a0034 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 006a0034 bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89fb760cf1098730ae34d073948193ac"></a>

### [`0069fff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069f/0069fff0.md) → [`006a0048`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a0/006a0048.md) FUN_006a0048

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`0069ef14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069e/0069ef14.md) [`006a2e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a2/006a2e50.md) [`006a31dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a3/006a31dc.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 3件 [`0069ef6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0069e/0069ef6c.md) [`006a2ea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a2/006a2ea8.md) [`006a3234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a3/006a3234.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 96.58% / 新版 96.58%

CFGの説明率　旧版 87.27% / 新版 87.27%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006a0128"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006a0180"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "006a0150"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006a0150",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a0100"
      ]
    ]
  ],
  "added": [
    [
      "006a01a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a0100"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006a0128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069f/0069fff0.md#insn-006a0128) · [`006a0150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069f/0069fff0.md#insn-006a0150) · [`006a0180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069f/0069fff0.md#insn-006a0180)
- 新版 [`006a01d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a0/006a0048.md#insn-006a01d8)

~~~diff
- 006a0128 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:30:8"]]
- 006a0128 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 006a0128 bytes a00e803d
- 006a0150 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 006a0150 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 006a0150 bytes cbfaff54
- 006a0180 ["COPY", "register:0:8", ["register:4040:8"]]
- 006a0180 ["INT_ADD", "register:40f0:8", ["const:6a0180:8", "const:4:8"]]
- 006a0180 ["CALLIND", null, ["register:0:8"]]
+ 006a01d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 006a01d8 ["INT_ADD", "register:40f0:8", ["const:6a01d8:8", "const:4:8"]]
+ 006a01d8 ["CALLIND", null, ["register:0:8"]]
- 006a0180 bytes 00013fd6
+ 006a01d8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-973bf3a297139aad998df0c18e9f0581"></a>

### [`006a0294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a0/006a0294.md) → [`006a02ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a0/006a02ec.md) FUN_006a02ec

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00699908`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00699/00699908.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`006a04a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a0/006a04a8.md) [`006a0660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a0/006a0660.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00699960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00699/00699960.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`006a0500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a0/006a0500.md) [`006a06b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a0/006a06b8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 branch_condition_or_target, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 83.06% / 新版 83.06%

CFGの説明率　旧版 64.71% / 新版 64.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006a02c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006a036c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006a036c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006a02c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:006a0398",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "unmatched:006a03b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "006a031c",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "006a03f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "006a0410",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006a02c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a0/006a0294.md#insn-006a02c4) · [`006a0338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a0/006a0294.md#insn-006a0338)
- 新版 [`006a031c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a0/006a02ec.md#insn-006a031c) · [`006a0390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a0/006a02ec.md#insn-006a0390)

~~~diff
- 006a02c4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 006a02c4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 006a02c4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 006a02c4 bytes a8831ff8
+ 006a031c ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 006a031c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
+ 006a031c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 006a031c bytes a8831ff8
- 006a0338 ["INT_EQUAL", "tmp:0:1", ["register:40b0:8", "const:0:8"]]
- 006a0338 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 006a0390 ["INT_EQUAL", "tmp:0:1", ["register:40b0:8", "const:0:8"]]
+ 006a0390 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 006a0338 bytes f60000b4
+ 006a0390 bytes f60000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec5122eefc55e16a921991cd4e2bc221"></a>

### [`006a155c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a1/006a155c.md) → [`006a15b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a1/006a15b4.md) FUN_006a15b4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0069a504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069a/0069a504.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)
- 新版 呼出元 1件 [`0069a55c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0069a/0069a55c.md) · 呼出先 1件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006a155c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006a155c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006a15b4"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006a155c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:006a1568",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ],
    [
      "unmatched:006a156c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00442970"
      ]
    ]
  ],
  "added": [
    [
      "006a15b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "006a15c0",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ],
    [
      "006a15c4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00442970"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006a155c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a1/006a155c.md#insn-006a155c) · [`006a156c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a1/006a155c.md#insn-006a156c)
- 新版 [`006a15b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a1/006a15b4.md#insn-006a15b4)

~~~diff
- 006a155c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 006a155c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 006a155c ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 006a155c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 006a155c bytes fd7bbfa9
- 006a156c ["INT_ADD", "register:40f0:8", ["const:6a156c:8", "const:4:8"]]
- 006a156c ["CALL", null, ["callee:00442970:8"]]
- 006a156c bytes f184f697
+ 006a15b4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 006a15b4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 006a15b4 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 006a15b4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 006a15b4 bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ee31878bdf534202b9fcdd7718546f6"></a>

### [`006a1570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a1/006a1570.md) → [`006a15c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a1/006a15c8.md) FUN_006a15c8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006a2a90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a2/006a2a90.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`006a2ae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a2/006a2ae8.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 42.86% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "006a15b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "006a1610"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`006a15b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a1/006a1570.md#insn-006a15b8) · [`006a1584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a1/006a1570.md#insn-006a1584)
- 新版 [`006a1610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a1/006a15c8.md#insn-006a1610) · [`006a15dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a1/006a15c8.md#insn-006a15dc)

~~~diff
- 006a15b8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 006a15b8 ["RETURN", null, ["register:0:8"]]
- 006a15b8 bytes c0035fd6
+ 006a1610 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 006a1610 ["RETURN", null, ["register:0:8"]]
+ 006a1610 bytes c0035fd6
- 006a1584 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 006a1584 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 006a15dc ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
+ 006a15dc ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 006a1584 bytes 730100b4
+ 006a15dc bytes 730100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9e3e362df02021de908ea89e600bd90"></a>

### [`006a1ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a1/006a1ea4.md) → [`006a1efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a1/006a1efc.md) FUN_006a1efc

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`006a15bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a1/006a15bc.md) [`006a1ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a1/006a1ea4.md) · 呼出先 6件 [`006a1ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a1/006a1ea4.md) [`006a259c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a2/006a259c.md) [`00800378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/00800378.md) [`008022c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/008022c8.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 2件 [`006a1614`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a1/006a1614.md) [`006a1efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a1/006a1efc.md) · 呼出先 6件 [`006a1efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a1/006a1efc.md) [`006a25f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a2/006a25f4.md) [`008003d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00800/008003d0.md) [`00802320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802320.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 93.72% / 新版 93.72%

CFGの説明率　旧版 42.64% / 新版 42.64%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 4件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006a24f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006a24f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006a2504"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006a21a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a2160"
      ]
    ],
    [
      "006a2498",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:006a256c"
      ]
    ],
    [
      "unmatched:006a24b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a2518"
      ]
    ]
  ],
  "added": [
    [
      "006a2200",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a2160"
      ]
    ],
    [
      "006a2498",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a25c4"
      ]
    ],
    [
      "006a250c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a2518"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006a2124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a1/006a1ea4.md#insn-006a2124) · [`006a2128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a1/006a1ea4.md#insn-006a2128) · [`006a2150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a1/006a1ea4.md#insn-006a2150)
- 新版 [`006a21a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a1/006a1efc.md#insn-006a21a8)

~~~diff
- 006a2124 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 006a2124 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
- 006a2124 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
- 006a2124 ["COPY", "tmp:3:8", ["register:4048:8"]]
- 006a2124 bytes 36c1999a
- 006a2128 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 006a2128 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
- 006a2128 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
- 006a2128 ["COPY", "tmp:3:8", ["register:4040:8"]]
- 006a2128 bytes 1ac19a9a
- 006a2150 ["INT_ADD", "register:40f0:8", ["const:6a2150:8", "const:4:8"]]
- 006a2150 ["CALL", null, ["callee:008003d0:8"]]
+ 006a21a8 ["INT_ADD", "register:40f0:8", ["const:6a21a8:8", "const:4:8"]]
+ 006a21a8 ["CALL", null, ["callee:008003d0:8"]]
- 006a2150 bytes 8a780594
+ 006a21a8 bytes 8a780594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-346255d22b9a725273e45a7373b63173"></a>

### [`006a27cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a2/006a27cc.md) → [`006a2824`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a2/006a2824.md) FUN_006a2824

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0069e88c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069e/0069e88c.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`006a28e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a2/006a28e8.md) [`006a2a90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a2/006a2a90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`0069e8e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0069e/0069e8e4.md) · 呼出先 4件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`006a2940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a2/006a2940.md) [`006a2ae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a2/006a2ae8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 95.77% / 新版 95.77%

CFGの説明率　旧版 86.96% / 新版 83.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006a2858"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006a2858"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006a285c"
    }
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`006a2858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a2/006a27cc.md#insn-006a2858) · [`006a285c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a2/006a27cc.md#insn-006a285c) · [`006a2860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a2/006a27cc.md#insn-006a2860)

~~~diff
- 006a2858 ["COPY", "tmp:0:8", ["const:0:8"]]
- 006a2858 ["COPY", "tmp:1:8", ["const:0:8"]]
- 006a2858 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 006a2858 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 006a2858 bytes 3f7c00a9
- 006a285c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:10:8"]]
- 006a285c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 006a285c bytes 280800f9
- 006a2860 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 006a2860 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:8"]]
- 006a2860 bytes c10200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b6d463b515f91af0b2ab1b2439fc6d0"></a>

### [`006a2b78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a2/006a2b78.md) → [`006a2bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a2/006a2bd0.md) FUN_006a2bd0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 14件 [`0069ec1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0069e/0069ec1c.md) [`006b7130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b7/006b7130.md) [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) [`00846c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00846/00846c50.md) [`00848080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00848/00848080.md) · 呼出先 8件 [`00c57e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e60.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c580d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580d0.md) [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md)
- 新版 呼出元 14件 [`0069ec74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0069e/0069ec74.md) [`006b7188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b7/006b7188.md) [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00846ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00846/00846ca8.md) [`008480d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/008480d8.md) · 呼出先 8件 [`00c57f30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f30.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c581a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581a0.md) [`00c581b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581b0.md) [`00c581c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c581c0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.83% / 新版 97.83%

CFGの説明率　旧版 75.00% / 新版 70.59%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "006a2be8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "006a2c40"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006a2be8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a2c60"
      ]
    ]
  ],
  "added": [
    [
      "006a2c40",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a2c60"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006a2be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a2/006a2b78.md#insn-006a2be8) · [`006a2b8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a2/006a2b78.md#insn-006a2b8c)
- 新版 [`006a2c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a2/006a2bd0.md#insn-006a2c40) · [`006a2be4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a2/006a2bd0.md#insn-006a2be4)

~~~diff
- 006a2be8 ["CBRANCH", null, ["local:b9:8", "register:101:1"]]
- 006a2be8 bytes 00010054
+ 006a2c40 ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
+ 006a2c40 bytes 00010054
- 006a2b8c ["INT_ADD", "register:40f0:8", ["const:6a2b8c:8", "const:4:8"]]
- 006a2b8c ["CALL", null, ["callee:00c581b0:8"]]
+ 006a2be4 ["INT_ADD", "register:40f0:8", ["const:6a2be4:8", "const:4:8"]]
+ 006a2be4 ["CALL", null, ["callee:00c581b0:8"]]
- 006a2b8c bytes 55d51694
+ 006a2be4 bytes 73d51694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50ef15cdc6ea2f67e52c30babb185c03"></a>

### [`006a3878`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a3/006a3878.md) → [`006a38d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a3/006a38d0.md) FUN_006a38d0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006a2d4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a2/006a2d4c.md) · 呼出先 5件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58130.md) [`00c58140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58140.md) [`00c58150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58150.md)
- 新版 呼出元 1件 [`006a2da4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a2/006a2da4.md) · 呼出先 5件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58200.md) [`00c58210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58210.md) [`00c58220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58220.md)

変更の種類 call, call_count, constant, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 97.30% / 新版 97.30%

CFGの説明率　旧版 33.33% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "006a38b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "006a3910"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006a38b8",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "006a3910",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006a38b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a3/006a3878.md#insn-006a38b8) · [`006a38a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a3/006a3878.md#insn-006a38a0)
- 新版 [`006a3910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a3/006a38d0.md#insn-006a3910) · [`006a38f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a3/006a38d0.md#insn-006a38f8)

~~~diff
- 006a38b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 006a38b8 ["INT_ADD", "register:40f0:8", ["const:6a38b8:8", "const:4:8"]]
- 006a38b8 ["CALLIND", null, ["register:0:8"]]
- 006a38b8 bytes 00013fd6
+ 006a3910 ["COPY", "register:0:8", ["register:4040:8"]]
+ 006a3910 ["INT_ADD", "register:40f0:8", ["const:6a3910:8", "const:4:8"]]
+ 006a3910 ["CALLIND", null, ["register:0:8"]]
+ 006a3910 bytes 00013fd6
- 006a38a0 ["INT_ADD", "register:40f0:8", ["const:6a38a0:8", "const:4:8"]]
- 006a38a0 ["CALL", null, ["callee:00c58200:8"]]
+ 006a38f8 ["INT_ADD", "register:40f0:8", ["const:6a38f8:8", "const:4:8"]]
+ 006a38f8 ["CALL", null, ["callee:00c58200:8"]]
- 006a38a0 bytes 24d21694
+ 006a38f8 bytes 42d21694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5ec17e6697dca83c7c1b50de5ed58e0"></a>

### [`006a39b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a3/006a39b8.md) → [`006a3a10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a3/006a3a10.md) FUN_006a3a10

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006a39c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006a39c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006a3a1c"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006a39c4",
      "DATA",
      [
        "storage",
        "00c75980",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006a3a1c",
      "DATA",
      [
        "storage",
        "00c75a50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006a39c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a3/006a39b8.md#insn-006a39c4) · [`006a39c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a3/006a39b8.md#insn-006a39c8)
- 新版 [`006a3a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a3/006a3a10.md#insn-006a3a1c)

~~~diff
- 006a39c4 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 006a39c4 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 006a39c4 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 006a39c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 006a39c4 bytes 292000a9
- 006a39c8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 006a39c8 ["RETURN", null, ["register:0:8"]]
- 006a39c8 bytes c0035fd6
+ 006a3a1c ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 006a3a1c ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 006a3a1c ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 006a3a1c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 006a3a1c bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8fc92aaa8910f65ea179bef3e92229d7"></a>

### [`006a4d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a4/006a4d70.md) → [`006a4dc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a4/006a4dc8.md) FUN_006a4dc8

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00a2b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2b/00a2b2e8.md) · 呼出先 2件 [`00480b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b90.md) [`00480be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480be8.md)
- 新版 呼出元 1件 [`00a2b33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2b/00a2b33c.md) · 呼出先 2件 [`00480bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480bd0.md) [`00480c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480c28.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.22% / 新版 97.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "006a4da8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "006a4e00"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006a4da8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a4e24"
      ]
    ]
  ],
  "added": [
    [
      "006a4e00",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a4e24"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006a4da8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a4/006a4d70.md#insn-006a4da8) · [`006a4d98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a4/006a4d70.md#insn-006a4d98)
- 新版 [`006a4e00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a4/006a4dc8.md#insn-006a4e00) · [`006a4df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a4/006a4dc8.md#insn-006a4df0)

~~~diff
- 006a4da8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 006a4da8 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 006a4da8 bytes 21010054
+ 006a4e00 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 006a4e00 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 006a4e00 bytes 21010054
- 006a4d98 ["INT_ADD", "register:40f0:8", ["const:6a4d98:8", "const:4:8"]]
- 006a4d98 ["CALL", null, ["callee:00480bd0:8"]]
+ 006a4df0 ["INT_ADD", "register:40f0:8", ["const:6a4df0:8", "const:4:8"]]
+ 006a4df0 ["CALL", null, ["callee:00480bd0:8"]]
- 006a4d98 bytes 7e6ff797
+ 006a4df0 bytes 786ff797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-022bd415aed5b55fc45d0a71ee42b27a"></a>

### [`006a4ec8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a4/006a4ec8.md) → [`006a4f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a4/006a4f20.md) FUN_006a4f20

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0090cc54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0090c/0090cc54.md) [`0090dcfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0090d/0090dcfc.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 2件 [`0090cca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0090c/0090cca8.md) [`0090dd50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0090d/0090dd50.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 78.00% / 新版 78.00%

CFGの説明率　旧版 46.90% / 新版 45.69%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 13件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006a4fb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006a5058"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006a50f4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006a4f0c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a4f54"
      ]
    ],
    [
      "unmatched:006a4f5c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a4f9c"
      ]
    ],
    [
      "006a5038",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:006a4ff4"
      ]
    ]
  ],
  "added": [
    [
      "006a4f64",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a4f54"
      ]
    ],
    [
      "006a4fb4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a4f9c"
      ]
    ],
    [
      "006a5038",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a504c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006a4f0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a4/006a4ec8.md#insn-006a4f0c) · [`006a4f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a4/006a4ec8.md#insn-006a4f5c) · [`006a4fac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a4/006a4ec8.md#insn-006a4fac)
- 新版 [`006a5004`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a4/006a4f20.md#insn-006a5004)

~~~diff
- 006a4f0c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 006a4f0c ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
- 006a4f0c ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
- 006a4f0c ["CBRANCH", null, ["local:b2:8", "tmp:2:1"]]
- 006a4f0c bytes 8cffff54
- 006a4f5c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 006a4f5c ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 006a4f5c bytes 48ffffb5
- 006a4fac ["INT_ADD", "register:40f0:8", ["const:6a4fac:8", "const:4:8"]]
- 006a4fac ["CALL", null, ["callee:0043bbe4:8"]]
+ 006a5004 ["INT_ADD", "register:40f0:8", ["const:6a5004:8", "const:4:8"]]
+ 006a5004 ["CALL", null, ["callee:0043bbe4:8"]]
- 006a4fac bytes fe5af697
+ 006a5004 bytes f85af697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e0c2faa2262a5b382d56fe0e01c93c1"></a>

### [`006a53b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a5/006a53b8.md) → [`006a5410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a5/006a5410.md) FUN_006a5410

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) [`0090cc54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0090c/0090cc54.md) [`0090dcfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0090d/0090dcfc.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 3件 [`0089e8d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089e/0089e8d4.md) [`0090cca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0090c/0090cca8.md) [`0090dd50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0090d/0090dd50.md) · 呼出先 2件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 97.14% / 新版 97.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006a5480"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006a5484"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006a54d8"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`006a5480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a5/006a53b8.md#insn-006a5480) · [`006a5484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a5/006a53b8.md#insn-006a5484)
- 新版 [`006a54d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a5/006a5410.md#insn-006a54d8)

~~~diff
- 006a5480 ["INT_ADD", "register:4048:8", ["register:4048:8", "const:38:8"]]
- 006a5480 ["STORE", null, ["const:1b1:8", "register:4048:8", "register:5000:16"]]
- 006a5480 bytes 208d833c
- 006a5484 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:30:8"]]
- 006a5484 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 006a5484 bytes 091800f9
+ 006a54d8 ["INT_ADD", "register:4048:8", ["register:4048:8", "const:38:8"]]
+ 006a54d8 ["STORE", null, ["const:1b1:8", "register:4048:8", "register:5000:16"]]
+ 006a54d8 bytes 208d833c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efbbc008e2db074c8003de8f07a23718"></a>

### [`006a54d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a5/006a54d0.md) → [`006a5528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a5/006a5528.md) FUN_006a5528

採用 · 移動量 `+0x58` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009d3af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d3/009d3af4.md) · 呼出先 3件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`009d3b48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d3/009d3b48.md) · 呼出先 3件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 97.86% / 新版 97.86%

CFGの説明率　旧版 71.19% / 新版 71.19%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006a55d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006a55d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006a562c"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006a564c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a568c"
      ]
    ]
  ],
  "added": [
    [
      "006a56a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a568c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006a55d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a5/006a54d0.md#insn-006a55d4) · [`006a55d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a5/006a54d0.md#insn-006a55d8)
- 新版 [`006a562c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a5/006a5528.md#insn-006a562c)

~~~diff
- 006a55d4 ["INT_ADD", "register:4040:8", ["register:4040:8", "const:38:8"]]
- 006a55d4 ["STORE", null, ["const:1b1:8", "register:4040:8", "register:5000:16"]]
- 006a55d4 bytes 008d833c
- 006a55d8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:30:8"]]
- 006a55d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 006a55d8 bytes 081800f9
+ 006a562c ["INT_ADD", "register:4040:8", ["register:4040:8", "const:38:8"]]
+ 006a562c ["STORE", null, ["const:1b1:8", "register:4040:8", "register:5000:16"]]
+ 006a562c bytes 008d833c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09a73add0ac17c23f7a41c7ef60d8dbb"></a>

### [`006a618c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a6/006a618c.md) → [`006a61e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a6/006a61e4.md) FUN_006a61e4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`006a5700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a5/006a5700.md) [`006a618c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a6/006a618c.md) [`0083a120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0083a/0083a120.md) · 呼出先 3件 [`006a618c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a6/006a618c.md) [`006a61dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a6/006a61dc.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`006a5758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a5/006a5758.md) [`006a61e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a6/006a61e4.md) [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) · 呼出先 3件 [`006a61e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a6/006a61e4.md) [`006a6234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a6/006a6234.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call_argument_candidate, constant, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006a6200",
      "incomplete_value": true,
      "site": "006a6204",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "old": {
      "definition_site": "006a61a8",
      "incomplete_value": true,
      "site": "006a61ac",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "live",
            "register:4008:8"
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
      "definition_site": "006a620c",
      "incomplete_value": true,
      "site": "006a6210",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006a6208",
      "incomplete_value": true,
      "site": "006a6210",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`006a61ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a6/006a618c.md#insn-006a61ac) · [`006a61b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a6/006a618c.md#insn-006a61b8) · [`006a61a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a6/006a618c.md#insn-006a61a8)
- 新版 [`006a6204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a6/006a61e4.md#insn-006a6204) · [`006a6210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a6/006a61e4.md#insn-006a6210)

~~~diff
- 006a61ac ["INT_ADD", "register:40f0:8", ["const:6a61ac:8", "const:4:8"]]
- 006a61ac ["CALL", null, ["local:b0:8"]]
+ 006a6204 ["INT_ADD", "register:40f0:8", ["const:6a6204:8", "const:4:8"]]
+ 006a6204 ["CALL", null, ["local:b0:8"]]
- 006a61ac bytes f8ffff97
+ 006a6204 bytes f8ffff97
- 006a61b8 ["INT_ADD", "register:40f0:8", ["const:6a61b8:8", "const:4:8"]]
- 006a61b8 ["CALL", null, ["local:b0:8"]]
+ 006a6210 ["INT_ADD", "register:40f0:8", ["const:6a6210:8", "const:4:8"]]
+ 006a6210 ["CALL", null, ["local:b0:8"]]
- 006a61b8 bytes f5ffff97
+ 006a6210 bytes f5ffff97
- 006a61a8 ["COPY", "register:4008:8", ["register:4040:8"]]
- 006a61a8 bytes e10308aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f2f4833856130cd1be4a000c28ad495"></a>

### [`006a61dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a6/006a61dc.md) → [`006a6234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a6/006a6234.md) FUN_006a6234

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`006a618c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a6/006a618c.md) [`006a61dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a6/006a61dc.md) · 呼出先 3件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`006a61dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a6/006a61dc.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`006a61e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a6/006a61e4.md) [`006a6234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a6/006a6234.md) · 呼出先 3件 [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`006a6234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a6/006a6234.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call_argument_candidate, constant, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006a6250",
      "incomplete_value": true,
      "site": "006a6254",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "old": {
      "definition_site": "006a61f8",
      "incomplete_value": true,
      "site": "006a61fc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "live",
            "register:4008:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`006a61fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a6/006a61dc.md#insn-006a61fc) · [`006a61f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a6/006a61dc.md#insn-006a61f8) · [`006a6208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a6/006a61dc.md#insn-006a6208)
- 新版 [`006a6254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a6/006a6234.md#insn-006a6254) · [`006a6260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a6/006a6234.md#insn-006a6260)

~~~diff
- 006a61fc ["INT_ADD", "register:40f0:8", ["const:6a61fc:8", "const:4:8"]]
- 006a61fc ["CALL", null, ["local:b0:8"]]
+ 006a6254 ["INT_ADD", "register:40f0:8", ["const:6a6254:8", "const:4:8"]]
+ 006a6254 ["CALL", null, ["local:b0:8"]]
- 006a61fc bytes f8ffff97
+ 006a6254 bytes f8ffff97
- 006a61f8 ["COPY", "register:4008:8", ["register:4040:8"]]
- 006a61f8 bytes e10308aa
- 006a6208 ["INT_ADD", "register:40f0:8", ["const:6a6208:8", "const:4:8"]]
- 006a6208 ["CALL", null, ["local:b0:8"]]
+ 006a6260 ["INT_ADD", "register:40f0:8", ["const:6a6260:8", "const:4:8"]]
+ 006a6260 ["CALL", null, ["local:b0:8"]]
- 006a6208 bytes f5ffff97
+ 006a6260 bytes f5ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ca8a0063e56ed46ead33debd1f3815b"></a>

### [`006a6e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a6/006a6e04.md) → [`006a6e5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a6/006a6e5c.md) FUN_006a6e5c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006a74c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a7/006a74c0.md) · 呼出先 4件 [`00811670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00811/00811670.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b2f9b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2f/00b2f9b8.md) [`00b3be94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3be94.md)
- 新版 呼出元 1件 [`006a7518`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a7/006a7518.md) · 呼出先 4件 [`008116c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00811/008116c8.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00b2fa54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2f/00b2fa54.md) [`00b3bf30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3b/00b3bf30.md)

変更の種類 branch_condition_or_target, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 66.15% / 新版 66.15%

CFGの説明率　旧版 5.26% / 新版 5.26%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "006a6f50"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "006a6f74"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "006a6f98"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006a6e34",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00b2fa54"
      ]
    ],
    [
      "unmatched:006a6e3c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00851550"
      ]
    ],
    [
      "unmatched:006a6eb4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00b2fa54"
      ]
    ]
  ],
  "added": [
    [
      "006a6e8c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00b2fa54"
      ]
    ],
    [
      "006a6e94",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00851550"
      ]
    ],
    [
      "006a6f0c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00b2fa54"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006a6e34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a6/006a6e04.md#insn-006a6e34) · [`006a6e3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a6/006a6e04.md#insn-006a6e3c)
- 新版 [`006a6e8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006a6/006a6e5c.md#insn-006a6e8c)

~~~diff
- 006a6e34 ["INT_ADD", "register:40f0:8", ["const:6a6e34:8", "const:4:8"]]
- 006a6e34 ["CALL", null, ["callee:00b2fa54:8"]]
- 006a6e34 bytes e1221294
- 006a6e3c ["INT_ADD", "register:40f0:8", ["const:6a6e3c:8", "const:4:8"]]
- 006a6e3c ["CALL", null, ["callee:00851550:8"]]
- 006a6e3c bytes afa90694
+ 006a6e8c ["INT_ADD", "register:40f0:8", ["const:6a6e8c:8", "const:4:8"]]
+ 006a6e8c ["CALL", null, ["callee:00b2fa54:8"]]
+ 006a6e8c bytes f2221294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04ec34ea0f707b04cba1f251376af035"></a>

### [`006aded8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ad/006aded8.md) → [`006adf30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ad/006adf30.md) FUN_006adf30

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006adefc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006adf54"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006adefc",
      "DATA",
      [
        "storage",
        "00c75a00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006adf54",
      "DATA",
      [
        "storage",
        "00c75ad0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006adefc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ad/006aded8.md#insn-006adefc) · [`006adeec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ad/006aded8.md#insn-006adeec)
- 新版 [`006adf54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ad/006adf30.md#insn-006adf54) · [`006adf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ad/006adf30.md#insn-006adf44)

~~~diff
- 006adefc ["COPY", "tmp:0:8", ["register:4000:8"]]
- 006adefc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 006adefc bytes 080000f9
+ 006adf54 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 006adf54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 006adf54 bytes 080000f9
- 006adeec ["INT_ADD", "register:40f0:8", ["const:6adeec:8", "const:4:8"]]
- 006adeec ["CALL", null, ["callee:00c57f60:8"]]
+ 006adf44 ["INT_ADD", "register:40f0:8", ["const:6adf44:8", "const:4:8"]]
+ 006adf44 ["CALL", null, ["callee:00c57f60:8"]]
- 006adeec bytes e9a71694
+ 006adf44 bytes 07a81694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71a1bee794956ddf43cb0aaa0ccde982"></a>

### [`006af538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006af/006af538.md) → [`006af590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006af/006af590.md) FUN_006af590

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006af55c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006af55c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006af5b4"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006af55c",
      "DATA",
      [
        "storage",
        "00c75ae0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:006af560",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:006af564",
      "DATA",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "006af5b4",
      "DATA",
      [
        "storage",
        "00c75bb0",
        null,
        "undefined *"
      ]
    ],
    [
      "006af5b8",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "006af5bc",
      "DATA",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006af55c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006af/006af538.md#insn-006af55c) · [`006af568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006af/006af538.md#insn-006af568)
- 新版 [`006af5b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006af/006af590.md#insn-006af5b4)

~~~diff
- 006af55c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 006af55c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 006af55c ["COPY", "tmp:2:8", ["register:4000:8"]]
- 006af55c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 006af55c bytes 082400a9
- 006af568 ["COPY", "register:0:8", ["register:40f0:8"]]
- 006af568 ["RETURN", null, ["register:0:8"]]
- 006af568 bytes c0035fd6
+ 006af5b4 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 006af5b4 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 006af5b4 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 006af5b4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 006af5b4 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fae5f2bef40cb6feb024b3e08dc94c1"></a>

### [`006af588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006af/006af588.md) → [`006af5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006af/006af5e0.md) FUN_006af5e0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00ab0ddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ab0/00ab0ddc.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00ab0e4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ab0/00ab0e4c.md)

変更の種類 constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006af5c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006af620"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006af5c8",
      "DATA",
      [
        "storage",
        "00333fcc",
        null,
        "fde_table_entry"
      ]
    ],
    [
      "006af63c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00ab0ddc"
      ]
    ]
  ],
  "added": [
    [
      "006af620",
      "DATA",
      [
        "storage",
        "00333fcc",
        null,
        "fde_table_entry"
      ]
    ],
    [
      "006af63c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00ab0e4c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006af5c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006af/006af588.md#insn-006af5c8) · [`006af598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006af/006af588.md#insn-006af598)
- 新版 [`006af620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006af/006af5e0.md#insn-006af620) · [`006af5f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006af/006af5e0.md#insn-006af5f0)

~~~diff
- 006af5c8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 006af5c8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 006af5c8 ["COPY", "tmp:2:8", ["register:4040:8"]]
- 006af5c8 ["COPY", "tmp:3:8", ["tmp:2:8"]]
- 006af5c8 bytes 1f6828b8
+ 006af620 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 006af620 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 006af620 ["COPY", "tmp:2:8", ["register:4040:8"]]
+ 006af620 ["COPY", "tmp:3:8", ["tmp:2:8"]]
+ 006af620 bytes 1f6828b8
- 006af598 ["INT_ADD", "register:40f0:8", ["const:6af598:8", "const:4:8"]]
- 006af598 ["CALL", null, ["callee:00851550:8"]]
+ 006af5f0 ["INT_ADD", "register:40f0:8", ["const:6af5f0:8", "const:4:8"]]
+ 006af5f0 ["CALL", null, ["callee:00851550:8"]]
- 006af598 bytes d8870694
+ 006af5f0 bytes d8870694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66662eb51ee15191c5b9fa68a01acb92"></a>

### [`006af614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006af/006af614.md) → [`006af66c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006af/006af66c.md) FUN_006af66c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006af638"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006af690"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006af638",
      "DATA",
      [
        "storage",
        "00c75b70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006af690",
      "DATA",
      [
        "storage",
        "00c75c40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006af638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006af/006af614.md#insn-006af638) · [`006af628`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006af/006af614.md#insn-006af628)
- 新版 [`006af690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006af/006af66c.md#insn-006af690) · [`006af680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006af/006af66c.md#insn-006af680)

~~~diff
- 006af638 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 006af638 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 006af638 bytes 080000f9
+ 006af690 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 006af690 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 006af690 bytes 080000f9
- 006af628 ["INT_ADD", "register:40f0:8", ["const:6af628:8", "const:4:8"]]
- 006af628 ["CALL", null, ["callee:00c57f60:8"]]
+ 006af680 ["INT_ADD", "register:40f0:8", ["const:6af680:8", "const:4:8"]]
+ 006af680 ["CALL", null, ["callee:00c57f60:8"]]
- 006af628 bytes 1aa21694
+ 006af680 bytes 38a21694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-310ac634af45c7b4d1c2749cdc268fc4"></a>

### [`006af64c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006af/006af64c.md) → [`006af6a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006af/006af6a4.md) FUN_006af6a4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006af654"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006af65c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006af6ac"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006af654",
      "DATA",
      [
        "storage",
        "00c75b70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006af6ac",
      "DATA",
      [
        "storage",
        "00c75c40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006af654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006af/006af64c.md#insn-006af654) · [`006af65c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006af/006af64c.md#insn-006af65c) · [`006af660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006af/006af64c.md#insn-006af660)

~~~diff
- 006af654 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 006af654 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 006af654 bytes 280000f9
- 006af65c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:8:8"]]
- 006af65c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 006af65c bytes 2080803c
- 006af660 ["COPY", "register:0:8", ["register:40f0:8"]]
- 006af660 ["RETURN", null, ["register:0:8"]]
- 006af660 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c48f7ce6f013caf37d40c7753f8e0af4"></a>

### [`006af6f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006af/006af6f8.md) → [`006af750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006af/006af750.md) FUN_006af750

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 38.46% / 新版 38.46%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006af6f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006af6f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006af6fc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006af6f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:006af6fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:006af71c",
      "DATA",
      [
        "storage",
        "00c75c00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006af750",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "006af754",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "006af774",
      "DATA",
      [
        "storage",
        "00c75cd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006af6f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006af/006af6f8.md#insn-006af6f8) · [`006af6fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006af/006af6f8.md#insn-006af6fc) · [`006af71c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006af/006af6f8.md#insn-006af71c)

~~~diff
- 006af6f8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 006af6f8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 006af6f8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 006af6f8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 006af6f8 bytes fd7bbea9
- 006af6fc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 006af6fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 006af6fc bytes f30b00f9
- 006af71c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 006af71c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 006af71c ["COPY", "tmp:2:8", ["register:4000:8"]]
- 006af71c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 006af71c bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51082820ad17d15b36b5fb2b4541c5a9"></a>

### [`006afa9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006af/006afa9c.md) → [`006afaf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006af/006afaf4.md) FUN_006afaf4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006afaa4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006afaac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006afafc"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006afaa4",
      "DATA",
      [
        "storage",
        "00c75c80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006afafc",
      "DATA",
      [
        "storage",
        "00c75d50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006afaa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006af/006afa9c.md#insn-006afaa4) · [`006afaac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006af/006afa9c.md#insn-006afaac) · [`006afab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006af/006afa9c.md#insn-006afab0)

~~~diff
- 006afaa4 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 006afaa4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 006afaa4 bytes 280000f9
- 006afaac ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:8:8"]]
- 006afaac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 006afaac bytes 2080803c
- 006afab0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 006afab0 ["RETURN", null, ["register:0:8"]]
- 006afab0 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0480806abd781f0808a9fb2425831aee"></a>

### [`006b26b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b2/006b26b8.md) → [`006b2710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b2/006b2710.md) FUN_006b2710

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`007102d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00710/007102d8.md) [`007119f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) · 呼出先 1件 [`00641b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00641/00641b60.md)
- 新版 呼出元 2件 [`00710330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00710/00710330.md) [`00711a48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00711/00711a48.md) · 呼出先 1件 [`00641ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00641/00641ba0.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 44.44% / 新版 44.44%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "006b26cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "006b2724"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "006b26d8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006b26cc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00641b60"
      ]
    ],
    [
      "unmatched:006b26d4",
      "DATA",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "006b2724",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00641ba0"
      ]
    ],
    [
      "006b272c",
      "DATA",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b26cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b2/006b26b8.md#insn-006b26cc) · [`006b26d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b2/006b26b8.md#insn-006b26d8)
- 新版 [`006b2724`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b2/006b2710.md#insn-006b2724)

~~~diff
- 006b26cc ["INT_ADD", "register:40f0:8", ["const:6b26cc:8", "const:4:8"]]
- 006b26cc ["CALL", null, ["ram:641b60:8"]]
- 006b26cc bytes 253dfe97
- 006b26d8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 006b26d8 ["RETURN", null, ["register:0:8"]]
- 006b26d8 bytes c0035fd6
+ 006b2724 ["INT_ADD", "register:40f0:8", ["const:6b2724:8", "const:4:8"]]
+ 006b2724 ["CALL", null, ["ram:641ba0:8"]]
+ 006b2724 bytes 1f3dfe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da195cb0ffc310592ab11a1fab81ab0a"></a>

### [`006b292c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b2/006b292c.md) → [`006b2984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b2/006b2984.md) FUN_006b2984

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0084e59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0084e/0084e59c.md) · 呼出先 1件 [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md)
- 新版 呼出元 1件 [`0084e5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0084e/0084e5f4.md) · 呼出先 1件 [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 80.65% / 新版 80.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b2950"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b295c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006b29a8"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`006b2950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b2/006b292c.md#insn-006b2950) · [`006b295c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b2/006b292c.md#insn-006b295c) · [`006b2984`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b2/006b292c.md#insn-006b2984)
- 新版 [`006b29dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b2/006b2984.md#insn-006b29dc)

~~~diff
- 006b2950 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 006b2950 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 006b2950 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 006b2950 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
- 006b2950 bytes 096828f8
- 006b295c ["COPY", "tmp:0:4", ["const:0:4"]]
- 006b295c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 006b295c ["INT_ADD", "tmp:2:8", ["register:4040:8", "const:8:8"]]
- 006b295c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 006b295c bytes 1f210039
- 006b2984 ["INT_ADD", "register:40f0:8", ["const:6b2984:8", "const:4:8"]]
- 006b2984 ["CALL", null, ["callee:005c17dc:8"]]
+ 006b29dc ["INT_ADD", "register:40f0:8", ["const:6b29dc:8", "const:4:8"]]
+ 006b29dc ["CALL", null, ["callee:005c17dc:8"]]
- 006b2984 bytes 863bfc97
+ 006b29dc bytes 803bfc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0da844b64f2acb2d3574e96cdd5fc7e0"></a>

### [`006b7670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b7/006b7670.md) → [`006b76c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b7/006b76c8.md) FUN_006b76c8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`006b750c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b7/006b750c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`006b7564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b7/006b7564.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b7670"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b7670"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b7674"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006b7670",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:006b7674",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "006b76c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "006b76cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b7670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b7/006b7670.md#insn-006b7670) · [`006b7674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b7/006b7670.md#insn-006b7674)
- 新版 [`006b76c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b7/006b76c8.md#insn-006b76c8)

~~~diff
- 006b7670 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 006b7670 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 006b7670 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 006b7670 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 006b7670 bytes fd7bbea9
- 006b7674 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 006b7674 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 006b7674 bytes f30b00f9
+ 006b76c8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 006b76c8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 006b76c8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 006b76c8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 006b76c8 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a56a7f960d9adf2196726eaabce7b10"></a>

### [`006b79ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b7/006b79ac.md) → [`006b7a04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b7/006b7a04.md) FUN_006b7a04

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b79c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006b7a1c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "006b79cc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006b79c4",
      "DATA",
      [
        "storage",
        "00c75e90",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:006b79c8",
      "DATA",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "006b7a1c",
      "DATA",
      [
        "storage",
        "00c75f60",
        null,
        "undefined *"
      ]
    ],
    [
      "006b7a20",
      "DATA",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b79c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b7/006b79ac.md#insn-006b79c4) · [`006b79cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b7/006b79ac.md#insn-006b79cc)
- 新版 [`006b7a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b7/006b7a04.md#insn-006b7a1c)

~~~diff
- 006b79c4 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 006b79c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 006b79c4 bytes 080000f9
- 006b79cc ["COPY", "register:0:8", ["register:40f0:8"]]
- 006b79cc ["RETURN", null, ["register:0:8"]]
- 006b79cc bytes c0035fd6
+ 006b7a1c ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 006b7a1c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 006b7a1c bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bd790c6e6e9537144c1ade2f7097822"></a>

### [`006b7b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b7/006b7b30.md) → [`006b7b88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b7/006b7b88.md) FUN_006b7b88

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b7b48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006b7ba0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "006b7b50"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006b7b48",
      "DATA",
      [
        "storage",
        "00c75fa0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:006b7b4c",
      "DATA",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "006b7ba0",
      "DATA",
      [
        "storage",
        "00c76070",
        null,
        "undefined *"
      ]
    ],
    [
      "006b7ba4",
      "DATA",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b7b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b7/006b7b30.md#insn-006b7b48) · [`006b7b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b7/006b7b30.md#insn-006b7b50)
- 新版 [`006b7ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b7/006b7b88.md#insn-006b7ba0)

~~~diff
- 006b7b48 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 006b7b48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 006b7b48 bytes 080000f9
- 006b7b50 ["COPY", "register:0:8", ["register:40f0:8"]]
- 006b7b50 ["RETURN", null, ["register:0:8"]]
- 006b7b50 bytes c0035fd6
+ 006b7ba0 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 006b7ba0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 006b7ba0 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e58b74f5ccc91bc2f4e4672c8c6b8e52"></a>

### [`006b8094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b8/006b8094.md) → [`006b80ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b8/006b80ec.md) FUN_006b80ec

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b80b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b80b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006b8110"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006b80b8",
      "DATA",
      [
        "storage",
        "00c760a0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:006b80bc",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:006b80c0",
      "DATA",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "006b8110",
      "DATA",
      [
        "storage",
        "00c76170",
        null,
        "undefined *"
      ]
    ],
    [
      "006b8114",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "006b8118",
      "DATA",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b80b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b8/006b8094.md#insn-006b80b8) · [`006b80c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b8/006b8094.md#insn-006b80c4)
- 新版 [`006b8110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b8/006b80ec.md#insn-006b8110)

~~~diff
- 006b80b8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 006b80b8 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 006b80b8 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 006b80b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 006b80b8 bytes 082400a9
- 006b80c4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 006b80c4 ["RETURN", null, ["register:0:8"]]
- 006b80c4 bytes c0035fd6
+ 006b8110 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 006b8110 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 006b8110 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 006b8110 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 006b8110 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a160000944f576520d064c5f2220615"></a>

### [`006b80c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b8/006b80c8.md) → [`006b8120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b8/006b8120.md) FUN_006b8120

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b80d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b80d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006b8128"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006b80d0",
      "DATA",
      [
        "storage",
        "00c760a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006b8128",
      "DATA",
      [
        "storage",
        "00c76170",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b80d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b8/006b80c8.md#insn-006b80d0) · [`006b80d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b8/006b80c8.md#insn-006b80d8) · [`006b80dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b8/006b80c8.md#insn-006b80dc)

~~~diff
- 006b80d0 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 006b80d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 006b80d0 bytes 280000f9
- 006b80d8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:8:8"]]
- 006b80d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 006b80d8 bytes 280400f9
- 006b80dc ["COPY", "register:0:8", ["register:40f0:8"]]
- 006b80dc ["RETURN", null, ["register:0:8"]]
- 006b80dc bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22ecc2d8c64227cc5c8a0815bfd3472c"></a>

### [`006ba4d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ba/006ba4d4.md) → [`006ba52c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ba/006ba52c.md) FUN_006ba52c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006b8f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b8/006b8f60.md) [`006b99e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b9/006b99e4.md) [`006ba540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ba/006ba540.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`006b8fb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b8/006b8fb8.md) [`006b9a3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b9/006b9a3c.md) [`006ba598`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ba/006ba598.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 74.07% / 新版 74.07%

CFGの説明率　旧版 46.15% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006ba4d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006ba4e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006ba4e0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006ba4dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006ba594"
      ]
    ],
    [
      "unmatched:006ba4e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:006ba4e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "006ba534",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006ba594"
      ]
    ],
    [
      "006ba538",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "006ba53c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ba4d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ba/006ba4d4.md#insn-006ba4d8) · [`006ba4dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ba/006ba4d4.md#insn-006ba4dc) · [`006ba4e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ba/006ba4d4.md#insn-006ba4e0)

~~~diff
- 006ba4d8 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 006ba4d8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 006ba4d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 006ba4d8 bytes 1f0000f9
- 006ba4dc ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 006ba4dc ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 006ba4dc bytes 090300b4
- 006ba4e0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 006ba4e0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 006ba4e0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 006ba4e0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 006ba4e0 bytes fd7bbda9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c131b14ba2955809cf7d6a29ba63ebc6"></a>

### [`006bf630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006bf/006bf630.md) → [`006bf688`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bf/006bf688.md) FUN_006bf688

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 6件 [`006bbc98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006bb/006bbc98.md) [`00720090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00720/00720090.md) [`0088c870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088c/0088c870.md) [`0090dcfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0090d/0090dcfc.md) [`0094726c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00947/0094726c.md) · 呼出先 3件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md) [`00c5a840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a840.md)
- 新版 呼出元 6件 [`006bbcf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bb/006bbcf0.md) [`007200e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00720/007200e8.md) [`0088c8c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c8c8.md) [`0090dd50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0090d/0090dd50.md) [`009472c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00947/009472c0.md) · 呼出先 3件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md) [`00c5a910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a910.md)

変更の種類 call_argument_candidate, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 91.18% / 新版 91.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006bf660"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006bf664"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006bf6b8"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006bf664",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "006bf6bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006bf660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006bf/006bf630.md#insn-006bf660) · [`006bf664`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006bf/006bf630.md#insn-006bf664) · [`006bf670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006bf/006bf630.md#insn-006bf670)
- 新版 [`006bf6c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bf/006bf688.md#insn-006bf6c8)

~~~diff
- 006bf660 ["COPY", "tmp:0:4", ["const:0:4"]]
- 006bf660 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 006bf660 ["INT_ADD", "register:40a0:8", ["register:40a0:8", "const:8:8"]]
- 006bf660 ["STORE", null, ["const:1b1:8", "register:40a0:8", "tmp:1:4"]]
- 006bf660 bytes 9f8e00b8
- 006bf664 ["COPY", "tmp:0:8", ["register:8:8"]]
- 006bf664 ["COPY", "tmp:1:4", ["const:0:4"]]
- 006bf664 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:4"]]
- 006bf664 bytes ff0300b9
- 006bf670 ["INT_ADD", "register:40f0:8", ["const:6bf670:8", "const:4:8"]]
- 006bf670 ["CALL", null, ["callee:00c5a900:8"]]
+ 006bf6c8 ["INT_ADD", "register:40f0:8", ["const:6bf6c8:8", "const:4:8"]]
+ 006bf6c8 ["CALL", null, ["callee:00c5a900:8"]]
- 006bf670 bytes 706c1694
+ 006bf6c8 bytes 8e6c1694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b662af016174a64a9acda18087120b3"></a>

### [`006c0370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c0/006c0370.md) → [`006c03c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c0/006c03c8.md) FUN_006c03c8

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 11.11% / 新版 11.11%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006c0370"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006c0370"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006c0388"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006c0370",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:006c037c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57f60"
      ]
    ],
    [
      "unmatched:006c0388",
      "DATA",
      [
        "storage",
        "00c76220",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006c03c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "006c03d4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57f60"
      ]
    ],
    [
      "006c03e0",
      "DATA",
      [
        "storage",
        "00c762f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006c0370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c0/006c0370.md#insn-006c0370) · [`006c037c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c0/006c0370.md#insn-006c037c) · [`006c0388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c0/006c0370.md#insn-006c0388)

~~~diff
- 006c0370 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 006c0370 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 006c0370 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 006c0370 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 006c0370 bytes fd7bbfa9
- 006c037c ["INT_ADD", "register:40f0:8", ["const:6c037c:8", "const:4:8"]]
- 006c037c ["CALL", null, ["callee:00c57f60:8"]]
- 006c037c bytes c55e1694
- 006c0388 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 006c0388 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 006c0388 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43ce33669feaaad4c5b03ab37598c14e"></a>

### [`006c0394`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c0/006c0394.md) → [`006c03ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c0/006c03ec.md) FUN_006c03ec

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006c039c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006c03f4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "006c03a0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006c039c",
      "DATA",
      [
        "storage",
        "00c76220",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006c03f4",
      "DATA",
      [
        "storage",
        "00c762f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006c039c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c0/006c0394.md#insn-006c039c) · [`006c03a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c0/006c0394.md#insn-006c03a0)
- 新版 [`006c03f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c0/006c03ec.md#insn-006c03f4)

~~~diff
- 006c039c ["COPY", "tmp:0:8", ["register:4008:8"]]
- 006c039c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 006c039c bytes 280000f9
- 006c03a0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 006c03a0 ["RETURN", null, ["register:0:8"]]
- 006c03a0 bytes c0035fd6
+ 006c03f4 ["COPY", "tmp:0:8", ["register:4008:8"]]
+ 006c03f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 006c03f4 bytes 280000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf3e618fedd5f3556e460c285855ba7f"></a>

### [`006c4fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c4/006c4fb4.md) → [`006c500c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c5/006c500c.md) FUN_006c500c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`008db6f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008db/008db6f4.md) [`008f2694`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f2/008f2694.md) [`008f39a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008f3/008f39a8.md) · 呼出先 0件 
- 新版 呼出元 3件 [`008db748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008db/008db748.md) [`008f26e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f2/008f26e8.md) [`008f39fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008f3/008f39fc.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 74.07% / 新版 74.07%

CFGの説明率　旧版 35.29% / 新版 35.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "006c5010"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "006c5068"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "006c4fc8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006c503c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:006c5018"
      ]
    ],
    [
      "unmatched:006c5010",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006c5058"
      ]
    ]
  ],
  "added": [
    [
      "006c503c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006c5070"
      ]
    ],
    [
      "006c5068",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006c5058"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006c4fc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c4/006c4fb4.md#insn-006c4fc8) · [`006c5010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c4/006c4fb4.md#insn-006c5010)
- 新版 [`006c5068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c5/006c500c.md#insn-006c5068)

~~~diff
- 006c4fc8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 006c4fc8 ["RETURN", null, ["register:0:8"]]
- 006c4fc8 bytes c0035fd6
- 006c5010 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 006c5010 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 006c5010 bytes 81ffff54
+ 006c5068 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 006c5068 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 006c5068 bytes 81ffff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab4f173d0e8b280cdeef04782da7b0d7"></a>

### [`006d66d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d6/006d66d8.md) → [`006d6730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d6/006d6730.md) FUN_006d6730

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006d635c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d6/006d635c.md) · 呼出先 1件 [`006d635c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d6/006d635c.md)
- 新版 呼出元 1件 [`006d63b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d6/006d63b4.md) · 呼出先 1件 [`006d63b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d6/006d63b4.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.70% / 新版 96.70%

CFGの説明率　旧版 89.71% / 新版 85.92%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006d6828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d6/006d66d8.md#insn-006d6828) · [`006d6840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d6/006d66d8.md#insn-006d6840) · [`006d6970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d6/006d66d8.md#insn-006d6970)
- 新版 [`006d6880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d6/006d6730.md#insn-006d6880) · [`006d6898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d6/006d6730.md#insn-006d6898)

~~~diff
- 006d6828 ["INT_ADD", "register:40f0:8", ["const:6d6828:8", "const:4:8"]]
- 006d6828 ["CALL", null, ["callee:006d63b4:8"]]
+ 006d6880 ["INT_ADD", "register:40f0:8", ["const:6d6880:8", "const:4:8"]]
+ 006d6880 ["CALL", null, ["callee:006d63b4:8"]]
- 006d6828 bytes cdfeff97
+ 006d6880 bytes cdfeff97
- 006d6840 ["INT_ADD", "register:40f0:8", ["const:6d6840:8", "const:4:8"]]
- 006d6840 ["CALL", null, ["callee:006d63b4:8"]]
+ 006d6898 ["INT_ADD", "register:40f0:8", ["const:6d6898:8", "const:4:8"]]
+ 006d6898 ["CALL", null, ["callee:006d63b4:8"]]
- 006d6840 bytes c7feff97
+ 006d6898 bytes c7feff97
- 006d6970 ["COPY", "tmp:0:8", ["const:1:8"]]
- 006d6970 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d6970 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d6970 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d6970 bytes 0c050091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-020715147d117cf8e2e9d1e856df35cc"></a>

### [`006d69b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d6/006d69b0.md) → [`006d6a08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d6/006d6a08.md) FUN_006d6a08

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`006d635c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d6/006d635c.md) [`006d69b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d6/006d69b0.md) · 呼出先 1件 [`006d69b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d6/006d69b0.md)
- 新版 呼出元 2件 [`006d63b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d6/006d63b4.md) [`006d6a08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d6/006d6a08.md) · 呼出先 1件 [`006d6a08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d6/006d6a08.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 92.23% / 新版 92.23%

CFGの説明率　旧版 67.97% / 新版 68.42%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 9件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006d69c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006d69c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006d69c4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006d69c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:006d69c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:006d69c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "006d6a18",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "006d6a1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "006d6a20",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d69c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d6/006d69b0.md#insn-006d69c0) · [`006d69c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d6/006d69b0.md#insn-006d69c4) · [`006d69c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d6/006d69b0.md#insn-006d69c8)

~~~diff
- 006d69c0 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 006d69c0 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 006d69c0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 006d69c0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 006d69c0 bytes f85f03a9
- 006d69c4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 006d69c4 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 006d69c4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 006d69c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 006d69c4 bytes f65704a9
- 006d69c8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 006d69c8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 006d69c8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 006d69c8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 006d69c8 bytes f44f05a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98af1cfacdbec23071ed1e0c8f8c5846"></a>

### [`006d9834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d9/006d9834.md) → [`006d988c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d9/006d988c.md) FUN_006d988c

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 38.46% / 新版 38.46%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006d9834"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006d9834"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006d9838"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006d9834",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:006d9838",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:006d9858",
      "DATA",
      [
        "storage",
        "00c76598",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d988c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "006d9890",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "006d98b0",
      "DATA",
      [
        "storage",
        "00c76668",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d9834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d9/006d9834.md#insn-006d9834) · [`006d9838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d9/006d9834.md#insn-006d9838) · [`006d9858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d9/006d9834.md#insn-006d9858)

~~~diff
- 006d9834 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 006d9834 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 006d9834 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 006d9834 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 006d9834 bytes fd7bbea9
- 006d9838 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 006d9838 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 006d9838 bytes f30b00f9
- 006d9858 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 006d9858 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 006d9858 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 006d9858 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 006d9858 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3840663e681ac01f58ac1dd8f2c85062"></a>

### [`006d996c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d9/006d996c.md) → [`006d99c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d9/006d99c4.md) FUN_006d99c4

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 38.46% / 新版 38.46%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006d996c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006d996c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006d9970"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006d996c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:006d9970",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:006d9990",
      "DATA",
      [
        "storage",
        "00c76618",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d99c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "006d99c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "006d99e8",
      "DATA",
      [
        "storage",
        "00c766e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d996c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d9/006d996c.md#insn-006d996c) · [`006d9970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d9/006d996c.md#insn-006d9970) · [`006d9990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d9/006d996c.md#insn-006d9990)

~~~diff
- 006d996c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 006d996c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 006d996c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 006d996c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 006d996c bytes fd7bbea9
- 006d9970 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 006d9970 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 006d9970 bytes f30b00f9
- 006d9990 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 006d9990 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 006d9990 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 006d9990 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 006d9990 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a41655fd35e0098143d5d6942ec87ef"></a>

### [`006d9a98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d9/006d9a98.md) → [`006d9af0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d9/006d9af0.md) FUN_006d9af0

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006d9abc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006d9abc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006d9b14"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006d9abc",
      "DATA",
      [
        "storage",
        "00c76698",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:006d9ac0",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:006d9ac4",
      "DATA",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "006d9b14",
      "DATA",
      [
        "storage",
        "00c76768",
        null,
        "undefined *"
      ]
    ],
    [
      "006d9b18",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "006d9b1c",
      "DATA",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d9abc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d9/006d9a98.md#insn-006d9abc) · [`006d9ac8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d9/006d9a98.md#insn-006d9ac8)
- 新版 [`006d9b14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d9/006d9af0.md#insn-006d9b14)

~~~diff
- 006d9abc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 006d9abc ["COPY", "tmp:1:8", ["register:4048:8"]]
- 006d9abc ["COPY", "tmp:2:8", ["register:4000:8"]]
- 006d9abc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 006d9abc bytes 082400a9
- 006d9ac8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 006d9ac8 ["RETURN", null, ["register:0:8"]]
- 006d9ac8 bytes c0035fd6
+ 006d9b14 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 006d9b14 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 006d9b14 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 006d9b14 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 006d9b14 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-708a53d1f122243e05867cbe4831f22b"></a>

### [`006da620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006da/006da620.md) → [`006da678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006da/006da678.md) FUN_006da678

採用 · 移動量 `+0x58` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006da644"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006da644"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006da69c"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006da644",
      "DATA",
      [
        "storage",
        "00c76898",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:006da648",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:006da64c",
      "DATA",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "006da69c",
      "DATA",
      [
        "storage",
        "00c76968",
        null,
        "undefined *"
      ]
    ],
    [
      "006da6a0",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "006da6a4",
      "DATA",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006da644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006da/006da620.md#insn-006da644) · [`006da650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006da/006da620.md#insn-006da650)
- 新版 [`006da69c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006da/006da678.md#insn-006da69c)

~~~diff
- 006da644 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 006da644 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 006da644 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 006da644 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 006da644 bytes 082400a9
- 006da650 ["COPY", "register:0:8", ["register:40f0:8"]]
- 006da650 ["RETURN", null, ["register:0:8"]]
- 006da650 bytes c0035fd6
+ 006da69c ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 006da69c ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 006da69c ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 006da69c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 006da69c bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f4e1b0d234c53d17ca3c60f93711667"></a>

### [`006dc904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006dc/006dc904.md) → [`006dc95c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006dc/006dc95c.md) FUN_006dc95c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006dd724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006dd/006dd724.md) · 呼出先 0件 
- 新版 呼出元 1件 [`006dd77c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006dd/006dd77c.md) · 呼出先 0件 

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 73.33% / 新版 73.33%

CFGの説明率　旧版 16.67% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006dc938"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006dc990"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "006dc91c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006dc91c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006dc994"
      ]
    ],
    [
      "unmatched:006dc934",
      "DATA",
      [
        "storage",
        "002e19b8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "006dc974",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006dc994"
      ]
    ],
    [
      "006dc98c",
      "DATA",
      [
        "storage",
        "002e19f8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006dc91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006dc/006dc904.md#insn-006dc91c) · [`006dc938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006dc/006dc904.md#insn-006dc938)
- 新版 [`006dc974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006dc/006dc95c.md#insn-006dc974)

~~~diff
- 006dc91c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 006dc91c ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 006dc91c ["CBRANCH", null, ["local:b4:8", "tmp:1:1"]]
- 006dc91c bytes 08010054
- 006dc938 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
- 006dc938 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 006dc938 bytes 080800b9
+ 006dc974 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 006dc974 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 006dc974 ["CBRANCH", null, ["local:b4:8", "tmp:1:1"]]
+ 006dc974 bytes 08010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1ab2bc99ef70d6658f355a34d645a27"></a>

### [`006de714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006de/006de714.md) → [`006de76c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006de/006de76c.md) FUN_006de76c

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006f24d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006f2/006f24d4.md) · 呼出先 3件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046d7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`006f252c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006f2/006f252c.md) · 呼出先 3件 [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0046d7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d7f0.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.55% / 新版 96.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006de71c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006de/006de714.md#insn-006de71c) · [`006de72c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006de/006de714.md#insn-006de72c) · [`006de748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006de/006de714.md#insn-006de748)
- 新版 [`006de784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006de/006de76c.md#insn-006de784) · [`006de7a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006de/006de76c.md#insn-006de7a0)

~~~diff
- 006de71c ["COPY", "register:40e8:8", ["register:8:8"]]
- 006de71c bytes fd030091
- 006de72c ["INT_ADD", "register:40f0:8", ["const:6de72c:8", "const:4:8"]]
- 006de72c ["CALL", null, ["callee:0046d7f0:8"]]
+ 006de784 ["INT_ADD", "register:40f0:8", ["const:6de784:8", "const:4:8"]]
+ 006de784 ["CALL", null, ["callee:0046d7f0:8"]]
- 006de72c bytes 213cf697
+ 006de784 bytes 1b3cf697
- 006de748 ["INT_ADD", "register:40f0:8", ["const:6de748:8", "const:4:8"]]
- 006de748 ["CALL", null, ["callee:00851550:8"]]
+ 006de7a0 ["INT_ADD", "register:40f0:8", ["const:6de7a0:8", "const:4:8"]]
+ 006de7a0 ["CALL", null, ["callee:00851550:8"]]
- 006de748 bytes 6ccb0594
+ 006de7a0 bytes 6ccb0594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-627c1ed1d709f987f17f38128206ae02"></a>

### [`006de788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006de/006de788.md) → [`006de7e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006de/006de7e0.md) FUN_006de7e0

採用 · 移動量 `+0x58` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006dea94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006de/006dea94.md) [`006e1ea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e1/006e1ea8.md) [`006e3320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e3/006e3320.md) · 呼出先 4件 [`006b26ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b2/006b26ec.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`0085b2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b2e0.md) [`009dcecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009dc/009dcecc.md)
- 新版 呼出元 3件 [`006deaec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006de/006deaec.md) [`006e1f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e1/006e1f00.md) [`006e3378`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006e3/006e3378.md) · 呼出先 4件 [`006b2744`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006b2/006b2744.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`0085b338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0085b/0085b338.md) [`009dcf20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009dc/009dcf20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 30.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006de788"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006de788"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006de78c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006de788",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:006de78c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "006de7e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "006de7e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006de788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006de/006de788.md#insn-006de788) · [`006de78c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006de/006de788.md#insn-006de78c)
- 新版 [`006de7e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006de/006de7e0.md#insn-006de7e0)

~~~diff
- 006de788 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 006de788 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 006de788 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 006de788 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 006de788 bytes fd7bbea9
- 006de78c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 006de78c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 006de78c bytes f30b00f9
+ 006de7e0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 006de7e0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 006de7e0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 006de7e0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 006de7e0 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

