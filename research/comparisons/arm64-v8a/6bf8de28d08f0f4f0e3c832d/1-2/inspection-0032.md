# v16.0.1 → v16.0.2 · 要調査の変更候補 (32)

[一覧の目次](README.md)

<a id="compare-a6354f1beffa8d2dfbc04111c65fc347"></a>

### [`009e6334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e6334.md) → [`009e6388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6388.md) FUN_009e6388

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009e5b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e5/009e5b60.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`009e5bb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e5/009e5bb4.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009e63a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e6334.md#insn-009e63a4) · [`009e63dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e6334.md#insn-009e63dc) · [`009e648c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e6334.md#insn-009e648c)
- 新版 [`009e63f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6388.md#insn-009e63f8) · [`009e6430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6388.md#insn-009e6430) · [`009e64e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6388.md#insn-009e64e0)

~~~diff
- 009e63a4 ["INT_ADD", "register:40f0:8", ["const:9e63a4:8", "const:4:8"]]
- 009e63a4 ["CALL", null, ["callee:00c58010:8"]]
+ 009e63f8 ["INT_ADD", "register:40f0:8", ["const:9e63f8:8", "const:4:8"]]
+ 009e63f8 ["CALL", null, ["callee:00c58010:8"]]
- 009e63a4 bytes e7c60994
+ 009e63f8 bytes 06c70994
- 009e63dc ["INT_ADD", "register:40f0:8", ["const:9e63dc:8", "const:4:8"]]
- 009e63dc ["CALL", null, ["callee:00c57f60:8"]]
+ 009e6430 ["INT_ADD", "register:40f0:8", ["const:9e6430:8", "const:4:8"]]
+ 009e6430 ["CALL", null, ["callee:00c57f60:8"]]
- 009e63dc bytes adc60994
+ 009e6430 bytes ccc60994
- 009e648c ["INT_ADD", "register:40f0:8", ["const:9e648c:8", "const:4:8"]]
- 009e648c ["CALL", null, ["callee:00c57f80:8"]]
+ 009e64e0 ["INT_ADD", "register:40f0:8", ["const:9e64e0:8", "const:4:8"]]
+ 009e64e0 ["CALL", null, ["callee:00c57f80:8"]]
- 009e648c bytes 89c60994
+ 009e64e0 bytes a8c60994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-432fa778ff617415a1365af6925f4112"></a>

### [`009e6540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e6540.md) → [`009e6594`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6594.md) FUN_009e6594

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009e037c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e037c.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`009e6774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e6774.md) [`009e6788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e6788.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`009e03d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e0/009e03d0.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`009e67c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e67c8.md) [`009e67dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e67dc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009e65f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e6540.md#insn-009e65f8) · [`009e6640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e6540.md#insn-009e6640) · [`009e665c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e6540.md#insn-009e665c)
- 新版 [`009e664c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6594.md#insn-009e664c) · [`009e6694`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6594.md#insn-009e6694) · [`009e66b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6594.md#insn-009e66b0)

~~~diff
- 009e65f8 ["INT_ADD", "register:40f0:8", ["const:9e65f8:8", "const:4:8"]]
- 009e65f8 ["CALL", null, ["callee:00c57f60:8"]]
+ 009e664c ["INT_ADD", "register:40f0:8", ["const:9e664c:8", "const:4:8"]]
+ 009e664c ["CALL", null, ["callee:00c57f60:8"]]
- 009e65f8 bytes 26c60994
+ 009e664c bytes 45c60994
- 009e6640 ["INT_ADD", "register:40f0:8", ["const:9e6640:8", "const:4:8"]]
- 009e6640 ["CALL", null, ["callee:009e67dc:8"]]
+ 009e6694 ["INT_ADD", "register:40f0:8", ["const:9e6694:8", "const:4:8"]]
+ 009e6694 ["CALL", null, ["callee:009e67dc:8"]]
- 009e6640 bytes 52000094
+ 009e6694 bytes 52000094
- 009e665c ["INT_ADD", "register:40f0:8", ["const:9e665c:8", "const:4:8"]]
- 009e665c ["CALL", null, ["callee:00c57f80:8"]]
+ 009e66b0 ["INT_ADD", "register:40f0:8", ["const:9e66b0:8", "const:4:8"]]
+ 009e66b0 ["CALL", null, ["callee:00c57f80:8"]]
- 009e665c bytes 15c60994
+ 009e66b0 bytes 34c60994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1eab96405584ff7f92eceb91851637dc"></a>

### [`009e66e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e66e8.md) → [`009e673c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e673c.md) FUN_009e673c

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009e6724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e66e8.md#insn-009e6724) · [`009e6734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e66e8.md#insn-009e6734) · [`009e6744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e66e8.md#insn-009e6744)
- 新版 [`009e6778`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e673c.md#insn-009e6778) · [`009e6788`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e673c.md#insn-009e6788) · [`009e6798`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e673c.md#insn-009e6798)

~~~diff
- 009e6724 ["INT_ADD", "register:40f0:8", ["const:9e6724:8", "const:4:8"]]
- 009e6724 ["CALL", null, ["callee:00c57f80:8"]]
+ 009e6778 ["INT_ADD", "register:40f0:8", ["const:9e6778:8", "const:4:8"]]
+ 009e6778 ["CALL", null, ["callee:00c57f80:8"]]
- 009e6724 bytes e3c50994
+ 009e6778 bytes 02c60994
- 009e6734 ["INT_ADD", "register:40f0:8", ["const:9e6734:8", "const:4:8"]]
- 009e6734 ["CALL", null, ["callee:00c57f80:8"]]
+ 009e6788 ["INT_ADD", "register:40f0:8", ["const:9e6788:8", "const:4:8"]]
+ 009e6788 ["CALL", null, ["callee:00c57f80:8"]]
- 009e6734 bytes dfc50994
+ 009e6788 bytes fec50994
- 009e6744 ["INT_ADD", "register:40f0:8", ["const:9e6744:8", "const:4:8"]]
- 009e6744 ["CALL", null, ["callee:00c57f80:8"]]
+ 009e6798 ["INT_ADD", "register:40f0:8", ["const:9e6798:8", "const:4:8"]]
+ 009e6798 ["CALL", null, ["callee:00c57f80:8"]]
- 009e6744 bytes dbc50994
+ 009e6798 bytes fac50994
~~~


<a id="compare-76d5a4c44679b65460a538df098828ad"></a>

### [`009e6788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e6788.md) → [`009e67dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e67dc.md) FUN_009e67dc

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009e6540`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e6540.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`009e6594`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6594.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009e682c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e6788.md#insn-009e682c) · [`009e683c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e6788.md#insn-009e683c) · [`009e684c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e6788.md#insn-009e684c)
- 新版 [`009e6880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e67dc.md#insn-009e6880) · [`009e6890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e67dc.md#insn-009e6890) · [`009e68a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e67dc.md#insn-009e68a0)

~~~diff
- 009e682c ["INT_ADD", "register:40f0:8", ["const:9e682c:8", "const:4:8"]]
- 009e682c ["CALL", null, ["callee:00c57f80:8"]]
+ 009e6880 ["INT_ADD", "register:40f0:8", ["const:9e6880:8", "const:4:8"]]
+ 009e6880 ["CALL", null, ["callee:00c57f80:8"]]
- 009e682c bytes a1c50994
+ 009e6880 bytes c0c50994
- 009e683c ["INT_ADD", "register:40f0:8", ["const:9e683c:8", "const:4:8"]]
- 009e683c ["CALL", null, ["callee:00c57f80:8"]]
+ 009e6890 ["INT_ADD", "register:40f0:8", ["const:9e6890:8", "const:4:8"]]
+ 009e6890 ["CALL", null, ["callee:00c57f80:8"]]
- 009e683c bytes 9dc50994
+ 009e6890 bytes bcc50994
- 009e684c ["INT_ADD", "register:40f0:8", ["const:9e684c:8", "const:4:8"]]
- 009e684c ["CALL", null, ["callee:00c57f80:8"]]
+ 009e68a0 ["INT_ADD", "register:40f0:8", ["const:9e68a0:8", "const:4:8"]]
+ 009e68a0 ["CALL", null, ["callee:00c57f80:8"]]
- 009e684c bytes 99c50994
+ 009e68a0 bytes b8c50994
~~~


<a id="compare-df7158aea6e3699c45bbbbceb8d846dc"></a>

### [`009e6860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e6860.md) → [`009e68b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e68b4.md) FUN_009e68b4

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009e30ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e3/009e30ec.md) · 呼出先 3件 [`009e6b24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e6b24.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5a820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a820.md)
- 新版 呼出元 1件 [`009e3140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e3/009e3140.md) · 呼出先 3件 [`009e6b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6b78.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5a8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a8f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009e692c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e6860.md#insn-009e692c) · [`009e69b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e6860.md#insn-009e69b8) · [`009e69d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e6860.md#insn-009e69d4)
- 新版 [`009e6980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e68b4.md#insn-009e6980) · [`009e6a0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e68b4.md#insn-009e6a0c) · [`009e6a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e68b4.md#insn-009e6a28)

~~~diff
- 009e692c ["INT_ADD", "register:40f0:8", ["const:9e692c:8", "const:4:8"]]
- 009e692c ["CALL", null, ["callee:00c57f60:8"]]
+ 009e6980 ["INT_ADD", "register:40f0:8", ["const:9e6980:8", "const:4:8"]]
+ 009e6980 ["CALL", null, ["callee:00c57f60:8"]]
- 009e692c bytes 59c50994
+ 009e6980 bytes 78c50994
- 009e69b8 ["INT_ADD", "register:40f0:8", ["const:9e69b8:8", "const:4:8"]]
- 009e69b8 ["CALL", null, ["callee:00c5a8f0:8"]]
+ 009e6a0c ["INT_ADD", "register:40f0:8", ["const:9e6a0c:8", "const:4:8"]]
+ 009e6a0c ["CALL", null, ["callee:00c5a8f0:8"]]
- 009e69b8 bytes 9acf0994
+ 009e6a0c bytes b9cf0994
- 009e69d4 ["INT_ADD", "register:40f0:8", ["const:9e69d4:8", "const:4:8"]]
- 009e69d4 ["CALL", null, ["callee:009e6b78:8"]]
+ 009e6a28 ["INT_ADD", "register:40f0:8", ["const:9e6a28:8", "const:4:8"]]
+ 009e6a28 ["CALL", null, ["callee:009e6b78:8"]]
- 009e69d4 bytes 54000094
+ 009e6a28 bytes 54000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0911659019047a69b7cdf1d8931686dc"></a>

### [`009e6b24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e6b24.md) → [`009e6b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6b78.md) FUN_009e6b78

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`009e6860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e6860.md) [`009e8458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8458.md) · 呼出先 3件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`009e68b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e68b4.md) [`009e84ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e84ac.md) · 呼出先 3件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009e6b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e6b24.md#insn-009e6b48) · [`009e6b5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e6b24.md#insn-009e6b5c) · [`009e6bbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e6b24.md#insn-009e6bbc)
- 新版 [`009e6b9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6b78.md#insn-009e6b9c) · [`009e6bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6b78.md#insn-009e6bb0) · [`009e6c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6b78.md#insn-009e6c10)

~~~diff
- 009e6b48 ["INT_ADD", "register:40f0:8", ["const:9e6b48:8", "const:4:8"]]
- 009e6b48 ["CALL", null, ["callee:00c57f60:8"]]
+ 009e6b9c ["INT_ADD", "register:40f0:8", ["const:9e6b9c:8", "const:4:8"]]
+ 009e6b9c ["CALL", null, ["callee:00c57f60:8"]]
- 009e6b48 bytes d2c40994
+ 009e6b9c bytes f1c40994
- 009e6b5c ["INT_ADD", "register:40f0:8", ["const:9e6b5c:8", "const:4:8"]]
- 009e6b5c ["CALL", null, ["callee:00c57f80:8"]]
+ 009e6bb0 ["INT_ADD", "register:40f0:8", ["const:9e6bb0:8", "const:4:8"]]
+ 009e6bb0 ["CALL", null, ["callee:00c57f80:8"]]
- 009e6b5c bytes d5c40994
+ 009e6bb0 bytes f4c40994
- 009e6bbc ["INT_ADD", "register:40f0:8", ["const:9e6bbc:8", "const:4:8"]]
- 009e6bbc ["CALL", null, ["callee:00c57f80:8"]]
+ 009e6c10 ["INT_ADD", "register:40f0:8", ["const:9e6c10:8", "const:4:8"]]
+ 009e6c10 ["CALL", null, ["callee:00c57f80:8"]]
- 009e6bbc bytes bdc40994
+ 009e6c10 bytes dcc40994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83146c55812643d6516efca75e4e0bf7"></a>

### [`009e8458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8458.md) → [`009e84ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e84ac.md) FUN_009e84ac

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`009e6c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e6c80.md) [`009e7bb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e7/009e7bb0.md) [`009e7e40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e7/009e7e40.md) [`009e8124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8124.md) [`009e871c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e871c.md) · 呼出先 3件 [`009e6b24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e6/009e6b24.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5a820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a820.md)
- 新版 呼出元 5件 [`009e6cd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6cd4.md) [`009e7c04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e7/009e7c04.md) [`009e7e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e7/009e7e94.md) [`009e8178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8178.md) [`009e8770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8770.md) · 呼出先 3件 [`009e6b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e6/009e6b78.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5a8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a8f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009e8524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8458.md#insn-009e8524) · [`009e85b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8458.md#insn-009e85b0) · [`009e85cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e8458.md#insn-009e85cc)
- 新版 [`009e8578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e84ac.md#insn-009e8578) · [`009e8604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e84ac.md#insn-009e8604) · [`009e8620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e84ac.md#insn-009e8620)

~~~diff
- 009e8524 ["INT_ADD", "register:40f0:8", ["const:9e8524:8", "const:4:8"]]
- 009e8524 ["CALL", null, ["callee:00c57f60:8"]]
+ 009e8578 ["INT_ADD", "register:40f0:8", ["const:9e8578:8", "const:4:8"]]
+ 009e8578 ["CALL", null, ["callee:00c57f60:8"]]
- 009e8524 bytes 5bbe0994
+ 009e8578 bytes 7abe0994
- 009e85b0 ["INT_ADD", "register:40f0:8", ["const:9e85b0:8", "const:4:8"]]
- 009e85b0 ["CALL", null, ["callee:00c5a8f0:8"]]
+ 009e8604 ["INT_ADD", "register:40f0:8", ["const:9e8604:8", "const:4:8"]]
+ 009e8604 ["CALL", null, ["callee:00c5a8f0:8"]]
- 009e85b0 bytes 9cc80994
+ 009e8604 bytes bbc80994
- 009e85cc ["INT_ADD", "register:40f0:8", ["const:9e85cc:8", "const:4:8"]]
- 009e85cc ["CALL", null, ["callee:009e6b78:8"]]
+ 009e8620 ["INT_ADD", "register:40f0:8", ["const:9e8620:8", "const:4:8"]]
+ 009e8620 ["CALL", null, ["callee:009e6b78:8"]]
- 009e85cc bytes 56f9ff97
+ 009e8620 bytes 56f9ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc0108a3881cfc4d39328c3a3213d950"></a>

### [`009e891c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e891c.md) → [`009e8970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8970.md) FUN_009e8970

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009e3b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e3/009e3b40.md) · 呼出先 3件 [`00494610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00494/00494610.md) [`0086ab38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086a/0086ab38.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`009e3b94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e3/009e3b94.md) · 呼出先 3件 [`00494650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494650.md) [`0086ab90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086a/0086ab90.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009e8980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e891c.md#insn-009e8980) · [`009e8990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e891c.md#insn-009e8990) · [`009e899c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e891c.md#insn-009e899c)
- 新版 [`009e89d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8970.md#insn-009e89d4) · [`009e89e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8970.md#insn-009e89e4) · [`009e89f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8970.md#insn-009e89f0)

~~~diff
- 009e8980 ["INT_ADD", "register:40f0:8", ["const:9e8980:8", "const:4:8"]]
- 009e8980 ["CALL", null, ["callee:00494650:8"]]
+ 009e89d4 ["INT_ADD", "register:40f0:8", ["const:9e89d4:8", "const:4:8"]]
+ 009e89d4 ["CALL", null, ["callee:00494650:8"]]
- 009e8980 bytes 24afea97
+ 009e89d4 bytes 1fafea97
- 009e8990 ["INT_ADD", "register:40f0:8", ["const:9e8990:8", "const:4:8"]]
- 009e8990 ["CALL", null, ["callee:00c57f80:8"]]
+ 009e89e4 ["INT_ADD", "register:40f0:8", ["const:9e89e4:8", "const:4:8"]]
+ 009e89e4 ["CALL", null, ["callee:00c57f80:8"]]
- 009e8990 bytes 48bd0994
+ 009e89e4 bytes 67bd0994
- 009e899c ["INT_ADD", "register:40f0:8", ["const:9e899c:8", "const:4:8"]]
- 009e899c ["CALL", null, ["callee:0086ab90:8"]]
+ 009e89f0 ["INT_ADD", "register:40f0:8", ["const:9e89f0:8", "const:4:8"]]
+ 009e89f0 ["CALL", null, ["callee:0086ab90:8"]]
- 009e899c bytes 6708fa97
+ 009e89f0 bytes 6808fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-105b32eaecc91e552810ae14c82e3876"></a>

### [`009e89b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e89b8.md) → [`009e8a0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8a0c.md) FUN_009e8a0c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`009e2464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e2/009e2464.md) [`009e89b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e89b8.md) · 呼出先 2件 [`009e89b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e89b8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`009e24b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e2/009e24b8.md) [`009e8a0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8a0c.md) · 呼出先 2件 [`009e8a0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8a0c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009e89d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e89b8.md#insn-009e89d8) · [`009e89e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e89b8.md#insn-009e89e4)
- 新版 [`009e8a2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8a0c.md#insn-009e8a2c) · [`009e8a38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8a0c.md#insn-009e8a38)

~~~diff
- 009e89d8 ["INT_ADD", "register:40f0:8", ["const:9e89d8:8", "const:4:8"]]
- 009e89d8 ["CALL", null, ["local:b0:8"]]
+ 009e8a2c ["INT_ADD", "register:40f0:8", ["const:9e8a2c:8", "const:4:8"]]
+ 009e8a2c ["CALL", null, ["local:b0:8"]]
- 009e89d8 bytes f8ffff97
+ 009e8a2c bytes f8ffff97
- 009e89e4 ["INT_ADD", "register:40f0:8", ["const:9e89e4:8", "const:4:8"]]
- 009e89e4 ["CALL", null, ["local:b0:8"]]
+ 009e8a38 ["INT_ADD", "register:40f0:8", ["const:9e8a38:8", "const:4:8"]]
+ 009e8a38 ["CALL", null, ["local:b0:8"]]
- 009e89e4 bytes f5ffff97
+ 009e8a38 bytes f5ffff97
~~~


<a id="compare-1275e84840163050290ba5aa60ac2395"></a>

### [`009e89fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e89fc.md) → [`009e8a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8a50.md) FUN_009e8a50

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`009e2464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e2/009e2464.md) [`009e89fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e89fc.md) · 呼出先 2件 [`009e89fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e89fc.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`009e24b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e2/009e24b8.md) [`009e8a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8a50.md) · 呼出先 2件 [`009e8a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8a50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009e8a1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e89fc.md#insn-009e8a1c) · [`009e8a28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e8/009e89fc.md#insn-009e8a28)
- 新版 [`009e8a70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8a50.md#insn-009e8a70) · [`009e8a7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e8/009e8a50.md#insn-009e8a7c)

~~~diff
- 009e8a1c ["INT_ADD", "register:40f0:8", ["const:9e8a1c:8", "const:4:8"]]
- 009e8a1c ["CALL", null, ["local:b0:8"]]
+ 009e8a70 ["INT_ADD", "register:40f0:8", ["const:9e8a70:8", "const:4:8"]]
+ 009e8a70 ["CALL", null, ["local:b0:8"]]
- 009e8a1c bytes f8ffff97
+ 009e8a70 bytes f8ffff97
- 009e8a28 ["INT_ADD", "register:40f0:8", ["const:9e8a28:8", "const:4:8"]]
- 009e8a28 ["CALL", null, ["local:b0:8"]]
+ 009e8a7c ["INT_ADD", "register:40f0:8", ["const:9e8a7c:8", "const:4:8"]]
+ 009e8a7c ["CALL", null, ["local:b0:8"]]
- 009e8a28 bytes f5ffff97
+ 009e8a7c bytes f5ffff97
~~~


<a id="compare-9957b85bc30d3d451825994986e91d47"></a>

### [`009e93d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e9/009e93d8.md) → [`009e942c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e9/009e942c.md) FUN_009e942c

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009eaf84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ea/009eaf84.md) · 呼出先 2件 [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md)
- 新版 呼出元 1件 [`009eafd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ea/009eafd8.md) · 呼出先 2件 [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009e93fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e9/009e93d8.md#insn-009e93fc) · [`009e9440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e9/009e93d8.md#insn-009e9440) · [`009e945c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e9/009e93d8.md#insn-009e945c)
- 新版 [`009e9450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e9/009e942c.md#insn-009e9450) · [`009e9494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e9/009e942c.md#insn-009e9494) · [`009e94b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e9/009e942c.md#insn-009e94b0)

~~~diff
- 009e93fc ["INT_ADD", "register:40f0:8", ["const:9e93fc:8", "const:4:8"]]
- 009e93fc ["CALL", null, ["callee:004410cc:8"]]
+ 009e9450 ["INT_ADD", "register:40f0:8", ["const:9e9450:8", "const:4:8"]]
+ 009e9450 ["CALL", null, ["callee:004410cc:8"]]
- 009e93fc bytes 245fe997
+ 009e9450 bytes 1f5fe997
- 009e9440 ["COPY", "register:0:8", ["register:4040:8"]]
- 009e9440 ["INT_ADD", "register:40f0:8", ["const:9e9440:8", "const:4:8"]]
- 009e9440 ["CALLIND", null, ["register:0:8"]]
+ 009e9494 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009e9494 ["INT_ADD", "register:40f0:8", ["const:9e9494:8", "const:4:8"]]
+ 009e9494 ["CALLIND", null, ["register:0:8"]]
- 009e9440 bytes 00013fd6
+ 009e9494 bytes 00013fd6
- 009e945c ["INT_ADD", "register:40f0:8", ["const:9e945c:8", "const:4:8"]]
- 009e945c ["CALL", null, ["callee:00459db4:8"]]
+ 009e94b0 ["INT_ADD", "register:40f0:8", ["const:9e94b0:8", "const:4:8"]]
+ 009e94b0 ["CALL", null, ["callee:00459db4:8"]]
- 009e945c bytes 46c2e997
+ 009e94b0 bytes 41c2e997
~~~


<a id="compare-9f1c95b2084dd986973c9342c9233a5d"></a>

### [`009ec078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ec/009ec078.md) → [`009ec0cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ec/009ec0cc.md) FUN_009ec0cc

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009eaf84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ea/009eaf84.md) · 呼出先 1件 [`009f2e64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2e64.md)
- 新版 呼出元 1件 [`009eafd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ea/009eafd8.md) · 呼出先 1件 [`009f2eb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2eb8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009ec0ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ec/009ec078.md#insn-009ec0ac)
- 新版 [`009ec100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ec/009ec0cc.md#insn-009ec100)

~~~diff
- 009ec0ac ["INT_ADD", "register:40f0:8", ["const:9ec0ac:8", "const:4:8"]]
- 009ec0ac ["CALL", null, ["callee:009f2eb8:8"]]
+ 009ec100 ["INT_ADD", "register:40f0:8", ["const:9ec100:8", "const:4:8"]]
+ 009ec100 ["CALL", null, ["callee:009f2eb8:8"]]
- 009ec0ac bytes 6e1b0094
+ 009ec100 bytes 6e1b0094
~~~


<a id="compare-21f694ff257f19ad4fb18c807c3bab8e"></a>

### [`009ec0c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ec/009ec0c0.md) → [`009ec114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ec/009ec114.md) FUN_009ec114

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009eaf84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ea/009eaf84.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`009eafd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ea/009eafd8.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009ec0dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ec/009ec0c0.md#insn-009ec0dc) · [`009ec0fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ec/009ec0c0.md#insn-009ec0fc)
- 新版 [`009ec130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ec/009ec114.md#insn-009ec130) · [`009ec150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ec/009ec114.md#insn-009ec150)

~~~diff
- 009ec0dc ["INT_ADD", "register:40f0:8", ["const:9ec0dc:8", "const:4:8"]]
- 009ec0dc ["CALL", null, ["callee:00c53da0:8"]]
+ 009ec130 ["INT_ADD", "register:40f0:8", ["const:9ec130:8", "const:4:8"]]
+ 009ec130 ["CALL", null, ["callee:00c53da0:8"]]
- 009ec0dc bytes 099f0994
+ 009ec130 bytes 1c9f0994
- 009ec0fc ["COPY", "register:0:8", ["register:4040:8"]]
- 009ec0fc ["INT_ADD", "register:40f0:8", ["const:9ec0fc:8", "const:4:8"]]
- 009ec0fc ["CALLIND", null, ["register:0:8"]]
+ 009ec150 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009ec150 ["INT_ADD", "register:40f0:8", ["const:9ec150:8", "const:4:8"]]
+ 009ec150 ["CALLIND", null, ["register:0:8"]]
- 009ec0fc bytes 00013fd6
+ 009ec150 bytes 00013fd6
~~~


<a id="compare-da0eb0406d474f883721b6fe855551ee"></a>

### [`009ec110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ec/009ec110.md) → [`009ec164`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ec/009ec164.md) FUN_009ec164

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009eaf84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ea/009eaf84.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`009eafd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ea/009eafd8.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009ec12c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ec/009ec110.md#insn-009ec12c) · [`009ec14c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ec/009ec110.md#insn-009ec14c)
- 新版 [`009ec180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ec/009ec164.md#insn-009ec180) · [`009ec1a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ec/009ec164.md#insn-009ec1a0)

~~~diff
- 009ec12c ["INT_ADD", "register:40f0:8", ["const:9ec12c:8", "const:4:8"]]
- 009ec12c ["CALL", null, ["callee:00c53da0:8"]]
+ 009ec180 ["INT_ADD", "register:40f0:8", ["const:9ec180:8", "const:4:8"]]
+ 009ec180 ["CALL", null, ["callee:00c53da0:8"]]
- 009ec12c bytes f59e0994
+ 009ec180 bytes 089f0994
- 009ec14c ["COPY", "register:0:8", ["register:4040:8"]]
- 009ec14c ["INT_ADD", "register:40f0:8", ["const:9ec14c:8", "const:4:8"]]
- 009ec14c ["CALLIND", null, ["register:0:8"]]
+ 009ec1a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009ec1a0 ["INT_ADD", "register:40f0:8", ["const:9ec1a0:8", "const:4:8"]]
+ 009ec1a0 ["CALLIND", null, ["register:0:8"]]
- 009ec14c bytes 00013fd6
+ 009ec1a0 bytes 00013fd6
~~~


<a id="compare-3f4864b9e8190c4f6f7e7d5df97f24d2"></a>

### [`009ec160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ec/009ec160.md) → [`009ec1b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ec/009ec1b4.md) FUN_009ec1b4

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009eaf84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ea/009eaf84.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`009eafd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ea/009eafd8.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009ec17c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ec/009ec160.md#insn-009ec17c) · [`009ec19c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ec/009ec160.md#insn-009ec19c)
- 新版 [`009ec1d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ec/009ec1b4.md#insn-009ec1d0) · [`009ec1f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ec/009ec1b4.md#insn-009ec1f0)

~~~diff
- 009ec17c ["INT_ADD", "register:40f0:8", ["const:9ec17c:8", "const:4:8"]]
- 009ec17c ["CALL", null, ["callee:00c53da0:8"]]
+ 009ec1d0 ["INT_ADD", "register:40f0:8", ["const:9ec1d0:8", "const:4:8"]]
+ 009ec1d0 ["CALL", null, ["callee:00c53da0:8"]]
- 009ec17c bytes e19e0994
+ 009ec1d0 bytes f49e0994
- 009ec19c ["COPY", "register:0:8", ["register:4040:8"]]
- 009ec19c ["INT_ADD", "register:40f0:8", ["const:9ec19c:8", "const:4:8"]]
- 009ec19c ["CALLIND", null, ["register:0:8"]]
+ 009ec1f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009ec1f0 ["INT_ADD", "register:40f0:8", ["const:9ec1f0:8", "const:4:8"]]
+ 009ec1f0 ["CALLIND", null, ["register:0:8"]]
- 009ec19c bytes 00013fd6
+ 009ec1f0 bytes 00013fd6
~~~


<a id="compare-b7783f4c5f6ee92eb3525ba2a0705eaa"></a>

### [`009ec1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ec/009ec1b0.md) → [`009ec204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ec/009ec204.md) FUN_009ec204

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009eaf84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ea/009eaf84.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`009eafd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ea/009eafd8.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009ec1cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ec/009ec1b0.md#insn-009ec1cc) · [`009ec1ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ec/009ec1b0.md#insn-009ec1ec)
- 新版 [`009ec220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ec/009ec204.md#insn-009ec220) · [`009ec240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ec/009ec204.md#insn-009ec240)

~~~diff
- 009ec1cc ["INT_ADD", "register:40f0:8", ["const:9ec1cc:8", "const:4:8"]]
- 009ec1cc ["CALL", null, ["callee:00c53da0:8"]]
+ 009ec220 ["INT_ADD", "register:40f0:8", ["const:9ec220:8", "const:4:8"]]
+ 009ec220 ["CALL", null, ["callee:00c53da0:8"]]
- 009ec1cc bytes cd9e0994
+ 009ec220 bytes e09e0994
- 009ec1ec ["COPY", "register:0:8", ["register:4040:8"]]
- 009ec1ec ["INT_ADD", "register:40f0:8", ["const:9ec1ec:8", "const:4:8"]]
- 009ec1ec ["CALLIND", null, ["register:0:8"]]
+ 009ec240 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009ec240 ["INT_ADD", "register:40f0:8", ["const:9ec240:8", "const:4:8"]]
+ 009ec240 ["CALLIND", null, ["register:0:8"]]
- 009ec1ec bytes 00013fd6
+ 009ec240 bytes 00013fd6
~~~


<a id="compare-d710026d2615dcc4ae2b192a3640f6c0"></a>

### [`009ec200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ec/009ec200.md) → [`009ec254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ec/009ec254.md) FUN_009ec254

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009eaf84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ea/009eaf84.md) · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`009eafd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ea/009eafd8.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009ec21c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ec/009ec200.md#insn-009ec21c) · [`009ec23c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ec/009ec200.md#insn-009ec23c)
- 新版 [`009ec270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ec/009ec254.md#insn-009ec270) · [`009ec290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ec/009ec254.md#insn-009ec290)

~~~diff
- 009ec21c ["INT_ADD", "register:40f0:8", ["const:9ec21c:8", "const:4:8"]]
- 009ec21c ["CALL", null, ["callee:00c53da0:8"]]
+ 009ec270 ["INT_ADD", "register:40f0:8", ["const:9ec270:8", "const:4:8"]]
+ 009ec270 ["CALL", null, ["callee:00c53da0:8"]]
- 009ec21c bytes b99e0994
+ 009ec270 bytes cc9e0994
- 009ec23c ["COPY", "register:0:8", ["register:4040:8"]]
- 009ec23c ["INT_ADD", "register:40f0:8", ["const:9ec23c:8", "const:4:8"]]
- 009ec23c ["CALLIND", null, ["register:0:8"]]
+ 009ec290 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009ec290 ["INT_ADD", "register:40f0:8", ["const:9ec290:8", "const:4:8"]]
+ 009ec290 ["CALLIND", null, ["register:0:8"]]
- 009ec23c bytes 00013fd6
+ 009ec290 bytes 00013fd6
~~~


<a id="compare-e966a433516f9d8d26d5ee27649fbc07"></a>

### [`009ecf6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ec/009ecf6c.md) → [`009ecfc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ec/009ecfc0.md) FUN_009ecfc0

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009ec95c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ec/009ec95c.md) · 呼出先 2件 [`009f34ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f34ac.md) [`00c5a930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a930.md)
- 新版 呼出元 1件 [`009ec9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ec/009ec9b0.md) · 呼出先 2件 [`009f3500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3500.md) [`00c5aa00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aa00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009ed020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ec/009ecf6c.md#insn-009ed020) · [`009ed03c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ec/009ecf6c.md#insn-009ed03c)
- 新版 [`009ed074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ec/009ecfc0.md#insn-009ed074) · [`009ed090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ec/009ecfc0.md#insn-009ed090)

~~~diff
- 009ed020 ["INT_ADD", "register:40f0:8", ["const:9ed020:8", "const:4:8"]]
- 009ed020 ["CALL", null, ["callee:009f3500:8"]]
+ 009ed074 ["INT_ADD", "register:40f0:8", ["const:9ed074:8", "const:4:8"]]
+ 009ed074 ["CALL", null, ["callee:009f3500:8"]]
- 009ed020 bytes 23190094
+ 009ed074 bytes 23190094
- 009ed03c ["INT_ADD", "register:40f0:8", ["const:9ed03c:8", "const:4:8"]]
- 009ed03c ["CALL", null, ["callee:00c5aa00:8"]]
+ 009ed090 ["INT_ADD", "register:40f0:8", ["const:9ed090:8", "const:4:8"]]
+ 009ed090 ["CALL", null, ["callee:00c5aa00:8"]]
- 009ed03c bytes 3db60994
+ 009ed090 bytes 5cb60994
~~~


<a id="compare-6367e67ecda08c28b16891dd44fe976e"></a>

### [`009ed0c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ed/009ed0c8.md) → [`009ed11c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ed/009ed11c.md) FUN_009ed11c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009ed0e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ed/009ed0c8.md#insn-009ed0e4) · [`009ed104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ed/009ed0c8.md#insn-009ed104)
- 新版 [`009ed138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ed/009ed11c.md#insn-009ed138) · [`009ed158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ed/009ed11c.md#insn-009ed158)

~~~diff
- 009ed0e4 ["INT_ADD", "register:40f0:8", ["const:9ed0e4:8", "const:4:8"]]
- 009ed0e4 ["CALL", null, ["callee:00c53da0:8"]]
+ 009ed138 ["INT_ADD", "register:40f0:8", ["const:9ed138:8", "const:4:8"]]
+ 009ed138 ["CALL", null, ["callee:00c53da0:8"]]
- 009ed0e4 bytes 079b0994
+ 009ed138 bytes 1a9b0994
- 009ed104 ["COPY", "register:0:8", ["register:4040:8"]]
- 009ed104 ["INT_ADD", "register:40f0:8", ["const:9ed104:8", "const:4:8"]]
- 009ed104 ["CALLIND", null, ["register:0:8"]]
+ 009ed158 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009ed158 ["INT_ADD", "register:40f0:8", ["const:9ed158:8", "const:4:8"]]
+ 009ed158 ["CALLIND", null, ["register:0:8"]]
- 009ed104 bytes 00013fd6
+ 009ed158 bytes 00013fd6
~~~


<a id="compare-4178be7cb49b418883781462085f3623"></a>

### [`009edefc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ed/009edefc.md) → [`009edf50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ed/009edf50.md) FUN_009edf50

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009ee138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ee/009ee138.md) · 呼出先 7件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`009edb3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ed/009edb3c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`009ee18c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ee/009ee18c.md) · 呼出先 7件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`009edb90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ed/009edb90.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009edf5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ed/009edefc.md#insn-009edf5c) · [`009edf94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ed/009edefc.md#insn-009edf94) · [`009edfc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ed/009edefc.md#insn-009edfc8)
- 新版 [`009edfb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ed/009edf50.md#insn-009edfb0) · [`009edfe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ed/009edf50.md#insn-009edfe8) · [`009ee01c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ed/009edf50.md#insn-009ee01c)

~~~diff
- 009edf5c ["INT_ADD", "register:40f0:8", ["const:9edf5c:8", "const:4:8"]]
- 009edf5c ["CALL", null, ["callee:004410cc:8"]]
+ 009edfb0 ["INT_ADD", "register:40f0:8", ["const:9edfb0:8", "const:4:8"]]
+ 009edfb0 ["CALL", null, ["callee:004410cc:8"]]
- 009edf5c bytes 4c4ce997
+ 009edfb0 bytes 474ce997
- 009edf94 ["INT_ADD", "register:40f0:8", ["const:9edf94:8", "const:4:8"]]
- 009edf94 ["CALL", null, ["callee:00c57f80:8"]]
+ 009edfe8 ["INT_ADD", "register:40f0:8", ["const:9edfe8:8", "const:4:8"]]
+ 009edfe8 ["CALL", null, ["callee:00c57f80:8"]]
- 009edf94 bytes c7a70994
+ 009edfe8 bytes e6a70994
- 009edfc8 ["INT_ADD", "register:40f0:8", ["const:9edfc8:8", "const:4:8"]]
- 009edfc8 ["CALL", null, ["callee:00c58130:8"]]
+ 009ee01c ["INT_ADD", "register:40f0:8", ["const:9ee01c:8", "const:4:8"]]
+ 009ee01c ["CALL", null, ["callee:00c58130:8"]]
- 009edfc8 bytes 26a80994
+ 009ee01c bytes 45a80994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20ccfc34ba44af3e8d47408f36ea8f91"></a>

### [`009ee138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ee/009ee138.md) → [`009ee18c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ee/009ee18c.md) FUN_009ee18c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009ee334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ee/009ee334.md) · 呼出先 6件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`009edefc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ed/009edefc.md) [`009f27f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f27f4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`009ee388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ee/009ee388.md) · 呼出先 6件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`009edf50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ed/009edf50.md) [`009f2848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2848.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009ee1a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ee/009ee138.md#insn-009ee1a4) · [`009ee214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ee/009ee138.md#insn-009ee214) · [`009ee258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ee/009ee138.md#insn-009ee258)
- 新版 [`009ee1f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ee/009ee18c.md#insn-009ee1f8) · [`009ee268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ee/009ee18c.md#insn-009ee268) · [`009ee2ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ee/009ee18c.md#insn-009ee2ac)

~~~diff
- 009ee1a4 ["INT_ADD", "register:40f0:8", ["const:9ee1a4:8", "const:4:8"]]
- 009ee1a4 ["CALL", null, ["callee:00c58130:8"]]
+ 009ee1f8 ["INT_ADD", "register:40f0:8", ["const:9ee1f8:8", "const:4:8"]]
+ 009ee1f8 ["CALL", null, ["callee:00c58130:8"]]
- 009ee1a4 bytes afa70994
+ 009ee1f8 bytes cea70994
- 009ee214 ["INT_ADD", "register:40f0:8", ["const:9ee214:8", "const:4:8"]]
- 009ee214 ["CALL", null, ["callee:00c57f60:8"]]
+ 009ee268 ["INT_ADD", "register:40f0:8", ["const:9ee268:8", "const:4:8"]]
+ 009ee268 ["CALL", null, ["callee:00c57f60:8"]]
- 009ee214 bytes 1fa70994
+ 009ee268 bytes 3ea70994
- 009ee258 ["INT_ADD", "register:40f0:8", ["const:9ee258:8", "const:4:8"]]
- 009ee258 ["CALL", null, ["callee:0043bbe4:8"]]
+ 009ee2ac ["INT_ADD", "register:40f0:8", ["const:9ee2ac:8", "const:4:8"]]
+ 009ee2ac ["CALL", null, ["callee:0043bbe4:8"]]
- 009ee258 bytes 5336e997
+ 009ee2ac bytes 4e36e997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59f6d162fa7c92ea455e449112f4f435"></a>

### [`009eecb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ee/009eecb0.md) → [`009eed04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ee/009eed04.md) FUN_009eed04

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009eee28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ee/009eee28.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`009ee970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ee/009ee970.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58060.md)
- 新版 呼出元 1件 [`009eee7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ee/009eee7c.md) · 呼出先 4件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`009ee9c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ee/009ee9c4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58130.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009eed04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ee/009eecb0.md#insn-009eed04) · [`009eed70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ee/009eecb0.md#insn-009eed70) · [`009eedac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ee/009eecb0.md#insn-009eedac)
- 新版 [`009eed58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ee/009eed04.md#insn-009eed58) · [`009eedc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ee/009eed04.md#insn-009eedc4) · [`009eee00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ee/009eed04.md#insn-009eee00)

~~~diff
- 009eed04 ["INT_ADD", "register:40f0:8", ["const:9eed04:8", "const:4:8"]]
- 009eed04 ["CALL", null, ["callee:00c58130:8"]]
+ 009eed58 ["INT_ADD", "register:40f0:8", ["const:9eed58:8", "const:4:8"]]
+ 009eed58 ["CALL", null, ["callee:00c58130:8"]]
- 009eed04 bytes d7a40994
+ 009eed58 bytes f6a40994
- 009eed70 ["INT_ADD", "register:40f0:8", ["const:9eed70:8", "const:4:8"]]
- 009eed70 ["CALL", null, ["callee:00c57f60:8"]]
+ 009eedc4 ["INT_ADD", "register:40f0:8", ["const:9eedc4:8", "const:4:8"]]
+ 009eedc4 ["CALL", null, ["callee:00c57f60:8"]]
- 009eed70 bytes 48a40994
+ 009eedc4 bytes 67a40994
- 009eedac ["INT_ADD", "register:40f0:8", ["const:9eedac:8", "const:4:8"]]
- 009eedac ["CALL", null, ["callee:0043bbe4:8"]]
+ 009eee00 ["INT_ADD", "register:40f0:8", ["const:9eee00:8", "const:4:8"]]
+ 009eee00 ["CALL", null, ["callee:0043bbe4:8"]]
- 009eedac bytes 7e33e997
+ 009eee00 bytes 7933e997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a5820e208aa056293cc1b8acae3aa11"></a>

### [`009eee28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ee/009eee28.md) → [`009eee7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ee/009eee7c.md) FUN_009eee7c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009ef024`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ef/009ef024.md) · 呼出先 6件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`009eecb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ee/009eecb0.md) [`009f3764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`009ef078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009ef078.md) · 呼出先 6件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`009eed04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ee/009eed04.md) [`009f37b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f37b8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009eee94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ee/009eee28.md#insn-009eee94) · [`009eef04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ee/009eee28.md#insn-009eef04) · [`009eef48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ee/009eee28.md#insn-009eef48)
- 新版 [`009eeee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ee/009eee7c.md#insn-009eeee8) · [`009eef58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ee/009eee7c.md#insn-009eef58) · [`009eef9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ee/009eee7c.md#insn-009eef9c)

~~~diff
- 009eee94 ["INT_ADD", "register:40f0:8", ["const:9eee94:8", "const:4:8"]]
- 009eee94 ["CALL", null, ["callee:00c58130:8"]]
+ 009eeee8 ["INT_ADD", "register:40f0:8", ["const:9eeee8:8", "const:4:8"]]
+ 009eeee8 ["CALL", null, ["callee:00c58130:8"]]
- 009eee94 bytes 73a40994
+ 009eeee8 bytes 92a40994
- 009eef04 ["INT_ADD", "register:40f0:8", ["const:9eef04:8", "const:4:8"]]
- 009eef04 ["CALL", null, ["callee:00c57f60:8"]]
+ 009eef58 ["INT_ADD", "register:40f0:8", ["const:9eef58:8", "const:4:8"]]
+ 009eef58 ["CALL", null, ["callee:00c57f60:8"]]
- 009eef04 bytes e3a30994
+ 009eef58 bytes 02a40994
- 009eef48 ["INT_ADD", "register:40f0:8", ["const:9eef48:8", "const:4:8"]]
- 009eef48 ["CALL", null, ["callee:0043bbe4:8"]]
+ 009eef9c ["INT_ADD", "register:40f0:8", ["const:9eef9c:8", "const:4:8"]]
+ 009eef9c ["CALL", null, ["callee:0043bbe4:8"]]
- 009eef48 bytes 1733e997
+ 009eef9c bytes 1233e997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-655dd50da3f168793f39d98d94ee5653"></a>

### [`009f1048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1048.md) → [`009f109c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f109c.md) FUN_009f109c

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f0d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f0/009f0d34.md) · 呼出先 4件 [`009f2b1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2b1c.md) [`009f3764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3764.md) [`009f42e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f42e0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`009f0d88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f0/009f0d88.md) · 呼出先 4件 [`009f2b70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2b70.md) [`009f37b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f37b8.md) [`009f4334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4334.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009f10c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1048.md#insn-009f10c4) · [`009f1134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1048.md#insn-009f1134) · [`009f119c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1048.md#insn-009f119c)
- 新版 [`009f1118`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f109c.md#insn-009f1118) · [`009f1188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f109c.md#insn-009f1188) · [`009f11f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f109c.md#insn-009f11f0)

~~~diff
- 009f10c4 ["INT_ADD", "register:40f0:8", ["const:9f10c4:8", "const:4:8"]]
- 009f10c4 ["CALL", null, ["callee:009f4334:8"]]
+ 009f1118 ["INT_ADD", "register:40f0:8", ["const:9f1118:8", "const:4:8"]]
+ 009f1118 ["CALL", null, ["callee:009f4334:8"]]
- 009f10c4 bytes 870c0094
+ 009f1118 bytes 870c0094
- 009f1134 ["INT_ADD", "register:40f0:8", ["const:9f1134:8", "const:4:8"]]
- 009f1134 ["CALL", null, ["callee:009f2b70:8"]]
+ 009f1188 ["INT_ADD", "register:40f0:8", ["const:9f1188:8", "const:4:8"]]
+ 009f1188 ["CALL", null, ["callee:009f2b70:8"]]
- 009f1134 bytes 7a060094
+ 009f1188 bytes 7a060094
- 009f119c ["INT_ADD", "register:40f0:8", ["const:9f119c:8", "const:4:8"]]
- 009f119c ["CALL", null, ["callee:009f2b70:8"]]
+ 009f11f0 ["INT_ADD", "register:40f0:8", ["const:9f11f0:8", "const:4:8"]]
+ 009f11f0 ["CALL", null, ["callee:009f2b70:8"]]
- 009f119c bytes 60060094
+ 009f11f0 bytes 60060094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03a6719ef2864f8527e7f03e6e422430"></a>

### [`009f1200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1200.md) → [`009f1254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f1254.md) FUN_009f1254

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 8件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`009f3ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3ab8.md) [`009f4950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4950.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`009f3b0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3b0c.md) [`009f49a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f49a4.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009f1268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1200.md#insn-009f1268) · [`009f1280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1200.md#insn-009f1280) · [`009f1318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1200.md#insn-009f1318)
- 新版 [`009f12bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f1254.md#insn-009f12bc) · [`009f12d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f1254.md#insn-009f12d4) · [`009f136c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f1254.md#insn-009f136c)

~~~diff
- 009f1268 ["INT_ADD", "register:40f0:8", ["const:9f1268:8", "const:4:8"]]
- 009f1268 ["CALL", null, ["callee:009f49a4:8"]]
+ 009f12bc ["INT_ADD", "register:40f0:8", ["const:9f12bc:8", "const:4:8"]]
+ 009f12bc ["CALL", null, ["callee:009f49a4:8"]]
- 009f1268 bytes ba0d0094
+ 009f12bc bytes ba0d0094
- 009f1280 ["INT_ADD", "register:40f0:8", ["const:9f1280:8", "const:4:8"]]
- 009f1280 ["CALL", null, ["callee:00c57f80:8"]]
+ 009f12d4 ["INT_ADD", "register:40f0:8", ["const:9f12d4:8", "const:4:8"]]
+ 009f12d4 ["CALL", null, ["callee:00c57f80:8"]]
- 009f1280 bytes 0c9b0994
+ 009f12d4 bytes 2b9b0994
- 009f1318 ["INT_ADD", "register:40f0:8", ["const:9f1318:8", "const:4:8"]]
- 009f1318 ["CALL", null, ["callee:00c57f60:8"]]
+ 009f136c ["INT_ADD", "register:40f0:8", ["const:9f136c:8", "const:4:8"]]
+ 009f136c ["CALL", null, ["callee:00c57f60:8"]]
- 009f1318 bytes de9a0994
+ 009f136c bytes fd9a0994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7cf200ec81e451aea7e7d0d5e329fe99"></a>

### [`009f15bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f15bc.md) → [`009f1610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f1610.md) FUN_009f1610

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`009f4adc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4adc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`009f4b30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4b30.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009f1660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f15bc.md#insn-009f1660) · [`009f1688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f15bc.md#insn-009f1688) · [`009f169c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f15bc.md#insn-009f169c)
- 新版 [`009f16b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f1610.md#insn-009f16b4) · [`009f16dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f1610.md#insn-009f16dc) · [`009f16f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f1610.md#insn-009f16f0)

~~~diff
- 009f1660 ["INT_ADD", "register:40f0:8", ["const:9f1660:8", "const:4:8"]]
- 009f1660 ["CALL", null, ["callee:00c57f60:8"]]
+ 009f16b4 ["INT_ADD", "register:40f0:8", ["const:9f16b4:8", "const:4:8"]]
+ 009f16b4 ["CALL", null, ["callee:00c57f60:8"]]
- 009f1660 bytes 0c9a0994
+ 009f16b4 bytes 2b9a0994
- 009f1688 ["INT_ADD", "register:40f0:8", ["const:9f1688:8", "const:4:8"]]
- 009f1688 ["CALL", null, ["callee:00c580d0:8"]]
+ 009f16dc ["INT_ADD", "register:40f0:8", ["const:9f16dc:8", "const:4:8"]]
+ 009f16dc ["CALL", null, ["callee:00c580d0:8"]]
- 009f1688 bytes 5e9a0994
+ 009f16dc bytes 7d9a0994
- 009f169c ["INT_ADD", "register:40f0:8", ["const:9f169c:8", "const:4:8"]]
- 009f169c ["CALL", null, ["callee:00c57f80:8"]]
+ 009f16f0 ["INT_ADD", "register:40f0:8", ["const:9f16f0:8", "const:4:8"]]
+ 009f16f0 ["CALL", null, ["callee:00c57f80:8"]]
- 009f169c bytes 059a0994
+ 009f16f0 bytes 249a0994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05ae652fb8c31e6701a8f9e6c9b0b1cc"></a>

### [`009f1700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1700.md) → [`009f1754`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f1754.md) FUN_009f1754

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`009f4af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4af0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`009f4b44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4b44.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009f17a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1700.md#insn-009f17a4) · [`009f17cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1700.md#insn-009f17cc) · [`009f17e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1700.md#insn-009f17e0)
- 新版 [`009f17f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f1754.md#insn-009f17f8) · [`009f1820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f1754.md#insn-009f1820) · [`009f1834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f1754.md#insn-009f1834)

~~~diff
- 009f17a4 ["INT_ADD", "register:40f0:8", ["const:9f17a4:8", "const:4:8"]]
- 009f17a4 ["CALL", null, ["callee:00c57f60:8"]]
+ 009f17f8 ["INT_ADD", "register:40f0:8", ["const:9f17f8:8", "const:4:8"]]
+ 009f17f8 ["CALL", null, ["callee:00c57f60:8"]]
- 009f17a4 bytes bb990994
+ 009f17f8 bytes da990994
- 009f17cc ["INT_ADD", "register:40f0:8", ["const:9f17cc:8", "const:4:8"]]
- 009f17cc ["CALL", null, ["callee:00c580d0:8"]]
+ 009f1820 ["INT_ADD", "register:40f0:8", ["const:9f1820:8", "const:4:8"]]
+ 009f1820 ["CALL", null, ["callee:00c580d0:8"]]
- 009f17cc bytes 0d9a0994
+ 009f1820 bytes 2c9a0994
- 009f17e0 ["INT_ADD", "register:40f0:8", ["const:9f17e0:8", "const:4:8"]]
- 009f17e0 ["CALL", null, ["callee:00c57f80:8"]]
+ 009f1834 ["INT_ADD", "register:40f0:8", ["const:9f1834:8", "const:4:8"]]
+ 009f1834 ["CALL", null, ["callee:00c57f80:8"]]
- 009f17e0 bytes b4990994
+ 009f1834 bytes d3990994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5603290c2d30ff33bf161d16bb969ea0"></a>

### [`009f24a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f24a4.md) → [`009f24f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f24f8.md) FUN_009f24f8

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`009f050c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f0/009f050c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`009f0560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f0/009f0560.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009f25f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f24a4.md#insn-009f25f8)
- 新版 [`009f264c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f24f8.md#insn-009f264c)

~~~diff
- 009f25f8 ["INT_ADD", "register:40f0:8", ["const:9f25f8:8", "const:4:8"]]
- 009f25f8 ["CALL", null, ["callee:009f0560:8"]]
+ 009f264c ["INT_ADD", "register:40f0:8", ["const:9f264c:8", "const:4:8"]]
+ 009f264c ["CALL", null, ["callee:009f0560:8"]]
- 009f25f8 bytes c5f7ff97
+ 009f264c bytes c5f7ff97
~~~


<a id="compare-1adac460350e85286029b4638ccda0ff"></a>

### [`009f27f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f27f4.md) → [`009f2848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2848.md) FUN_009f2848

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`009ee138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ee/009ee138.md) [`009f27f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f27f4.md) [`009f2844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2844.md) · 呼出先 2件 [`009f27f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f27f4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`009ee18c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ee/009ee18c.md) [`009f2848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2848.md) [`009f2898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2898.md) · 呼出先 2件 [`009f2848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2848.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009f2810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f27f4.md#insn-009f2810) · [`009f281c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f27f4.md#insn-009f281c) · [`009f282c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f27f4.md#insn-009f282c)
- 新版 [`009f2864`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2848.md#insn-009f2864) · [`009f2870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2848.md#insn-009f2870) · [`009f2880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2848.md#insn-009f2880)

~~~diff
- 009f2810 ["INT_ADD", "register:40f0:8", ["const:9f2810:8", "const:4:8"]]
- 009f2810 ["CALL", null, ["local:b0:8"]]
+ 009f2864 ["INT_ADD", "register:40f0:8", ["const:9f2864:8", "const:4:8"]]
+ 009f2864 ["CALL", null, ["local:b0:8"]]
- 009f2810 bytes f9ffff97
+ 009f2864 bytes f9ffff97
- 009f281c ["INT_ADD", "register:40f0:8", ["const:9f281c:8", "const:4:8"]]
- 009f281c ["CALL", null, ["local:b0:8"]]
+ 009f2870 ["INT_ADD", "register:40f0:8", ["const:9f2870:8", "const:4:8"]]
+ 009f2870 ["CALL", null, ["local:b0:8"]]
- 009f281c bytes f6ffff97
+ 009f2870 bytes f6ffff97
- 009f282c ["INT_ADD", "register:40f0:8", ["const:9f282c:8", "const:4:8"]]
- 009f282c ["CALL", null, ["callee:00c57f80:8"]]
+ 009f2880 ["INT_ADD", "register:40f0:8", ["const:9f2880:8", "const:4:8"]]
+ 009f2880 ["CALL", null, ["callee:00c57f80:8"]]
- 009f282c bytes a1950994
+ 009f2880 bytes c0950994
~~~


<a id="compare-1a67543601beb19d0a6efdc72c568669"></a>

### [`009f2844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2844.md) → [`009f2898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2898.md) FUN_009f2898

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`009ee334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ee/009ee334.md) [`009f2844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2844.md) [`009f2894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2894.md) · 呼出先 3件 [`009f27f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f27f4.md) [`009f2844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2844.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 3件 [`009ee388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ee/009ee388.md) [`009f2898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2898.md) [`009f28e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f28e8.md) · 呼出先 3件 [`009f2848`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2848.md) [`009f2898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2898.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009f2864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2844.md#insn-009f2864) · [`009f2870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2844.md#insn-009f2870) · [`009f287c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2844.md#insn-009f287c)
- 新版 [`009f28b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2898.md#insn-009f28b8) · [`009f28c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2898.md#insn-009f28c4) · [`009f28d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2898.md#insn-009f28d0)

~~~diff
- 009f2864 ["INT_ADD", "register:40f0:8", ["const:9f2864:8", "const:4:8"]]
- 009f2864 ["CALL", null, ["local:b0:8"]]
+ 009f28b8 ["INT_ADD", "register:40f0:8", ["const:9f28b8:8", "const:4:8"]]
+ 009f28b8 ["CALL", null, ["local:b0:8"]]
- 009f2864 bytes f8ffff97
+ 009f28b8 bytes f8ffff97
- 009f2870 ["INT_ADD", "register:40f0:8", ["const:9f2870:8", "const:4:8"]]
- 009f2870 ["CALL", null, ["local:b0:8"]]
+ 009f28c4 ["INT_ADD", "register:40f0:8", ["const:9f28c4:8", "const:4:8"]]
+ 009f28c4 ["CALL", null, ["local:b0:8"]]
- 009f2870 bytes f5ffff97
+ 009f28c4 bytes f5ffff97
- 009f287c ["INT_ADD", "register:40f0:8", ["const:9f287c:8", "const:4:8"]]
- 009f287c ["CALL", null, ["callee:009f2848:8"]]
+ 009f28d0 ["INT_ADD", "register:40f0:8", ["const:9f28d0:8", "const:4:8"]]
+ 009f28d0 ["CALL", null, ["callee:009f2848:8"]]
- 009f287c bytes deffff97
+ 009f28d0 bytes deffff97
~~~


<a id="compare-161a7c10d23fee1ba09b272a84b59a1e"></a>

### [`009f2894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2894.md) → [`009f28e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f28e8.md) FUN_009f28e8

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`009f2894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2894.md) [`009f4b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4b50.md) · 呼出先 3件 [`009f2844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2844.md) [`009f2894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2894.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`009f28e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f28e8.md) [`009f4ba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4ba4.md) · 呼出先 3件 [`009f2898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2898.md) [`009f28e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f28e8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009f28b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2894.md#insn-009f28b4) · [`009f28c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2894.md#insn-009f28c0) · [`009f28cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2894.md#insn-009f28cc)
- 新版 [`009f2908`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f28e8.md#insn-009f2908) · [`009f2914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f28e8.md#insn-009f2914) · [`009f2920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f28e8.md#insn-009f2920)

~~~diff
- 009f28b4 ["INT_ADD", "register:40f0:8", ["const:9f28b4:8", "const:4:8"]]
- 009f28b4 ["CALL", null, ["local:b0:8"]]
+ 009f2908 ["INT_ADD", "register:40f0:8", ["const:9f2908:8", "const:4:8"]]
+ 009f2908 ["CALL", null, ["local:b0:8"]]
- 009f28b4 bytes f8ffff97
+ 009f2908 bytes f8ffff97
- 009f28c0 ["INT_ADD", "register:40f0:8", ["const:9f28c0:8", "const:4:8"]]
- 009f28c0 ["CALL", null, ["local:b0:8"]]
+ 009f2914 ["INT_ADD", "register:40f0:8", ["const:9f2914:8", "const:4:8"]]
+ 009f2914 ["CALL", null, ["local:b0:8"]]
- 009f28c0 bytes f5ffff97
+ 009f2914 bytes f5ffff97
- 009f28cc ["INT_ADD", "register:40f0:8", ["const:9f28cc:8", "const:4:8"]]
- 009f28cc ["CALL", null, ["callee:009f2898:8"]]
+ 009f2920 ["INT_ADD", "register:40f0:8", ["const:9f2920:8", "const:4:8"]]
+ 009f2920 ["CALL", null, ["callee:009f2898:8"]]
- 009f28cc bytes deffff97
+ 009f2920 bytes deffff97
~~~


<a id="compare-e0b6c435378111c655c43339c294a070"></a>

### [`009f28e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f28e4.md) → [`009f2938`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2938.md) FUN_009f2938

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`009f28e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f28e4.md) [`009f4b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4b50.md) · 呼出先 2件 [`009f28e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f28e4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`009f2938`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2938.md) [`009f4ba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4ba4.md) · 呼出先 2件 [`009f2938`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2938.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009f2900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f28e4.md#insn-009f2900) · [`009f290c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f28e4.md#insn-009f290c) · [`009f291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f28e4.md#insn-009f291c)
- 新版 [`009f2954`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2938.md#insn-009f2954) · [`009f2960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2938.md#insn-009f2960) · [`009f2970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2938.md#insn-009f2970)

~~~diff
- 009f2900 ["INT_ADD", "register:40f0:8", ["const:9f2900:8", "const:4:8"]]
- 009f2900 ["CALL", null, ["local:b0:8"]]
+ 009f2954 ["INT_ADD", "register:40f0:8", ["const:9f2954:8", "const:4:8"]]
+ 009f2954 ["CALL", null, ["local:b0:8"]]
- 009f2900 bytes f9ffff97
+ 009f2954 bytes f9ffff97
- 009f290c ["INT_ADD", "register:40f0:8", ["const:9f290c:8", "const:4:8"]]
- 009f290c ["CALL", null, ["local:b0:8"]]
+ 009f2960 ["INT_ADD", "register:40f0:8", ["const:9f2960:8", "const:4:8"]]
+ 009f2960 ["CALL", null, ["local:b0:8"]]
- 009f290c bytes f6ffff97
+ 009f2960 bytes f6ffff97
- 009f291c ["INT_ADD", "register:40f0:8", ["const:9f291c:8", "const:4:8"]]
- 009f291c ["CALL", null, ["callee:00c57f80:8"]]
+ 009f2970 ["INT_ADD", "register:40f0:8", ["const:9f2970:8", "const:4:8"]]
+ 009f2970 ["CALL", null, ["callee:00c57f80:8"]]
- 009f291c bytes 65950994
+ 009f2970 bytes 84950994
~~~


<a id="compare-a9d54af104707c771762b67cd94a4b44"></a>

### [`009f2934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2934.md) → [`009f2988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2988.md) FUN_009f2988

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`009f2934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2934.md) [`009f4b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4b50.md) · 呼出先 2件 [`009f2934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2934.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`009f2988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2988.md) [`009f4ba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4ba4.md) · 呼出先 2件 [`009f2988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2988.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009f2954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2934.md#insn-009f2954) · [`009f2960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2934.md#insn-009f2960)
- 新版 [`009f29a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2988.md#insn-009f29a8) · [`009f29b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2988.md#insn-009f29b4)

~~~diff
- 009f2954 ["INT_ADD", "register:40f0:8", ["const:9f2954:8", "const:4:8"]]
- 009f2954 ["CALL", null, ["local:b0:8"]]
+ 009f29a8 ["INT_ADD", "register:40f0:8", ["const:9f29a8:8", "const:4:8"]]
+ 009f29a8 ["CALL", null, ["local:b0:8"]]
- 009f2954 bytes f8ffff97
+ 009f29a8 bytes f8ffff97
- 009f2960 ["INT_ADD", "register:40f0:8", ["const:9f2960:8", "const:4:8"]]
- 009f2960 ["CALL", null, ["local:b0:8"]]
+ 009f29b4 ["INT_ADD", "register:40f0:8", ["const:9f29b4:8", "const:4:8"]]
+ 009f29b4 ["CALL", null, ["local:b0:8"]]
- 009f2960 bytes f5ffff97
+ 009f29b4 bytes f5ffff97
~~~


<a id="compare-1278b760e5258c5a0dc262d48892a252"></a>

### [`009f2978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2978.md) → [`009f29cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f29cc.md) FUN_009f29cc

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`009f2978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2978.md) [`009f4b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4b50.md) · 呼出先 2件 [`009f2978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2978.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`009f29cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f29cc.md) [`009f4ba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4ba4.md) · 呼出先 2件 [`009f29cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f29cc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009f2994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2978.md#insn-009f2994) · [`009f29a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2978.md#insn-009f29a0) · [`009f29b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2978.md#insn-009f29b0)
- 新版 [`009f29e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f29cc.md#insn-009f29e8) · [`009f29f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f29cc.md#insn-009f29f4) · [`009f2a04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f29cc.md#insn-009f2a04)

~~~diff
- 009f2994 ["INT_ADD", "register:40f0:8", ["const:9f2994:8", "const:4:8"]]
- 009f2994 ["CALL", null, ["local:b0:8"]]
+ 009f29e8 ["INT_ADD", "register:40f0:8", ["const:9f29e8:8", "const:4:8"]]
+ 009f29e8 ["CALL", null, ["local:b0:8"]]
- 009f2994 bytes f9ffff97
+ 009f29e8 bytes f9ffff97
- 009f29a0 ["INT_ADD", "register:40f0:8", ["const:9f29a0:8", "const:4:8"]]
- 009f29a0 ["CALL", null, ["local:b0:8"]]
+ 009f29f4 ["INT_ADD", "register:40f0:8", ["const:9f29f4:8", "const:4:8"]]
+ 009f29f4 ["CALL", null, ["local:b0:8"]]
- 009f29a0 bytes f6ffff97
+ 009f29f4 bytes f6ffff97
- 009f29b0 ["INT_ADD", "register:40f0:8", ["const:9f29b0:8", "const:4:8"]]
- 009f29b0 ["CALL", null, ["callee:00c57f80:8"]]
+ 009f2a04 ["INT_ADD", "register:40f0:8", ["const:9f2a04:8", "const:4:8"]]
+ 009f2a04 ["CALL", null, ["callee:00c57f80:8"]]
- 009f29b0 bytes 40950994
+ 009f2a04 bytes 5f950994
~~~


<a id="compare-974e97473ed71c2b8f55f17f70b89888"></a>

### [`009f29c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f29c8.md) → [`009f2a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2a1c.md) FUN_009f2a1c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`009f29c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f29c8.md) [`009f4b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4b50.md) · 呼出先 3件 [`009f29c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f29c8.md) [`009f2a14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2a14.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`009f2a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2a1c.md) [`009f4ba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4ba4.md) · 呼出先 3件 [`009f2a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2a1c.md) [`009f2a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2a68.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009f29e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f29c8.md#insn-009f29e8) · [`009f29f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f29c8.md#insn-009f29f4) · [`009f29fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f29c8.md#insn-009f29fc)
- 新版 [`009f2a3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2a1c.md#insn-009f2a3c) · [`009f2a48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2a1c.md#insn-009f2a48) · [`009f2a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2a1c.md#insn-009f2a50)

~~~diff
- 009f29e8 ["INT_ADD", "register:40f0:8", ["const:9f29e8:8", "const:4:8"]]
- 009f29e8 ["CALL", null, ["local:b0:8"]]
+ 009f2a3c ["INT_ADD", "register:40f0:8", ["const:9f2a3c:8", "const:4:8"]]
+ 009f2a3c ["CALL", null, ["local:b0:8"]]
- 009f29e8 bytes f8ffff97
+ 009f2a3c bytes f8ffff97
- 009f29f4 ["INT_ADD", "register:40f0:8", ["const:9f29f4:8", "const:4:8"]]
- 009f29f4 ["CALL", null, ["local:b0:8"]]
+ 009f2a48 ["INT_ADD", "register:40f0:8", ["const:9f2a48:8", "const:4:8"]]
+ 009f2a48 ["CALL", null, ["local:b0:8"]]
- 009f29f4 bytes f5ffff97
+ 009f2a48 bytes f5ffff97
- 009f29fc ["INT_ADD", "register:40f0:8", ["const:9f29fc:8", "const:4:8"]]
- 009f29fc ["CALL", null, ["callee:009f2a68:8"]]
+ 009f2a50 ["INT_ADD", "register:40f0:8", ["const:9f2a50:8", "const:4:8"]]
+ 009f2a50 ["CALL", null, ["callee:009f2a68:8"]]
- 009f29fc bytes 06000094
+ 009f2a50 bytes 06000094
~~~


<a id="compare-7d9e4b062d266b47ca72f9e62a03424a"></a>

### [`009f2ad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2ad8.md) → [`009f2b2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2b2c.md) FUN_009f2b2c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`009f2ad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2ad8.md) [`009f4b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4b50.md) · 呼出先 2件 [`009f2ad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2ad8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`009f2b2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2b2c.md) [`009f4ba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4ba4.md) · 呼出先 2件 [`009f2b2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2b2c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009f2af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2ad8.md#insn-009f2af8) · [`009f2b04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2ad8.md#insn-009f2b04)
- 新版 [`009f2b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2b2c.md#insn-009f2b4c) · [`009f2b58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2b2c.md#insn-009f2b58)

~~~diff
- 009f2af8 ["INT_ADD", "register:40f0:8", ["const:9f2af8:8", "const:4:8"]]
- 009f2af8 ["CALL", null, ["local:b0:8"]]
+ 009f2b4c ["INT_ADD", "register:40f0:8", ["const:9f2b4c:8", "const:4:8"]]
+ 009f2b4c ["CALL", null, ["local:b0:8"]]
- 009f2af8 bytes f8ffff97
+ 009f2b4c bytes f8ffff97
- 009f2b04 ["INT_ADD", "register:40f0:8", ["const:9f2b04:8", "const:4:8"]]
- 009f2b04 ["CALL", null, ["local:b0:8"]]
+ 009f2b58 ["INT_ADD", "register:40f0:8", ["const:9f2b58:8", "const:4:8"]]
+ 009f2b58 ["CALL", null, ["local:b0:8"]]
- 009f2b04 bytes f5ffff97
+ 009f2b58 bytes f5ffff97
~~~


<a id="compare-aec77f3f2546d7eaf7375bb5a9715317"></a>

### [`009f2b1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2b1c.md) → [`009f2b70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2b70.md) FUN_009f2b70

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1048.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`009f2de4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2de4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`009f109c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f109c.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`009f2e38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2e38.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009f2ba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2b1c.md#insn-009f2ba0) · [`009f2bd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2b1c.md#insn-009f2bd8) · [`009f2ce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2b1c.md#insn-009f2ce0)
- 新版 [`009f2bf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2b70.md#insn-009f2bf4) · [`009f2c2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2b70.md#insn-009f2c2c) · [`009f2d34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2b70.md#insn-009f2d34)

~~~diff
- 009f2ba0 ["INT_ADD", "register:40f0:8", ["const:9f2ba0:8", "const:4:8"]]
- 009f2ba0 ["CALL", null, ["callee:00c57f60:8"]]
+ 009f2bf4 ["INT_ADD", "register:40f0:8", ["const:9f2bf4:8", "const:4:8"]]
+ 009f2bf4 ["CALL", null, ["callee:00c57f60:8"]]
- 009f2ba0 bytes bc940994
+ 009f2bf4 bytes db940994
- 009f2bd8 ["INT_ADD", "register:40f0:8", ["const:9f2bd8:8", "const:4:8"]]
- 009f2bd8 ["CALL", null, ["callee:00c58010:8"]]
+ 009f2c2c ["INT_ADD", "register:40f0:8", ["const:9f2c2c:8", "const:4:8"]]
+ 009f2c2c ["CALL", null, ["callee:00c58010:8"]]
- 009f2bd8 bytes da940994
+ 009f2c2c bytes f9940994
- 009f2ce0 ["INT_ADD", "register:40f0:8", ["const:9f2ce0:8", "const:4:8"]]
- 009f2ce0 ["CALL", null, ["callee:00c580d0:8"]]
+ 009f2d34 ["INT_ADD", "register:40f0:8", ["const:9f2d34:8", "const:4:8"]]
+ 009f2d34 ["CALL", null, ["callee:00c580d0:8"]]
- 009f2ce0 bytes c8940994
+ 009f2d34 bytes e7940994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31c6851528b2095de2726e3995fa52e6"></a>

### [`009f2e64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2e64.md) → [`009f2eb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2eb8.md) FUN_009f2eb8

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009ec078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ec/009ec078.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`009f2fa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2fa4.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`009ec0cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ec/009ec0cc.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`009f2ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2ff8.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009f2ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2e64.md#insn-009f2ed0) · [`009f2f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2e64.md#insn-009f2f40) · [`009f2f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2e64.md#insn-009f2f54)
- 新版 [`009f2f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2eb8.md#insn-009f2f24) · [`009f2f94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2eb8.md#insn-009f2f94) · [`009f2fa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2eb8.md#insn-009f2fa8)

~~~diff
- 009f2ed0 ["INT_ADD", "register:40f0:8", ["const:9f2ed0:8", "const:4:8"]]
- 009f2ed0 ["CALL", null, ["callee:00c57f60:8"]]
+ 009f2f24 ["INT_ADD", "register:40f0:8", ["const:9f2f24:8", "const:4:8"]]
+ 009f2f24 ["CALL", null, ["callee:00c57f60:8"]]
- 009f2ed0 bytes f0930994
+ 009f2f24 bytes 0f940994
- 009f2f40 ["INT_ADD", "register:40f0:8", ["const:9f2f40:8", "const:4:8"]]
- 009f2f40 ["CALL", null, ["callee:00c53da0:8"]]
+ 009f2f94 ["INT_ADD", "register:40f0:8", ["const:9f2f94:8", "const:4:8"]]
+ 009f2f94 ["CALL", null, ["callee:00c53da0:8"]]
- 009f2f40 bytes 70830994
+ 009f2f94 bytes 83830994
- 009f2f54 ["COPY", "register:0:8", ["register:4040:8"]]
- 009f2f54 ["INT_ADD", "register:40f0:8", ["const:9f2f54:8", "const:4:8"]]
- 009f2f54 ["CALLIND", null, ["register:0:8"]]
+ 009f2fa8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009f2fa8 ["INT_ADD", "register:40f0:8", ["const:9f2fa8:8", "const:4:8"]]
+ 009f2fa8 ["CALLIND", null, ["register:0:8"]]
- 009f2f54 bytes 00013fd6
+ 009f2fa8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32f9b3c53a6adc883e3c2c8813648b80"></a>

### [`009f3610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3610.md) → [`009f3664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3664.md) FUN_009f3664

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009ed5b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ed/009ed5b8.md) · 呼出先 3件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`009ed60c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ed/009ed60c.md) · 呼出先 3件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009f3630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3610.md#insn-009f3630) · [`009f36cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3610.md#insn-009f36cc) · [`009f36f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3610.md#insn-009f36f0)
- 新版 [`009f3684`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3664.md#insn-009f3684) · [`009f3720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3664.md#insn-009f3720) · [`009f3744`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3664.md#insn-009f3744)

~~~diff
- 009f3630 ["INT_ADD", "register:40f0:8", ["const:9f3630:8", "const:4:8"]]
- 009f3630 ["CALL", null, ["callee:00c57f60:8"]]
+ 009f3684 ["INT_ADD", "register:40f0:8", ["const:9f3684:8", "const:4:8"]]
+ 009f3684 ["CALL", null, ["callee:00c57f60:8"]]
- 009f3630 bytes 18920994
+ 009f3684 bytes 37920994
- 009f36cc ["INT_ADD", "register:40f0:8", ["const:9f36cc:8", "const:4:8"]]
- 009f36cc ["CALL", null, ["callee:0043bbe4:8"]]
+ 009f3720 ["INT_ADD", "register:40f0:8", ["const:9f3720:8", "const:4:8"]]
+ 009f3720 ["CALL", null, ["callee:0043bbe4:8"]]
- 009f36cc bytes 3621e997
+ 009f3720 bytes 3121e997
- 009f36f0 ["INT_ADD", "register:40f0:8", ["const:9f36f0:8", "const:4:8"]]
- 009f36f0 ["CALL", null, ["callee:00c57f80:8"]]
+ 009f3744 ["INT_ADD", "register:40f0:8", ["const:9f3744:8", "const:4:8"]]
+ 009f3744 ["CALL", null, ["callee:00c57f80:8"]]
- 009f36f0 bytes f0910994
+ 009f3744 bytes 0f920994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e95957fe1936f9a23044c1bcf8aade29"></a>

### [`009f3718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3718.md) → [`009f376c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f376c.md) FUN_009f376c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f45a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f45a4.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`009f45f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f45f8.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009f3744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3718.md#insn-009f3744)
- 新版 [`009f3798`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f376c.md#insn-009f3798)

~~~diff
- 009f3744 ["INT_ADD", "register:40f0:8", ["const:9f3744:8", "const:4:8"]]
- 009f3744 ["CALL", null, ["callee:00c57f80:8"]]
+ 009f3798 ["INT_ADD", "register:40f0:8", ["const:9f3798:8", "const:4:8"]]
+ 009f3798 ["CALL", null, ["callee:00c57f80:8"]]
- 009f3744 bytes db910994
+ 009f3798 bytes fa910994
~~~


<a id="compare-d46bfa5eb3119aa8aebc03832340a1cf"></a>

### [`009f3764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3764.md) → [`009f37b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f37b8.md) FUN_009f37b8

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`009eee28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ee/009eee28.md) [`009f1048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1048.md) [`009f1e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1e4c.md) [`009f3764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3764.md) [`009f37b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f37b4.md) · 呼出先 2件 [`009f3764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3764.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 6件 [`009eee7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ee/009eee7c.md) [`009f109c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f109c.md) [`009f1ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f1ea0.md) [`009f37b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f37b8.md) [`009f3808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3808.md) · 呼出先 2件 [`009f37b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f37b8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009f3780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3764.md#insn-009f3780) · [`009f378c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3764.md#insn-009f378c) · [`009f379c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3764.md#insn-009f379c)
- 新版 [`009f37d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f37b8.md#insn-009f37d4) · [`009f37e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f37b8.md#insn-009f37e0) · [`009f37f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f37b8.md#insn-009f37f0)

~~~diff
- 009f3780 ["INT_ADD", "register:40f0:8", ["const:9f3780:8", "const:4:8"]]
- 009f3780 ["CALL", null, ["local:b0:8"]]
+ 009f37d4 ["INT_ADD", "register:40f0:8", ["const:9f37d4:8", "const:4:8"]]
+ 009f37d4 ["CALL", null, ["local:b0:8"]]
- 009f3780 bytes f9ffff97
+ 009f37d4 bytes f9ffff97
- 009f378c ["INT_ADD", "register:40f0:8", ["const:9f378c:8", "const:4:8"]]
- 009f378c ["CALL", null, ["local:b0:8"]]
+ 009f37e0 ["INT_ADD", "register:40f0:8", ["const:9f37e0:8", "const:4:8"]]
+ 009f37e0 ["CALL", null, ["local:b0:8"]]
- 009f378c bytes f6ffff97
+ 009f37e0 bytes f6ffff97
- 009f379c ["INT_ADD", "register:40f0:8", ["const:9f379c:8", "const:4:8"]]
- 009f379c ["CALL", null, ["callee:00c57f80:8"]]
+ 009f37f0 ["INT_ADD", "register:40f0:8", ["const:9f37f0:8", "const:4:8"]]
+ 009f37f0 ["CALL", null, ["callee:00c57f80:8"]]
- 009f379c bytes c5910994
+ 009f37f0 bytes e4910994
~~~


<a id="compare-d69df6c15e5f6f23714aea407c2ef849"></a>

### [`009f37b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f37b4.md) → [`009f3808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3808.md) FUN_009f3808

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`009f3764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3764.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`009f37b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f37b8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009f37dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f37b4.md#insn-009f37dc)
- 新版 [`009f3830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3808.md#insn-009f3830)

~~~diff
- 009f37dc ["INT_ADD", "register:40f0:8", ["const:9f37dc:8", "const:4:8"]]
- 009f37dc ["CALL", null, ["callee:009f37b8:8"]]
+ 009f3830 ["INT_ADD", "register:40f0:8", ["const:9f3830:8", "const:4:8"]]
+ 009f3830 ["CALL", null, ["callee:009f37b8:8"]]
- 009f37dc bytes e2ffff97
+ 009f3830 bytes e2ffff97
~~~


<a id="compare-ffe0f311cc6573acd8330549892783b9"></a>

### [`009f37fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f37fc.md) → [`009f3850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3850.md) FUN_009f3850

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`009ef024`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ef/009ef024.md) [`009f0d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f0/009f0d34.md) [`009f1e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1e4c.md) [`009f37fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f37fc.md) [`009f384c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f384c.md) · 呼出先 3件 [`009f3764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3764.md) [`009f37fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f37fc.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 6件 [`009ef078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009ef078.md) [`009f0d88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f0/009f0d88.md) [`009f1ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f1ea0.md) [`009f3850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3850.md) [`009f38a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f38a0.md) · 呼出先 3件 [`009f37b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f37b8.md) [`009f3850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3850.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009f381c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f37fc.md#insn-009f381c) · [`009f3828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f37fc.md#insn-009f3828) · [`009f3834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f37fc.md#insn-009f3834)
- 新版 [`009f3870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3850.md#insn-009f3870) · [`009f387c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3850.md#insn-009f387c) · [`009f3888`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3850.md#insn-009f3888)

~~~diff
- 009f381c ["INT_ADD", "register:40f0:8", ["const:9f381c:8", "const:4:8"]]
- 009f381c ["CALL", null, ["local:b0:8"]]
+ 009f3870 ["INT_ADD", "register:40f0:8", ["const:9f3870:8", "const:4:8"]]
+ 009f3870 ["CALL", null, ["local:b0:8"]]
- 009f381c bytes f8ffff97
+ 009f3870 bytes f8ffff97
- 009f3828 ["INT_ADD", "register:40f0:8", ["const:9f3828:8", "const:4:8"]]
- 009f3828 ["CALL", null, ["local:b0:8"]]
+ 009f387c ["INT_ADD", "register:40f0:8", ["const:9f387c:8", "const:4:8"]]
+ 009f387c ["CALL", null, ["local:b0:8"]]
- 009f3828 bytes f5ffff97
+ 009f387c bytes f5ffff97
- 009f3834 ["INT_ADD", "register:40f0:8", ["const:9f3834:8", "const:4:8"]]
- 009f3834 ["CALL", null, ["callee:009f37b8:8"]]
+ 009f3888 ["INT_ADD", "register:40f0:8", ["const:9f3888:8", "const:4:8"]]
+ 009f3888 ["CALL", null, ["callee:009f37b8:8"]]
- 009f3834 bytes ccffff97
+ 009f3888 bytes ccffff97
~~~


<a id="compare-ac5fc0c09ea30b03ffd13ad8855711e6"></a>

### [`009f384c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f384c.md) → [`009f38a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f38a0.md) FUN_009f38a0

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`009f37fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f37fc.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`009f3850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3850.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009f3874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f384c.md#insn-009f3874)
- 新版 [`009f38c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f38a0.md#insn-009f38c8)

~~~diff
- 009f3874 ["INT_ADD", "register:40f0:8", ["const:9f3874:8", "const:4:8"]]
- 009f3874 ["CALL", null, ["callee:009f3850:8"]]
+ 009f38c8 ["INT_ADD", "register:40f0:8", ["const:9f38c8:8", "const:4:8"]]
+ 009f38c8 ["CALL", null, ["callee:009f3850:8"]]
- 009f3874 bytes e2ffff97
+ 009f38c8 bytes e2ffff97
~~~


<a id="compare-d1bdb791c4327417bc0d97c87ff15605"></a>

### [`009f3894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3894.md) → [`009f38e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f38e8.md) FUN_009f38e8

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`009f0d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f0/009f0d34.md) [`009f1978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1978.md) [`009f1e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1e4c.md) [`009f3894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3894.md) [`009f4b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4b50.md) · 呼出先 3件 [`009f37fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f37fc.md) [`009f3894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3894.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 5件 [`009f0d88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f0/009f0d88.md) [`009f19cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f19cc.md) [`009f1ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f1ea0.md) [`009f38e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f38e8.md) [`009f4ba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4ba4.md) · 呼出先 3件 [`009f3850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3850.md) [`009f38e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f38e8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009f38b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3894.md#insn-009f38b4) · [`009f38c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3894.md#insn-009f38c0) · [`009f38cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3894.md#insn-009f38cc)
- 新版 [`009f3908`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f38e8.md#insn-009f3908) · [`009f3914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f38e8.md#insn-009f3914) · [`009f3920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f38e8.md#insn-009f3920)

~~~diff
- 009f38b4 ["INT_ADD", "register:40f0:8", ["const:9f38b4:8", "const:4:8"]]
- 009f38b4 ["CALL", null, ["local:b0:8"]]
+ 009f3908 ["INT_ADD", "register:40f0:8", ["const:9f3908:8", "const:4:8"]]
+ 009f3908 ["CALL", null, ["local:b0:8"]]
- 009f38b4 bytes f8ffff97
+ 009f3908 bytes f8ffff97
- 009f38c0 ["INT_ADD", "register:40f0:8", ["const:9f38c0:8", "const:4:8"]]
- 009f38c0 ["CALL", null, ["local:b0:8"]]
+ 009f3914 ["INT_ADD", "register:40f0:8", ["const:9f3914:8", "const:4:8"]]
+ 009f3914 ["CALL", null, ["local:b0:8"]]
- 009f38c0 bytes f5ffff97
+ 009f3914 bytes f5ffff97
- 009f38cc ["INT_ADD", "register:40f0:8", ["const:9f38cc:8", "const:4:8"]]
- 009f38cc ["CALL", null, ["callee:009f3850:8"]]
+ 009f3920 ["INT_ADD", "register:40f0:8", ["const:9f3920:8", "const:4:8"]]
+ 009f3920 ["CALL", null, ["callee:009f3850:8"]]
- 009f38cc bytes ccffff97
+ 009f3920 bytes ccffff97
~~~


<a id="compare-a386ef80e39f4246e81ee43b22f4422e"></a>

### [`009f38e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f38e4.md) → [`009f3938`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3938.md) FUN_009f3938

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009ef66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ef/009ef66c.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`009ef6c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009ef6c0.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009f3950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f38e4.md#insn-009f3950) · [`009f3960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f38e4.md#insn-009f3960) · [`009f3980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f38e4.md#insn-009f3980)
- 新版 [`009f39a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3938.md#insn-009f39a4) · [`009f39b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3938.md#insn-009f39b4) · [`009f39d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3938.md#insn-009f39d4)

~~~diff
- 009f3950 ["COPY", "register:0:8", ["register:4040:8"]]
- 009f3950 ["INT_ADD", "register:40f0:8", ["const:9f3950:8", "const:4:8"]]
- 009f3950 ["CALLIND", null, ["register:0:8"]]
+ 009f39a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009f39a4 ["INT_ADD", "register:40f0:8", ["const:9f39a4:8", "const:4:8"]]
+ 009f39a4 ["CALLIND", null, ["register:0:8"]]
- 009f3950 bytes 00013fd6
+ 009f39a4 bytes 00013fd6
- 009f3960 ["COPY", "register:0:8", ["register:4040:8"]]
- 009f3960 ["INT_ADD", "register:40f0:8", ["const:9f3960:8", "const:4:8"]]
- 009f3960 ["CALLIND", null, ["register:0:8"]]
+ 009f39b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009f39b4 ["INT_ADD", "register:40f0:8", ["const:9f39b4:8", "const:4:8"]]
+ 009f39b4 ["CALLIND", null, ["register:0:8"]]
- 009f3960 bytes 00013fd6
+ 009f39b4 bytes 00013fd6
- 009f3980 ["COPY", "register:0:8", ["register:4040:8"]]
- 009f3980 ["INT_ADD", "register:40f0:8", ["const:9f3980:8", "const:4:8"]]
- 009f3980 ["CALLIND", null, ["register:0:8"]]
+ 009f39d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009f39d4 ["INT_ADD", "register:40f0:8", ["const:9f39d4:8", "const:4:8"]]
+ 009f39d4 ["CALLIND", null, ["register:0:8"]]
- 009f3980 bytes 00013fd6
+ 009f39d4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1cd8e4041481cd41226977aab68bc5a"></a>

### [`009f3acc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3acc.md) → [`009f3b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3b20.md) FUN_009f3b20

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009efde8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ef/009efde8.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`009f3c58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3c58.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`009efe3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ef/009efe3c.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`009f3cac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3cac.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009f3b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3acc.md#insn-009f3b58) · [`009f3c10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3acc.md#insn-009f3c10) · [`009f3c2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3acc.md#insn-009f3c2c)
- 新版 [`009f3bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3b20.md#insn-009f3bac) · [`009f3c64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3b20.md#insn-009f3c64) · [`009f3c80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3b20.md#insn-009f3c80)

~~~diff
- 009f3b58 ["INT_ADD", "register:40f0:8", ["const:9f3b58:8", "const:4:8"]]
- 009f3b58 ["CALL", null, ["callee:00c57f60:8"]]
+ 009f3bac ["INT_ADD", "register:40f0:8", ["const:9f3bac:8", "const:4:8"]]
+ 009f3bac ["CALL", null, ["callee:00c57f60:8"]]
- 009f3b58 bytes ce900994
+ 009f3bac bytes ed900994
- 009f3c10 ["INT_ADD", "register:40f0:8", ["const:9f3c10:8", "const:4:8"]]
- 009f3c10 ["CALL", null, ["callee:00c57f80:8"]]
+ 009f3c64 ["INT_ADD", "register:40f0:8", ["const:9f3c64:8", "const:4:8"]]
+ 009f3c64 ["CALL", null, ["callee:00c57f80:8"]]
- 009f3c10 bytes a8900994
+ 009f3c64 bytes c7900994
- 009f3c2c ["INT_ADD", "register:40f0:8", ["const:9f3c2c:8", "const:4:8"]]
- 009f3c2c ["CALL", null, ["callee:00c57f80:8"]]
+ 009f3c80 ["INT_ADD", "register:40f0:8", ["const:9f3c80:8", "const:4:8"]]
+ 009f3c80 ["CALL", null, ["callee:00c57f80:8"]]
- 009f3c2c bytes a1900994
+ 009f3c80 bytes c0900994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2429b18f996b64ba333202add003fd3"></a>

### [`009f3c6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3c6c.md) → [`009f3cc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3cc0.md) FUN_009f3cc0

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f050c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f0/009f050c.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`009f3ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3ab8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`009f0560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f0/009f0560.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`009f3b0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3b0c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009f3cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3c6c.md#insn-009f3cf0) · [`009f3d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3c6c.md#insn-009f3d28) · [`009f3e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3c6c.md#insn-009f3e30)
- 新版 [`009f3d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3cc0.md#insn-009f3d44) · [`009f3d7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3cc0.md#insn-009f3d7c) · [`009f3e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3cc0.md#insn-009f3e84)

~~~diff
- 009f3cf0 ["INT_ADD", "register:40f0:8", ["const:9f3cf0:8", "const:4:8"]]
- 009f3cf0 ["CALL", null, ["callee:00c57f60:8"]]
+ 009f3d44 ["INT_ADD", "register:40f0:8", ["const:9f3d44:8", "const:4:8"]]
+ 009f3d44 ["CALL", null, ["callee:00c57f60:8"]]
- 009f3cf0 bytes 68900994
+ 009f3d44 bytes 87900994
- 009f3d28 ["INT_ADD", "register:40f0:8", ["const:9f3d28:8", "const:4:8"]]
- 009f3d28 ["CALL", null, ["callee:00c58010:8"]]
+ 009f3d7c ["INT_ADD", "register:40f0:8", ["const:9f3d7c:8", "const:4:8"]]
+ 009f3d7c ["CALL", null, ["callee:00c58010:8"]]
- 009f3d28 bytes 86900994
+ 009f3d7c bytes a5900994
- 009f3e30 ["INT_ADD", "register:40f0:8", ["const:9f3e30:8", "const:4:8"]]
- 009f3e30 ["CALL", null, ["callee:00c580d0:8"]]
+ 009f3e84 ["INT_ADD", "register:40f0:8", ["const:9f3e84:8", "const:4:8"]]
+ 009f3e84 ["CALL", null, ["callee:00c580d0:8"]]
- 009f3e30 bytes 74900994
+ 009f3e84 bytes 93900994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3323af8b84fee312cb160e965031334"></a>

### [`009f3f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3f34.md) → [`009f3f88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3f88.md) FUN_009f3f88

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`009f0d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f0/009f0d34.md) [`009f1978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1978.md) [`009f1e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1e4c.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`009f4050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4050.md) [`009f41f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f41f8.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 3件 [`009f0d88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f0/009f0d88.md) [`009f19cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f19cc.md) [`009f1ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f1ea0.md) · 呼出先 4件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`009f40a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f40a4.md) [`009f424c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f424c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009f3f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3f34.md#insn-009f3f90) · [`009f3fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3f34.md#insn-009f3fb8) · [`009f3fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3f34.md#insn-009f3fe4)
- 新版 [`009f3fe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3f88.md#insn-009f3fe4) · [`009f400c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3f88.md#insn-009f400c) · [`009f4038`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3f88.md#insn-009f4038)

~~~diff
- 009f3f90 ["INT_ADD", "register:40f0:8", ["const:9f3f90:8", "const:4:8"]]
- 009f3f90 ["CALL", null, ["callee:009f40a4:8"]]
+ 009f3fe4 ["INT_ADD", "register:40f0:8", ["const:9f3fe4:8", "const:4:8"]]
+ 009f3fe4 ["CALL", null, ["callee:009f40a4:8"]]
- 009f3f90 bytes 30000094
+ 009f3fe4 bytes 30000094
- 009f3fb8 ["INT_ADD", "register:40f0:8", ["const:9f3fb8:8", "const:4:8"]]
- 009f3fb8 ["CALL", null, ["callee:009f424c:8"]]
+ 009f400c ["INT_ADD", "register:40f0:8", ["const:9f400c:8", "const:4:8"]]
+ 009f400c ["CALL", null, ["callee:009f424c:8"]]
- 009f3fb8 bytes 90000094
+ 009f400c bytes 90000094
- 009f3fe4 ["INT_ADD", "register:40f0:8", ["const:9f3fe4:8", "const:4:8"]]
- 009f3fe4 ["CALL", null, ["callee:0043bbe4:8"]]
+ 009f4038 ["INT_ADD", "register:40f0:8", ["const:9f4038:8", "const:4:8"]]
+ 009f4038 ["CALL", null, ["callee:0043bbe4:8"]]
- 009f3fe4 bytes f01ee997
+ 009f4038 bytes eb1ee997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60f25dd0ee25e0398abe5b85a92cd7be"></a>

### [`009f41f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f41f8.md) → [`009f424c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f424c.md) FUN_009f424c

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f3f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3f34.md) · 呼出先 2件 [`009f466c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f466c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`009f3f88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3f88.md) · 呼出先 2件 [`009f46c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f46c0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009f421c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f41f8.md#insn-009f421c) · [`009f428c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f41f8.md#insn-009f428c)
- 新版 [`009f4270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f424c.md#insn-009f4270) · [`009f42e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f424c.md#insn-009f42e0)

~~~diff
- 009f421c ["INT_ADD", "register:40f0:8", ["const:9f421c:8", "const:4:8"]]
- 009f421c ["CALL", null, ["callee:00c57f60:8"]]
+ 009f4270 ["INT_ADD", "register:40f0:8", ["const:9f4270:8", "const:4:8"]]
+ 009f4270 ["CALL", null, ["callee:00c57f60:8"]]
- 009f421c bytes 1d8f0994
+ 009f4270 bytes 3c8f0994
- 009f428c ["INT_ADD", "register:40f0:8", ["const:9f428c:8", "const:4:8"]]
- 009f428c ["CALL", null, ["callee:009f46c0:8"]]
+ 009f42e0 ["INT_ADD", "register:40f0:8", ["const:9f42e0:8", "const:4:8"]]
+ 009f42e0 ["CALL", null, ["callee:009f46c0:8"]]
- 009f428c bytes f8000094
+ 009f42e0 bytes f8000094
~~~


<a id="compare-910fe38db5a3fc7e73943ac863f3d917"></a>

### [`009f42e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f42e0.md) → [`009f4334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4334.md) FUN_009f4334

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`009f1048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1048.md) [`009f1e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1e4c.md) [`009f466c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f466c.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`009f43fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f43fc.md) [`009f45a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f45a4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 3件 [`009f109c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f109c.md) [`009f1ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f1ea0.md) [`009f46c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f46c0.md) · 呼出先 4件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`009f4450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4450.md) [`009f45f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f45f8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009f433c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f42e0.md#insn-009f433c) · [`009f4364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f42e0.md#insn-009f4364) · [`009f4390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f42e0.md#insn-009f4390)
- 新版 [`009f4390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4334.md#insn-009f4390) · [`009f43b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4334.md#insn-009f43b8) · [`009f43e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4334.md#insn-009f43e4)

~~~diff
- 009f433c ["INT_ADD", "register:40f0:8", ["const:9f433c:8", "const:4:8"]]
- 009f433c ["CALL", null, ["callee:009f4450:8"]]
+ 009f4390 ["INT_ADD", "register:40f0:8", ["const:9f4390:8", "const:4:8"]]
+ 009f4390 ["CALL", null, ["callee:009f4450:8"]]
- 009f433c bytes 30000094
+ 009f4390 bytes 30000094
- 009f4364 ["INT_ADD", "register:40f0:8", ["const:9f4364:8", "const:4:8"]]
- 009f4364 ["CALL", null, ["callee:009f45f8:8"]]
+ 009f43b8 ["INT_ADD", "register:40f0:8", ["const:9f43b8:8", "const:4:8"]]
+ 009f43b8 ["CALL", null, ["callee:009f45f8:8"]]
- 009f4364 bytes 90000094
+ 009f43b8 bytes 90000094
- 009f4390 ["INT_ADD", "register:40f0:8", ["const:9f4390:8", "const:4:8"]]
- 009f4390 ["CALL", null, ["callee:0043bbe4:8"]]
+ 009f43e4 ["INT_ADD", "register:40f0:8", ["const:9f43e4:8", "const:4:8"]]
+ 009f43e4 ["CALL", null, ["callee:0043bbe4:8"]]
- 009f4390 bytes 051ee997
+ 009f43e4 bytes 001ee997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38f7d05ed46a3f40db179a680d993dd9"></a>

### [`009f45a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f45a4.md) → [`009f45f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f45f8.md) FUN_009f45f8

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f42e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f42e0.md) · 呼出先 6件 [`009f2de4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f2/009f2de4.md) [`009f3718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3718.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`009f4334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4334.md) · 呼出先 6件 [`009f2e38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f2/009f2e38.md) [`009f376c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f376c.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009f45c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f45a4.md#insn-009f45c8) · [`009f4600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f45a4.md#insn-009f4600) · [`009f4618`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f45a4.md#insn-009f4618)
- 新版 [`009f461c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f45f8.md#insn-009f461c) · [`009f4654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f45f8.md#insn-009f4654) · [`009f466c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f45f8.md#insn-009f466c)

~~~diff
- 009f45c8 ["INT_ADD", "register:40f0:8", ["const:9f45c8:8", "const:4:8"]]
- 009f45c8 ["CALL", null, ["callee:00c57f60:8"]]
+ 009f461c ["INT_ADD", "register:40f0:8", ["const:9f461c:8", "const:4:8"]]
+ 009f461c ["CALL", null, ["callee:00c57f60:8"]]
- 009f45c8 bytes 328e0994
+ 009f461c bytes 518e0994
- 009f4600 ["INT_ADD", "register:40f0:8", ["const:9f4600:8", "const:4:8"]]
- 009f4600 ["CALL", null, ["callee:00c57f60:8"]]
+ 009f4654 ["INT_ADD", "register:40f0:8", ["const:9f4654:8", "const:4:8"]]
+ 009f4654 ["CALL", null, ["callee:00c57f60:8"]]
- 009f4600 bytes 248e0994
+ 009f4654 bytes 438e0994
- 009f4618 ["INT_ADD", "register:40f0:8", ["const:9f4618:8", "const:4:8"]]
- 009f4618 ["CALL", null, ["callee:00c580d0:8"]]
+ 009f466c ["INT_ADD", "register:40f0:8", ["const:9f466c:8", "const:4:8"]]
+ 009f466c ["CALL", null, ["callee:00c580d0:8"]]
- 009f4618 bytes 7a8e0994
+ 009f466c bytes 998e0994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-366bbdcbf993b2df49bcb30696c9a052"></a>

### [`009f466c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f466c.md) → [`009f46c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f46c0.md) FUN_009f46c0

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`009f0d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f0/009f0d34.md) [`009f1e4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1e4c.md) [`009f41f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f41f8.md) · 呼出先 5件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`009f42e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f42e0.md) [`009f47a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f47a8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 3件 [`009f0d88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f0/009f0d88.md) [`009f1ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f1ea0.md) [`009f424c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f424c.md) · 呼出先 5件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`009f4334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f4334.md) [`009f47fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f47fc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009f46a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f466c.md#insn-009f46a8) · [`009f46c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f466c.md#insn-009f46c8) · [`009f4700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f466c.md#insn-009f4700)
- 新版 [`009f46fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f46c0.md#insn-009f46fc) · [`009f471c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f46c0.md#insn-009f471c) · [`009f4754`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f46c0.md#insn-009f4754)

~~~diff
- 009f46a8 ["INT_ADD", "register:40f0:8", ["const:9f46a8:8", "const:4:8"]]
- 009f46a8 ["CALL", null, ["callee:009f47fc:8"]]
+ 009f46fc ["INT_ADD", "register:40f0:8", ["const:9f46fc:8", "const:4:8"]]
+ 009f46fc ["CALL", null, ["callee:009f47fc:8"]]
- 009f46a8 bytes 40000094
+ 009f46fc bytes 40000094
- 009f46c8 ["INT_ADD", "register:40f0:8", ["const:9f46c8:8", "const:4:8"]]
- 009f46c8 ["CALL", null, ["callee:00c57f60:8"]]
+ 009f471c ["INT_ADD", "register:40f0:8", ["const:9f471c:8", "const:4:8"]]
+ 009f471c ["CALL", null, ["callee:00c57f60:8"]]
- 009f46c8 bytes f28d0994
+ 009f471c bytes 118e0994
- 009f4700 ["INT_ADD", "register:40f0:8", ["const:9f4700:8", "const:4:8"]]
- 009f4700 ["CALL", null, ["callee:009f4334:8"]]
+ 009f4754 ["INT_ADD", "register:40f0:8", ["const:9f4754:8", "const:4:8"]]
+ 009f4754 ["CALL", null, ["callee:009f4334:8"]]
- 009f4700 bytes f8feff97
+ 009f4754 bytes f8feff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-638bb5d40bb8dd6806b29d18bd279d84"></a>

### [`009f4950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4950.md) → [`009f49a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f49a4.md) FUN_009f49a4

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f1200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f1/009f1200.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`009f3c58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f3/009f3c58.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`009f1254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f1/009f1254.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`009f3cac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f3/009f3cac.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009f49dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4950.md#insn-009f49dc) · [`009f4a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4950.md#insn-009f4a94) · [`009f4ab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f4/009f4950.md#insn-009f4ab0)
- 新版 [`009f4a30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f49a4.md#insn-009f4a30) · [`009f4ae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f49a4.md#insn-009f4ae8) · [`009f4b04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f4/009f49a4.md#insn-009f4b04)

~~~diff
- 009f49dc ["INT_ADD", "register:40f0:8", ["const:9f49dc:8", "const:4:8"]]
- 009f49dc ["CALL", null, ["callee:00c57f60:8"]]
+ 009f4a30 ["INT_ADD", "register:40f0:8", ["const:9f4a30:8", "const:4:8"]]
+ 009f4a30 ["CALL", null, ["callee:00c57f60:8"]]
- 009f49dc bytes 2d8d0994
+ 009f4a30 bytes 4c8d0994
- 009f4a94 ["INT_ADD", "register:40f0:8", ["const:9f4a94:8", "const:4:8"]]
- 009f4a94 ["CALL", null, ["callee:00c57f80:8"]]
+ 009f4ae8 ["INT_ADD", "register:40f0:8", ["const:9f4ae8:8", "const:4:8"]]
+ 009f4ae8 ["CALL", null, ["callee:00c57f80:8"]]
- 009f4a94 bytes 078d0994
+ 009f4ae8 bytes 268d0994
- 009f4ab0 ["INT_ADD", "register:40f0:8", ["const:9f4ab0:8", "const:4:8"]]
- 009f4ab0 ["CALL", null, ["callee:00c57f80:8"]]
+ 009f4b04 ["INT_ADD", "register:40f0:8", ["const:9f4b04:8", "const:4:8"]]
+ 009f4b04 ["CALL", null, ["callee:00c57f80:8"]]
- 009f4ab0 bytes 008d0994
+ 009f4b04 bytes 1f8d0994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-700199923b16b8960917113cb15f089f"></a>

### [`009f9d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f9/009f9d10.md) → [`009f9d64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f9/009f9d64.md) FUN_009f9d64

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009ff40c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ff40c.md) · 呼出先 6件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`009df8c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009df/009df8c4.md) [`009e2f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e2/009e2f94.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)
- 新版 呼出元 1件 [`009ff460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ff/009ff460.md) · 呼出先 6件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`009df918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009df/009df918.md) [`009e2fe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e2/009e2fe8.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009f9d3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f9/009f9d10.md#insn-009f9d3c) · [`009f9d4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f9/009f9d10.md#insn-009f9d4c) · [`009f9d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f9/009f9d10.md#insn-009f9d68)
- 新版 [`009f9d90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f9/009f9d64.md#insn-009f9d90) · [`009f9da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f9/009f9d64.md#insn-009f9da0) · [`009f9dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f9/009f9d64.md#insn-009f9dbc)

~~~diff
- 009f9d3c ["INT_ADD", "register:40f0:8", ["const:9f9d3c:8", "const:4:8"]]
- 009f9d3c ["CALL", null, ["callee:00851550:8"]]
+ 009f9d90 ["INT_ADD", "register:40f0:8", ["const:9f9d90:8", "const:4:8"]]
+ 009f9d90 ["CALL", null, ["callee:00851550:8"]]
- 009f9d3c bytes ef5df997
+ 009f9d90 bytes f05df997
- 009f9d4c ["INT_ADD", "register:40f0:8", ["const:9f9d4c:8", "const:4:8"]]
- 009f9d4c ["CALL", null, ["callee:009e2fe8:8"]]
+ 009f9da0 ["INT_ADD", "register:40f0:8", ["const:9f9da0:8", "const:4:8"]]
+ 009f9da0 ["CALL", null, ["callee:009e2fe8:8"]]
- 009f9d4c bytes 92a4ff97
+ 009f9da0 bytes 92a4ff97
- 009f9d68 ["COPY", "register:0:8", ["register:4040:8"]]
- 009f9d68 ["INT_ADD", "register:40f0:8", ["const:9f9d68:8", "const:4:8"]]
- 009f9d68 ["CALLIND", null, ["register:0:8"]]
+ 009f9dbc ["COPY", "register:0:8", ["register:4040:8"]]
+ 009f9dbc ["INT_ADD", "register:40f0:8", ["const:9f9dbc:8", "const:4:8"]]
+ 009f9dbc ["CALLIND", null, ["register:0:8"]]
- 009f9d68 bytes 00013fd6
+ 009f9dbc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70d1107edf12d1f0b64491ab09815a35"></a>

### [`009fcd04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fc/009fcd04.md) → [`009fcd58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fc/009fcd58.md) FUN_009fcd58

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009fcd40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fc/009fcd04.md#insn-009fcd40)
- 新版 [`009fcd94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fc/009fcd58.md#insn-009fcd94)

~~~diff
- 009fcd40 ["COPY", "register:0:8", ["register:4040:8"]]
- 009fcd40 ["INT_ADD", "register:40f0:8", ["const:9fcd40:8", "const:4:8"]]
- 009fcd40 ["CALLIND", null, ["register:0:8"]]
+ 009fcd94 ["COPY", "register:0:8", ["register:4040:8"]]
+ 009fcd94 ["INT_ADD", "register:40f0:8", ["const:9fcd94:8", "const:4:8"]]
+ 009fcd94 ["CALLIND", null, ["register:0:8"]]
- 009fcd40 bytes 00013fd6
+ 009fcd94 bytes 00013fd6
~~~


<a id="compare-e8f6e3a1dce2349b82182d2f8f085910"></a>

### [`009fcdf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fc/009fcdf8.md) → [`009fce4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fc/009fce4c.md) FUN_009fce4c

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009f6214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f6/009f6214.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`009fcf14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fc/009fcf14.md) [`009fd0bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd0bc.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`009f6268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f6/009f6268.md) · 呼出先 4件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`009fcf68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fc/009fcf68.md) [`009fd110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fd/009fd110.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009fce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fc/009fcdf8.md#insn-009fce54) · [`009fce7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fc/009fcdf8.md#insn-009fce7c) · [`009fcea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fc/009fcdf8.md#insn-009fcea8)
- 新版 [`009fcea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fc/009fce4c.md#insn-009fcea8) · [`009fced0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fc/009fce4c.md#insn-009fced0) · [`009fcefc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fc/009fce4c.md#insn-009fcefc)

~~~diff
- 009fce54 ["INT_ADD", "register:40f0:8", ["const:9fce54:8", "const:4:8"]]
- 009fce54 ["CALL", null, ["callee:009fcf68:8"]]
+ 009fcea8 ["INT_ADD", "register:40f0:8", ["const:9fcea8:8", "const:4:8"]]
+ 009fcea8 ["CALL", null, ["callee:009fcf68:8"]]
- 009fce54 bytes 30000094
+ 009fcea8 bytes 30000094
- 009fce7c ["INT_ADD", "register:40f0:8", ["const:9fce7c:8", "const:4:8"]]
- 009fce7c ["CALL", null, ["callee:009fd110:8"]]
+ 009fced0 ["INT_ADD", "register:40f0:8", ["const:9fced0:8", "const:4:8"]]
+ 009fced0 ["CALL", null, ["callee:009fd110:8"]]
- 009fce7c bytes 90000094
+ 009fced0 bytes 90000094
- 009fcea8 ["INT_ADD", "register:40f0:8", ["const:9fcea8:8", "const:4:8"]]
- 009fcea8 ["CALL", null, ["callee:0043bbe4:8"]]
+ 009fcefc ["INT_ADD", "register:40f0:8", ["const:9fcefc:8", "const:4:8"]]
+ 009fcefc ["CALL", null, ["callee:0043bbe4:8"]]
- 009fcea8 bytes 3ffbe897
+ 009fcefc bytes 3afbe897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62dd3de4e43c38f4eb906128b4bcc90f"></a>

### [`009fd0bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd0bc.md) → [`009fd110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fd/009fd110.md) FUN_009fd110

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009fcdf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fc/009fcdf8.md) · 呼出先 3件 [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`009fce4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fc/009fce4c.md) · 呼出先 3件 [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009fd0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd0bc.md#insn-009fd0e0) · [`009fd118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd0bc.md#insn-009fd118) · [`009fd130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd0bc.md#insn-009fd130)
- 新版 [`009fd134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fd/009fd110.md#insn-009fd134) · [`009fd16c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fd/009fd110.md#insn-009fd16c) · [`009fd184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fd/009fd110.md#insn-009fd184)

~~~diff
- 009fd0e0 ["INT_ADD", "register:40f0:8", ["const:9fd0e0:8", "const:4:8"]]
- 009fd0e0 ["CALL", null, ["callee:00c57f60:8"]]
+ 009fd134 ["INT_ADD", "register:40f0:8", ["const:9fd134:8", "const:4:8"]]
+ 009fd134 ["CALL", null, ["callee:00c57f60:8"]]
- 009fd0e0 bytes 6c6b0994
+ 009fd134 bytes 8b6b0994
- 009fd118 ["INT_ADD", "register:40f0:8", ["const:9fd118:8", "const:4:8"]]
- 009fd118 ["CALL", null, ["callee:00c57f60:8"]]
+ 009fd16c ["INT_ADD", "register:40f0:8", ["const:9fd16c:8", "const:4:8"]]
+ 009fd16c ["CALL", null, ["callee:00c57f60:8"]]
- 009fd118 bytes 5e6b0994
+ 009fd16c bytes 7d6b0994
- 009fd130 ["INT_ADD", "register:40f0:8", ["const:9fd130:8", "const:4:8"]]
- 009fd130 ["CALL", null, ["callee:00c580d0:8"]]
+ 009fd184 ["INT_ADD", "register:40f0:8", ["const:9fd184:8", "const:4:8"]]
+ 009fd184 ["CALL", null, ["callee:00c580d0:8"]]
- 009fd130 bytes b46b0994
+ 009fd184 bytes d36b0994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02e5a659bb9be9f54626f2ea5f3cc0cc"></a>

### [`009fd1c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd1c4.md) → [`009fd218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fd/009fd218.md) FUN_009fd218

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b7948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b7948.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b79a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b79a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009fd1dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd1c4.md#insn-009fd1dc) · [`009fd1ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd1c4.md#insn-009fd1ec) · [`009fd1f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd1c4.md#insn-009fd1f0)
- 新版 [`009fd230`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fd/009fd218.md#insn-009fd230) · [`009fd240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fd/009fd218.md#insn-009fd240) · [`009fd244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fd/009fd218.md#insn-009fd244)

~~~diff
- 009fd1dc ["INT_ADD", "register:40f0:8", ["const:9fd1dc:8", "const:4:8"]]
- 009fd1dc ["CALL", null, ["callee:00851550:8"]]
+ 009fd230 ["INT_ADD", "register:40f0:8", ["const:9fd230:8", "const:4:8"]]
+ 009fd230 ["CALL", null, ["callee:00851550:8"]]
- 009fd1dc bytes c750f997
+ 009fd230 bytes c850f997
- 009fd1ec ["INT_ADD", "register:40f0:8", ["const:9fd1ec:8", "const:4:8"]]
- 009fd1ec ["CALL", null, ["callee:008b79a0:8"]]
+ 009fd240 ["INT_ADD", "register:40f0:8", ["const:9fd240:8", "const:4:8"]]
+ 009fd240 ["CALL", null, ["callee:008b79a0:8"]]
- 009fd1ec bytes d7e9fa97
+ 009fd240 bytes d8e9fa97
- 009fd1f0 ["INT_ADD", "register:40f0:8", ["const:9fd1f0:8", "const:4:8"]]
- 009fd1f0 ["CALL", null, ["callee:00851550:8"]]
+ 009fd244 ["INT_ADD", "register:40f0:8", ["const:9fd244:8", "const:4:8"]]
+ 009fd244 ["CALL", null, ["callee:00851550:8"]]
- 009fd1f0 bytes c250f997
+ 009fd244 bytes c350f997
~~~


<a id="compare-109623109a0a290626ce693ceaa2e4d8"></a>

### [`009fdccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fdccc.md) → [`009fdd20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fd/009fdd20.md) FUN_009fdd20

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`009f92c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f9/009f92c8.md) [`009fdccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fdccc.md) [`009fdf94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fdf94.md) · 呼出先 4件 [`009fdccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fdccc.md) [`009fdf94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fdf94.md) [`009fe20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fe/009fe20c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 3件 [`009f931c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f9/009f931c.md) [`009fdd20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fd/009fdd20.md) [`009fdfe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fd/009fdfe8.md) · 呼出先 4件 [`009fdd20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fd/009fdd20.md) [`009fdfe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fd/009fdfe8.md) [`009fe260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fe/009fe260.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009fde38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fdccc.md#insn-009fde38) · [`009fde58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fdccc.md#insn-009fde58) · [`009fdeb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fdccc.md#insn-009fdeb4)
- 新版 [`009fde8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fd/009fdd20.md#insn-009fde8c) · [`009fdeac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fd/009fdd20.md#insn-009fdeac) · [`009fdf08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fd/009fdd20.md#insn-009fdf08)

~~~diff
- 009fde38 ["INT_ADD", "register:40f0:8", ["const:9fde38:8", "const:4:8"]]
- 009fde38 ["CALL", null, ["local:b0:8"]]
+ 009fde8c ["INT_ADD", "register:40f0:8", ["const:9fde8c:8", "const:4:8"]]
+ 009fde8c ["CALL", null, ["local:b0:8"]]
- 009fde38 bytes a5ffff97
+ 009fde8c bytes a5ffff97
- 009fde58 ["INT_ADD", "register:40f0:8", ["const:9fde58:8", "const:4:8"]]
- 009fde58 ["CALL", null, ["local:b0:8"]]
+ 009fdeac ["INT_ADD", "register:40f0:8", ["const:9fdeac:8", "const:4:8"]]
+ 009fdeac ["CALL", null, ["local:b0:8"]]
- 009fde58 bytes 9dffff97
+ 009fdeac bytes 9dffff97
- 009fdeb4 ["INT_ADD", "register:40f0:8", ["const:9fdeb4:8", "const:4:8"]]
- 009fdeb4 ["CALL", null, ["callee:009fdfe8:8"]]
+ 009fdf08 ["INT_ADD", "register:40f0:8", ["const:9fdf08:8", "const:4:8"]]
+ 009fdf08 ["CALL", null, ["callee:009fdfe8:8"]]
- 009fdeb4 bytes 38000094
+ 009fdf08 bytes 38000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-295904bc1fae1245904747cea99baa26"></a>

### [`009fdf94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fdf94.md) → [`009fdfe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fd/009fdfe8.md) FUN_009fdfe8

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009fdccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fdccc.md) · 呼出先 1件 [`009fdccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fdccc.md)
- 新版 呼出元 1件 [`009fdd20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fd/009fdd20.md) · 呼出先 1件 [`009fdd20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fd/009fdd20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009fe124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fdf94.md#insn-009fe124) · [`009fe13c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fdf94.md#insn-009fe13c)
- 新版 [`009fe178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fd/009fdfe8.md#insn-009fe178) · [`009fe190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fd/009fdfe8.md#insn-009fe190)

~~~diff
- 009fe124 ["INT_ADD", "register:40f0:8", ["const:9fe124:8", "const:4:8"]]
- 009fe124 ["CALL", null, ["callee:009fdd20:8"]]
+ 009fe178 ["INT_ADD", "register:40f0:8", ["const:9fe178:8", "const:4:8"]]
+ 009fe178 ["CALL", null, ["callee:009fdd20:8"]]
- 009fe124 bytes eafeff97
+ 009fe178 bytes eafeff97
- 009fe13c ["INT_ADD", "register:40f0:8", ["const:9fe13c:8", "const:4:8"]]
- 009fe13c ["CALL", null, ["callee:009fdd20:8"]]
+ 009fe190 ["INT_ADD", "register:40f0:8", ["const:9fe190:8", "const:4:8"]]
+ 009fe190 ["CALL", null, ["callee:009fdd20:8"]]
- 009fe13c bytes e4feff97
+ 009fe190 bytes e4feff97
~~~


<a id="compare-dc4a14532ea7b6f64f38a1c0d0facfe0"></a>

### [`009fe20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fe/009fe20c.md) → [`009fe260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fe/009fe260.md) FUN_009fe260

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`009fdccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fdccc.md) [`009fe20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fe/009fe20c.md) · 呼出先 4件 [`009fe20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fe/009fe20c.md) [`009fe630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fe/009fe630.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 2件 [`009fdd20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fd/009fdd20.md) [`009fe260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fe/009fe260.md) · 呼出先 4件 [`009fe260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fe/009fe260.md) [`009fe684`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fe/009fe684.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009fe3a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fe/009fe20c.md#insn-009fe3a0) · [`009fe3e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fe/009fe20c.md#insn-009fe3e0) · [`009fe41c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fe/009fe20c.md#insn-009fe41c)
- 新版 [`009fe3f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fe/009fe260.md#insn-009fe3f4) · [`009fe434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fe/009fe260.md#insn-009fe434) · [`009fe470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fe/009fe260.md#insn-009fe470)

~~~diff
- 009fe3a0 ["INT_ADD", "register:40f0:8", ["const:9fe3a0:8", "const:4:8"]]
- 009fe3a0 ["CALL", null, ["callee:009fe684:8"]]
+ 009fe3f4 ["INT_ADD", "register:40f0:8", ["const:9fe3f4:8", "const:4:8"]]
+ 009fe3f4 ["CALL", null, ["callee:009fe684:8"]]
- 009fe3a0 bytes a4000094
+ 009fe3f4 bytes a4000094
- 009fe3e0 ["INT_ADD", "register:40f0:8", ["const:9fe3e0:8", "const:4:8"]]
- 009fe3e0 ["CALL", null, ["local:b0:8"]]
+ 009fe434 ["INT_ADD", "register:40f0:8", ["const:9fe434:8", "const:4:8"]]
+ 009fe434 ["CALL", null, ["local:b0:8"]]
- 009fe3e0 bytes 8bffff97
+ 009fe434 bytes 8bffff97
- 009fe41c ["INT_ADD", "register:40f0:8", ["const:9fe41c:8", "const:4:8"]]
- 009fe41c ["CALL", null, ["local:b0:8"]]
+ 009fe470 ["INT_ADD", "register:40f0:8", ["const:9fe470:8", "const:4:8"]]
+ 009fe470 ["CALL", null, ["local:b0:8"]]
- 009fe41c bytes 7cffff97
+ 009fe470 bytes 7cffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b1acc83227189719e8c4e3496e9147e"></a>

### [`009fe630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fe/009fe630.md) → [`009fe684`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fe/009fe684.md) FUN_009fe684

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`009fe20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fe/009fe20c.md) [`009fed94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fe/009fed94.md) · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 2件 [`009fe260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fe/009fe260.md) [`009fede8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fe/009fede8.md) · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009fe714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fe/009fe630.md#insn-009fe714) · [`009fe76c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fe/009fe630.md#insn-009fe76c) · [`009fe850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fe/009fe630.md#insn-009fe850)
- 新版 [`009fe768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fe/009fe684.md#insn-009fe768) · [`009fe7c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fe/009fe684.md#insn-009fe7c0) · [`009fe8a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fe/009fe684.md#insn-009fe8a4)

~~~diff
- 009fe714 ["INT_ADD", "register:40f0:8", ["const:9fe714:8", "const:4:8"]]
- 009fe714 ["CALL", null, ["callee:00c58010:8"]]
+ 009fe768 ["INT_ADD", "register:40f0:8", ["const:9fe768:8", "const:4:8"]]
+ 009fe768 ["CALL", null, ["callee:00c58010:8"]]
- 009fe714 bytes 0b660994
+ 009fe768 bytes 2a660994
- 009fe76c ["INT_ADD", "register:40f0:8", ["const:9fe76c:8", "const:4:8"]]
- 009fe76c ["CALL", null, ["callee:00c58010:8"]]
+ 009fe7c0 ["INT_ADD", "register:40f0:8", ["const:9fe7c0:8", "const:4:8"]]
+ 009fe7c0 ["CALL", null, ["callee:00c58010:8"]]
- 009fe76c bytes f5650994
+ 009fe7c0 bytes 14660994
- 009fe850 ["INT_ADD", "register:40f0:8", ["const:9fe850:8", "const:4:8"]]
- 009fe850 ["CALL", null, ["callee:00c57fb0:8"]]
+ 009fe8a4 ["INT_ADD", "register:40f0:8", ["const:9fe8a4:8", "const:4:8"]]
+ 009fe8a4 ["CALL", null, ["callee:00c57fb0:8"]]
- 009fe850 bytes a4650994
+ 009fe8a4 bytes c3650994
~~~


<a id="compare-ebaa58088339a47860a6fcce3b530e48"></a>

### [`009fe854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fe/009fe854.md) → [`009fe8a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fe/009fe8a8.md) FUN_009fe8a8

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`009f981c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f9/009f981c.md) [`009fe854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fe/009fe854.md) [`009feb1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fe/009feb1c.md) · 呼出先 4件 [`009fe854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fe/009fe854.md) [`009feb1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fe/009feb1c.md) [`009fed94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fe/009fed94.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 3件 [`009f9870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f9/009f9870.md) [`009fe8a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fe/009fe8a8.md) [`009feb70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fe/009feb70.md) · 呼出先 4件 [`009fe8a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fe/009fe8a8.md) [`009feb70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fe/009feb70.md) [`009fede8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fe/009fede8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009fe9c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fe/009fe854.md#insn-009fe9c0) · [`009fe9e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fe/009fe854.md#insn-009fe9e0) · [`009fea3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fe/009fe854.md#insn-009fea3c)
- 新版 [`009fea14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fe/009fe8a8.md#insn-009fea14) · [`009fea34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fe/009fe8a8.md#insn-009fea34) · [`009fea90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fe/009fe8a8.md#insn-009fea90)

~~~diff
- 009fe9c0 ["INT_ADD", "register:40f0:8", ["const:9fe9c0:8", "const:4:8"]]
- 009fe9c0 ["CALL", null, ["local:b0:8"]]
+ 009fea14 ["INT_ADD", "register:40f0:8", ["const:9fea14:8", "const:4:8"]]
+ 009fea14 ["CALL", null, ["local:b0:8"]]
- 009fe9c0 bytes a5ffff97
+ 009fea14 bytes a5ffff97
- 009fe9e0 ["INT_ADD", "register:40f0:8", ["const:9fe9e0:8", "const:4:8"]]
- 009fe9e0 ["CALL", null, ["local:b0:8"]]
+ 009fea34 ["INT_ADD", "register:40f0:8", ["const:9fea34:8", "const:4:8"]]
+ 009fea34 ["CALL", null, ["local:b0:8"]]
- 009fe9e0 bytes 9dffff97
+ 009fea34 bytes 9dffff97
- 009fea3c ["INT_ADD", "register:40f0:8", ["const:9fea3c:8", "const:4:8"]]
- 009fea3c ["CALL", null, ["callee:009feb70:8"]]
+ 009fea90 ["INT_ADD", "register:40f0:8", ["const:9fea90:8", "const:4:8"]]
+ 009fea90 ["CALL", null, ["callee:009feb70:8"]]
- 009fea3c bytes 38000094
+ 009fea90 bytes 38000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1085c0a6e9a83dbc81db848bfd999a8e"></a>

### [`009feb1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fe/009feb1c.md) → [`009feb70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fe/009feb70.md) FUN_009feb70

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009fe854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fe/009fe854.md) · 呼出先 1件 [`009fe854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fe/009fe854.md)
- 新版 呼出元 1件 [`009fe8a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fe/009fe8a8.md) · 呼出先 1件 [`009fe8a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fe/009fe8a8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009fecac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fe/009feb1c.md#insn-009fecac) · [`009fecc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fe/009feb1c.md#insn-009fecc4)
- 新版 [`009fed00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fe/009feb70.md#insn-009fed00) · [`009fed18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fe/009feb70.md#insn-009fed18)

~~~diff
- 009fecac ["INT_ADD", "register:40f0:8", ["const:9fecac:8", "const:4:8"]]
- 009fecac ["CALL", null, ["callee:009fe8a8:8"]]
+ 009fed00 ["INT_ADD", "register:40f0:8", ["const:9fed00:8", "const:4:8"]]
+ 009fed00 ["CALL", null, ["callee:009fe8a8:8"]]
- 009fecac bytes eafeff97
+ 009fed00 bytes eafeff97
- 009fecc4 ["INT_ADD", "register:40f0:8", ["const:9fecc4:8", "const:4:8"]]
- 009fecc4 ["CALL", null, ["callee:009fe8a8:8"]]
+ 009fed18 ["INT_ADD", "register:40f0:8", ["const:9fed18:8", "const:4:8"]]
+ 009fed18 ["CALL", null, ["callee:009fe8a8:8"]]
- 009fecc4 bytes e4feff97
+ 009fed18 bytes e4feff97
~~~


<a id="compare-ba87ed5cbb6992e85e68506e1bbe1d6e"></a>

### [`009fed94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fe/009fed94.md) → [`009fede8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fe/009fede8.md) FUN_009fede8

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`009fe854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fe/009fe854.md) [`009fed94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fe/009fed94.md) · 呼出先 4件 [`009fe630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fe/009fe630.md) [`009fed94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fe/009fed94.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 2件 [`009fe8a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fe/009fe8a8.md) [`009fede8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fe/009fede8.md) · 呼出先 4件 [`009fe684`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fe/009fe684.md) [`009fede8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fe/009fede8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009fef28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fe/009fed94.md#insn-009fef28) · [`009fef68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fe/009fed94.md#insn-009fef68) · [`009fefa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fe/009fed94.md#insn-009fefa4)
- 新版 [`009fef7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fe/009fede8.md#insn-009fef7c) · [`009fefbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fe/009fede8.md#insn-009fefbc) · [`009feff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fe/009fede8.md#insn-009feff8)

~~~diff
- 009fef28 ["INT_ADD", "register:40f0:8", ["const:9fef28:8", "const:4:8"]]
- 009fef28 ["CALL", null, ["callee:009fe684:8"]]
+ 009fef7c ["INT_ADD", "register:40f0:8", ["const:9fef7c:8", "const:4:8"]]
+ 009fef7c ["CALL", null, ["callee:009fe684:8"]]
- 009fef28 bytes c2fdff97
+ 009fef7c bytes c2fdff97
- 009fef68 ["INT_ADD", "register:40f0:8", ["const:9fef68:8", "const:4:8"]]
- 009fef68 ["CALL", null, ["local:b0:8"]]
+ 009fefbc ["INT_ADD", "register:40f0:8", ["const:9fefbc:8", "const:4:8"]]
+ 009fefbc ["CALL", null, ["local:b0:8"]]
- 009fef68 bytes 8bffff97
+ 009fefbc bytes 8bffff97
- 009fefa4 ["INT_ADD", "register:40f0:8", ["const:9fefa4:8", "const:4:8"]]
- 009fefa4 ["CALL", null, ["local:b0:8"]]
+ 009feff8 ["INT_ADD", "register:40f0:8", ["const:9feff8:8", "const:4:8"]]
+ 009feff8 ["CALL", null, ["local:b0:8"]]
- 009fefa4 bytes 7cffff97
+ 009feff8 bytes 7cffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f14f70f9f28ef108eb07956565a72ed7"></a>

### [`009ff3bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ff3bc.md) → [`009ff410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ff/009ff410.md) FUN_009ff410

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009f9ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009f9/009f9ee0.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`009f9f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009f9/009f9f34.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009ff3f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ff3bc.md#insn-009ff3f8)
- 新版 [`009ff44c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ff/009ff410.md#insn-009ff44c)

~~~diff
- 009ff3f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 009ff3f8 ["INT_ADD", "register:40f0:8", ["const:9ff3f8:8", "const:4:8"]]
- 009ff3f8 ["CALLIND", null, ["register:0:8"]]
+ 009ff44c ["COPY", "register:0:8", ["register:4040:8"]]
+ 009ff44c ["INT_ADD", "register:40f0:8", ["const:9ff44c:8", "const:4:8"]]
+ 009ff44c ["CALLIND", null, ["register:0:8"]]
- 009ff3f8 bytes 00013fd6
+ 009ff44c bytes 00013fd6
~~~


<a id="compare-494c12fcb8f6b92f07ac8105e0e32f27"></a>

### [`009fffa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009fffa4.md) → [`009ffff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ff/009ffff8.md) FUN_009ffff8

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009ff40c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009ff40c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`009ff460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ff/009ff460.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`009fffe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ff/009fffa4.md#insn-009fffe0)
- 新版 [`00a00034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ff/009ffff8.md#insn-00a00034)

~~~diff
- 009fffe0 ["COPY", "register:0:8", ["register:4040:8"]]
- 009fffe0 ["INT_ADD", "register:40f0:8", ["const:9fffe0:8", "const:4:8"]]
- 009fffe0 ["CALLIND", null, ["register:0:8"]]
+ 00a00034 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a00034 ["INT_ADD", "register:40f0:8", ["const:a00034:8", "const:4:8"]]
+ 00a00034 ["CALLIND", null, ["register:0:8"]]
- 009fffe0 bytes 00013fd6
+ 00a00034 bytes 00013fd6
~~~


<a id="compare-c038d0dad4ff9eefc54b43a096ec7b78"></a>

### [`00a001a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a001a0.md) → [`00a001f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a00/00a001f4.md) FUN_00a001f4

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9290.md) [`008b9298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9298.md) [`00a83588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a83/00a83588.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b92e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b92e8.md) [`008b92f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b92f0.md) [`00a835f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a83/00a835f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a001c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a001a0.md#insn-00a001c4) · [`00a001d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a001a0.md#insn-00a001d4) · [`00a001e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a001a0.md#insn-00a001e4)
- 新版 [`00a00218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a00/00a001f4.md#insn-00a00218) · [`00a00228`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a00/00a001f4.md#insn-00a00228) · [`00a00238`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a00/00a001f4.md#insn-00a00238)

~~~diff
- 00a001c4 ["INT_ADD", "register:40f0:8", ["const:a001c4:8", "const:4:8"]]
- 00a001c4 ["CALL", null, ["callee:008b92e8:8"]]
+ 00a00218 ["INT_ADD", "register:40f0:8", ["const:a00218:8", "const:4:8"]]
+ 00a00218 ["CALL", null, ["callee:008b92e8:8"]]
- 00a001c4 bytes 33e4fa97
+ 00a00218 bytes 34e4fa97
- 00a001d4 ["INT_ADD", "register:40f0:8", ["const:a001d4:8", "const:4:8"]]
- 00a001d4 ["CALL", null, ["callee:008b92e8:8"]]
+ 00a00228 ["INT_ADD", "register:40f0:8", ["const:a00228:8", "const:4:8"]]
+ 00a00228 ["CALL", null, ["callee:008b92e8:8"]]
- 00a001d4 bytes 2fe4fa97
+ 00a00228 bytes 30e4fa97
- 00a001e4 ["INT_ADD", "register:40f0:8", ["const:a001e4:8", "const:4:8"]]
- 00a001e4 ["CALL", null, ["callee:008b92f0:8"]]
+ 00a00238 ["INT_ADD", "register:40f0:8", ["const:a00238:8", "const:4:8"]]
+ 00a00238 ["CALL", null, ["callee:008b92f0:8"]]
- 00a001e4 bytes 2de4fa97
+ 00a00238 bytes 2ee4fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4fefb22f6ff33f23fe7935b73e96fad"></a>

### [`00a02ae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a02ae4.md) → [`00a02b38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a02/00a02b38.md) FUN_00a02b38

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a02b20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a02ae4.md#insn-00a02b20)
- 新版 [`00a02b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a02/00a02b38.md#insn-00a02b74)

~~~diff
- 00a02b20 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a02b20 ["INT_ADD", "register:40f0:8", ["const:a02b20:8", "const:4:8"]]
- 00a02b20 ["CALLIND", null, ["register:0:8"]]
+ 00a02b74 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a02b74 ["INT_ADD", "register:40f0:8", ["const:a02b74:8", "const:4:8"]]
+ 00a02b74 ["CALLIND", null, ["register:0:8"]]
- 00a02b20 bytes 00013fd6
+ 00a02b74 bytes 00013fd6
~~~


<a id="compare-fd4859a9b0d5ee558e44f9818081a24e"></a>

### [`00a02b68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a02b68.md) → [`00a02bbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a02/00a02bbc.md) FUN_00a02bbc

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`009fb44c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fb/009fb44c.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`009fb4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009fb/009fb4a0.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a02ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a02b68.md#insn-00a02ba4) · [`00a02bd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a02b68.md#insn-00a02bd4)
- 新版 [`00a02bf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a02/00a02bbc.md#insn-00a02bf8) · [`00a02c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a02/00a02bbc.md#insn-00a02c28)

~~~diff
- 00a02ba4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a02ba4 ["INT_ADD", "register:40f0:8", ["const:a02ba4:8", "const:4:8"]]
- 00a02ba4 ["CALLIND", null, ["register:0:8"]]
+ 00a02bf8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a02bf8 ["INT_ADD", "register:40f0:8", ["const:a02bf8:8", "const:4:8"]]
+ 00a02bf8 ["CALLIND", null, ["register:0:8"]]
- 00a02ba4 bytes 00013fd6
+ 00a02bf8 bytes 00013fd6
- 00a02bd4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a02bd4 ["INT_ADD", "register:40f0:8", ["const:a02bd4:8", "const:4:8"]]
- 00a02bd4 ["CALLIND", null, ["register:0:8"]]
+ 00a02c28 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a02c28 ["INT_ADD", "register:40f0:8", ["const:a02c28:8", "const:4:8"]]
+ 00a02c28 ["CALLIND", null, ["register:0:8"]]
- 00a02bd4 bytes 00013fd6
+ 00a02c28 bytes 00013fd6
~~~


<a id="compare-298cf22e71b05d460df7e5009164e616"></a>

### [`00a03974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03974.md) → [`00a039c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a03/00a039c8.md) FUN_00a039c8

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a02be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a02be8.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00a02c3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a02/00a02c3c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a039b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03974.md#insn-00a039b0)
- 新版 [`00a03a04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a03/00a039c8.md#insn-00a03a04)

~~~diff
- 00a039b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a039b0 ["INT_ADD", "register:40f0:8", ["const:a039b0:8", "const:4:8"]]
- 00a039b0 ["CALLIND", null, ["register:0:8"]]
+ 00a03a04 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a03a04 ["INT_ADD", "register:40f0:8", ["const:a03a04:8", "const:4:8"]]
+ 00a03a04 ["CALLIND", null, ["register:0:8"]]
- 00a039b0 bytes 00013fd6
+ 00a03a04 bytes 00013fd6
~~~


<a id="compare-bb860755d4b0e2231ce49d30e6c82afe"></a>

### [`00a03cb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03cb4.md) → [`00a03d08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a03/00a03d08.md) FUN_00a03d08

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a02be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a02be8.md) · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00a02c3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a02/00a02c3c.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a03cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a03/00a03cb4.md#insn-00a03cf0)
- 新版 [`00a03d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a03/00a03d08.md#insn-00a03d44)

~~~diff
- 00a03cf0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a03cf0 ["INT_ADD", "register:40f0:8", ["const:a03cf0:8", "const:4:8"]]
- 00a03cf0 ["CALLIND", null, ["register:0:8"]]
+ 00a03d44 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00a03d44 ["INT_ADD", "register:40f0:8", ["const:a03d44:8", "const:4:8"]]
+ 00a03d44 ["CALLIND", null, ["register:0:8"]]
- 00a03cf0 bytes 00013fd6
+ 00a03d44 bytes 00013fd6
~~~


<a id="compare-8aacdff8df31f8b642ac6863c84f12dc"></a>

### [`00a04e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a04e2c.md) → [`00a04e80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a04/00a04e80.md) FUN_00a04e80

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`008b97a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b97a0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`008b97f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b97f8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a04e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a04/00a04e2c.md#insn-00a04e50)
- 新版 [`00a04ea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a04/00a04e80.md#insn-00a04ea4)

~~~diff
- 00a04e50 ["INT_ADD", "register:40f0:8", ["const:a04e50:8", "const:4:8"]]
- 00a04e50 ["CALL", null, ["callee:008b97f8:8"]]
+ 00a04ea4 ["INT_ADD", "register:40f0:8", ["const:a04ea4:8", "const:4:8"]]
+ 00a04ea4 ["CALL", null, ["callee:008b97f8:8"]]
- 00a04e50 bytes 54d2fa97
+ 00a04ea4 bytes 55d2fa97
~~~


<a id="compare-584e4671ed33705415cf7c4a5c5be973"></a>

### [`00a06274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06274.md) → [`00a062c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a062c8.md) FUN_00a062c8

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 8件 [`0059765c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059765c.md) [`00597778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597778.md) [`00597a4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a4c.md) [`00597a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a58.md) [`00597a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a64.md)
- 新版 呼出元 1件 [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) · 呼出先 8件 [`0059769c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059769c.md) [`005977b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/005977b8.md) [`00597a8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597a8c.md) [`00597a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597a98.md) [`00597aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597aa4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a0629c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06274.md#insn-00a0629c) · [`00a06308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06274.md#insn-00a06308) · [`00a06310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06274.md#insn-00a06310)
- 新版 [`00a062f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a062c8.md#insn-00a062f0) · [`00a0635c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a062c8.md#insn-00a0635c) · [`00a06364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a062c8.md#insn-00a06364)

~~~diff
- 00a0629c ["INT_ADD", "register:40f0:8", ["const:a0629c:8", "const:4:8"]]
- 00a0629c ["CALL", null, ["callee:00a06428:8"]]
+ 00a062f0 ["INT_ADD", "register:40f0:8", ["const:a062f0:8", "const:4:8"]]
+ 00a062f0 ["CALL", null, ["callee:00a06428:8"]]
- 00a0629c bytes 4e000094
+ 00a062f0 bytes 4e000094
- 00a06308 ["INT_ADD", "register:40f0:8", ["const:a06308:8", "const:4:8"]]
- 00a06308 ["CALL", null, ["callee:005977b8:8"]]
+ 00a0635c ["INT_ADD", "register:40f0:8", ["const:a0635c:8", "const:4:8"]]
+ 00a0635c ["CALL", null, ["callee:005977b8:8"]]
- 00a06308 bytes 1c45ee97
+ 00a0635c bytes 1745ee97
- 00a06310 ["INT_ADD", "register:40f0:8", ["const:a06310:8", "const:4:8"]]
- 00a06310 ["CALL", null, ["callee:0059769c:8"]]
+ 00a06364 ["INT_ADD", "register:40f0:8", ["const:a06364:8", "const:4:8"]]
+ 00a06364 ["CALL", null, ["callee:0059769c:8"]]
- 00a06310 bytes d344ee97
+ 00a06364 bytes ce44ee97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-359a6850900d9cdfd38973c25b4a5272"></a>

### [`00a063d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a063d4.md) → [`00a06428`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a06428.md) FUN_00a06428

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`00a06274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06274.md) · 呼出先 9件 [`0059765c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059765c.md) [`00597778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597778.md) [`00597a4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a4c.md) [`00597a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a58.md) [`00597a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a64.md)
- 新版 呼出元 2件 [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) [`00a062c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a062c8.md) · 呼出先 9件 [`0059769c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/0059769c.md) [`005977b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/005977b8.md) [`00597a8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597a8c.md) [`00597a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597a98.md) [`00597aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597aa4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a063f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a063d4.md#insn-00a063f8) · [`00a06404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a063d4.md#insn-00a06404) · [`00a0647c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a063d4.md#insn-00a0647c)
- 新版 [`00a0644c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a06428.md#insn-00a0644c) · [`00a06458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a06428.md#insn-00a06458) · [`00a064d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a06428.md#insn-00a064d0)

~~~diff
- 00a063f8 ["INT_ADD", "register:40f0:8", ["const:a063f8:8", "const:4:8"]]
- 00a063f8 ["CALL", null, ["callee:00851550:8"]]
+ 00a0644c ["INT_ADD", "register:40f0:8", ["const:a0644c:8", "const:4:8"]]
+ 00a0644c ["CALL", null, ["callee:00851550:8"]]
- 00a063f8 bytes 402cf997
+ 00a0644c bytes 412cf997
- 00a06404 ["INT_ADD", "register:40f0:8", ["const:a06404:8", "const:4:8"]]
- 00a06404 ["CALL", null, ["callee:00a871c0:8"]]
+ 00a06458 ["INT_ADD", "register:40f0:8", ["const:a06458:8", "const:4:8"]]
+ 00a06458 ["CALL", null, ["callee:00a871c0:8"]]
- 00a06404 bytes 53030294
+ 00a06458 bytes 5a030294
- 00a0647c ["INT_ADD", "register:40f0:8", ["const:a0647c:8", "const:4:8"]]
- 00a0647c ["CALL", null, ["callee:005977b8:8"]]
+ 00a064d0 ["INT_ADD", "register:40f0:8", ["const:a064d0:8", "const:4:8"]]
+ 00a064d0 ["CALL", null, ["callee:005977b8:8"]]
- 00a0647c bytes bf44ee97
+ 00a064d0 bytes ba44ee97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8ff1e8cd3ae67aa90fda0c0cf22439f"></a>

### [`00a06510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06510.md) → [`00a06564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a06564.md) FUN_00a06564

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007efca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007efca8.md) · 呼出先 4件 [`0071c460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0071c/0071c460.md) [`00732c84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00732/00732c84.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008d35ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d3/008d35ac.md)
- 新版 呼出元 1件 [`007efd00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ef/007efd00.md) · 呼出先 4件 [`0071c4b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0071c/0071c4b8.md) [`00732cdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00732/00732cdc.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008d3600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d3/008d3600.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a06520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06510.md#insn-00a06520) · [`00a06530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06510.md#insn-00a06530) · [`00a06538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06510.md#insn-00a06538)
- 新版 [`00a06574`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a06564.md#insn-00a06574) · [`00a06584`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a06564.md#insn-00a06584) · [`00a0658c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a06564.md#insn-00a0658c)

~~~diff
- 00a06520 ["INT_ADD", "register:40f0:8", ["const:a06520:8", "const:4:8"]]
- 00a06520 ["CALL", null, ["callee:00851550:8"]]
+ 00a06574 ["INT_ADD", "register:40f0:8", ["const:a06574:8", "const:4:8"]]
+ 00a06574 ["CALL", null, ["callee:00851550:8"]]
- 00a06520 bytes f62bf997
+ 00a06574 bytes f72bf997
- 00a06530 ["INT_ADD", "register:40f0:8", ["const:a06530:8", "const:4:8"]]
- 00a06530 ["CALL", null, ["callee:00732cdc:8"]]
+ 00a06584 ["INT_ADD", "register:40f0:8", ["const:a06584:8", "const:4:8"]]
+ 00a06584 ["CALL", null, ["callee:00732cdc:8"]]
- 00a06530 bytes d5b1f497
+ 00a06584 bytes d6b1f497
- 00a06538 ["INT_ADD", "register:40f0:8", ["const:a06538:8", "const:4:8"]]
- 00a06538 ["CALL", null, ["callee:00851550:8"]]
+ 00a0658c ["INT_ADD", "register:40f0:8", ["const:a0658c:8", "const:4:8"]]
+ 00a0658c ["CALL", null, ["callee:00851550:8"]]
- 00a06538 bytes f02bf997
+ 00a0658c bytes f12bf997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cde4e96b073a48d7c62b0fdd92981cf1"></a>

### [`00a065dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a065dc.md) → [`00a06630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a06630.md) FUN_00a06630

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) · 呼出先 2件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008d35ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d3/008d35ac.md)
- 新版 呼出元 1件 [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) · 呼出先 2件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008d3600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d3/008d3600.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a065ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a065dc.md#insn-00a065ec) · [`00a065f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a065dc.md#insn-00a065f8) · [`00a0660c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a065dc.md#insn-00a0660c)
- 新版 [`00a06640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a06630.md#insn-00a06640) · [`00a0664c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a06630.md#insn-00a0664c) · [`00a06660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a06630.md#insn-00a06660)

~~~diff
- 00a065ec ["INT_ADD", "register:40f0:8", ["const:a065ec:8", "const:4:8"]]
- 00a065ec ["CALL", null, ["callee:00851550:8"]]
+ 00a06640 ["INT_ADD", "register:40f0:8", ["const:a06640:8", "const:4:8"]]
+ 00a06640 ["CALL", null, ["callee:00851550:8"]]
- 00a065ec bytes c32bf997
+ 00a06640 bytes c42bf997
- 00a065f8 ["INT_ADD", "register:40f0:8", ["const:a065f8:8", "const:4:8"]]
- 00a065f8 ["CALL", null, ["callee:008d3600:8"]]
+ 00a0664c ["INT_ADD", "register:40f0:8", ["const:a0664c:8", "const:4:8"]]
+ 00a0664c ["CALL", null, ["callee:008d3600:8"]]
- 00a065f8 bytes ed33fb97
+ 00a0664c bytes ed33fb97
- 00a0660c ["INT_ADD", "register:40f0:8", ["const:a0660c:8", "const:4:8"]]
- 00a0660c ["CALL", null, ["callee:00851550:8"]]
+ 00a06660 ["INT_ADD", "register:40f0:8", ["const:a06660:8", "const:4:8"]]
+ 00a06660 ["CALL", null, ["callee:00851550:8"]]
- 00a0660c bytes bb2bf997
+ 00a06660 bytes bc2bf997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c4f7c3e8200ff8a82d6416c08f57079"></a>

### [`00a06674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06674.md) → [`00a066c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a066c8.md) FUN_00a066c8

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`007ef320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ef/007ef320.md) · 呼出先 2件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008d35ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d3/008d35ac.md)
- 新版 呼出元 2件 [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) [`007ef378`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ef/007ef378.md) · 呼出先 2件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008d3600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008d3/008d3600.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a06684`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06674.md#insn-00a06684) · [`00a06690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06674.md#insn-00a06690) · [`00a066a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06674.md#insn-00a066a4)
- 新版 [`00a066d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a066c8.md#insn-00a066d8) · [`00a066e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a066c8.md#insn-00a066e4) · [`00a066f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a066c8.md#insn-00a066f8)

~~~diff
- 00a06684 ["INT_ADD", "register:40f0:8", ["const:a06684:8", "const:4:8"]]
- 00a06684 ["CALL", null, ["callee:00851550:8"]]
+ 00a066d8 ["INT_ADD", "register:40f0:8", ["const:a066d8:8", "const:4:8"]]
+ 00a066d8 ["CALL", null, ["callee:00851550:8"]]
- 00a06684 bytes 9d2bf997
+ 00a066d8 bytes 9e2bf997
- 00a06690 ["INT_ADD", "register:40f0:8", ["const:a06690:8", "const:4:8"]]
- 00a06690 ["CALL", null, ["callee:008d3600:8"]]
+ 00a066e4 ["INT_ADD", "register:40f0:8", ["const:a066e4:8", "const:4:8"]]
+ 00a066e4 ["CALL", null, ["callee:008d3600:8"]]
- 00a06690 bytes c733fb97
+ 00a066e4 bytes c733fb97
- 00a066a4 ["INT_ADD", "register:40f0:8", ["const:a066a4:8", "const:4:8"]]
- 00a066a4 ["CALL", null, ["callee:00851550:8"]]
+ 00a066f8 ["INT_ADD", "register:40f0:8", ["const:a066f8:8", "const:4:8"]]
+ 00a066f8 ["CALL", null, ["callee:00851550:8"]]
- 00a066a4 bytes 952bf997
+ 00a066f8 bytes 962bf997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fab0c1e87f8655bdf648f9658afa1fed"></a>

### [`00a06830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06830.md) → [`00a06884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a06884.md) FUN_00a06884

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) · 呼出先 2件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b3e410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3e/00b3e410.md)
- 新版 呼出元 2件 [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) [`007df140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007df/007df140.md) · 呼出先 2件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00b3e4ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b3e/00b3e4ac.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a06838`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06830.md#insn-00a06838)
- 新版 [`00a0688c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a06884.md#insn-00a0688c)

~~~diff
- 00a06838 ["INT_ADD", "register:40f0:8", ["const:a06838:8", "const:4:8"]]
- 00a06838 ["CALL", null, ["callee:00851550:8"]]
+ 00a0688c ["INT_ADD", "register:40f0:8", ["const:a0688c:8", "const:4:8"]]
+ 00a0688c ["CALL", null, ["callee:00851550:8"]]
- 00a06838 bytes 302bf997
+ 00a0688c bytes 312bf997
~~~


<a id="compare-9a6a4bc96b94d94985ce12d57e2b020f"></a>

### [`00a06850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06850.md) → [`00a068a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a068a4.md) FUN_00a068a4

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a86e9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a86/00a86e9c.md) · 呼出先 7件 [`005976e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/005976e8.md) [`00597778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597778.md) [`00597a4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a4c.md) [`00597a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a58.md) [`00597a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597a64.md)
- 新版 呼出元 1件 [`00a86f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a86/00a86f0c.md) · 呼出先 7件 [`00597728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597728.md) [`005977b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/005977b8.md) [`00597a8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597a8c.md) [`00597a98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597a98.md) [`00597aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597aa4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a068e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06850.md#insn-00a068e0) · [`00a068e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06850.md#insn-00a068e8) · [`00a06914`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06850.md#insn-00a06914)
- 新版 [`00a06934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a068a4.md#insn-00a06934) · [`00a0693c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a068a4.md#insn-00a0693c) · [`00a06968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a068a4.md#insn-00a06968)

~~~diff
- 00a068e0 ["INT_ADD", "register:40f0:8", ["const:a068e0:8", "const:4:8"]]
- 00a068e0 ["CALL", null, ["callee:005977b8:8"]]
+ 00a06934 ["INT_ADD", "register:40f0:8", ["const:a06934:8", "const:4:8"]]
+ 00a06934 ["CALL", null, ["callee:005977b8:8"]]
- 00a068e0 bytes a643ee97
+ 00a06934 bytes a143ee97
- 00a068e8 ["INT_ADD", "register:40f0:8", ["const:a068e8:8", "const:4:8"]]
- 00a068e8 ["CALL", null, ["callee:00597acc:8"]]
+ 00a0693c ["INT_ADD", "register:40f0:8", ["const:a0693c:8", "const:4:8"]]
+ 00a0693c ["CALL", null, ["callee:00597acc:8"]]
- 00a068e8 bytes 6944ee97
+ 00a0693c bytes 6444ee97
- 00a06914 ["INT_ADD", "register:40f0:8", ["const:a06914:8", "const:4:8"]]
- 00a06914 ["CALL", null, ["callee:00597728:8"]]
+ 00a06968 ["INT_ADD", "register:40f0:8", ["const:a06968:8", "const:4:8"]]
+ 00a06968 ["CALL", null, ["callee:00597728:8"]]
- 00a06914 bytes 7543ee97
+ 00a06968 bytes 7043ee97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b29379b00b049ff8a5e80fe28bf1f9a"></a>

### [`00a06970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06970.md) → [`00a069c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a069c4.md) FUN_00a069c4

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a2b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2b/00a2b2e8.md) · 呼出先 2件 [`00480b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b38.md) [`00480be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480be8.md)
- 新版 呼出元 1件 [`00a2b33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2b/00a2b33c.md) · 呼出先 2件 [`00480b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480b78.md) [`00480c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480c28.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a06990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06970.md#insn-00a06990)
- 新版 [`00a069e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a069c4.md#insn-00a069e4)

~~~diff
- 00a06990 ["INT_ADD", "register:40f0:8", ["const:a06990:8", "const:4:8"]]
- 00a06990 ["CALL", null, ["callee:00480c28:8"]]
+ 00a069e4 ["INT_ADD", "register:40f0:8", ["const:a069e4:8", "const:4:8"]]
+ 00a069e4 ["CALL", null, ["callee:00480c28:8"]]
- 00a06990 bytes 96e8e997
+ 00a069e4 bytes 91e8e997
~~~


<a id="compare-c1835875c519f9feaf0ebc4bc69ed4ad"></a>

### [`00a069a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a069a8.md) → [`00a069fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a069fc.md) FUN_00a069fc

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 2件 [`00480118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480118.md) [`004801d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004801d8.md)
- 新版 呼出元 1件 [`00a26210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a26/00a26210.md) · 呼出先 2件 [`00480158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480158.md) [`00480218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480218.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a069c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a069a8.md#insn-00a069c0) · [`00a069cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a069a8.md#insn-00a069cc)
- 新版 [`00a06a14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a069fc.md#insn-00a06a14) · [`00a06a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a06/00a069fc.md#insn-00a06a20)

~~~diff
- 00a069c0 ["INT_ADD", "register:40f0:8", ["const:a069c0:8", "const:4:8"]]
- 00a069c0 ["CALL", null, ["callee:00480218:8"]]
+ 00a06a14 ["INT_ADD", "register:40f0:8", ["const:a06a14:8", "const:4:8"]]
+ 00a06a14 ["CALL", null, ["callee:00480218:8"]]
- 00a069c0 bytes 06e6e997
+ 00a06a14 bytes 01e6e997
- 00a069cc ["INT_ADD", "register:40f0:8", ["const:a069cc:8", "const:4:8"]]
- 00a069cc ["CALL", null, ["callee:00480158:8"]]
+ 00a06a20 ["INT_ADD", "register:40f0:8", ["const:a06a20:8", "const:4:8"]]
+ 00a06a20 ["CALL", null, ["callee:00480158:8"]]
- 00a069cc bytes d3e5e997
+ 00a06a20 bytes cee5e997
~~~


<a id="compare-c11dcc73e97312b12eb0de91e867e391"></a>

### [`00a2a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2a/00a2a830.md) → [`00a2a884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2a/00a2a884.md) FUN_00a2a884

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 14件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00480178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480178.md) [`004802f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004802f8.md) [`004803f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004803f0.md) [`00480744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480744.md)
- 新版 呼出元 1件 [`00a26210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a26/00a26210.md) · 呼出先 14件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`004801b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/004801b8.md) [`00480338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480338.md) [`00480430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480430.md) [`00480784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480784.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a2a870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2a/00a2a830.md#insn-00a2a870) · [`00a2a888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2a/00a2a830.md#insn-00a2a888) · [`00a2a8b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2a/00a2a830.md#insn-00a2a8b0)
- 新版 [`00a2a8c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2a/00a2a884.md#insn-00a2a8c4) · [`00a2a8dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2a/00a2a884.md#insn-00a2a8dc) · [`00a2a904`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2a/00a2a884.md#insn-00a2a904)

~~~diff
- 00a2a870 ["INT_ADD", "register:40f0:8", ["const:a2a870:8", "const:4:8"]]
- 00a2a870 ["CALL", null, ["callee:004801b8:8"]]
+ 00a2a8c4 ["INT_ADD", "register:40f0:8", ["const:a2a8c4:8", "const:4:8"]]
+ 00a2a8c4 ["CALL", null, ["callee:004801b8:8"]]
- 00a2a870 bytes 4256e997
+ 00a2a8c4 bytes 3d56e997
- 00a2a888 ["INT_ADD", "register:40f0:8", ["const:a2a888:8", "const:4:8"]]
- 00a2a888 ["CALL", null, ["callee:00676aa0:8"]]
+ 00a2a8dc ["INT_ADD", "register:40f0:8", ["const:a2a8dc:8", "const:4:8"]]
+ 00a2a8dc ["CALL", null, ["callee:00676aa0:8"]]
- 00a2a888 bytes 7630f197
+ 00a2a8dc bytes 7130f197
- 00a2a8b0 ["INT_ADD", "register:40f0:8", ["const:a2a8b0:8", "const:4:8"]]
- 00a2a8b0 ["CALL", null, ["callee:0043bbe4:8"]]
+ 00a2a904 ["INT_ADD", "register:40f0:8", ["const:a2a904:8", "const:4:8"]]
+ 00a2a904 ["CALL", null, ["callee:0043bbe4:8"]]
- 00a2a8b0 bytes bd44e897
+ 00a2a904 bytes b844e897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8dca1ef6d92300e0f643f865c20689a"></a>

### [`00a2ad8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2a/00a2ad8c.md) → [`00a2ade0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2a/00a2ade0.md) FUN_00a2ade0

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 14件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00480178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480178.md) [`004802f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004802f8.md) [`004803f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004803f0.md) [`00480744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480744.md)
- 新版 呼出元 1件 [`00a26210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a26/00a26210.md) · 呼出先 14件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`004801b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/004801b8.md) [`00480338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480338.md) [`00480430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480430.md) [`00480784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480784.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a2adcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2a/00a2ad8c.md#insn-00a2adcc) · [`00a2ade4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2a/00a2ad8c.md#insn-00a2ade4) · [`00a2ae0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2a/00a2ad8c.md#insn-00a2ae0c)
- 新版 [`00a2ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2a/00a2ade0.md#insn-00a2ae20) · [`00a2ae38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2a/00a2ade0.md#insn-00a2ae38) · [`00a2ae60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2a/00a2ade0.md#insn-00a2ae60)

~~~diff
- 00a2adcc ["INT_ADD", "register:40f0:8", ["const:a2adcc:8", "const:4:8"]]
- 00a2adcc ["CALL", null, ["callee:004801b8:8"]]
+ 00a2ae20 ["INT_ADD", "register:40f0:8", ["const:a2ae20:8", "const:4:8"]]
+ 00a2ae20 ["CALL", null, ["callee:004801b8:8"]]
- 00a2adcc bytes eb54e997
+ 00a2ae20 bytes e654e997
- 00a2ade4 ["INT_ADD", "register:40f0:8", ["const:a2ade4:8", "const:4:8"]]
- 00a2ade4 ["CALL", null, ["callee:00676aa0:8"]]
+ 00a2ae38 ["INT_ADD", "register:40f0:8", ["const:a2ae38:8", "const:4:8"]]
+ 00a2ae38 ["CALL", null, ["callee:00676aa0:8"]]
- 00a2ade4 bytes 1f2ff197
+ 00a2ae38 bytes 1a2ff197
- 00a2ae0c ["INT_ADD", "register:40f0:8", ["const:a2ae0c:8", "const:4:8"]]
- 00a2ae0c ["CALL", null, ["callee:0043bbe4:8"]]
+ 00a2ae60 ["INT_ADD", "register:40f0:8", ["const:a2ae60:8", "const:4:8"]]
+ 00a2ae60 ["CALL", null, ["callee:0043bbe4:8"]]
- 00a2ae0c bytes 6643e897
+ 00a2ae60 bytes 6143e897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81b162bb2e227b293f9f8ce1541942ec"></a>

### [`00a2db54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2d/00a2db54.md) → [`00a2dba8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2d/00a2dba8.md) FUN_00a2dba8

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a2b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2b/00a2b2e8.md) · 呼出先 6件 [`00480b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b90.md) [`00480d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480d48.md) [`00480e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480e28.md) [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`00691800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00691/00691800.md)
- 新版 呼出元 1件 [`00a2b33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2b/00a2b33c.md) · 呼出先 6件 [`00480bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480bd0.md) [`00480d88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480d88.md) [`00480e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480e68.md) [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`00691858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691858.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a2db94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2d/00a2db54.md#insn-00a2db94) · [`00a2dbb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2d/00a2db54.md#insn-00a2dbb0) · [`00a2dbe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2d/00a2db54.md#insn-00a2dbe8)
- 新版 [`00a2dbe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2d/00a2dba8.md#insn-00a2dbe8) · [`00a2dc04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2d/00a2dba8.md#insn-00a2dc04) · [`00a2dc3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2d/00a2dba8.md#insn-00a2dc3c)

~~~diff
- 00a2db94 ["INT_ADD", "register:40f0:8", ["const:a2db94:8", "const:4:8"]]
- 00a2db94 ["CALL", null, ["callee:00480bd0:8"]]
+ 00a2dbe8 ["INT_ADD", "register:40f0:8", ["const:a2dbe8:8", "const:4:8"]]
+ 00a2dbe8 ["CALL", null, ["callee:00480bd0:8"]]
- 00a2db94 bytes ff4be997
+ 00a2dbe8 bytes fa4be997
- 00a2dbb0 ["INT_ADD", "register:40f0:8", ["const:a2dbb0:8", "const:4:8"]]
- 00a2dbb0 ["CALL", null, ["callee:00480bd0:8"]]
+ 00a2dc04 ["INT_ADD", "register:40f0:8", ["const:a2dc04:8", "const:4:8"]]
+ 00a2dc04 ["CALL", null, ["callee:00480bd0:8"]]
- 00a2dbb0 bytes f84be997
+ 00a2dc04 bytes f34be997
- 00a2dbe8 ["INT_ADD", "register:40f0:8", ["const:a2dbe8:8", "const:4:8"]]
- 00a2dbe8 ["CALL", null, ["callee:00480bd0:8"]]
+ 00a2dc3c ["INT_ADD", "register:40f0:8", ["const:a2dc3c:8", "const:4:8"]]
+ 00a2dc3c ["CALL", null, ["callee:00480bd0:8"]]
- 00a2dbe8 bytes ea4be997
+ 00a2dc3c bytes e54be997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16beb2983aaccc4037da6913bfdc603f"></a>

### [`00a2dddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2d/00a2dddc.md) → [`00a2de30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2d/00a2de30.md) FUN_00a2de30

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a2b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2b/00a2b2e8.md) · 呼出先 6件 [`00480b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480b90.md) [`00480d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480d48.md) [`00480e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/00480e28.md) [`005c179c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c1/005c179c.md) [`00691800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00691/00691800.md)
- 新版 呼出元 1件 [`00a2b33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2b/00a2b33c.md) · 呼出先 6件 [`00480bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480bd0.md) [`00480d88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480d88.md) [`00480e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480e68.md) [`005c17dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c17dc.md) [`00691858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00691/00691858.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a2de1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2d/00a2dddc.md#insn-00a2de1c) · [`00a2de38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2d/00a2dddc.md#insn-00a2de38) · [`00a2de70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2d/00a2dddc.md#insn-00a2de70)
- 新版 [`00a2de70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2d/00a2de30.md#insn-00a2de70) · [`00a2de8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2d/00a2de30.md#insn-00a2de8c) · [`00a2dec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2d/00a2de30.md#insn-00a2dec4)

~~~diff
- 00a2de1c ["INT_ADD", "register:40f0:8", ["const:a2de1c:8", "const:4:8"]]
- 00a2de1c ["CALL", null, ["callee:00480bd0:8"]]
+ 00a2de70 ["INT_ADD", "register:40f0:8", ["const:a2de70:8", "const:4:8"]]
+ 00a2de70 ["CALL", null, ["callee:00480bd0:8"]]
- 00a2de1c bytes 5d4be997
+ 00a2de70 bytes 584be997
- 00a2de38 ["INT_ADD", "register:40f0:8", ["const:a2de38:8", "const:4:8"]]
- 00a2de38 ["CALL", null, ["callee:00480bd0:8"]]
+ 00a2de8c ["INT_ADD", "register:40f0:8", ["const:a2de8c:8", "const:4:8"]]
+ 00a2de8c ["CALL", null, ["callee:00480bd0:8"]]
- 00a2de38 bytes 564be997
+ 00a2de8c bytes 514be997
- 00a2de70 ["INT_ADD", "register:40f0:8", ["const:a2de70:8", "const:4:8"]]
- 00a2de70 ["CALL", null, ["callee:00480bd0:8"]]
+ 00a2dec4 ["INT_ADD", "register:40f0:8", ["const:a2dec4:8", "const:4:8"]]
+ 00a2dec4 ["CALL", null, ["callee:00480bd0:8"]]
- 00a2de70 bytes 484be997
+ 00a2dec4 bytes 434be997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-668943f435e240f0477bf5fdbff2d0f5"></a>

### [`00a2e9c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2e/00a2e9c8.md) → [`00a2ea1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2e/00a2ea1c.md) FUN_00a2ea1c

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a2b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2b/00a2b2e8.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00a2eaf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2e/00a2eaf4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00a2b33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2b/00a2b33c.md) · 呼出先 4件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00a2eb48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2e/00a2eb48.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a2ea24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2e/00a2e9c8.md#insn-00a2ea24) · [`00a2ea44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2e/00a2e9c8.md#insn-00a2ea44) · [`00a2ea88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2e/00a2e9c8.md#insn-00a2ea88)
- 新版 [`00a2ea78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2e/00a2ea1c.md#insn-00a2ea78) · [`00a2ea98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2e/00a2ea1c.md#insn-00a2ea98) · [`00a2eadc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2e/00a2ea1c.md#insn-00a2eadc)

~~~diff
- 00a2ea24 ["INT_ADD", "register:40f0:8", ["const:a2ea24:8", "const:4:8"]]
- 00a2ea24 ["CALL", null, ["callee:00a2eb48:8"]]
+ 00a2ea78 ["INT_ADD", "register:40f0:8", ["const:a2ea78:8", "const:4:8"]]
+ 00a2ea78 ["CALL", null, ["callee:00a2eb48:8"]]
- 00a2ea24 bytes 34000094
+ 00a2ea78 bytes 34000094
- 00a2ea44 ["INT_ADD", "register:40f0:8", ["const:a2ea44:8", "const:4:8"]]
- 00a2ea44 ["CALL", null, ["callee:00c57f60:8"]]
+ 00a2ea98 ["INT_ADD", "register:40f0:8", ["const:a2ea98:8", "const:4:8"]]
+ 00a2ea98 ["CALL", null, ["callee:00c57f60:8"]]
- 00a2ea44 bytes 13a50894
+ 00a2ea98 bytes 32a50894
- 00a2ea88 ["INT_ADD", "register:40f0:8", ["const:a2ea88:8", "const:4:8"]]
- 00a2ea88 ["CALL", null, ["callee:0043bbe4:8"]]
+ 00a2eadc ["INT_ADD", "register:40f0:8", ["const:a2eadc:8", "const:4:8"]]
+ 00a2eadc ["CALL", null, ["callee:0043bbe4:8"]]
- 00a2ea88 bytes 4734e897
+ 00a2eadc bytes 4234e897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98df26d6e1b083c24c76081ca382d977"></a>

### [`00a2ec9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2e/00a2ec9c.md) → [`00a2ecf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2e/00a2ecf0.md) FUN_00a2ecf0

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a2b2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2b/00a2b2e8.md) · 呼出先 4件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00a2edc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2e/00a2edc0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00a2b33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2b/00a2b33c.md) · 呼出先 4件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00a2ee14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2e/00a2ee14.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a2ecf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2e/00a2ec9c.md#insn-00a2ecf8) · [`00a2ed18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2e/00a2ec9c.md#insn-00a2ed18) · [`00a2ed54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2e/00a2ec9c.md#insn-00a2ed54)
- 新版 [`00a2ed4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2e/00a2ecf0.md#insn-00a2ed4c) · [`00a2ed6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2e/00a2ecf0.md#insn-00a2ed6c) · [`00a2eda8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2e/00a2ecf0.md#insn-00a2eda8)

~~~diff
- 00a2ecf8 ["INT_ADD", "register:40f0:8", ["const:a2ecf8:8", "const:4:8"]]
- 00a2ecf8 ["CALL", null, ["callee:00a2ee14:8"]]
+ 00a2ed4c ["INT_ADD", "register:40f0:8", ["const:a2ed4c:8", "const:4:8"]]
+ 00a2ed4c ["CALL", null, ["callee:00a2ee14:8"]]
- 00a2ecf8 bytes 32000094
+ 00a2ed4c bytes 32000094
- 00a2ed18 ["INT_ADD", "register:40f0:8", ["const:a2ed18:8", "const:4:8"]]
- 00a2ed18 ["CALL", null, ["callee:00c57f60:8"]]
+ 00a2ed6c ["INT_ADD", "register:40f0:8", ["const:a2ed6c:8", "const:4:8"]]
+ 00a2ed6c ["CALL", null, ["callee:00c57f60:8"]]
- 00a2ed18 bytes 5ea40894
+ 00a2ed6c bytes 7da40894
- 00a2ed54 ["INT_ADD", "register:40f0:8", ["const:a2ed54:8", "const:4:8"]]
- 00a2ed54 ["CALL", null, ["callee:0043bbe4:8"]]
+ 00a2eda8 ["INT_ADD", "register:40f0:8", ["const:a2eda8:8", "const:4:8"]]
+ 00a2eda8 ["CALL", null, ["callee:0043bbe4:8"]]
- 00a2ed54 bytes 9433e897
+ 00a2eda8 bytes 8f33e897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1701b3be728696da75682c36c311019f"></a>

### [`00a2ef68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2e/00a2ef68.md) → [`00a2efbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2e/00a2efbc.md) FUN_00a2efbc

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 3件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0086c2b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0086c/0086c2b4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00a26210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a26/00a26210.md) · 呼出先 3件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0086c30c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0086c/0086c30c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a2f0a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2e/00a2ef68.md#insn-00a2f0a8) · [`00a2f164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2e/00a2ef68.md#insn-00a2f164) · [`00a2f188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2e/00a2ef68.md#insn-00a2f188)
- 新版 [`00a2f0fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2e/00a2efbc.md#insn-00a2f0fc) · [`00a2f1b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2e/00a2efbc.md#insn-00a2f1b8) · [`00a2f1dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2e/00a2efbc.md#insn-00a2f1dc)

~~~diff
- 00a2f0a8 ["INT_ADD", "register:40f0:8", ["const:a2f0a8:8", "const:4:8"]]
- 00a2f0a8 ["CALL", null, ["callee:0043bbe4:8"]]
+ 00a2f0fc ["INT_ADD", "register:40f0:8", ["const:a2f0fc:8", "const:4:8"]]
+ 00a2f0fc ["CALL", null, ["callee:0043bbe4:8"]]
- 00a2f0a8 bytes bf32e897
+ 00a2f0fc bytes ba32e897
- 00a2f164 ["INT_ADD", "register:40f0:8", ["const:a2f164:8", "const:4:8"]]
- 00a2f164 ["CALL", null, ["callee:0086c30c:8"]]
+ 00a2f1b8 ["INT_ADD", "register:40f0:8", ["const:a2f1b8:8", "const:4:8"]]
+ 00a2f1b8 ["CALL", null, ["callee:0086c30c:8"]]
- 00a2f164 bytes 54f4f897
+ 00a2f1b8 bytes 55f4f897
- 00a2f188 ["INT_ADD", "register:40f0:8", ["const:a2f188:8", "const:4:8"]]
- 00a2f188 ["CALL", null, ["callee:0086c30c:8"]]
+ 00a2f1dc ["INT_ADD", "register:40f0:8", ["const:a2f1dc:8", "const:4:8"]]
+ 00a2f1dc ["CALL", null, ["callee:0086c30c:8"]]
- 00a2f188 bytes 4bf4f897
+ 00a2f1dc bytes 4cf4f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85e461ff16d62ee897e9dafcf291c384"></a>

### [`00a30430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a30/00a30430.md) → [`00a30484`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a30/00a30484.md) FUN_00a30484

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`008959d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00895/008959d0.md) [`0089bc8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089b/0089bc8c.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 2件 [`00895a28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00895/00895a28.md) [`0089bce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0089b/0089bce4.md) · 呼出先 1件 [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a30438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a30/00a30430.md#insn-00a30438)
- 新版 [`00a3048c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a30/00a30484.md#insn-00a3048c)

~~~diff
- 00a30438 ["INT_ADD", "register:40f0:8", ["const:a30438:8", "const:4:8"]]
- 00a30438 ["CALL", null, ["callee:00851550:8"]]
+ 00a3048c ["INT_ADD", "register:40f0:8", ["const:a3048c:8", "const:4:8"]]
+ 00a3048c ["CALL", null, ["callee:00851550:8"]]
- 00a30438 bytes 3084f897
+ 00a3048c bytes 3184f897
~~~


<a id="compare-43f1f63577f16b4d524fdb745623843f"></a>

### [`00a31b1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a31/00a31b1c.md) → [`00a31b70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a31/00a31b70.md) FUN_00a31b70

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 11件 [`005e0ea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e0ea8.md) [`00605254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00605/00605254.md) [`00626a34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00626/00626a34.md) [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) [`007102d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00710/007102d8.md) · 呼出先 1件 [`00802b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b58.md)
- 新版 呼出元 11件 [`005e0ee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e0/005e0ee8.md) [`00605294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00605/00605294.md) [`00626a74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00626/00626a74.md) [`00700b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700b50.md) [`00710330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00710/00710330.md) · 呼出先 1件 [`00802bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802bb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a31b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a31/00a31b1c.md#insn-00a31b30)
- 新版 [`00a31b84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a31/00a31b70.md#insn-00a31b84)

~~~diff
- 00a31b30 ["INT_ADD", "register:40f0:8", ["const:a31b30:8", "const:4:8"]]
- 00a31b30 ["CALL", null, ["callee:00802bb0:8"]]
+ 00a31b84 ["INT_ADD", "register:40f0:8", ["const:a31b84:8", "const:4:8"]]
+ 00a31b84 ["CALL", null, ["callee:00802bb0:8"]]
- 00a31b30 bytes 0a44f797
+ 00a31b84 bytes 0b44f797
~~~


<a id="compare-ce8763e896c7b52fe0a3beef8f8e32eb"></a>

### [`00a31b78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a31/00a31b78.md) → [`00a31bcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a31/00a31bcc.md) FUN_00a31bcc

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`007ca06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ca/007ca06c.md) [`00a9edec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a9e/00a9edec.md) · 呼出先 3件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00802b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b58.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 2件 [`007ca0c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ca/007ca0c4.md) [`00a9ee5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a9e/00a9ee5c.md) · 呼出先 3件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00802bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802bb0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a31ba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a31/00a31b78.md#insn-00a31ba8) · [`00a31c2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a31/00a31b78.md#insn-00a31c2c) · [`00a31c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a31/00a31b78.md#insn-00a31c80)
- 新版 [`00a31bfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a31/00a31bcc.md#insn-00a31bfc) · [`00a31c80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a31/00a31bcc.md#insn-00a31c80) · [`00a31cd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a31/00a31bcc.md#insn-00a31cd4)

~~~diff
- 00a31ba8 ["INT_ADD", "register:40f0:8", ["const:a31ba8:8", "const:4:8"]]
- 00a31ba8 ["CALL", null, ["callee:00802bb0:8"]]
+ 00a31bfc ["INT_ADD", "register:40f0:8", ["const:a31bfc:8", "const:4:8"]]
+ 00a31bfc ["CALL", null, ["callee:00802bb0:8"]]
- 00a31ba8 bytes ec43f797
+ 00a31bfc bytes ed43f797
- 00a31c2c ["INT_ADD", "register:40f0:8", ["const:a31c2c:8", "const:4:8"]]
- 00a31c2c ["CALL", null, ["callee:00c57f60:8"]]
+ 00a31c80 ["INT_ADD", "register:40f0:8", ["const:a31c80:8", "const:4:8"]]
+ 00a31c80 ["CALL", null, ["callee:00c57f60:8"]]
- 00a31c2c bytes 99980894
+ 00a31c80 bytes b8980894
- 00a31c80 ["INT_ADD", "register:40f0:8", ["const:a31c80:8", "const:4:8"]]
- 00a31c80 ["CALL", null, ["callee:0043bbe4:8"]]
+ 00a31cd4 ["INT_ADD", "register:40f0:8", ["const:a31cd4:8", "const:4:8"]]
+ 00a31cd4 ["CALL", null, ["callee:0043bbe4:8"]]
- 00a31c80 bytes c927e897
+ 00a31cd4 bytes c427e897
~~~


<a id="compare-a70fda94954f6096121cb8e42d28be0b"></a>

### [`00a31cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a31/00a31cb0.md) → [`00a31d04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a31/00a31d04.md) FUN_00a31d04

採用 · 移動量 `+0x54` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a31f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a31/00a31f54.md) · 呼出先 3件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00802b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b58.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00a31fa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a31/00a31fa8.md) · 呼出先 3件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00802bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802bb0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a31cd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a31/00a31cb0.md#insn-00a31cd4) · [`00a31d50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a31/00a31cb0.md#insn-00a31d50) · [`00a31da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a31/00a31cb0.md#insn-00a31da4)
- 新版 [`00a31d28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a31/00a31d04.md#insn-00a31d28) · [`00a31da4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a31/00a31d04.md#insn-00a31da4) · [`00a31df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a31/00a31d04.md#insn-00a31df8)

~~~diff
- 00a31cd4 ["INT_ADD", "register:40f0:8", ["const:a31cd4:8", "const:4:8"]]
- 00a31cd4 ["CALL", null, ["callee:00802bb0:8"]]
+ 00a31d28 ["INT_ADD", "register:40f0:8", ["const:a31d28:8", "const:4:8"]]
+ 00a31d28 ["CALL", null, ["callee:00802bb0:8"]]
- 00a31cd4 bytes a143f797
+ 00a31d28 bytes a243f797
- 00a31d50 ["INT_ADD", "register:40f0:8", ["const:a31d50:8", "const:4:8"]]
- 00a31d50 ["CALL", null, ["callee:00c57f60:8"]]
+ 00a31da4 ["INT_ADD", "register:40f0:8", ["const:a31da4:8", "const:4:8"]]
+ 00a31da4 ["CALL", null, ["callee:00c57f60:8"]]
- 00a31d50 bytes 50980894
+ 00a31da4 bytes 6f980894
- 00a31da4 ["INT_ADD", "register:40f0:8", ["const:a31da4:8", "const:4:8"]]
- 00a31da4 ["CALL", null, ["callee:0043bbe4:8"]]
+ 00a31df8 ["INT_ADD", "register:40f0:8", ["const:a31df8:8", "const:4:8"]]
+ 00a31df8 ["CALL", null, ["callee:0043bbe4:8"]]
- 00a31da4 bytes 8027e897
+ 00a31df8 bytes 7b27e897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ffc5945d2ff6a7fd7a770bb83d2c3a5"></a>

### [`00a31f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a31/00a31f54.md) → [`00a31fa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a31/00a31fa8.md) FUN_00a31fa8

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`0070ea5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070e/0070ea5c.md) [`007102d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00710/007102d8.md) [`007119f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) · 呼出先 1件 [`00a31cb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a31/00a31cb0.md)
- 新版 呼出元 3件 [`0070eab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0070e/0070eab4.md) [`00710330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00710/00710330.md) [`00711a48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00711/00711a48.md) · 呼出先 1件 [`00a31d04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a31/00a31d04.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a31f64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a31/00a31f54.md#insn-00a31f64)
- 新版 [`00a31fb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a31/00a31fa8.md#insn-00a31fb8)

~~~diff
- 00a31f64 ["INT_ADD", "register:40f0:8", ["const:a31f64:8", "const:4:8"]]
- 00a31f64 ["CALL", null, ["callee:00a31d04:8"]]
+ 00a31fb8 ["INT_ADD", "register:40f0:8", ["const:a31fb8:8", "const:4:8"]]
+ 00a31fb8 ["CALL", null, ["callee:00a31d04:8"]]
- 00a31f64 bytes 53ffff97
+ 00a31fb8 bytes 53ffff97
~~~


<a id="compare-6f48a186bc1fd858e89dd45824565bef"></a>

### [`00a31f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a31/00a31f98.md) → [`00a31fec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a31/00a31fec.md) FUN_00a31fec

採用 · 移動量 `+0x54` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00a261bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a26/00a261bc.md) · 呼出先 1件 [`004802f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00480/004802f8.md)
- 新版 呼出元 1件 [`00a26210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a26/00a26210.md) · 呼出先 1件 [`00480338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480338.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a31fac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a31/00a31f98.md#insn-00a31fac)
- 新版 [`00a32000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a31/00a31fec.md#insn-00a32000)

~~~diff
- 00a31fac ["INT_ADD", "register:40f0:8", ["const:a31fac:8", "const:4:8"]]
- 00a31fac ["CALL", null, ["callee:00480338:8"]]
+ 00a32000 ["INT_ADD", "register:40f0:8", ["const:a32000:8", "const:4:8"]]
+ 00a32000 ["CALL", null, ["callee:00480338:8"]]
- 00a31fac bytes d338e997
+ 00a32000 bytes ce38e997
~~~


<a id="compare-699081bbc5b45c136f78ababe230cdbd"></a>

### [`00a32364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a32/00a32364.md) → [`00a323b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a32/00a323b8.md) FUN_00a323b8

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0084e59c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0084e/0084e59c.md) · 呼出先 1件 [`005c3e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c3/005c3e7c.md)
- 新版 呼出元 1件 [`0084e5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0084e/0084e5f4.md) · 呼出先 1件 [`005c3ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c3/005c3ebc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a32380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a32/00a32364.md#insn-00a32380)
- 新版 [`00a323d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a32/00a323b8.md#insn-00a323d4)

~~~diff
- 00a32380 ["INT_ADD", "register:40f0:8", ["const:a32380:8", "const:4:8"]]
- 00a32380 ["CALL", null, ["callee:005c3ebc:8"]]
+ 00a323d4 ["INT_ADD", "register:40f0:8", ["const:a323d4:8", "const:4:8"]]
+ 00a323d4 ["CALL", null, ["callee:005c3ebc:8"]]
- 00a32380 bytes bf46ee97
+ 00a323d4 bytes ba46ee97
~~~


<a id="compare-aafc48131038534b1afc11a88b56ec0d"></a>

### [`00a323a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a32/00a323a0.md) → [`00a323f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a32/00a323f4.md) FUN_00a323f4

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0066ae50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066a/0066ae50.md) · 呼出先 2件 [`00719738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00719/00719738.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`0066ae90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0066a/0066ae90.md) · 呼出先 2件 [`00719790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00719/00719790.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a32400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a32/00a323a0.md#insn-00a32400) · [`00a32448`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a32/00a323a0.md#insn-00a32448) · [`00a32474`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a32/00a323a0.md#insn-00a32474)
- 新版 [`00a32454`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a32/00a323f4.md#insn-00a32454) · [`00a3249c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a32/00a323f4.md#insn-00a3249c) · [`00a324c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a32/00a323f4.md#insn-00a324c8)

~~~diff
- 00a32400 ["INT_ADD", "register:40f0:8", ["const:a32400:8", "const:4:8"]]
- 00a32400 ["CALL", null, ["callee:00719790:8"]]
+ 00a32454 ["INT_ADD", "register:40f0:8", ["const:a32454:8", "const:4:8"]]
+ 00a32454 ["CALL", null, ["callee:00719790:8"]]
- 00a32400 bytes ce9cf397
+ 00a32454 bytes cf9cf397
- 00a32448 ["INT_ADD", "register:40f0:8", ["const:a32448:8", "const:4:8"]]
- 00a32448 ["CALL", null, ["callee:00719790:8"]]
+ 00a3249c ["INT_ADD", "register:40f0:8", ["const:a3249c:8", "const:4:8"]]
+ 00a3249c ["CALL", null, ["callee:00719790:8"]]
- 00a32448 bytes bc9cf397
+ 00a3249c bytes bd9cf397
- 00a32474 ["INT_ADD", "register:40f0:8", ["const:a32474:8", "const:4:8"]]
- 00a32474 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00a324c8 ["INT_ADD", "register:40f0:8", ["const:a324c8:8", "const:4:8"]]
+ 00a324c8 ["CALL", null, ["callee:00c57fb0:8"]]
- 00a32474 bytes 9b960894
+ 00a324c8 bytes ba960894
~~~


<a id="compare-6da218b52db30600fa2d246c356662e3"></a>

### [`00a32478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a32/00a32478.md) → [`00a324cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a32/00a324cc.md) FUN_00a324cc

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009d0320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009d0/009d0320.md) · 呼出先 2件 [`00719738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00719/00719738.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`009d0374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009d0/009d0374.md) · 呼出先 2件 [`00719790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00719/00719790.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a324d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a32/00a32478.md#insn-00a324d0) · [`00a324fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a32/00a32478.md#insn-00a324fc)
- 新版 [`00a32524`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a32/00a324cc.md#insn-00a32524) · [`00a32550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a32/00a324cc.md#insn-00a32550)

~~~diff
- 00a324d0 ["INT_ADD", "register:40f0:8", ["const:a324d0:8", "const:4:8"]]
- 00a324d0 ["CALL", null, ["callee:00719790:8"]]
+ 00a32524 ["INT_ADD", "register:40f0:8", ["const:a32524:8", "const:4:8"]]
+ 00a32524 ["CALL", null, ["callee:00719790:8"]]
- 00a324d0 bytes 9a9cf397
+ 00a32524 bytes 9b9cf397
- 00a324fc ["INT_ADD", "register:40f0:8", ["const:a324fc:8", "const:4:8"]]
- 00a324fc ["CALL", null, ["callee:00c57fb0:8"]]
+ 00a32550 ["INT_ADD", "register:40f0:8", ["const:a32550:8", "const:4:8"]]
+ 00a32550 ["CALL", null, ["callee:00c57fb0:8"]]
- 00a324fc bytes 79960894
+ 00a32550 bytes 98960894
~~~


<a id="compare-b5ecc01af5fb8870f101f8301ce241c8"></a>

### [`00a32a04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a32/00a32a04.md) → [`00a32a58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a32/00a32a58.md) FUN_00a32a58

採用 · 移動量 `+0x54` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 12件 [`006bed5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006be/006bed5c.md) [`00773894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/00773894.md) [`007cb5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cb/007cb5e0.md) [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`007df0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007df/007df0e8.md) · 呼出先 5件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00802b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b58.md) [`00802ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ca8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58450.md)
- 新版 呼出元 12件 [`006bedb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006be/006bedb4.md) [`007738ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00773/007738ec.md) [`007cb638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cb/007cb638.md) [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) [`007df140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007df/007df140.md) · 呼出先 5件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00802bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802bb0.md) [`00802d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802d00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58520.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a32ae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a32/00a32a04.md#insn-00a32ae0) · [`00a32af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a32/00a32a04.md#insn-00a32af4) · [`00a32b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a32/00a32a04.md#insn-00a32b48)
- 新版 [`00a32b34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a32/00a32a58.md#insn-00a32b34) · [`00a32b48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a32/00a32a58.md#insn-00a32b48) · [`00a32b9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a32/00a32a58.md#insn-00a32b9c)

~~~diff
- 00a32ae0 ["INT_ADD", "register:40f0:8", ["const:a32ae0:8", "const:4:8"]]
- 00a32ae0 ["CALL", null, ["callee:00802bb0:8"]]
+ 00a32b34 ["INT_ADD", "register:40f0:8", ["const:a32b34:8", "const:4:8"]]
+ 00a32b34 ["CALL", null, ["callee:00802bb0:8"]]
- 00a32ae0 bytes 1e40f797
+ 00a32b34 bytes 1f40f797
- 00a32af4 ["INT_ADD", "register:40f0:8", ["const:a32af4:8", "const:4:8"]]
- 00a32af4 ["CALL", null, ["callee:00802d00:8"]]
+ 00a32b48 ["INT_ADD", "register:40f0:8", ["const:a32b48:8", "const:4:8"]]
+ 00a32b48 ["CALL", null, ["callee:00802d00:8"]]
- 00a32af4 bytes 6d40f797
+ 00a32b48 bytes 6e40f797
- 00a32b48 ["INT_ADD", "register:40f0:8", ["const:a32b48:8", "const:4:8"]]
- 00a32b48 ["CALL", null, ["callee:00c57f60:8"]]
+ 00a32b9c ["INT_ADD", "register:40f0:8", ["const:a32b9c:8", "const:4:8"]]
+ 00a32b9c ["CALL", null, ["callee:00c57f60:8"]]
- 00a32b48 bytes d2940894
+ 00a32b9c bytes f1940894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

