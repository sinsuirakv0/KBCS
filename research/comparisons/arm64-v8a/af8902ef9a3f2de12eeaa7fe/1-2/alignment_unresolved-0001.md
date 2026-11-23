# v15.7.4 → v16.0.0 · 命令位置の検査未完了 (1)

[一覧の目次](README.md)

<a id="compare-12f335acd7a8625453e6d657dba973a8"></a>

### [`0046a3a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046a/0046a3a8.md) → [`0048d240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048d240.md) FUN_0048d240

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00829180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00829/00829180.md) · 呼出先 0件 
- 新版 呼出元 1件 [`0085b0f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085b0f8.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0048d24c",
      "READ",
      [
        "storage",
        "00c24dc8",
        null,
        "undefined4"
      ]
    ],
    [
      "0048d254",
      "READ",
      [
        "storage",
        "00c24db8",
        null,
        "undefined4"
      ]
    ],
    [
      "0048d260",
      "READ",
      [
        "storage",
        "00c24dcc",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0048d24c",
      "READ",
      [
        "storage",
        "00ca4888",
        null,
        "undefined4"
      ]
    ],
    [
      "0048d254",
      "READ",
      [
        "storage",
        "00ca4878",
        null,
        "undefined4"
      ]
    ],
    [
      "0048d260",
      "READ",
      [
        "storage",
        "00ca488c",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046a3a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046a/0046a3a8.md#insn-0046a3a8) · [`0046a3ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046a/0046a3a8.md#insn-0046a3ac) · [`0046a3b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046a/0046a3a8.md#insn-0046a3b8)
- 新版 [`0048d240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048d240.md#insn-0048d240) · [`0048d244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048d240.md#insn-0048d244)

~~~diff
- 0046a3a8 ["COPY", "register:4040:8", ["const:c24000:8"]]
+ 0048d240 ["COPY", "register:4040:8", ["const:ca4000:8"]]
- 0046a3a8 bytes c83d00d0
+ 0048d240 bytes a84000f0
- 0046a3ac ["COPY", "tmp:0:8", ["const:db0:8"]]
- 0046a3ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0046a3ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0046a3ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0048d244 ["COPY", "tmp:0:8", ["const:870:8"]]
+ 0048d244 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0048d244 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0048d244 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0046a3ac bytes 08c13691
+ 0048d244 bytes 08c12191
- 0046a3b8 ["INT_MULT", "tmp:0:4", ["register:4050:4", "register:4048:4"]]
- 0046a3b8 ["INT_ZEXT", "register:4048:8", ["tmp:0:4"]]
- 0046a3b8 bytes 497d091b
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e1318e30b249b816d5ea31c810c65f2"></a>

### [`00470c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/00470c54.md) → [`00493aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493aec.md) FUN_00493aec

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00906b9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00906/00906b9c.md) · 呼出先 3件 [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb7a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7a0.md) [`00bdb7b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7b0.md)
- 新版 呼出元 1件 [`0093b5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093b/0093b5d4.md) · 呼出先 3件 [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c581f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c581f0.md) [`00c58200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58200.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00493b88",
      "PARAM",
      [
        "storage",
        "0029f40a",
        null,
        null
      ]
    ],
    [
      "00493b90",
      "PARAM",
      [
        "storage",
        "00298c50",
        null,
        null
      ]
    ],
    [
      "00493b90",
      "PARAM",
      [
        "storage",
        "0029f407",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00493b88",
      "PARAM",
      [
        "storage",
        "002af81d",
        null,
        null
      ]
    ],
    [
      "00493b90",
      "PARAM",
      [
        "storage",
        "002a8a0e",
        null,
        null
      ]
    ],
    [
      "00493b90",
      "PARAM",
      [
        "storage",
        "002af81a",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00470ca4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/00470c54.md#insn-00470ca4) · [`00470cc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/00470c54.md#insn-00470cc4) · [`00470cc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/00470c54.md#insn-00470cc8)
- 新版 [`00493b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493aec.md#insn-00493b3c) · [`00493b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493aec.md#insn-00493b5c) · [`00493b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493aec.md#insn-00493b60)

~~~diff
- 00470ca4 ["INT_ADD", "register:40f0:8", ["const:470ca4:8", "const:4:8"]]
- 00470ca4 ["CALL", null, ["callee:00c581f0:8"]]
+ 00493b3c ["INT_ADD", "register:40f0:8", ["const:493b3c:8", "const:4:8"]]
+ 00493b3c ["CALL", null, ["callee:00c581f0:8"]]
- 00470ca4 bytes bfaa1d94
+ 00493b3c bytes ad111f94
- 00470cc4 ["COPY", "register:40b0:8", ["const:29f000:8"]]
+ 00493b5c ["COPY", "register:40b0:8", ["const:2af000:8"]]
- 00470cc4 bytes 76f1fff0
+ 00493b5c bytes f6f0ff90
- 00470cc8 ["COPY", "tmp:0:8", ["const:407:8"]]
- 00470cc8 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
- 00470cc8 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
- 00470cc8 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
+ 00493b60 ["COPY", "tmp:0:8", ["const:81a:8"]]
+ 00493b60 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
+ 00493b60 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
+ 00493b60 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
- 00470cc8 bytes d61e1091
+ 00493b60 bytes d66a2091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de895c10a077f7f178de845b894f0477"></a>

### [`00492270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00492/00492270.md) → [`004b5108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5108.md) _ZN5Botan10hex_encodeEPKhmb

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdbd50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbd50.md) · 呼出先 3件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)
- 新版 呼出元 1件 [`00c587a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c587a0.md) · 呼出先 3件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004b51e4",
      "DATA",
      [
        "storage",
        "002b19e0",
        null,
        "string"
      ]
    ],
    [
      "004b51e4",
      "DATA",
      [
        "storage",
        "002b0bc0",
        null,
        null
      ]
    ],
    [
      "004b51ec",
      "DATA",
      [
        "storage",
        "002b19e0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004b51e4",
      "DATA",
      [
        "storage",
        "002c3090",
        null,
        "string"
      ]
    ],
    [
      "004b51e4",
      "DATA",
      [
        "storage",
        "002c21b0",
        null,
        null
      ]
    ],
    [
      "004b51ec",
      "DATA",
      [
        "storage",
        "002c3090",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004922e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00492/00492270.md#insn-004922e4) · [`00492304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00492/00492270.md#insn-00492304) · [`00492318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00492/00492270.md#insn-00492318)
- 新版 [`004b517c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5108.md#insn-004b517c) · [`004b519c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5108.md#insn-004b519c) · [`004b51b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5108.md#insn-004b51b0)

~~~diff
- 004922e4 ["INT_ADD", "register:40f0:8", ["const:4922e4:8", "const:4:8"]]
- 004922e4 ["CALL", null, ["callee:00c57a90:8"]]
+ 004b517c ["INT_ADD", "register:40f0:8", ["const:4b517c:8", "const:4:8"]]
+ 004b517c ["CALL", null, ["callee:00c57a90:8"]]
- 004922e4 bytes 57231d94
+ 004b517c bytes 458a1e94
- 00492304 ["INT_ADD", "register:40f0:8", ["const:492304:8", "const:4:8"]]
- 00492304 ["CALL", null, ["callee:00c57c90:8"]]
+ 004b519c ["INT_ADD", "register:40f0:8", ["const:4b519c:8", "const:4:8"]]
+ 004b519c ["CALL", null, ["callee:00c57c90:8"]]
- 00492304 bytes cf231d94
+ 004b519c bytes bd8a1e94
- 00492318 ["COPY", "register:4050:8", ["const:2b0000:8"]]
+ 004b51b0 ["COPY", "register:4050:8", ["const:2c2000:8"]]
- 00492318 bytes eaf0ffd0
+ 004b51b0 bytes 6af0ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d97d73d29c5581f8653236de6ad00c24"></a>

### [`004937b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00493/004937b8.md) → [`004b6650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b6/004b6650.md) _ZN5Botan10hex_encodeEPcPKhmb

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

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
      "004b6680",
      "DATA",
      [
        "storage",
        "002b19e0",
        null,
        "string"
      ]
    ],
    [
      "004b6680",
      "DATA",
      [
        "storage",
        "002b0bc0",
        null,
        null
      ]
    ],
    [
      "004b6688",
      "DATA",
      [
        "storage",
        "002b19e0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004b6680",
      "DATA",
      [
        "storage",
        "002c3090",
        null,
        "string"
      ]
    ],
    [
      "004b6680",
      "DATA",
      [
        "storage",
        "002c21b0",
        null,
        null
      ]
    ],
    [
      "004b6688",
      "DATA",
      [
        "storage",
        "002c3090",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004937b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00493/004937b8.md#insn-004937b8) · [`004937bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00493/004937b8.md#insn-004937bc) · [`004937c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00493/004937b8.md#insn-004937c4)
- 新版 [`004b6654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b6/004b6650.md#insn-004b6654)

~~~diff
- 004937b8 ["COPY", "register:4040:8", ["const:2b1000:8"]]
- 004937b8 bytes e8f0ffd0
- 004937bc ["COPY", "tmp:0:8", ["const:9e0:8"]]
- 004937bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004937bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004937bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004b6654 ["COPY", "tmp:0:8", ["const:90:8"]]
+ 004b6654 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004b6654 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004b6654 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004937bc bytes 08812791
+ 004b6654 bytes 08410291
- 004937c4 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 004937c4 bytes e9f0ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af9a29e5f036d8f4fed401a66fbe7e98"></a>

### [`004acf8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ac/004acf8c.md) → [`004cfe24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cfe24.md) _ZNK5Botan13PKCS7_Padding5unpadEPKhm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

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
      "004cfe8c",
      "READ",
      [
        "storage",
        "002b0d40",
        null,
        null
      ]
    ],
    [
      "004cfe90",
      "READ",
      [
        "storage",
        "002b0b60",
        null,
        null
      ]
    ],
    [
      "004cfe94",
      "READ",
      [
        "storage",
        "002b14e0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004cfe8c",
      "READ",
      [
        "storage",
        "002c2340",
        null,
        null
      ]
    ],
    [
      "004cfe90",
      "READ",
      [
        "storage",
        "002c2150",
        null,
        null
      ]
    ],
    [
      "004cfe94",
      "READ",
      [
        "storage",
        "002c2b30",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004acfd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ac/004acf8c.md#insn-004acfd0) · [`004acfd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ac/004acf8c.md#insn-004acfd4) · [`004acfd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ac/004acf8c.md#insn-004acfd8)
- 新版 [`004cfe68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cfe24.md#insn-004cfe68) · [`004cfe6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cfe24.md#insn-004cfe6c) · [`004cfe70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cfe24.md#insn-004cfe70)

~~~diff
- 004acfd0 ["COPY", "register:4070:8", ["const:2b0000:8"]]
+ 004cfe68 ["COPY", "register:4070:8", ["const:2c2000:8"]]
- 004acfd0 bytes 2ef0ff90
+ 004cfe68 bytes 8eeffff0
- 004acfd4 ["COPY", "register:4068:8", ["const:2b0000:8"]]
+ 004cfe6c ["COPY", "register:4068:8", ["const:2c2000:8"]]
- 004acfd4 bytes 2df0ff90
+ 004cfe6c bytes 8deffff0
- 004acfd8 ["COPY", "register:4058:8", ["const:2b1000:8"]]
+ 004cfe70 ["COPY", "register:4058:8", ["const:2c2000:8"]]
- 004acfd8 bytes 2bf0ffb0
+ 004cfe70 bytes 8beffff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4bada521c09c700dc03983189c3d456c"></a>

### [`004ad480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ad/004ad480.md) → [`004d0318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d0318.md) _ZNK5Botan17ANSI_X923_Padding5unpadEPKhm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

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
      "004d037c",
      "READ",
      [
        "storage",
        "002b0d40",
        null,
        null
      ]
    ],
    [
      "004d0380",
      "READ",
      [
        "storage",
        "002b0b60",
        null,
        null
      ]
    ],
    [
      "004d0384",
      "READ",
      [
        "storage",
        "002b14e0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004d037c",
      "READ",
      [
        "storage",
        "002c2340",
        null,
        null
      ]
    ],
    [
      "004d0380",
      "READ",
      [
        "storage",
        "002c2150",
        null,
        null
      ]
    ],
    [
      "004d0384",
      "READ",
      [
        "storage",
        "002c2b30",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ad4c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ad/004ad480.md#insn-004ad4c0) · [`004ad4c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ad/004ad480.md#insn-004ad4c4) · [`004ad4c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ad/004ad480.md#insn-004ad4c8)
- 新版 [`004d0358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d0318.md#insn-004d0358) · [`004d035c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d0318.md#insn-004d035c) · [`004d0360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d0318.md#insn-004d0360)

~~~diff
- 004ad4c0 ["COPY", "register:4068:8", ["const:2b0000:8"]]
+ 004d0358 ["COPY", "register:4068:8", ["const:2c2000:8"]]
- 004ad4c0 bytes 0df0fff0
+ 004d0358 bytes 8defffd0
- 004ad4c4 ["COPY", "register:4050:8", ["const:2b0000:8"]]
+ 004d035c ["COPY", "register:4050:8", ["const:2c2000:8"]]
- 004ad4c4 bytes 0af0fff0
+ 004d035c bytes 8aefffd0
- 004ad4c8 ["COPY", "register:4058:8", ["const:2b1000:8"]]
+ 004d0360 ["COPY", "register:4058:8", ["const:2c2000:8"]]
- 004ad4c8 bytes 2bf0ff90
+ 004d0360 bytes 8befffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-268166946c10b40adcb9d9fd69da89c7"></a>

### [`004ada88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ad/004ada88.md) → [`004d0920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d0920.md) _ZNK5Botan11ESP_Padding5unpadEPKhm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

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
      "004d0988",
      "READ",
      [
        "storage",
        "002b0d40",
        null,
        null
      ]
    ],
    [
      "004d098c",
      "READ",
      [
        "storage",
        "002b0b60",
        null,
        null
      ]
    ],
    [
      "004d0990",
      "READ",
      [
        "storage",
        "002b14e0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004d0988",
      "READ",
      [
        "storage",
        "002c2340",
        null,
        null
      ]
    ],
    [
      "004d098c",
      "READ",
      [
        "storage",
        "002c2150",
        null,
        null
      ]
    ],
    [
      "004d0990",
      "READ",
      [
        "storage",
        "002c2b30",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004adacc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ad/004ada88.md#insn-004adacc) · [`004adad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ad/004ada88.md#insn-004adad0) · [`004adad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ad/004ada88.md#insn-004adad4)
- 新版 [`004d0964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d0920.md#insn-004d0964) · [`004d0968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d0920.md#insn-004d0968) · [`004d096c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d0920.md#insn-004d096c)

~~~diff
- 004adacc ["COPY", "register:4068:8", ["const:2b0000:8"]]
+ 004d0964 ["COPY", "register:4068:8", ["const:2c2000:8"]]
- 004adacc bytes 0df0fff0
+ 004d0964 bytes 8defffd0
- 004adad0 ["COPY", "register:4050:8", ["const:2b0000:8"]]
+ 004d0968 ["COPY", "register:4050:8", ["const:2c2000:8"]]
- 004adad0 bytes 0af0fff0
+ 004d0968 bytes 8aefffd0
- 004adad4 ["COPY", "register:4058:8", ["const:2b1000:8"]]
+ 004d096c ["COPY", "register:4058:8", ["const:2c2000:8"]]
- 004adad4 bytes 2bf0ff90
+ 004d096c bytes 8befffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7179c2da7a521a407ae68c6e0d77d572"></a>

### [`004dbc58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004db/004dbc58.md) → [`004feaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fe/004feaf0.md) _ZN5Botan14version_stringEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "site": "004dbc8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "004dbc90"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "004dbc90"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004feb14",
      "READ",
      [
        "storage",
        "002ab6ab",
        null,
        "string"
      ]
    ],
    [
      "004feb14",
      "READ",
      [
        "storage",
        "002ab6bb",
        null,
        "string"
      ]
    ],
    [
      "004feb18",
      "READ",
      [
        "storage",
        "002b1420",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004feb14",
      "READ",
      [
        "storage",
        "002bc5ce",
        null,
        "string"
      ]
    ],
    [
      "004feb14",
      "READ",
      [
        "storage",
        "002bc5de",
        null,
        "string"
      ]
    ],
    [
      "004feb18",
      "READ",
      [
        "storage",
        "002c2a70",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004dbc8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004db/004dbc58.md#insn-004dbc8c) · [`004dbc90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004db/004dbc58.md#insn-004dbc90) · [`004dbc98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004db/004dbc58.md#insn-004dbc98)

~~~diff
- 004dbc8c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 004dbc8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5040:16"]]
- 004dbc8c bytes 6202803d
- 004dbc90 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:40:8"]]
- 004dbc90 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 004dbc90 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 004dbc90 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5020:16"]]
- 004dbc90 bytes 000402ad
- 004dbc98 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:60:8"]]
- 004dbc98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 004dbc98 bytes 0018803d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1aaeab1825aa7f6ad804ceb7653860ca"></a>

### [`00518c98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/00518c98.md) → [`0053bb30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053bb30.md) FUN_0053bb30

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`004e1eb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e1/004e1eb8.md) [`004f6b24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f6/004f6b24.md) [`004f6c0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f6/004f6c0c.md) [`004fdfd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fd/004fdfd8.md) [`005188a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/005188a4.md) · 呼出先 4件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00518dd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/00518dd8.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 5件 [`00504d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00504/00504d50.md) [`005199bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00519/005199bc.md) [`00519aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00519/00519aa4.md) [`00520e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00520/00520e70.md) [`0053b73c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053b73c.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0053bc70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053bc70.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 91.25% / 新版 91.25%

CFGの説明率　旧版 38.10% / 新版 47.06%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00518cc0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0053bb58"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00518d4c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00518cc0",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:00518d4c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0053bb94"
      ]
    ],
    [
      "unmatched:00518d58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0053bb9c"
      ]
    ]
  ],
  "added": [
    [
      "0053bb58",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "0053bbe4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0053bb94"
      ]
    ],
    [
      "0053bbf0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0053bb9c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00518cc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/00518c98.md#insn-00518cc0) · [`00518d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/00518c98.md#insn-00518d4c) · [`00518d58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/00518c98.md#insn-00518d58)

~~~diff
- 00518cc0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00518cc0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00518cc0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00518cc0 bytes a8831ff8
- 00518d4c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00518d4c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00518d4c bytes 81fdff54
- 00518d58 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00518d58 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00518d58 bytes 68fdffb5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-935ab995aba41344af988f204d7d65f5"></a>

### [`00518ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/00518ea0.md) → [`0053bd38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053bd38.md) FUN_0053bd38

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`004e7c0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e7/004e7c0c.md) [`004eb16c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004eb/004eb16c.md) [`004efe30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ef/004efe30.md) [`004fbbe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fb/004fbbe8.md) [`004fdfd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fd/004fdfd8.md) · 呼出先 7件 [`005180b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/005180b8.md) [`0051915c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00519/0051915c.md) [`005192a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00519/005192a0.md) [`005193d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00519/005193d0.md) [`00525f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525f90.md)
- 新版 呼出元 5件 [`0050aaa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050a/0050aaa4.md) [`0050e004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0050e/0050e004.md) [`00512cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00512/00512cc8.md) [`0051ea80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051e/0051ea80.md) [`00520e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00520/00520e70.md) · 呼出先 7件 [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`0053bff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053bff4.md) [`0053c138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053c138.md) [`0053c268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053c268.md) [`00548e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548e28.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 83.73% / 新版 83.73%

CFGの説明率　旧版 52.94% / 新版 51.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 11件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00518f08"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00518f24"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00518fec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00518f08",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00518f0c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0053bddc"
      ]
    ],
    [
      "unmatched:00518f14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0053be08"
      ]
    ]
  ],
  "added": [
    [
      "0053bda0",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "0053bda4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0053bddc"
      ]
    ],
    [
      "0053bdac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0053be08"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00518f04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/00518ea0.md#insn-00518f04) · [`00518f08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/00518ea0.md#insn-00518f08) · [`00518f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/00518ea0.md#insn-00518f0c)

~~~diff
- 00518f04 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00518f04 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00518f04 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00518f04 ["COPY", "register:40a8:8", ["tmp:0:8"]]
- 00518f04 bytes 5501889a
- 00518f08 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00518f08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00518f08 bytes f50b00f9
- 00518f0c ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 00518f0c ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00518f0c bytes d50100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-108ab8b77cfe4cb3a9b812a0c492e08c"></a>

### [`0051915c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00519/0051915c.md) → [`0053bff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053bff4.md) FUN_0053bff4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00518ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/00518ea0.md) · 呼出先 1件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md)
- 新版 呼出元 1件 [`0053bd38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053bd38.md) · 呼出先 1件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 98.31% / 新版 98.31%

CFGの説明率　旧版 84.00% / 新版 80.77%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005191d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0053c070"
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
      "unmatched:005191d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0053c028"
      ]
    ]
  ],
  "added": [
    [
      "0053c070",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0053c028"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005191d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00519/0051915c.md#insn-005191d8) · [`00519178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00519/0051915c.md#insn-00519178)
- 新版 [`0053c070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053bff4.md#insn-0053c070) · [`0053c010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053bff4.md#insn-0053c010)

~~~diff
- 005191d8 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 005191d8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 005191d8 bytes c3fdff54
+ 0053c070 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 0053c070 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 0053c070 bytes c3fdff54
- 00519178 ["INT_EQUAL", "tmp:0:1", ["register:4068:8", "const:0:8"]]
- 00519178 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
+ 0053c010 ["INT_EQUAL", "tmp:0:1", ["register:4068:8", "const:0:8"]]
+ 0053c010 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 00519178 bytes 2d0400b4
+ 0053c010 bytes 2d0400b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a9de1a0b986d2ffc9130241d506285d"></a>

### [`005199dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00519/005199dc.md) → [`0053c874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053c874.md) FUN_0053c874

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 82.86% / 新版 82.86%

CFGの説明率　旧版 55.56% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005199dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005199dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005199e0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005199dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:005199e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005199f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0053c8f4"
      ]
    ]
  ],
  "added": [
    [
      "0053c874",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0053c878",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0053c888",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0053c8f4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005199dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00519/005199dc.md#insn-005199dc) · [`005199e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00519/005199dc.md#insn-005199e0) · [`005199ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00519/005199dc.md#insn-005199ec)

~~~diff
- 005199dc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005199dc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005199dc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 005199dc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005199dc bytes fd7bbea9
- 005199e0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 005199e0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 005199e0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 005199e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005199e0 bytes f44f01a9
- 005199ec ["COPY", "tmp:0:8", ["register:4000:8"]]
- 005199ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:8"]]
- 005199ec bytes 010000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d7643ed226365774f67cdcb1fcb72a6"></a>

### [`00519a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00519/00519a68.md) → [`0053c900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053c900.md) FUN_0053c900

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 6件 [`004ede80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ed/004ede80.md) [`0050e774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e774.md) [`0050e944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050e/0050e944.md) [`0050fae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050f/0050fae8.md) [`0051cc00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051cc00.md) · 呼出先 2件 [`00517bcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00517/00517bcc.md) [`00519bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00519/00519bb0.md)
- 新版 呼出元 6件 [`00510d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00510/00510d18.md) [`0053160c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/0053160c.md) [`005317dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00531/005317dc.md) [`00532980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00532/00532980.md) [`0053fa98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053fa98.md) · 呼出先 2件 [`0053aa64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053aa64.md) [`0053ca48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053ca48.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 64.79% / 新版 64.79%

CFGの説明率　旧版 7.41% / 新版 8.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 5件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00519ab0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0053c948"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00519ad4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00519a98",
      "READ",
      [
        "storage",
        "00c1b2d8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00519ab0",
      "DATA",
      [
        "storage",
        "00bea7a8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "unmatched:00519ad4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0053c9dc"
      ]
    ]
  ],
  "added": [
    [
      "0053c930",
      "READ",
      [
        "storage",
        "00c9acc8",
        null,
        "pointer"
      ]
    ],
    [
      "0053c948",
      "DATA",
      [
        "storage",
        "00c67368",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0053c96c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0053c9dc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00519ab0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00519/00519a68.md#insn-00519ab0) · [`00519ad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00519/00519a68.md#insn-00519ad4) · [`00519af4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00519/00519a68.md#insn-00519af4)

~~~diff
- 00519ab0 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00519ab0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00519ab0 bytes 080000f9
- 00519ad4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00519ad4 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 00519ad4 bytes 81030054
- 00519af4 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00519af4 bytes 20feff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e32a2c65a9ec447be5419c6500b15539"></a>

### [`00519c84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00519/00519c84.md) → [`0053cb1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053cb1c.md) FUN_0053cb1c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00519bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00519/00519bb0.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`0053ca48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053ca48.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 63.12% / 新版 63.12%

CFGの説明率　旧版 30.23% / 新版 27.08%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 17件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00519c84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00519c84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00519c88"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00519c84",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00519c88",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00519c8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0053cb1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "0053cb20",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "0053cb24",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00519c84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00519/00519c84.md#insn-00519c84) · [`00519c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00519/00519c84.md#insn-00519c88) · [`00519c8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00519/00519c84.md#insn-00519c8c)

~~~diff
- 00519c84 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00519c84 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00519c84 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00519c84 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00519c84 bytes fd7bbba9
- 00519c88 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00519c88 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00519c88 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00519c88 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00519c88 bytes fa6701a9
- 00519c8c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00519c8c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00519c8c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00519c8c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00519c8c bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aef599eecc63899e1a45bf92bb988572"></a>

### [`0051a4c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051a/0051a4c0.md) → [`0053d358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053d358.md) FUN_0053d358

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`004eef84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ee/004eef84.md) [`0051a320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051a/0051a320.md) [`00527c8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/00527c8c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 3件 [`00511e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/00511e1c.md) [`0053d1b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053d1b8.md) [`0054ab24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054ab24.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0051a4c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0051a4c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0053d358"
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
      "unmatched:0051a4c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0051a4cc",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:0051a4d0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "0053d358",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0053d364",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "0053d368",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0043b738"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051a4c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051a/0051a4c0.md#insn-0051a4c0) · [`0051a4d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051a/0051a4c0.md#insn-0051a4d0)
- 新版 [`0053d358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053d358.md#insn-0053d358)

~~~diff
- 0051a4c0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0051a4c0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0051a4c0 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 0051a4c0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0051a4c0 bytes fd7bbfa9
- 0051a4d0 ["INT_ADD", "register:40f0:8", ["const:51a4d0:8", "const:4:8"]]
- 0051a4d0 ["CALL", null, ["ram:418c38:8"]]
- 0051a4d0 bytes daf9fb97
+ 0053d358 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 0053d358 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 0053d358 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 0053d358 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 0053d358 bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18aaecd89c9a25a667825c66ee2444a4"></a>

### [`0051a4d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051a/0051a4d4.md) → [`0053d36c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053d36c.md) FUN_0053d36c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`004f2228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f2/004f2228.md) · 呼出先 0件 
- 新版 呼出元 1件 [`005150c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/005150c0.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 86.61% / 新版 86.61%

CFGの説明率　旧版 32.00% / 新版 29.63%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 8件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0051a4fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0051a53c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0051a554"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0051a4fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0053d520"
      ]
    ],
    [
      "unmatched:0051a53c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0053d38c"
      ]
    ],
    [
      "unmatched:0051a554",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0053d400"
      ]
    ]
  ],
  "added": [
    [
      "0053d394",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0053d520"
      ]
    ],
    [
      "0053d3d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0053d38c"
      ]
    ],
    [
      "0053d3ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0053d400"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051a4fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051a/0051a4d4.md#insn-0051a4fc) · [`0051a53c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051a/0051a4d4.md#insn-0051a53c) · [`0051a554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051a/0051a4d4.md#insn-0051a554)

~~~diff
- 0051a4fc ["INT_EQUAL", "tmp:0:1", ["register:4068:8", "const:0:8"]]
- 0051a4fc ["CBRANCH", null, ["local:b43:8", "tmp:0:1"]]
- 0051a4fc bytes 6d0c00b4
- 0051a53c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 0051a53c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 0051a53c bytes c3fdff54
- 0051a554 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 0051a554 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 0051a554 ["CBRANCH", null, ["local:b13:8", "tmp:1:1"]]
- 0051a554 bytes a9000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91399fdb0922be1957465fd4c0e208d4"></a>

### [`0051a850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051a/0051a850.md) → [`0053d6e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053d6e8.md) FUN_0053d6e8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`004e01ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e01ec.md) [`004ee4f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ee/004ee4f4.md) · 呼出先 0件 
- 新版 呼出元 2件 [`00503084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/00503084.md) [`0051138c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/0051138c.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0051a854"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0053d6ec"
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
      "unmatched:0051a854",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0053d6fc"
      ]
    ]
  ],
  "added": [
    [
      "0053d6ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0053d6fc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051a854`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051a/0051a850.md#insn-0051a854) · [`0051a850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051a/0051a850.md#insn-0051a850)
- 新版 [`0053d6ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053d6e8.md#insn-0053d6ec)

~~~diff
- 0051a854 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 0051a854 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 0051a854 bytes 800000b4
+ 0053d6ec ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 0053d6ec ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 0053d6ec bytes 800000b4
- 0051a850 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:18:8"]]
- 0051a850 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0051a850 bytes 000c40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1dd985262de1949030d966c999b926c"></a>

### [`0051a920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051a/0051a920.md) → [`0053d7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053d7b8.md) FUN_0053d7b8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`004f7afc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f7/004f7afc.md) [`0051bb34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051b/0051bb34.md) [`0051ca38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051ca38.md) [`005299a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/005299a4.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 4件 [`0051a994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051a994.md) [`0053e9cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053e/0053e9cc.md) [`0053f8d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f8d0.md) [`0054c83c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c83c.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

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
      "site": "0051a920"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0051a920"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0053d7b8"
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
      "unmatched:0051a920",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0051a92c",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:0051a930",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "0053d7b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0053d7c4",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "0053d7c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0043b738"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051a920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051a/0051a920.md#insn-0051a920) · [`0051a930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051a/0051a920.md#insn-0051a930)
- 新版 [`0053d7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053d7b8.md#insn-0053d7b8)

~~~diff
- 0051a920 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0051a920 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0051a920 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 0051a920 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0051a920 bytes fd7bbfa9
- 0051a930 ["INT_ADD", "register:40f0:8", ["const:51a930:8", "const:4:8"]]
- 0051a930 ["CALL", null, ["ram:418c38:8"]]
- 0051a930 bytes c2f8fb97
+ 0053d7b8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 0053d7b8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 0053d7b8 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 0053d7b8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 0053d7b8 bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-570c4a741e9fcbef832771767d81bed8"></a>

### [`0051a934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051a/0051a934.md) → [`0053d7cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053d7cc.md) FUN_0053d7cc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`004f7afc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f7/004f7afc.md) [`0051bb34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051b/0051bb34.md) [`0051ca38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051ca38.md) · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 3件 [`0051a994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051a994.md) [`0053e9cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053e/0053e9cc.md) [`0053f8d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f8d0.md) · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 87.14% / 新版 87.14%

CFGの説明率　旧版 13.64% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0051a95c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0051a9ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0053d7f4"
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
      "unmatched:0051a95c",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:0051a988",
      "READ",
      [
        "storage",
        "00c1b360",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:0051a98c",
      "READ",
      [
        "storage",
        "00c1b338",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0053d7f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "0053d820",
      "READ",
      [
        "storage",
        "00c9ad50",
        null,
        "pointer"
      ]
    ],
    [
      "0053d824",
      "READ",
      [
        "storage",
        "00c9ad28",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051a95c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051a/0051a934.md#insn-0051a95c) · [`0051a9cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051a/0051a934.md#insn-0051a9cc) · [`0051a9ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051a/0051a934.md#insn-0051a9ec)

~~~diff
- 0051a95c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0051a95c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0051a95c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0051a95c bytes a8831ff8
- 0051a9cc ["CBRANCH", null, ["local:b16:8", "register:101:1"]]
- 0051a9cc bytes 80020054
- 0051a9ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
- 0051a9ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 0051a9ec bytes 6002813c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5bd8732f0aae6dd6d53bef2727fb85c3"></a>

### [`0051aa88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051a/0051aa88.md) → [`0053d920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053d920.md) FUN_0053d920

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 46.15% / 新版 46.15%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0051aa98"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0051aa98"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0053d930"
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
      "unmatched:0051aa98",
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
      "0053d930",
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

- 旧版 [`0051aa98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051a/0051aa88.md#insn-0051aa98) · [`0051aa9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051a/0051aa88.md#insn-0051aa9c)
- 新版 [`0053d930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053d920.md#insn-0053d930)

~~~diff
- 0051aa98 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0051aa98 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0051aa98 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0051aa98 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0051aa98 bytes f44f01a9
+ 0053d930 ["COPY", "tmp:0:8", ["register:40a0:8"]]
+ 0053d930 ["COPY", "tmp:1:8", ["register:4098:8"]]
+ 0053d930 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
+ 0053d930 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 0053d930 bytes f44f01a9
- 0051aa9c ["COPY", "register:40e8:8", ["register:8:8"]]
- 0051aa9c bytes fd030091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-416de067b4f27df3a075a004cd6704d1"></a>

### [`0051ac38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051a/0051ac38.md) → [`0053dad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053dad0.md) FUN_0053dad0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 50.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0051ac3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051a/0051ac38.md#insn-0051ac3c) · [`0051ac48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051a/0051ac38.md#insn-0051ac48) · [`0051ac58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051a/0051ac38.md#insn-0051ac58)
- 新版 [`0053dad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053dad0.md#insn-0053dad4) · [`0053daf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053d/0053dad0.md#insn-0053daf0)

~~~diff
- 0051ac3c ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 0051ac3c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 0053dad4 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 0053dad4 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 0051ac3c bytes 680100b4
+ 0053dad4 bytes 680100b4
- 0051ac48 ["COPY", "register:40e8:8", ["register:8:8"]]
- 0051ac48 bytes fd030091
- 0051ac58 ["INT_ADD", "register:40f0:8", ["const:51ac58:8", "const:4:8"]]
- 0051ac58 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0053daf0 ["INT_ADD", "register:40f0:8", ["const:53daf0:8", "const:4:8"]]
+ 0053daf0 ["CALL", null, ["callee:00c57ab0:8"]]
- 0051ac58 bytes 02011b94
+ 0053daf0 bytes f0671c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a577357d2860b1d86ad89d06b92e1bb3"></a>

### [`0051c9e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051c9e8.md) → [`0053f880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f880.md) FUN_0053f880

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`0051c938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051c938.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0053f7d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f7d0.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 57.14% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "0051ca34"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "0053f8cc"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`0051ca34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051c9e8.md#insn-0051ca34) · [`0051ca20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051c9e8.md#insn-0051ca20)
- 新版 [`0053f8cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f880.md#insn-0053f8cc) · [`0053f8b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053f880.md#insn-0053f8b8)

~~~diff
- 0051ca34 ["COPY", "register:0:8", ["register:40f0:8"]]
- 0051ca34 ["RETURN", null, ["register:0:8"]]
- 0051ca34 bytes c0035fd6
+ 0053f8cc ["COPY", "register:0:8", ["register:40f0:8"]]
+ 0053f8cc ["RETURN", null, ["register:0:8"]]
+ 0053f8cc bytes c0035fd6
- 0051ca20 ["INT_ADD", "register:40f0:8", ["const:51ca20:8", "const:4:8"]]
- 0051ca20 ["CALL", null, ["callee:0053f7d0:8"]]
+ 0053f8b8 ["INT_ADD", "register:40f0:8", ["const:53f8b8:8", "const:4:8"]]
+ 0053f8b8 ["CALL", null, ["callee:0053f7d0:8"]]
- 0051ca20 bytes c6ffff97
+ 0053f8b8 bytes c6ffff97
~~~


<a id="compare-f769ffb5259bf4c0e63b98488ae41f95"></a>

### [`0051cddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051cddc.md) → [`0053fc74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053fc74.md) FUN_0053fc74

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`005180b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/005180b8.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 33.33% / 新版 37.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0051ce30"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0053fcc8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "0051ce3c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0053fc9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:0051ce34"
      ]
    ],
    [
      "unmatched:0051ce30",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0053fca4"
      ]
    ],
    [
      "unmatched:0051ce34",
      "READ",
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
      "0053fc9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0053fccc"
      ]
    ],
    [
      "0053fcc8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0053fca4"
      ]
    ],
    [
      "0053fccc",
      "READ",
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

- 旧版 [`0051ce30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051cddc.md#insn-0051ce30) · [`0051ce3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051cddc.md#insn-0051ce3c)
- 新版 [`0053fcc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053fc74.md#insn-0053fcc8)

~~~diff
- 0051ce30 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0051ce30 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 0051ce30 bytes e1feff54
- 0051ce3c ["COPY", "register:0:8", ["register:40f0:8"]]
- 0051ce3c ["RETURN", null, ["register:0:8"]]
- 0051ce3c bytes c0035fd6
+ 0053fcc8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 0053fcc8 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 0053fcc8 bytes e1feff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-885a73eefccb21564e5eee761dea114c"></a>

### [`0051cf70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051cf70.md) → [`0053fe08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053fe08.md) FUN_0053fe08

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0051ce40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051ce40.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 1件 [`0053fcd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053fcd8.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 65.22% / 新版 65.22%

CFGの説明率　旧版 29.41% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0051cf70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0051cf70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0051cf74"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0051cf70",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:0051cf74",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0051cf78",
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
      "0053fe08",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "0053fe0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0053fe10",
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

- 旧版 [`0051cf70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051cf70.md#insn-0051cf70) · [`0051cf74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051cf70.md#insn-0051cf74) · [`0051cf78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051cf70.md#insn-0051cf78)

~~~diff
- 0051cf70 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0051cf70 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0051cf70 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 0051cf70 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0051cf70 bytes fd7bbca9
- 0051cf74 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 0051cf74 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 0051cf74 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0051cf74 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0051cf74 bytes f85f01a9
- 0051cf78 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 0051cf78 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 0051cf78 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0051cf78 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0051cf78 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89e17952925d043275b7b8ad7c1e4197"></a>

### [`0051d040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d040.md) → [`0053fed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053fed8.md) FUN_0053fed8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 75.76% / 新版 75.76%

CFGの説明率　旧版 72.73% / 新版 80.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "0051d0b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "0051d0bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "0053ff4c"
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
      "unmatched:0051d0a4",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:0051d0b4",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0112a058"
      ]
    ],
    [
      "unmatched:0051d0bc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c58260"
      ]
    ]
  ],
  "added": [
    [
      "0053ff3c",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "0053ff4c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0112a058"
      ]
    ],
    [
      "0053ff54",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c58260"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051d0b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d040.md#insn-0051d0b4) · [`0051d0bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d040.md#insn-0051d0bc)
- 新版 [`0053ff4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053fed8.md#insn-0053ff4c)

~~~diff
- 0051d0b4 ["COPY", "register:0:8", ["register:4048:8"]]
- 0051d0b4 ["INT_ADD", "register:40f0:8", ["const:51d0b4:8", "const:4:8"]]
- 0051d0b4 ["CALLIND", null, ["register:0:8"]]
- 0051d0b4 bytes 20013fd6
- 0051d0bc ["INT_ADD", "register:40f0:8", ["const:51d0bc:8", "const:4:8"]]
- 0051d0bc ["CALL", null, ["callee:00c58260:8"]]
- 0051d0bc bytes d5f91a94
+ 0053ff4c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0053ff4c ["INT_ADD", "register:40f0:8", ["const:53ff4c:8", "const:4:8"]]
+ 0053ff4c ["CALLIND", null, ["register:0:8"]]
+ 0053ff4c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e767a205ef11f8acfd022e1327c49f5"></a>

### [`0051d4f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d4f0.md) → [`00540388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540388.md) FUN_00540388

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 8件 [`0048d684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048d684.md) [`0048d834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048d834.md) [`0048f85c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048f85c.md) [`004a31f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a31f0.md) [`004d6c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6c30.md) · 呼出先 8件 [`00513fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/00513fb0.md) [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 8件 [`004b051c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b051c.md) [`004b06cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b0/004b06cc.md) [`004b26f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b2/004b26f4.md) [`004c6088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c6088.md) [`004f9ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004f9/004f9ac8.md) · 呼出先 8件 [`00536e48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00536/00536e48.md) [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 branch_condition_or_target, call, call_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 81.25% / 新版 81.25%

CFGの説明率　旧版 60.00% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0051d510"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0051d514"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0051d518"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0051d510",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:0051d514",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:0051d518",
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
      "005403a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "005403ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "005403b0",
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

- 旧版 [`0051d510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d4f0.md#insn-0051d510) · [`0051d514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d4f0.md#insn-0051d514) · [`0051d518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d4f0.md#insn-0051d518)

~~~diff
- 0051d510 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0051d510 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0051d510 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0051d510 bytes a8831ff8
- 0051d514 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 0051d514 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 0051d514 bytes e00700f9
- 0051d518 ["COPY", "tmp:0:4", ["const:0:4"]]
- 0051d518 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 0051d518 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0051d518 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 0051d518 bytes ff430039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc92051bd6924c576e575e1f79665bfa"></a>

### [`0051d9e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d9e4.md) → [`0054087c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/0054087c.md) FUN_0054087c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 6件 [`004f8244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f8/004f8244.md) [`004f9934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f9/004f9934.md) [`00503af8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00503/00503af8.md) [`00504f50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00504/00504f50.md) [`005054cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00505/005054cc.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)
- 新版 呼出元 6件 [`0051b0dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051b/0051b0dc.md) [`0051c7cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051c/0051c7cc.md) [`00526990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00526/00526990.md) [`00527de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00527/00527de8.md) [`00528364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00528/00528364.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0051d9e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0051d9e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0054087c"
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
      "unmatched:0051d9e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0051d9f0",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:0051d9f4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0041fdf0"
      ]
    ]
  ],
  "added": [
    [
      "0054087c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00540888",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "0054088c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "004428f0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051d9e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d9e4.md#insn-0051d9e4) · [`0051d9f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d9e4.md#insn-0051d9f4)
- 新版 [`0054087c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/0054087c.md#insn-0054087c)

~~~diff
- 0051d9e4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0051d9e4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0051d9e4 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 0051d9e4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0051d9e4 bytes fd7bbfa9
- 0051d9f4 ["INT_ADD", "register:40f0:8", ["const:51d9f4:8", "const:4:8"]]
- 0051d9f4 ["CALL", null, ["ram:41fdf0:8"]]
- 0051d9f4 bytes ff08fc97
+ 0054087c ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 0054087c ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 0054087c ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 0054087c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 0054087c bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8caacc99e6874482b3e44da994a347e"></a>

### [`0051e3d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051e/0051e3d8.md) → [`00541270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/00541270.md) FUN_00541270

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0048f014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048f014.md) [`0051e3d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051e/0051e3d8.md) · 呼出先 9件 [`0051e3d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051e/0051e3d8.md) [`0051e9ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051e/0051e9ec.md) [`0051ec50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051e/0051ec50.md) [`0051ef84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051e/0051ef84.md) [`0051f2b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051f/0051f2b4.md)
- 新版 呼出元 2件 [`004b1eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b1/004b1eac.md) [`00541270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/00541270.md) · 呼出先 9件 [`00541270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/00541270.md) [`00541884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/00541884.md) [`00541ae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/00541ae8.md) [`00541e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/00541e1c.md) [`0054214c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00542/0054214c.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 94.86% / 新版 94.86%

CFGの説明率　旧版 73.83% / 新版 71.90%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 5件, `unresolved_store_alignment` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0051e3dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0051e3dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0051e3e0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0051e3dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:0051e3e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:0051e3e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00541274",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00541278",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "0054127c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051e3dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051e/0051e3d8.md#insn-0051e3dc) · [`0051e3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051e/0051e3d8.md#insn-0051e3e0) · [`0051e3e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051e/0051e3d8.md#insn-0051e3e4)

~~~diff
- 0051e3dc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0051e3dc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0051e3dc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0051e3dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0051e3dc bytes fd7b01a9
- 0051e3e0 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 0051e3e0 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 0051e3e0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0051e3e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0051e3e0 bytes fc6f02a9
- 0051e3e4 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 0051e3e4 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 0051e3e4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 0051e3e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0051e3e4 bytes fa6703a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f23908526c7d8d623e70f8f874306bb"></a>

### [`0051e9ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051e/0051e9ec.md) → [`00541884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/00541884.md) FUN_00541884

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`0051e3d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051e/0051e3d8.md) [`0051f2b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051f/0051f2b4.md) [`0051f53c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051f/0051f53c.md) · 呼出先 0件 
- 新版 呼出元 3件 [`00541270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/00541270.md) [`0054214c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00542/0054214c.md) [`005423d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00542/005423d4.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 66.01% / 新版 66.01%

CFGの説明率　旧版 14.71% / 新版 13.89%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 10件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0051ead4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0051eae0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0051eae8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0051e9f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005418cc"
      ]
    ],
    [
      "unmatched:0051ea38",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00541a58"
      ]
    ],
    [
      "unmatched:0051ea4c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005419d8"
      ]
    ]
  ],
  "added": [
    [
      "00541890",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005418cc"
      ]
    ],
    [
      "005418d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00541a58"
      ]
    ],
    [
      "005418e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005419d8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051e9f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051e/0051e9ec.md#insn-0051e9f8) · [`0051ea38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051e/0051e9ec.md#insn-0051ea38) · [`0051ea4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051e/0051e9ec.md#insn-0051ea4c)

~~~diff
- 0051e9f8 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
- 0051e9f8 bytes e0010054
- 0051ea38 ["CBRANCH", null, ["local:b39:8", "register:101:1"]]
- 0051ea38 bytes 400c0054
- 0051ea4c ["CBRANCH", null, ["local:b31:8", "register:101:1"]]
- 0051ea4c bytes a0070054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27b1106650d3a93e597ef1b377823e5c"></a>

### [`0051ec50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051e/0051ec50.md) → [`00541ae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/00541ae8.md) FUN_00541ae8

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0051e3d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051e/0051e3d8.md) · 呼出先 2件 [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 1件 [`00541270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/00541270.md) · 呼出先 2件 [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 78.33% / 新版 78.33%

CFGの説明率　旧版 27.27% / 新版 25.64%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 15件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0051ec98"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0051eccc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0051ece8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0051ec98",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00541b74"
      ]
    ],
    [
      "unmatched:0051eccc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00541c20"
      ]
    ],
    [
      "00541b70",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:0051ed38"
      ]
    ]
  ],
  "added": [
    [
      "00541b30",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00541b74"
      ]
    ],
    [
      "00541b64",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00541c20"
      ]
    ],
    [
      "00541b70",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00541bd0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051ec98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051e/0051ec50.md#insn-0051ec98) · [`0051eccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051e/0051ec50.md#insn-0051eccc) · [`0051ece8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051e/0051ec50.md#insn-0051ece8)

~~~diff
- 0051ec98 ["CBRANCH", null, ["local:b11:8", "register:101:1"]]
- 0051ec98 bytes 20020054
- 0051eccc ["CBRANCH", null, ["local:b29:8", "register:102:1"]]
- 0051eccc bytes e2050054
- 0051ece8 ["CBRANCH", null, ["local:b12:8", "register:101:1"]]
- 0051ece8 bytes c0ffff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d93d2eddff85c5534d5cc1066923dfaf"></a>

### [`0051ef84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051e/0051ef84.md) → [`00541e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/00541e1c.md) FUN_00541e1c

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0051e3d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051e/0051e3d8.md) · 呼出先 2件 [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 1件 [`00541270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/00541270.md) · 呼出先 2件 [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 83.66% / 新版 83.66%

CFGの説明率　旧版 33.33% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 9件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0051f130"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00541fc8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0051efc4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0051efc4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00541f14"
      ]
    ],
    [
      "00541f38",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00541f2c"
      ]
    ],
    [
      "00541efc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00541f2c"
      ]
    ]
  ],
  "added": [
    [
      "00541e5c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00541f14"
      ]
    ],
    [
      "00541ec8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00541ebc"
      ]
    ],
    [
      "00541efc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00541ebc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051efc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051e/0051ef84.md#insn-0051efc4) · [`0051f080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051e/0051ef84.md#insn-0051f080) · [`0051f090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051e/0051ef84.md#insn-0051f090)

~~~diff
- 0051efc4 ["CBRANCH", null, ["local:b21:8", "register:101:1"]]
- 0051efc4 bytes c0050054
- 0051f080 ["CBRANCH", null, ["local:b40:8", "register:102:1"]]
- 0051f080 bytes 22030054
- 0051f090 ["CBRANCH", null, ["local:b40:8", "register:102:1"]]
- 0051f090 bytes a2020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1380411419d0ae1dd4d13c0adb2459a1"></a>

### [`0051f53c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051f/0051f53c.md) → [`005423d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00542/005423d4.md) FUN_005423d4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`0051e3d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051e/0051e3d8.md) [`0051f2b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051f/0051f2b4.md) [`0051f6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051f/0051f6d0.md) · 呼出先 1件 [`0051e9ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051e/0051e9ec.md)
- 新版 呼出元 3件 [`00541270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/00541270.md) [`0054214c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00542/0054214c.md) [`00542568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00542/00542568.md) · 呼出先 1件 [`00541884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/00541884.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 81.19% / 新版 81.19%

CFGの説明率　旧版 52.63% / 新版 45.45%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0051f5c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0051f634"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0051f638"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0051f604",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005424bc"
      ]
    ],
    [
      "unmatched:0051f60c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00542558"
      ]
    ],
    [
      "unmatched:0051f678",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00542530"
      ]
    ]
  ],
  "added": [
    [
      "0054249c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005424bc"
      ]
    ],
    [
      "005424a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00542558"
      ]
    ],
    [
      "00542510",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00542530"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051f5c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051f/0051f53c.md#insn-0051f5c0) · [`0051f604`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051f/0051f53c.md#insn-0051f604) · [`0051f60c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051f/0051f53c.md#insn-0051f60c)

~~~diff
- 0051f5c0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:8:8"]]
- 0051f5c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0051f5c0 bytes a80600f9
- 0051f604 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 0051f604 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 0051f604 bytes 03010054
- 0051f60c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 0051f60c ["CBRANCH", null, ["local:b23:8", "tmp:0:1"]]
- 0051f60c bytes a3050054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abf8260f10ffd84d8e5dbef70299b91e"></a>

### [`0051f8e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051f/0051f8e4.md) → [`0054277c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00542/0054277c.md) FUN_0054277c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0051e3d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051e/0051e3d8.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00541270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/00541270.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 93.23% / 新版 93.23%

CFGの説明率　旧版 55.56% / 新版 59.70%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0051fa0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005428a4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0051fa44"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0051fa44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00542938"
      ]
    ],
    [
      "unmatched:0051fa54",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00542938"
      ]
    ],
    [
      "unmatched:0051fa90",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005428fc"
      ]
    ]
  ],
  "added": [
    [
      "005428dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00542938"
      ]
    ],
    [
      "005428ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00542938"
      ]
    ],
    [
      "00542928",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005428fc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051fa0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051f/0051f8e4.md#insn-0051fa0c) · [`0051fa44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051f/0051f8e4.md#insn-0051fa44) · [`0051fa54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051f/0051f8e4.md#insn-0051fa54)

~~~diff
- 0051fa0c ["COPY", "tmp:0:8", ["register:4080:8"]]
- 0051fa0c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 0051fa0c bytes 0002803d
- 0051fa44 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 0051fa44 ["CBRANCH", null, ["local:b35:8", "tmp:0:1"]]
- 0051fa44 bytes ea020054
- 0051fa54 ["CBRANCH", null, ["local:b35:8", "register:101:1"]]
- 0051fa54 bytes 60020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18539150d6cec1527d5cabc9c12184cc"></a>

### [`0051fdac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051f/0051fdac.md) → [`00542c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00542/00542c44.md) FUN_00542c44

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0051faf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051f/0051faf8.md) · 呼出先 2件 [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 1件 [`00542990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00542/00542990.md) · 呼出先 2件 [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 85.53% / 新版 85.53%

CFGの説明率　旧版 37.04% / 新版 47.62%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0051fdf4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00542c8c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0051fe0c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0051fe0c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00542d58"
      ]
    ],
    [
      "unmatched:0051fe30",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00542d20"
      ]
    ],
    [
      "unmatched:0051fe78",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00542ce4"
      ]
    ]
  ],
  "added": [
    [
      "00542ca4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00542d58"
      ]
    ],
    [
      "00542cc8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00542d20"
      ]
    ],
    [
      "00542d10",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00542ce4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051fdf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051f/0051fdac.md#insn-0051fdf4) · [`0051fe0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051f/0051fdac.md#insn-0051fe0c) · [`0051fe30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051f/0051fdac.md#insn-0051fe30)

~~~diff
- 0051fdf4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0051fdf4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 0051fdf4 bytes 8002803d
- 0051fe0c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0051fe0c ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
- 0051fe0c ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
- 0051fe0c ["CBRANCH", null, ["local:b18:8", "tmp:2:1"]]
- 0051fe0c bytes ac050054
- 0051fe30 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 0051fe30 ["CBRANCH", null, ["local:b16:8", "tmp:0:1"]]
- 0051fe30 bytes ca020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c6a1c821e9d90d42bac97070c4e4e1c"></a>

### [`0052009c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/0052009c.md) → [`00542f34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00542/00542f34.md) FUN_00542f34

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0051fee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051f/0051fee0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00542d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00542/00542d78.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0052009c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0052009c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00542f34"
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
      "unmatched:0052009c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005200a8",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:005200ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "00542f34",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00542f40",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "00542f44",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0043b738"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052009c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/0052009c.md#insn-0052009c) · [`005200ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/0052009c.md#insn-005200ac)
- 新版 [`00542f34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00542/00542f34.md#insn-00542f34)

~~~diff
- 0052009c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0052009c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0052009c ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 0052009c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0052009c bytes fd7bbfa9
- 005200ac ["INT_ADD", "register:40f0:8", ["const:5200ac:8", "const:4:8"]]
- 005200ac ["CALL", null, ["ram:418c38:8"]]
- 005200ac bytes e3e2fb97
+ 00542f34 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00542f34 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00542f34 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 00542f34 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00542f34 bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f86b37f930a7df97bf4df7c471e9f5a0"></a>

### [`005200b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/005200b0.md) → [`00542f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00542/00542f48.md) FUN_00542f48

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00482500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482500.md) · 呼出先 5件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00512ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512ca8.md) [`00520264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520264.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`004a5398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a5/004a5398.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00535b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b40.md) [`005430fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/005430fc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 94.50% / 新版 94.50%

CFGの説明率　旧版 75.00% / 新版 65.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00520100"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00520144"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00542f98"
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
      "unmatched:00520100",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005430f0"
      ]
    ],
    [
      "unmatched:00520144",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005430f8"
      ]
    ]
  ],
  "added": [
    [
      "00542f98",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005430f0"
      ]
    ],
    [
      "00542fdc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005430f8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00520100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/005200b0.md#insn-00520100) · [`00520144`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/005200b0.md#insn-00520144)
- 新版 [`00542f98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00542/00542f48.md#insn-00542f98)

~~~diff
- 00520100 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00520100 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00520100 ["CBRANCH", null, ["local:b13:8", "tmp:1:1"]]
- 00520100 bytes c80a0054
- 00520144 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00520144 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00520144 ["CBRANCH", null, ["local:b14:8", "tmp:1:1"]]
- 00520144 bytes e8080054
+ 00542f98 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00542f98 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 00542f98 ["CBRANCH", null, ["local:b16:8", "tmp:1:1"]]
+ 00542f98 bytes c80a0054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30aafb24eec1e71b6aa91b5138ecf573"></a>

### [`0052046c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/0052046c.md) → [`00543304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543304.md) FUN_00543304

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 70.00% / 新版 77.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00520484"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0054331c"
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
      "unmatched:00520484",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00543340"
      ]
    ]
  ],
  "added": [
    [
      "0054331c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00543340"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00520484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/0052046c.md#insn-00520484) · [`00520480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/0052046c.md#insn-00520480)
- 新版 [`0054331c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543304.md#insn-0054331c)

~~~diff
- 00520484 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00520484 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00520484 bytes 21010054
+ 0054331c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 0054331c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 0054331c bytes 21010054
- 00520480 ["INT_LESSEQUAL", "register:105:1", ["register:40a0:8", "register:4040:8"]]
- 00520480 ["INT_SBORROW", "register:106:1", ["register:4040:8", "register:40a0:8"]]
- 00520480 ["INT_SUB", "tmp:0:8", ["register:4040:8", "register:40a0:8"]]
- 00520480 ["INT_SLESS", "register:107:1", ["tmp:0:8", "const:0:8"]]
- 00520480 bytes 1f0114eb
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-925123c9a4bac291c43e1a420aa41c55"></a>

### [`005204d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/005204d4.md) → [`0054336c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/0054336c.md) FUN_0054336c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00520278`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520278.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00543110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543110.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

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
      "site": "005204d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005204d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0054336c"
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
      "unmatched:005204d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005204e0",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:005204e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "0054336c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00543378",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "0054337c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0043b738"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005204d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/005204d4.md#insn-005204d4) · [`005204e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/005204d4.md#insn-005204e4)
- 新版 [`0054336c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/0054336c.md#insn-0054336c)

~~~diff
- 005204d4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005204d4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005204d4 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 005204d4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005204d4 bytes fd7bbfa9
- 005204e4 ["INT_ADD", "register:40f0:8", ["const:5204e4:8", "const:4:8"]]
- 005204e4 ["CALL", null, ["ram:418c38:8"]]
- 005204e4 bytes d5e1fb97
+ 0054336c ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 0054336c ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 0054336c ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 0054336c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 0054336c bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-845a42bc2777d1f39f729c90732822c3"></a>

### [`00520d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520d84.md) → [`00543c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543c1c.md) FUN_00543c1c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 20件 [`004a1040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a1040.md) [`004a1190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a1190.md) [`004a1328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a1328.md) [`004a15d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a15d0.md) [`004a181c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a181c.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00520eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520eb0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 20件 [`004c3ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c3/004c3ed8.md) [`004c4028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c4028.md) [`004c41c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c41c0.md) [`004c4468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c4468.md) [`004c46b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c46b4.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00543d48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543d48.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.33% / 新版 97.33%

CFGの説明率　旧版 82.35% / 新版 77.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00520dc4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00543c5c"
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
      "unmatched:00520dc4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00543d3c"
      ]
    ]
  ],
  "added": [
    [
      "00543c5c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00543d3c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00520dc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520d84.md#insn-00520dc4) · [`00520dac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520d84.md#insn-00520dac)
- 新版 [`00543c5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543c1c.md#insn-00543c5c) · [`00543c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543c1c.md#insn-00543c44)

~~~diff
- 00520dc4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
- 00520dc4 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 00520dc4 bytes 0a0700b5
+ 00543c5c ["INT_NOTEQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
+ 00543c5c ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
+ 00543c5c bytes 0a0700b5
- 00520dac ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00520dac ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00520dac ["CBRANCH", null, ["local:b5:8", "tmp:1:1"]]
+ 00543c44 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00543c44 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
+ 00543c44 ["CBRANCH", null, ["local:b6:8", "tmp:1:1"]]
- 00520dac bytes 09030054
+ 00543c44 bytes 09030054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd74e062a4d6a07ff5b04a24c75b82ce"></a>

### [`00520ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520ff4.md) → [`00543e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543e8c.md) FUN_00543e8c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`004a4bf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a4bf0.md) · 呼出先 8件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`005214b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00521/005214b4.md) [`0052163c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00521/0052163c.md) [`005217c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00521/005217c8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`004c7a88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c7/004c7a88.md) · 呼出先 8件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0054434c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/0054434c.md) [`005444d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/005444d4.md) [`00544660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544660.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 76.43% / 新版 76.43%

CFGの説明率　旧版 45.24% / 新版 47.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 11件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0052133c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0052133c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00521380"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00543f7c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00521384"
      ]
    ],
    [
      "unmatched:00521160",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005442c0"
      ]
    ],
    [
      "unmatched:00521170",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57a90"
      ]
    ]
  ],
  "added": [
    [
      "00543f7c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "0054421c"
      ]
    ],
    [
      "00543ff8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005442c0"
      ]
    ],
    [
      "00544008",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57a90"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00521158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520ff4.md#insn-00521158) · [`00521160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520ff4.md#insn-00521160) · [`00521184`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520ff4.md#insn-00521184)

~~~diff
- 00521158 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00521158 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00521158 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00521158 ["INT_ADD", "tmp:1:8", ["const:0:8", "const:1:8"]]
- 00521158 bytes 08159f9a
- 00521160 ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00521160 ["CBRANCH", null, ["local:b51:8", "tmp:0:1"]]
- 00521160 bytes 491600b5
- 00521184 ["CBRANCH", null, ["local:b39:8", "register:101:1"]]
- 00521184 bytes e00e0054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb77c9814ef4ebf4b38d79d1664b6ad1"></a>

### [`005214b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00521/005214b4.md) → [`0054434c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/0054434c.md) FUN_0054434c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00520ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520ff4.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`00543e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543e8c.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 94.90% / 新版 94.90%

CFGの説明率　旧版 78.57% / 新版 78.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00521578"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00521598"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00544410"
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
      "unmatched:00521578",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0054441c"
      ]
    ],
    [
      "unmatched:00521598",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0054447c"
      ]
    ]
  ],
  "added": [
    [
      "00544410",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0054441c"
      ]
    ],
    [
      "00544430",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0054447c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00521578`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00521/005214b4.md#insn-00521578) · [`00521598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00521/005214b4.md#insn-00521598)
- 新版 [`00544410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/0054434c.md#insn-00544410)

~~~diff
- 00521578 ["CBRANCH", null, ["local:b10:8", "register:102:1"]]
- 00521578 bytes 62000054
- 00521598 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00521598 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 00521598 bytes 63020054
+ 00544410 ["CBRANCH", null, ["local:b9:8", "register:102:1"]]
+ 00544410 bytes 62000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cfb2452557bb4c689060f3db9faba0af"></a>

### [`0052163c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00521/0052163c.md) → [`005444d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/005444d4.md) FUN_005444d4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00520ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520ff4.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`00543e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543e8c.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 91.92% / 新版 91.92%

CFGの説明率　旧版 66.67% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0052163c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0052163c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00521640"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0052163c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00521640",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00521644",
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
      "005444d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "005444d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "005444dc",
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

- 旧版 [`0052163c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00521/0052163c.md#insn-0052163c) · [`00521640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00521/0052163c.md#insn-00521640) · [`00521644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00521/0052163c.md#insn-00521644)

~~~diff
- 0052163c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0052163c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0052163c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 0052163c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0052163c bytes fd7bbca9
- 00521640 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00521640 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00521640 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00521640 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00521640 bytes f85f01a9
- 00521644 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00521644 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00521644 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00521644 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00521644 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80c3f1de15cca85f68fe6a8cfcc1aab0"></a>

### [`005217c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00521/005217c8.md) → [`00544660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544660.md) FUN_00544660

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00520ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520ff4.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`00543e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543e8c.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 67.86% / 新版 65.52%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00521814"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0052189c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "005446ac"
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
      "unmatched:0052189c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00544798"
      ]
    ]
  ],
  "added": [
    [
      "00544734",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00544798"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00521814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00521/005217c8.md#insn-00521814) · [`0052189c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00521/005217c8.md#insn-0052189c)
- 新版 [`005446ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544660.md#insn-005446ac)

~~~diff
- 00521814 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00521814 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00521814 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00521814 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:1:8"]]
- 00521814 bytes 28b5889a
- 0052189c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 0052189c ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 0052189c bytes 23030054
+ 005446ac ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 005446ac ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 005446ac ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
+ 005446ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:1:8"]]
+ 005446ac bytes 28b5889a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abcd4fe75c074dc5687a9836c7da73aa"></a>

### [`00521ad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00521/00521ad8.md) → [`00544970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544970.md) FUN_00544970

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`004a80c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a80c8.md) [`00521cc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00521/00521cc4.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`004caf60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004caf60.md) [`00544b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544b5c.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00521ad8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00521ad8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00544970"
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
      "unmatched:00521ad8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00521ae4",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00521ae8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "00544970",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0054497c",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "00544980",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0043b738"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00521ad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00521/00521ad8.md#insn-00521ad8) · [`00521ae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00521/00521ad8.md#insn-00521ae8)
- 新版 [`00544970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544970.md#insn-00544970)

~~~diff
- 00521ad8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00521ad8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00521ad8 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 00521ad8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00521ad8 bytes fd7bbfa9
- 00521ae8 ["INT_ADD", "register:40f0:8", ["const:521ae8:8", "const:4:8"]]
- 00521ae8 ["CALL", null, ["ram:418c38:8"]]
- 00521ae8 bytes 54dcfb97
+ 00544970 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00544970 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00544970 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 00544970 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00544970 bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f701fece3fc61ee6fbaaaba8ba9280a9"></a>

### [`00521c0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00521/00521c0c.md) → [`00544aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544aa4.md) FUN_00544aa4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb330.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00521c20"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00544ab8"
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
      "unmatched:00521c20",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00544ad4"
      ]
    ]
  ],
  "added": [
    [
      "00544ab8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00544ad4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00521c20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00521/00521c0c.md#insn-00521c20) · [`00521c28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00521/00521c0c.md#insn-00521c28)
- 新版 [`00544ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544aa4.md#insn-00544ab8) · [`00544ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544aa4.md#insn-00544ac0)

~~~diff
- 00521c20 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 00521c20 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00521c20 bytes f30000b4
+ 00544ab8 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
+ 00544ab8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00544ab8 bytes f30000b4
- 00521c28 ["INT_ADD", "register:40f0:8", ["const:521c28:8", "const:4:8"]]
- 00521c28 ["CALL", null, ["callee:00c57d80:8"]]
+ 00544ac0 ["INT_ADD", "register:40f0:8", ["const:544ac0:8", "const:4:8"]]
+ 00544ac0 ["CALL", null, ["callee:00c57d80:8"]]
- 00521c28 bytes c2e51a94
+ 00544ac0 bytes b04c1c94
~~~


<a id="compare-e72d18b7f28303046275c8eb40a333be"></a>

### [`00521f10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00521/00521f10.md) → [`00544da8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544da8.md) FUN_00544da8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`0112a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a058.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 78.26% / 新版 78.26%

CFGの説明率　旧版 25.00% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00521f58"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00544df0"
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
      "unmatched:00521f48",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00521f58",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0112a058"
      ]
    ]
  ],
  "added": [
    [
      "00544de0",
      "READ",
      [
        "storage",
        "00c67338",
        null,
        "pointer"
      ]
    ],
    [
      "00544df0",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "0112a058"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00521f58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00521/00521f10.md#insn-00521f58) · [`00521f20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00521/00521f10.md#insn-00521f20)
- 新版 [`00544df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544da8.md#insn-00544df0) · [`00544db8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544da8.md#insn-00544db8)

~~~diff
- 00521f58 ["COPY", "register:0:8", ["register:4048:8"]]
- 00521f58 ["INT_ADD", "register:40f0:8", ["const:521f58:8", "const:4:8"]]
- 00521f58 ["CALLIND", null, ["register:0:8"]]
- 00521f58 bytes 20013fd6
+ 00544df0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00544df0 ["INT_ADD", "register:40f0:8", ["const:544df0:8", "const:4:8"]]
+ 00544df0 ["CALLIND", null, ["register:0:8"]]
+ 00544df0 bytes 20013fd6
- 00521f20 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00521f20 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00521f20 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00521f20 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
+ 00544db8 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 00544db8 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00544db8 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00544db8 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00521f20 bytes 88000036
+ 00544db8 bytes 88000036
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2efa9ffc9e0458e653421052207fd170"></a>

### [`00522300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522300.md) → [`00545198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545198.md) FUN_00545198

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`004c45bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c4/004c45bc.md) · 呼出先 2件 [`00522664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522664.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`004e7454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e7454.md) · 呼出先 2件 [`005454fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/005454fc.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 86.23% / 新版 86.23%

CFGの説明率　旧版 65.31% / 新版 64.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 8件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00522334"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005224a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005451cc"
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
      "unmatched:00522334",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00522338",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00545240"
      ]
    ],
    [
      "unmatched:00522388",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57c50"
      ]
    ]
  ],
  "added": [
    [
      "005451cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "005451d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00545240"
      ]
    ],
    [
      "00545220",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57c50"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00522334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522300.md#insn-00522334) · [`00522338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522300.md#insn-00522338) · [`00522370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522300.md#insn-00522370)

~~~diff
- 00522334 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00522334 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4010:8"]]
- 00522334 bytes e20700f9
- 00522338 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00522338 bytes 80030054
- 00522370 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00522370 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00522370 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00522370 ["COPY", "register:40e0:8", ["tmp:0:8"]]
- 00522370 bytes 3c018b9a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5edd5d2c8ce0a7353c3034e30bbe591"></a>

### [`00522664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522664.md) → [`005454fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/005454fc.md) FUN_005454fc

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`004c476c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c4/004c476c.md) [`00522300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522300.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 2件 [`004e7604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e7604.md) [`00545198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545198.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 70.77% / 新版 70.77%

CFGの説明率　旧版 21.43% / 新版 17.65%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 4件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00522664"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00522664"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00522668"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00522664",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00522668",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:0052266c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005454fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00545500",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00545504",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00522664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522664.md#insn-00522664) · [`00522668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522664.md#insn-00522668) · [`0052266c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522664.md#insn-0052266c)

~~~diff
- 00522664 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00522664 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00522664 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00522664 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00522664 bytes fd7bbba9
- 00522668 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00522668 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00522668 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00522668 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00522668 bytes fa6701a9
- 0052266c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 0052266c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 0052266c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0052266c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0052266c bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5845ea1a7b74f4f409fa931b09ea149"></a>

### [`00522768`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522768.md) → [`00545600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545600.md) FUN_00545600

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.56% / 新版 97.56%

CFGの説明率　旧版 57.14% / 新版 63.16%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005227b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0054564c"
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
      "unmatched:005227b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00545674"
      ]
    ]
  ],
  "added": [
    [
      "0054564c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00545674"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005227b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522768.md#insn-005227b4) · [`00522780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522768.md#insn-00522780)
- 新版 [`0054564c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545600.md#insn-0054564c) · [`00545618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545600.md#insn-00545618)

~~~diff
- 005227b4 ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
- 005227b4 bytes 40010054
+ 0054564c ["CBRANCH", null, ["local:b9:8", "register:101:1"]]
+ 0054564c bytes 40010054
- 00522780 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 00522780 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 00545618 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
+ 00545618 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00522780 bytes 730200b4
+ 00545618 bytes 730200b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3dc5b7fc86e7129cc32e8264d4706f30"></a>

### [`005228d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/005228d0.md) → [`00545768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545768.md) FUN_00545768

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

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
      "site": "005228dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00545774"
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
      "unmatched:005228dc",
      "DATA",
      [
        "storage",
        "00bed560",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00545774",
      "DATA",
      [
        "storage",
        "00c6a120",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005228dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/005228d0.md#insn-005228dc) · [`005228d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/005228d0.md#insn-005228d0)
- 新版 [`00545774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545768.md#insn-00545774)

~~~diff
- 005228dc ["COPY", "tmp:0:8", ["register:4000:8"]]
- 005228dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 005228dc bytes 090000f9
+ 00545774 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00545774 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00545774 bytes 090000f9
- 005228d0 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
- 005228d0 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 005228d0 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 005228d0 bytes 08204039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59dd6299d96133144a071ff8e6a4b57c"></a>

### [`00522a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522a64.md) → [`005458fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/005458fc.md) FUN_005458fc

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00522a64"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00522a64"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00522a7c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00522a64",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00522a70",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57a90"
      ]
    ],
    [
      "unmatched:00522a7c",
      "DATA",
      [
        "storage",
        "00bed5f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005458fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00545908",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57a90"
      ]
    ],
    [
      "00545914",
      "DATA",
      [
        "storage",
        "00c6a1b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00522a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522a64.md#insn-00522a64) · [`00522a70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522a64.md#insn-00522a70) · [`00522a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522a64.md#insn-00522a7c)

~~~diff
- 00522a64 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00522a64 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00522a64 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 00522a64 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00522a64 bytes fd7bbfa9
- 00522a70 ["INT_ADD", "register:40f0:8", ["const:522a70:8", "const:4:8"]]
- 00522a70 ["CALL", null, ["callee:00c57a90:8"]]
- 00522a70 bytes 74e11a94
- 00522a7c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00522a7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00522a7c bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43efd563023e0402bc8b242555f2e334"></a>

### [`00522bb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522bb8.md) → [`00545a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545a50.md) FUN_00545a50

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

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
      "site": "00522bc4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00545a5c"
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
      "unmatched:00522bc4",
      "DATA",
      [
        "storage",
        "00bed670",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00545a5c",
      "DATA",
      [
        "storage",
        "00c6a230",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00522bc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522bb8.md#insn-00522bc4) · [`00522bb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522bb8.md#insn-00522bb8)
- 新版 [`00545a5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545a50.md#insn-00545a5c)

~~~diff
- 00522bc4 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00522bc4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00522bc4 bytes 090000f9
+ 00545a5c ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00545a5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00545a5c bytes 090000f9
- 00522bb8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
- 00522bb8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00522bb8 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00522bb8 bytes 08204039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3b06c484e52719da5bc186dfaa2f6ef"></a>

### [`00522bd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522bd8.md) → [`00545a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545a70.md) FUN_00545a70

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

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
      "site": "00522be4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00545a7c"
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
      "unmatched:00522be4",
      "DATA",
      [
        "storage",
        "00bed670",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00545a7c",
      "DATA",
      [
        "storage",
        "00c6a230",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00522be4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522bd8.md#insn-00522be4) · [`00522bd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522bd8.md#insn-00522bd8)
- 新版 [`00545a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545a70.md#insn-00545a7c)

~~~diff
- 00522be4 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00522be4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00522be4 bytes 090000f9
+ 00545a7c ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00545a7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00545a7c bytes 090000f9
- 00522bd8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
- 00522bd8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00522bd8 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00522bd8 bytes 08204039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac9b0c648b579b3f46026759911c1b8c"></a>

### [`00522c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522c18.md) → [`00545ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545ab0.md) FUN_00545ab0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`004cb65c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cb/004cb65c.md) · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`004ee4f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ee/004ee4f4.md) · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 50.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00522c44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00545adc"
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
      "unmatched:00522c44",
      "DATA",
      [
        "storage",
        "00bed670",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00545adc",
      "DATA",
      [
        "storage",
        "00c6a230",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00522c44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522c18.md#insn-00522c44) · [`00522c2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522c18.md#insn-00522c2c)
- 新版 [`00545adc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545ab0.md#insn-00545adc) · [`00545ac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545ab0.md#insn-00545ac4)

~~~diff
- 00522c44 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00522c44 ["COPY", "tmp:1:8", ["register:4000:8"]]
- 00522c44 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:8:8"]]
- 00522c44 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00522c44 bytes 0a8400f8
+ 00545adc ["COPY", "tmp:0:8", ["register:4050:8"]]
+ 00545adc ["COPY", "tmp:1:8", ["register:4000:8"]]
+ 00545adc ["INT_ADD", "register:4000:8", ["register:4000:8", "const:8:8"]]
+ 00545adc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 00545adc bytes 0a8400f8
- 00522c2c ["INT_ADD", "register:40f0:8", ["const:522c2c:8", "const:4:8"]]
- 00522c2c ["CALL", null, ["callee:00c57a90:8"]]
+ 00545ac4 ["INT_ADD", "register:40f0:8", ["const:545ac4:8", "const:4:8"]]
+ 00545ac4 ["CALL", null, ["callee:00c57a90:8"]]
- 00522c2c bytes 05e11a94
+ 00545ac4 bytes f3471c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35278021ec8c217f6ac56857187d62f4"></a>

### [`00523270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00523/00523270.md) → [`00546108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/00546108.md) FUN_00546108

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00522d64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522d64.md) · 呼出先 2件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`00545bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545bfc.md) · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 80.18% / 新版 80.18%

CFGの説明率　旧版 7.69% / 新版 8.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 9件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0052329c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005232d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00546134"
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
      "unmatched:0052329c",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:005232a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:005233f8"
      ]
    ],
    [
      "unmatched:005232b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:005233f8"
      ]
    ]
  ],
  "added": [
    [
      "00546134",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00546138",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00546290"
      ]
    ],
    [
      "0054614c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00546290"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052329c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00523/00523270.md#insn-0052329c) · [`005232a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00523/00523270.md#insn-005232a0) · [`005232b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00523/00523270.md#insn-005232b4)

~~~diff
- 0052329c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0052329c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0052329c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0052329c bytes a8831ff8
- 005232a0 ["CBRANCH", null, ["local:b17:8", "register:101:1"]]
- 005232a0 bytes c00a0054
- 005232b4 ["CBRANCH", null, ["local:b17:8", "register:101:1"]]
- 005232b4 bytes 200a0054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af068f797862c3f9d6fd907e6f851d47"></a>

### [`0052342c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00523/0052342c.md) → [`005462c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/005462c4.md) FUN_005462c4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00522d64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522d64.md) · 呼出先 2件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`00545bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545bfc.md) · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 65.00% / 新版 65.00%

CFGの説明率　旧版 6.06% / 新版 11.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 12件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00523440"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00523440"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00523540"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00523440",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0052346c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00546424"
      ]
    ],
    [
      "unmatched:00523488",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00546424"
      ]
    ]
  ],
  "added": [
    [
      "005462d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00546304",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00546424"
      ]
    ],
    [
      "00546320",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00546424"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00523440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00523/0052342c.md#insn-00523440) · [`0052346c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00523/0052342c.md#insn-0052346c) · [`00523488`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00523/0052342c.md#insn-00523488)

~~~diff
- 00523440 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00523440 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00523440 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00523440 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00523440 bytes f44f06a9
- 0052346c ["CBRANCH", null, ["local:b25:8", "register:101:1"]]
- 0052346c bytes 00090054
- 00523488 ["CBRANCH", null, ["local:b25:8", "register:101:1"]]
- 00523488 bytes 20080054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2c2cc6007614773eee4f88f97c7750e"></a>

### [`0052383c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00523/0052383c.md) → [`005466d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/005466d4.md) FUN_005466d4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00522d64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522d64.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`00545bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545bfc.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 83.60% / 新版 83.60%

CFGの説明率　旧版 63.16% / 新版 54.55%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00523870"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00523884"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005238a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00523870",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:00523884",
      "WRITE",
      [
        "storage",
        "Stack[-0x90]",
        null,
        null
      ]
    ],
    [
      "unmatched:0052388c",
      "READ",
      [
        "storage",
        "Stack[-0x90]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00546708",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "0054671c",
      "WRITE",
      [
        "storage",
        "Stack[-0x90]",
        null,
        null
      ]
    ],
    [
      "00546724",
      "READ",
      [
        "storage",
        "Stack[-0x90]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00523870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00523/0052383c.md#insn-00523870) · [`00523884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00523/0052383c.md#insn-00523884) · [`005238a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00523/0052383c.md#insn-005238a4)

~~~diff
- 00523870 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00523870 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00523870 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00523870 bytes a8831ff8
- 00523884 ["COPY", "tmp:0:8", ["register:8:8"]]
- 00523884 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00523884 bytes e003803d
- 005238a4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 005238a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 005238a4 bytes e80b00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf0ac2e0adfb55dba0449bfe8090ebed"></a>

### [`00523df4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00523/00523df4.md) → [`00546c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/00546c8c.md) FUN_00546c8c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00522d64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522d64.md) · 呼出先 5件 [`005235bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00523/005235bc.md) [`005240ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/005240ec.md) [`005242cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/005242cc.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`00545bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545bfc.md) · 呼出先 5件 [`00546454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/00546454.md) [`00546f84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/00546f84.md) [`00547164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547164.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 53.33% / 新版 58.54%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 8件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00523ec0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00523ec4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00523ec8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00523ee8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00546db8"
      ]
    ],
    [
      "unmatched:00524048",
      "READ",
      [
        "storage",
        "Stack[-0x98]",
        null,
        null
      ]
    ],
    [
      "unmatched:005240b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00546f80"
      ]
    ]
  ],
  "added": [
    [
      "00546d80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00546db8"
      ]
    ],
    [
      "00546ee0",
      "READ",
      [
        "storage",
        "Stack[-0x98]",
        null,
        null
      ]
    ],
    [
      "00546f4c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00546f80"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00523ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00523/00523df4.md#insn-00523ea0) · [`00523ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00523/00523df4.md#insn-00523ec0) · [`00523ec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00523/00523df4.md#insn-00523ec4)

~~~diff
- 00523ea0 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00523ea0 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00523ea0 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00523ea0 ["INT_ZEXT", "register:4040:8", ["tmp:0:4"]]
- 00523ea0 bytes 0801891a
- 00523ec0 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00523ec0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00523ec0 bytes 6002803d
- 00523ec4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
- 00523ec4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00523ec4 bytes 680a00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc9506dc422923e621714c46ce7126cd"></a>

### [`005242cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/005242cc.md) → [`00547164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547164.md) FUN_00547164

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00522d64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00522/00522d64.md) [`00523df4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00523/00523df4.md) · 呼出先 3件 [`005240ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/005240ec.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 2件 [`00545bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00545/00545bfc.md) [`00546c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/00546c8c.md) · 呼出先 3件 [`00546f84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00546/00546f84.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 70.39% / 新版 70.39%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 14件, `unresolved_store_alignment` 19件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005242d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005242d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005242d4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005242d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:005242d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:005242d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00547168",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "0054716c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00547170",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005242d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/005242cc.md#insn-005242d0) · [`005242d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/005242cc.md#insn-005242d4) · [`005242d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/005242cc.md#insn-005242d8)

~~~diff
- 005242d0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005242d0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005242d0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 005242d0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005242d0 bytes fd7b08a9
- 005242d4 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 005242d4 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 005242d4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 005242d4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005242d4 bytes fa6709a9
- 005242d8 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 005242d8 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 005242d8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:a0:8"]]
- 005242d8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005242d8 bytes f85f0aa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63aadb370fac47677db5b2ab54cd4aca"></a>

### [`00524ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524ab4.md) → [`0054794c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/0054794c.md) FUN_0054794c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00524810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524810.md) · 呼出先 2件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`005476a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/005476a8.md) · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 2.70% / 新版 5.26%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 11件, `unresolved_store_alignment` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00524ab8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00524ab8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00524abc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00524ab8",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00524abc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00524ac0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00547950",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00547954",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00547958",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00524ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524ab4.md#insn-00524ab8) · [`00524abc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524ab4.md#insn-00524abc) · [`00524ac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524ab4.md#insn-00524ac0)

~~~diff
- 00524ab8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00524ab8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00524ab8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00524ab8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00524ab8 bytes fd7b02a9
- 00524abc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:30:8"]]
- 00524abc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
- 00524abc bytes fb1b00f9
- 00524ac0 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00524ac0 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00524ac0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00524ac0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00524ac0 bytes fa6704a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5da61d4758ec4e388a9ea5ad6e33f22"></a>

### [`00524c7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524c7c.md) → [`00547b14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00547/00547b14.md) FUN_00547b14

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

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
      "site": "00524c88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00524c8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00547b20"
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
      "unmatched:00524c88",
      "DATA",
      [
        "storage",
        "00bed6f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00547b20",
      "DATA",
      [
        "storage",
        "00c6a2b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00524c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524c7c.md#insn-00524c88) · [`00524c8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524c7c.md#insn-00524c8c) · [`00524c90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00524/00524c7c.md#insn-00524c90)

~~~diff
- 00524c88 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00524c88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00524c88 bytes 290000f9
- 00524c8c ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00524c8c ["INT_ADD", "tmp:1:8", ["register:4008:8", "const:8:8"]]
- 00524c8c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00524c8c bytes 28200039
- 00524c90 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00524c90 ["RETURN", null, ["register:0:8"]]
- 00524c90 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a144f2a16d0e7301b43bd5ddf0ec1a5"></a>

### [`00525380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525380.md) → [`00548218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548218.md) FUN_00548218

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`004e56e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e56e4.md) [`004f7f54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f7/004f7f54.md) [`0053d168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d168.md) [`00b88310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88310.md) · 呼出先 1件 [`00bdd170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd170.md)
- 新版 呼出元 4件 [`0050857c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/0050857c.md) [`0051adec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051adec.md) [`00560000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560000.md) [`00c04d58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c04/00c04d58.md) · 呼出先 1件 [`00c59bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59bc0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 78.57% / 新版 73.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00525418"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005482b0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0052540c"
    }
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`0052540c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525380.md#insn-0052540c) · [`00525418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525380.md#insn-00525418)
- 新版 [`005482a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548218.md#insn-005482a4)

~~~diff
- 0052540c ["COPY", "tmp:0:8", ["register:4050:8"]]
- 0052540c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 0052540c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 0052540c ["COPY", "register:4048:8", ["tmp:0:8"]]
- 0052540c bytes 4901899a
- 00525418 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:38:8"]]
- 00525418 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00525418 bytes 691e00f9
+ 005482a4 ["COPY", "tmp:0:8", ["register:4050:8"]]
+ 005482a4 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
+ 005482a4 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 005482a4 ["COPY", "register:4048:8", ["tmp:0:8"]]
+ 005482a4 bytes 4901899a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e165081f53cb1ec1a1c4c19dec17c79c"></a>

### [`005254e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/005254e0.md) → [`00548378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548378.md) FUN_00548378

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`004de4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004de/004de4b0.md) [`004dfd64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004df/004dfd64.md) [`00508860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00508/00508860.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`005256ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/005256ac.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 3件 [`00501348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00501/00501348.md) [`00502bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00502/00502bfc.md) [`0052b6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052b/0052b6f8.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00548544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548544.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 50.00% / 新版 46.88%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0052557c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00548414"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00525610"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0052557c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0054847c"
      ]
    ]
  ],
  "added": [
    [
      "00548414",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0054847c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052557c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/005254e0.md#insn-0052557c) · [`00525610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/005254e0.md#insn-00525610)
- 新版 [`00548414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548378.md#insn-00548414)

~~~diff
- 0052557c ["CBRANCH", null, ["local:b18:8", "register:101:1"]]
- 0052557c bytes 40030054
- 00525610 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00525610 ["RETURN", null, ["register:0:8"]]
- 00525610 bytes c0035fd6
+ 00548414 ["CBRANCH", null, ["local:b18:8", "register:101:1"]]
+ 00548414 bytes 40030054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef17d421480a1b798e7d4db77d6a409d"></a>

### [`005256ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/005256ac.md) → [`00548544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548544.md) FUN_00548544

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 8件 [`00506ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00506/00506ee0.md) [`00508860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00508/00508860.md) [`0050947c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/0050947c.md) [`00509f18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/00509f18.md) [`005254e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/005254e0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 8件 [`00529d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00529/00529d78.md) [`0052b6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052b/0052b6f8.md) [`0052c314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c314.md) [`0052cdb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052cdb0.md) [`00548378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548378.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "005256ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005256ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00548544"
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
      "unmatched:005256ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005256b8",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:005256bc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "00548544",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00548550",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "00548554",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0043b738"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005256ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/005256ac.md#insn-005256ac) · [`005256bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/005256ac.md#insn-005256bc)
- 新版 [`00548544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548544.md#insn-00548544)

~~~diff
- 005256ac ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005256ac ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005256ac ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 005256ac ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005256ac bytes fd7bbfa9
- 005256bc ["INT_ADD", "register:40f0:8", ["const:5256bc:8", "const:4:8"]]
- 005256bc ["CALL", null, ["ram:418c38:8"]]
- 005256bc bytes 5fcdfb97
+ 00548544 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00548544 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00548544 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 00548544 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00548544 bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bcaf0d9dad8ff6cb7895ebbba1d1b7c7"></a>

### [`005259e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/005259e4.md) → [`0054887c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/0054887c.md) FUN_0054887c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0052581c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/0052581c.md) · 呼出先 2件 [`005180b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/005180b8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`005486b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/005486b4.md) · 呼出先 2件 [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 6.45% / 新版 12.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00525a44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00525a44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00525a48"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00525a14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00548968"
      ]
    ],
    [
      "unmatched:00525a20",
      "READ",
      [
        "storage",
        "00c1b2e0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00525a6c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00548954"
      ]
    ]
  ],
  "added": [
    [
      "005488ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00548968"
      ]
    ],
    [
      "005488b8",
      "READ",
      [
        "storage",
        "00c9acd0",
        null,
        "pointer"
      ]
    ],
    [
      "00548904",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00548954"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00525a14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/005259e4.md#insn-00525a14) · [`00525a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/005259e4.md#insn-00525a44) · [`00525a48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/005259e4.md#insn-00525a48)

~~~diff
- 00525a14 ["CBRANCH", null, ["local:b14:8", "register:101:1"]]
- 00525a14 bytes e0050054
- 00525a44 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00525a44 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00525a44 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00525a44 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00525a44 bytes 5f7d02a9
- 00525a48 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:30:8"]]
- 00525a48 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00525a48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00525a48 bytes 5f1900f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7dd1124abc62b39d435f420a40e2d0cf"></a>

### [`00525b1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525b1c.md) → [`005489b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/005489b4.md) FUN_005489b4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`005180b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/005180b8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 46.15% / 新版 54.55%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00525b1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00525b1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00525b20"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00525b1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00525b20",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00525b24",
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
      "005489b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "005489b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005489bc",
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

- 旧版 [`00525b1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525b1c.md#insn-00525b1c) · [`00525b20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525b1c.md#insn-00525b20) · [`00525b24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525b1c.md#insn-00525b24)

~~~diff
- 00525b1c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00525b1c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00525b1c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00525b1c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00525b1c bytes fd7bbda9
- 00525b20 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00525b20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00525b20 bytes f50b00f9
- 00525b24 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00525b24 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00525b24 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00525b24 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00525b24 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80967c726c46bdb1c33d637310c5c80d"></a>

### [`00525b94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525b94.md) → [`00548a2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548a2c.md) FUN_00548a2c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0052581c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/0052581c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`005486b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/005486b4.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "00525b94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00525b94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00548a2c"
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
      "unmatched:00525b94",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00525ba0",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00525ba4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "00548a2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00548a38",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "00548a3c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0043b738"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00525b94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525b94.md#insn-00525b94) · [`00525ba4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525b94.md#insn-00525ba4)
- 新版 [`00548a2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548a2c.md#insn-00548a2c)

~~~diff
- 00525b94 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00525b94 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00525b94 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 00525b94 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00525b94 bytes fd7bbfa9
- 00525ba4 ["INT_ADD", "register:40f0:8", ["const:525ba4:8", "const:4:8"]]
- 00525ba4 ["CALL", null, ["ram:418c38:8"]]
- 00525ba4 bytes 25ccfb97
+ 00548a2c ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00548a2c ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00548a2c ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 00548a2c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00548a2c bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d17749bb4b389b3b48e953f890a99490"></a>

### [`00525e44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525e44.md) → [`00548cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548cdc.md) FUN_00548cdc

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`005060a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00506/005060a8.md) [`00525ce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525ce8.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`00528f40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00528/00528f40.md) [`00548b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548b80.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00525e44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00525e44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00548cdc"
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
      "unmatched:00525e44",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00525e50",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00525e54",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "00548cdc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00548ce8",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "00548cec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0043b738"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00525e44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525e44.md#insn-00525e44) · [`00525e54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525e44.md#insn-00525e54)
- 新版 [`00548cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548cdc.md#insn-00548cdc)

~~~diff
- 00525e44 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00525e44 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00525e44 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 00525e44 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00525e44 bytes fd7bbfa9
- 00525e54 ["INT_ADD", "register:40f0:8", ["const:525e54:8", "const:4:8"]]
- 00525e54 ["CALL", null, ["ram:418c38:8"]]
- 00525e54 bytes 79cbfb97
+ 00548cdc ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00548cdc ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00548cdc ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 00548cdc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00548cdc bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f4fc4ee551405537f1860ac0c26c16f"></a>

### [`00525efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525efc.md) → [`00548d94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548d94.md) FUN_00548d94

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`004e0894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e0/004e0894.md) [`00525ed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525ed4.md) · 呼出先 2件 [`0051854c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/0051854c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`0050372c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00503/0050372c.md) [`00548d6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548d6c.md) · 呼出先 2件 [`0053b3e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053b3e4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 78.38% / 新版 78.38%

CFGの説明率　旧版 45.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00525f24"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00525f34"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00548dbc"
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
      "unmatched:00525f1c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0053b3e4"
      ]
    ],
    [
      "unmatched:00525f24",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00548e04"
      ]
    ],
    [
      "unmatched:00525f34",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00548de0"
      ]
    ]
  ],
  "added": [
    [
      "00548db4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0053b3e4"
      ]
    ],
    [
      "00548dbc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00548e04"
      ]
    ],
    [
      "00548dcc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00548de0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00525f1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525efc.md#insn-00525f1c) · [`00525f24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525efc.md#insn-00525f24) · [`00525f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525efc.md#insn-00525f34)

~~~diff
- 00525f1c ["INT_ADD", "register:40f0:8", ["const:525f1c:8", "const:4:8"]]
- 00525f1c ["CALL", null, ["callee:0053b3e4:8"]]
- 00525f1c bytes 8cc9ff97
- 00525f24 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 00525f24 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 00525f24 bytes 540200b4
- 00525f34 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00525f34 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00525f34 bytes a1000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ea451743220d3cd21b27d7a6a4319f2"></a>

### [`00526364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/00526364.md) → [`005491fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/005491fc.md) FUN_005491fc

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

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
      "site": "0052636c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00549204"
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
      "unmatched:0052636c",
      "DATA",
      [
        "storage",
        "00bed8c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00549204",
      "DATA",
      [
        "storage",
        "00c6a480",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052636c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/00526364.md#insn-0052636c) · [`00526364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/00526364.md#insn-00526364)
- 新版 [`00549204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/005491fc.md#insn-00549204) · [`005491fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/005491fc.md#insn-005491fc)

~~~diff
- 0052636c ["COPY", "tmp:0:8", ["register:4008:8"]]
- 0052636c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0052636c bytes 280000f9
+ 00549204 ["COPY", "tmp:0:8", ["register:4008:8"]]
+ 00549204 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00549204 bytes 280000f9
- 00526364 ["COPY", "register:4040:8", ["const:bed000:8"]]
+ 005491fc ["COPY", "register:4040:8", ["const:c6a000:8"]]
- 00526364 bytes 283600f0
+ 005491fc bytes 083900b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35850765b3afa1f82f2b6bc944156530"></a>

### [`0052637c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/0052637c.md) → [`00549214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549214.md) FUN_00549214

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bd0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 82.05% / 新版 82.05%

CFGの説明率　旧版 25.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005263f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00549288"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00526414"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005263f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00549258"
      ]
    ],
    [
      "unmatched:00526408",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0052640c",
      "READ",
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
      "00549288",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00549258"
      ]
    ],
    [
      "005492a0",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005492a4",
      "READ",
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

- 旧版 [`005263f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/0052637c.md#insn-005263f0) · [`00526414`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/0052637c.md#insn-00526414)
- 新版 [`00549288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549214.md#insn-00549288)

~~~diff
- 005263f0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 005263f0 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
- 005263f0 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
- 005263f0 ["CBRANCH", null, ["local:b2:8", "tmp:2:1"]]
- 005263f0 bytes 8cfeff54
- 00526414 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00526414 ["RETURN", null, ["register:0:8"]]
- 00526414 bytes c0035fd6
+ 00549288 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00549288 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
+ 00549288 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
+ 00549288 ["CBRANCH", null, ["local:b2:8", "tmp:2:1"]]
+ 00549288 bytes 8cfeff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9e68ea194971b5e99f4a4db7fe76f5f"></a>

### [`00526448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/00526448.md) → [`005492e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/005492e0.md) FUN_005492e0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00526448"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00526448"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00526460"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00526448",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00526454",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57a90"
      ]
    ],
    [
      "unmatched:00526460",
      "DATA",
      [
        "storage",
        "00bed950",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005492e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005492ec",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57a90"
      ]
    ],
    [
      "005492f8",
      "DATA",
      [
        "storage",
        "00c6a510",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00526448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/00526448.md#insn-00526448) · [`00526454`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/00526448.md#insn-00526454) · [`00526460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/00526448.md#insn-00526460)

~~~diff
- 00526448 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00526448 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00526448 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 00526448 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00526448 bytes fd7bbfa9
- 00526454 ["INT_ADD", "register:40f0:8", ["const:526454:8", "const:4:8"]]
- 00526454 ["CALL", null, ["callee:00c57a90:8"]]
- 00526454 bytes fbd21a94
- 00526460 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00526460 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00526460 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a4caa06fd6179ad038c4cfaf1f82ce9"></a>

### [`0052646c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/0052646c.md) → [`00549304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549304.md) FUN_00549304

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 25.00% / 新版 25.00%

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
      "site": "00526474"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0054930c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00526478"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00526474",
      "DATA",
      [
        "storage",
        "00bed950",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0054930c",
      "DATA",
      [
        "storage",
        "00c6a510",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00526474`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/0052646c.md#insn-00526474) · [`00526478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/0052646c.md#insn-00526478)
- 新版 [`0054930c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549304.md#insn-0054930c)

~~~diff
- 00526474 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00526474 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00526474 bytes 280000f9
- 00526478 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00526478 ["RETURN", null, ["register:0:8"]]
- 00526478 bytes c0035fd6
+ 0054930c ["COPY", "tmp:0:8", ["register:4008:8"]]
+ 0054930c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 0054930c bytes 280000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f53ce1d0e850b0328930715d3fc02193"></a>

### [`005265bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/005265bc.md) → [`00549454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549454.md) FUN_00549454

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005265c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005265d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00549460"
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
      "unmatched:005265c0",
      "READ",
      [
        "storage",
        "00c1b340",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:005265c8",
      "DATA",
      [
        "storage",
        "00bed9d0",
        null,
        "undefined1[88]"
      ]
    ]
  ],
  "added": [
    [
      "00549458",
      "READ",
      [
        "storage",
        "00c9ad30",
        null,
        "pointer"
      ]
    ],
    [
      "00549460",
      "DATA",
      [
        "storage",
        "00c6a590",
        null,
        "undefined1[88]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005265c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/005265bc.md#insn-005265c8) · [`005265d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/005265bc.md#insn-005265d0) · [`005265d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/005265bc.md#insn-005265d4)

~~~diff
- 005265c8 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 005265c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 005265c8 bytes 280000f9
- 005265d0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:8:8"]]
- 005265d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 005265d0 bytes 2080803c
- 005265d4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 005265d4 ["RETURN", null, ["register:0:8"]]
- 005265d4 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-794e5a5c2debc801539ede4259b836ce"></a>

### [`005265e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/005265e0.md) → [`00549478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549478.md) FUN_00549478

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 33.33% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005265e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/005265e0.md#insn-005265e0) · [`005265e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/005265e0.md#insn-005265e4) · [`005265e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/005265e0.md#insn-005265e8)

~~~diff
- 005265e0 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
- 005265e0 ["LOAD", "tmp:1:8", ["const:1b1:8", "tmp:0:8"]]
- 005265e0 ["INT_ADD", "tmp:2:8", ["tmp:0:8", "const:8:8"]]
- 005265e0 ["LOAD", "tmp:3:8", ["const:1b1:8", "tmp:2:8"]]
- 005265e0 bytes 03a440a9
- 005265e4 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 005265e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005265e4 bytes 280040f9
- 005265e8 ["COPY", "register:4008:8", ["register:4010:8"]]
- 005265e8 bytes e10302aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8289e699cacd4d4497227bef47f6afc"></a>

### [`005267f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/005267f0.md) → [`00549688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549688.md) FUN_00549688

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`004e50d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e50d0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00507f68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/00507f68.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 66.96% / 新版 66.96%

CFGの説明率　旧版 17.95% / 新版 15.05%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005267f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00526868"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0052687c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005267f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0054983c"
      ]
    ],
    [
      "unmatched:0052680c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "005496b4"
      ]
    ],
    [
      "005496c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00526810"
      ]
    ]
  ],
  "added": [
    [
      "005496a4",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "005496b4"
      ]
    ],
    [
      "005496b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0054983c"
      ]
    ],
    [
      "005496c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005496a8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005267f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/005267f0.md#insn-005267f8) · [`00526868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/005267f0.md#insn-00526868) · [`0052687c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/005267f0.md#insn-0052687c)

~~~diff
- 005267f8 ["INT_EQUAL", "tmp:0:1", ["register:4068:8", "const:0:8"]]
- 005267f8 ["CBRANCH", null, ["local:b47:8", "tmp:0:1"]]
- 005267f8 bytes 6d0d00b4
- 00526868 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00526868 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00526868 ["CBRANCH", null, ["local:b9:8", "tmp:1:1"]]
- 00526868 bytes 29ffff54
- 0052687c ["INT_NOTEQUAL", "tmp:0:1", ["register:4068:8", "const:0:8"]]
- 0052687c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 0052687c bytes 0dfdffb5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b9ad629ade0c99f8f364a243d83bf75"></a>

### [`00526ef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/00526ef8.md) → [`00549d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549d90.md) FUN_00549d90

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`0051d764`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d764.md)
- 新版 呼出元 0件  · 呼出先 1件 [`005405fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005405fc.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 86.96% / 新版 86.96%

CFGの説明率　旧版 57.14% / 新版 44.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00526f24"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00549dbc"
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
      "unmatched:00526f24",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00549ddc"
      ]
    ]
  ],
  "added": [
    [
      "00549dbc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00549ddc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00526f24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/00526ef8.md#insn-00526f24) · [`00526f1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/00526ef8.md#insn-00526f1c)
- 新版 [`00549dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549d90.md#insn-00549dbc)

~~~diff
- 00526f24 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 00526f24 bytes 00010054
+ 00549dbc ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
+ 00549dbc bytes 00010054
- 00526f1c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00526f1c ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
- 00526f1c bytes 350140f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-950687cc08ac59b3006fc0cdc168f88d"></a>

### [`005271dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/005271dc.md) → [`0054a074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a074.md) FUN_0054a074

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00526f54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00526/00526f54.md) · 呼出先 1件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md)
- 新版 呼出元 1件 [`00549dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00549/00549dec.md) · 呼出先 1件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 84.75% / 新版 84.75%

CFGの説明率　旧版 46.43% / 新版 46.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005272b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0054a150"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00527218"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00527218",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0054a118"
      ]
    ],
    [
      "unmatched:00527230",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0054a0a8"
      ]
    ],
    [
      "unmatched:00527268",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0054a0e4"
      ]
    ]
  ],
  "added": [
    [
      "0054a0b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0054a118"
      ]
    ],
    [
      "0054a0c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0054a0a8"
      ]
    ],
    [
      "0054a100",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0054a0e4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00527218`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/005271dc.md#insn-00527218) · [`00527230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/005271dc.md#insn-00527230) · [`00527268`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/005271dc.md#insn-00527268)

~~~diff
- 00527218 ["INT_EQUAL", "tmp:0:1", ["register:4068:8", "const:0:8"]]
- 00527218 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 00527218 bytes 4d0300b4
- 00527230 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00527230 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00527230 bytes 03ffff54
- 00527268 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00527268 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00527268 ["CBRANCH", null, ["local:b8:8", "tmp:1:1"]]
- 00527268 bytes 29ffff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb5c9a88a73d0f4082856b5d40ac004b"></a>

### [`0052773c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/0052773c.md) → [`0054a5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a5d4.md) FUN_0054a5d4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`00509ac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00509/00509ac0.md) [`0050a3ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050a/0050a3ac.md) [`0052761c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/0052761c.md) [`00b26b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b26/00b26b28.md) [`00b284c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b28/00b284c4.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 9件 [`0052c958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052c/0052c958.md) [`0052d244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052d244.md) [`0054a4b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a4b4.md) [`00b6eebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6e/00b6eebc.md) [`00b82890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b82/00b82890.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 69.23% / 新版 69.23%

CFGの説明率　旧版 50.00% / 新版 41.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0052773c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0052773c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00527740"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0052773c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00527740",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00527744",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0054a5d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "0054a5d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "0054a5dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052773c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/0052773c.md#insn-0052773c) · [`00527740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/0052773c.md#insn-00527740) · [`00527744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/0052773c.md#insn-00527744)

~~~diff
- 0052773c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0052773c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0052773c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 0052773c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0052773c bytes fd7bbba9
- 00527740 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00527740 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00527740 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00527740 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00527740 bytes fa6701a9
- 00527744 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00527744 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00527744 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00527744 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00527744 bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7526b79546a4abc5804ce61f01f06ce9"></a>

### [`005278b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/005278b4.md) → [`0054a74c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a74c.md) FUN_0054a74c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00527554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/00527554.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0054a3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a3ec.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 78.57% / 新版 78.57%

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
      "site": "005278b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005278b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005278b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005278b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:005278b8",
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
      "0054a74c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0054a750",
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

- 旧版 [`005278b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/005278b4.md#insn-005278b4) · [`005278b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/005278b4.md#insn-005278b8)
- 新版 [`0054a74c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a74c.md#insn-0054a74c)

~~~diff
- 005278b4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005278b4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005278b4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 005278b4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005278b4 bytes fd7bbea9
- 005278b8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 005278b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 005278b8 bytes f30b00f9
+ 0054a74c ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 0054a74c ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 0054a74c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 0054a74c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 0054a74c bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fb79299b73fb10291db892bf3312d7f"></a>

### [`00527a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/00527a44.md) → [`0054a8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054a8dc.md) FUN_0054a8dc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`004eef84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ee/004eef84.md) · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00511e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00511/00511e1c.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 22.22% / 新版 22.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00527a90"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00527aa0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0054a928"
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
      "unmatched:00527a6c",
      "DATA",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00527a90",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0054a93c"
      ]
    ],
    [
      "unmatched:00527aa0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0054a970"
      ]
    ]
  ],
  "added": [
    [
      "0054a904",
      "DATA",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "0054a928",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0054a93c"
      ]
    ],
    [
      "0054a938",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0054a970"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00527a70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/00527a44.md#insn-00527a70) · [`00527a90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/00527a44.md#insn-00527a90) · [`00527aa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/00527a44.md#insn-00527aa0)

~~~diff
- 00527a70 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00527a70 ["RETURN", null, ["register:0:8"]]
- 00527a70 bytes c0035fd6
- 00527a90 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00527a90 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00527a90 bytes a1000054
- 00527aa0 ["CBRANCH", null, ["local:b11:8", "register:101:1"]]
- 00527aa0 bytes c0010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f35b3794f74c70630d6df69c6d763871"></a>

### [`00527fd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/00527fd4.md) → [`0054ae6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054ae6c.md) FUN_0054ae6c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`004f11e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f11e0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00514078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/00514078.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 94.64% / 新版 94.64%

CFGの説明率　旧版 87.50% / 新版 87.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0052804c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00528138"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0054aee4"
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
      "unmatched:0052804c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0054aec8"
      ]
    ],
    [
      "0054afac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00528128"
      ]
    ],
    [
      "unmatched:00528138",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0054afb4"
      ]
    ]
  ],
  "added": [
    [
      "0054aee4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0054aec8"
      ]
    ],
    [
      "0054afac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0054afc0"
      ]
    ],
    [
      "0054afd0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0054afb4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052804c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/00527fd4.md#insn-0052804c) · [`00528138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/00527fd4.md#insn-00528138)
- 新版 [`0054aee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054a/0054ae6c.md#insn-0054aee4)

~~~diff
- 0052804c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 0052804c ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 0052804c ["CBRANCH", null, ["local:b7:8", "tmp:1:1"]]
- 0052804c bytes 29ffff54
- 00528138 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00528138 ["CBRANCH", null, ["local:b31:8", "tmp:0:1"]]
- 00528138 bytes 23ffff54
+ 0054aee4 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 0054aee4 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
+ 0054aee4 ["CBRANCH", null, ["local:b7:8", "tmp:1:1"]]
+ 0054aee4 bytes 29ffff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-360ee2d766d04050be38ab3c6dccc360"></a>

### [`005282c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/005282c4.md) → [`0054b15c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b15c.md) FUN_0054b15c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`004e5c34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e5/004e5c34.md) · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00512c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512c94.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00508acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00508/00508acc.md) · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00535b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 85.19% / 新版 85.19%

CFGの説明率　旧版 69.23% / 新版 56.25%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005282f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00528300"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0054b188"
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
      "unmatched:005282ec",
      "READ",
      [
        "storage",
        "00c1af50",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00528300",
      "DATA",
      [
        "storage",
        "00be92c8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "unmatched:00528308",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0054b1cc"
      ]
    ]
  ],
  "added": [
    [
      "0054b184",
      "READ",
      [
        "storage",
        "00c9a940",
        null,
        "pointer"
      ]
    ],
    [
      "0054b198",
      "DATA",
      [
        "storage",
        "00c65e88",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0054b1a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0054b1cc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005282f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/005282c4.md#insn-005282f0) · [`00528300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/005282c4.md#insn-00528300) · [`00528308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/005282c4.md#insn-00528308)

~~~diff
- 005282f0 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:10:8"]]
- 005282f0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 005282f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 005282f0 bytes 1f0800f9
- 00528300 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00528300 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00528300 bytes 080000f9
- 00528308 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00528308 bytes 60010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5cec229a794b63b5e62ca4f95d25afa4"></a>

### [`0052839c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/0052839c.md) → [`0054b234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b234.md) FUN_0054b234

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`004e4f2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004e4/004e4f2c.md) [`004f1650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f1/004f1650.md) · 呼出先 0件 
- 新版 呼出元 2件 [`00507dc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00507/00507dc4.md) [`005144e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00514/005144e8.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.43% / 新版 96.43%

CFGの説明率　旧版 80.28% / 新版 76.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005283c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00528414"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00528498"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005283c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0054b3e8"
      ]
    ],
    [
      "unmatched:00528414",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0054b290"
      ]
    ],
    [
      "unmatched:00528498",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0054b364"
      ]
    ]
  ],
  "added": [
    [
      "0054b25c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0054b3e8"
      ]
    ],
    [
      "0054b2ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0054b290"
      ]
    ],
    [
      "0054b330",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0054b364"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005283c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/0052839c.md#insn-005283c4) · [`00528414`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/0052839c.md#insn-00528414) · [`00528498`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/0052839c.md#insn-00528498)

~~~diff
- 005283c4 ["INT_EQUAL", "tmp:0:1", ["register:4068:8", "const:0:8"]]
- 005283c4 ["CBRANCH", null, ["local:b40:8", "tmp:0:1"]]
- 005283c4 bytes 6d0c00b4
- 00528414 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00528414 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00528414 ["CBRANCH", null, ["local:b7:8", "tmp:1:1"]]
- 00528414 bytes 29ffff54
- 00528498 ["CBRANCH", null, ["local:b28:8", "register:101:1"]]
- 00528498 bytes a0010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6bc5db792010c9b5f814db2c9535f101"></a>

### [`00528cb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/00528cb4.md) → [`0054bb4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054bb4c.md) FUN_0054bb4c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00528a6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/00528a6c.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0054b904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054b904.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.43% / 新版 96.43%

CFGの説明率　旧版 50.00% / 新版 54.55%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00528d08"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0054bba0"
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
      "unmatched:00528d08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0054bbb0"
      ]
    ]
  ],
  "added": [
    [
      "0054bba0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0054bbb0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00528d08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/00528cb4.md#insn-00528d08) · [`00528cd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/00528cb4.md#insn-00528cd8)
- 新版 [`0054bba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054bb4c.md#insn-0054bba0) · [`0054bb70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054bb4c.md#insn-0054bb70)

~~~diff
- 00528d08 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00528d08 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00528d08 bytes 800000b4
+ 0054bba0 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 0054bba0 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 0054bba0 bytes 800000b4
- 00528cd8 ["INT_ADD", "register:40f0:8", ["const:528cd8:8", "const:4:8"]]
- 00528cd8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0054bb70 ["INT_ADD", "register:40f0:8", ["const:54bb70:8", "const:4:8"]]
+ 0054bb70 ["CALL", null, ["callee:00c57ab0:8"]]
- 00528cd8 bytes e2c81a94
+ 0054bb70 bytes d02f1c94
~~~


<a id="compare-c53a3c49323cfa544579aef031fd6623"></a>

### [`00528ef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/00528ef0.md) → [`0054bd88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054bd88.md) FUN_0054bd88

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00528d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/00528d24.md) · 呼出先 5件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00512c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512c94.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`0054bbbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054b/0054bbbc.md) · 呼出先 5件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00535b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 branch_condition_or_target, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 73.44% / 新版 73.44%

CFGの説明率　旧版 21.05% / 新版 21.05%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00528ef0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00528ef0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00528ef4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00528ef0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00528ef4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00528ef8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0054bd88",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "0054bd8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "0054bd90",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00528ef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/00528ef0.md#insn-00528ef0) · [`00528ef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/00528ef0.md#insn-00528ef4) · [`00528ef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00528/00528ef0.md#insn-00528ef8)

~~~diff
- 00528ef0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00528ef0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00528ef0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00528ef0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00528ef0 bytes fd7bbba9
- 00528ef4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00528ef4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 00528ef4 bytes f90b00f9
- 00528ef8 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00528ef8 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00528ef8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00528ef8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00528ef8 bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b4b0d96110144e248432e43f6212ee2"></a>

### [`00529214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/00529214.md) → [`0054c0ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c0ac.md) FUN_0054c0ac

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`004f4030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f4/004f4030.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0052934c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/0052934c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00516ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00516/00516ec8.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0054c1e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054c1e4.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 85.90% / 新版 85.90%

CFGの説明率　旧版 46.43% / 新版 44.83%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 5件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005292f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0054c190"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0052925c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005292b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0054c1ac"
      ]
    ],
    [
      "0054c17c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:005292f4"
      ]
    ],
    [
      "unmatched:005292f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0054c1a8"
      ]
    ]
  ],
  "added": [
    [
      "0054c14c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0054c1ac"
      ]
    ],
    [
      "0054c17c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "0054c18c"
      ]
    ],
    [
      "0054c188",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0054c1a8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052925c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/00529214.md#insn-0052925c) · [`00529268`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/00529214.md#insn-00529268) · [`005292b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/00529214.md#insn-005292b4)

~~~diff
- 0052925c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0052925c ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 0052925c ["COPY", "tmp:2:8", ["register:4050:8"]]
- 0052925c ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 0052925c bytes 4881889a
- 00529268 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00529268 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00529268 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00529268 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00529268 bytes 1631899a
- 005292b4 ["CBRANCH", null, ["local:b17:8", "register:101:1"]]
- 005292b4 bytes 00030054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-557608d8eec0919ba608b4c7278c28fd"></a>

### [`00529d48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/00529d48.md) → [`0054cbe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054cbe0.md) FUN_0054cbe0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`004f8c10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f8/004f8c10.md) [`004f9190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f9/004f9190.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`0051baa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051b/0051baa8.md) [`0051c028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051c/0051c028.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

変更の種類 call, call_count, comparison, comparison_count, constant, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 40.00% / 新版 40.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00529d58"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "0054cbf0"
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
      "unmatched:00529d54",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00529d58",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "0054cbec",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "0054cbf0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0043b738"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00529d58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/00529d48.md#insn-00529d58) · [`00529d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/00529d48.md#insn-00529d50)
- 新版 [`0054cbf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054cbe0.md#insn-0054cbf0)

~~~diff
- 00529d58 ["INT_ADD", "register:40f0:8", ["const:529d58:8", "const:4:8"]]
- 00529d58 ["CALL", null, ["ram:418c38:8"]]
- 00529d58 bytes b8bbfb97
+ 0054cbf0 ["INT_ADD", "register:40f0:8", ["const:54cbf0:8", "const:4:8"]]
+ 0054cbf0 ["CALL", null, ["ram:43b738:8"]]
+ 0054cbf0 bytes d2bafb97
- 00529d50 ["COPY", "register:4000:8", ["const:2a7000:8"]]
- 00529d50 bytes e0ebffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44e367b8f260d026e1b57cfe643fa321"></a>

### [`0052a1c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052a1c8.md) → [`0054d060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d060.md) FUN_0054d060

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0052a0f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052a0f8.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0054cf90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054cf90.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 68.42% / 新版 68.42%

CFGの説明率　旧版 22.22% / 新版 22.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0052a1c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0052a1c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0052a1cc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0052a1c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0052a1cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0052a1dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0054d0a0"
      ]
    ]
  ],
  "added": [
    [
      "0054d060",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0054d064",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0054d074",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0054d0a0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052a1c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052a1c8.md#insn-0052a1c8) · [`0052a1cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052a1c8.md#insn-0052a1cc) · [`0052a1d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052a1c8.md#insn-0052a1d8)

~~~diff
- 0052a1c8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0052a1c8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0052a1c8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0052a1c8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0052a1c8 bytes fd7bbea9
- 0052a1cc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0052a1cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 0052a1cc bytes f30b00f9
- 0052a1d8 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0052a1d8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 0052a1d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 0052a1d8 bytes 1f0000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ba023a06de4eef5e46bb8a275fe2e94"></a>

### [`005537fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005537fc.md) → [`00576694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576694.md) FUN_00576694

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0052db28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052db28.md) · 呼出先 0件 
- 新版 呼出元 1件 [`005509c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/005509c0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 11.11% / 新版 11.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0057669c",
      "READ",
      [
        "storage",
        "00c1ad80",
        null,
        "pointer"
      ]
    ],
    [
      "005766a0",
      "READ",
      [
        "storage",
        "00c1ad88",
        null,
        "pointer"
      ]
    ],
    [
      "005766a4",
      "READ",
      [
        "storage",
        "00c2659c",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0057669c",
      "READ",
      [
        "storage",
        "00c9a770",
        null,
        "pointer"
      ]
    ],
    [
      "005766a0",
      "READ",
      [
        "storage",
        "00c9a778",
        null,
        "pointer"
      ]
    ],
    [
      "005766a4",
      "READ",
      [
        "storage",
        "00ca605c",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005537fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005537fc.md#insn-005537fc) · [`00553800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005537fc.md#insn-00553800) · [`00553804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005537fc.md#insn-00553804)
- 新版 [`0057669c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576694.md#insn-0057669c)

~~~diff
- 005537fc ["COPY", "register:4040:8", ["const:c1a000:8"]]
- 005537fc bytes 283600f0
- 00553800 ["COPY", "register:4048:8", ["const:c1a000:8"]]
- 00553800 bytes 293600f0
- 00553804 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d80:8"]]
- 00553804 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0057669c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:770:8"]]
+ 0057669c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00553804 bytes 08c146f9
+ 0057669c bytes 08b943f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c50350f2981ac17d2475341beaa4d10"></a>

### [`00562188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/00562188.md) → [`00585020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/00585020.md) FUN_00585020

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 7件 [`0056233c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/0056233c.md) [`00564d7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00564/00564d7c.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 7件 [`005851d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/005851d4.md) [`00587c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00587/00587c14.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.94% / 新版 96.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00585080",
      "PARAM",
      [
        "storage",
        "00befa10",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00585084",
      "PARAM",
      [
        "storage",
        "00befa20",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00585080",
      "PARAM",
      [
        "storage",
        "00c6c5d0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00585084",
      "PARAM",
      [
        "storage",
        "00c6c5e0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005621bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/00562188.md#insn-005621bc) · [`005621c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/00562188.md#insn-005621c0) · [`005621c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/00562188.md#insn-005621c8)
- 新版 [`00585054`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/00585020.md#insn-00585054) · [`00585058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/00585020.md#insn-00585058)

~~~diff
- 005621bc ["COPY", "register:40a0:8", ["const:bef000:8"]]
+ 00585054 ["COPY", "register:40a0:8", ["const:c6c000:8"]]
- 005621bc bytes 743400b0
+ 00585054 bytes 343700f0
- 005621c0 ["COPY", "tmp:0:8", ["const:a10:8"]]
- 005621c0 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 005621c0 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 005621c0 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 00585058 ["COPY", "tmp:0:8", ["const:5d0:8"]]
+ 00585058 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 00585058 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 00585058 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 005621c0 bytes 94422891
+ 00585058 bytes 94421791
- 005621c8 ["COPY", "register:40a8:8", ["const:bef000:8"]]
- 005621c8 bytes 753400b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-611d371f74a88d0e37847c7dffd4a591"></a>

### [`0056b688`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056b/0056b688.md) → [`0058e520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058e520.md) FUN_0058e520

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056626c.md) [`00566448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566448.md) [`00566968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566968.md)
- 新版 呼出元 0件  · 呼出先 12件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md) [`00589800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589800.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.04% / 新版 96.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0058e59c",
      "READ",
      [
        "storage",
        "00299e49",
        null,
        "string"
      ]
    ],
    [
      "0058e59c",
      "READ",
      [
        "storage",
        "00299e59",
        null,
        "string"
      ]
    ],
    [
      "0058e5a0",
      "READ",
      [
        "storage",
        "002b0d60",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0058e59c",
      "READ",
      [
        "storage",
        "002a9d22",
        null,
        "string"
      ]
    ],
    [
      "0058e59c",
      "READ",
      [
        "storage",
        "002a9d32",
        null,
        "string"
      ]
    ],
    [
      "0058e5a0",
      "READ",
      [
        "storage",
        "002c2360",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0056b6bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056b/0056b688.md#insn-0056b6bc) · [`0056b6c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056b/0056b688.md#insn-0056b6c4) · [`0056b6f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056b/0056b688.md#insn-0056b6f4)
- 新版 [`0058e554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058e520.md#insn-0058e554) · [`0058e55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058e520.md#insn-0058e55c) · [`0058e58c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058e/0058e520.md#insn-0058e58c)

~~~diff
- 0056b6bc ["INT_ADD", "register:40f0:8", ["const:56b6bc:8", "const:4:8"]]
- 0056b6bc ["CALL", null, ["callee:00589800:8"]]
+ 0058e554 ["INT_ADD", "register:40f0:8", ["const:58e554:8", "const:4:8"]]
+ 0058e554 ["CALL", null, ["callee:00589800:8"]]
- 0056b6bc bytes abecff97
+ 0058e554 bytes abecff97
- 0056b6c4 ["INT_ADD", "register:40f0:8", ["const:56b6c4:8", "const:4:8"]]
- 0056b6c4 ["CALL", null, ["callee:00588e2c:8"]]
+ 0058e55c ["INT_ADD", "register:40f0:8", ["const:58e55c:8", "const:4:8"]]
+ 0058e55c ["CALL", null, ["callee:00588e2c:8"]]
- 0056b6c4 bytes 34eaff97
+ 0058e55c bytes 34eaff97
- 0056b6f4 ["INT_ADD", "register:40f0:8", ["const:56b6f4:8", "const:4:8"]]
- 0056b6f4 ["CALL", null, ["callee:00c57a90:8"]]
+ 0058e58c ["INT_ADD", "register:40f0:8", ["const:58e58c:8", "const:4:8"]]
+ 0058e58c ["CALL", null, ["callee:00c57a90:8"]]
- 0056b6f4 bytes 53be1994
+ 0058e58c bytes 41251b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a2914d920e1eb5223b724a3cf8738d9"></a>

### [`00572998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572998.md) → [`00595830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595830.md) FUN_00595830

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`005727b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/005727b4.md) [`00572b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572b04.md) [`00572e44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572e44.md) · 呼出先 0件 
- 新版 呼出元 3件 [`0059564c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/0059564c.md) [`0059599c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/0059599c.md) [`00595cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595cdc.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.70% / 新版 96.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00595860",
      "DATA",
      [
        "storage",
        "002c189d",
        "switchD_005729d8::switchdataD_002c189d",
        "byte"
      ]
    ]
  ],
  "added": [
    [
      "00595860",
      "DATA",
      [
        "storage",
        "002d2fdd",
        "switchD_00595870::switchdataD_002d2fdd",
        "byte"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005729bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572998.md#insn-005729bc) · [`005729c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572998.md#insn-005729c0) · [`005729c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572998.md#insn-005729c4)
- 新版 [`00595854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595830.md#insn-00595854) · [`00595858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595830.md#insn-00595858)

~~~diff
- 005729bc ["COPY", "register:4058:8", ["const:2c1000:8"]]
+ 00595854 ["COPY", "register:4058:8", ["const:2d2000:8"]]
- 005729bc bytes 6beafff0
+ 00595854 bytes ebe9ffb0
- 005729c0 ["COPY", "tmp:0:8", ["const:89d:8"]]
- 005729c0 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
- 005729c0 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
- 005729c0 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
+ 00595858 ["COPY", "tmp:0:8", ["const:fdd:8"]]
+ 00595858 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
+ 00595858 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
+ 00595858 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
- 005729c0 bytes 6b752291
+ 00595858 bytes 6b753f91
- 005729c4 ["COPY", "register:4068:8", ["const:5729dc:8"]]
- 005729c4 bytes cd000010
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1a5e7794835c6e04606fd4f9a55cc69"></a>

### [`0057710c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/0057710c.md) → [`005999e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/005999e4.md) FUN_005999e4

採用 · 移動量 `+0x228d8` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00577138"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00599a10"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00577138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/0057710c.md#insn-00577138) · [`0057711c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/0057710c.md#insn-0057711c)
- 新版 [`00599a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/005999e4.md#insn-00599a10) · [`005999f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/005999e4.md#insn-005999f4)

~~~diff
- 00577138 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00577138 ["RETURN", null, ["register:0:8"]]
- 00577138 bytes c0035fd6
+ 00599a10 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00599a10 ["RETURN", null, ["register:0:8"]]
+ 00599a10 bytes c0035fd6
- 0057711c ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 0057711c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 005999f4 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
+ 005999f4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 0057711c bytes b30000b4
+ 005999f4 bytes b30000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c210ef8540a51f735fc936661867ec3a"></a>

### [`00577358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577358.md) → [`00599c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599c30.md) FUN_00599c30

採用 · 移動量 `+0x228d8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00577df0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577df0.md) [`00578500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/00578500.md) · 呼出先 4件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 2件 [`0059a6c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a6c8.md) [`0059add8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059add8.md) · 呼出先 4件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 63.16% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005773e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00599cb8"
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
      "unmatched:005773e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00599cd4"
      ]
    ]
  ],
  "added": [
    [
      "00599cb8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00599cd4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005773e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577358.md#insn-005773e0) · [`00577390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577358.md#insn-00577390)
- 新版 [`00599cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599c30.md#insn-00599cb8) · [`00599c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599c30.md#insn-00599c68)

~~~diff
- 005773e0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 005773e0 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 005773e0 bytes e00000b5
+ 00599cb8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00599cb8 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00599cb8 bytes e00000b5
- 00577390 ["COPY", "register:0:8", ["register:4048:8"]]
- 00577390 ["INT_ADD", "register:40f0:8", ["const:577390:8", "const:4:8"]]
- 00577390 ["CALLIND", null, ["register:0:8"]]
+ 00599c68 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00599c68 ["INT_ADD", "register:40f0:8", ["const:599c68:8", "const:4:8"]]
+ 00599c68 ["CALLIND", null, ["register:0:8"]]
- 00577390 bytes 20013fd6
+ 00599c68 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-266a9b9c51d45085bbdc09c54c3d5e85"></a>

### [`00577620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577620.md) → [`00599ef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599ef8.md) FUN_00599ef8

採用 · 移動量 `+0x228d8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`0057753c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/0057753c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00599e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599e14.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00577620"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00577620"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00577624"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00577620",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00577624",
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
      "00599ef8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00599efc",
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

- 旧版 [`00577620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577620.md#insn-00577620) · [`00577624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577620.md#insn-00577624)
- 新版 [`00599ef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599ef8.md#insn-00599ef8)

~~~diff
- 00577620 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00577620 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00577620 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00577620 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00577620 bytes fd7bbea9
- 00577624 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00577624 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00577624 bytes f30b00f9
+ 00599ef8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00599ef8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00599ef8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00599ef8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00599ef8 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fda60ed1d3620cc748425bf486295f7f"></a>

### [`00577818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577818.md) → [`0059a0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a0f0.md) FUN_0059a0f0

採用 · 移動量 `+0x228d8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 30.00% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00577834"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0059a10c"
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
      "unmatched:00577834",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0059a11c"
      ]
    ]
  ],
  "added": [
    [
      "0059a10c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0059a11c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00577834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577818.md#insn-00577834) · [`0057782c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577818.md#insn-0057782c)
- 新版 [`0059a10c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a0f0.md#insn-0059a10c)

~~~diff
- 00577834 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
- 00577834 bytes 80000054
+ 0059a10c ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
+ 0059a10c bytes 80000054
- 0057782c ["COPY", "tmp:0:8", ["const:10:8"]]
- 0057782c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0057782c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0057782c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0057782c bytes 69420091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6c78c28472e50da0b75f136cd7fa434"></a>

### [`005778b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/005778b0.md) → [`0059a188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a188.md) FUN_0059a188

採用 · 移動量 `+0x228d8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005760b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/005760b0.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00598afc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598afc.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 97.75% / 新版 97.75%

CFGの説明率　旧版 86.67% / 新版 81.25%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00577990"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "0059a268"
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
      "unmatched:00577990",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "0059a268",
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

- 旧版 [`00577990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/005778b0.md#insn-00577990) · [`005778d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/005778b0.md#insn-005778d4)
- 新版 [`0059a268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a188.md#insn-0059a268) · [`0059a1ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a188.md#insn-0059a1ac)

~~~diff
- 00577990 ["COPY", "register:0:8", ["register:4040:8"]]
- 00577990 ["INT_ADD", "register:40f0:8", ["const:577990:8", "const:4:8"]]
- 00577990 ["CALLIND", null, ["register:0:8"]]
- 00577990 bytes 00013fd6
+ 0059a268 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0059a268 ["INT_ADD", "register:40f0:8", ["const:59a268:8", "const:4:8"]]
+ 0059a268 ["CALLIND", null, ["register:0:8"]]
+ 0059a268 bytes 00013fd6
- 005778d4 ["CBRANCH", null, ["local:b9:8", "register:101:1"]]
+ 0059a1ac ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
- 005778d4 bytes c0080054
+ 0059a1ac bytes c0080054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b98cb253cbce3356ca62a3e132383e4c"></a>

### [`00577a18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577a18.md) → [`0059a2f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a2f0.md) FUN_0059a2f0

採用 · 移動量 `+0x228d8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00576268`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/00576268.md) · 呼出先 1件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00598cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00598/00598cb4.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 97.75% / 新版 97.75%

CFGの説明率　旧版 86.67% / 新版 76.47%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00577ac4"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "0059a39c"
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
      "unmatched:00577ac4",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "0059a39c",
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

- 旧版 [`00577ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577a18.md#insn-00577ac4) · [`00577a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577a18.md#insn-00577a3c)
- 新版 [`0059a39c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a2f0.md#insn-0059a39c) · [`0059a314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a2f0.md#insn-0059a314)

~~~diff
- 00577ac4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00577ac4 ["INT_ADD", "register:40f0:8", ["const:577ac4:8", "const:4:8"]]
- 00577ac4 ["CALLIND", null, ["register:0:8"]]
- 00577ac4 bytes 00013fd6
+ 0059a39c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0059a39c ["INT_ADD", "register:40f0:8", ["const:59a39c:8", "const:4:8"]]
+ 0059a39c ["CALLIND", null, ["register:0:8"]]
+ 0059a39c bytes 00013fd6
- 00577a3c ["CBRANCH", null, ["local:b9:8", "register:101:1"]]
+ 0059a314 ["CBRANCH", null, ["local:b11:8", "register:101:1"]]
- 00577a3c bytes c0080054
+ 0059a314 bytes c0080054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b62042581be98a570134115e670e0e1e"></a>

### [`005783a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/005783a4.md) → [`0059ac7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059ac7c.md) FUN_0059ac7c

採用 · 移動量 `+0x228d8` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 81.82% / 新版 81.82%

CFGの説明率　旧版 55.56% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005783c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005783d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005783d8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005783c0",
      "DATA",
      [
        "storage",
        "00bf0940",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:005783dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0059acc4"
      ]
    ]
  ],
  "added": [
    [
      "0059ac98",
      "DATA",
      [
        "storage",
        "00c6d500",
        null,
        "undefined *"
      ]
    ],
    [
      "0059acb4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0059acc4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005783c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/005783a4.md#insn-005783c0) · [`005783d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/005783a4.md#insn-005783d4) · [`005783d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00578/005783a4.md#insn-005783d8)

~~~diff
- 005783c0 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 005783c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 005783c0 bytes 280000f9
- 005783d4 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 005783d4 ["INT_ADD", "register:40a0:8", ["register:40a0:8", "const:8:8"]]
- 005783d4 ["STORE", null, ["const:1b1:8", "register:40a0:8", "tmp:0:8"]]
- 005783d4 bytes 898e00f8
- 005783d8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:10:8"]]
- 005783d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 005783d8 bytes 280800f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

