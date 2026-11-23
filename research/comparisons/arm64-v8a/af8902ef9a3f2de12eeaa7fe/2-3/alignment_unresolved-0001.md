# v16.0.0 → v16.0.1 · 命令位置の検査未完了 (1)

[一覧の目次](README.md)

<a id="compare-e61122367c850ea41852fface8c47899"></a>

### [`0048d240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048d240.md) → [`0048d280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048d280.md) FUN_0048d280

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0085b0f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085b0f8.md) · 呼出先 0件 
- 新版 呼出元 1件 [`0085b138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b138.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0048d28c",
      "READ",
      [
        "storage",
        "00ca4888",
        null,
        "undefined4"
      ]
    ],
    [
      "0048d294",
      "READ",
      [
        "storage",
        "00ca4878",
        null,
        "undefined4"
      ]
    ],
    [
      "0048d2a0",
      "READ",
      [
        "storage",
        "00ca488c",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0048d28c",
      "READ",
      [
        "storage",
        "00ca4c88",
        null,
        "undefined4"
      ]
    ],
    [
      "0048d294",
      "READ",
      [
        "storage",
        "00ca4c78",
        null,
        "undefined4"
      ]
    ],
    [
      "0048d2a0",
      "READ",
      [
        "storage",
        "00ca4c8c",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048d244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048d240.md#insn-0048d244) · [`0048d250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048d240.md#insn-0048d250)
- 新版 `0048d284`（命令位置の公開資料なし） · `0048d290`（命令位置の公開資料なし）

~~~diff
- 0048d244 ["COPY", "tmp:0:8", ["const:870:8"]]
- 0048d244 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0048d244 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0048d244 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0048d284 ["COPY", "tmp:0:8", ["const:c70:8"]]
+ 0048d284 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0048d284 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0048d284 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0048d244 bytes 08c12191
+ 0048d284 bytes 08c13191
- 0048d250 ["INT_MULT", "tmp:0:4", ["register:4050:4", "register:4048:4"]]
- 0048d250 ["INT_ZEXT", "register:4048:8", ["tmp:0:4"]]
- 0048d250 bytes 497d091b
+ 0048d290 ["INT_MULT", "tmp:0:4", ["register:4050:4", "register:4048:4"]]
+ 0048d290 ["INT_ZEXT", "register:4048:8", ["tmp:0:4"]]
+ 0048d290 bytes 497d091b
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5766aa81cfe74ddbc3f37aa396134320"></a>

### [`00493aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493aec.md) → [`00493b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00493/00493b2c.md) FUN_00493b2c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0093b5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093b/0093b5d4.md) · 呼出先 3件 [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c581f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c581f0.md) [`00c58200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58200.md)
- 新版 呼出元 1件 [`0093b770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0093b/0093b770.md) · 呼出先 3件 [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c585f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c585f0.md) [`00c58600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58600.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00493bc8",
      "PARAM",
      [
        "storage",
        "002af81d",
        null,
        null
      ]
    ],
    [
      "00493bd0",
      "PARAM",
      [
        "storage",
        "002a8a0e",
        null,
        null
      ]
    ],
    [
      "00493bd0",
      "PARAM",
      [
        "storage",
        "002af81a",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00493bc8",
      "PARAM",
      [
        "storage",
        "002af85d",
        null,
        null
      ]
    ],
    [
      "00493bd0",
      "PARAM",
      [
        "storage",
        "002a8adb",
        null,
        null
      ]
    ],
    [
      "00493bd0",
      "PARAM",
      [
        "storage",
        "002af85a",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00493b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493aec.md#insn-00493b3c) · [`00493b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493aec.md#insn-00493b60) · [`00493b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493aec.md#insn-00493b64)
- 新版 `00493b7c`（命令位置の公開資料なし） · `00493ba0`（命令位置の公開資料なし）

~~~diff
- 00493b3c ["INT_ADD", "register:40f0:8", ["const:493b3c:8", "const:4:8"]]
- 00493b3c ["CALL", null, ["callee:00c585f0:8"]]
+ 00493b7c ["INT_ADD", "register:40f0:8", ["const:493b7c:8", "const:4:8"]]
+ 00493b7c ["CALL", null, ["callee:00c585f0:8"]]
- 00493b3c bytes ad111f94
+ 00493b7c bytes 9d121f94
- 00493b60 ["COPY", "tmp:0:8", ["const:81a:8"]]
- 00493b60 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
- 00493b60 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
- 00493b60 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
+ 00493ba0 ["COPY", "tmp:0:8", ["const:85a:8"]]
+ 00493ba0 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
+ 00493ba0 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
+ 00493ba0 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
- 00493b60 bytes d66a2091
+ 00493ba0 bytes d66a2191
- 00493b64 ["COPY", "register:40b8:8", ["const:2be000:8"]]
- 00493b64 bytes 57f1fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6017e1e81e536b1b871d1b4536ef71e8"></a>

### [`004b5108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5108.md) → [`004b5148`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b5/004b5148.md) _ZN5Botan10hex_encodeEPKhmb

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c587a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c587a0.md) · 呼出先 3件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)
- 新版 呼出元 1件 [`00c58ba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58ba0.md) · 呼出先 3件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004b5224",
      "DATA",
      [
        "storage",
        "002c3090",
        null,
        "string"
      ]
    ],
    [
      "004b5224",
      "DATA",
      [
        "storage",
        "002c21b0",
        null,
        null
      ]
    ],
    [
      "004b522c",
      "DATA",
      [
        "storage",
        "002c3090",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004b5224",
      "DATA",
      [
        "storage",
        "002c30d0",
        null,
        "string"
      ]
    ],
    [
      "004b5224",
      "DATA",
      [
        "storage",
        "002c21f0",
        null,
        null
      ]
    ],
    [
      "004b522c",
      "DATA",
      [
        "storage",
        "002c30d0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b517c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5108.md#insn-004b517c) · [`004b519c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5108.md#insn-004b519c) · [`004b51b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5108.md#insn-004b51b4)
- 新版 `004b51bc`（命令位置の公開資料なし） · `004b51dc`（命令位置の公開資料なし） · `004b51f4`（命令位置の公開資料なし）

~~~diff
- 004b517c ["INT_ADD", "register:40f0:8", ["const:4b517c:8", "const:4:8"]]
- 004b517c ["CALL", null, ["callee:00c57e90:8"]]
+ 004b51bc ["INT_ADD", "register:40f0:8", ["const:4b51bc:8", "const:4:8"]]
+ 004b51bc ["CALL", null, ["callee:00c57e90:8"]]
- 004b517c bytes 458a1e94
+ 004b51bc bytes 358b1e94
- 004b519c ["INT_ADD", "register:40f0:8", ["const:4b519c:8", "const:4:8"]]
- 004b519c ["CALL", null, ["callee:00c58090:8"]]
+ 004b51dc ["INT_ADD", "register:40f0:8", ["const:4b51dc:8", "const:4:8"]]
+ 004b51dc ["CALL", null, ["callee:00c58090:8"]]
- 004b519c bytes bd8a1e94
+ 004b51dc bytes ad8b1e94
- 004b51b4 ["COPY", "tmp:0:8", ["const:1b0:8"]]
- 004b51b4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004b51b4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004b51b4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 004b51f4 ["COPY", "tmp:0:8", ["const:1f0:8"]]
+ 004b51f4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 004b51f4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 004b51f4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004b51b4 bytes 4ac10691
+ 004b51f4 bytes 4ac10791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be3b227b820fa2e1b5b02061ffb3fb23"></a>

### [`004b6650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b6/004b6650.md) → [`004b6690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b6/004b6690.md) _ZN5Botan10hex_encodeEPcPKhmb

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
      "004b66c0",
      "DATA",
      [
        "storage",
        "002c3090",
        null,
        "string"
      ]
    ],
    [
      "004b66c0",
      "DATA",
      [
        "storage",
        "002c21b0",
        null,
        null
      ]
    ],
    [
      "004b66c8",
      "DATA",
      [
        "storage",
        "002c3090",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004b66c0",
      "DATA",
      [
        "storage",
        "002c30d0",
        null,
        "string"
      ]
    ],
    [
      "004b66c0",
      "DATA",
      [
        "storage",
        "002c21f0",
        null,
        null
      ]
    ],
    [
      "004b66c8",
      "DATA",
      [
        "storage",
        "002c30d0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b6650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b6/004b6650.md#insn-004b6650) · [`004b6654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b6/004b6650.md#insn-004b6654) · [`004b665c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b6/004b6650.md#insn-004b665c)
- 新版 `004b6694`（命令位置の公開資料なし）

~~~diff
- 004b6650 ["COPY", "register:4040:8", ["const:2c3000:8"]]
- 004b6650 bytes 68f0ffb0
- 004b6654 ["COPY", "tmp:0:8", ["const:90:8"]]
- 004b6654 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004b6654 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004b6654 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004b6694 ["COPY", "tmp:0:8", ["const:d0:8"]]
+ 004b6694 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004b6694 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004b6694 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004b6654 bytes 08410291
+ 004b6694 bytes 08410391
- 004b665c ["COPY", "register:4048:8", ["const:2c2000:8"]]
- 004b665c bytes 69f0ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f92b6d3a4ec664bac4c24c2861f9d68c"></a>

### [`004cfe24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cfe24.md) → [`004cfe64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004cf/004cfe64.md) _ZNK5Botan13PKCS7_Padding5unpadEPKhm

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
      "004cfecc",
      "READ",
      [
        "storage",
        "002c2340",
        null,
        null
      ]
    ],
    [
      "004cfed0",
      "READ",
      [
        "storage",
        "002c2150",
        null,
        null
      ]
    ],
    [
      "004cfed4",
      "READ",
      [
        "storage",
        "002c2b30",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004cfecc",
      "READ",
      [
        "storage",
        "002c2380",
        null,
        null
      ]
    ],
    [
      "004cfed0",
      "READ",
      [
        "storage",
        "002c2190",
        null,
        null
      ]
    ],
    [
      "004cfed4",
      "READ",
      [
        "storage",
        "002c2b70",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004cfe8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cfe24.md#insn-004cfe8c) · [`004cfe90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cfe24.md#insn-004cfe90) · [`004cfe94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cfe24.md#insn-004cfe94)
- 新版 `004cfecc`（命令位置の公開資料なし） · `004cfed0`（命令位置の公開資料なし） · `004cfed4`（命令位置の公開資料なし）

~~~diff
- 004cfe8c ["INT_ADD", "tmp:0:8", ["register:4070:8", "const:340:8"]]
- 004cfe8c ["LOAD", "register:50a0:16", ["const:1b1:8", "tmp:0:8"]]
- 004cfe8c ["COPY", "register:50b0:8", ["const:0:8"]]
- 004cfe8c ["COPY", "register:50b8:8", ["const:0:8"]]
+ 004cfecc ["INT_ADD", "tmp:0:8", ["register:4070:8", "const:380:8"]]
+ 004cfecc ["LOAD", "register:50a0:16", ["const:1b1:8", "tmp:0:8"]]
+ 004cfecc ["COPY", "register:50b0:8", ["const:0:8"]]
+ 004cfecc ["COPY", "register:50b8:8", ["const:0:8"]]
- 004cfe8c bytes c5d1c03d
+ 004cfecc bytes c5e1c03d
- 004cfe90 ["INT_ADD", "tmp:0:8", ["register:4068:8", "const:150:8"]]
- 004cfe90 ["LOAD", "register:50c0:16", ["const:1b1:8", "tmp:0:8"]]
- 004cfe90 ["COPY", "register:50d0:8", ["const:0:8"]]
- 004cfe90 ["COPY", "register:50d8:8", ["const:0:8"]]
+ 004cfed0 ["INT_ADD", "tmp:0:8", ["register:4068:8", "const:190:8"]]
+ 004cfed0 ["LOAD", "register:50c0:16", ["const:1b1:8", "tmp:0:8"]]
+ 004cfed0 ["COPY", "register:50d0:8", ["const:0:8"]]
+ 004cfed0 ["COPY", "register:50d8:8", ["const:0:8"]]
- 004cfe90 bytes a655c03d
+ 004cfed0 bytes a665c03d
- 004cfe94 ["INT_ADD", "tmp:0:8", ["register:4058:8", "const:b30:8"]]
- 004cfe94 ["LOAD", "register:50e0:16", ["const:1b1:8", "tmp:0:8"]]
- 004cfe94 ["COPY", "register:50f0:8", ["const:0:8"]]
- 004cfe94 ["COPY", "register:50f8:8", ["const:0:8"]]
+ 004cfed4 ["INT_ADD", "tmp:0:8", ["register:4058:8", "const:b70:8"]]
+ 004cfed4 ["LOAD", "register:50e0:16", ["const:1b1:8", "tmp:0:8"]]
+ 004cfed4 ["COPY", "register:50f0:8", ["const:0:8"]]
+ 004cfed4 ["COPY", "register:50f8:8", ["const:0:8"]]
- 004cfe94 bytes 67cdc23d
+ 004cfed4 bytes 67ddc23d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe643ee1ad2e0546ca48893eab370050"></a>

### [`004d0318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d0318.md) → [`004d0358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d0/004d0358.md) _ZNK5Botan17ANSI_X923_Padding5unpadEPKhm

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
      "004d03bc",
      "READ",
      [
        "storage",
        "002c2340",
        null,
        null
      ]
    ],
    [
      "004d03c0",
      "READ",
      [
        "storage",
        "002c2150",
        null,
        null
      ]
    ],
    [
      "004d03c4",
      "READ",
      [
        "storage",
        "002c2b30",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004d03bc",
      "READ",
      [
        "storage",
        "002c2380",
        null,
        null
      ]
    ],
    [
      "004d03c0",
      "READ",
      [
        "storage",
        "002c2190",
        null,
        null
      ]
    ],
    [
      "004d03c4",
      "READ",
      [
        "storage",
        "002c2b70",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d037c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d0318.md#insn-004d037c) · [`004d0380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d0318.md#insn-004d0380) · [`004d0384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d0318.md#insn-004d0384)
- 新版 `004d03bc`（命令位置の公開資料なし） · `004d03c0`（命令位置の公開資料なし） · `004d03c4`（命令位置の公開資料なし）

~~~diff
- 004d037c ["INT_ADD", "tmp:0:8", ["register:4068:8", "const:340:8"]]
- 004d037c ["LOAD", "register:50a0:16", ["const:1b1:8", "tmp:0:8"]]
- 004d037c ["COPY", "register:50b0:8", ["const:0:8"]]
- 004d037c ["COPY", "register:50b8:8", ["const:0:8"]]
+ 004d03bc ["INT_ADD", "tmp:0:8", ["register:4068:8", "const:380:8"]]
+ 004d03bc ["LOAD", "register:50a0:16", ["const:1b1:8", "tmp:0:8"]]
+ 004d03bc ["COPY", "register:50b0:8", ["const:0:8"]]
+ 004d03bc ["COPY", "register:50b8:8", ["const:0:8"]]
- 004d037c bytes a5d1c03d
+ 004d03bc bytes a5e1c03d
- 004d0380 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:150:8"]]
- 004d0380 ["LOAD", "register:50c0:16", ["const:1b1:8", "tmp:0:8"]]
- 004d0380 ["COPY", "register:50d0:8", ["const:0:8"]]
- 004d0380 ["COPY", "register:50d8:8", ["const:0:8"]]
+ 004d03c0 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:190:8"]]
+ 004d03c0 ["LOAD", "register:50c0:16", ["const:1b1:8", "tmp:0:8"]]
+ 004d03c0 ["COPY", "register:50d0:8", ["const:0:8"]]
+ 004d03c0 ["COPY", "register:50d8:8", ["const:0:8"]]
- 004d0380 bytes 4655c03d
+ 004d03c0 bytes 4665c03d
- 004d0384 ["INT_ADD", "tmp:0:8", ["register:4058:8", "const:b30:8"]]
- 004d0384 ["LOAD", "register:50e0:16", ["const:1b1:8", "tmp:0:8"]]
- 004d0384 ["COPY", "register:50f0:8", ["const:0:8"]]
- 004d0384 ["COPY", "register:50f8:8", ["const:0:8"]]
+ 004d03c4 ["INT_ADD", "tmp:0:8", ["register:4058:8", "const:b70:8"]]
+ 004d03c4 ["LOAD", "register:50e0:16", ["const:1b1:8", "tmp:0:8"]]
+ 004d03c4 ["COPY", "register:50f0:8", ["const:0:8"]]
+ 004d03c4 ["COPY", "register:50f8:8", ["const:0:8"]]
- 004d0384 bytes 67cdc23d
+ 004d03c4 bytes 67ddc23d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4fde29a8dfd3fed185ea2ad1f9ad4540"></a>

### [`004d0920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d0920.md) → [`004d0960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d0/004d0960.md) _ZNK5Botan11ESP_Padding5unpadEPKhm

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
      "004d09c8",
      "READ",
      [
        "storage",
        "002c2340",
        null,
        null
      ]
    ],
    [
      "004d09cc",
      "READ",
      [
        "storage",
        "002c2150",
        null,
        null
      ]
    ],
    [
      "004d09d0",
      "READ",
      [
        "storage",
        "002c2b30",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004d09c8",
      "READ",
      [
        "storage",
        "002c2380",
        null,
        null
      ]
    ],
    [
      "004d09cc",
      "READ",
      [
        "storage",
        "002c2190",
        null,
        null
      ]
    ],
    [
      "004d09d0",
      "READ",
      [
        "storage",
        "002c2b70",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004d0988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d0920.md#insn-004d0988) · [`004d098c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d0920.md#insn-004d098c) · [`004d0990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d0920.md#insn-004d0990)
- 新版 `004d09c8`（命令位置の公開資料なし） · `004d09cc`（命令位置の公開資料なし） · `004d09d0`（命令位置の公開資料なし）

~~~diff
- 004d0988 ["INT_ADD", "tmp:0:8", ["register:4068:8", "const:340:8"]]
- 004d0988 ["LOAD", "register:50a0:16", ["const:1b1:8", "tmp:0:8"]]
- 004d0988 ["COPY", "register:50b0:8", ["const:0:8"]]
- 004d0988 ["COPY", "register:50b8:8", ["const:0:8"]]
+ 004d09c8 ["INT_ADD", "tmp:0:8", ["register:4068:8", "const:380:8"]]
+ 004d09c8 ["LOAD", "register:50a0:16", ["const:1b1:8", "tmp:0:8"]]
+ 004d09c8 ["COPY", "register:50b0:8", ["const:0:8"]]
+ 004d09c8 ["COPY", "register:50b8:8", ["const:0:8"]]
- 004d0988 bytes a5d1c03d
+ 004d09c8 bytes a5e1c03d
- 004d098c ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:150:8"]]
- 004d098c ["LOAD", "register:50c0:16", ["const:1b1:8", "tmp:0:8"]]
- 004d098c ["COPY", "register:50d0:8", ["const:0:8"]]
- 004d098c ["COPY", "register:50d8:8", ["const:0:8"]]
+ 004d09cc ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:190:8"]]
+ 004d09cc ["LOAD", "register:50c0:16", ["const:1b1:8", "tmp:0:8"]]
+ 004d09cc ["COPY", "register:50d0:8", ["const:0:8"]]
+ 004d09cc ["COPY", "register:50d8:8", ["const:0:8"]]
- 004d098c bytes 4655c03d
+ 004d09cc bytes 4665c03d
- 004d0990 ["INT_ADD", "tmp:0:8", ["register:4058:8", "const:b30:8"]]
- 004d0990 ["LOAD", "register:50e0:16", ["const:1b1:8", "tmp:0:8"]]
- 004d0990 ["COPY", "register:50f0:8", ["const:0:8"]]
- 004d0990 ["COPY", "register:50f8:8", ["const:0:8"]]
+ 004d09d0 ["INT_ADD", "tmp:0:8", ["register:4058:8", "const:b70:8"]]
+ 004d09d0 ["LOAD", "register:50e0:16", ["const:1b1:8", "tmp:0:8"]]
+ 004d09d0 ["COPY", "register:50f0:8", ["const:0:8"]]
+ 004d09d0 ["COPY", "register:50f8:8", ["const:0:8"]]
- 004d0990 bytes 67cdc23d
+ 004d09d0 bytes 67ddc23d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35a59b9f78e5b4e6164be02e464a8833"></a>

### [`004feaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fe/004feaf0.md) → [`004feb30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004fe/004feb30.md) _ZN5Botan14version_stringEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "site": "004feb24"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "004feb28"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "004feb28"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004feb54",
      "READ",
      [
        "storage",
        "002bc5ce",
        null,
        "string"
      ]
    ],
    [
      "004feb54",
      "READ",
      [
        "storage",
        "002bc5de",
        null,
        "string"
      ]
    ],
    [
      "004feb58",
      "READ",
      [
        "storage",
        "002c2a70",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004feb54",
      "READ",
      [
        "storage",
        "002bc60e",
        null,
        "string"
      ]
    ],
    [
      "004feb54",
      "READ",
      [
        "storage",
        "002bc61e",
        null,
        "string"
      ]
    ],
    [
      "004feb58",
      "READ",
      [
        "storage",
        "002c2ab0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004feb04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fe/004feaf0.md#insn-004feb04) · [`004feb24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fe/004feaf0.md#insn-004feb24) · [`004feb28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fe/004feaf0.md#insn-004feb28)
- 新版 `004feb44`（命令位置の公開資料なし）

~~~diff
- 004feb04 ["INT_ADD", "register:40f0:8", ["const:4feb04:8", "const:4:8"]]
- 004feb04 ["CALL", null, ["callee:00c57e90:8"]]
+ 004feb44 ["INT_ADD", "register:40f0:8", ["const:4feb44:8", "const:4:8"]]
+ 004feb44 ["CALL", null, ["callee:00c57e90:8"]]
- 004feb04 bytes e3631d94
+ 004feb44 bytes d3641d94
- 004feb24 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 004feb24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5040:16"]]
- 004feb24 bytes 6202803d
- 004feb28 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:40:8"]]
- 004feb28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 004feb28 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 004feb28 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5020:16"]]
- 004feb28 bytes 000402ad
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96559ef8d6faa9a8180d866670027608"></a>

### [`00576694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576694.md) → [`005766d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005766d4.md) FUN_005766d4

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005509c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/005509c0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00550a00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00550/00550a00.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 11.11% / 新版 11.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005766dc",
      "READ",
      [
        "storage",
        "00c9a770",
        null,
        "pointer"
      ]
    ],
    [
      "005766e0",
      "READ",
      [
        "storage",
        "00c9a778",
        null,
        "pointer"
      ]
    ],
    [
      "005766e4",
      "READ",
      [
        "storage",
        "00ca605c",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "005766dc",
      "READ",
      [
        "storage",
        "00c9ab70",
        null,
        "pointer"
      ]
    ],
    [
      "005766e0",
      "READ",
      [
        "storage",
        "00c9ab78",
        null,
        "pointer"
      ]
    ],
    [
      "005766e4",
      "READ",
      [
        "storage",
        "00ca645c",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00576694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576694.md#insn-00576694) · [`00576698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576694.md#insn-00576698) · [`0057669c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576694.md#insn-0057669c)
- 新版 `005766dc`（命令位置の公開資料なし）

~~~diff
- 00576694 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00576694 bytes 28390090
- 00576698 ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 00576698 bytes 29390090
- 0057669c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:770:8"]]
- 0057669c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005766dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b70:8"]]
+ 005766dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0057669c bytes 08b943f9
+ 005766dc bytes 08b945f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c9a1a4d0affbd40d0fb1fd43066f047"></a>

### [`00585020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/00585020.md) → [`00585060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/00585060.md) FUN_00585060

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 7件 [`005851d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/005851d4.md) [`00587c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587c14.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00585214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00585/00585214.md) [`00587c54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00587/00587c54.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.94% / 新版 96.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005850c0",
      "PARAM",
      [
        "storage",
        "00c6c5d0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005850c4",
      "PARAM",
      [
        "storage",
        "00c6c5e0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "005850c0",
      "PARAM",
      [
        "storage",
        "00c6c9d0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "005850c4",
      "PARAM",
      [
        "storage",
        "00c6c9e0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00585058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/00585020.md#insn-00585058) · [`00585060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/00585020.md#insn-00585060) · [`00585064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/00585020.md#insn-00585064)
- 新版 `00585098`（命令位置の公開資料なし） · `005850a4`（命令位置の公開資料なし）

~~~diff
- 00585058 ["COPY", "tmp:0:8", ["const:5d0:8"]]
- 00585058 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 00585058 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 00585058 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 00585098 ["COPY", "tmp:0:8", ["const:9d0:8"]]
+ 00585098 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 00585098 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 00585098 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 00585058 bytes 94421791
+ 00585098 bytes 94422791
- 00585060 ["COPY", "register:40a8:8", ["const:c6c000:8"]]
- 00585060 bytes 353700f0
- 00585064 ["COPY", "tmp:0:8", ["const:5e0:8"]]
- 00585064 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 00585064 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 00585064 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 005850a4 ["COPY", "tmp:0:8", ["const:9e0:8"]]
+ 005850a4 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 005850a4 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 005850a4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 00585064 bytes b5821791
+ 005850a4 bytes b5822791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c11e035a0a9f1e6837838a7d6399f9b1"></a>

### [`0058e520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058e520.md) → [`0058e560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058e/0058e560.md) FUN_0058e560

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589800.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md) [`00589840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589840.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.04% / 新版 96.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0058e5dc",
      "READ",
      [
        "storage",
        "002a9d22",
        null,
        "string"
      ]
    ],
    [
      "0058e5dc",
      "READ",
      [
        "storage",
        "002a9d32",
        null,
        "string"
      ]
    ],
    [
      "0058e5e0",
      "READ",
      [
        "storage",
        "002c2360",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0058e5dc",
      "READ",
      [
        "storage",
        "002a9def",
        null,
        "string"
      ]
    ],
    [
      "0058e5dc",
      "READ",
      [
        "storage",
        "002a9dff",
        null,
        "string"
      ]
    ],
    [
      "0058e5e0",
      "READ",
      [
        "storage",
        "002c23a0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0058e554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058e520.md#insn-0058e554) · [`0058e55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058e520.md#insn-0058e55c) · [`0058e58c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058e520.md#insn-0058e58c)
- 新版 `0058e594`（命令位置の公開資料なし） · `0058e59c`（命令位置の公開資料なし） · `0058e5cc`（命令位置の公開資料なし）

~~~diff
- 0058e554 ["INT_ADD", "register:40f0:8", ["const:58e554:8", "const:4:8"]]
- 0058e554 ["CALL", null, ["callee:00589840:8"]]
+ 0058e594 ["INT_ADD", "register:40f0:8", ["const:58e594:8", "const:4:8"]]
+ 0058e594 ["CALL", null, ["callee:00589840:8"]]
- 0058e554 bytes abecff97
+ 0058e594 bytes abecff97
- 0058e55c ["INT_ADD", "register:40f0:8", ["const:58e55c:8", "const:4:8"]]
- 0058e55c ["CALL", null, ["callee:00588e6c:8"]]
+ 0058e59c ["INT_ADD", "register:40f0:8", ["const:58e59c:8", "const:4:8"]]
+ 0058e59c ["CALL", null, ["callee:00588e6c:8"]]
- 0058e55c bytes 34eaff97
+ 0058e59c bytes 34eaff97
- 0058e58c ["INT_ADD", "register:40f0:8", ["const:58e58c:8", "const:4:8"]]
- 0058e58c ["CALL", null, ["callee:00c57e90:8"]]
+ 0058e5cc ["INT_ADD", "register:40f0:8", ["const:58e5cc:8", "const:4:8"]]
+ 0058e5cc ["CALL", null, ["callee:00c57e90:8"]]
- 0058e58c bytes 41251b94
+ 0058e5cc bytes 31261b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-780af7b8649d641b46924dbdd96269b4"></a>

### [`00595830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595830.md) → [`00595870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595870.md) FUN_00595870

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0059564c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/0059564c.md) [`0059599c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/0059599c.md) [`00595cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595cdc.md) · 呼出先 0件 
- 新版 呼出元 3件 [`0059568c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/0059568c.md) [`005959dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/005959dc.md) [`00595d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00595/00595d1c.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.70% / 新版 96.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005958a0",
      "DATA",
      [
        "storage",
        "002d2fdd",
        "switchD_00595870::switchdataD_002d2fdd",
        "byte"
      ]
    ]
  ],
  "added": [
    [
      "005958a0",
      "DATA",
      [
        "storage",
        "002d301d",
        "switchD_005958b0::switchdataD_002d301d",
        "byte"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00595854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595830.md#insn-00595854) · [`00595858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595830.md#insn-00595858) · [`0059585c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595830.md#insn-0059585c)
- 新版 `00595894`（命令位置の公開資料なし） · `00595898`（命令位置の公開資料なし）

~~~diff
- 00595854 ["COPY", "register:4058:8", ["const:2d2000:8"]]
+ 00595894 ["COPY", "register:4058:8", ["const:2d3000:8"]]
- 00595854 bytes ebe9ffb0
+ 00595894 bytes ebe9ffd0
- 00595858 ["COPY", "tmp:0:8", ["const:fdd:8"]]
- 00595858 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
- 00595858 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
- 00595858 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
+ 00595898 ["COPY", "tmp:0:8", ["const:1d:8"]]
+ 00595898 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
+ 00595898 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
+ 00595898 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
- 00595858 bytes 6b753f91
+ 00595898 bytes 6b750091
- 0059585c ["COPY", "register:4068:8", ["const:595874:8"]]
- 0059585c bytes cd000010
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c4bce210ae4a4f5205c4e4ef653c102"></a>

### [`0063bc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063b/0063bc58.md) → [`0063bc98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063b/0063bc98.md) FUN_0063bc98

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0063d070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063d/0063d070.md) [`0064ec78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064ec78.md) · 呼出先 11件 [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`0046ee18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ee18.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md)
- 新版 呼出元 2件 [`0063d0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0063d/0063d0b0.md) [`0064ecb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064e/0064ecb8.md) · 呼出先 11件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046d7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`0046ee58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046ee58.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md)

変更の種類 call, call_count, call_target, constant, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 92.34% / 新版 92.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 29件, `unresolved_call_alignment` 9件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0063bf94",
      "incomplete_value": true,
      "site": "0063bf9c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0063bf54",
      "incomplete_value": true,
      "site": "0063bf5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0063bcc8",
      "value": [
        "leaf",
        "ram:63b54c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0063bc88",
      "value": [
        "leaf",
        "ram:63b50c:8"
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
      "site": "0063bcf0",
      "value": [
        "leaf",
        "ram:63acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0063bcb0",
      "value": [
        "leaf",
        "ram:63ac74:8"
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
      "0063bcb8",
      "DATA",
      [
        "storage",
        "0042ef64",
        null,
        "byte[43]"
      ]
    ],
    [
      "0063bcc8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0063b50c"
      ]
    ],
    [
      "0063bcdc",
      "DATA",
      [
        "storage",
        "00434788",
        null,
        "byte[47]"
      ]
    ]
  ],
  "added": [
    [
      "0063bcb8",
      "DATA",
      [
        "storage",
        "0042ef64",
        null,
        "byte[39]"
      ]
    ],
    [
      "0063bcc8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0063b54c"
      ]
    ],
    [
      "0063bcdc",
      "DATA",
      [
        "storage",
        "00434788",
        null,
        "byte[43]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0063bc88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063b/0063bc58.md#insn-0063bc88) · [`0063bcb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063b/0063bc58.md#insn-0063bcb0) · [`0063bce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063b/0063bc58.md#insn-0063bce0)
- 新版 `0063bcc8`（命令位置の公開資料なし） · `0063bcf0`（命令位置の公開資料なし） · `0063bd20`（命令位置の公開資料なし）

~~~diff
- 0063bc88 ["INT_ADD", "register:40f0:8", ["const:63bc88:8", "const:4:8"]]
- 0063bc88 ["CALL", null, ["ram:63b50c:8"]]
+ 0063bcc8 ["INT_ADD", "register:40f0:8", ["const:63bcc8:8", "const:4:8"]]
+ 0063bcc8 ["CALL", null, ["ram:63b54c:8"]]
- 0063bc88 bytes 21feff97
+ 0063bcc8 bytes 21feff97
- 0063bcb0 ["INT_ADD", "register:40f0:8", ["const:63bcb0:8", "const:4:8"]]
- 0063bcb0 ["CALL", null, ["ram:63ac74:8"]]
+ 0063bcf0 ["INT_ADD", "register:40f0:8", ["const:63bcf0:8", "const:4:8"]]
+ 0063bcf0 ["CALL", null, ["ram:63acb4:8"]]
- 0063bcb0 bytes f1fbff97
+ 0063bcf0 bytes f1fbff97
- 0063bce0 ["INT_ADD", "register:40f0:8", ["const:63bce0:8", "const:4:8"]]
- 0063bce0 ["CALL", null, ["ram:47acb4:8"]]
+ 0063bd20 ["INT_ADD", "register:40f0:8", ["const:63bd20:8", "const:4:8"]]
+ 0063bd20 ["CALL", null, ["ram:47acf4:8"]]
- 0063bce0 bytes f5fbf897
+ 0063bd20 bytes f5fbf897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6564e756f0583e174633540de6a9318"></a>

### [`0064db88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064d/0064db88.md) → [`0064dbc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064d/0064dbc8.md) FUN_0064dbc8

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006554b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00655/006554b0.md) · 呼出先 12件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00641134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00641/00641134.md) [`00641c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00641/00641c28.md) [`006b70f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b7/006b70f0.md) [`0071be98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071be98.md)
- 新版 呼出元 1件 [`006554f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00655/006554f0.md) · 呼出先 12件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00641174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00641/00641174.md) [`00641c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00641/00641c68.md) [`006b7130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b7/006b7130.md) [`0071bed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071b/0071bed8.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 94.50% / 新版 94.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0064dcc4",
      "value": [
        "leaf",
        "ram:71bed8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0064dc84",
      "value": [
        "leaf",
        "ram:71be98:8"
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
      "site": "0064dcd4",
      "value": [
        "leaf",
        "ram:71d1fc:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0064dc94",
      "value": [
        "leaf",
        "ram:71d1bc:8"
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
      "site": "0064dcdc",
      "value": [
        "leaf",
        "ram:71bed8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0064dc9c",
      "value": [
        "leaf",
        "ram:71be98:8"
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
      "0064dcbc",
      "DATA",
      [
        "storage",
        "0042ef78",
        "fde_0042ef78",
        "dword"
      ]
    ],
    [
      "0064dcc4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071be98"
      ]
    ],
    [
      "0064dcd4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071d1bc"
      ]
    ]
  ],
  "added": [
    [
      "0064dcbc",
      "DATA",
      [
        "storage",
        "0042ef78",
        null,
        "dword"
      ]
    ],
    [
      "0064dcc4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bed8"
      ]
    ],
    [
      "0064dcd4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071d1fc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0064dc84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064d/0064db88.md#insn-0064dc84) · [`0064dc94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064d/0064db88.md#insn-0064dc94) · [`0064dc9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064d/0064db88.md#insn-0064dc9c)
- 新版 `0064dcc4`（命令位置の公開資料なし） · `0064dcd4`（命令位置の公開資料なし） · `0064dcdc`（命令位置の公開資料なし）

~~~diff
- 0064dc84 ["INT_ADD", "register:40f0:8", ["const:64dc84:8", "const:4:8"]]
- 0064dc84 ["CALL", null, ["ram:71be98:8"]]
+ 0064dcc4 ["INT_ADD", "register:40f0:8", ["const:64dcc4:8", "const:4:8"]]
+ 0064dcc4 ["CALL", null, ["ram:71bed8:8"]]
- 0064dc84 bytes 85380394
+ 0064dcc4 bytes 85380394
- 0064dc94 ["INT_ADD", "register:40f0:8", ["const:64dc94:8", "const:4:8"]]
- 0064dc94 ["CALL", null, ["ram:71d1bc:8"]]
+ 0064dcd4 ["INT_ADD", "register:40f0:8", ["const:64dcd4:8", "const:4:8"]]
+ 0064dcd4 ["CALL", null, ["ram:71d1fc:8"]]
- 0064dc94 bytes 4a3d0394
+ 0064dcd4 bytes 4a3d0394
- 0064dc9c ["INT_ADD", "register:40f0:8", ["const:64dc9c:8", "const:4:8"]]
- 0064dc9c ["CALL", null, ["ram:71be98:8"]]
+ 0064dcdc ["INT_ADD", "register:40f0:8", ["const:64dcdc:8", "const:4:8"]]
+ 0064dcdc ["CALL", null, ["ram:71bed8:8"]]
- 0064dc9c bytes 7f380394
+ 0064dcdc bytes 7f380394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d01e96f678e16fac8b9d43f89389ca63"></a>

### [`0064e15c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064e15c.md) → [`0064e19c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064e/0064e19c.md) FUN_0064e19c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0064a4f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064a/0064a4f0.md) [`00653560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00653/00653560.md) · 呼出先 8件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00641134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00641/00641134.md) [`00641c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00641/00641c28.md) [`0071be98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071be98.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`0064a530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0064a/0064a530.md) [`006535a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00653/006535a0.md) · 呼出先 8件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00641174`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00641/00641174.md) [`00641c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00641/00641c68.md) [`0071bed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071b/0071bed8.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

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
      "site": "0064e1d4",
      "value": [
        "leaf",
        "ram:71bed8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0064e194",
      "value": [
        "leaf",
        "ram:71be98:8"
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
      "site": "0064e294",
      "value": [
        "leaf",
        "ram:641c68:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0064e254",
      "value": [
        "leaf",
        "ram:641c28:8"
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
      "site": "0064e2a0",
      "value": [
        "leaf",
        "ram:71bed8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0064e260",
      "value": [
        "leaf",
        "ram:71be98:8"
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
      "0064e1d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071be98"
      ]
    ],
    [
      "0064e294",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00641c28"
      ]
    ],
    [
      "0064e2a0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071be98"
      ]
    ]
  ],
  "added": [
    [
      "0064e1d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071bed8"
      ]
    ],
    [
      "0064e294",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00641c68"
      ]
    ],
    [
      "0064e2a0",
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

- 旧版 [`0064e194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064e15c.md#insn-0064e194) · [`0064e254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064e15c.md#insn-0064e254) · [`0064e260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064e15c.md#insn-0064e260)
- 新版 `0064e1d4`（命令位置の公開資料なし） · `0064e294`（命令位置の公開資料なし） · `0064e2a0`（命令位置の公開資料なし）

~~~diff
- 0064e194 ["INT_ADD", "register:40f0:8", ["const:64e194:8", "const:4:8"]]
- 0064e194 ["CALL", null, ["ram:71be98:8"]]
+ 0064e1d4 ["INT_ADD", "register:40f0:8", ["const:64e1d4:8", "const:4:8"]]
+ 0064e1d4 ["CALL", null, ["ram:71bed8:8"]]
- 0064e194 bytes 41370394
+ 0064e1d4 bytes 41370394
- 0064e254 ["INT_ADD", "register:40f0:8", ["const:64e254:8", "const:4:8"]]
- 0064e254 ["CALL", null, ["ram:641c28:8"]]
+ 0064e294 ["INT_ADD", "register:40f0:8", ["const:64e294:8", "const:4:8"]]
+ 0064e294 ["CALL", null, ["ram:641c68:8"]]
- 0064e254 bytes 75ceff97
+ 0064e294 bytes 75ceff97
- 0064e260 ["INT_ADD", "register:40f0:8", ["const:64e260:8", "const:4:8"]]
- 0064e260 ["CALL", null, ["ram:71be98:8"]]
+ 0064e2a0 ["INT_ADD", "register:40f0:8", ["const:64e2a0:8", "const:4:8"]]
+ 0064e2a0 ["CALL", null, ["ram:71bed8:8"]]
- 0064e260 bytes 0e370394
+ 0064e2a0 bytes 0e370394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a58b7480d6ebe43ae33f3c0e5b505bb7"></a>

### [`00676da8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676da8.md) → [`00676de8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676de8.md) FUN_00676de8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00676ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676ac8.md) · 呼出先 1件 [`00676ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676ac8.md)
- 新版 呼出元 1件 [`00676b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676b08.md) · 呼出先 1件 [`00676b08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/00676b08.md)

変更の種類 branch_condition_or_target, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 99.41% / 新版 99.41%

CFGの説明率　旧版 91.89% / 新版 91.89%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00676e70"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00676eb0"
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
      "unmatched:00676e70",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00676edc"
      ]
    ]
  ],
  "added": [
    [
      "00676eb0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00676edc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00676e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676da8.md#insn-00676e70) · [`00676e38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676da8.md#insn-00676e38)
- 新版 `00676eb0`（命令位置の公開資料なし） · `00676e78`（命令位置の公開資料なし）

~~~diff
- 00676e70 ["CBRANCH", null, ["local:b22:8", "register:101:1"]]
- 00676e70 bytes 60010054
+ 00676eb0 ["CBRANCH", null, ["local:b22:8", "register:101:1"]]
+ 00676eb0 bytes 60010054
- 00676e38 ["BRANCH", null, ["local:b14:8"]]
+ 00676e78 ["BRANCH", null, ["local:b15:8"]]
- 00676e38 bytes 07000014
+ 00676e78 bytes 07000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-169a1152b5b6c1403649a5359ba8e610"></a>

### [`0068bdd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068b/0068bdd0.md) → [`0068be10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068b/0068be10.md) FUN_0068be10

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0068d950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068d/0068d950.md) [`00a79a0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a79/00a79a0c.md) · 呼出先 21件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467d74.md) [`00467e5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467e5c.md) [`00467e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467e64.md)
- 新版 呼出元 2件 [`0068d990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068d/0068d990.md) [`00a79c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a79/00a79c04.md) · 呼出先 21件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467db4.md) [`00467e9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467e9c.md) [`00467ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467ea4.md)

変更の種類 call, call_count, call_target, constant, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 97.66% / 新版 97.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 11件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0068be74",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0068be34",
      "value": [
        "leaf",
        "ram:46c984:8"
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
      "site": "0068beb8",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0068be78",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 10,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0068c094",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0068c054",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 34,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0068be74",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "0068beb8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "0068c094",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ]
  ],
  "added": [
    [
      "0068be74",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "0068beb8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "0068c094",
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

- 旧版 [`0068be34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068b/0068bdd0.md#insn-0068be34) · [`0068be74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068b/0068bdd0.md#insn-0068be74) · [`0068be78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068b/0068bdd0.md#insn-0068be78)
- 新版 `0068be74`（命令位置の公開資料なし） · `0068beb4`（命令位置の公開資料なし） · `0068beb8`（命令位置の公開資料なし）

~~~diff
- 0068be34 ["INT_ADD", "register:40f0:8", ["const:68be34:8", "const:4:8"]]
- 0068be34 ["CALL", null, ["ram:46c984:8"]]
+ 0068be74 ["INT_ADD", "register:40f0:8", ["const:68be74:8", "const:4:8"]]
+ 0068be74 ["CALL", null, ["ram:46c9c4:8"]]
- 0068be34 bytes d482f797
+ 0068be74 bytes d482f797
- 0068be74 ["INT_ADD", "register:40f0:8", ["const:68be74:8", "const:4:8"]]
- 0068be74 ["CALL", null, ["callee:008514f8:8"]]
+ 0068beb4 ["INT_ADD", "register:40f0:8", ["const:68beb4:8", "const:4:8"]]
+ 0068beb4 ["CALL", null, ["callee:008514f8:8"]]
- 0068be74 bytes 91150794
+ 0068beb4 bytes 91150794
- 0068be78 ["INT_ADD", "register:40f0:8", ["const:68be78:8", "const:4:8"]]
- 0068be78 ["CALL", null, ["ram:46c984:8"]]
+ 0068beb8 ["INT_ADD", "register:40f0:8", ["const:68beb8:8", "const:4:8"]]
+ 0068beb8 ["CALL", null, ["ram:46c9c4:8"]]
- 0068be78 bytes c382f797
+ 0068beb8 bytes c382f797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1611071e937ba7453d5cbc6658dfda8"></a>

### [`006a6dc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a6/006a6dc4.md) → [`006a6e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a6/006a6e04.md) FUN_006a6e04

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006a7480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a7/006a7480.md) · 呼出先 4件 [`00811630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00811/00811630.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00b2f590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f590.md) [`00b3ba6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3ba6c.md)
- 新版 呼出元 1件 [`006a74c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006a7/006a74c0.md) · 呼出先 4件 [`00811670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00811/00811670.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b2f9b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2f/00b2f9b8.md) [`00b3be94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3be94.md)

変更の種類 call, call_target, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 91.54% / 新版 91.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006a6f48",
      "value": [
        "leaf",
        "ram:811670:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006a6f08",
      "value": [
        "leaf",
        "ram:811630:8"
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
      "site": "006a6f58",
      "value": [
        "leaf",
        "ram:811670:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006a6f18",
      "value": [
        "leaf",
        "ram:811630:8"
      ]
    },
    "ordinal": 9,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006a6f6c",
      "value": [
        "leaf",
        "ram:811670:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006a6f2c",
      "value": [
        "leaf",
        "ram:811630:8"
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
      "006a6f48",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00811630"
      ]
    ],
    [
      "006a6f58",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00811630"
      ]
    ],
    [
      "006a6f6c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00811630"
      ]
    ]
  ],
  "added": [
    [
      "006a6f48",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00811670"
      ]
    ],
    [
      "006a6f58",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00811670"
      ]
    ],
    [
      "006a6f6c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00811670"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006a6f08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a6/006a6dc4.md#insn-006a6f08) · [`006a6f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a6/006a6dc4.md#insn-006a6f18) · [`006a6f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a6/006a6dc4.md#insn-006a6f2c)
- 新版 `006a6f48`（命令位置の公開資料なし） · `006a6f58`（命令位置の公開資料なし） · `006a6f6c`（命令位置の公開資料なし）

~~~diff
- 006a6f08 ["INT_ADD", "register:40f0:8", ["const:6a6f08:8", "const:4:8"]]
- 006a6f08 ["CALL", null, ["ram:811630:8"]]
+ 006a6f48 ["INT_ADD", "register:40f0:8", ["const:6a6f48:8", "const:4:8"]]
+ 006a6f48 ["CALL", null, ["ram:811670:8"]]
- 006a6f08 bytes caa90594
+ 006a6f48 bytes caa90594
- 006a6f18 ["INT_ADD", "register:40f0:8", ["const:6a6f18:8", "const:4:8"]]
- 006a6f18 ["CALL", null, ["ram:811630:8"]]
+ 006a6f58 ["INT_ADD", "register:40f0:8", ["const:6a6f58:8", "const:4:8"]]
+ 006a6f58 ["CALL", null, ["ram:811670:8"]]
- 006a6f18 bytes c6a90594
+ 006a6f58 bytes c6a90594
- 006a6f2c ["INT_ADD", "register:40f0:8", ["const:6a6f2c:8", "const:4:8"]]
- 006a6f2c ["CALL", null, ["ram:811630:8"]]
+ 006a6f6c ["INT_ADD", "register:40f0:8", ["const:6a6f6c:8", "const:4:8"]]
+ 006a6f6c ["CALL", null, ["ram:811670:8"]]
- 006a6f2c bytes c1a90594
+ 006a6f6c bytes c1a90594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74c3002db81eee7ce9655dd94f6b7577"></a>

### [`006ad3d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ad/006ad3d4.md) → [`006ad414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ad/006ad414.md) FUN_006ad414

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006acaac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ac/006acaac.md) · 呼出先 7件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467f14.md) [`00467fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467fbc.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md)
- 新版 呼出元 1件 [`006acaec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ac/006acaec.md) · 呼出先 7件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f54.md) [`00467ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467ffc.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md)

変更の種類 call, call_count, call_target, constant, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 91.57% / 新版 91.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 52件, `unresolved_call_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006ad488",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006ad448",
      "value": [
        "leaf",
        "ram:46c984:8"
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
      "site": "006ad498",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006ad458",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006ad4d0",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006ad490",
      "value": [
        "leaf",
        "ram:46c984:8"
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
      "006ad488",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "006ad498",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "006ad4d0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ]
  ],
  "added": [
    [
      "006ad488",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "006ad498",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "006ad4d0",
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

- 旧版 [`006ad448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ad/006ad3d4.md#insn-006ad448) · [`006ad458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ad/006ad3d4.md#insn-006ad458) · [`006ad490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ad/006ad3d4.md#insn-006ad490)
- 新版 `006ad488`（命令位置の公開資料なし） · `006ad498`（命令位置の公開資料なし） · `006ad4d0`（命令位置の公開資料なし）

~~~diff
- 006ad448 ["INT_ADD", "register:40f0:8", ["const:6ad448:8", "const:4:8"]]
- 006ad448 ["CALL", null, ["ram:46c984:8"]]
+ 006ad488 ["INT_ADD", "register:40f0:8", ["const:6ad488:8", "const:4:8"]]
+ 006ad488 ["CALL", null, ["ram:46c9c4:8"]]
- 006ad448 bytes 4ffdf697
+ 006ad488 bytes 4ffdf697
- 006ad458 ["INT_ADD", "register:40f0:8", ["const:6ad458:8", "const:4:8"]]
- 006ad458 ["CALL", null, ["ram:46c984:8"]]
+ 006ad498 ["INT_ADD", "register:40f0:8", ["const:6ad498:8", "const:4:8"]]
+ 006ad498 ["CALL", null, ["ram:46c9c4:8"]]
- 006ad458 bytes 4bfdf697
+ 006ad498 bytes 4bfdf697
- 006ad490 ["INT_ADD", "register:40f0:8", ["const:6ad490:8", "const:4:8"]]
- 006ad490 ["CALL", null, ["ram:46c984:8"]]
+ 006ad4d0 ["INT_ADD", "register:40f0:8", ["const:6ad4d0:8", "const:4:8"]]
+ 006ad4d0 ["CALL", null, ["ram:46c9c4:8"]]
- 006ad490 bytes 3dfdf697
+ 006ad4d0 bytes 3dfdf697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4064ded73253b3a8f7a914274fcd30aa"></a>

### [`006b66a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b6/006b66a8.md) → [`006b66e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b6/006b66e8.md) FUN_006b66e8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0062a1fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062a/0062a1fc.md) [`006b6610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b6/006b6610.md) · 呼出先 7件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467f14.md) [`00467fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467fbc.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md)
- 新版 呼出元 2件 [`0062a23c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0062a/0062a23c.md) [`006b6650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b6/006b6650.md) · 呼出先 7件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f54.md) [`00467ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467ffc.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md)

変更の種類 call, call_count, call_target, constant, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 84.35% / 新版 84.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 51件, `unresolved_call_alignment` 33件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "006b6718"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006b675c",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006b671c",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "006b6724"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006b6718",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514f8"
      ]
    ],
    [
      "006b675c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "unmatched:006b6724",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514f8"
      ]
    ]
  ],
  "added": [
    [
      "006b6758",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514f8"
      ]
    ],
    [
      "006b675c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "006b6764",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514f8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b66e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b6/006b66a8.md#insn-006b66e4) · [`006b6718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b6/006b66a8.md#insn-006b6718) · [`006b671c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b6/006b66a8.md#insn-006b671c)
- 新版 `006b6724`（命令位置の公開資料なし） · `006b675c`（命令位置の公開資料なし）

~~~diff
- 006b66e4 ["INT_ADD", "register:40f0:8", ["const:6b66e4:8", "const:4:8"]]
- 006b66e4 ["CALL", null, ["callee:00467b2c:8"]]
+ 006b6724 ["INT_ADD", "register:40f0:8", ["const:6b6724:8", "const:4:8"]]
+ 006b6724 ["CALL", null, ["callee:00467b2c:8"]]
- 006b66e4 bytes 02c5f697
+ 006b6724 bytes 02c5f697
- 006b6718 ["INT_ADD", "register:40f0:8", ["const:6b6718:8", "const:4:8"]]
- 006b6718 ["CALL", null, ["callee:008514f8:8"]]
- 006b6718 bytes 686b0694
- 006b671c ["INT_ADD", "register:40f0:8", ["const:6b671c:8", "const:4:8"]]
- 006b671c ["CALL", null, ["ram:46c984:8"]]
+ 006b675c ["INT_ADD", "register:40f0:8", ["const:6b675c:8", "const:4:8"]]
+ 006b675c ["CALL", null, ["ram:46c9c4:8"]]
- 006b671c bytes 9ad8f697
+ 006b675c bytes 9ad8f697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83daee28ec9e513b46e5da5314bab163"></a>

### [`0071e354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071e/0071e354.md) → [`0071e394`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071e/0071e394.md) FUN_0071e394

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0071d1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071d/0071d1bc.md) [`00921948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00921/00921948.md) [`0097d818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d818.md) · 呼出先 10件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00697250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/00697250.md) [`00b3ba38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3ba38.md) [`00b3ba6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3ba6c.md) [`00b3bab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3bab0.md)
- 新版 呼出元 3件 [`0071d1fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071d/0071d1fc.md) [`00921ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00921/00921ae4.md) [`0097d9b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0097d/0097d9b4.md) · 呼出先 10件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00697290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/00697290.md) [`00b3be60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3be60.md) [`00b3be94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3be94.md) [`00b3bed8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3bed8.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 94.26% / 新版 94.26%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0071e45c",
      "PARAM",
      [
        "storage",
        "002a4584",
        null,
        "string"
      ]
    ],
    [
      "0071e45c",
      "PARAM",
      [
        "storage",
        "002a33c6",
        null,
        "string"
      ]
    ],
    [
      "0071e45c",
      "PARAM",
      [
        "storage",
        "002c0250",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0071e45c",
      "PARAM",
      [
        "storage",
        "002a4651",
        null,
        "string"
      ]
    ],
    [
      "0071e45c",
      "PARAM",
      [
        "storage",
        "002a3493",
        null,
        "string"
      ]
    ],
    [
      "0071e45c",
      "PARAM",
      [
        "storage",
        "002c0290",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071e3bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071e/0071e354.md#insn-0071e3bc) · [`0071e3c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071e/0071e354.md#insn-0071e3c4) · [`0071e3dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071e/0071e354.md#insn-0071e3dc)
- 新版 `0071e3fc`（命令位置の公開資料なし） · `0071e404`（命令位置の公開資料なし） · `0071e41c`（命令位置の公開資料なし）

~~~diff
- 0071e3bc ["INT_ADD", "register:40f0:8", ["const:71e3bc:8", "const:4:8"]]
- 0071e3bc ["CALL", null, ["callee:00b3bed8:8"]]
+ 0071e3fc ["INT_ADD", "register:40f0:8", ["const:71e3fc:8", "const:4:8"]]
+ 0071e3fc ["CALL", null, ["callee:00b3bed8:8"]]
- 0071e3bc bytes bd751094
+ 0071e3fc bytes b7761094
- 0071e3c4 ["INT_ADD", "register:40f0:8", ["const:71e3c4:8", "const:4:8"]]
- 0071e3c4 ["CALL", null, ["callee:00b3be94:8"]]
+ 0071e404 ["INT_ADD", "register:40f0:8", ["const:71e404:8", "const:4:8"]]
+ 0071e404 ["CALL", null, ["callee:00b3be94:8"]]
- 0071e3c4 bytes aa751094
+ 0071e404 bytes a4761094
- 0071e3dc ["INT_ADD", "register:40f0:8", ["const:71e3dc:8", "const:4:8"]]
- 0071e3dc ["CALL", null, ["callee:00b3be60:8"]]
+ 0071e41c ["INT_ADD", "register:40f0:8", ["const:71e41c:8", "const:4:8"]]
+ 0071e41c ["CALL", null, ["callee:00b3be60:8"]]
- 0071e3dc bytes 97751094
+ 0071e41c bytes 91761094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a821abf3e1a7cdacf54f745d485e833"></a>

### [`0071e580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071e/0071e580.md) → [`0071e5c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071e/0071e5c0.md) FUN_0071e5c0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0071d1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071d/0071d1bc.md) · 呼出先 9件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00697250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/00697250.md) [`00b3ba6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3ba6c.md) [`00b3baf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3baf8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`0071d1fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071d/0071d1fc.md) · 呼出先 9件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00697290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/00697290.md) [`00b3be94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3be94.md) [`00b3bf20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3bf20.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 93.86% / 新版 93.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0071e690",
      "PARAM",
      [
        "storage",
        "002a4584",
        null,
        "string"
      ]
    ],
    [
      "0071e690",
      "PARAM",
      [
        "storage",
        "002a33c6",
        null,
        "string"
      ]
    ],
    [
      "0071e690",
      "PARAM",
      [
        "storage",
        "002c0250",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0071e690",
      "PARAM",
      [
        "storage",
        "002a4651",
        null,
        "string"
      ]
    ],
    [
      "0071e690",
      "PARAM",
      [
        "storage",
        "002a3493",
        null,
        "string"
      ]
    ],
    [
      "0071e690",
      "PARAM",
      [
        "storage",
        "002c0290",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0071e5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071e/0071e580.md#insn-0071e5f0) · [`0071e60c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071e/0071e580.md#insn-0071e60c) · [`0071e620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071e/0071e580.md#insn-0071e620)
- 新版 `0071e630`（命令位置の公開資料なし） · `0071e64c`（命令位置の公開資料なし） · `0071e660`（命令位置の公開資料なし）

~~~diff
- 0071e5f0 ["INT_ADD", "register:40f0:8", ["const:71e5f0:8", "const:4:8"]]
- 0071e5f0 ["CALL", null, ["callee:00b3be94:8"]]
+ 0071e630 ["INT_ADD", "register:40f0:8", ["const:71e630:8", "const:4:8"]]
+ 0071e630 ["CALL", null, ["callee:00b3be94:8"]]
- 0071e5f0 bytes 1f751094
+ 0071e630 bytes 19761094
- 0071e60c ["INT_ADD", "register:40f0:8", ["const:71e60c:8", "const:4:8"]]
- 0071e60c ["CALL", null, ["callee:00b3bf20:8"]]
+ 0071e64c ["INT_ADD", "register:40f0:8", ["const:71e64c:8", "const:4:8"]]
+ 0071e64c ["CALL", null, ["callee:00b3bf20:8"]]
- 0071e60c bytes 3b751094
+ 0071e64c bytes 35761094
- 0071e620 ["COPY", "tmp:0:8", ["const:584:8"]]
- 0071e620 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0071e620 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0071e620 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0071e660 ["COPY", "tmp:0:8", ["const:651:8"]]
+ 0071e660 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0071e660 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0071e660 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0071e620 bytes 4a111691
+ 0071e660 bytes 4a451991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f73c523991a4963fc5537b499dcd9f1"></a>

### [`008001ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/008001ac.md) → [`008001ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/008001ec.md) FUN_008001ec

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 50件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`00605214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00605/00605214.md) [`0060e084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0060e/0060e084.md) [`006bbc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bb/006bbc58.md) [`006c036c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c0/006c036c.md) · 呼出先 0件 
- 新版 呼出元 50件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`00605254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00605/00605254.md) [`0060e0c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0060e/0060e0c4.md) [`006bbc98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006bb/006bbc98.md) [`006c03ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c0/006c03ac.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.70% / 新版 95.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00800208",
      "DATA",
      [
        "storage",
        "002ec8a4",
        "switchD_008001d0::switchdataD_002ec8a4",
        "byte"
      ]
    ]
  ],
  "added": [
    [
      "00800208",
      "DATA",
      [
        "storage",
        "002ec8e4",
        "switchD_00800210::switchdataD_002ec8e4",
        "byte"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008001bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/008001ac.md#insn-008001bc) · [`008001c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/008001ac.md#insn-008001c4)
- 新版 `008001fc`（命令位置の公開資料なし） · `00800204`（命令位置の公開資料なし）

~~~diff
- 008001bc ["COPY", "tmp:0:8", ["const:8a4:8"]]
- 008001bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008001bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008001bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008001fc ["COPY", "tmp:0:8", ["const:8e4:8"]]
+ 008001fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008001fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008001fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008001bc bytes 29912291
+ 008001fc bytes 29912391
- 008001c4 ["COPY", "register:4050:8", ["const:8001d4:8"]]
- 008001c4 bytes 8a000010
+ 00800204 ["COPY", "register:4050:8", ["const:800214:8"]]
+ 00800204 bytes 8a000010
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a99081a347d2ad686ec4786f24cbf9cf"></a>

### [`00800638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/00800638.md) → [`00800678`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/00800678.md) FUN_00800678

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`00aa3c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa3/00aa3c28.md) · 呼出先 0件 
- 新版 呼出元 2件 [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) [`00aa3e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aa3/00aa3e24.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.12% / 新版 95.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00800690",
      "DATA",
      [
        "storage",
        "002ec8c3",
        "switchD_00800658::switchdataD_002ec8c3",
        "byte"
      ]
    ]
  ],
  "added": [
    [
      "00800690",
      "DATA",
      [
        "storage",
        "002ec903",
        "switchD_00800698::switchdataD_002ec903",
        "byte"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00800648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/00800638.md#insn-00800648) · [`0080064c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/00800638.md#insn-0080064c)
- 新版 `00800688`（命令位置の公開資料なし） · `0080068c`（命令位置の公開資料なし）

~~~diff
- 00800648 ["COPY", "tmp:0:8", ["const:8c3:8"]]
- 00800648 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00800648 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00800648 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00800688 ["COPY", "tmp:0:8", ["const:903:8"]]
+ 00800688 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00800688 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00800688 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00800648 bytes 4a0d2391
+ 00800688 bytes 4a0d2491
- 0080064c ["COPY", "register:4058:8", ["const:80065c:8"]]
- 0080064c bytes 8b000010
+ 0080068c ["COPY", "register:4058:8", ["const:80069c:8"]]
+ 0080068c bytes 8b000010
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8a83fffbe3132fa234856b7acbf8070"></a>

### [`00800780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/00800780.md) → [`008007c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/008007c0.md) FUN_008007c0

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`007290c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00729/007290c8.md) [`007b09d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007b0/007b09d8.md) [`00a52c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a52/00a52c38.md) · 呼出先 0件 
- 新版 呼出元 3件 [`00729108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00729/00729108.md) [`007b0a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007b0/007b0a18.md) [`00a52e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a52/00a52e30.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 93.85% / 新版 93.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008007dc",
      "DATA",
      [
        "storage",
        "002ec8e2",
        "switchD_008007a4::switchdataD_002ec8e2",
        "byte"
      ]
    ]
  ],
  "added": [
    [
      "008007dc",
      "DATA",
      [
        "storage",
        "002ec922",
        "switchD_008007e4::switchdataD_002ec922",
        "byte"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00800794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/00800780.md#insn-00800794) · [`00800798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/00800780.md#insn-00800798)
- 新版 `008007d4`（命令位置の公開資料なし） · `008007d8`（命令位置の公開資料なし）

~~~diff
- 00800794 ["COPY", "tmp:0:8", ["const:8e2:8"]]
- 00800794 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
- 00800794 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
- 00800794 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
+ 008007d4 ["COPY", "tmp:0:8", ["const:922:8"]]
+ 008007d4 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
+ 008007d4 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
+ 008007d4 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
- 00800794 bytes 6b892391
+ 008007d4 bytes 6b892491
- 00800798 ["COPY", "register:4060:8", ["const:8007a8:8"]]
- 00800798 bytes 8c000010
+ 008007d8 ["COPY", "register:4060:8", ["const:8007e8:8"]]
+ 008007d8 bytes 8c000010
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb56b104d815889a9eace1e06274be95"></a>

### [`00805bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00805/00805bb4.md) → [`00805bf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00805/00805bf4.md) FUN_00805bf4

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`0072c80c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072c/0072c80c.md) [`0072f198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0072f/0072f198.md) [`007317cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/007317cc.md) [`00a878d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a87/00a878d8.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 4件 [`0072c84c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072c/0072c84c.md) [`0072f1d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0072f/0072f1d8.md) [`0073180c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/0073180c.md) [`00a87ad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a87/00a87ad0.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00805c20",
      "DATA",
      [
        "storage",
        "002ec9a3",
        "switchD_00805bec::switchdataD_002ec9a3",
        "byte"
      ]
    ],
    [
      "00805ce4",
      "DATA",
      [
        "storage",
        "0038b098",
        null,
        "dword"
      ]
    ],
    [
      "00805ce4",
      "DATA",
      [
        "storage",
        "0038a8c8",
        null,
        "qword"
      ]
    ]
  ],
  "added": [
    [
      "00805c20",
      "DATA",
      [
        "storage",
        "002ec9e3",
        "switchD_00805c2c::switchdataD_002ec9e3",
        "byte"
      ]
    ],
    [
      "00805ce4",
      "DATA",
      [
        "storage",
        "0038b098",
        null,
        "byte[27]"
      ]
    ],
    [
      "00805ce4",
      "DATA",
      [
        "storage",
        "0038a8c8",
        null,
        "byte[23]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00805bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00805/00805bb4.md#insn-00805bd4) · [`00805bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00805/00805bb4.md#insn-00805bdc) · [`00805bf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00805/00805bb4.md#insn-00805bf4)
- 新版 `00805c14`（命令位置の公開資料なし） · `00805c34`（命令位置の公開資料なし）

~~~diff
- 00805bd4 ["COPY", "tmp:0:8", ["const:9a3:8"]]
- 00805bd4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00805bd4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00805bd4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00805c14 ["COPY", "tmp:0:8", ["const:9e3:8"]]
+ 00805c14 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00805c14 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00805c14 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00805bd4 bytes 298d2691
+ 00805c14 bytes 298d2791
- 00805bdc ["COPY", "register:4050:8", ["const:805bf0:8"]]
- 00805bdc bytes aa000010
- 00805bf4 ["INT_ADD", "register:40f0:8", ["const:805bf4:8", "const:4:8"]]
- 00805bf4 ["CALL", null, ["callee:008514f8:8"]]
+ 00805c34 ["INT_ADD", "register:40f0:8", ["const:805c34:8", "const:4:8"]]
+ 00805c34 ["CALL", null, ["callee:008514f8:8"]]
- 00805bf4 bytes 312e0194
+ 00805c34 bytes 312e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29d4c2ced21db3fb0b3de36c47895323"></a>

### [`00886f04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886f04.md) → [`00886f44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00886/00886f44.md) FUN_00886f44

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 10件 [`0044f8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f8a0.md) [`004573c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00457/004573c0.md) [`00764344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764344.md) [`00764ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764ea0.md) [`00767d64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00767/00767d64.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0044f8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f8e0.md) [`00457400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00457/00457400.md) [`00764384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764384.md) [`00764ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764ee0.md) [`00767da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00767/00767da4.md)

変更の種類 call, call_count, call_target, constant, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 95.95% / 新版 95.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00886f80",
      "value": [
        "leaf",
        "ram:764384:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00886f40",
      "value": [
        "leaf",
        "ram:764344:8"
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00886f44"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00886f8c",
      "value": [
        "leaf",
        "ram:764ee0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00886f4c",
      "value": [
        "leaf",
        "ram:764ea0:8"
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
      "00886f80",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764344"
      ]
    ],
    [
      "unmatched:00886f44",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514f8"
      ]
    ],
    [
      "00886f8c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764ea0"
      ]
    ]
  ],
  "added": [
    [
      "00886f80",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764384"
      ]
    ],
    [
      "00886f84",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514f8"
      ]
    ],
    [
      "00886f8c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764ee0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00886f40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886f04.md#insn-00886f40) · [`00886f44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886f04.md#insn-00886f44) · [`00886f4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886f04.md#insn-00886f4c)
- 新版 `00886f80`（命令位置の公開資料なし） · `00886f8c`（命令位置の公開資料なし）

~~~diff
- 00886f40 ["INT_ADD", "register:40f0:8", ["const:886f40:8", "const:4:8"]]
- 00886f40 ["CALL", null, ["ram:764344:8"]]
+ 00886f80 ["INT_ADD", "register:40f0:8", ["const:886f80:8", "const:4:8"]]
+ 00886f80 ["CALL", null, ["ram:764384:8"]]
- 00886f40 bytes 0175fb97
+ 00886f80 bytes 0175fb97
- 00886f44 ["INT_ADD", "register:40f0:8", ["const:886f44:8", "const:4:8"]]
- 00886f44 ["CALL", null, ["callee:008514f8:8"]]
- 00886f44 bytes 5d29ff97
- 00886f4c ["INT_ADD", "register:40f0:8", ["const:886f4c:8", "const:4:8"]]
- 00886f4c ["CALL", null, ["ram:764ea0:8"]]
+ 00886f8c ["INT_ADD", "register:40f0:8", ["const:886f8c:8", "const:4:8"]]
+ 00886f8c ["CALL", null, ["ram:764ee0:8"]]
- 00886f4c bytes d577fb97
+ 00886f8c bytes d577fb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64619bd0379f50456d7ea545e1a6809e"></a>

### [`0088ffe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088ffe4.md) → [`00890028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890028.md) FUN_00890028

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0088ffe8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0089002c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00890010"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0088ffe8",
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
      "0089002c",
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

- 旧版 [`0088ffe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088ffe4.md#insn-0088ffe8) · [`00890010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088ffe4.md#insn-00890010)
- 新版 `0089002c`（命令位置の公開資料なし）

~~~diff
- 0088ffe8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0088ffe8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 0088ffe8 bytes f30b00f9
- 00890010 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00890010 ["RETURN", null, ["register:0:8"]]
- 00890010 bytes c0035fd6
+ 0089002c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
+ 0089002c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 0089002c bytes f30b00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7c27b606a9fe32e55f0566c2e29a35d"></a>

### [`008900ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/008900ec.md) → [`00890130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890130.md) FUN_00890130

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 33.33% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00890110"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00890110"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00890114"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00890110",
      "DATA",
      [
        "storage",
        "00c81908",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00890118",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00890174"
      ]
    ]
  ],
  "added": [
    [
      "00890154",
      "DATA",
      [
        "storage",
        "00c81d08",
        null,
        "undefined *"
      ]
    ],
    [
      "0089015c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00890174"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00890110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/008900ec.md#insn-00890110) · [`00890114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/008900ec.md#insn-00890114) · [`00890118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/008900ec.md#insn-00890118)

~~~diff
- 00890110 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00890110 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00890110 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00890110 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00890110 bytes 092800a9
- 00890114 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:10:8"]]
- 00890114 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00890114 bytes 080800f9
- 00890118 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00890118 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00890118 bytes c80000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09f599c3a4b188fcebd62e9bb159dc3f"></a>

### [`00890170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890170.md) → [`008901b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/008901b4.md) FUN_008901b4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0088fd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fd58.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`0088fd9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fd9c.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "0089019c"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "008901e0"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`0089019c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890170.md#insn-0089019c) · [`0089018c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890170.md#insn-0089018c)
- 新版 `008901e0`（命令位置の公開資料なし） · `008901d0`（命令位置の公開資料なし）

~~~diff
- 0089019c ["COPY", "register:0:8", ["register:40f0:8"]]
- 0089019c ["RETURN", null, ["register:0:8"]]
- 0089019c bytes c0035fd6
+ 008901e0 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 008901e0 ["RETURN", null, ["register:0:8"]]
+ 008901e0 bytes c0035fd6
- 0089018c ["INT_ADD", "register:40f0:8", ["const:89018c:8", "const:4:8"]]
- 0089018c ["CALL", null, ["callee:00c53d00:8"]]
+ 008901d0 ["INT_ADD", "register:40f0:8", ["const:8901d0:8", "const:4:8"]]
+ 008901d0 ["CALL", null, ["callee:00c53d00:8"]]
- 0089018c bytes d50d0f94
+ 008901d0 bytes cc0e0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8180ed49d4147b6fd0f6415d671b1c2"></a>

### [`008901c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/008901c0.md) → [`00890204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890204.md) FUN_00890204

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0088fd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088f/0088fd58.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 1件 [`0088fd9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088f/0088fd9c.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 50.00% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008901c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008901c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008901c4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008901c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:008901c4",
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
      "00890204",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00890208",
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

- 旧版 [`008901c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/008901c0.md#insn-008901c0) · [`008901c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/008901c0.md#insn-008901c4)
- 新版 `00890204`（命令位置の公開資料なし）

~~~diff
- 008901c0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008901c0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008901c0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 008901c0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 008901c0 bytes fd7bbea9
- 008901c4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 008901c4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 008901c4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 008901c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008901c4 bytes f44f01a9
+ 00890204 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00890204 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00890204 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00890204 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00890204 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80ac41b40a46fc726ccf4b62aa9fd01e"></a>

### [`00890ee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890ee4.md) → [`00890f28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00890/00890f28.md) FUN_00890f28

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 97.83% / 新版 97.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00890f98"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00890fdc"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00890f98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890ee4.md#insn-00890f98) · [`00890f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00890/00890ee4.md#insn-00890f18)
- 新版 `00890fdc`（命令位置の公開資料なし） · `00890f5c`（命令位置の公開資料なし）

~~~diff
- 00890f98 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00890f98 ["RETURN", null, ["register:0:8"]]
- 00890f98 bytes c0035fd6
+ 00890fdc ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00890fdc ["RETURN", null, ["register:0:8"]]
+ 00890fdc bytes c0035fd6
- 00890f18 ["INT_ADD", "register:40f0:8", ["const:890f18:8", "const:4:8"]]
- 00890f18 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00890f5c ["INT_ADD", "register:40f0:8", ["const:890f5c:8", "const:4:8"]]
+ 00890f5c ["CALL", null, ["callee:00c57eb0:8"]]
- 00890f18 bytes e61a0f94
+ 00890f5c bytes d51b0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b69ebc0b093d6abc42e03d6f948034c"></a>

### [`008926e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/008926e4.md) → [`00892728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892728.md) FUN_00892728

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008926e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008926e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008926fc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008926e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:008926f0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57e90"
      ]
    ],
    [
      "unmatched:008926fc",
      "DATA",
      [
        "storage",
        "00c81a18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00892728",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00892734",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57e90"
      ]
    ],
    [
      "00892740",
      "DATA",
      [
        "storage",
        "00c81e18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008926e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/008926e4.md#insn-008926e4) · [`008926f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/008926e4.md#insn-008926f0) · [`008926fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/008926e4.md#insn-008926fc)

~~~diff
- 008926e4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008926e4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008926e4 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 008926e4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 008926e4 bytes fd7bbfa9
- 008926f0 ["INT_ADD", "register:40f0:8", ["const:8926f0:8", "const:4:8"]]
- 008926f0 ["CALL", null, ["callee:00c57e90:8"]]
- 008926f0 bytes e8140f94
- 008926fc ["COPY", "tmp:0:8", ["register:4000:8"]]
- 008926fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008926fc bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70b9fdfd01959a623de7fa8064544c94"></a>

### [`00892bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892bb4.md) → [`00892bf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892bf8.md) FUN_00892bf8

採用 · 移動量 `+0x44` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`0066d09c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066d/0066d09c.md) [`00727990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727990.md) [`00b38e58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b38/00b38e58.md) [`00b39fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b39/00b39fc8.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0066d0dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066d/0066d0dc.md) [`007279d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00727/007279d0.md) [`00b39280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b39/00b39280.md) [`00b3a3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3a/00b3a3f0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00892bd8",
      "PARAM",
      [
        "storage",
        "011234a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00892c1c",
      "PARAM",
      [
        "storage",
        "011238a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00892bc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892bb4.md#insn-00892bc8) · [`00892bcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892bb4.md#insn-00892bcc) · [`00892bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892bb4.md#insn-00892bd0)
- 新版 `00892c0c`（命令位置の公開資料なし） · `00892c10`（命令位置の公開資料なし） · `00892c14`（命令位置の公開資料なし）

~~~diff
- 00892bc8 ["INT_ADD", "register:40f0:8", ["const:892bc8:8", "const:4:8"]]
- 00892bc8 ["CALL", null, ["callee:0066d0dc:8"]]
+ 00892c0c ["INT_ADD", "register:40f0:8", ["const:892c0c:8", "const:4:8"]]
+ 00892c0c ["CALL", null, ["callee:0066d0dc:8"]]
- 00892bc8 bytes 3569f797
+ 00892c0c bytes 3469f797
- 00892bcc ["INT_ADD", "register:40f0:8", ["const:892bcc:8", "const:4:8"]]
- 00892bcc ["CALL", null, ["callee:007279d0:8"]]
+ 00892c10 ["INT_ADD", "register:40f0:8", ["const:892c10:8", "const:4:8"]]
+ 00892c10 ["CALL", null, ["callee:007279d0:8"]]
- 00892bcc bytes 7153fa97
+ 00892c10 bytes 7053fa97
- 00892bd0 ["INT_ADD", "register:40f0:8", ["const:892bd0:8", "const:4:8"]]
- 00892bd0 ["CALL", null, ["callee:00b39280:8"]]
+ 00892c14 ["INT_ADD", "register:40f0:8", ["const:892c14:8", "const:4:8"]]
+ 00892c14 ["CALL", null, ["callee:00b39280:8"]]
- 00892bd0 bytes a2980a94
+ 00892c14 bytes 9b990a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc26182f982928fa194537b1ddd5a4c3"></a>

### [`00892c18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892c18.md) → [`00892c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892c5c.md) FUN_00892c5c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

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
      "site": "00892c30"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00892c74"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00892c38"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00892c30",
      "DATA",
      [
        "storage",
        "00c81ba8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00892c34",
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
      "00892c74",
      "DATA",
      [
        "storage",
        "00c81fa8",
        null,
        "undefined *"
      ]
    ],
    [
      "00892c78",
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

- 旧版 [`00892c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892c18.md#insn-00892c30) · [`00892c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892c18.md#insn-00892c38)
- 新版 `00892c74`（命令位置の公開資料なし）

~~~diff
- 00892c30 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00892c30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00892c30 bytes 080000f9
- 00892c38 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00892c38 ["RETURN", null, ["register:0:8"]]
- 00892c38 bytes c0035fd6
+ 00892c74 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00892c74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00892c74 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef6f250b86aa6cdedaad7f33c52b344e"></a>

### [`00892c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892c3c.md) → [`00892c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00892/00892c80.md) FUN_00892c80

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

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
      "site": "00892c44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00892c88"
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
      "unmatched:00892c44",
      "DATA",
      [
        "storage",
        "00c81ba8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00892c88",
      "DATA",
      [
        "storage",
        "00c81fa8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00892c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892c3c.md#insn-00892c44) · [`00892c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00892/00892c3c.md#insn-00892c40)
- 新版 `00892c88`（命令位置の公開資料なし）

~~~diff
- 00892c44 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00892c44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00892c44 bytes 280000f9
+ 00892c88 ["COPY", "tmp:0:8", ["register:4008:8"]]
+ 00892c88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00892c88 bytes 280000f9
- 00892c40 ["COPY", "tmp:0:8", ["const:ba8:8"]]
- 00892c40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00892c40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00892c40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00892c40 bytes 08a12e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e7ef732052989c9e558a3fdb0c7e784"></a>

### [`00893200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893200.md) → [`00893244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/00893244.md) FUN_00893244

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "site": "00893224"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00893268"
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
      "unmatched:00893224",
      "DATA",
      [
        "storage",
        "00c81d28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00893268",
      "DATA",
      [
        "storage",
        "00c82128",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00893224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893200.md#insn-00893224) · [`00893214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893200.md#insn-00893214)
- 新版 `00893268`（命令位置の公開資料なし） · `00893258`（命令位置の公開資料なし）

~~~diff
- 00893224 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00893224 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00893224 bytes 080000f9
+ 00893268 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00893268 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00893268 bytes 080000f9
- 00893214 ["INT_ADD", "register:40f0:8", ["const:893214:8", "const:4:8"]]
- 00893214 ["CALL", null, ["callee:00c57e90:8"]]
+ 00893258 ["INT_ADD", "register:40f0:8", ["const:893258:8", "const:4:8"]]
+ 00893258 ["CALL", null, ["callee:00c57e90:8"]]
- 00893214 bytes 1f120f94
+ 00893258 bytes 0e130f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5875537e1dcf0169d16a1c8b744735e"></a>

### [`0089334c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/0089334c.md) → [`00893390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/00893390.md) FUN_00893390

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 57.14% / 新版 57.14%

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
      "site": "00893370"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00893374"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008933b4"
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
      "unmatched:00893370",
      "DATA",
      [
        "storage",
        "00c81da8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00893378",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0089337c",
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
      "008933b4",
      "DATA",
      [
        "storage",
        "00c821a8",
        null,
        "undefined *"
      ]
    ],
    [
      "008933bc",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008933c0",
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

- 旧版 [`00893370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/0089334c.md#insn-00893370) · [`00893374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/0089334c.md#insn-00893374) · [`00893380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/0089334c.md#insn-00893380)

~~~diff
- 00893370 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00893370 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00893370 bytes 080000f9
- 00893374 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
- 00893374 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00893374 bytes 0080803c
- 00893380 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00893380 ["RETURN", null, ["register:0:8"]]
- 00893380 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d255e2c3637e3a969f337bc6b99aae4"></a>

### [`0089a3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089a/0089a3d0.md) → [`0089a414`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089a/0089a414.md) FUN_0089a414

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00897848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00897/00897848.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`008a8c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a8/008a8c7c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0089788c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00897/0089788c.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`008a8cc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a8/008a8cc0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 95.31% / 新版 95.31%

CFGの説明率　旧版 42.11% / 新版 44.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0089a4ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0089a4f0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "0089a4c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0089a4ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0089a554"
      ]
    ]
  ],
  "added": [
    [
      "0089a4f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0089a554"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0089a4ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089a/0089a3d0.md#insn-0089a4ac) · [`0089a4c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089a/0089a3d0.md#insn-0089a4c8)
- 新版 `0089a4f0`（命令位置の公開資料なし）

~~~diff
- 0089a4ac ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0089a4ac ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 0089a4ac bytes 21030054
- 0089a4c8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 0089a4c8 ["RETURN", null, ["register:0:8"]]
- 0089a4c8 bytes c0035fd6
+ 0089a4f0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 0089a4f0 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
+ 0089a4f0 bytes 21030054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-241d7df3f620eae72199f07929ae6d00"></a>

### [`0089b200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089b/0089b200.md) → [`0089b244`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089b/0089b244.md) FUN_0089b244

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00897848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00897/00897848.md) [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 0件 
- 新版 呼出元 2件 [`0089788c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00897/0089788c.md) [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) · 呼出先 0件 

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-fe91d9b4d290f9a5b4eb795645a5e04a"></a>

### [`008a3b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a3/008a3b20.md) → [`008a3b64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a3/008a3b64.md) FUN_008a3b64

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`008ade54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ade54.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) · 呼出先 4件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`008ade98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ad/008ade98.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 98.33% / 新版 98.33%

CFGの説明率　旧版 52.94% / 新版 47.37%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008a3b68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008a3bac"
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
      "unmatched:008a3b68",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "008a3bac",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a3b68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a3/008a3b20.md#insn-008a3b68) · [`008a3b58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a3/008a3b20.md#insn-008a3b58)
- 新版 `008a3bac`（命令位置の公開資料なし） · `008a3b9c`（命令位置の公開資料なし）

~~~diff
- 008a3b68 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 008a3b68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008a3b68 bytes e80b00f9
+ 008a3bac ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
+ 008a3bac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 008a3bac bytes e80b00f9
- 008a3b58 ["INT_RIGHT", "tmp:0:4", ["register:4048:4", "const:0:4"]]
- 008a3b58 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 008a3b58 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 008a3b58 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 008a3b9c ["INT_RIGHT", "tmp:0:4", ["register:4048:4", "const:0:4"]]
+ 008a3b9c ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 008a3b9c ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 008a3b9c ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 008a3b58 bytes 69010037
+ 008a3b9c bytes 69010037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0a682c120311d5d427d62756a428023"></a>

### [`008a3c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a3/008a3c54.md) → [`008a3c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a3/008a3c98.md) FUN_008a3c98

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0074a794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0074a/0074a794.md)
- 新版 呼出元 1件 [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0074a7d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0074a/0074a7d4.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008a3c80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008a3cc4"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`008a3c80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a3/008a3c54.md#insn-008a3c80) · [`008a3c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a3/008a3c54.md#insn-008a3c68)
- 新版 `008a3cc4`（命令位置の公開資料なし） · `008a3cac`（命令位置の公開資料なし）

~~~diff
- 008a3c80 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 008a3c80 ["INT_ADD", "tmp:1:8", ["register:4098:8", "const:68:8"]]
- 008a3c80 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008a3c80 bytes 698206f8
+ 008a3cc4 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 008a3cc4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "const:68:8"]]
+ 008a3cc4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 008a3cc4 bytes 698206f8
- 008a3c68 ["INT_ADD", "register:40f0:8", ["const:8a3c68:8", "const:4:8"]]
- 008a3c68 ["CALL", null, ["callee:0074a7d4:8"]]
+ 008a3cac ["INT_ADD", "register:40f0:8", ["const:8a3cac:8", "const:4:8"]]
+ 008a3cac ["CALL", null, ["callee:0074a7d4:8"]]
- 008a3c68 bytes cb9afa97
+ 008a3cac bytes ca9afa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56b1747109b4d5372f7c717639943bef"></a>

### [`008a3df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a3/008a3df0.md) → [`008a3e34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a3/008a3e34.md) FUN_008a3e34

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 1件 [`008b0a28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b0/008b0a28.md)
- 新版 呼出元 1件 [`0089e87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089e/0089e87c.md) · 呼出先 1件 [`008b0a6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b0/008b0a6c.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 45.45% / 新版 45.45%

CFGの説明率　旧版 14.29% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008a3e14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008a3e58"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008a3e00"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008a3e00",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008a3e50"
      ]
    ]
  ],
  "added": [
    [
      "008a3e44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008a3e50"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a3e00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a3/008a3df0.md#insn-008a3e00) · [`008a3e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a3/008a3df0.md#insn-008a3e14)
- 新版 `008a3e44`（命令位置の公開資料なし）

~~~diff
- 008a3e00 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 008a3e00 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 008a3e00 ["CBRANCH", null, ["local:b3:8", "tmp:1:1"]]
- 008a3e00 bytes 69000054
- 008a3e14 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
- 008a3e14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008a3e14 bytes 080400f9
+ 008a3e44 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 008a3e44 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
+ 008a3e44 ["CBRANCH", null, ["local:b2:8", "tmp:1:1"]]
+ 008a3e44 bytes 69000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e8618a8b86e00b347fb0731a4048229"></a>

### [`008a4390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4390.md) → [`008a43d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a4/008a43d4.md) FUN_008a43d4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

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
      "site": "008a4398"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008a43dc"
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
      "unmatched:008a4398",
      "DATA",
      [
        "storage",
        "00c82010",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a43dc",
      "DATA",
      [
        "storage",
        "00c82410",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a4398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4390.md#insn-008a4398) · [`008a4394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4390.md#insn-008a4394)
- 新版 `008a43dc`（命令位置の公開資料なし）

~~~diff
- 008a4398 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 008a4398 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008a4398 bytes 280000f9
+ 008a43dc ["COPY", "tmp:0:8", ["register:4008:8"]]
+ 008a43dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 008a43dc bytes 280000f9
- 008a4394 ["COPY", "tmp:0:8", ["const:10:8"]]
- 008a4394 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008a4394 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008a4394 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008a4394 bytes 08410091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80de65b9a3312ac1934c443f8f620b22"></a>

### [`008a4ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4ab0.md) → [`008a4af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a4/008a4af4.md) FUN_008a4af4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

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
      "site": "008a4ac8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008a4b0c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "008a4ad0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008a4ac8",
      "DATA",
      [
        "storage",
        "00c82220",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008a4acc",
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
      "008a4b0c",
      "DATA",
      [
        "storage",
        "00c82620",
        null,
        "undefined *"
      ]
    ],
    [
      "008a4b10",
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

- 旧版 [`008a4ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4ab0.md#insn-008a4ac8) · [`008a4ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4ab0.md#insn-008a4ad0)
- 新版 `008a4b0c`（命令位置の公開資料なし）

~~~diff
- 008a4ac8 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 008a4ac8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008a4ac8 bytes 080000f9
- 008a4ad0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 008a4ad0 ["RETURN", null, ["register:0:8"]]
- 008a4ad0 bytes c0035fd6
+ 008a4b0c ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 008a4b0c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 008a4b0c bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2436181096603f2aa0d43c4e11dbe11f"></a>

### [`008a4f20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4f20.md) → [`008a4f64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a4/008a4f64.md) FUN_008a4f64

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008a4f38"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008a4f7c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "008a4f40"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008a4f38",
      "DATA",
      [
        "storage",
        "00c82390",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008a4f3c",
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
      "008a4f7c",
      "DATA",
      [
        "storage",
        "00c82790",
        null,
        "undefined *"
      ]
    ],
    [
      "008a4f80",
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

- 旧版 [`008a4f38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4f20.md#insn-008a4f38) · [`008a4f40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4f20.md#insn-008a4f40)
- 新版 `008a4f7c`（命令位置の公開資料なし）

~~~diff
- 008a4f38 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 008a4f38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008a4f38 bytes 080000f9
- 008a4f40 ["COPY", "register:0:8", ["register:40f0:8"]]
- 008a4f40 ["RETURN", null, ["register:0:8"]]
- 008a4f40 bytes c0035fd6
+ 008a4f7c ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 008a4f7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 008a4f7c bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bac2095aee19e275d9fdaea7e06fbf7f"></a>

### [`008a4f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4f5c.md) → [`008a4fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a4/008a4fa0.md) FUN_008a4fa0

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 call, call_target, constant, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 88.89% / 新版 88.89%

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
      "site": "008a4fc4",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008a4f80",
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
      "008a4fc4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "008a4fc4",
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

- 旧版 [`008a4f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4f5c.md#insn-008a4f80) · [`008a4f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4f5c.md#insn-008a4f78) · [`008a4f8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4f5c.md#insn-008a4f8c)
- 新版 `008a4fc4`（命令位置の公開資料なし） · `008a4fd0`（命令位置の公開資料なし）

~~~diff
- 008a4f80 ["INT_ADD", "register:40f0:8", ["const:8a4f80:8", "const:4:8"]]
- 008a4f80 ["CALL", null, ["ram:47acb4:8"]]
+ 008a4fc4 ["INT_ADD", "register:40f0:8", ["const:8a4fc4:8", "const:4:8"]]
+ 008a4fc4 ["CALL", null, ["ram:47acf4:8"]]
- 008a4f80 bytes 4d57ef97
+ 008a4fc4 bytes 4c57ef97
- 008a4f78 ["COPY", "register:40e8:8", ["register:8:8"]]
- 008a4f78 bytes fd030091
- 008a4f8c ["INT_ADD", "register:40f0:8", ["const:8a4f8c:8", "const:4:8"]]
- 008a4f8c ["CALL", null, ["callee:0047cdd4:8"]]
+ 008a4fd0 ["INT_ADD", "register:40f0:8", ["const:8a4fd0:8", "const:4:8"]]
+ 008a4fd0 ["CALL", null, ["callee:0047cdd4:8"]]
- 008a4f8c bytes 825fef97
+ 008a4fd0 bytes 815fef97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9bfd2dd9bfb09100e1738a9b9d59a8d0"></a>

### [`008a4fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4fd0.md) → [`008a5014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a5/008a5014.md) FUN_008a5014

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 77.78% / 新版 77.78%

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
      "site": "008a4fe8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008a502c"
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
      "unmatched:008a4fe8",
      "DATA",
      [
        "storage",
        "00c82420",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a502c",
      "DATA",
      [
        "storage",
        "00c82820",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a4fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4fd0.md#insn-008a4fe8) · [`008a4fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a4/008a4fd0.md#insn-008a4fdc)
- 新版 `008a502c`（命令位置の公開資料なし） · `008a5020`（命令位置の公開資料なし）

~~~diff
- 008a4fe8 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 008a4fe8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008a4fe8 bytes 080000f9
+ 008a502c ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 008a502c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 008a502c bytes 080000f9
- 008a4fdc ["INT_ADD", "register:40f0:8", ["const:8a4fdc:8", "const:4:8"]]
- 008a4fdc ["CALL", null, ["callee:00c57e90:8"]]
+ 008a5020 ["INT_ADD", "register:40f0:8", ["const:8a5020:8", "const:4:8"]]
+ 008a5020 ["CALL", null, ["callee:00c57e90:8"]]
- 008a4fdc bytes adca0e94
+ 008a5020 bytes 9ccb0e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f907a2684e0180939aa98575859a7f5a"></a>

### [`008a5058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a5/008a5058.md) → [`008a509c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a5/008a509c.md) FUN_008a509c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 77.78% / 新版 77.78%

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
      "site": "008a5070"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008a50b4"
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
      "unmatched:008a5070",
      "DATA",
      [
        "storage",
        "00c824a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a50b4",
      "DATA",
      [
        "storage",
        "00c828a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a5070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a5/008a5058.md#insn-008a5070) · [`008a5064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a5/008a5058.md#insn-008a5064)
- 新版 `008a50b4`（命令位置の公開資料なし） · `008a50a8`（命令位置の公開資料なし）

~~~diff
- 008a5070 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 008a5070 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008a5070 bytes 080000f9
+ 008a50b4 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 008a50b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 008a50b4 bytes 080000f9
- 008a5064 ["INT_ADD", "register:40f0:8", ["const:8a5064:8", "const:4:8"]]
- 008a5064 ["CALL", null, ["callee:00c57e90:8"]]
+ 008a50a8 ["INT_ADD", "register:40f0:8", ["const:8a50a8:8", "const:4:8"]]
+ 008a50a8 ["CALL", null, ["callee:00c57e90:8"]]
- 008a5064 bytes 8bca0e94
+ 008a50a8 bytes 7acb0e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ada3ec97de9161e6f68efa3b0b93bcca"></a>

### [`008a57b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a5/008a57b8.md) → [`008a57fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a5/008a57fc.md) FUN_008a57fc

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

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
      "site": "008a57c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008a5804"
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
      "unmatched:008a57c0",
      "DATA",
      [
        "storage",
        "00c82620",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a5804",
      "DATA",
      [
        "storage",
        "00c82a20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a57c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a5/008a57b8.md#insn-008a57c0) · [`008a57bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a5/008a57b8.md#insn-008a57bc)
- 新版 `008a5804`（命令位置の公開資料なし）

~~~diff
- 008a57c0 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 008a57c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008a57c0 bytes 280000f9
+ 008a5804 ["COPY", "tmp:0:8", ["register:4008:8"]]
+ 008a5804 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 008a5804 bytes 280000f9
- 008a57bc ["COPY", "tmp:0:8", ["const:620:8"]]
- 008a57bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008a57bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008a57bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008a57bc bytes 08811891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-227d2fc988fc394a2c3b2590820b3d0c"></a>

### [`008a5954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a5/008a5954.md) → [`008a5998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a5/008a5998.md) FUN_008a5998

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008a595c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008a59a0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "008a5960"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008a595c",
      "DATA",
      [
        "storage",
        "00c826a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a59a0",
      "DATA",
      [
        "storage",
        "00c82aa0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a595c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a5/008a5954.md#insn-008a595c) · [`008a5960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a5/008a5954.md#insn-008a5960)
- 新版 `008a59a0`（命令位置の公開資料なし）

~~~diff
- 008a595c ["COPY", "tmp:0:8", ["register:4008:8"]]
- 008a595c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008a595c bytes 280000f9
- 008a5960 ["COPY", "register:0:8", ["register:40f0:8"]]
- 008a5960 ["RETURN", null, ["register:0:8"]]
- 008a5960 bytes c0035fd6
+ 008a59a0 ["COPY", "tmp:0:8", ["register:4008:8"]]
+ 008a59a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 008a59a0 bytes 280000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89a8dd0ebf6ed36938a87913103292e1"></a>

### [`008a5c18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a5/008a5c18.md) → [`008a5c5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a5/008a5c5c.md) FUN_008a5c5c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

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
      "site": "008a5c20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008a5c64"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "008a5c24"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008a5c20",
      "DATA",
      [
        "storage",
        "00c82720",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a5c64",
      "DATA",
      [
        "storage",
        "00c82b20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a5c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a5/008a5c18.md#insn-008a5c20) · [`008a5c24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a5/008a5c18.md#insn-008a5c24)
- 新版 `008a5c64`（命令位置の公開資料なし）

~~~diff
- 008a5c20 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 008a5c20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008a5c20 bytes 280000f9
- 008a5c24 ["COPY", "register:0:8", ["register:40f0:8"]]
- 008a5c24 ["RETURN", null, ["register:0:8"]]
- 008a5c24 bytes c0035fd6
+ 008a5c64 ["COPY", "tmp:0:8", ["register:4008:8"]]
+ 008a5c64 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 008a5c64 bytes 280000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2209c997af97e8bde74537aa0a6e08c5"></a>

### [`008a5d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a5/008a5d5c.md) → [`008a5da0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a5/008a5da0.md) FUN_008a5da0

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

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
      "site": "008a5d74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008a5db8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "008a5d7c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008a5d74",
      "DATA",
      [
        "storage",
        "00c827a0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008a5d78",
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
      "008a5db8",
      "DATA",
      [
        "storage",
        "00c82ba0",
        null,
        "undefined *"
      ]
    ],
    [
      "008a5dbc",
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

- 旧版 [`008a5d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a5/008a5d5c.md#insn-008a5d74) · [`008a5d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a5/008a5d5c.md#insn-008a5d7c)
- 新版 `008a5db8`（命令位置の公開資料なし）

~~~diff
- 008a5d74 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 008a5d74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008a5d74 bytes 080000f9
- 008a5d7c ["COPY", "register:0:8", ["register:40f0:8"]]
- 008a5d7c ["RETURN", null, ["register:0:8"]]
- 008a5d7c bytes c0035fd6
+ 008a5db8 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 008a5db8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 008a5db8 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e47bdcd41046d0a99a353db3e77bdc79"></a>

### [`008a61f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a6/008a61f0.md) → [`008a6234`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a6/008a6234.md) FUN_008a6234

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008a6208"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008a624c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "008a6210"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008a6208",
      "DATA",
      [
        "storage",
        "00c828a0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008a620c",
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
      "008a624c",
      "DATA",
      [
        "storage",
        "00c82ca0",
        null,
        "undefined *"
      ]
    ],
    [
      "008a6250",
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

- 旧版 [`008a6208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a6/008a61f0.md#insn-008a6208) · [`008a6210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a6/008a61f0.md#insn-008a6210)
- 新版 `008a624c`（命令位置の公開資料なし）

~~~diff
- 008a6208 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 008a6208 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008a6208 bytes 080000f9
- 008a6210 ["COPY", "register:0:8", ["register:40f0:8"]]
- 008a6210 ["RETURN", null, ["register:0:8"]]
- 008a6210 bytes c0035fd6
+ 008a624c ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 008a624c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 008a624c bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17b7c4f6ddcf3418cb6341a9e0ce09ac"></a>

### [`008a6800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a6/008a6800.md) → [`008a6844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a6/008a6844.md) FUN_008a6844

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008a6808"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008a684c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "008a680c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008a6808",
      "DATA",
      [
        "storage",
        "00c82a20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a684c",
      "DATA",
      [
        "storage",
        "00c82e20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a6808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a6/008a6800.md#insn-008a6808) · [`008a680c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a6/008a6800.md#insn-008a680c)
- 新版 `008a684c`（命令位置の公開資料なし）

~~~diff
- 008a6808 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 008a6808 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008a6808 bytes 280000f9
- 008a680c ["COPY", "register:0:8", ["register:40f0:8"]]
- 008a680c ["RETURN", null, ["register:0:8"]]
- 008a680c bytes c0035fd6
+ 008a684c ["COPY", "tmp:0:8", ["register:4008:8"]]
+ 008a684c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 008a684c bytes 280000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a26c6f2679badb37075fe0c4df8ba9f3"></a>

### [`008a7228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a7/008a7228.md) → [`008a726c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a7/008a726c.md) FUN_008a726c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 call, call_count, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008a7240"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008a7284"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "008a7234"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008a7234",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57e90"
      ]
    ],
    [
      "unmatched:008a7240",
      "DATA",
      [
        "storage",
        "00c82c10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a7278",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57e90"
      ]
    ],
    [
      "008a7284",
      "DATA",
      [
        "storage",
        "00c83010",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a7234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a7/008a7228.md#insn-008a7234) · [`008a7240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a7/008a7228.md#insn-008a7240)
- 新版 `008a7278`（命令位置の公開資料なし）

~~~diff
- 008a7234 ["INT_ADD", "register:40f0:8", ["const:8a7234:8", "const:4:8"]]
- 008a7234 ["CALL", null, ["callee:00c57e90:8"]]
- 008a7234 bytes 17c20e94
- 008a7240 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 008a7240 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008a7240 bytes 080000f9
+ 008a7278 ["INT_ADD", "register:40f0:8", ["const:8a7278:8", "const:4:8"]]
+ 008a7278 ["CALL", null, ["callee:00c57e90:8"]]
+ 008a7278 bytes 06c30e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d261f3791b907a601a5e2ab3fd3b4747"></a>

### [`008a744c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a7/008a744c.md) → [`008a7490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a7/008a7490.md) FUN_008a7490

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

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
      "site": "008a7454"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008a7498"
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
      "unmatched:008a7454",
      "DATA",
      [
        "storage",
        "00c82c80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a7498",
      "DATA",
      [
        "storage",
        "00c83080",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a7454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a7/008a744c.md#insn-008a7454) · [`008a744c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a7/008a744c.md#insn-008a744c)
- 新版 `008a7498`（命令位置の公開資料なし） · `008a7490`（命令位置の公開資料なし）

~~~diff
- 008a7454 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 008a7454 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008a7454 bytes 280000f9
+ 008a7498 ["COPY", "tmp:0:8", ["register:4008:8"]]
+ 008a7498 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 008a7498 bytes 280000f9
- 008a744c ["COPY", "register:4040:8", ["const:c82000:8"]]
+ 008a7490 ["COPY", "register:4040:8", ["const:c83000:8"]]
- 008a744c bytes c81e00f0
+ 008a7490 bytes e81e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f40ad40444e49aef6eeb65530cb335cd"></a>

### [`008a7464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a7/008a7464.md) → [`008a74a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a7/008a74a8.md) FUN_008a74a8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`0044f858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f858.md) [`0082eab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082e/0082eab8.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0044f898`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f898.md) [`0082eaf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082e/0082eaf8.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008a746c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a7/008a7464.md#insn-008a746c) · [`008a7480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a7/008a7464.md#insn-008a7480) · [`008a7484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a7/008a7464.md#insn-008a7484)
- 新版 `008a74b0`（命令位置の公開資料なし） · `008a74c4`（命令位置の公開資料なし） · `008a74c8`（命令位置の公開資料なし）

~~~diff
- 008a746c ["INT_ADD", "register:40f0:8", ["const:8a746c:8", "const:4:8"]]
- 008a746c ["CALL", null, ["callee:008514f8:8"]]
+ 008a74b0 ["INT_ADD", "register:40f0:8", ["const:8a74b0:8", "const:4:8"]]
+ 008a74b0 ["CALL", null, ["callee:008514f8:8"]]
- 008a746c bytes 13a8fe97
+ 008a74b0 bytes 12a8fe97
- 008a7480 ["INT_ADD", "register:40f0:8", ["const:8a7480:8", "const:4:8"]]
- 008a7480 ["CALL", null, ["callee:0082eaf8:8"]]
+ 008a74c4 ["INT_ADD", "register:40f0:8", ["const:8a74c4:8", "const:4:8"]]
+ 008a74c4 ["CALL", null, ["callee:0082eaf8:8"]]
- 008a7480 bytes 8e1dfe97
+ 008a74c4 bytes 8d1dfe97
- 008a7484 ["INT_ADD", "register:40f0:8", ["const:8a7484:8", "const:4:8"]]
- 008a7484 ["CALL", null, ["callee:0044f898:8"]]
+ 008a74c8 ["INT_ADD", "register:40f0:8", ["const:8a74c8:8", "const:4:8"]]
+ 008a74c8 ["CALL", null, ["callee:0044f898:8"]]
- 008a7484 bytes f5a0ee97
+ 008a74c8 bytes f4a0ee97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-192005cddb2bfbafae9161dfe32036be"></a>

### [`008a74ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a7/008a74ec.md) → [`008a7530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a7/008a7530.md) FUN_008a7530

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

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
      "site": "008a74f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008a7538"
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
      "unmatched:008a74f4",
      "DATA",
      [
        "storage",
        "00c82d00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a7538",
      "DATA",
      [
        "storage",
        "00c83100",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a74f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a7/008a74ec.md#insn-008a74f4) · [`008a74ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a7/008a74ec.md#insn-008a74ec)
- 新版 `008a7538`（命令位置の公開資料なし） · `008a7530`（命令位置の公開資料なし）

~~~diff
- 008a74f4 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 008a74f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008a74f4 bytes 280000f9
+ 008a7538 ["COPY", "tmp:0:8", ["register:4008:8"]]
+ 008a7538 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 008a7538 bytes 280000f9
- 008a74ec ["COPY", "register:4040:8", ["const:c82000:8"]]
+ 008a7530 ["COPY", "register:4040:8", ["const:c83000:8"]]
- 008a74ec bytes c81e00f0
+ 008a7530 bytes e81e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fef409d315c0d0871fefcbe378db32ef"></a>

### [`008a7504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a7/008a7504.md) → [`008a7548`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a7/008a7548.md) FUN_008a7548

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`0044f858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f858.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0044f898`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044f898.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008a750c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a7/008a7504.md#insn-008a750c) · [`008a7520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a7/008a7504.md#insn-008a7520)
- 新版 `008a7550`（命令位置の公開資料なし） · `008a7564`（命令位置の公開資料なし）

~~~diff
- 008a750c ["INT_ADD", "register:40f0:8", ["const:8a750c:8", "const:4:8"]]
- 008a750c ["CALL", null, ["callee:0044f898:8"]]
+ 008a7550 ["INT_ADD", "register:40f0:8", ["const:8a7550:8", "const:4:8"]]
+ 008a7550 ["CALL", null, ["callee:0044f898:8"]]
- 008a750c bytes d3a0ee97
+ 008a7550 bytes d2a0ee97
- 008a7520 ["COPY", "register:0:8", ["register:4010:8"]]
- 008a7520 ["BRANCHIND", null, ["register:0:8"]]
- 008a7520 bytes 40001fd6
+ 008a7564 ["COPY", "register:0:8", ["register:4010:8"]]
+ 008a7564 ["BRANCHIND", null, ["register:0:8"]]
+ 008a7564 bytes 40001fd6
~~~


<a id="compare-c50c307ed50707e786fd893a04d28aa4"></a>

### [`008a76d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a7/008a76d8.md) → [`008a771c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a7/008a771c.md) FUN_008a771c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 77.78% / 新版 77.78%

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
      "site": "008a76f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008a7734"
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
      "unmatched:008a76f0",
      "DATA",
      [
        "storage",
        "00c82e20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a7734",
      "DATA",
      [
        "storage",
        "00c83220",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a76f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a7/008a76d8.md#insn-008a76f0) · [`008a76e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a7/008a76d8.md#insn-008a76e4)
- 新版 `008a7734`（命令位置の公開資料なし） · `008a7728`（命令位置の公開資料なし）

~~~diff
- 008a76f0 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 008a76f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008a76f0 bytes 080000f9
+ 008a7734 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 008a7734 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 008a7734 bytes 080000f9
- 008a76e4 ["INT_ADD", "register:40f0:8", ["const:8a76e4:8", "const:4:8"]]
- 008a76e4 ["CALL", null, ["callee:00c57e90:8"]]
+ 008a7728 ["INT_ADD", "register:40f0:8", ["const:8a7728:8", "const:4:8"]]
+ 008a7728 ["CALL", null, ["callee:00c57e90:8"]]
- 008a76e4 bytes ebc00e94
+ 008a7728 bytes dac10e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89bd06b2b89cc10569574a31d83ac4da"></a>

### [`008a7824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a7/008a7824.md) → [`008a7868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a7/008a7868.md) FUN_008a7868

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 77.78% / 新版 77.78%

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
      "site": "008a783c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008a7880"
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
      "unmatched:008a783c",
      "DATA",
      [
        "storage",
        "00c82eb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a7880",
      "DATA",
      [
        "storage",
        "00c832b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a783c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a7/008a7824.md#insn-008a783c) · [`008a7830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a7/008a7824.md#insn-008a7830)
- 新版 `008a7880`（命令位置の公開資料なし） · `008a7874`（命令位置の公開資料なし）

~~~diff
- 008a783c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 008a783c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008a783c bytes 080000f9
+ 008a7880 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 008a7880 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 008a7880 bytes 080000f9
- 008a7830 ["INT_ADD", "register:40f0:8", ["const:8a7830:8", "const:4:8"]]
- 008a7830 ["CALL", null, ["callee:00c57e90:8"]]
+ 008a7874 ["INT_ADD", "register:40f0:8", ["const:8a7874:8", "const:4:8"]]
+ 008a7874 ["CALL", null, ["callee:00c57e90:8"]]
- 008a7830 bytes 98c00e94
+ 008a7874 bytes 87c10e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1c80af06c5bbae555ea5dff2c618304"></a>

### [`008a7abc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a7/008a7abc.md) → [`008a7b00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008a7/008a7b00.md) FUN_008a7b00

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 77.78% / 新版 77.78%

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
      "site": "008a7ad4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008a7b18"
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
      "unmatched:008a7ad4",
      "DATA",
      [
        "storage",
        "00c82f30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008a7b18",
      "DATA",
      [
        "storage",
        "00c83330",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008a7ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a7/008a7abc.md#insn-008a7ad4) · [`008a7ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008a7/008a7abc.md#insn-008a7ac8)
- 新版 `008a7b18`（命令位置の公開資料なし） · `008a7b0c`（命令位置の公開資料なし）

~~~diff
- 008a7ad4 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 008a7ad4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008a7ad4 bytes 080000f9
+ 008a7b18 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 008a7b18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 008a7b18 bytes 080000f9
- 008a7ac8 ["INT_ADD", "register:40f0:8", ["const:8a7ac8:8", "const:4:8"]]
- 008a7ac8 ["CALL", null, ["callee:00c57e90:8"]]
+ 008a7b0c ["INT_ADD", "register:40f0:8", ["const:8a7b0c:8", "const:4:8"]]
+ 008a7b0c ["CALL", null, ["callee:00c57e90:8"]]
- 008a7ac8 bytes f2bf0e94
+ 008a7b0c bytes e1c00e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-221310f3c5c064b429a762d21c968108"></a>

### [`008ab84c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ab/008ab84c.md) → [`008ab890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ab/008ab890.md) FUN_008ab890

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

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
      "site": "008ab870"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008ab8b4"
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
      "unmatched:008ab870",
      "DATA",
      [
        "storage",
        "00c830a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ab8b4",
      "DATA",
      [
        "storage",
        "00c834a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ab870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ab/008ab84c.md#insn-008ab870) · [`008ab860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ab/008ab84c.md#insn-008ab860)
- 新版 `008ab8b4`（命令位置の公開資料なし） · `008ab8a4`（命令位置の公開資料なし）

~~~diff
- 008ab870 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 008ab870 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008ab870 bytes 080000f9
+ 008ab8b4 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 008ab8b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 008ab8b4 bytes 080000f9
- 008ab860 ["INT_ADD", "register:40f0:8", ["const:8ab860:8", "const:4:8"]]
- 008ab860 ["CALL", null, ["callee:00c57e90:8"]]
+ 008ab8a4 ["INT_ADD", "register:40f0:8", ["const:8ab8a4:8", "const:4:8"]]
+ 008ab8a4 ["CALL", null, ["callee:00c57e90:8"]]
- 008ab860 bytes 8cb00e94
+ 008ab8a4 bytes 7bb10e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3205cd958baa49fbf9b0f087b2f3918f"></a>

### [`008ab924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ab/008ab924.md) → [`008ab968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ab/008ab968.md) FUN_008ab968

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`008ab274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ab/008ab274.md) [`00a3bb4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3b/00a3bb4c.md) [`00a3cc20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3c/00a3cc20.md) [`00a3d7fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3d/00a3d7fc.md) [`00a3d8a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3d/00a3d8a8.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 5件 [`008ab2b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ab/008ab2b8.md) [`00a3bd44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3b/00a3bd44.md) [`00a3ce18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3c/00a3ce18.md) [`00a3d9f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3d/00a3d9f4.md) [`00a3daa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3d/00a3daa0.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 39.73% / 新版 39.19%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 5件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008aba10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008aba54"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008ab958"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008ab974",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008ab9c8"
      ]
    ],
    [
      "008abacc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:008abaa4"
      ]
    ],
    [
      "unmatched:008abaa0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008abad0"
      ]
    ]
  ],
  "added": [
    [
      "008ab9b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008ab9c8"
      ]
    ],
    [
      "008abacc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008abae8"
      ]
    ],
    [
      "008abae4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008abad0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ab958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ab/008ab924.md#insn-008ab958) · [`008ab974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ab/008ab924.md#insn-008ab974) · [`008ab99c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ab/008ab924.md#insn-008ab99c)
- 新版 `008ab9e0`（命令位置の公開資料なし）

~~~diff
- 008ab958 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 008ab958 ["COPY", "tmp:1:8", ["register:4058:8"]]
- 008ab958 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 008ab958 ["COPY", "tmp:1:8", ["register:4060:8"]]
- 008ab958 bytes 6bb18c9a
- 008ab974 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 008ab974 ["BOOL_OR", "tmp:1:1", ["register:101:1", "tmp:0:1"]]
- 008ab974 ["CBRANCH", null, ["local:b8:8", "tmp:1:1"]]
- 008ab974 bytes 8d000054
- 008ab99c ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 008ab99c ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 008ab9e0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 008ab9e0 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 008ab99c bytes 49ffffb5
+ 008ab9e0 bytes 49ffffb5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b190371c4a28f1e8e9f0c9f72e61f47"></a>

### [`008ac918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008ac918.md) → [`008ac95c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ac/008ac95c.md) FUN_008ac95c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`0058fb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fb40.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0058fb80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0058f/0058fb80.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 constant, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.45% / 新版 95.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008ac920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008ac918.md#insn-008ac920) · [`008ac938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008ac918.md#insn-008ac938) · [`008ac93c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008ac918.md#insn-008ac93c)
- 新版 `008ac97c`（命令位置の公開資料なし） · `008ac980`（命令位置の公開資料なし）

~~~diff
- 008ac920 ["COPY", "register:40e8:8", ["register:8:8"]]
- 008ac920 bytes fd030091
- 008ac938 ["INT_ADD", "register:40f0:8", ["const:8ac938:8", "const:4:8"]]
- 008ac938 ["CALL", null, ["callee:0058fb80:8"]]
+ 008ac97c ["INT_ADD", "register:40f0:8", ["const:8ac97c:8", "const:4:8"]]
+ 008ac97c ["CALL", null, ["callee:0058fb80:8"]]
- 008ac938 bytes 828cf397
+ 008ac97c bytes 818cf397
- 008ac93c ["INT_ADD", "register:40f0:8", ["const:8ac93c:8", "const:4:8"]]
- 008ac93c ["CALL", null, ["callee:008514f8:8"]]
+ 008ac980 ["INT_ADD", "register:40f0:8", ["const:8ac980:8", "const:4:8"]]
+ 008ac980 ["CALL", null, ["callee:008514f8:8"]]
- 008ac93c bytes df92fe97
+ 008ac980 bytes de92fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52536b0be49dcbf066e26e9f8e8dfceb"></a>

### [`008ac998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008ac998.md) → [`008ac9dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ac/008ac9dc.md) FUN_008ac9dc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`008ac33c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008ac33c.md) [`008fd364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fd/008fd364.md) [`008fe3e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fe/008fe3e8.md) [`008fe494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fe/008fe494.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 4件 [`008ac380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ac/008ac380.md) [`008fd500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fd/008fd500.md) [`008fe584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fe/008fe584.md) [`008fe630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fe/008fe630.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 94.62% / 新版 94.62%

CFGの説明率　旧版 42.86% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008ac9b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008acb48"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008acb68"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008ac9b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008acb64"
      ]
    ],
    [
      "008aca2c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:008ac9f8"
      ]
    ],
    [
      "008aca54",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:008ac9f8"
      ]
    ]
  ],
  "added": [
    [
      "008ac9f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008acb64"
      ]
    ],
    [
      "008aca2c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008aca3c"
      ]
    ],
    [
      "008aca54",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008aca3c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ac9b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008ac998.md#insn-008ac9b4) · [`008ac9f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008ac998.md#insn-008ac9f8)
- 新版 `008ac9f8`（命令位置の公開資料なし）

~~~diff
- 008ac9b4 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 008ac9b4 ["CBRANCH", null, ["local:b36:8", "tmp:0:1"]]
- 008ac9b4 bytes 690b00b4
- 008ac9f8 ["COPY", "register:40b0:8", ["register:4048:8"]]
- 008ac9f8 bytes f60309aa
+ 008ac9f8 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 008ac9f8 ["CBRANCH", null, ["local:b34:8", "tmp:0:1"]]
+ 008ac9f8 bytes 690b00b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4429bbe2783dc32bf39e6bd21984d20"></a>

### [`008acf5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008acf5c.md) → [`008acfa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ac/008acfa0.md) FUN_008acfa0

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 77.78% / 新版 77.78%

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
      "site": "008acf74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008acfb8"
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
      "unmatched:008acf74",
      "DATA",
      [
        "storage",
        "00c834a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008acfb8",
      "DATA",
      [
        "storage",
        "00c838a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008acf74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008acf5c.md#insn-008acf74) · [`008acf68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008acf5c.md#insn-008acf68)
- 新版 `008acfb8`（命令位置の公開資料なし） · `008acfac`（命令位置の公開資料なし）

~~~diff
- 008acf74 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 008acf74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008acf74 bytes 080000f9
+ 008acfb8 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 008acfb8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 008acfb8 bytes 080000f9
- 008acf68 ["INT_ADD", "register:40f0:8", ["const:8acf68:8", "const:4:8"]]
- 008acf68 ["CALL", null, ["callee:00c57e90:8"]]
+ 008acfac ["INT_ADD", "register:40f0:8", ["const:8acfac:8", "const:4:8"]]
+ 008acfac ["CALL", null, ["callee:00c57e90:8"]]
- 008acf68 bytes caaa0e94
+ 008acfac bytes b9ab0e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b46b6ef7432626b7221bc378222ac5e"></a>

### [`008acf80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008acf80.md) → [`008acfc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ac/008acfc4.md) FUN_008acfc4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

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
      "site": "008acf88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008acfcc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "008acf8c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008acf88",
      "DATA",
      [
        "storage",
        "00c834a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008acfcc",
      "DATA",
      [
        "storage",
        "00c838a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008acf88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008acf80.md#insn-008acf88) · [`008acf8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ac/008acf80.md#insn-008acf8c)
- 新版 `008acfcc`（命令位置の公開資料なし）

~~~diff
- 008acf88 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 008acf88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008acf88 bytes 280000f9
- 008acf8c ["COPY", "register:0:8", ["register:40f0:8"]]
- 008acf8c ["RETURN", null, ["register:0:8"]]
- 008acf8c bytes c0035fd6
+ 008acfcc ["COPY", "tmp:0:8", ["register:4008:8"]]
+ 008acfcc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 008acfcc bytes 280000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-569bb2668824a95133a7b841d4df69a8"></a>

### [`008ad048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad048.md) → [`008ad08c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ad/008ad08c.md) FUN_008ad08c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`008ad17c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad17c.md) [`008ad180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad180.md) [`00b39fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b39/00b39fc8.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`008ad1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ad/008ad1c0.md) [`008ad1c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ad/008ad1c4.md) [`00b3a3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3a/00b3a3f0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 73.53% / 新版 73.53%

CFGの説明率　旧版 30.77% / 新版 36.36%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ad04c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ad04c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ad050"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008ad04c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:008ad050",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008ad0b4",
      "DATA",
      [
        "storage",
        "00c835a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ad090",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "008ad094",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008ad0b4",
      "DATA",
      [
        "storage",
        "00c839a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ad04c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad048.md#insn-008ad04c) · [`008ad050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad048.md#insn-008ad050) · [`008ad074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad048.md#insn-008ad074)

~~~diff
- 008ad04c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008ad04c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008ad04c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 008ad04c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008ad04c bytes fd7b04a9
- 008ad050 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 008ad050 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 008ad050 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 008ad050 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008ad050 bytes f44f05a9
- 008ad074 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 008ad074 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 008ad074 bytes f31300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf635eb01973fe38e715d74069ea9d8c"></a>

### [`008ad184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad184.md) → [`008ad1c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ad/008ad1c8.md) FUN_008ad1c8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`008ad2c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad2c4.md) [`008ad2c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad2c8.md) [`00b3a190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3a190.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`008ad308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ad/008ad308.md) [`008ad30c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ad/008ad30c.md) [`00b3a5b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3a/00b3a5b8.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 56.76% / 新版 56.76%

CFGの説明率　旧版 46.67% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ad188"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ad188"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ad18c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008ad188",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:008ad18c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:008ad19c",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "008ad1cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "008ad1d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008ad1e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ad188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad184.md#insn-008ad188) · [`008ad18c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad184.md#insn-008ad18c) · [`008ad19c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad184.md#insn-008ad19c)

~~~diff
- 008ad188 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008ad188 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008ad188 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 008ad188 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008ad188 bytes fd7b04a9
- 008ad18c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 008ad18c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 008ad18c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 008ad18c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008ad18c bytes f44f05a9
- 008ad19c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008ad19c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 008ad19c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008ad19c bytes a8831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f468a872b1e3c38d28d0346ce086e9f5"></a>

### [`008ad290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad290.md) → [`008ad2d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ad/008ad2d4.md) FUN_008ad2d4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

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
      "site": "008ad2a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008ad2ec"
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
      "unmatched:008ad2a8",
      "DATA",
      [
        "storage",
        "00c83610",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ad2ec",
      "DATA",
      [
        "storage",
        "00c83a10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ad2a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad290.md#insn-008ad2a8) · [`008ad294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad290.md#insn-008ad294)
- 新版 `008ad2ec`（命令位置の公開資料なし）

~~~diff
- 008ad2a8 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 008ad2a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008ad2a8 bytes 080000f9
+ 008ad2ec ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 008ad2ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 008ad2ec bytes 080000f9
- 008ad294 ["COPY", "register:40e8:8", ["register:8:8"]]
- 008ad294 bytes fd030091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50d3dd4414c5479b62a390e96a76746b"></a>

### [`008ad2b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad2b4.md) → [`008ad2f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ad/008ad2f8.md) FUN_008ad2f8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

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
      "site": "008ad2bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008ad300"
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
      "unmatched:008ad2bc",
      "DATA",
      [
        "storage",
        "00c83610",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ad300",
      "DATA",
      [
        "storage",
        "00c83a10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ad2bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad2b4.md#insn-008ad2bc) · [`008ad2b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad2b4.md#insn-008ad2b8)
- 新版 `008ad300`（命令位置の公開資料なし）

~~~diff
- 008ad2bc ["COPY", "tmp:0:8", ["register:4008:8"]]
- 008ad2bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008ad2bc bytes 280000f9
+ 008ad300 ["COPY", "tmp:0:8", ["register:4008:8"]]
+ 008ad300 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 008ad300 bytes 280000f9
- 008ad2b8 ["COPY", "tmp:0:8", ["const:610:8"]]
- 008ad2b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ad2b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ad2b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ad2b8 bytes 08411891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81cb00584c6f1f4f79d522daa42a5c3b"></a>

### [`008ad2cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad2cc.md) → [`008ad310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ad/008ad310.md) FUN_008ad310

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 14件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00442af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/00442af8.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`0071c420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071c/0071c420.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00442b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442b38.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`0071c460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071c/0071c460.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 89.54% / 新版 89.54%

CFGの説明率　旧版 40.35% / 新版 41.07%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ad2e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ad414"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ad41c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008ad2e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:008ad304",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071c420"
      ]
    ],
    [
      "unmatched:008ad33c",
      "READ",
      [
        "storage",
        "002a338f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008ad32c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "008ad348",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071c460"
      ]
    ],
    [
      "008ad380",
      "READ",
      [
        "storage",
        "002a345c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ad2e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad2cc.md#insn-008ad2e8) · [`008ad304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad2cc.md#insn-008ad304) · [`008ad32c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad2cc.md#insn-008ad32c)
- 新版 `008ad370`（命令位置の公開資料なし）

~~~diff
- 008ad2e8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008ad2e8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 008ad2e8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008ad2e8 bytes a8831ff8
- 008ad304 ["INT_ADD", "register:40f0:8", ["const:8ad304:8", "const:4:8"]]
- 008ad304 ["CALL", null, ["ram:71c420:8"]]
- 008ad304 bytes 47bcf997
- 008ad32c ["INT_ADD", "register:40f0:8", ["const:8ad32c:8", "const:4:8"]]
- 008ad32c ["CALL", null, ["callee:008514f8:8"]]
+ 008ad370 ["INT_ADD", "register:40f0:8", ["const:8ad370:8", "const:4:8"]]
+ 008ad370 ["CALL", null, ["callee:008514f8:8"]]
- 008ad32c bytes 6390fe97
+ 008ad370 bytes 6290fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0953454d870c563ce1d3ca1d3af43bed"></a>

### [`008ad698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad698.md) → [`008ad6dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ad/008ad6dc.md) FUN_008ad6dc

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ad6a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008ad6e4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "008ad6a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008ad6a0",
      "DATA",
      [
        "storage",
        "00c83680",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ad6e4",
      "DATA",
      [
        "storage",
        "00c83a80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ad6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad698.md#insn-008ad6a0) · [`008ad6a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad698.md#insn-008ad6a4)
- 新版 `008ad6e4`（命令位置の公開資料なし）

~~~diff
- 008ad6a0 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 008ad6a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008ad6a0 bytes 280000f9
- 008ad6a4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 008ad6a4 ["RETURN", null, ["register:0:8"]]
- 008ad6a4 bytes c0035fd6
+ 008ad6e4 ["COPY", "tmp:0:8", ["register:4008:8"]]
+ 008ad6e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 008ad6e4 bytes 280000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dac56a321cb3f5883e36f7f91b514846"></a>

### [`008ad6b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad6b0.md) → [`008ad6f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ad/008ad6f4.md) FUN_008ad6f4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008ad6b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008ad6fc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "008ad6d4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008ad6b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008ad738"
      ]
    ],
    [
      "unmatched:008ad6d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "008ad6fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008ad738"
      ]
    ],
    [
      "008ad718",
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

- 旧版 [`008ad6b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad6b0.md#insn-008ad6b8) · [`008ad6d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad6b0.md#insn-008ad6d4)
- 新版 `008ad6fc`（命令位置の公開資料なし）

~~~diff
- 008ad6b8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 008ad6b8 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 008ad6b8 bytes e1010054
- 008ad6d4 ["INT_ADD", "register:40f0:8", ["const:8ad6d4:8", "const:4:8"]]
- 008ad6d4 ["CALL", null, ["ram:47acb4:8"]]
- 008ad6d4 bytes 7835ef97
+ 008ad6fc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 008ad6fc ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 008ad6fc bytes e1010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e3c8d204fcc68536b32423ebf17e63d"></a>

### [`008ad724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad724.md) → [`008ad768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ad/008ad768.md) FUN_008ad768

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 11.11% / 新版 11.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ad73c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008ad780"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "008ad730"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008ad730",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57e90"
      ]
    ],
    [
      "unmatched:008ad73c",
      "DATA",
      [
        "storage",
        "00c83730",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008ad740",
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
      "008ad774",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57e90"
      ]
    ],
    [
      "008ad780",
      "DATA",
      [
        "storage",
        "00c83b30",
        null,
        "undefined *"
      ]
    ],
    [
      "008ad784",
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

- 旧版 [`008ad730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad724.md#insn-008ad730) · [`008ad73c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad724.md#insn-008ad73c) · [`008ad744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008ad724.md#insn-008ad744)

~~~diff
- 008ad730 ["INT_ADD", "register:40f0:8", ["const:8ad730:8", "const:4:8"]]
- 008ad730 ["CALL", null, ["callee:00c57e90:8"]]
- 008ad730 bytes d8a80e94
- 008ad73c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 008ad73c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008ad73c bytes 080000f9
- 008ad744 ["COPY", "register:0:8", ["register:40f0:8"]]
- 008ad744 ["RETURN", null, ["register:0:8"]]
- 008ad744 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2abec7aed731b29c831ad04cf0e4d280"></a>

### [`008adc24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008adc24.md) → [`008adc68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ad/008adc68.md) FUN_008adc68

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

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
      "site": "008adc3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008adc80"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "008adc44"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008adc3c",
      "DATA",
      [
        "storage",
        "00c83820",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008adc40",
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
      "008adc80",
      "DATA",
      [
        "storage",
        "00c83c20",
        null,
        "undefined *"
      ]
    ],
    [
      "008adc84",
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

- 旧版 [`008adc3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008adc24.md#insn-008adc3c) · [`008adc44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008adc24.md#insn-008adc44)
- 新版 `008adc80`（命令位置の公開資料なし）

~~~diff
- 008adc3c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 008adc3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008adc3c bytes 080000f9
- 008adc44 ["COPY", "register:0:8", ["register:40f0:8"]]
- 008adc44 ["RETURN", null, ["register:0:8"]]
- 008adc44 bytes c0035fd6
+ 008adc80 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 008adc80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 008adc80 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b3856aa7a09ee0f7e6edd0e225ceee2"></a>

### [`008b6894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6894.md) → [`008b68d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b68d8.md) FUN_008b68d8

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008b6fa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6fa8.md) · 呼出先 5件 [`008b79d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b79d4.md) [`008b7aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7aa0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`008b6fec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6fec.md) · 呼出先 5件 [`008b7a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b7a18.md) [`008b7ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b7ae4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 88.66% / 新版 88.66%

CFGの説明率　旧版 52.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008b68f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008b69cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008b69d0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008b68f0",
      "READ",
      [
        "storage",
        "00c9af68",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:008b68f8",
      "DATA",
      [
        "storage",
        "00c8b358",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008b69c0",
      "READ",
      [
        "storage",
        "00ca41f0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "008b6934",
      "READ",
      [
        "storage",
        "00c9b368",
        null,
        "pointer"
      ]
    ],
    [
      "008b693c",
      "DATA",
      [
        "storage",
        "00c8b758",
        null,
        "undefined *"
      ]
    ],
    [
      "008b6a04",
      "READ",
      [
        "storage",
        "00ca45f0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b68f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6894.md#insn-008b68f8) · [`008b698c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6894.md#insn-008b698c)
- 新版 `008b693c`（命令位置の公開資料なし）

~~~diff
- 008b68f8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008b68f8 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 008b68f8 ["INT_ADD", "register:4048:8", ["register:4048:8", "const:50:8"]]
- 008b68f8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008b68f8 bytes 280505f8
+ 008b693c ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 008b693c ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 008b693c ["INT_ADD", "register:4048:8", ["register:4048:8", "const:50:8"]]
+ 008b693c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 008b693c bytes 280505f8
- 008b698c ["COPY", "register:0:8", ["register:4040:8"]]
- 008b698c ["INT_ADD", "register:40f0:8", ["const:8b698c:8", "const:4:8"]]
- 008b698c ["CALLIND", null, ["register:0:8"]]
- 008b698c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8dc9b3d88dbbafd0194fc7523f6bbc2"></a>

### [`008b6a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6a18.md) → [`008b6a5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6a5c.md) FUN_008b6a5c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 12件 [`00697770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/00697770.md) [`00698958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00698/00698958.md) [`0069900c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00699/0069900c.md) [`007f46b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f4/007f46b8.md) [`007fa950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fa/007fa950.md) · 呼出先 12件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048dc0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048dc0c.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00859b0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00859/00859b0c.md)
- 新版 呼出元 12件 [`006977b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00697/006977b0.md) [`00698998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00698/00698998.md) [`0069904c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00699/0069904c.md) [`007f46f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007f4/007f46f8.md) [`007fa990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007fa990.md) · 呼出先 12件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`0048dc4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048d/0048dc4c.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00859b4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859b4c.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 91.57% / 新版 91.57%

CFGの説明率　旧版 49.37% / 新版 48.75%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008b6b78"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008b6b7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008b6b80"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008b6afc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "unmatched:008b6b7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:008b6b80",
      "WRITE",
      [
        "storage",
        "Stack[-0x44]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "008b6b40",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ],
    [
      "008b6bc0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "008b6bc4",
      "WRITE",
      [
        "storage",
        "Stack[-0x44]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b6afc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6a18.md#insn-008b6afc) · [`008b6b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6a18.md#insn-008b6b78)
- 新版 `008b6b40`（命令位置の公開資料なし）

~~~diff
- 008b6afc ["INT_ADD", "register:40f0:8", ["const:8b6afc:8", "const:4:8"]]
- 008b6afc ["CALL", null, ["ram:48ccb8:8"]]
- 008b6afc bytes 6f58ef97
+ 008b6b40 ["INT_ADD", "register:40f0:8", ["const:8b6b40:8", "const:4:8"]]
+ 008b6b40 ["CALL", null, ["ram:48ccf8:8"]]
+ 008b6b40 bytes 6e58ef97
- 008b6b78 ["COPY", "tmp:0:4", ["const:0:4"]]
- 008b6b78 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 008b6b78 ["INT_ADD", "tmp:2:8", ["register:4098:8", "const:64:8"]]
- 008b6b78 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 008b6b78 bytes 7f920139
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eed32f6b70b0e9a018d266dcf55e9a63"></a>

### [`008b6e34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e34.md) → [`008b6e78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6e78.md) FUN_008b6e78

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) · 呼出先 0件 
- 新版 呼出元 1件 [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 60.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`008b6e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e34.md#insn-008b6e40) · [`008b6e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e34.md#insn-008b6e50) · [`008b6e58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e34.md#insn-008b6e58)
- 新版 `008b6e84`（命令位置の公開資料なし） · `008b6e94`（命令位置の公開資料なし）

~~~diff
- 008b6e40 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 008b6e40 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 008b6e84 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 008b6e84 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 008b6e40 bytes eb000054
+ 008b6e84 bytes eb000054
- 008b6e50 ["CBRANCH", null, ["local:b3:8", "register:102:1"]]
+ 008b6e94 ["CBRANCH", null, ["local:b4:8", "register:102:1"]]
- 008b6e50 bytes 62000054
+ 008b6e94 bytes 62000054
- 008b6e58 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fffffffffffffffc:8"]]
- 008b6e58 ["LOAD", "register:5000:4", ["const:1b1:8", "tmp:0:8"]]
- 008b6e58 ["COPY", "register:5004:4", ["const:0:4"]]
- 008b6e58 ["COPY", "register:5008:8", ["const:0:8"]]
- 008b6e58 bytes 00c15fbc
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d7fdbe4a4bb147acfa083656bab06d9"></a>

### [`008b7904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7904.md) → [`008b7948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b7948.md) FUN_008b7948

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 27件 [`00658364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00658/00658364.md) [`00659e5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00659/00659e5c.md) [`0065bdec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065b/0065bdec.md) [`0068ba90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068b/0068ba90.md) [`00696de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00696/00696de4.md) · 呼出先 2件 [`008b7c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7c08.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 27件 [`006583a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00658/006583a4.md) [`00659e9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00659/00659e9c.md) [`0065be2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065b/0065be2c.md) [`0068bad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068b/0068bad0.md) [`00696e24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00696/00696e24.md) · 呼出先 2件 [`008b7c4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b7c4c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008b790c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008b7950"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008b7968",
      "incomplete_value": true,
      "site": "008b796c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:4:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008b790c",
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
      "008b7950",
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

- 旧版 [`008b790c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7904.md#insn-008b790c) · [`008b7928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7904.md#insn-008b7928)
- 新版 `008b796c`（命令位置の公開資料なし） · `008b7950`（命令位置の公開資料なし）

~~~diff
- 008b790c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 008b790c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 008b790c bytes f31300f9
- 008b7928 ["INT_ADD", "register:40f0:8", ["const:8b7928:8", "const:4:8"]]
- 008b7928 ["CALL", null, ["callee:008b7c4c:8"]]
+ 008b796c ["INT_ADD", "register:40f0:8", ["const:8b796c:8", "const:4:8"]]
+ 008b796c ["CALL", null, ["callee:008b7c4c:8"]]
- 008b7928 bytes b8000094
+ 008b796c bytes b8000094
+ 008b7950 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
+ 008b7950 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 008b7950 bytes f31300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bef69b1e832b898e61770a49fa225e5"></a>

### [`008b7984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7984.md) → [`008b79c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b79c8.md) FUN_008b79c8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 186件 [`005c6938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c6/005c6938.md) [`005c71e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c7/005c71e0.md) [`005c7cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c7/005c7cc0.md) [`005c8780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c8/005c8780.md) [`005c8ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c8/005c8ebc.md) · 呼出先 0件 
- 新版 呼出元 186件 [`005c6978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c6/005c6978.md) [`005c7220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c7/005c7220.md) [`005c7d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c7/005c7d00.md) [`005c87c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c8/005c87c0.md) [`005c8efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c8/005c8efc.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 66.67% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008b79b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008b79fc"
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
      "unmatched:008b79b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008b7a08"
      ]
    ]
  ],
  "added": [
    [
      "008b79fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008b7a08"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b79b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7984.md#insn-008b79b8) · [`008b7988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7984.md#insn-008b7988)
- 新版 `008b79fc`（命令位置の公開資料なし） · `008b79cc`（命令位置の公開資料なし）

~~~diff
- 008b79b8 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 008b79b8 ["BOOL_OR", "tmp:1:1", ["register:101:1", "tmp:0:1"]]
- 008b79b8 ["CBRANCH", null, ["local:b6:8", "tmp:1:1"]]
- 008b79b8 bytes 6d000054
+ 008b79fc ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 008b79fc ["BOOL_OR", "tmp:1:1", ["register:101:1", "tmp:0:1"]]
+ 008b79fc ["CBRANCH", null, ["local:b7:8", "tmp:1:1"]]
+ 008b79fc bytes 6d000054
- 008b7988 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 008b7988 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 008b79cc ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 008b79cc ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 008b7988 bytes a90100b4
+ 008b79cc bytes a90100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8a56114609a9de199128a49a162b731"></a>

### [`008b79d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b79d4.md) → [`008b7a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b7a18.md) FUN_008b7a18

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`008b6894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6894.md) [`008b6fa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6fa8.md) [`008b7388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7388.md) [`008b79d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b79d4.md) · 呼出先 3件 [`008b79d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b79d4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 4件 [`008b68d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b68d8.md) [`008b6fec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6fec.md) [`008b73cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b73cc.md) [`008b7a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b7a18.md) · 呼出先 3件 [`008b7a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b7a18.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 90.20% / 新版 90.20%

CFGの説明率　旧版 60.00% / 新版 56.25%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008b7a4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008b7a90"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008b7a30"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008b7a30",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008b7aa4"
      ]
    ],
    [
      "008b7a80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:008b7a2c"
      ]
    ],
    [
      "008b7a8c",
      "DATA",
      [
        "storage",
        "00c8b358",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b7a74",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008b7aa4"
      ]
    ],
    [
      "008b7a80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008b7a70"
      ]
    ],
    [
      "008b7a8c",
      "DATA",
      [
        "storage",
        "00c8b758",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b7a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b79d4.md#insn-008b7a30) · [`008b7a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b79d4.md#insn-008b7a4c)
- 新版 `008b7a74`（命令位置の公開資料なし）

~~~diff
- 008b7a30 ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
- 008b7a30 bytes 80010054
- 008b7a4c ["COPY", "tmp:0:8", ["register:8:8"]]
- 008b7a4c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008b7a4c bytes e80300f9
+ 008b7a74 ["CBRANCH", null, ["local:b8:8", "register:101:1"]]
+ 008b7a74 bytes 80010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb7b4e34fb40bea5ae8585dfd35e5e02"></a>

### [`008b7aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7aa0.md) → [`008b7ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b7ae4.md) FUN_008b7ae4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008b6894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6894.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`008b68d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b68d8.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call_argument_candidate, call_target, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 94.38% / 新版 94.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 2件, `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "008b7bb4",
      "incomplete_value": true,
      "site": "008b7bb4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b7b70",
      "incomplete_value": true,
      "site": "008b7b70",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "008b7bdc",
      "incomplete_value": true,
      "site": "008b7bdc",
      "value": [
        "LOAD",
        "8",
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
                "const:18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b7b98",
      "incomplete_value": true,
      "site": "008b7b98",
      "value": [
        "LOAD",
        "8",
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
                "const:18:8"
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
      "definition_site": "008b7bcc",
      "incomplete_value": true,
      "site": "008b7bdc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 6,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`008b7b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7aa0.md#insn-008b7b70) · [`008b7b98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7aa0.md#insn-008b7b98) · [`008b7bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7aa0.md#insn-008b7bc4)
- 新版 `008b7bb4`（命令位置の公開資料なし） · `008b7bdc`（命令位置の公開資料なし） · `008b7c08`（命令位置の公開資料なし）

~~~diff
- 008b7b70 ["COPY", "register:0:8", ["register:4040:8"]]
- 008b7b70 ["INT_ADD", "register:40f0:8", ["const:8b7b70:8", "const:4:8"]]
- 008b7b70 ["CALLIND", null, ["register:0:8"]]
+ 008b7bb4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008b7bb4 ["INT_ADD", "register:40f0:8", ["const:8b7bb4:8", "const:4:8"]]
+ 008b7bb4 ["CALLIND", null, ["register:0:8"]]
- 008b7b70 bytes 00013fd6
+ 008b7bb4 bytes 00013fd6
- 008b7b98 ["COPY", "register:0:8", ["register:4040:8"]]
- 008b7b98 ["INT_ADD", "register:40f0:8", ["const:8b7b98:8", "const:4:8"]]
- 008b7b98 ["CALLIND", null, ["register:0:8"]]
+ 008b7bdc ["COPY", "register:0:8", ["register:4040:8"]]
+ 008b7bdc ["INT_ADD", "register:40f0:8", ["const:8b7bdc:8", "const:4:8"]]
+ 008b7bdc ["CALLIND", null, ["register:0:8"]]
- 008b7b98 bytes 00013fd6
+ 008b7bdc bytes 00013fd6
- 008b7bc4 ["COPY", "register:0:8", ["register:4040:8"]]
- 008b7bc4 ["INT_ADD", "register:40f0:8", ["const:8b7bc4:8", "const:4:8"]]
- 008b7bc4 ["CALLIND", null, ["register:0:8"]]
+ 008b7c08 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008b7c08 ["INT_ADD", "register:40f0:8", ["const:8b7c08:8", "const:4:8"]]
+ 008b7c08 ["CALLIND", null, ["register:0:8"]]
- 008b7bc4 bytes 00013fd6
+ 008b7c08 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-630d5772eb474a582dc96a0af8a0356d"></a>

### [`008b909c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b909c.md) → [`008b90e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b90e0.md) FUN_008b90e0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.37% / 新版 97.37%

CFGの説明率　旧版 50.00% / 新版 46.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008b90dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008b9120"
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
      "unmatched:008b90dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008b9110"
      ]
    ]
  ],
  "added": [
    [
      "008b9120",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008b9110"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b90dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b909c.md#insn-008b90dc) · [`008b90b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b909c.md#insn-008b90b0)
- 新版 `008b9120`（命令位置の公開資料なし） · `008b90f4`（命令位置の公開資料なし）

~~~diff
- 008b90dc ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 008b90dc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 008b90dc bytes 94ffffb4
+ 008b9120 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
+ 008b9120 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 008b9120 bytes 94ffffb4
- 008b90b0 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 008b90b0 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
+ 008b90f4 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
+ 008b90f4 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 008b90b0 bytes b50300b4
+ 008b90f4 bytes b50300b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8573cf9356c021087a049edca96a23d2"></a>

### [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md) → [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) FUN_008b9178

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 343件 [`005d9c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9c54.md) [`005d9f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9f0c.md) [`005daf8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005da/005daf8c.md) [`005db034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005db034.md) [`005db7b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005db7b4.md) · 呼出先 2件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 343件 [`005d9c94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d9/005d9c94.md) [`005d9f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d9/005d9f4c.md) [`005dafcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005da/005dafcc.md) [`005db074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005db/005db074.md) [`005db7f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005db/005db7f4.md) · 呼出先 2件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 94.29% / 新版 94.29%

CFGの説明率　旧版 50.00% / 新版 37.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008b916c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008b91b0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "008b91a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008b916c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008b91ec"
      ]
    ]
  ],
  "added": [
    [
      "008b91b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008b91ec"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b916c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md#insn-008b916c) · [`008b91a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md#insn-008b91a4)
- 新版 `008b91b0`（命令位置の公開資料なし）

~~~diff
- 008b916c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 008b916c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 008b916c bytes e00100b4
- 008b91a4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 008b91a4 ["RETURN", null, ["register:0:8"]]
- 008b91a4 bytes c0035fd6
+ 008b91b0 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 008b91b0 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 008b91b0 bytes e00100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ecd59acf6494f574b2348580cb3bd8aa"></a>

### [`008b91c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b91c0.md) → [`008b9204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9204.md) FUN_008b9204

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`009ffe58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ff/009ffe58.md) [`00a02a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a02/00a02a4c.md) [`00a03828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a03/00a03828.md) [`00a03b68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a03/00a03b68.md) [`00a05644`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a05/00a05644.md) · 呼出先 2件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 5件 [`009ffff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ffff4.md) [`00a02be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a02be8.md) [`00a039c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a039c4.md) [`00a03d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03d04.md) [`00a057e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a05/00a057e0.md) · 呼出先 2件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 57.14% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008b91c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008b91c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008b91c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008b91c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:008b91c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:008b91dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "008b9208",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "008b920c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008b9220",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b91c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b91c0.md#insn-008b91c4) · [`008b91c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b91c0.md#insn-008b91c8) · [`008b91dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b91c0.md#insn-008b91dc)

~~~diff
- 008b91c4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 008b91c4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 008b91c4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 008b91c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008b91c4 bytes fd7b02a9
- 008b91c8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:30:8"]]
- 008b91c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 008b91c8 bytes f31b00f9
- 008b91dc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008b91dc ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 008b91dc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008b91dc bytes a8831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa8f08a901b0121a5b3a7fdb560fa07e"></a>

### [`008bc1fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008bc/008bc1fc.md) → [`008bc240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008bc/008bc240.md) FUN_008bc240

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008b9588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9588.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 1件 [`008b95cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b95cc.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 96.63% / 新版 96.63%

CFGの説明率　旧版 62.50% / 新版 58.82%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008bc238"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008bc27c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "008bc330"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008bc238",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008bc294"
      ]
    ],
    [
      "unmatched:008bc330",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "008bc27c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008bc294"
      ]
    ],
    [
      "008bc374",
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

- 旧版 [`008bc238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008bc/008bc1fc.md#insn-008bc238) · [`008bc330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008bc/008bc1fc.md#insn-008bc330)
- 新版 `008bc27c`（命令位置の公開資料なし）

~~~diff
- 008bc238 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 008bc238 bytes c0000054
+ 008bc27c ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
+ 008bc27c bytes c0000054
- 008bc330 ["COPY", "register:0:8", ["register:4040:8"]]
- 008bc330 ["INT_ADD", "register:40f0:8", ["const:8bc330:8", "const:4:8"]]
- 008bc330 ["CALLIND", null, ["register:0:8"]]
- 008bc330 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-edf8760376e33011a6ac0dd165f548cf"></a>

### [`008c0d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c0/008c0d3c.md) → [`008c0d80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c0/008c0d80.md) FUN_008c0d80

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008cb4a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cb/008cb4a8.md) · 呼出先 26件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467d74.md) [`00467e5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467e5c.md)
- 新版 呼出元 1件 [`008cb644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cb644.md) · 呼出先 26件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467db4.md) [`00467e9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467e9c.md)

変更の種類 call, call_argument_candidate, call_count, call_target, constant, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 98.46% / 新版 98.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `call_target` 6件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "008c0d88"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "008c0d94",
      "incomplete_value": false,
      "site": "008c0dac",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "leaf",
            "const:0:4"
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
    "new": null,
    "old": {
      "definition_site": "008c0d9c",
      "incomplete_value": false,
      "site": "008c0dac",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "leaf",
            "const:0:4"
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
      "unmatched:008c0d88",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "008c0e0c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "008c0f90",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ]
  ],
  "added": [
    [
      "008c0dcc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "008c0e0c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "008c0f90",
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

- 旧版 [`008c0d84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c0/008c0d3c.md#insn-008c0d84) · [`008c0d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c0/008c0d3c.md#insn-008c0d88) · [`008c0dac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c0/008c0d3c.md#insn-008c0dac)
- 新版 `008c0dc8`（命令位置の公開資料なし） · `008c0df0`（命令位置の公開資料なし）

~~~diff
- 008c0d84 ["INT_ADD", "register:40f0:8", ["const:8c0d84:8", "const:4:8"]]
- 008c0d84 ["CALL", null, ["callee:008514f8:8"]]
+ 008c0dc8 ["INT_ADD", "register:40f0:8", ["const:8c0dc8:8", "const:4:8"]]
+ 008c0dc8 ["CALL", null, ["callee:008514f8:8"]]
- 008c0d84 bytes cd41fe97
+ 008c0dc8 bytes cc41fe97
- 008c0d88 ["INT_ADD", "register:40f0:8", ["const:8c0d88:8", "const:4:8"]]
- 008c0d88 ["CALL", null, ["ram:46c984:8"]]
- 008c0d88 bytes ffaeee97
- 008c0dac ["INT_ADD", "register:40f0:8", ["const:8c0dac:8", "const:4:8"]]
- 008c0dac ["CALL", null, ["callee:00467b2c:8"]]
+ 008c0df0 ["INT_ADD", "register:40f0:8", ["const:8c0df0:8", "const:4:8"]]
+ 008c0df0 ["CALL", null, ["callee:00467b2c:8"]]
- 008c0dac bytes 509bee97
+ 008c0df0 bytes 4f9bee97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c92435f10844ec7c0d05cefd5c6a622f"></a>

### [`008c2990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c2/008c2990.md) → [`008c29d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c2/008c29d4.md) FUN_008c29d4

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`008c28e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c2/008c28e8.md) [`008c3818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c3/008c3818.md) [`008c506c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c5/008c506c.md) [`008caa24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ca/008caa24.md) · 呼出先 5件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`009df498`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009df/009df498.md) [`009e0e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e0/009e0e24.md) [`009e2df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e2/009e2df8.md) [`00b2f590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f590.md)
- 新版 呼出元 4件 [`008c292c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c2/008c292c.md) [`008c385c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c3/008c385c.md) [`008c5208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c5/008c5208.md) [`008cabc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ca/008cabc0.md) · 呼出先 5件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`009df634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009df634.md) [`009e0fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e0fc0.md) [`009e2f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e2/009e2f94.md) [`00b2f9b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2f/00b2f9b8.md)

変更の種類 constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 99.06% / 新版 99.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008c2ae4",
      "DATA",
      [
        "storage",
        "003b5258",
        null,
        "byte[67]"
      ]
    ]
  ],
  "added": [
    [
      "008c2b28",
      "DATA",
      [
        "storage",
        "003b5258",
        null,
        "uleb128"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c29d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c2/008c2990.md#insn-008c29d0) · [`008c29e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c2/008c2990.md#insn-008c29e0) · [`008c29e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c2/008c2990.md#insn-008c29e8)
- 新版 `008c2a14`（命令位置の公開資料なし） · `008c2a24`（命令位置の公開資料なし） · `008c2a2c`（命令位置の公開資料なし）

~~~diff
- 008c29d0 ["INT_ADD", "register:40f0:8", ["const:8c29d0:8", "const:4:8"]]
- 008c29d0 ["CALL", null, ["callee:008514f8:8"]]
+ 008c2a14 ["INT_ADD", "register:40f0:8", ["const:8c2a14:8", "const:4:8"]]
+ 008c2a14 ["CALL", null, ["callee:008514f8:8"]]
- 008c29d0 bytes ba3afe97
+ 008c2a14 bytes b93afe97
- 008c29e0 ["INT_ADD", "register:40f0:8", ["const:8c29e0:8", "const:4:8"]]
- 008c29e0 ["CALL", null, ["callee:009e0fc0:8"]]
+ 008c2a24 ["INT_ADD", "register:40f0:8", ["const:8c2a24:8", "const:4:8"]]
+ 008c2a24 ["CALL", null, ["callee:009e0fc0:8"]]
- 008c29e0 bytes 11790494
+ 008c2a24 bytes 67790494
- 008c29e8 ["INT_ADD", "register:40f0:8", ["const:8c29e8:8", "const:4:8"]]
- 008c29e8 ["CALL", null, ["callee:008514f8:8"]]
+ 008c2a2c ["INT_ADD", "register:40f0:8", ["const:8c2a2c:8", "const:4:8"]]
+ 008c2a2c ["CALL", null, ["callee:008514f8:8"]]
- 008c29e8 bytes b43afe97
+ 008c2a2c bytes b33afe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-722b176fb5da7c3145371d9267176700"></a>

### [`008c865c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c8/008c865c.md) → [`008c87f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c8/008c87f8.md) FUN_008c87f8

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008c5c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c5/008c5c08.md) · 呼出先 6件 [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`0085b264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085b264.md) [`0085b26c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085b26c.md) [`00ac8be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8be8.md)
- 新版 呼出元 1件 [`008c5da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c5/008c5da4.md) · 呼出先 6件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`0085b2a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b2a4.md) [`0085b2ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b2ac.md) [`00ac8de4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac8/00ac8de4.md)

変更の種類 call, call_count, constant, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 98.28% / 新版 98.28%

CFGの説明率　旧版 50.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "008c869c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "008c8838"
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
      "unmatched:008c869c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ]
  ],
  "added": [
    [
      "008c8838",
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

- 旧版 [`008c869c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c8/008c865c.md#insn-008c869c) · [`008c8698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c8/008c865c.md#insn-008c8698)
- 新版 `008c8838`（命令位置の公開資料なし） · `008c8834`（命令位置の公開資料なし）

~~~diff
- 008c869c ["INT_ADD", "register:40f0:8", ["const:8c869c:8", "const:4:8"]]
- 008c869c ["CALL", null, ["ram:46c984:8"]]
- 008c869c bytes ba90ee97
+ 008c8838 ["INT_ADD", "register:40f0:8", ["const:8c8838:8", "const:4:8"]]
+ 008c8838 ["CALL", null, ["ram:46c9c4:8"]]
+ 008c8838 bytes 6390ee97
- 008c8698 ["INT_ADD", "register:40f0:8", ["const:8c8698:8", "const:4:8"]]
- 008c8698 ["CALL", null, ["callee:008514f8:8"]]
+ 008c8834 ["INT_ADD", "register:40f0:8", ["const:8c8834:8", "const:4:8"]]
+ 008c8834 ["CALL", null, ["callee:008514f8:8"]]
- 008c8698 bytes 8823fe97
+ 008c8834 bytes 3123fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-719917a17d18dd6b1be31b6eab71b69b"></a>

### [`008c8744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c8/008c8744.md) → [`008c88e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c8/008c88e0.md) FUN_008c88e0

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008c5c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c5/008c5c08.md) · 呼出先 4件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`009df460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009df/009df460.md) [`009e0e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e0/009e0e24.md) [`009e2df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e2/009e2df8.md)
- 新版 呼出元 1件 [`008c5da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c5/008c5da4.md) · 呼出先 4件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`009df5fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009df5fc.md) [`009e0fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e0fc0.md) [`009e2f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e2/009e2f94.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 83.10% / 新版 83.10%

CFGの説明率　旧版 64.71% / 新版 57.89%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008c87b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008c8954"
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
      "unmatched:008c87b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008c89e4"
      ]
    ]
  ],
  "added": [
    [
      "008c8954",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008c89e4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c87b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c8/008c8744.md#insn-008c87b8) · [`008c8760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c8/008c8744.md#insn-008c8760)
- 新版 `008c8954`（命令位置の公開資料なし） · `008c88fc`（命令位置の公開資料なし）

~~~diff
- 008c87b8 ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
- 008c87b8 bytes 80040054
+ 008c8954 ["CBRANCH", null, ["local:b12:8", "register:101:1"]]
+ 008c8954 bytes 80040054
- 008c8760 ["INT_ADD", "register:40f0:8", ["const:8c8760:8", "const:4:8"]]
- 008c8760 ["CALL", null, ["callee:008514f8:8"]]
+ 008c88fc ["INT_ADD", "register:40f0:8", ["const:8c88fc:8", "const:4:8"]]
+ 008c88fc ["CALL", null, ["callee:008514f8:8"]]
- 008c8760 bytes 5623fe97
+ 008c88fc bytes ff22fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6fedab9a87219820e730ebc6870d25b2"></a>

### [`008ca9a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ca/008ca9a4.md) → [`008cab40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ca/008cab40.md) FUN_008cab40

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`007dd324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007dd/007dd324.md) · 呼出先 0件 
- 新版 呼出元 1件 [`007dd364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007dd/007dd364.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 29.63% / 新版 29.63%

CFGの説明率　旧版 5.00% / 新版 9.09%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 4件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ca9e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ca9ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008caa04"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008ca9c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:008ca9fc"
      ]
    ],
    [
      "unmatched:008ca9f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:008ca9dc"
      ]
    ],
    [
      "unmatched:008ca9f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008caba8"
      ]
    ]
  ],
  "added": [
    [
      "008cab5c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008cab98"
      ]
    ],
    [
      "008cab8c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008cab78"
      ]
    ],
    [
      "008cab94",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008caba8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ca9c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ca/008ca9a4.md#insn-008ca9c0) · [`008ca9e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ca/008ca9a4.md#insn-008ca9e8) · [`008ca9ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ca/008ca9a4.md#insn-008ca9ec)

~~~diff
- 008ca9c0 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 008ca9c0 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 008ca9c0 bytes e3010054
- 008ca9e8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 008ca9e8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 008ca9e8 ["INT_ADD", "tmp:2:8", ["register:4070:8", "const:65:8"]]
- 008ca9e8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 008ca9e8 bytes df950139
- 008ca9ec ["COPY", "tmp:0:4", ["const:0:4"]]
- 008ca9ec ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 008ca9ec ["INT_ADD", "tmp:2:8", ["register:4078:8", "const:65:8"]]
- 008ca9ec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 008ca9ec bytes ff950139
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81651c9595205a403ee0f4878063f502"></a>

### [`008cb774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cb/008cb774.md) → [`008cb910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cb910.md) FUN_008cb910

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "008cb77c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cb784"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008cb918"
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
      "unmatched:008cb77c",
      "DATA",
      [
        "storage",
        "00c83968",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008cb918",
      "DATA",
      [
        "storage",
        "00c83d68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cb77c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cb/008cb774.md#insn-008cb77c) · [`008cb784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cb/008cb774.md#insn-008cb784) · [`008cb788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cb/008cb774.md#insn-008cb788)

~~~diff
- 008cb77c ["COPY", "tmp:0:8", ["register:4008:8"]]
- 008cb77c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008cb77c bytes 280000f9
- 008cb784 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:8:8"]]
- 008cb784 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 008cb784 bytes 2080803c
- 008cb788 ["COPY", "register:0:8", ["register:40f0:8"]]
- 008cb788 ["RETURN", null, ["register:0:8"]]
- 008cb788 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-838904041a1e12b414848488dbb17869"></a>

### [`008cba6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cb/008cba6c.md) → [`008cbc08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cbc08.md) FUN_008cbc08

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "site": "008cba90"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cba90"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008cbc2c"
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
      "unmatched:008cba90",
      "DATA",
      [
        "storage",
        "00c839e8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008cba94",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:008cba98",
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
      "008cbc2c",
      "DATA",
      [
        "storage",
        "00c83de8",
        null,
        "undefined *"
      ]
    ],
    [
      "008cbc30",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008cbc34",
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

- 旧版 [`008cba90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cb/008cba6c.md#insn-008cba90) · [`008cba9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cb/008cba6c.md#insn-008cba9c)
- 新版 `008cbc2c`（命令位置の公開資料なし）

~~~diff
- 008cba90 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008cba90 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 008cba90 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 008cba90 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008cba90 bytes 082400a9
- 008cba9c ["COPY", "register:0:8", ["register:40f0:8"]]
- 008cba9c ["RETURN", null, ["register:0:8"]]
- 008cba9c bytes c0035fd6
+ 008cbc2c ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 008cbc2c ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 008cbc2c ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 008cbc2c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 008cbc2c bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1982fda06552575b5713725b58d27f5f"></a>

### [`008cbaa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cb/008cbaa0.md) → [`008cbc3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cbc3c.md) FUN_008cbc3c

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "008cbaac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cbaac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008cbc48"
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
      "unmatched:008cbaac",
      "DATA",
      [
        "storage",
        "00c839e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008cbc48",
      "DATA",
      [
        "storage",
        "00c83de8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cbaac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cb/008cbaa0.md#insn-008cbaac) · [`008cbab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cb/008cbaa0.md#insn-008cbab0)
- 新版 `008cbc48`（命令位置の公開資料なし）

~~~diff
- 008cbaac ["COPY", "tmp:0:8", ["register:4048:8"]]
- 008cbaac ["COPY", "tmp:1:8", ["register:4040:8"]]
- 008cbaac ["COPY", "tmp:2:8", ["register:4008:8"]]
- 008cbaac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008cbaac bytes 292000a9
- 008cbab0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 008cbab0 ["RETURN", null, ["register:0:8"]]
- 008cbab0 bytes c0035fd6
+ 008cbc48 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 008cbc48 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 008cbc48 ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 008cbc48 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 008cbc48 bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-671c926f90deb8f2c5c56163db93f3ac"></a>

### [`008cc210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cc/008cc210.md) → [`008cc3ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008cc3ac.md) FUN_008cc3ac

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 69.23% / 新版 69.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cc214"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cc234"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008cc234"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008cc214",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:008cc234",
      "DATA",
      [
        "storage",
        "00c83ae8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008cc3b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "008cc3d0",
      "DATA",
      [
        "storage",
        "00c83ee8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cc214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cc/008cc210.md#insn-008cc214) · [`008cc234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cc/008cc210.md#insn-008cc234)
- 新版 `008cc3b0`（命令位置の公開資料なし）

~~~diff
- 008cc214 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 008cc214 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 008cc214 bytes f30b00f9
- 008cc234 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008cc234 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 008cc234 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 008cc234 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 008cc234 bytes 082400a9
+ 008cc3b0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
+ 008cc3b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 008cc3b0 bytes f30b00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8c27cd6d7f0c482300bc0e45da04d1e"></a>

### [`008cc2ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cc/008cc2ec.md) → [`008cc488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cc/008cc488.md) FUN_008cc488

採用 · 移動量 `+0x19c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57aa0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

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
      "site": "008cc304"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008cc4a0"
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
      "unmatched:008cc304",
      "DATA",
      [
        "storage",
        "00c83b68",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008cc4a0",
      "DATA",
      [
        "storage",
        "00c83f68",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cc304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cc/008cc2ec.md#insn-008cc304) · [`008cc2fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cc/008cc2ec.md#insn-008cc2fc)
- 新版 `008cc4a0`（命令位置の公開資料なし）

~~~diff
- 008cc304 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 008cc304 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008cc304 bytes 080000f9
+ 008cc4a0 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 008cc4a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 008cc4a0 bytes 080000f9
- 008cc2fc ["COPY", "tmp:0:8", ["const:b68:8"]]
- 008cc2fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008cc2fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008cc2fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008cc2fc bytes 08a12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be557907850fd3bf462dd12b7ab21f35"></a>

### [`008cd818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cd/008cd818.md) → [`008cd9b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cd/008cd9b4.md) FUN_008cd9b4

採用 · 移動量 `+0x19c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`008cd330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cd/008cd330.md) [`008cd994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cd/008cd994.md) [`008cdd28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cd/008cdd28.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 3件 [`008cd4cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cd/008cd4cc.md) [`008cdb30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cd/008cdb30.md) [`008cdec4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cd/008cdec4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 90.53% / 新版 90.53%

CFGの説明率　旧版 14.29% / 新版 22.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008cd91c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008cdab8"
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
      "unmatched:008cd91c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008cdb0c"
      ]
    ]
  ],
  "added": [
    [
      "008cdab8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008cdb0c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cd91c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cd/008cd818.md#insn-008cd91c) · [`008cd844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cd/008cd818.md#insn-008cd844)
- 新版 `008cdab8`（命令位置の公開資料なし） · `008cd9e0`（命令位置の公開資料なし）

~~~diff
- 008cd91c ["CBRANCH", null, ["local:b21:8", "register:101:1"]]
- 008cd91c bytes a0020054
+ 008cdab8 ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
+ 008cdab8 bytes a0020054
- 008cd844 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 008cd844 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 008cd9e0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 008cd9e0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 008cd844 bytes c1000054
+ 008cd9e0 bytes c1000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

