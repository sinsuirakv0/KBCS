# v16.0.2 → v16.0.3 · 命令位置の検査未完了 (14)

[一覧の目次](README.md)

<a id="compare-9dc9ca35d7fdfcb102b1e4f450ea6bdb"></a>

### [`00bae5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00bae5f4.md) → [`00baf5e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baf/00baf5e8.md) FUN_00baf5e8

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bad494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bad/00bad494.md) · 呼出先 4件 [`00bade60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bad/00bade60.md) [`00bae10c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00bae10c.md) [`00bae314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00bae314.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00bae488`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bae/00bae488.md) · 呼出先 4件 [`00baee54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bae/00baee54.md) [`00baf100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baf/00baf100.md) [`00baf308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baf/00baf308.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.97% / 新版 97.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00baf62c",
      "DATA",
      [
        "storage",
        "0030e252",
        "switchD_00bae644::switchdataD_0030e252",
        "byte"
      ]
    ]
  ],
  "added": [
    [
      "00baf62c",
      "DATA",
      [
        "storage",
        "0030e292",
        "switchD_00baf638::switchdataD_0030e292",
        "byte"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bae630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00bae5f4.md#insn-00bae630) · [`00bae634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00bae5f4.md#insn-00bae634) · [`00bae6ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00bae5f4.md#insn-00bae6ac)
- 新版 [`00baf624`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baf/00baf5e8.md#insn-00baf624) · [`00baf6a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baf/00baf5e8.md#insn-00baf6a0)

~~~diff
- 00bae630 ["COPY", "tmp:0:8", ["const:252:8"]]
- 00bae630 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00bae630 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00bae630 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00baf624 ["COPY", "tmp:0:8", ["const:292:8"]]
+ 00baf624 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00baf624 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00baf624 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00bae630 bytes 29490991
+ 00baf624 bytes 29490a91
- 00bae634 ["COPY", "register:4050:8", ["const:bae648:8"]]
- 00bae634 bytes aa000010
- 00bae6ac ["INT_ADD", "register:40f0:8", ["const:bae6ac:8", "const:4:8"]]
- 00bae6ac ["CALL", null, ["callee:00c590f0:8"]]
+ 00baf6a0 ["INT_ADD", "register:40f0:8", ["const:baf6a0:8", "const:4:8"]]
+ 00baf6a0 ["CALL", null, ["callee:00c590f0:8"]]
- 00bae6ac bytes 9da60294
+ 00baf6a0 bytes 94a60294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1aad86994332fc4a652873c33ff0dd2b"></a>

### [`00baeec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00baeec4.md) → [`00bafeb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baf/00bafeb8.md) _ZNSt6__ndk16__sortIRPFbPKN11flatbuffers8FieldDefES4_EPPS2_EEvT0_SA_T_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5cec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cec0.md) · 呼出先 5件 [`00baf560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00baf560.md) [`00c5ccc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ccc0.md) [`00c5ce80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ce80.md) [`00c5cec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5cec0.md) [`00c5d180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d180.md)
- 新版 呼出元 1件 [`00c5de90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5de90.md) · 呼出先 5件 [`00bb0554`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb0/00bb0554.md) [`00c5dc90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dc90.md) [`00c5de50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5de50.md) [`00c5de90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5de90.md) [`00c5e150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e150.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.77% / 新版 98.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bb0254",
      "DATA",
      [
        "storage",
        "0030e258",
        "switchD_00baf268::switchdataD_0030e258",
        "byte"
      ]
    ]
  ],
  "added": [
    [
      "00bb0254",
      "DATA",
      [
        "storage",
        "0030e298",
        "switchD_00bb025c::switchdataD_0030e298",
        "byte"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00baef68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00baeec4.md#insn-00baef68) · [`00baef7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00baeec4.md#insn-00baef7c) · [`00baef98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bae/00baeec4.md#insn-00baef98)
- 新版 [`00baff5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baf/00bafeb8.md#insn-00baff5c) · [`00baff70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baf/00bafeb8.md#insn-00baff70) · [`00baff8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00baf/00bafeb8.md#insn-00baff8c)

~~~diff
- 00baef68 ["INT_ADD", "register:40f0:8", ["const:baef68:8", "const:4:8"]]
- 00baef68 ["CALL", null, ["callee:00bb0554:8"]]
+ 00baff5c ["INT_ADD", "register:40f0:8", ["const:baff5c:8", "const:4:8"]]
+ 00baff5c ["CALL", null, ["callee:00bb0554:8"]]
- 00baef68 bytes 7e010094
+ 00baff5c bytes 7e010094
- 00baef7c ["COPY", "register:0:8", ["register:4040:8"]]
- 00baef7c ["INT_ADD", "register:40f0:8", ["const:baef7c:8", "const:4:8"]]
- 00baef7c ["CALLIND", null, ["register:0:8"]]
+ 00baff70 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00baff70 ["INT_ADD", "register:40f0:8", ["const:baff70:8", "const:4:8"]]
+ 00baff70 ["CALLIND", null, ["register:0:8"]]
- 00baef7c bytes 00013fd6
+ 00baff70 bytes 00013fd6
- 00baef98 ["COPY", "register:0:8", ["register:4040:8"]]
- 00baef98 ["INT_ADD", "register:40f0:8", ["const:baef98:8", "const:4:8"]]
- 00baef98 ["CALLIND", null, ["register:0:8"]]
+ 00baff8c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00baff8c ["INT_ADD", "register:40f0:8", ["const:baff8c:8", "const:4:8"]]
+ 00baff8c ["CALLIND", null, ["register:0:8"]]
- 00baef98 bytes 00013fd6
+ 00baff8c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8d93ea737ad763b6e7b1ba4b3e17557"></a>

### [`00baf7c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00baf7c4.md) → [`00bb07b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb0/00bb07b8.md) _ZNSt6__ndk127__insertion_sort_incompleteIRPFbPKN11flatbuffers8FieldDefES4_EPPS2_EEbT0_SA_T_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5ce80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ce80.md) · 呼出先 2件 [`00baf560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00baf560.md) [`00c5d180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d180.md)
- 新版 呼出元 1件 [`00c5de50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5de50.md) · 呼出先 2件 [`00bb0554`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb0/00bb0554.md) [`00c5e150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e150.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.67% / 新版 97.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bb07f8",
      "DATA",
      [
        "storage",
        "0030e25e",
        "switchD_00baf810::switchdataD_0030e25e",
        "byte"
      ]
    ]
  ],
  "added": [
    [
      "00bb07f8",
      "DATA",
      [
        "storage",
        "0030e29e",
        "switchD_00bb0804::switchdataD_0030e29e",
        "byte"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00baf7fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00baf7c4.md#insn-00baf7fc) · [`00baf800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00baf7c4.md#insn-00baf800) · [`00baf820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00baf7c4.md#insn-00baf820)
- 新版 [`00bb07f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb0/00bb07b8.md#insn-00bb07f0) · [`00bb0814`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb0/00bb07b8.md#insn-00bb0814)

~~~diff
- 00baf7fc ["COPY", "tmp:0:8", ["const:25e:8"]]
- 00baf7fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00baf7fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00baf7fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00bb07f0 ["COPY", "tmp:0:8", ["const:29e:8"]]
+ 00bb07f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00bb07f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00bb07f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00baf7fc bytes 29790991
+ 00bb07f0 bytes 29790a91
- 00baf800 ["COPY", "register:4050:8", ["const:baf814:8"]]
- 00baf800 bytes aa000010
- 00baf820 ["COPY", "register:0:8", ["register:4040:8"]]
- 00baf820 ["INT_ADD", "register:40f0:8", ["const:baf820:8", "const:4:8"]]
- 00baf820 ["CALLIND", null, ["register:0:8"]]
+ 00bb0814 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb0814 ["INT_ADD", "register:40f0:8", ["const:bb0814:8", "const:4:8"]]
+ 00bb0814 ["CALLIND", null, ["register:0:8"]]
- 00baf820 bytes 00013fd6
+ 00bb0814 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b62b9ca25dc63b74fddf1caee820537"></a>

### [`00bb0b2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb0b2c.md) → [`00bb1b20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb1/00bb1b20.md) _ZNSt6__ndk16__sortIRPFbPKN11flatbuffers9StructDefES4_EPPS2_EEvT0_SA_T_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5ced0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ced0.md) · 呼出先 5件 [`00bb11c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb11c8.md) [`00c5ccd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ccd0.md) [`00c5ce90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ce90.md) [`00c5ced0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ced0.md) [`00c5d190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d190.md)
- 新版 呼出元 1件 [`00c5dea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dea0.md) · 呼出先 5件 [`00bb21bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb2/00bb21bc.md) [`00c5dca0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dca0.md) [`00c5de60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5de60.md) [`00c5dea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dea0.md) [`00c5e160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e160.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.77% / 新版 98.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bb1ebc",
      "DATA",
      [
        "storage",
        "0030e264",
        "switchD_00bb0ed0::switchdataD_0030e264",
        "byte"
      ]
    ]
  ],
  "added": [
    [
      "00bb1ebc",
      "DATA",
      [
        "storage",
        "0030e2a4",
        "switchD_00bb1ec4::switchdataD_0030e2a4",
        "byte"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb0bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb0b2c.md#insn-00bb0bd0) · [`00bb0be4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb0b2c.md#insn-00bb0be4) · [`00bb0c00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb0/00bb0b2c.md#insn-00bb0c00)
- 新版 [`00bb1bc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb1/00bb1b20.md#insn-00bb1bc4) · [`00bb1bd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb1/00bb1b20.md#insn-00bb1bd8) · [`00bb1bf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb1/00bb1b20.md#insn-00bb1bf4)

~~~diff
- 00bb0bd0 ["INT_ADD", "register:40f0:8", ["const:bb0bd0:8", "const:4:8"]]
- 00bb0bd0 ["CALL", null, ["callee:00bb21bc:8"]]
+ 00bb1bc4 ["INT_ADD", "register:40f0:8", ["const:bb1bc4:8", "const:4:8"]]
+ 00bb1bc4 ["CALL", null, ["callee:00bb21bc:8"]]
- 00bb0bd0 bytes 7e010094
+ 00bb1bc4 bytes 7e010094
- 00bb0be4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb0be4 ["INT_ADD", "register:40f0:8", ["const:bb0be4:8", "const:4:8"]]
- 00bb0be4 ["CALLIND", null, ["register:0:8"]]
+ 00bb1bd8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb1bd8 ["INT_ADD", "register:40f0:8", ["const:bb1bd8:8", "const:4:8"]]
+ 00bb1bd8 ["CALLIND", null, ["register:0:8"]]
- 00bb0be4 bytes 00013fd6
+ 00bb1bd8 bytes 00013fd6
- 00bb0c00 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb0c00 ["INT_ADD", "register:40f0:8", ["const:bb0c00:8", "const:4:8"]]
- 00bb0c00 ["CALLIND", null, ["register:0:8"]]
+ 00bb1bf4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb1bf4 ["INT_ADD", "register:40f0:8", ["const:bb1bf4:8", "const:4:8"]]
+ 00bb1bf4 ["CALLIND", null, ["register:0:8"]]
- 00bb0c00 bytes 00013fd6
+ 00bb1bf4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-591a86371808cdb2f4a4e57e33d48beb"></a>

### [`00bb142c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb142c.md) → [`00bb2420`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb2/00bb2420.md) _ZNSt6__ndk127__insertion_sort_incompleteIRPFbPKN11flatbuffers9StructDefES4_EPPS2_EEbT0_SA_T_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5ce90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ce90.md) · 呼出先 2件 [`00bb11c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb11c8.md) [`00c5d190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d190.md)
- 新版 呼出元 1件 [`00c5de60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5de60.md) · 呼出先 2件 [`00bb21bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb2/00bb21bc.md) [`00c5e160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e160.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.67% / 新版 97.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bb2460",
      "DATA",
      [
        "storage",
        "0030e26a",
        "switchD_00bb1478::switchdataD_0030e26a",
        "byte"
      ]
    ]
  ],
  "added": [
    [
      "00bb2460",
      "DATA",
      [
        "storage",
        "0030e2aa",
        "switchD_00bb246c::switchdataD_0030e2aa",
        "byte"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb1464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb142c.md#insn-00bb1464) · [`00bb1468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb142c.md#insn-00bb1468) · [`00bb1488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb142c.md#insn-00bb1488)
- 新版 [`00bb2458`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb2/00bb2420.md#insn-00bb2458) · [`00bb247c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb2/00bb2420.md#insn-00bb247c)

~~~diff
- 00bb1464 ["COPY", "tmp:0:8", ["const:26a:8"]]
- 00bb1464 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00bb1464 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00bb1464 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00bb2458 ["COPY", "tmp:0:8", ["const:2aa:8"]]
+ 00bb2458 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00bb2458 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00bb2458 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00bb1464 bytes 29a90991
+ 00bb2458 bytes 29a90a91
- 00bb1468 ["COPY", "register:4050:8", ["const:bb147c:8"]]
- 00bb1468 bytes aa000010
- 00bb1488 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb1488 ["INT_ADD", "register:40f0:8", ["const:bb1488:8", "const:4:8"]]
- 00bb1488 ["CALLIND", null, ["register:0:8"]]
+ 00bb247c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb247c ["INT_ADD", "register:40f0:8", ["const:bb247c:8", "const:4:8"]]
+ 00bb247c ["CALLIND", null, ["register:0:8"]]
- 00bb1488 bytes 00013fd6
+ 00bb247c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d09aa1da31d27093cfcd3e646e331fa"></a>

### [`00bb1810`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb1810.md) → [`00bb2804`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb2/00bb2804.md) _ZNSt6__ndk16__sortIRPFbPKN11flatbuffers7EnumDefES4_EPPS2_EEvT0_SA_T_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5ceb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ceb0.md) · 呼出先 5件 [`00bb1eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb1eac.md) [`00c5ccb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ccb0.md) [`00c5ce70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ce70.md) [`00c5ceb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ceb0.md) [`00c5d170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d170.md)
- 新版 呼出元 1件 [`00c5de80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5de80.md) · 呼出先 5件 [`00bb2ea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb2/00bb2ea0.md) [`00c5dc80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5dc80.md) [`00c5de40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5de40.md) [`00c5de80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5de80.md) [`00c5e140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e140.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.77% / 新版 98.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bb2ba0",
      "DATA",
      [
        "storage",
        "0030e270",
        "switchD_00bb1bb4::switchdataD_0030e270",
        "byte"
      ]
    ]
  ],
  "added": [
    [
      "00bb2ba0",
      "DATA",
      [
        "storage",
        "0030e2b0",
        "switchD_00bb2ba8::switchdataD_0030e2b0",
        "byte"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb18b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb1810.md#insn-00bb18b4) · [`00bb18c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb1810.md#insn-00bb18c8) · [`00bb18e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb1810.md#insn-00bb18e4)
- 新版 [`00bb28a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb2/00bb2804.md#insn-00bb28a8) · [`00bb28bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb2/00bb2804.md#insn-00bb28bc) · [`00bb28d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb2/00bb2804.md#insn-00bb28d8)

~~~diff
- 00bb18b4 ["INT_ADD", "register:40f0:8", ["const:bb18b4:8", "const:4:8"]]
- 00bb18b4 ["CALL", null, ["callee:00bb2ea0:8"]]
+ 00bb28a8 ["INT_ADD", "register:40f0:8", ["const:bb28a8:8", "const:4:8"]]
+ 00bb28a8 ["CALL", null, ["callee:00bb2ea0:8"]]
- 00bb18b4 bytes 7e010094
+ 00bb28a8 bytes 7e010094
- 00bb18c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb18c8 ["INT_ADD", "register:40f0:8", ["const:bb18c8:8", "const:4:8"]]
- 00bb18c8 ["CALLIND", null, ["register:0:8"]]
+ 00bb28bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb28bc ["INT_ADD", "register:40f0:8", ["const:bb28bc:8", "const:4:8"]]
+ 00bb28bc ["CALLIND", null, ["register:0:8"]]
- 00bb18c8 bytes 00013fd6
+ 00bb28bc bytes 00013fd6
- 00bb18e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb18e4 ["INT_ADD", "register:40f0:8", ["const:bb18e4:8", "const:4:8"]]
- 00bb18e4 ["CALLIND", null, ["register:0:8"]]
+ 00bb28d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb28d8 ["INT_ADD", "register:40f0:8", ["const:bb28d8:8", "const:4:8"]]
+ 00bb28d8 ["CALLIND", null, ["register:0:8"]]
- 00bb18e4 bytes 00013fd6
+ 00bb28d8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a519ed7df2a8dcc236b45e320e2a0e46"></a>

### [`00bb2110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb2/00bb2110.md) → [`00bb3104`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb3/00bb3104.md) _ZNSt6__ndk127__insertion_sort_incompleteIRPFbPKN11flatbuffers7EnumDefES4_EPPS2_EEbT0_SA_T_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5ce70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5c/00c5ce70.md) · 呼出先 2件 [`00bb1eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb1/00bb1eac.md) [`00c5d170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d170.md)
- 新版 呼出元 1件 [`00c5de40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5d/00c5de40.md) · 呼出先 2件 [`00bb2ea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb2/00bb2ea0.md) [`00c5e140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e140.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.67% / 新版 97.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bb3144",
      "DATA",
      [
        "storage",
        "0030e276",
        "switchD_00bb215c::switchdataD_0030e276",
        "byte"
      ]
    ]
  ],
  "added": [
    [
      "00bb3144",
      "DATA",
      [
        "storage",
        "0030e2b6",
        "switchD_00bb3150::switchdataD_0030e2b6",
        "byte"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb2148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb2/00bb2110.md#insn-00bb2148) · [`00bb214c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb2/00bb2110.md#insn-00bb214c) · [`00bb216c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb2/00bb2110.md#insn-00bb216c)
- 新版 [`00bb313c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb3/00bb3104.md#insn-00bb313c) · [`00bb3160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb3/00bb3104.md#insn-00bb3160)

~~~diff
- 00bb2148 ["COPY", "tmp:0:8", ["const:276:8"]]
- 00bb2148 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00bb2148 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00bb2148 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00bb313c ["COPY", "tmp:0:8", ["const:2b6:8"]]
+ 00bb313c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00bb313c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00bb313c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00bb2148 bytes 29d90991
+ 00bb313c bytes 29d90a91
- 00bb214c ["COPY", "register:4050:8", ["const:bb2160:8"]]
- 00bb214c bytes aa000010
- 00bb216c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bb216c ["INT_ADD", "register:40f0:8", ["const:bb216c:8", "const:4:8"]]
- 00bb216c ["CALLIND", null, ["register:0:8"]]
+ 00bb3160 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bb3160 ["INT_ADD", "register:40f0:8", ["const:bb3160:8", "const:4:8"]]
+ 00bb3160 ["CALLIND", null, ["register:0:8"]]
- 00bb216c bytes 00013fd6
+ 00bb3160 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eac03306133501248c2ac51a4c2a330a"></a>

### [`00bb56a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb56a0.md) → [`00bb6694`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb6694.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEE4openEPKcj

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c58fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58fe0.md) · 呼出先 3件 [`00c5a0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0d0.md) [`00c5a130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a130.md) [`00c5a160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a160.md)
- 新版 呼出元 1件 [`00c59fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59fb0.md) · 呼出先 3件 [`00c5b0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b0a0.md) [`00c5b100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b100.md) [`00c5b130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b130.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 77.03% / 新版 77.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bb66e0",
      "DATA",
      [
        "storage",
        "0030e596",
        "switchD_00bb56fc::switchdataD_0030e596",
        "byte"
      ]
    ],
    [
      "00bb6778",
      "PARAM",
      [
        "storage",
        "002b3705",
        null,
        null
      ]
    ],
    [
      "00bb6778",
      "PARAM",
      [
        "storage",
        "002a1b87",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bb66e0",
      "DATA",
      [
        "storage",
        "0030e5d6",
        "switchD_00bb66f0::switchdataD_0030e5d6",
        "byte"
      ]
    ],
    [
      "00bb6778",
      "PARAM",
      [
        "storage",
        "002b374f",
        null,
        null
      ]
    ],
    [
      "00bb6778",
      "PARAM",
      [
        "storage",
        "002a1bc7",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb56e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb56a0.md#insn-00bb56e4) · [`00bb56e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb56a0.md#insn-00bb56e8) · [`00bb56f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb5/00bb56a0.md#insn-00bb56f4)
- 新版 [`00bb66d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb6/00bb6694.md#insn-00bb66d8)

~~~diff
- 00bb56e4 ["COPY", "tmp:0:8", ["const:596:8"]]
- 00bb56e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00bb56e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00bb56e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00bb66d8 ["COPY", "tmp:0:8", ["const:5d6:8"]]
+ 00bb66d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00bb66d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00bb66d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00bb56e4 bytes 29591691
+ 00bb66d8 bytes 29591791
- 00bb56e8 ["COPY", "register:4050:8", ["const:bb56b8:8"]]
- 00bb56e8 bytes 8afeff10
- 00bb56f4 ["COPY", "register:4040:8", ["const:2bc000:8"]]
- 00bb56f4 bytes 28b8fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c77030d31ce046d8dcd81d26e0025908"></a>

### [`00bbd7d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd7d0.md) → [`00bbe7c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe7c4.md) _ZNK8firebase9messaging8internal13MessageReader14ReadFromBufferERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5d620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d620.md) · 呼出先 4件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5ad70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad70.md) [`00c5d5a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d5a0.md) [`00c5d610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d610.md)
- 新版 呼出元 1件 [`00c5e5f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e5f0.md) · 呼出先 4件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5bd40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd40.md) [`00c5e570`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e570.md) [`00c5e5e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e5e0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 92.42% / 新版 92.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bbe814",
      "READ",
      [
        "storage",
        "002c3db0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbe8e8",
      "DATA",
      [
        "storage",
        "0030e8e0",
        "switchD_00bbd8fc::switchdataD_0030e8e0",
        "byte"
      ]
    ],
    [
      "00bbe914",
      "PARAM",
      [
        "storage",
        "0030e8e8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bbe814",
      "READ",
      [
        "storage",
        "002c3e00",
        null,
        "undefined8"
      ]
    ],
    [
      "00bbe8e8",
      "DATA",
      [
        "storage",
        "0030e920",
        "switchD_00bbe8f0::switchdataD_0030e920",
        "byte"
      ]
    ],
    [
      "00bbe914",
      "PARAM",
      [
        "storage",
        "0030e928",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbd820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd7d0.md#insn-00bbd820) · [`00bbd840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd7d0.md#insn-00bbd840) · [`00bbd84c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbd/00bbd7d0.md#insn-00bbd84c)
- 新版 [`00bbe814`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe7c4.md#insn-00bbe814) · [`00bbe834`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe7c4.md#insn-00bbe834) · [`00bbe840`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbe/00bbe7c4.md#insn-00bbe840)

~~~diff
- 00bbd820 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:db0:8"]]
- 00bbd820 ["LOAD", "register:5100:8", ["const:1b1:8", "tmp:0:8"]]
- 00bbd820 ["COPY", "register:5108:8", ["const:0:8"]]
- 00bbd820 ["COPY", "register:5110:8", ["const:0:8"]]
+ 00bbe814 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:e00:8"]]
+ 00bbe814 ["LOAD", "register:5100:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bbe814 ["COPY", "register:5108:8", ["const:0:8"]]
+ 00bbe814 ["COPY", "register:5110:8", ["const:0:8"]]
- 00bbd820 bytes 48d946fd
+ 00bbe814 bytes 480147fd
- 00bbd840 ["COPY", "tmp:0:8", ["const:8e8:8"]]
- 00bbd840 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 00bbd840 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 00bbd840 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 00bbe834 ["COPY", "tmp:0:8", ["const:928:8"]]
+ 00bbe834 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 00bbe834 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 00bbe834 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 00bbd840 bytes 94a22391
+ 00bbe834 bytes 94a22491
- 00bbd84c ["COPY", "tmp:0:8", ["const:736:8"]]
- 00bbd84c ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 00bbd84c ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 00bbd84c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 00bbe840 ["COPY", "tmp:0:8", ["const:80d:8"]]
+ 00bbe840 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 00bbe840 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 00bbe840 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 00bbd84c bytes b5da1c91
+ 00bbe840 bytes b5362091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-955fbef8b7d91e1e95b79c9b3b3b8a34"></a>

### [`00bbecb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbe/00bbecb8.md) → [`00bbfcac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbf/00bbfcac.md) _ZNK3com6google8firebase9messaging3cpp15SerializedEvent6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5d5a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d5a0.md) · 呼出先 4件 [`00c5d5b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d5b0.md) [`00c5d5d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d5d0.md) [`00c5d5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d5e0.md) [`00c5d5f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d5f0.md)
- 新版 呼出元 1件 [`00c5e570`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e570.md) · 呼出先 4件 [`00c5e580`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e580.md) [`00c5e5a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e5a0.md) [`00c5e5b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e5b0.md) [`00c5e5c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e5c0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bbfe40",
      "DATA",
      [
        "storage",
        "0030e8e4",
        "switchD_00bbee54::switchdataD_0030e8e4",
        "byte"
      ]
    ]
  ],
  "added": [
    [
      "00bbfe40",
      "DATA",
      [
        "storage",
        "0030e924",
        "switchD_00bbfe48::switchdataD_0030e924",
        "byte"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbee44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbe/00bbecb8.md#insn-00bbee44) · [`00bbee48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbe/00bbecb8.md#insn-00bbee48) · [`00bbee64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbe/00bbecb8.md#insn-00bbee64)
- 新版 [`00bbfe38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbf/00bbfcac.md#insn-00bbfe38) · [`00bbfe58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bbf/00bbfcac.md#insn-00bbfe58)

~~~diff
- 00bbee44 ["COPY", "tmp:0:8", ["const:8e4:8"]]
- 00bbee44 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00bbee44 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00bbee44 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00bbfe38 ["COPY", "tmp:0:8", ["const:924:8"]]
+ 00bbfe38 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00bbfe38 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00bbfe38 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00bbee44 bytes 4a912391
+ 00bbfe38 bytes 4a912491
- 00bbee48 ["COPY", "register:4058:8", ["const:bbee58:8"]]
- 00bbee48 bytes 8b000010
- 00bbee64 ["INT_ADD", "register:40f0:8", ["const:bbee64:8", "const:4:8"]]
- 00bbee64 ["CALL", null, ["callee:00c5e580:8"]]
+ 00bbfe58 ["INT_ADD", "register:40f0:8", ["const:bbfe58:8", "const:4:8"]]
+ 00bbfe58 ["CALL", null, ["callee:00c5e580:8"]]
- 00bbee64 bytes d3790294
+ 00bbfe58 bytes ca790294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e02f63dbe94b01f30cab09e252c2fb1"></a>

### [`00c30b0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c30/00c30b0c.md) → [`00c31b00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c31/00c31b00.md) _ZNSt6__ndk118__time_get_storageIcE4initERKNS_5ctypeIcEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5edc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5edc0.md) · 呼出先 4件 [`00bf2034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2034.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e730.md) [`00c5eda0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5eda0.md)
- 新版 呼出元 1件 [`00c5fd90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fd90.md) · 呼出先 4件 [`00bf3028`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3028.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5f700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f700.md) [`00c5fd70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5fd70.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 94.94% / 新版 94.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c31b5c",
      "PARAM",
      [
        "storage",
        "002b2832",
        null,
        null
      ]
    ],
    [
      "00c31b84",
      "PARAM",
      [
        "storage",
        "002ac4c1",
        null,
        null
      ]
    ],
    [
      "00c31bd0",
      "PARAM",
      [
        "storage",
        "002af6eb",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c31b5c",
      "PARAM",
      [
        "storage",
        "002b287c",
        null,
        null
      ]
    ],
    [
      "00c31b84",
      "PARAM",
      [
        "storage",
        "002ac58e",
        null,
        null
      ]
    ],
    [
      "00c31bd0",
      "PARAM",
      [
        "storage",
        "002af7c2",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c30b3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c30/00c30b0c.md#insn-00c30b3c) · [`00c30b44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c30/00c30b0c.md#insn-00c30b44) · [`00c30b48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c30/00c30b0c.md#insn-00c30b48)
- 新版 [`00c31b30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c31/00c31b00.md#insn-00c31b30) · [`00c31b3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c31/00c31b00.md#insn-00c31b3c)

~~~diff
- 00c30b3c ["COPY", "tmp:0:8", ["const:832:8"]]
- 00c30b3c ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 00c30b3c ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 00c30b3c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 00c31b30 ["COPY", "tmp:0:8", ["const:87c:8"]]
+ 00c31b30 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 00c31b30 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 00c31b30 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 00c30b3c bytes b5ca2091
+ 00c31b30 bytes b5f22191
- 00c30b44 ["COPY", "register:40b8:8", ["const:2ac000:8"]]
- 00c30b44 bytes f7b3ff90
- 00c30b48 ["COPY", "tmp:0:8", ["const:4c1:8"]]
- 00c30b48 ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
- 00c30b48 ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
- 00c30b48 ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
+ 00c31b3c ["COPY", "tmp:0:8", ["const:58e:8"]]
+ 00c31b3c ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
+ 00c31b3c ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
+ 00c31b3c ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
- 00c30b48 bytes f7061391
+ 00c31b3c bytes f73a1691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-347332357a211cf77e82b12d80dc7b1d"></a>

### [`00c4717c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c4717c.md) → [`00c48170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c48/00c48170.md) FUN_00c48170

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c481e8",
      "PARAM",
      [
        "storage",
        "002ae69e",
        null,
        null
      ]
    ],
    [
      "00c481e8",
      "PARAM",
      [
        "storage",
        "0029ede0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c481e8",
      "PARAM",
      [
        "storage",
        "002ae76b",
        null,
        null
      ]
    ],
    [
      "00c481e8",
      "PARAM",
      [
        "storage",
        "0029ee20",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c471cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c4717c.md#insn-00c471cc) · [`00c471e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c4717c.md#insn-00c471e0) · [`00c471e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c4717c.md#insn-00c471e8)
- 新版 [`00c481c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c48/00c48170.md#insn-00c481c0) · [`00c481d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c48/00c48170.md#insn-00c481d4)

~~~diff
- 00c471cc ["INT_ADD", "register:40f0:8", ["const:c471cc:8", "const:4:8"]]
- 00c471cc ["CALL", null, ["callee:00c5b140:8"]]
+ 00c481c0 ["INT_ADD", "register:40f0:8", ["const:c481c0:8", "const:4:8"]]
+ 00c481c0 ["CALL", null, ["callee:00c5b140:8"]]
- 00c471cc bytes e94b0094
+ 00c481c0 bytes e04b0094
- 00c471e0 ["COPY", "tmp:0:8", ["const:69e:8"]]
- 00c471e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c471e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c471e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c481d4 ["COPY", "tmp:0:8", ["const:76b:8"]]
+ 00c481d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c481d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c481d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c471e0 bytes 29791a91
+ 00c481d4 bytes 29ad1d91
- 00c471e8 ["COPY", "register:4050:8", ["const:29e000:8"]]
- 00c471e8 bytes aab2fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd92a66358da6e9bb06027320910a1e3"></a>

### [`00c518d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c518d8.md) → [`00c528cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c528cc.md) FUN_00c528cc

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c51c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c51c10.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c52c04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c52c04.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5b140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b140.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.92% / 新版 96.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c52a98",
      "PARAM",
      [
        "storage",
        "002a9a11",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c52a98",
      "PARAM",
      [
        "storage",
        "002a9ade",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c51904`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c518d8.md#insn-00c51904) · [`00c51924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c518d8.md#insn-00c51924) · [`00c5194c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c51/00c518d8.md#insn-00c5194c)
- 新版 [`00c528f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c528cc.md#insn-00c528f8) · [`00c52918`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c528cc.md#insn-00c52918) · [`00c52940`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c52/00c528cc.md#insn-00c52940)

~~~diff
- 00c51904 ["INT_ADD", "register:40f0:8", ["const:c51904:8", "const:4:8"]]
- 00c51904 ["CALL", null, ["callee:00c52c04:8"]]
+ 00c528f8 ["INT_ADD", "register:40f0:8", ["const:c528f8:8", "const:4:8"]]
+ 00c528f8 ["CALL", null, ["callee:00c52c04:8"]]
- 00c51904 bytes c3000094
+ 00c528f8 bytes c3000094
- 00c51924 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c51924 ["INT_ADD", "register:40f0:8", ["const:c51924:8", "const:4:8"]]
- 00c51924 ["CALLIND", null, ["register:0:8"]]
+ 00c52918 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c52918 ["INT_ADD", "register:40f0:8", ["const:c52918:8", "const:4:8"]]
+ 00c52918 ["CALLIND", null, ["register:0:8"]]
- 00c51924 bytes 00013fd6
+ 00c52918 bytes 00013fd6
- 00c5194c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c5194c ["INT_ADD", "register:40f0:8", ["const:c5194c:8", "const:4:8"]]
- 00c5194c ["CALLIND", null, ["register:0:8"]]
+ 00c52940 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c52940 ["INT_ADD", "register:40f0:8", ["const:c52940:8", "const:4:8"]]
+ 00c52940 ["CALLIND", null, ["register:0:8"]]
- 00c5194c bytes 00013fd6
+ 00c52940 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

