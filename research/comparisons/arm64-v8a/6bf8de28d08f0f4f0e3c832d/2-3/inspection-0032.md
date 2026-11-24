# v16.0.2 → v16.0.3 · 要調査の変更候補 (32)

[一覧の目次](README.md)

<a id="compare-ab745ab8e7af7484a2f10961d7b82fae"></a>

### [`00b5843c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b5843c.md) → [`00b59430`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b59430.md) _ZNSt6__ndk16__treeINS_12__value_typeIPKcNS_4listIN8firebase4util12CallbackDataENS_9allocatorIS7_EEEEEENS_19__map_value_compareIS3_SB_NS_4le

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b6d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b6d0.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5b6a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b6a0.md)
- 新版 呼出元 1件 [`00c5c6a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c6a0.md) · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5c670`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c670.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b584b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b5843c.md#insn-00b584b8) · [`00b584f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b5843c.md#insn-00b584f0) · [`00b58504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b5843c.md#insn-00b58504)
- 新版 [`00b594ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b59430.md#insn-00b594ac) · [`00b594e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b59430.md#insn-00b594e4) · [`00b594f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b59430.md#insn-00b594f8)

~~~diff
- 00b584b8 ["INT_ADD", "register:40f0:8", ["const:b584b8:8", "const:4:8"]]
- 00b584b8 ["CALL", null, ["callee:00c5c670:8"]]
+ 00b594ac ["INT_ADD", "register:40f0:8", ["const:b594ac:8", "const:4:8"]]
+ 00b594ac ["CALL", null, ["callee:00c5c670:8"]]
- 00b584b8 bytes 7a0c0494
+ 00b594ac bytes 710c0494
- 00b584f0 ["INT_ADD", "register:40f0:8", ["const:b584f0:8", "const:4:8"]]
- 00b584f0 ["CALL", null, ["callee:00c58f50:8"]]
+ 00b594e4 ["INT_ADD", "register:40f0:8", ["const:b594e4:8", "const:4:8"]]
+ 00b594e4 ["CALL", null, ["callee:00c58f50:8"]]
- 00b584f0 bytes a4fe0394
+ 00b594e4 bytes 9bfe0394
- 00b58504 ["INT_ADD", "register:40f0:8", ["const:b58504:8", "const:4:8"]]
- 00b58504 ["CALL", null, ["callee:00c58f50:8"]]
+ 00b594f8 ["INT_ADD", "register:40f0:8", ["const:b594f8:8", "const:4:8"]]
+ 00b594f8 ["CALL", null, ["callee:00c58f50:8"]]
- 00b58504 bytes 9ffe0394
+ 00b594f8 bytes 96fe0394
~~~


<a id="compare-40ddee452add4ae8ad5851431ab36018"></a>

### [`00b588cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b588cc.md) → [`00b598c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b598c0.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) · 呼出先 2件 [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5b170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b170.md)
- 新版 呼出元 1件 [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md) · 呼出先 2件 [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5c140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b58930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b588cc.md#insn-00b58930) · [`00b58958`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b588cc.md#insn-00b58958)
- 新版 [`00b59924`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b598c0.md#insn-00b59924) · [`00b5994c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b598c0.md#insn-00b5994c)

~~~diff
- 00b58930 ["INT_ADD", "register:40f0:8", ["const:b58930:8", "const:4:8"]]
- 00b58930 ["CALL", null, ["callee:00c5c140:8"]]
+ 00b59924 ["INT_ADD", "register:40f0:8", ["const:b59924:8", "const:4:8"]]
+ 00b59924 ["CALL", null, ["callee:00c5c140:8"]]
- 00b58930 bytes 100a0494
+ 00b59924 bytes 070a0494
- 00b58958 ["INT_ADD", "register:40f0:8", ["const:b58958:8", "const:4:8"]]
- 00b58958 ["CALL", null, ["callee:00c590a0:8"]]
+ 00b5994c ["INT_ADD", "register:40f0:8", ["const:b5994c:8", "const:4:8"]]
+ 00b5994c ["CALL", null, ["callee:00c590a0:8"]]
- 00b58958 bytes defd0394
+ 00b5994c bytes d5fd0394
~~~


<a id="compare-757e15b8e6ac1594f50e7711ab3dd816"></a>

### [`00b58990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58990.md) → [`00b59984`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b59984.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE9__grow_byEmmmmmm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5a9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a9b0.md) · 呼出先 4件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c5b980`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b980.md) · 呼出先 4件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b58a2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58990.md#insn-00b58a2c) · [`00b58a44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58990.md#insn-00b58a44) · [`00b58a64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58990.md#insn-00b58a64)
- 新版 [`00b59a20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b59984.md#insn-00b59a20) · [`00b59a38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b59984.md#insn-00b59a38) · [`00b59a58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b59984.md#insn-00b59a58)

~~~diff
- 00b58a2c ["INT_ADD", "register:40f0:8", ["const:b58a2c:8", "const:4:8"]]
- 00b58a2c ["CALL", null, ["callee:00c58f30:8"]]
+ 00b59a20 ["INT_ADD", "register:40f0:8", ["const:b59a20:8", "const:4:8"]]
+ 00b59a20 ["CALL", null, ["callee:00c58f30:8"]]
- 00b58a2c bytes 4dfd0394
+ 00b59a20 bytes 44fd0394
- 00b58a44 ["INT_ADD", "register:40f0:8", ["const:b58a44:8", "const:4:8"]]
- 00b58a44 ["CALL", null, ["callee:00c590a0:8"]]
+ 00b59a38 ["INT_ADD", "register:40f0:8", ["const:b59a38:8", "const:4:8"]]
+ 00b59a38 ["CALL", null, ["callee:00c590a0:8"]]
- 00b58a44 bytes a3fd0394
+ 00b59a38 bytes 9afd0394
- 00b58a64 ["INT_ADD", "register:40f0:8", ["const:b58a64:8", "const:4:8"]]
- 00b58a64 ["CALL", null, ["callee:00c590a0:8"]]
+ 00b59a58 ["INT_ADD", "register:40f0:8", ["const:b59a58:8", "const:4:8"]]
+ 00b59a58 ["CALL", null, ["callee:00c590a0:8"]]
- 00b58a64 bytes 9bfd0394
+ 00b59a58 bytes 92fd0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0d7c8817379f4fadb3cd0f516428a16"></a>

### [`00b58b8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58b8c.md) → [`00b59b80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b59b80.md) _ZN8firebase8internal16JObjectReferenceC1EP7_JNIEnv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5b260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b260.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00c5c230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c230.md) · 呼出先 1件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b58bc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58b8c.md#insn-00b58bc4) · [`00b58bf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58b8c.md#insn-00b58bf0)
- 新版 [`00b59bb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b59b80.md#insn-00b59bb8) · [`00b59be4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b59b80.md#insn-00b59be4)

~~~diff
- 00b58bc4 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b58bc4 ["INT_ADD", "register:40f0:8", ["const:b58bc4:8", "const:4:8"]]
- 00b58bc4 ["CALLIND", null, ["register:0:8"]]
+ 00b59bb8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b59bb8 ["INT_ADD", "register:40f0:8", ["const:b59bb8:8", "const:4:8"]]
+ 00b59bb8 ["CALLIND", null, ["register:0:8"]]
- 00b58bc4 bytes 20013fd6
+ 00b59bb8 bytes 20013fd6
- 00b58bf0 ["INT_ADD", "register:40f0:8", ["const:b58bf0:8", "const:4:8"]]
- 00b58bf0 ["CALL", null, ["callee:00c58f80:8"]]
+ 00b59be4 ["INT_ADD", "register:40f0:8", ["const:b59be4:8", "const:4:8"]]
+ 00b59be4 ["CALL", null, ["callee:00c58f80:8"]]
- 00b58bf0 bytes f0fc0394
+ 00b59be4 bytes e7fc0394
~~~


<a id="compare-92198059498de60cef73618776d86978"></a>

### [`00b58bf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58bf4.md) → [`00b59be8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b59be8.md) _ZN8firebase8internal16JObjectReference9GetJavaVMEP7_JNIEnv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b58c20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58bf4.md#insn-00b58c20) · [`00b58c48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58bf4.md#insn-00b58c48)
- 新版 [`00b59c14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b59be8.md#insn-00b59c14) · [`00b59c3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b59be8.md#insn-00b59c3c)

~~~diff
- 00b58c20 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b58c20 ["INT_ADD", "register:40f0:8", ["const:b58c20:8", "const:4:8"]]
- 00b58c20 ["CALLIND", null, ["register:0:8"]]
+ 00b59c14 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b59c14 ["INT_ADD", "register:40f0:8", ["const:b59c14:8", "const:4:8"]]
+ 00b59c14 ["CALLIND", null, ["register:0:8"]]
- 00b58c20 bytes 00013fd6
+ 00b59c14 bytes 00013fd6
- 00b58c48 ["INT_ADD", "register:40f0:8", ["const:b58c48:8", "const:4:8"]]
- 00b58c48 ["CALL", null, ["callee:00c58f80:8"]]
+ 00b59c3c ["INT_ADD", "register:40f0:8", ["const:b59c3c:8", "const:4:8"]]
+ 00b59c3c ["CALL", null, ["callee:00c58f80:8"]]
- 00b58c48 bytes dafc0394
+ 00b59c3c bytes d1fc0394
~~~


<a id="compare-94a507199ae3a9945641a6c1f281791c"></a>

### [`00b58c4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58c4c.md) → [`00b59c40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b59c40.md) _ZN8firebase8internal16JObjectReferenceC2EP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b58c8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58c4c.md#insn-00b58c8c) · [`00b58cac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58c4c.md#insn-00b58cac) · [`00b58cd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58c4c.md#insn-00b58cd8)
- 新版 [`00b59c80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b59c40.md#insn-00b59c80) · [`00b59ca0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b59c40.md#insn-00b59ca0) · [`00b59ccc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b59c40.md#insn-00b59ccc)

~~~diff
- 00b58c8c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b58c8c ["INT_ADD", "register:40f0:8", ["const:b58c8c:8", "const:4:8"]]
- 00b58c8c ["CALLIND", null, ["register:0:8"]]
+ 00b59c80 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b59c80 ["INT_ADD", "register:40f0:8", ["const:b59c80:8", "const:4:8"]]
+ 00b59c80 ["CALLIND", null, ["register:0:8"]]
- 00b58c8c bytes 00013fd6
+ 00b59c80 bytes 00013fd6
- 00b58cac ["COPY", "register:0:8", ["register:4040:8"]]
- 00b58cac ["INT_ADD", "register:40f0:8", ["const:b58cac:8", "const:4:8"]]
- 00b58cac ["CALLIND", null, ["register:0:8"]]
+ 00b59ca0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b59ca0 ["INT_ADD", "register:40f0:8", ["const:b59ca0:8", "const:4:8"]]
+ 00b59ca0 ["CALLIND", null, ["register:0:8"]]
- 00b58cac bytes 00013fd6
+ 00b59ca0 bytes 00013fd6
- 00b58cd8 ["INT_ADD", "register:40f0:8", ["const:b58cd8:8", "const:4:8"]]
- 00b58cd8 ["CALL", null, ["callee:00c58f80:8"]]
+ 00b59ccc ["INT_ADD", "register:40f0:8", ["const:b59ccc:8", "const:4:8"]]
+ 00b59ccc ["CALL", null, ["callee:00c58f80:8"]]
- 00b58cd8 bytes b6fc0394
+ 00b59ccc bytes adfc0394
~~~


<a id="compare-b409431cc09961e9934038a954c512d3"></a>

### [`00b58cdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58cdc.md) → [`00b59cd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b59cd0.md) _ZN8firebase8internal16JObjectReference10InitializeEP7_JavaVMP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b58d04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58cdc.md#insn-00b58d04)
- 新版 [`00b59cf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b59cd0.md#insn-00b59cf8)

~~~diff
- 00b58d04 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b58d04 ["INT_ADD", "register:40f0:8", ["const:b58d04:8", "const:4:8"]]
- 00b58d04 ["CALLIND", null, ["register:0:8"]]
+ 00b59cf8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b59cf8 ["INT_ADD", "register:40f0:8", ["const:b59cf8:8", "const:4:8"]]
+ 00b59cf8 ["CALLIND", null, ["register:0:8"]]
- 00b58d04 bytes 00013fd6
+ 00b59cf8 bytes 00013fd6
~~~


<a id="compare-51a7248cc47ad2270f58484502bca89d"></a>

### [`00b58d18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58d18.md) → [`00b59d0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b59d0c.md) _ZN8firebase8internal16JObjectReferenceC2ERKS1_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5b270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b270.md) · 呼出先 1件 [`00c5b490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b490.md)
- 新版 呼出元 1件 [`00c5c240`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c240.md) · 呼出先 1件 [`00c5c460`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c460.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b58d3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58d18.md#insn-00b58d3c) · [`00b58d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58d18.md#insn-00b58d5c)
- 新版 [`00b59d30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b59d0c.md#insn-00b59d30) · [`00b59d50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b59d0c.md#insn-00b59d50)

~~~diff
- 00b58d3c ["INT_ADD", "register:40f0:8", ["const:b58d3c:8", "const:4:8"]]
- 00b58d3c ["CALL", null, ["callee:00c5c460:8"]]
+ 00b59d30 ["INT_ADD", "register:40f0:8", ["const:b59d30:8", "const:4:8"]]
+ 00b59d30 ["CALL", null, ["callee:00c5c460:8"]]
- 00b58d3c bytes d5090494
+ 00b59d30 bytes cc090494
- 00b58d5c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b58d5c ["INT_ADD", "register:40f0:8", ["const:b58d5c:8", "const:4:8"]]
- 00b58d5c ["CALLIND", null, ["register:0:8"]]
+ 00b59d50 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b59d50 ["INT_ADD", "register:40f0:8", ["const:b59d50:8", "const:4:8"]]
+ 00b59d50 ["CALLIND", null, ["register:0:8"]]
- 00b58d5c bytes 00013fd6
+ 00b59d50 bytes 00013fd6
~~~


<a id="compare-d3939c2251b9e1416bfa0a1cc973a53f"></a>

### [`00b58da4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58da4.md) → [`00b59d98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b59d98.md) _ZN8firebase8internal16JObjectReferenceD1Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c5b280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b280.md) [`00c5b290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b290.md) · 呼出先 1件 [`00c5b490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b490.md)
- 新版 呼出元 2件 [`00c5c250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c250.md) [`00c5c260`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c260.md) · 呼出先 1件 [`00c5c460`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c460.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b58dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58da4.md#insn-00b58dbc) · [`00b58dd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58da4.md#insn-00b58dd4)
- 新版 [`00b59db0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b59d98.md#insn-00b59db0) · [`00b59dc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b59d98.md#insn-00b59dc8)

~~~diff
- 00b58dbc ["INT_ADD", "register:40f0:8", ["const:b58dbc:8", "const:4:8"]]
- 00b58dbc ["CALL", null, ["callee:00c5c460:8"]]
+ 00b59db0 ["INT_ADD", "register:40f0:8", ["const:b59db0:8", "const:4:8"]]
+ 00b59db0 ["CALL", null, ["callee:00c5c460:8"]]
- 00b58dbc bytes b5090494
+ 00b59db0 bytes ac090494
- 00b58dd4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b58dd4 ["INT_ADD", "register:40f0:8", ["const:b58dd4:8", "const:4:8"]]
- 00b58dd4 ["CALLIND", null, ["register:0:8"]]
+ 00b59dc8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b59dc8 ["INT_ADD", "register:40f0:8", ["const:b59dc8:8", "const:4:8"]]
+ 00b59dc8 ["CALLIND", null, ["register:0:8"]]
- 00b58dd4 bytes 00013fd6
+ 00b59dc8 bytes 00013fd6
~~~


<a id="compare-30b9c4e08895b2ae4b8084062b83693b"></a>

### [`00b58de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58de8.md) → [`00b59ddc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b59ddc.md) _ZN8firebase8internal16JObjectReference3SetEP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5b250`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b250.md) · 呼出先 1件 [`00c5b490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b490.md)
- 新版 呼出元 1件 [`00c5c220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c220.md) · 呼出先 1件 [`00c5c460`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c460.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b58e08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58de8.md#insn-00b58e08) · [`00b58e28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58de8.md#insn-00b58e28) · [`00b58e54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58de8.md#insn-00b58e54)
- 新版 [`00b59dfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b59ddc.md#insn-00b59dfc) · [`00b59e1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b59ddc.md#insn-00b59e1c) · [`00b59e48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b59ddc.md#insn-00b59e48)

~~~diff
- 00b58e08 ["INT_ADD", "register:40f0:8", ["const:b58e08:8", "const:4:8"]]
- 00b58e08 ["CALL", null, ["callee:00c5c460:8"]]
+ 00b59dfc ["INT_ADD", "register:40f0:8", ["const:b59dfc:8", "const:4:8"]]
+ 00b59dfc ["CALL", null, ["callee:00c5c460:8"]]
- 00b58e08 bytes a2090494
+ 00b59dfc bytes 99090494
- 00b58e28 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b58e28 ["INT_ADD", "register:40f0:8", ["const:b58e28:8", "const:4:8"]]
- 00b58e28 ["CALLIND", null, ["register:0:8"]]
+ 00b59e1c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b59e1c ["INT_ADD", "register:40f0:8", ["const:b59e1c:8", "const:4:8"]]
+ 00b59e1c ["CALLIND", null, ["register:0:8"]]
- 00b58e28 bytes 00013fd6
+ 00b59e1c bytes 00013fd6
- 00b58e54 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b58e54 ["INT_ADD", "register:40f0:8", ["const:b58e54:8", "const:4:8"]]
- 00b58e54 ["CALLIND", null, ["register:0:8"]]
+ 00b59e48 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b59e48 ["INT_ADD", "register:40f0:8", ["const:b59e48:8", "const:4:8"]]
+ 00b59e48 ["CALLIND", null, ["register:0:8"]]
- 00b58e54 bytes 00013fd6
+ 00b59e48 bytes 00013fd6
~~~


<a id="compare-761bf50686a7a2b2fa45b59d23eabb26"></a>

### [`00b58e6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58e6c.md) → [`00b59e60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b59e60.md) _ZN8firebase8internal16JObjectReferenceaSERKS1_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5b490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b490.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5c460`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c460.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b58ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58e6c.md#insn-00b58ea0) · [`00b58ec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58e6c.md#insn-00b58ec4) · [`00b58eec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58e6c.md#insn-00b58eec)
- 新版 [`00b59e94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b59e60.md#insn-00b59e94) · [`00b59eb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b59e60.md#insn-00b59eb8) · [`00b59ee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b59e60.md#insn-00b59ee0)

~~~diff
- 00b58ea0 ["INT_ADD", "register:40f0:8", ["const:b58ea0:8", "const:4:8"]]
- 00b58ea0 ["CALL", null, ["callee:00c5c460:8"]]
+ 00b59e94 ["INT_ADD", "register:40f0:8", ["const:b59e94:8", "const:4:8"]]
+ 00b59e94 ["CALL", null, ["callee:00c5c460:8"]]
- 00b58ea0 bytes 7c090494
+ 00b59e94 bytes 73090494
- 00b58ec4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b58ec4 ["INT_ADD", "register:40f0:8", ["const:b58ec4:8", "const:4:8"]]
- 00b58ec4 ["CALLIND", null, ["register:0:8"]]
+ 00b59eb8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b59eb8 ["INT_ADD", "register:40f0:8", ["const:b59eb8:8", "const:4:8"]]
+ 00b59eb8 ["CALLIND", null, ["register:0:8"]]
- 00b58ec4 bytes 00013fd6
+ 00b59eb8 bytes 00013fd6
- 00b58eec ["COPY", "register:0:8", ["register:4040:8"]]
- 00b58eec ["INT_ADD", "register:40f0:8", ["const:b58eec:8", "const:4:8"]]
- 00b58eec ["CALLIND", null, ["register:0:8"]]
+ 00b59ee0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b59ee0 ["INT_ADD", "register:40f0:8", ["const:b59ee0:8", "const:4:8"]]
+ 00b59ee0 ["CALLIND", null, ["register:0:8"]]
- 00b58eec bytes 00013fd6
+ 00b59ee0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db4e62a89210d8a525490644d6ebaaa0"></a>

### [`00b58f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58f40.md) → [`00b59f34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b59f34.md) _ZN8firebase8internal16JObjectReference3SetEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b58f84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58f40.md#insn-00b58f84) · [`00b58fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58f40.md#insn-00b58fa0) · [`00b58fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58f40.md#insn-00b58fc0)
- 新版 [`00b59f78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b59f34.md#insn-00b59f78) · [`00b59f94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b59f34.md#insn-00b59f94) · [`00b59fb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b59f34.md#insn-00b59fb4)

~~~diff
- 00b58f84 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b58f84 ["INT_ADD", "register:40f0:8", ["const:b58f84:8", "const:4:8"]]
- 00b58f84 ["CALLIND", null, ["register:0:8"]]
+ 00b59f78 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b59f78 ["INT_ADD", "register:40f0:8", ["const:b59f78:8", "const:4:8"]]
+ 00b59f78 ["CALLIND", null, ["register:0:8"]]
- 00b58f84 bytes 00013fd6
+ 00b59f78 bytes 00013fd6
- 00b58fa0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b58fa0 ["INT_ADD", "register:40f0:8", ["const:b58fa0:8", "const:4:8"]]
- 00b58fa0 ["CALLIND", null, ["register:0:8"]]
+ 00b59f94 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b59f94 ["INT_ADD", "register:40f0:8", ["const:b59f94:8", "const:4:8"]]
+ 00b59f94 ["CALLIND", null, ["register:0:8"]]
- 00b58fa0 bytes 00013fd6
+ 00b59f94 bytes 00013fd6
- 00b58fc0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b58fc0 ["INT_ADD", "register:40f0:8", ["const:b58fc0:8", "const:4:8"]]
- 00b58fc0 ["CALLIND", null, ["register:0:8"]]
+ 00b59fb4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b59fb4 ["INT_ADD", "register:40f0:8", ["const:b59fb4:8", "const:4:8"]]
+ 00b59fb4 ["CALLIND", null, ["register:0:8"]]
- 00b58fc0 bytes 00013fd6
+ 00b59fb4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-644aa99529a0dd82860ddb9821447057"></a>

### [`00b58ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58ff0.md) → [`00b59fe4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b59fe4.md) _ZNK8firebase8internal16JObjectReference11GetLocalRefEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5b2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b2a0.md) · 呼出先 1件 [`00c5b490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b490.md)
- 新版 呼出元 1件 [`00c5c270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c270.md) · 呼出先 1件 [`00c5c460`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c460.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b59008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b58/00b58ff0.md#insn-00b59008)
- 新版 [`00b59ffc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b59/00b59fe4.md#insn-00b59ffc)

~~~diff
- 00b59008 ["INT_ADD", "register:40f0:8", ["const:b59008:8", "const:4:8"]]
- 00b59008 ["CALL", null, ["callee:00c5c460:8"]]
+ 00b59ffc ["INT_ADD", "register:40f0:8", ["const:b59ffc:8", "const:4:8"]]
+ 00b59ffc ["CALL", null, ["callee:00c5c460:8"]]
- 00b59008 bytes 22090494
+ 00b59ffc bytes 19090494
~~~


<a id="compare-24c5196a99cae0267beff8a275d5b17c"></a>

### [`00b5903c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b59/00b5903c.md) → [`00b5a030`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5a/00b5a030.md) _ZN8firebase8internal16JObjectReference18FromLocalReferenceEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5b240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b240.md) · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00c5c210`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c210.md) · 呼出先 1件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b59078`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b59/00b5903c.md#insn-00b59078) · [`00b59098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b59/00b5903c.md#insn-00b59098) · [`00b590b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b59/00b5903c.md#insn-00b590b0)
- 新版 [`00b5a06c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5a/00b5a030.md#insn-00b5a06c) · [`00b5a08c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5a/00b5a030.md#insn-00b5a08c) · [`00b5a0a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5a/00b5a030.md#insn-00b5a0a4)

~~~diff
- 00b59078 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b59078 ["INT_ADD", "register:40f0:8", ["const:b59078:8", "const:4:8"]]
- 00b59078 ["CALLIND", null, ["register:0:8"]]
+ 00b5a06c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b5a06c ["INT_ADD", "register:40f0:8", ["const:b5a06c:8", "const:4:8"]]
+ 00b5a06c ["CALLIND", null, ["register:0:8"]]
- 00b59078 bytes 20013fd6
+ 00b5a06c bytes 20013fd6
- 00b59098 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b59098 ["INT_ADD", "register:40f0:8", ["const:b59098:8", "const:4:8"]]
- 00b59098 ["CALLIND", null, ["register:0:8"]]
+ 00b5a08c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5a08c ["INT_ADD", "register:40f0:8", ["const:b5a08c:8", "const:4:8"]]
+ 00b5a08c ["CALLIND", null, ["register:0:8"]]
- 00b59098 bytes 00013fd6
+ 00b5a08c bytes 00013fd6
- 00b590b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b590b0 ["INT_ADD", "register:40f0:8", ["const:b590b0:8", "const:4:8"]]
- 00b590b0 ["CALLIND", null, ["register:0:8"]]
+ 00b5a0a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5a0a4 ["INT_ADD", "register:40f0:8", ["const:b5a0a4:8", "const:4:8"]]
+ 00b5a0a4 ["CALLIND", null, ["register:0:8"]]
- 00b590b0 bytes 00013fd6
+ 00b5a0a4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c186a13235b044a1b537a9fbaa2544e"></a>

### [`00b5ac50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5a/00b5ac50.md) → [`00b5bc44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5b/00b5bc44.md) FUN_00b5bc44

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 9件 [`00b5a174`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5a/00b5a174.md) [`00b5d6d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5d6d4.md) [`00b5d798`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5d798.md) [`00b71e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b71/00b71e50.md) [`00b72ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b72/00b72ff8.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 9件 [`00b5b168`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5b/00b5b168.md) [`00b5e6c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5e/00b5e6c8.md) [`00b5e78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5e/00b5e78c.md) [`00b72e44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b72/00b72e44.md) [`00b73fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b73/00b73fec.md) · 呼出先 5件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c59020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59020.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5ac8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5a/00b5ac50.md#insn-00b5ac8c) · [`00b5aca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5a/00b5ac50.md#insn-00b5aca4) · [`00b5ace4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5a/00b5ac50.md#insn-00b5ace4)
- 新版 [`00b5bc80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5b/00b5bc44.md#insn-00b5bc80) · [`00b5bc98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5b/00b5bc44.md#insn-00b5bc98) · [`00b5bcd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5b/00b5bc44.md#insn-00b5bcd8)

~~~diff
- 00b5ac8c ["INT_ADD", "register:40f0:8", ["const:b5ac8c:8", "const:4:8"]]
- 00b5ac8c ["CALL", null, ["callee:00c59080:8"]]
+ 00b5bc80 ["INT_ADD", "register:40f0:8", ["const:b5bc80:8", "const:4:8"]]
+ 00b5bc80 ["CALL", null, ["callee:00c59080:8"]]
- 00b5ac8c bytes 09f50394
+ 00b5bc80 bytes 00f50394
- 00b5aca4 ["INT_ADD", "register:40f0:8", ["const:b5aca4:8", "const:4:8"]]
- 00b5aca4 ["CALL", null, ["callee:00c59080:8"]]
+ 00b5bc98 ["INT_ADD", "register:40f0:8", ["const:b5bc98:8", "const:4:8"]]
+ 00b5bc98 ["CALL", null, ["callee:00c59080:8"]]
- 00b5aca4 bytes 03f50394
+ 00b5bc98 bytes faf40394
- 00b5ace4 ["INT_ADD", "register:40f0:8", ["const:b5ace4:8", "const:4:8"]]
- 00b5ace4 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b5bcd8 ["INT_ADD", "register:40f0:8", ["const:b5bcd8:8", "const:4:8"]]
+ 00b5bcd8 ["CALL", null, ["callee:00c58f30:8"]]
- 00b5ace4 bytes 9ff40394
+ 00b5bcd8 bytes 96f40394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-764a124dff01e4469ab17a6d101d16ac"></a>

### [`00b5ad38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5a/00b5ad38.md) → [`00b5bd2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5b/00b5bd2c.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_mmRKS4_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b8c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b8c0.md) · 呼出先 3件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c5c890`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c890.md) · 呼出先 3件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5adb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5a/00b5ad38.md#insn-00b5adb8) · [`00b5add8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5a/00b5ad38.md#insn-00b5add8) · [`00b5adf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5a/00b5ad38.md#insn-00b5adf4)
- 新版 [`00b5bdac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5b/00b5bd2c.md#insn-00b5bdac) · [`00b5bdcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5b/00b5bd2c.md#insn-00b5bdcc) · [`00b5bde8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5b/00b5bd2c.md#insn-00b5bde8)

~~~diff
- 00b5adb8 ["INT_ADD", "register:40f0:8", ["const:b5adb8:8", "const:4:8"]]
- 00b5adb8 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b5bdac ["INT_ADD", "register:40f0:8", ["const:b5bdac:8", "const:4:8"]]
+ 00b5bdac ["CALL", null, ["callee:00c58f30:8"]]
- 00b5adb8 bytes 6af40394
+ 00b5bdac bytes 61f40394
- 00b5add8 ["INT_ADD", "register:40f0:8", ["const:b5add8:8", "const:4:8"]]
- 00b5add8 ["CALL", null, ["callee:00c590a0:8"]]
+ 00b5bdcc ["INT_ADD", "register:40f0:8", ["const:b5bdcc:8", "const:4:8"]]
+ 00b5bdcc ["CALL", null, ["callee:00c590a0:8"]]
- 00b5add8 bytes bef40394
+ 00b5bdcc bytes b5f40394
- 00b5adf4 ["INT_ADD", "register:40f0:8", ["const:b5adf4:8", "const:4:8"]]
- 00b5adf4 ["CALL", null, ["callee:00c5c1e0:8"]]
+ 00b5bde8 ["INT_ADD", "register:40f0:8", ["const:b5bde8:8", "const:4:8"]]
+ 00b5bde8 ["CALL", null, ["callee:00c5c1e0:8"]]
- 00b5adf4 bytes 07010494
+ 00b5bde8 bytes fe000494
~~~


<a id="compare-54deb9c67cd6d978c4c6fd20f7eea1b6"></a>

### [`00b5adf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5a/00b5adf8.md) → [`00b5bdec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5b/00b5bdec.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDa

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b8d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b8d0.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00c5c8a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c8a0.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5ae94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5a/00b5adf8.md#insn-00b5ae94) · [`00b5aed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5a/00b5adf8.md#insn-00b5aed4)
- 新版 [`00b5be88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5b/00b5bdec.md#insn-00b5be88) · [`00b5bec8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5b/00b5bdec.md#insn-00b5bec8)

~~~diff
- 00b5ae94 ["INT_ADD", "register:40f0:8", ["const:b5ae94:8", "const:4:8"]]
- 00b5ae94 ["CALL", null, ["callee:00c590f0:8"]]
+ 00b5be88 ["INT_ADD", "register:40f0:8", ["const:b5be88:8", "const:4:8"]]
+ 00b5be88 ["CALL", null, ["callee:00c590f0:8"]]
- 00b5ae94 bytes a3f40394
+ 00b5be88 bytes 9af40394
- 00b5aed4 ["INT_ADD", "register:40f0:8", ["const:b5aed4:8", "const:4:8"]]
- 00b5aed4 ["CALL", null, ["callee:00c590f0:8"]]
+ 00b5bec8 ["INT_ADD", "register:40f0:8", ["const:b5bec8:8", "const:4:8"]]
+ 00b5bec8 ["CALL", null, ["callee:00c590f0:8"]]
- 00b5aed4 bytes 93f40394
+ 00b5bec8 bytes 8af40394
~~~


<a id="compare-86fab598e7bbd623f37ab30fd6fa0924"></a>

### [`00b5af18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5a/00b5af18.md) → [`00b5bf0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5b/00b5bf0c.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDa

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b8e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b8e0.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00c5c8b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c8b0.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5afb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5a/00b5af18.md#insn-00b5afb0) · [`00b5aff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5a/00b5af18.md#insn-00b5aff8)
- 新版 [`00b5bfa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5b/00b5bf0c.md#insn-00b5bfa4) · [`00b5bfec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5b/00b5bf0c.md#insn-00b5bfec)

~~~diff
- 00b5afb0 ["INT_ADD", "register:40f0:8", ["const:b5afb0:8", "const:4:8"]]
- 00b5afb0 ["CALL", null, ["callee:00c590f0:8"]]
+ 00b5bfa4 ["INT_ADD", "register:40f0:8", ["const:b5bfa4:8", "const:4:8"]]
+ 00b5bfa4 ["CALL", null, ["callee:00c590f0:8"]]
- 00b5afb0 bytes 5cf40394
+ 00b5bfa4 bytes 53f40394
- 00b5aff8 ["INT_ADD", "register:40f0:8", ["const:b5aff8:8", "const:4:8"]]
- 00b5aff8 ["CALL", null, ["callee:00c590f0:8"]]
+ 00b5bfec ["INT_ADD", "register:40f0:8", ["const:b5bfec:8", "const:4:8"]]
+ 00b5bfec ["CALL", null, ["callee:00c590f0:8"]]
- 00b5aff8 bytes 4af40394
+ 00b5bfec bytes 41f40394
~~~


<a id="compare-1a3db667fa2f55716720d0439940872e"></a>

### [`00b5b02c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b02c.md) → [`00b5c020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c020.md) _ZNSt6__ndk16vectorIPN8firebase3AppENS_9allocatorIS3_EEE21__push_back_slow_pathIRKS3_EEvOT_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b910.md) · 呼出先 4件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c5c8e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c8e0.md) · 呼出先 4件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5b090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b02c.md#insn-00b5b090) · [`00b5b09c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b02c.md#insn-00b5b09c) · [`00b5b0c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b02c.md#insn-00b5b0c8)
- 新版 [`00b5c084`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c020.md#insn-00b5c084) · [`00b5c090`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c020.md#insn-00b5c090) · [`00b5c0bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c020.md#insn-00b5c0bc)

~~~diff
- 00b5b090 ["INT_ADD", "register:40f0:8", ["const:b5b090:8", "const:4:8"]]
- 00b5b090 ["CALL", null, ["callee:00c5c1e0:8"]]
+ 00b5c084 ["INT_ADD", "register:40f0:8", ["const:b5c084:8", "const:4:8"]]
+ 00b5c084 ["CALL", null, ["callee:00c5c1e0:8"]]
- 00b5b090 bytes 60000494
+ 00b5c084 bytes 57000494
- 00b5b09c ["INT_ADD", "register:40f0:8", ["const:b5b09c:8", "const:4:8"]]
- 00b5b09c ["CALL", null, ["callee:00c58f30:8"]]
+ 00b5c090 ["INT_ADD", "register:40f0:8", ["const:b5c090:8", "const:4:8"]]
+ 00b5c090 ["CALL", null, ["callee:00c58f30:8"]]
- 00b5b09c bytes b1f30394
+ 00b5c090 bytes a8f30394
- 00b5b0c8 ["INT_ADD", "register:40f0:8", ["const:b5b0c8:8", "const:4:8"]]
- 00b5b0c8 ["CALL", null, ["callee:00c590a0:8"]]
+ 00b5c0bc ["INT_ADD", "register:40f0:8", ["const:b5c0bc:8", "const:4:8"]]
+ 00b5c0bc ["CALL", null, ["callee:00c590a0:8"]]
- 00b5b0c8 bytes 02f40394
+ 00b5c0bc bytes f9f30394
~~~


<a id="compare-4e208e902ffcdc540e79168b7bee6d19"></a>

### [`00b5b114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b114.md) → [`00b5c108`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c108.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDa

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b8f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b8f0.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ad00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad00.md) [`00c5b230`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b230.md) [`00c5b6a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b6a0.md)
- 新版 呼出元 1件 [`00c5c8c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c8c0.md) · 呼出先 4件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5bcd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bcd0.md) [`00c5c200`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c200.md) [`00c5c670`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c670.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5b190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b114.md#insn-00b5b190) · [`00b5b1a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b114.md#insn-00b5b1a4) · [`00b5b1ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b114.md#insn-00b5b1ac)
- 新版 [`00b5c184`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c108.md#insn-00b5c184) · [`00b5c198`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c108.md#insn-00b5c198) · [`00b5c1a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c108.md#insn-00b5c1a0)

~~~diff
- 00b5b190 ["INT_ADD", "register:40f0:8", ["const:b5b190:8", "const:4:8"]]
- 00b5b190 ["CALL", null, ["callee:00c5c670:8"]]
+ 00b5c184 ["INT_ADD", "register:40f0:8", ["const:b5c184:8", "const:4:8"]]
+ 00b5c184 ["CALL", null, ["callee:00c5c670:8"]]
- 00b5b190 bytes 44010494
+ 00b5c184 bytes 3b010494
- 00b5b1a4 ["INT_ADD", "register:40f0:8", ["const:b5b1a4:8", "const:4:8"]]
- 00b5b1a4 ["CALL", null, ["callee:00c5c200:8"]]
+ 00b5c198 ["INT_ADD", "register:40f0:8", ["const:b5c198:8", "const:4:8"]]
+ 00b5c198 ["CALL", null, ["callee:00c5c200:8"]]
- 00b5b1a4 bytes 23000494
+ 00b5c198 bytes 1a000494
- 00b5b1ac ["INT_ADD", "register:40f0:8", ["const:b5b1ac:8", "const:4:8"]]
- 00b5b1ac ["CALL", null, ["callee:00c5bcd0:8"]]
+ 00b5c1a0 ["INT_ADD", "register:40f0:8", ["const:b5c1a0:8", "const:4:8"]]
+ 00b5c1a0 ["CALL", null, ["callee:00c5bcd0:8"]]
- 00b5b1ac bytes d5fe0394
+ 00b5c1a0 bytes ccfe0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f82bd350ebe809f440ab85870004a7ce"></a>

### [`00b5b1e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b1e4.md) → [`00b5c1d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c1d8.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10unique_ptrIN8firebase10app_common7AppDa

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b900.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5ad00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad00.md) [`00c5b230`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b230.md) [`00c5b900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b900.md)
- 新版 呼出元 1件 [`00c5c8d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c8d0.md) · 呼出先 4件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5bcd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bcd0.md) [`00c5c200`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c200.md) [`00c5c8d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c8d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5b200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b1e4.md#insn-00b5b200) · [`00b5b20c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b1e4.md#insn-00b5b20c) · [`00b5b220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b1e4.md#insn-00b5b220)
- 新版 [`00b5c1f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c1d8.md#insn-00b5c1f4) · [`00b5c200`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c1d8.md#insn-00b5c200) · [`00b5c214`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c1d8.md#insn-00b5c214)

~~~diff
- 00b5b200 ["INT_ADD", "register:40f0:8", ["const:b5b200:8", "const:4:8"]]
- 00b5b200 ["CALL", null, ["callee:00c5c8d0:8"]]
+ 00b5c1f4 ["INT_ADD", "register:40f0:8", ["const:b5c1f4:8", "const:4:8"]]
+ 00b5c1f4 ["CALL", null, ["callee:00c5c8d0:8"]]
- 00b5b200 bytes c0010494
+ 00b5c1f4 bytes b7010494
- 00b5b20c ["INT_ADD", "register:40f0:8", ["const:b5b20c:8", "const:4:8"]]
- 00b5b20c ["CALL", null, ["callee:00c5c8d0:8"]]
+ 00b5c200 ["INT_ADD", "register:40f0:8", ["const:b5c200:8", "const:4:8"]]
+ 00b5c200 ["CALL", null, ["callee:00c5c8d0:8"]]
- 00b5b20c bytes bd010494
+ 00b5c200 bytes b4010494
- 00b5b220 ["INT_ADD", "register:40f0:8", ["const:b5b220:8", "const:4:8"]]
- 00b5b220 ["CALL", null, ["callee:00c5c200:8"]]
+ 00b5c214 ["INT_ADD", "register:40f0:8", ["const:b5c214:8", "const:4:8"]]
+ 00b5c214 ["CALL", null, ["callee:00c5c200:8"]]
- 00b5b220 bytes 04000494
+ 00b5c214 bytes fbff0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6554128ba866293c153909dbe78a47c3"></a>

### [`00b5b2b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b2b0.md) → [`00b5c2a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c2a4.md) _ZNK8firebase10LoggerBase8LogDebugEPKcz

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5b328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b2b0.md#insn-00b5b328) · [`00b5b354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b2b0.md#insn-00b5b354) · [`00b5b37c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b2b0.md#insn-00b5b37c)
- 新版 [`00b5c31c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c2a4.md#insn-00b5c31c) · [`00b5c348`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c2a4.md#insn-00b5c348) · [`00b5c370`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c2a4.md#insn-00b5c370)

~~~diff
- 00b5b328 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5b328 ["INT_ADD", "register:40f0:8", ["const:b5b328:8", "const:4:8"]]
- 00b5b328 ["CALLIND", null, ["register:0:8"]]
+ 00b5c31c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5c31c ["INT_ADD", "register:40f0:8", ["const:b5c31c:8", "const:4:8"]]
+ 00b5c31c ["CALLIND", null, ["register:0:8"]]
- 00b5b328 bytes 00013fd6
+ 00b5c31c bytes 00013fd6
- 00b5b354 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5b354 ["INT_ADD", "register:40f0:8", ["const:b5b354:8", "const:4:8"]]
- 00b5b354 ["CALLIND", null, ["register:0:8"]]
+ 00b5c348 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5c348 ["INT_ADD", "register:40f0:8", ["const:b5c348:8", "const:4:8"]]
+ 00b5c348 ["CALLIND", null, ["register:0:8"]]
- 00b5b354 bytes 00013fd6
+ 00b5c348 bytes 00013fd6
- 00b5b37c ["INT_ADD", "register:40f0:8", ["const:b5b37c:8", "const:4:8"]]
- 00b5b37c ["CALL", null, ["callee:00c58f80:8"]]
+ 00b5c370 ["INT_ADD", "register:40f0:8", ["const:b5c370:8", "const:4:8"]]
+ 00b5c370 ["CALL", null, ["callee:00c58f80:8"]]
- 00b5b37c bytes 0df30394
+ 00b5c370 bytes 04f30394
~~~


<a id="compare-5051a390ae8d1b89d7ef0dfe7ff90fab"></a>

### [`00b5b380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b380.md) → [`00b5c374`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c374.md) _ZNK8firebase10LoggerBase17FilterLogMessageVENS_8LogLevelEPKcSt9__va_list

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5b3bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b380.md#insn-00b5b3bc) · [`00b5b3e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b380.md#insn-00b5b3e8) · [`00b5b414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b380.md#insn-00b5b414)
- 新版 [`00b5c3b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c374.md#insn-00b5c3b0) · [`00b5c3dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c374.md#insn-00b5c3dc) · [`00b5c408`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c374.md#insn-00b5c408)

~~~diff
- 00b5b3bc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5b3bc ["INT_ADD", "register:40f0:8", ["const:b5b3bc:8", "const:4:8"]]
- 00b5b3bc ["CALLIND", null, ["register:0:8"]]
+ 00b5c3b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5c3b0 ["INT_ADD", "register:40f0:8", ["const:b5c3b0:8", "const:4:8"]]
+ 00b5c3b0 ["CALLIND", null, ["register:0:8"]]
- 00b5b3bc bytes 00013fd6
+ 00b5c3b0 bytes 00013fd6
- 00b5b3e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5b3e8 ["INT_ADD", "register:40f0:8", ["const:b5b3e8:8", "const:4:8"]]
- 00b5b3e8 ["CALLIND", null, ["register:0:8"]]
+ 00b5c3dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5c3dc ["INT_ADD", "register:40f0:8", ["const:b5c3dc:8", "const:4:8"]]
+ 00b5c3dc ["CALLIND", null, ["register:0:8"]]
- 00b5b3e8 bytes 00013fd6
+ 00b5c3dc bytes 00013fd6
- 00b5b414 ["INT_ADD", "register:40f0:8", ["const:b5b414:8", "const:4:8"]]
- 00b5b414 ["CALL", null, ["callee:00c58f80:8"]]
+ 00b5c408 ["INT_ADD", "register:40f0:8", ["const:b5c408:8", "const:4:8"]]
+ 00b5c408 ["CALL", null, ["callee:00c58f80:8"]]
- 00b5b414 bytes e7f20394
+ 00b5c408 bytes def20394
~~~


<a id="compare-f571cf99546fed0ba5fc15e85b703dd5"></a>

### [`00b5b418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b418.md) → [`00b5c40c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c40c.md) _ZNK8firebase10LoggerBase7LogInfoEPKcz

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5b490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b418.md#insn-00b5b490) · [`00b5b4bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b418.md#insn-00b5b4bc) · [`00b5b4e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b418.md#insn-00b5b4e4)
- 新版 [`00b5c484`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c40c.md#insn-00b5c484) · [`00b5c4b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c40c.md#insn-00b5c4b0) · [`00b5c4d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c40c.md#insn-00b5c4d8)

~~~diff
- 00b5b490 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5b490 ["INT_ADD", "register:40f0:8", ["const:b5b490:8", "const:4:8"]]
- 00b5b490 ["CALLIND", null, ["register:0:8"]]
+ 00b5c484 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5c484 ["INT_ADD", "register:40f0:8", ["const:b5c484:8", "const:4:8"]]
+ 00b5c484 ["CALLIND", null, ["register:0:8"]]
- 00b5b490 bytes 00013fd6
+ 00b5c484 bytes 00013fd6
- 00b5b4bc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5b4bc ["INT_ADD", "register:40f0:8", ["const:b5b4bc:8", "const:4:8"]]
- 00b5b4bc ["CALLIND", null, ["register:0:8"]]
+ 00b5c4b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5c4b0 ["INT_ADD", "register:40f0:8", ["const:b5c4b0:8", "const:4:8"]]
+ 00b5c4b0 ["CALLIND", null, ["register:0:8"]]
- 00b5b4bc bytes 00013fd6
+ 00b5c4b0 bytes 00013fd6
- 00b5b4e4 ["INT_ADD", "register:40f0:8", ["const:b5b4e4:8", "const:4:8"]]
- 00b5b4e4 ["CALL", null, ["callee:00c58f80:8"]]
+ 00b5c4d8 ["INT_ADD", "register:40f0:8", ["const:b5c4d8:8", "const:4:8"]]
+ 00b5c4d8 ["CALL", null, ["callee:00c58f80:8"]]
- 00b5b4e4 bytes b3f20394
+ 00b5c4d8 bytes aaf20394
~~~


<a id="compare-c90620767818eca3653e951bd36f2aa8"></a>

### [`00b5b4e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b4e8.md) → [`00b5c4dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c4dc.md) _ZNK8firebase10LoggerBase10LogWarningEPKcz

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5b560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b4e8.md#insn-00b5b560) · [`00b5b58c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b4e8.md#insn-00b5b58c) · [`00b5b5b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b4e8.md#insn-00b5b5b4)
- 新版 [`00b5c554`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c4dc.md#insn-00b5c554) · [`00b5c580`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c4dc.md#insn-00b5c580) · [`00b5c5a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c4dc.md#insn-00b5c5a8)

~~~diff
- 00b5b560 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5b560 ["INT_ADD", "register:40f0:8", ["const:b5b560:8", "const:4:8"]]
- 00b5b560 ["CALLIND", null, ["register:0:8"]]
+ 00b5c554 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5c554 ["INT_ADD", "register:40f0:8", ["const:b5c554:8", "const:4:8"]]
+ 00b5c554 ["CALLIND", null, ["register:0:8"]]
- 00b5b560 bytes 00013fd6
+ 00b5c554 bytes 00013fd6
- 00b5b58c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5b58c ["INT_ADD", "register:40f0:8", ["const:b5b58c:8", "const:4:8"]]
- 00b5b58c ["CALLIND", null, ["register:0:8"]]
+ 00b5c580 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5c580 ["INT_ADD", "register:40f0:8", ["const:b5c580:8", "const:4:8"]]
+ 00b5c580 ["CALLIND", null, ["register:0:8"]]
- 00b5b58c bytes 00013fd6
+ 00b5c580 bytes 00013fd6
- 00b5b5b4 ["INT_ADD", "register:40f0:8", ["const:b5b5b4:8", "const:4:8"]]
- 00b5b5b4 ["CALL", null, ["callee:00c58f80:8"]]
+ 00b5c5a8 ["INT_ADD", "register:40f0:8", ["const:b5c5a8:8", "const:4:8"]]
+ 00b5c5a8 ["CALL", null, ["callee:00c58f80:8"]]
- 00b5b5b4 bytes 7ff20394
+ 00b5c5a8 bytes 76f20394
~~~


<a id="compare-aa55c69b50a58e46163c75f8c89db62e"></a>

### [`00b5b5b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b5b8.md) → [`00b5c5ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c5ac.md) _ZNK8firebase10LoggerBase8LogErrorEPKcz

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5b630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b5b8.md#insn-00b5b630) · [`00b5b65c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b5b8.md#insn-00b5b65c) · [`00b5b684`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b5b8.md#insn-00b5b684)
- 新版 [`00b5c624`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c5ac.md#insn-00b5c624) · [`00b5c650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c5ac.md#insn-00b5c650) · [`00b5c678`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c5ac.md#insn-00b5c678)

~~~diff
- 00b5b630 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5b630 ["INT_ADD", "register:40f0:8", ["const:b5b630:8", "const:4:8"]]
- 00b5b630 ["CALLIND", null, ["register:0:8"]]
+ 00b5c624 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5c624 ["INT_ADD", "register:40f0:8", ["const:b5c624:8", "const:4:8"]]
+ 00b5c624 ["CALLIND", null, ["register:0:8"]]
- 00b5b630 bytes 00013fd6
+ 00b5c624 bytes 00013fd6
- 00b5b65c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5b65c ["INT_ADD", "register:40f0:8", ["const:b5b65c:8", "const:4:8"]]
- 00b5b65c ["CALLIND", null, ["register:0:8"]]
+ 00b5c650 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5c650 ["INT_ADD", "register:40f0:8", ["const:b5c650:8", "const:4:8"]]
+ 00b5c650 ["CALLIND", null, ["register:0:8"]]
- 00b5b65c bytes 00013fd6
+ 00b5c650 bytes 00013fd6
- 00b5b684 ["INT_ADD", "register:40f0:8", ["const:b5b684:8", "const:4:8"]]
- 00b5b684 ["CALL", null, ["callee:00c58f80:8"]]
+ 00b5c678 ["INT_ADD", "register:40f0:8", ["const:b5c678:8", "const:4:8"]]
+ 00b5c678 ["CALL", null, ["callee:00c58f80:8"]]
- 00b5b684 bytes 4bf20394
+ 00b5c678 bytes 42f20394
~~~


<a id="compare-2b6096a8ae035aec81ab9c540fd7c9cb"></a>

### [`00b5b688`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b688.md) → [`00b5c67c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c67c.md) _ZNK8firebase10LoggerBase9LogAssertEPKcz

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5b700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b688.md#insn-00b5b700) · [`00b5b72c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b688.md#insn-00b5b72c) · [`00b5b754`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b688.md#insn-00b5b754)
- 新版 [`00b5c6f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c67c.md#insn-00b5c6f4) · [`00b5c720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c67c.md#insn-00b5c720) · [`00b5c748`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c67c.md#insn-00b5c748)

~~~diff
- 00b5b700 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5b700 ["INT_ADD", "register:40f0:8", ["const:b5b700:8", "const:4:8"]]
- 00b5b700 ["CALLIND", null, ["register:0:8"]]
+ 00b5c6f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5c6f4 ["INT_ADD", "register:40f0:8", ["const:b5c6f4:8", "const:4:8"]]
+ 00b5c6f4 ["CALLIND", null, ["register:0:8"]]
- 00b5b700 bytes 00013fd6
+ 00b5c6f4 bytes 00013fd6
- 00b5b72c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5b72c ["INT_ADD", "register:40f0:8", ["const:b5b72c:8", "const:4:8"]]
- 00b5b72c ["CALLIND", null, ["register:0:8"]]
+ 00b5c720 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5c720 ["INT_ADD", "register:40f0:8", ["const:b5c720:8", "const:4:8"]]
+ 00b5c720 ["CALLIND", null, ["register:0:8"]]
- 00b5b72c bytes 00013fd6
+ 00b5c720 bytes 00013fd6
- 00b5b754 ["INT_ADD", "register:40f0:8", ["const:b5b754:8", "const:4:8"]]
- 00b5b754 ["CALL", null, ["callee:00c58f80:8"]]
+ 00b5c748 ["INT_ADD", "register:40f0:8", ["const:b5c748:8", "const:4:8"]]
+ 00b5c748 ["CALL", null, ["callee:00c58f80:8"]]
- 00b5b754 bytes 17f20394
+ 00b5c748 bytes 0ef20394
~~~


<a id="compare-8da443b9613991c6e5b45d6518b75884"></a>

### [`00b5b758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b758.md) → [`00b5c74c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c74c.md) _ZNK8firebase10LoggerBase10LogMessageENS_8LogLevelEPKcz

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5b7d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b758.md#insn-00b5b7d8) · [`00b5b804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b758.md#insn-00b5b804) · [`00b5b830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b758.md#insn-00b5b830)
- 新版 [`00b5c7cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c74c.md#insn-00b5c7cc) · [`00b5c7f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c74c.md#insn-00b5c7f8) · [`00b5c824`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c74c.md#insn-00b5c824)

~~~diff
- 00b5b7d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5b7d8 ["INT_ADD", "register:40f0:8", ["const:b5b7d8:8", "const:4:8"]]
- 00b5b7d8 ["CALLIND", null, ["register:0:8"]]
+ 00b5c7cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5c7cc ["INT_ADD", "register:40f0:8", ["const:b5c7cc:8", "const:4:8"]]
+ 00b5c7cc ["CALLIND", null, ["register:0:8"]]
- 00b5b7d8 bytes 00013fd6
+ 00b5c7cc bytes 00013fd6
- 00b5b804 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5b804 ["INT_ADD", "register:40f0:8", ["const:b5b804:8", "const:4:8"]]
- 00b5b804 ["CALLIND", null, ["register:0:8"]]
+ 00b5c7f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5c7f8 ["INT_ADD", "register:40f0:8", ["const:b5c7f8:8", "const:4:8"]]
+ 00b5c7f8 ["CALLIND", null, ["register:0:8"]]
- 00b5b804 bytes 00013fd6
+ 00b5c7f8 bytes 00013fd6
- 00b5b830 ["INT_ADD", "register:40f0:8", ["const:b5b830:8", "const:4:8"]]
- 00b5b830 ["CALL", null, ["callee:00c58f80:8"]]
+ 00b5c824 ["INT_ADD", "register:40f0:8", ["const:b5c824:8", "const:4:8"]]
+ 00b5c824 ["CALL", null, ["callee:00c58f80:8"]]
- 00b5b830 bytes e0f10394
+ 00b5c824 bytes d7f10394
~~~


<a id="compare-d858996e8db5af2c088573ce548ff032"></a>

### [`00b5b834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b834.md) → [`00b5c828`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c828.md) _ZNK8firebase10LoggerBase11LogMessageVENS_8LogLevelEPKcSt9__va_list

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5b870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b834.md#insn-00b5b870) · [`00b5b89c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b834.md#insn-00b5b89c) · [`00b5b8c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b834.md#insn-00b5b8c4)
- 新版 [`00b5c864`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c828.md#insn-00b5c864) · [`00b5c890`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c828.md#insn-00b5c890) · [`00b5c8b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c828.md#insn-00b5c8b8)

~~~diff
- 00b5b870 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5b870 ["INT_ADD", "register:40f0:8", ["const:b5b870:8", "const:4:8"]]
- 00b5b870 ["CALLIND", null, ["register:0:8"]]
+ 00b5c864 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5c864 ["INT_ADD", "register:40f0:8", ["const:b5c864:8", "const:4:8"]]
+ 00b5c864 ["CALLIND", null, ["register:0:8"]]
- 00b5b870 bytes 00013fd6
+ 00b5c864 bytes 00013fd6
- 00b5b89c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5b89c ["INT_ADD", "register:40f0:8", ["const:b5b89c:8", "const:4:8"]]
- 00b5b89c ["CALLIND", null, ["register:0:8"]]
+ 00b5c890 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5c890 ["INT_ADD", "register:40f0:8", ["const:b5c890:8", "const:4:8"]]
+ 00b5c890 ["CALLIND", null, ["register:0:8"]]
- 00b5b89c bytes 00013fd6
+ 00b5c890 bytes 00013fd6
- 00b5b8c4 ["INT_ADD", "register:40f0:8", ["const:b5b8c4:8", "const:4:8"]]
- 00b5b8c4 ["CALL", null, ["callee:00c58f80:8"]]
+ 00b5c8b8 ["INT_ADD", "register:40f0:8", ["const:b5c8b8:8", "const:4:8"]]
+ 00b5c8b8 ["CALL", null, ["callee:00c58f80:8"]]
- 00b5b8c4 bytes bbf10394
+ 00b5c8b8 bytes b2f10394
~~~


<a id="compare-e6b57304b26439ad0dc47e1cafda6fc1"></a>

### [`00b5b8d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b8d8.md) → [`00b5c8cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c8cc.md) _ZNK8firebase12SystemLogger15LogMessageImplVENS_8LogLevelEPKcSt9__va_list

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5b1f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b1f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5c1c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5b90c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b8d8.md#insn-00b5b90c) · [`00b5b930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b8d8.md#insn-00b5b930)
- 新版 [`00b5c900`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c8cc.md#insn-00b5c900) · [`00b5c924`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c8cc.md#insn-00b5c924)

~~~diff
- 00b5b90c ["INT_ADD", "register:40f0:8", ["const:b5b90c:8", "const:4:8"]]
- 00b5b90c ["CALL", null, ["callee:00c5c1c0:8"]]
+ 00b5c900 ["INT_ADD", "register:40f0:8", ["const:b5c900:8", "const:4:8"]]
+ 00b5c900 ["CALL", null, ["callee:00c5c1c0:8"]]
- 00b5b90c bytes 39fe0394
+ 00b5c900 bytes 30fe0394
- 00b5b930 ["INT_ADD", "register:40f0:8", ["const:b5b930:8", "const:4:8"]]
- 00b5b930 ["CALL", null, ["callee:00c58f80:8"]]
+ 00b5c924 ["INT_ADD", "register:40f0:8", ["const:b5c924:8", "const:4:8"]]
+ 00b5c924 ["CALL", null, ["callee:00c58f80:8"]]
- 00b5b930 bytes a0f10394
+ 00b5c924 bytes 97f10394
~~~


<a id="compare-968d4533a53838a257302a95d028ce00"></a>

### [`00b5b948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b948.md) → [`00b5c93c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c93c.md) _ZNK8firebase6Logger15LogMessageImplVENS_8LogLevelEPKcSt9__va_list

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5b988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b948.md#insn-00b5b988) · [`00b5b9b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b948.md#insn-00b5b9b4) · [`00b5b9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5b948.md#insn-00b5b9dc)
- 新版 [`00b5c97c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c93c.md#insn-00b5c97c) · [`00b5c9a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c93c.md#insn-00b5c9a8) · [`00b5c9d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5c93c.md#insn-00b5c9d0)

~~~diff
- 00b5b988 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5b988 ["INT_ADD", "register:40f0:8", ["const:b5b988:8", "const:4:8"]]
- 00b5b988 ["CALLIND", null, ["register:0:8"]]
+ 00b5c97c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5c97c ["INT_ADD", "register:40f0:8", ["const:b5c97c:8", "const:4:8"]]
+ 00b5c97c ["CALLIND", null, ["register:0:8"]]
- 00b5b988 bytes 00013fd6
+ 00b5c97c bytes 00013fd6
- 00b5b9b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5b9b4 ["INT_ADD", "register:40f0:8", ["const:b5b9b4:8", "const:4:8"]]
- 00b5b9b4 ["CALLIND", null, ["register:0:8"]]
+ 00b5c9a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5c9a8 ["INT_ADD", "register:40f0:8", ["const:b5c9a8:8", "const:4:8"]]
+ 00b5c9a8 ["CALLIND", null, ["register:0:8"]]
- 00b5b9b4 bytes 00013fd6
+ 00b5c9a8 bytes 00013fd6
- 00b5b9dc ["INT_ADD", "register:40f0:8", ["const:b5b9dc:8", "const:4:8"]]
- 00b5b9dc ["CALL", null, ["callee:00c58f80:8"]]
+ 00b5c9d0 ["INT_ADD", "register:40f0:8", ["const:b5c9d0:8", "const:4:8"]]
+ 00b5c9d0 ["CALL", null, ["callee:00c58f80:8"]]
- 00b5b9dc bytes 75f10394
+ 00b5c9d0 bytes 6cf10394
~~~


<a id="compare-962cf2ecf7785ea780b20c7e47d627e8"></a>

### [`00b5bac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5bac8.md) → [`00b5cabc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5cabc.md) _ZN8firebase8callback18CallbackDispatcher14FlushCallbacksEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5bbf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bbf0.md) · 呼出先 4件 [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)
- 新版 呼出元 1件 [`00c5cbc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cbc0.md) · 呼出先 4件 [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5bae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5bac8.md#insn-00b5bae8) · [`00b5bb00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5bac8.md#insn-00b5bb00) · [`00b5bb44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5bac8.md#insn-00b5bb44)
- 新版 [`00b5cadc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5cabc.md#insn-00b5cadc) · [`00b5caf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5cabc.md#insn-00b5caf4) · [`00b5cb38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5cabc.md#insn-00b5cb38)

~~~diff
- 00b5bae8 ["INT_ADD", "register:40f0:8", ["const:b5bae8:8", "const:4:8"]]
- 00b5bae8 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b5cadc ["INT_ADD", "register:40f0:8", ["const:b5cadc:8", "const:4:8"]]
+ 00b5cadc ["CALL", null, ["callee:00c5baa0:8"]]
- 00b5bae8 bytes fafb0394
+ 00b5cadc bytes f1fb0394
- 00b5bb00 ["INT_ADD", "register:40f0:8", ["const:b5bb00:8", "const:4:8"]]
- 00b5bb00 ["CALL", null, ["callee:00c58f50:8"]]
+ 00b5caf4 ["INT_ADD", "register:40f0:8", ["const:b5caf4:8", "const:4:8"]]
+ 00b5caf4 ["CALL", null, ["callee:00c58f50:8"]]
- 00b5bb00 bytes 20f10394
+ 00b5caf4 bytes 17f10394
- 00b5bb44 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5bb44 ["INT_ADD", "register:40f0:8", ["const:b5bb44:8", "const:4:8"]]
- 00b5bb44 ["CALLIND", null, ["register:0:8"]]
+ 00b5cb38 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5cb38 ["INT_ADD", "register:40f0:8", ["const:b5cb38:8", "const:4:8"]]
+ 00b5cb38 ["CALLIND", null, ["register:0:8"]]
- 00b5bb44 bytes 00013fd6
+ 00b5cb38 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fbeec6053a485bc713bc49c109727c1b"></a>

### [`00b5c1c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5c1c0.md) → [`00b5d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5d1b4.md) _ZN8firebase8callback18CallbackDispatcher17DispatchCallbacksEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5bc00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bc00.md) · 呼出先 5件 [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5bbd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bbd0.md)
- 新版 呼出元 1件 [`00c5cbd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cbd0.md) · 呼出先 5件 [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5cba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cba0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5c1e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5c1c0.md#insn-00b5c1e4) · [`00b5c268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5c1c0.md#insn-00b5c268) · [`00b5c270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5c1c0.md#insn-00b5c270)
- 新版 [`00b5d1d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5d1b4.md#insn-00b5d1d8) · [`00b5d25c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5d1b4.md#insn-00b5d25c) · [`00b5d264`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5d1b4.md#insn-00b5d264)

~~~diff
- 00b5c1e4 ["INT_ADD", "register:40f0:8", ["const:b5c1e4:8", "const:4:8"]]
- 00b5c1e4 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b5d1d8 ["INT_ADD", "register:40f0:8", ["const:b5d1d8:8", "const:4:8"]]
+ 00b5d1d8 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b5c1e4 bytes 3bfa0394
+ 00b5d1d8 bytes 32fa0394
- 00b5c268 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5c268 ["INT_ADD", "register:40f0:8", ["const:b5c268:8", "const:4:8"]]
- 00b5c268 ["CALLIND", null, ["register:0:8"]]
+ 00b5d25c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5d25c ["INT_ADD", "register:40f0:8", ["const:b5d25c:8", "const:4:8"]]
+ 00b5d25c ["CALLIND", null, ["register:0:8"]]
- 00b5c268 bytes 00013fd6
+ 00b5d25c bytes 00013fd6
- 00b5c270 ["INT_ADD", "register:40f0:8", ["const:b5c270:8", "const:4:8"]]
- 00b5c270 ["CALL", null, ["callee:00c58f20:8"]]
+ 00b5d264 ["INT_ADD", "register:40f0:8", ["const:b5d264:8", "const:4:8"]]
+ 00b5d264 ["CALL", null, ["callee:00c58f20:8"]]
- 00b5c270 bytes 38ef0394
+ 00b5d264 bytes 2fef0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe99b961679abd170e017664b358a287"></a>

### [`00b5c590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5c590.md) → [`00b5d584`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5d584.md) _ZNSt6__ndk120__shared_ptr_emplaceIN8firebase8callback13CallbackEntryENS_9allocatorIS3_EEE16__on_zero_sharedEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b5bd48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5bd48.md) · 呼出先 2件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)
- 新版 呼出元 1件 [`00b5cd3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5c/00b5cd3c.md) · 呼出先 2件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5c5ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5c590.md#insn-00b5c5ac) · [`00b5c5dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5c590.md#insn-00b5c5dc)
- 新版 [`00b5d5a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5d584.md#insn-00b5d5a0) · [`00b5d5d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5d584.md#insn-00b5d5d0)

~~~diff
- 00b5c5ac ["INT_ADD", "register:40f0:8", ["const:b5c5ac:8", "const:4:8"]]
- 00b5c5ac ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b5d5a0 ["INT_ADD", "register:40f0:8", ["const:b5d5a0:8", "const:4:8"]]
+ 00b5d5a0 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b5c5ac bytes 49f90394
+ 00b5d5a0 bytes 40f90394
- 00b5c5dc ["INT_ADD", "register:40f0:8", ["const:b5c5dc:8", "const:4:8"]]
- 00b5c5dc ["CALL", null, ["callee:00c5bab0:8"]]
+ 00b5d5d0 ["INT_ADD", "register:40f0:8", ["const:b5d5d0:8", "const:4:8"]]
+ 00b5d5d0 ["CALL", null, ["callee:00c5bab0:8"]]
- 00b5c5dc bytes 41f90394
+ 00b5d5d0 bytes 38f90394
~~~


<a id="compare-04ff22f61d583dbe4661e0a614099bdd"></a>

### [`00b5c6b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5c6b4.md) → [`00b5d6a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5d6a8.md) _ZN8firebase8callback13CallbackEntry7ExecuteEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5bbd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bbd0.md) · 呼出先 2件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)
- 新版 呼出元 1件 [`00c5cba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cba0.md) · 呼出先 2件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5c6d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5c6b4.md#insn-00b5c6d0) · [`00b5c6e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5c6b4.md#insn-00b5c6e8) · [`00b5c6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5c6b4.md#insn-00b5c6f8)
- 新版 [`00b5d6c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5d6a8.md#insn-00b5d6c4) · [`00b5d6dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5d6a8.md#insn-00b5d6dc) · [`00b5d6ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5d6a8.md#insn-00b5d6ec)

~~~diff
- 00b5c6d0 ["INT_ADD", "register:40f0:8", ["const:b5c6d0:8", "const:4:8"]]
- 00b5c6d0 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b5d6c4 ["INT_ADD", "register:40f0:8", ["const:b5d6c4:8", "const:4:8"]]
+ 00b5d6c4 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b5c6d0 bytes 00f90394
+ 00b5d6c4 bytes f7f80394
- 00b5c6e8 ["INT_ADD", "register:40f0:8", ["const:b5c6e8:8", "const:4:8"]]
- 00b5c6e8 ["CALL", null, ["callee:00c5bab0:8"]]
+ 00b5d6dc ["INT_ADD", "register:40f0:8", ["const:b5d6dc:8", "const:4:8"]]
+ 00b5d6dc ["CALL", null, ["callee:00c5bab0:8"]]
- 00b5c6e8 bytes fef80394
+ 00b5d6dc bytes f5f80394
- 00b5c6f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5c6f8 ["INT_ADD", "register:40f0:8", ["const:b5c6f8:8", "const:4:8"]]
- 00b5c6f8 ["CALLIND", null, ["register:0:8"]]
+ 00b5d6ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5d6ec ["INT_ADD", "register:40f0:8", ["const:b5d6ec:8", "const:4:8"]]
+ 00b5d6ec ["CALLIND", null, ["register:0:8"]]
- 00b5c6f8 bytes 00013fd6
+ 00b5d6ec bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed6f05b8d53d6182b703771e8284f04a"></a>

### [`00b5c920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5c920.md) → [`00b5d914`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5d914.md) _ZN8firebase15CleanupNotifier10CleanupAllEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5b860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b860.md) · 呼出先 3件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ace0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ace0.md)
- 新版 呼出元 1件 [`00c5c830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c830.md) · 呼出先 3件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bcb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bcb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5c934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5c920.md#insn-00b5c934) · [`00b5c958`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5c920.md#insn-00b5c958) · [`00b5c964`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5c920.md#insn-00b5c964)
- 新版 [`00b5d928`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5d914.md#insn-00b5d928) · [`00b5d94c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5d914.md#insn-00b5d94c) · [`00b5d958`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5d914.md#insn-00b5d958)

~~~diff
- 00b5c934 ["INT_ADD", "register:40f0:8", ["const:b5c934:8", "const:4:8"]]
- 00b5c934 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b5d928 ["INT_ADD", "register:40f0:8", ["const:b5d928:8", "const:4:8"]]
+ 00b5d928 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b5c934 bytes 67f80394
+ 00b5d928 bytes 5ef80394
- 00b5c958 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5c958 ["INT_ADD", "register:40f0:8", ["const:b5c958:8", "const:4:8"]]
- 00b5c958 ["CALLIND", null, ["register:0:8"]]
+ 00b5d94c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5d94c ["INT_ADD", "register:40f0:8", ["const:b5d94c:8", "const:4:8"]]
+ 00b5d94c ["CALLIND", null, ["register:0:8"]]
- 00b5c958 bytes 00013fd6
+ 00b5d94c bytes 00013fd6
- 00b5c964 ["INT_ADD", "register:40f0:8", ["const:b5c964:8", "const:4:8"]]
- 00b5c964 ["CALL", null, ["callee:00c5bcb0:8"]]
+ 00b5d958 ["INT_ADD", "register:40f0:8", ["const:b5d958:8", "const:4:8"]]
+ 00b5d958 ["CALL", null, ["callee:00c5bcb0:8"]]
- 00b5c964 bytes dff80394
+ 00b5d958 bytes d6f80394
~~~


<a id="compare-021d7f954bdbda6f192fca07ea79b9ef"></a>

### [`00b5ca54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5ca54.md) → [`00b5da48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5da48.md) _ZN8firebase15CleanupNotifier14RegisterObjectEPvPFvS1_E

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5acd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5acd0.md) · 呼出先 4件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5b6b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b6b0.md)
- 新版 呼出元 1件 [`00c5bca0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bca0.md) · 呼出先 4件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5c680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c680.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5ca74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5ca54.md#insn-00b5ca74) · [`00b5cb28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5ca54.md#insn-00b5cb28) · [`00b5cb5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5ca54.md#insn-00b5cb5c)
- 新版 [`00b5da68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5da48.md#insn-00b5da68) · [`00b5db1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5da48.md#insn-00b5db1c) · [`00b5db50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5da48.md#insn-00b5db50)

~~~diff
- 00b5ca74 ["INT_ADD", "register:40f0:8", ["const:b5ca74:8", "const:4:8"]]
- 00b5ca74 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b5da68 ["INT_ADD", "register:40f0:8", ["const:b5da68:8", "const:4:8"]]
+ 00b5da68 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b5ca74 bytes 17f80394
+ 00b5da68 bytes 0ef80394
- 00b5cb28 ["INT_ADD", "register:40f0:8", ["const:b5cb28:8", "const:4:8"]]
- 00b5cb28 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b5db1c ["INT_ADD", "register:40f0:8", ["const:b5db1c:8", "const:4:8"]]
+ 00b5db1c ["CALL", null, ["callee:00c58f30:8"]]
- 00b5cb28 bytes 0eed0394
+ 00b5db1c bytes 05ed0394
- 00b5cb5c ["INT_ADD", "register:40f0:8", ["const:b5cb5c:8", "const:4:8"]]
- 00b5cb5c ["CALL", null, ["callee:00c5c680:8"]]
+ 00b5db50 ["INT_ADD", "register:40f0:8", ["const:b5db50:8", "const:4:8"]]
+ 00b5db50 ["CALL", null, ["callee:00c5c680:8"]]
- 00b5cb5c bytes d5fa0394
+ 00b5db50 bytes ccfa0394
~~~


<a id="compare-63f26a3466251a1526e4e43015305fce"></a>

### [`00b5cb84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5cb84.md) → [`00b5db78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5db78.md) _ZN8firebase15CleanupNotifier16UnregisterObjectEPv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ace0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ace0.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5b6a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b6a0.md)
- 新版 呼出元 1件 [`00c5bcb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bcb0.md) · 呼出先 4件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5c670`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c670.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5cb9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5cb84.md#insn-00b5cb9c) · [`00b5cc44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5cb84.md#insn-00b5cc44) · [`00b5cc4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5c/00b5cb84.md#insn-00b5cc4c)
- 新版 [`00b5db90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5db78.md#insn-00b5db90) · [`00b5dc38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5db78.md#insn-00b5dc38) · [`00b5dc40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5db78.md#insn-00b5dc40)

~~~diff
- 00b5cb9c ["INT_ADD", "register:40f0:8", ["const:b5cb9c:8", "const:4:8"]]
- 00b5cb9c ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b5db90 ["INT_ADD", "register:40f0:8", ["const:b5db90:8", "const:4:8"]]
+ 00b5db90 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b5cb9c bytes cdf70394
+ 00b5db90 bytes c4f70394
- 00b5cc44 ["INT_ADD", "register:40f0:8", ["const:b5cc44:8", "const:4:8"]]
- 00b5cc44 ["CALL", null, ["callee:00c5c670:8"]]
+ 00b5dc38 ["INT_ADD", "register:40f0:8", ["const:b5dc38:8", "const:4:8"]]
+ 00b5dc38 ["CALL", null, ["callee:00c5c670:8"]]
- 00b5cc44 bytes 97fa0394
+ 00b5dc38 bytes 8efa0394
- 00b5cc4c ["INT_ADD", "register:40f0:8", ["const:b5cc4c:8", "const:4:8"]]
- 00b5cc4c ["CALL", null, ["callee:00c58f50:8"]]
+ 00b5dc40 ["INT_ADD", "register:40f0:8", ["const:b5dc40:8", "const:4:8"]]
+ 00b5dc40 ["CALL", null, ["callee:00c58f50:8"]]
- 00b5cc4c bytes cdec0394
+ 00b5dc40 bytes c4ec0394
~~~


<a id="compare-132f5e836a4fdeada6c6aa72436b6bbb"></a>

### [`00b5d08c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5d08c.md) → [`00b5e080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5e/00b5e080.md) _ZNSt6__ndk16__treeINS_12__value_typeIPvPFvS2_EEENS_19__map_value_compareIS2_S5_NS_4lessIS2_EELb1EEENS_9allocatorIS5_EEE7destroyEPNS_11__tre

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5bc90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bc90.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bc90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bc90.md)
- 新版 呼出元 1件 [`00c5cc60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cc60.md) · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5cc60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cc60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5d0a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5d08c.md#insn-00b5d0a8) · [`00b5d0b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5d08c.md#insn-00b5d0b4)
- 新版 [`00b5e09c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5e/00b5e080.md#insn-00b5e09c) · [`00b5e0a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5e/00b5e080.md#insn-00b5e0a8)

~~~diff
- 00b5d0a8 ["INT_ADD", "register:40f0:8", ["const:b5d0a8:8", "const:4:8"]]
- 00b5d0a8 ["CALL", null, ["callee:00c5cc60:8"]]
+ 00b5e09c ["INT_ADD", "register:40f0:8", ["const:b5e09c:8", "const:4:8"]]
+ 00b5e09c ["CALL", null, ["callee:00c5cc60:8"]]
- 00b5d0a8 bytes fafa0394
+ 00b5e09c bytes f1fa0394
- 00b5d0b4 ["INT_ADD", "register:40f0:8", ["const:b5d0b4:8", "const:4:8"]]
- 00b5d0b4 ["CALL", null, ["callee:00c5cc60:8"]]
+ 00b5e0a8 ["INT_ADD", "register:40f0:8", ["const:b5e0a8:8", "const:4:8"]]
+ 00b5e0a8 ["CALL", null, ["callee:00c5cc60:8"]]
- 00b5d0b4 bytes f7fa0394
+ 00b5e0a8 bytes eefa0394
~~~


<a id="compare-ed710f4e83a63ac3246eff60a965a2b0"></a>

### [`00b5d0cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5d0cc.md) → [`00b5e0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5e/00b5e0c0.md) _ZNSt6__ndk16__treeINS_12__value_typeIPvPN8firebase15CleanupNotifierEEENS_19__map_value_compareIS2_S6_NS_4lessIS2_EELb1EEENS_9allocatorIS6_E

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5bca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bca0.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bca0.md)
- 新版 呼出元 1件 [`00c5cc70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cc70.md) · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5cc70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cc70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5d0e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5d0cc.md#insn-00b5d0e8) · [`00b5d0f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5d0cc.md#insn-00b5d0f4)
- 新版 [`00b5e0dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5e/00b5e0c0.md#insn-00b5e0dc) · [`00b5e0e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5e/00b5e0c0.md#insn-00b5e0e8)

~~~diff
- 00b5d0e8 ["INT_ADD", "register:40f0:8", ["const:b5d0e8:8", "const:4:8"]]
- 00b5d0e8 ["CALL", null, ["callee:00c5cc70:8"]]
+ 00b5e0dc ["INT_ADD", "register:40f0:8", ["const:b5e0dc:8", "const:4:8"]]
+ 00b5e0dc ["CALL", null, ["callee:00c5cc70:8"]]
- 00b5d0e8 bytes eefa0394
+ 00b5e0dc bytes e5fa0394
- 00b5d0f4 ["INT_ADD", "register:40f0:8", ["const:b5d0f4:8", "const:4:8"]]
- 00b5d0f4 ["CALL", null, ["callee:00c5cc70:8"]]
+ 00b5e0e8 ["INT_ADD", "register:40f0:8", ["const:b5e0e8:8", "const:4:8"]]
+ 00b5e0e8 ["CALL", null, ["callee:00c5cc70:8"]]
- 00b5d0f4 bytes ebfa0394
+ 00b5e0e8 bytes e2fa0394
~~~


<a id="compare-0d368d38586798321be532039fa06523"></a>

### [`00b5d144`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5d144.md) → [`00b5e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5e/00b5e138.md) _ZN8firebase4PathC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5bcc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bcc0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5cc90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cc90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5d154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5d144.md#insn-00b5d154)
- 新版 [`00b5e148`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5e/00b5e138.md#insn-00b5e148)

~~~diff
- 00b5d154 ["INT_ADD", "register:40f0:8", ["const:b5d154:8", "const:4:8"]]
- 00b5d154 ["CALL", null, ["callee:00c5cc90:8"]]
+ 00b5e148 ["INT_ADD", "register:40f0:8", ["const:b5e148:8", "const:4:8"]]
+ 00b5e148 ["CALL", null, ["callee:00c5cc90:8"]]
- 00b5d154 bytes dbfa0394
+ 00b5e148 bytes d2fa0394
~~~


<a id="compare-1e7fd0119294184acc2a82ca4add7639"></a>

### [`00b5d350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5d350.md) → [`00b5e344`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5e/00b5e344.md) _ZN8firebase4PathC2ERKNSt6__ndk16vectorINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS6_IS8_EEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 7件 [`00b5d4f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5d4f4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00b5e4e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5e/00b5e4e8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5d3ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5d350.md#insn-00b5d3ac) · [`00b5d3c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5d350.md#insn-00b5d3c8) · [`00b5d3f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5d350.md#insn-00b5d3f4)
- 新版 [`00b5e3a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5e/00b5e344.md#insn-00b5e3a0) · [`00b5e3bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5e/00b5e344.md#insn-00b5e3bc) · [`00b5e3e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5e/00b5e344.md#insn-00b5e3e8)

~~~diff
- 00b5d3ac ["INT_ADD", "register:40f0:8", ["const:b5d3ac:8", "const:4:8"]]
- 00b5d3ac ["CALL", null, ["callee:00c58f30:8"]]
+ 00b5e3a0 ["INT_ADD", "register:40f0:8", ["const:b5e3a0:8", "const:4:8"]]
+ 00b5e3a0 ["CALL", null, ["callee:00c58f30:8"]]
- 00b5d3ac bytes edea0394
+ 00b5e3a0 bytes e4ea0394
- 00b5d3c8 ["INT_ADD", "register:40f0:8", ["const:b5d3c8:8", "const:4:8"]]
- 00b5d3c8 ["CALL", null, ["callee:00c5c650:8"]]
+ 00b5e3bc ["INT_ADD", "register:40f0:8", ["const:b5e3bc:8", "const:4:8"]]
+ 00b5e3bc ["CALL", null, ["callee:00c5c650:8"]]
- 00b5d3c8 bytes aef80394
+ 00b5e3bc bytes a5f80394
- 00b5d3f4 ["INT_ADD", "register:40f0:8", ["const:b5d3f4:8", "const:4:8"]]
- 00b5d3f4 ["CALL", null, ["callee:00b5e4e8:8"]]
+ 00b5e3e8 ["INT_ADD", "register:40f0:8", ["const:b5e3e8:8", "const:4:8"]]
+ 00b5e3e8 ["CALL", null, ["callee:00b5e4e8:8"]]
- 00b5d3f4 bytes 40000094
+ 00b5e3e8 bytes 40000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2bc9e803b62d7ee65d4f21fd3d2e19d"></a>

### [`00b5d484`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5d484.md) → [`00b5e478`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5e/00b5e478.md) _ZN8firebase4PathC1ENSt6__ndk111__wrap_iterIPNS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEEESA_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00b5d4f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5d4f4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5bcc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bcc0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00b5e4e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5e/00b5e4e8.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5cc90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cc90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5d4b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5d484.md#insn-00b5d4b0) · [`00b5d4bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5d484.md#insn-00b5d4bc) · [`00b5d4cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5d484.md#insn-00b5d4cc)
- 新版 [`00b5e4a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5e/00b5e478.md#insn-00b5e4a4) · [`00b5e4b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5e/00b5e478.md#insn-00b5e4b0) · [`00b5e4c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5e/00b5e478.md#insn-00b5e4c0)

~~~diff
- 00b5d4b0 ["INT_ADD", "register:40f0:8", ["const:b5d4b0:8", "const:4:8"]]
- 00b5d4b0 ["CALL", null, ["callee:00b5e4e8:8"]]
+ 00b5e4a4 ["INT_ADD", "register:40f0:8", ["const:b5e4a4:8", "const:4:8"]]
+ 00b5e4a4 ["CALL", null, ["callee:00b5e4e8:8"]]
- 00b5d4b0 bytes 11000094
+ 00b5e4a4 bytes 11000094
- 00b5d4bc ["INT_ADD", "register:40f0:8", ["const:b5d4bc:8", "const:4:8"]]
- 00b5d4bc ["CALL", null, ["callee:00c5cc90:8"]]
+ 00b5e4b0 ["INT_ADD", "register:40f0:8", ["const:b5e4b0:8", "const:4:8"]]
+ 00b5e4b0 ["CALL", null, ["callee:00c5cc90:8"]]
- 00b5d4bc bytes 01fa0394
+ 00b5e4b0 bytes f8f90394
- 00b5d4cc ["INT_ADD", "register:40f0:8", ["const:b5d4cc:8", "const:4:8"]]
- 00b5d4cc ["CALL", null, ["callee:00c58f50:8"]]
+ 00b5e4c0 ["INT_ADD", "register:40f0:8", ["const:b5e4c0:8", "const:4:8"]]
+ 00b5e4c0 ["CALL", null, ["callee:00c58f50:8"]]
- 00b5d4cc bytes adea0394
+ 00b5e4c0 bytes a4ea0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91028fca2b25db82f7c7e1ef3fe65bfa"></a>

### [`00b5d85c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5d85c.md) → [`00b5e850`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5e/00b5e850.md) _ZNK8firebase4Path9GetParentEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5b180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b180.md) [`00c5b8c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b8c0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5c150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c150.md) [`00c5c890`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c890.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5d8d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5d85c.md#insn-00b5d8d0) · [`00b5d904`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5d85c.md#insn-00b5d904) · [`00b5d914`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5d85c.md#insn-00b5d914)
- 新版 [`00b5e8c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5e/00b5e850.md#insn-00b5e8c4) · [`00b5e8f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5e/00b5e850.md#insn-00b5e8f8) · [`00b5e908`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5e/00b5e850.md#insn-00b5e908)

~~~diff
- 00b5d8d0 ["INT_ADD", "register:40f0:8", ["const:b5d8d0:8", "const:4:8"]]
- 00b5d8d0 ["CALL", null, ["callee:00c5c890:8"]]
+ 00b5e8c4 ["INT_ADD", "register:40f0:8", ["const:b5e8c4:8", "const:4:8"]]
+ 00b5e8c4 ["CALL", null, ["callee:00c5c890:8"]]
- 00b5d8d0 bytes fcf70394
+ 00b5e8c4 bytes f3f70394
- 00b5d904 ["INT_ADD", "register:40f0:8", ["const:b5d904:8", "const:4:8"]]
- 00b5d904 ["CALL", null, ["callee:00c5c150:8"]]
+ 00b5e8f8 ["INT_ADD", "register:40f0:8", ["const:b5e8f8:8", "const:4:8"]]
+ 00b5e8f8 ["CALL", null, ["callee:00c5c150:8"]]
- 00b5d904 bytes 1ff60394
+ 00b5e8f8 bytes 16f60394
- 00b5d914 ["INT_ADD", "register:40f0:8", ["const:b5d914:8", "const:4:8"]]
- 00b5d914 ["CALL", null, ["callee:00c58f50:8"]]
+ 00b5e908 ["INT_ADD", "register:40f0:8", ["const:b5e908:8", "const:4:8"]]
+ 00b5e908 ["CALL", null, ["callee:00c58f50:8"]]
- 00b5d914 bytes 9be90394
+ 00b5e908 bytes 92e90394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c57836a60a32bcfed0cd20ad5a82336"></a>

### [`00b5d94c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5d94c.md) → [`00b5e940`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5e/00b5e940.md) _ZN8firebase4Path8MakePathERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c150.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5d980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5d94c.md#insn-00b5d980)
- 新版 [`00b5e974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5e/00b5e940.md#insn-00b5e974)

~~~diff
- 00b5d980 ["INT_ADD", "register:40f0:8", ["const:b5d980:8", "const:4:8"]]
- 00b5d980 ["CALL", null, ["callee:00c5c150:8"]]
+ 00b5e974 ["INT_ADD", "register:40f0:8", ["const:b5e974:8", "const:4:8"]]
+ 00b5e974 ["CALL", null, ["callee:00c5c150:8"]]
- 00b5d980 bytes 00f60394
+ 00b5e974 bytes f7f50394
~~~


<a id="compare-bf88db47a748492ae572ed00c0b18eba"></a>

### [`00b5ddb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5ddb8.md) → [`00b5edac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5e/00b5edac.md) _ZNK8firebase4Path14FrontDirectoryEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5bcc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bcc0.md) [`00c5bcd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bcd0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5cc90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cc90.md) [`00c5cca0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cca0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5ddf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5ddb8.md#insn-00b5ddf0) · [`00b5ddfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5ddb8.md#insn-00b5ddfc) · [`00b5de38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5ddb8.md#insn-00b5de38)
- 新版 [`00b5ede4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5e/00b5edac.md#insn-00b5ede4) · [`00b5edf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5e/00b5edac.md#insn-00b5edf0) · [`00b5ee2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5e/00b5edac.md#insn-00b5ee2c)

~~~diff
- 00b5ddf0 ["INT_ADD", "register:40f0:8", ["const:b5ddf0:8", "const:4:8"]]
- 00b5ddf0 ["CALL", null, ["callee:00c5cca0:8"]]
+ 00b5ede4 ["INT_ADD", "register:40f0:8", ["const:b5ede4:8", "const:4:8"]]
+ 00b5ede4 ["CALL", null, ["callee:00c5cca0:8"]]
- 00b5ddf0 bytes b8f70394
+ 00b5ede4 bytes aff70394
- 00b5ddfc ["INT_ADD", "register:40f0:8", ["const:b5ddfc:8", "const:4:8"]]
- 00b5ddfc ["CALL", null, ["callee:00c5cc90:8"]]
+ 00b5edf0 ["INT_ADD", "register:40f0:8", ["const:b5edf0:8", "const:4:8"]]
+ 00b5edf0 ["CALL", null, ["callee:00c5cc90:8"]]
- 00b5ddfc bytes b1f70394
+ 00b5edf0 bytes a8f70394
- 00b5de38 ["INT_ADD", "register:40f0:8", ["const:b5de38:8", "const:4:8"]]
- 00b5de38 ["CALL", null, ["callee:00c58f50:8"]]
+ 00b5ee2c ["INT_ADD", "register:40f0:8", ["const:b5ee2c:8", "const:4:8"]]
+ 00b5ee2c ["CALL", null, ["callee:00c58f50:8"]]
- 00b5de38 bytes 52e80394
+ 00b5ee2c bytes 49e80394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee274f41bc2e537f787256632a8cc633"></a>

### [`00b5de90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5de90.md) → [`00b5ee84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5e/00b5ee84.md) _ZNK8firebase4Path17PopFrontDirectoryEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00b5d4f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5d4f4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5bcc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bcc0.md) [`00c5bcd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bcd0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00b5e4e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5e/00b5e4e8.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5cc90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cc90.md) [`00c5cca0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cca0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5dec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5de90.md#insn-00b5dec8) · [`00b5ded8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5de90.md#insn-00b5ded8) · [`00b5dee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5de90.md#insn-00b5dee4)
- 新版 [`00b5eebc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5e/00b5ee84.md#insn-00b5eebc) · [`00b5eecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5e/00b5ee84.md#insn-00b5eecc) · [`00b5eed8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5e/00b5ee84.md#insn-00b5eed8)

~~~diff
- 00b5dec8 ["INT_ADD", "register:40f0:8", ["const:b5dec8:8", "const:4:8"]]
- 00b5dec8 ["CALL", null, ["callee:00c5cca0:8"]]
+ 00b5eebc ["INT_ADD", "register:40f0:8", ["const:b5eebc:8", "const:4:8"]]
+ 00b5eebc ["CALL", null, ["callee:00c5cca0:8"]]
- 00b5dec8 bytes 82f70394
+ 00b5eebc bytes 79f70394
- 00b5ded8 ["INT_ADD", "register:40f0:8", ["const:b5ded8:8", "const:4:8"]]
- 00b5ded8 ["CALL", null, ["callee:00b5e4e8:8"]]
+ 00b5eecc ["INT_ADD", "register:40f0:8", ["const:b5eecc:8", "const:4:8"]]
+ 00b5eecc ["CALL", null, ["callee:00b5e4e8:8"]]
- 00b5ded8 bytes 87fdff97
+ 00b5eecc bytes 87fdff97
- 00b5dee4 ["INT_ADD", "register:40f0:8", ["const:b5dee4:8", "const:4:8"]]
- 00b5dee4 ["CALL", null, ["callee:00c5cc90:8"]]
+ 00b5eed8 ["INT_ADD", "register:40f0:8", ["const:b5eed8:8", "const:4:8"]]
+ 00b5eed8 ["CALL", null, ["callee:00c5cc90:8"]]
- 00b5dee4 bytes 77f70394
+ 00b5eed8 bytes 6ef70394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92f2482c625d4158d1d1dd6b758be649"></a>

### [`00b5df88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5df88.md) → [`00b5ef7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5e/00b5ef7c.md) _ZN8firebase4Path11GetRelativeERKS0_S2_PS0_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5b180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b180.md) [`00c5bcb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bcb0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5c150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c150.md) [`00c5cc80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cc80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5dfb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5df88.md#insn-00b5dfb4) · [`00b5dfec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5df88.md#insn-00b5dfec) · [`00b5e004`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5df88.md#insn-00b5e004)
- 新版 [`00b5efa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5e/00b5ef7c.md#insn-00b5efa8) · [`00b5efe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5e/00b5ef7c.md#insn-00b5efe0) · [`00b5eff8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5e/00b5ef7c.md#insn-00b5eff8)

~~~diff
- 00b5dfb4 ["INT_ADD", "register:40f0:8", ["const:b5dfb4:8", "const:4:8"]]
- 00b5dfb4 ["CALL", null, ["callee:00c5cc80:8"]]
+ 00b5efa8 ["INT_ADD", "register:40f0:8", ["const:b5efa8:8", "const:4:8"]]
+ 00b5efa8 ["CALL", null, ["callee:00c5cc80:8"]]
- 00b5dfb4 bytes 3ff70394
+ 00b5efa8 bytes 36f70394
- 00b5dfec ["INT_ADD", "register:40f0:8", ["const:b5dfec:8", "const:4:8"]]
- 00b5dfec ["CALL", null, ["callee:00c5c150:8"]]
+ 00b5efe0 ["INT_ADD", "register:40f0:8", ["const:b5efe0:8", "const:4:8"]]
+ 00b5efe0 ["CALL", null, ["callee:00c5c150:8"]]
- 00b5dfec bytes 65f40394
+ 00b5efe0 bytes 5cf40394
- 00b5e004 ["INT_ADD", "register:40f0:8", ["const:b5e004:8", "const:4:8"]]
- 00b5e004 ["CALL", null, ["callee:00c58f50:8"]]
+ 00b5eff8 ["INT_ADD", "register:40f0:8", ["const:b5eff8:8", "const:4:8"]]
+ 00b5eff8 ["CALL", null, ["callee:00c58f50:8"]]
- 00b5e004 bytes dfe70394
+ 00b5eff8 bytes d6e70394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a5c341ac46c28420e826239b1daa44f"></a>

### [`00b5e040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5e040.md) → [`00b5f034`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5f/00b5f034.md) _ZN8firebase4Path11GetRelativeERKS0_S2_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5bcb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bcb0.md) · 呼出先 6件 [`00b5d4f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5d/00b5d4f4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c5b180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b180.md)
- 新版 呼出元 1件 [`00c5cc80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cc80.md) · 呼出先 6件 [`00b5e4e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5e/00b5e4e8.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md) [`00c5c150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c150.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5e074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5e040.md#insn-00b5e074) · [`00b5e080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5e040.md#insn-00b5e080) · [`00b5e13c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5e040.md#insn-00b5e13c)
- 新版 [`00b5f068`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5f/00b5f034.md#insn-00b5f068) · [`00b5f074`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5f/00b5f034.md#insn-00b5f074) · [`00b5f130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5f/00b5f034.md#insn-00b5f130)

~~~diff
- 00b5e074 ["INT_ADD", "register:40f0:8", ["const:b5e074:8", "const:4:8"]]
- 00b5e074 ["CALL", null, ["callee:00c5cca0:8"]]
+ 00b5f068 ["INT_ADD", "register:40f0:8", ["const:b5f068:8", "const:4:8"]]
+ 00b5f068 ["CALL", null, ["callee:00c5cca0:8"]]
- 00b5e074 bytes 17f70394
+ 00b5f068 bytes 0ef70394
- 00b5e080 ["INT_ADD", "register:40f0:8", ["const:b5e080:8", "const:4:8"]]
- 00b5e080 ["CALL", null, ["callee:00c5cca0:8"]]
+ 00b5f074 ["INT_ADD", "register:40f0:8", ["const:b5f074:8", "const:4:8"]]
+ 00b5f074 ["CALL", null, ["callee:00c5cca0:8"]]
- 00b5e080 bytes 14f70394
+ 00b5f074 bytes 0bf70394
- 00b5e13c ["INT_ADD", "register:40f0:8", ["const:b5e13c:8", "const:4:8"]]
- 00b5e13c ["CALL", null, ["callee:00c590f0:8"]]
+ 00b5f130 ["INT_ADD", "register:40f0:8", ["const:b5f130:8", "const:4:8"]]
+ 00b5f130 ["CALL", null, ["callee:00c590f0:8"]]
- 00b5e13c bytes f9e70394
+ 00b5f130 bytes f0e70394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef2a8b3f1ff7dece867bd63883b773ed"></a>

### [`00b5e2a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5e2a4.md) → [`00b5f298`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5f/00b5f298.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertINS_11__wrap_iterIPKcEEEENS_9enable_ifIXaasr21__is_forward_iterator

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5bce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bce0.md) · 呼出先 7件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c5a9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a9b0.md)
- 新版 呼出元 1件 [`00c5ccb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5ccb0.md) · 呼出先 7件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c5b980`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b980.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5e3b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5e2a4.md#insn-00b5e3b4) · [`00b5e3e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5e2a4.md#insn-00b5e3e0) · [`00b5e430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5e2a4.md#insn-00b5e430)
- 新版 [`00b5f3a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5f/00b5f298.md#insn-00b5f3a8) · [`00b5f3d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5f/00b5f298.md#insn-00b5f3d4) · [`00b5f424`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5f/00b5f298.md#insn-00b5f424)

~~~diff
- 00b5e3b4 ["INT_ADD", "register:40f0:8", ["const:b5e3b4:8", "const:4:8"]]
- 00b5e3b4 ["CALL", null, ["callee:00c5b980:8"]]
+ 00b5f3a8 ["INT_ADD", "register:40f0:8", ["const:b5f3a8:8", "const:4:8"]]
+ 00b5f3a8 ["CALL", null, ["callee:00c5b980:8"]]
- 00b5e3b4 bytes 7ff10394
+ 00b5f3a8 bytes 76f10394
- 00b5e3e0 ["INT_ADD", "register:40f0:8", ["const:b5e3e0:8", "const:4:8"]]
- 00b5e3e0 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b5f3d4 ["INT_ADD", "register:40f0:8", ["const:b5f3d4:8", "const:4:8"]]
+ 00b5f3d4 ["CALL", null, ["callee:00c58f30:8"]]
- 00b5e3e0 bytes e0e60394
+ 00b5f3d4 bytes d7e60394
- 00b5e430 ["INT_ADD", "register:40f0:8", ["const:b5e430:8", "const:4:8"]]
- 00b5e430 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00b5f424 ["INT_ADD", "register:40f0:8", ["const:b5f424:8", "const:4:8"]]
+ 00b5f424 ["CALL", null, ["callee:00c58fe0:8"]]
- 00b5e430 bytes f8e60394
+ 00b5f424 bytes efe60394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b8962c88caadf05566e3b14a59ab6bd"></a>

### [`00b5e5c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5e5c4.md) → [`00b5f5b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5f/00b5f5b8.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7reserveEm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c586c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586c0.md) · 呼出先 4件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c59690`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59690.md) · 呼出先 4件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5e660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5e5c4.md#insn-00b5e660) · [`00b5e6a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5e5c4.md#insn-00b5e6a8) · [`00b5e6cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5e5c4.md#insn-00b5e6cc)
- 新版 [`00b5f654`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5f/00b5f5b8.md#insn-00b5f654) · [`00b5f69c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5f/00b5f5b8.md#insn-00b5f69c) · [`00b5f6c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5f/00b5f5b8.md#insn-00b5f6c0)

~~~diff
- 00b5e660 ["INT_ADD", "register:40f0:8", ["const:b5e660:8", "const:4:8"]]
- 00b5e660 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b5f654 ["INT_ADD", "register:40f0:8", ["const:b5f654:8", "const:4:8"]]
+ 00b5f654 ["CALL", null, ["callee:00c58f30:8"]]
- 00b5e660 bytes 40e60394
+ 00b5f654 bytes 37e60394
- 00b5e6a8 ["INT_ADD", "register:40f0:8", ["const:b5e6a8:8", "const:4:8"]]
- 00b5e6a8 ["CALL", null, ["callee:00c590a0:8"]]
+ 00b5f69c ["INT_ADD", "register:40f0:8", ["const:b5f69c:8", "const:4:8"]]
+ 00b5f69c ["CALL", null, ["callee:00c590a0:8"]]
- 00b5e6a8 bytes 8ae60394
+ 00b5f69c bytes 81e60394
- 00b5e6cc ["INT_ADD", "register:40f0:8", ["const:b5e6cc:8", "const:4:8"]]
- 00b5e6cc ["CALL", null, ["callee:00c58f50:8"]]
+ 00b5f6c0 ["INT_ADD", "register:40f0:8", ["const:b5f6c0:8", "const:4:8"]]
+ 00b5f6c0 ["CALL", null, ["callee:00c58f50:8"]]
- 00b5e6cc bytes 2de60394
+ 00b5f6c0 bytes 24e60394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30ee1f13792871c3a04f5a3dde73bbe4"></a>

### [`00b5e6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5e6f8.md) → [`00b5f6ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5f/00b5f6ec.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertIPKcEENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr38__li

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5bcf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bcf0.md) · 呼出先 7件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c5a9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a9b0.md)
- 新版 呼出元 1件 [`00c5ccc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5ccc0.md) · 呼出先 7件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c5b980`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b980.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5e808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5e6f8.md#insn-00b5e808) · [`00b5e834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5e6f8.md#insn-00b5e834) · [`00b5e8c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5e6f8.md#insn-00b5e8c4)
- 新版 [`00b5f7fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5f/00b5f6ec.md#insn-00b5f7fc) · [`00b5f828`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5f/00b5f6ec.md#insn-00b5f828) · [`00b5f8b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5f/00b5f6ec.md#insn-00b5f8b8)

~~~diff
- 00b5e808 ["INT_ADD", "register:40f0:8", ["const:b5e808:8", "const:4:8"]]
- 00b5e808 ["CALL", null, ["callee:00c5b980:8"]]
+ 00b5f7fc ["INT_ADD", "register:40f0:8", ["const:b5f7fc:8", "const:4:8"]]
+ 00b5f7fc ["CALL", null, ["callee:00c5b980:8"]]
- 00b5e808 bytes 6af00394
+ 00b5f7fc bytes 61f00394
- 00b5e834 ["INT_ADD", "register:40f0:8", ["const:b5e834:8", "const:4:8"]]
- 00b5e834 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b5f828 ["INT_ADD", "register:40f0:8", ["const:b5f828:8", "const:4:8"]]
+ 00b5f828 ["CALL", null, ["callee:00c58f30:8"]]
- 00b5e834 bytes cbe50394
+ 00b5f828 bytes c2e50394
- 00b5e8c4 ["INT_ADD", "register:40f0:8", ["const:b5e8c4:8", "const:4:8"]]
- 00b5e8c4 ["CALL", null, ["callee:00c5ccc0:8"]]
+ 00b5f8b8 ["INT_ADD", "register:40f0:8", ["const:b5f8b8:8", "const:4:8"]]
+ 00b5f8b8 ["CALL", null, ["callee:00c5ccc0:8"]]
- 00b5e8c4 bytes 0bf50394
+ 00b5f8b8 bytes 02f50394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5f5080a263d30da182cc5f925d92743"></a>

### [`00b5ec70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5ec70.md) → [`00b5fc64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5f/00b5fc64.md) _ZN8firebase17FutureBackingData22ClearExistingCallbacksEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5bd50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bd50.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00c5cd20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cd20.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5ec9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5ec70.md#insn-00b5ec9c) · [`00b5ecb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5ec70.md#insn-00b5ecb8) · [`00b5ed14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5ec70.md#insn-00b5ed14)
- 新版 [`00b5fc90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5f/00b5fc64.md#insn-00b5fc90) · [`00b5fcac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5f/00b5fc64.md#insn-00b5fcac) · [`00b5fd08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5f/00b5fc64.md#insn-00b5fd08)

~~~diff
- 00b5ec9c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5ec9c ["INT_ADD", "register:40f0:8", ["const:b5ec9c:8", "const:4:8"]]
- 00b5ec9c ["CALLIND", null, ["register:0:8"]]
+ 00b5fc90 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5fc90 ["INT_ADD", "register:40f0:8", ["const:b5fc90:8", "const:4:8"]]
+ 00b5fc90 ["CALLIND", null, ["register:0:8"]]
- 00b5ec9c bytes 00013fd6
+ 00b5fc90 bytes 00013fd6
- 00b5ecb8 ["INT_ADD", "register:40f0:8", ["const:b5ecb8:8", "const:4:8"]]
- 00b5ecb8 ["CALL", null, ["callee:00c58f50:8"]]
+ 00b5fcac ["INT_ADD", "register:40f0:8", ["const:b5fcac:8", "const:4:8"]]
+ 00b5fcac ["CALL", null, ["callee:00c58f50:8"]]
- 00b5ecb8 bytes b2e40394
+ 00b5fcac bytes a9e40394
- 00b5ed14 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5ed14 ["INT_ADD", "register:40f0:8", ["const:b5ed14:8", "const:4:8"]]
- 00b5ed14 ["CALLIND", null, ["register:0:8"]]
+ 00b5fd08 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5fd08 ["INT_ADD", "register:40f0:8", ["const:b5fd08:8", "const:4:8"]]
+ 00b5fd08 ["CALLIND", null, ["register:0:8"]]
- 00b5ed14 bytes 00013fd6
+ 00b5fd08 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8026a0d164e3b1f756aa47e560daeac7"></a>

### [`00b5ef64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5ef64.md) → [`00b5ff58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5f/00b5ff58.md) _ZN8firebase26ReferenceCountedFutureImplD0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5bda0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bda0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5cd70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cd70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5ef74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5ef64.md#insn-00b5ef74)
- 新版 [`00b5ff68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5f/00b5ff58.md#insn-00b5ff68)

~~~diff
- 00b5ef74 ["INT_ADD", "register:40f0:8", ["const:b5ef74:8", "const:4:8"]]
- 00b5ef74 ["CALL", null, ["callee:00c5cd70:8"]]
+ 00b5ff68 ["INT_ADD", "register:40f0:8", ["const:b5ff68:8", "const:4:8"]]
+ 00b5ff68 ["CALL", null, ["callee:00c5cd70:8"]]
- 00b5ef74 bytes 8bf30394
+ 00b5ff68 bytes 82f30394
~~~


<a id="compare-717b2ae64d2c09d2ddcd989062897042"></a>

### [`00b5f638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5f638.md) → [`00b6062c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b60/00b6062c.md) _ZN8firebase26ReferenceCountedFutureImpl17BackingFromHandleEm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5af50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af50.md) · 呼出先 2件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)
- 新版 呼出元 1件 [`00c5bf20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf20.md) · 呼出先 2件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5f658`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5f638.md#insn-00b5f658) · [`00b5f6a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5f638.md#insn-00b5f6a4)
- 新版 [`00b6064c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b60/00b6062c.md#insn-00b6064c) · [`00b60698`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b60/00b6062c.md#insn-00b60698)

~~~diff
- 00b5f658 ["INT_ADD", "register:40f0:8", ["const:b5f658:8", "const:4:8"]]
- 00b5f658 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b6064c ["INT_ADD", "register:40f0:8", ["const:b6064c:8", "const:4:8"]]
+ 00b6064c ["CALL", null, ["callee:00c5baa0:8"]]
- 00b5f658 bytes 1eed0394
+ 00b6064c bytes 15ed0394
- 00b5f6a4 ["INT_ADD", "register:40f0:8", ["const:b5f6a4:8", "const:4:8"]]
- 00b5f6a4 ["CALL", null, ["callee:00c5bab0:8"]]
+ 00b60698 ["INT_ADD", "register:40f0:8", ["const:b60698:8", "const:4:8"]]
+ 00b60698 ["CALL", null, ["callee:00c5bab0:8"]]
- 00b5f6a4 bytes 0fed0394
+ 00b60698 bytes 06ed0394
~~~


<a id="compare-6e8fe317c56650a22faf1153ce9437dc"></a>

### [`00b5f9f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5f9f0.md) → [`00b609e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b60/00b609e4.md) _ZN8firebase26ReferenceCountedFutureImpl11RunCallbackEPNS_10FutureBaseEPFvRKS1_PvES5_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5fa24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5f9f0.md#insn-00b5fa24) · [`00b5fa30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5f9f0.md#insn-00b5fa30) · [`00b5fa38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5f9f0.md#insn-00b5fa38)
- 新版 [`00b60a18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b60/00b609e4.md#insn-00b60a18) · [`00b60a24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b60/00b609e4.md#insn-00b60a24) · [`00b60a2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b60/00b609e4.md#insn-00b60a2c)

~~~diff
- 00b5fa24 ["INT_ADD", "register:40f0:8", ["const:b5fa24:8", "const:4:8"]]
- 00b5fa24 ["CALL", null, ["callee:00c5bab0:8"]]
+ 00b60a18 ["INT_ADD", "register:40f0:8", ["const:b60a18:8", "const:4:8"]]
+ 00b60a18 ["CALL", null, ["callee:00c5bab0:8"]]
- 00b5fa24 bytes 2fec0394
+ 00b60a18 bytes 26ec0394
- 00b5fa30 ["COPY", "register:0:8", ["register:40a0:8"]]
- 00b5fa30 ["INT_ADD", "register:40f0:8", ["const:b5fa30:8", "const:4:8"]]
- 00b5fa30 ["CALLIND", null, ["register:0:8"]]
+ 00b60a24 ["COPY", "register:0:8", ["register:40a0:8"]]
+ 00b60a24 ["INT_ADD", "register:40f0:8", ["const:b60a24:8", "const:4:8"]]
+ 00b60a24 ["CALLIND", null, ["register:0:8"]]
- 00b5fa30 bytes 80023fd6
+ 00b60a24 bytes 80023fd6
- 00b5fa38 ["INT_ADD", "register:40f0:8", ["const:b5fa38:8", "const:4:8"]]
- 00b5fa38 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b60a2c ["INT_ADD", "register:40f0:8", ["const:b60a2c:8", "const:4:8"]]
+ 00b60a2c ["CALL", null, ["callee:00c5baa0:8"]]
- 00b5fa38 bytes 26ec0394
+ 00b60a2c bytes 1dec0394
~~~


<a id="compare-892e73ecf21f5f329159fa6d2089a00b"></a>

### [`00b5fa54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5fa54.md) → [`00b60a48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b60/00b60a48.md) _ZNK8firebase26ReferenceCountedFutureImpl11is_orphanedEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b140.md) · 呼出先 2件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)
- 新版 呼出元 1件 [`00c5c110`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c110.md) · 呼出先 2件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5fa6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5fa54.md#insn-00b5fa6c) · [`00b5fa78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5fa54.md#insn-00b5fa78)
- 新版 [`00b60a60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b60/00b60a48.md#insn-00b60a60) · [`00b60a6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b60/00b60a48.md#insn-00b60a6c)

~~~diff
- 00b5fa6c ["INT_ADD", "register:40f0:8", ["const:b5fa6c:8", "const:4:8"]]
- 00b5fa6c ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b60a60 ["INT_ADD", "register:40f0:8", ["const:b60a60:8", "const:4:8"]]
+ 00b60a60 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b5fa6c bytes 19ec0394
+ 00b60a60 bytes 10ec0394
- 00b5fa78 ["INT_ADD", "register:40f0:8", ["const:b5fa78:8", "const:4:8"]]
- 00b5fa78 ["CALL", null, ["callee:00c5bab0:8"]]
+ 00b60a6c ["INT_ADD", "register:40f0:8", ["const:b60a6c:8", "const:4:8"]]
+ 00b60a6c ["CALL", null, ["callee:00c5bab0:8"]]
- 00b5fa78 bytes 1aec0394
+ 00b60a6c bytes 11ec0394
~~~


<a id="compare-fc2915d200d0655b581afea41b8bac6c"></a>

### [`00b5fa9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5fa9c.md) → [`00b60a90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b60/00b60a90.md) FUN_00b60a90

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b5fa8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5fa8c.md) · 呼出先 2件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)
- 新版 呼出元 1件 [`00b60a80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b60/00b60a80.md) · 呼出先 2件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5faac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5fa9c.md#insn-00b5faac) · [`00b5fac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5fa9c.md#insn-00b5fac4) · [`00b5fad8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5fa9c.md#insn-00b5fad8)
- 新版 [`00b60aa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b60/00b60a90.md#insn-00b60aa0) · [`00b60ab8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b60/00b60a90.md#insn-00b60ab8) · [`00b60acc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b60/00b60a90.md#insn-00b60acc)

~~~diff
- 00b5faac ["INT_ADD", "register:40f0:8", ["const:b5faac:8", "const:4:8"]]
- 00b5faac ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b60aa0 ["INT_ADD", "register:40f0:8", ["const:b60aa0:8", "const:4:8"]]
+ 00b60aa0 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b5faac bytes 09ec0394
+ 00b60aa0 bytes 00ec0394
- 00b5fac4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5fac4 ["INT_ADD", "register:40f0:8", ["const:b5fac4:8", "const:4:8"]]
- 00b5fac4 ["CALLIND", null, ["register:0:8"]]
+ 00b60ab8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b60ab8 ["INT_ADD", "register:40f0:8", ["const:b60ab8:8", "const:4:8"]]
+ 00b60ab8 ["CALLIND", null, ["register:0:8"]]
- 00b5fac4 bytes 00013fd6
+ 00b60ab8 bytes 00013fd6
- 00b5fad8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5fad8 ["INT_ADD", "register:40f0:8", ["const:b5fad8:8", "const:4:8"]]
- 00b5fad8 ["CALLIND", null, ["register:0:8"]]
+ 00b60acc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b60acc ["INT_ADD", "register:40f0:8", ["const:b60acc:8", "const:4:8"]]
+ 00b60acc ["CALLIND", null, ["register:0:8"]]
- 00b5fad8 bytes 00013fd6
+ 00b60acc bytes 00013fd6
~~~


<a id="compare-0b449ee273a51b4a505603e5003fa61c"></a>

### [`00b5faf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5faf8.md) → [`00b60aec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b60/00b60aec.md) _ZN8firebase26ReferenceCountedFutureImpl15ReferenceFutureERKNS_12FutureHandleE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5fb18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5faf8.md#insn-00b5fb18) · [`00b5fb24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5faf8.md#insn-00b5fb24) · [`00b5fb70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5faf8.md#insn-00b5fb70)
- 新版 [`00b60b0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b60/00b60aec.md#insn-00b60b0c) · [`00b60b18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b60/00b60aec.md#insn-00b60b18) · [`00b60b64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b60/00b60aec.md#insn-00b60b64)

~~~diff
- 00b5fb18 ["INT_ADD", "register:40f0:8", ["const:b5fb18:8", "const:4:8"]]
- 00b5fb18 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b60b0c ["INT_ADD", "register:40f0:8", ["const:b60b0c:8", "const:4:8"]]
+ 00b60b0c ["CALL", null, ["callee:00c5baa0:8"]]
- 00b5fb18 bytes eeeb0394
+ 00b60b0c bytes e5eb0394
- 00b5fb24 ["INT_ADD", "register:40f0:8", ["const:b5fb24:8", "const:4:8"]]
- 00b5fb24 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b60b18 ["INT_ADD", "register:40f0:8", ["const:b60b18:8", "const:4:8"]]
+ 00b60b18 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b5fb24 bytes ebeb0394
+ 00b60b18 bytes e2eb0394
- 00b5fb70 ["INT_ADD", "register:40f0:8", ["const:b5fb70:8", "const:4:8"]]
- 00b5fb70 ["CALL", null, ["callee:00c5bab0:8"]]
+ 00b60b64 ["INT_ADD", "register:40f0:8", ["const:b60b64:8", "const:4:8"]]
+ 00b60b64 ["CALL", null, ["callee:00c5bab0:8"]]
- 00b5fb70 bytes dceb0394
+ 00b60b64 bytes d3eb0394
~~~


<a id="compare-96bb1e06cfc4a87f4070ddc1767bd705"></a>

### [`00b5fcb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5fcb8.md) → [`00b60cac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b60/00b60cac.md) _ZNK8firebase26ReferenceCountedFutureImpl15GetFutureStatusERKNS_12FutureHandleE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5fcd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5fcb8.md#insn-00b5fcd8) · [`00b5fce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5fcb8.md#insn-00b5fce4) · [`00b5fd24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5fcb8.md#insn-00b5fd24)
- 新版 [`00b60ccc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b60/00b60cac.md#insn-00b60ccc) · [`00b60cd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b60/00b60cac.md#insn-00b60cd8) · [`00b60d18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b60/00b60cac.md#insn-00b60d18)

~~~diff
- 00b5fcd8 ["INT_ADD", "register:40f0:8", ["const:b5fcd8:8", "const:4:8"]]
- 00b5fcd8 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b60ccc ["INT_ADD", "register:40f0:8", ["const:b60ccc:8", "const:4:8"]]
+ 00b60ccc ["CALL", null, ["callee:00c5baa0:8"]]
- 00b5fcd8 bytes 7eeb0394
+ 00b60ccc bytes 75eb0394
- 00b5fce4 ["INT_ADD", "register:40f0:8", ["const:b5fce4:8", "const:4:8"]]
- 00b5fce4 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b60cd8 ["INT_ADD", "register:40f0:8", ["const:b60cd8:8", "const:4:8"]]
+ 00b60cd8 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b5fce4 bytes 7beb0394
+ 00b60cd8 bytes 72eb0394
- 00b5fd24 ["INT_ADD", "register:40f0:8", ["const:b5fd24:8", "const:4:8"]]
- 00b5fd24 ["CALL", null, ["callee:00c5bab0:8"]]
+ 00b60d18 ["INT_ADD", "register:40f0:8", ["const:b60d18:8", "const:4:8"]]
+ 00b60d18 ["CALL", null, ["callee:00c5bab0:8"]]
- 00b5fd24 bytes 6feb0394
+ 00b60d18 bytes 66eb0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e471cfe9877b4f18c10f0a3fe35ccaa"></a>

### [`00b5fd60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5fd60.md) → [`00b60d54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b60/00b60d54.md) _ZNK8firebase26ReferenceCountedFutureImpl14GetFutureErrorERKNS_12FutureHandleE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5fd80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5fd60.md#insn-00b5fd80) · [`00b5fd8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5fd60.md#insn-00b5fd8c) · [`00b5fdcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5fd60.md#insn-00b5fdcc)
- 新版 [`00b60d74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b60/00b60d54.md#insn-00b60d74) · [`00b60d80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b60/00b60d54.md#insn-00b60d80) · [`00b60dc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b60/00b60d54.md#insn-00b60dc0)

~~~diff
- 00b5fd80 ["INT_ADD", "register:40f0:8", ["const:b5fd80:8", "const:4:8"]]
- 00b5fd80 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b60d74 ["INT_ADD", "register:40f0:8", ["const:b60d74:8", "const:4:8"]]
+ 00b60d74 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b5fd80 bytes 54eb0394
+ 00b60d74 bytes 4beb0394
- 00b5fd8c ["INT_ADD", "register:40f0:8", ["const:b5fd8c:8", "const:4:8"]]
- 00b5fd8c ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b60d80 ["INT_ADD", "register:40f0:8", ["const:b60d80:8", "const:4:8"]]
+ 00b60d80 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b5fd8c bytes 51eb0394
+ 00b60d80 bytes 48eb0394
- 00b5fdcc ["INT_ADD", "register:40f0:8", ["const:b5fdcc:8", "const:4:8"]]
- 00b5fdcc ["CALL", null, ["callee:00c5bab0:8"]]
+ 00b60dc0 ["INT_ADD", "register:40f0:8", ["const:b60dc0:8", "const:4:8"]]
+ 00b60dc0 ["CALL", null, ["callee:00c5bab0:8"]]
- 00b5fdcc bytes 45eb0394
+ 00b60dc0 bytes 3ceb0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2632025366422bd6923875d361d36c5"></a>

### [`00b5fec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5fec8.md) → [`00b60ebc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b60/00b60ebc.md) _ZNK8firebase26ReferenceCountedFutureImpl15GetFutureResultERKNS_12FutureHandleE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5fee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5fec8.md#insn-00b5fee8) · [`00b5fef4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5fec8.md#insn-00b5fef4) · [`00b5ff34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5fec8.md#insn-00b5ff34)
- 新版 [`00b60edc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b60/00b60ebc.md#insn-00b60edc) · [`00b60ee8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b60/00b60ebc.md#insn-00b60ee8) · [`00b60f28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b60/00b60ebc.md#insn-00b60f28)

~~~diff
- 00b5fee8 ["INT_ADD", "register:40f0:8", ["const:b5fee8:8", "const:4:8"]]
- 00b5fee8 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b60edc ["INT_ADD", "register:40f0:8", ["const:b60edc:8", "const:4:8"]]
+ 00b60edc ["CALL", null, ["callee:00c5baa0:8"]]
- 00b5fee8 bytes faea0394
+ 00b60edc bytes f1ea0394
- 00b5fef4 ["INT_ADD", "register:40f0:8", ["const:b5fef4:8", "const:4:8"]]
- 00b5fef4 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b60ee8 ["INT_ADD", "register:40f0:8", ["const:b60ee8:8", "const:4:8"]]
+ 00b60ee8 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b5fef4 bytes f7ea0394
+ 00b60ee8 bytes eeea0394
- 00b5ff34 ["INT_ADD", "register:40f0:8", ["const:b5ff34:8", "const:4:8"]]
- 00b5ff34 ["CALL", null, ["callee:00c5bab0:8"]]
+ 00b60f28 ["INT_ADD", "register:40f0:8", ["const:b60f28:8", "const:4:8"]]
+ 00b60f28 ["CALL", null, ["callee:00c5bab0:8"]]
- 00b5ff34 bytes ebea0394
+ 00b60f28 bytes e2ea0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb7897c70ab5041747a6569e925f5345"></a>

### [`00b5ff78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5ff78.md) → [`00b60f6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b60/00b60f6c.md) _ZN8firebase26ReferenceCountedFutureImpl21AddCompletionCallbackERKNS_12FutureHandleEPFvRKNS_10FutureBaseEPvES7_PFvS7_Eb

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5af60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af60.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bf30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b5ffb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5ff78.md#insn-00b5ffb4) · [`00b5ffd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5ff78.md#insn-00b5ffd0) · [`00b5ffdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5f/00b5ff78.md#insn-00b5ffdc)
- 新版 [`00b60fa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b60/00b60f6c.md#insn-00b60fa8) · [`00b60fc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b60/00b60f6c.md#insn-00b60fc4) · [`00b60fd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b60/00b60f6c.md#insn-00b60fd0)

~~~diff
- 00b5ffb4 ["INT_ADD", "register:40f0:8", ["const:b5ffb4:8", "const:4:8"]]
- 00b5ffb4 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b60fa8 ["INT_ADD", "register:40f0:8", ["const:b60fa8:8", "const:4:8"]]
+ 00b60fa8 ["CALL", null, ["callee:00c58f30:8"]]
- 00b5ffb4 bytes ebdf0394
+ 00b60fa8 bytes e2df0394
- 00b5ffd0 ["INT_ADD", "register:40f0:8", ["const:b5ffd0:8", "const:4:8"]]
- 00b5ffd0 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b60fc4 ["INT_ADD", "register:40f0:8", ["const:b60fc4:8", "const:4:8"]]
+ 00b60fc4 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b5ffd0 bytes c0ea0394
+ 00b60fc4 bytes b7ea0394
- 00b5ffdc ["INT_ADD", "register:40f0:8", ["const:b5ffdc:8", "const:4:8"]]
- 00b5ffdc ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b60fd0 ["INT_ADD", "register:40f0:8", ["const:b60fd0:8", "const:4:8"]]
+ 00b60fd0 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b5ffdc bytes bdea0394
+ 00b60fd0 bytes b4ea0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bff99b6482a975c882a2f5632273387d"></a>

### [`00b6012c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b6012c.md) → [`00b61120`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b61/00b61120.md) _ZN8firebase26ReferenceCountedFutureImpl24RemoveCompletionCallbackERKNS_12FutureHandleENS_6detail24CompletionCallbackHandleE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b60164`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b6012c.md#insn-00b60164) · [`00b60170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b6012c.md#insn-00b60170) · [`00b601b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b6012c.md#insn-00b601b0)
- 新版 [`00b61158`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b61/00b61120.md#insn-00b61158) · [`00b61164`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b61/00b61120.md#insn-00b61164) · [`00b611a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b61/00b61120.md#insn-00b611a4)

~~~diff
- 00b60164 ["INT_ADD", "register:40f0:8", ["const:b60164:8", "const:4:8"]]
- 00b60164 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b61158 ["INT_ADD", "register:40f0:8", ["const:b61158:8", "const:4:8"]]
+ 00b61158 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b60164 bytes 5bea0394
+ 00b61158 bytes 52ea0394
- 00b60170 ["INT_ADD", "register:40f0:8", ["const:b60170:8", "const:4:8"]]
- 00b60170 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b61164 ["INT_ADD", "register:40f0:8", ["const:b61164:8", "const:4:8"]]
+ 00b61164 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b60170 bytes 58ea0394
+ 00b61164 bytes 4fea0394
- 00b601b0 ["INT_ADD", "register:40f0:8", ["const:b601b0:8", "const:4:8"]]
- 00b601b0 ["CALL", null, ["callee:00c5bab0:8"]]
+ 00b611a4 ["INT_ADD", "register:40f0:8", ["const:b611a4:8", "const:4:8"]]
+ 00b611a4 ["CALL", null, ["callee:00c5bab0:8"]]
- 00b601b0 bytes 4cea0394
+ 00b611a4 bytes 43ea0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ef0ec1b7106304c3ab56b86a3aa3de9"></a>

### [`00b60530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60530.md) → [`00b61524`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b61/00b61524.md) FUN_00b61524

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b60320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60320.md) · 呼出先 1件 [`00b611c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b611c8.md)
- 新版 呼出元 1件 [`00b61314`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b61/00b61314.md) · 呼出先 1件 [`00b621bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b621bc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b60564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60530.md#insn-00b60564)
- 新版 [`00b61558`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b61/00b61524.md#insn-00b61558)

~~~diff
- 00b60564 ["INT_ADD", "register:40f0:8", ["const:b60564:8", "const:4:8"]]
- 00b60564 ["CALL", null, ["callee:00b621bc:8"]]
+ 00b61558 ["INT_ADD", "register:40f0:8", ["const:b61558:8", "const:4:8"]]
+ 00b61558 ["CALL", null, ["callee:00b621bc:8"]]
- 00b60564 bytes 19030094
+ 00b61558 bytes 19030094
~~~


<a id="compare-a50686693badef894d583b8c12e686c9"></a>

### [`00b60568`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60568.md) → [`00b6155c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b61/00b6155c.md) FUN_00b6155c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b60320`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60320.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00b61314`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b61/00b61314.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b605a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60568.md#insn-00b605a4)
- 新版 [`00b61598`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b61/00b6155c.md#insn-00b61598)

~~~diff
- 00b605a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b605a4 ["INT_ADD", "register:40f0:8", ["const:b605a4:8", "const:4:8"]]
- 00b605a4 ["CALLIND", null, ["register:0:8"]]
+ 00b61598 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b61598 ["INT_ADD", "register:40f0:8", ["const:b61598:8", "const:4:8"]]
+ 00b61598 ["CALLIND", null, ["register:0:8"]]
- 00b605a4 bytes 00013fd6
+ 00b61598 bytes 00013fd6
~~~


<a id="compare-bb856b916c3078a52bf70c2e7fd0caaf"></a>

### [`00b605b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b605b8.md) → [`00b615ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b61/00b615ac.md) _ZNK8firebase26ReferenceCountedFutureImpl14IsSafeToDeleteEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5bdb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bdb0.md) · 呼出先 2件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)
- 新版 呼出元 1件 [`00c5cd80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cd80.md) · 呼出先 2件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b605d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b605b8.md#insn-00b605d0) · [`00b60664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b605b8.md#insn-00b60664)
- 新版 [`00b615c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b61/00b615ac.md#insn-00b615c4) · [`00b61658`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b61/00b615ac.md#insn-00b61658)

~~~diff
- 00b605d0 ["INT_ADD", "register:40f0:8", ["const:b605d0:8", "const:4:8"]]
- 00b605d0 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b615c4 ["INT_ADD", "register:40f0:8", ["const:b615c4:8", "const:4:8"]]
+ 00b615c4 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b605d0 bytes 40e90394
+ 00b615c4 bytes 37e90394
- 00b60664 ["INT_ADD", "register:40f0:8", ["const:b60664:8", "const:4:8"]]
- 00b60664 ["CALL", null, ["callee:00c5bab0:8"]]
+ 00b61658 ["INT_ADD", "register:40f0:8", ["const:b61658:8", "const:4:8"]]
+ 00b61658 ["CALL", null, ["callee:00c5bab0:8"]]
- 00b60664 bytes 1fe90394
+ 00b61658 bytes 16e90394
~~~


<a id="compare-dc67b079e326b3aa5f6ee7e8ce4ed482"></a>

### [`00b60678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60678.md) → [`00b6166c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b61/00b6166c.md) _ZNK8firebase26ReferenceCountedFutureImpl17IsRunningCallbackEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b60690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60678.md#insn-00b60690) · [`00b6069c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60678.md#insn-00b6069c)
- 新版 [`00b61684`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b61/00b6166c.md#insn-00b61684) · [`00b61690`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b61/00b6166c.md#insn-00b61690)

~~~diff
- 00b60690 ["INT_ADD", "register:40f0:8", ["const:b60690:8", "const:4:8"]]
- 00b60690 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b61684 ["INT_ADD", "register:40f0:8", ["const:b61684:8", "const:4:8"]]
+ 00b61684 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b60690 bytes 10e90394
+ 00b61684 bytes 07e90394
- 00b6069c ["INT_ADD", "register:40f0:8", ["const:b6069c:8", "const:4:8"]]
- 00b6069c ["CALL", null, ["callee:00c5bab0:8"]]
+ 00b61690 ["INT_ADD", "register:40f0:8", ["const:b61690:8", "const:4:8"]]
+ 00b61690 ["CALL", null, ["callee:00c5bab0:8"]]
- 00b6069c bytes 11e90394
+ 00b61690 bytes 08e90394
~~~


<a id="compare-c519b5310ad2b83b354cf41e702ad8ad"></a>

### [`00b606b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b606b0.md) → [`00b616a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b61/00b616a4.md) _ZNK8firebase26ReferenceCountedFutureImpl22IsReferencedExternallyEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b606d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b606b0.md#insn-00b606d4) · [`00b6077c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b606b0.md#insn-00b6077c) · [`00b607a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b606b0.md#insn-00b607a0)
- 新版 [`00b616c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b61/00b616a4.md#insn-00b616c8) · [`00b61770`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b61/00b616a4.md#insn-00b61770) · [`00b61794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b61/00b616a4.md#insn-00b61794)

~~~diff
- 00b606d4 ["INT_ADD", "register:40f0:8", ["const:b606d4:8", "const:4:8"]]
- 00b606d4 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b616c8 ["INT_ADD", "register:40f0:8", ["const:b616c8:8", "const:4:8"]]
+ 00b616c8 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b606d4 bytes ffe80394
+ 00b616c8 bytes f6e80394
- 00b6077c ["INT_ADD", "register:40f0:8", ["const:b6077c:8", "const:4:8"]]
- 00b6077c ["CALL", null, ["callee:00c5bab0:8"]]
+ 00b61770 ["INT_ADD", "register:40f0:8", ["const:b61770:8", "const:4:8"]]
+ 00b61770 ["CALL", null, ["callee:00c5bab0:8"]]
- 00b6077c bytes d9e80394
+ 00b61770 bytes d0e80394
- 00b607a0 ["INT_ADD", "register:40f0:8", ["const:b607a0:8", "const:4:8"]]
- 00b607a0 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b61794 ["INT_ADD", "register:40f0:8", ["const:b61794:8", "const:4:8"]]
+ 00b61794 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b607a0 bytes cce80394
+ 00b61794 bytes c3e80394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef45d87ec3cecf2478e8900f268ceaf0"></a>

### [`00b60dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60dfc.md) → [`00b61df0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b61/00b61df0.md) _ZN8firebase26ReferenceCountedFutureImpl18ForceReleaseFutureERKNS_12FutureHandleE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5bd90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bd90.md) · 呼出先 2件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)
- 新版 呼出元 1件 [`00c5cd60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cd60.md) · 呼出先 2件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b60e1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60dfc.md#insn-00b60e1c) · [`00b60e28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60dfc.md#insn-00b60e28) · [`00b60e6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60dfc.md#insn-00b60e6c)
- 新版 [`00b61e10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b61/00b61df0.md#insn-00b61e10) · [`00b61e1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b61/00b61df0.md#insn-00b61e1c) · [`00b61e60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b61/00b61df0.md#insn-00b61e60)

~~~diff
- 00b60e1c ["INT_ADD", "register:40f0:8", ["const:b60e1c:8", "const:4:8"]]
- 00b60e1c ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b61e10 ["INT_ADD", "register:40f0:8", ["const:b61e10:8", "const:4:8"]]
+ 00b61e10 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b60e1c bytes 2de70394
+ 00b61e10 bytes 24e70394
- 00b60e28 ["INT_ADD", "register:40f0:8", ["const:b60e28:8", "const:4:8"]]
- 00b60e28 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b61e1c ["INT_ADD", "register:40f0:8", ["const:b61e1c:8", "const:4:8"]]
+ 00b61e1c ["CALL", null, ["callee:00c5baa0:8"]]
- 00b60e28 bytes 2ae70394
+ 00b61e1c bytes 21e70394
- 00b60e6c ["INT_ADD", "register:40f0:8", ["const:b60e6c:8", "const:4:8"]]
- 00b60e6c ["CALL", null, ["callee:00c5bab0:8"]]
+ 00b61e60 ["INT_ADD", "register:40f0:8", ["const:b61e60:8", "const:4:8"]]
+ 00b61e60 ["CALL", null, ["callee:00c5bab0:8"]]
- 00b60e6c bytes 1de70394
+ 00b61e60 bytes 14e70394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8727d00f12193e7eb663243bff4bf77a"></a>

### [`00b60eb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60eb4.md) → [`00b61ea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b61/00b61ea8.md) _ZN8firebase26ReferenceCountedFutureImpl12MarkOrphanedEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b60ecc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60eb4.md#insn-00b60ecc)
- 新版 [`00b61ec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b61/00b61ea8.md#insn-00b61ec0)

~~~diff
- 00b60ecc ["INT_ADD", "register:40f0:8", ["const:b60ecc:8", "const:4:8"]]
- 00b60ecc ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b61ec0 ["INT_ADD", "register:40f0:8", ["const:b61ec0:8", "const:4:8"]]
+ 00b61ec0 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b60ecc bytes 01e70394
+ 00b61ec0 bytes f8e60394
~~~


<a id="compare-042af50e66748d5176bd09443f79e000"></a>

### [`00b60f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60f50.md) → [`00b61f44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b61/00b61f44.md) _ZN8firebase12FutureHandleD2Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00b6144c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b6144c.md) [`00c5ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab60.md) · 呼出先 1件 [`00c5ace0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ace0.md)
- 新版 呼出元 2件 [`00b62440`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b62440.md) [`00c5bb30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb30.md) · 呼出先 1件 [`00c5bcb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bcb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b60f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60f50.md#insn-00b60f70)
- 新版 [`00b61f64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b61/00b61f44.md#insn-00b61f64)

~~~diff
- 00b60f70 ["INT_ADD", "register:40f0:8", ["const:b60f70:8", "const:4:8"]]
- 00b60f70 ["CALL", null, ["callee:00c5bcb0:8"]]
+ 00b61f64 ["INT_ADD", "register:40f0:8", ["const:b61f64:8", "const:4:8"]]
+ 00b61f64 ["CALL", null, ["callee:00c5bcb0:8"]]
- 00b60f70 bytes 5ce70394
+ 00b61f64 bytes 53e70394
~~~


<a id="compare-825a46b724a74a460d0c27858df81081"></a>

### [`00b61180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b61180.md) → [`00b62174`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b62174.md) _ZN8firebase12FutureHandle6DetachEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5aec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aec0.md) · 呼出先 1件 [`00c5ace0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ace0.md)
- 新版 呼出元 1件 [`00c5be90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5be90.md) · 呼出先 1件 [`00c5bcb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bcb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b611a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b61180.md#insn-00b611a0) · [`00b611b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b61180.md#insn-00b611b4)
- 新版 [`00b62194`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b62174.md#insn-00b62194) · [`00b621a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b62174.md#insn-00b621a8)

~~~diff
- 00b611a0 ["INT_ADD", "register:40f0:8", ["const:b611a0:8", "const:4:8"]]
- 00b611a0 ["CALL", null, ["callee:00c5bcb0:8"]]
+ 00b62194 ["INT_ADD", "register:40f0:8", ["const:b62194:8", "const:4:8"]]
+ 00b62194 ["CALL", null, ["callee:00c5bcb0:8"]]
- 00b611a0 bytes d0e60394
+ 00b62194 bytes c7e60394
- 00b611b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b611b4 ["INT_ADD", "register:40f0:8", ["const:b611b4:8", "const:4:8"]]
- 00b611b4 ["CALLIND", null, ["register:0:8"]]
+ 00b621a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b621a8 ["INT_ADD", "register:40f0:8", ["const:b621a8:8", "const:4:8"]]
+ 00b621a8 ["CALLIND", null, ["register:0:8"]]
- 00b611b4 bytes 00013fd6
+ 00b621a8 bytes 00013fd6
~~~


<a id="compare-f021adc2d7836be1834c4fff5c56e697"></a>

### [`00b611c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b611c8.md) → [`00b621bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b621bc.md) FUN_00b621bc

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 7件 [`00b60530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b60/00b60530.md) [`00b682dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b68/00b682dc.md) [`00bb40ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb4/00bb40ac.md) [`00bc952c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc952c.md) [`00bc96f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc9/00bc96f0.md) · 呼出先 1件 [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 7件 [`00b61524`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b61/00b61524.md) [`00b692d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b69/00b692d0.md) [`00bb50a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb5/00bb50a0.md) [`00bca520`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bca/00bca520.md) [`00bca6e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bca/00bca6e4.md) · 呼出先 1件 [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b611d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b611c8.md#insn-00b611d0)
- 新版 [`00b621c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b621bc.md#insn-00b621c4)

~~~diff
- 00b611d0 ["INT_ADD", "register:40f0:8", ["const:b611d0:8", "const:4:8"]]
- 00b611d0 ["CALL", null, ["callee:00c5c1e0:8"]]
+ 00b621c4 ["INT_ADD", "register:40f0:8", ["const:b621c4:8", "const:4:8"]]
+ 00b621c4 ["CALL", null, ["callee:00c5c1e0:8"]]
- 00b611d0 bytes 10e80394
+ 00b621c4 bytes 07e80394
~~~


<a id="compare-66c1ff05a636a53bf7e1db85522b53c4"></a>

### [`00b613bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b613bc.md) → [`00b623b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b623b0.md) FUN_00b623b0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b5ed6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5e/00b5ed6c.md) · 呼出先 4件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ab70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab70.md) [`00c5ace0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ace0.md)
- 新版 呼出元 1件 [`00b5fd60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5f/00b5fd60.md) · 呼出先 4件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bb40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb40.md) [`00c5bcb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bcb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b613d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b613bc.md#insn-00b613d0) · [`00b613e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b613bc.md#insn-00b613e8) · [`00b613fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b613bc.md#insn-00b613fc)
- 新版 [`00b623c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b623b0.md#insn-00b623c4) · [`00b623dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b623b0.md#insn-00b623dc) · [`00b623f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b623b0.md#insn-00b623f0)

~~~diff
- 00b613d0 ["INT_ADD", "register:40f0:8", ["const:b613d0:8", "const:4:8"]]
- 00b613d0 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b623c4 ["INT_ADD", "register:40f0:8", ["const:b623c4:8", "const:4:8"]]
+ 00b623c4 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b613d0 bytes c0e50394
+ 00b623c4 bytes b7e50394
- 00b613e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b613e8 ["INT_ADD", "register:40f0:8", ["const:b613e8:8", "const:4:8"]]
- 00b613e8 ["CALLIND", null, ["register:0:8"]]
+ 00b623dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b623dc ["INT_ADD", "register:40f0:8", ["const:b623dc:8", "const:4:8"]]
+ 00b623dc ["CALLIND", null, ["register:0:8"]]
- 00b613e8 bytes 00013fd6
+ 00b623dc bytes 00013fd6
- 00b613fc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b613fc ["INT_ADD", "register:40f0:8", ["const:b613fc:8", "const:4:8"]]
- 00b613fc ["CALLIND", null, ["register:0:8"]]
+ 00b623f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b623f0 ["INT_ADD", "register:40f0:8", ["const:b623f0:8", "const:4:8"]]
+ 00b623f0 ["CALLIND", null, ["register:0:8"]]
- 00b613fc bytes 00013fd6
+ 00b623f0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf6cc397fd83c8974531564998376f56"></a>

### [`00b619e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b619e8.md) → [`00b629dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b629dc.md) _ZN8firebase17ModuleInitializer20InitializeLastResultEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bd10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bd10.md) [`00c5bdf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bdf0.md) [`00c5beb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5beb0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b61a08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b619e8.md#insn-00b61a08) · [`00b61a14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b619e8.md#insn-00b61a14) · [`00b61a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b619e8.md#insn-00b61a20)
- 新版 [`00b629fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b629dc.md#insn-00b629fc) · [`00b62a08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b629dc.md#insn-00b62a08) · [`00b62a14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b629dc.md#insn-00b62a14)

~~~diff
- 00b61a08 ["INT_ADD", "register:40f0:8", ["const:b61a08:8", "const:4:8"]]
- 00b61a08 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00b629fc ["INT_ADD", "register:40f0:8", ["const:b629fc:8", "const:4:8"]]
+ 00b629fc ["CALL", null, ["callee:00c5baa0:8"]]
- 00b61a08 bytes 32e40394
+ 00b629fc bytes 29e40394
- 00b61a14 ["INT_ADD", "register:40f0:8", ["const:b61a14:8", "const:4:8"]]
- 00b61a14 ["CALL", null, ["callee:00c5bab0:8"]]
+ 00b62a08 ["INT_ADD", "register:40f0:8", ["const:b62a08:8", "const:4:8"]]
+ 00b62a08 ["CALL", null, ["callee:00c5bab0:8"]]
- 00b61a14 bytes 33e40394
+ 00b62a08 bytes 2ae40394
- 00b61a20 ["INT_ADD", "register:40f0:8", ["const:b61a20:8", "const:4:8"]]
- 00b61a20 ["CALL", null, ["callee:00c5bd10:8"]]
+ 00b62a14 ["INT_ADD", "register:40f0:8", ["const:b62a14:8", "const:4:8"]]
+ 00b62a14 ["CALL", null, ["callee:00c5bd10:8"]]
- 00b61a20 bytes c8e40394
+ 00b62a14 bytes bfe40394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7dd6b6eb7f74b382d2ce33215632732"></a>

### [`00b62608`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b62608.md) → [`00b635fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b635fc.md) _ZN8firebase16StaticFutureData13CreateNewDataEPKvi

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5ad10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c5bce0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bce0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6261c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b62608.md#insn-00b6261c) · [`00b62628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b62608.md#insn-00b62628)
- 新版 [`00b63610`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b635fc.md#insn-00b63610) · [`00b6361c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b635fc.md#insn-00b6361c)

~~~diff
- 00b6261c ["INT_ADD", "register:40f0:8", ["const:b6261c:8", "const:4:8"]]
- 00b6261c ["CALL", null, ["callee:00c58f30:8"]]
+ 00b63610 ["INT_ADD", "register:40f0:8", ["const:b63610:8", "const:4:8"]]
+ 00b63610 ["CALL", null, ["callee:00c58f30:8"]]
- 00b6261c bytes 51d60394
+ 00b63610 bytes 48d60394
- 00b62628 ["INT_ADD", "register:40f0:8", ["const:b62628:8", "const:4:8"]]
- 00b62628 ["CALL", null, ["callee:00c5bce0:8"]]
+ 00b6361c ["INT_ADD", "register:40f0:8", ["const:b6361c:8", "const:4:8"]]
+ 00b6361c ["CALL", null, ["callee:00c5bce0:8"]]
- 00b62628 bytes bae10394
+ 00b6361c bytes b1e10394
~~~


<a id="compare-ba77047133a333a7c85b8f07d17fe8ea"></a>

### [`00b6263c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b6263c.md) → [`00b63630`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b63630.md) _ZN8firebase11SplitStringERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c580a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580a0.md) [`00c5b720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b720.md) [`00c5b8c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b8c0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59070.md) [`00c5c6f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c6f0.md) [`00c5c890`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c890.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b62700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b6263c.md#insn-00b62700) · [`00b62728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b6263c.md#insn-00b62728) · [`00b62764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b6263c.md#insn-00b62764)
- 新版 [`00b636f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b63630.md#insn-00b636f4) · [`00b6371c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b63630.md#insn-00b6371c) · [`00b63758`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b63630.md#insn-00b63758)

~~~diff
- 00b62700 ["INT_ADD", "register:40f0:8", ["const:b62700:8", "const:4:8"]]
- 00b62700 ["CALL", null, ["callee:00c59070:8"]]
+ 00b636f4 ["INT_ADD", "register:40f0:8", ["const:b636f4:8", "const:4:8"]]
+ 00b636f4 ["CALL", null, ["callee:00c59070:8"]]
- 00b62700 bytes 68d60394
+ 00b636f4 bytes 5fd60394
- 00b62728 ["INT_ADD", "register:40f0:8", ["const:b62728:8", "const:4:8"]]
- 00b62728 ["CALL", null, ["callee:00c5c890:8"]]
+ 00b6371c ["INT_ADD", "register:40f0:8", ["const:b6371c:8", "const:4:8"]]
+ 00b6371c ["CALL", null, ["callee:00c5c890:8"]]
- 00b62728 bytes 66e40394
+ 00b6371c bytes 5de40394
- 00b62764 ["INT_ADD", "register:40f0:8", ["const:b62764:8", "const:4:8"]]
- 00b62764 ["CALL", null, ["callee:00c5c6f0:8"]]
+ 00b63758 ["INT_ADD", "register:40f0:8", ["const:b63758:8", "const:4:8"]]
+ 00b63758 ["CALL", null, ["callee:00c5c6f0:8"]]
- 00b62764 bytes efe30394
+ 00b63758 bytes e6e30394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d877f153789a52d21c36f5b5cab07f55"></a>

### [`00b62af8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b62af8.md) → [`00b63aec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b63aec.md) _ZNSt6__ndk16vectorIPFN8firebase10InitResultEPNS1_3AppEPvENS_9allocatorIS7_EEE21__push_back_slow_pathIRKS7_EEvOT_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5be80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5be80.md) · 呼出先 4件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c5ce50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5ce50.md) · 呼出先 4件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b62b5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b62af8.md#insn-00b62b5c) · [`00b62b68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b62af8.md#insn-00b62b68) · [`00b62b94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b62af8.md#insn-00b62b94)
- 新版 [`00b63b50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b63aec.md#insn-00b63b50) · [`00b63b5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b63aec.md#insn-00b63b5c) · [`00b63b88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b63aec.md#insn-00b63b88)

~~~diff
- 00b62b5c ["INT_ADD", "register:40f0:8", ["const:b62b5c:8", "const:4:8"]]
- 00b62b5c ["CALL", null, ["callee:00c5c1e0:8"]]
+ 00b63b50 ["INT_ADD", "register:40f0:8", ["const:b63b50:8", "const:4:8"]]
+ 00b63b50 ["CALL", null, ["callee:00c5c1e0:8"]]
- 00b62b5c bytes ade10394
+ 00b63b50 bytes a4e10394
- 00b62b68 ["INT_ADD", "register:40f0:8", ["const:b62b68:8", "const:4:8"]]
- 00b62b68 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b63b5c ["INT_ADD", "register:40f0:8", ["const:b63b5c:8", "const:4:8"]]
+ 00b63b5c ["CALL", null, ["callee:00c58f30:8"]]
- 00b62b68 bytes fed40394
+ 00b63b5c bytes f5d40394
- 00b62b94 ["INT_ADD", "register:40f0:8", ["const:b62b94:8", "const:4:8"]]
- 00b62b94 ["CALL", null, ["callee:00c590a0:8"]]
+ 00b63b88 ["INT_ADD", "register:40f0:8", ["const:b63b88:8", "const:4:8"]]
+ 00b63b88 ["CALL", null, ["callee:00c590a0:8"]]
- 00b62b94 bytes 4fd50394
+ 00b63b88 bytes 46d50394
~~~


<a id="compare-a5a7b23cf29e1bfe9a8688cb7698c9d4"></a>

### [`00b62be0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b62be0.md) → [`00b63bd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b63bd4.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8firebase10InitResultEEENS_19__map_value_co

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5be50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5be50.md) · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5be50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5be50.md)
- 新版 呼出元 1件 [`00c5ce20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5ce20.md) · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5ce20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5ce20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b62bfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b62be0.md#insn-00b62bfc) · [`00b62c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b62be0.md#insn-00b62c08) · [`00b62c18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b62be0.md#insn-00b62c18)
- 新版 [`00b63bf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b63bd4.md#insn-00b63bf0) · [`00b63bfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b63bd4.md#insn-00b63bfc) · [`00b63c0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b63bd4.md#insn-00b63c0c)

~~~diff
- 00b62bfc ["INT_ADD", "register:40f0:8", ["const:b62bfc:8", "const:4:8"]]
- 00b62bfc ["CALL", null, ["callee:00c5ce20:8"]]
+ 00b63bf0 ["INT_ADD", "register:40f0:8", ["const:b63bf0:8", "const:4:8"]]
+ 00b63bf0 ["CALL", null, ["callee:00c5ce20:8"]]
- 00b62bfc bytes 95e40394
+ 00b63bf0 bytes 8ce40394
- 00b62c08 ["INT_ADD", "register:40f0:8", ["const:b62c08:8", "const:4:8"]]
- 00b62c08 ["CALL", null, ["callee:00c5ce20:8"]]
+ 00b63bfc ["INT_ADD", "register:40f0:8", ["const:b63bfc:8", "const:4:8"]]
+ 00b63bfc ["CALL", null, ["callee:00c5ce20:8"]]
- 00b62c08 bytes 92e40394
+ 00b63bfc bytes 89e40394
- 00b62c18 ["INT_ADD", "register:40f0:8", ["const:b62c18:8", "const:4:8"]]
- 00b62c18 ["CALL", null, ["callee:00c58f50:8"]]
+ 00b63c0c ["INT_ADD", "register:40f0:8", ["const:b63c0c:8", "const:4:8"]]
+ 00b63c0c ["CALL", null, ["callee:00c58f50:8"]]
- 00b62c18 bytes dad40394
+ 00b63c0c bytes d1d40394
~~~


<a id="compare-848862de713435fe44f51fbb2aba5e7f"></a>

### [`00b62c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b62c30.md) → [`00b63c24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b63c24.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8firebase10InitResultEEENS_19__map_value_co

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5be40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5be40.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00c5ce10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5ce10.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b62ccc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b62c30.md#insn-00b62ccc) · [`00b62d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b62c30.md#insn-00b62d0c)
- 新版 [`00b63cc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b63c24.md#insn-00b63cc0) · [`00b63d00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b63c24.md#insn-00b63d00)

~~~diff
- 00b62ccc ["INT_ADD", "register:40f0:8", ["const:b62ccc:8", "const:4:8"]]
- 00b62ccc ["CALL", null, ["callee:00c590f0:8"]]
+ 00b63cc0 ["INT_ADD", "register:40f0:8", ["const:b63cc0:8", "const:4:8"]]
+ 00b63cc0 ["CALL", null, ["callee:00c590f0:8"]]
- 00b62ccc bytes 15d50394
+ 00b63cc0 bytes 0cd50394
- 00b62d0c ["INT_ADD", "register:40f0:8", ["const:b62d0c:8", "const:4:8"]]
- 00b62d0c ["CALL", null, ["callee:00c590f0:8"]]
+ 00b63d00 ["INT_ADD", "register:40f0:8", ["const:b63d00:8", "const:4:8"]]
+ 00b63d00 ["CALL", null, ["callee:00c590f0:8"]]
- 00b62d0c bytes 05d50394
+ 00b63d00 bytes fcd40394
~~~


<a id="compare-091094c554e35d0353984b4e7dab6968"></a>

### [`00b62d50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b62d50.md) → [`00b63d44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b63d44.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN8firebase11AppCallbackEEENS_19__map_value_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5be70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5be70.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00c5ce40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5ce40.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b62de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b62d50.md#insn-00b62de8) · [`00b62e30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b62d50.md#insn-00b62e30)
- 新版 [`00b63ddc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b63d44.md#insn-00b63ddc) · [`00b63e24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b63d44.md#insn-00b63e24)

~~~diff
- 00b62de8 ["INT_ADD", "register:40f0:8", ["const:b62de8:8", "const:4:8"]]
- 00b62de8 ["CALL", null, ["callee:00c590f0:8"]]
+ 00b63ddc ["INT_ADD", "register:40f0:8", ["const:b63ddc:8", "const:4:8"]]
+ 00b63ddc ["CALL", null, ["callee:00c590f0:8"]]
- 00b62de8 bytes ced40394
+ 00b63ddc bytes c5d40394
- 00b62e30 ["INT_ADD", "register:40f0:8", ["const:b62e30:8", "const:4:8"]]
- 00b62e30 ["CALL", null, ["callee:00c590f0:8"]]
+ 00b63e24 ["INT_ADD", "register:40f0:8", ["const:b63e24:8", "const:4:8"]]
+ 00b63e24 ["CALL", null, ["callee:00c590f0:8"]]
- 00b62e30 bytes bcd40394
+ 00b63e24 bytes b3d40394
~~~


<a id="compare-72fb48577860b89e6a54bbb38556b4cc"></a>

### [`00b62e64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b62e64.md) → [`00b63e58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b63e58.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN8firebase11AppCallbackEEENS_19__map_value_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5be60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5be60.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00c5ce30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5ce30.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b62f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b62e64.md#insn-00b62f00) · [`00b62f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b62/00b62e64.md#insn-00b62f40)
- 新版 [`00b63ef4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b63e58.md#insn-00b63ef4) · [`00b63f34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b63/00b63e58.md#insn-00b63f34)

~~~diff
- 00b62f00 ["INT_ADD", "register:40f0:8", ["const:b62f00:8", "const:4:8"]]
- 00b62f00 ["CALL", null, ["callee:00c590f0:8"]]
+ 00b63ef4 ["INT_ADD", "register:40f0:8", ["const:b63ef4:8", "const:4:8"]]
+ 00b63ef4 ["CALL", null, ["callee:00c590f0:8"]]
- 00b62f00 bytes 88d40394
+ 00b63ef4 bytes 7fd40394
- 00b62f40 ["INT_ADD", "register:40f0:8", ["const:b62f40:8", "const:4:8"]]
- 00b62f40 ["CALL", null, ["callee:00c590f0:8"]]
+ 00b63f34 ["INT_ADD", "register:40f0:8", ["const:b63f34:8", "const:4:8"]]
+ 00b63f34 ["CALL", null, ["callee:00c590f0:8"]]
- 00b62f40 bytes 78d40394
+ 00b63f34 bytes 6fd40394
~~~


<a id="compare-53ed181d82437f4dcda449f586efaa66"></a>

### [`00b64990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b64990.md) → [`00b65984`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b65/00b65984.md) FUN_00b65984

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00b647ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b647ec.md) · 呼出先 2件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5b220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b220.md)
- 新版 呼出元 1件 [`00b657e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b65/00b657e0.md) · 呼出先 2件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5c1f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b64a00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b64990.md#insn-00b64a00) · [`00b64a24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b64990.md#insn-00b64a24)
- 新版 [`00b659f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b65/00b65984.md#insn-00b659f4) · [`00b65a18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b65/00b65984.md#insn-00b65a18)

~~~diff
- 00b64a00 ["INT_ADD", "register:40f0:8", ["const:b64a00:8", "const:4:8"]]
- 00b64a00 ["CALL", null, ["callee:00c5c1f0:8"]]
+ 00b659f4 ["INT_ADD", "register:40f0:8", ["const:b659f4:8", "const:4:8"]]
+ 00b659f4 ["CALL", null, ["callee:00c5c1f0:8"]]
- 00b64a00 bytes 08da0394
+ 00b659f4 bytes ffd90394
- 00b64a24 ["INT_ADD", "register:40f0:8", ["const:b64a24:8", "const:4:8"]]
- 00b64a24 ["CALL", null, ["callee:00c58f80:8"]]
+ 00b65a18 ["INT_ADD", "register:40f0:8", ["const:b65a18:8", "const:4:8"]]
+ 00b65a18 ["CALL", null, ["callee:00c58f80:8"]]
- 00b64a24 bytes 63cd0394
+ 00b65a18 bytes 5acd0394
~~~


<a id="compare-cf78eb4dd6dafd676cd86e726b748813"></a>

### [`00b64edc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b64edc.md) → [`00b65ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b65/00b65ed0.md) _ZNSt6__ndk16vectorIN8firebase7VariantENS_9allocatorIS2_EEE6assignIPS2_EENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constru

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5bf00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bf00.md) · 呼出先 5件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md) [`00c5a9c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a9c0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c5ced0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5ced0.md) · 呼出先 5件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5b8d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8d0.md) [`00c5b990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b990.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b64f4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b64edc.md#insn-00b64f4c) · [`00b64f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b64edc.md#insn-00b64f8c) · [`00b64fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b64/00b64edc.md#insn-00b64fc0)
- 新版 [`00b65f40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b65/00b65ed0.md#insn-00b65f40) · [`00b65f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b65/00b65ed0.md#insn-00b65f80) · [`00b65fb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b65/00b65ed0.md#insn-00b65fb4)

~~~diff
- 00b64f4c ["INT_ADD", "register:40f0:8", ["const:b64f4c:8", "const:4:8"]]
- 00b64f4c ["CALL", null, ["callee:00c5b8d0:8"]]
+ 00b65f40 ["INT_ADD", "register:40f0:8", ["const:b65f40:8", "const:4:8"]]
+ 00b65f40 ["CALL", null, ["callee:00c5b8d0:8"]]
- 00b64f4c bytes 6dd60394
+ 00b65f40 bytes 64d60394
- 00b64f8c ["INT_ADD", "register:40f0:8", ["const:b64f8c:8", "const:4:8"]]
- 00b64f8c ["CALL", null, ["callee:00c5b990:8"]]
+ 00b65f80 ["INT_ADD", "register:40f0:8", ["const:b65f80:8", "const:4:8"]]
+ 00b65f80 ["CALL", null, ["callee:00c5b990:8"]]
- 00b64f8c bytes 8dd60394
+ 00b65f80 bytes 84d60394
- 00b64fc0 ["INT_ADD", "register:40f0:8", ["const:b64fc0:8", "const:4:8"]]
- 00b64fc0 ["CALL", null, ["callee:00c5b990:8"]]
+ 00b65fb4 ["INT_ADD", "register:40f0:8", ["const:b65fb4:8", "const:4:8"]]
+ 00b65fb4 ["CALL", null, ["callee:00c5b990:8"]]
- 00b64fc0 bytes 80d60394
+ 00b65fb4 bytes 77d60394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0bf3bd9f861d42a01fd5ddb9287bfb0c"></a>

### [`00b650c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b650c4.md) → [`00b660b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b660b8.md) _ZNSt6__ndk16__treeINS_12__value_typeIN8firebase7VariantES3_EENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE14__ass

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5bed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bed0.md) · 呼出先 5件 [`00c5a9c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a9c0.md) [`00c5b670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b670.md) [`00c5b6b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b6b0.md) [`00c5bee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bee0.md) [`00c5bef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bef0.md)
- 新版 呼出元 1件 [`00c5cea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cea0.md) · 呼出先 5件 [`00c5b990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b990.md) [`00c5c640`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c640.md) [`00c5c680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c680.md) [`00c5ceb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5ceb0.md) [`00c5cec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cec0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b651a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b650c4.md#insn-00b651a0) · [`00b651ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b650c4.md#insn-00b651ac) · [`00b651d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b650c4.md#insn-00b651d8)
- 新版 [`00b66194`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b660b8.md#insn-00b66194) · [`00b661a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b660b8.md#insn-00b661a0) · [`00b661cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b660b8.md#insn-00b661cc)

~~~diff
- 00b651a0 ["INT_ADD", "register:40f0:8", ["const:b651a0:8", "const:4:8"]]
- 00b651a0 ["CALL", null, ["callee:00c5b990:8"]]
+ 00b66194 ["INT_ADD", "register:40f0:8", ["const:b66194:8", "const:4:8"]]
+ 00b66194 ["CALL", null, ["callee:00c5b990:8"]]
- 00b651a0 bytes 08d60394
+ 00b66194 bytes ffd50394
- 00b651ac ["INT_ADD", "register:40f0:8", ["const:b651ac:8", "const:4:8"]]
- 00b651ac ["CALL", null, ["callee:00c5b990:8"]]
+ 00b661a0 ["INT_ADD", "register:40f0:8", ["const:b661a0:8", "const:4:8"]]
+ 00b661a0 ["CALL", null, ["callee:00c5b990:8"]]
- 00b651ac bytes 05d60394
+ 00b661a0 bytes fcd50394
- 00b651d8 ["INT_ADD", "register:40f0:8", ["const:b651d8:8", "const:4:8"]]
- 00b651d8 ["CALL", null, ["callee:00c5c640:8"]]
+ 00b661cc ["INT_ADD", "register:40f0:8", ["const:b661cc:8", "const:4:8"]]
+ 00b661cc ["CALL", null, ["callee:00c5c640:8"]]
- 00b651d8 bytes 26d90394
+ 00b661cc bytes 1dd90394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67d7cbcaf2e42585e36e6daaeff4ad6f"></a>

### [`00b653b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b653b8.md) → [`00b663ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b663ac.md) _ZNSt6__ndk16__treeINS_12__value_typeIN8firebase7VariantES3_EENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE7destro

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5bef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bef0.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md) [`00c5bef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bef0.md)
- 新版 呼出元 1件 [`00c5cec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cec0.md) · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5b8d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8d0.md) [`00c5cec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cec0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b653d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b653b8.md#insn-00b653d4) · [`00b653e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b653b8.md#insn-00b653e0) · [`00b653f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b653b8.md#insn-00b653f0)
- 新版 [`00b663c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b663ac.md#insn-00b663c8) · [`00b663d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b663ac.md#insn-00b663d4) · [`00b663e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b663ac.md#insn-00b663e4)

~~~diff
- 00b653d4 ["INT_ADD", "register:40f0:8", ["const:b653d4:8", "const:4:8"]]
- 00b653d4 ["CALL", null, ["callee:00c5cec0:8"]]
+ 00b663c8 ["INT_ADD", "register:40f0:8", ["const:b663c8:8", "const:4:8"]]
+ 00b663c8 ["CALL", null, ["callee:00c5cec0:8"]]
- 00b653d4 bytes c7da0394
+ 00b663c8 bytes beda0394
- 00b653e0 ["INT_ADD", "register:40f0:8", ["const:b653e0:8", "const:4:8"]]
- 00b653e0 ["CALL", null, ["callee:00c5cec0:8"]]
+ 00b663d4 ["INT_ADD", "register:40f0:8", ["const:b663d4:8", "const:4:8"]]
+ 00b663d4 ["CALL", null, ["callee:00c5cec0:8"]]
- 00b653e0 bytes c4da0394
+ 00b663d4 bytes bbda0394
- 00b653f0 ["INT_ADD", "register:40f0:8", ["const:b653f0:8", "const:4:8"]]
- 00b653f0 ["CALL", null, ["callee:00c5b8d0:8"]]
+ 00b663e4 ["INT_ADD", "register:40f0:8", ["const:b663e4:8", "const:4:8"]]
+ 00b663e4 ["CALL", null, ["callee:00c5b8d0:8"]]
- 00b653f0 bytes 44d50394
+ 00b663e4 bytes 3bd50394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efdab0a58a7e189f619db64ac01aa45b"></a>

### [`00b65414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65414.md) → [`00b66408`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66408.md) _ZNSt6__ndk16__treeINS_12__value_typeIN8firebase7VariantES3_EENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE15__emp

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5bee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bee0.md) · 呼出先 4件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5a9c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a9c0.md) [`00c5b670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b670.md) [`00c5b6b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b6b0.md)
- 新版 呼出元 1件 [`00c5ceb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5ceb0.md) · 呼出先 4件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c5b990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b990.md) [`00c5c640`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c640.md) [`00c5c680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c680.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b65430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65414.md#insn-00b65430) · [`00b65448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65414.md#insn-00b65448) · [`00b65458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b65/00b65414.md#insn-00b65458)
- 新版 [`00b66424`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66408.md#insn-00b66424) · [`00b6643c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66408.md#insn-00b6643c) · [`00b6644c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b66/00b66408.md#insn-00b6644c)

~~~diff
- 00b65430 ["INT_ADD", "register:40f0:8", ["const:b65430:8", "const:4:8"]]
- 00b65430 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b66424 ["INT_ADD", "register:40f0:8", ["const:b66424:8", "const:4:8"]]
+ 00b66424 ["CALL", null, ["callee:00c58f30:8"]]
- 00b65430 bytes ccca0394
+ 00b66424 bytes c3ca0394
- 00b65448 ["INT_ADD", "register:40f0:8", ["const:b65448:8", "const:4:8"]]
- 00b65448 ["CALL", null, ["callee:00c5b990:8"]]
+ 00b6643c ["INT_ADD", "register:40f0:8", ["const:b6643c:8", "const:4:8"]]
+ 00b6643c ["CALL", null, ["callee:00c5b990:8"]]
- 00b65448 bytes 5ed50394
+ 00b6643c bytes 55d50394
- 00b65458 ["INT_ADD", "register:40f0:8", ["const:b65458:8", "const:4:8"]]
- 00b65458 ["CALL", null, ["callee:00c5b990:8"]]
+ 00b6644c ["INT_ADD", "register:40f0:8", ["const:b6644c:8", "const:4:8"]]
+ 00b6644c ["CALL", null, ["callee:00c5b990:8"]]
- 00b65458 bytes 5ad50394
+ 00b6644c bytes 51d50394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33addc1c4d5f012e1e1c294ad6687c7e"></a>

### [`00b66c94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66c94.md) → [`00b67c88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67c88.md) _ZN8firebase3AppD2Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5b890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b890.md) · 呼出先 7件 [`00879ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00879/00879ce0.md) [`00b66ae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66ae4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5b290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b290.md) [`00c5b490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b490.md)
- 新版 呼出元 1件 [`00c5c860`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c860.md) · 呼出先 7件 [`0087ac8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087a/0087ac8c.md) [`00b67ad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67ad8.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5c260`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c260.md) [`00c5c460`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c460.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b66ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66c94.md#insn-00b66ca8) · [`00b66cb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66c94.md#insn-00b66cb4) · [`00b66cc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66c94.md#insn-00b66cc8)
- 新版 [`00b67c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67c88.md#insn-00b67c9c) · [`00b67ca8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67c88.md#insn-00b67ca8) · [`00b67cbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67c88.md#insn-00b67cbc)

~~~diff
- 00b66ca8 ["INT_ADD", "register:40f0:8", ["const:b66ca8:8", "const:4:8"]]
- 00b66ca8 ["CALL", null, ["callee:00c5c800:8"]]
+ 00b67c9c ["INT_ADD", "register:40f0:8", ["const:b67c9c:8", "const:4:8"]]
+ 00b67c9c ["CALL", null, ["callee:00c5c800:8"]]
- 00b66ca8 bytes e2d20394
+ 00b67c9c bytes d9d20394
- 00b66cb4 ["INT_ADD", "register:40f0:8", ["const:b66cb4:8", "const:4:8"]]
- 00b66cb4 ["CALL", null, ["callee:00c5c460:8"]]
+ 00b67ca8 ["INT_ADD", "register:40f0:8", ["const:b67ca8:8", "const:4:8"]]
+ 00b67ca8 ["CALL", null, ["callee:00c5c460:8"]]
- 00b66cb4 bytes f7d10394
+ 00b67ca8 bytes eed10394
- 00b66cc8 ["INT_ADD", "register:40f0:8", ["const:b66cc8:8", "const:4:8"]]
- 00b66cc8 ["CALL", null, ["callee:00c5c260:8"]]
+ 00b67cbc ["INT_ADD", "register:40f0:8", ["const:b67cbc:8", "const:4:8"]]
+ 00b67cbc ["CALL", null, ["callee:00c5c260:8"]]
- 00b66cc8 bytes 72d10394
+ 00b67cbc bytes 69d10394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40d999a772888bc3d4ff5603a4afeeab"></a>

### [`00b682dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b68/00b682dc.md) → [`00b692d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b69/00b692d0.md) _ZN8firebase28CallAfterEnsureMethodsCachedEP7_JNIEnvP8_jobjectNSt6__ndk18functionIFvvEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b611c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b61/00b611c8.md) [`00b664f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b664f0.md) [`00b66ae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b66/00b66ae4.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00b621bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b62/00b621bc.md) [`00b674e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b674e4.md) [`00b67ad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b67/00b67ad8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b682f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b68/00b682dc.md#insn-00b682f0) · [`00b68308`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b68/00b682dc.md#insn-00b68308) · [`00b68328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b68/00b682dc.md#insn-00b68328)
- 新版 [`00b692e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b69/00b692d0.md#insn-00b692e4) · [`00b692fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b69/00b692d0.md#insn-00b692fc) · [`00b6931c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b69/00b692d0.md#insn-00b6931c)

~~~diff
- 00b682f0 ["INT_ADD", "register:40f0:8", ["const:b682f0:8", "const:4:8"]]
- 00b682f0 ["CALL", null, ["callee:00b674e4:8"]]
+ 00b692e4 ["INT_ADD", "register:40f0:8", ["const:b692e4:8", "const:4:8"]]
+ 00b692e4 ["CALL", null, ["callee:00b674e4:8"]]
- 00b682f0 bytes 80f8ff97
+ 00b692e4 bytes 80f8ff97
- 00b68308 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b68308 ["INT_ADD", "register:40f0:8", ["const:b68308:8", "const:4:8"]]
- 00b68308 ["CALLIND", null, ["register:0:8"]]
+ 00b692fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b692fc ["INT_ADD", "register:40f0:8", ["const:b692fc:8", "const:4:8"]]
+ 00b692fc ["CALLIND", null, ["register:0:8"]]
- 00b68308 bytes 00013fd6
+ 00b692fc bytes 00013fd6
- 00b68328 ["INT_ADD", "register:40f0:8", ["const:b68328:8", "const:4:8"]]
- 00b68328 ["CALL", null, ["callee:00b621bc:8"]]
+ 00b6931c ["INT_ADD", "register:40f0:8", ["const:b6931c:8", "const:4:8"]]
+ 00b6931c ["CALL", null, ["callee:00b621bc:8"]]
- 00b68328 bytes a8e3ff97
+ 00b6931c bytes a8e3ff97
~~~


<a id="compare-f573474131deae3b53ddc03a362f2e97"></a>

### [`00b6832c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b68/00b6832c.md) → [`00b69320`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b69/00b69320.md) _ZNK8firebase10AppOptionseqERKS0_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5bfb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bfb0.md) · 呼出先 1件 [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 1件 [`00c5cf80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cf80.md) · 呼出先 1件 [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b683d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b68/00b6832c.md#insn-00b683d4) · [`00b68478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b68/00b6832c.md#insn-00b68478) · [`00b6851c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b68/00b6832c.md#insn-00b6851c)
- 新版 [`00b693c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b69/00b69320.md#insn-00b693c8) · [`00b6946c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b69/00b69320.md#insn-00b6946c) · [`00b69510`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b69/00b69320.md#insn-00b69510)

~~~diff
- 00b683d4 ["INT_ADD", "register:40f0:8", ["const:b683d4:8", "const:4:8"]]
- 00b683d4 ["CALL", null, ["callee:00c590f0:8"]]
+ 00b693c8 ["INT_ADD", "register:40f0:8", ["const:b693c8:8", "const:4:8"]]
+ 00b693c8 ["CALL", null, ["callee:00c590f0:8"]]
- 00b683d4 bytes 53bf0394
+ 00b693c8 bytes 4abf0394
- 00b68478 ["INT_ADD", "register:40f0:8", ["const:b68478:8", "const:4:8"]]
- 00b68478 ["CALL", null, ["callee:00c590f0:8"]]
+ 00b6946c ["INT_ADD", "register:40f0:8", ["const:b6946c:8", "const:4:8"]]
+ 00b6946c ["CALL", null, ["callee:00c590f0:8"]]
- 00b68478 bytes 2abf0394
+ 00b6946c bytes 21bf0394
- 00b6851c ["INT_ADD", "register:40f0:8", ["const:b6851c:8", "const:4:8"]]
- 00b6851c ["CALL", null, ["callee:00c590f0:8"]]
+ 00b69510 ["INT_ADD", "register:40f0:8", ["const:b69510:8", "const:4:8"]]
+ 00b69510 ["CALL", null, ["callee:00c590f0:8"]]
- 00b6851c bytes 01bf0394
+ 00b69510 bytes f8be0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1df9fc9de6488f6bb3f9a4bab55a499"></a>

### [`00b6a8d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6a/00b6a8d8.md) → [`00b6b8cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6b/00b6b8cc.md) _ZN11flatbuffers6ParserD2Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b9e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b9e0.md) · 呼出先 13件 [`00540910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540910.md) [`0073a35c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0073a/0073a35c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5b970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b970.md) [`00c5b980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b980.md)
- 新版 呼出元 1件 [`00c5c9b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c9b0.md) · 呼出先 13件 [`00540c30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540c30.md) [`0073a70c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0073a/0073a70c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5c940`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c940.md) [`00c5c950`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c950.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6a908`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6a/00b6a8d8.md#insn-00b6a908) · [`00b6a910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6a/00b6a8d8.md#insn-00b6a910) · [`00b6a964`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6a/00b6a8d8.md#insn-00b6a964)
- 新版 [`00b6b8fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6b/00b6b8cc.md#insn-00b6b8fc) · [`00b6b904`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6b/00b6b8cc.md#insn-00b6b904) · [`00b6b958`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6b/00b6b8cc.md#insn-00b6b958)

~~~diff
- 00b6a908 ["INT_ADD", "register:40f0:8", ["const:b6a908:8", "const:4:8"]]
- 00b6a908 ["CALL", null, ["callee:00c58f50:8"]]
+ 00b6b8fc ["INT_ADD", "register:40f0:8", ["const:b6b8fc:8", "const:4:8"]]
+ 00b6b8fc ["CALL", null, ["callee:00c58f50:8"]]
- 00b6a908 bytes 9eb50394
+ 00b6b8fc bytes 95b50394
- 00b6a910 ["INT_ADD", "register:40f0:8", ["const:b6a910:8", "const:4:8"]]
- 00b6a910 ["CALL", null, ["callee:00c58f50:8"]]
+ 00b6b904 ["INT_ADD", "register:40f0:8", ["const:b6b904:8", "const:4:8"]]
+ 00b6b904 ["CALL", null, ["callee:00c58f50:8"]]
- 00b6a910 bytes 9cb50394
+ 00b6b904 bytes 93b50394
- 00b6a964 ["INT_ADD", "register:40f0:8", ["const:b6a964:8", "const:4:8"]]
- 00b6a964 ["CALL", null, ["callee:00c58f50:8"]]
+ 00b6b958 ["INT_ADD", "register:40f0:8", ["const:b6b958:8", "const:4:8"]]
+ 00b6b958 ["CALL", null, ["callee:00c58f50:8"]]
- 00b6a964 bytes 87b50394
+ 00b6b958 bytes 7eb50394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75ac808b84f1ff76db92f8800dc1580d"></a>

### [`00b6abd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6a/00b6abd0.md) → [`00b6bbc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6b/00b6bbc4.md) _ZN11flatbuffers10IDLOptionsD2Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b970.md) · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00c5c940`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c940.md) · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6ac1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6a/00b6abd0.md#insn-00b6ac1c) · [`00b6ac34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6a/00b6abd0.md#insn-00b6ac34) · [`00b6ace4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6a/00b6abd0.md#insn-00b6ace4)
- 新版 [`00b6bc10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6b/00b6bbc4.md#insn-00b6bc10) · [`00b6bc28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6b/00b6bbc4.md#insn-00b6bc28) · [`00b6bcd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6b/00b6bbc4.md#insn-00b6bcd8)

~~~diff
- 00b6ac1c ["INT_ADD", "register:40f0:8", ["const:b6ac1c:8", "const:4:8"]]
- 00b6ac1c ["CALL", null, ["callee:00c58f50:8"]]
+ 00b6bc10 ["INT_ADD", "register:40f0:8", ["const:b6bc10:8", "const:4:8"]]
+ 00b6bc10 ["CALL", null, ["callee:00c58f50:8"]]
- 00b6ac1c bytes d9b40394
+ 00b6bc10 bytes d0b40394
- 00b6ac34 ["INT_ADD", "register:40f0:8", ["const:b6ac34:8", "const:4:8"]]
- 00b6ac34 ["CALL", null, ["callee:00c58f50:8"]]
+ 00b6bc28 ["INT_ADD", "register:40f0:8", ["const:b6bc28:8", "const:4:8"]]
+ 00b6bc28 ["CALL", null, ["callee:00c58f50:8"]]
- 00b6ac34 bytes d3b40394
+ 00b6bc28 bytes cab40394
- 00b6ace4 ["INT_ADD", "register:40f0:8", ["const:b6ace4:8", "const:4:8"]]
- 00b6ace4 ["CALL", null, ["callee:00c58f50:8"]]
+ 00b6bcd8 ["INT_ADD", "register:40f0:8", ["const:b6bcd8:8", "const:4:8"]]
+ 00b6bcd8 ["CALL", null, ["callee:00c58f50:8"]]
- 00b6ace4 bytes a7b40394
+ 00b6bcd8 bytes 9eb40394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc8395b279d2befc85d8ad5251f1d3b4"></a>

### [`00b6b094`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6b/00b6b094.md) → [`00b6c088`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6c/00b6c088.md) _ZN11flatbuffers10IDLOptionsC2ERKS0_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5b950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b950.md) · 呼出先 3件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md) [`00c5b680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b680.md)
- 新版 呼出元 1件 [`00c5c920`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c920.md) · 呼出先 3件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md) [`00c5c650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c650.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6b/00b6b094.md#insn-00b6b0d0) · [`00b6b0dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6b/00b6b094.md#insn-00b6b0dc) · [`00b6b0f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6b/00b6b094.md#insn-00b6b0f8)
- 新版 [`00b6c0c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6c/00b6c088.md#insn-00b6c0c4) · [`00b6c0d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6c/00b6c088.md#insn-00b6c0d0) · [`00b6c0ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6c/00b6c088.md#insn-00b6c0ec)

~~~diff
- 00b6b0d0 ["INT_ADD", "register:40f0:8", ["const:b6b0d0:8", "const:4:8"]]
- 00b6b0d0 ["CALL", null, ["callee:00c5c650:8"]]
+ 00b6c0c4 ["INT_ADD", "register:40f0:8", ["const:b6c0c4:8", "const:4:8"]]
+ 00b6c0c4 ["CALL", null, ["callee:00c5c650:8"]]
- 00b6b0d0 bytes 6cc10394
+ 00b6c0c4 bytes 63c10394
- 00b6b0dc ["INT_ADD", "register:40f0:8", ["const:b6b0dc:8", "const:4:8"]]
- 00b6b0dc ["CALL", null, ["callee:00c5c650:8"]]
+ 00b6c0d0 ["INT_ADD", "register:40f0:8", ["const:b6c0d0:8", "const:4:8"]]
+ 00b6c0d0 ["CALL", null, ["callee:00c5c650:8"]]
- 00b6b0dc bytes 69c10394
+ 00b6c0d0 bytes 60c10394
- 00b6b0f8 ["INT_ADD", "register:40f0:8", ["const:b6b0f8:8", "const:4:8"]]
- 00b6b0f8 ["CALL", null, ["callee:00c5c650:8"]]
+ 00b6c0ec ["INT_ADD", "register:40f0:8", ["const:b6c0ec:8", "const:4:8"]]
+ 00b6c0ec ["CALL", null, ["callee:00c5c650:8"]]
- 00b6b0f8 bytes 62c10394
+ 00b6c0ec bytes 59c10394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf76c2d1f25e3da7646a4914ed67633d"></a>

### [`00b6b344`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6b/00b6b344.md) → [`00b6c338`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6c/00b6c338.md) _ZNSt6__ndk16vectorIPN11flatbuffers9NamespaceENS_9allocatorIS3_EEE21__push_back_slow_pathIRKS3_EEvOT_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5bbb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bbb0.md) · 呼出先 4件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)
- 新版 呼出元 1件 [`00c5cb80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5cb80.md) · 呼出先 4件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md) [`00c5c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c1e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6b3a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6b/00b6b344.md#insn-00b6b3a8) · [`00b6b3b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6b/00b6b344.md#insn-00b6b3b4) · [`00b6b3e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6b/00b6b344.md#insn-00b6b3e0)
- 新版 [`00b6c39c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6c/00b6c338.md#insn-00b6c39c) · [`00b6c3a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6c/00b6c338.md#insn-00b6c3a8) · [`00b6c3d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6c/00b6c338.md#insn-00b6c3d4)

~~~diff
- 00b6b3a8 ["INT_ADD", "register:40f0:8", ["const:b6b3a8:8", "const:4:8"]]
- 00b6b3a8 ["CALL", null, ["callee:00c5c1e0:8"]]
+ 00b6c39c ["INT_ADD", "register:40f0:8", ["const:b6c39c:8", "const:4:8"]]
+ 00b6c39c ["CALL", null, ["callee:00c5c1e0:8"]]
- 00b6b3a8 bytes 9abf0394
+ 00b6c39c bytes 91bf0394
- 00b6b3b4 ["INT_ADD", "register:40f0:8", ["const:b6b3b4:8", "const:4:8"]]
- 00b6b3b4 ["CALL", null, ["callee:00c58f30:8"]]
+ 00b6c3a8 ["INT_ADD", "register:40f0:8", ["const:b6c3a8:8", "const:4:8"]]
+ 00b6c3a8 ["CALL", null, ["callee:00c58f30:8"]]
- 00b6b3b4 bytes ebb20394
+ 00b6c3a8 bytes e2b20394
- 00b6b3e0 ["INT_ADD", "register:40f0:8", ["const:b6b3e0:8", "const:4:8"]]
- 00b6b3e0 ["CALL", null, ["callee:00c590a0:8"]]
+ 00b6c3d4 ["INT_ADD", "register:40f0:8", ["const:b6c3d4:8", "const:4:8"]]
+ 00b6c3d4 ["CALL", null, ["callee:00c590a0:8"]]
- 00b6b3e0 bytes 3cb30394
+ 00b6c3d4 bytes 33b30394
~~~


<a id="compare-ede90ca07e8853586af51b50cca3ba5c"></a>

### [`00b6b42c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6b/00b6b42c.md) → [`00b6c420`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6c/00b6c420.md) _ZNK8firebase3fbs14GoogleServices6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ba60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5ba60.md) · 呼出先 2件 [`00c5ba50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5ba50.md) [`00c5bab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bab0.md)
- 新版 呼出元 1件 [`00c5ca30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5ca30.md) · 呼出先 2件 [`00c5ca20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5ca20.md) [`00c5ca80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5ca80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6b570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6b/00b6b42c.md#insn-00b6b570) · [`00b6b698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6b/00b6b42c.md#insn-00b6b698)
- 新版 [`00b6c564`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6c/00b6c420.md#insn-00b6c564) · [`00b6c68c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6c/00b6c420.md#insn-00b6c68c)

~~~diff
- 00b6b570 ["INT_ADD", "register:40f0:8", ["const:b6b570:8", "const:4:8"]]
- 00b6b570 ["CALL", null, ["callee:00c5ca20:8"]]
+ 00b6c564 ["INT_ADD", "register:40f0:8", ["const:b6c564:8", "const:4:8"]]
+ 00b6c564 ["CALL", null, ["callee:00c5ca20:8"]]
- 00b6b570 bytes 38c10394
+ 00b6c564 bytes 2fc10394
- 00b6b698 ["INT_ADD", "register:40f0:8", ["const:b6b698:8", "const:4:8"]]
- 00b6b698 ["CALL", null, ["callee:00c5ca80:8"]]
+ 00b6c68c ["INT_ADD", "register:40f0:8", ["const:b6c68c:8", "const:4:8"]]
+ 00b6c68c ["CALL", null, ["callee:00c5ca80:8"]]
- 00b6b698 bytes 06c10394
+ 00b6c68c bytes fdc00394
~~~


<a id="compare-d6cecbae515379c09e9a578064364495"></a>

### [`00b6bc2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6b/00b6bc2c.md) → [`00b6cc20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6c/00b6cc20.md) _ZNK8firebase3fbs6Client6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5bab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bab0.md) · 呼出先 4件 [`00c5ba20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5ba20.md) [`00c5ba40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5ba40.md) [`00c5baa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5baa0.md) [`00c5bac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bac0.md)
- 新版 呼出元 1件 [`00c5ca80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5ca80.md) · 呼出先 4件 [`00c5c9f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c9f0.md) [`00c5ca10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5ca10.md) [`00c5ca70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5ca70.md) [`00c5ca90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5ca90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6bd70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6b/00b6bc2c.md#insn-00b6bd70) · [`00b6be98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6b/00b6bc2c.md#insn-00b6be98) · [`00b6bfd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6b/00b6bc2c.md#insn-00b6bfd4)
- 新版 [`00b6cd64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6c/00b6cc20.md#insn-00b6cd64) · [`00b6ce8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6c/00b6cc20.md#insn-00b6ce8c) · [`00b6cfc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6c/00b6cc20.md#insn-00b6cfc8)

~~~diff
- 00b6bd70 ["INT_ADD", "register:40f0:8", ["const:b6bd70:8", "const:4:8"]]
- 00b6bd70 ["CALL", null, ["callee:00c5c9f0:8"]]
+ 00b6cd64 ["INT_ADD", "register:40f0:8", ["const:b6cd64:8", "const:4:8"]]
+ 00b6cd64 ["CALL", null, ["callee:00c5c9f0:8"]]
- 00b6bd70 bytes 2cbf0394
+ 00b6cd64 bytes 23bf0394
- 00b6be98 ["INT_ADD", "register:40f0:8", ["const:b6be98:8", "const:4:8"]]
- 00b6be98 ["CALL", null, ["callee:00c5ca10:8"]]
+ 00b6ce8c ["INT_ADD", "register:40f0:8", ["const:b6ce8c:8", "const:4:8"]]
+ 00b6ce8c ["CALL", null, ["callee:00c5ca10:8"]]
- 00b6be98 bytes eabe0394
+ 00b6ce8c bytes e1be0394
- 00b6bfd4 ["INT_ADD", "register:40f0:8", ["const:b6bfd4:8", "const:4:8"]]
- 00b6bfd4 ["CALL", null, ["callee:00c5ca70:8"]]
+ 00b6cfc8 ["INT_ADD", "register:40f0:8", ["const:b6cfc8:8", "const:4:8"]]
+ 00b6cfc8 ["CALL", null, ["callee:00c5ca70:8"]]
- 00b6bfd4 bytes b3be0394
+ 00b6cfc8 bytes aabe0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19af07f8ecc65c2946625bfab7a7f4a3"></a>

### [`00b6c0b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6c/00b6c0b4.md) → [`00b6d0a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6d/00b6d0a8.md) _ZNK8firebase3fbs10ClientInfo6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ba20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5ba20.md) · 呼出先 1件 [`00c5ba90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5ba90.md)
- 新版 呼出元 1件 [`00c5c9f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c9f0.md) · 呼出先 1件 [`00c5ca60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5ca60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6c2c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6c/00b6c0b4.md#insn-00b6c2c4)
- 新版 [`00b6d2b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6d/00b6d0a8.md#insn-00b6d2b8)

~~~diff
- 00b6c2c4 ["INT_ADD", "register:40f0:8", ["const:b6c2c4:8", "const:4:8"]]
- 00b6c2c4 ["CALL", null, ["callee:00c5ca60:8"]]
+ 00b6d2b8 ["INT_ADD", "register:40f0:8", ["const:b6d2b8:8", "const:4:8"]]
+ 00b6d2b8 ["CALL", null, ["callee:00c5ca60:8"]]
- 00b6c2c4 bytes f3bd0394
+ 00b6d2b8 bytes eabd0394
~~~


<a id="compare-fc11d56926bce44976d9381dda9fbc26"></a>

### [`00b6c4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6c/00b6c4a0.md) → [`00b6d494`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6d/00b6d494.md) _ZNK8firebase3fbs11OAuthClient6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5ba40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5ba40.md) · 呼出先 1件 [`00c5ba30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5ba30.md)
- 新版 呼出元 1件 [`00c5ca10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5ca10.md) · 呼出先 1件 [`00c5ca00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5ca00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6c6f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6c/00b6c4a0.md#insn-00b6c6f0)
- 新版 [`00b6d6e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6d/00b6d494.md#insn-00b6d6e4)

~~~diff
- 00b6c6f0 ["INT_ADD", "register:40f0:8", ["const:b6c6f0:8", "const:4:8"]]
- 00b6c6f0 ["CALL", null, ["callee:00c5ca00:8"]]
+ 00b6d6e4 ["INT_ADD", "register:40f0:8", ["const:b6d6e4:8", "const:4:8"]]
+ 00b6d6e4 ["CALL", null, ["callee:00c5ca00:8"]]
- 00b6c6f0 bytes d0bc0394
+ 00b6d6e4 bytes c7bc0394
~~~


<a id="compare-b47ab3e8b499704e8c5b476b541d7df8"></a>

### [`00b6cb50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6c/00b6cb50.md) → [`00b6db44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6d/00b6db44.md) _ZNK8firebase3fbs8Services6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5bac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5bac0.md) · 呼出先 2件 [`00c5ba10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5ba10.md) [`00c5ba70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5ba70.md)
- 新版 呼出元 1件 [`00c5ca90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5ca90.md) · 呼出先 2件 [`00c5c9e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c9e0.md) [`00c5ca40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5ca40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b6cc8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6c/00b6cb50.md#insn-00b6cc8c) · [`00b6cea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6c/00b6cb50.md#insn-00b6cea4)
- 新版 [`00b6dc80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6d/00b6db44.md#insn-00b6dc80) · [`00b6de98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6d/00b6db44.md#insn-00b6de98)

~~~diff
- 00b6cc8c ["INT_ADD", "register:40f0:8", ["const:b6cc8c:8", "const:4:8"]]
- 00b6cc8c ["CALL", null, ["callee:00c5ca40:8"]]
+ 00b6dc80 ["INT_ADD", "register:40f0:8", ["const:b6dc80:8", "const:4:8"]]
+ 00b6dc80 ["CALL", null, ["callee:00c5ca40:8"]]
- 00b6cc8c bytes 79bb0394
+ 00b6dc80 bytes 70bb0394
- 00b6cea4 ["INT_ADD", "register:40f0:8", ["const:b6cea4:8", "const:4:8"]]
- 00b6cea4 ["CALL", null, ["callee:00c5c9e0:8"]]
+ 00b6de98 ["INT_ADD", "register:40f0:8", ["const:b6de98:8", "const:4:8"]]
+ 00b6de98 ["CALL", null, ["callee:00c5c9e0:8"]]
- 00b6cea4 bytes dbba0394
+ 00b6de98 bytes d2ba0394
~~~


